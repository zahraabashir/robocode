# Obstruction3D · claude-opus-5-5 · replicate 24: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `e08beb0` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `a6d08eb` | Calibrated Kinova FK (mount + tool offsets), exploration scripts | approach.py, explore0.py, explore1.py, explore10.py, explore11.py, explore12.py, explore13.py, explore14.py, explore2.py, explore3.py, explore4.py, explore5.py, explore6.py, explo… | [E0126](01_timeline.md#E0126) |
| [C003](#C003) · `16f5645` | First full state-machine approach | approach.py, explore14.py, test_approach.py | [E0142](01_timeline.md#E0142) |
| [C004](#C004) · `f930731` | Grasp at top+0.02, retry yaws | approach.py, debug_run.py, explore15.py, explore16.py, o16b.txt | [E0189](01_timeline.md#E0189) |
| [C005](#C005) · `88ec9d8` | Grasp height window based on object extent | approach.py, explore16.py, o16a.txt, o16b.txt, o16c.txt | [E0200](01_timeline.md#E0200) |
| [C006](#C006) · `8668a75` | Analytic-Jacobian IK with null-space posture regularization | dbg2.py, kin.py, par_test.sh, res1.txt, t_ik.py | [E0242](01_timeline.md#E0242) |
| [C007](#C007) · `85d185e` | Free spot: nearest clear spot in reachable band | approach.py | [E0252](01_timeline.md#E0252) |
| [C008](#C008) · `62bb1ae` | Rewrite: finger-aware yaw/free-spot, joint-path lookahead, adaptive transit height | approach.py, dbg3.py, debug_run.py, explore17.py, o17a.txt, o17b.txt, par_test.sh, res2.txt, t_count.py, test_approach.py | [E0363](01_timeline.md#E0363) |
| [C009](#C009) · `996e375` | Fix path tracking truncation; open gripper while approaching grasp | approach.py, dbg_old.py, dbg_rw.py, old_approach.py | [E0438](01_timeline.md#E0438) |
| [C010](#C010) · `ecc0bf3` | Path lookahead cannot skip Cartesian corners | approach.py, dbg_pp.py, res_new.txt | [E0482](01_timeline.md#E0482) |
| [C011](#C011) · `a830579` | Interpolate yaw along path; allow gripper flip for grasp | approach.py, dbg_pos.py | [E0511](01_timeline.md#E0511) |
| [C012](#C012) · `d1a1402` | Adaptive lookahead shrink on blocked steps | approach.py, dbg_pp.py, probe86.py | [E0548](01_timeline.md#E0548) |
| [C013](#C013) · `d20aad0` | Task selection by graspability, blocker clearing, grasp height candidates | approach.py, dbg_pos.py, prof.out, res_c4.txt, res_new2.txt | [E0642](01_timeline.md#E0642) |
| [C014](#C014) · `79e4d38` | Better task switching; abort grasp approach blocked high | approach.py, probe_diag.py | [E0673](01_timeline.md#E0673) |
| [C015](#C015) · `ce0527f` | Blocker only when overlapping; cap blocker moves | approach.py | [E0685](01_timeline.md#E0685) |
| [C016](#C016) · `328f15a` | Merge grip with final motion, drop retreat step, cut path corners when safe | approach.py, dbg_rw.py, res_d3.txt | [E0719](01_timeline.md#E0719), [E0721](01_timeline.md#E0721) |
| [C017](#C017) · `87f3bd0` | Prefer grasp yaw near current tool yaw; finer rotation path resolution | approach.py, dbg_jd.py, par_test.sh, probe_base_1.py, probe_base_2.py, res_c4b.txt, res_d3.txt, res_d4.txt, snap/approach.py, snap/env_client.py, snap/env_spaces.json, snap/kin.py… | [E0845](01_timeline.md#E0845) |
| [C018](#C018) · `c3ece12` | Whole-body IK using base y/rot for faster motions | approach.py, kin.py, res_d5.txt, snap/approach.py | [E0905](01_timeline.md#E0905) |
| [C019](#C019) · `4d813a2` | wb_ik2: base x (bounded) + extended nominal posture | approach.py, kin.py, probe52.py, res_c4c.txt, res_c4d.txt, res_d5.txt, res_d6.txt, snap/approach.py, snap/kin.py, snapw/approach.py, snapw/env_client.py, snapw/env_spaces.json, sn… | [E1012](01_timeline.md#E1012) |
| [C020](#C020) · `cc5e97f` | Tune whole-body IK: gentler null pull, bx_max -0.09 | approach.py, res_c4e.txt, res_d7.txt, res_var.txt, snap/approach.py, snap/kin.py, snapw/approach.py, snapw/kin.py, test_approach.py, v_0.05_-0.09/approach.py, v_0.05_-0.09/env_cli… | [E1135](01_timeline.md#E1135) |
| [C021](#C021) · `37ffc6e` | Micro-lift fallback when held object is wedged and lift blocked | approach.py, dbg_jd.py, probe_c6.py, probe_up.py, probe_up2.py, res_c1.txt, res_c4f.txt, res_c6.txt, res_d8.txt, snap/approach.py, snap/test_approach.py | [E1250](01_timeline.md#E1250) |
| [C022](#C022) · `2997cec` | regression results | r_c4.txt, r_c6.txt, r_def.txt, snap/approach.py | [E1305](01_timeline.md#E1305) |
| [C023](#C023) · `7d554d6` | Regression results for counts 3/5/8 | r_c3.txt, r_c5.txt, r_c8.txt | [E1336](01_timeline.md#E1336) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `e08beb03d00c3730a7c48158942f4a54a0ea21e4`; parents: none (initial snapshot). Recorded author date: 2026-09-30T19:47:43+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_e08beb0.diff)

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
index 0000000..dff8dfd
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "6eefef35bfaa192f7898ebf189cf2b7d", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Calibrated Kinova FK (mount + tool offsets), exploration scripts

Commit `a6d08ebb9d48a69a42d4ba56e5f0b04153d90d8f`; parents: e08beb03d00c3730a7c48158942f4a54a0ea21e4. Recorded author date: 2026-09-30T19:57:37+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0126](01_timeline.md#E0126): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_a6d08eb_approach.py) · [Exact all-file diff](evidence/diffs/C002_a6d08eb.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..2d0f6a3
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,15 @@
           1 +import numpy as np
           2 +from kin import fk, ik, down_R
           3 +class GeneratedApproach:
           4 +    def __init__(self, action_space, observation_space, primitives): pass
           5 +    def reset(self, state, info):
           6 +        R = state.get_object_from_name('robot'); B = state.get_object_from_name('target_block')
           7 +        self.R=R
           8 +        base=(state.get(R,'pos_base_x'), state.get(R,'pos_base_y'), state.get(R,'pos_base_rot'))
           9 +        q=np.array([state.get(R,f'joint_{i}') for i in range(1,8)])
          10 +        p=np.array([state.get(B,'pose_x'),state.get(B,'pose_y'),0.24])
          11 +        self.qt,_=ik(q,p,down_R(0),base)
          12 +    def get_action(self, state):
          13 +        q=np.array([state.get(self.R,f'joint_{i}') for i in range(1,8)])
          14 +        d=(self.qt-q+np.pi)%(2*np.pi)-np.pi
          15 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); return a
diff --git a/explore0.py b/explore0.py
new file mode 100644
index 0000000..7464081
--- /dev/null
+++ b/explore0.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +for seed in [0,1]:
           5 +    obs, info = env.reset(seed=seed)
           6 +    print("info", info)
           7 +    for n in sorted(obs.get_object_names(), key=str):
           8 +        o = obs.get_object_from_name(n) if isinstance(n,str) else n
           9 +        name = n if isinstance(n,str) else n.name
          10 +        t = o.type if hasattr(o,'type') else None
          11 +        print(name, t, {f: round(float(obs.get(o,f)),4) for f in env.observation_space.get_type(t.name if hasattr(t,'name') else t).features} if False else "")
          12 +    print(type(obs), dir(obs)[:60])
          13 +env.close()
diff --git a/explore1.py b/explore1.py
new file mode 100644
index 0000000..35ac471
--- /dev/null
+++ b/explore1.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +def dump(obs):
           5 +    for n in sorted(obs.get_object_names(), key=str):
           6 +        o = obs.get_object_from_name(n)
           7 +        feats = obs.type_features[o.type] if o.type in obs.type_features else obs.type_features[o.type.name]
           8 +        print(n, {f: round(float(obs.get(o,f)),4) for f in feats})
           9 +for seed in [0,1,2]:
          10 +    obs, info = env.reset(seed=seed)
          11 +    dump(obs); print()
          12 +env.close()
diff --git a/explore10.py b/explore10.py
new file mode 100644
index 0000000..55d652d
--- /dev/null
+++ b/explore10.py
@@ -0,0 +1,36 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import fk, ik, down_R
           4 +env = make_env()
           5 +seed=1
           6 +jn=[f'joint_{i}' for i in range(1,8)]
           7 +def q_of(o): return np.array([o.get(R,f) for f in jn])
           8 +def goto(qt):
           9 +    global obs
          10 +    for _ in range(60):
          11 +        q=q_of(obs); d=qt-q
          12 +        d=(d+np.pi)%(2*np.pi)-np.pi
          13 +        if np.max(np.abs(d))<1e-5: return True
          14 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          15 +        obs,r,te,tr,info=env.step(a)
          16 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          17 +    return False
          18 +bx,by=0.1377,0.1831
          19 +yaw=float(sys.argv[1])
          20 +for dirn in [(1,0),(-1,0),(0,1),(0,-1)]:
          21 +  for z in [0.24,0.28,0.32,0.36]:
          22 +    obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot')
          23 +    base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          24 +    start=np.array([bx-0.15*dirn[0],by-0.15*dirn[1],z])
          25 +    qt,ok=ik(q_of(obs),start+[0,0,0.1],down_R(yaw),base); goto(qt)
          26 +    qt,ok=ik(q_of(obs),start,down_R(yaw),base); r=goto(qt)
          27 +    if not r: print('start blocked'); continue
          28 +    s=0
          29 +    while s<0.3:
          30 +        p=start+np.array([dirn[0],dirn[1],0])*(s+0.002)
          31 +        qt,ok=ik(q_of(obs),p,down_R(yaw),base)
          32 +        if not goto(qt): break
          33 +        s+=0.002
          34 +    pos=start+np.array([dirn[0],dirn[1],0])*s
          35 +    print('dir',dirn,'z',z,'stopped at',np.round(pos,3),'offset from block ctr',np.round(pos[:2]-[bx,by],3) if s<0.3 else 'passed')
          36 +env.close()
diff --git a/explore11.py b/explore11.py
new file mode 100644
index 0000000..f49bfb9
--- /dev/null
+++ b/explore11.py
@@ -0,0 +1,30 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import fk, ik, down_R
           4 +env = make_env()
           5 +seed=1
           6 +jn=[f'joint_{i}' for i in range(1,8)]
           7 +def q_of(o): return np.array([o.get(R,f) for f in jn])
           8 +def goto(qt):
           9 +    global obs
          10 +    for _ in range(60):
          11 +        q=q_of(obs); d=qt-q
          12 +        d=(d+np.pi)%(2*np.pi)-np.pi
          13 +        if np.max(np.abs(d))<1e-5: return True
          14 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          15 +        obs,r,te,tr,info=env.step(a)
          16 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          17 +    return False
          18 +yaw=float(sys.argv[1]); y=float(sys.argv[2])
          19 +for x in np.arange(0.36,0.62,0.02):
          20 +    obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot')
          21 +    base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          22 +    qt,ok=ik(q_of(obs),np.array([x,y,0.32]),down_R(yaw),base); goto(qt)
          23 +    z=0.32
          24 +    while z>0.0:
          25 +        qt,ok=ik(q_of(obs),np.array([x,y,z-0.004]),down_R(yaw),base)
          26 +        if not ok: print('ikfail'); break
          27 +        if not goto(qt): break
          28 +        z-=0.004
          29 +    print(round(x,3),'lowest',round(z,3))
          30 +env.close()
diff --git a/explore12.py b/explore12.py
new file mode 100644
index 0000000..ff25af5
--- /dev/null
+++ b/explore12.py
@@ -0,0 +1,34 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import fk, ik, down_R
           4 +env = make_env()
           5 +seed=1
           6 +jn=[f'joint_{i}' for i in range(1,8)]
           7 +def q_of(o): return np.array([o.get(R,f) for f in jn])
           8 +def goto(qt,g=0):
           9 +    global obs
          10 +    for _ in range(60):
          11 +        q=q_of(obs); d=qt-q
          12 +        d=(d+np.pi)%(2*np.pi)-np.pi
          13 +        if np.max(np.abs(d))<1e-5: return True
          14 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=g
          15 +        obs,r,te,tr,info=env.step(a)
          16 +        if obs.get(R,'grasp_active')>0: return 'G'
          17 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          18 +    return False
          19 +bx,by=0.1377,0.1831
          20 +z=float(sys.argv[1]); yaw=float(sys.argv[2])
          21 +obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot')
          22 +base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          23 +found=False
          24 +for dx in np.arange(-0.12,0.121,0.02):
          25 +    for dy in np.arange(-0.12,0.121,0.02):
          26 +        p=np.array([bx+dx,by+dy,z])
          27 +        qt,ok=ik(q_of(obs),p+[0,0,0.05],down_R(yaw),base); goto(qt)
          28 +        qt,ok=ik(q_of(obs),p,down_R(yaw),base); r=goto(qt)
          29 +        a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
          30 +        if obs.get(R,'grasp_active')>0 or r=='G':
          31 +            print('GRASP at',dx,dy,z, [round(obs.get(R,f),4) for f in ['finger_state','grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']]); found=True; break
          32 +    if found: break
          33 +print('done',z,yaw,found)
          34 +env.close()
diff --git a/explore13.py b/explore13.py
new file mode 100644
index 0000000..a50645a
--- /dev/null
+++ b/explore13.py
@@ -0,0 +1,44 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys, json
           3 +from kin import fk, ik, down_R
           4 +env = make_env()
           5 +seed=1
           6 +jn=[f'joint_{i}' for i in range(1,8)]
           7 +def q_of(o): return np.array([o.get(R,f) for f in jn])
           8 +def goto(qt,g=0):
           9 +    global obs
          10 +    for _ in range(60):
          11 +        q=q_of(obs); d=qt-q
          12 +        d=(d+np.pi)%(2*np.pi)-np.pi
          13 +        if np.max(np.abs(d))<1e-5: return True
          14 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=g
          15 +        obs,r,te,tr,info=env.step(a)
          16 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          17 +    return False
          18 +bx,by=0.1377,0.1831
          19 +obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot')
          20 +base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          21 +p=np.array([bx-0.1,by-0.04,0.235])
          22 +qt,ok=ik(q_of(obs),p+[0,0,0.05],down_R(0),base); goto(qt)
          23 +qt,ok=ik(q_of(obs),p,down_R(0),base); goto(qt)
          24 +a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
          25 +for n in sorted(obs.get_object_names()):
          26 +    o=obs.get_object_from_name(n)
          27 +    print(n, 'grasp_active', obs.get(o,'grasp_active'))
          28 +recs=[]
          29 +def rec():
          30 +    d={'q':q_of(obs).tolist(),'base':[obs.get(R,f) for f in ['pos_base_x','pos_base_y','pos_base_rot']],
          31 +       'tf':[obs.get(R,f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']],
          32 +       'fs':obs.get(R,'finger_state')}
          33 +    for n in ['target_block']:
          34 +        o=obs.get_object_from_name(n); d[n]=[obs.get(o,f) for f in ['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']]
          35 +    recs.append(d)
          36 +rec()
          37 +qt,ok=ik(q_of(obs),p+[0,0,0.08],down_R(0),base); print('lift',goto(qt)); rec()
          38 +rng=np.random.default_rng(0)
          39 +for i in range(15):
          40 +    a=np.zeros(11,dtype=np.float32); a[3:10]=rng.uniform(-0.1,0.1,7); a[1]=rng.uniform(-0.05,0.05); a[2]=rng.uniform(-0.1,0.1)
          41 +    obs,*_=env.step(a); rec()
          42 +json.dump(recs,open('grasp_recs.json','w'))
          43 +for d in recs: print(np.round(d['target_block'],4), np.round(d['tf'],4), d['fs'])
          44 +env.close()
diff --git a/explore14.py b/explore14.py
new file mode 100644
index 0000000..19b5477
--- /dev/null
+++ b/explore14.py
@@ -0,0 +1,39 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import tool_fk, tool_ik, down_R
           4 +env = make_env()
           5 +seed=int(sys.argv[1]); dz=float(sys.argv[2])
           6 +jn=[f'joint_{i}' for i in range(1,8)]
           7 +def q_of(o): return np.array([o.get(R,f) for f in jn])
           8 +def goto(qt,g=0):
           9 +    global obs
          10 +    for _ in range(60):
          11 +        q=q_of(obs); d=qt-q
          12 +        d=(d+np.pi)%(2*np.pi)-np.pi
          13 +        if np.max(np.abs(d))<1e-5: return True
          14 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=g
          15 +        obs,r,te,tr,info=env.step(a)
          16 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          17 +    return False
          18 +def move(p, n=10):
          19 +    cur=tool_fk(q_of(obs),base)[:3,3]
          20 +    for k in range(1,n+1):
          21 +        qt,ok=tool_ik(q_of(obs),cur+(p-cur)*k/n,down_R(0),base)
          22 +        if not goto(qt): return False
          23 +    return True
          24 +obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot'); B=obs.get_object_from_name('target_block')
          25 +base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          26 +bp=np.array([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]); hz=obs.get(B,'half_extent_z')
          27 +print('block',bp)
          28 +print(move(bp+[0,0,0.15]), move(bp+[0,0,hz+dz]))
          29 +print('tool',np.round(tool_fk(q_of(obs),base)[:3,3],4))
          30 +a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
          31 +print('grasp',obs.get(R,'grasp_active'),obs.get(R,'finger_state'),np.round([obs.get(R,f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qw']],4))
          32 +print('lift',move(bp+[0,0,0.2]), 'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
          33 +print('move',move(bp+[0,-0.1,0.2]))
          34 +print('down',move(bp+[0,-0.1,hz+dz+0.05]), 'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
          35 +a=np.zeros(11,dtype=np.float32); a[10]=1; obs,*_=env.step(a)
          36 +print('open: grasp',obs.get(R,'grasp_active'),'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
          37 +obs,*_=env.step(np.zeros(11,dtype=np.float32))
          38 +print('block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
          39 +env.close()
diff --git a/explore2.py b/explore2.py
new file mode 100644
index 0000000..af402d1
--- /dev/null
+++ b/explore2.py
@@ -0,0 +1,18 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +R = obs.get_object_from_name('robot')
           6 +feats = ['pos_base_x','pos_base_y','pos_base_rot']+[f'joint_{i}' for i in range(1,8)]+['finger_state','grasp_active']
           7 +def rs(o): return np.array([o.get(R,f) for f in feats])
           8 +prev = rs(obs)
           9 +tests = [np.eye(11)[i]*0.1 for i in range(10)] + [np.eye(11)[i]*-0.1 for i in range(10)]
          10 +a = np.zeros(11); a[10]=-1; tests.append(a)
          11 +a = np.zeros(11); a[10]=1; tests.append(a)
          12 +a = np.zeros(11); a[3]=0.5; tests.append(a)
          13 +for a in tests:
          14 +    obs, r, term, trunc, info = env.step(a.astype(np.float32))
          15 +    cur = rs(obs)
          16 +    print(np.round(a,2).tolist(), 'd=', np.round(cur-prev,3).tolist(), r, term, trunc)
          17 +    prev = cur
          18 +env.close()
diff --git a/explore3.py b/explore3.py
new file mode 100644
index 0000000..fe6b7a5
--- /dev/null
+++ b/explore3.py
@@ -0,0 +1,30 @@
           1 +# descend EE over free table spot, find where motion gets blocked
           2 +from env_client import make_env
           3 +import numpy as np
           4 +from kin import fk, ik, down_R
           5 +env = make_env()
           6 +obs, info = env.reset(seed=1)
           7 +R = obs.get_object_from_name('robot')
           8 +jn=[f'joint_{i}' for i in range(1,8)]
           9 +def q_of(o): return np.array([o.get(R,f) for f in jn])
          10 +base=(o:=obs, o.get(R,'pos_base_x'), o.get(R,'pos_base_y'), o.get(R,'pos_base_rot'))[1:]
          11 +q=q_of(obs)
          12 +print('start ee', fk(q,base)[:3,3])
          13 +x,y=0.25,-0.3
          14 +def goto(qt):
          15 +    global obs
          16 +    for _ in range(40):
          17 +        q=q_of(obs); d=qt-q
          18 +        d=(d+np.pi)%(2*np.pi)-np.pi
          19 +        if np.max(np.abs(d))<1e-4: return True
          20 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          21 +        obs,r,te,tr,info=env.step(a)
          22 +        if np.allclose(q_of(obs),q): return False
          23 +    return False
          24 +for z in np.arange(0.35,-0.1,-0.01):
          25 +    qt,ok=ik(q_of(obs),np.array([x,y,z]),down_R(0),base)
          26 +    moved=goto(qt)
          27 +    ee=fk(q_of(obs),base)[:3,3]
          28 +    print(round(z,3),ok,moved,np.round(ee,3))
          29 +    if not moved: break
          30 +env.close()
diff --git a/explore4.py b/explore4.py
new file mode 100644
index 0000000..c69a068
--- /dev/null
+++ b/explore4.py
@@ -0,0 +1,36 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import fk, ik, down_R
           4 +env = make_env()
           5 +seed=int(sys.argv[1]); yaw=float(sys.argv[2])
           6 +obs, info = env.reset(seed=seed)
           7 +R = obs.get_object_from_name('robot'); B=obs.get_object_from_name('target_block')
           8 +jn=[f'joint_{i}' for i in range(1,8)]
           9 +def q_of(o): return np.array([o.get(R,f) for f in jn])
          10 +base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          11 +bx,by,bz=[obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]
          12 +print('block',bx,by,bz,[obs.get(B,f) for f in ['half_extent_x','half_extent_y','half_extent_z']])
          13 +def goto(qt, grip=0):
          14 +    global obs
          15 +    for _ in range(40):
          16 +        q=q_of(obs); d=qt-q
          17 +        d=(d+np.pi)%(2*np.pi)-np.pi
          18 +        if np.max(np.abs(d))<1e-4: return True
          19 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=grip
          20 +        obs,r,te,tr,info=env.step(a)
          21 +        if np.allclose(q_of(obs),q): return False
          22 +    return False
          23 +for z in np.arange(0.35,0.1,-0.005):
          24 +    qt,ok=ik(q_of(obs),np.array([bx,by,z]),down_R(yaw),base)
          25 +    if not goto(qt): print('blocked at',z); break
          26 +ee=fk(q_of(obs),base)[:3,3]; print('ee',ee)
          27 +a=np.zeros(11,dtype=np.float32); a[10]=-1
          28 +obs,*_=env.step(a)
          29 +print('grasp', obs.get(R,'grasp_active'), obs.get(R,'finger_state'), obs.get(B,'grasp_active'))
          30 +print('tf',[round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
          31 +# lift
          32 +for z in np.arange(ee[2],0.35,0.01):
          33 +    qt,ok=ik(q_of(obs),np.array([bx,by,z]),down_R(yaw),base)
          34 +    goto(qt)
          35 +print('block after lift',[round(obs.get(B,f),4) for f in ['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']], 'ee',fk(q_of(obs),base)[:3,3])
          36 +env.close()
diff --git a/explore5.py b/explore5.py
new file mode 100644
index 0000000..d4261b4
--- /dev/null
+++ b/explore5.py
@@ -0,0 +1,36 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import fk, ik, down_R
           4 +env = make_env()
           5 +obs, info = env.reset(seed=1)
           6 +R = obs.get_object_from_name('robot')
           7 +jn=[f'joint_{i}' for i in range(1,8)]
           8 +def q_of(o): return np.array([o.get(R,f) for f in jn])
           9 +base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          10 +x,y=float(sys.argv[1]),float(sys.argv[2])
          11 +def goto(qt):
          12 +    global obs
          13 +    for _ in range(40):
          14 +        q=q_of(obs); d=qt-q
          15 +        d=(d+np.pi)%(2*np.pi)-np.pi
          16 +        if np.max(np.abs(d))<1e-4: return True
          17 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          18 +        obs,r,te,tr,info=env.step(a)
          19 +        if np.allclose(q_of(obs),q): 
          20 +            print('blocked; q',np.round(q,3),'d',np.round(d,3)); return False
          21 +    return False
          22 +for z in np.arange(0.35,0.0,-0.005):
          23 +    qt,ok=ik(q_of(obs),np.array([x,y,z]),down_R(0),base)
          24 +    if not goto(qt): print('blocked at',z); break
          25 +# try single joint moves
          26 +q0=q_of(obs)
          27 +for j in range(7):
          28 +    for s in [0.02,-0.02]:
          29 +        a=np.zeros(11,dtype=np.float32); a[3+j]=s
          30 +        o2,*_=env.step(a)
          31 +        moved=not np.allclose(q_of(o2),q_of(obs))
          32 +        print(j,s,moved, 'eez', round(fk(q_of(o2),base)[2,3],4))
          33 +        obs=o2
          34 +        if moved:
          35 +            a[3+j]=-s; obs,*_=env.step(a)
          36 +env.close()
diff --git a/explore6.py b/explore6.py
new file mode 100644
index 0000000..5e00691
--- /dev/null
+++ b/explore6.py
@@ -0,0 +1,30 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import fk, ik, down_R
           4 +env = make_env()
           5 +seed=int(sys.argv[1]); yaw=float(sys.argv[2]); zt=float(sys.argv[3])
           6 +obs, info = env.reset(seed=seed)
           7 +R = obs.get_object_from_name('robot'); B=obs.get_object_from_name('target_block')
           8 +jn=[f'joint_{i}' for i in range(1,8)]
           9 +def q_of(o): return np.array([o.get(R,f) for f in jn])
          10 +base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          11 +bx,by,bz=[obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]
          12 +def goto(qt, grip=0):
          13 +    global obs
          14 +    for _ in range(40):
          15 +        q=q_of(obs); d=qt-q
          16 +        d=(d+np.pi)%(2*np.pi)-np.pi
          17 +        if np.max(np.abs(d))<1e-4: return True
          18 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=grip
          19 +        obs,r,te,tr,info=env.step(a)
          20 +        if np.allclose(q_of(obs),q): return False
          21 +    return False
          22 +for z in np.arange(0.35,zt-1e-6,-0.005):
          23 +    qt,ok=ik(q_of(obs),np.array([bx,by,z]),down_R(yaw),base)
          24 +    if not goto(qt): print('blocked at',z); break
          25 +print('ee',fk(q_of(obs),base)[:3,3])
          26 +for g in [-1,-1,-1,0,1,1,-1]:
          27 +    a=np.zeros(11,dtype=np.float32); a[10]=g
          28 +    obs,*_=env.step(a)
          29 +    print(g,'grasp', obs.get(R,'grasp_active'), obs.get(R,'finger_state'), obs.get(B,'grasp_active'), [round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
          30 +env.close()
diff --git a/explore7.py b/explore7.py
new file mode 100644
index 0000000..b29f719
--- /dev/null
+++ b/explore7.py
@@ -0,0 +1,35 @@
           1 +# measure blocking height at many xy
           2 +from env_client import make_env
           3 +import numpy as np, sys
           4 +from kin import fk, ik, down_R
           5 +env = make_env()
           6 +seed=int(sys.argv[1])
           7 +obs0, info = env.reset(seed=seed)
           8 +R = obs0.get_object_from_name('robot')
           9 +jn=[f'joint_{i}' for i in range(1,8)]
          10 +def q_of(o): return np.array([o.get(R,f) for f in jn])
          11 +base=(obs0.get(R,'pos_base_x'), obs0.get(R,'pos_base_y'), obs0.get(R,'pos_base_rot'))
          12 +for n in sorted(obs0.get_object_names()):
          13 +    if n=='robot': continue
          14 +    o=obs0.get_object_from_name(n); print(n,[round(obs0.get(o,f),3) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z']])
          15 +def goto(qt):
          16 +    global obs
          17 +    for _ in range(40):
          18 +        q=q_of(obs); d=qt-q
          19 +        d=(d+np.pi)%(2*np.pi)-np.pi
          20 +        if np.max(np.abs(d))<1e-5: return True
          21 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          22 +        obs,r,te,tr,info=env.step(a)
          23 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          24 +    return False
          25 +pts=[tuple(map(float,s.split(','))) for s in sys.argv[2:]]
          26 +for (x,y) in pts:
          27 +    obs,_=env.reset(seed=seed)
          28 +    qt,ok=ik(q_of(obs),np.array([x,y,0.32]),down_R(0),base); goto(qt)
          29 +    z=0.32
          30 +    while z>0.0:
          31 +        qt,ok=ik(q_of(obs),np.array([x,y,z-0.002]),down_R(0),base)
          32 +        if not goto(qt): break
          33 +        z-=0.002
          34 +    print((x,y),'lowest flange z',round(z,4))
          35 +env.close()
diff --git a/explore8.py b/explore8.py
new file mode 100644
index 0000000..babb84d
--- /dev/null
+++ b/explore8.py
@@ -0,0 +1,35 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import fk, ik, down_R
           4 +env = make_env()
           5 +seed=1
           6 +obs, info = env.reset(seed=seed)
           7 +R = obs.get_object_from_name('robot'); B=obs.get_object_from_name('target_block')
           8 +jn=[f'joint_{i}' for i in range(1,8)]
           9 +def q_of(o): return np.array([o.get(R,f) for f in jn])
          10 +base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          11 +bx,by,bz=[obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]
          12 +def goto(qt):
          13 +    global obs
          14 +    for _ in range(60):
          15 +        q=q_of(obs); d=qt-q
          16 +        d=(d+np.pi)%(2*np.pi)-np.pi
          17 +        if np.max(np.abs(d))<1e-5: return True
          18 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          19 +        obs,r,te,tr,info=env.step(a)
          20 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          21 +    return False
          22 +configs=[]
          23 +for z in [0.235,0.26,0.29]:
          24 +  for yaw in [0,np.pi/4,np.pi/2]:
          25 +    for off in [(0,0),(0.03,0),(0,0.035),(0.05,0),(0,0.05)]:
          26 +        configs.append((z,yaw,off))
          27 +for z,yaw,off in configs:
          28 +    obs,_=env.reset(seed=seed)
          29 +    qt,_=ik(q_of(obs),np.array([bx+off[0],by+off[1],0.32]),down_R(yaw),base); r1=goto(qt)
          30 +    qt,ok=ik(q_of(obs),np.array([bx+off[0],by+off[1],z]),down_R(yaw),base); r2=goto(qt)
          31 +    a=np.zeros(11,dtype=np.float32); a[10]=-1
          32 +    obs,*_=env.step(a)
          33 +    g=obs.get(R,'grasp_active')
          34 +    print(z,round(yaw,2),off,r1,r2,'grasp',g,obs.get(R,'finger_state'))
          35 +env.close()
diff --git a/explore9.py b/explore9.py
new file mode 100644
index 0000000..6e13734
--- /dev/null
+++ b/explore9.py
@@ -0,0 +1,32 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import fk, ik, down_R
           4 +env = make_env()
           5 +seed=1
           6 +R=None
           7 +jn=[f'joint_{i}' for i in range(1,8)]
           8 +def q_of(o): return np.array([o.get(R,f) for f in jn])
           9 +def goto(qt):
          10 +    global obs
          11 +    for _ in range(60):
          12 +        q=q_of(obs); d=qt-q
          13 +        d=(d+np.pi)%(2*np.pi)-np.pi
          14 +        if np.max(np.abs(d))<1e-5: return True
          15 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
          16 +        obs,r,te,tr,info=env.step(a)
          17 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          18 +    return False
          19 +for (x,y,bdy,bdx) in [(0.3,0.0,0,0),(0.3,0,0.2,0),(0.3,0,-0.2,0),(0.3,0,0,-0.1),(0.45,0.3,0,0),(0.45,0.3,0.2,0),(0.45,0.0,0,0),(0.2,0.0,0,0),(0.1,0,0,0)]:
          20 +    obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot')
          21 +    for _ in range(2):
          22 +        a=np.zeros(11,dtype=np.float32); a[1]=bdy/2; a[0]=bdx/2; obs,*_=env.step(a)
          23 +    base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          24 +    qt,ok=ik(q_of(obs),np.array([x,y,0.32]),down_R(0),base); goto(qt)
          25 +    z=0.32
          26 +    while z>0.0:
          27 +        qt,ok=ik(q_of(obs),np.array([x,y,z-0.002]),down_R(0),base)
          28 +        if not ok: print('ik fail'); break
          29 +        if not goto(qt): break
          30 +        z-=0.002
          31 +    print((x,y),np.round(base,3),'lowest',round(z,4),'q',np.round(q_of(obs),2))
          32 +env.close()
diff --git a/fit.py b/fit.py
new file mode 100644
index 0000000..9804957
--- /dev/null
+++ b/fit.py
@@ -0,0 +1,26 @@
           1 +import json, numpy as np
           2 +from scipy.optimize import least_squares
           3 +from kin import fk
           4 +def q2R(x,y,z,w):
           5 +    return np.array([[1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],[2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],[2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]])
           6 +def T(p,q): M=np.eye(4); M[:3,:3]=q2R(*q); M[:3,3]=p; return M
           7 +recs=json.load(open('grasp_recs.json'))
           8 +W=[]
           9 +for d in recs:
          10 +    To=T(d['target_block'][:3],d['target_block'][3:]); Tg=T(d['tf'][:3],d['tf'][3:])
          11 +    W.append(To@np.linalg.inv(Tg))
          12 +def pred(params,d):
          13 +    mx,my,mz,tx,ty,tz=params
          14 +    b=d['base']; c,s=np.cos(b[2]),np.sin(b[2])
          15 +    base=(b[0]+c*mx-s*my, b[1]+s*mx+c*my, b[2])
          16 +    F=fk(d['q'],base,mz); Tt=np.eye(4); Tt[:3,3]=[tx,ty,tz]
          17 +    return F@Tt
          18 +def res(params):
          19 +    r=[]
          20 +    for d,Wt in zip(recs,W):
          21 +        P=pred(params,d); r.extend(P[:3,3]-Wt[:3,3]); r.extend(0.1*(P[:3,:3]-Wt[:3,:3]).ravel())
          22 +    return np.array(r)
          23 +sol=least_squares(res,np.zeros(6))
          24 +print('params',np.round(sol.x,4),'rms',np.sqrt(np.mean(sol.fun**2)))
          25 +for d,Wt in zip(recs,W):
          26 +    P=pred(sol.x,d); print(np.round(P[:3,3]-Wt[:3,3],4), round(np.linalg.norm(P[:3,:3]-Wt[:3,:3]),4), np.round(d['base'],3))
diff --git a/grasp_recs.json b/grasp_recs.json
new file mode 100644
index 0000000..b0f926f
--- /dev/null
+++ b/grasp_recs.json
@@ -0,0 +1 @@
           1 +[{"q": [0.13092538714408875, 0.1355351358652115, -4.070899963378906, -2.4199166297912598, 0.18024161458015442, -0.6480788588523865, -0.9382089376449585], "base": [-0.11999999731779099, 0.0, 0.0], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.13774842023849487, 0.18313223123550415, 0.10000000149011612, 0.0, 0.0, 0.0, 1.0]}, {"q": [0.2602936327457428, 0.005289873108267784, -4.112614154815674, -2.3573458194732666, 0.006321930792182684, -0.7813294529914856, -0.7152383327484131], "base": [-0.11999999731779099, 0.0, 0.0], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.13777418434619904, 0.18315619230270386, 0.12993764877319336, -7.310877845156938e-05, -1.5168604477366898e-05, -2.0737112208735198e-05, 1.0]}, {"q": [0.28768596053123474, -0.04075278714299202, -4.2044196128845215, -2.454040288925171, 0.06897597759962082, -0.6987783312797546, -0.6939111948013306], "base": [-0.11999999731779099, 0.02294965647161007, 0.00872499868273735], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.11841627955436707, 0.18431049585342407, 0.11117354035377502, -0.027075249701738358, -0.029832175001502037, 0.07107656449079514, 0.9966569542884827]}, {"q": [0.3747004568576813, 0.02241792343556881, -4.3038716316223145, -2.3825595378875732, -0.024306906387209892, -0.6528472304344177, -0.7587800621986389], "base": [-0.11999999731779099, 0.0592675507068634, 0.017017241567373276], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.1340419501066208, 0.2859647274017334, 0.12804409861564636, 0.047015685588121414, -0.02168448455631733, 0.013040252029895782, 0.9985736012458801]}, {"q": [0.33464282751083374, 0.006955367513000965, -4.398207664489746, -2.457702875137329, 0.00981797743588686, -0.6234093308448792, -0.7357030510902405], "base": [-0.11999999731779099, 0.04763530194759369, 0.11645923554897308], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.06615465134382248, 0.2772578299045563, 0.11039917916059494, 0.022801784798502922, -0.01819007284939289, 0.154471293091774, 0.9875665903091431]}, {"q": [0.430809885263443, 0.044063761830329895, -4.3681159019470215, -2.420013666152954, -0.012397737242281437, -0.6963900327682495, -0.6914053559303284], "base": [-0.11999999731779099, 0.05017073452472687, 0.07850760966539383], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.08899686485528946, 0.2631990313529968, 0.11706054210662842, 0.021082546561956406, 0.01384740974754095, 0.08626984059810638, 0.9959524273872375]}, {"q": [0.42797696590423584, 0.1219613254070282, -4.281307220458984, -2.4484546184539795, 0.001908229081891477, -0.7320161461830139, -0.6725453734397888], "base": [-0.11999999731779099, 0.033961858600378036, 0.05683140829205513], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.0783730000257492, 0.21458899974822998, 0.10859720408916473, 0.011547951027750969, 0.06979651749134064, 0.04967912659049034, 0.9962565302848816]}, {"q": [0.42797696590423584, 0.1219613254070282, -4.281307220458984, -2.4484546184539795, 0.001908229081891477, -0.7320161461830139, -0.6725453734397888], "base": [-0.11999999731779099, 0.033961858600378036, 0.05683140829205513], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.0783730000257492, 0.21458899974822998, 0.10859720408916473, 0.011547951027750969, 0.06979651749134064, 0.04967912659049034, 0.9962565302848816]}, {"q": [0.39520037174224854, 0.0520172193646431, -4.291239261627197, -2.3891897201538086, -0.05196332931518555, -0.8216118812561035, -0.691635012626648], "base": [-0.11999999731779099, 0.00381316221319139, -0.025017980486154556], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.09280125051736832, 0.18034812808036804, 0.12468945980072021, 0.0019837466534227133, 0.06191391497850418, 0.001145858783274889, 0.9980788826942444]}, {"q": [0.41126686334609985, 0.01175644714385271, -4.256840229034424, -2.449286460876465, 0.036459289491176605, -0.8485898375511169, -0.770535945892334], "base": [-0.11999999731779099, 0.016723977401852608, 0.0604129321873188], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.07642045617103577, 0.15718945860862732, 0.11200276762247086, -0.06127870827913284, 0.05282686650753021, 0.010459961369633675, 0.9966668486595154]}, {"q": [0.39934229850769043, 0.10267455130815506, -4.256861209869385, -2.464240789413452, 0.060501981526613235, -0.7495705485343933, -0.6807472109794617], "base": [-0.11999999731779099, 0.012728490866720676, 0.11195869743824005], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.06889219582080841, 0.1813991814851761, 0.10365962237119675, -0.01990514062345028, 0.060252998024225235, 0.09820836037397385, 0.993140697479248]}, {"q": [0.39934229850769043, 0.10267455130815506, -4.256861209869385, -2.464240789413452, 0.060501981526613235, -0.7495705485343933, -0.6807472109794617], "base": [-0.11999999731779099, 0.012728490866720676, 0.11195869743824005], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.06889219582080841, 0.1813991814851761, 0.10365962237119675, -0.01990514062345028, 0.060252998024225235, 0.09820836037397385, 0.993140697479248]}, {"q": [0.48482707142829895, 0.1962597817182541, -4.353919982910156, -2.391512870788574, 0.15674099326133728, -0.6581284999847412, -0.7509943842887878], "base": [-0.11999999731779099, 0.059991370886564255, 0.18994581699371338], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.10044056177139282, 0.29826128482818604, 0.11269284039735794, 0.0413275845348835, 0.020512929186224937, 0.13962697982788086, 0.9891287088394165]}, {"q": [0.5493018627166748, 0.1922573745250702, -4.407445430755615, -2.331136703491211, 0.24144701659679413, -0.7049024701118469, -0.7432075142860413], "base": [-0.11999999731779099, 0.05426665395498276, 0.27614927291870117], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.11149708181619644, 0.3146091401576996, 0.12423250824213028, 0.031112143769860268, -0.012103511951863766, 0.20791339874267578, 0.9775773882865906]}, {"q": [0.4574039876461029, 0.238658607006073, -4.384570598602295, -2.4254636764526367, 0.28529098629951477, -0.8017041087150574, -0.6916173100471497], "base": [-0.11999999731779099, 0.05554252862930298, 0.36197012662887573], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.03835344314575195, 0.25337013602256775, 0.10227729380130768, -0.04327385127544403, 0.05593603849411011, 0.3320944011211395, 0.9405912160873413]}, {"q": [0.3706204891204834, 0.3069220781326294, -4.471232891082764, -2.456601619720459, 0.2713507115840912, -0.7084916830062866, -0.6791709065437317], "base": [-0.11999999731779099, 0.0314289852976799, 0.31030526757240295], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.0010528229176998138, 0.2471524178981781, 0.0999068096280098, 0.009837355464696884, 0.0719449371099472, 0.39112570881843567, 0.9174681305885315]}, {"q": [0.4482441544532776, 0.2520959675312042, -4.546321868896484, -2.4989354610443115, 0.28857532143592834, -0.6976736187934875, -0.6172288060188293], "base": [-0.11999999731779099, 0.03747658059000969, 0.26798951625823975], "tf": [-0.01984672248363495, -0.04004167020320892, 0.059822000563144684, 1.0, 6.5922113208216615e-06, -7.122983788576676e-06, 2.2484688088297844e-05], "fs": 0.18000000715255737, "target_block": [0.01322268322110176, 0.22675953805446625, 0.09632780402898788, -0.004735234193503857, 0.04927924647927284, 0.4082244038581848, 0.9115382432937622]}]
\ No newline at end of file
diff --git a/kin.py b/kin.py
new file mode 100644
index 0000000..53f14cb
--- /dev/null
+++ b/kin.py
@@ -0,0 +1,95 @@
           1 +import numpy as np
           2 +
           3 +def _rpy(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def _T(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = _rpy(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +PI = np.pi
          13 +H = PI / 2
          14 +JOINTS = [
          15 +    _T((0, 0, 0.15643), (PI, 0, 0)),
          16 +    _T((0, 0.005375, -0.12838), (H, 0, 0)),
          17 +    _T((0, -0.21038, -0.006375), (-H, 0, 0)),
          18 +    _T((0, 0.006375, -0.21038), (H, 0, 0)),
          19 +    _T((0, -0.20843, -0.006375), (-H, 0, 0)),
          20 +    _T((0, 0.00017505, -0.10593), (H, 0, 0)),
          21 +    _T((0, -0.10593, -0.00017505), (-H, 0, 0)),
          22 +]
          23 +EE = _T((0, 0, -0.061525), (PI, 0, 0))
          24 +
          25 +def _rz(q):
          26 +    c, s = np.cos(q), np.sin(q)
          27 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          28 +
          29 +def fk(q, base=(0, 0, 0), base_z=0.0, tool=0.0):
          30 +    """Return 4x4 world transform of end effector (+tool offset along EE z)."""
          31 +    bx, by, br = base
          32 +    T = _rz(br); T[0, 3] = bx; T[1, 3] = by; T[2, 3] = base_z
          33 +    for Tj, qj in zip(JOINTS, q):
          34 +        T = T @ Tj @ _rz(qj)
          35 +    T = T @ EE
          36 +    if tool:
          37 +        Tt = np.eye(4); Tt[2, 3] = tool; T = T @ Tt
          38 +    return T
          39 +
          40 +def pose_err(T, p, R):
          41 +    ep = p - T[:3, 3]
          42 +    Re = R @ T[:3, :3].T
          43 +    # axis-angle of Re
          44 +    ang = np.arccos(np.clip((np.trace(Re) - 1) / 2, -1, 1))
          45 +    if ang < 1e-9:
          46 +        eo = np.zeros(3)
          47 +    else:
          48 +        v = np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
          49 +        s = np.sin(ang)
          50 +        eo = v / (2 * s) * ang if s > 1e-6 else np.zeros(3)
          51 +    return np.concatenate([ep, eo])
          52 +
          53 +def ik(q0, p, R, base, base_z=0.0, tool=0.0, iters=200, wo=0.3, tol=1e-4):
          54 +    q = np.array(q0, dtype=float)
          55 +    for it in range(iters):
          56 +        T = fk(q, base, base_z, tool)
          57 +        e = pose_err(T, p, R)
          58 +        e[3:] *= wo
          59 +        if np.linalg.norm(e) < tol:
          60 +            return q, True
          61 +        J = np.zeros((6, 7))
          62 +        h = 1e-6
          63 +        for j in range(7):
          64 +            dq = q.copy(); dq[j] += h
          65 +            e2 = pose_err(fk(dq, base, base_z, tool), p, R); e2[3:] *= wo
          66 +            J[:, j] = (e - e2) / h
          67 +        lam = 1e-3
          68 +        dq = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
          69 +        n = np.linalg.norm(dq)
          70 +        if n > 0.3: dq *= 0.3 / n
          71 +        q = q + dq
          72 +    return q, False
          73 +
          74 +def down_R(yaw):
          75 +    # EE z axis pointing down, x axis at yaw
          76 +    c, s = np.cos(yaw), np.sin(yaw)
          77 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          78 +    return np.stack([x, y, z], axis=1)
          79 +
          80 +MOUNT = (0.12, 0.0, -0.0052)
          81 +TOOL = 0.12
          82 +
          83 +def tool_fk(q, base):
          84 +    bx, by, br = base
          85 +    c, s = np.cos(br), np.sin(br)
          86 +    b = (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
          87 +    return fk(q, b, MOUNT[2], TOOL)
          88 +
          89 +def mount_base(base):
          90 +    bx, by, br = base
          91 +    c, s = np.cos(br), np.sin(br)
          92 +    return (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
          93 +
          94 +def tool_ik(q0, p, R, base, **kw):
          95 +    return ik(q0, p, R, mount_base(base), MOUNT[2], TOOL, **kw)
diff --git a/t_fk.py b/t_fk.py
new file mode 100644
index 0000000..ad05b82
--- /dev/null
+++ b/t_fk.py
@@ -0,0 +1,4 @@
           1 +import numpy as np
           2 +from kin import fk
           3 +q=[0,-0.35,-np.pi,-2.5,0,-0.87,np.pi/2]
           4 +T=fk(q,(-0.12,0,0)); np.set_printoptions(precision=3,suppress=True); print(T)
```

</details>

<a id="C003"></a>
### C003 · First full state-machine approach

Commit `16f56456fec706f04e3a62eb21234a4f66190a7d`; parents: a6d08ebb9d48a69a42d4ba56e5f0b04153d90d8f. Recorded author date: 2026-09-30T19:59:02+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0142](01_timeline.md#E0142): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_16f5645_approach.py) · [Exact all-file diff](evidence/diffs/C003_16f5645.diff)

[Previous saved controller snapshot](evidence/versions/C002_a6d08eb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2d0f6a3..c3cb75d 100644
--- a/approach.py
+++ b/approach.py
@@ -1,15 +1,310 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place
           2 +the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py)."""
    1      3  import numpy as np
    2        -from kin import fk, ik, down_R
           4 +from kin import tool_fk, tool_ik, down_R
           5 +
           6 +JN = [f'joint_{i}' for i in range(1, 8)]
           7 +Z_SAFE = 0.30          # tool height for transit
           8 +STEP = 0.2             # max joint delta per step
           9 +SEG = 0.03             # cartesian interpolation segment length
          10 +
          11 +
          12 +def _q2R(x, y, z, w):
          13 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          14 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          15 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          16 +
          17 +
          18 +def _T(p, q):
          19 +    M = np.eye(4); M[:3, :3] = _q2R(*q); M[:3, 3] = p
          20 +    return M
          21 +
          22 +
          23 +def _yaw_of_quat(q):
          24 +    x, y, z, w = q
          25 +    return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
          26 +
          27 +
    3     28  class GeneratedApproach:
    4        -    def __init__(self, action_space, observation_space, primitives): pass
          29 +    def __init__(self, action_space, observation_space, primitives):
          30 +        self.action_space = action_space
          31 +        self.observation_space = observation_space
          32 +
          33 +    # ------------------------------------------------------------ helpers
          34 +    def _obj(self, state, name):
          35 +        return state.get_object_from_name(name)
          36 +
          37 +    def _pose(self, state, name):
          38 +        o = self._obj(state, name)
          39 +        return (np.array([state.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')]),
          40 +                np.array([state.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]),
          41 +                np.array([state.get(o, f) for f in ('half_extent_x', 'half_extent_y', 'half_extent_z')]))
          42 +
          43 +    def _q(self, state):
          44 +        return np.array([state.get(self.robot, f) for f in JN])
          45 +
          46 +    def _base(self, state):
          47 +        return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
          48 +                state.get(self.robot, 'pos_base_rot'))
          49 +
          50 +    def _tool(self, state):
          51 +        return tool_fk(self._q(state), self._base(state))
          52 +
          53 +    def _grasped_name(self, state):
          54 +        for n in self.names:
          55 +            if state.get(self._obj(state, n), 'grasp_active') > 0.5:
          56 +                return n
          57 +        return None
          58 +
          59 +    # ------------------------------------------------------------ planning
    5     60      def reset(self, state, info):
    6        -        R = state.get_object_from_name('robot'); B = state.get_object_from_name('target_block')
    7        -        self.R=R
    8        -        base=(state.get(R,'pos_base_x'), state.get(R,'pos_base_y'), state.get(R,'pos_base_rot'))
    9        -        q=np.array([state.get(R,f'joint_{i}') for i in range(1,8)])
   10        -        p=np.array([state.get(B,'pose_x'),state.get(B,'pose_y'),0.24])
   11        -        self.qt,_=ik(q,p,down_R(0),base)
          61 +        self.robot = state.get_object_from_name('robot')
          62 +        self.names = sorted(n for n in state.get_object_names() if n != 'robot')
          63 +        self.obstructions = sorted(n for n in self.names if n.startswith('obstruction'))
          64 +        rp, _, rh = self._pose(state, 'target_region')
          65 +        self.table_z = rp[2] - rh[2]
          66 +        self.region = (rp, rh)
          67 +        self.tasks = []  # list of (obj_name, kind)
          68 +        for n in self._blocking_obstructions(state):
          69 +            self.tasks.append((n, 'clear'))
          70 +        self.tasks.append(('target_block', 'goal'))
          71 +        self.phase = None
          72 +        self.waypoints = []
          73 +        self.wp_yaw = 0.0
          74 +        self.last_q = None
          75 +        self.stuck = 0
          76 +        self.release_tries = 0
          77 +        self.grasp_tries = 0
          78 +        self.placed_spots = []
          79 +        self.prev_was_motion = False
          80 +        self.descent_len = 0
          81 +        self._start_task(state)
          82 +
          83 +    def _blocking_obstructions(self, state, margin=0.005):
          84 +        rp, rh = self.region
          85 +        out = []
          86 +        for n in self.obstructions:
          87 +            p, _, h = self._pose(state, n)
          88 +            if (abs(p[0] - rp[0]) < rh[0] + h[0] + margin and
          89 +                    abs(p[1] - rp[1]) < rh[1] + h[1] + margin):
          90 +                out.append(n)
          91 +        return out
          92 +
          93 +    def _free_spot(self, state, name):
          94 +        """Pick a spot on the table far from region, target block, other objects."""
          95 +        _, _, h = self._pose(state, name)
          96 +        others = []
          97 +        for n in self.names:
          98 +            if n == name:
          99 +                continue
         100 +            p, _, hh = self._pose(state, n)
         101 +            others.append((p[:2], hh[:2]))
         102 +        rp, rh = self.region
         103 +        best, best_score = None, -1e9
         104 +        for x in np.linspace(0.12, 0.48, 13):
         105 +            for y in np.linspace(-0.32, 0.32, 17):
         106 +                c = np.array([x, y])
         107 +                score = 1e9
         108 +                for p, hh in others:
         109 +                    d = np.max(np.abs(c - p) - hh - h[:2])
         110 +                    score = min(score, d)
         111 +                d = np.max(np.abs(c - rp[:2]) - rh[:2] - h[:2]) - 0.03
         112 +                score = min(score, d)
         113 +                # prefer closer to robot-ish center for reachability
         114 +                score -= 0.02 * np.hypot(x - 0.3, y)
         115 +                if score > best_score:
         116 +                    best, best_score = c, score
         117 +        return best
         118 +
         119 +    def _start_task(self, state):
         120 +        if not self.tasks:
         121 +            self.phase = 'done'
         122 +            return
         123 +        name, kind = self.tasks[0]
         124 +        p, q, h = self._pose(state, name)
         125 +        self.cur_obj = name
         126 +        self.grasp_yaw = self._pick_yaw(q)
         127 +        top = p[2] + h[2]
         128 +        tool = self._tool(state)[:3, 3]
         129 +        wps = []
         130 +        if tool[2] < Z_SAFE - 0.01:
         131 +            wps.append(np.array([tool[0], tool[1], Z_SAFE]))
         132 +        wps.append(np.array([p[0], p[1], Z_SAFE]))
         133 +        wps.append(np.array([p[0], p[1], top + 0.005]))
         134 +        self._set_path(state, wps, self.grasp_yaw)
         135 +        self.phase = 'to_grasp'
         136 +
         137 +    def _pick_yaw(self, q):
         138 +        y = _yaw_of_quat(q)
         139 +        # choose equivalent yaw (mod pi/2) closest to 0
         140 +        y = (y + np.pi / 4) % (np.pi / 2) - np.pi / 4
         141 +        return y
         142 +
         143 +    def _set_path(self, state, wps, yaw):
         144 +        cur = self._tool(state)[:3, 3]
         145 +        pts = []
         146 +        for w in wps:
         147 +            d = np.linalg.norm(w - cur)
         148 +            n = max(1, int(np.ceil(d / SEG)))
         149 +            for k in range(1, n + 1):
         150 +                pts.append(cur + (w - cur) * k / n)
         151 +            cur = w
         152 +        self.waypoints = pts
         153 +        self.wp_yaw = yaw
         154 +        self.stuck = 0
         155 +
         156 +    # ------------------------------------------------------------ control
         157 +    def _track(self, state, grip=0.0):
         158 +        """Return action moving toward current waypoint; None if path complete."""
         159 +        q = self._q(state)
         160 +        base = self._base(state)
         161 +        while self.waypoints:
         162 +            wp = self.waypoints[0]
         163 +            qt, ok = tool_ik(q, wp, down_R(self.wp_yaw), base, iters=100)
         164 +            d = (qt - q + np.pi) % (2 * np.pi) - np.pi
         165 +            if np.max(np.abs(d)) < 1e-4:
         166 +                self.waypoints.pop(0)
         167 +                continue
         168 +            a = np.zeros(11, dtype=np.float32)
         169 +            a[3:10] = np.clip(d, -STEP, STEP)
         170 +            a[10] = grip
         171 +            return a
         172 +        return None
         173 +
         174 +    def _noop(self, grip=0.0):
         175 +        a = np.zeros(11, dtype=np.float32); a[10] = grip
         176 +        return a
         177 +
   12    178      def get_action(self, state):
   13        -        q=np.array([state.get(self.R,f'joint_{i}') for i in range(1,8)])
   14        -        d=(self.qt-q+np.pi)%(2*np.pi)-np.pi
   15        -        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); return a
         179 +        q = self._q(state)
         180 +        moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
         181 +        self.last_q = q.copy()
         182 +        a = self._policy(state, moved)
         183 +        return np.asarray(a, dtype=np.float32)
         184 +
         185 +    def _policy(self, state, moved):
         186 +        ph = self.phase
         187 +        if ph == 'done':
         188 +            return self._noop()
         189 +
         190 +        if ph == 'to_grasp':
         191 +            if not moved and self.prev_was_motion:
         192 +                self.stuck += 1
         193 +            if self.stuck >= 2:
         194 +                self.waypoints = []  # blocked: try grasping here
         195 +            a = self._track(state)
         196 +            if a is not None:
         197 +                self.prev_was_motion = True
         198 +                return a
         199 +            self.phase = 'close'
         200 +            self.prev_was_motion = False
         201 +            return self._noop(-1.0)
         202 +
         203 +        if ph == 'close':
         204 +            g = self._grasped_name(state)
         205 +            if g is None:
         206 +                # descend a bit more and retry
         207 +                self.grasp_tries += 1
         208 +                p, _, h = self._pose(state, self.cur_obj)
         209 +                tool = self._tool(state)[:3, 3]
         210 +                self._set_path(state, [np.array([p[0], p[1], tool[2] - 0.01])], self.grasp_yaw)
         211 +                self.phase = 'to_grasp'
         212 +                self.prev_was_motion = False
         213 +                if self.grasp_tries > 6:
         214 +                    self.grasp_tries = 0
         215 +                    self._start_task(state)
         216 +                return self._noop()
         217 +            self.grasp_tries = 0
         218 +            self.held = g
         219 +            if g != self.cur_obj:
         220 +                # grabbed wrong object: treat it as an obstruction to clear
         221 +                self.tasks.insert(0, (g, 'clear'))
         222 +                self.cur_obj = g
         223 +            self._plan_place(state)
         224 +            return self._noop()
         225 +
         226 +        if ph == 'to_place':
         227 +            if not moved and self.prev_was_motion:
         228 +                self.stuck += 1
         229 +                if len(self.waypoints) <= self.descent_len and self.stuck >= 1:
         230 +                    self.waypoints = []
         231 +            a = self._track(state)
         232 +            if a is not None:
         233 +                self.prev_was_motion = True
         234 +                return a
         235 +            self.phase = 'open'
         236 +            self.prev_was_motion = False
         237 +            return self._noop(1.0)
         238 +
         239 +        if ph == 'open':
         240 +            if self._grasped_name(state) is None and state.get(self.robot, 'grasp_active') < 0.5:
         241 +                self.release_tries = 0
         242 +                self.tasks.pop(0)
         243 +                tool = self._tool(state)[:3, 3]
         244 +                self._set_path(state, [np.array([tool[0], tool[1], Z_SAFE])], self.wp_yaw)
         245 +                self.phase = 'retreat'
         246 +                self.prev_was_motion = False
         247 +                return self._noop(1.0)
         248 +            self.release_tries += 1
         249 +            tool = self._tool(state)[:3, 3]
         250 +            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw)
         251 +            self.descent_len = 1
         252 +            self.phase = 'to_place'
         253 +            self.prev_was_motion = False
         254 +            if self.release_tries > 20:
         255 +                self.release_tries = 0
         256 +                self._plan_place(state)
         257 +            return self._noop(1.0)
         258 +
         259 +        if ph == 'retreat':
         260 +            a = self._track(state)
         261 +            if a is not None:
         262 +                return a
         263 +            if self.tasks and self.tasks[0][1] == 'goal':
         264 +                # re-check obstructions (in case something moved)
         265 +                for n in self._blocking_obstructions(state):
         266 +                    if all(t[0] != n for t in self.tasks):
         267 +                        self.tasks.insert(0, (n, 'clear'))
         268 +            self._start_task(state)
         269 +            return self._noop()
         270 +
         271 +        return self._noop()
         272 +
         273 +    def _plan_place(self, state):
         274 +        name = self.cur_obj
         275 +        p, qo, h = self._pose(state, name)
         276 +        r = self.robot
         277 +        tf = _T([state.get(r, 'grasp_tf_x'), state.get(r, 'grasp_tf_y'), state.get(r, 'grasp_tf_z')],
         278 +                [state.get(r, 'grasp_tf_qx'), state.get(r, 'grasp_tf_qy'), state.get(r, 'grasp_tf_qz'),
         279 +                 state.get(r, 'grasp_tf_qw')])
         280 +        kind = self.tasks[0][1] if self.tasks and self.tasks[0][0] == name else 'clear'
         281 +        if kind == 'goal':
         282 +            rp, rh = self.region
         283 +            xy = rp[:2]
         284 +            surf = rp[2] + rh[2]
         285 +        else:
         286 +            xy = self._free_spot(state, name)
         287 +            surf = self.table_z
         288 +        # desired object pose: same orientation as now, at xy, resting on surface
         289 +        Tobj = _T([xy[0], xy[1], surf + h[2] + 0.001], qo)
         290 +        Ttool = Tobj @ np.linalg.inv(tf)
         291 +        tgt = Ttool[:3, 3]
         292 +        yaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
         293 +        # tool orientation is down_R(yaw); keep current yaw (grasp yaw)
         294 +        yaw = self.grasp_yaw
         295 +        tool = self._tool(state)[:3, 3]
         296 +        wps = [np.array([tool[0], tool[1], Z_SAFE]),
         297 +               np.array([tgt[0], tgt[1], Z_SAFE]),
         298 +               np.array([tgt[0], tgt[1], tgt[2] + 0.03])]
         299 +        self._set_path(state, wps, yaw)
         300 +        n_before = len(self.waypoints)
         301 +        # fine descent in 5mm steps
         302 +        cur = wps[-1]
         303 +        k = 0
         304 +        while cur[2] > tgt[2] - 0.004:
         305 +            cur = cur - np.array([0, 0, 0.005])
         306 +            self.waypoints.append(cur.copy())
         307 +            k += 1
         308 +        self.descent_len = k + 6
         309 +        self.phase = 'to_place'
         310 +        self.prev_was_motion = False
diff --git a/explore14.py b/explore14.py
index 19b5477..2f686bd 100644
--- a/explore14.py
+++ b/explore14.py
@@ -32,7 +32,13 @@ print('grasp',obs.get(R,'grasp_active'),obs.get(R,'finger_state'),np.round([obs.
   32     32  print('lift',move(bp+[0,0,0.2]), 'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
   33     33  print('move',move(bp+[0,-0.1,0.2]))
   34     34  print('down',move(bp+[0,-0.1,hz+dz+0.05]), 'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
   35        -a=np.zeros(11,dtype=np.float32); a[10]=1; obs,*_=env.step(a)
          35 +for k in range(3):
          36 +    a=np.zeros(11,dtype=np.float32); a[10]=1; obs,*_=env.step(a)
          37 +    print('open: grasp',obs.get(R,'grasp_active'),obs.get(R,'finger_state'))
          38 +print('down2',move(bp+[0,-0.1,hz+dz+float(sys.argv[3])]), 'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
          39 +for k in range(3):
          40 +    a=np.zeros(11,dtype=np.float32); a[10]=1; obs,*_=env.step(a)
          41 +    print('open: grasp',obs.get(R,'grasp_active'),obs.get(R,'finger_state'))
   36     42  print('open: grasp',obs.get(R,'grasp_active'),'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
   37     43  obs,*_=env.step(np.zeros(11,dtype=np.float32))
   38     44  print('block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..c3dceb4
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,32 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +def run(seed, verbose=False, max_steps=None):
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0 = time.time()
          11 +    ap.reset(obs, info)
          12 +    ms = max_steps or env.max_steps
          13 +    steps = 0
          14 +    term = False
          15 +    for steps in range(1, ms + 1):
          16 +        a = ap.get_action(obs)
          17 +        obs, r, term, trunc, info = env.step(a)
          18 +        if term or trunc:
          19 +            break
          20 +    dt = time.time() - t0
          21 +    nobs = len([n for n in obs.get_object_names() if n.startswith('obstruction')])
          22 +    env.close()
          23 +    return term, steps, dt, nobs, ap.phase
          24 +
          25 +if __name__ == '__main__':
          26 +    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          27 +    ok = 0
          28 +    for s in seeds:
          29 +        term, steps, dt, n, ph = run(s)
          30 +        ok += term
          31 +        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s nobs={n} phase={ph}', flush=True)
          32 +    print(f'{ok}/{len(seeds)}')
```

</details>

<a id="C004"></a>
### C004 · Grasp at top+0.02, retry yaws

Commit `f930731acf8cab7502deb3d418a9477388389300`; parents: 16f56456fec706f04e3a62eb21234a4f66190a7d. Recorded author date: 2026-09-30T20:07:50+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0189](01_timeline.md#E0189): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_f930731_approach.py) · [Exact all-file diff](evidence/diffs/C004_f930731.diff)

[Previous saved controller snapshot](evidence/versions/C003_16f5645_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c3cb75d..3500d44 100644
--- a/approach.py
+++ b/approach.py
@@ -74,7 +74,7 @@ class GeneratedApproach:
   74     74          self.last_q = None
   75     75          self.stuck = 0
   76     76          self.release_tries = 0
   77        -        self.grasp_tries = 0
          77 +        self.grasp_attempt = 0
   78     78          self.placed_spots = []
   79     79          self.prev_was_motion = False
   80     80          self.descent_len = 0
@@ -123,14 +123,16 @@ class GeneratedApproach:
  123    123          name, kind = self.tasks[0]
  124    124          p, q, h = self._pose(state, name)
  125    125          self.cur_obj = name
  126        -        self.grasp_yaw = self._pick_yaw(q)
         126 +        yaws = [0.0, np.pi / 2, np.pi / 4, -np.pi / 4]
         127 +        self.grasp_yaw = self._pick_yaw(q) + yaws[self.grasp_attempt % len(yaws)]
         128 +        self.grasp_yaw = (self.grasp_yaw + np.pi / 2) % np.pi - np.pi / 2
  127    129          top = p[2] + h[2]
  128    130          tool = self._tool(state)[:3, 3]
  129    131          wps = []
  130    132          if tool[2] < Z_SAFE - 0.01:
  131    133              wps.append(np.array([tool[0], tool[1], Z_SAFE]))
  132    134          wps.append(np.array([p[0], p[1], Z_SAFE]))
  133        -        wps.append(np.array([p[0], p[1], top + 0.005]))
         135 +        wps.append(np.array([p[0], p[1], top + 0.02]))
  134    136          self._set_path(state, wps, self.grasp_yaw)
  135    137          self.phase = 'to_grasp'
  136    138  
@@ -203,18 +205,11 @@ class GeneratedApproach:
  203    205          if ph == 'close':
  204    206              g = self._grasped_name(state)
  205    207              if g is None:
  206        -                # descend a bit more and retry
  207        -                self.grasp_tries += 1
  208        -                p, _, h = self._pose(state, self.cur_obj)
  209        -                tool = self._tool(state)[:3, 3]
  210        -                self._set_path(state, [np.array([p[0], p[1], tool[2] - 0.01])], self.grasp_yaw)
  211        -                self.phase = 'to_grasp'
  212        -                self.prev_was_motion = False
  213        -                if self.grasp_tries > 6:
  214        -                    self.grasp_tries = 0
  215        -                    self._start_task(state)
         208 +                # failed: retry with a different yaw
         209 +                self.grasp_attempt += 1
         210 +                self._start_task(state)
  216    211                  return self._noop()
  217        -            self.grasp_tries = 0
         212 +            self.grasp_attempt = 0
  218    213              self.held = g
  219    214              if g != self.cur_obj:
  220    215                  # grabbed wrong object: treat it as an obstruction to clear
diff --git a/debug_run.py b/debug_run.py
new file mode 100644
index 0000000..7b5a4d0
--- /dev/null
+++ b/debug_run.py
@@ -0,0 +1,23 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import tool_fk
           5 +seed=int(sys.argv[1]); ms=int(sys.argv[2]) if len(sys.argv)>2 else 300
           6 +env=make_env(); obs,info=env.reset(seed=seed)
           7 +for n in sorted(obs.get_object_names()):
           8 +    if n=='robot': continue
           9 +    o=obs.get_object_from_name(n); print(n,[round(obs.get(o,f),3) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z']])
          10 +ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
          11 +print('tasks',ap.tasks)
          12 +prev=None
          13 +for t in range(ms):
          14 +    a=ap.get_action(obs)
          15 +    q0=ap._q(obs)
          16 +    obs,r,term,trunc,info=env.step(a)
          17 +    moved=not np.allclose(ap._q(obs),q0,atol=1e-7)
          18 +    tool=ap._tool(obs)[:3,3]
          19 +    key=(ap.phase, moved)
          20 +    if key!=prev or t%25==0:
          21 +        print(t,ap.phase,'moved',moved,'tool',np.round(tool,3),'grip',a[10],'held',ap._grasped_name(obs),'nwp',len(ap.waypoints),'task',ap.tasks[0] if ap.tasks else None)
          22 +    prev=key
          23 +    if term: print('SUCCESS',t); break
diff --git a/explore15.py b/explore15.py
new file mode 100644
index 0000000..5f11697
--- /dev/null
+++ b/explore15.py
@@ -0,0 +1,38 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import tool_fk, tool_ik, down_R
           4 +env = make_env()
           5 +seed=0; name=sys.argv[1]; dz=float(sys.argv[2]); yaw=float(sys.argv[3])
           6 +jn=[f'joint_{i}' for i in range(1,8)]
           7 +def q_of(o): return np.array([o.get(R,f) for f in jn])
           8 +def goto(qt,g=0):
           9 +    global obs
          10 +    for _ in range(60):
          11 +        q=q_of(obs); d=qt-q
          12 +        d=(d+np.pi)%(2*np.pi)-np.pi
          13 +        if np.max(np.abs(d))<1e-5: return True
          14 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=g
          15 +        obs,r,te,tr,info=env.step(a)
          16 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          17 +    return False
          18 +def move(p, n=6):
          19 +    cur=tool_fk(q_of(obs),base)[:3,3]
          20 +    for k in range(1,n+1):
          21 +        qt,ok=tool_ik(q_of(obs),cur+(p-cur)*k/n,down_R(yaw),base)
          22 +        if not goto(qt): return False
          23 +    return True
          24 +obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot'); B=obs.get_object_from_name(name)
          25 +base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          26 +bp=np.array([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]); h=[obs.get(B,f) for f in ['half_extent_x','half_extent_y','half_extent_z']]
          27 +print(name,bp,h)
          28 +rows=[]
          29 +for dy in np.arange(-0.07,0.071,0.01):
          30 +    row=''
          31 +    for dx in np.arange(-0.07,0.071,0.01):
          32 +        obs,_=env.reset(seed=seed)
          33 +        move(bp+[dx,dy,0.12]); r=move(bp+[dx,dy,h[2]+dz])
          34 +        a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
          35 +        g=[n for n in sorted(obs.get_object_names()) if n!='robot' and obs.get(obs.get_object_from_name(n),'grasp_active')>0]
          36 +        row+=('.' if not g else ('G' if g[0]==name else g[0][0]))+('' if r else '!')+' '
          37 +    print(round(dy,2),row,flush=True)
          38 +env.close()
diff --git a/explore16.py b/explore16.py
new file mode 100644
index 0000000..19a6262
--- /dev/null
+++ b/explore16.py
@@ -0,0 +1,35 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import tool_fk, tool_ik, down_R
           4 +env = make_env()
           5 +seed=int(sys.argv[1]); name=sys.argv[2]; yaw=float(sys.argv[3])
           6 +jn=[f'joint_{i}' for i in range(1,8)]
           7 +def q_of(o): return np.array([o.get(R,f) for f in jn])
           8 +def goto(qt,g=0):
           9 +    global obs
          10 +    for _ in range(60):
          11 +        q=q_of(obs); d=qt-q
          12 +        d=(d+np.pi)%(2*np.pi)-np.pi
          13 +        if np.max(np.abs(d))<1e-5: return True
          14 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=g
          15 +        obs,r,te,tr,info=env.step(a)
          16 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          17 +    return False
          18 +def move(p, n=6):
          19 +    cur=tool_fk(q_of(obs),base)[:3,3]
          20 +    for k in range(1,n+1):
          21 +        qt,ok=tool_ik(q_of(obs),cur+(p-cur)*k/n,down_R(yaw),base)
          22 +        if not goto(qt): return False
          23 +    return True
          24 +obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot'); B=obs.get_object_from_name(name)
          25 +base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          26 +bp=np.array([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]); h=[obs.get(B,f) for f in ['half_extent_x','half_extent_y','half_extent_z']]
          27 +print(name,bp,h)
          28 +for dz in np.arange(0.05,-0.03,-0.004):
          29 +    obs,_=env.reset(seed=seed)
          30 +    move(bp+[0,0,h[2]+0.08]); r=move(bp+[0,0,h[2]+dz],n=20)
          31 +    tz=tool_fk(q_of(obs),base)[2,3]
          32 +    a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
          33 +    g=[n for n in sorted(obs.get_object_names()) if n!='robot' and obs.get(obs.get_object_from_name(n),'grasp_active')>0]
          34 +    print('dz',round(dz,3),'reached',r,'tool-top',round(tz-bp[2]-h[2],4),'grasp',g, round(obs.get(R,'finger_state'),3),flush=True)
          35 +env.close()
diff --git a/o16b.txt b/o16b.txt
new file mode 100644
index 0000000..aef1d61
--- /dev/null
+++ b/o16b.txt
@@ -0,0 +1,21 @@
           1 +obstruction1 [0.10313927 0.20900817 0.10099424] [0.018631789833307266, 0.015414612367749214, 0.0159942377358675]
           2 +dz 0.05 reached True tool-top 0.05 grasp [] 0.0
           3 +dz 0.046 reached True tool-top 0.046 grasp [] 0.0
           4 +dz 0.042 reached True tool-top 0.042 grasp [] 0.0
           5 +dz 0.038 reached True tool-top 0.038 grasp [] 0.0
           6 +dz 0.034 reached True tool-top 0.034 grasp ['obstruction1'] 0.55
           7 +dz 0.03 reached True tool-top 0.03 grasp ['obstruction1'] 0.55
           8 +dz 0.026 reached True tool-top 0.026 grasp [] 0.0
           9 +dz 0.022 reached True tool-top 0.022 grasp [] 0.0
          10 +dz 0.018 reached True tool-top 0.0181 grasp [] 0.0
          11 +dz 0.014 reached False tool-top 0.0174 grasp [] 0.0
          12 +dz 0.01 reached False tool-top 0.0206 grasp [] 0.0
          13 +dz 0.006 reached False tool-top 0.0209 grasp [] 0.0
          14 +dz 0.002 reached False tool-top 0.0177 grasp [] 0.0
          15 +dz -0.002 reached False tool-top 0.0185 grasp [] 0.0
          16 +dz -0.006 reached False tool-top 0.0198 grasp [] 0.0
          17 +dz -0.01 reached False tool-top 0.0215 grasp [] 0.0
          18 +dz -0.014 reached False tool-top 0.0189 grasp [] 0.0
          19 +dz -0.018 reached False tool-top 0.0212 grasp [] 0.0
          20 +dz -0.022 reached False tool-top 0.0188 grasp [] 0.0
          21 +dz -0.026 reached False tool-top 0.0217 grasp [] 0.0
```

</details>

<a id="C005"></a>
### C005 · Grasp height window based on object extent

Commit `88ec9d8c239ff896a9a2e25346bc68f10c8543a4`; parents: f930731acf8cab7502deb3d418a9477388389300. Recorded author date: 2026-09-30T20:08:54+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0200](01_timeline.md#E0200): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_88ec9d8_approach.py) · [Exact all-file diff](evidence/diffs/C005_88ec9d8.diff)

[Previous saved controller snapshot](evidence/versions/C004_f930731_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3500d44..d397b67 100644
--- a/approach.py
+++ b/approach.py
@@ -132,7 +132,10 @@ class GeneratedApproach:
  132    132          if tool[2] < Z_SAFE - 0.01:
  133    133              wps.append(np.array([tool[0], tool[1], Z_SAFE]))
  134    134          wps.append(np.array([p[0], p[1], Z_SAFE]))
  135        -        wps.append(np.array([p[0], p[1], top + 0.02]))
         135 +        lo = p[2] - h[2] + 0.044
         136 +        hi = top + 0.033
         137 +        gz = 0.5 * (lo + hi) if hi > lo else hi - 0.002
         138 +        wps.append(np.array([p[0], p[1], gz]))
  136    139          self._set_path(state, wps, self.grasp_yaw)
  137    140          self.phase = 'to_grasp'
  138    141  
diff --git a/explore16.py b/explore16.py
index 19a6262..2048cac 100644
--- a/explore16.py
+++ b/explore16.py
@@ -25,7 +25,7 @@ obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot'); B=obs.get_objec
   25     25  base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
   26     26  bp=np.array([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]); h=[obs.get(B,f) for f in ['half_extent_x','half_extent_y','half_extent_z']]
   27     27  print(name,bp,h)
   28        -for dz in np.arange(0.05,-0.03,-0.004):
          28 +for dz in np.arange(0.05,-0.005,-0.004):
   29     29      obs,_=env.reset(seed=seed)
   30     30      move(bp+[0,0,h[2]+0.08]); r=move(bp+[0,0,h[2]+dz],n=20)
   31     31      tz=tool_fk(q_of(obs),base)[2,3]
diff --git a/o16a.txt b/o16a.txt
new file mode 100644
index 0000000..3c8929a
--- /dev/null
+++ b/o16a.txt
@@ -0,0 +1,15 @@
           1 +obstruction0 [0.10343256 0.24800321 0.09505477] [0.019350724294781685, 0.01815853640437126, 0.010054769925773144]
           2 +dz 0.05 reached True tool-top 0.05 grasp [] 0.0
           3 +dz 0.046 reached True tool-top 0.046 grasp [] 0.0
           4 +dz 0.042 reached True tool-top 0.042 grasp [] 0.0
           5 +dz 0.038 reached True tool-top 0.038 grasp [] 0.0
           6 +dz 0.034 reached True tool-top 0.034 grasp ['obstruction0'] 0.47
           7 +dz 0.03 reached True tool-top 0.03 grasp ['obstruction0'] 0.47
           8 +dz 0.026 reached True tool-top 0.026 grasp ['obstruction0'] 0.47
           9 +dz 0.022 reached True tool-top 0.022 grasp ['obstruction0'] 0.47
          10 +dz 0.018 reached True tool-top 0.018 grasp [] 0.0
          11 +dz 0.014 reached True tool-top 0.014 grasp [] 0.0
          12 +dz 0.01 reached True tool-top 0.01 grasp [] 0.0
          13 +dz 0.006 reached False tool-top 0.0097 grasp [] 0.0
          14 +dz 0.002 reached False tool-top 0.0098 grasp [] 0.0
          15 +dz -0.002 reached False tool-top 0.0103 grasp [] 0.0
diff --git a/o16b.txt b/o16b.txt
index aef1d61..47d2b3a 100644
--- a/o16b.txt
+++ b/o16b.txt
@@ -1,21 +1,15 @@
    1        -obstruction1 [0.10313927 0.20900817 0.10099424] [0.018631789833307266, 0.015414612367749214, 0.0159942377358675]
           1 +target_block [0.33598167 0.17328143 0.1       ] [0.03128708153963089, 0.022474881261587143, 0.02500000037252903]
    2      2  dz 0.05 reached True tool-top 0.05 grasp [] 0.0
    3      3  dz 0.046 reached True tool-top 0.046 grasp [] 0.0
    4      4  dz 0.042 reached True tool-top 0.042 grasp [] 0.0
    5      5  dz 0.038 reached True tool-top 0.038 grasp [] 0.0
    6        -dz 0.034 reached True tool-top 0.034 grasp ['obstruction1'] 0.55
    7        -dz 0.03 reached True tool-top 0.03 grasp ['obstruction1'] 0.55
    8        -dz 0.026 reached True tool-top 0.026 grasp [] 0.0
    9        -dz 0.022 reached True tool-top 0.022 grasp [] 0.0
   10        -dz 0.018 reached True tool-top 0.0181 grasp [] 0.0
   11        -dz 0.014 reached False tool-top 0.0174 grasp [] 0.0
   12        -dz 0.01 reached False tool-top 0.0206 grasp [] 0.0
   13        -dz 0.006 reached False tool-top 0.0209 grasp [] 0.0
   14        -dz 0.002 reached False tool-top 0.0177 grasp [] 0.0
   15        -dz -0.002 reached False tool-top 0.0185 grasp [] 0.0
   16        -dz -0.006 reached False tool-top 0.0198 grasp [] 0.0
   17        -dz -0.01 reached False tool-top 0.0215 grasp [] 0.0
   18        -dz -0.014 reached False tool-top 0.0189 grasp [] 0.0
   19        -dz -0.018 reached False tool-top 0.0212 grasp [] 0.0
   20        -dz -0.022 reached False tool-top 0.0188 grasp [] 0.0
   21        -dz -0.026 reached False tool-top 0.0217 grasp [] 0.0
           6 +dz 0.034 reached True tool-top 0.0341 grasp ['target_block'] 0.25
           7 +dz 0.03 reached True tool-top 0.0301 grasp ['target_block'] 0.25
           8 +dz 0.026 reached True tool-top 0.0261 grasp ['target_block'] 0.25
           9 +dz 0.022 reached True tool-top 0.0221 grasp ['target_block'] 0.25
          10 +dz 0.018 reached True tool-top 0.018 grasp ['target_block'] 0.25
          11 +dz 0.014 reached True tool-top 0.014 grasp ['target_block'] 0.25
          12 +dz 0.01 reached True tool-top 0.01 grasp ['target_block'] 0.25
          13 +dz 0.006 reached True tool-top 0.006 grasp ['target_block'] 0.25
          14 +dz 0.002 reached True tool-top 0.002 grasp ['target_block'] 0.25
          15 +dz -0.002 reached True tool-top -0.002 grasp ['target_block'] 0.25
diff --git a/o16c.txt b/o16c.txt
new file mode 100644
index 0000000..f5b6e5b
--- /dev/null
+++ b/o16c.txt
@@ -0,0 +1,15 @@
           1 +obstruction0 [0.17032762 0.069209   0.09800124] [0.016574330627918243, 0.015622656792402267, 0.013001245446503162]
           2 +dz 0.05 reached True tool-top 0.05 grasp [] 0.0
           3 +dz 0.046 reached True tool-top 0.046 grasp [] 0.0
           4 +dz 0.042 reached True tool-top 0.0421 grasp [] 0.0
           5 +dz 0.038 reached True tool-top 0.038 grasp [] 0.0
           6 +dz 0.034 reached True tool-top 0.034 grasp ['obstruction0'] 0.52
           7 +dz 0.03 reached True tool-top 0.03 grasp ['obstruction0'] 0.52
           8 +dz 0.026 reached True tool-top 0.026 grasp ['obstruction0'] 0.52
           9 +dz 0.022 reached True tool-top 0.022 grasp ['obstruction0'] 0.52
          10 +dz 0.018 reached True tool-top 0.018 grasp ['obstruction0'] 0.52
          11 +dz 0.014 reached True tool-top 0.0141 grasp [] 0.0
          12 +dz 0.01 reached True tool-top 0.0101 grasp [] 0.0
          13 +dz 0.006 reached True tool-top 0.0061 grasp [] 0.0
          14 +dz 0.002 reached True tool-top 0.002 grasp [] 0.0
          15 +dz -0.002 reached True tool-top -0.002 grasp [] 0.0
```

</details>

<a id="C006"></a>
### C006 · Analytic-Jacobian IK with null-space posture regularization

Commit `8668a75e666d87983ae310cf34580699fc7b99cb`; parents: 88ec9d8c239ff896a9a2e25346bc68f10c8543a4. Recorded author date: 2026-09-30T20:13:52+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0242](01_timeline.md#E0242): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C006_8668a75.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..c7f2cd8
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,17 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import tool_fk, tool_ik, down_R
           5 +seed=int(sys.argv[1]); T=int(sys.argv[2])
           6 +env=make_env(); obs,info=env.reset(seed=seed)
           7 +ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           8 +for t in range(T):
           9 +    a=ap.get_action(obs); obs,*_=env.step(a)
          10 +q=ap._q(obs); base=ap._base(obs)
          11 +print('q',np.round(q,3)); print('wp',ap.waypoints[:2], 'yaw',ap.wp_yaw)
          12 +a=ap.get_action(obs); print('a',np.round(a,3))
          13 +qt,ok=tool_ik(q,ap.waypoints[0],down_R(ap.wp_yaw),base,iters=100); print('ik ok',ok,np.round(qt,3))
          14 +print('tool now',np.round(tool_fk(q,base),3))
          15 +# try smaller steps
          16 +for s in [0.5,0.25,0.1]:
          17 +    a2=a.copy(); a2[3:10]*=s; o2,*_=env.step(a2); print('scale',s,'moved',not np.allclose(ap._q(o2),q,atol=1e-7))
diff --git a/kin.py b/kin.py
index 53f14cb..a00201a 100644
--- a/kin.py
+++ b/kin.py
@@ -21,75 +21,68 @@ JOINTS = [
   21     21      _T((0, -0.10593, -0.00017505), (-H, 0, 0)),
   22     22  ]
   23     23  EE = _T((0, 0, -0.061525), (PI, 0, 0))
          24 +MOUNT = (0.12, 0.0, -0.0052)
          25 +TOOL = 0.12
          26 +HOME = np.array([0.0, -0.35, -np.pi, -2.5, 0.0, -0.87, np.pi / 2])
   24     27  
   25     28  def _rz(q):
   26     29      c, s = np.cos(q), np.sin(q)
   27     30      T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
   28     31  
   29        -def fk(q, base=(0, 0, 0), base_z=0.0, tool=0.0):
   30        -    """Return 4x4 world transform of end effector (+tool offset along EE z)."""
          32 +def mount_base(base):
   31     33      bx, by, br = base
   32        -    T = _rz(br); T[0, 3] = bx; T[1, 3] = by; T[2, 3] = base_z
          34 +    c, s = np.cos(br), np.sin(br)
          35 +    return (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
          36 +
          37 +def _chain(q, base):
          38 +    """Returns tool transform and list of (axis, origin) of joints in world."""
          39 +    bx, by, br = mount_base(base)
          40 +    T = _rz(br); T[0, 3] = bx; T[1, 3] = by; T[2, 3] = MOUNT[2]
          41 +    axes = []
   33     42      for Tj, qj in zip(JOINTS, q):
   34        -        T = T @ Tj @ _rz(qj)
          43 +        T = T @ Tj
          44 +        axes.append((T[:3, 2].copy(), T[:3, 3].copy()))
          45 +        T = T @ _rz(qj)
   35     46      T = T @ EE
   36        -    if tool:
   37        -        Tt = np.eye(4); Tt[2, 3] = tool; T = T @ Tt
   38        -    return T
          47 +    Tt = np.eye(4); Tt[2, 3] = TOOL
          48 +    return T @ Tt, axes
   39     49  
   40        -def pose_err(T, p, R):
   41        -    ep = p - T[:3, 3]
   42        -    Re = R @ T[:3, :3].T
   43        -    # axis-angle of Re
   44        -    ang = np.arccos(np.clip((np.trace(Re) - 1) / 2, -1, 1))
   45        -    if ang < 1e-9:
   46        -        eo = np.zeros(3)
   47        -    else:
   48        -        v = np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
   49        -        s = np.sin(ang)
   50        -        eo = v / (2 * s) * ang if s > 1e-6 else np.zeros(3)
   51        -    return np.concatenate([ep, eo])
          50 +def tool_fk(q, base):
          51 +    return _chain(q, base)[0]
          52 +
          53 +def _rot_err(Rc, Rd):
          54 +    Re = Rd @ Rc.T
          55 +    v = 0.5 * np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
          56 +    return v
   52     57  
   53        -def ik(q0, p, R, base, base_z=0.0, tool=0.0, iters=200, wo=0.3, tol=1e-4):
          58 +def tool_ik(q0, p, R, base, iters=60, tol=1e-5, q_nom=None, k_null=0.3):
   54     59      q = np.array(q0, dtype=float)
          60 +    if q_nom is None:
          61 +        q_nom = HOME
   55     62      for it in range(iters):
   56        -        T = fk(q, base, base_z, tool)
   57        -        e = pose_err(T, p, R)
   58        -        e[3:] *= wo
   59        -        if np.linalg.norm(e) < tol:
          63 +        T, axes = _chain(q, base)
          64 +        e = np.concatenate([p - T[:3, 3], _rot_err(T[:3, :3], R)])
          65 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
   60     66              return q, True
   61     67          J = np.zeros((6, 7))
   62        -        h = 1e-6
   63        -        for j in range(7):
   64        -            dq = q.copy(); dq[j] += h
   65        -            e2 = pose_err(fk(dq, base, base_z, tool), p, R); e2[3:] *= wo
   66        -            J[:, j] = (e - e2) / h
   67        -        lam = 1e-3
   68        -        dq = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
   69        -        n = np.linalg.norm(dq)
   70        -        if n > 0.3: dq *= 0.3 / n
          68 +        pt = T[:3, 3]
          69 +        for j, (z, o) in enumerate(axes):
          70 +            J[:3, j] = np.cross(z, pt - o)
          71 +            J[3:, j] = z
          72 +        JJt = J @ J.T + 1e-6 * np.eye(6)
          73 +        Jp = J.T @ np.linalg.inv(JJt)
          74 +        dq = Jp @ e
          75 +        dn = (q_nom - q + np.pi) % (2 * np.pi) - np.pi
          76 +        dq += (np.eye(7) - Jp @ J) @ (k_null * dn)
          77 +        n = np.max(np.abs(dq))
          78 +        if n > 0.3:
          79 +            dq *= 0.3 / n
   71     80          q = q + dq
   72        -    return q, False
          81 +    T, _ = _chain(q, base)
          82 +    ok = np.linalg.norm(p - T[:3, 3]) < 1e-3
          83 +    return q, ok
   73     84  
   74     85  def down_R(yaw):
   75        -    # EE z axis pointing down, x axis at yaw
   76     86      c, s = np.cos(yaw), np.sin(yaw)
   77     87      x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
   78     88      return np.stack([x, y, z], axis=1)
   79        -
   80        -MOUNT = (0.12, 0.0, -0.0052)
   81        -TOOL = 0.12
   82        -
   83        -def tool_fk(q, base):
   84        -    bx, by, br = base
   85        -    c, s = np.cos(br), np.sin(br)
   86        -    b = (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
   87        -    return fk(q, b, MOUNT[2], TOOL)
   88        -
   89        -def mount_base(base):
   90        -    bx, by, br = base
   91        -    c, s = np.cos(br), np.sin(br)
   92        -    return (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
   93        -
   94        -def tool_ik(q0, p, R, base, **kw):
   95        -    return ik(q0, p, R, mount_base(base), MOUNT[2], TOOL, **kw)
diff --git a/par_test.sh b/par_test.sh
new file mode 100755
index 0000000..e8fa170
--- /dev/null
+++ b/par_test.sh
@@ -0,0 +1,4 @@
           1 +#!/bin/bash
           2 +# usage: par_test.sh start end nproc
           3 +S=$1; E=$2; P=${3:-8}
           4 +seq $S $((E-1)) | xargs -P $P -I{} sh -c '/opt/robocode-strict/bin/python test_approach.py {} $(({}+1)) 2>&1 | head -1'
diff --git a/res1.txt b/res1.txt
new file mode 100644
index 0000000..875b7af
--- /dev/null
+++ b/res1.txt
@@ -0,0 +1,40 @@
           1 +seed 1: success=True steps=124 time=39.5s nobs=1 phase=open
           2 +seed 3: success=True steps=112 time=34.0s nobs=2 phase=open
           3 +seed 9: success=True steps=130 time=39.8s nobs=1 phase=open
           4 +seed 7: success=True steps=118 time=35.5s nobs=2 phase=open
           5 +seed 11: success=True steps=52 time=14.9s nobs=0 phase=open
           6 +seed 0: success=True steps=184 time=55.1s nobs=2 phase=open
           7 +seed 4: success=True steps=176 time=59.6s nobs=2 phase=open
           8 +seed 8: success=True steps=181 time=60.3s nobs=2 phase=open
           9 +seed 5: success=True steps=212 time=64.0s nobs=2 phase=open
          10 +seed 14: success=True steps=50 time=14.8s nobs=0 phase=open
          11 +seed 10: success=True steps=120 time=49.5s nobs=2 phase=open
          12 +seed 12: success=True steps=125 time=45.0s nobs=1 phase=open
          13 +seed 15: success=True steps=108 time=39.9s nobs=2 phase=open
          14 +seed 16: success=True steps=122 time=35.7s nobs=1 phase=open
          15 +seed 21: success=True steps=60 time=13.7s nobs=0 phase=open
          16 +seed 19: success=True steps=108 time=35.0s nobs=1 phase=open
          17 +seed 18: success=True steps=130 time=45.3s nobs=2 phase=open
          18 +seed 13: success=True steps=216 time=73.6s nobs=2 phase=open
          19 +seed 23: success=True steps=54 time=20.6s nobs=0 phase=open
          20 +seed 24: success=True steps=62 time=23.1s nobs=1 phase=open
          21 +seed 17: success=True steps=181 time=66.8s nobs=2 phase=open
          22 +seed 22: success=True steps=113 time=41.2s nobs=2 phase=open
          23 +seed 27: success=True steps=62 time=23.1s nobs=0 phase=open
          24 +seed 29: success=True steps=47 time=17.0s nobs=2 phase=open
          25 +seed 20: success=True steps=191 time=70.9s nobs=2 phase=open
          26 +seed 30: success=True steps=63 time=21.6s nobs=0 phase=open
          27 +seed 25: success=True steps=135 time=50.7s nobs=1 phase=open
          28 +seed 6: success=False steps=1000 time=174.5s nobs=1 phase=open
          29 +seed 34: success=True steps=62 time=20.2s nobs=0 phase=open
          30 +seed 28: success=True steps=135 time=51.0s nobs=1 phase=open
          31 +seed 35: success=True steps=67 time=21.1s nobs=0 phase=open
          32 +seed 31: success=True steps=116 time=43.7s nobs=1 phase=open
          33 +seed 37: success=True steps=58 time=14.5s nobs=0 phase=open
          34 +seed 38: success=True steps=56 time=11.2s nobs=0 phase=open
          35 +seed 32: success=True steps=173 time=46.2s nobs=2 phase=open
          36 +seed 36: success=True steps=120 time=26.6s nobs=1 phase=open
          37 +seed 33: success=True steps=170 time=45.5s nobs=2 phase=open
          38 +seed 39: success=True steps=206 time=20.0s nobs=2 phase=open
          39 +seed 2: success=False steps=1000 time=214.6s nobs=2 phase=to_place
          40 +seed 26: success=False steps=1000 time=82.9s nobs=2 phase=to_place
diff --git a/t_ik.py b/t_ik.py
new file mode 100644
index 0000000..fe9e0fe
--- /dev/null
+++ b/t_ik.py
@@ -0,0 +1,8 @@
           1 +import numpy as np, time
           2 +from kin import tool_fk, tool_ik, down_R, HOME
           3 +base=(-0.12,0,0)
           4 +q=HOME.copy(); t=time.time(); n=0
           5 +for p in [(0.15,0.2,0.13),(0.45,-0.3,0.12),(0.3,0,0.3),(0.12,-0.35,0.12),(0.5,0.3,0.15)]:
           6 +    qt,ok=tool_ik(q,np.array(p),down_R(0.3),base); n+=1
           7 +    print(p,ok,np.round(qt,2), np.round(tool_fk(qt,base)[:3,3],4))
           8 +print('time per ik',(time.time()-t)/n)
```

</details>

<a id="C007"></a>
### C007 · Free spot: nearest clear spot in reachable band

Commit `85d185ee49e866ea33960b0a6f3b68273421ce21`; parents: 8668a75e666d87983ae310cf34580699fc7b99cb. Recorded author date: 2026-09-30T20:15:45+02:00.

File roles (automatic): policy.

- [E0252](01_timeline.md#E0252): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_85d185e_approach.py) · [Exact all-file diff](evidence/diffs/C007_85d185e.diff)

[Previous saved controller snapshot](evidence/versions/C005_88ec9d8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d397b67..601b67f 100644
--- a/approach.py
+++ b/approach.py
@@ -91,30 +91,30 @@ class GeneratedApproach:
   91     91          return out
   92     92  
   93     93      def _free_spot(self, state, name):
   94        -        """Pick a spot on the table far from region, target block, other objects."""
   95        -        _, _, h = self._pose(state, name)
          94 +        """Pick a table spot clear of region/other objects, close to the object."""
          95 +        p0, _, h = self._pose(state, name)
   96     96          others = []
   97     97          for n in self.names:
   98        -            if n == name:
          98 +            if n == name or n == 'target_region':
   99     99                  continue
  100    100              p, _, hh = self._pose(state, n)
  101    101              others.append((p[:2], hh[:2]))
  102    102          rp, rh = self.region
  103        -        best, best_score = None, -1e9
  104        -        for x in np.linspace(0.12, 0.48, 13):
  105        -            for y in np.linspace(-0.32, 0.32, 17):
         103 +        best, best_score = None, 1e9
         104 +        fb, fb_score = None, -1e9
         105 +        for x in np.linspace(0.2, 0.5, 16):
         106 +            for y in np.linspace(-0.34, 0.34, 35):
  106    107                  c = np.array([x, y])
  107        -                score = 1e9
         108 +                clear = np.max(np.abs(c - rp[:2]) - rh[:2] - h[:2]) - 0.04
  108    109                  for p, hh in others:
  109        -                    d = np.max(np.abs(c - p) - hh - h[:2])
  110        -                    score = min(score, d)
  111        -                d = np.max(np.abs(c - rp[:2]) - rh[:2] - h[:2]) - 0.03
  112        -                score = min(score, d)
  113        -                # prefer closer to robot-ish center for reachability
  114        -                score -= 0.02 * np.hypot(x - 0.3, y)
  115        -                if score > best_score:
  116        -                    best, best_score = c, score
  117        -        return best
         110 +                    clear = min(clear, np.max(np.abs(c - p) - hh - h[:2]) - 0.03)
         111 +                if clear > fb_score:
         112 +                    fb, fb_score = c, clear
         113 +                if clear >= 0:
         114 +                    score = np.linalg.norm(c - p0[:2]) + 0.3 * abs(y) * 0 
         115 +                    if score < best_score:
         116 +                        best, best_score = c, score
         117 +        return best if best is not None else fb
  118    118  
  119    119      def _start_task(self, state):
  120    120          if not self.tasks:
```

</details>

<a id="C008"></a>
### C008 · Rewrite: finger-aware yaw/free-spot, joint-path lookahead, adaptive transit height

Commit `62bb1aef960fbda12acdf45c9296bb87044f5566`; parents: 85d185ee49e866ea33960b0a6f3b68273421ce21. Recorded author date: 2026-09-30T20:29:55+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0363](01_timeline.md#E0363): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_62bb1ae_approach.py) · [Exact all-file diff](evidence/diffs/C008_62bb1ae.diff)

[Previous saved controller snapshot](evidence/versions/C007_85d185e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 601b67f..cc0b211 100644
--- a/approach.py
+++ b/approach.py
@@ -1,12 +1,20 @@
    1      1  """Obstruction3D approach: clear obstructions off the target region, then place
    2        -the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py)."""
           2 +the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py).
           3 +
           4 +Empirical facts (black-box probing):
           5 +- Arm mount is +0.12m along base x; the grasp/tool frame is 0.12m past the flange.
           6 +- Gripper fingers lie along the tool x axis, extending ~0.07m from the centre and
           7 +  ~0.035m below the tool frame.  Robot/held object collisions reject a step.
           8 +- Grasp (close) succeeds when tool z in [bottom+0.044, top+0.033] over the object.
           9 +- Release (open) succeeds only if the held object rests within a few mm of a surface.
          10 +"""
    3     11  import numpy as np
    4     12  from kin import tool_fk, tool_ik, down_R
    5     13  
    6     14  JN = [f'joint_{i}' for i in range(1, 8)]
    7        -Z_SAFE = 0.30          # tool height for transit
    8     15  STEP = 0.2             # max joint delta per step
    9        -SEG = 0.03             # cartesian interpolation segment length
          16 +FINGER_DOWN = 0.036    # fingertips below tool frame
          17 +F_OFF, F_HL, F_HW = 0.046, 0.024, 0.013   # finger centre offset, half length, half width
   10     18  
   11     19  
   12     20  def _q2R(x, y, z, w):
@@ -25,6 +33,28 @@ def _yaw_of_quat(q):
   25     33      return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
   26     34  
   27     35  
          36 +def _wrap(a):
          37 +    return (a + np.pi) % (2 * np.pi) - np.pi
          38 +
          39 +
          40 +def _aabb_of_rect(c, hx, hy, yaw):
          41 +    c_, s_ = abs(np.cos(yaw)), abs(np.sin(yaw))
          42 +    return np.array(c), np.array([c_ * hx + s_ * hy, s_ * hx + c_ * hy])
          43 +
          44 +
          45 +def _gap(c1, h1, c2, h2):
          46 +    """Signed separation between two AABBs (positive = apart)."""
          47 +    return np.max(np.abs(np.asarray(c1) - np.asarray(c2)) - np.asarray(h1) - np.asarray(h2))
          48 +
          49 +
          50 +def _finger_boxes(xy, yaw):
          51 +    d = np.array([np.cos(yaw), np.sin(yaw)])
          52 +    out = []
          53 +    for sgn in (1, -1):
          54 +        out.append(_aabb_of_rect(np.asarray(xy) + sgn * F_OFF * d, F_HL, F_HW, yaw))
          55 +    return out
          56 +
          57 +
   28     58  class GeneratedApproach:
   29     59      def __init__(self, action_space, observation_space, primitives):
   30     60          self.action_space = action_space
@@ -40,6 +70,12 @@ class GeneratedApproach:
   40     70                  np.array([state.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]),
   41     71                  np.array([state.get(o, f) for f in ('half_extent_x', 'half_extent_y', 'half_extent_z')]))
   42     72  
          73 +    def _box(self, state, name):
          74 +        """(centre_xy, half_xy AABB, bottom z, top z)"""
          75 +        p, q, h = self._pose(state, name)
          76 +        c, hh = _aabb_of_rect(p[:2], h[0], h[1], _yaw_of_quat(q))
          77 +        return c, hh, p[2] - h[2], p[2] + h[2]
          78 +
   43     79      def _q(self, state):
   44     80          return np.array([state.get(self.robot, f) for f in JN])
   45     81  
@@ -56,6 +92,14 @@ class GeneratedApproach:
   56     92                  return n
   57     93          return None
   58     94  
          95 +    def _max_top(self, state, exclude=()):
          96 +        t = self.table_z
          97 +        for n in self.names:
          98 +            if n in exclude:
          99 +                continue
         100 +            t = max(t, self._box(state, n)[3])
         101 +        return t
         102 +
   59    103      # ------------------------------------------------------------ planning
   60    104      def reset(self, state, info):
   61    105          self.robot = state.get_object_from_name('robot')
@@ -64,58 +108,104 @@ class GeneratedApproach:
   64    108          rp, _, rh = self._pose(state, 'target_region')
   65    109          self.table_z = rp[2] - rh[2]
   66    110          self.region = (rp, rh)
   67        -        self.tasks = []  # list of (obj_name, kind)
   68        -        for n in self._blocking_obstructions(state):
   69        -            self.tasks.append((n, 'clear'))
         111 +        self.tasks = [(n, 'clear') for n in self._blocking_obstructions(state)]
   70    112          self.tasks.append(('target_block', 'goal'))
   71    113          self.phase = None
   72        -        self.waypoints = []
   73        -        self.wp_yaw = 0.0
         114 +        self.qpath = []
   74    115          self.last_q = None
         116 +        self.last_a = None
         117 +        self.blocked = False
   75    118          self.stuck = 0
         119 +        self.descent_len = 0
   76    120          self.release_tries = 0
   77    121          self.grasp_attempt = 0
   78        -        self.placed_spots = []
   79        -        self.prev_was_motion = False
   80        -        self.descent_len = 0
         122 +        self.total_fail = 0
         123 +        self.final_grip = 0.0
         124 +        self.wp_yaw = 0.0
   81    125          self._start_task(state)
   82    126  
   83        -    def _blocking_obstructions(self, state, margin=0.005):
         127 +    def _blocking_obstructions(self, state, margin=0.003):
   84    128          rp, rh = self.region
   85    129          out = []
   86    130          for n in self.obstructions:
   87        -            p, _, h = self._pose(state, n)
   88        -            if (abs(p[0] - rp[0]) < rh[0] + h[0] + margin and
   89        -                    abs(p[1] - rp[1]) < rh[1] + h[1] + margin):
         131 +            c, hh, _, _ = self._box(state, n)
         132 +            if _gap(c, hh, rp[:2], rh[:2]) < margin:
   90    133                  out.append(n)
   91    134          return out
   92    135  
   93        -    def _free_spot(self, state, name):
   94        -        """Pick a table spot clear of region/other objects, close to the object."""
   95        -        p0, _, h = self._pose(state, name)
         136 +    def _finger_clearance(self, state, xy, yaw, tip_z, exclude):
         137 +        """Min xy gap between finger boxes and objects whose top is above tip_z."""
         138 +        clear = 1.0
         139 +        fbs = _finger_boxes(xy, yaw)
         140 +        for n in self.names:
         141 +            if n in exclude:
         142 +                continue
         143 +            c, hh, bot, top = self._box(state, n)
         144 +            if top < tip_z - 0.002:
         145 +                continue
         146 +            for fc, fh in fbs:
         147 +                clear = min(clear, _gap(fc, fh, c, hh))
         148 +        return clear
         149 +
         150 +    def _choose_yaw(self, state, name, kind, attempt):
         151 +        p, q, h = self._pose(state, name)
         152 +        oy = _yaw_of_quat(q)
         153 +        gz = self._grasp_z(p, h)
         154 +        cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
         155 +        scored = []
         156 +        for i, y in enumerate(cands):
         157 +            y = _wrap(2 * y) / 2  # modulo pi
         158 +            c = self._finger_clearance(state, p[:2], y, gz - FINGER_DOWN, exclude=(name,))
         159 +            if kind == 'goal':
         160 +                rp, rh = self.region
         161 +                surf = rp[2] + rh[2]
         162 +                tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
         163 +                c = min(c, self._finger_clearance(state, rp[:2], y, tip,
         164 +                                                  exclude=(name, 'target_region')))
         165 +            scored.append((min(c, 0.02) - 0.001 * i, y))
         166 +        scored.sort(key=lambda t: -t[0])
         167 +        return scored[attempt % len(scored)][1]
         168 +
         169 +    def _grasp_z(self, p, h):
         170 +        lo = p[2] - h[2] + 0.045
         171 +        hi = p[2] + h[2] + 0.032
         172 +        return 0.5 * (lo + hi) if hi > lo else hi - 0.001
         173 +
         174 +    def _free_spot(self, state, name, yaw, hold_off):
         175 +        """Pick a table spot clear of region/other objects (object + fingers)."""
         176 +        p0, _, _ = self._pose(state, name)
         177 +        c0, h, _, _ = self._box(state, name)
   96    178          others = []
   97    179          for n in self.names:
   98        -            if n == name or n == 'target_region':
         180 +            if n == name:
   99    181                  continue
  100        -            p, _, hh = self._pose(state, n)
  101        -            others.append((p[:2], hh[:2]))
         182 +            others.append(self._box(state, n))
  102    183          rp, rh = self.region
         184 +        tip = self.table_z + 0.001 + hold_off - FINGER_DOWN
  103    185          best, best_score = None, 1e9
  104    186          fb, fb_score = None, -1e9
  105    187          for x in np.linspace(0.2, 0.5, 16):
  106    188              for y in np.linspace(-0.34, 0.34, 35):
  107    189                  c = np.array([x, y])
  108        -                clear = np.max(np.abs(c - rp[:2]) - rh[:2] - h[:2]) - 0.04
  109        -                for p, hh in others:
  110        -                    clear = min(clear, np.max(np.abs(c - p) - hh - h[:2]) - 0.03)
         190 +                clear = _gap(c, h, rp[:2], rh[:2]) - 0.03
         191 +                fbs = _finger_boxes(c, yaw)
         192 +                for oc, oh, bot, top in others:
         193 +                    clear = min(clear, _gap(c, h, oc, oh) - 0.02)
         194 +                    if top > tip - 0.002:
         195 +                        for fc, fh in fbs:
         196 +                            clear = min(clear, _gap(fc, fh, oc, oh) - 0.008)
  111    197                  if clear > fb_score:
  112    198                      fb, fb_score = c, clear
  113    199                  if clear >= 0:
  114        -                    score = np.linalg.norm(c - p0[:2]) + 0.3 * abs(y) * 0 
         200 +                    score = np.linalg.norm(c - p0[:2])
  115    201                      if score < best_score:
  116    202                          best, best_score = c, score
  117    203          return best if best is not None else fb
  118    204  
         205 +    def _transit_z(self, state, hold_off=0.0, exclude=()):
         206 +        top = self._max_top(state, exclude)
         207 +        return max(top + 0.03 + max(FINGER_DOWN, hold_off), 0.2)
         208 +
  119    209      def _start_task(self, state):
  120    210          if not self.tasks:
  121    211              self.phase = 'done'
@@ -123,58 +213,65 @@ class GeneratedApproach:
  123    213          name, kind = self.tasks[0]
  124    214          p, q, h = self._pose(state, name)
  125    215          self.cur_obj = name
  126        -        yaws = [0.0, np.pi / 2, np.pi / 4, -np.pi / 4]
  127        -        self.grasp_yaw = self._pick_yaw(q) + yaws[self.grasp_attempt % len(yaws)]
  128        -        self.grasp_yaw = (self.grasp_yaw + np.pi / 2) % np.pi - np.pi / 2
  129        -        top = p[2] + h[2]
         216 +        self.grasp_yaw = self._choose_yaw(state, name, kind, self.grasp_attempt)
         217 +        gz = self._grasp_z(p, h)
         218 +        zt = self._transit_z(state)
  130    219          tool = self._tool(state)[:3, 3]
  131    220          wps = []
  132        -        if tool[2] < Z_SAFE - 0.01:
  133        -            wps.append(np.array([tool[0], tool[1], Z_SAFE]))
  134        -        wps.append(np.array([p[0], p[1], Z_SAFE]))
  135        -        lo = p[2] - h[2] + 0.044
  136        -        hi = top + 0.033
  137        -        gz = 0.5 * (lo + hi) if hi > lo else hi - 0.002
         221 +        if tool[2] < zt - 0.01:
         222 +            wps.append(np.array([tool[0], tool[1], zt]))
         223 +        wps.append(np.array([p[0], p[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]))
  138    224          wps.append(np.array([p[0], p[1], gz]))
  139        -        self._set_path(state, wps, self.grasp_yaw)
         225 +        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0)
  140    226          self.phase = 'to_grasp'
  141    227  
  142        -    def _pick_yaw(self, q):
  143        -        y = _yaw_of_quat(q)
  144        -        # choose equivalent yaw (mod pi/2) closest to 0
  145        -        y = (y + np.pi / 4) % (np.pi / 2) - np.pi / 4
  146        -        return y
  147        -
  148        -    def _set_path(self, state, wps, yaw):
  149        -        cur = self._tool(state)[:3, 3]
  150        -        pts = []
         228 +    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01):
         229 +        """Cartesian waypoints -> dense joint path (IK warm-started)."""
         230 +        q = self._q(state)
         231 +        base = self._base(state)
         232 +        cur = tool_fk(q, base)[:3, 3]
         233 +        R = down_R(yaw)
         234 +        path = []
         235 +        qc = q.copy()
  151    236          for w in wps:
  152    237              d = np.linalg.norm(w - cur)
  153        -            n = max(1, int(np.ceil(d / SEG)))
         238 +            n = max(1, int(np.ceil(d / res)))
  154    239              for k in range(1, n + 1):
  155        -                pts.append(cur + (w - cur) * k / n)
         240 +                pt = cur + (w - cur) * k / n
         241 +                qn, ok = tool_ik(qc, pt, R, base, iters=40)
         242 +                qn = qc + _wrap(qn - qc)
         243 +                path.append(qn)
         244 +                qc = qn
  156    245              cur = w
  157        -        self.waypoints = pts
         246 +        self.qpath = path
  158    247          self.wp_yaw = yaw
         248 +        self.final_grip = final_grip
  159    249          self.stuck = 0
  160    250  
  161    251      # ------------------------------------------------------------ control
  162        -    def _track(self, state, grip=0.0):
  163        -        """Return action moving toward current waypoint; None if path complete."""
         252 +    def _track(self, state):
         253 +        """Step along the precomputed joint path; None if done."""
  164    254          q = self._q(state)
  165        -        base = self._base(state)
  166        -        while self.waypoints:
  167        -            wp = self.waypoints[0]
  168        -            qt, ok = tool_ik(q, wp, down_R(self.wp_yaw), base, iters=100)
  169        -            d = (qt - q + np.pi) % (2 * np.pi) - np.pi
  170        -            if np.max(np.abs(d)) < 1e-4:
  171        -                self.waypoints.pop(0)
  172        -                continue
  173        -            a = np.zeros(11, dtype=np.float32)
  174        -            a[3:10] = np.clip(d, -STEP, STEP)
  175        -            a[10] = grip
  176        -            return a
  177        -        return None
         255 +        while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
         256 +            self.qpath.pop(0)
         257 +        if not self.qpath:
         258 +            return None
         259 +        k = -1
         260 +        for i, qp in enumerate(self.qpath):
         261 +            if np.max(np.abs(_wrap(qp - q))) <= STEP:
         262 +                k = i
         263 +            else:
         264 +                break
         265 +        a = np.zeros(11, dtype=np.float32)
         266 +        if k >= 0:
         267 +            d = _wrap(self.qpath[k] - q)
         268 +            a[3:10] = d
         269 +            if k == len(self.qpath) - 1:
         270 +                a[10] = self.final_grip
         271 +        else:
         272 +            d = _wrap(self.qpath[0] - q)
         273 +            a[3:10] = d * (STEP / np.max(np.abs(d)))
         274 +        return a
  178    275  
  179    276      def _noop(self, grip=0.0):
  180    277          a = np.zeros(11, dtype=np.float32); a[10] = grip
@@ -183,92 +280,121 @@ class GeneratedApproach:
  183    280      def get_action(self, state):
  184    281          q = self._q(state)
  185    282          moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
         283 +        attempted = self.last_a is not None and np.any(np.abs(self.last_a[3:10]) > 1e-9)
         284 +        self.blocked = attempted and not moved
  186    285          self.last_q = q.copy()
  187        -        a = self._policy(state, moved)
  188        -        return np.asarray(a, dtype=np.float32)
         286 +        try:
         287 +            a = self._policy(state)
         288 +        except Exception:
         289 +            a = self._noop()
         290 +        a = np.asarray(a, dtype=np.float32).copy()
         291 +        a[:10] = np.clip(a[:10], -STEP, STEP)
         292 +        a[10] = np.clip(a[10], -1, 1)
         293 +        self.last_a = a
         294 +        return a
  189    295  
  190        -    def _policy(self, state, moved):
         296 +    def _policy(self, state):
  191    297          ph = self.phase
  192    298          if ph == 'done':
         299 +            if self._grasped_name(state) is None and self.tasks:
         300 +                self._start_task(state)
  193    301              return self._noop()
  194    302  
  195    303          if ph == 'to_grasp':
  196        -            if not moved and self.prev_was_motion:
         304 +            g = self._grasped_name(state)
         305 +            if g is not None:
         306 +                return self._on_grasped(state, g)
         307 +            if self.blocked:
  197    308                  self.stuck += 1
  198        -            if self.stuck >= 2:
  199        -                self.waypoints = []  # blocked: try grasping here
         309 +                if self.stuck >= 2:
         310 +                    self.qpath = []
  200    311              a = self._track(state)
  201    312              if a is not None:
  202        -                self.prev_was_motion = True
  203    313                  return a
  204    314              self.phase = 'close'
  205        -            self.prev_was_motion = False
  206    315              return self._noop(-1.0)
  207    316  
  208    317          if ph == 'close':
  209    318              g = self._grasped_name(state)
  210    319              if g is None:
  211        -                # failed: retry with a different yaw
  212    320                  self.grasp_attempt += 1
         321 +                self.total_fail += 1
  213    322                  self._start_task(state)
  214        -                return self._noop()
  215        -            self.grasp_attempt = 0
  216        -            self.held = g
  217        -            if g != self.cur_obj:
  218        -                # grabbed wrong object: treat it as an obstruction to clear
  219        -                self.tasks.insert(0, (g, 'clear'))
  220        -                self.cur_obj = g
  221        -            self._plan_place(state)
  222        -            return self._noop()
         323 +                return self._track(state) if self.qpath else self._noop()
         324 +            return self._on_grasped(state, g)
  223    325  
  224    326          if ph == 'to_place':
  225        -            if not moved and self.prev_was_motion:
         327 +            if self._grasped_name(state) is None:
         328 +                return self._on_released(state)
         329 +            if self.blocked:
  226    330                  self.stuck += 1
  227        -                if len(self.waypoints) <= self.descent_len and self.stuck >= 1:
  228        -                    self.waypoints = []
         331 +                if len(self.qpath) <= self.descent_len:
         332 +                    self.qpath = []
         333 +                elif self.stuck >= 3:
         334 +                    self._plan_place(state, replan=True)
  229    335              a = self._track(state)
  230    336              if a is not None:
  231        -                self.prev_was_motion = True
  232    337                  return a
  233    338              self.phase = 'open'
  234        -            self.prev_was_motion = False
  235    339              return self._noop(1.0)
  236    340  
  237    341          if ph == 'open':
  238        -            if self._grasped_name(state) is None and state.get(self.robot, 'grasp_active') < 0.5:
  239        -                self.release_tries = 0
  240        -                self.tasks.pop(0)
  241        -                tool = self._tool(state)[:3, 3]
  242        -                self._set_path(state, [np.array([tool[0], tool[1], Z_SAFE])], self.wp_yaw)
  243        -                self.phase = 'retreat'
  244        -                self.prev_was_motion = False
  245        -                return self._noop(1.0)
         342 +            if self._grasped_name(state) is None:
         343 +                return self._on_released(state)
  246    344              self.release_tries += 1
  247    345              tool = self._tool(state)[:3, 3]
  248        -            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw)
  249        -            self.descent_len = 1
         346 +            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw, final_grip=1.0)
         347 +            self.descent_len = 2
  250    348              self.phase = 'to_place'
  251        -            self.prev_was_motion = False
  252        -            if self.release_tries > 20:
         349 +            if self.release_tries > 12:
  253    350                  self.release_tries = 0
  254        -                self._plan_place(state)
  255        -            return self._noop(1.0)
         351 +                self._plan_place(state, replan=True)
         352 +            a = self._track(state)
         353 +            return a if a is not None else self._noop(1.0)
  256    354  
  257    355          if ph == 'retreat':
         356 +            if self.blocked:
         357 +                self.stuck += 1
         358 +                if self.stuck >= 2:
         359 +                    self.qpath = []
  258    360              a = self._track(state)
  259    361              if a is not None:
  260    362                  return a
  261        -            if self.tasks and self.tasks[0][1] == 'goal':
  262        -                # re-check obstructions (in case something moved)
  263        -                for n in self._blocking_obstructions(state):
  264        -                    if all(t[0] != n for t in self.tasks):
  265        -                        self.tasks.insert(0, (n, 'clear'))
  266        -            self._start_task(state)
  267        -            return self._noop()
         363 +            self._next_task(state)
         364 +            a = self._track(state) if self.phase == 'to_grasp' else None
         365 +            return a if a is not None else self._noop()
  268    366  
  269    367          return self._noop()
  270    368  
  271        -    def _plan_place(self, state):
         369 +    def _on_grasped(self, state, g):
         370 +        self.grasp_attempt = 0
         371 +        if g != self.cur_obj:
         372 +            self.tasks.insert(0, (g, 'clear'))
         373 +            self.cur_obj = g
         374 +        self._plan_place(state)
         375 +        a = self._track(state)
         376 +        return a if a is not None else self._noop()
         377 +
         378 +    def _on_released(self, state):
         379 +        self.release_tries = 0
         380 +        name, kind = self.tasks.pop(0) if self.tasks else (None, None)
         381 +        if kind == 'goal':
         382 +            self.phase = 'done'
         383 +            return self._noop()
         384 +        tool = self._tool(state)[:3, 3]
         385 +        self._set_path(state, [tool + np.array([0, 0, 0.03])], self.wp_yaw)
         386 +        self.phase = 'retreat'
         387 +        a = self._track(state)
         388 +        return a if a is not None else self._noop()
         389 +
         390 +    def _next_task(self, state):
         391 +        if self.tasks and self.tasks[0][1] == 'goal':
         392 +            for n in self._blocking_obstructions(state):
         393 +                if all(t[0] != n for t in self.tasks):
         394 +                    self.tasks.insert(0, (n, 'clear'))
         395 +        self._start_task(state)
         396 +
         397 +    def _plan_place(self, state, replan=False):
  272    398          name = self.cur_obj
  273    399          p, qo, h = self._pose(state, name)
  274    400          r = self.robot
@@ -276,33 +402,42 @@ class GeneratedApproach:
  276    402                  [state.get(r, 'grasp_tf_qx'), state.get(r, 'grasp_tf_qy'), state.get(r, 'grasp_tf_qz'),
  277    403                   state.get(r, 'grasp_tf_qw')])
  278    404          kind = self.tasks[0][1] if self.tasks and self.tasks[0][0] == name else 'clear'
         405 +        Ttool_now = self._tool(state)
         406 +        hold_off = Ttool_now[2, 3] - (p[2] - h[2])   # tool height above held-object bottom
         407 +        yaw = np.arctan2(Ttool_now[1, 0], Ttool_now[0, 0])
  279    408          if kind == 'goal':
  280    409              rp, rh = self.region
  281    410              xy = rp[:2]
  282    411              surf = rp[2] + rh[2]
  283    412          else:
  284        -            xy = self._free_spot(state, name)
         413 +            xy = self._free_spot(state, name, yaw, hold_off)
         414 +            if replan:
         415 +                xy = xy + np.random.uniform(-0.03, 0.03, 2)
  285    416              surf = self.table_z
  286        -        # desired object pose: same orientation as now, at xy, resting on surface
  287    417          Tobj = _T([xy[0], xy[1], surf + h[2] + 0.001], qo)
  288    418          Ttool = Tobj @ np.linalg.inv(tf)
  289    419          tgt = Ttool[:3, 3]
  290        -        yaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
  291        -        # tool orientation is down_R(yaw); keep current yaw (grasp yaw)
  292        -        yaw = self.grasp_yaw
  293        -        tool = self._tool(state)[:3, 3]
  294        -        wps = [np.array([tool[0], tool[1], Z_SAFE]),
  295        -               np.array([tgt[0], tgt[1], Z_SAFE]),
  296        -               np.array([tgt[0], tgt[1], tgt[2] + 0.03])]
  297        -        self._set_path(state, wps, yaw)
  298        -        n_before = len(self.waypoints)
  299        -        # fine descent in 5mm steps
  300        -        cur = wps[-1]
  301        -        k = 0
  302        -        while cur[2] > tgt[2] - 0.004:
  303        -            cur = cur - np.array([0, 0, 0.005])
  304        -            self.waypoints.append(cur.copy())
  305        -            k += 1
  306        -        self.descent_len = k + 6
         420 +        tyaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
         421 +        zt = self._transit_z(state, hold_off, exclude=(name,))
         422 +        tool = Ttool_now[:3, 3]
         423 +        wps = []
         424 +        if tool[2] < zt - 0.005:
         425 +            wps.append(np.array([tool[0], tool[1], zt]))
         426 +        wps += [np.array([tgt[0], tgt[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]),
         427 +                np.array([tgt[0], tgt[1], tgt[2] + 0.015])]
         428 +        self._set_path(state, wps, tyaw)
         429 +        n_before = len(self.qpath)
         430 +        self._append_descent(state, tgt, tyaw)
         431 +        self.descent_len = len(self.qpath) - n_before + 2
         432 +        self.final_grip = 1.0
  307    433          self.phase = 'to_place'
  308        -        self.prev_was_motion = False
         434 +
         435 +    def _append_descent(self, state, tgt, yaw):
         436 +        base = self._base(state)
         437 +        qc = self.qpath[-1] if self.qpath else self._q(state)
         438 +        R = down_R(yaw)
         439 +        for dz in (0.008, 0.003, 0.0):
         440 +            qn, ok = tool_ik(qc, tgt + np.array([0, 0, dz]), R, base, iters=40)
         441 +            qn = qc + _wrap(qn - qc)
         442 +            self.qpath.append(qn)
         443 +            qc = qn
diff --git a/dbg3.py b/dbg3.py
new file mode 100644
index 0000000..1a7f503
--- /dev/null
+++ b/dbg3.py
@@ -0,0 +1,24 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import tool_fk, tool_ik, down_R
           5 +seed=int(sys.argv[1]); T=int(sys.argv[2])
           6 +env=make_env(); obs,info=env.reset(seed=seed)
           7 +ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           8 +for t in range(T):
           9 +    a=ap.get_action(obs); obs,*_=env.step(a)
          10 +q=ap._q(obs); base=ap._base(obs)
          11 +print('phase',ap.phase,'q',np.round(q,3),'tool',np.round(tool_fk(q,base)[:3,3],3),'yaw',ap.wp_yaw)
          12 +print('finger',obs.get(ap.robot,'finger_state'),'grasp',obs.get(ap.robot,'grasp_active'))
          13 +for n in ap.names:
          14 +    p,_,h=ap._pose(obs,n); print(n,np.round(p,3),np.round(h,3))
          15 +for j in range(7):
          16 +    for s in [0.01,-0.01]:
          17 +        a=np.zeros(11,dtype=np.float32); a[3+j]=s; o2,*_=env.step(a)
          18 +        mv=not np.allclose(ap._q(o2),q,atol=1e-7)
          19 +        if mv:
          20 +            a[3+j]=-s; obs,*_=env.step(a)
          21 +        print(j,s,mv,end=' | ')
          22 +print()
          23 +for g in [1,-1,0]:
          24 +    a=np.zeros(11,dtype=np.float32); a[3]=0.01; a[10]=g; o2,*_=env.step(a); print('grip',g,'moved',not np.allclose(ap._q(o2),q,atol=1e-7))
diff --git a/debug_run.py b/debug_run.py
index 7b5a4d0..eadc615 100644
--- a/debug_run.py
+++ b/debug_run.py
@@ -3,7 +3,8 @@ from env_client import make_env
    3      3  from approach import GeneratedApproach
    4      4  from kin import tool_fk
    5      5  seed=int(sys.argv[1]); ms=int(sys.argv[2]) if len(sys.argv)>2 else 300
    6        -env=make_env(); obs,info=env.reset(seed=seed)
           6 +env=make_env(); cnt=int(sys.argv[3]) if len(sys.argv)>3 else None
           7 +obs,info=env.reset(seed=seed,options={'object_count':cnt} if cnt else None)
    7      8  for n in sorted(obs.get_object_names()):
    8      9      if n=='robot': continue
    9     10      o=obs.get_object_from_name(n); print(n,[round(obs.get(o,f),3) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z']])
diff --git a/explore17.py b/explore17.py
new file mode 100644
index 0000000..4bb33da
--- /dev/null
+++ b/explore17.py
@@ -0,0 +1,42 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +from kin import tool_fk, tool_ik, down_R
           4 +env = make_env()
           5 +seed=int(sys.argv[1]); name=sys.argv[2]; yaw=float(sys.argv[3])
           6 +jn=[f'joint_{i}' for i in range(1,8)]
           7 +def q_of(o): return np.array([o.get(R,f) for f in jn])
           8 +def goto(qt,g=0):
           9 +    global obs
          10 +    for _ in range(60):
          11 +        q=q_of(obs); d=qt-q
          12 +        d=(d+np.pi)%(2*np.pi)-np.pi
          13 +        if np.max(np.abs(d))<1e-5: return True
          14 +        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=g
          15 +        obs,r,te,tr,info=env.step(a)
          16 +        if np.allclose(q_of(obs),q,atol=1e-7): return False
          17 +    return False
          18 +def move(p, n=6):
          19 +    cur=tool_fk(q_of(obs),base)[:3,3]
          20 +    for k in range(1,n+1):
          21 +        qt,ok=tool_ik(q_of(obs),cur+(p-cur)*k/n,down_R(yaw),base)
          22 +        if not goto(qt): return False
          23 +    return True
          24 +obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot'); B=obs.get_object_from_name(name)
          25 +base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
          26 +bp=np.array([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]); h=np.array([obs.get(B,f) for f in ['half_extent_x','half_extent_y','half_extent_z']])
          27 +print(name,bp,h)
          28 +for dz in [0.02, 0.0]:
          29 +  for dirn in [(0,1),(0,-1),(1,0),(-1,0)]:
          30 +    dv=np.array([dirn[0],dirn[1],0.0])
          31 +    obs,_=env.reset(seed=seed)
          32 +    start=bp+dv*0.14+[0,0,h[2]+dz]
          33 +    move(start+[0,0,0.08]); r=move(start)
          34 +    s=0.14
          35 +    while s>-0.14 and r:
          36 +        qt,ok=tool_ik(q_of(obs),bp+dv*(s-0.002)+[0,0,h[2]+dz],down_R(yaw),base)
          37 +        if not goto(qt): break
          38 +        s-=0.002
          39 +    # contact offset in direction; subtract object half extent
          40 +    he=h[0] if dirn[0] else h[1]
          41 +    print('dz',dz,'dir',dirn,'start ok',r,'blocked at offset',round(s,3),'gap from face',round(s-he,3))
          42 +env.close()
diff --git a/o17a.txt b/o17a.txt
new file mode 100644
index 0000000..1db84e2
--- /dev/null
+++ b/o17a.txt
@@ -0,0 +1,9 @@
           1 +target_block [ 0.34410098 -0.09747366  0.1       ] [0.01908568 0.02798267 0.025     ]
           2 +dz 0.02 dir (0, 1) start ok True blocked at offset -0.14 gap from face -0.168
           3 +dz 0.02 dir (0, -1) start ok True blocked at offset -0.14 gap from face -0.168
           4 +dz 0.02 dir (1, 0) start ok True blocked at offset 0.076 gap from face 0.057
           5 +dz 0.02 dir (-1, 0) start ok True blocked at offset 0.076 gap from face 0.057
           6 +dz 0.0 dir (0, 1) start ok True blocked at offset -0.14 gap from face -0.168
           7 +dz 0.0 dir (0, -1) start ok True blocked at offset -0.14 gap from face -0.168
           8 +dz 0.0 dir (1, 0) start ok True blocked at offset 0.086 gap from face 0.067
           9 +dz 0.0 dir (-1, 0) start ok True blocked at offset 0.086 gap from face 0.067
diff --git a/o17b.txt b/o17b.txt
new file mode 100644
index 0000000..1f6144a
--- /dev/null
+++ b/o17b.txt
@@ -0,0 +1,9 @@
           1 +target_block [ 0.34410098 -0.09747366  0.1       ] [0.01908568 0.02798267 0.025     ]
           2 +dz 0.02 dir (0, 1) start ok True blocked at offset 0.086 gap from face 0.058
           3 +dz 0.02 dir (0, -1) start ok True blocked at offset 0.086 gap from face 0.058
           4 +dz 0.02 dir (1, 0) start ok True blocked at offset -0.14 gap from face -0.159
           5 +dz 0.02 dir (-1, 0) start ok True blocked at offset -0.14 gap from face -0.159
           6 +dz 0.0 dir (0, 1) start ok True blocked at offset 0.094 gap from face 0.066
           7 +dz 0.0 dir (0, -1) start ok True blocked at offset 0.094 gap from face 0.066
           8 +dz 0.0 dir (1, 0) start ok True blocked at offset -0.14 gap from face -0.159
           9 +dz 0.0 dir (-1, 0) start ok True blocked at offset -0.14 gap from face -0.159
diff --git a/par_test.sh b/par_test.sh
index e8fa170..7f6e64f 100755
--- a/par_test.sh
+++ b/par_test.sh
@@ -1,4 +1,4 @@
    1      1  #!/bin/bash
    2        -# usage: par_test.sh start end nproc
    3        -S=$1; E=$2; P=${3:-8}
    4        -seq $S $((E-1)) | xargs -P $P -I{} sh -c '/opt/robocode-strict/bin/python test_approach.py {} $(({}+1)) 2>&1 | head -1'
           2 +# usage: par_test.sh start end nproc [count]
           3 +S=$1; E=$2; P=${3:-8}; export CNT=$4
           4 +seq $S $((E-1)) | xargs -P $P -I{} sh -c '/opt/robocode-strict/bin/python test_approach.py {} $(({}+1)) $CNT 2>&1 | head -1'
diff --git a/res2.txt b/res2.txt
new file mode 100644
index 0000000..362a82a
--- /dev/null
+++ b/res2.txt
@@ -0,0 +1,100 @@
           1 +seed 3: success=True steps=100 time=36.1s nobs=2 phase=open
           2 +seed 7: success=True steps=105 time=34.5s nobs=2 phase=open
           3 +seed 1: success=True steps=118 time=36.6s nobs=1 phase=open
           4 +seed 6: success=True steps=120 time=33.9s nobs=1 phase=open
           5 +seed 0: success=True steps=141 time=43.7s nobs=2 phase=open
           6 +seed 4: success=True steps=149 time=60.4s nobs=2 phase=open
           7 +seed 11: success=True steps=53 time=14.4s nobs=0 phase=open
           8 +seed 2: success=True steps=163 time=51.0s nobs=2 phase=open
           9 +seed 5: success=True steps=184 time=57.1s nobs=2 phase=open
          10 +seed 9: success=True steps=96 time=32.7s nobs=1 phase=open
          11 +seed 10: success=True steps=97 time=35.1s nobs=2 phase=open
          12 +seed 12: success=True steps=94 time=30.0s nobs=1 phase=open
          13 +seed 14: success=True steps=49 time=15.9s nobs=0 phase=open
          14 +seed 8: success=True steps=156 time=55.6s nobs=2 phase=open
          15 +seed 16: success=True steps=95 time=27.6s nobs=1 phase=open
          16 +seed 15: success=True steps=91 time=33.8s nobs=2 phase=open
          17 +seed 21: success=True steps=61 time=16.1s nobs=0 phase=open
          18 +seed 18: success=True steps=110 time=31.8s nobs=2 phase=open
          19 +seed 19: success=True steps=96 time=31.9s nobs=1 phase=open
          20 +seed 17: success=True steps=148 time=48.4s nobs=2 phase=open
          21 +seed 23: success=True steps=55 time=21.3s nobs=0 phase=open
          22 +seed 20: success=True steps=150 time=49.0s nobs=2 phase=open
          23 +seed 24: success=True steps=63 time=23.7s nobs=1 phase=open
          24 +seed 22: success=True steps=104 time=36.6s nobs=2 phase=open
          25 +seed 27: success=True steps=63 time=22.1s nobs=0 phase=open
          26 +seed 25: success=True steps=128 time=36.4s nobs=1 phase=open
          27 +seed 29: success=True steps=48 time=16.6s nobs=2 phase=open
          28 +seed 30: success=True steps=64 time=17.6s nobs=0 phase=open
          29 +seed 26: success=True steps=119 time=40.7s nobs=2 phase=open
          30 +seed 28: success=True steps=129 time=41.5s nobs=1 phase=open
          31 +seed 34: success=True steps=61 time=20.0s nobs=0 phase=open
          32 +seed 31: success=True steps=108 time=36.3s nobs=1 phase=open
          33 +seed 35: success=True steps=69 time=21.5s nobs=0 phase=open
          34 +seed 36: success=True steps=92 time=27.1s nobs=1 phase=open
          35 +seed 37: success=True steps=59 time=20.5s nobs=0 phase=open
          36 +seed 38: success=True steps=57 time=19.5s nobs=0 phase=open
          37 +seed 32: success=True steps=137 time=55.3s nobs=2 phase=open
          38 +seed 33: success=True steps=130 time=53.9s nobs=2 phase=open
          39 +seed 42: success=True steps=65 time=17.4s nobs=0 phase=open
          40 +seed 13: success=False steps=1000 time=162.5s nobs=2 phase=retreat
          41 +seed 40: success=True steps=99 time=36.5s nobs=1 phase=open
          42 +seed 41: success=True steps=99 time=31.4s nobs=1 phase=open
          43 +seed 43: success=True steps=96 time=30.1s nobs=1 phase=open
          44 +seed 48: success=True steps=46 time=10.9s nobs=0 phase=open
          45 +seed 44: success=True steps=106 time=37.2s nobs=2 phase=open
          46 +seed 47: success=True steps=52 time=20.9s nobs=0 phase=open
          47 +seed 49: success=True steps=60 time=19.1s nobs=0 phase=open
          48 +seed 46: success=True steps=98 time=36.2s nobs=1 phase=open
          49 +seed 39: success=True steps=180 time=77.4s nobs=2 phase=open
          50 +seed 54: success=True steps=58 time=13.5s nobs=0 phase=open
          51 +seed 51: success=True steps=96 time=29.7s nobs=1 phase=open
          52 +seed 50: success=True steps=156 time=45.1s nobs=2 phase=open
          53 +seed 56: success=True steps=94 time=21.7s nobs=1 phase=open
          54 +seed 57: success=True steps=52 time=13.8s nobs=0 phase=open
          55 +seed 53: success=True steps=159 time=46.3s nobs=2 phase=open
          56 +seed 58: success=True steps=63 time=26.1s nobs=1 phase=open
          57 +seed 55: success=True steps=141 time=50.1s nobs=2 phase=open
          58 +seed 52: success=True steps=174 time=67.3s nobs=2 phase=open
          59 +seed 60: success=True steps=57 time=24.7s nobs=0 phase=open
          60 +seed 61: success=True steps=109 time=33.8s nobs=1 phase=open
          61 +seed 62: success=True steps=94 time=32.7s nobs=1 phase=open
          62 +seed 63: success=True steps=105 time=28.7s nobs=1 phase=open
          63 +seed 65: success=True steps=71 time=23.1s nobs=0 phase=open
          64 +seed 64: success=True steps=107 time=33.8s nobs=1 phase=open
          65 +seed 45: success=False steps=1000 time=140.1s nobs=2 phase=retreat
          66 +seed 59: success=True steps=173 time=70.1s nobs=2 phase=open
          67 +seed 68: success=True steps=51 time=22.7s nobs=1 phase=open
          68 +seed 69: success=True steps=54 time=22.0s nobs=0 phase=open
          69 +seed 66: success=True steps=138 time=49.0s nobs=2 phase=open
          70 +seed 74: success=True steps=52 time=15.5s nobs=0 phase=open
          71 +seed 70: success=True steps=123 time=38.4s nobs=1 phase=open
          72 +seed 67: success=True steps=135 time=55.0s nobs=2 phase=open
          73 +seed 75: success=True steps=98 time=28.4s nobs=1 phase=open
          74 +seed 77: success=True steps=58 time=17.5s nobs=0 phase=open
          75 +seed 73: success=True steps=139 time=42.8s nobs=2 phase=open
          76 +seed 79: success=True steps=51 time=22.1s nobs=0 phase=open
          77 +seed 71: success=True steps=162 time=65.5s nobs=2 phase=open
          78 +seed 76: success=True steps=131 time=50.0s nobs=1 phase=open
          79 +seed 78: success=True steps=98 time=41.4s nobs=2 phase=open
          80 +seed 81: success=True steps=57 time=25.4s nobs=0 phase=open
          81 +seed 72: success=True steps=185 time=78.4s nobs=2 phase=open
          82 +seed 83: success=True steps=94 time=32.3s nobs=2 phase=open
          83 +seed 84: success=True steps=97 time=28.5s nobs=1 phase=open
          84 +seed 82: success=True steps=146 time=53.3s nobs=2 phase=open
          85 +seed 87: success=True steps=107 time=30.9s nobs=1 phase=open
          86 +seed 88: success=True steps=104 time=33.3s nobs=1 phase=open
          87 +seed 85: success=True steps=145 time=48.7s nobs=2 phase=open
          88 +seed 80: success=True steps=183 time=81.9s nobs=2 phase=open
          89 +seed 90: success=True steps=89 time=30.6s nobs=1 phase=open
          90 +seed 92: success=True steps=98 time=29.7s nobs=1 phase=open
          91 +seed 94: success=True steps=62 time=23.3s nobs=0 phase=open
          92 +seed 91: success=True steps=113 time=45.0s nobs=2 phase=open
          93 +seed 89: success=True steps=142 time=59.6s nobs=2 phase=open
          94 +seed 95: success=True steps=102 time=29.8s nobs=1 phase=open
          95 +seed 97: success=True steps=59 time=15.3s nobs=0 phase=open
          96 +seed 98: success=True steps=99 time=17.5s nobs=1 phase=open
          97 +seed 96: success=True steps=150 time=37.7s nobs=2 phase=open
          98 +seed 99: success=True steps=140 time=18.8s nobs=2 phase=open
          99 +seed 93: success=False steps=1000 time=60.7s nobs=2 phase=retreat
         100 +seed 86: success=False steps=1000 time=150.7s nobs=2 phase=to_place
diff --git a/t_count.py b/t_count.py
new file mode 100644
index 0000000..06d9117
--- /dev/null
+++ b/t_count.py
@@ -0,0 +1,7 @@
           1 +from env_client import make_env
           2 +env=make_env()
           3 +for opt in [{'object_count':5},{'num_obstructions':5}]:
           4 +    try:
           5 +        obs,info=env.reset(seed=0,options=opt); print(opt, info, len(obs.get_object_names()))
           6 +    except Exception as e: print(opt,'ERR',str(e)[:200])
           7 +env.close()
diff --git a/test_approach.py b/test_approach.py
index c3dceb4..d238650 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -3,9 +3,9 @@ import numpy as np
    3      3  from env_client import make_env
    4      4  from approach import GeneratedApproach
    5      5  
    6        -def run(seed, verbose=False, max_steps=None):
           6 +def run(seed, verbose=False, max_steps=None, count=None):
    7      7      env = make_env()
    8        -    obs, info = env.reset(seed=seed)
           8 +    obs, info = env.reset(seed=seed, options={'object_count': count} if count else None)
    9      9      ap = GeneratedApproach(env.action_space, env.observation_space, {})
   10     10      t0 = time.time()
   11     11      ap.reset(obs, info)
@@ -24,9 +24,10 @@ def run(seed, verbose=False, max_steps=None):
   24     24  
   25     25  if __name__ == '__main__':
   26     26      seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          27 +    count = int(sys.argv[3]) if len(sys.argv) > 3 else None
   27     28      ok = 0
   28     29      for s in seeds:
   29        -        term, steps, dt, n, ph = run(s)
          30 +        term, steps, dt, n, ph = run(s, count=count)
   30     31          ok += term
   31     32          print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s nobs={n} phase={ph}', flush=True)
   32     33      print(f'{ok}/{len(seeds)}')
```

</details>

<a id="C009"></a>
### C009 · Fix path tracking truncation; open gripper while approaching grasp

Commit `996e3753706e275754e93bc2b623d842ae39ba84`; parents: 62bb1aef960fbda12acdf45c9296bb87044f5566. Recorded author date: 2026-09-30T20:37:13+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0438](01_timeline.md#E0438): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_996e375_approach.py) · [Exact all-file diff](evidence/diffs/C009_996e375.diff)

[Previous saved controller snapshot](evidence/versions/C008_62bb1ae_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index cc0b211..987d3b0 100644
--- a/approach.py
+++ b/approach.py
@@ -246,6 +246,7 @@ class GeneratedApproach:
  246    246          self.qpath = path
  247    247          self.wp_yaw = yaw
  248    248          self.final_grip = final_grip
         249 +        self.travel_grip = 1.0 if final_grip < 0 else 0.0
  249    250          self.stuck = 0
  250    251  
  251    252      # ------------------------------------------------------------ control
@@ -264,10 +265,11 @@ class GeneratedApproach:
  264    265                  break
  265    266          a = np.zeros(11, dtype=np.float32)
  266    267          if k >= 0:
  267        -            d = _wrap(self.qpath[k] - q)
         268 +            self.qpath = self.qpath[k:]
         269 +            k = 0
         270 +            d = _wrap(self.qpath[0] - q)
  268    271              a[3:10] = d
  269        -            if k == len(self.qpath) - 1:
  270        -                a[10] = self.final_grip
         272 +            a[10] = self.travel_grip
  271    273          else:
  272    274              d = _wrap(self.qpath[0] - q)
  273    275              a[3:10] = d * (STEP / np.max(np.abs(d)))
diff --git a/dbg_old.py b/dbg_old.py
new file mode 100644
index 0000000..86726ba
--- /dev/null
+++ b/dbg_old.py
@@ -0,0 +1,11 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +from old_approach import GeneratedApproach
           4 +env=make_env(); obs,info=env.reset(seed=0)
           5 +ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           6 +for t in range(80):
           7 +    a=ap.get_action(obs)
           8 +    if a[10]<-0.5:
           9 +        print(t,'close q',np.round(ap._q(obs),4),'tool',np.round(ap._tool(obs)[:3,:],3).tolist())
          10 +    obs,*_=env.step(a)
          11 +    if a[10]<-0.5: print(' grasped',ap._grasped_name(obs)); 
diff --git a/dbg_rw.py b/dbg_rw.py
new file mode 100644
index 0000000..c9a06d0
--- /dev/null
+++ b/dbg_rw.py
@@ -0,0 +1,15 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +cnt=int(sys.argv[3]) if len(sys.argv)>3 else None
           5 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]),options={'object_count':cnt} if cnt else None)
           6 +ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           7 +print('tasks',ap.tasks)
           8 +last=None
           9 +for t in range(int(sys.argv[2])):
          10 +    a=ap.get_action(obs)
          11 +    obs,r,term,tr,_=env.step(a)
          12 +    key=(ap.phase, ap._grasped_name(obs), ap.tasks[0] if ap.tasks else None)
          13 +    if key!=last or ap.blocked:
          14 +        print(t,ap.phase,len(ap.qpath),np.round(ap._tool(obs)[:3,3],3),'blk',ap.blocked,'grip',a[10],key[1],key[2]); last=key
          15 +    if term: print('DONE',t+1);break
diff --git a/old_approach.py b/old_approach.py
new file mode 100644
index 0000000..601b67f
--- /dev/null
+++ b/old_approach.py
@@ -0,0 +1,308 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place
           2 +the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py)."""
           3 +import numpy as np
           4 +from kin import tool_fk, tool_ik, down_R
           5 +
           6 +JN = [f'joint_{i}' for i in range(1, 8)]
           7 +Z_SAFE = 0.30          # tool height for transit
           8 +STEP = 0.2             # max joint delta per step
           9 +SEG = 0.03             # cartesian interpolation segment length
          10 +
          11 +
          12 +def _q2R(x, y, z, w):
          13 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          14 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          15 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          16 +
          17 +
          18 +def _T(p, q):
          19 +    M = np.eye(4); M[:3, :3] = _q2R(*q); M[:3, 3] = p
          20 +    return M
          21 +
          22 +
          23 +def _yaw_of_quat(q):
          24 +    x, y, z, w = q
          25 +    return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
          26 +
          27 +
          28 +class GeneratedApproach:
          29 +    def __init__(self, action_space, observation_space, primitives):
          30 +        self.action_space = action_space
          31 +        self.observation_space = observation_space
          32 +
          33 +    # ------------------------------------------------------------ helpers
          34 +    def _obj(self, state, name):
          35 +        return state.get_object_from_name(name)
          36 +
          37 +    def _pose(self, state, name):
          38 +        o = self._obj(state, name)
          39 +        return (np.array([state.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')]),
          40 +                np.array([state.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]),
          41 +                np.array([state.get(o, f) for f in ('half_extent_x', 'half_extent_y', 'half_extent_z')]))
          42 +
          43 +    def _q(self, state):
          44 +        return np.array([state.get(self.robot, f) for f in JN])
          45 +
          46 +    def _base(self, state):
          47 +        return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
          48 +                state.get(self.robot, 'pos_base_rot'))
          49 +
          50 +    def _tool(self, state):
          51 +        return tool_fk(self._q(state), self._base(state))
          52 +
          53 +    def _grasped_name(self, state):
          54 +        for n in self.names:
          55 +            if state.get(self._obj(state, n), 'grasp_active') > 0.5:
          56 +                return n
          57 +        return None
          58 +
          59 +    # ------------------------------------------------------------ planning
          60 +    def reset(self, state, info):
          61 +        self.robot = state.get_object_from_name('robot')
          62 +        self.names = sorted(n for n in state.get_object_names() if n != 'robot')
          63 +        self.obstructions = sorted(n for n in self.names if n.startswith('obstruction'))
          64 +        rp, _, rh = self._pose(state, 'target_region')
          65 +        self.table_z = rp[2] - rh[2]
          66 +        self.region = (rp, rh)
          67 +        self.tasks = []  # list of (obj_name, kind)
          68 +        for n in self._blocking_obstructions(state):
          69 +            self.tasks.append((n, 'clear'))
          70 +        self.tasks.append(('target_block', 'goal'))
          71 +        self.phase = None
          72 +        self.waypoints = []
          73 +        self.wp_yaw = 0.0
          74 +        self.last_q = None
          75 +        self.stuck = 0
          76 +        self.release_tries = 0
          77 +        self.grasp_attempt = 0
          78 +        self.placed_spots = []
          79 +        self.prev_was_motion = False
          80 +        self.descent_len = 0
          81 +        self._start_task(state)
          82 +
          83 +    def _blocking_obstructions(self, state, margin=0.005):
          84 +        rp, rh = self.region
          85 +        out = []
          86 +        for n in self.obstructions:
          87 +            p, _, h = self._pose(state, n)
          88 +            if (abs(p[0] - rp[0]) < rh[0] + h[0] + margin and
          89 +                    abs(p[1] - rp[1]) < rh[1] + h[1] + margin):
          90 +                out.append(n)
          91 +        return out
          92 +
          93 +    def _free_spot(self, state, name):
          94 +        """Pick a table spot clear of region/other objects, close to the object."""
          95 +        p0, _, h = self._pose(state, name)
          96 +        others = []
          97 +        for n in self.names:
          98 +            if n == name or n == 'target_region':
          99 +                continue
         100 +            p, _, hh = self._pose(state, n)
         101 +            others.append((p[:2], hh[:2]))
         102 +        rp, rh = self.region
         103 +        best, best_score = None, 1e9
         104 +        fb, fb_score = None, -1e9
         105 +        for x in np.linspace(0.2, 0.5, 16):
         106 +            for y in np.linspace(-0.34, 0.34, 35):
         107 +                c = np.array([x, y])
         108 +                clear = np.max(np.abs(c - rp[:2]) - rh[:2] - h[:2]) - 0.04
         109 +                for p, hh in others:
         110 +                    clear = min(clear, np.max(np.abs(c - p) - hh - h[:2]) - 0.03)
         111 +                if clear > fb_score:
         112 +                    fb, fb_score = c, clear
         113 +                if clear >= 0:
         114 +                    score = np.linalg.norm(c - p0[:2]) + 0.3 * abs(y) * 0 
         115 +                    if score < best_score:
         116 +                        best, best_score = c, score
         117 +        return best if best is not None else fb
         118 +
         119 +    def _start_task(self, state):
         120 +        if not self.tasks:
         121 +            self.phase = 'done'
         122 +            return
         123 +        name, kind = self.tasks[0]
         124 +        p, q, h = self._pose(state, name)
         125 +        self.cur_obj = name
         126 +        yaws = [0.0, np.pi / 2, np.pi / 4, -np.pi / 4]
         127 +        self.grasp_yaw = self._pick_yaw(q) + yaws[self.grasp_attempt % len(yaws)]
         128 +        self.grasp_yaw = (self.grasp_yaw + np.pi / 2) % np.pi - np.pi / 2
         129 +        top = p[2] + h[2]
         130 +        tool = self._tool(state)[:3, 3]
         131 +        wps = []
         132 +        if tool[2] < Z_SAFE - 0.01:
         133 +            wps.append(np.array([tool[0], tool[1], Z_SAFE]))
         134 +        wps.append(np.array([p[0], p[1], Z_SAFE]))
         135 +        lo = p[2] - h[2] + 0.044
         136 +        hi = top + 0.033
         137 +        gz = 0.5 * (lo + hi) if hi > lo else hi - 0.002
         138 +        wps.append(np.array([p[0], p[1], gz]))
         139 +        self._set_path(state, wps, self.grasp_yaw)
         140 +        self.phase = 'to_grasp'
         141 +
         142 +    def _pick_yaw(self, q):
         143 +        y = _yaw_of_quat(q)
         144 +        # choose equivalent yaw (mod pi/2) closest to 0
         145 +        y = (y + np.pi / 4) % (np.pi / 2) - np.pi / 4
         146 +        return y
         147 +
         148 +    def _set_path(self, state, wps, yaw):
         149 +        cur = self._tool(state)[:3, 3]
         150 +        pts = []
         151 +        for w in wps:
         152 +            d = np.linalg.norm(w - cur)
         153 +            n = max(1, int(np.ceil(d / SEG)))
         154 +            for k in range(1, n + 1):
         155 +                pts.append(cur + (w - cur) * k / n)
         156 +            cur = w
         157 +        self.waypoints = pts
         158 +        self.wp_yaw = yaw
         159 +        self.stuck = 0
         160 +
         161 +    # ------------------------------------------------------------ control
         162 +    def _track(self, state, grip=0.0):
         163 +        """Return action moving toward current waypoint; None if path complete."""
         164 +        q = self._q(state)
         165 +        base = self._base(state)
         166 +        while self.waypoints:
         167 +            wp = self.waypoints[0]
         168 +            qt, ok = tool_ik(q, wp, down_R(self.wp_yaw), base, iters=100)
         169 +            d = (qt - q + np.pi) % (2 * np.pi) - np.pi
         170 +            if np.max(np.abs(d)) < 1e-4:
         171 +                self.waypoints.pop(0)
         172 +                continue
         173 +            a = np.zeros(11, dtype=np.float32)
         174 +            a[3:10] = np.clip(d, -STEP, STEP)
         175 +            a[10] = grip
         176 +            return a
         177 +        return None
         178 +
         179 +    def _noop(self, grip=0.0):
         180 +        a = np.zeros(11, dtype=np.float32); a[10] = grip
         181 +        return a
         182 +
         183 +    def get_action(self, state):
         184 +        q = self._q(state)
         185 +        moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
         186 +        self.last_q = q.copy()
         187 +        a = self._policy(state, moved)
         188 +        return np.asarray(a, dtype=np.float32)
         189 +
         190 +    def _policy(self, state, moved):
         191 +        ph = self.phase
         192 +        if ph == 'done':
         193 +            return self._noop()
         194 +
         195 +        if ph == 'to_grasp':
         196 +            if not moved and self.prev_was_motion:
         197 +                self.stuck += 1
         198 +            if self.stuck >= 2:
         199 +                self.waypoints = []  # blocked: try grasping here
         200 +            a = self._track(state)
         201 +            if a is not None:
         202 +                self.prev_was_motion = True
         203 +                return a
         204 +            self.phase = 'close'
         205 +            self.prev_was_motion = False
         206 +            return self._noop(-1.0)
         207 +
         208 +        if ph == 'close':
         209 +            g = self._grasped_name(state)
         210 +            if g is None:
         211 +                # failed: retry with a different yaw
         212 +                self.grasp_attempt += 1
         213 +                self._start_task(state)
         214 +                return self._noop()
         215 +            self.grasp_attempt = 0
         216 +            self.held = g
         217 +            if g != self.cur_obj:
         218 +                # grabbed wrong object: treat it as an obstruction to clear
         219 +                self.tasks.insert(0, (g, 'clear'))
         220 +                self.cur_obj = g
         221 +            self._plan_place(state)
         222 +            return self._noop()
         223 +
         224 +        if ph == 'to_place':
         225 +            if not moved and self.prev_was_motion:
         226 +                self.stuck += 1
         227 +                if len(self.waypoints) <= self.descent_len and self.stuck >= 1:
         228 +                    self.waypoints = []
         229 +            a = self._track(state)
         230 +            if a is not None:
         231 +                self.prev_was_motion = True
         232 +                return a
         233 +            self.phase = 'open'
         234 +            self.prev_was_motion = False
         235 +            return self._noop(1.0)
         236 +
         237 +        if ph == 'open':
         238 +            if self._grasped_name(state) is None and state.get(self.robot, 'grasp_active') < 0.5:
         239 +                self.release_tries = 0
         240 +                self.tasks.pop(0)
         241 +                tool = self._tool(state)[:3, 3]
         242 +                self._set_path(state, [np.array([tool[0], tool[1], Z_SAFE])], self.wp_yaw)
         243 +                self.phase = 'retreat'
         244 +                self.prev_was_motion = False
         245 +                return self._noop(1.0)
         246 +            self.release_tries += 1
         247 +            tool = self._tool(state)[:3, 3]
         248 +            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw)
         249 +            self.descent_len = 1
         250 +            self.phase = 'to_place'
         251 +            self.prev_was_motion = False
         252 +            if self.release_tries > 20:
         253 +                self.release_tries = 0
         254 +                self._plan_place(state)
         255 +            return self._noop(1.0)
         256 +
         257 +        if ph == 'retreat':
         258 +            a = self._track(state)
         259 +            if a is not None:
         260 +                return a
         261 +            if self.tasks and self.tasks[0][1] == 'goal':
         262 +                # re-check obstructions (in case something moved)
         263 +                for n in self._blocking_obstructions(state):
         264 +                    if all(t[0] != n for t in self.tasks):
         265 +                        self.tasks.insert(0, (n, 'clear'))
         266 +            self._start_task(state)
         267 +            return self._noop()
         268 +
         269 +        return self._noop()
         270 +
         271 +    def _plan_place(self, state):
         272 +        name = self.cur_obj
         273 +        p, qo, h = self._pose(state, name)
         274 +        r = self.robot
         275 +        tf = _T([state.get(r, 'grasp_tf_x'), state.get(r, 'grasp_tf_y'), state.get(r, 'grasp_tf_z')],
         276 +                [state.get(r, 'grasp_tf_qx'), state.get(r, 'grasp_tf_qy'), state.get(r, 'grasp_tf_qz'),
         277 +                 state.get(r, 'grasp_tf_qw')])
         278 +        kind = self.tasks[0][1] if self.tasks and self.tasks[0][0] == name else 'clear'
         279 +        if kind == 'goal':
         280 +            rp, rh = self.region
         281 +            xy = rp[:2]
         282 +            surf = rp[2] + rh[2]
         283 +        else:
         284 +            xy = self._free_spot(state, name)
         285 +            surf = self.table_z
         286 +        # desired object pose: same orientation as now, at xy, resting on surface
         287 +        Tobj = _T([xy[0], xy[1], surf + h[2] + 0.001], qo)
         288 +        Ttool = Tobj @ np.linalg.inv(tf)
         289 +        tgt = Ttool[:3, 3]
         290 +        yaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
         291 +        # tool orientation is down_R(yaw); keep current yaw (grasp yaw)
         292 +        yaw = self.grasp_yaw
         293 +        tool = self._tool(state)[:3, 3]
         294 +        wps = [np.array([tool[0], tool[1], Z_SAFE]),
         295 +               np.array([tgt[0], tgt[1], Z_SAFE]),
         296 +               np.array([tgt[0], tgt[1], tgt[2] + 0.03])]
         297 +        self._set_path(state, wps, yaw)
         298 +        n_before = len(self.waypoints)
         299 +        # fine descent in 5mm steps
         300 +        cur = wps[-1]
         301 +        k = 0
         302 +        while cur[2] > tgt[2] - 0.004:
         303 +            cur = cur - np.array([0, 0, 0.005])
         304 +            self.waypoints.append(cur.copy())
         305 +            k += 1
         306 +        self.descent_len = k + 6
         307 +        self.phase = 'to_place'
         308 +        self.prev_was_motion = False
```

</details>

<a id="C010"></a>
### C010 · Path lookahead cannot skip Cartesian corners

Commit `ecc0bf347c02fbad680aa82f0a5eb35a5d0251d6`; parents: 996e3753706e275754e93bc2b623d842ae39ba84. Recorded author date: 2026-09-30T20:52:08+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0482](01_timeline.md#E0482): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_ecc0bf3_approach.py) · [Exact all-file diff](evidence/diffs/C010_ecc0bf3.diff)

[Previous saved controller snapshot](evidence/versions/C009_996e375_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 987d3b0..731a453 100644
--- a/approach.py
+++ b/approach.py
@@ -232,6 +232,7 @@ class GeneratedApproach:
  232    232          cur = tool_fk(q, base)[:3, 3]
  233    233          R = down_R(yaw)
  234    234          path = []
         235 +        self.corners = set()
  235    236          qc = q.copy()
  236    237          for w in wps:
  237    238              d = np.linalg.norm(w - cur)
@@ -242,8 +243,10 @@ class GeneratedApproach:
  242    243                  qn = qc + _wrap(qn - qc)
  243    244                  path.append(qn)
  244    245                  qc = qn
         246 +            self.corners.add(len(path) - 1)
  245    247              cur = w
  246    248          self.qpath = path
         249 +        self.popped = 0
  247    250          self.wp_yaw = yaw
  248    251          self.final_grip = final_grip
  249    252          self.travel_grip = 1.0 if final_grip < 0 else 0.0
@@ -255,17 +258,21 @@ class GeneratedApproach:
  255    258          q = self._q(state)
  256    259          while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
  257    260              self.qpath.pop(0)
         261 +            self.popped += 1
  258    262          if not self.qpath:
  259    263              return None
  260    264          k = -1
  261    265          for i, qp in enumerate(self.qpath):
  262    266              if np.max(np.abs(_wrap(qp - q))) <= STEP:
  263    267                  k = i
         268 +                if (i + self.popped) in self.corners:
         269 +                    break
  264    270              else:
  265    271                  break
  266    272          a = np.zeros(11, dtype=np.float32)
  267    273          if k >= 0:
  268    274              self.qpath = self.qpath[k:]
         275 +            self.popped += k
  269    276              k = 0
  270    277              d = _wrap(self.qpath[0] - q)
  271    278              a[3:10] = d
diff --git a/dbg_pp.py b/dbg_pp.py
new file mode 100644
index 0000000..9ed102a
--- /dev/null
+++ b/dbg_pp.py
@@ -0,0 +1,15 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +from approach import GeneratedApproach
           5 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
           6 +ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           7 +for t in range(int(sys.argv[2])):
           8 +    a=ap.get_action(obs); obs,*_=env.step(a)
           9 +orig=ap._set_path
          10 +def sp(state,wps,yaw,final_grip=0.0,res=0.01):
          11 +    print('wps',[np.round(w,3) for w in wps],'yaw',round(float(yaw),3))
          12 +    orig(state,wps,yaw,final_grip,res); print('len',len(ap.qpath))
          13 +ap._set_path=sp
          14 +ap._plan_place(obs)
          15 +for n in ap.names: print(n,np.round(ap._pose(obs,n)[0],3),np.round(ap._pose(obs,n)[2],3))
diff --git a/res_new.txt b/res_new.txt
new file mode 100644
index 0000000..a141397
--- /dev/null
+++ b/res_new.txt
@@ -0,0 +1,100 @@
           1 +seed 9: success=True steps=27 time=14.8s nobs=1 phase=open
           2 +seed 3: success=True steps=33 time=34.6s nobs=2 phase=open
           3 +seed 1: success=True steps=43 time=37.9s nobs=1 phase=open
           4 +seed 0: success=True steps=41 time=35.0s nobs=2 phase=open
           5 +seed 11: success=True steps=19 time=12.5s nobs=0 phase=open
           6 +seed 7: success=True steps=47 time=36.7s nobs=2 phase=open
           7 +seed 5: success=True steps=45 time=34.3s nobs=2 phase=open
           8 +seed 2: success=True steps=65 time=59.8s nobs=2 phase=open
           9 +seed 10: success=True steps=34 time=35.5s nobs=2 phase=open
          10 +seed 12: success=True steps=29 time=24.8s nobs=1 phase=open
          11 +seed 8: success=True steps=72 time=76.8s nobs=2 phase=open
          12 +seed 16: success=True steps=33 time=26.4s nobs=1 phase=open
          13 +seed 15: success=True steps=33 time=31.0s nobs=2 phase=open
          14 +seed 4: success=True steps=95 time=90.6s nobs=2 phase=open
          15 +seed 13: success=True steps=52 time=51.5s nobs=2 phase=open
          16 +seed 17: success=True steps=46 time=36.4s nobs=2 phase=open
          17 +seed 18: success=True steps=43 time=40.2s nobs=2 phase=open
          18 +seed 19: success=True steps=42 time=35.9s nobs=1 phase=open
          19 +seed 21: success=True steps=26 time=26.0s nobs=0 phase=open
          20 +seed 24: success=True steps=22 time=20.4s nobs=1 phase=open
          21 +seed 22: success=True steps=32 time=30.7s nobs=2 phase=open
          22 +seed 23: success=True steps=26 time=25.4s nobs=0 phase=open
          23 +seed 20: success=True steps=51 time=44.2s nobs=2 phase=open
          24 +seed 29: success=True steps=17 time=15.2s nobs=2 phase=open
          25 +seed 27: success=True steps=31 time=28.3s nobs=0 phase=open
          26 +seed 30: success=True steps=25 time=21.7s nobs=0 phase=open
          27 +seed 26: success=True steps=40 time=44.7s nobs=2 phase=open
          28 +seed 28: success=True steps=49 time=46.8s nobs=1 phase=open
          29 +seed 34: success=True steps=24 time=19.9s nobs=0 phase=open
          30 +seed 25: success=True steps=61 time=71.7s nobs=1 phase=open
          31 +seed 35: success=True steps=29 time=28.0s nobs=0 phase=open
          32 +seed 32: success=True steps=54 time=55.7s nobs=2 phase=open
          33 +seed 37: success=True steps=20 time=24.0s nobs=0 phase=open
          34 +seed 38: success=True steps=19 time=19.2s nobs=0 phase=open
          35 +seed 31: success=True steps=67 time=75.8s nobs=1 phase=open
          36 +seed 36: success=True steps=46 time=52.1s nobs=1 phase=open
          37 +seed 41: success=True steps=34 time=26.7s nobs=1 phase=open
          38 +seed 33: success=True steps=69 time=77.8s nobs=2 phase=open
          39 +seed 42: success=True steps=24 time=15.8s nobs=0 phase=open
          40 +seed 40: success=True steps=48 time=50.7s nobs=1 phase=open
          41 +seed 48: success=True steps=17 time=9.2s nobs=0 phase=open
          42 +seed 39: success=True steps=54 time=62.6s nobs=2 phase=open
          43 +seed 47: success=True steps=24 time=19.1s nobs=0 phase=open
          44 +seed 44: success=True steps=45 time=45.1s nobs=2 phase=open
          45 +seed 43: success=True steps=53 time=50.5s nobs=1 phase=open
          46 +seed 49: success=True steps=24 time=20.8s nobs=0 phase=open
          47 +seed 46: success=True steps=41 time=39.9s nobs=1 phase=open
          48 +seed 54: success=True steps=19 time=11.5s nobs=0 phase=open
          49 +seed 51: success=True steps=41 time=28.7s nobs=1 phase=open
          50 +seed 56: success=True steps=28 time=13.6s nobs=1 phase=open
          51 +seed 57: success=True steps=25 time=12.4s nobs=0 phase=open
          52 +seed 14: success=False steps=1000 time=245.7s nobs=0 phase=done
          53 +seed 55: success=True steps=48 time=38.4s nobs=2 phase=open
          54 +seed 58: success=True steps=29 time=19.7s nobs=1 phase=open
          55 +seed 60: success=True steps=23 time=13.0s nobs=0 phase=open
          56 +seed 61: success=True steps=33 time=24.0s nobs=1 phase=open
          57 +seed 62: success=True steps=36 time=26.3s nobs=1 phase=open
          58 +seed 63: success=True steps=28 time=16.8s nobs=1 phase=open
          59 +seed 59: success=True steps=63 time=52.3s nobs=2 phase=open
          60 +seed 64: success=True steps=42 time=27.2s nobs=1 phase=open
          61 +seed 65: success=True steps=32 time=21.6s nobs=0 phase=open
          62 +seed 68: success=True steps=23 time=14.4s nobs=1 phase=open
          63 +seed 69: success=True steps=21 time=11.6s nobs=0 phase=open
          64 +seed 67: success=True steps=46 time=32.7s nobs=2 phase=open
          65 +seed 70: success=True steps=41 time=22.9s nobs=1 phase=open
          66 +seed 66: success=True steps=72 time=50.5s nobs=2 phase=open
          67 +seed 74: success=True steps=25 time=11.3s nobs=0 phase=open
          68 +seed 71: success=True steps=55 time=36.3s nobs=2 phase=open
          69 +seed 77: success=True steps=20 time=5.4s nobs=0 phase=open
          70 +seed 75: success=True steps=38 time=22.3s nobs=1 phase=open
          71 +seed 78: success=True steps=33 time=13.8s nobs=2 phase=open
          72 +seed 79: success=True steps=21 time=8.3s nobs=0 phase=open
          73 +seed 72: success=True steps=109 time=70.1s nobs=2 phase=open
          74 +seed 81: success=True steps=20 time=9.3s nobs=0 phase=open
          75 +seed 83: success=True steps=29 time=10.5s nobs=2 phase=open
          76 +seed 82: success=True steps=53 time=23.4s nobs=2 phase=open
          77 +seed 80: success=True steps=62 time=37.2s nobs=2 phase=open
          78 +seed 84: success=True steps=28 time=14.6s nobs=1 phase=open
          79 +seed 6: success=False steps=1000 time=484.4s nobs=1 phase=to_place
          80 +seed 85: success=True steps=60 time=31.6s nobs=2 phase=open
          81 +seed 87: success=True steps=40 time=19.7s nobs=1 phase=open
          82 +seed 90: success=True steps=42 time=15.3s nobs=1 phase=open
          83 +seed 88: success=True steps=60 time=30.2s nobs=1 phase=open
          84 +seed 89: success=True steps=61 time=34.8s nobs=2 phase=open
          85 +seed 91: success=True steps=47 time=24.1s nobs=2 phase=open
          86 +seed 92: success=True steps=43 time=21.8s nobs=1 phase=open
          87 +seed 52: success=False steps=1000 time=309.2s nobs=2 phase=close
          88 +seed 93: success=True steps=56 time=32.2s nobs=2 phase=open
          89 +seed 94: success=True steps=30 time=22.2s nobs=0 phase=open
          90 +seed 97: success=True steps=21 time=11.1s nobs=0 phase=open
          91 +seed 95: success=True steps=56 time=31.0s nobs=1 phase=open
          92 +seed 98: success=True steps=35 time=12.2s nobs=1 phase=open
          93 +seed 96: success=True steps=53 time=28.0s nobs=2 phase=open
          94 +seed 45: success=False steps=1000 time=386.7s nobs=2 phase=close
          95 +seed 99: success=True steps=68 time=15.5s nobs=2 phase=open
          96 +seed 50: success=False steps=1000 time=359.2s nobs=2 phase=close
          97 +seed 53: success=False steps=1000 time=349.5s nobs=2 phase=open
          98 +seed 73: success=False steps=1000 time=244.4s nobs=2 phase=retreat
          99 +seed 76: success=False steps=1000 time=216.7s nobs=1 phase=to_place
         100 +seed 86: success=False steps=1000 time=151.2s nobs=2 phase=to_place
```

</details>

<a id="C011"></a>
### C011 · Interpolate yaw along path; allow gripper flip for grasp

Commit `a830579a06b59b90ac74b6645217d3a16e438a13`; parents: ecc0bf347c02fbad680aa82f0a5eb35a5d0251d6. Recorded author date: 2026-09-30T20:55:04+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0511](01_timeline.md#E0511): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_a830579_approach.py) · [Exact all-file diff](evidence/diffs/C011_a830579.diff)

[Previous saved controller snapshot](evidence/versions/C010_ecc0bf3_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 731a453..9dae5e3 100644
--- a/approach.py
+++ b/approach.py
@@ -222,27 +222,43 @@ class GeneratedApproach:
  222    222              wps.append(np.array([tool[0], tool[1], zt]))
  223    223          wps.append(np.array([p[0], p[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]))
  224    224          wps.append(np.array([p[0], p[1], gz]))
  225        -        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0)
         225 +        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0, flip=True)
  226    226          self.phase = 'to_grasp'
  227    227  
  228        -    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01):
  229        -        """Cartesian waypoints -> dense joint path (IK warm-started)."""
         228 +    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False):
         229 +        """Cartesian waypoints -> dense joint path (IK warm-started).
         230 +        Yaw is interpolated from the current tool yaw over all but the last segment."""
  230    231          q = self._q(state)
  231    232          base = self._base(state)
  232        -        cur = tool_fk(q, base)[:3, 3]
  233        -        R = down_R(yaw)
         233 +        T0 = tool_fk(q, base)
         234 +        cur = T0[:3, 3]
         235 +        y0 = np.arctan2(T0[1, 0], T0[0, 0])
         236 +        dy = _wrap(yaw - y0)
         237 +        if flip and abs(dy) > np.pi / 2:
         238 +            dy = dy - np.sign(dy) * np.pi
         239 +        yaw = y0 + dy
         240 +        pts = [cur]
         241 +        for w in wps:
         242 +            pts.append(np.asarray(w, dtype=float))
         243 +        seg = [np.linalg.norm(pts[i + 1] - pts[i]) for i in range(len(wps))]
         244 +        rot_len = sum(seg[:-1]) if len(seg) > 1 and sum(seg[:-1]) > 0.02 else sum(seg)
         245 +        rot_len = max(rot_len, 1e-6)
  234    246          path = []
  235    247          self.corners = set()
  236    248          qc = q.copy()
  237        -        for w in wps:
  238        -            d = np.linalg.norm(w - cur)
  239        -            n = max(1, int(np.ceil(d / res)))
         249 +        travelled = 0.0
         250 +        for i, w in enumerate(wps):
         251 +            w = pts[i + 1]
         252 +            d = seg[i]
         253 +            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.1)))
  240    254              for k in range(1, n + 1):
  241    255                  pt = cur + (w - cur) * k / n
  242        -                qn, ok = tool_ik(qc, pt, R, base, iters=40)
         256 +                f = min(1.0, (travelled + d * k / n) / rot_len)
         257 +                qn, ok = tool_ik(qc, pt, down_R(y0 + f * dy), base, iters=40)
  243    258                  qn = qc + _wrap(qn - qc)
  244    259                  path.append(qn)
  245    260                  qc = qn
         261 +            travelled += d
  246    262              self.corners.add(len(path) - 1)
  247    263              cur = w
  248    264          self.qpath = path
@@ -391,7 +407,7 @@ class GeneratedApproach:
  391    407              self.phase = 'done'
  392    408              return self._noop()
  393    409          tool = self._tool(state)[:3, 3]
  394        -        self._set_path(state, [tool + np.array([0, 0, 0.03])], self.wp_yaw)
         410 +        self._set_path(state, [tool + np.array([0, 0, 0.03])], self.wp_yaw, flip=True)
  395    411          self.phase = 'retreat'
  396    412          a = self._track(state)
  397    413          return a if a is not None else self._noop()
diff --git a/dbg_pos.py b/dbg_pos.py
new file mode 100644
index 0000000..ac157c1
--- /dev/null
+++ b/dbg_pos.py
@@ -0,0 +1,8 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach, _yaw_of_quat as yq
           4 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
           5 +ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           6 +for n in ap.names: print(n,np.round(ap._pose(obs,n)[0],3),np.round(ap._pose(obs,n)[2],3), round(float(np.degrees(yq(ap._pose(obs,n)[1]))),1))
           7 +print('yaw',ap.grasp_yaw,'q0',np.round(ap._q(obs),2))
           8 +for qp in ap.qpath[::3]: print(np.round(qp,2))
```

</details>

<a id="C012"></a>
### C012 · Adaptive lookahead shrink on blocked steps

Commit `d1a140224d8afc3223f4608b45d8f51bb1b72656`; parents: a830579a06b59b90ac74b6645217d3a16e438a13. Recorded author date: 2026-09-30T20:56:05+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0548](01_timeline.md#E0548): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_d1a1402_approach.py) · [Exact all-file diff](evidence/diffs/C012_d1a1402.diff)

[Previous saved controller snapshot](evidence/versions/C011_a830579_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9dae5e3..436c962 100644
--- a/approach.py
+++ b/approach.py
@@ -115,6 +115,7 @@ class GeneratedApproach:
  115    115          self.last_q = None
  116    116          self.last_a = None
  117    117          self.blocked = False
         118 +        self.look = STEP
  118    119          self.stuck = 0
  119    120          self.descent_len = 0
  120    121          self.release_tries = 0
@@ -279,7 +280,7 @@ class GeneratedApproach:
  279    280              return None
  280    281          k = -1
  281    282          for i, qp in enumerate(self.qpath):
  282        -            if np.max(np.abs(_wrap(qp - q))) <= STEP:
         283 +            if np.max(np.abs(_wrap(qp - q))) <= self.look:
  283    284                  k = i
  284    285                  if (i + self.popped) in self.corners:
  285    286                      break
@@ -295,7 +296,7 @@ class GeneratedApproach:
  295    296              a[10] = self.travel_grip
  296    297          else:
  297    298              d = _wrap(self.qpath[0] - q)
  298        -            a[3:10] = d * (STEP / np.max(np.abs(d)))
         299 +            a[3:10] = d * (self.look / np.max(np.abs(d)))
  299    300          return a
  300    301  
  301    302      def _noop(self, grip=0.0):
@@ -307,6 +308,10 @@ class GeneratedApproach:
  307    308          moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
  308    309          attempted = self.last_a is not None and np.any(np.abs(self.last_a[3:10]) > 1e-9)
  309    310          self.blocked = attempted and not moved
         311 +        if self.blocked:
         312 +            self.look = max(0.02, self.look * 0.35)
         313 +        elif attempted:
         314 +            self.look = min(STEP, self.look * 1.5)
  310    315          self.last_q = q.copy()
  311    316          try:
  312    317              a = self._policy(state)
diff --git a/dbg_pp.py b/dbg_pp.py
index 9ed102a..f5f28b4 100644
--- a/dbg_pp.py
+++ b/dbg_pp.py
@@ -13,3 +13,5 @@ def sp(state,wps,yaw,final_grip=0.0,res=0.01):
   13     13  ap._set_path=sp
   14     14  ap._plan_place(obs)
   15     15  for n in ap.names: print(n,np.round(ap._pose(obs,n)[0],3),np.round(ap._pose(obs,n)[2],3))
          16 +from kin import tool_fk
          17 +for qp in ap.qpath[:4]: T=tool_fk(qp,ap._base(obs)); print(np.round(T[:3,3],3), round(float(np.arctan2(T[1,0],T[0,0])),3), np.round(qp-ap._q(obs),3))
diff --git a/probe86.py b/probe86.py
new file mode 100644
index 0000000..2915915
--- /dev/null
+++ b/probe86.py
@@ -0,0 +1,23 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import tool_fk, tool_ik, down_R
           5 +seed=int(sys.argv[1]); T=int(sys.argv[2])
           6 +def replay():
           7 +    env=make_env(); obs,info=env.reset(seed=seed)
           8 +    ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           9 +    for t in range(T):
          10 +        a=ap.get_action(obs); obs,*_=env.step(a)
          11 +    return env,obs,ap
          12 +env,obs,ap=replay()
          13 +q=ap._q(obs); base=ap._base(obs); Tt=tool_fk(q,base); yaw=np.arctan2(Tt[1,0],Tt[0,0])
          14 +print('tool',np.round(Tt[:3,3],3),'yaw',yaw,'finger',obs.get(ap.robot,'finger_state'))
          15 +tests={'up1cm':(0,0,0.01),'up3mm':(0,0,0.003),'-x':(-0.005,0,0.002),'+x':(0.005,0,0.002),'-y':(0,-0.005,0.002),'+y':(0,0.005,0.002)}
          16 +for k,d in tests.items():
          17 +    env.close(); env,obs,ap=replay()
          18 +    qn,ok=tool_ik(q,Tt[:3,3]+np.array(d),down_R(yaw),base)
          19 +    a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qn-q,-0.2,0.2)
          20 +    obs2,*_=env.step(a)
          21 +    print(k,'moved',not np.allclose(ap._q(obs2),q))
          22 +a=np.zeros(11,dtype=np.float32); a[1]=0.01
          23 +env.close(); env,obs,ap=replay(); obs2,*_=env.step(a); print('base dy moved', not np.allclose(ap._base(obs2),base))
```

</details>

<a id="C013"></a>
### C013 · Task selection by graspability, blocker clearing, grasp height candidates

Commit `d20aad046c37ebfc08bf3df6a81dede90626be41`; parents: d1a140224d8afc3223f4608b45d8f51bb1b72656. Recorded author date: 2026-09-30T21:19:22+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0642](01_timeline.md#E0642): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_d20aad0_approach.py) · [Exact all-file diff](evidence/diffs/C013_d20aad0.diff)

[Previous saved controller snapshot](evidence/versions/C012_d1a1402_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 436c962..c68fabe 100644
--- a/approach.py
+++ b/approach.py
@@ -116,6 +116,7 @@ class GeneratedApproach:
  116    116          self.last_a = None
  117    117          self.blocked = False
  118    118          self.look = STEP
         119 +        self.fails = {}
  119    120          self.stuck = 0
  120    121          self.descent_len = 0
  121    122          self.release_tries = 0
@@ -145,27 +146,73 @@ class GeneratedApproach:
  145    146              if top < tip_z - 0.002:
  146    147                  continue
  147    148              for fc, fh in fbs:
  148        -                clear = min(clear, _gap(fc, fh, c, hh))
         149 +                g = _gap(fc, fh, c, hh)
         150 +                if g < clear:
         151 +                    clear = g
         152 +                    self._blocker = n
  149    153          return clear
  150    154  
  151    155      def _choose_yaw(self, state, name, kind, attempt):
         156 +        sc = self._yaw_scores(state, name, kind)
         157 +        c = sc[attempt % len(sc)]
         158 +        self.grasp_z = c[3]
         159 +        return c[1]
         160 +
         161 +    def _yaw_scores(self, state, name, kind):
         162 +        """Sorted [(clearance score, yaw, blocker, grasp z)] for grasp candidates."""
  152    163          p, q, h = self._pose(state, name)
  153    164          oy = _yaw_of_quat(q)
  154        -        gz = self._grasp_z(p, h)
         165 +        lo = p[2] - h[2] + 0.045
         166 +        hi = p[2] + h[2] + 0.032
         167 +        gzs = [self._grasp_z(p, h)]
         168 +        if hi - 0.004 > gzs[0] + 0.004:
         169 +            gzs.append(hi - 0.004)
  155    170          cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
  156    171          scored = []
  157        -        for i, y in enumerate(cands):
  158        -            y = _wrap(2 * y) / 2  # modulo pi
  159        -            c = self._finger_clearance(state, p[:2], y, gz - FINGER_DOWN, exclude=(name,))
  160        -            if kind == 'goal':
  161        -                rp, rh = self.region
  162        -                surf = rp[2] + rh[2]
  163        -                tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
  164        -                c = min(c, self._finger_clearance(state, rp[:2], y, tip,
  165        -                                                  exclude=(name, 'target_region')))
  166        -            scored.append((min(c, 0.02) - 0.001 * i, y))
         172 +        for j, gz in enumerate(gzs):
         173 +            for i, y in enumerate(cands):
         174 +                y = _wrap(2 * y) / 2  # modulo pi
         175 +                self._blocker = None
         176 +                c = self._finger_clearance(state, p[:2], y, gz - FINGER_DOWN, exclude=(name,))
         177 +                blk = self._blocker
         178 +                if kind == 'goal':
         179 +                    rp, rh = self.region
         180 +                    surf = rp[2] + rh[2]
         181 +                    tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
         182 +                    c = min(c, self._finger_clearance(state, rp[:2], y, tip,
         183 +                                                      exclude=(name, 'target_region')))
         184 +                scored.append((min(c, 0.02) - 0.001 * i - 0.004 * j, y, blk, gz))
  167    185          scored.sort(key=lambda t: -t[0])
  168        -        return scored[attempt % len(scored)][1]
         186 +        return scored
         187 +
         188 +    def _select_task(self, state):
         189 +        """Reorder tasks so the front one is graspable; add blockers if needed."""
         190 +        for _ in range(len(self.names)):
         191 +            name, kind = self.tasks[0]
         192 +            f = self.fails.get(name, 0)
         193 +            sc = self._yaw_scores(state, name, kind)
         194 +            if sc[0][0] > 0.002 and f < 4:
         195 +                return
         196 +            # try another pending clear task that is more graspable
         197 +            best = None
         198 +            for t in self.tasks:
         199 +                if t[1] != 'clear' or t[0] == name:
         200 +                    continue
         201 +                s2 = self._yaw_scores(state, t[0], 'clear')[0][0] - 0.01 * self.fails.get(t[0], 0)
         202 +                if best is None or s2 > best[0]:
         203 +                    best = (s2, t)
         204 +            if best is not None and best[0] > max(0.002, sc[0][0] - 0.01 * f):
         205 +                self.tasks.remove(best[1])
         206 +                self.tasks.insert(0, best[1])
         207 +                continue
         208 +            # add the obstruction blocking the fingers as a new task
         209 +            blk = sc[0][2]
         210 +            if (blk is not None and blk.startswith('obstruction')
         211 +                    and all(t[0] != blk for t in self.tasks)
         212 +                    and self._yaw_scores(state, blk, 'clear')[0][0] > 0.002):
         213 +                self.tasks.insert(0, (blk, 'clear'))
         214 +                continue
         215 +            return
  169    216  
  170    217      def _grasp_z(self, p, h):
  171    218          lo = p[2] - h[2] + 0.045
@@ -211,11 +258,15 @@ class GeneratedApproach:
  211    258          if not self.tasks:
  212    259              self.phase = 'done'
  213    260              return
         261 +        try:
         262 +            self._select_task(state)
         263 +        except Exception:
         264 +            pass
  214    265          name, kind = self.tasks[0]
  215    266          p, q, h = self._pose(state, name)
  216    267          self.cur_obj = name
  217        -        self.grasp_yaw = self._choose_yaw(state, name, kind, self.grasp_attempt)
  218        -        gz = self._grasp_z(p, h)
         268 +        self.grasp_yaw = self._choose_yaw(state, name, kind, self.fails.get(name, 0))
         269 +        gz = self.grasp_z
  219    270          zt = self._transit_z(state)
  220    271          tool = self._tool(state)[:3, 3]
  221    272          wps = []
@@ -348,6 +399,7 @@ class GeneratedApproach:
  348    399              g = self._grasped_name(state)
  349    400              if g is None:
  350    401                  self.grasp_attempt += 1
         402 +                self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
  351    403                  self.total_fail += 1
  352    404                  self._start_task(state)
  353    405                  return self._track(state) if self.qpath else self._noop()
diff --git a/dbg_pos.py b/dbg_pos.py
index ac157c1..8696c1f 100644
--- a/dbg_pos.py
+++ b/dbg_pos.py
@@ -1,7 +1,8 @@
    1      1  import sys, numpy as np
    2      2  from env_client import make_env
    3      3  from approach import GeneratedApproach, _yaw_of_quat as yq
    4        -env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
           4 +cnt=int(sys.argv[2]) if len(sys.argv)>2 else None
           5 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]),options={"object_count":cnt} if cnt else None)
    5      6  ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
    6      7  for n in ap.names: print(n,np.round(ap._pose(obs,n)[0],3),np.round(ap._pose(obs,n)[2],3), round(float(np.degrees(yq(ap._pose(obs,n)[1]))),1))
    7      8  print('yaw',ap.grasp_yaw,'q0',np.round(ap._q(obs),2))
diff --git a/prof.out b/prof.out
new file mode 100644
index 0000000..f2d5183
Binary files /dev/null and b/prof.out differ
diff --git a/res_c4.txt b/res_c4.txt
new file mode 100644
index 0000000..721b5ff
--- /dev/null
+++ b/res_c4.txt
@@ -0,0 +1,40 @@
           1 +seed 3: success=True steps=64 time=41.9s nobs=4 phase=open
           2 +seed 1: success=True steps=74 time=38.6s nobs=4 phase=open
           3 +seed 0: success=True steps=85 time=63.3s nobs=4 phase=open
           4 +seed 9: success=True steps=87 time=78.2s nobs=4 phase=open
           5 +seed 8: success=True steps=93 time=73.8s nobs=4 phase=open
           6 +seed 6: success=True steps=91 time=64.4s nobs=4 phase=open
           7 +seed 2: success=True steps=98 time=70.4s nobs=4 phase=open
           8 +seed 14: success=True steps=45 time=29.1s nobs=4 phase=open
           9 +seed 10: success=True steps=78 time=64.1s nobs=4 phase=open
          10 +seed 4: success=True steps=146 time=129.0s nobs=4 phase=open
          11 +seed 5: success=True steps=155 time=123.8s nobs=4 phase=open
          12 +seed 16: success=True steps=50 time=31.6s nobs=4 phase=open
          13 +seed 13: success=True steps=98 time=73.0s nobs=4 phase=open
          14 +seed 15: success=True steps=98 time=78.2s nobs=4 phase=open
          15 +seed 18: success=True steps=55 time=41.1s nobs=4 phase=open
          16 +seed 17: success=True steps=74 time=63.3s nobs=4 phase=open
          17 +seed 19: success=True steps=75 time=65.8s nobs=4 phase=open
          18 +seed 22: success=True steps=51 time=41.8s nobs=4 phase=open
          19 +seed 20: success=True steps=84 time=66.8s nobs=4 phase=open
          20 +seed 25: success=True steps=57 time=45.5s nobs=4 phase=open
          21 +seed 23: success=True steps=112 time=83.6s nobs=4 phase=open
          22 +seed 27: success=True steps=93 time=56.7s nobs=4 phase=open
          23 +seed 26: success=True steps=92 time=60.7s nobs=4 phase=open
          24 +seed 28: success=True steps=105 time=73.5s nobs=4 phase=open
          25 +seed 29: success=True steps=66 time=51.1s nobs=4 phase=open
          26 +seed 30: success=True steps=85 time=66.0s nobs=4 phase=open
          27 +seed 32: success=True steps=86 time=59.6s nobs=4 phase=open
          28 +seed 33: success=True steps=85 time=59.6s nobs=4 phase=open
          29 +seed 34: success=True steps=84 time=57.8s nobs=4 phase=open
          30 +seed 35: success=True steps=62 time=45.3s nobs=4 phase=open
          31 +seed 37: success=True steps=83 time=51.0s nobs=4 phase=open
          32 +seed 39: success=True steps=84 time=40.9s nobs=4 phase=open
          33 +seed 12: success=False steps=1000 time=458.8s nobs=4 phase=to_grasp
          34 +seed 11: success=False steps=1000 time=476.1s nobs=4 phase=to_grasp
          35 +seed 7: success=False steps=1000 time=543.0s nobs=4 phase=to_grasp
          36 +seed 24: success=False steps=1000 time=444.3s nobs=4 phase=to_grasp
          37 +seed 21: success=False steps=1000 time=492.2s nobs=4 phase=to_grasp
          38 +seed 31: success=False steps=1000 time=364.3s nobs=4 phase=to_grasp
          39 +seed 36: success=False steps=1000 time=300.9s nobs=4 phase=to_grasp
          40 +seed 38: success=False steps=1000 time=277.3s nobs=4 phase=close
diff --git a/res_new2.txt b/res_new2.txt
new file mode 100644
index 0000000..284f269
--- /dev/null
+++ b/res_new2.txt
@@ -0,0 +1,100 @@
           1 +seed 9: success=True steps=25 time=16.8s nobs=1 phase=open
           2 +seed 0: success=True steps=43 time=38.7s nobs=2 phase=open
           3 +seed 1: success=True steps=45 time=28.4s nobs=1 phase=open
           4 +seed 5: success=True steps=51 time=46.8s nobs=2 phase=open
           5 +seed 3: success=True steps=49 time=44.8s nobs=2 phase=open
           6 +seed 10: success=True steps=36 time=28.2s nobs=2 phase=open
           7 +seed 4: success=True steps=59 time=59.0s nobs=2 phase=open
           8 +seed 11: success=True steps=25 time=20.6s nobs=0 phase=open
           9 +seed 6: success=True steps=60 time=55.6s nobs=1 phase=open
          10 +seed 14: success=True steps=14 time=5.9s nobs=0 phase=open
          11 +seed 7: success=True steps=61 time=46.8s nobs=2 phase=open
          12 +seed 8: success=True steps=68 time=66.1s nobs=2 phase=open
          13 +seed 2: success=True steps=75 time=87.2s nobs=2 phase=open
          14 +seed 16: success=True steps=36 time=27.8s nobs=1 phase=open
          15 +seed 12: success=True steps=48 time=46.1s nobs=1 phase=open
          16 +seed 15: success=True steps=38 time=44.7s nobs=2 phase=open
          17 +seed 21: success=True steps=30 time=21.8s nobs=0 phase=open
          18 +seed 18: success=True steps=46 time=41.8s nobs=2 phase=open
          19 +seed 13: success=True steps=70 time=72.2s nobs=2 phase=open
          20 +seed 24: success=True steps=25 time=21.7s nobs=1 phase=open
          21 +seed 17: success=True steps=60 time=63.2s nobs=2 phase=open
          22 +seed 19: success=True steps=60 time=54.4s nobs=1 phase=open
          23 +seed 22: success=True steps=39 time=43.3s nobs=2 phase=open
          24 +seed 20: success=True steps=66 time=64.4s nobs=2 phase=open
          25 +seed 23: success=True steps=39 time=42.2s nobs=0 phase=open
          26 +seed 26: success=True steps=37 time=41.0s nobs=2 phase=open
          27 +seed 27: success=True steps=48 time=39.1s nobs=0 phase=open
          28 +seed 30: success=True steps=31 time=26.1s nobs=0 phase=open
          29 +seed 34: success=True steps=18 time=10.7s nobs=0 phase=open
          30 +seed 29: success=True steps=30 time=32.0s nobs=2 phase=open
          31 +seed 25: success=True steps=54 time=64.8s nobs=1 phase=open
          32 +seed 35: success=True steps=21 time=21.6s nobs=0 phase=open
          33 +seed 31: success=True steps=43 time=42.8s nobs=1 phase=open
          34 +seed 32: success=True steps=47 time=48.7s nobs=2 phase=open
          35 +seed 38: success=True steps=21 time=22.4s nobs=0 phase=open
          36 +seed 37: success=True steps=22 time=26.7s nobs=0 phase=open
          37 +seed 33: success=True steps=50 time=54.8s nobs=2 phase=open
          38 +seed 28: success=True steps=65 time=80.4s nobs=1 phase=open
          39 +seed 36: success=True steps=36 time=48.1s nobs=1 phase=open
          40 +seed 42: success=True steps=20 time=25.7s nobs=0 phase=open
          41 +seed 47: success=True steps=16 time=12.6s nobs=0 phase=open
          42 +seed 41: success=True steps=32 time=39.8s nobs=1 phase=open
          43 +seed 40: success=True steps=42 time=47.5s nobs=1 phase=open
          44 +seed 48: success=True steps=19 time=12.1s nobs=0 phase=open
          45 +seed 43: success=True steps=35 time=32.9s nobs=1 phase=open
          46 +seed 39: success=True steps=53 time=58.7s nobs=2 phase=open
          47 +seed 49: success=True steps=17 time=19.3s nobs=0 phase=open
          48 +seed 46: success=True steps=33 time=41.9s nobs=1 phase=open
          49 +seed 44: success=True steps=42 time=55.0s nobs=2 phase=open
          50 +seed 54: success=True steps=20 time=20.8s nobs=0 phase=open
          51 +seed 57: success=True steps=20 time=12.8s nobs=0 phase=open
          52 +seed 51: success=True steps=37 time=38.0s nobs=1 phase=open
          53 +seed 45: success=True steps=62 time=73.3s nobs=2 phase=open
          54 +seed 56: success=True steps=35 time=31.8s nobs=1 phase=open
          55 +seed 60: success=True steps=17 time=16.7s nobs=0 phase=open
          56 +seed 58: success=True steps=35 time=34.2s nobs=1 phase=open
          57 +seed 53: success=True steps=48 time=60.0s nobs=2 phase=open
          58 +seed 50: success=True steps=57 time=68.4s nobs=2 phase=open
          59 +seed 62: success=True steps=36 time=27.0s nobs=1 phase=open
          60 +seed 52: success=True steps=74 time=67.6s nobs=2 phase=open
          61 +seed 55: success=True steps=69 time=65.7s nobs=2 phase=open
          62 +seed 61: success=True steps=41 time=33.8s nobs=1 phase=open
          63 +seed 64: success=True steps=31 time=27.4s nobs=1 phase=open
          64 +seed 63: success=True steps=39 time=34.7s nobs=1 phase=open
          65 +seed 69: success=True steps=17 time=15.3s nobs=0 phase=open
          66 +seed 65: success=True steps=37 time=35.9s nobs=0 phase=open
          67 +seed 68: success=True steps=24 time=28.0s nobs=1 phase=open
          68 +seed 74: success=True steps=16 time=12.5s nobs=0 phase=open
          69 +seed 59: success=True steps=82 time=87.5s nobs=2 phase=open
          70 +seed 67: success=True steps=52 time=52.6s nobs=2 phase=open
          71 +seed 70: success=True steps=42 time=42.6s nobs=1 phase=open
          72 +seed 75: success=True steps=28 time=24.6s nobs=1 phase=open
          73 +seed 66: success=True steps=66 time=62.9s nobs=2 phase=open
          74 +seed 77: success=True steps=23 time=19.8s nobs=0 phase=open
          75 +seed 73: success=True steps=48 time=49.0s nobs=2 phase=open
          76 +seed 79: success=True steps=29 time=21.5s nobs=0 phase=open
          77 +seed 71: success=True steps=64 time=66.7s nobs=2 phase=open
          78 +seed 76: success=True steps=50 time=41.7s nobs=1 phase=open
          79 +seed 81: success=True steps=25 time=18.9s nobs=0 phase=open
          80 +seed 78: success=True steps=44 time=38.6s nobs=2 phase=open
          81 +seed 72: success=True steps=70 time=76.0s nobs=2 phase=open
          82 +seed 84: success=True steps=35 time=24.8s nobs=1 phase=open
          83 +seed 82: success=True steps=51 time=38.2s nobs=2 phase=open
          84 +seed 80: success=True steps=53 time=49.1s nobs=2 phase=open
          85 +seed 83: success=True steps=44 time=40.1s nobs=2 phase=open
          86 +seed 88: success=True steps=36 time=25.3s nobs=1 phase=open
          87 +seed 85: success=True steps=56 time=44.4s nobs=2 phase=open
          88 +seed 90: success=True steps=41 time=28.1s nobs=1 phase=open
          89 +seed 87: success=True steps=51 time=39.9s nobs=1 phase=open
          90 +seed 86: success=True steps=57 time=48.7s nobs=2 phase=open
          91 +seed 94: success=True steps=24 time=18.4s nobs=0 phase=open
          92 +seed 91: success=True steps=41 time=36.0s nobs=2 phase=open
          93 +seed 89: success=True steps=54 time=45.6s nobs=2 phase=open
          94 +seed 92: success=True steps=43 time=31.1s nobs=1 phase=open
          95 +seed 97: success=True steps=32 time=10.7s nobs=0 phase=open
          96 +seed 93: success=True steps=58 time=33.9s nobs=2 phase=open
          97 +seed 95: success=True steps=58 time=25.1s nobs=1 phase=open
          98 +seed 98: success=True steps=47 time=10.3s nobs=1 phase=open
          99 +seed 96: success=True steps=59 time=19.9s nobs=2 phase=open
         100 +seed 99: success=True steps=53 time=10.6s nobs=2 phase=open
```

</details>

<a id="C014"></a>
### C014 · Better task switching; abort grasp approach blocked high

Commit `79e4d38434ae7a22341066cc2694a2a5cf49dadb`; parents: d20aad046c37ebfc08bf3df6a81dede90626be41. Recorded author date: 2026-09-30T21:23:27+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0673](01_timeline.md#E0673): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_79e4d38_approach.py) · [Exact all-file diff](evidence/diffs/C014_79e4d38.diff)

[Previous saved controller snapshot](evidence/versions/C013_d20aad0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c68fabe..0f62fd5 100644
--- a/approach.py
+++ b/approach.py
@@ -201,7 +201,7 @@ class GeneratedApproach:
  201    201                  s2 = self._yaw_scores(state, t[0], 'clear')[0][0] - 0.01 * self.fails.get(t[0], 0)
  202    202                  if best is None or s2 > best[0]:
  203    203                      best = (s2, t)
  204        -            if best is not None and best[0] > max(0.002, sc[0][0] - 0.01 * f):
         204 +            if best is not None and best[0] > sc[0][0] - 0.01 * f + 0.001:
  205    205                  self.tasks.remove(best[1])
  206    206                  self.tasks.insert(0, best[1])
  207    207                  continue
@@ -388,6 +388,12 @@ class GeneratedApproach:
  388    388              if self.blocked:
  389    389                  self.stuck += 1
  390    390                  if self.stuck >= 2:
         391 +                    if self._tool(state)[2, 3] > self.grasp_z + 0.012:
         392 +                        # cannot get down to the grasp: try something else
         393 +                        self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         394 +                        self._start_task(state)
         395 +                        a = self._track(state)
         396 +                        return a if a is not None else self._noop()
  391    397                      self.qpath = []
  392    398              a = self._track(state)
  393    399              if a is not None:
diff --git a/probe_diag.py b/probe_diag.py
new file mode 100644
index 0000000..0c2f864
--- /dev/null
+++ b/probe_diag.py
@@ -0,0 +1,15 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +import approach
           4 +from approach import GeneratedApproach
           5 +Y=float(sys.argv[2])
           6 +def cy(self,state,name,kind,attempt):
           7 +    p,q,h=self._pose(state,name); self.grasp_z=self._grasp_z(p,h); return approach._yaw_of_quat(q)+Y
           8 +GeneratedApproach._choose_yaw=cy
           9 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
          10 +ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
          11 +for t in range(40):
          12 +    a=ap.get_action(obs); obs,*_=env.step(a)
          13 +    if ap.phase=='close':
          14 +        T=ap._tool(obs); print(t,'close at',np.round(T[:3,3],3),ap.cur_obj,np.round(ap._pose(obs,ap.cur_obj)[2],3))
          15 +    if ap.phase=='to_place': print('grasped',ap._grasped_name(obs)); break
```

</details>

<a id="C015"></a>
### C015 · Blocker only when overlapping; cap blocker moves

Commit `ce0527f93f9b673678caf1455ba1e7abf41d789f`; parents: 79e4d38434ae7a22341066cc2694a2a5cf49dadb. Recorded author date: 2026-09-30T21:24:38+02:00.

File roles (automatic): policy.

- [E0685](01_timeline.md#E0685): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_ce0527f_approach.py) · [Exact all-file diff](evidence/diffs/C015_ce0527f.diff)

[Previous saved controller snapshot](evidence/versions/C014_79e4d38_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0f62fd5..a80cd54 100644
--- a/approach.py
+++ b/approach.py
@@ -117,6 +117,7 @@ class GeneratedApproach:
  117    117          self.blocked = False
  118    118          self.look = STEP
  119    119          self.fails = {}
         120 +        self.blk_moves = {}
  120    121          self.stuck = 0
  121    122          self.descent_len = 0
  122    123          self.release_tries = 0
@@ -149,7 +150,8 @@ class GeneratedApproach:
  149    150                  g = _gap(fc, fh, c, hh)
  150    151                  if g < clear:
  151    152                      clear = g
  152        -                    self._blocker = n
         153 +                    if g < 0.005:
         154 +                        self._blocker = n
  153    155          return clear
  154    156  
  155    157      def _choose_yaw(self, state, name, kind, attempt):
@@ -209,7 +211,9 @@ class GeneratedApproach:
  209    211              blk = sc[0][2]
  210    212              if (blk is not None and blk.startswith('obstruction')
  211    213                      and all(t[0] != blk for t in self.tasks)
         214 +                    and self.blk_moves.get(blk, 0) < 2
  212    215                      and self._yaw_scores(state, blk, 'clear')[0][0] > 0.002):
         216 +                self.blk_moves[blk] = self.blk_moves.get(blk, 0) + 1
  213    217                  self.tasks.insert(0, (blk, 'clear'))
  214    218                  continue
  215    219              return
```

</details>

<a id="C016"></a>
### C016 · Merge grip with final motion, drop retreat step, cut path corners when safe

Commit `328f15a53a02eb0566a9e7139d28536608094a06`; parents: ce0527f93f9b673678caf1455ba1e7abf41d789f. Recorded author date: 2026-09-30T21:29:14+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0719](01_timeline.md#E0719): commit title in command; output may not confirm creation.
- [E0721](01_timeline.md#E0721): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_328f15a_approach.py) · [Exact all-file diff](evidence/diffs/C016_328f15a.diff)

[Previous saved controller snapshot](evidence/versions/C015_ce0527f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a80cd54..67e5f1a 100644
--- a/approach.py
+++ b/approach.py
@@ -12,6 +12,8 @@ import numpy as np
   12     12  from kin import tool_fk, tool_ik, down_R
   13     13  
   14     14  JN = [f'joint_{i}' for i in range(1, 8)]
          15 +MERGE_GRIP = True
          16 +CUT_CORNERS = True
   15     17  STEP = 0.2             # max joint delta per step
   16     18  FINGER_DOWN = 0.036    # fingertips below tool frame
   17     19  F_OFF, F_HL, F_HW = 0.046, 0.024, 0.013   # finger centre offset, half length, half width
@@ -274,14 +276,16 @@ class GeneratedApproach:
  274    276          zt = self._transit_z(state)
  275    277          tool = self._tool(state)[:3, 3]
  276    278          wps = []
         279 +        rs = 0
  277    280          if tool[2] < zt - 0.01:
  278    281              wps.append(np.array([tool[0], tool[1], zt]))
         282 +            rs = 1
  279    283          wps.append(np.array([p[0], p[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]))
  280    284          wps.append(np.array([p[0], p[1], gz]))
  281        -        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0, flip=True)
         285 +        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0, flip=True, rot_start=rs)
  282    286          self.phase = 'to_grasp'
  283    287  
  284        -    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False):
         288 +    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False, rot_start=0):
  285    289          """Cartesian waypoints -> dense joint path (IK warm-started).
  286    290          Yaw is interpolated from the current tool yaw over all but the last segment."""
  287    291          q = self._q(state)
@@ -297,7 +301,10 @@ class GeneratedApproach:
  297    301          for w in wps:
  298    302              pts.append(np.asarray(w, dtype=float))
  299    303          seg = [np.linalg.norm(pts[i + 1] - pts[i]) for i in range(len(wps))]
  300        -        rot_len = sum(seg[:-1]) if len(seg) > 1 and sum(seg[:-1]) > 0.02 else sum(seg)
         304 +        if len(seg) - 1 <= rot_start:
         305 +            rot_start = 0
         306 +        rot0 = sum(seg[:rot_start])
         307 +        rot_len = sum(seg[rot_start:-1]) if len(seg) > 1 and sum(seg[rot_start:-1]) > 0.02 else sum(seg[rot_start:])
  301    308          rot_len = max(rot_len, 1e-6)
  302    309          path = []
  303    310          self.corners = set()
@@ -309,7 +316,7 @@ class GeneratedApproach:
  309    316              n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.1)))
  310    317              for k in range(1, n + 1):
  311    318                  pt = cur + (w - cur) * k / n
  312        -                f = min(1.0, (travelled + d * k / n) / rot_len)
         319 +                f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
  313    320                  qn, ok = tool_ik(qc, pt, down_R(y0 + f * dy), base, iters=40)
  314    321                  qn = qc + _wrap(qn - qc)
  315    322                  path.append(qn)
@@ -334,11 +341,16 @@ class GeneratedApproach:
  334    341          if not self.qpath:
  335    342              return None
  336    343          k = -1
         344 +        crossed = False
  337    345          for i, qp in enumerate(self.qpath):
  338    346              if np.max(np.abs(_wrap(qp - q))) <= self.look:
         347 +                if crossed and not self._safe_move(state, q, qp):
         348 +                    break
  339    349                  k = i
  340    350                  if (i + self.popped) in self.corners:
  341        -                    break
         351 +                    if not CUT_CORNERS or self.blocked or self.look < STEP:
         352 +                        break
         353 +                    crossed = True
  342    354              else:
  343    355                  break
  344    356          a = np.zeros(11, dtype=np.float32)
@@ -349,11 +361,37 @@ class GeneratedApproach:
  349    361              d = _wrap(self.qpath[0] - q)
  350    362              a[3:10] = d
  351    363              a[10] = self.travel_grip
         364 +            if MERGE_GRIP and len(self.qpath) == 1 and self.final_grip != 0.0:
         365 +                a[10] = self.final_grip
  352    366          else:
  353    367              d = _wrap(self.qpath[0] - q)
  354    368              a[3:10] = d * (self.look / np.max(np.abs(d)))
  355    369          return a
  356    370  
         371 +    def _safe_move(self, state, q0, q1):
         372 +        """Check the joint-linear move q0->q1 keeps tool/fingers/held object
         373 +        above all nearby objects (used when cutting path corners)."""
         374 +        base = self._base(state)
         375 +        held = self._grasped_name(state)
         376 +        depth, rad = FINGER_DOWN, 0.075
         377 +        if held is not None:
         378 +            p, _, h = self._pose(state, held)
         379 +            tz = self._tool(state)[2, 3]
         380 +            depth = max(depth, tz - (p[2] - h[2]))
         381 +            rad = max(rad, np.hypot(h[0], h[1]) + 0.01)
         382 +        boxes = [self._box(state, n) for n in self.names if n != held]
         383 +        dq = _wrap(q1 - q0)
         384 +        for f in (0.25, 0.5, 0.75, 1.0):
         385 +            pt = tool_fk(q0 + f * dq, base)[:3, 3]
         386 +            low = pt[2] - depth
         387 +            if low < self.table_z + 0.01:
         388 +                return False
         389 +            for c, hh, bot, top in boxes:
         390 +                dxy = np.maximum(np.abs(pt[:2] - c) - hh, 0.0)
         391 +                if np.hypot(dxy[0], dxy[1]) < rad and low < top + 0.012:
         392 +                    return False
         393 +        return True
         394 +
  357    395      def _noop(self, grip=0.0):
  358    396          a = np.zeros(11, dtype=np.float32); a[10] = grip
  359    397          return a
@@ -473,10 +511,8 @@ class GeneratedApproach:
  473    511          if kind == 'goal':
  474    512              self.phase = 'done'
  475    513              return self._noop()
  476        -        tool = self._tool(state)[:3, 3]
  477        -        self._set_path(state, [tool + np.array([0, 0, 0.03])], self.wp_yaw, flip=True)
  478        -        self.phase = 'retreat'
  479        -        a = self._track(state)
         514 +        self._next_task(state)
         515 +        a = self._track(state) if self.phase == 'to_grasp' else None
  480    516          return a if a is not None else self._noop()
  481    517  
  482    518      def _next_task(self, state):
diff --git a/dbg_rw.py b/dbg_rw.py
index c9a06d0..e8a2901 100644
--- a/dbg_rw.py
+++ b/dbg_rw.py
@@ -10,6 +10,6 @@ for t in range(int(sys.argv[2])):
   10     10      a=ap.get_action(obs)
   11     11      obs,r,term,tr,_=env.step(a)
   12     12      key=(ap.phase, ap._grasped_name(obs), ap.tasks[0] if ap.tasks else None)
   13        -    if key!=last or ap.blocked:
          13 +    if key!=last or ap.blocked or len(sys.argv)>4:
   14     14          print(t,ap.phase,len(ap.qpath),np.round(ap._tool(obs)[:3,3],3),'blk',ap.blocked,'grip',a[10],key[1],key[2]); last=key
   15     15      if term: print('DONE',t+1);break
diff --git a/res_d3.txt b/res_d3.txt
new file mode 100644
index 0000000..8458174
--- /dev/null
+++ b/res_d3.txt
@@ -0,0 +1,48 @@
           1 +seed 9: success=True steps=25 time=18.3s nobs=1 phase=open
           2 +seed 1: success=True steps=45 time=39.6s nobs=1 phase=open
           3 +seed 0: success=True steps=43 time=42.4s nobs=2 phase=open
           4 +seed 3: success=True steps=49 time=39.6s nobs=2 phase=open
           5 +seed 4: success=True steps=60 time=63.9s nobs=2 phase=open
           6 +seed 6: success=True steps=60 time=58.3s nobs=1 phase=open
           7 +seed 11: success=True steps=23 time=22.4s nobs=0 phase=to_place
           8 +seed 10: success=True steps=32 time=33.3s nobs=2 phase=to_place
           9 +seed 5: success=True steps=62 time=62.9s nobs=2 phase=open
          10 +seed 8: success=True steps=68 time=81.4s nobs=2 phase=open
          11 +seed 7: success=True steps=61 time=67.2s nobs=2 phase=open
          12 +seed 14: success=True steps=12 time=18.2s nobs=0 phase=to_place
          13 +seed 2: success=True steps=75 time=86.6s nobs=2 phase=open
          14 +seed 12: success=True steps=44 time=48.1s nobs=1 phase=to_place
          15 +seed 16: success=True steps=32 time=33.6s nobs=1 phase=to_place
          16 +seed 15: success=True steps=34 time=45.8s nobs=2 phase=to_place
          17 +seed 21: success=True steps=28 time=26.3s nobs=0 phase=to_place
          18 +seed 18: success=True steps=42 time=44.9s nobs=2 phase=to_place
          19 +seed 22: success=True steps=35 time=36.5s nobs=2 phase=to_place
          20 +seed 17: success=True steps=54 time=60.0s nobs=2 phase=to_place
          21 +seed 24: success=True steps=23 time=28.3s nobs=1 phase=to_place
          22 +seed 13: success=True steps=76 time=84.2s nobs=2 phase=to_place
          23 +seed 19: success=True steps=60 time=59.9s nobs=1 phase=to_place
          24 +seed 23: success=True steps=37 time=46.1s nobs=0 phase=to_place
          25 +seed 20: success=True steps=60 time=70.5s nobs=2 phase=to_place
          26 +seed 26: success=True steps=32 time=43.0s nobs=2 phase=to_place
          27 +seed 29: success=True steps=28 time=30.3s nobs=2 phase=to_place
          28 +seed 25: success=True steps=49 time=59.5s nobs=1 phase=to_place
          29 +seed 34: success=True steps=16 time=16.9s nobs=0 phase=to_place
          30 +seed 30: success=True steps=29 time=32.8s nobs=0 phase=to_place
          31 +seed 27: success=True steps=46 time=51.7s nobs=0 phase=to_place
          32 +seed 35: success=True steps=19 time=24.7s nobs=0 phase=to_place
          33 +seed 31: success=True steps=39 time=49.1s nobs=1 phase=to_place
          34 +seed 32: success=True steps=42 time=56.4s nobs=2 phase=to_place
          35 +seed 33: success=True steps=45 time=56.3s nobs=2 phase=to_place
          36 +seed 38: success=True steps=19 time=25.1s nobs=0 phase=to_place
          37 +seed 37: success=True steps=20 time=31.6s nobs=0 phase=to_place
          38 +seed 42: success=True steps=18 time=21.3s nobs=0 phase=to_place
          39 +seed 36: success=True steps=40 time=53.2s nobs=1 phase=to_place
          40 +seed 28: success=True steps=61 time=93.3s nobs=1 phase=to_place
          41 +seed 41: success=True steps=27 time=37.9s nobs=1 phase=to_place
          42 +seed 47: success=True steps=11 time=14.1s nobs=0 phase=to_place
          43 +seed 40: success=True steps=37 time=54.6s nobs=1 phase=to_place
          44 +seed 48: success=True steps=14 time=16.3s nobs=0 phase=to_place
          45 +seed 49: success=True steps=13 time=13.1s nobs=0 phase=to_place
          46 +seed 43: success=True steps=28 time=43.3s nobs=1 phase=to_place
          47 +seed 39: success=True steps=48 time=71.8s nobs=2 phase=to_place
          48 +seed 46: success=True steps=32 time=42.2s nobs=1 phase=to_place
```

</details>

<a id="C017"></a>
### C017 · Prefer grasp yaw near current tool yaw; finer rotation path resolution

Commit `87f3bd01cbabfcfc7641c551be5fc5f0487a207c`; parents: 328f15a53a02eb0566a9e7139d28536608094a06. Recorded author date: 2026-09-30T21:46:20+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0845](01_timeline.md#E0845): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_87f3bd0_approach.py) · [Exact all-file diff](evidence/diffs/C017_87f3bd0.diff)

[Previous saved controller snapshot](evidence/versions/C016_328f15a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 67e5f1a..76599d7 100644
--- a/approach.py
+++ b/approach.py
@@ -172,6 +172,8 @@ class GeneratedApproach:
  172    172          if hi - 0.004 > gzs[0] + 0.004:
  173    173              gzs.append(hi - 0.004)
  174    174          cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
         175 +        T = self._tool(state)
         176 +        ty = np.arctan2(T[1, 0], T[0, 0])
  175    177          scored = []
  176    178          for j, gz in enumerate(gzs):
  177    179              for i, y in enumerate(cands):
@@ -185,7 +187,8 @@ class GeneratedApproach:
  185    187                      tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
  186    188                      c = min(c, self._finger_clearance(state, rp[:2], y, tip,
  187    189                                                        exclude=(name, 'target_region')))
  188        -                scored.append((min(c, 0.02) - 0.001 * i - 0.004 * j, y, blk, gz))
         190 +                rot = abs(_wrap(2 * (y - ty)) / 2)   # rotation needed (mod pi), <= pi/2
         191 +                scored.append((min(c, 0.02) - 0.0005 * i - 0.004 * j - 0.004 * rot, y, blk, gz))
  189    192          scored.sort(key=lambda t: -t[0])
  190    193          return scored
  191    194  
@@ -313,7 +316,7 @@ class GeneratedApproach:
  313    316          for i, w in enumerate(wps):
  314    317              w = pts[i + 1]
  315    318              d = seg[i]
  316        -            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.1)))
         319 +            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.04)))
  317    320              for k in range(1, n + 1):
  318    321                  pt = cur + (w - cur) * k / n
  319    322                  f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
diff --git a/dbg_jd.py b/dbg_jd.py
new file mode 100644
index 0000000..6517da5
--- /dev/null
+++ b/dbg_jd.py
@@ -0,0 +1,12 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import tool_fk
           5 +cnt=int(sys.argv[3]) if len(sys.argv)>3 else None
           6 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]),options={'object_count':cnt} if cnt else None)
           7 +ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           8 +for t in range(int(sys.argv[2])):
           9 +    a=ap.get_action(obs); obs,*_=env.step(a)
          10 +q=ap._q(obs); print('q',np.round(q,2))
          11 +for i,qp in enumerate(ap.qpath[:30]):
          12 +    T=tool_fk(qp,ap._base(obs)); print(i,np.round(T[:3,3],3),round(float(np.arctan2(T[1,0],T[0,0])),2),np.round(qp-q,2)); q=qp
diff --git a/par_test.sh b/par_test.sh
index 7f6e64f..df8bca4 100755
--- a/par_test.sh
+++ b/par_test.sh
@@ -1,4 +1,4 @@
    1      1  #!/bin/bash
    2      2  # usage: par_test.sh start end nproc [count]
    3      3  S=$1; E=$2; P=${3:-8}; export CNT=$4
    4        -seq $S $((E-1)) | xargs -P $P -I{} sh -c '/opt/robocode-strict/bin/python test_approach.py {} $(({}+1)) $CNT 2>&1 | head -1'
           4 +seq $S $((E-1)) | xargs -P $P -I{} sh -c 'cd /sandbox/snap && /opt/robocode-strict/bin/python test_approach.py {} $(({}+1)) $CNT 2>&1 | head -1'
diff --git a/probe_base_1.py b/probe_base_1.py
new file mode 100644
index 0000000..d45881c
--- /dev/null
+++ b/probe_base_1.py
@@ -0,0 +1,28 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +def st(o):
           6 +    r=o.get_object_from_name('robot')
           7 +    return [round(float(o.get(r,k)),4) for k in ['pos_base_x','pos_base_y','pos_base_rot']], [round(float(o.get(r,f'joint_{i}')),3) for i in range(1,8)]
           8 +print(st(obs))
           9 +print(obs.get_object_names())
          10 +for n in obs.get_object_names():
          11 +    o=obs.get_object_from_name(n)
          12 +    try: print(n,[round(float(obs.get(o,k)),3) for k in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z']])
          13 +    except Exception as e: pass
          14 +def A(**kw):
          15 +    a=np.zeros(11,dtype=np.float32)
          16 +    for k,v in kw.items(): a[int(k[1:])]=v
          17 +    return a
          18 +o,*_=env.step(A(a0=-0.2)); print('dx-0.2',st(o))
          19 +o,*_=env.step(A(a0=0.3)); print('dx+0.3',st(o))
          20 +o,*_=env.step(A(a2=0.2)); print('rot',st(o))
          21 +for i in range(7): o,*_=env.step(A(a2=0.2))
          22 +print('rot total',st(o))
          23 +o,*_=env.step(A(a0=-0.1)); print('dx-0.1 after rot',st(o))
          24 +o,*_=env.step(A(a1=-0.1)); print('dy-0.1 after rot',st(o))
          25 +# combined
          26 +p=st(o)
          27 +o,*_=env.step(A(a1=0.1,a3=0.1)); print('combined',p,'->',st(o))
          28 +env.close()
diff --git a/probe_base_2.py b/probe_base_2.py
new file mode 100644
index 0000000..fca5e95
--- /dev/null
+++ b/probe_base_2.py
@@ -0,0 +1,32 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +from kin import tool_fk
           4 +env = make_env()
           5 +def base(o):
           6 +    r=o.get_object_from_name('robot'); return np.array([float(o.get(r,k)) for k in ['pos_base_x','pos_base_y','pos_base_rot']])
           7 +def q(o):
           8 +    r=o.get_object_from_name('robot'); return np.array([float(o.get(r,f'joint_{i}')) for i in range(1,8)])
           9 +def A(i,v):
          10 +    a=np.zeros(11,dtype=np.float32); a[i]=v; return a
          11 +for seed in [0,1,2]:
          12 +    res=[]
          13 +    for i,s in [(0,1),(0,-1),(1,1),(1,-1),(2,1),(2,-1)]:
          14 +        obs,_=env.reset(seed=seed); b0=base(obs)
          15 +        n=0
          16 +        for step_sz in [0.05,0.01,0.002]:
          17 +            for k in range(400):
          18 +                o,*_=env.step(A(i,s*step_sz)); b=base(o)
          19 +                if np.allclose(b,base(obs)): break
          20 +                obs=o
          21 +        res.append(round(float(base(obs)[i]),3))
          22 +    print('seed',seed,'+x,-x,+y,-y,+rot,-rot limits:',res)
          23 +# FK check
          24 +obs,_=env.reset(seed=0)
          25 +T0=tool_fk(q(obs),base=tuple(base(obs)))
          26 +o,*_=env.step(A(0,-0.2)); o,*_=env.step(A(1,0.15))
          27 +T1=tool_fk(q(o),base=tuple(base(o)))
          28 +print('base delta',base(o)-np.array([-0.12,0,0]),'tool delta',np.round(T1[:3,3]-T0[:3,3],4), 'Rsame',np.allclose(T0[:3,:3],T1[:3,:3]))
          29 +o,*_=env.step(A(2,0.2)); b=base(o); T2=tool_fk(q(o),base=tuple(b))
          30 +c,s=np.cos(0.2),np.sin(0.2); Rz=np.array([[c,-s,0],[s,c,0],[0,0,1]])
          31 +p=T1[:3,3]-np.array([b[0],b[1],0]); print('rot pred',np.round(Rz@p+np.array([b[0],b[1],0]),4),'fk',np.round(T2[:3,3],4))
          32 +env.close()
diff --git a/res_c4b.txt b/res_c4b.txt
new file mode 100644
index 0000000..b5bd702
--- /dev/null
+++ b/res_c4b.txt
@@ -0,0 +1,40 @@
           1 +seed 47: success=True steps=21 time=22.4s nobs=4 phase=to_place
           2 +seed 48: success=True steps=36 time=24.7s nobs=4 phase=to_place
           3 +seed 44: success=True steps=50 time=43.7s nobs=4 phase=to_place
           4 +seed 46: success=True steps=59 time=42.4s nobs=4 phase=to_place
           5 +seed 43: success=True steps=50 time=41.7s nobs=4 phase=to_place
           6 +seed 45: success=True steps=58 time=67.1s nobs=4 phase=to_place
           7 +seed 49: success=True steps=57 time=69.1s nobs=4 phase=to_place
           8 +seed 42: success=True steps=56 time=41.9s nobs=4 phase=to_place
           9 +seed 41: success=True steps=82 time=78.8s nobs=4 phase=to_place
          10 +seed 51: success=True steps=57 time=51.5s nobs=4 phase=to_place
          11 +seed 50: success=True steps=83 time=71.5s nobs=4 phase=to_place
          12 +seed 40: success=True steps=105 time=106.9s nobs=4 phase=to_place
          13 +seed 54: success=True steps=58 time=48.3s nobs=4 phase=to_place
          14 +seed 56: success=True steps=60 time=48.6s nobs=4 phase=to_place
          15 +seed 53: success=True steps=69 time=68.2s nobs=4 phase=to_place
          16 +seed 55: success=True steps=68 time=58.8s nobs=4 phase=to_place
          17 +seed 58: success=True steps=51 time=49.4s nobs=4 phase=to_place
          18 +seed 57: success=True steps=64 time=61.4s nobs=4 phase=to_place
          19 +seed 60: success=True steps=44 time=45.9s nobs=4 phase=to_place
          20 +seed 63: success=True steps=48 time=44.3s nobs=4 phase=to_place
          21 +seed 64: success=True steps=49 time=42.8s nobs=4 phase=to_place
          22 +seed 59: success=True steps=84 time=88.2s nobs=4 phase=to_place
          23 +seed 61: success=True steps=84 time=82.5s nobs=4 phase=to_place
          24 +seed 62: success=True steps=78 time=81.5s nobs=4 phase=to_place
          25 +seed 68: success=True steps=44 time=42.4s nobs=4 phase=to_place
          26 +seed 65: success=True steps=79 time=76.1s nobs=4 phase=to_place
          27 +seed 66: success=True steps=86 time=78.6s nobs=4 phase=to_place
          28 +seed 69: success=True steps=45 time=54.8s nobs=4 phase=to_place
          29 +seed 67: success=True steps=85 time=85.4s nobs=4 phase=to_place
          30 +seed 73: success=True steps=41 time=39.3s nobs=4 phase=to_place
          31 +seed 70: success=True steps=62 time=69.9s nobs=4 phase=to_place
          32 +seed 71: success=True steps=72 time=70.4s nobs=4 phase=to_place
          33 +seed 78: success=True steps=44 time=25.3s nobs=4 phase=to_place
          34 +seed 72: success=True steps=77 time=70.1s nobs=4 phase=to_place
          35 +seed 75: success=True steps=70 time=52.4s nobs=4 phase=to_place
          36 +seed 74: success=True steps=84 time=63.0s nobs=4 phase=to_place
          37 +seed 76: success=True steps=75 time=44.2s nobs=4 phase=to_place
          38 +seed 79: success=True steps=61 time=22.2s nobs=4 phase=to_place
          39 +seed 77: success=True steps=119 time=42.8s nobs=4 phase=to_place
          40 +seed 52: success=False steps=1000 time=239.7s nobs=4 phase=to_grasp
diff --git a/res_d3.txt b/res_d3.txt
index 8458174..c6b488b 100644
--- a/res_d3.txt
+++ b/res_d3.txt
@@ -46,3 +46,55 @@ seed 49: success=True steps=13 time=13.1s nobs=0 phase=to_place
   46     46  seed 43: success=True steps=28 time=43.3s nobs=1 phase=to_place
   47     47  seed 39: success=True steps=48 time=71.8s nobs=2 phase=to_place
   48     48  seed 46: success=True steps=32 time=42.2s nobs=1 phase=to_place
          49 +seed 44: success=True steps=36 time=55.7s nobs=2 phase=to_place
          50 +seed 54: success=True steps=16 time=19.2s nobs=0 phase=to_place
          51 +seed 45: success=True steps=51 time=69.1s nobs=2 phase=to_place
          52 +seed 51: success=True steps=28 time=34.2s nobs=1 phase=to_place
          53 +seed 57: success=True steps=16 time=15.6s nobs=0 phase=to_place
          54 +seed 56: success=True steps=26 time=33.0s nobs=1 phase=to_place
          55 +seed 53: success=True steps=39 time=52.3s nobs=2 phase=to_place
          56 +seed 60: success=True steps=14 time=15.2s nobs=0 phase=to_place
          57 +seed 58: success=True steps=31 time=35.5s nobs=1 phase=to_place
          58 +seed 52: success=True steps=57 time=70.7s nobs=2 phase=to_place
          59 +seed 50: success=True steps=58 time=76.8s nobs=2 phase=to_place
          60 +seed 62: success=True steps=25 time=28.1s nobs=1 phase=to_place
          61 +seed 61: success=True steps=32 time=38.3s nobs=1 phase=to_place
          62 +seed 55: success=True steps=55 time=72.9s nobs=2 phase=to_place
          63 +seed 64: success=True steps=23 time=30.2s nobs=1 phase=to_place
          64 +seed 63: success=True steps=31 time=45.9s nobs=1 phase=to_place
          65 +seed 69: success=True steps=12 time=27.1s nobs=0 phase=to_place
          66 +seed 65: success=True steps=33 time=69.2s nobs=0 phase=to_place
          67 +seed 68: success=True steps=19 time=52.4s nobs=1 phase=to_place
          68 +seed 74: success=True steps=12 time=21.8s nobs=0 phase=to_place
          69 +seed 59: success=True steps=67 time=128.2s nobs=2 phase=to_place
          70 +seed 70: success=True steps=35 time=80.7s nobs=1 phase=to_place
          71 +seed 67: success=True steps=38 time=97.8s nobs=2 phase=to_place
          72 +seed 75: success=True steps=21 time=33.6s nobs=1 phase=to_place
          73 +seed 66: success=True steps=54 time=117.5s nobs=2 phase=to_place
          74 +seed 77: success=True steps=20 time=22.5s nobs=0 phase=to_place
          75 +seed 76: success=True steps=42 time=61.8s nobs=1 phase=to_place
          76 +seed 73: success=True steps=40 time=79.2s nobs=2 phase=to_place
          77 +seed 71: success=True steps=51 time=119.3s nobs=2 phase=to_place
          78 +seed 79: success=True steps=26 time=28.1s nobs=0 phase=to_place
          79 +seed 81: success=True steps=21 time=21.5s nobs=0 phase=to_place
          80 +seed 72: success=True steps=61 time=130.9s nobs=2 phase=to_place
          81 +seed 78: success=True steps=33 time=55.4s nobs=2 phase=to_place
          82 +seed 82: success=True steps=40 time=70.7s nobs=2 phase=to_place
          83 +seed 80: success=True steps=50 time=88.3s nobs=2 phase=to_place
          84 +seed 83: success=True steps=36 time=66.6s nobs=2 phase=to_place
          85 +seed 84: success=True steps=27 time=48.2s nobs=1 phase=to_place
          86 +seed 88: success=True steps=28 time=37.8s nobs=1 phase=to_place
          87 +seed 87: success=True steps=42 time=61.2s nobs=1 phase=to_place
          88 +seed 85: success=True steps=48 time=90.9s nobs=2 phase=to_place
          89 +seed 86: success=True steps=50 time=95.9s nobs=2 phase=to_place
          90 +seed 89: success=True steps=39 time=72.0s nobs=2 phase=to_place
          91 +seed 90: success=True steps=34 time=47.2s nobs=1 phase=to_place
          92 +seed 94: success=True steps=19 time=22.0s nobs=0 phase=to_place
          93 +seed 91: success=True steps=33 time=52.4s nobs=2 phase=to_place
          94 +seed 92: success=True steps=35 time=49.4s nobs=1 phase=to_place
          95 +seed 93: success=True steps=46 time=75.1s nobs=2 phase=to_place
          96 +seed 97: success=True steps=27 time=38.3s nobs=0 phase=to_place
          97 +seed 95: success=True steps=49 time=66.6s nobs=1 phase=to_place
          98 +seed 96: success=True steps=45 time=71.6s nobs=2 phase=to_place
          99 +seed 98: success=True steps=41 time=56.3s nobs=1 phase=to_place
         100 +seed 99: success=True steps=62 time=93.8s nobs=2 phase=to_place
diff --git a/res_d4.txt b/res_d4.txt
new file mode 100644
index 0000000..3b91f82
--- /dev/null
+++ b/res_d4.txt
@@ -0,0 +1,100 @@
           1 +seed 9: success=True steps=19 time=45.5s nobs=1 phase=to_place
           2 +seed 0: success=True steps=32 time=69.0s nobs=2 phase=to_place
           3 +seed 1: success=True steps=37 time=65.6s nobs=1 phase=to_place
           4 +seed 3: success=True steps=41 time=101.9s nobs=2 phase=to_place
           5 +seed 4: success=True steps=45 time=102.8s nobs=2 phase=to_place
           6 +seed 6: success=True steps=53 time=104.9s nobs=1 phase=to_place
           7 +seed 7: success=True steps=51 time=103.6s nobs=2 phase=to_place
           8 +seed 10: success=True steps=29 time=48.2s nobs=2 phase=to_place
           9 +seed 5: success=True steps=52 time=113.6s nobs=2 phase=to_place
          10 +seed 8: success=True steps=58 time=112.5s nobs=2 phase=to_place
          11 +seed 11: success=True steps=20 time=18.5s nobs=0 phase=to_place
          12 +seed 2: success=True steps=63 time=133.4s nobs=2 phase=to_place
          13 +seed 14: success=True steps=10 time=8.7s nobs=0 phase=to_place
          14 +seed 12: success=True steps=41 time=64.8s nobs=1 phase=to_place
          15 +seed 16: success=True steps=25 time=42.0s nobs=1 phase=to_place
          16 +seed 15: success=True steps=30 time=63.5s nobs=2 phase=to_place
          17 +seed 21: success=True steps=26 time=32.4s nobs=0 phase=to_place
          18 +seed 18: success=True steps=38 time=65.4s nobs=2 phase=to_place
          19 +seed 13: success=True steps=65 time=111.7s nobs=2 phase=to_place
          20 +seed 17: success=True steps=47 time=84.2s nobs=2 phase=to_place
          21 +seed 22: success=True steps=30 time=49.2s nobs=2 phase=to_place
          22 +seed 19: success=True steps=55 time=74.5s nobs=1 phase=to_place
          23 +seed 24: success=True steps=21 time=28.4s nobs=1 phase=to_place
          24 +seed 20: success=True steps=54 time=88.7s nobs=2 phase=to_place
          25 +seed 23: success=True steps=36 time=38.7s nobs=0 phase=to_place
          26 +seed 26: success=True steps=30 time=50.6s nobs=2 phase=to_place
          27 +seed 34: success=True steps=14 time=11.4s nobs=0 phase=to_place
          28 +seed 25: success=True steps=48 time=70.1s nobs=1 phase=to_place
          29 +seed 29: success=True steps=26 time=37.6s nobs=2 phase=to_place
          30 +seed 27: success=True steps=44 time=53.0s nobs=0 phase=to_place
          31 +seed 30: success=True steps=27 time=32.2s nobs=0 phase=to_place
          32 +seed 35: success=True steps=16 time=14.8s nobs=0 phase=to_place
          33 +seed 31: success=True steps=34 time=43.7s nobs=1 phase=to_place
          34 +seed 32: success=True steps=33 time=45.4s nobs=2 phase=to_place
          35 +seed 37: success=True steps=18 time=16.8s nobs=0 phase=to_place
          36 +seed 38: success=True steps=16 time=14.6s nobs=0 phase=to_place
          37 +seed 33: success=True steps=39 time=52.6s nobs=2 phase=to_place
          38 +seed 28: success=True steps=58 time=80.5s nobs=1 phase=to_place
          39 +seed 36: success=True steps=35 time=41.8s nobs=1 phase=to_place
          40 +seed 42: success=True steps=15 time=21.5s nobs=0 phase=to_place
          41 +seed 47: success=True steps=11 time=12.9s nobs=0 phase=to_place
          42 +seed 41: success=True steps=24 time=32.7s nobs=1 phase=to_place
          43 +seed 48: success=True steps=14 time=15.3s nobs=0 phase=to_place
          44 +seed 40: success=True steps=32 time=47.2s nobs=1 phase=to_place
          45 +seed 49: success=True steps=13 time=12.6s nobs=0 phase=to_place
          46 +seed 43: success=True steps=28 time=36.9s nobs=1 phase=to_place
          47 +seed 39: success=True steps=43 time=58.0s nobs=2 phase=to_place
          48 +seed 46: success=True steps=32 time=34.8s nobs=1 phase=to_place
          49 +seed 44: success=True steps=36 time=51.7s nobs=2 phase=to_place
          50 +seed 51: success=True steps=28 time=28.7s nobs=1 phase=to_place
          51 +seed 45: success=True steps=51 time=58.2s nobs=2 phase=to_place
          52 +seed 54: success=True steps=16 time=18.2s nobs=0 phase=to_place
          53 +seed 57: success=True steps=16 time=12.0s nobs=0 phase=to_place
          54 +seed 56: success=True steps=26 time=26.4s nobs=1 phase=to_place
          55 +seed 60: success=True steps=14 time=14.0s nobs=0 phase=to_place
          56 +seed 53: success=True steps=39 time=46.9s nobs=2 phase=to_place
          57 +seed 58: success=True steps=31 time=35.6s nobs=1 phase=to_place
          58 +seed 50: success=True steps=58 time=68.4s nobs=2 phase=to_place
          59 +seed 62: success=True steps=25 time=25.7s nobs=1 phase=to_place
          60 +seed 61: success=True steps=32 time=35.3s nobs=1 phase=to_place
          61 +seed 52: success=True steps=57 time=69.0s nobs=2 phase=to_place
          62 +seed 55: success=True steps=55 time=66.5s nobs=2 phase=to_place
          63 +seed 64: success=True steps=23 time=29.9s nobs=1 phase=to_place
          64 +seed 63: success=True steps=31 time=36.2s nobs=1 phase=to_place
          65 +seed 69: success=True steps=12 time=11.3s nobs=0 phase=to_place
          66 +seed 65: success=True steps=33 time=32.6s nobs=0 phase=to_place
          67 +seed 68: success=True steps=19 time=21.8s nobs=1 phase=to_place
          68 +seed 74: success=True steps=12 time=10.5s nobs=0 phase=to_place
          69 +seed 67: success=True steps=38 time=47.8s nobs=2 phase=to_place
          70 +seed 59: success=True steps=67 time=88.4s nobs=2 phase=to_place
          71 +seed 66: success=True steps=54 time=59.5s nobs=2 phase=to_place
          72 +seed 75: success=True steps=21 time=23.5s nobs=1 phase=to_place
          73 +seed 70: success=True steps=35 time=44.4s nobs=1 phase=to_place
          74 +seed 77: success=True steps=20 time=20.3s nobs=0 phase=to_place
          75 +seed 73: success=True steps=40 time=45.2s nobs=2 phase=to_place
          76 +seed 79: success=True steps=26 time=22.5s nobs=0 phase=to_place
          77 +seed 76: success=True steps=42 time=43.4s nobs=1 phase=to_place
          78 +seed 81: success=True steps=21 time=18.0s nobs=0 phase=to_place
          79 +seed 71: success=True steps=51 time=65.4s nobs=2 phase=to_place
          80 +seed 78: success=True steps=33 time=46.3s nobs=2 phase=to_place
          81 +seed 72: success=True steps=61 time=78.5s nobs=2 phase=to_place
          82 +seed 84: success=True steps=27 time=28.5s nobs=1 phase=to_place
          83 +seed 82: success=True steps=40 time=46.2s nobs=2 phase=to_place
          84 +seed 83: success=True steps=36 time=41.1s nobs=2 phase=to_place
          85 +seed 80: success=True steps=50 time=57.8s nobs=2 phase=to_place
          86 +seed 88: success=True steps=28 time=23.7s nobs=1 phase=to_place
          87 +seed 87: success=True steps=42 time=39.8s nobs=1 phase=to_place
          88 +seed 85: success=True steps=48 time=55.3s nobs=2 phase=to_place
          89 +seed 89: success=True steps=39 time=39.6s nobs=2 phase=to_place
          90 +seed 94: success=True steps=19 time=14.8s nobs=0 phase=to_place
          91 +seed 90: success=True steps=34 time=33.7s nobs=1 phase=to_place
          92 +seed 86: success=True steps=50 time=58.8s nobs=2 phase=to_place
          93 +seed 92: success=True steps=35 time=29.4s nobs=1 phase=to_place
          94 +seed 91: success=True steps=33 time=36.7s nobs=2 phase=to_place
          95 +seed 97: success=True steps=27 time=11.4s nobs=0 phase=to_place
          96 +seed 93: success=True steps=46 time=32.3s nobs=2 phase=to_place
          97 +seed 95: success=True steps=49 time=23.6s nobs=1 phase=to_place
          98 +seed 96: success=True steps=45 time=23.2s nobs=2 phase=to_place
          99 +seed 98: success=True steps=41 time=12.7s nobs=1 phase=to_place
         100 +seed 99: success=True steps=62 time=12.6s nobs=2 phase=to_place
diff --git a/snap/approach.py b/snap/approach.py
new file mode 100644
index 0000000..67e5f1a
--- /dev/null
+++ b/snap/approach.py
@@ -0,0 +1,571 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place
           2 +the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py).
           3 +
           4 +Empirical facts (black-box probing):
           5 +- Arm mount is +0.12m along base x; the grasp/tool frame is 0.12m past the flange.
           6 +- Gripper fingers lie along the tool x axis, extending ~0.07m from the centre and
           7 +  ~0.035m below the tool frame.  Robot/held object collisions reject a step.
           8 +- Grasp (close) succeeds when tool z in [bottom+0.044, top+0.033] over the object.
           9 +- Release (open) succeeds only if the held object rests within a few mm of a surface.
          10 +"""
          11 +import numpy as np
          12 +from kin import tool_fk, tool_ik, down_R
          13 +
          14 +JN = [f'joint_{i}' for i in range(1, 8)]
          15 +MERGE_GRIP = True
          16 +CUT_CORNERS = True
          17 +STEP = 0.2             # max joint delta per step
          18 +FINGER_DOWN = 0.036    # fingertips below tool frame
          19 +F_OFF, F_HL, F_HW = 0.046, 0.024, 0.013   # finger centre offset, half length, half width
          20 +
          21 +
          22 +def _q2R(x, y, z, w):
          23 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          24 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          25 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          26 +
          27 +
          28 +def _T(p, q):
          29 +    M = np.eye(4); M[:3, :3] = _q2R(*q); M[:3, 3] = p
          30 +    return M
          31 +
          32 +
          33 +def _yaw_of_quat(q):
          34 +    x, y, z, w = q
          35 +    return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
          36 +
          37 +
          38 +def _wrap(a):
          39 +    return (a + np.pi) % (2 * np.pi) - np.pi
          40 +
          41 +
          42 +def _aabb_of_rect(c, hx, hy, yaw):
          43 +    c_, s_ = abs(np.cos(yaw)), abs(np.sin(yaw))
          44 +    return np.array(c), np.array([c_ * hx + s_ * hy, s_ * hx + c_ * hy])
          45 +
          46 +
          47 +def _gap(c1, h1, c2, h2):
          48 +    """Signed separation between two AABBs (positive = apart)."""
          49 +    return np.max(np.abs(np.asarray(c1) - np.asarray(c2)) - np.asarray(h1) - np.asarray(h2))
          50 +
          51 +
          52 +def _finger_boxes(xy, yaw):
          53 +    d = np.array([np.cos(yaw), np.sin(yaw)])
          54 +    out = []
          55 +    for sgn in (1, -1):
          56 +        out.append(_aabb_of_rect(np.asarray(xy) + sgn * F_OFF * d, F_HL, F_HW, yaw))
          57 +    return out
          58 +
          59 +
          60 +class GeneratedApproach:
          61 +    def __init__(self, action_space, observation_space, primitives):
          62 +        self.action_space = action_space
          63 +        self.observation_space = observation_space
          64 +
          65 +    # ------------------------------------------------------------ helpers
          66 +    def _obj(self, state, name):
          67 +        return state.get_object_from_name(name)
          68 +
          69 +    def _pose(self, state, name):
          70 +        o = self._obj(state, name)
          71 +        return (np.array([state.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')]),
          72 +                np.array([state.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]),
          73 +                np.array([state.get(o, f) for f in ('half_extent_x', 'half_extent_y', 'half_extent_z')]))
          74 +
          75 +    def _box(self, state, name):
          76 +        """(centre_xy, half_xy AABB, bottom z, top z)"""
          77 +        p, q, h = self._pose(state, name)
          78 +        c, hh = _aabb_of_rect(p[:2], h[0], h[1], _yaw_of_quat(q))
          79 +        return c, hh, p[2] - h[2], p[2] + h[2]
          80 +
          81 +    def _q(self, state):
          82 +        return np.array([state.get(self.robot, f) for f in JN])
          83 +
          84 +    def _base(self, state):
          85 +        return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
          86 +                state.get(self.robot, 'pos_base_rot'))
          87 +
          88 +    def _tool(self, state):
          89 +        return tool_fk(self._q(state), self._base(state))
          90 +
          91 +    def _grasped_name(self, state):
          92 +        for n in self.names:
          93 +            if state.get(self._obj(state, n), 'grasp_active') > 0.5:
          94 +                return n
          95 +        return None
          96 +
          97 +    def _max_top(self, state, exclude=()):
          98 +        t = self.table_z
          99 +        for n in self.names:
         100 +            if n in exclude:
         101 +                continue
         102 +            t = max(t, self._box(state, n)[3])
         103 +        return t
         104 +
         105 +    # ------------------------------------------------------------ planning
         106 +    def reset(self, state, info):
         107 +        self.robot = state.get_object_from_name('robot')
         108 +        self.names = sorted(n for n in state.get_object_names() if n != 'robot')
         109 +        self.obstructions = sorted(n for n in self.names if n.startswith('obstruction'))
         110 +        rp, _, rh = self._pose(state, 'target_region')
         111 +        self.table_z = rp[2] - rh[2]
         112 +        self.region = (rp, rh)
         113 +        self.tasks = [(n, 'clear') for n in self._blocking_obstructions(state)]
         114 +        self.tasks.append(('target_block', 'goal'))
         115 +        self.phase = None
         116 +        self.qpath = []
         117 +        self.last_q = None
         118 +        self.last_a = None
         119 +        self.blocked = False
         120 +        self.look = STEP
         121 +        self.fails = {}
         122 +        self.blk_moves = {}
         123 +        self.stuck = 0
         124 +        self.descent_len = 0
         125 +        self.release_tries = 0
         126 +        self.grasp_attempt = 0
         127 +        self.total_fail = 0
         128 +        self.final_grip = 0.0
         129 +        self.wp_yaw = 0.0
         130 +        self._start_task(state)
         131 +
         132 +    def _blocking_obstructions(self, state, margin=0.003):
         133 +        rp, rh = self.region
         134 +        out = []
         135 +        for n in self.obstructions:
         136 +            c, hh, _, _ = self._box(state, n)
         137 +            if _gap(c, hh, rp[:2], rh[:2]) < margin:
         138 +                out.append(n)
         139 +        return out
         140 +
         141 +    def _finger_clearance(self, state, xy, yaw, tip_z, exclude):
         142 +        """Min xy gap between finger boxes and objects whose top is above tip_z."""
         143 +        clear = 1.0
         144 +        fbs = _finger_boxes(xy, yaw)
         145 +        for n in self.names:
         146 +            if n in exclude:
         147 +                continue
         148 +            c, hh, bot, top = self._box(state, n)
         149 +            if top < tip_z - 0.002:
         150 +                continue
         151 +            for fc, fh in fbs:
         152 +                g = _gap(fc, fh, c, hh)
         153 +                if g < clear:
         154 +                    clear = g
         155 +                    if g < 0.005:
         156 +                        self._blocker = n
         157 +        return clear
         158 +
         159 +    def _choose_yaw(self, state, name, kind, attempt):
         160 +        sc = self._yaw_scores(state, name, kind)
         161 +        c = sc[attempt % len(sc)]
         162 +        self.grasp_z = c[3]
         163 +        return c[1]
         164 +
         165 +    def _yaw_scores(self, state, name, kind):
         166 +        """Sorted [(clearance score, yaw, blocker, grasp z)] for grasp candidates."""
         167 +        p, q, h = self._pose(state, name)
         168 +        oy = _yaw_of_quat(q)
         169 +        lo = p[2] - h[2] + 0.045
         170 +        hi = p[2] + h[2] + 0.032
         171 +        gzs = [self._grasp_z(p, h)]
         172 +        if hi - 0.004 > gzs[0] + 0.004:
         173 +            gzs.append(hi - 0.004)
         174 +        cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
         175 +        scored = []
         176 +        for j, gz in enumerate(gzs):
         177 +            for i, y in enumerate(cands):
         178 +                y = _wrap(2 * y) / 2  # modulo pi
         179 +                self._blocker = None
         180 +                c = self._finger_clearance(state, p[:2], y, gz - FINGER_DOWN, exclude=(name,))
         181 +                blk = self._blocker
         182 +                if kind == 'goal':
         183 +                    rp, rh = self.region
         184 +                    surf = rp[2] + rh[2]
         185 +                    tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
         186 +                    c = min(c, self._finger_clearance(state, rp[:2], y, tip,
         187 +                                                      exclude=(name, 'target_region')))
         188 +                scored.append((min(c, 0.02) - 0.001 * i - 0.004 * j, y, blk, gz))
         189 +        scored.sort(key=lambda t: -t[0])
         190 +        return scored
         191 +
         192 +    def _select_task(self, state):
         193 +        """Reorder tasks so the front one is graspable; add blockers if needed."""
         194 +        for _ in range(len(self.names)):
         195 +            name, kind = self.tasks[0]
         196 +            f = self.fails.get(name, 0)
         197 +            sc = self._yaw_scores(state, name, kind)
         198 +            if sc[0][0] > 0.002 and f < 4:
         199 +                return
         200 +            # try another pending clear task that is more graspable
         201 +            best = None
         202 +            for t in self.tasks:
         203 +                if t[1] != 'clear' or t[0] == name:
         204 +                    continue
         205 +                s2 = self._yaw_scores(state, t[0], 'clear')[0][0] - 0.01 * self.fails.get(t[0], 0)
         206 +                if best is None or s2 > best[0]:
         207 +                    best = (s2, t)
         208 +            if best is not None and best[0] > sc[0][0] - 0.01 * f + 0.001:
         209 +                self.tasks.remove(best[1])
         210 +                self.tasks.insert(0, best[1])
         211 +                continue
         212 +            # add the obstruction blocking the fingers as a new task
         213 +            blk = sc[0][2]
         214 +            if (blk is not None and blk.startswith('obstruction')
         215 +                    and all(t[0] != blk for t in self.tasks)
         216 +                    and self.blk_moves.get(blk, 0) < 2
         217 +                    and self._yaw_scores(state, blk, 'clear')[0][0] > 0.002):
         218 +                self.blk_moves[blk] = self.blk_moves.get(blk, 0) + 1
         219 +                self.tasks.insert(0, (blk, 'clear'))
         220 +                continue
         221 +            return
         222 +
         223 +    def _grasp_z(self, p, h):
         224 +        lo = p[2] - h[2] + 0.045
         225 +        hi = p[2] + h[2] + 0.032
         226 +        return 0.5 * (lo + hi) if hi > lo else hi - 0.001
         227 +
         228 +    def _free_spot(self, state, name, yaw, hold_off):
         229 +        """Pick a table spot clear of region/other objects (object + fingers)."""
         230 +        p0, _, _ = self._pose(state, name)
         231 +        c0, h, _, _ = self._box(state, name)
         232 +        others = []
         233 +        for n in self.names:
         234 +            if n == name:
         235 +                continue
         236 +            others.append(self._box(state, n))
         237 +        rp, rh = self.region
         238 +        tip = self.table_z + 0.001 + hold_off - FINGER_DOWN
         239 +        best, best_score = None, 1e9
         240 +        fb, fb_score = None, -1e9
         241 +        for x in np.linspace(0.2, 0.5, 16):
         242 +            for y in np.linspace(-0.34, 0.34, 35):
         243 +                c = np.array([x, y])
         244 +                clear = _gap(c, h, rp[:2], rh[:2]) - 0.03
         245 +                fbs = _finger_boxes(c, yaw)
         246 +                for oc, oh, bot, top in others:
         247 +                    clear = min(clear, _gap(c, h, oc, oh) - 0.02)
         248 +                    if top > tip - 0.002:
         249 +                        for fc, fh in fbs:
         250 +                            clear = min(clear, _gap(fc, fh, oc, oh) - 0.008)
         251 +                if clear > fb_score:
         252 +                    fb, fb_score = c, clear
         253 +                if clear >= 0:
         254 +                    score = np.linalg.norm(c - p0[:2])
         255 +                    if score < best_score:
         256 +                        best, best_score = c, score
         257 +        return best if best is not None else fb
         258 +
         259 +    def _transit_z(self, state, hold_off=0.0, exclude=()):
         260 +        top = self._max_top(state, exclude)
         261 +        return max(top + 0.03 + max(FINGER_DOWN, hold_off), 0.2)
         262 +
         263 +    def _start_task(self, state):
         264 +        if not self.tasks:
         265 +            self.phase = 'done'
         266 +            return
         267 +        try:
         268 +            self._select_task(state)
         269 +        except Exception:
         270 +            pass
         271 +        name, kind = self.tasks[0]
         272 +        p, q, h = self._pose(state, name)
         273 +        self.cur_obj = name
         274 +        self.grasp_yaw = self._choose_yaw(state, name, kind, self.fails.get(name, 0))
         275 +        gz = self.grasp_z
         276 +        zt = self._transit_z(state)
         277 +        tool = self._tool(state)[:3, 3]
         278 +        wps = []
         279 +        rs = 0
         280 +        if tool[2] < zt - 0.01:
         281 +            wps.append(np.array([tool[0], tool[1], zt]))
         282 +            rs = 1
         283 +        wps.append(np.array([p[0], p[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]))
         284 +        wps.append(np.array([p[0], p[1], gz]))
         285 +        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0, flip=True, rot_start=rs)
         286 +        self.phase = 'to_grasp'
         287 +
         288 +    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False, rot_start=0):
         289 +        """Cartesian waypoints -> dense joint path (IK warm-started).
         290 +        Yaw is interpolated from the current tool yaw over all but the last segment."""
         291 +        q = self._q(state)
         292 +        base = self._base(state)
         293 +        T0 = tool_fk(q, base)
         294 +        cur = T0[:3, 3]
         295 +        y0 = np.arctan2(T0[1, 0], T0[0, 0])
         296 +        dy = _wrap(yaw - y0)
         297 +        if flip and abs(dy) > np.pi / 2:
         298 +            dy = dy - np.sign(dy) * np.pi
         299 +        yaw = y0 + dy
         300 +        pts = [cur]
         301 +        for w in wps:
         302 +            pts.append(np.asarray(w, dtype=float))
         303 +        seg = [np.linalg.norm(pts[i + 1] - pts[i]) for i in range(len(wps))]
         304 +        if len(seg) - 1 <= rot_start:
         305 +            rot_start = 0
         306 +        rot0 = sum(seg[:rot_start])
         307 +        rot_len = sum(seg[rot_start:-1]) if len(seg) > 1 and sum(seg[rot_start:-1]) > 0.02 else sum(seg[rot_start:])
         308 +        rot_len = max(rot_len, 1e-6)
         309 +        path = []
         310 +        self.corners = set()
         311 +        qc = q.copy()
         312 +        travelled = 0.0
         313 +        for i, w in enumerate(wps):
         314 +            w = pts[i + 1]
         315 +            d = seg[i]
         316 +            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.1)))
         317 +            for k in range(1, n + 1):
         318 +                pt = cur + (w - cur) * k / n
         319 +                f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
         320 +                qn, ok = tool_ik(qc, pt, down_R(y0 + f * dy), base, iters=40)
         321 +                qn = qc + _wrap(qn - qc)
         322 +                path.append(qn)
         323 +                qc = qn
         324 +            travelled += d
         325 +            self.corners.add(len(path) - 1)
         326 +            cur = w
         327 +        self.qpath = path
         328 +        self.popped = 0
         329 +        self.wp_yaw = yaw
         330 +        self.final_grip = final_grip
         331 +        self.travel_grip = 1.0 if final_grip < 0 else 0.0
         332 +        self.stuck = 0
         333 +
         334 +    # ------------------------------------------------------------ control
         335 +    def _track(self, state):
         336 +        """Step along the precomputed joint path; None if done."""
         337 +        q = self._q(state)
         338 +        while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
         339 +            self.qpath.pop(0)
         340 +            self.popped += 1
         341 +        if not self.qpath:
         342 +            return None
         343 +        k = -1
         344 +        crossed = False
         345 +        for i, qp in enumerate(self.qpath):
         346 +            if np.max(np.abs(_wrap(qp - q))) <= self.look:
         347 +                if crossed and not self._safe_move(state, q, qp):
         348 +                    break
         349 +                k = i
         350 +                if (i + self.popped) in self.corners:
         351 +                    if not CUT_CORNERS or self.blocked or self.look < STEP:
         352 +                        break
         353 +                    crossed = True
         354 +            else:
         355 +                break
         356 +        a = np.zeros(11, dtype=np.float32)
         357 +        if k >= 0:
         358 +            self.qpath = self.qpath[k:]
         359 +            self.popped += k
         360 +            k = 0
         361 +            d = _wrap(self.qpath[0] - q)
         362 +            a[3:10] = d
         363 +            a[10] = self.travel_grip
         364 +            if MERGE_GRIP and len(self.qpath) == 1 and self.final_grip != 0.0:
         365 +                a[10] = self.final_grip
         366 +        else:
         367 +            d = _wrap(self.qpath[0] - q)
         368 +            a[3:10] = d * (self.look / np.max(np.abs(d)))
         369 +        return a
         370 +
         371 +    def _safe_move(self, state, q0, q1):
         372 +        """Check the joint-linear move q0->q1 keeps tool/fingers/held object
         373 +        above all nearby objects (used when cutting path corners)."""
         374 +        base = self._base(state)
         375 +        held = self._grasped_name(state)
         376 +        depth, rad = FINGER_DOWN, 0.075
         377 +        if held is not None:
         378 +            p, _, h = self._pose(state, held)
         379 +            tz = self._tool(state)[2, 3]
         380 +            depth = max(depth, tz - (p[2] - h[2]))
         381 +            rad = max(rad, np.hypot(h[0], h[1]) + 0.01)
         382 +        boxes = [self._box(state, n) for n in self.names if n != held]
         383 +        dq = _wrap(q1 - q0)
         384 +        for f in (0.25, 0.5, 0.75, 1.0):
         385 +            pt = tool_fk(q0 + f * dq, base)[:3, 3]
         386 +            low = pt[2] - depth
         387 +            if low < self.table_z + 0.01:
         388 +                return False
         389 +            for c, hh, bot, top in boxes:
         390 +                dxy = np.maximum(np.abs(pt[:2] - c) - hh, 0.0)
         391 +                if np.hypot(dxy[0], dxy[1]) < rad and low < top + 0.012:
         392 +                    return False
         393 +        return True
         394 +
         395 +    def _noop(self, grip=0.0):
         396 +        a = np.zeros(11, dtype=np.float32); a[10] = grip
         397 +        return a
         398 +
         399 +    def get_action(self, state):
         400 +        q = self._q(state)
         401 +        moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
         402 +        attempted = self.last_a is not None and np.any(np.abs(self.last_a[3:10]) > 1e-9)
         403 +        self.blocked = attempted and not moved
         404 +        if self.blocked:
         405 +            self.look = max(0.02, self.look * 0.35)
         406 +        elif attempted:
         407 +            self.look = min(STEP, self.look * 1.5)
         408 +        self.last_q = q.copy()
         409 +        try:
         410 +            a = self._policy(state)
         411 +        except Exception:
         412 +            a = self._noop()
         413 +        a = np.asarray(a, dtype=np.float32).copy()
         414 +        a[:10] = np.clip(a[:10], -STEP, STEP)
         415 +        a[10] = np.clip(a[10], -1, 1)
         416 +        self.last_a = a
         417 +        return a
         418 +
         419 +    def _policy(self, state):
         420 +        ph = self.phase
         421 +        if ph == 'done':
         422 +            if self._grasped_name(state) is None and self.tasks:
         423 +                self._start_task(state)
         424 +            return self._noop()
         425 +
         426 +        if ph == 'to_grasp':
         427 +            g = self._grasped_name(state)
         428 +            if g is not None:
         429 +                return self._on_grasped(state, g)
         430 +            if self.blocked:
         431 +                self.stuck += 1
         432 +                if self.stuck >= 2:
         433 +                    if self._tool(state)[2, 3] > self.grasp_z + 0.012:
         434 +                        # cannot get down to the grasp: try something else
         435 +                        self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         436 +                        self._start_task(state)
         437 +                        a = self._track(state)
         438 +                        return a if a is not None else self._noop()
         439 +                    self.qpath = []
         440 +            a = self._track(state)
         441 +            if a is not None:
         442 +                return a
         443 +            self.phase = 'close'
         444 +            return self._noop(-1.0)
         445 +
         446 +        if ph == 'close':
         447 +            g = self._grasped_name(state)
         448 +            if g is None:
         449 +                self.grasp_attempt += 1
         450 +                self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         451 +                self.total_fail += 1
         452 +                self._start_task(state)
         453 +                return self._track(state) if self.qpath else self._noop()
         454 +            return self._on_grasped(state, g)
         455 +
         456 +        if ph == 'to_place':
         457 +            if self._grasped_name(state) is None:
         458 +                return self._on_released(state)
         459 +            if self.blocked:
         460 +                self.stuck += 1
         461 +                if len(self.qpath) <= self.descent_len:
         462 +                    self.qpath = []
         463 +                elif self.stuck >= 3:
         464 +                    self._plan_place(state, replan=True)
         465 +            a = self._track(state)
         466 +            if a is not None:
         467 +                return a
         468 +            self.phase = 'open'
         469 +            return self._noop(1.0)
         470 +
         471 +        if ph == 'open':
         472 +            if self._grasped_name(state) is None:
         473 +                return self._on_released(state)
         474 +            self.release_tries += 1
         475 +            tool = self._tool(state)[:3, 3]
         476 +            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw, final_grip=1.0)
         477 +            self.descent_len = 2
         478 +            self.phase = 'to_place'
         479 +            if self.release_tries > 12:
         480 +                self.release_tries = 0
         481 +                self._plan_place(state, replan=True)
         482 +            a = self._track(state)
         483 +            return a if a is not None else self._noop(1.0)
         484 +
         485 +        if ph == 'retreat':
         486 +            if self.blocked:
         487 +                self.stuck += 1
         488 +                if self.stuck >= 2:
         489 +                    self.qpath = []
         490 +            a = self._track(state)
         491 +            if a is not None:
         492 +                return a
         493 +            self._next_task(state)
         494 +            a = self._track(state) if self.phase == 'to_grasp' else None
         495 +            return a if a is not None else self._noop()
         496 +
         497 +        return self._noop()
         498 +
         499 +    def _on_grasped(self, state, g):
         500 +        self.grasp_attempt = 0
         501 +        if g != self.cur_obj:
         502 +            self.tasks.insert(0, (g, 'clear'))
         503 +            self.cur_obj = g
         504 +        self._plan_place(state)
         505 +        a = self._track(state)
         506 +        return a if a is not None else self._noop()
         507 +
         508 +    def _on_released(self, state):
         509 +        self.release_tries = 0
         510 +        name, kind = self.tasks.pop(0) if self.tasks else (None, None)
         511 +        if kind == 'goal':
         512 +            self.phase = 'done'
         513 +            return self._noop()
         514 +        self._next_task(state)
         515 +        a = self._track(state) if self.phase == 'to_grasp' else None
         516 +        return a if a is not None else self._noop()
         517 +
         518 +    def _next_task(self, state):
         519 +        if self.tasks and self.tasks[0][1] == 'goal':
         520 +            for n in self._blocking_obstructions(state):
         521 +                if all(t[0] != n for t in self.tasks):
         522 +                    self.tasks.insert(0, (n, 'clear'))
         523 +        self._start_task(state)
         524 +
         525 +    def _plan_place(self, state, replan=False):
         526 +        name = self.cur_obj
         527 +        p, qo, h = self._pose(state, name)
         528 +        r = self.robot
         529 +        tf = _T([state.get(r, 'grasp_tf_x'), state.get(r, 'grasp_tf_y'), state.get(r, 'grasp_tf_z')],
         530 +                [state.get(r, 'grasp_tf_qx'), state.get(r, 'grasp_tf_qy'), state.get(r, 'grasp_tf_qz'),
         531 +                 state.get(r, 'grasp_tf_qw')])
         532 +        kind = self.tasks[0][1] if self.tasks and self.tasks[0][0] == name else 'clear'
         533 +        Ttool_now = self._tool(state)
         534 +        hold_off = Ttool_now[2, 3] - (p[2] - h[2])   # tool height above held-object bottom
         535 +        yaw = np.arctan2(Ttool_now[1, 0], Ttool_now[0, 0])
         536 +        if kind == 'goal':
         537 +            rp, rh = self.region
         538 +            xy = rp[:2]
         539 +            surf = rp[2] + rh[2]
         540 +        else:
         541 +            xy = self._free_spot(state, name, yaw, hold_off)
         542 +            if replan:
         543 +                xy = xy + np.random.uniform(-0.03, 0.03, 2)
         544 +            surf = self.table_z
         545 +        Tobj = _T([xy[0], xy[1], surf + h[2] + 0.001], qo)
         546 +        Ttool = Tobj @ np.linalg.inv(tf)
         547 +        tgt = Ttool[:3, 3]
         548 +        tyaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
         549 +        zt = self._transit_z(state, hold_off, exclude=(name,))
         550 +        tool = Ttool_now[:3, 3]
         551 +        wps = []
         552 +        if tool[2] < zt - 0.005:
         553 +            wps.append(np.array([tool[0], tool[1], zt]))
         554 +        wps += [np.array([tgt[0], tgt[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]),
         555 +                np.array([tgt[0], tgt[1], tgt[2] + 0.015])]
         556 +        self._set_path(state, wps, tyaw)
         557 +        n_before = len(self.qpath)
         558 +        self._append_descent(state, tgt, tyaw)
         559 +        self.descent_len = len(self.qpath) - n_before + 2
         560 +        self.final_grip = 1.0
         561 +        self.phase = 'to_place'
         562 +
         563 +    def _append_descent(self, state, tgt, yaw):
         564 +        base = self._base(state)
         565 +        qc = self.qpath[-1] if self.qpath else self._q(state)
         566 +        R = down_R(yaw)
         567 +        for dz in (0.008, 0.003, 0.0):
         568 +            qn, ok = tool_ik(qc, tgt + np.array([0, 0, dz]), R, base, iters=40)
         569 +            qn = qc + _wrap(qn - qc)
         570 +            self.qpath.append(qn)
         571 +            qc = qn
diff --git a/snap/env_client.py b/snap/env_client.py
new file mode 100644
index 0000000..108c884
--- /dev/null
+++ b/snap/env_client.py
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
diff --git a/snap/env_spaces.json b/snap/env_spaces.json
new file mode 100644
index 0000000..dff8dfd
--- /dev/null
+++ b/snap/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "6eefef35bfaa192f7898ebf189cf2b7d", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
diff --git a/snap/kin.py b/snap/kin.py
new file mode 100644
index 0000000..a00201a
--- /dev/null
+++ b/snap/kin.py
@@ -0,0 +1,88 @@
           1 +import numpy as np
           2 +
           3 +def _rpy(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def _T(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = _rpy(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +PI = np.pi
          13 +H = PI / 2
          14 +JOINTS = [
          15 +    _T((0, 0, 0.15643), (PI, 0, 0)),
          16 +    _T((0, 0.005375, -0.12838), (H, 0, 0)),
          17 +    _T((0, -0.21038, -0.006375), (-H, 0, 0)),
          18 +    _T((0, 0.006375, -0.21038), (H, 0, 0)),
          19 +    _T((0, -0.20843, -0.006375), (-H, 0, 0)),
          20 +    _T((0, 0.00017505, -0.10593), (H, 0, 0)),
          21 +    _T((0, -0.10593, -0.00017505), (-H, 0, 0)),
          22 +]
          23 +EE = _T((0, 0, -0.061525), (PI, 0, 0))
          24 +MOUNT = (0.12, 0.0, -0.0052)
          25 +TOOL = 0.12
          26 +HOME = np.array([0.0, -0.35, -np.pi, -2.5, 0.0, -0.87, np.pi / 2])
          27 +
          28 +def _rz(q):
          29 +    c, s = np.cos(q), np.sin(q)
          30 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          31 +
          32 +def mount_base(base):
          33 +    bx, by, br = base
          34 +    c, s = np.cos(br), np.sin(br)
          35 +    return (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
          36 +
          37 +def _chain(q, base):
          38 +    """Returns tool transform and list of (axis, origin) of joints in world."""
          39 +    bx, by, br = mount_base(base)
          40 +    T = _rz(br); T[0, 3] = bx; T[1, 3] = by; T[2, 3] = MOUNT[2]
          41 +    axes = []
          42 +    for Tj, qj in zip(JOINTS, q):
          43 +        T = T @ Tj
          44 +        axes.append((T[:3, 2].copy(), T[:3, 3].copy()))
          45 +        T = T @ _rz(qj)
          46 +    T = T @ EE
          47 +    Tt = np.eye(4); Tt[2, 3] = TOOL
          48 +    return T @ Tt, axes
          49 +
          50 +def tool_fk(q, base):
          51 +    return _chain(q, base)[0]
          52 +
          53 +def _rot_err(Rc, Rd):
          54 +    Re = Rd @ Rc.T
          55 +    v = 0.5 * np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
          56 +    return v
          57 +
          58 +def tool_ik(q0, p, R, base, iters=60, tol=1e-5, q_nom=None, k_null=0.3):
          59 +    q = np.array(q0, dtype=float)
          60 +    if q_nom is None:
          61 +        q_nom = HOME
          62 +    for it in range(iters):
          63 +        T, axes = _chain(q, base)
          64 +        e = np.concatenate([p - T[:3, 3], _rot_err(T[:3, :3], R)])
          65 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
          66 +            return q, True
          67 +        J = np.zeros((6, 7))
          68 +        pt = T[:3, 3]
          69 +        for j, (z, o) in enumerate(axes):
          70 +            J[:3, j] = np.cross(z, pt - o)
          71 +            J[3:, j] = z
          72 +        JJt = J @ J.T + 1e-6 * np.eye(6)
          73 +        Jp = J.T @ np.linalg.inv(JJt)
          74 +        dq = Jp @ e
          75 +        dn = (q_nom - q + np.pi) % (2 * np.pi) - np.pi
          76 +        dq += (np.eye(7) - Jp @ J) @ (k_null * dn)
          77 +        n = np.max(np.abs(dq))
          78 +        if n > 0.3:
          79 +            dq *= 0.3 / n
          80 +        q = q + dq
          81 +    T, _ = _chain(q, base)
          82 +    ok = np.linalg.norm(p - T[:3, 3]) < 1e-3
          83 +    return q, ok
          84 +
          85 +def down_R(yaw):
          86 +    c, s = np.cos(yaw), np.sin(yaw)
          87 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          88 +    return np.stack([x, y, z], axis=1)
diff --git a/snap/test_approach.py b/snap/test_approach.py
new file mode 100644
index 0000000..d238650
--- /dev/null
+++ b/snap/test_approach.py
@@ -0,0 +1,33 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +def run(seed, verbose=False, max_steps=None, count=None):
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed, options={'object_count': count} if count else None)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0 = time.time()
          11 +    ap.reset(obs, info)
          12 +    ms = max_steps or env.max_steps
          13 +    steps = 0
          14 +    term = False
          15 +    for steps in range(1, ms + 1):
          16 +        a = ap.get_action(obs)
          17 +        obs, r, term, trunc, info = env.step(a)
          18 +        if term or trunc:
          19 +            break
          20 +    dt = time.time() - t0
          21 +    nobs = len([n for n in obs.get_object_names() if n.startswith('obstruction')])
          22 +    env.close()
          23 +    return term, steps, dt, nobs, ap.phase
          24 +
          25 +if __name__ == '__main__':
          26 +    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          27 +    count = int(sys.argv[3]) if len(sys.argv) > 3 else None
          28 +    ok = 0
          29 +    for s in seeds:
          30 +        term, steps, dt, n, ph = run(s, count=count)
          31 +        ok += term
          32 +        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s nobs={n} phase={ph}', flush=True)
          33 +    print(f'{ok}/{len(seeds)}')
```

</details>

<a id="C018"></a>
### C018 · Whole-body IK using base y/rot for faster motions

Commit `c3ece12ba98bc730837790302447af35b041d1ae`; parents: 87f3bd01cbabfcfc7641c551be5fc5f0487a207c. Recorded author date: 2026-09-30T21:55:34+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0905](01_timeline.md#E0905): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_c3ece12_approach.py) · [Exact all-file diff](evidence/diffs/C018_c3ece12.diff)

[Previous saved controller snapshot](evidence/versions/C017_87f3bd0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 76599d7..eedb988 100644
--- a/approach.py
+++ b/approach.py
@@ -9,10 +9,11 @@ Empirical facts (black-box probing):
    9      9  - Release (open) succeeds only if the held object rests within a few mm of a surface.
   10     10  """
   11     11  import numpy as np
   12        -from kin import tool_fk, tool_ik, down_R
          12 +from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik
   13     13  
   14     14  JN = [f'joint_{i}' for i in range(1, 8)]
   15     15  MERGE_GRIP = True
          16 +WB = True
   16     17  CUT_CORNERS = True
   17     18  STEP = 0.2             # max joint delta per step
   18     19  FINGER_DOWN = 0.036    # fingertips below tool frame
@@ -81,6 +82,15 @@ class GeneratedApproach:
   81     82      def _q(self, state):
   82     83          return np.array([state.get(self.robot, f) for f in JN])
   83     84  
          85 +    def _x(self, state):
          86 +        return np.concatenate([np.array(self._base(state)), self._q(state)])
          87 +
          88 +    def _ik(self, xc, pt, R):
          89 +        if WB:
          90 +            return wb_ik(xc, pt, R, iters=40)
          91 +        q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
          92 +        return np.concatenate([xc[:3], q]), ok
          93 +
   84     94      def _base(self, state):
   85     95          return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
   86     96                  state.get(self.robot, 'pos_base_rot'))
@@ -291,9 +301,9 @@ class GeneratedApproach:
  291    301      def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False, rot_start=0):
  292    302          """Cartesian waypoints -> dense joint path (IK warm-started).
  293    303          Yaw is interpolated from the current tool yaw over all but the last segment."""
  294        -        q = self._q(state)
         304 +        q = self._x(state)
  295    305          base = self._base(state)
  296        -        T0 = tool_fk(q, base)
         306 +        T0 = wb_fk(q)
  297    307          cur = T0[:3, 3]
  298    308          y0 = np.arctan2(T0[1, 0], T0[0, 0])
  299    309          dy = _wrap(yaw - y0)
@@ -320,7 +330,7 @@ class GeneratedApproach:
  320    330              for k in range(1, n + 1):
  321    331                  pt = cur + (w - cur) * k / n
  322    332                  f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
  323        -                qn, ok = tool_ik(qc, pt, down_R(y0 + f * dy), base, iters=40)
         333 +                qn, ok = self._ik(qc, pt, down_R(y0 + f * dy))
  324    334                  qn = qc + _wrap(qn - qc)
  325    335                  path.append(qn)
  326    336                  qc = qn
@@ -337,7 +347,7 @@ class GeneratedApproach:
  337    347      # ------------------------------------------------------------ control
  338    348      def _track(self, state):
  339    349          """Step along the precomputed joint path; None if done."""
  340        -        q = self._q(state)
         350 +        q = self._x(state)
  341    351          while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
  342    352              self.qpath.pop(0)
  343    353              self.popped += 1
@@ -362,13 +372,13 @@ class GeneratedApproach:
  362    372              self.popped += k
  363    373              k = 0
  364    374              d = _wrap(self.qpath[0] - q)
  365        -            a[3:10] = d
         375 +            a[0:10] = d
  366    376              a[10] = self.travel_grip
  367    377              if MERGE_GRIP and len(self.qpath) == 1 and self.final_grip != 0.0:
  368    378                  a[10] = self.final_grip
  369    379          else:
  370    380              d = _wrap(self.qpath[0] - q)
  371        -            a[3:10] = d * (self.look / np.max(np.abs(d)))
         381 +            a[0:10] = d * (self.look / np.max(np.abs(d)))
  372    382          return a
  373    383  
  374    384      def _safe_move(self, state, q0, q1):
@@ -385,7 +395,7 @@ class GeneratedApproach:
  385    395          boxes = [self._box(state, n) for n in self.names if n != held]
  386    396          dq = _wrap(q1 - q0)
  387    397          for f in (0.25, 0.5, 0.75, 1.0):
  388        -            pt = tool_fk(q0 + f * dq, base)[:3, 3]
         398 +            pt = wb_fk(q0 + f * dq)[:3, 3]
  389    399              low = pt[2] - depth
  390    400              if low < self.table_z + 0.01:
  391    401                  return False
@@ -400,9 +410,9 @@ class GeneratedApproach:
  400    410          return a
  401    411  
  402    412      def get_action(self, state):
  403        -        q = self._q(state)
         413 +        q = self._x(state)
  404    414          moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
  405        -        attempted = self.last_a is not None and np.any(np.abs(self.last_a[3:10]) > 1e-9)
         415 +        attempted = self.last_a is not None and np.any(np.abs(self.last_a[0:10]) > 1e-9)
  406    416          self.blocked = attempted and not moved
  407    417          if self.blocked:
  408    418              self.look = max(0.02, self.look * 0.35)
@@ -565,10 +575,10 @@ class GeneratedApproach:
  565    575  
  566    576      def _append_descent(self, state, tgt, yaw):
  567    577          base = self._base(state)
  568        -        qc = self.qpath[-1] if self.qpath else self._q(state)
         578 +        qc = self.qpath[-1] if self.qpath else self._x(state)
  569    579          R = down_R(yaw)
  570    580          for dz in (0.008, 0.003, 0.0):
  571        -            qn, ok = tool_ik(qc, tgt + np.array([0, 0, dz]), R, base, iters=40)
         581 +            qn, ok = self._ik(qc, tgt + np.array([0, 0, dz]), R)
  572    582              qn = qc + _wrap(qn - qc)
  573    583              self.qpath.append(qn)
  574    584              qc = qn
diff --git a/kin.py b/kin.py
index a00201a..cb079c6 100644
--- a/kin.py
+++ b/kin.py
@@ -86,3 +86,43 @@ def down_R(yaw):
   86     86      c, s = np.cos(yaw), np.sin(yaw)
   87     87      x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
   88     88      return np.stack([x, y, z], axis=1)
          89 +
          90 +
          91 +def wb_fk(x):
          92 +    """x = [bx, by, br, q1..q7] -> tool transform."""
          93 +    return _chain(x[3:], x[:3])[0]
          94 +
          95 +
          96 +def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1.0):
          97 +    """Whole-body IK over base y, base rot and the 7 arm joints (base x fixed)."""
          98 +    x = np.array(x0, dtype=float)
          99 +    if q_nom is None:
         100 +        q_nom = HOME
         101 +    W = np.array([w_by, w_br] + [1.0] * 7)
         102 +    for it in range(iters):
         103 +        T, axes = _chain(x[3:], x[:3])
         104 +        pt = T[:3, 3]
         105 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         106 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         107 +            return x, True
         108 +        J = np.zeros((6, 9))
         109 +        J[1, 0] = 1.0
         110 +        ez = np.array([0.0, 0.0, 1.0])
         111 +        J[:3, 1] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         112 +        J[3:, 1] = ez
         113 +        for j, (z, o) in enumerate(axes):
         114 +            J[:3, 2 + j] = np.cross(z, pt - o)
         115 +            J[3:, 2 + j] = z
         116 +        JW = J * W
         117 +        Jp = JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6))
         118 +        Jp = W[:, None] * Jp
         119 +        dv = Jp @ e
         120 +        dn = np.zeros(9)
         121 +        dn[2:] = k_null * ((q_nom - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         122 +        dv += dn - Jp @ (J @ dn)
         123 +        n = np.max(np.abs(dv))
         124 +        if n > 0.3:
         125 +            dv *= 0.3 / n
         126 +        x[1:] += dv
         127 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         128 +    return x, ok
diff --git a/res_d5.txt b/res_d5.txt
new file mode 100644
index 0000000..c9d33a1
--- /dev/null
+++ b/res_d5.txt
@@ -0,0 +1,72 @@
           1 +seed 9: success=True steps=20 time=21.0s nobs=1 phase=to_place
           2 +seed 1: success=True steps=31 time=25.0s nobs=1 phase=to_place
           3 +seed 0: success=True steps=32 time=36.8s nobs=2 phase=to_place
           4 +seed 6: success=True steps=32 time=24.3s nobs=1 phase=to_place
           5 +seed 3: success=True steps=37 time=29.7s nobs=2 phase=to_place
           6 +seed 8: success=True steps=36 time=36.5s nobs=2 phase=to_place
           7 +seed 7: success=True steps=36 time=33.8s nobs=2 phase=to_place
           8 +seed 10: success=True steps=22 time=27.9s nobs=2 phase=to_place
           9 +seed 14: success=True steps=9 time=8.8s nobs=0 phase=to_place
          10 +seed 11: success=True steps=13 time=22.0s nobs=0 phase=to_place
          11 +seed 4: success=True steps=57 time=71.0s nobs=2 phase=to_place
          12 +seed 2: success=True steps=50 time=70.5s nobs=2 phase=to_place
          13 +seed 5: success=True steps=54 time=64.1s nobs=2 phase=to_place
          14 +seed 12: success=True steps=24 time=30.2s nobs=1 phase=to_place
          15 +seed 15: success=True steps=20 time=26.3s nobs=2 phase=to_place
          16 +seed 16: success=True steps=21 time=29.5s nobs=1 phase=to_place
          17 +seed 13: success=True steps=32 time=48.0s nobs=2 phase=to_place
          18 +seed 21: success=True steps=17 time=19.5s nobs=0 phase=to_place
          19 +seed 19: success=True steps=24 time=30.0s nobs=1 phase=to_place
          20 +seed 23: success=True steps=17 time=18.4s nobs=0 phase=to_place
          21 +seed 18: success=True steps=31 time=41.0s nobs=2 phase=to_place
          22 +seed 24: success=True steps=15 time=22.3s nobs=1 phase=to_place
          23 +seed 17: success=True steps=35 time=60.4s nobs=2 phase=to_place
          24 +seed 22: success=True steps=24 time=46.2s nobs=2 phase=to_place
          25 +seed 29: success=True steps=10 time=19.5s nobs=2 phase=to_place
          26 +seed 27: success=True steps=23 time=33.2s nobs=0 phase=to_place
          27 +seed 30: success=True steps=19 time=22.9s nobs=0 phase=to_place
          28 +seed 25: success=True steps=35 time=49.0s nobs=1 phase=to_place
          29 +seed 34: success=True steps=13 time=16.0s nobs=0 phase=to_place
          30 +seed 20: success=True steps=48 time=80.3s nobs=2 phase=to_place
          31 +seed 26: success=True steps=30 time=54.2s nobs=2 phase=to_place
          32 +seed 31: success=True steps=33 time=40.9s nobs=1 phase=to_place
          33 +seed 37: success=True steps=14 time=17.7s nobs=0 phase=to_place
          34 +seed 32: success=True steps=28 time=41.1s nobs=2 phase=to_place
          35 +seed 35: success=True steps=17 time=26.4s nobs=0 phase=to_place
          36 +seed 38: success=True steps=12 time=19.1s nobs=0 phase=to_place
          37 +seed 36: success=True steps=18 time=30.1s nobs=1 phase=to_place
          38 +seed 33: success=True steps=36 time=57.1s nobs=2 phase=to_place
          39 +seed 42: success=True steps=14 time=16.0s nobs=0 phase=to_place
          40 +seed 28: success=True steps=55 time=84.0s nobs=1 phase=to_place
          41 +seed 40: success=True steps=26 time=41.5s nobs=1 phase=to_place
          42 +seed 46: success=True steps=20 time=22.8s nobs=1 phase=to_place
          43 +seed 47: success=True steps=11 time=13.7s nobs=0 phase=to_place
          44 +seed 48: success=True steps=9 time=7.8s nobs=0 phase=to_place
          45 +seed 43: success=True steps=23 time=32.5s nobs=1 phase=to_place
          46 +seed 44: success=True steps=26 time=36.6s nobs=2 phase=to_place
          47 +seed 39: success=True steps=39 time=63.4s nobs=2 phase=to_place
          48 +seed 41: success=True steps=32 time=56.0s nobs=1 phase=to_place
          49 +seed 49: success=True steps=14 time=22.3s nobs=0 phase=to_place
          50 +seed 54: success=True steps=11 time=14.8s nobs=0 phase=to_place
          51 +seed 57: success=True steps=13 time=9.7s nobs=0 phase=to_place
          52 +seed 45: success=True steps=43 time=64.0s nobs=2 phase=to_place
          53 +seed 51: success=True steps=20 time=31.5s nobs=1 phase=to_place
          54 +seed 56: success=True steps=19 time=25.5s nobs=1 phase=to_place
          55 +seed 58: success=True steps=21 time=28.6s nobs=1 phase=to_place
          56 +seed 50: success=True steps=37 time=62.9s nobs=2 phase=to_place
          57 +seed 53: success=True steps=39 time=58.1s nobs=2 phase=to_place
          58 +seed 60: success=True steps=14 time=24.0s nobs=0 phase=to_place
          59 +seed 62: success=True steps=20 time=23.8s nobs=1 phase=to_place
          60 +seed 61: success=True steps=24 time=27.9s nobs=1 phase=to_place
          61 +seed 63: success=True steps=22 time=21.9s nobs=1 phase=to_place
          62 +seed 52: success=True steps=46 time=70.8s nobs=2 phase=to_place
          63 +seed 64: success=True steps=26 time=31.4s nobs=1 phase=to_place
          64 +seed 55: success=True steps=49 time=80.1s nobs=2 phase=to_place
          65 +seed 65: success=True steps=23 time=31.1s nobs=0 phase=to_place
          66 +seed 69: success=True steps=11 time=15.5s nobs=0 phase=to_place
          67 +seed 68: success=True steps=13 time=21.2s nobs=1 phase=to_place
          68 +seed 59: success=True steps=51 time=76.1s nobs=2 phase=to_place
          69 +seed 66: success=True steps=29 time=49.2s nobs=2 phase=to_place
          70 +seed 74: success=True steps=14 time=16.1s nobs=0 phase=to_place
          71 +seed 67: success=True steps=37 time=52.2s nobs=2 phase=to_place
          72 +seed 77: success=True steps=13 time=8.0s nobs=0 phase=to_place
diff --git a/snap/approach.py b/snap/approach.py
index 67e5f1a..76599d7 100644
--- a/snap/approach.py
+++ b/snap/approach.py
@@ -172,6 +172,8 @@ class GeneratedApproach:
  172    172          if hi - 0.004 > gzs[0] + 0.004:
  173    173              gzs.append(hi - 0.004)
  174    174          cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
         175 +        T = self._tool(state)
         176 +        ty = np.arctan2(T[1, 0], T[0, 0])
  175    177          scored = []
  176    178          for j, gz in enumerate(gzs):
  177    179              for i, y in enumerate(cands):
@@ -185,7 +187,8 @@ class GeneratedApproach:
  185    187                      tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
  186    188                      c = min(c, self._finger_clearance(state, rp[:2], y, tip,
  187    189                                                        exclude=(name, 'target_region')))
  188        -                scored.append((min(c, 0.02) - 0.001 * i - 0.004 * j, y, blk, gz))
         190 +                rot = abs(_wrap(2 * (y - ty)) / 2)   # rotation needed (mod pi), <= pi/2
         191 +                scored.append((min(c, 0.02) - 0.0005 * i - 0.004 * j - 0.004 * rot, y, blk, gz))
  189    192          scored.sort(key=lambda t: -t[0])
  190    193          return scored
  191    194  
@@ -313,7 +316,7 @@ class GeneratedApproach:
  313    316          for i, w in enumerate(wps):
  314    317              w = pts[i + 1]
  315    318              d = seg[i]
  316        -            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.1)))
         319 +            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.04)))
  317    320              for k in range(1, n + 1):
  318    321                  pt = cur + (w - cur) * k / n
  319    322                  f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
```

</details>

<a id="C019"></a>
### C019 · wb_ik2: base x (bounded) + extended nominal posture

Commit `4d813a288903f8cb57b0ad618ccb302cc741dba6`; parents: c3ece12ba98bc730837790302447af35b041d1ae. Recorded author date: 2026-09-30T22:16:26+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E1012](01_timeline.md#E1012): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_4d813a2_approach.py) · [Exact all-file diff](evidence/diffs/C019_4d813a2.diff)

[Previous saved controller snapshot](evidence/versions/C018_c3ece12_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index eedb988..e410e51 100644
--- a/approach.py
+++ b/approach.py
@@ -9,7 +9,7 @@ Empirical facts (black-box probing):
    9      9  - Release (open) succeeds only if the held object rests within a few mm of a surface.
   10     10  """
   11     11  import numpy as np
   12        -from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik
          12 +from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik, wb_ik2
   13     13  
   14     14  JN = [f'joint_{i}' for i in range(1, 8)]
   15     15  MERGE_GRIP = True
@@ -87,7 +87,7 @@ class GeneratedApproach:
   87     87  
   88     88      def _ik(self, xc, pt, R):
   89     89          if WB:
   90        -            return wb_ik(xc, pt, R, iters=40)
          90 +            return wb_ik2(xc, pt, R, iters=40)
   91     91          q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
   92     92          return np.concatenate([xc[:3], q]), ok
   93     93  
diff --git a/kin.py b/kin.py
index cb079c6..b360a71 100644
--- a/kin.py
+++ b/kin.py
@@ -126,3 +126,47 @@ def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1
  126    126          x[1:] += dv
  127    127      ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
  128    128      return x, ok
         129 +
         130 +
         131 +Q_NOM = np.array([0.0, 0.3, -np.pi, -2.15, 0.0, -0.69, 0.0])
         132 +K_NOM = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
         133 +
         134 +
         135 +def wb_ik2(x0, p, R, iters=40, tol=1e-5, k_null=0.3, bx_max=-0.12, w_base=1.0):
         136 +    """Whole-body IK over base x (<= bx_max), y, rot and the 7 arm joints.
         137 +    Null space pulls the arm to an extended nominal posture Q_NOM."""
         138 +    x = np.array(x0, dtype=float)
         139 +    ez = np.array([0.0, 0.0, 1.0])
         140 +    for it in range(iters):
         141 +        T, axes = _chain(x[3:], x[:3])
         142 +        pt = T[:3, 3]
         143 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         144 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         145 +            return x, True
         146 +        J = np.zeros((6, 10))
         147 +        J[0, 0] = 1.0
         148 +        J[1, 1] = 1.0
         149 +        J[:3, 2] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         150 +        J[3:, 2] = ez
         151 +        for j, (z, o) in enumerate(axes):
         152 +            J[:3, 3 + j] = np.cross(z, pt - o)
         153 +            J[3:, 3 + j] = z
         154 +        dn = np.zeros(10)
         155 +        dn[3:] = k_null * K_NOM * ((Q_NOM - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         156 +        W = np.array([w_base, w_base, w_base] + [1.0] * 7)
         157 +        for _ in range(2):
         158 +            JW = J * W
         159 +            Jp = W[:, None] * (JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6)))
         160 +            dv = Jp @ e + dn - Jp @ (J @ dn)
         161 +            n = np.max(np.abs(dv))
         162 +            if n > 0.3:
         163 +                dv *= 0.3 / n
         164 +            if x[0] + dv[0] > bx_max + 1e-9 and W[0] > 0:
         165 +                W[0] = 0.0
         166 +                x[0] = min(x[0], bx_max)
         167 +                continue
         168 +            break
         169 +        x += dv
         170 +        x[0] = min(x[0], bx_max) if x0[0] <= bx_max + 1e-9 else x[0]
         171 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         172 +    return x, ok
diff --git a/probe52.py b/probe52.py
new file mode 100644
index 0000000..fd4227f
--- /dev/null
+++ b/probe52.py
@@ -0,0 +1,24 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import tool_fk, tool_ik, down_R, wb_ik, wb_fk
           5 +seed=int(sys.argv[1]); T=int(sys.argv[2])
           6 +def replay():
           7 +    env=make_env(); obs,info=env.reset(seed=seed)
           8 +    ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           9 +    for t in range(T):
          10 +        a=ap.get_action(obs); obs,*_=env.step(a)
          11 +    return env,obs,ap
          12 +env,obs,ap=replay()
          13 +x=ap._x(obs); Tt=wb_fk(x); yaw=np.arctan2(Tt[1,0],Tt[0,0])
          14 +print('x',np.round(x,3),'tool',np.round(Tt[:3,3],3),'yaw',round(yaw,2))
          15 +for mode in ['arm','wb']:
          16 +  for dz in [0.005,0.02]:
          17 +    env.close(); env,obs,ap=replay()
          18 +    tgt=Tt[:3,3]+np.array([0,0,dz])
          19 +    if mode=='arm':
          20 +        q,ok=tool_ik(x[3:],tgt,down_R(yaw),tuple(x[:3])); xn=np.concatenate([x[:3],q])
          21 +    else:
          22 +        xn,ok=wb_ik(x,tgt,down_R(yaw))
          23 +    a=np.zeros(11,dtype=np.float32); a[0:10]=np.clip(xn-x,-0.2,0.2)
          24 +    obs2,*_=env.step(a); print(mode,dz,'moved',not np.allclose(ap._x(obs2),x),np.round(xn-x,3))
diff --git a/res_c4c.txt b/res_c4c.txt
new file mode 100644
index 0000000..4a8399e
--- /dev/null
+++ b/res_c4c.txt
@@ -0,0 +1,13 @@
           1 +seed 47: success=True steps=24 time=22.1s nobs=4 phase=to_place
           2 +seed 48: success=True steps=31 time=27.4s nobs=4 phase=to_place
           3 +seed 43: success=True steps=30 time=28.7s nobs=4 phase=to_place
           4 +seed 46: success=True steps=48 time=57.1s nobs=4 phase=to_place
           5 +seed 44: success=True steps=46 time=56.3s nobs=4 phase=to_place
           6 +seed 45: success=True steps=51 time=77.4s nobs=4 phase=to_place
           7 +seed 42: success=True steps=64 time=81.8s nobs=4 phase=to_place
           8 +seed 49: success=True steps=59 time=74.5s nobs=4 phase=to_place
           9 +seed 41: success=True steps=70 time=79.9s nobs=4 phase=to_place
          10 +seed 40: success=True steps=70 time=96.4s nobs=4 phase=to_place
          11 +seed 50: success=True steps=61 time=69.9s nobs=4 phase=to_place
          12 +seed 51: success=True steps=53 time=56.9s nobs=4 phase=to_place
          13 +Terminated
diff --git a/res_c4d.txt b/res_c4d.txt
new file mode 100644
index 0000000..0185009
--- /dev/null
+++ b/res_c4d.txt
@@ -0,0 +1,40 @@
           1 +seed 47: success=True steps=19 time=29.5s nobs=4 phase=to_place
           2 +seed 43: success=True steps=26 time=61.2s nobs=4 phase=to_place
           3 +seed 48: success=True steps=27 time=46.4s nobs=4 phase=to_place
           4 +seed 44: success=True steps=32 time=75.1s nobs=4 phase=to_place
           5 +seed 45: success=True steps=41 time=75.6s nobs=4 phase=to_place
           6 +seed 40: success=True steps=50 time=92.8s nobs=4 phase=to_place
           7 +seed 42: success=True steps=48 time=83.6s nobs=4 phase=to_place
           8 +seed 46: success=True steps=46 time=78.0s nobs=4 phase=to_place
           9 +seed 49: success=True steps=49 time=81.0s nobs=4 phase=to_place
          10 +seed 41: success=True steps=82 time=116.9s nobs=4 phase=to_place
          11 +seed 51: success=True steps=44 time=57.3s nobs=4 phase=to_place
          12 +seed 50: success=True steps=49 time=64.2s nobs=4 phase=to_place
          13 +seed 53: success=True steps=43 time=59.6s nobs=4 phase=to_place
          14 +seed 54: success=True steps=36 time=50.0s nobs=4 phase=to_place
          15 +seed 58: success=True steps=29 time=39.8s nobs=4 phase=to_place
          16 +seed 52: success=True steps=55 time=76.6s nobs=4 phase=to_place
          17 +seed 56: success=True steps=38 time=48.1s nobs=4 phase=to_place
          18 +seed 55: success=True steps=39 time=52.9s nobs=4 phase=to_place
          19 +seed 57: success=True steps=39 time=61.0s nobs=4 phase=to_place
          20 +seed 60: success=True steps=30 time=45.7s nobs=4 phase=to_place
          21 +seed 59: success=True steps=39 time=59.5s nobs=4 phase=to_place
          22 +seed 63: success=True steps=28 time=40.9s nobs=4 phase=to_place
          23 +seed 64: success=True steps=29 time=39.4s nobs=4 phase=to_place
          24 +seed 61: success=True steps=53 time=68.5s nobs=4 phase=to_place
          25 +seed 68: success=True steps=36 time=38.1s nobs=4 phase=to_place
          26 +seed 69: success=True steps=27 time=31.1s nobs=4 phase=to_place
          27 +seed 66: success=True steps=42 time=45.8s nobs=4 phase=to_place
          28 +seed 65: success=True steps=42 time=52.1s nobs=4 phase=to_place
          29 +seed 67: success=True steps=43 time=54.1s nobs=4 phase=to_place
          30 +seed 62: success=True steps=64 time=89.9s nobs=4 phase=to_place
          31 +seed 70: success=True steps=38 time=50.7s nobs=4 phase=to_place
          32 +seed 73: success=True steps=26 time=34.4s nobs=4 phase=to_place
          33 +seed 71: success=True steps=50 time=53.9s nobs=4 phase=to_place
          34 +seed 72: success=True steps=50 time=50.1s nobs=4 phase=to_place
          35 +seed 78: success=True steps=35 time=16.3s nobs=4 phase=to_place
          36 +seed 76: success=True steps=45 time=25.7s nobs=4 phase=to_place
          37 +seed 74: success=True steps=47 time=38.4s nobs=4 phase=to_place
          38 +seed 79: success=True steps=41 time=16.2s nobs=4 phase=to_place
          39 +seed 75: success=True steps=94 time=33.3s nobs=4 phase=to_place
          40 +seed 77: success=False steps=1000 time=73.2s nobs=4 phase=to_place
diff --git a/res_d5.txt b/res_d5.txt
index c9d33a1..74687b4 100644
--- a/res_d5.txt
+++ b/res_d5.txt
@@ -70,3 +70,31 @@ seed 66: success=True steps=29 time=49.2s nobs=2 phase=to_place
   70     70  seed 74: success=True steps=14 time=16.1s nobs=0 phase=to_place
   71     71  seed 67: success=True steps=37 time=52.2s nobs=2 phase=to_place
   72     72  seed 77: success=True steps=13 time=8.0s nobs=0 phase=to_place
          73 +seed 70: success=True steps=31 time=41.5s nobs=1 phase=to_place
          74 +seed 73: success=True steps=29 time=36.3s nobs=2 phase=to_place
          75 +seed 75: success=True steps=21 time=32.2s nobs=1 phase=to_place
          76 +seed 79: success=True steps=12 time=25.9s nobs=0 phase=to_place
          77 +seed 81: success=True steps=13 time=23.9s nobs=0 phase=to_place
          78 +seed 78: success=True steps=22 time=40.5s nobs=2 phase=to_place
          79 +seed 76: success=True steps=34 time=49.8s nobs=1 phase=to_place
          80 +seed 72: success=True steps=45 time=74.3s nobs=2 phase=to_place
          81 +seed 83: success=True steps=21 time=35.1s nobs=2 phase=to_place
          82 +seed 71: success=True steps=56 time=82.1s nobs=2 phase=to_place
          83 +seed 80: success=True steps=27 time=47.3s nobs=2 phase=to_place
          84 +seed 84: success=True steps=27 time=28.5s nobs=1 phase=to_place
          85 +seed 82: success=True steps=40 time=63.1s nobs=2 phase=to_place
          86 +seed 85: success=True steps=29 time=39.1s nobs=2 phase=to_place
          87 +seed 90: success=True steps=20 time=22.2s nobs=1 phase=to_place
          88 +seed 86: success=True steps=33 time=43.6s nobs=2 phase=to_place
          89 +seed 88: success=True steps=28 time=33.9s nobs=1 phase=to_place
          90 +seed 94: success=True steps=17 time=23.2s nobs=0 phase=to_place
          91 +seed 92: success=True steps=22 time=30.3s nobs=1 phase=to_place
          92 +seed 87: success=True steps=44 time=52.3s nobs=1 phase=to_place
          93 +seed 97: success=True steps=16 time=11.0s nobs=0 phase=to_place
          94 +seed 91: success=True steps=30 time=40.3s nobs=2 phase=to_place
          95 +seed 95: success=True steps=27 time=23.6s nobs=1 phase=to_place
          96 +seed 89: success=True steps=44 time=52.2s nobs=2 phase=to_place
          97 +seed 93: success=True steps=43 time=38.7s nobs=2 phase=to_place
          98 +seed 98: success=True steps=37 time=14.7s nobs=1 phase=to_place
          99 +seed 96: success=True steps=45 time=26.2s nobs=2 phase=to_place
         100 +seed 99: success=True steps=41 time=12.3s nobs=2 phase=to_place
diff --git a/res_d6.txt b/res_d6.txt
new file mode 100644
index 0000000..0fe37f0
--- /dev/null
+++ b/res_d6.txt
@@ -0,0 +1,100 @@
           1 +seed 9: success=True steps=18 time=29.7s nobs=1 phase=to_place
           2 +seed 6: success=True steps=20 time=35.9s nobs=1 phase=to_place
           3 +seed 1: success=True steps=24 time=45.9s nobs=1 phase=to_place
           4 +seed 3: success=True steps=19 time=44.1s nobs=2 phase=to_place
           5 +seed 7: success=True steps=20 time=35.8s nobs=2 phase=to_place
           6 +seed 2: success=True steps=28 time=62.7s nobs=2 phase=to_place
           7 +seed 0: success=True steps=28 time=48.1s nobs=2 phase=to_place
           8 +seed 11: success=True steps=10 time=9.9s nobs=0 phase=to_place
           9 +seed 8: success=True steps=29 time=50.7s nobs=2 phase=to_place
          10 +seed 4: success=True steps=41 time=67.6s nobs=2 phase=to_place
          11 +seed 10: success=True steps=18 time=23.6s nobs=2 phase=to_place
          12 +seed 14: success=True steps=8 time=4.8s nobs=0 phase=to_place
          13 +seed 5: success=True steps=38 time=59.6s nobs=2 phase=to_place
          14 +seed 12: success=True steps=17 time=20.8s nobs=1 phase=to_place
          15 +seed 13: success=True steps=24 time=29.9s nobs=2 phase=to_place
          16 +seed 16: success=True steps=19 time=20.3s nobs=1 phase=to_place
          17 +seed 15: success=True steps=20 time=26.4s nobs=2 phase=to_place
          18 +seed 21: success=True steps=8 time=9.6s nobs=0 phase=to_place
          19 +seed 18: success=True steps=20 time=29.7s nobs=2 phase=to_place
          20 +seed 19: success=True steps=21 time=25.3s nobs=1 phase=to_place
          21 +seed 23: success=True steps=8 time=10.4s nobs=0 phase=to_place
          22 +seed 17: success=True steps=26 time=37.5s nobs=2 phase=to_place
          23 +seed 24: success=True steps=10 time=14.3s nobs=1 phase=to_place
          24 +seed 22: success=True steps=17 time=26.7s nobs=2 phase=to_place
          25 +seed 20: success=True steps=26 time=41.1s nobs=2 phase=to_place
          26 +seed 27: success=True steps=9 time=8.7s nobs=0 phase=to_place
          27 +seed 29: success=True steps=7 time=11.6s nobs=2 phase=to_place
          28 +seed 25: success=True steps=21 time=29.0s nobs=1 phase=to_place
          29 +seed 30: success=True steps=9 time=9.6s nobs=0 phase=to_place
          30 +seed 26: success=True steps=20 time=29.8s nobs=2 phase=to_place
          31 +seed 34: success=True steps=9 time=12.4s nobs=0 phase=to_place
          32 +seed 28: success=True steps=30 time=39.4s nobs=1 phase=to_place
          33 +seed 35: success=True steps=10 time=11.7s nobs=0 phase=to_place
          34 +seed 31: success=True steps=21 time=34.5s nobs=1 phase=to_place
          35 +seed 37: success=True steps=10 time=12.9s nobs=0 phase=to_place
          36 +seed 38: success=True steps=9 time=8.4s nobs=0 phase=to_place
          37 +seed 36: success=True steps=15 time=21.1s nobs=1 phase=to_place
          38 +seed 32: success=True steps=30 time=46.8s nobs=2 phase=to_place
          39 +seed 33: success=True steps=28 time=49.8s nobs=2 phase=to_place
          40 +seed 42: success=True steps=9 time=23.2s nobs=0 phase=to_place
          41 +seed 47: success=True steps=7 time=13.7s nobs=0 phase=to_place
          42 +seed 48: success=True steps=8 time=12.9s nobs=0 phase=to_place
          43 +seed 49: success=True steps=8 time=11.7s nobs=0 phase=to_place
          44 +seed 41: success=True steps=21 time=42.8s nobs=1 phase=to_place
          45 +seed 43: success=True steps=19 time=41.9s nobs=1 phase=to_place
          46 +seed 46: success=True steps=15 time=32.9s nobs=1 phase=to_place
          47 +seed 39: success=True steps=30 time=66.9s nobs=2 phase=to_place
          48 +seed 40: success=True steps=35 time=63.7s nobs=1 phase=to_place
          49 +seed 44: success=True steps=25 time=61.3s nobs=2 phase=to_place
          50 +seed 54: success=True steps=10 time=18.6s nobs=0 phase=to_place
          51 +seed 57: success=True steps=8 time=11.1s nobs=0 phase=to_place
          52 +seed 51: success=True steps=19 time=39.3s nobs=1 phase=to_place
          53 +seed 45: success=True steps=34 time=69.1s nobs=2 phase=to_place
          54 +seed 58: success=True steps=8 time=16.9s nobs=1 phase=to_place
          55 +seed 56: success=True steps=16 time=27.3s nobs=1 phase=to_place
          56 +seed 60: success=True steps=10 time=12.9s nobs=0 phase=to_place
          57 +seed 50: success=True steps=34 time=67.5s nobs=2 phase=to_place
          58 +seed 53: success=True steps=29 time=59.7s nobs=2 phase=to_place
          59 +seed 55: success=True steps=29 time=51.9s nobs=2 phase=to_place
          60 +seed 61: success=True steps=19 time=25.9s nobs=1 phase=to_place
          61 +seed 62: success=True steps=16 time=24.1s nobs=1 phase=to_place
          62 +seed 65: success=True steps=9 time=8.5s nobs=0 phase=to_place
          63 +seed 63: success=True steps=18 time=24.5s nobs=1 phase=to_place
          64 +seed 59: success=True steps=30 time=49.7s nobs=2 phase=to_place
          65 +seed 64: success=True steps=21 time=28.4s nobs=1 phase=to_place
          66 +seed 68: success=True steps=10 time=12.1s nobs=1 phase=to_place
          67 +seed 69: success=True steps=9 time=7.8s nobs=0 phase=to_place
          68 +seed 66: success=True steps=27 time=34.8s nobs=2 phase=to_place
          69 +seed 67: success=True steps=24 time=31.3s nobs=2 phase=to_place
          70 +seed 74: success=True steps=9 time=9.8s nobs=0 phase=to_place
          71 +seed 70: success=True steps=23 time=24.5s nobs=1 phase=to_place
          72 +seed 77: success=True steps=9 time=8.5s nobs=0 phase=to_place
          73 +seed 79: success=True steps=9 time=7.3s nobs=0 phase=to_place
          74 +seed 72: success=True steps=29 time=39.6s nobs=2 phase=to_place
          75 +seed 76: success=True steps=21 time=27.1s nobs=1 phase=to_place
          76 +seed 73: success=True steps=26 time=38.2s nobs=2 phase=to_place
          77 +seed 75: success=True steps=19 time=23.2s nobs=1 phase=to_place
          78 +seed 71: success=True steps=38 time=48.3s nobs=2 phase=to_place
          79 +seed 81: success=True steps=8 time=6.6s nobs=0 phase=to_place
          80 +seed 78: success=True steps=32 time=38.5s nobs=2 phase=to_place
          81 +seed 80: success=True steps=26 time=33.9s nobs=2 phase=to_place
          82 +seed 83: success=True steps=19 time=27.2s nobs=2 phase=to_place
          83 +seed 84: success=True steps=27 time=27.4s nobs=1 phase=to_place
          84 +seed 88: success=True steps=20 time=18.8s nobs=1 phase=to_place
          85 +seed 85: success=True steps=24 time=30.3s nobs=2 phase=to_place
          86 +seed 87: success=True steps=25 time=28.4s nobs=1 phase=to_place
          87 +seed 82: success=True steps=36 time=45.3s nobs=2 phase=to_place
          88 +seed 86: success=True steps=27 time=36.0s nobs=2 phase=to_place
          89 +seed 90: success=True steps=17 time=18.3s nobs=1 phase=to_place
          90 +seed 91: success=True steps=18 time=25.4s nobs=2 phase=to_place
          91 +seed 94: success=True steps=9 time=8.9s nobs=0 phase=to_place
          92 +seed 89: success=True steps=31 time=41.2s nobs=2 phase=to_place
          93 +seed 92: success=True steps=19 time=25.8s nobs=1 phase=to_place
          94 +seed 97: success=True steps=11 time=7.3s nobs=0 phase=to_place
          95 +seed 95: success=True steps=18 time=16.4s nobs=1 phase=to_place
          96 +seed 96: success=True steps=27 time=15.3s nobs=2 phase=to_place
          97 +seed 93: success=True steps=39 time=30.1s nobs=2 phase=to_place
          98 +seed 98: success=True steps=22 time=6.5s nobs=1 phase=to_place
          99 +seed 99: success=True steps=29 time=8.8s nobs=2 phase=to_place
         100 +seed 52: success=False steps=1000 time=248.6s nobs=2 phase=to_place
diff --git a/snap/approach.py b/snap/approach.py
index 76599d7..eedb988 100644
--- a/snap/approach.py
+++ b/snap/approach.py
@@ -9,10 +9,11 @@ Empirical facts (black-box probing):
    9      9  - Release (open) succeeds only if the held object rests within a few mm of a surface.
   10     10  """
   11     11  import numpy as np
   12        -from kin import tool_fk, tool_ik, down_R
          12 +from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik
   13     13  
   14     14  JN = [f'joint_{i}' for i in range(1, 8)]
   15     15  MERGE_GRIP = True
          16 +WB = True
   16     17  CUT_CORNERS = True
   17     18  STEP = 0.2             # max joint delta per step
   18     19  FINGER_DOWN = 0.036    # fingertips below tool frame
@@ -81,6 +82,15 @@ class GeneratedApproach:
   81     82      def _q(self, state):
   82     83          return np.array([state.get(self.robot, f) for f in JN])
   83     84  
          85 +    def _x(self, state):
          86 +        return np.concatenate([np.array(self._base(state)), self._q(state)])
          87 +
          88 +    def _ik(self, xc, pt, R):
          89 +        if WB:
          90 +            return wb_ik(xc, pt, R, iters=40)
          91 +        q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
          92 +        return np.concatenate([xc[:3], q]), ok
          93 +
   84     94      def _base(self, state):
   85     95          return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
   86     96                  state.get(self.robot, 'pos_base_rot'))
@@ -291,9 +301,9 @@ class GeneratedApproach:
  291    301      def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False, rot_start=0):
  292    302          """Cartesian waypoints -> dense joint path (IK warm-started).
  293    303          Yaw is interpolated from the current tool yaw over all but the last segment."""
  294        -        q = self._q(state)
         304 +        q = self._x(state)
  295    305          base = self._base(state)
  296        -        T0 = tool_fk(q, base)
         306 +        T0 = wb_fk(q)
  297    307          cur = T0[:3, 3]
  298    308          y0 = np.arctan2(T0[1, 0], T0[0, 0])
  299    309          dy = _wrap(yaw - y0)
@@ -320,7 +330,7 @@ class GeneratedApproach:
  320    330              for k in range(1, n + 1):
  321    331                  pt = cur + (w - cur) * k / n
  322    332                  f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
  323        -                qn, ok = tool_ik(qc, pt, down_R(y0 + f * dy), base, iters=40)
         333 +                qn, ok = self._ik(qc, pt, down_R(y0 + f * dy))
  324    334                  qn = qc + _wrap(qn - qc)
  325    335                  path.append(qn)
  326    336                  qc = qn
@@ -337,7 +347,7 @@ class GeneratedApproach:
  337    347      # ------------------------------------------------------------ control
  338    348      def _track(self, state):
  339    349          """Step along the precomputed joint path; None if done."""
  340        -        q = self._q(state)
         350 +        q = self._x(state)
  341    351          while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
  342    352              self.qpath.pop(0)
  343    353              self.popped += 1
@@ -362,13 +372,13 @@ class GeneratedApproach:
  362    372              self.popped += k
  363    373              k = 0
  364    374              d = _wrap(self.qpath[0] - q)
  365        -            a[3:10] = d
         375 +            a[0:10] = d
  366    376              a[10] = self.travel_grip
  367    377              if MERGE_GRIP and len(self.qpath) == 1 and self.final_grip != 0.0:
  368    378                  a[10] = self.final_grip
  369    379          else:
  370    380              d = _wrap(self.qpath[0] - q)
  371        -            a[3:10] = d * (self.look / np.max(np.abs(d)))
         381 +            a[0:10] = d * (self.look / np.max(np.abs(d)))
  372    382          return a
  373    383  
  374    384      def _safe_move(self, state, q0, q1):
@@ -385,7 +395,7 @@ class GeneratedApproach:
  385    395          boxes = [self._box(state, n) for n in self.names if n != held]
  386    396          dq = _wrap(q1 - q0)
  387    397          for f in (0.25, 0.5, 0.75, 1.0):
  388        -            pt = tool_fk(q0 + f * dq, base)[:3, 3]
         398 +            pt = wb_fk(q0 + f * dq)[:3, 3]
  389    399              low = pt[2] - depth
  390    400              if low < self.table_z + 0.01:
  391    401                  return False
@@ -400,9 +410,9 @@ class GeneratedApproach:
  400    410          return a
  401    411  
  402    412      def get_action(self, state):
  403        -        q = self._q(state)
         413 +        q = self._x(state)
  404    414          moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
  405        -        attempted = self.last_a is not None and np.any(np.abs(self.last_a[3:10]) > 1e-9)
         415 +        attempted = self.last_a is not None and np.any(np.abs(self.last_a[0:10]) > 1e-9)
  406    416          self.blocked = attempted and not moved
  407    417          if self.blocked:
  408    418              self.look = max(0.02, self.look * 0.35)
@@ -565,10 +575,10 @@ class GeneratedApproach:
  565    575  
  566    576      def _append_descent(self, state, tgt, yaw):
  567    577          base = self._base(state)
  568        -        qc = self.qpath[-1] if self.qpath else self._q(state)
         578 +        qc = self.qpath[-1] if self.qpath else self._x(state)
  569    579          R = down_R(yaw)
  570    580          for dz in (0.008, 0.003, 0.0):
  571        -            qn, ok = tool_ik(qc, tgt + np.array([0, 0, dz]), R, base, iters=40)
         581 +            qn, ok = self._ik(qc, tgt + np.array([0, 0, dz]), R)
  572    582              qn = qc + _wrap(qn - qc)
  573    583              self.qpath.append(qn)
  574    584              qc = qn
diff --git a/snap/kin.py b/snap/kin.py
index a00201a..cb079c6 100644
--- a/snap/kin.py
+++ b/snap/kin.py
@@ -86,3 +86,43 @@ def down_R(yaw):
   86     86      c, s = np.cos(yaw), np.sin(yaw)
   87     87      x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
   88     88      return np.stack([x, y, z], axis=1)
          89 +
          90 +
          91 +def wb_fk(x):
          92 +    """x = [bx, by, br, q1..q7] -> tool transform."""
          93 +    return _chain(x[3:], x[:3])[0]
          94 +
          95 +
          96 +def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1.0):
          97 +    """Whole-body IK over base y, base rot and the 7 arm joints (base x fixed)."""
          98 +    x = np.array(x0, dtype=float)
          99 +    if q_nom is None:
         100 +        q_nom = HOME
         101 +    W = np.array([w_by, w_br] + [1.0] * 7)
         102 +    for it in range(iters):
         103 +        T, axes = _chain(x[3:], x[:3])
         104 +        pt = T[:3, 3]
         105 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         106 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         107 +            return x, True
         108 +        J = np.zeros((6, 9))
         109 +        J[1, 0] = 1.0
         110 +        ez = np.array([0.0, 0.0, 1.0])
         111 +        J[:3, 1] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         112 +        J[3:, 1] = ez
         113 +        for j, (z, o) in enumerate(axes):
         114 +            J[:3, 2 + j] = np.cross(z, pt - o)
         115 +            J[3:, 2 + j] = z
         116 +        JW = J * W
         117 +        Jp = JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6))
         118 +        Jp = W[:, None] * Jp
         119 +        dv = Jp @ e
         120 +        dn = np.zeros(9)
         121 +        dn[2:] = k_null * ((q_nom - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         122 +        dv += dn - Jp @ (J @ dn)
         123 +        n = np.max(np.abs(dv))
         124 +        if n > 0.3:
         125 +            dv *= 0.3 / n
         126 +        x[1:] += dv
         127 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         128 +    return x, ok
diff --git a/snapw/approach.py b/snapw/approach.py
new file mode 100644
index 0000000..3e4e678
--- /dev/null
+++ b/snapw/approach.py
@@ -0,0 +1,584 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place
           2 +the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py).
           3 +
           4 +Empirical facts (black-box probing):
           5 +- Arm mount is +0.12m along base x; the grasp/tool frame is 0.12m past the flange.
           6 +- Gripper fingers lie along the tool x axis, extending ~0.07m from the centre and
           7 +  ~0.035m below the tool frame.  Robot/held object collisions reject a step.
           8 +- Grasp (close) succeeds when tool z in [bottom+0.044, top+0.033] over the object.
           9 +- Release (open) succeeds only if the held object rests within a few mm of a surface.
          10 +"""
          11 +import numpy as np
          12 +from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik
          13 +
          14 +JN = [f'joint_{i}' for i in range(1, 8)]
          15 +MERGE_GRIP = True
          16 +WB = True
          17 +CUT_CORNERS = True
          18 +STEP = 0.2             # max joint delta per step
          19 +FINGER_DOWN = 0.036    # fingertips below tool frame
          20 +F_OFF, F_HL, F_HW = 0.046, 0.024, 0.013   # finger centre offset, half length, half width
          21 +
          22 +
          23 +def _q2R(x, y, z, w):
          24 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          25 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          26 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          27 +
          28 +
          29 +def _T(p, q):
          30 +    M = np.eye(4); M[:3, :3] = _q2R(*q); M[:3, 3] = p
          31 +    return M
          32 +
          33 +
          34 +def _yaw_of_quat(q):
          35 +    x, y, z, w = q
          36 +    return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
          37 +
          38 +
          39 +def _wrap(a):
          40 +    return (a + np.pi) % (2 * np.pi) - np.pi
          41 +
          42 +
          43 +def _aabb_of_rect(c, hx, hy, yaw):
          44 +    c_, s_ = abs(np.cos(yaw)), abs(np.sin(yaw))
          45 +    return np.array(c), np.array([c_ * hx + s_ * hy, s_ * hx + c_ * hy])
          46 +
          47 +
          48 +def _gap(c1, h1, c2, h2):
          49 +    """Signed separation between two AABBs (positive = apart)."""
          50 +    return np.max(np.abs(np.asarray(c1) - np.asarray(c2)) - np.asarray(h1) - np.asarray(h2))
          51 +
          52 +
          53 +def _finger_boxes(xy, yaw):
          54 +    d = np.array([np.cos(yaw), np.sin(yaw)])
          55 +    out = []
          56 +    for sgn in (1, -1):
          57 +        out.append(_aabb_of_rect(np.asarray(xy) + sgn * F_OFF * d, F_HL, F_HW, yaw))
          58 +    return out
          59 +
          60 +
          61 +class GeneratedApproach:
          62 +    def __init__(self, action_space, observation_space, primitives):
          63 +        self.action_space = action_space
          64 +        self.observation_space = observation_space
          65 +
          66 +    # ------------------------------------------------------------ helpers
          67 +    def _obj(self, state, name):
          68 +        return state.get_object_from_name(name)
          69 +
          70 +    def _pose(self, state, name):
          71 +        o = self._obj(state, name)
          72 +        return (np.array([state.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')]),
          73 +                np.array([state.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]),
          74 +                np.array([state.get(o, f) for f in ('half_extent_x', 'half_extent_y', 'half_extent_z')]))
          75 +
          76 +    def _box(self, state, name):
          77 +        """(centre_xy, half_xy AABB, bottom z, top z)"""
          78 +        p, q, h = self._pose(state, name)
          79 +        c, hh = _aabb_of_rect(p[:2], h[0], h[1], _yaw_of_quat(q))
          80 +        return c, hh, p[2] - h[2], p[2] + h[2]
          81 +
          82 +    def _q(self, state):
          83 +        return np.array([state.get(self.robot, f) for f in JN])
          84 +
          85 +    def _x(self, state):
          86 +        return np.concatenate([np.array(self._base(state)), self._q(state)])
          87 +
          88 +    def _ik(self, xc, pt, R):
          89 +        if WB:
          90 +            return wb_ik(xc, pt, R, iters=40, w_by=3.0, w_br=3.0)
          91 +        q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
          92 +        return np.concatenate([xc[:3], q]), ok
          93 +
          94 +    def _base(self, state):
          95 +        return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
          96 +                state.get(self.robot, 'pos_base_rot'))
          97 +
          98 +    def _tool(self, state):
          99 +        return tool_fk(self._q(state), self._base(state))
         100 +
         101 +    def _grasped_name(self, state):
         102 +        for n in self.names:
         103 +            if state.get(self._obj(state, n), 'grasp_active') > 0.5:
         104 +                return n
         105 +        return None
         106 +
         107 +    def _max_top(self, state, exclude=()):
         108 +        t = self.table_z
         109 +        for n in self.names:
         110 +            if n in exclude:
         111 +                continue
         112 +            t = max(t, self._box(state, n)[3])
         113 +        return t
         114 +
         115 +    # ------------------------------------------------------------ planning
         116 +    def reset(self, state, info):
         117 +        self.robot = state.get_object_from_name('robot')
         118 +        self.names = sorted(n for n in state.get_object_names() if n != 'robot')
         119 +        self.obstructions = sorted(n for n in self.names if n.startswith('obstruction'))
         120 +        rp, _, rh = self._pose(state, 'target_region')
         121 +        self.table_z = rp[2] - rh[2]
         122 +        self.region = (rp, rh)
         123 +        self.tasks = [(n, 'clear') for n in self._blocking_obstructions(state)]
         124 +        self.tasks.append(('target_block', 'goal'))
         125 +        self.phase = None
         126 +        self.qpath = []
         127 +        self.last_q = None
         128 +        self.last_a = None
         129 +        self.blocked = False
         130 +        self.look = STEP
         131 +        self.fails = {}
         132 +        self.blk_moves = {}
         133 +        self.stuck = 0
         134 +        self.descent_len = 0
         135 +        self.release_tries = 0
         136 +        self.grasp_attempt = 0
         137 +        self.total_fail = 0
         138 +        self.final_grip = 0.0
         139 +        self.wp_yaw = 0.0
         140 +        self._start_task(state)
         141 +
         142 +    def _blocking_obstructions(self, state, margin=0.003):
         143 +        rp, rh = self.region
         144 +        out = []
         145 +        for n in self.obstructions:
         146 +            c, hh, _, _ = self._box(state, n)
         147 +            if _gap(c, hh, rp[:2], rh[:2]) < margin:
         148 +                out.append(n)
         149 +        return out
         150 +
         151 +    def _finger_clearance(self, state, xy, yaw, tip_z, exclude):
         152 +        """Min xy gap between finger boxes and objects whose top is above tip_z."""
         153 +        clear = 1.0
         154 +        fbs = _finger_boxes(xy, yaw)
         155 +        for n in self.names:
         156 +            if n in exclude:
         157 +                continue
         158 +            c, hh, bot, top = self._box(state, n)
         159 +            if top < tip_z - 0.002:
         160 +                continue
         161 +            for fc, fh in fbs:
         162 +                g = _gap(fc, fh, c, hh)
         163 +                if g < clear:
         164 +                    clear = g
         165 +                    if g < 0.005:
         166 +                        self._blocker = n
         167 +        return clear
         168 +
         169 +    def _choose_yaw(self, state, name, kind, attempt):
         170 +        sc = self._yaw_scores(state, name, kind)
         171 +        c = sc[attempt % len(sc)]
         172 +        self.grasp_z = c[3]
         173 +        return c[1]
         174 +
         175 +    def _yaw_scores(self, state, name, kind):
         176 +        """Sorted [(clearance score, yaw, blocker, grasp z)] for grasp candidates."""
         177 +        p, q, h = self._pose(state, name)
         178 +        oy = _yaw_of_quat(q)
         179 +        lo = p[2] - h[2] + 0.045
         180 +        hi = p[2] + h[2] + 0.032
         181 +        gzs = [self._grasp_z(p, h)]
         182 +        if hi - 0.004 > gzs[0] + 0.004:
         183 +            gzs.append(hi - 0.004)
         184 +        cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
         185 +        T = self._tool(state)
         186 +        ty = np.arctan2(T[1, 0], T[0, 0])
         187 +        scored = []
         188 +        for j, gz in enumerate(gzs):
         189 +            for i, y in enumerate(cands):
         190 +                y = _wrap(2 * y) / 2  # modulo pi
         191 +                self._blocker = None
         192 +                c = self._finger_clearance(state, p[:2], y, gz - FINGER_DOWN, exclude=(name,))
         193 +                blk = self._blocker
         194 +                if kind == 'goal':
         195 +                    rp, rh = self.region
         196 +                    surf = rp[2] + rh[2]
         197 +                    tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
         198 +                    c = min(c, self._finger_clearance(state, rp[:2], y, tip,
         199 +                                                      exclude=(name, 'target_region')))
         200 +                rot = abs(_wrap(2 * (y - ty)) / 2)   # rotation needed (mod pi), <= pi/2
         201 +                scored.append((min(c, 0.02) - 0.0005 * i - 0.004 * j - 0.004 * rot, y, blk, gz))
         202 +        scored.sort(key=lambda t: -t[0])
         203 +        return scored
         204 +
         205 +    def _select_task(self, state):
         206 +        """Reorder tasks so the front one is graspable; add blockers if needed."""
         207 +        for _ in range(len(self.names)):
         208 +            name, kind = self.tasks[0]
         209 +            f = self.fails.get(name, 0)
         210 +            sc = self._yaw_scores(state, name, kind)
         211 +            if sc[0][0] > 0.002 and f < 4:
         212 +                return
         213 +            # try another pending clear task that is more graspable
         214 +            best = None
         215 +            for t in self.tasks:
         216 +                if t[1] != 'clear' or t[0] == name:
         217 +                    continue
         218 +                s2 = self._yaw_scores(state, t[0], 'clear')[0][0] - 0.01 * self.fails.get(t[0], 0)
         219 +                if best is None or s2 > best[0]:
         220 +                    best = (s2, t)
         221 +            if best is not None and best[0] > sc[0][0] - 0.01 * f + 0.001:
         222 +                self.tasks.remove(best[1])
         223 +                self.tasks.insert(0, best[1])
         224 +                continue
         225 +            # add the obstruction blocking the fingers as a new task
         226 +            blk = sc[0][2]
         227 +            if (blk is not None and blk.startswith('obstruction')
         228 +                    and all(t[0] != blk for t in self.tasks)
         229 +                    and self.blk_moves.get(blk, 0) < 2
         230 +                    and self._yaw_scores(state, blk, 'clear')[0][0] > 0.002):
         231 +                self.blk_moves[blk] = self.blk_moves.get(blk, 0) + 1
         232 +                self.tasks.insert(0, (blk, 'clear'))
         233 +                continue
         234 +            return
         235 +
         236 +    def _grasp_z(self, p, h):
         237 +        lo = p[2] - h[2] + 0.045
         238 +        hi = p[2] + h[2] + 0.032
         239 +        return 0.5 * (lo + hi) if hi > lo else hi - 0.001
         240 +
         241 +    def _free_spot(self, state, name, yaw, hold_off):
         242 +        """Pick a table spot clear of region/other objects (object + fingers)."""
         243 +        p0, _, _ = self._pose(state, name)
         244 +        c0, h, _, _ = self._box(state, name)
         245 +        others = []
         246 +        for n in self.names:
         247 +            if n == name:
         248 +                continue
         249 +            others.append(self._box(state, n))
         250 +        rp, rh = self.region
         251 +        tip = self.table_z + 0.001 + hold_off - FINGER_DOWN
         252 +        best, best_score = None, 1e9
         253 +        fb, fb_score = None, -1e9
         254 +        for x in np.linspace(0.2, 0.5, 16):
         255 +            for y in np.linspace(-0.34, 0.34, 35):
         256 +                c = np.array([x, y])
         257 +                clear = _gap(c, h, rp[:2], rh[:2]) - 0.03
         258 +                fbs = _finger_boxes(c, yaw)
         259 +                for oc, oh, bot, top in others:
         260 +                    clear = min(clear, _gap(c, h, oc, oh) - 0.02)
         261 +                    if top > tip - 0.002:
         262 +                        for fc, fh in fbs:
         263 +                            clear = min(clear, _gap(fc, fh, oc, oh) - 0.008)
         264 +                if clear > fb_score:
         265 +                    fb, fb_score = c, clear
         266 +                if clear >= 0:
         267 +                    score = np.linalg.norm(c - p0[:2])
         268 +                    if score < best_score:
         269 +                        best, best_score = c, score
         270 +        return best if best is not None else fb
         271 +
         272 +    def _transit_z(self, state, hold_off=0.0, exclude=()):
         273 +        top = self._max_top(state, exclude)
         274 +        return max(top + 0.03 + max(FINGER_DOWN, hold_off), 0.2)
         275 +
         276 +    def _start_task(self, state):
         277 +        if not self.tasks:
         278 +            self.phase = 'done'
         279 +            return
         280 +        try:
         281 +            self._select_task(state)
         282 +        except Exception:
         283 +            pass
         284 +        name, kind = self.tasks[0]
         285 +        p, q, h = self._pose(state, name)
         286 +        self.cur_obj = name
         287 +        self.grasp_yaw = self._choose_yaw(state, name, kind, self.fails.get(name, 0))
         288 +        gz = self.grasp_z
         289 +        zt = self._transit_z(state)
         290 +        tool = self._tool(state)[:3, 3]
         291 +        wps = []
         292 +        rs = 0
         293 +        if tool[2] < zt - 0.01:
         294 +            wps.append(np.array([tool[0], tool[1], zt]))
         295 +            rs = 1
         296 +        wps.append(np.array([p[0], p[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]))
         297 +        wps.append(np.array([p[0], p[1], gz]))
         298 +        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0, flip=True, rot_start=rs)
         299 +        self.phase = 'to_grasp'
         300 +
         301 +    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False, rot_start=0):
         302 +        """Cartesian waypoints -> dense joint path (IK warm-started).
         303 +        Yaw is interpolated from the current tool yaw over all but the last segment."""
         304 +        q = self._x(state)
         305 +        base = self._base(state)
         306 +        T0 = wb_fk(q)
         307 +        cur = T0[:3, 3]
         308 +        y0 = np.arctan2(T0[1, 0], T0[0, 0])
         309 +        dy = _wrap(yaw - y0)
         310 +        if flip and abs(dy) > np.pi / 2:
         311 +            dy = dy - np.sign(dy) * np.pi
         312 +        yaw = y0 + dy
         313 +        pts = [cur]
         314 +        for w in wps:
         315 +            pts.append(np.asarray(w, dtype=float))
         316 +        seg = [np.linalg.norm(pts[i + 1] - pts[i]) for i in range(len(wps))]
         317 +        if len(seg) - 1 <= rot_start:
         318 +            rot_start = 0
         319 +        rot0 = sum(seg[:rot_start])
         320 +        rot_len = sum(seg[rot_start:-1]) if len(seg) > 1 and sum(seg[rot_start:-1]) > 0.02 else sum(seg[rot_start:])
         321 +        rot_len = max(rot_len, 1e-6)
         322 +        path = []
         323 +        self.corners = set()
         324 +        qc = q.copy()
         325 +        travelled = 0.0
         326 +        for i, w in enumerate(wps):
         327 +            w = pts[i + 1]
         328 +            d = seg[i]
         329 +            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.04)))
         330 +            for k in range(1, n + 1):
         331 +                pt = cur + (w - cur) * k / n
         332 +                f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
         333 +                qn, ok = self._ik(qc, pt, down_R(y0 + f * dy))
         334 +                qn = qc + _wrap(qn - qc)
         335 +                path.append(qn)
         336 +                qc = qn
         337 +            travelled += d
         338 +            self.corners.add(len(path) - 1)
         339 +            cur = w
         340 +        self.qpath = path
         341 +        self.popped = 0
         342 +        self.wp_yaw = yaw
         343 +        self.final_grip = final_grip
         344 +        self.travel_grip = 1.0 if final_grip < 0 else 0.0
         345 +        self.stuck = 0
         346 +
         347 +    # ------------------------------------------------------------ control
         348 +    def _track(self, state):
         349 +        """Step along the precomputed joint path; None if done."""
         350 +        q = self._x(state)
         351 +        while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
         352 +            self.qpath.pop(0)
         353 +            self.popped += 1
         354 +        if not self.qpath:
         355 +            return None
         356 +        k = -1
         357 +        crossed = False
         358 +        for i, qp in enumerate(self.qpath):
         359 +            if np.max(np.abs(_wrap(qp - q))) <= self.look:
         360 +                if crossed and not self._safe_move(state, q, qp):
         361 +                    break
         362 +                k = i
         363 +                if (i + self.popped) in self.corners:
         364 +                    if not CUT_CORNERS or self.blocked or self.look < STEP:
         365 +                        break
         366 +                    crossed = True
         367 +            else:
         368 +                break
         369 +        a = np.zeros(11, dtype=np.float32)
         370 +        if k >= 0:
         371 +            self.qpath = self.qpath[k:]
         372 +            self.popped += k
         373 +            k = 0
         374 +            d = _wrap(self.qpath[0] - q)
         375 +            a[0:10] = d
         376 +            a[10] = self.travel_grip
         377 +            if MERGE_GRIP and len(self.qpath) == 1 and self.final_grip != 0.0:
         378 +                a[10] = self.final_grip
         379 +        else:
         380 +            d = _wrap(self.qpath[0] - q)
         381 +            a[0:10] = d * (self.look / np.max(np.abs(d)))
         382 +        return a
         383 +
         384 +    def _safe_move(self, state, q0, q1):
         385 +        """Check the joint-linear move q0->q1 keeps tool/fingers/held object
         386 +        above all nearby objects (used when cutting path corners)."""
         387 +        base = self._base(state)
         388 +        held = self._grasped_name(state)
         389 +        depth, rad = FINGER_DOWN, 0.075
         390 +        if held is not None:
         391 +            p, _, h = self._pose(state, held)
         392 +            tz = self._tool(state)[2, 3]
         393 +            depth = max(depth, tz - (p[2] - h[2]))
         394 +            rad = max(rad, np.hypot(h[0], h[1]) + 0.01)
         395 +        boxes = [self._box(state, n) for n in self.names if n != held]
         396 +        dq = _wrap(q1 - q0)
         397 +        for f in (0.25, 0.5, 0.75, 1.0):
         398 +            pt = wb_fk(q0 + f * dq)[:3, 3]
         399 +            low = pt[2] - depth
         400 +            if low < self.table_z + 0.01:
         401 +                return False
         402 +            for c, hh, bot, top in boxes:
         403 +                dxy = np.maximum(np.abs(pt[:2] - c) - hh, 0.0)
         404 +                if np.hypot(dxy[0], dxy[1]) < rad and low < top + 0.012:
         405 +                    return False
         406 +        return True
         407 +
         408 +    def _noop(self, grip=0.0):
         409 +        a = np.zeros(11, dtype=np.float32); a[10] = grip
         410 +        return a
         411 +
         412 +    def get_action(self, state):
         413 +        q = self._x(state)
         414 +        moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
         415 +        attempted = self.last_a is not None and np.any(np.abs(self.last_a[0:10]) > 1e-9)
         416 +        self.blocked = attempted and not moved
         417 +        if self.blocked:
         418 +            self.look = max(0.02, self.look * 0.35)
         419 +        elif attempted:
         420 +            self.look = min(STEP, self.look * 1.5)
         421 +        self.last_q = q.copy()
         422 +        try:
         423 +            a = self._policy(state)
         424 +        except Exception:
         425 +            a = self._noop()
         426 +        a = np.asarray(a, dtype=np.float32).copy()
         427 +        a[:10] = np.clip(a[:10], -STEP, STEP)
         428 +        a[10] = np.clip(a[10], -1, 1)
         429 +        self.last_a = a
         430 +        return a
         431 +
         432 +    def _policy(self, state):
         433 +        ph = self.phase
         434 +        if ph == 'done':
         435 +            if self._grasped_name(state) is None and self.tasks:
         436 +                self._start_task(state)
         437 +            return self._noop()
         438 +
         439 +        if ph == 'to_grasp':
         440 +            g = self._grasped_name(state)
         441 +            if g is not None:
         442 +                return self._on_grasped(state, g)
         443 +            if self.blocked:
         444 +                self.stuck += 1
         445 +                if self.stuck >= 2:
         446 +                    if self._tool(state)[2, 3] > self.grasp_z + 0.012:
         447 +                        # cannot get down to the grasp: try something else
         448 +                        self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         449 +                        self._start_task(state)
         450 +                        a = self._track(state)
         451 +                        return a if a is not None else self._noop()
         452 +                    self.qpath = []
         453 +            a = self._track(state)
         454 +            if a is not None:
         455 +                return a
         456 +            self.phase = 'close'
         457 +            return self._noop(-1.0)
         458 +
         459 +        if ph == 'close':
         460 +            g = self._grasped_name(state)
         461 +            if g is None:
         462 +                self.grasp_attempt += 1
         463 +                self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         464 +                self.total_fail += 1
         465 +                self._start_task(state)
         466 +                return self._track(state) if self.qpath else self._noop()
         467 +            return self._on_grasped(state, g)
         468 +
         469 +        if ph == 'to_place':
         470 +            if self._grasped_name(state) is None:
         471 +                return self._on_released(state)
         472 +            if self.blocked:
         473 +                self.stuck += 1
         474 +                if len(self.qpath) <= self.descent_len:
         475 +                    self.qpath = []
         476 +                elif self.stuck >= 3:
         477 +                    self._plan_place(state, replan=True)
         478 +            a = self._track(state)
         479 +            if a is not None:
         480 +                return a
         481 +            self.phase = 'open'
         482 +            return self._noop(1.0)
         483 +
         484 +        if ph == 'open':
         485 +            if self._grasped_name(state) is None:
         486 +                return self._on_released(state)
         487 +            self.release_tries += 1
         488 +            tool = self._tool(state)[:3, 3]
         489 +            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw, final_grip=1.0)
         490 +            self.descent_len = 2
         491 +            self.phase = 'to_place'
         492 +            if self.release_tries > 12:
         493 +                self.release_tries = 0
         494 +                self._plan_place(state, replan=True)
         495 +            a = self._track(state)
         496 +            return a if a is not None else self._noop(1.0)
         497 +
         498 +        if ph == 'retreat':
         499 +            if self.blocked:
         500 +                self.stuck += 1
         501 +                if self.stuck >= 2:
         502 +                    self.qpath = []
         503 +            a = self._track(state)
         504 +            if a is not None:
         505 +                return a
         506 +            self._next_task(state)
         507 +            a = self._track(state) if self.phase == 'to_grasp' else None
         508 +            return a if a is not None else self._noop()
         509 +
         510 +        return self._noop()
         511 +
         512 +    def _on_grasped(self, state, g):
         513 +        self.grasp_attempt = 0
         514 +        if g != self.cur_obj:
         515 +            self.tasks.insert(0, (g, 'clear'))
         516 +            self.cur_obj = g
         517 +        self._plan_place(state)
         518 +        a = self._track(state)
         519 +        return a if a is not None else self._noop()
         520 +
         521 +    def _on_released(self, state):
         522 +        self.release_tries = 0
         523 +        name, kind = self.tasks.pop(0) if self.tasks else (None, None)
         524 +        if kind == 'goal':
         525 +            self.phase = 'done'
         526 +            return self._noop()
         527 +        self._next_task(state)
         528 +        a = self._track(state) if self.phase == 'to_grasp' else None
         529 +        return a if a is not None else self._noop()
         530 +
         531 +    def _next_task(self, state):
         532 +        if self.tasks and self.tasks[0][1] == 'goal':
         533 +            for n in self._blocking_obstructions(state):
         534 +                if all(t[0] != n for t in self.tasks):
         535 +                    self.tasks.insert(0, (n, 'clear'))
         536 +        self._start_task(state)
         537 +
         538 +    def _plan_place(self, state, replan=False):
         539 +        name = self.cur_obj
         540 +        p, qo, h = self._pose(state, name)
         541 +        r = self.robot
         542 +        tf = _T([state.get(r, 'grasp_tf_x'), state.get(r, 'grasp_tf_y'), state.get(r, 'grasp_tf_z')],
         543 +                [state.get(r, 'grasp_tf_qx'), state.get(r, 'grasp_tf_qy'), state.get(r, 'grasp_tf_qz'),
         544 +                 state.get(r, 'grasp_tf_qw')])
         545 +        kind = self.tasks[0][1] if self.tasks and self.tasks[0][0] == name else 'clear'
         546 +        Ttool_now = self._tool(state)
         547 +        hold_off = Ttool_now[2, 3] - (p[2] - h[2])   # tool height above held-object bottom
         548 +        yaw = np.arctan2(Ttool_now[1, 0], Ttool_now[0, 0])
         549 +        if kind == 'goal':
         550 +            rp, rh = self.region
         551 +            xy = rp[:2]
         552 +            surf = rp[2] + rh[2]
         553 +        else:
         554 +            xy = self._free_spot(state, name, yaw, hold_off)
         555 +            if replan:
         556 +                xy = xy + np.random.uniform(-0.03, 0.03, 2)
         557 +            surf = self.table_z
         558 +        Tobj = _T([xy[0], xy[1], surf + h[2] + 0.001], qo)
         559 +        Ttool = Tobj @ np.linalg.inv(tf)
         560 +        tgt = Ttool[:3, 3]
         561 +        tyaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
         562 +        zt = self._transit_z(state, hold_off, exclude=(name,))
         563 +        tool = Ttool_now[:3, 3]
         564 +        wps = []
         565 +        if tool[2] < zt - 0.005:
         566 +            wps.append(np.array([tool[0], tool[1], zt]))
         567 +        wps += [np.array([tgt[0], tgt[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]),
         568 +                np.array([tgt[0], tgt[1], tgt[2] + 0.015])]
         569 +        self._set_path(state, wps, tyaw)
         570 +        n_before = len(self.qpath)
         571 +        self._append_descent(state, tgt, tyaw)
         572 +        self.descent_len = len(self.qpath) - n_before + 2
         573 +        self.final_grip = 1.0
         574 +        self.phase = 'to_place'
         575 +
         576 +    def _append_descent(self, state, tgt, yaw):
         577 +        base = self._base(state)
         578 +        qc = self.qpath[-1] if self.qpath else self._x(state)
         579 +        R = down_R(yaw)
         580 +        for dz in (0.008, 0.003, 0.0):
         581 +            qn, ok = self._ik(qc, tgt + np.array([0, 0, dz]), R)
         582 +            qn = qc + _wrap(qn - qc)
         583 +            self.qpath.append(qn)
         584 +            qc = qn
diff --git a/snapw/env_client.py b/snapw/env_client.py
new file mode 100644
index 0000000..108c884
--- /dev/null
+++ b/snapw/env_client.py
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
diff --git a/snapw/env_spaces.json b/snapw/env_spaces.json
new file mode 100644
index 0000000..dff8dfd
--- /dev/null
+++ b/snapw/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "6eefef35bfaa192f7898ebf189cf2b7d", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
diff --git a/snapw/kin.py b/snapw/kin.py
new file mode 100644
index 0000000..cb079c6
--- /dev/null
+++ b/snapw/kin.py
@@ -0,0 +1,128 @@
           1 +import numpy as np
           2 +
           3 +def _rpy(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def _T(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = _rpy(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +PI = np.pi
          13 +H = PI / 2
          14 +JOINTS = [
          15 +    _T((0, 0, 0.15643), (PI, 0, 0)),
          16 +    _T((0, 0.005375, -0.12838), (H, 0, 0)),
          17 +    _T((0, -0.21038, -0.006375), (-H, 0, 0)),
          18 +    _T((0, 0.006375, -0.21038), (H, 0, 0)),
          19 +    _T((0, -0.20843, -0.006375), (-H, 0, 0)),
          20 +    _T((0, 0.00017505, -0.10593), (H, 0, 0)),
          21 +    _T((0, -0.10593, -0.00017505), (-H, 0, 0)),
          22 +]
          23 +EE = _T((0, 0, -0.061525), (PI, 0, 0))
          24 +MOUNT = (0.12, 0.0, -0.0052)
          25 +TOOL = 0.12
          26 +HOME = np.array([0.0, -0.35, -np.pi, -2.5, 0.0, -0.87, np.pi / 2])
          27 +
          28 +def _rz(q):
          29 +    c, s = np.cos(q), np.sin(q)
          30 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          31 +
          32 +def mount_base(base):
          33 +    bx, by, br = base
          34 +    c, s = np.cos(br), np.sin(br)
          35 +    return (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
          36 +
          37 +def _chain(q, base):
          38 +    """Returns tool transform and list of (axis, origin) of joints in world."""
          39 +    bx, by, br = mount_base(base)
          40 +    T = _rz(br); T[0, 3] = bx; T[1, 3] = by; T[2, 3] = MOUNT[2]
          41 +    axes = []
          42 +    for Tj, qj in zip(JOINTS, q):
          43 +        T = T @ Tj
          44 +        axes.append((T[:3, 2].copy(), T[:3, 3].copy()))
          45 +        T = T @ _rz(qj)
          46 +    T = T @ EE
          47 +    Tt = np.eye(4); Tt[2, 3] = TOOL
          48 +    return T @ Tt, axes
          49 +
          50 +def tool_fk(q, base):
          51 +    return _chain(q, base)[0]
          52 +
          53 +def _rot_err(Rc, Rd):
          54 +    Re = Rd @ Rc.T
          55 +    v = 0.5 * np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
          56 +    return v
          57 +
          58 +def tool_ik(q0, p, R, base, iters=60, tol=1e-5, q_nom=None, k_null=0.3):
          59 +    q = np.array(q0, dtype=float)
          60 +    if q_nom is None:
          61 +        q_nom = HOME
          62 +    for it in range(iters):
          63 +        T, axes = _chain(q, base)
          64 +        e = np.concatenate([p - T[:3, 3], _rot_err(T[:3, :3], R)])
          65 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
          66 +            return q, True
          67 +        J = np.zeros((6, 7))
          68 +        pt = T[:3, 3]
          69 +        for j, (z, o) in enumerate(axes):
          70 +            J[:3, j] = np.cross(z, pt - o)
          71 +            J[3:, j] = z
          72 +        JJt = J @ J.T + 1e-6 * np.eye(6)
          73 +        Jp = J.T @ np.linalg.inv(JJt)
          74 +        dq = Jp @ e
          75 +        dn = (q_nom - q + np.pi) % (2 * np.pi) - np.pi
          76 +        dq += (np.eye(7) - Jp @ J) @ (k_null * dn)
          77 +        n = np.max(np.abs(dq))
          78 +        if n > 0.3:
          79 +            dq *= 0.3 / n
          80 +        q = q + dq
          81 +    T, _ = _chain(q, base)
          82 +    ok = np.linalg.norm(p - T[:3, 3]) < 1e-3
          83 +    return q, ok
          84 +
          85 +def down_R(yaw):
          86 +    c, s = np.cos(yaw), np.sin(yaw)
          87 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          88 +    return np.stack([x, y, z], axis=1)
          89 +
          90 +
          91 +def wb_fk(x):
          92 +    """x = [bx, by, br, q1..q7] -> tool transform."""
          93 +    return _chain(x[3:], x[:3])[0]
          94 +
          95 +
          96 +def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1.0):
          97 +    """Whole-body IK over base y, base rot and the 7 arm joints (base x fixed)."""
          98 +    x = np.array(x0, dtype=float)
          99 +    if q_nom is None:
         100 +        q_nom = HOME
         101 +    W = np.array([w_by, w_br] + [1.0] * 7)
         102 +    for it in range(iters):
         103 +        T, axes = _chain(x[3:], x[:3])
         104 +        pt = T[:3, 3]
         105 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         106 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         107 +            return x, True
         108 +        J = np.zeros((6, 9))
         109 +        J[1, 0] = 1.0
         110 +        ez = np.array([0.0, 0.0, 1.0])
         111 +        J[:3, 1] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         112 +        J[3:, 1] = ez
         113 +        for j, (z, o) in enumerate(axes):
         114 +            J[:3, 2 + j] = np.cross(z, pt - o)
         115 +            J[3:, 2 + j] = z
         116 +        JW = J * W
         117 +        Jp = JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6))
         118 +        Jp = W[:, None] * Jp
         119 +        dv = Jp @ e
         120 +        dn = np.zeros(9)
         121 +        dn[2:] = k_null * ((q_nom - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         122 +        dv += dn - Jp @ (J @ dn)
         123 +        n = np.max(np.abs(dv))
         124 +        if n > 0.3:
         125 +            dv *= 0.3 / n
         126 +        x[1:] += dv
         127 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         128 +    return x, ok
diff --git a/snapw/test_approach.py b/snapw/test_approach.py
new file mode 100644
index 0000000..d238650
--- /dev/null
+++ b/snapw/test_approach.py
@@ -0,0 +1,33 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +def run(seed, verbose=False, max_steps=None, count=None):
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed, options={'object_count': count} if count else None)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0 = time.time()
          11 +    ap.reset(obs, info)
          12 +    ms = max_steps or env.max_steps
          13 +    steps = 0
          14 +    term = False
          15 +    for steps in range(1, ms + 1):
          16 +        a = ap.get_action(obs)
          17 +        obs, r, term, trunc, info = env.step(a)
          18 +        if term or trunc:
          19 +            break
          20 +    dt = time.time() - t0
          21 +    nobs = len([n for n in obs.get_object_names() if n.startswith('obstruction')])
          22 +    env.close()
          23 +    return term, steps, dt, nobs, ap.phase
          24 +
          25 +if __name__ == '__main__':
          26 +    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          27 +    count = int(sys.argv[3]) if len(sys.argv) > 3 else None
          28 +    ok = 0
          29 +    for s in seeds:
          30 +        term, steps, dt, n, ph = run(s, count=count)
          31 +        ok += term
          32 +        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s nobs={n} phase={ph}', flush=True)
          33 +    print(f'{ok}/{len(seeds)}')
```

</details>

<a id="C020"></a>
### C020 · Tune whole-body IK: gentler null pull, bx_max -0.09

Commit `cc5e97f05d3f4d62ca49b212baae34ff93d23594`; parents: 4d813a288903f8cb57b0ad618ccb302cc741dba6. Recorded author date: 2026-09-30T22:49:03+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E1135](01_timeline.md#E1135): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_cc5e97f_approach.py) · [Exact all-file diff](evidence/diffs/C020_cc5e97f.diff)

[Previous saved controller snapshot](evidence/versions/C019_4d813a2_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e410e51..83fd918 100644
--- a/approach.py
+++ b/approach.py
@@ -87,7 +87,7 @@ class GeneratedApproach:
   87     87  
   88     88      def _ik(self, xc, pt, R):
   89     89          if WB:
   90        -            return wb_ik2(xc, pt, R, iters=40)
          90 +            return wb_ik2(xc, pt, R, iters=40, k_null=0.05, bx_max=-0.09)
   91     91          q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
   92     92          return np.concatenate([xc[:3], q]), ok
   93     93  
diff --git a/res_c4e.txt b/res_c4e.txt
new file mode 100644
index 0000000..481c361
--- /dev/null
+++ b/res_c4e.txt
@@ -0,0 +1,40 @@
           1 +seed 47: success=True steps=15 time=14.6s nobs=4 phase=to_place
           2 +seed 43: success=True steps=26 time=54.5s nobs=4 phase=to_place
           3 +seed 48: success=True steps=33 time=51.0s nobs=4 phase=to_place
           4 +seed 44: success=True steps=37 time=60.4s nobs=4 phase=to_place
           5 +seed 46: success=True steps=36 time=45.0s nobs=4 phase=to_place
           6 +seed 42: success=True steps=49 time=79.9s nobs=4 phase=to_place
           7 +seed 40: success=True steps=50 time=64.6s nobs=4 phase=to_place
           8 +seed 45: success=True steps=47 time=65.1s nobs=4 phase=to_place
           9 +seed 49: success=True steps=54 time=84.9s nobs=4 phase=to_place
          10 +seed 51: success=True steps=40 time=48.3s nobs=4 phase=to_place
          11 +seed 50: success=True steps=52 time=61.7s nobs=4 phase=to_place
          12 +seed 41: success=True steps=73 time=96.9s nobs=4 phase=to_place
          13 +seed 54: success=True steps=37 time=38.3s nobs=4 phase=to_place
          14 +seed 53: success=True steps=50 time=56.7s nobs=4 phase=to_place
          15 +seed 52: success=True steps=57 time=67.3s nobs=4 phase=to_place
          16 +seed 55: success=True steps=42 time=52.5s nobs=4 phase=to_place
          17 +seed 58: success=True steps=30 time=37.8s nobs=4 phase=to_place
          18 +seed 57: success=True steps=41 time=52.2s nobs=4 phase=to_place
          19 +seed 56: success=True steps=42 time=56.9s nobs=4 phase=to_place
          20 +seed 59: success=True steps=34 time=52.8s nobs=4 phase=to_place
          21 +seed 60: success=True steps=33 time=46.1s nobs=4 phase=to_place
          22 +seed 64: success=True steps=27 time=35.1s nobs=4 phase=to_place
          23 +seed 63: success=True steps=33 time=42.3s nobs=4 phase=to_place
          24 +seed 65: success=True steps=36 time=43.6s nobs=4 phase=to_place
          25 +seed 62: success=True steps=63 time=70.6s nobs=4 phase=to_place
          26 +seed 69: success=True steps=28 time=32.9s nobs=4 phase=to_place
          27 +seed 61: success=True steps=66 time=83.7s nobs=4 phase=to_place
          28 +seed 68: success=True steps=37 time=44.3s nobs=4 phase=to_place
          29 +seed 67: success=True steps=41 time=52.2s nobs=4 phase=to_place
          30 +seed 66: success=True steps=48 time=68.2s nobs=4 phase=to_place
          31 +seed 70: success=True steps=37 time=47.8s nobs=4 phase=to_place
          32 +seed 73: success=True steps=26 time=34.1s nobs=4 phase=to_place
          33 +seed 72: success=True steps=42 time=45.7s nobs=4 phase=to_place
          34 +seed 79: success=True steps=25 time=13.5s nobs=4 phase=to_place
          35 +seed 78: success=True steps=38 time=19.1s nobs=4 phase=to_place
          36 +seed 71: success=True steps=58 time=53.2s nobs=4 phase=to_place
          37 +seed 74: success=True steps=46 time=37.7s nobs=4 phase=to_place
          38 +seed 76: success=True steps=52 time=28.9s nobs=4 phase=to_place
          39 +seed 77: success=True steps=72 time=28.1s nobs=4 phase=to_place
          40 +seed 75: success=True steps=111 time=36.8s nobs=4 phase=to_place
diff --git a/res_d7.txt b/res_d7.txt
new file mode 100644
index 0000000..429ec45
--- /dev/null
+++ b/res_d7.txt
@@ -0,0 +1,100 @@
           1 +seed 7: success=True steps=17 time=28.8s nobs=2 phase=to_place
           2 +seed 1: success=True steps=20 time=21.2s nobs=1 phase=to_place
           3 +seed 9: success=True steps=18 time=18.5s nobs=1 phase=to_place
           4 +seed 6: success=True steps=20 time=22.1s nobs=1 phase=to_place
           5 +seed 3: success=True steps=22 time=39.8s nobs=2 phase=to_place
           6 +seed 8: success=True steps=28 time=52.7s nobs=2 phase=to_place
           7 +seed 0: success=True steps=28 time=42.9s nobs=2 phase=to_place
           8 +seed 2: success=True steps=27 time=48.2s nobs=2 phase=to_place
           9 +seed 11: success=True steps=8 time=19.8s nobs=0 phase=to_place
          10 +seed 10: success=True steps=16 time=33.3s nobs=2 phase=to_place
          11 +seed 14: success=True steps=8 time=13.9s nobs=0 phase=to_place
          12 +seed 5: success=True steps=40 time=59.1s nobs=2 phase=to_place
          13 +seed 4: success=True steps=43 time=55.9s nobs=2 phase=to_place
          14 +seed 12: success=True steps=19 time=34.8s nobs=1 phase=to_place
          15 +seed 15: success=True steps=15 time=26.3s nobs=2 phase=to_place
          16 +seed 13: success=True steps=23 time=37.8s nobs=2 phase=to_place
          17 +seed 21: success=True steps=9 time=15.7s nobs=0 phase=to_place
          18 +seed 18: success=True steps=18 time=31.9s nobs=2 phase=to_place
          19 +seed 19: success=True steps=17 time=28.5s nobs=1 phase=to_place
          20 +seed 16: success=True steps=19 time=39.2s nobs=1 phase=to_place
          21 +seed 17: success=True steps=24 time=45.6s nobs=2 phase=to_place
          22 +seed 23: success=True steps=8 time=18.0s nobs=0 phase=to_place
          23 +seed 24: success=True steps=10 time=27.2s nobs=1 phase=to_place
          24 +seed 22: success=True steps=17 time=39.6s nobs=2 phase=to_place
          25 +seed 29: success=True steps=7 time=16.3s nobs=2 phase=to_place
          26 +seed 27: success=True steps=10 time=19.1s nobs=0 phase=to_place
          27 +seed 30: success=True steps=10 time=18.4s nobs=0 phase=to_place
          28 +seed 20: success=True steps=30 time=63.9s nobs=2 phase=to_place
          29 +seed 25: success=True steps=21 time=45.8s nobs=1 phase=to_place
          30 +seed 26: success=True steps=20 time=43.8s nobs=2 phase=to_place
          31 +seed 34: success=True steps=9 time=10.8s nobs=0 phase=to_place
          32 +seed 31: success=True steps=17 time=23.3s nobs=1 phase=to_place
          33 +seed 35: success=True steps=10 time=17.0s nobs=0 phase=to_place
          34 +seed 37: success=True steps=9 time=23.7s nobs=0 phase=to_place
          35 +seed 28: success=True steps=32 time=64.8s nobs=1 phase=to_place
          36 +seed 38: success=True steps=9 time=23.9s nobs=0 phase=to_place
          37 +seed 36: success=True steps=15 time=38.1s nobs=1 phase=to_place
          38 +seed 32: success=True steps=25 time=58.2s nobs=2 phase=to_place
          39 +seed 42: success=True steps=9 time=20.1s nobs=0 phase=to_place
          40 +seed 33: success=True steps=27 time=66.3s nobs=2 phase=to_place
          41 +seed 40: success=True steps=15 time=35.8s nobs=1 phase=to_place
          42 +seed 47: success=True steps=7 time=10.9s nobs=0 phase=to_place
          43 +seed 39: success=True steps=26 time=59.2s nobs=2 phase=to_place
          44 +seed 41: success=True steps=23 time=52.4s nobs=1 phase=to_place
          45 +seed 48: success=True steps=7 time=18.3s nobs=0 phase=to_place
          46 +seed 46: success=True steps=15 time=31.5s nobs=1 phase=to_place
          47 +seed 49: success=True steps=9 time=14.3s nobs=0 phase=to_place
          48 +seed 43: success=True steps=18 time=41.4s nobs=1 phase=to_place
          49 +seed 44: success=True steps=19 time=41.0s nobs=2 phase=to_place
          50 +seed 54: success=True steps=10 time=16.4s nobs=0 phase=to_place
          51 +seed 57: success=True steps=8 time=5.3s nobs=0 phase=to_place
          52 +seed 51: success=True steps=17 time=27.3s nobs=1 phase=to_place
          53 +seed 58: success=True steps=10 time=12.8s nobs=1 phase=to_place
          54 +seed 50: success=True steps=28 time=53.7s nobs=2 phase=to_place
          55 +seed 56: success=True steps=18 time=31.6s nobs=1 phase=to_place
          56 +seed 45: success=True steps=40 time=89.8s nobs=2 phase=to_place
          57 +seed 52: success=True steps=25 time=58.7s nobs=2 phase=to_place
          58 +seed 60: success=True steps=10 time=27.8s nobs=0 phase=to_place
          59 +seed 53: success=True steps=33 time=65.6s nobs=2 phase=to_place
          60 +seed 62: success=True steps=15 time=25.6s nobs=1 phase=to_place
          61 +seed 55: success=True steps=32 time=65.6s nobs=2 phase=to_place
          62 +seed 65: success=True steps=11 time=19.5s nobs=0 phase=to_place
          63 +seed 61: success=True steps=19 time=41.0s nobs=1 phase=to_place
          64 +seed 63: success=True steps=18 time=33.0s nobs=1 phase=to_place
          65 +seed 59: success=True steps=27 time=56.3s nobs=2 phase=to_place
          66 +seed 68: success=True steps=8 time=17.8s nobs=1 phase=to_place
          67 +seed 64: success=True steps=19 time=35.9s nobs=1 phase=to_place
          68 +seed 69: success=True steps=9 time=21.3s nobs=0 phase=to_place
          69 +seed 66: success=True steps=23 time=40.8s nobs=2 phase=to_place
          70 +seed 74: success=True steps=7 time=12.8s nobs=0 phase=to_place
          71 +seed 67: success=True steps=27 time=43.0s nobs=2 phase=to_place
          72 +seed 77: success=True steps=8 time=11.3s nobs=0 phase=to_place
          73 +seed 70: success=True steps=22 time=42.4s nobs=1 phase=to_place
          74 +seed 79: success=True steps=7 time=12.5s nobs=0 phase=to_place
          75 +seed 75: success=True steps=19 time=28.6s nobs=1 phase=to_place
          76 +seed 76: success=True steps=20 time=33.1s nobs=1 phase=to_place
          77 +seed 72: success=True steps=27 time=48.1s nobs=2 phase=to_place
          78 +seed 73: success=True steps=26 time=49.9s nobs=2 phase=to_place
          79 +seed 81: success=True steps=9 time=20.2s nobs=0 phase=to_place
          80 +seed 71: success=True steps=37 time=62.8s nobs=2 phase=to_place
          81 +seed 80: success=True steps=23 time=38.4s nobs=2 phase=to_place
          82 +seed 78: success=True steps=37 time=48.2s nobs=2 phase=to_place
          83 +seed 83: success=True steps=18 time=31.5s nobs=2 phase=to_place
          84 +seed 84: success=True steps=26 time=33.5s nobs=1 phase=to_place
          85 +seed 88: success=True steps=18 time=20.5s nobs=1 phase=to_place
          86 +seed 85: success=True steps=23 time=36.9s nobs=2 phase=to_place
          87 +seed 87: success=True steps=27 time=34.5s nobs=1 phase=to_place
          88 +seed 90: success=True steps=15 time=20.3s nobs=1 phase=to_place
          89 +seed 86: success=True steps=25 time=40.1s nobs=2 phase=to_place
          90 +seed 92: success=True steps=16 time=22.9s nobs=1 phase=to_place
          91 +seed 82: success=True steps=44 time=67.3s nobs=2 phase=to_place
          92 +seed 91: success=True steps=18 time=33.1s nobs=2 phase=to_place
          93 +seed 94: success=True steps=9 time=16.8s nobs=0 phase=to_place
          94 +seed 89: success=True steps=31 time=44.7s nobs=2 phase=to_place
          95 +seed 97: success=True steps=10 time=6.2s nobs=0 phase=to_place
          96 +seed 95: success=True steps=16 time=14.3s nobs=1 phase=to_place
          97 +seed 98: success=True steps=25 time=6.2s nobs=1 phase=to_place
          98 +seed 93: success=True steps=41 time=29.5s nobs=2 phase=to_place
          99 +seed 96: success=True steps=30 time=17.3s nobs=2 phase=to_place
         100 +seed 99: success=True steps=36 time=7.4s nobs=2 phase=to_place
diff --git a/res_var.txt b/res_var.txt
new file mode 100644
index 0000000..a70e72d
--- /dev/null
+++ b/res_var.txt
@@ -0,0 +1,160 @@
           1 +v_0.05_-0.09 seed 105: success=True steps=9 time=20.2s ptime=0.1s nobs=0 phase=to_place
           2 +v_0.05_-0.09 seed 108: success=True steps=10 time=25.8s ptime=0.1s nobs=0 phase=to_place
           3 +v_0.05_-0.09 seed 101: success=True steps=8 time=11.6s ptime=0.1s nobs=0 phase=to_place
           4 +v_0.05_-0.09 seed 110: success=True steps=16 time=42.2s ptime=0.2s nobs=1 phase=to_place
           5 +v_0.05_-0.09 seed 107: success=True steps=9 time=10.4s ptime=0.1s nobs=0 phase=to_place
           6 +v_0.05_-0.09 seed 106: success=True steps=10 time=20.7s ptime=0.1s nobs=1 phase=to_place
           7 +v_0.05_-0.09 seed 102: success=True steps=16 time=45.0s ptime=0.2s nobs=1 phase=to_place
           8 +v_0.05_-0.09 seed 103: success=True steps=20 time=56.5s ptime=0.2s nobs=1 phase=to_place
           9 +v_0.05_-0.09 seed 114: success=True steps=7 time=18.3s ptime=0.0s nobs=0 phase=to_place
          10 +v_0.05_-0.09 seed 112: success=True steps=8 time=28.9s ptime=0.1s nobs=0 phase=to_place
          11 +v_0.05_-0.09 seed 111: success=True steps=16 time=39.5s ptime=0.3s nobs=1 phase=to_place
          12 +v_0.05_-0.09 seed 113: success=True steps=9 time=26.1s ptime=0.1s nobs=0 phase=to_place
          13 +v_0.05_-0.09 seed 100: success=True steps=29 time=79.6s ptime=0.4s nobs=2 phase=to_place
          14 +v_0.05_-0.09 seed 116: success=True steps=8 time=17.6s ptime=0.1s nobs=0 phase=to_place
          15 +v_0.05_-0.09 seed 109: success=True steps=28 time=57.5s ptime=0.4s nobs=1 phase=to_place
          16 +v_0.05_-0.09 seed 117: success=True steps=7 time=17.4s ptime=0.0s nobs=0 phase=to_place
          17 +v_0.05_-0.09 seed 120: success=True steps=7 time=20.9s ptime=0.0s nobs=0 phase=to_place
          18 +v_0.05_-0.09 seed 115: success=True steps=17 time=48.4s ptime=0.3s nobs=1 phase=to_place
          19 +v_0.05_-0.09 seed 121: success=True steps=7 time=22.1s ptime=0.0s nobs=0 phase=to_place
          20 +v_0.05_-0.09 seed 118: success=True steps=16 time=44.9s ptime=0.2s nobs=1 phase=to_place
          21 +v_0.05_-0.09 seed 123: success=True steps=9 time=27.2s ptime=0.1s nobs=0 phase=to_place
          22 +v_0.05_-0.09 seed 104: success=True steps=46 time=106.7s ptime=0.4s nobs=2 phase=to_place
          23 +v_0.05_-0.09 seed 127: success=True steps=9 time=18.9s ptime=0.1s nobs=1 phase=to_place
          24 +v_0.05_-0.09 seed 126: success=True steps=11 time=25.6s ptime=0.1s nobs=0 phase=to_place
          25 +v_0.05_-0.09 seed 119: success=True steps=27 time=53.4s ptime=0.4s nobs=1 phase=to_place
          26 +v_0.05_-0.09 seed 124: success=True steps=18 time=44.2s ptime=0.2s nobs=2 phase=to_place
          27 +v_0.05_-0.09 seed 125: success=True steps=19 time=39.7s ptime=0.3s nobs=1 phase=to_place
          28 +v_0.05_-0.09 seed 122: success=True steps=28 time=63.2s ptime=0.4s nobs=2 phase=to_place
          29 +v_0.05_-0.09 seed 133: success=True steps=16 time=25.0s ptime=0.2s nobs=1 phase=to_place
          30 +v_0.05_-0.09 seed 129: success=True steps=24 time=37.7s ptime=0.3s nobs=1 phase=to_place
          31 +v_0.05_-0.09 seed 131: success=True steps=25 time=36.2s ptime=0.2s nobs=1 phase=to_place
          32 +v_0.05_-0.09 seed 135: success=True steps=18 time=25.2s ptime=0.2s nobs=1 phase=to_place
          33 +v_0.05_-0.09 seed 137: success=True steps=15 time=25.8s ptime=0.2s nobs=1 phase=to_place
          34 +v_0.05_-0.09 seed 136: success=True steps=20 time=32.1s ptime=0.3s nobs=2 phase=to_place
          35 +v_0.05_-0.09 seed 128: success=True steps=29 time=59.6s ptime=0.4s nobs=2 phase=to_place
          36 +v_0.05_-0.09 seed 130: success=True steps=27 time=49.8s ptime=0.5s nobs=2 phase=to_place
          37 +v_0.05_-0.09 seed 134: success=True steps=24 time=42.5s ptime=0.4s nobs=2 phase=to_place
          38 +v_0.05_-0.09 seed 132: success=True steps=26 time=49.5s ptime=0.3s nobs=2 phase=to_place
          39 +v_0.1_-0.09 seed 101: success=True steps=9 time=13.2s ptime=0.1s nobs=0 phase=to_place
          40 +v_0.05_-0.09 seed 138: success=True steps=19 time=26.4s ptime=0.3s nobs=1 phase=to_place
          41 +v_0.05_-0.09 seed 139: success=True steps=20 time=40.6s ptime=0.3s nobs=1 phase=to_place
          42 +v_0.1_-0.09 seed 105: success=True steps=8 time=23.0s ptime=0.0s nobs=0 phase=to_place
          43 +v_0.1_-0.09 seed 102: success=True steps=16 time=35.3s ptime=0.2s nobs=1 phase=to_place
          44 +v_0.1_-0.09 seed 107: success=True steps=9 time=29.2s ptime=0.1s nobs=0 phase=to_place
          45 +v_0.1_-0.09 seed 106: success=True steps=10 time=32.1s ptime=0.1s nobs=1 phase=to_place
          46 +v_0.1_-0.09 seed 103: success=True steps=20 time=44.4s ptime=0.2s nobs=1 phase=to_place
          47 +v_0.1_-0.09 seed 108: success=True steps=10 time=28.0s ptime=0.1s nobs=0 phase=to_place
          48 +v_0.1_-0.09 seed 114: success=True steps=7 time=15.8s ptime=0.0s nobs=0 phase=to_place
          49 +v_0.1_-0.09 seed 112: success=True steps=9 time=23.4s ptime=0.1s nobs=0 phase=to_place
          50 +v_0.1_-0.09 seed 100: success=True steps=30 time=71.5s ptime=0.4s nobs=2 phase=to_place
          51 +v_0.1_-0.09 seed 113: success=True steps=9 time=19.0s ptime=0.1s nobs=0 phase=to_place
          52 +v_0.1_-0.09 seed 116: success=True steps=8 time=22.9s ptime=0.1s nobs=0 phase=to_place
          53 +v_0.1_-0.09 seed 117: success=True steps=7 time=18.9s ptime=0.1s nobs=0 phase=to_place
          54 +v_0.1_-0.09 seed 111: success=True steps=16 time=45.2s ptime=0.2s nobs=1 phase=to_place
          55 +v_0.1_-0.09 seed 110: success=True steps=17 time=46.9s ptime=0.4s nobs=1 phase=to_place
          56 +v_0.1_-0.09 seed 121: success=True steps=7 time=13.9s ptime=0.1s nobs=0 phase=to_place
          57 +v_0.1_-0.09 seed 120: success=True steps=7 time=16.5s ptime=0.1s nobs=0 phase=to_place
          58 +v_0.1_-0.09 seed 115: success=True steps=17 time=45.5s ptime=0.3s nobs=1 phase=to_place
          59 +v_0.1_-0.09 seed 109: success=True steps=28 time=74.7s ptime=0.4s nobs=1 phase=to_place
          60 +v_0.1_-0.09 seed 104: success=True steps=47 time=100.6s ptime=0.4s nobs=2 phase=to_place
          61 +v_0.1_-0.09 seed 123: success=True steps=9 time=22.4s ptime=0.0s nobs=0 phase=to_place
          62 +v_0.1_-0.09 seed 118: success=True steps=16 time=49.0s ptime=0.3s nobs=1 phase=to_place
          63 +v_0.1_-0.09 seed 127: success=True steps=9 time=20.2s ptime=0.1s nobs=1 phase=to_place
          64 +v_0.1_-0.09 seed 126: success=True steps=11 time=25.1s ptime=0.1s nobs=0 phase=to_place
          65 +v_0.1_-0.09 seed 119: success=True steps=27 time=51.5s ptime=0.6s nobs=1 phase=to_place
          66 +v_0.1_-0.09 seed 124: success=True steps=18 time=42.8s ptime=0.2s nobs=2 phase=to_place
          67 +v_0.1_-0.09 seed 125: success=True steps=19 time=43.4s ptime=0.3s nobs=1 phase=to_place
          68 +v_0.1_-0.09 seed 122: success=True steps=28 time=63.1s ptime=0.7s nobs=2 phase=to_place
          69 +v_0.1_-0.09 seed 129: success=True steps=25 time=40.8s ptime=0.2s nobs=1 phase=to_place
          70 +v_0.1_-0.09 seed 133: success=True steps=16 time=30.9s ptime=0.3s nobs=1 phase=to_place
          71 +v_0.1_-0.09 seed 131: success=True steps=30 time=42.6s ptime=0.3s nobs=1 phase=to_place
          72 +v_0.1_-0.09 seed 135: success=True steps=18 time=29.9s ptime=0.2s nobs=1 phase=to_place
          73 +v_0.1_-0.09 seed 137: success=True steps=17 time=24.2s ptime=0.2s nobs=1 phase=to_place
          74 +v_0.1_-0.09 seed 130: success=True steps=28 time=53.9s ptime=0.3s nobs=2 phase=to_place
          75 +v_0.1_-0.09 seed 132: success=True steps=27 time=48.8s ptime=0.4s nobs=2 phase=to_place
          76 +v_0.1_-0.09 seed 134: success=True steps=24 time=44.9s ptime=0.4s nobs=2 phase=to_place
          77 +v_0.1_-0.09 seed 128: success=True steps=30 time=66.3s ptime=0.4s nobs=2 phase=to_place
          78 +v_0.1_-0.09 seed 136: success=True steps=20 time=39.9s ptime=0.3s nobs=2 phase=to_place
          79 +v_0.1_-0.09 seed 138: success=True steps=20 time=45.0s ptime=0.3s nobs=1 phase=to_place
          80 +v_0.1_-0.09 seed 139: success=True steps=20 time=41.1s ptime=0.3s nobs=1 phase=to_place
          81 +v_0.1_-0.12 seed 101: success=True steps=10 time=29.4s ptime=0.1s nobs=0 phase=to_place
          82 +v_0.1_-0.12 seed 107: success=True steps=9 time=18.9s ptime=0.1s nobs=0 phase=to_place
          83 +v_0.1_-0.12 seed 105: success=True steps=10 time=27.0s ptime=0.1s nobs=0 phase=to_place
          84 +v_0.1_-0.12 seed 108: success=True steps=10 time=13.8s ptime=0.1s nobs=0 phase=to_place
          85 +v_0.1_-0.12 seed 102: success=True steps=18 time=41.3s ptime=0.2s nobs=1 phase=to_place
          86 +v_0.1_-0.12 seed 106: success=True steps=10 time=25.7s ptime=0.1s nobs=1 phase=to_place
          87 +v_0.1_-0.12 seed 103: success=True steps=21 time=56.5s ptime=0.3s nobs=1 phase=to_place
          88 +v_0.1_-0.12 seed 112: success=True steps=10 time=25.2s ptime=0.1s nobs=0 phase=to_place
          89 +v_0.1_-0.12 seed 114: success=True steps=7 time=18.8s ptime=0.0s nobs=0 phase=to_place
          90 +v_0.1_-0.12 seed 113: success=True steps=8 time=21.7s ptime=0.1s nobs=0 phase=to_place
          91 +v_0.1_-0.12 seed 110: success=True steps=18 time=43.9s ptime=0.3s nobs=1 phase=to_place
          92 +v_0.1_-0.12 seed 116: success=True steps=9 time=18.5s ptime=0.1s nobs=0 phase=to_place
          93 +v_0.1_-0.12 seed 117: success=True steps=8 time=16.3s ptime=0.1s nobs=0 phase=to_place
          94 +v_0.1_-0.12 seed 100: success=True steps=32 time=85.7s ptime=0.4s nobs=2 phase=to_place
          95 +v_0.1_-0.12 seed 111: success=True steps=17 time=44.6s ptime=0.3s nobs=1 phase=to_place
          96 +v_0.1_-0.12 seed 109: success=True steps=29 time=67.3s ptime=0.4s nobs=1 phase=to_place
          97 +v_0.1_-0.12 seed 120: success=True steps=7 time=23.1s ptime=0.1s nobs=0 phase=to_place
          98 +v_0.1_-0.12 seed 115: success=True steps=17 time=44.2s ptime=0.2s nobs=1 phase=to_place
          99 +v_0.1_-0.12 seed 121: success=True steps=7 time=21.1s ptime=0.0s nobs=0 phase=to_place
         100 +v_0.1_-0.12 seed 104: success=True steps=47 time=100.4s ptime=0.5s nobs=2 phase=to_place
         101 +v_0.1_-0.12 seed 118: success=True steps=16 time=47.4s ptime=0.3s nobs=1 phase=to_place
         102 +v_0.1_-0.12 seed 123: success=True steps=10 time=27.2s ptime=0.1s nobs=0 phase=to_place
         103 +v_0.1_-0.12 seed 126: success=True steps=11 time=21.5s ptime=0.1s nobs=0 phase=to_place
         104 +v_0.1_-0.12 seed 127: success=True steps=10 time=19.1s ptime=0.1s nobs=1 phase=to_place
         105 +v_0.1_-0.12 seed 119: success=True steps=27 time=56.6s ptime=0.3s nobs=1 phase=to_place
         106 +v_0.1_-0.12 seed 124: success=True steps=20 time=43.6s ptime=0.2s nobs=2 phase=to_place
         107 +v_0.1_-0.12 seed 125: success=True steps=19 time=43.3s ptime=0.3s nobs=1 phase=to_place
         108 +v_0.1_-0.12 seed 122: success=True steps=28 time=61.7s ptime=0.5s nobs=2 phase=to_place
         109 +v_0.1_-0.12 seed 133: success=True steps=16 time=23.4s ptime=0.2s nobs=1 phase=to_place
         110 +v_0.1_-0.12 seed 129: success=True steps=25 time=37.1s ptime=0.3s nobs=1 phase=to_place
         111 +v_0.1_-0.12 seed 135: success=True steps=19 time=21.7s ptime=0.2s nobs=1 phase=to_place
         112 +v_0.1_-0.12 seed 131: success=True steps=30 time=40.2s ptime=0.4s nobs=1 phase=to_place
         113 +v_0.1_-0.12 seed 130: success=True steps=28 time=47.7s ptime=0.4s nobs=2 phase=to_place
         114 +v_0.1_-0.12 seed 128: success=True steps=30 time=55.5s ptime=0.4s nobs=2 phase=to_place
         115 +v_0.1_-0.12 seed 136: success=True steps=20 time=28.2s ptime=0.3s nobs=2 phase=to_place
         116 +v_0.1_-0.12 seed 134: success=True steps=25 time=37.5s ptime=0.5s nobs=2 phase=to_place
         117 +v_0.1_-0.12 seed 132: success=True steps=28 time=44.5s ptime=0.4s nobs=2 phase=to_place
         118 +v_0.1_-0.12 seed 137: success=True steps=18 time=22.7s ptime=0.2s nobs=1 phase=to_place
         119 +v_0.1_-0.12 seed 138: success=True steps=21 time=39.7s ptime=0.3s nobs=1 phase=to_place
         120 +v_0.3_-0.12 seed 101: success=True steps=10 time=28.1s ptime=0.0s nobs=0 phase=to_place
         121 +v_0.1_-0.12 seed 139: success=True steps=19 time=42.7s ptime=0.2s nobs=1 phase=to_place
         122 +v_0.3_-0.12 seed 105: success=True steps=10 time=28.3s ptime=0.1s nobs=0 phase=to_place
         123 +v_0.3_-0.12 seed 107: success=True steps=9 time=25.0s ptime=0.1s nobs=0 phase=to_place
         124 +v_0.3_-0.12 seed 106: success=True steps=10 time=33.4s ptime=0.1s nobs=1 phase=to_place
         125 +v_0.3_-0.12 seed 102: success=True steps=18 time=48.2s ptime=0.2s nobs=1 phase=to_place
         126 +v_0.3_-0.12 seed 108: success=True steps=10 time=26.6s ptime=0.1s nobs=0 phase=to_place
         127 +v_0.3_-0.12 seed 112: success=True steps=10 time=20.8s ptime=0.0s nobs=0 phase=to_place
         128 +v_0.3_-0.12 seed 103: success=True steps=21 time=58.4s ptime=0.2s nobs=1 phase=to_place
         129 +v_0.3_-0.12 seed 113: success=True steps=9 time=26.0s ptime=0.1s nobs=0 phase=to_place
         130 +v_0.3_-0.12 seed 110: success=True steps=18 time=41.8s ptime=0.2s nobs=1 phase=to_place
         131 +v_0.3_-0.12 seed 114: success=True steps=7 time=22.1s ptime=0.1s nobs=0 phase=to_place
         132 +v_0.3_-0.12 seed 111: success=True steps=17 time=44.1s ptime=0.3s nobs=1 phase=to_place
         133 +v_0.3_-0.12 seed 100: success=True steps=33 time=88.2s ptime=0.4s nobs=2 phase=to_place
         134 +v_0.3_-0.12 seed 117: success=True steps=8 time=20.2s ptime=0.0s nobs=0 phase=to_place
         135 +v_0.3_-0.12 seed 116: success=True steps=9 time=21.9s ptime=0.1s nobs=0 phase=to_place
         136 +v_0.3_-0.12 seed 120: success=True steps=7 time=19.0s ptime=0.1s nobs=0 phase=to_place
         137 +v_0.3_-0.12 seed 109: success=True steps=30 time=73.3s ptime=0.4s nobs=1 phase=to_place
         138 +v_0.3_-0.12 seed 121: success=True steps=7 time=20.8s ptime=0.1s nobs=0 phase=to_place
         139 +v_0.3_-0.12 seed 115: success=True steps=17 time=49.2s ptime=0.3s nobs=1 phase=to_place
         140 +v_0.3_-0.12 seed 123: success=True steps=10 time=22.6s ptime=0.1s nobs=0 phase=to_place
         141 +v_0.3_-0.12 seed 118: success=True steps=16 time=42.1s ptime=0.3s nobs=1 phase=to_place
         142 +v_0.3_-0.12 seed 104: success=True steps=51 time=107.1s ptime=0.4s nobs=2 phase=to_place
         143 +v_0.3_-0.12 seed 126: success=True steps=11 time=23.5s ptime=0.1s nobs=0 phase=to_place
         144 +v_0.3_-0.12 seed 127: success=True steps=10 time=22.7s ptime=0.1s nobs=1 phase=to_place
         145 +v_0.3_-0.12 seed 119: success=True steps=28 time=55.5s ptime=0.4s nobs=1 phase=to_place
         146 +v_0.3_-0.12 seed 125: success=True steps=19 time=36.4s ptime=0.3s nobs=1 phase=to_place
         147 +v_0.3_-0.12 seed 124: success=True steps=19 time=47.6s ptime=0.2s nobs=2 phase=to_place
         148 +v_0.3_-0.12 seed 122: success=True steps=29 time=61.1s ptime=0.5s nobs=2 phase=to_place
         149 +v_0.3_-0.12 seed 133: success=True steps=16 time=28.4s ptime=0.5s nobs=1 phase=to_place
         150 +v_0.3_-0.12 seed 129: success=True steps=25 time=41.9s ptime=0.3s nobs=1 phase=to_place
         151 +v_0.3_-0.12 seed 135: success=True steps=19 time=21.2s ptime=0.2s nobs=1 phase=to_place
         152 +v_0.3_-0.12 seed 137: success=True steps=18 time=17.1s ptime=0.2s nobs=1 phase=to_place
         153 +v_0.3_-0.12 seed 131: success=True steps=31 time=38.3s ptime=0.4s nobs=1 phase=to_place
         154 +v_0.3_-0.12 seed 128: success=True steps=32 time=50.7s ptime=0.6s nobs=2 phase=to_place
         155 +v_0.3_-0.12 seed 136: success=True steps=20 time=23.3s ptime=0.3s nobs=2 phase=to_place
         156 +v_0.3_-0.12 seed 132: success=True steps=29 time=35.6s ptime=0.4s nobs=2 phase=to_place
         157 +v_0.3_-0.12 seed 130: success=True steps=30 time=43.9s ptime=0.4s nobs=2 phase=to_place
         158 +v_0.3_-0.12 seed 134: success=True steps=25 time=30.6s ptime=0.4s nobs=2 phase=to_place
         159 +v_0.3_-0.12 seed 138: success=True steps=21 time=13.3s ptime=0.3s nobs=1 phase=to_place
         160 +v_0.3_-0.12 seed 139: success=True steps=19 time=5.9s ptime=0.2s nobs=1 phase=to_place
diff --git a/snap/approach.py b/snap/approach.py
index eedb988..e410e51 100644
--- a/snap/approach.py
+++ b/snap/approach.py
@@ -9,7 +9,7 @@ Empirical facts (black-box probing):
    9      9  - Release (open) succeeds only if the held object rests within a few mm of a surface.
   10     10  """
   11     11  import numpy as np
   12        -from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik
          12 +from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik, wb_ik2
   13     13  
   14     14  JN = [f'joint_{i}' for i in range(1, 8)]
   15     15  MERGE_GRIP = True
@@ -87,7 +87,7 @@ class GeneratedApproach:
   87     87  
   88     88      def _ik(self, xc, pt, R):
   89     89          if WB:
   90        -            return wb_ik(xc, pt, R, iters=40)
          90 +            return wb_ik2(xc, pt, R, iters=40)
   91     91          q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
   92     92          return np.concatenate([xc[:3], q]), ok
   93     93  
diff --git a/snap/kin.py b/snap/kin.py
index cb079c6..b360a71 100644
--- a/snap/kin.py
+++ b/snap/kin.py
@@ -126,3 +126,47 @@ def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1
  126    126          x[1:] += dv
  127    127      ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
  128    128      return x, ok
         129 +
         130 +
         131 +Q_NOM = np.array([0.0, 0.3, -np.pi, -2.15, 0.0, -0.69, 0.0])
         132 +K_NOM = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
         133 +
         134 +
         135 +def wb_ik2(x0, p, R, iters=40, tol=1e-5, k_null=0.3, bx_max=-0.12, w_base=1.0):
         136 +    """Whole-body IK over base x (<= bx_max), y, rot and the 7 arm joints.
         137 +    Null space pulls the arm to an extended nominal posture Q_NOM."""
         138 +    x = np.array(x0, dtype=float)
         139 +    ez = np.array([0.0, 0.0, 1.0])
         140 +    for it in range(iters):
         141 +        T, axes = _chain(x[3:], x[:3])
         142 +        pt = T[:3, 3]
         143 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         144 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         145 +            return x, True
         146 +        J = np.zeros((6, 10))
         147 +        J[0, 0] = 1.0
         148 +        J[1, 1] = 1.0
         149 +        J[:3, 2] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         150 +        J[3:, 2] = ez
         151 +        for j, (z, o) in enumerate(axes):
         152 +            J[:3, 3 + j] = np.cross(z, pt - o)
         153 +            J[3:, 3 + j] = z
         154 +        dn = np.zeros(10)
         155 +        dn[3:] = k_null * K_NOM * ((Q_NOM - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         156 +        W = np.array([w_base, w_base, w_base] + [1.0] * 7)
         157 +        for _ in range(2):
         158 +            JW = J * W
         159 +            Jp = W[:, None] * (JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6)))
         160 +            dv = Jp @ e + dn - Jp @ (J @ dn)
         161 +            n = np.max(np.abs(dv))
         162 +            if n > 0.3:
         163 +                dv *= 0.3 / n
         164 +            if x[0] + dv[0] > bx_max + 1e-9 and W[0] > 0:
         165 +                W[0] = 0.0
         166 +                x[0] = min(x[0], bx_max)
         167 +                continue
         168 +            break
         169 +        x += dv
         170 +        x[0] = min(x[0], bx_max) if x0[0] <= bx_max + 1e-9 else x[0]
         171 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         172 +    return x, ok
diff --git a/snapw/approach.py b/snapw/approach.py
index 3e4e678..e410e51 100644
--- a/snapw/approach.py
+++ b/snapw/approach.py
@@ -9,7 +9,7 @@ Empirical facts (black-box probing):
    9      9  - Release (open) succeeds only if the held object rests within a few mm of a surface.
   10     10  """
   11     11  import numpy as np
   12        -from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik
          12 +from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik, wb_ik2
   13     13  
   14     14  JN = [f'joint_{i}' for i in range(1, 8)]
   15     15  MERGE_GRIP = True
@@ -87,7 +87,7 @@ class GeneratedApproach:
   87     87  
   88     88      def _ik(self, xc, pt, R):
   89     89          if WB:
   90        -            return wb_ik(xc, pt, R, iters=40, w_by=3.0, w_br=3.0)
          90 +            return wb_ik2(xc, pt, R, iters=40)
   91     91          q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
   92     92          return np.concatenate([xc[:3], q]), ok
   93     93  
diff --git a/snapw/kin.py b/snapw/kin.py
index cb079c6..b360a71 100644
--- a/snapw/kin.py
+++ b/snapw/kin.py
@@ -126,3 +126,47 @@ def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1
  126    126          x[1:] += dv
  127    127      ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
  128    128      return x, ok
         129 +
         130 +
         131 +Q_NOM = np.array([0.0, 0.3, -np.pi, -2.15, 0.0, -0.69, 0.0])
         132 +K_NOM = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
         133 +
         134 +
         135 +def wb_ik2(x0, p, R, iters=40, tol=1e-5, k_null=0.3, bx_max=-0.12, w_base=1.0):
         136 +    """Whole-body IK over base x (<= bx_max), y, rot and the 7 arm joints.
         137 +    Null space pulls the arm to an extended nominal posture Q_NOM."""
         138 +    x = np.array(x0, dtype=float)
         139 +    ez = np.array([0.0, 0.0, 1.0])
         140 +    for it in range(iters):
         141 +        T, axes = _chain(x[3:], x[:3])
         142 +        pt = T[:3, 3]
         143 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         144 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         145 +            return x, True
         146 +        J = np.zeros((6, 10))
         147 +        J[0, 0] = 1.0
         148 +        J[1, 1] = 1.0
         149 +        J[:3, 2] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         150 +        J[3:, 2] = ez
         151 +        for j, (z, o) in enumerate(axes):
         152 +            J[:3, 3 + j] = np.cross(z, pt - o)
         153 +            J[3:, 3 + j] = z
         154 +        dn = np.zeros(10)
         155 +        dn[3:] = k_null * K_NOM * ((Q_NOM - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         156 +        W = np.array([w_base, w_base, w_base] + [1.0] * 7)
         157 +        for _ in range(2):
         158 +            JW = J * W
         159 +            Jp = W[:, None] * (JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6)))
         160 +            dv = Jp @ e + dn - Jp @ (J @ dn)
         161 +            n = np.max(np.abs(dv))
         162 +            if n > 0.3:
         163 +                dv *= 0.3 / n
         164 +            if x[0] + dv[0] > bx_max + 1e-9 and W[0] > 0:
         165 +                W[0] = 0.0
         166 +                x[0] = min(x[0], bx_max)
         167 +                continue
         168 +            break
         169 +        x += dv
         170 +        x[0] = min(x[0], bx_max) if x0[0] <= bx_max + 1e-9 else x[0]
         171 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         172 +    return x, ok
diff --git a/test_approach.py b/test_approach.py
index d238650..afc13cc 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -12,22 +12,25 @@ def run(seed, verbose=False, max_steps=None, count=None):
   12     12      ms = max_steps or env.max_steps
   13     13      steps = 0
   14     14      term = False
          15 +    pt = 0.0
   15     16      for steps in range(1, ms + 1):
          17 +        t1 = time.time()
   16     18          a = ap.get_action(obs)
          19 +        pt += time.time() - t1
   17     20          obs, r, term, trunc, info = env.step(a)
   18     21          if term or trunc:
   19     22              break
   20     23      dt = time.time() - t0
   21     24      nobs = len([n for n in obs.get_object_names() if n.startswith('obstruction')])
   22     25      env.close()
   23        -    return term, steps, dt, nobs, ap.phase
          26 +    return term, steps, dt, nobs, ap.phase, pt
   24     27  
   25     28  if __name__ == '__main__':
   26     29      seeds = range(int(sys.argv[1]), int(sys.argv[2]))
   27     30      count = int(sys.argv[3]) if len(sys.argv) > 3 else None
   28     31      ok = 0
   29     32      for s in seeds:
   30        -        term, steps, dt, n, ph = run(s, count=count)
          33 +        term, steps, dt, n, ph, pt = run(s, count=count)
   31     34          ok += term
   32        -        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s nobs={n} phase={ph}', flush=True)
          35 +        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s ptime={pt:.1f}s nobs={n} phase={ph}', flush=True)
   33     36      print(f'{ok}/{len(seeds)}')
diff --git a/v_0.05_-0.09/approach.py b/v_0.05_-0.09/approach.py
new file mode 100644
index 0000000..83fd918
--- /dev/null
+++ b/v_0.05_-0.09/approach.py
@@ -0,0 +1,584 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place
           2 +the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py).
           3 +
           4 +Empirical facts (black-box probing):
           5 +- Arm mount is +0.12m along base x; the grasp/tool frame is 0.12m past the flange.
           6 +- Gripper fingers lie along the tool x axis, extending ~0.07m from the centre and
           7 +  ~0.035m below the tool frame.  Robot/held object collisions reject a step.
           8 +- Grasp (close) succeeds when tool z in [bottom+0.044, top+0.033] over the object.
           9 +- Release (open) succeeds only if the held object rests within a few mm of a surface.
          10 +"""
          11 +import numpy as np
          12 +from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik, wb_ik2
          13 +
          14 +JN = [f'joint_{i}' for i in range(1, 8)]
          15 +MERGE_GRIP = True
          16 +WB = True
          17 +CUT_CORNERS = True
          18 +STEP = 0.2             # max joint delta per step
          19 +FINGER_DOWN = 0.036    # fingertips below tool frame
          20 +F_OFF, F_HL, F_HW = 0.046, 0.024, 0.013   # finger centre offset, half length, half width
          21 +
          22 +
          23 +def _q2R(x, y, z, w):
          24 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          25 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          26 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          27 +
          28 +
          29 +def _T(p, q):
          30 +    M = np.eye(4); M[:3, :3] = _q2R(*q); M[:3, 3] = p
          31 +    return M
          32 +
          33 +
          34 +def _yaw_of_quat(q):
          35 +    x, y, z, w = q
          36 +    return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
          37 +
          38 +
          39 +def _wrap(a):
          40 +    return (a + np.pi) % (2 * np.pi) - np.pi
          41 +
          42 +
          43 +def _aabb_of_rect(c, hx, hy, yaw):
          44 +    c_, s_ = abs(np.cos(yaw)), abs(np.sin(yaw))
          45 +    return np.array(c), np.array([c_ * hx + s_ * hy, s_ * hx + c_ * hy])
          46 +
          47 +
          48 +def _gap(c1, h1, c2, h2):
          49 +    """Signed separation between two AABBs (positive = apart)."""
          50 +    return np.max(np.abs(np.asarray(c1) - np.asarray(c2)) - np.asarray(h1) - np.asarray(h2))
          51 +
          52 +
          53 +def _finger_boxes(xy, yaw):
          54 +    d = np.array([np.cos(yaw), np.sin(yaw)])
          55 +    out = []
          56 +    for sgn in (1, -1):
          57 +        out.append(_aabb_of_rect(np.asarray(xy) + sgn * F_OFF * d, F_HL, F_HW, yaw))
          58 +    return out
          59 +
          60 +
          61 +class GeneratedApproach:
          62 +    def __init__(self, action_space, observation_space, primitives):
          63 +        self.action_space = action_space
          64 +        self.observation_space = observation_space
          65 +
          66 +    # ------------------------------------------------------------ helpers
          67 +    def _obj(self, state, name):
          68 +        return state.get_object_from_name(name)
          69 +
          70 +    def _pose(self, state, name):
          71 +        o = self._obj(state, name)
          72 +        return (np.array([state.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')]),
          73 +                np.array([state.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]),
          74 +                np.array([state.get(o, f) for f in ('half_extent_x', 'half_extent_y', 'half_extent_z')]))
          75 +
          76 +    def _box(self, state, name):
          77 +        """(centre_xy, half_xy AABB, bottom z, top z)"""
          78 +        p, q, h = self._pose(state, name)
          79 +        c, hh = _aabb_of_rect(p[:2], h[0], h[1], _yaw_of_quat(q))
          80 +        return c, hh, p[2] - h[2], p[2] + h[2]
          81 +
          82 +    def _q(self, state):
          83 +        return np.array([state.get(self.robot, f) for f in JN])
          84 +
          85 +    def _x(self, state):
          86 +        return np.concatenate([np.array(self._base(state)), self._q(state)])
          87 +
          88 +    def _ik(self, xc, pt, R):
          89 +        if WB:
          90 +            return wb_ik2(xc, pt, R, iters=40, k_null=0.05, bx_max=-0.09)
          91 +        q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
          92 +        return np.concatenate([xc[:3], q]), ok
          93 +
          94 +    def _base(self, state):
          95 +        return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
          96 +                state.get(self.robot, 'pos_base_rot'))
          97 +
          98 +    def _tool(self, state):
          99 +        return tool_fk(self._q(state), self._base(state))
         100 +
         101 +    def _grasped_name(self, state):
         102 +        for n in self.names:
         103 +            if state.get(self._obj(state, n), 'grasp_active') > 0.5:
         104 +                return n
         105 +        return None
         106 +
         107 +    def _max_top(self, state, exclude=()):
         108 +        t = self.table_z
         109 +        for n in self.names:
         110 +            if n in exclude:
         111 +                continue
         112 +            t = max(t, self._box(state, n)[3])
         113 +        return t
         114 +
         115 +    # ------------------------------------------------------------ planning
         116 +    def reset(self, state, info):
         117 +        self.robot = state.get_object_from_name('robot')
         118 +        self.names = sorted(n for n in state.get_object_names() if n != 'robot')
         119 +        self.obstructions = sorted(n for n in self.names if n.startswith('obstruction'))
         120 +        rp, _, rh = self._pose(state, 'target_region')
         121 +        self.table_z = rp[2] - rh[2]
         122 +        self.region = (rp, rh)
         123 +        self.tasks = [(n, 'clear') for n in self._blocking_obstructions(state)]
         124 +        self.tasks.append(('target_block', 'goal'))
         125 +        self.phase = None
         126 +        self.qpath = []
         127 +        self.last_q = None
         128 +        self.last_a = None
         129 +        self.blocked = False
         130 +        self.look = STEP
         131 +        self.fails = {}
         132 +        self.blk_moves = {}
         133 +        self.stuck = 0
         134 +        self.descent_len = 0
         135 +        self.release_tries = 0
         136 +        self.grasp_attempt = 0
         137 +        self.total_fail = 0
         138 +        self.final_grip = 0.0
         139 +        self.wp_yaw = 0.0
         140 +        self._start_task(state)
         141 +
         142 +    def _blocking_obstructions(self, state, margin=0.003):
         143 +        rp, rh = self.region
         144 +        out = []
         145 +        for n in self.obstructions:
         146 +            c, hh, _, _ = self._box(state, n)
         147 +            if _gap(c, hh, rp[:2], rh[:2]) < margin:
         148 +                out.append(n)
         149 +        return out
         150 +
         151 +    def _finger_clearance(self, state, xy, yaw, tip_z, exclude):
         152 +        """Min xy gap between finger boxes and objects whose top is above tip_z."""
         153 +        clear = 1.0
         154 +        fbs = _finger_boxes(xy, yaw)
         155 +        for n in self.names:
         156 +            if n in exclude:
         157 +                continue
         158 +            c, hh, bot, top = self._box(state, n)
         159 +            if top < tip_z - 0.002:
         160 +                continue
         161 +            for fc, fh in fbs:
         162 +                g = _gap(fc, fh, c, hh)
         163 +                if g < clear:
         164 +                    clear = g
         165 +                    if g < 0.005:
         166 +                        self._blocker = n
         167 +        return clear
         168 +
         169 +    def _choose_yaw(self, state, name, kind, attempt):
         170 +        sc = self._yaw_scores(state, name, kind)
         171 +        c = sc[attempt % len(sc)]
         172 +        self.grasp_z = c[3]
         173 +        return c[1]
         174 +
         175 +    def _yaw_scores(self, state, name, kind):
         176 +        """Sorted [(clearance score, yaw, blocker, grasp z)] for grasp candidates."""
         177 +        p, q, h = self._pose(state, name)
         178 +        oy = _yaw_of_quat(q)
         179 +        lo = p[2] - h[2] + 0.045
         180 +        hi = p[2] + h[2] + 0.032
         181 +        gzs = [self._grasp_z(p, h)]
         182 +        if hi - 0.004 > gzs[0] + 0.004:
         183 +            gzs.append(hi - 0.004)
         184 +        cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
         185 +        T = self._tool(state)
         186 +        ty = np.arctan2(T[1, 0], T[0, 0])
         187 +        scored = []
         188 +        for j, gz in enumerate(gzs):
         189 +            for i, y in enumerate(cands):
         190 +                y = _wrap(2 * y) / 2  # modulo pi
         191 +                self._blocker = None
         192 +                c = self._finger_clearance(state, p[:2], y, gz - FINGER_DOWN, exclude=(name,))
         193 +                blk = self._blocker
         194 +                if kind == 'goal':
         195 +                    rp, rh = self.region
         196 +                    surf = rp[2] + rh[2]
         197 +                    tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
         198 +                    c = min(c, self._finger_clearance(state, rp[:2], y, tip,
         199 +                                                      exclude=(name, 'target_region')))
         200 +                rot = abs(_wrap(2 * (y - ty)) / 2)   # rotation needed (mod pi), <= pi/2
         201 +                scored.append((min(c, 0.02) - 0.0005 * i - 0.004 * j - 0.004 * rot, y, blk, gz))
         202 +        scored.sort(key=lambda t: -t[0])
         203 +        return scored
         204 +
         205 +    def _select_task(self, state):
         206 +        """Reorder tasks so the front one is graspable; add blockers if needed."""
         207 +        for _ in range(len(self.names)):
         208 +            name, kind = self.tasks[0]
         209 +            f = self.fails.get(name, 0)
         210 +            sc = self._yaw_scores(state, name, kind)
         211 +            if sc[0][0] > 0.002 and f < 4:
         212 +                return
         213 +            # try another pending clear task that is more graspable
         214 +            best = None
         215 +            for t in self.tasks:
         216 +                if t[1] != 'clear' or t[0] == name:
         217 +                    continue
         218 +                s2 = self._yaw_scores(state, t[0], 'clear')[0][0] - 0.01 * self.fails.get(t[0], 0)
         219 +                if best is None or s2 > best[0]:
         220 +                    best = (s2, t)
         221 +            if best is not None and best[0] > sc[0][0] - 0.01 * f + 0.001:
         222 +                self.tasks.remove(best[1])
         223 +                self.tasks.insert(0, best[1])
         224 +                continue
         225 +            # add the obstruction blocking the fingers as a new task
         226 +            blk = sc[0][2]
         227 +            if (blk is not None and blk.startswith('obstruction')
         228 +                    and all(t[0] != blk for t in self.tasks)
         229 +                    and self.blk_moves.get(blk, 0) < 2
         230 +                    and self._yaw_scores(state, blk, 'clear')[0][0] > 0.002):
         231 +                self.blk_moves[blk] = self.blk_moves.get(blk, 0) + 1
         232 +                self.tasks.insert(0, (blk, 'clear'))
         233 +                continue
         234 +            return
         235 +
         236 +    def _grasp_z(self, p, h):
         237 +        lo = p[2] - h[2] + 0.045
         238 +        hi = p[2] + h[2] + 0.032
         239 +        return 0.5 * (lo + hi) if hi > lo else hi - 0.001
         240 +
         241 +    def _free_spot(self, state, name, yaw, hold_off):
         242 +        """Pick a table spot clear of region/other objects (object + fingers)."""
         243 +        p0, _, _ = self._pose(state, name)
         244 +        c0, h, _, _ = self._box(state, name)
         245 +        others = []
         246 +        for n in self.names:
         247 +            if n == name:
         248 +                continue
         249 +            others.append(self._box(state, n))
         250 +        rp, rh = self.region
         251 +        tip = self.table_z + 0.001 + hold_off - FINGER_DOWN
         252 +        best, best_score = None, 1e9
         253 +        fb, fb_score = None, -1e9
         254 +        for x in np.linspace(0.2, 0.5, 16):
         255 +            for y in np.linspace(-0.34, 0.34, 35):
         256 +                c = np.array([x, y])
         257 +                clear = _gap(c, h, rp[:2], rh[:2]) - 0.03
         258 +                fbs = _finger_boxes(c, yaw)
         259 +                for oc, oh, bot, top in others:
         260 +                    clear = min(clear, _gap(c, h, oc, oh) - 0.02)
         261 +                    if top > tip - 0.002:
         262 +                        for fc, fh in fbs:
         263 +                            clear = min(clear, _gap(fc, fh, oc, oh) - 0.008)
         264 +                if clear > fb_score:
         265 +                    fb, fb_score = c, clear
         266 +                if clear >= 0:
         267 +                    score = np.linalg.norm(c - p0[:2])
         268 +                    if score < best_score:
         269 +                        best, best_score = c, score
         270 +        return best if best is not None else fb
         271 +
         272 +    def _transit_z(self, state, hold_off=0.0, exclude=()):
         273 +        top = self._max_top(state, exclude)
         274 +        return max(top + 0.03 + max(FINGER_DOWN, hold_off), 0.2)
         275 +
         276 +    def _start_task(self, state):
         277 +        if not self.tasks:
         278 +            self.phase = 'done'
         279 +            return
         280 +        try:
         281 +            self._select_task(state)
         282 +        except Exception:
         283 +            pass
         284 +        name, kind = self.tasks[0]
         285 +        p, q, h = self._pose(state, name)
         286 +        self.cur_obj = name
         287 +        self.grasp_yaw = self._choose_yaw(state, name, kind, self.fails.get(name, 0))
         288 +        gz = self.grasp_z
         289 +        zt = self._transit_z(state)
         290 +        tool = self._tool(state)[:3, 3]
         291 +        wps = []
         292 +        rs = 0
         293 +        if tool[2] < zt - 0.01:
         294 +            wps.append(np.array([tool[0], tool[1], zt]))
         295 +            rs = 1
         296 +        wps.append(np.array([p[0], p[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]))
         297 +        wps.append(np.array([p[0], p[1], gz]))
         298 +        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0, flip=True, rot_start=rs)
         299 +        self.phase = 'to_grasp'
         300 +
         301 +    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False, rot_start=0):
         302 +        """Cartesian waypoints -> dense joint path (IK warm-started).
         303 +        Yaw is interpolated from the current tool yaw over all but the last segment."""
         304 +        q = self._x(state)
         305 +        base = self._base(state)
         306 +        T0 = wb_fk(q)
         307 +        cur = T0[:3, 3]
         308 +        y0 = np.arctan2(T0[1, 0], T0[0, 0])
         309 +        dy = _wrap(yaw - y0)
         310 +        if flip and abs(dy) > np.pi / 2:
         311 +            dy = dy - np.sign(dy) * np.pi
         312 +        yaw = y0 + dy
         313 +        pts = [cur]
         314 +        for w in wps:
         315 +            pts.append(np.asarray(w, dtype=float))
         316 +        seg = [np.linalg.norm(pts[i + 1] - pts[i]) for i in range(len(wps))]
         317 +        if len(seg) - 1 <= rot_start:
         318 +            rot_start = 0
         319 +        rot0 = sum(seg[:rot_start])
         320 +        rot_len = sum(seg[rot_start:-1]) if len(seg) > 1 and sum(seg[rot_start:-1]) > 0.02 else sum(seg[rot_start:])
         321 +        rot_len = max(rot_len, 1e-6)
         322 +        path = []
         323 +        self.corners = set()
         324 +        qc = q.copy()
         325 +        travelled = 0.0
         326 +        for i, w in enumerate(wps):
         327 +            w = pts[i + 1]
         328 +            d = seg[i]
         329 +            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.04)))
         330 +            for k in range(1, n + 1):
         331 +                pt = cur + (w - cur) * k / n
         332 +                f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
         333 +                qn, ok = self._ik(qc, pt, down_R(y0 + f * dy))
         334 +                qn = qc + _wrap(qn - qc)
         335 +                path.append(qn)
         336 +                qc = qn
         337 +            travelled += d
         338 +            self.corners.add(len(path) - 1)
         339 +            cur = w
         340 +        self.qpath = path
         341 +        self.popped = 0
         342 +        self.wp_yaw = yaw
         343 +        self.final_grip = final_grip
         344 +        self.travel_grip = 1.0 if final_grip < 0 else 0.0
         345 +        self.stuck = 0
         346 +
         347 +    # ------------------------------------------------------------ control
         348 +    def _track(self, state):
         349 +        """Step along the precomputed joint path; None if done."""
         350 +        q = self._x(state)
         351 +        while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
         352 +            self.qpath.pop(0)
         353 +            self.popped += 1
         354 +        if not self.qpath:
         355 +            return None
         356 +        k = -1
         357 +        crossed = False
         358 +        for i, qp in enumerate(self.qpath):
         359 +            if np.max(np.abs(_wrap(qp - q))) <= self.look:
         360 +                if crossed and not self._safe_move(state, q, qp):
         361 +                    break
         362 +                k = i
         363 +                if (i + self.popped) in self.corners:
         364 +                    if not CUT_CORNERS or self.blocked or self.look < STEP:
         365 +                        break
         366 +                    crossed = True
         367 +            else:
         368 +                break
         369 +        a = np.zeros(11, dtype=np.float32)
         370 +        if k >= 0:
         371 +            self.qpath = self.qpath[k:]
         372 +            self.popped += k
         373 +            k = 0
         374 +            d = _wrap(self.qpath[0] - q)
         375 +            a[0:10] = d
         376 +            a[10] = self.travel_grip
         377 +            if MERGE_GRIP and len(self.qpath) == 1 and self.final_grip != 0.0:
         378 +                a[10] = self.final_grip
         379 +        else:
         380 +            d = _wrap(self.qpath[0] - q)
         381 +            a[0:10] = d * (self.look / np.max(np.abs(d)))
         382 +        return a
         383 +
         384 +    def _safe_move(self, state, q0, q1):
         385 +        """Check the joint-linear move q0->q1 keeps tool/fingers/held object
         386 +        above all nearby objects (used when cutting path corners)."""
         387 +        base = self._base(state)
         388 +        held = self._grasped_name(state)
         389 +        depth, rad = FINGER_DOWN, 0.075
         390 +        if held is not None:
         391 +            p, _, h = self._pose(state, held)
         392 +            tz = self._tool(state)[2, 3]
         393 +            depth = max(depth, tz - (p[2] - h[2]))
         394 +            rad = max(rad, np.hypot(h[0], h[1]) + 0.01)
         395 +        boxes = [self._box(state, n) for n in self.names if n != held]
         396 +        dq = _wrap(q1 - q0)
         397 +        for f in (0.25, 0.5, 0.75, 1.0):
         398 +            pt = wb_fk(q0 + f * dq)[:3, 3]
         399 +            low = pt[2] - depth
         400 +            if low < self.table_z + 0.01:
         401 +                return False
         402 +            for c, hh, bot, top in boxes:
         403 +                dxy = np.maximum(np.abs(pt[:2] - c) - hh, 0.0)
         404 +                if np.hypot(dxy[0], dxy[1]) < rad and low < top + 0.012:
         405 +                    return False
         406 +        return True
         407 +
         408 +    def _noop(self, grip=0.0):
         409 +        a = np.zeros(11, dtype=np.float32); a[10] = grip
         410 +        return a
         411 +
         412 +    def get_action(self, state):
         413 +        q = self._x(state)
         414 +        moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
         415 +        attempted = self.last_a is not None and np.any(np.abs(self.last_a[0:10]) > 1e-9)
         416 +        self.blocked = attempted and not moved
         417 +        if self.blocked:
         418 +            self.look = max(0.02, self.look * 0.35)
         419 +        elif attempted:
         420 +            self.look = min(STEP, self.look * 1.5)
         421 +        self.last_q = q.copy()
         422 +        try:
         423 +            a = self._policy(state)
         424 +        except Exception:
         425 +            a = self._noop()
         426 +        a = np.asarray(a, dtype=np.float32).copy()
         427 +        a[:10] = np.clip(a[:10], -STEP, STEP)
         428 +        a[10] = np.clip(a[10], -1, 1)
         429 +        self.last_a = a
         430 +        return a
         431 +
         432 +    def _policy(self, state):
         433 +        ph = self.phase
         434 +        if ph == 'done':
         435 +            if self._grasped_name(state) is None and self.tasks:
         436 +                self._start_task(state)
         437 +            return self._noop()
         438 +
         439 +        if ph == 'to_grasp':
         440 +            g = self._grasped_name(state)
         441 +            if g is not None:
         442 +                return self._on_grasped(state, g)
         443 +            if self.blocked:
         444 +                self.stuck += 1
         445 +                if self.stuck >= 2:
         446 +                    if self._tool(state)[2, 3] > self.grasp_z + 0.012:
         447 +                        # cannot get down to the grasp: try something else
         448 +                        self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         449 +                        self._start_task(state)
         450 +                        a = self._track(state)
         451 +                        return a if a is not None else self._noop()
         452 +                    self.qpath = []
         453 +            a = self._track(state)
         454 +            if a is not None:
         455 +                return a
         456 +            self.phase = 'close'
         457 +            return self._noop(-1.0)
         458 +
         459 +        if ph == 'close':
         460 +            g = self._grasped_name(state)
         461 +            if g is None:
         462 +                self.grasp_attempt += 1
         463 +                self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         464 +                self.total_fail += 1
         465 +                self._start_task(state)
         466 +                return self._track(state) if self.qpath else self._noop()
         467 +            return self._on_grasped(state, g)
         468 +
         469 +        if ph == 'to_place':
         470 +            if self._grasped_name(state) is None:
         471 +                return self._on_released(state)
         472 +            if self.blocked:
         473 +                self.stuck += 1
         474 +                if len(self.qpath) <= self.descent_len:
         475 +                    self.qpath = []
         476 +                elif self.stuck >= 3:
         477 +                    self._plan_place(state, replan=True)
         478 +            a = self._track(state)
         479 +            if a is not None:
         480 +                return a
         481 +            self.phase = 'open'
         482 +            return self._noop(1.0)
         483 +
         484 +        if ph == 'open':
         485 +            if self._grasped_name(state) is None:
         486 +                return self._on_released(state)
         487 +            self.release_tries += 1
         488 +            tool = self._tool(state)[:3, 3]
         489 +            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw, final_grip=1.0)
         490 +            self.descent_len = 2
         491 +            self.phase = 'to_place'
         492 +            if self.release_tries > 12:
         493 +                self.release_tries = 0
         494 +                self._plan_place(state, replan=True)
         495 +            a = self._track(state)
         496 +            return a if a is not None else self._noop(1.0)
         497 +
         498 +        if ph == 'retreat':
         499 +            if self.blocked:
         500 +                self.stuck += 1
         501 +                if self.stuck >= 2:
         502 +                    self.qpath = []
         503 +            a = self._track(state)
         504 +            if a is not None:
         505 +                return a
         506 +            self._next_task(state)
         507 +            a = self._track(state) if self.phase == 'to_grasp' else None
         508 +            return a if a is not None else self._noop()
         509 +
         510 +        return self._noop()
         511 +
         512 +    def _on_grasped(self, state, g):
         513 +        self.grasp_attempt = 0
         514 +        if g != self.cur_obj:
         515 +            self.tasks.insert(0, (g, 'clear'))
         516 +            self.cur_obj = g
         517 +        self._plan_place(state)
         518 +        a = self._track(state)
         519 +        return a if a is not None else self._noop()
         520 +
         521 +    def _on_released(self, state):
         522 +        self.release_tries = 0
         523 +        name, kind = self.tasks.pop(0) if self.tasks else (None, None)
         524 +        if kind == 'goal':
         525 +            self.phase = 'done'
         526 +            return self._noop()
         527 +        self._next_task(state)
         528 +        a = self._track(state) if self.phase == 'to_grasp' else None
         529 +        return a if a is not None else self._noop()
         530 +
         531 +    def _next_task(self, state):
         532 +        if self.tasks and self.tasks[0][1] == 'goal':
         533 +            for n in self._blocking_obstructions(state):
         534 +                if all(t[0] != n for t in self.tasks):
         535 +                    self.tasks.insert(0, (n, 'clear'))
         536 +        self._start_task(state)
         537 +
         538 +    def _plan_place(self, state, replan=False):
         539 +        name = self.cur_obj
         540 +        p, qo, h = self._pose(state, name)
         541 +        r = self.robot
         542 +        tf = _T([state.get(r, 'grasp_tf_x'), state.get(r, 'grasp_tf_y'), state.get(r, 'grasp_tf_z')],
         543 +                [state.get(r, 'grasp_tf_qx'), state.get(r, 'grasp_tf_qy'), state.get(r, 'grasp_tf_qz'),
         544 +                 state.get(r, 'grasp_tf_qw')])
         545 +        kind = self.tasks[0][1] if self.tasks and self.tasks[0][0] == name else 'clear'
         546 +        Ttool_now = self._tool(state)
         547 +        hold_off = Ttool_now[2, 3] - (p[2] - h[2])   # tool height above held-object bottom
         548 +        yaw = np.arctan2(Ttool_now[1, 0], Ttool_now[0, 0])
         549 +        if kind == 'goal':
         550 +            rp, rh = self.region
         551 +            xy = rp[:2]
         552 +            surf = rp[2] + rh[2]
         553 +        else:
         554 +            xy = self._free_spot(state, name, yaw, hold_off)
         555 +            if replan:
         556 +                xy = xy + np.random.uniform(-0.03, 0.03, 2)
         557 +            surf = self.table_z
         558 +        Tobj = _T([xy[0], xy[1], surf + h[2] + 0.001], qo)
         559 +        Ttool = Tobj @ np.linalg.inv(tf)
         560 +        tgt = Ttool[:3, 3]
         561 +        tyaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
         562 +        zt = self._transit_z(state, hold_off, exclude=(name,))
         563 +        tool = Ttool_now[:3, 3]
         564 +        wps = []
         565 +        if tool[2] < zt - 0.005:
         566 +            wps.append(np.array([tool[0], tool[1], zt]))
         567 +        wps += [np.array([tgt[0], tgt[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]),
         568 +                np.array([tgt[0], tgt[1], tgt[2] + 0.015])]
         569 +        self._set_path(state, wps, tyaw)
         570 +        n_before = len(self.qpath)
         571 +        self._append_descent(state, tgt, tyaw)
         572 +        self.descent_len = len(self.qpath) - n_before + 2
         573 +        self.final_grip = 1.0
         574 +        self.phase = 'to_place'
         575 +
         576 +    def _append_descent(self, state, tgt, yaw):
         577 +        base = self._base(state)
         578 +        qc = self.qpath[-1] if self.qpath else self._x(state)
         579 +        R = down_R(yaw)
         580 +        for dz in (0.008, 0.003, 0.0):
         581 +            qn, ok = self._ik(qc, tgt + np.array([0, 0, dz]), R)
         582 +            qn = qc + _wrap(qn - qc)
         583 +            self.qpath.append(qn)
         584 +            qc = qn
diff --git a/v_0.05_-0.09/env_client.py b/v_0.05_-0.09/env_client.py
new file mode 100644
index 0000000..108c884
--- /dev/null
+++ b/v_0.05_-0.09/env_client.py
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
diff --git a/v_0.05_-0.09/env_spaces.json b/v_0.05_-0.09/env_spaces.json
new file mode 100644
index 0000000..dff8dfd
--- /dev/null
+++ b/v_0.05_-0.09/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "6eefef35bfaa192f7898ebf189cf2b7d", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
diff --git a/v_0.05_-0.09/kin.py b/v_0.05_-0.09/kin.py
new file mode 100644
index 0000000..b360a71
--- /dev/null
+++ b/v_0.05_-0.09/kin.py
@@ -0,0 +1,172 @@
           1 +import numpy as np
           2 +
           3 +def _rpy(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def _T(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = _rpy(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +PI = np.pi
          13 +H = PI / 2
          14 +JOINTS = [
          15 +    _T((0, 0, 0.15643), (PI, 0, 0)),
          16 +    _T((0, 0.005375, -0.12838), (H, 0, 0)),
          17 +    _T((0, -0.21038, -0.006375), (-H, 0, 0)),
          18 +    _T((0, 0.006375, -0.21038), (H, 0, 0)),
          19 +    _T((0, -0.20843, -0.006375), (-H, 0, 0)),
          20 +    _T((0, 0.00017505, -0.10593), (H, 0, 0)),
          21 +    _T((0, -0.10593, -0.00017505), (-H, 0, 0)),
          22 +]
          23 +EE = _T((0, 0, -0.061525), (PI, 0, 0))
          24 +MOUNT = (0.12, 0.0, -0.0052)
          25 +TOOL = 0.12
          26 +HOME = np.array([0.0, -0.35, -np.pi, -2.5, 0.0, -0.87, np.pi / 2])
          27 +
          28 +def _rz(q):
          29 +    c, s = np.cos(q), np.sin(q)
          30 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          31 +
          32 +def mount_base(base):
          33 +    bx, by, br = base
          34 +    c, s = np.cos(br), np.sin(br)
          35 +    return (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
          36 +
          37 +def _chain(q, base):
          38 +    """Returns tool transform and list of (axis, origin) of joints in world."""
          39 +    bx, by, br = mount_base(base)
          40 +    T = _rz(br); T[0, 3] = bx; T[1, 3] = by; T[2, 3] = MOUNT[2]
          41 +    axes = []
          42 +    for Tj, qj in zip(JOINTS, q):
          43 +        T = T @ Tj
          44 +        axes.append((T[:3, 2].copy(), T[:3, 3].copy()))
          45 +        T = T @ _rz(qj)
          46 +    T = T @ EE
          47 +    Tt = np.eye(4); Tt[2, 3] = TOOL
          48 +    return T @ Tt, axes
          49 +
          50 +def tool_fk(q, base):
          51 +    return _chain(q, base)[0]
          52 +
          53 +def _rot_err(Rc, Rd):
          54 +    Re = Rd @ Rc.T
          55 +    v = 0.5 * np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
          56 +    return v
          57 +
          58 +def tool_ik(q0, p, R, base, iters=60, tol=1e-5, q_nom=None, k_null=0.3):
          59 +    q = np.array(q0, dtype=float)
          60 +    if q_nom is None:
          61 +        q_nom = HOME
          62 +    for it in range(iters):
          63 +        T, axes = _chain(q, base)
          64 +        e = np.concatenate([p - T[:3, 3], _rot_err(T[:3, :3], R)])
          65 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
          66 +            return q, True
          67 +        J = np.zeros((6, 7))
          68 +        pt = T[:3, 3]
          69 +        for j, (z, o) in enumerate(axes):
          70 +            J[:3, j] = np.cross(z, pt - o)
          71 +            J[3:, j] = z
          72 +        JJt = J @ J.T + 1e-6 * np.eye(6)
          73 +        Jp = J.T @ np.linalg.inv(JJt)
          74 +        dq = Jp @ e
          75 +        dn = (q_nom - q + np.pi) % (2 * np.pi) - np.pi
          76 +        dq += (np.eye(7) - Jp @ J) @ (k_null * dn)
          77 +        n = np.max(np.abs(dq))
          78 +        if n > 0.3:
          79 +            dq *= 0.3 / n
          80 +        q = q + dq
          81 +    T, _ = _chain(q, base)
          82 +    ok = np.linalg.norm(p - T[:3, 3]) < 1e-3
          83 +    return q, ok
          84 +
          85 +def down_R(yaw):
          86 +    c, s = np.cos(yaw), np.sin(yaw)
          87 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          88 +    return np.stack([x, y, z], axis=1)
          89 +
          90 +
          91 +def wb_fk(x):
          92 +    """x = [bx, by, br, q1..q7] -> tool transform."""
          93 +    return _chain(x[3:], x[:3])[0]
          94 +
          95 +
          96 +def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1.0):
          97 +    """Whole-body IK over base y, base rot and the 7 arm joints (base x fixed)."""
          98 +    x = np.array(x0, dtype=float)
          99 +    if q_nom is None:
         100 +        q_nom = HOME
         101 +    W = np.array([w_by, w_br] + [1.0] * 7)
         102 +    for it in range(iters):
         103 +        T, axes = _chain(x[3:], x[:3])
         104 +        pt = T[:3, 3]
         105 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         106 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         107 +            return x, True
         108 +        J = np.zeros((6, 9))
         109 +        J[1, 0] = 1.0
         110 +        ez = np.array([0.0, 0.0, 1.0])
         111 +        J[:3, 1] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         112 +        J[3:, 1] = ez
         113 +        for j, (z, o) in enumerate(axes):
         114 +            J[:3, 2 + j] = np.cross(z, pt - o)
         115 +            J[3:, 2 + j] = z
         116 +        JW = J * W
         117 +        Jp = JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6))
         118 +        Jp = W[:, None] * Jp
         119 +        dv = Jp @ e
         120 +        dn = np.zeros(9)
         121 +        dn[2:] = k_null * ((q_nom - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         122 +        dv += dn - Jp @ (J @ dn)
         123 +        n = np.max(np.abs(dv))
         124 +        if n > 0.3:
         125 +            dv *= 0.3 / n
         126 +        x[1:] += dv
         127 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         128 +    return x, ok
         129 +
         130 +
         131 +Q_NOM = np.array([0.0, 0.3, -np.pi, -2.15, 0.0, -0.69, 0.0])
         132 +K_NOM = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
         133 +
         134 +
         135 +def wb_ik2(x0, p, R, iters=40, tol=1e-5, k_null=0.3, bx_max=-0.12, w_base=1.0):
         136 +    """Whole-body IK over base x (<= bx_max), y, rot and the 7 arm joints.
         137 +    Null space pulls the arm to an extended nominal posture Q_NOM."""
         138 +    x = np.array(x0, dtype=float)
         139 +    ez = np.array([0.0, 0.0, 1.0])
         140 +    for it in range(iters):
         141 +        T, axes = _chain(x[3:], x[:3])
         142 +        pt = T[:3, 3]
         143 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         144 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         145 +            return x, True
         146 +        J = np.zeros((6, 10))
         147 +        J[0, 0] = 1.0
         148 +        J[1, 1] = 1.0
         149 +        J[:3, 2] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         150 +        J[3:, 2] = ez
         151 +        for j, (z, o) in enumerate(axes):
         152 +            J[:3, 3 + j] = np.cross(z, pt - o)
         153 +            J[3:, 3 + j] = z
         154 +        dn = np.zeros(10)
         155 +        dn[3:] = k_null * K_NOM * ((Q_NOM - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         156 +        W = np.array([w_base, w_base, w_base] + [1.0] * 7)
         157 +        for _ in range(2):
         158 +            JW = J * W
         159 +            Jp = W[:, None] * (JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6)))
         160 +            dv = Jp @ e + dn - Jp @ (J @ dn)
         161 +            n = np.max(np.abs(dv))
         162 +            if n > 0.3:
         163 +                dv *= 0.3 / n
         164 +            if x[0] + dv[0] > bx_max + 1e-9 and W[0] > 0:
         165 +                W[0] = 0.0
         166 +                x[0] = min(x[0], bx_max)
         167 +                continue
         168 +            break
         169 +        x += dv
         170 +        x[0] = min(x[0], bx_max) if x0[0] <= bx_max + 1e-9 else x[0]
         171 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         172 +    return x, ok
diff --git a/v_0.05_-0.09/test_approach.py b/v_0.05_-0.09/test_approach.py
new file mode 100644
index 0000000..afc13cc
--- /dev/null
+++ b/v_0.05_-0.09/test_approach.py
@@ -0,0 +1,36 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +def run(seed, verbose=False, max_steps=None, count=None):
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed, options={'object_count': count} if count else None)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0 = time.time()
          11 +    ap.reset(obs, info)
          12 +    ms = max_steps or env.max_steps
          13 +    steps = 0
          14 +    term = False
          15 +    pt = 0.0
          16 +    for steps in range(1, ms + 1):
          17 +        t1 = time.time()
          18 +        a = ap.get_action(obs)
          19 +        pt += time.time() - t1
          20 +        obs, r, term, trunc, info = env.step(a)
          21 +        if term or trunc:
          22 +            break
          23 +    dt = time.time() - t0
          24 +    nobs = len([n for n in obs.get_object_names() if n.startswith('obstruction')])
          25 +    env.close()
          26 +    return term, steps, dt, nobs, ap.phase, pt
          27 +
          28 +if __name__ == '__main__':
          29 +    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          30 +    count = int(sys.argv[3]) if len(sys.argv) > 3 else None
          31 +    ok = 0
          32 +    for s in seeds:
          33 +        term, steps, dt, n, ph, pt = run(s, count=count)
          34 +        ok += term
          35 +        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s ptime={pt:.1f}s nobs={n} phase={ph}', flush=True)
          36 +    print(f'{ok}/{len(seeds)}')
diff --git a/v_0.1_-0.09/approach.py b/v_0.1_-0.09/approach.py
new file mode 100644
index 0000000..5ee0d42
--- /dev/null
+++ b/v_0.1_-0.09/approach.py
@@ -0,0 +1,584 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place
           2 +the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py).
           3 +
           4 +Empirical facts (black-box probing):
           5 +- Arm mount is +0.12m along base x; the grasp/tool frame is 0.12m past the flange.
           6 +- Gripper fingers lie along the tool x axis, extending ~0.07m from the centre and
           7 +  ~0.035m below the tool frame.  Robot/held object collisions reject a step.
           8 +- Grasp (close) succeeds when tool z in [bottom+0.044, top+0.033] over the object.
           9 +- Release (open) succeeds only if the held object rests within a few mm of a surface.
          10 +"""
          11 +import numpy as np
          12 +from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik, wb_ik2
          13 +
          14 +JN = [f'joint_{i}' for i in range(1, 8)]
          15 +MERGE_GRIP = True
          16 +WB = True
          17 +CUT_CORNERS = True
          18 +STEP = 0.2             # max joint delta per step
          19 +FINGER_DOWN = 0.036    # fingertips below tool frame
          20 +F_OFF, F_HL, F_HW = 0.046, 0.024, 0.013   # finger centre offset, half length, half width
          21 +
          22 +
          23 +def _q2R(x, y, z, w):
          24 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          25 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          26 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          27 +
          28 +
          29 +def _T(p, q):
          30 +    M = np.eye(4); M[:3, :3] = _q2R(*q); M[:3, 3] = p
          31 +    return M
          32 +
          33 +
          34 +def _yaw_of_quat(q):
          35 +    x, y, z, w = q
          36 +    return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
          37 +
          38 +
          39 +def _wrap(a):
          40 +    return (a + np.pi) % (2 * np.pi) - np.pi
          41 +
          42 +
          43 +def _aabb_of_rect(c, hx, hy, yaw):
          44 +    c_, s_ = abs(np.cos(yaw)), abs(np.sin(yaw))
          45 +    return np.array(c), np.array([c_ * hx + s_ * hy, s_ * hx + c_ * hy])
          46 +
          47 +
          48 +def _gap(c1, h1, c2, h2):
          49 +    """Signed separation between two AABBs (positive = apart)."""
          50 +    return np.max(np.abs(np.asarray(c1) - np.asarray(c2)) - np.asarray(h1) - np.asarray(h2))
          51 +
          52 +
          53 +def _finger_boxes(xy, yaw):
          54 +    d = np.array([np.cos(yaw), np.sin(yaw)])
          55 +    out = []
          56 +    for sgn in (1, -1):
          57 +        out.append(_aabb_of_rect(np.asarray(xy) + sgn * F_OFF * d, F_HL, F_HW, yaw))
          58 +    return out
          59 +
          60 +
          61 +class GeneratedApproach:
          62 +    def __init__(self, action_space, observation_space, primitives):
          63 +        self.action_space = action_space
          64 +        self.observation_space = observation_space
          65 +
          66 +    # ------------------------------------------------------------ helpers
          67 +    def _obj(self, state, name):
          68 +        return state.get_object_from_name(name)
          69 +
          70 +    def _pose(self, state, name):
          71 +        o = self._obj(state, name)
          72 +        return (np.array([state.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')]),
          73 +                np.array([state.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]),
          74 +                np.array([state.get(o, f) for f in ('half_extent_x', 'half_extent_y', 'half_extent_z')]))
          75 +
          76 +    def _box(self, state, name):
          77 +        """(centre_xy, half_xy AABB, bottom z, top z)"""
          78 +        p, q, h = self._pose(state, name)
          79 +        c, hh = _aabb_of_rect(p[:2], h[0], h[1], _yaw_of_quat(q))
          80 +        return c, hh, p[2] - h[2], p[2] + h[2]
          81 +
          82 +    def _q(self, state):
          83 +        return np.array([state.get(self.robot, f) for f in JN])
          84 +
          85 +    def _x(self, state):
          86 +        return np.concatenate([np.array(self._base(state)), self._q(state)])
          87 +
          88 +    def _ik(self, xc, pt, R):
          89 +        if WB:
          90 +            return wb_ik2(xc, pt, R, iters=40, k_null=0.1, bx_max=-0.09)
          91 +        q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
          92 +        return np.concatenate([xc[:3], q]), ok
          93 +
          94 +    def _base(self, state):
          95 +        return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
          96 +                state.get(self.robot, 'pos_base_rot'))
          97 +
          98 +    def _tool(self, state):
          99 +        return tool_fk(self._q(state), self._base(state))
         100 +
         101 +    def _grasped_name(self, state):
         102 +        for n in self.names:
         103 +            if state.get(self._obj(state, n), 'grasp_active') > 0.5:
         104 +                return n
         105 +        return None
         106 +
         107 +    def _max_top(self, state, exclude=()):
         108 +        t = self.table_z
         109 +        for n in self.names:
         110 +            if n in exclude:
         111 +                continue
         112 +            t = max(t, self._box(state, n)[3])
         113 +        return t
         114 +
         115 +    # ------------------------------------------------------------ planning
         116 +    def reset(self, state, info):
         117 +        self.robot = state.get_object_from_name('robot')
         118 +        self.names = sorted(n for n in state.get_object_names() if n != 'robot')
         119 +        self.obstructions = sorted(n for n in self.names if n.startswith('obstruction'))
         120 +        rp, _, rh = self._pose(state, 'target_region')
         121 +        self.table_z = rp[2] - rh[2]
         122 +        self.region = (rp, rh)
         123 +        self.tasks = [(n, 'clear') for n in self._blocking_obstructions(state)]
         124 +        self.tasks.append(('target_block', 'goal'))
         125 +        self.phase = None
         126 +        self.qpath = []
         127 +        self.last_q = None
         128 +        self.last_a = None
         129 +        self.blocked = False
         130 +        self.look = STEP
         131 +        self.fails = {}
         132 +        self.blk_moves = {}
         133 +        self.stuck = 0
         134 +        self.descent_len = 0
         135 +        self.release_tries = 0
         136 +        self.grasp_attempt = 0
         137 +        self.total_fail = 0
         138 +        self.final_grip = 0.0
         139 +        self.wp_yaw = 0.0
         140 +        self._start_task(state)
         141 +
         142 +    def _blocking_obstructions(self, state, margin=0.003):
         143 +        rp, rh = self.region
         144 +        out = []
         145 +        for n in self.obstructions:
         146 +            c, hh, _, _ = self._box(state, n)
         147 +            if _gap(c, hh, rp[:2], rh[:2]) < margin:
         148 +                out.append(n)
         149 +        return out
         150 +
         151 +    def _finger_clearance(self, state, xy, yaw, tip_z, exclude):
         152 +        """Min xy gap between finger boxes and objects whose top is above tip_z."""
         153 +        clear = 1.0
         154 +        fbs = _finger_boxes(xy, yaw)
         155 +        for n in self.names:
         156 +            if n in exclude:
         157 +                continue
         158 +            c, hh, bot, top = self._box(state, n)
         159 +            if top < tip_z - 0.002:
         160 +                continue
         161 +            for fc, fh in fbs:
         162 +                g = _gap(fc, fh, c, hh)
         163 +                if g < clear:
         164 +                    clear = g
         165 +                    if g < 0.005:
         166 +                        self._blocker = n
         167 +        return clear
         168 +
         169 +    def _choose_yaw(self, state, name, kind, attempt):
         170 +        sc = self._yaw_scores(state, name, kind)
         171 +        c = sc[attempt % len(sc)]
         172 +        self.grasp_z = c[3]
         173 +        return c[1]
         174 +
         175 +    def _yaw_scores(self, state, name, kind):
         176 +        """Sorted [(clearance score, yaw, blocker, grasp z)] for grasp candidates."""
         177 +        p, q, h = self._pose(state, name)
         178 +        oy = _yaw_of_quat(q)
         179 +        lo = p[2] - h[2] + 0.045
         180 +        hi = p[2] + h[2] + 0.032
         181 +        gzs = [self._grasp_z(p, h)]
         182 +        if hi - 0.004 > gzs[0] + 0.004:
         183 +            gzs.append(hi - 0.004)
         184 +        cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
         185 +        T = self._tool(state)
         186 +        ty = np.arctan2(T[1, 0], T[0, 0])
         187 +        scored = []
         188 +        for j, gz in enumerate(gzs):
         189 +            for i, y in enumerate(cands):
         190 +                y = _wrap(2 * y) / 2  # modulo pi
         191 +                self._blocker = None
         192 +                c = self._finger_clearance(state, p[:2], y, gz - FINGER_DOWN, exclude=(name,))
         193 +                blk = self._blocker
         194 +                if kind == 'goal':
         195 +                    rp, rh = self.region
         196 +                    surf = rp[2] + rh[2]
         197 +                    tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
         198 +                    c = min(c, self._finger_clearance(state, rp[:2], y, tip,
         199 +                                                      exclude=(name, 'target_region')))
         200 +                rot = abs(_wrap(2 * (y - ty)) / 2)   # rotation needed (mod pi), <= pi/2
         201 +                scored.append((min(c, 0.02) - 0.0005 * i - 0.004 * j - 0.004 * rot, y, blk, gz))
         202 +        scored.sort(key=lambda t: -t[0])
         203 +        return scored
         204 +
         205 +    def _select_task(self, state):
         206 +        """Reorder tasks so the front one is graspable; add blockers if needed."""
         207 +        for _ in range(len(self.names)):
         208 +            name, kind = self.tasks[0]
         209 +            f = self.fails.get(name, 0)
         210 +            sc = self._yaw_scores(state, name, kind)
         211 +            if sc[0][0] > 0.002 and f < 4:
         212 +                return
         213 +            # try another pending clear task that is more graspable
         214 +            best = None
         215 +            for t in self.tasks:
         216 +                if t[1] != 'clear' or t[0] == name:
         217 +                    continue
         218 +                s2 = self._yaw_scores(state, t[0], 'clear')[0][0] - 0.01 * self.fails.get(t[0], 0)
         219 +                if best is None or s2 > best[0]:
         220 +                    best = (s2, t)
         221 +            if best is not None and best[0] > sc[0][0] - 0.01 * f + 0.001:
         222 +                self.tasks.remove(best[1])
         223 +                self.tasks.insert(0, best[1])
         224 +                continue
         225 +            # add the obstruction blocking the fingers as a new task
         226 +            blk = sc[0][2]
         227 +            if (blk is not None and blk.startswith('obstruction')
         228 +                    and all(t[0] != blk for t in self.tasks)
         229 +                    and self.blk_moves.get(blk, 0) < 2
         230 +                    and self._yaw_scores(state, blk, 'clear')[0][0] > 0.002):
         231 +                self.blk_moves[blk] = self.blk_moves.get(blk, 0) + 1
         232 +                self.tasks.insert(0, (blk, 'clear'))
         233 +                continue
         234 +            return
         235 +
         236 +    def _grasp_z(self, p, h):
         237 +        lo = p[2] - h[2] + 0.045
         238 +        hi = p[2] + h[2] + 0.032
         239 +        return 0.5 * (lo + hi) if hi > lo else hi - 0.001
         240 +
         241 +    def _free_spot(self, state, name, yaw, hold_off):
         242 +        """Pick a table spot clear of region/other objects (object + fingers)."""
         243 +        p0, _, _ = self._pose(state, name)
         244 +        c0, h, _, _ = self._box(state, name)
         245 +        others = []
         246 +        for n in self.names:
         247 +            if n == name:
         248 +                continue
         249 +            others.append(self._box(state, n))
         250 +        rp, rh = self.region
         251 +        tip = self.table_z + 0.001 + hold_off - FINGER_DOWN
         252 +        best, best_score = None, 1e9
         253 +        fb, fb_score = None, -1e9
         254 +        for x in np.linspace(0.2, 0.5, 16):
         255 +            for y in np.linspace(-0.34, 0.34, 35):
         256 +                c = np.array([x, y])
         257 +                clear = _gap(c, h, rp[:2], rh[:2]) - 0.03
         258 +                fbs = _finger_boxes(c, yaw)
         259 +                for oc, oh, bot, top in others:
         260 +                    clear = min(clear, _gap(c, h, oc, oh) - 0.02)
         261 +                    if top > tip - 0.002:
         262 +                        for fc, fh in fbs:
         263 +                            clear = min(clear, _gap(fc, fh, oc, oh) - 0.008)
         264 +                if clear > fb_score:
         265 +                    fb, fb_score = c, clear
         266 +                if clear >= 0:
         267 +                    score = np.linalg.norm(c - p0[:2])
         268 +                    if score < best_score:
         269 +                        best, best_score = c, score
         270 +        return best if best is not None else fb
         271 +
         272 +    def _transit_z(self, state, hold_off=0.0, exclude=()):
         273 +        top = self._max_top(state, exclude)
         274 +        return max(top + 0.03 + max(FINGER_DOWN, hold_off), 0.2)
         275 +
         276 +    def _start_task(self, state):
         277 +        if not self.tasks:
         278 +            self.phase = 'done'
         279 +            return
         280 +        try:
         281 +            self._select_task(state)
         282 +        except Exception:
         283 +            pass
         284 +        name, kind = self.tasks[0]
         285 +        p, q, h = self._pose(state, name)
         286 +        self.cur_obj = name
         287 +        self.grasp_yaw = self._choose_yaw(state, name, kind, self.fails.get(name, 0))
         288 +        gz = self.grasp_z
         289 +        zt = self._transit_z(state)
         290 +        tool = self._tool(state)[:3, 3]
         291 +        wps = []
         292 +        rs = 0
         293 +        if tool[2] < zt - 0.01:
         294 +            wps.append(np.array([tool[0], tool[1], zt]))
         295 +            rs = 1
         296 +        wps.append(np.array([p[0], p[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]))
         297 +        wps.append(np.array([p[0], p[1], gz]))
         298 +        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0, flip=True, rot_start=rs)
         299 +        self.phase = 'to_grasp'
         300 +
         301 +    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False, rot_start=0):
         302 +        """Cartesian waypoints -> dense joint path (IK warm-started).
         303 +        Yaw is interpolated from the current tool yaw over all but the last segment."""
         304 +        q = self._x(state)
         305 +        base = self._base(state)
         306 +        T0 = wb_fk(q)
         307 +        cur = T0[:3, 3]
         308 +        y0 = np.arctan2(T0[1, 0], T0[0, 0])
         309 +        dy = _wrap(yaw - y0)
         310 +        if flip and abs(dy) > np.pi / 2:
         311 +            dy = dy - np.sign(dy) * np.pi
         312 +        yaw = y0 + dy
         313 +        pts = [cur]
         314 +        for w in wps:
         315 +            pts.append(np.asarray(w, dtype=float))
         316 +        seg = [np.linalg.norm(pts[i + 1] - pts[i]) for i in range(len(wps))]
         317 +        if len(seg) - 1 <= rot_start:
         318 +            rot_start = 0
         319 +        rot0 = sum(seg[:rot_start])
         320 +        rot_len = sum(seg[rot_start:-1]) if len(seg) > 1 and sum(seg[rot_start:-1]) > 0.02 else sum(seg[rot_start:])
         321 +        rot_len = max(rot_len, 1e-6)
         322 +        path = []
         323 +        self.corners = set()
         324 +        qc = q.copy()
         325 +        travelled = 0.0
         326 +        for i, w in enumerate(wps):
         327 +            w = pts[i + 1]
         328 +            d = seg[i]
         329 +            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.04)))
         330 +            for k in range(1, n + 1):
         331 +                pt = cur + (w - cur) * k / n
         332 +                f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
         333 +                qn, ok = self._ik(qc, pt, down_R(y0 + f * dy))
         334 +                qn = qc + _wrap(qn - qc)
         335 +                path.append(qn)
         336 +                qc = qn
         337 +            travelled += d
         338 +            self.corners.add(len(path) - 1)
         339 +            cur = w
         340 +        self.qpath = path
         341 +        self.popped = 0
         342 +        self.wp_yaw = yaw
         343 +        self.final_grip = final_grip
         344 +        self.travel_grip = 1.0 if final_grip < 0 else 0.0
         345 +        self.stuck = 0
         346 +
         347 +    # ------------------------------------------------------------ control
         348 +    def _track(self, state):
         349 +        """Step along the precomputed joint path; None if done."""
         350 +        q = self._x(state)
         351 +        while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
         352 +            self.qpath.pop(0)
         353 +            self.popped += 1
         354 +        if not self.qpath:
         355 +            return None
         356 +        k = -1
         357 +        crossed = False
         358 +        for i, qp in enumerate(self.qpath):
         359 +            if np.max(np.abs(_wrap(qp - q))) <= self.look:
         360 +                if crossed and not self._safe_move(state, q, qp):
         361 +                    break
         362 +                k = i
         363 +                if (i + self.popped) in self.corners:
         364 +                    if not CUT_CORNERS or self.blocked or self.look < STEP:
         365 +                        break
         366 +                    crossed = True
         367 +            else:
         368 +                break
         369 +        a = np.zeros(11, dtype=np.float32)
         370 +        if k >= 0:
         371 +            self.qpath = self.qpath[k:]
         372 +            self.popped += k
         373 +            k = 0
         374 +            d = _wrap(self.qpath[0] - q)
         375 +            a[0:10] = d
         376 +            a[10] = self.travel_grip
         377 +            if MERGE_GRIP and len(self.qpath) == 1 and self.final_grip != 0.0:
         378 +                a[10] = self.final_grip
         379 +        else:
         380 +            d = _wrap(self.qpath[0] - q)
         381 +            a[0:10] = d * (self.look / np.max(np.abs(d)))
         382 +        return a
         383 +
         384 +    def _safe_move(self, state, q0, q1):
         385 +        """Check the joint-linear move q0->q1 keeps tool/fingers/held object
         386 +        above all nearby objects (used when cutting path corners)."""
         387 +        base = self._base(state)
         388 +        held = self._grasped_name(state)
         389 +        depth, rad = FINGER_DOWN, 0.075
         390 +        if held is not None:
         391 +            p, _, h = self._pose(state, held)
         392 +            tz = self._tool(state)[2, 3]
         393 +            depth = max(depth, tz - (p[2] - h[2]))
         394 +            rad = max(rad, np.hypot(h[0], h[1]) + 0.01)
         395 +        boxes = [self._box(state, n) for n in self.names if n != held]
         396 +        dq = _wrap(q1 - q0)
         397 +        for f in (0.25, 0.5, 0.75, 1.0):
         398 +            pt = wb_fk(q0 + f * dq)[:3, 3]
         399 +            low = pt[2] - depth
         400 +            if low < self.table_z + 0.01:
         401 +                return False
         402 +            for c, hh, bot, top in boxes:
         403 +                dxy = np.maximum(np.abs(pt[:2] - c) - hh, 0.0)
         404 +                if np.hypot(dxy[0], dxy[1]) < rad and low < top + 0.012:
         405 +                    return False
         406 +        return True
         407 +
         408 +    def _noop(self, grip=0.0):
         409 +        a = np.zeros(11, dtype=np.float32); a[10] = grip
         410 +        return a
         411 +
         412 +    def get_action(self, state):
         413 +        q = self._x(state)
         414 +        moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
         415 +        attempted = self.last_a is not None and np.any(np.abs(self.last_a[0:10]) > 1e-9)
         416 +        self.blocked = attempted and not moved
         417 +        if self.blocked:
         418 +            self.look = max(0.02, self.look * 0.35)
         419 +        elif attempted:
         420 +            self.look = min(STEP, self.look * 1.5)
         421 +        self.last_q = q.copy()
         422 +        try:
         423 +            a = self._policy(state)
         424 +        except Exception:
         425 +            a = self._noop()
         426 +        a = np.asarray(a, dtype=np.float32).copy()
         427 +        a[:10] = np.clip(a[:10], -STEP, STEP)
         428 +        a[10] = np.clip(a[10], -1, 1)
         429 +        self.last_a = a
         430 +        return a
         431 +
         432 +    def _policy(self, state):
         433 +        ph = self.phase
         434 +        if ph == 'done':
         435 +            if self._grasped_name(state) is None and self.tasks:
         436 +                self._start_task(state)
         437 +            return self._noop()
         438 +
         439 +        if ph == 'to_grasp':
         440 +            g = self._grasped_name(state)
         441 +            if g is not None:
         442 +                return self._on_grasped(state, g)
         443 +            if self.blocked:
         444 +                self.stuck += 1
         445 +                if self.stuck >= 2:
         446 +                    if self._tool(state)[2, 3] > self.grasp_z + 0.012:
         447 +                        # cannot get down to the grasp: try something else
         448 +                        self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         449 +                        self._start_task(state)
         450 +                        a = self._track(state)
         451 +                        return a if a is not None else self._noop()
         452 +                    self.qpath = []
         453 +            a = self._track(state)
         454 +            if a is not None:
         455 +                return a
         456 +            self.phase = 'close'
         457 +            return self._noop(-1.0)
         458 +
         459 +        if ph == 'close':
         460 +            g = self._grasped_name(state)
         461 +            if g is None:
         462 +                self.grasp_attempt += 1
         463 +                self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         464 +                self.total_fail += 1
         465 +                self._start_task(state)
         466 +                return self._track(state) if self.qpath else self._noop()
         467 +            return self._on_grasped(state, g)
         468 +
         469 +        if ph == 'to_place':
         470 +            if self._grasped_name(state) is None:
         471 +                return self._on_released(state)
         472 +            if self.blocked:
         473 +                self.stuck += 1
         474 +                if len(self.qpath) <= self.descent_len:
         475 +                    self.qpath = []
         476 +                elif self.stuck >= 3:
         477 +                    self._plan_place(state, replan=True)
         478 +            a = self._track(state)
         479 +            if a is not None:
         480 +                return a
         481 +            self.phase = 'open'
         482 +            return self._noop(1.0)
         483 +
         484 +        if ph == 'open':
         485 +            if self._grasped_name(state) is None:
         486 +                return self._on_released(state)
         487 +            self.release_tries += 1
         488 +            tool = self._tool(state)[:3, 3]
         489 +            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw, final_grip=1.0)
         490 +            self.descent_len = 2
         491 +            self.phase = 'to_place'
         492 +            if self.release_tries > 12:
         493 +                self.release_tries = 0
         494 +                self._plan_place(state, replan=True)
         495 +            a = self._track(state)
         496 +            return a if a is not None else self._noop(1.0)
         497 +
         498 +        if ph == 'retreat':
         499 +            if self.blocked:
         500 +                self.stuck += 1
         501 +                if self.stuck >= 2:
         502 +                    self.qpath = []
         503 +            a = self._track(state)
         504 +            if a is not None:
         505 +                return a
         506 +            self._next_task(state)
         507 +            a = self._track(state) if self.phase == 'to_grasp' else None
         508 +            return a if a is not None else self._noop()
         509 +
         510 +        return self._noop()
         511 +
         512 +    def _on_grasped(self, state, g):
         513 +        self.grasp_attempt = 0
         514 +        if g != self.cur_obj:
         515 +            self.tasks.insert(0, (g, 'clear'))
         516 +            self.cur_obj = g
         517 +        self._plan_place(state)
         518 +        a = self._track(state)
         519 +        return a if a is not None else self._noop()
         520 +
         521 +    def _on_released(self, state):
         522 +        self.release_tries = 0
         523 +        name, kind = self.tasks.pop(0) if self.tasks else (None, None)
         524 +        if kind == 'goal':
         525 +            self.phase = 'done'
         526 +            return self._noop()
         527 +        self._next_task(state)
         528 +        a = self._track(state) if self.phase == 'to_grasp' else None
         529 +        return a if a is not None else self._noop()
         530 +
         531 +    def _next_task(self, state):
         532 +        if self.tasks and self.tasks[0][1] == 'goal':
         533 +            for n in self._blocking_obstructions(state):
         534 +                if all(t[0] != n for t in self.tasks):
         535 +                    self.tasks.insert(0, (n, 'clear'))
         536 +        self._start_task(state)
         537 +
         538 +    def _plan_place(self, state, replan=False):
         539 +        name = self.cur_obj
         540 +        p, qo, h = self._pose(state, name)
         541 +        r = self.robot
         542 +        tf = _T([state.get(r, 'grasp_tf_x'), state.get(r, 'grasp_tf_y'), state.get(r, 'grasp_tf_z')],
         543 +                [state.get(r, 'grasp_tf_qx'), state.get(r, 'grasp_tf_qy'), state.get(r, 'grasp_tf_qz'),
         544 +                 state.get(r, 'grasp_tf_qw')])
         545 +        kind = self.tasks[0][1] if self.tasks and self.tasks[0][0] == name else 'clear'
         546 +        Ttool_now = self._tool(state)
         547 +        hold_off = Ttool_now[2, 3] - (p[2] - h[2])   # tool height above held-object bottom
         548 +        yaw = np.arctan2(Ttool_now[1, 0], Ttool_now[0, 0])
         549 +        if kind == 'goal':
         550 +            rp, rh = self.region
         551 +            xy = rp[:2]
         552 +            surf = rp[2] + rh[2]
         553 +        else:
         554 +            xy = self._free_spot(state, name, yaw, hold_off)
         555 +            if replan:
         556 +                xy = xy + np.random.uniform(-0.03, 0.03, 2)
         557 +            surf = self.table_z
         558 +        Tobj = _T([xy[0], xy[1], surf + h[2] + 0.001], qo)
         559 +        Ttool = Tobj @ np.linalg.inv(tf)
         560 +        tgt = Ttool[:3, 3]
         561 +        tyaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
         562 +        zt = self._transit_z(state, hold_off, exclude=(name,))
         563 +        tool = Ttool_now[:3, 3]
         564 +        wps = []
         565 +        if tool[2] < zt - 0.005:
         566 +            wps.append(np.array([tool[0], tool[1], zt]))
         567 +        wps += [np.array([tgt[0], tgt[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]),
         568 +                np.array([tgt[0], tgt[1], tgt[2] + 0.015])]
         569 +        self._set_path(state, wps, tyaw)
         570 +        n_before = len(self.qpath)
         571 +        self._append_descent(state, tgt, tyaw)
         572 +        self.descent_len = len(self.qpath) - n_before + 2
         573 +        self.final_grip = 1.0
         574 +        self.phase = 'to_place'
         575 +
         576 +    def _append_descent(self, state, tgt, yaw):
         577 +        base = self._base(state)
         578 +        qc = self.qpath[-1] if self.qpath else self._x(state)
         579 +        R = down_R(yaw)
         580 +        for dz in (0.008, 0.003, 0.0):
         581 +            qn, ok = self._ik(qc, tgt + np.array([0, 0, dz]), R)
         582 +            qn = qc + _wrap(qn - qc)
         583 +            self.qpath.append(qn)
         584 +            qc = qn
diff --git a/v_0.1_-0.09/env_client.py b/v_0.1_-0.09/env_client.py
new file mode 100644
index 0000000..108c884
--- /dev/null
+++ b/v_0.1_-0.09/env_client.py
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
diff --git a/v_0.1_-0.09/env_spaces.json b/v_0.1_-0.09/env_spaces.json
new file mode 100644
index 0000000..dff8dfd
--- /dev/null
+++ b/v_0.1_-0.09/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "6eefef35bfaa192f7898ebf189cf2b7d", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
diff --git a/v_0.1_-0.09/kin.py b/v_0.1_-0.09/kin.py
new file mode 100644
index 0000000..b360a71
--- /dev/null
+++ b/v_0.1_-0.09/kin.py
@@ -0,0 +1,172 @@
           1 +import numpy as np
           2 +
           3 +def _rpy(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def _T(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = _rpy(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +PI = np.pi
          13 +H = PI / 2
          14 +JOINTS = [
          15 +    _T((0, 0, 0.15643), (PI, 0, 0)),
          16 +    _T((0, 0.005375, -0.12838), (H, 0, 0)),
          17 +    _T((0, -0.21038, -0.006375), (-H, 0, 0)),
          18 +    _T((0, 0.006375, -0.21038), (H, 0, 0)),
          19 +    _T((0, -0.20843, -0.006375), (-H, 0, 0)),
          20 +    _T((0, 0.00017505, -0.10593), (H, 0, 0)),
          21 +    _T((0, -0.10593, -0.00017505), (-H, 0, 0)),
          22 +]
          23 +EE = _T((0, 0, -0.061525), (PI, 0, 0))
          24 +MOUNT = (0.12, 0.0, -0.0052)
          25 +TOOL = 0.12
          26 +HOME = np.array([0.0, -0.35, -np.pi, -2.5, 0.0, -0.87, np.pi / 2])
          27 +
          28 +def _rz(q):
          29 +    c, s = np.cos(q), np.sin(q)
          30 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          31 +
          32 +def mount_base(base):
          33 +    bx, by, br = base
          34 +    c, s = np.cos(br), np.sin(br)
          35 +    return (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
          36 +
          37 +def _chain(q, base):
          38 +    """Returns tool transform and list of (axis, origin) of joints in world."""
          39 +    bx, by, br = mount_base(base)
          40 +    T = _rz(br); T[0, 3] = bx; T[1, 3] = by; T[2, 3] = MOUNT[2]
          41 +    axes = []
          42 +    for Tj, qj in zip(JOINTS, q):
          43 +        T = T @ Tj
          44 +        axes.append((T[:3, 2].copy(), T[:3, 3].copy()))
          45 +        T = T @ _rz(qj)
          46 +    T = T @ EE
          47 +    Tt = np.eye(4); Tt[2, 3] = TOOL
          48 +    return T @ Tt, axes
          49 +
          50 +def tool_fk(q, base):
          51 +    return _chain(q, base)[0]
          52 +
          53 +def _rot_err(Rc, Rd):
          54 +    Re = Rd @ Rc.T
          55 +    v = 0.5 * np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
          56 +    return v
          57 +
          58 +def tool_ik(q0, p, R, base, iters=60, tol=1e-5, q_nom=None, k_null=0.3):
          59 +    q = np.array(q0, dtype=float)
          60 +    if q_nom is None:
          61 +        q_nom = HOME
          62 +    for it in range(iters):
          63 +        T, axes = _chain(q, base)
          64 +        e = np.concatenate([p - T[:3, 3], _rot_err(T[:3, :3], R)])
          65 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
          66 +            return q, True
          67 +        J = np.zeros((6, 7))
          68 +        pt = T[:3, 3]
          69 +        for j, (z, o) in enumerate(axes):
          70 +            J[:3, j] = np.cross(z, pt - o)
          71 +            J[3:, j] = z
          72 +        JJt = J @ J.T + 1e-6 * np.eye(6)
          73 +        Jp = J.T @ np.linalg.inv(JJt)
          74 +        dq = Jp @ e
          75 +        dn = (q_nom - q + np.pi) % (2 * np.pi) - np.pi
          76 +        dq += (np.eye(7) - Jp @ J) @ (k_null * dn)
          77 +        n = np.max(np.abs(dq))
          78 +        if n > 0.3:
          79 +            dq *= 0.3 / n
          80 +        q = q + dq
          81 +    T, _ = _chain(q, base)
          82 +    ok = np.linalg.norm(p - T[:3, 3]) < 1e-3
          83 +    return q, ok
          84 +
          85 +def down_R(yaw):
          86 +    c, s = np.cos(yaw), np.sin(yaw)
          87 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          88 +    return np.stack([x, y, z], axis=1)
          89 +
          90 +
          91 +def wb_fk(x):
          92 +    """x = [bx, by, br, q1..q7] -> tool transform."""
          93 +    return _chain(x[3:], x[:3])[0]
          94 +
          95 +
          96 +def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1.0):
          97 +    """Whole-body IK over base y, base rot and the 7 arm joints (base x fixed)."""
          98 +    x = np.array(x0, dtype=float)
          99 +    if q_nom is None:
         100 +        q_nom = HOME
         101 +    W = np.array([w_by, w_br] + [1.0] * 7)
         102 +    for it in range(iters):
         103 +        T, axes = _chain(x[3:], x[:3])
         104 +        pt = T[:3, 3]
         105 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         106 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         107 +            return x, True
         108 +        J = np.zeros((6, 9))
         109 +        J[1, 0] = 1.0
         110 +        ez = np.array([0.0, 0.0, 1.0])
         111 +        J[:3, 1] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         112 +        J[3:, 1] = ez
         113 +        for j, (z, o) in enumerate(axes):
         114 +            J[:3, 2 + j] = np.cross(z, pt - o)
         115 +            J[3:, 2 + j] = z
         116 +        JW = J * W
         117 +        Jp = JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6))
         118 +        Jp = W[:, None] * Jp
         119 +        dv = Jp @ e
         120 +        dn = np.zeros(9)
         121 +        dn[2:] = k_null * ((q_nom - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         122 +        dv += dn - Jp @ (J @ dn)
         123 +        n = np.max(np.abs(dv))
         124 +        if n > 0.3:
         125 +            dv *= 0.3 / n
         126 +        x[1:] += dv
         127 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         128 +    return x, ok
         129 +
         130 +
         131 +Q_NOM = np.array([0.0, 0.3, -np.pi, -2.15, 0.0, -0.69, 0.0])
         132 +K_NOM = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
         133 +
         134 +
         135 +def wb_ik2(x0, p, R, iters=40, tol=1e-5, k_null=0.3, bx_max=-0.12, w_base=1.0):
         136 +    """Whole-body IK over base x (<= bx_max), y, rot and the 7 arm joints.
         137 +    Null space pulls the arm to an extended nominal posture Q_NOM."""
         138 +    x = np.array(x0, dtype=float)
         139 +    ez = np.array([0.0, 0.0, 1.0])
         140 +    for it in range(iters):
         141 +        T, axes = _chain(x[3:], x[:3])
         142 +        pt = T[:3, 3]
         143 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         144 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         145 +            return x, True
         146 +        J = np.zeros((6, 10))
         147 +        J[0, 0] = 1.0
         148 +        J[1, 1] = 1.0
         149 +        J[:3, 2] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         150 +        J[3:, 2] = ez
         151 +        for j, (z, o) in enumerate(axes):
         152 +            J[:3, 3 + j] = np.cross(z, pt - o)
         153 +            J[3:, 3 + j] = z
         154 +        dn = np.zeros(10)
         155 +        dn[3:] = k_null * K_NOM * ((Q_NOM - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         156 +        W = np.array([w_base, w_base, w_base] + [1.0] * 7)
         157 +        for _ in range(2):
         158 +            JW = J * W
         159 +            Jp = W[:, None] * (JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6)))
         160 +            dv = Jp @ e + dn - Jp @ (J @ dn)
         161 +            n = np.max(np.abs(dv))
         162 +            if n > 0.3:
         163 +                dv *= 0.3 / n
         164 +            if x[0] + dv[0] > bx_max + 1e-9 and W[0] > 0:
         165 +                W[0] = 0.0
         166 +                x[0] = min(x[0], bx_max)
         167 +                continue
         168 +            break
         169 +        x += dv
         170 +        x[0] = min(x[0], bx_max) if x0[0] <= bx_max + 1e-9 else x[0]
         171 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         172 +    return x, ok
diff --git a/v_0.1_-0.09/test_approach.py b/v_0.1_-0.09/test_approach.py
new file mode 100644
index 0000000..afc13cc
--- /dev/null
+++ b/v_0.1_-0.09/test_approach.py
@@ -0,0 +1,36 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +def run(seed, verbose=False, max_steps=None, count=None):
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed, options={'object_count': count} if count else None)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0 = time.time()
          11 +    ap.reset(obs, info)
          12 +    ms = max_steps or env.max_steps
          13 +    steps = 0
          14 +    term = False
          15 +    pt = 0.0
          16 +    for steps in range(1, ms + 1):
          17 +        t1 = time.time()
          18 +        a = ap.get_action(obs)
          19 +        pt += time.time() - t1
          20 +        obs, r, term, trunc, info = env.step(a)
          21 +        if term or trunc:
          22 +            break
          23 +    dt = time.time() - t0
          24 +    nobs = len([n for n in obs.get_object_names() if n.startswith('obstruction')])
          25 +    env.close()
          26 +    return term, steps, dt, nobs, ap.phase, pt
          27 +
          28 +if __name__ == '__main__':
          29 +    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          30 +    count = int(sys.argv[3]) if len(sys.argv) > 3 else None
          31 +    ok = 0
          32 +    for s in seeds:
          33 +        term, steps, dt, n, ph, pt = run(s, count=count)
          34 +        ok += term
          35 +        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s ptime={pt:.1f}s nobs={n} phase={ph}', flush=True)
          36 +    print(f'{ok}/{len(seeds)}')
diff --git a/v_0.1_-0.12/approach.py b/v_0.1_-0.12/approach.py
new file mode 100644
index 0000000..c415aa7
--- /dev/null
+++ b/v_0.1_-0.12/approach.py
@@ -0,0 +1,584 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place
           2 +the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py).
           3 +
           4 +Empirical facts (black-box probing):
           5 +- Arm mount is +0.12m along base x; the grasp/tool frame is 0.12m past the flange.
           6 +- Gripper fingers lie along the tool x axis, extending ~0.07m from the centre and
           7 +  ~0.035m below the tool frame.  Robot/held object collisions reject a step.
           8 +- Grasp (close) succeeds when tool z in [bottom+0.044, top+0.033] over the object.
           9 +- Release (open) succeeds only if the held object rests within a few mm of a surface.
          10 +"""
          11 +import numpy as np
          12 +from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik, wb_ik2
          13 +
          14 +JN = [f'joint_{i}' for i in range(1, 8)]
          15 +MERGE_GRIP = True
          16 +WB = True
          17 +CUT_CORNERS = True
          18 +STEP = 0.2             # max joint delta per step
          19 +FINGER_DOWN = 0.036    # fingertips below tool frame
          20 +F_OFF, F_HL, F_HW = 0.046, 0.024, 0.013   # finger centre offset, half length, half width
          21 +
          22 +
          23 +def _q2R(x, y, z, w):
          24 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          25 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          26 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          27 +
          28 +
          29 +def _T(p, q):
          30 +    M = np.eye(4); M[:3, :3] = _q2R(*q); M[:3, 3] = p
          31 +    return M
          32 +
          33 +
          34 +def _yaw_of_quat(q):
          35 +    x, y, z, w = q
          36 +    return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
          37 +
          38 +
          39 +def _wrap(a):
          40 +    return (a + np.pi) % (2 * np.pi) - np.pi
          41 +
          42 +
          43 +def _aabb_of_rect(c, hx, hy, yaw):
          44 +    c_, s_ = abs(np.cos(yaw)), abs(np.sin(yaw))
          45 +    return np.array(c), np.array([c_ * hx + s_ * hy, s_ * hx + c_ * hy])
          46 +
          47 +
          48 +def _gap(c1, h1, c2, h2):
          49 +    """Signed separation between two AABBs (positive = apart)."""
          50 +    return np.max(np.abs(np.asarray(c1) - np.asarray(c2)) - np.asarray(h1) - np.asarray(h2))
          51 +
          52 +
          53 +def _finger_boxes(xy, yaw):
          54 +    d = np.array([np.cos(yaw), np.sin(yaw)])
          55 +    out = []
          56 +    for sgn in (1, -1):
          57 +        out.append(_aabb_of_rect(np.asarray(xy) + sgn * F_OFF * d, F_HL, F_HW, yaw))
          58 +    return out
          59 +
          60 +
          61 +class GeneratedApproach:
          62 +    def __init__(self, action_space, observation_space, primitives):
          63 +        self.action_space = action_space
          64 +        self.observation_space = observation_space
          65 +
          66 +    # ------------------------------------------------------------ helpers
          67 +    def _obj(self, state, name):
          68 +        return state.get_object_from_name(name)
          69 +
          70 +    def _pose(self, state, name):
          71 +        o = self._obj(state, name)
          72 +        return (np.array([state.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')]),
          73 +                np.array([state.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]),
          74 +                np.array([state.get(o, f) for f in ('half_extent_x', 'half_extent_y', 'half_extent_z')]))
          75 +
          76 +    def _box(self, state, name):
          77 +        """(centre_xy, half_xy AABB, bottom z, top z)"""
          78 +        p, q, h = self._pose(state, name)
          79 +        c, hh = _aabb_of_rect(p[:2], h[0], h[1], _yaw_of_quat(q))
          80 +        return c, hh, p[2] - h[2], p[2] + h[2]
          81 +
          82 +    def _q(self, state):
          83 +        return np.array([state.get(self.robot, f) for f in JN])
          84 +
          85 +    def _x(self, state):
          86 +        return np.concatenate([np.array(self._base(state)), self._q(state)])
          87 +
          88 +    def _ik(self, xc, pt, R):
          89 +        if WB:
          90 +            return wb_ik2(xc, pt, R, iters=40, k_null=0.1, bx_max=-0.12)
          91 +        q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
          92 +        return np.concatenate([xc[:3], q]), ok
          93 +
          94 +    def _base(self, state):
          95 +        return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
          96 +                state.get(self.robot, 'pos_base_rot'))
          97 +
          98 +    def _tool(self, state):
          99 +        return tool_fk(self._q(state), self._base(state))
         100 +
         101 +    def _grasped_name(self, state):
         102 +        for n in self.names:
         103 +            if state.get(self._obj(state, n), 'grasp_active') > 0.5:
         104 +                return n
         105 +        return None
         106 +
         107 +    def _max_top(self, state, exclude=()):
         108 +        t = self.table_z
         109 +        for n in self.names:
         110 +            if n in exclude:
         111 +                continue
         112 +            t = max(t, self._box(state, n)[3])
         113 +        return t
         114 +
         115 +    # ------------------------------------------------------------ planning
         116 +    def reset(self, state, info):
         117 +        self.robot = state.get_object_from_name('robot')
         118 +        self.names = sorted(n for n in state.get_object_names() if n != 'robot')
         119 +        self.obstructions = sorted(n for n in self.names if n.startswith('obstruction'))
         120 +        rp, _, rh = self._pose(state, 'target_region')
         121 +        self.table_z = rp[2] - rh[2]
         122 +        self.region = (rp, rh)
         123 +        self.tasks = [(n, 'clear') for n in self._blocking_obstructions(state)]
         124 +        self.tasks.append(('target_block', 'goal'))
         125 +        self.phase = None
         126 +        self.qpath = []
         127 +        self.last_q = None
         128 +        self.last_a = None
         129 +        self.blocked = False
         130 +        self.look = STEP
         131 +        self.fails = {}
         132 +        self.blk_moves = {}
         133 +        self.stuck = 0
         134 +        self.descent_len = 0
         135 +        self.release_tries = 0
         136 +        self.grasp_attempt = 0
         137 +        self.total_fail = 0
         138 +        self.final_grip = 0.0
         139 +        self.wp_yaw = 0.0
         140 +        self._start_task(state)
         141 +
         142 +    def _blocking_obstructions(self, state, margin=0.003):
         143 +        rp, rh = self.region
         144 +        out = []
         145 +        for n in self.obstructions:
         146 +            c, hh, _, _ = self._box(state, n)
         147 +            if _gap(c, hh, rp[:2], rh[:2]) < margin:
         148 +                out.append(n)
         149 +        return out
         150 +
         151 +    def _finger_clearance(self, state, xy, yaw, tip_z, exclude):
         152 +        """Min xy gap between finger boxes and objects whose top is above tip_z."""
         153 +        clear = 1.0
         154 +        fbs = _finger_boxes(xy, yaw)
         155 +        for n in self.names:
         156 +            if n in exclude:
         157 +                continue
         158 +            c, hh, bot, top = self._box(state, n)
         159 +            if top < tip_z - 0.002:
         160 +                continue
         161 +            for fc, fh in fbs:
         162 +                g = _gap(fc, fh, c, hh)
         163 +                if g < clear:
         164 +                    clear = g
         165 +                    if g < 0.005:
         166 +                        self._blocker = n
         167 +        return clear
         168 +
         169 +    def _choose_yaw(self, state, name, kind, attempt):
         170 +        sc = self._yaw_scores(state, name, kind)
         171 +        c = sc[attempt % len(sc)]
         172 +        self.grasp_z = c[3]
         173 +        return c[1]
         174 +
         175 +    def _yaw_scores(self, state, name, kind):
         176 +        """Sorted [(clearance score, yaw, blocker, grasp z)] for grasp candidates."""
         177 +        p, q, h = self._pose(state, name)
         178 +        oy = _yaw_of_quat(q)
         179 +        lo = p[2] - h[2] + 0.045
         180 +        hi = p[2] + h[2] + 0.032
         181 +        gzs = [self._grasp_z(p, h)]
         182 +        if hi - 0.004 > gzs[0] + 0.004:
         183 +            gzs.append(hi - 0.004)
         184 +        cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
         185 +        T = self._tool(state)
         186 +        ty = np.arctan2(T[1, 0], T[0, 0])
         187 +        scored = []
         188 +        for j, gz in enumerate(gzs):
         189 +            for i, y in enumerate(cands):
         190 +                y = _wrap(2 * y) / 2  # modulo pi
         191 +                self._blocker = None
         192 +                c = self._finger_clearance(state, p[:2], y, gz - FINGER_DOWN, exclude=(name,))
         193 +                blk = self._blocker
         194 +                if kind == 'goal':
         195 +                    rp, rh = self.region
         196 +                    surf = rp[2] + rh[2]
         197 +                    tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
         198 +                    c = min(c, self._finger_clearance(state, rp[:2], y, tip,
         199 +                                                      exclude=(name, 'target_region')))
         200 +                rot = abs(_wrap(2 * (y - ty)) / 2)   # rotation needed (mod pi), <= pi/2
         201 +                scored.append((min(c, 0.02) - 0.0005 * i - 0.004 * j - 0.004 * rot, y, blk, gz))
         202 +        scored.sort(key=lambda t: -t[0])
         203 +        return scored
         204 +
         205 +    def _select_task(self, state):
         206 +        """Reorder tasks so the front one is graspable; add blockers if needed."""
         207 +        for _ in range(len(self.names)):
         208 +            name, kind = self.tasks[0]
         209 +            f = self.fails.get(name, 0)
         210 +            sc = self._yaw_scores(state, name, kind)
         211 +            if sc[0][0] > 0.002 and f < 4:
         212 +                return
         213 +            # try another pending clear task that is more graspable
         214 +            best = None
         215 +            for t in self.tasks:
         216 +                if t[1] != 'clear' or t[0] == name:
         217 +                    continue
         218 +                s2 = self._yaw_scores(state, t[0], 'clear')[0][0] - 0.01 * self.fails.get(t[0], 0)
         219 +                if best is None or s2 > best[0]:
         220 +                    best = (s2, t)
         221 +            if best is not None and best[0] > sc[0][0] - 0.01 * f + 0.001:
         222 +                self.tasks.remove(best[1])
         223 +                self.tasks.insert(0, best[1])
         224 +                continue
         225 +            # add the obstruction blocking the fingers as a new task
         226 +            blk = sc[0][2]
         227 +            if (blk is not None and blk.startswith('obstruction')
         228 +                    and all(t[0] != blk for t in self.tasks)
         229 +                    and self.blk_moves.get(blk, 0) < 2
         230 +                    and self._yaw_scores(state, blk, 'clear')[0][0] > 0.002):
         231 +                self.blk_moves[blk] = self.blk_moves.get(blk, 0) + 1
         232 +                self.tasks.insert(0, (blk, 'clear'))
         233 +                continue
         234 +            return
         235 +
         236 +    def _grasp_z(self, p, h):
         237 +        lo = p[2] - h[2] + 0.045
         238 +        hi = p[2] + h[2] + 0.032
         239 +        return 0.5 * (lo + hi) if hi > lo else hi - 0.001
         240 +
         241 +    def _free_spot(self, state, name, yaw, hold_off):
         242 +        """Pick a table spot clear of region/other objects (object + fingers)."""
         243 +        p0, _, _ = self._pose(state, name)
         244 +        c0, h, _, _ = self._box(state, name)
         245 +        others = []
         246 +        for n in self.names:
         247 +            if n == name:
         248 +                continue
         249 +            others.append(self._box(state, n))
         250 +        rp, rh = self.region
         251 +        tip = self.table_z + 0.001 + hold_off - FINGER_DOWN
         252 +        best, best_score = None, 1e9
         253 +        fb, fb_score = None, -1e9
         254 +        for x in np.linspace(0.2, 0.5, 16):
         255 +            for y in np.linspace(-0.34, 0.34, 35):
         256 +                c = np.array([x, y])
         257 +                clear = _gap(c, h, rp[:2], rh[:2]) - 0.03
         258 +                fbs = _finger_boxes(c, yaw)
         259 +                for oc, oh, bot, top in others:
         260 +                    clear = min(clear, _gap(c, h, oc, oh) - 0.02)
         261 +                    if top > tip - 0.002:
         262 +                        for fc, fh in fbs:
         263 +                            clear = min(clear, _gap(fc, fh, oc, oh) - 0.008)
         264 +                if clear > fb_score:
         265 +                    fb, fb_score = c, clear
         266 +                if clear >= 0:
         267 +                    score = np.linalg.norm(c - p0[:2])
         268 +                    if score < best_score:
         269 +                        best, best_score = c, score
         270 +        return best if best is not None else fb
         271 +
         272 +    def _transit_z(self, state, hold_off=0.0, exclude=()):
         273 +        top = self._max_top(state, exclude)
         274 +        return max(top + 0.03 + max(FINGER_DOWN, hold_off), 0.2)
         275 +
         276 +    def _start_task(self, state):
         277 +        if not self.tasks:
         278 +            self.phase = 'done'
         279 +            return
         280 +        try:
         281 +            self._select_task(state)
         282 +        except Exception:
         283 +            pass
         284 +        name, kind = self.tasks[0]
         285 +        p, q, h = self._pose(state, name)
         286 +        self.cur_obj = name
         287 +        self.grasp_yaw = self._choose_yaw(state, name, kind, self.fails.get(name, 0))
         288 +        gz = self.grasp_z
         289 +        zt = self._transit_z(state)
         290 +        tool = self._tool(state)[:3, 3]
         291 +        wps = []
         292 +        rs = 0
         293 +        if tool[2] < zt - 0.01:
         294 +            wps.append(np.array([tool[0], tool[1], zt]))
         295 +            rs = 1
         296 +        wps.append(np.array([p[0], p[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]))
         297 +        wps.append(np.array([p[0], p[1], gz]))
         298 +        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0, flip=True, rot_start=rs)
         299 +        self.phase = 'to_grasp'
         300 +
         301 +    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False, rot_start=0):
         302 +        """Cartesian waypoints -> dense joint path (IK warm-started).
         303 +        Yaw is interpolated from the current tool yaw over all but the last segment."""
         304 +        q = self._x(state)
         305 +        base = self._base(state)
         306 +        T0 = wb_fk(q)
         307 +        cur = T0[:3, 3]
         308 +        y0 = np.arctan2(T0[1, 0], T0[0, 0])
         309 +        dy = _wrap(yaw - y0)
         310 +        if flip and abs(dy) > np.pi / 2:
         311 +            dy = dy - np.sign(dy) * np.pi
         312 +        yaw = y0 + dy
         313 +        pts = [cur]
         314 +        for w in wps:
         315 +            pts.append(np.asarray(w, dtype=float))
         316 +        seg = [np.linalg.norm(pts[i + 1] - pts[i]) for i in range(len(wps))]
         317 +        if len(seg) - 1 <= rot_start:
         318 +            rot_start = 0
         319 +        rot0 = sum(seg[:rot_start])
         320 +        rot_len = sum(seg[rot_start:-1]) if len(seg) > 1 and sum(seg[rot_start:-1]) > 0.02 else sum(seg[rot_start:])
         321 +        rot_len = max(rot_len, 1e-6)
         322 +        path = []
         323 +        self.corners = set()
         324 +        qc = q.copy()
         325 +        travelled = 0.0
         326 +        for i, w in enumerate(wps):
         327 +            w = pts[i + 1]
         328 +            d = seg[i]
         329 +            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.04)))
         330 +            for k in range(1, n + 1):
         331 +                pt = cur + (w - cur) * k / n
         332 +                f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
         333 +                qn, ok = self._ik(qc, pt, down_R(y0 + f * dy))
         334 +                qn = qc + _wrap(qn - qc)
         335 +                path.append(qn)
         336 +                qc = qn
         337 +            travelled += d
         338 +            self.corners.add(len(path) - 1)
         339 +            cur = w
         340 +        self.qpath = path
         341 +        self.popped = 0
         342 +        self.wp_yaw = yaw
         343 +        self.final_grip = final_grip
         344 +        self.travel_grip = 1.0 if final_grip < 0 else 0.0
         345 +        self.stuck = 0
         346 +
         347 +    # ------------------------------------------------------------ control
         348 +    def _track(self, state):
         349 +        """Step along the precomputed joint path; None if done."""
         350 +        q = self._x(state)
         351 +        while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
         352 +            self.qpath.pop(0)
         353 +            self.popped += 1
         354 +        if not self.qpath:
         355 +            return None
         356 +        k = -1
         357 +        crossed = False
         358 +        for i, qp in enumerate(self.qpath):
         359 +            if np.max(np.abs(_wrap(qp - q))) <= self.look:
         360 +                if crossed and not self._safe_move(state, q, qp):
         361 +                    break
         362 +                k = i
         363 +                if (i + self.popped) in self.corners:
         364 +                    if not CUT_CORNERS or self.blocked or self.look < STEP:
         365 +                        break
         366 +                    crossed = True
         367 +            else:
         368 +                break
         369 +        a = np.zeros(11, dtype=np.float32)
         370 +        if k >= 0:
         371 +            self.qpath = self.qpath[k:]
         372 +            self.popped += k
         373 +            k = 0
         374 +            d = _wrap(self.qpath[0] - q)
         375 +            a[0:10] = d
         376 +            a[10] = self.travel_grip
         377 +            if MERGE_GRIP and len(self.qpath) == 1 and self.final_grip != 0.0:
         378 +                a[10] = self.final_grip
         379 +        else:
         380 +            d = _wrap(self.qpath[0] - q)
         381 +            a[0:10] = d * (self.look / np.max(np.abs(d)))
         382 +        return a
         383 +
         384 +    def _safe_move(self, state, q0, q1):
         385 +        """Check the joint-linear move q0->q1 keeps tool/fingers/held object
         386 +        above all nearby objects (used when cutting path corners)."""
         387 +        base = self._base(state)
         388 +        held = self._grasped_name(state)
         389 +        depth, rad = FINGER_DOWN, 0.075
         390 +        if held is not None:
         391 +            p, _, h = self._pose(state, held)
         392 +            tz = self._tool(state)[2, 3]
         393 +            depth = max(depth, tz - (p[2] - h[2]))
         394 +            rad = max(rad, np.hypot(h[0], h[1]) + 0.01)
         395 +        boxes = [self._box(state, n) for n in self.names if n != held]
         396 +        dq = _wrap(q1 - q0)
         397 +        for f in (0.25, 0.5, 0.75, 1.0):
         398 +            pt = wb_fk(q0 + f * dq)[:3, 3]
         399 +            low = pt[2] - depth
         400 +            if low < self.table_z + 0.01:
         401 +                return False
         402 +            for c, hh, bot, top in boxes:
         403 +                dxy = np.maximum(np.abs(pt[:2] - c) - hh, 0.0)
         404 +                if np.hypot(dxy[0], dxy[1]) < rad and low < top + 0.012:
         405 +                    return False
         406 +        return True
         407 +
         408 +    def _noop(self, grip=0.0):
         409 +        a = np.zeros(11, dtype=np.float32); a[10] = grip
         410 +        return a
         411 +
         412 +    def get_action(self, state):
         413 +        q = self._x(state)
         414 +        moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
         415 +        attempted = self.last_a is not None and np.any(np.abs(self.last_a[0:10]) > 1e-9)
         416 +        self.blocked = attempted and not moved
         417 +        if self.blocked:
         418 +            self.look = max(0.02, self.look * 0.35)
         419 +        elif attempted:
         420 +            self.look = min(STEP, self.look * 1.5)
         421 +        self.last_q = q.copy()
         422 +        try:
         423 +            a = self._policy(state)
         424 +        except Exception:
         425 +            a = self._noop()
         426 +        a = np.asarray(a, dtype=np.float32).copy()
         427 +        a[:10] = np.clip(a[:10], -STEP, STEP)
         428 +        a[10] = np.clip(a[10], -1, 1)
         429 +        self.last_a = a
         430 +        return a
         431 +
         432 +    def _policy(self, state):
         433 +        ph = self.phase
         434 +        if ph == 'done':
         435 +            if self._grasped_name(state) is None and self.tasks:
         436 +                self._start_task(state)
         437 +            return self._noop()
         438 +
         439 +        if ph == 'to_grasp':
         440 +            g = self._grasped_name(state)
         441 +            if g is not None:
         442 +                return self._on_grasped(state, g)
         443 +            if self.blocked:
         444 +                self.stuck += 1
         445 +                if self.stuck >= 2:
         446 +                    if self._tool(state)[2, 3] > self.grasp_z + 0.012:
         447 +                        # cannot get down to the grasp: try something else
         448 +                        self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         449 +                        self._start_task(state)
         450 +                        a = self._track(state)
         451 +                        return a if a is not None else self._noop()
         452 +                    self.qpath = []
         453 +            a = self._track(state)
         454 +            if a is not None:
         455 +                return a
         456 +            self.phase = 'close'
         457 +            return self._noop(-1.0)
         458 +
         459 +        if ph == 'close':
         460 +            g = self._grasped_name(state)
         461 +            if g is None:
         462 +                self.grasp_attempt += 1
         463 +                self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         464 +                self.total_fail += 1
         465 +                self._start_task(state)
         466 +                return self._track(state) if self.qpath else self._noop()
         467 +            return self._on_grasped(state, g)
         468 +
         469 +        if ph == 'to_place':
         470 +            if self._grasped_name(state) is None:
         471 +                return self._on_released(state)
         472 +            if self.blocked:
         473 +                self.stuck += 1
         474 +                if len(self.qpath) <= self.descent_len:
         475 +                    self.qpath = []
         476 +                elif self.stuck >= 3:
         477 +                    self._plan_place(state, replan=True)
         478 +            a = self._track(state)
         479 +            if a is not None:
         480 +                return a
         481 +            self.phase = 'open'
         482 +            return self._noop(1.0)
         483 +
         484 +        if ph == 'open':
         485 +            if self._grasped_name(state) is None:
         486 +                return self._on_released(state)
         487 +            self.release_tries += 1
         488 +            tool = self._tool(state)[:3, 3]
         489 +            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw, final_grip=1.0)
         490 +            self.descent_len = 2
         491 +            self.phase = 'to_place'
         492 +            if self.release_tries > 12:
         493 +                self.release_tries = 0
         494 +                self._plan_place(state, replan=True)
         495 +            a = self._track(state)
         496 +            return a if a is not None else self._noop(1.0)
         497 +
         498 +        if ph == 'retreat':
         499 +            if self.blocked:
         500 +                self.stuck += 1
         501 +                if self.stuck >= 2:
         502 +                    self.qpath = []
         503 +            a = self._track(state)
         504 +            if a is not None:
         505 +                return a
         506 +            self._next_task(state)
         507 +            a = self._track(state) if self.phase == 'to_grasp' else None
         508 +            return a if a is not None else self._noop()
         509 +
         510 +        return self._noop()
         511 +
         512 +    def _on_grasped(self, state, g):
         513 +        self.grasp_attempt = 0
         514 +        if g != self.cur_obj:
         515 +            self.tasks.insert(0, (g, 'clear'))
         516 +            self.cur_obj = g
         517 +        self._plan_place(state)
         518 +        a = self._track(state)
         519 +        return a if a is not None else self._noop()
         520 +
         521 +    def _on_released(self, state):
         522 +        self.release_tries = 0
         523 +        name, kind = self.tasks.pop(0) if self.tasks else (None, None)
         524 +        if kind == 'goal':
         525 +            self.phase = 'done'
         526 +            return self._noop()
         527 +        self._next_task(state)
         528 +        a = self._track(state) if self.phase == 'to_grasp' else None
         529 +        return a if a is not None else self._noop()
         530 +
         531 +    def _next_task(self, state):
         532 +        if self.tasks and self.tasks[0][1] == 'goal':
         533 +            for n in self._blocking_obstructions(state):
         534 +                if all(t[0] != n for t in self.tasks):
         535 +                    self.tasks.insert(0, (n, 'clear'))
         536 +        self._start_task(state)
         537 +
         538 +    def _plan_place(self, state, replan=False):
         539 +        name = self.cur_obj
         540 +        p, qo, h = self._pose(state, name)
         541 +        r = self.robot
         542 +        tf = _T([state.get(r, 'grasp_tf_x'), state.get(r, 'grasp_tf_y'), state.get(r, 'grasp_tf_z')],
         543 +                [state.get(r, 'grasp_tf_qx'), state.get(r, 'grasp_tf_qy'), state.get(r, 'grasp_tf_qz'),
         544 +                 state.get(r, 'grasp_tf_qw')])
         545 +        kind = self.tasks[0][1] if self.tasks and self.tasks[0][0] == name else 'clear'
         546 +        Ttool_now = self._tool(state)
         547 +        hold_off = Ttool_now[2, 3] - (p[2] - h[2])   # tool height above held-object bottom
         548 +        yaw = np.arctan2(Ttool_now[1, 0], Ttool_now[0, 0])
         549 +        if kind == 'goal':
         550 +            rp, rh = self.region
         551 +            xy = rp[:2]
         552 +            surf = rp[2] + rh[2]
         553 +        else:
         554 +            xy = self._free_spot(state, name, yaw, hold_off)
         555 +            if replan:
         556 +                xy = xy + np.random.uniform(-0.03, 0.03, 2)
         557 +            surf = self.table_z
         558 +        Tobj = _T([xy[0], xy[1], surf + h[2] + 0.001], qo)
         559 +        Ttool = Tobj @ np.linalg.inv(tf)
         560 +        tgt = Ttool[:3, 3]
         561 +        tyaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
         562 +        zt = self._transit_z(state, hold_off, exclude=(name,))
         563 +        tool = Ttool_now[:3, 3]
         564 +        wps = []
         565 +        if tool[2] < zt - 0.005:
         566 +            wps.append(np.array([tool[0], tool[1], zt]))
         567 +        wps += [np.array([tgt[0], tgt[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]),
         568 +                np.array([tgt[0], tgt[1], tgt[2] + 0.015])]
         569 +        self._set_path(state, wps, tyaw)
         570 +        n_before = len(self.qpath)
         571 +        self._append_descent(state, tgt, tyaw)
         572 +        self.descent_len = len(self.qpath) - n_before + 2
         573 +        self.final_grip = 1.0
         574 +        self.phase = 'to_place'
         575 +
         576 +    def _append_descent(self, state, tgt, yaw):
         577 +        base = self._base(state)
         578 +        qc = self.qpath[-1] if self.qpath else self._x(state)
         579 +        R = down_R(yaw)
         580 +        for dz in (0.008, 0.003, 0.0):
         581 +            qn, ok = self._ik(qc, tgt + np.array([0, 0, dz]), R)
         582 +            qn = qc + _wrap(qn - qc)
         583 +            self.qpath.append(qn)
         584 +            qc = qn
diff --git a/v_0.1_-0.12/env_client.py b/v_0.1_-0.12/env_client.py
new file mode 100644
index 0000000..108c884
--- /dev/null
+++ b/v_0.1_-0.12/env_client.py
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
diff --git a/v_0.1_-0.12/env_spaces.json b/v_0.1_-0.12/env_spaces.json
new file mode 100644
index 0000000..dff8dfd
--- /dev/null
+++ b/v_0.1_-0.12/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "6eefef35bfaa192f7898ebf189cf2b7d", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
diff --git a/v_0.1_-0.12/kin.py b/v_0.1_-0.12/kin.py
new file mode 100644
index 0000000..b360a71
--- /dev/null
+++ b/v_0.1_-0.12/kin.py
@@ -0,0 +1,172 @@
           1 +import numpy as np
           2 +
           3 +def _rpy(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def _T(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = _rpy(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +PI = np.pi
          13 +H = PI / 2
          14 +JOINTS = [
          15 +    _T((0, 0, 0.15643), (PI, 0, 0)),
          16 +    _T((0, 0.005375, -0.12838), (H, 0, 0)),
          17 +    _T((0, -0.21038, -0.006375), (-H, 0, 0)),
          18 +    _T((0, 0.006375, -0.21038), (H, 0, 0)),
          19 +    _T((0, -0.20843, -0.006375), (-H, 0, 0)),
          20 +    _T((0, 0.00017505, -0.10593), (H, 0, 0)),
          21 +    _T((0, -0.10593, -0.00017505), (-H, 0, 0)),
          22 +]
          23 +EE = _T((0, 0, -0.061525), (PI, 0, 0))
          24 +MOUNT = (0.12, 0.0, -0.0052)
          25 +TOOL = 0.12
          26 +HOME = np.array([0.0, -0.35, -np.pi, -2.5, 0.0, -0.87, np.pi / 2])
          27 +
          28 +def _rz(q):
          29 +    c, s = np.cos(q), np.sin(q)
          30 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          31 +
          32 +def mount_base(base):
          33 +    bx, by, br = base
          34 +    c, s = np.cos(br), np.sin(br)
          35 +    return (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
          36 +
          37 +def _chain(q, base):
          38 +    """Returns tool transform and list of (axis, origin) of joints in world."""
          39 +    bx, by, br = mount_base(base)
          40 +    T = _rz(br); T[0, 3] = bx; T[1, 3] = by; T[2, 3] = MOUNT[2]
          41 +    axes = []
          42 +    for Tj, qj in zip(JOINTS, q):
          43 +        T = T @ Tj
          44 +        axes.append((T[:3, 2].copy(), T[:3, 3].copy()))
          45 +        T = T @ _rz(qj)
          46 +    T = T @ EE
          47 +    Tt = np.eye(4); Tt[2, 3] = TOOL
          48 +    return T @ Tt, axes
          49 +
          50 +def tool_fk(q, base):
          51 +    return _chain(q, base)[0]
          52 +
          53 +def _rot_err(Rc, Rd):
          54 +    Re = Rd @ Rc.T
          55 +    v = 0.5 * np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
          56 +    return v
          57 +
          58 +def tool_ik(q0, p, R, base, iters=60, tol=1e-5, q_nom=None, k_null=0.3):
          59 +    q = np.array(q0, dtype=float)
          60 +    if q_nom is None:
          61 +        q_nom = HOME
          62 +    for it in range(iters):
          63 +        T, axes = _chain(q, base)
          64 +        e = np.concatenate([p - T[:3, 3], _rot_err(T[:3, :3], R)])
          65 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
          66 +            return q, True
          67 +        J = np.zeros((6, 7))
          68 +        pt = T[:3, 3]
          69 +        for j, (z, o) in enumerate(axes):
          70 +            J[:3, j] = np.cross(z, pt - o)
          71 +            J[3:, j] = z
          72 +        JJt = J @ J.T + 1e-6 * np.eye(6)
          73 +        Jp = J.T @ np.linalg.inv(JJt)
          74 +        dq = Jp @ e
          75 +        dn = (q_nom - q + np.pi) % (2 * np.pi) - np.pi
          76 +        dq += (np.eye(7) - Jp @ J) @ (k_null * dn)
          77 +        n = np.max(np.abs(dq))
          78 +        if n > 0.3:
          79 +            dq *= 0.3 / n
          80 +        q = q + dq
          81 +    T, _ = _chain(q, base)
          82 +    ok = np.linalg.norm(p - T[:3, 3]) < 1e-3
          83 +    return q, ok
          84 +
          85 +def down_R(yaw):
          86 +    c, s = np.cos(yaw), np.sin(yaw)
          87 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          88 +    return np.stack([x, y, z], axis=1)
          89 +
          90 +
          91 +def wb_fk(x):
          92 +    """x = [bx, by, br, q1..q7] -> tool transform."""
          93 +    return _chain(x[3:], x[:3])[0]
          94 +
          95 +
          96 +def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1.0):
          97 +    """Whole-body IK over base y, base rot and the 7 arm joints (base x fixed)."""
          98 +    x = np.array(x0, dtype=float)
          99 +    if q_nom is None:
         100 +        q_nom = HOME
         101 +    W = np.array([w_by, w_br] + [1.0] * 7)
         102 +    for it in range(iters):
         103 +        T, axes = _chain(x[3:], x[:3])
         104 +        pt = T[:3, 3]
         105 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         106 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         107 +            return x, True
         108 +        J = np.zeros((6, 9))
         109 +        J[1, 0] = 1.0
         110 +        ez = np.array([0.0, 0.0, 1.0])
         111 +        J[:3, 1] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         112 +        J[3:, 1] = ez
         113 +        for j, (z, o) in enumerate(axes):
         114 +            J[:3, 2 + j] = np.cross(z, pt - o)
         115 +            J[3:, 2 + j] = z
         116 +        JW = J * W
         117 +        Jp = JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6))
         118 +        Jp = W[:, None] * Jp
         119 +        dv = Jp @ e
         120 +        dn = np.zeros(9)
         121 +        dn[2:] = k_null * ((q_nom - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         122 +        dv += dn - Jp @ (J @ dn)
         123 +        n = np.max(np.abs(dv))
         124 +        if n > 0.3:
         125 +            dv *= 0.3 / n
         126 +        x[1:] += dv
         127 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         128 +    return x, ok
         129 +
         130 +
         131 +Q_NOM = np.array([0.0, 0.3, -np.pi, -2.15, 0.0, -0.69, 0.0])
         132 +K_NOM = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
         133 +
         134 +
         135 +def wb_ik2(x0, p, R, iters=40, tol=1e-5, k_null=0.3, bx_max=-0.12, w_base=1.0):
         136 +    """Whole-body IK over base x (<= bx_max), y, rot and the 7 arm joints.
         137 +    Null space pulls the arm to an extended nominal posture Q_NOM."""
         138 +    x = np.array(x0, dtype=float)
         139 +    ez = np.array([0.0, 0.0, 1.0])
         140 +    for it in range(iters):
         141 +        T, axes = _chain(x[3:], x[:3])
         142 +        pt = T[:3, 3]
         143 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         144 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         145 +            return x, True
         146 +        J = np.zeros((6, 10))
         147 +        J[0, 0] = 1.0
         148 +        J[1, 1] = 1.0
         149 +        J[:3, 2] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         150 +        J[3:, 2] = ez
         151 +        for j, (z, o) in enumerate(axes):
         152 +            J[:3, 3 + j] = np.cross(z, pt - o)
         153 +            J[3:, 3 + j] = z
         154 +        dn = np.zeros(10)
         155 +        dn[3:] = k_null * K_NOM * ((Q_NOM - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         156 +        W = np.array([w_base, w_base, w_base] + [1.0] * 7)
         157 +        for _ in range(2):
         158 +            JW = J * W
         159 +            Jp = W[:, None] * (JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6)))
         160 +            dv = Jp @ e + dn - Jp @ (J @ dn)
         161 +            n = np.max(np.abs(dv))
         162 +            if n > 0.3:
         163 +                dv *= 0.3 / n
         164 +            if x[0] + dv[0] > bx_max + 1e-9 and W[0] > 0:
         165 +                W[0] = 0.0
         166 +                x[0] = min(x[0], bx_max)
         167 +                continue
         168 +            break
         169 +        x += dv
         170 +        x[0] = min(x[0], bx_max) if x0[0] <= bx_max + 1e-9 else x[0]
         171 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         172 +    return x, ok
diff --git a/v_0.1_-0.12/test_approach.py b/v_0.1_-0.12/test_approach.py
new file mode 100644
index 0000000..afc13cc
--- /dev/null
+++ b/v_0.1_-0.12/test_approach.py
@@ -0,0 +1,36 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +def run(seed, verbose=False, max_steps=None, count=None):
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed, options={'object_count': count} if count else None)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0 = time.time()
          11 +    ap.reset(obs, info)
          12 +    ms = max_steps or env.max_steps
          13 +    steps = 0
          14 +    term = False
          15 +    pt = 0.0
          16 +    for steps in range(1, ms + 1):
          17 +        t1 = time.time()
          18 +        a = ap.get_action(obs)
          19 +        pt += time.time() - t1
          20 +        obs, r, term, trunc, info = env.step(a)
          21 +        if term or trunc:
          22 +            break
          23 +    dt = time.time() - t0
          24 +    nobs = len([n for n in obs.get_object_names() if n.startswith('obstruction')])
          25 +    env.close()
          26 +    return term, steps, dt, nobs, ap.phase, pt
          27 +
          28 +if __name__ == '__main__':
          29 +    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          30 +    count = int(sys.argv[3]) if len(sys.argv) > 3 else None
          31 +    ok = 0
          32 +    for s in seeds:
          33 +        term, steps, dt, n, ph, pt = run(s, count=count)
          34 +        ok += term
          35 +        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s ptime={pt:.1f}s nobs={n} phase={ph}', flush=True)
          36 +    print(f'{ok}/{len(seeds)}')
diff --git a/v_0.3_-0.12/approach.py b/v_0.3_-0.12/approach.py
new file mode 100644
index 0000000..98e486e
--- /dev/null
+++ b/v_0.3_-0.12/approach.py
@@ -0,0 +1,584 @@
           1 +"""Obstruction3D approach: clear obstructions off the target region, then place
           2 +the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py).
           3 +
           4 +Empirical facts (black-box probing):
           5 +- Arm mount is +0.12m along base x; the grasp/tool frame is 0.12m past the flange.
           6 +- Gripper fingers lie along the tool x axis, extending ~0.07m from the centre and
           7 +  ~0.035m below the tool frame.  Robot/held object collisions reject a step.
           8 +- Grasp (close) succeeds when tool z in [bottom+0.044, top+0.033] over the object.
           9 +- Release (open) succeeds only if the held object rests within a few mm of a surface.
          10 +"""
          11 +import numpy as np
          12 +from kin import tool_fk, tool_ik, down_R, wb_fk, wb_ik, wb_ik2
          13 +
          14 +JN = [f'joint_{i}' for i in range(1, 8)]
          15 +MERGE_GRIP = True
          16 +WB = True
          17 +CUT_CORNERS = True
          18 +STEP = 0.2             # max joint delta per step
          19 +FINGER_DOWN = 0.036    # fingertips below tool frame
          20 +F_OFF, F_HL, F_HW = 0.046, 0.024, 0.013   # finger centre offset, half length, half width
          21 +
          22 +
          23 +def _q2R(x, y, z, w):
          24 +    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
          25 +                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
          26 +                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
          27 +
          28 +
          29 +def _T(p, q):
          30 +    M = np.eye(4); M[:3, :3] = _q2R(*q); M[:3, 3] = p
          31 +    return M
          32 +
          33 +
          34 +def _yaw_of_quat(q):
          35 +    x, y, z, w = q
          36 +    return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
          37 +
          38 +
          39 +def _wrap(a):
          40 +    return (a + np.pi) % (2 * np.pi) - np.pi
          41 +
          42 +
          43 +def _aabb_of_rect(c, hx, hy, yaw):
          44 +    c_, s_ = abs(np.cos(yaw)), abs(np.sin(yaw))
          45 +    return np.array(c), np.array([c_ * hx + s_ * hy, s_ * hx + c_ * hy])
          46 +
          47 +
          48 +def _gap(c1, h1, c2, h2):
          49 +    """Signed separation between two AABBs (positive = apart)."""
          50 +    return np.max(np.abs(np.asarray(c1) - np.asarray(c2)) - np.asarray(h1) - np.asarray(h2))
          51 +
          52 +
          53 +def _finger_boxes(xy, yaw):
          54 +    d = np.array([np.cos(yaw), np.sin(yaw)])
          55 +    out = []
          56 +    for sgn in (1, -1):
          57 +        out.append(_aabb_of_rect(np.asarray(xy) + sgn * F_OFF * d, F_HL, F_HW, yaw))
          58 +    return out
          59 +
          60 +
          61 +class GeneratedApproach:
          62 +    def __init__(self, action_space, observation_space, primitives):
          63 +        self.action_space = action_space
          64 +        self.observation_space = observation_space
          65 +
          66 +    # ------------------------------------------------------------ helpers
          67 +    def _obj(self, state, name):
          68 +        return state.get_object_from_name(name)
          69 +
          70 +    def _pose(self, state, name):
          71 +        o = self._obj(state, name)
          72 +        return (np.array([state.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')]),
          73 +                np.array([state.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]),
          74 +                np.array([state.get(o, f) for f in ('half_extent_x', 'half_extent_y', 'half_extent_z')]))
          75 +
          76 +    def _box(self, state, name):
          77 +        """(centre_xy, half_xy AABB, bottom z, top z)"""
          78 +        p, q, h = self._pose(state, name)
          79 +        c, hh = _aabb_of_rect(p[:2], h[0], h[1], _yaw_of_quat(q))
          80 +        return c, hh, p[2] - h[2], p[2] + h[2]
          81 +
          82 +    def _q(self, state):
          83 +        return np.array([state.get(self.robot, f) for f in JN])
          84 +
          85 +    def _x(self, state):
          86 +        return np.concatenate([np.array(self._base(state)), self._q(state)])
          87 +
          88 +    def _ik(self, xc, pt, R):
          89 +        if WB:
          90 +            return wb_ik2(xc, pt, R, iters=40, k_null=0.3, bx_max=-0.12)
          91 +        q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
          92 +        return np.concatenate([xc[:3], q]), ok
          93 +
          94 +    def _base(self, state):
          95 +        return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
          96 +                state.get(self.robot, 'pos_base_rot'))
          97 +
          98 +    def _tool(self, state):
          99 +        return tool_fk(self._q(state), self._base(state))
         100 +
         101 +    def _grasped_name(self, state):
         102 +        for n in self.names:
         103 +            if state.get(self._obj(state, n), 'grasp_active') > 0.5:
         104 +                return n
         105 +        return None
         106 +
         107 +    def _max_top(self, state, exclude=()):
         108 +        t = self.table_z
         109 +        for n in self.names:
         110 +            if n in exclude:
         111 +                continue
         112 +            t = max(t, self._box(state, n)[3])
         113 +        return t
         114 +
         115 +    # ------------------------------------------------------------ planning
         116 +    def reset(self, state, info):
         117 +        self.robot = state.get_object_from_name('robot')
         118 +        self.names = sorted(n for n in state.get_object_names() if n != 'robot')
         119 +        self.obstructions = sorted(n for n in self.names if n.startswith('obstruction'))
         120 +        rp, _, rh = self._pose(state, 'target_region')
         121 +        self.table_z = rp[2] - rh[2]
         122 +        self.region = (rp, rh)
         123 +        self.tasks = [(n, 'clear') for n in self._blocking_obstructions(state)]
         124 +        self.tasks.append(('target_block', 'goal'))
         125 +        self.phase = None
         126 +        self.qpath = []
         127 +        self.last_q = None
         128 +        self.last_a = None
         129 +        self.blocked = False
         130 +        self.look = STEP
         131 +        self.fails = {}
         132 +        self.blk_moves = {}
         133 +        self.stuck = 0
         134 +        self.descent_len = 0
         135 +        self.release_tries = 0
         136 +        self.grasp_attempt = 0
         137 +        self.total_fail = 0
         138 +        self.final_grip = 0.0
         139 +        self.wp_yaw = 0.0
         140 +        self._start_task(state)
         141 +
         142 +    def _blocking_obstructions(self, state, margin=0.003):
         143 +        rp, rh = self.region
         144 +        out = []
         145 +        for n in self.obstructions:
         146 +            c, hh, _, _ = self._box(state, n)
         147 +            if _gap(c, hh, rp[:2], rh[:2]) < margin:
         148 +                out.append(n)
         149 +        return out
         150 +
         151 +    def _finger_clearance(self, state, xy, yaw, tip_z, exclude):
         152 +        """Min xy gap between finger boxes and objects whose top is above tip_z."""
         153 +        clear = 1.0
         154 +        fbs = _finger_boxes(xy, yaw)
         155 +        for n in self.names:
         156 +            if n in exclude:
         157 +                continue
         158 +            c, hh, bot, top = self._box(state, n)
         159 +            if top < tip_z - 0.002:
         160 +                continue
         161 +            for fc, fh in fbs:
         162 +                g = _gap(fc, fh, c, hh)
         163 +                if g < clear:
         164 +                    clear = g
         165 +                    if g < 0.005:
         166 +                        self._blocker = n
         167 +        return clear
         168 +
         169 +    def _choose_yaw(self, state, name, kind, attempt):
         170 +        sc = self._yaw_scores(state, name, kind)
         171 +        c = sc[attempt % len(sc)]
         172 +        self.grasp_z = c[3]
         173 +        return c[1]
         174 +
         175 +    def _yaw_scores(self, state, name, kind):
         176 +        """Sorted [(clearance score, yaw, blocker, grasp z)] for grasp candidates."""
         177 +        p, q, h = self._pose(state, name)
         178 +        oy = _yaw_of_quat(q)
         179 +        lo = p[2] - h[2] + 0.045
         180 +        hi = p[2] + h[2] + 0.032
         181 +        gzs = [self._grasp_z(p, h)]
         182 +        if hi - 0.004 > gzs[0] + 0.004:
         183 +            gzs.append(hi - 0.004)
         184 +        cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
         185 +        T = self._tool(state)
         186 +        ty = np.arctan2(T[1, 0], T[0, 0])
         187 +        scored = []
         188 +        for j, gz in enumerate(gzs):
         189 +            for i, y in enumerate(cands):
         190 +                y = _wrap(2 * y) / 2  # modulo pi
         191 +                self._blocker = None
         192 +                c = self._finger_clearance(state, p[:2], y, gz - FINGER_DOWN, exclude=(name,))
         193 +                blk = self._blocker
         194 +                if kind == 'goal':
         195 +                    rp, rh = self.region
         196 +                    surf = rp[2] + rh[2]
         197 +                    tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
         198 +                    c = min(c, self._finger_clearance(state, rp[:2], y, tip,
         199 +                                                      exclude=(name, 'target_region')))
         200 +                rot = abs(_wrap(2 * (y - ty)) / 2)   # rotation needed (mod pi), <= pi/2
         201 +                scored.append((min(c, 0.02) - 0.0005 * i - 0.004 * j - 0.004 * rot, y, blk, gz))
         202 +        scored.sort(key=lambda t: -t[0])
         203 +        return scored
         204 +
         205 +    def _select_task(self, state):
         206 +        """Reorder tasks so the front one is graspable; add blockers if needed."""
         207 +        for _ in range(len(self.names)):
         208 +            name, kind = self.tasks[0]
         209 +            f = self.fails.get(name, 0)
         210 +            sc = self._yaw_scores(state, name, kind)
         211 +            if sc[0][0] > 0.002 and f < 4:
         212 +                return
         213 +            # try another pending clear task that is more graspable
         214 +            best = None
         215 +            for t in self.tasks:
         216 +                if t[1] != 'clear' or t[0] == name:
         217 +                    continue
         218 +                s2 = self._yaw_scores(state, t[0], 'clear')[0][0] - 0.01 * self.fails.get(t[0], 0)
         219 +                if best is None or s2 > best[0]:
         220 +                    best = (s2, t)
         221 +            if best is not None and best[0] > sc[0][0] - 0.01 * f + 0.001:
         222 +                self.tasks.remove(best[1])
         223 +                self.tasks.insert(0, best[1])
         224 +                continue
         225 +            # add the obstruction blocking the fingers as a new task
         226 +            blk = sc[0][2]
         227 +            if (blk is not None and blk.startswith('obstruction')
         228 +                    and all(t[0] != blk for t in self.tasks)
         229 +                    and self.blk_moves.get(blk, 0) < 2
         230 +                    and self._yaw_scores(state, blk, 'clear')[0][0] > 0.002):
         231 +                self.blk_moves[blk] = self.blk_moves.get(blk, 0) + 1
         232 +                self.tasks.insert(0, (blk, 'clear'))
         233 +                continue
         234 +            return
         235 +
         236 +    def _grasp_z(self, p, h):
         237 +        lo = p[2] - h[2] + 0.045
         238 +        hi = p[2] + h[2] + 0.032
         239 +        return 0.5 * (lo + hi) if hi > lo else hi - 0.001
         240 +
         241 +    def _free_spot(self, state, name, yaw, hold_off):
         242 +        """Pick a table spot clear of region/other objects (object + fingers)."""
         243 +        p0, _, _ = self._pose(state, name)
         244 +        c0, h, _, _ = self._box(state, name)
         245 +        others = []
         246 +        for n in self.names:
         247 +            if n == name:
         248 +                continue
         249 +            others.append(self._box(state, n))
         250 +        rp, rh = self.region
         251 +        tip = self.table_z + 0.001 + hold_off - FINGER_DOWN
         252 +        best, best_score = None, 1e9
         253 +        fb, fb_score = None, -1e9
         254 +        for x in np.linspace(0.2, 0.5, 16):
         255 +            for y in np.linspace(-0.34, 0.34, 35):
         256 +                c = np.array([x, y])
         257 +                clear = _gap(c, h, rp[:2], rh[:2]) - 0.03
         258 +                fbs = _finger_boxes(c, yaw)
         259 +                for oc, oh, bot, top in others:
         260 +                    clear = min(clear, _gap(c, h, oc, oh) - 0.02)
         261 +                    if top > tip - 0.002:
         262 +                        for fc, fh in fbs:
         263 +                            clear = min(clear, _gap(fc, fh, oc, oh) - 0.008)
         264 +                if clear > fb_score:
         265 +                    fb, fb_score = c, clear
         266 +                if clear >= 0:
         267 +                    score = np.linalg.norm(c - p0[:2])
         268 +                    if score < best_score:
         269 +                        best, best_score = c, score
         270 +        return best if best is not None else fb
         271 +
         272 +    def _transit_z(self, state, hold_off=0.0, exclude=()):
         273 +        top = self._max_top(state, exclude)
         274 +        return max(top + 0.03 + max(FINGER_DOWN, hold_off), 0.2)
         275 +
         276 +    def _start_task(self, state):
         277 +        if not self.tasks:
         278 +            self.phase = 'done'
         279 +            return
         280 +        try:
         281 +            self._select_task(state)
         282 +        except Exception:
         283 +            pass
         284 +        name, kind = self.tasks[0]
         285 +        p, q, h = self._pose(state, name)
         286 +        self.cur_obj = name
         287 +        self.grasp_yaw = self._choose_yaw(state, name, kind, self.fails.get(name, 0))
         288 +        gz = self.grasp_z
         289 +        zt = self._transit_z(state)
         290 +        tool = self._tool(state)[:3, 3]
         291 +        wps = []
         292 +        rs = 0
         293 +        if tool[2] < zt - 0.01:
         294 +            wps.append(np.array([tool[0], tool[1], zt]))
         295 +            rs = 1
         296 +        wps.append(np.array([p[0], p[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]))
         297 +        wps.append(np.array([p[0], p[1], gz]))
         298 +        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0, flip=True, rot_start=rs)
         299 +        self.phase = 'to_grasp'
         300 +
         301 +    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False, rot_start=0):
         302 +        """Cartesian waypoints -> dense joint path (IK warm-started).
         303 +        Yaw is interpolated from the current tool yaw over all but the last segment."""
         304 +        q = self._x(state)
         305 +        base = self._base(state)
         306 +        T0 = wb_fk(q)
         307 +        cur = T0[:3, 3]
         308 +        y0 = np.arctan2(T0[1, 0], T0[0, 0])
         309 +        dy = _wrap(yaw - y0)
         310 +        if flip and abs(dy) > np.pi / 2:
         311 +            dy = dy - np.sign(dy) * np.pi
         312 +        yaw = y0 + dy
         313 +        pts = [cur]
         314 +        for w in wps:
         315 +            pts.append(np.asarray(w, dtype=float))
         316 +        seg = [np.linalg.norm(pts[i + 1] - pts[i]) for i in range(len(wps))]
         317 +        if len(seg) - 1 <= rot_start:
         318 +            rot_start = 0
         319 +        rot0 = sum(seg[:rot_start])
         320 +        rot_len = sum(seg[rot_start:-1]) if len(seg) > 1 and sum(seg[rot_start:-1]) > 0.02 else sum(seg[rot_start:])
         321 +        rot_len = max(rot_len, 1e-6)
         322 +        path = []
         323 +        self.corners = set()
         324 +        qc = q.copy()
         325 +        travelled = 0.0
         326 +        for i, w in enumerate(wps):
         327 +            w = pts[i + 1]
         328 +            d = seg[i]
         329 +            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.04)))
         330 +            for k in range(1, n + 1):
         331 +                pt = cur + (w - cur) * k / n
         332 +                f = min(1.0, max(0.0, travelled + d * k / n - rot0) / rot_len)
         333 +                qn, ok = self._ik(qc, pt, down_R(y0 + f * dy))
         334 +                qn = qc + _wrap(qn - qc)
         335 +                path.append(qn)
         336 +                qc = qn
         337 +            travelled += d
         338 +            self.corners.add(len(path) - 1)
         339 +            cur = w
         340 +        self.qpath = path
         341 +        self.popped = 0
         342 +        self.wp_yaw = yaw
         343 +        self.final_grip = final_grip
         344 +        self.travel_grip = 1.0 if final_grip < 0 else 0.0
         345 +        self.stuck = 0
         346 +
         347 +    # ------------------------------------------------------------ control
         348 +    def _track(self, state):
         349 +        """Step along the precomputed joint path; None if done."""
         350 +        q = self._x(state)
         351 +        while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
         352 +            self.qpath.pop(0)
         353 +            self.popped += 1
         354 +        if not self.qpath:
         355 +            return None
         356 +        k = -1
         357 +        crossed = False
         358 +        for i, qp in enumerate(self.qpath):
         359 +            if np.max(np.abs(_wrap(qp - q))) <= self.look:
         360 +                if crossed and not self._safe_move(state, q, qp):
         361 +                    break
         362 +                k = i
         363 +                if (i + self.popped) in self.corners:
         364 +                    if not CUT_CORNERS or self.blocked or self.look < STEP:
         365 +                        break
         366 +                    crossed = True
         367 +            else:
         368 +                break
         369 +        a = np.zeros(11, dtype=np.float32)
         370 +        if k >= 0:
         371 +            self.qpath = self.qpath[k:]
         372 +            self.popped += k
         373 +            k = 0
         374 +            d = _wrap(self.qpath[0] - q)
         375 +            a[0:10] = d
         376 +            a[10] = self.travel_grip
         377 +            if MERGE_GRIP and len(self.qpath) == 1 and self.final_grip != 0.0:
         378 +                a[10] = self.final_grip
         379 +        else:
         380 +            d = _wrap(self.qpath[0] - q)
         381 +            a[0:10] = d * (self.look / np.max(np.abs(d)))
         382 +        return a
         383 +
         384 +    def _safe_move(self, state, q0, q1):
         385 +        """Check the joint-linear move q0->q1 keeps tool/fingers/held object
         386 +        above all nearby objects (used when cutting path corners)."""
         387 +        base = self._base(state)
         388 +        held = self._grasped_name(state)
         389 +        depth, rad = FINGER_DOWN, 0.075
         390 +        if held is not None:
         391 +            p, _, h = self._pose(state, held)
         392 +            tz = self._tool(state)[2, 3]
         393 +            depth = max(depth, tz - (p[2] - h[2]))
         394 +            rad = max(rad, np.hypot(h[0], h[1]) + 0.01)
         395 +        boxes = [self._box(state, n) for n in self.names if n != held]
         396 +        dq = _wrap(q1 - q0)
         397 +        for f in (0.25, 0.5, 0.75, 1.0):
         398 +            pt = wb_fk(q0 + f * dq)[:3, 3]
         399 +            low = pt[2] - depth
         400 +            if low < self.table_z + 0.01:
         401 +                return False
         402 +            for c, hh, bot, top in boxes:
         403 +                dxy = np.maximum(np.abs(pt[:2] - c) - hh, 0.0)
         404 +                if np.hypot(dxy[0], dxy[1]) < rad and low < top + 0.012:
         405 +                    return False
         406 +        return True
         407 +
         408 +    def _noop(self, grip=0.0):
         409 +        a = np.zeros(11, dtype=np.float32); a[10] = grip
         410 +        return a
         411 +
         412 +    def get_action(self, state):
         413 +        q = self._x(state)
         414 +        moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
         415 +        attempted = self.last_a is not None and np.any(np.abs(self.last_a[0:10]) > 1e-9)
         416 +        self.blocked = attempted and not moved
         417 +        if self.blocked:
         418 +            self.look = max(0.02, self.look * 0.35)
         419 +        elif attempted:
         420 +            self.look = min(STEP, self.look * 1.5)
         421 +        self.last_q = q.copy()
         422 +        try:
         423 +            a = self._policy(state)
         424 +        except Exception:
         425 +            a = self._noop()
         426 +        a = np.asarray(a, dtype=np.float32).copy()
         427 +        a[:10] = np.clip(a[:10], -STEP, STEP)
         428 +        a[10] = np.clip(a[10], -1, 1)
         429 +        self.last_a = a
         430 +        return a
         431 +
         432 +    def _policy(self, state):
         433 +        ph = self.phase
         434 +        if ph == 'done':
         435 +            if self._grasped_name(state) is None and self.tasks:
         436 +                self._start_task(state)
         437 +            return self._noop()
         438 +
         439 +        if ph == 'to_grasp':
         440 +            g = self._grasped_name(state)
         441 +            if g is not None:
         442 +                return self._on_grasped(state, g)
         443 +            if self.blocked:
         444 +                self.stuck += 1
         445 +                if self.stuck >= 2:
         446 +                    if self._tool(state)[2, 3] > self.grasp_z + 0.012:
         447 +                        # cannot get down to the grasp: try something else
         448 +                        self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         449 +                        self._start_task(state)
         450 +                        a = self._track(state)
         451 +                        return a if a is not None else self._noop()
         452 +                    self.qpath = []
         453 +            a = self._track(state)
         454 +            if a is not None:
         455 +                return a
         456 +            self.phase = 'close'
         457 +            return self._noop(-1.0)
         458 +
         459 +        if ph == 'close':
         460 +            g = self._grasped_name(state)
         461 +            if g is None:
         462 +                self.grasp_attempt += 1
         463 +                self.fails[self.cur_obj] = self.fails.get(self.cur_obj, 0) + 1
         464 +                self.total_fail += 1
         465 +                self._start_task(state)
         466 +                return self._track(state) if self.qpath else self._noop()
         467 +            return self._on_grasped(state, g)
         468 +
         469 +        if ph == 'to_place':
         470 +            if self._grasped_name(state) is None:
         471 +                return self._on_released(state)
         472 +            if self.blocked:
         473 +                self.stuck += 1
         474 +                if len(self.qpath) <= self.descent_len:
         475 +                    self.qpath = []
         476 +                elif self.stuck >= 3:
         477 +                    self._plan_place(state, replan=True)
         478 +            a = self._track(state)
         479 +            if a is not None:
         480 +                return a
         481 +            self.phase = 'open'
         482 +            return self._noop(1.0)
         483 +
         484 +        if ph == 'open':
         485 +            if self._grasped_name(state) is None:
         486 +                return self._on_released(state)
         487 +            self.release_tries += 1
         488 +            tool = self._tool(state)[:3, 3]
         489 +            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw, final_grip=1.0)
         490 +            self.descent_len = 2
         491 +            self.phase = 'to_place'
         492 +            if self.release_tries > 12:
         493 +                self.release_tries = 0
         494 +                self._plan_place(state, replan=True)
         495 +            a = self._track(state)
         496 +            return a if a is not None else self._noop(1.0)
         497 +
         498 +        if ph == 'retreat':
         499 +            if self.blocked:
         500 +                self.stuck += 1
         501 +                if self.stuck >= 2:
         502 +                    self.qpath = []
         503 +            a = self._track(state)
         504 +            if a is not None:
         505 +                return a
         506 +            self._next_task(state)
         507 +            a = self._track(state) if self.phase == 'to_grasp' else None
         508 +            return a if a is not None else self._noop()
         509 +
         510 +        return self._noop()
         511 +
         512 +    def _on_grasped(self, state, g):
         513 +        self.grasp_attempt = 0
         514 +        if g != self.cur_obj:
         515 +            self.tasks.insert(0, (g, 'clear'))
         516 +            self.cur_obj = g
         517 +        self._plan_place(state)
         518 +        a = self._track(state)
         519 +        return a if a is not None else self._noop()
         520 +
         521 +    def _on_released(self, state):
         522 +        self.release_tries = 0
         523 +        name, kind = self.tasks.pop(0) if self.tasks else (None, None)
         524 +        if kind == 'goal':
         525 +            self.phase = 'done'
         526 +            return self._noop()
         527 +        self._next_task(state)
         528 +        a = self._track(state) if self.phase == 'to_grasp' else None
         529 +        return a if a is not None else self._noop()
         530 +
         531 +    def _next_task(self, state):
         532 +        if self.tasks and self.tasks[0][1] == 'goal':
         533 +            for n in self._blocking_obstructions(state):
         534 +                if all(t[0] != n for t in self.tasks):
         535 +                    self.tasks.insert(0, (n, 'clear'))
         536 +        self._start_task(state)
         537 +
         538 +    def _plan_place(self, state, replan=False):
         539 +        name = self.cur_obj
         540 +        p, qo, h = self._pose(state, name)
         541 +        r = self.robot
         542 +        tf = _T([state.get(r, 'grasp_tf_x'), state.get(r, 'grasp_tf_y'), state.get(r, 'grasp_tf_z')],
         543 +                [state.get(r, 'grasp_tf_qx'), state.get(r, 'grasp_tf_qy'), state.get(r, 'grasp_tf_qz'),
         544 +                 state.get(r, 'grasp_tf_qw')])
         545 +        kind = self.tasks[0][1] if self.tasks and self.tasks[0][0] == name else 'clear'
         546 +        Ttool_now = self._tool(state)
         547 +        hold_off = Ttool_now[2, 3] - (p[2] - h[2])   # tool height above held-object bottom
         548 +        yaw = np.arctan2(Ttool_now[1, 0], Ttool_now[0, 0])
         549 +        if kind == 'goal':
         550 +            rp, rh = self.region
         551 +            xy = rp[:2]
         552 +            surf = rp[2] + rh[2]
         553 +        else:
         554 +            xy = self._free_spot(state, name, yaw, hold_off)
         555 +            if replan:
         556 +                xy = xy + np.random.uniform(-0.03, 0.03, 2)
         557 +            surf = self.table_z
         558 +        Tobj = _T([xy[0], xy[1], surf + h[2] + 0.001], qo)
         559 +        Ttool = Tobj @ np.linalg.inv(tf)
         560 +        tgt = Ttool[:3, 3]
         561 +        tyaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
         562 +        zt = self._transit_z(state, hold_off, exclude=(name,))
         563 +        tool = Ttool_now[:3, 3]
         564 +        wps = []
         565 +        if tool[2] < zt - 0.005:
         566 +            wps.append(np.array([tool[0], tool[1], zt]))
         567 +        wps += [np.array([tgt[0], tgt[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]),
         568 +                np.array([tgt[0], tgt[1], tgt[2] + 0.015])]
         569 +        self._set_path(state, wps, tyaw)
         570 +        n_before = len(self.qpath)
         571 +        self._append_descent(state, tgt, tyaw)
         572 +        self.descent_len = len(self.qpath) - n_before + 2
         573 +        self.final_grip = 1.0
         574 +        self.phase = 'to_place'
         575 +
         576 +    def _append_descent(self, state, tgt, yaw):
         577 +        base = self._base(state)
         578 +        qc = self.qpath[-1] if self.qpath else self._x(state)
         579 +        R = down_R(yaw)
         580 +        for dz in (0.008, 0.003, 0.0):
         581 +            qn, ok = self._ik(qc, tgt + np.array([0, 0, dz]), R)
         582 +            qn = qc + _wrap(qn - qc)
         583 +            self.qpath.append(qn)
         584 +            qc = qn
diff --git a/v_0.3_-0.12/env_client.py b/v_0.3_-0.12/env_client.py
new file mode 100644
index 0000000..108c884
--- /dev/null
+++ b/v_0.3_-0.12/env_client.py
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
diff --git a/v_0.3_-0.12/env_spaces.json b/v_0.3_-0.12/env_spaces.json
new file mode 100644
index 0000000..dff8dfd
--- /dev/null
+++ b/v_0.3_-0.12/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "6eefef35bfaa192f7898ebf189cf2b7d", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
diff --git a/v_0.3_-0.12/kin.py b/v_0.3_-0.12/kin.py
new file mode 100644
index 0000000..b360a71
--- /dev/null
+++ b/v_0.3_-0.12/kin.py
@@ -0,0 +1,172 @@
           1 +import numpy as np
           2 +
           3 +def _rpy(r, p, y):
           4 +    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
           5 +    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
           6 +                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
           7 +                     [-sp, cp*sr, cp*cr]])
           8 +
           9 +def _T(xyz, rpy):
          10 +    T = np.eye(4); T[:3, :3] = _rpy(*rpy); T[:3, 3] = xyz; return T
          11 +
          12 +PI = np.pi
          13 +H = PI / 2
          14 +JOINTS = [
          15 +    _T((0, 0, 0.15643), (PI, 0, 0)),
          16 +    _T((0, 0.005375, -0.12838), (H, 0, 0)),
          17 +    _T((0, -0.21038, -0.006375), (-H, 0, 0)),
          18 +    _T((0, 0.006375, -0.21038), (H, 0, 0)),
          19 +    _T((0, -0.20843, -0.006375), (-H, 0, 0)),
          20 +    _T((0, 0.00017505, -0.10593), (H, 0, 0)),
          21 +    _T((0, -0.10593, -0.00017505), (-H, 0, 0)),
          22 +]
          23 +EE = _T((0, 0, -0.061525), (PI, 0, 0))
          24 +MOUNT = (0.12, 0.0, -0.0052)
          25 +TOOL = 0.12
          26 +HOME = np.array([0.0, -0.35, -np.pi, -2.5, 0.0, -0.87, np.pi / 2])
          27 +
          28 +def _rz(q):
          29 +    c, s = np.cos(q), np.sin(q)
          30 +    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T
          31 +
          32 +def mount_base(base):
          33 +    bx, by, br = base
          34 +    c, s = np.cos(br), np.sin(br)
          35 +    return (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)
          36 +
          37 +def _chain(q, base):
          38 +    """Returns tool transform and list of (axis, origin) of joints in world."""
          39 +    bx, by, br = mount_base(base)
          40 +    T = _rz(br); T[0, 3] = bx; T[1, 3] = by; T[2, 3] = MOUNT[2]
          41 +    axes = []
          42 +    for Tj, qj in zip(JOINTS, q):
          43 +        T = T @ Tj
          44 +        axes.append((T[:3, 2].copy(), T[:3, 3].copy()))
          45 +        T = T @ _rz(qj)
          46 +    T = T @ EE
          47 +    Tt = np.eye(4); Tt[2, 3] = TOOL
          48 +    return T @ Tt, axes
          49 +
          50 +def tool_fk(q, base):
          51 +    return _chain(q, base)[0]
          52 +
          53 +def _rot_err(Rc, Rd):
          54 +    Re = Rd @ Rc.T
          55 +    v = 0.5 * np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
          56 +    return v
          57 +
          58 +def tool_ik(q0, p, R, base, iters=60, tol=1e-5, q_nom=None, k_null=0.3):
          59 +    q = np.array(q0, dtype=float)
          60 +    if q_nom is None:
          61 +        q_nom = HOME
          62 +    for it in range(iters):
          63 +        T, axes = _chain(q, base)
          64 +        e = np.concatenate([p - T[:3, 3], _rot_err(T[:3, :3], R)])
          65 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
          66 +            return q, True
          67 +        J = np.zeros((6, 7))
          68 +        pt = T[:3, 3]
          69 +        for j, (z, o) in enumerate(axes):
          70 +            J[:3, j] = np.cross(z, pt - o)
          71 +            J[3:, j] = z
          72 +        JJt = J @ J.T + 1e-6 * np.eye(6)
          73 +        Jp = J.T @ np.linalg.inv(JJt)
          74 +        dq = Jp @ e
          75 +        dn = (q_nom - q + np.pi) % (2 * np.pi) - np.pi
          76 +        dq += (np.eye(7) - Jp @ J) @ (k_null * dn)
          77 +        n = np.max(np.abs(dq))
          78 +        if n > 0.3:
          79 +            dq *= 0.3 / n
          80 +        q = q + dq
          81 +    T, _ = _chain(q, base)
          82 +    ok = np.linalg.norm(p - T[:3, 3]) < 1e-3
          83 +    return q, ok
          84 +
          85 +def down_R(yaw):
          86 +    c, s = np.cos(yaw), np.sin(yaw)
          87 +    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
          88 +    return np.stack([x, y, z], axis=1)
          89 +
          90 +
          91 +def wb_fk(x):
          92 +    """x = [bx, by, br, q1..q7] -> tool transform."""
          93 +    return _chain(x[3:], x[:3])[0]
          94 +
          95 +
          96 +def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1.0):
          97 +    """Whole-body IK over base y, base rot and the 7 arm joints (base x fixed)."""
          98 +    x = np.array(x0, dtype=float)
          99 +    if q_nom is None:
         100 +        q_nom = HOME
         101 +    W = np.array([w_by, w_br] + [1.0] * 7)
         102 +    for it in range(iters):
         103 +        T, axes = _chain(x[3:], x[:3])
         104 +        pt = T[:3, 3]
         105 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         106 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         107 +            return x, True
         108 +        J = np.zeros((6, 9))
         109 +        J[1, 0] = 1.0
         110 +        ez = np.array([0.0, 0.0, 1.0])
         111 +        J[:3, 1] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         112 +        J[3:, 1] = ez
         113 +        for j, (z, o) in enumerate(axes):
         114 +            J[:3, 2 + j] = np.cross(z, pt - o)
         115 +            J[3:, 2 + j] = z
         116 +        JW = J * W
         117 +        Jp = JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6))
         118 +        Jp = W[:, None] * Jp
         119 +        dv = Jp @ e
         120 +        dn = np.zeros(9)
         121 +        dn[2:] = k_null * ((q_nom - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         122 +        dv += dn - Jp @ (J @ dn)
         123 +        n = np.max(np.abs(dv))
         124 +        if n > 0.3:
         125 +            dv *= 0.3 / n
         126 +        x[1:] += dv
         127 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         128 +    return x, ok
         129 +
         130 +
         131 +Q_NOM = np.array([0.0, 0.3, -np.pi, -2.15, 0.0, -0.69, 0.0])
         132 +K_NOM = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])
         133 +
         134 +
         135 +def wb_ik2(x0, p, R, iters=40, tol=1e-5, k_null=0.3, bx_max=-0.12, w_base=1.0):
         136 +    """Whole-body IK over base x (<= bx_max), y, rot and the 7 arm joints.
         137 +    Null space pulls the arm to an extended nominal posture Q_NOM."""
         138 +    x = np.array(x0, dtype=float)
         139 +    ez = np.array([0.0, 0.0, 1.0])
         140 +    for it in range(iters):
         141 +        T, axes = _chain(x[3:], x[:3])
         142 +        pt = T[:3, 3]
         143 +        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
         144 +        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
         145 +            return x, True
         146 +        J = np.zeros((6, 10))
         147 +        J[0, 0] = 1.0
         148 +        J[1, 1] = 1.0
         149 +        J[:3, 2] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
         150 +        J[3:, 2] = ez
         151 +        for j, (z, o) in enumerate(axes):
         152 +            J[:3, 3 + j] = np.cross(z, pt - o)
         153 +            J[3:, 3 + j] = z
         154 +        dn = np.zeros(10)
         155 +        dn[3:] = k_null * K_NOM * ((Q_NOM - x[3:] + np.pi) % (2 * np.pi) - np.pi)
         156 +        W = np.array([w_base, w_base, w_base] + [1.0] * 7)
         157 +        for _ in range(2):
         158 +            JW = J * W
         159 +            Jp = W[:, None] * (JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6)))
         160 +            dv = Jp @ e + dn - Jp @ (J @ dn)
         161 +            n = np.max(np.abs(dv))
         162 +            if n > 0.3:
         163 +                dv *= 0.3 / n
         164 +            if x[0] + dv[0] > bx_max + 1e-9 and W[0] > 0:
         165 +                W[0] = 0.0
         166 +                x[0] = min(x[0], bx_max)
         167 +                continue
         168 +            break
         169 +        x += dv
         170 +        x[0] = min(x[0], bx_max) if x0[0] <= bx_max + 1e-9 else x[0]
         171 +    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
         172 +    return x, ok
diff --git a/v_0.3_-0.12/test_approach.py b/v_0.3_-0.12/test_approach.py
new file mode 100644
index 0000000..afc13cc
--- /dev/null
+++ b/v_0.3_-0.12/test_approach.py
@@ -0,0 +1,36 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +def run(seed, verbose=False, max_steps=None, count=None):
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed, options={'object_count': count} if count else None)
           9 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          10 +    t0 = time.time()
          11 +    ap.reset(obs, info)
          12 +    ms = max_steps or env.max_steps
          13 +    steps = 0
          14 +    term = False
          15 +    pt = 0.0
          16 +    for steps in range(1, ms + 1):
          17 +        t1 = time.time()
          18 +        a = ap.get_action(obs)
          19 +        pt += time.time() - t1
          20 +        obs, r, term, trunc, info = env.step(a)
          21 +        if term or trunc:
          22 +            break
          23 +    dt = time.time() - t0
          24 +    nobs = len([n for n in obs.get_object_names() if n.startswith('obstruction')])
          25 +    env.close()
          26 +    return term, steps, dt, nobs, ap.phase, pt
          27 +
          28 +if __name__ == '__main__':
          29 +    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
          30 +    count = int(sys.argv[3]) if len(sys.argv) > 3 else None
          31 +    ok = 0
          32 +    for s in seeds:
          33 +        term, steps, dt, n, ph, pt = run(s, count=count)
          34 +        ok += term
          35 +        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s ptime={pt:.1f}s nobs={n} phase={ph}', flush=True)
          36 +    print(f'{ok}/{len(seeds)}')
```

</details>

<a id="C021"></a>
### C021 · Micro-lift fallback when held object is wedged and lift blocked

Commit `37ffc6ed4efbdc9709aeff4d7c356d17a87d6aa2`; parents: cc5e97f05d3f4d62ca49b212baae34ff93d23594. Recorded author date: 2026-09-30T23:12:26+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E1250](01_timeline.md#E1250): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C021_37ffc6e_approach.py) · [Exact all-file diff](evidence/diffs/C021_37ffc6e.diff)

[Previous saved controller snapshot](evidence/versions/C020_cc5e97f_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 83fd918..62fd63f 100644
--- a/approach.py
+++ b/approach.py
@@ -131,6 +131,7 @@ class GeneratedApproach:
  131    131          self.fails = {}
  132    132          self.blk_moves = {}
  133    133          self.stuck = 0
         134 +        self.micro = 0
  134    135          self.descent_len = 0
  135    136          self.release_tries = 0
  136    137          self.grasp_attempt = 0
@@ -469,10 +470,19 @@ class GeneratedApproach:
  469    470          if ph == 'to_place':
  470    471              if self._grasped_name(state) is None:
  471    472                  return self._on_released(state)
         473 +            if self.micro > 0:
         474 +                a = self._micro_up(state)
         475 +                if a is not None:
         476 +                    return a
  472    477              if self.blocked:
  473    478                  self.stuck += 1
  474    479                  if len(self.qpath) <= self.descent_len:
  475    480                      self.qpath = []
         481 +                elif self.stuck >= 2 and self.micro == 0 and self._held_low(state):
         482 +                    self.micro = 1
         483 +                    a = self._micro_up(state)
         484 +                    if a is not None:
         485 +                        return a
  476    486                  elif self.stuck >= 3:
  477    487                      self._plan_place(state, replan=True)
  478    488              a = self._track(state)
@@ -535,6 +545,35 @@ class GeneratedApproach:
  535    545                      self.tasks.insert(0, (n, 'clear'))
  536    546          self._start_task(state)
  537    547  
         548 +    def _held_low(self, state):
         549 +        g = self._grasped_name(state)
         550 +        if g is None:
         551 +            return False
         552 +        p, _, h = self._pose(state, g)
         553 +        top = self.table_z
         554 +        for n in self.names:
         555 +            if n == g:
         556 +                continue
         557 +            c, hh, b, t = self._box(state, n)
         558 +            if np.linalg.norm(c[:2] - p[:2]) < 0.1:
         559 +                top = max(top, t)
         560 +        return p[2] - h[2] < top + 0.01
         561 +
         562 +    def _micro_up(self, state):
         563 +        # tiny straight-up steps: large moves get rejected when the held object is wedged
         564 +        if (self.micro > 1 and self.blocked) or self.micro > 60 or not self._held_low(state):
         565 +            self.micro = 0
         566 +            self._plan_place(state, replan=False)
         567 +            return None
         568 +        self.micro += 1
         569 +        x = self._x(state)
         570 +        T = wb_fk(x)
         571 +        yaw = np.arctan2(T[1, 0], T[0, 0])
         572 +        xn, ok = self._ik(x, T[:3, 3] + np.array([0, 0, 0.0045]), down_R(yaw))
         573 +        a = self._noop()
         574 +        a[:10] = np.clip(xn - x, -STEP, STEP)
         575 +        return a
         576 +
  538    577      def _plan_place(self, state, replan=False):
  539    578          name = self.cur_obj
  540    579          p, qo, h = self._pose(state, name)
diff --git a/dbg_jd.py b/dbg_jd.py
index 6517da5..d2ce510 100644
--- a/dbg_jd.py
+++ b/dbg_jd.py
@@ -7,6 +7,6 @@ env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]),options={'object_count'
    7      7  ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
    8      8  for t in range(int(sys.argv[2])):
    9      9      a=ap.get_action(obs); obs,*_=env.step(a)
   10        -q=ap._q(obs); print('q',np.round(q,2))
          10 +q=ap._x(obs); print('q',np.round(q,2))
   11     11  for i,qp in enumerate(ap.qpath[:30]):
   12        -    T=tool_fk(qp,ap._base(obs)); print(i,np.round(T[:3,3],3),round(float(np.arctan2(T[1,0],T[0,0])),2),np.round(qp-q,2)); q=qp
          12 +    from kin import wb_fk; T=wb_fk(qp); print(i,np.round(T[:3,3],3),round(float(np.arctan2(T[1,0],T[0,0])),2),np.round(qp-q,2)); q=qp
diff --git a/probe_c6.py b/probe_c6.py
new file mode 100644
index 0000000..51929a6
--- /dev/null
+++ b/probe_c6.py
@@ -0,0 +1,28 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import tool_fk, tool_ik, down_R, wb_ik2, wb_fk
           5 +seed=int(sys.argv[1]); T=int(sys.argv[2]); cnt=int(sys.argv[3])
           6 +def replay():
           7 +    env=make_env(); obs,info=env.reset(seed=seed,options={'object_count':cnt})
           8 +    ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           9 +    for t in range(T):
          10 +        a=ap.get_action(obs); obs,*_=env.step(a)
          11 +    return env,obs,ap
          12 +env,obs,ap=replay()
          13 +x=ap._x(obs); Tt=wb_fk(x); yaw=np.arctan2(Tt[1,0],Tt[0,0])
          14 +print('x',np.round(x,3),'tool',np.round(Tt[:3,3],3),'yaw',round(yaw,2), 'held', ap._grasped_name(obs))
          15 +for n in ap.names:
          16 +    c,hh,b,t=ap._box(obs,n); print(' ',n,np.round(c,3),np.round(hh,3),round(b,3),round(t,3))
          17 +tests=[('arm up 5mm',None,(0,0,0.005)),('wb up 5mm','wb',(0,0,0.005)),('base -x 1cm','bx',None),('base -y 1cm','by-',None),('base +y 1cm','by+',None),('arm +x5mm',None,(0.005,0,0)),('arm -x5mm',None,(-0.005,0,0)),('arm +y5mm',None,(0,0.005,0)),('arm -y5mm',None,(0,-0.005,0))]
          18 +for name,mode,d in tests:
          19 +    env.close(); env,obs,ap=replay()
          20 +    a=np.zeros(11,dtype=np.float32)
          21 +    if mode=='bx': a[0]=-0.01
          22 +    elif mode=='by-': a[1]=-0.01
          23 +    elif mode=='by+': a[1]=0.01
          24 +    elif mode=='wb':
          25 +        xn,ok=wb_ik2(x,Tt[:3,3]+np.array(d),down_R(yaw),k_null=0.05,bx_max=-0.09); a[0:10]=np.clip(xn-x,-0.2,0.2)
          26 +    else:
          27 +        q,ok=tool_ik(x[3:],Tt[:3,3]+np.array(d),down_R(yaw),tuple(x[:3])); a[3:10]=np.clip(q-x[3:],-0.2,0.2)
          28 +    obs2,*_=env.step(a); print(name,'moved',not np.allclose(ap._x(obs2),x))
diff --git a/probe_up.py b/probe_up.py
new file mode 100644
index 0000000..70961f8
--- /dev/null
+++ b/probe_up.py
@@ -0,0 +1,30 @@
           1 +import sys, numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +from kin import tool_fk, tool_ik, down_R, wb_ik2, wb_fk
           5 +seed=int(sys.argv[1]); T=int(sys.argv[2]); cnt=int(sys.argv[3])
           6 +def replay():
           7 +    env=make_env(); obs,info=env.reset(seed=seed,options={'object_count':cnt})
           8 +    ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
           9 +    for t in range(T):
          10 +        a=ap.get_action(obs); obs,*_=env.step(a)
          11 +    return env,obs,ap
          12 +env,obs,ap=replay()
          13 +x=ap._x(obs); Tt=wb_fk(x); yaw=np.arctan2(Tt[1,0],Tt[0,0])
          14 +print('x',np.round(x,3),'tool',np.round(Tt[:3,3],3),'yaw',round(yaw,2), 'held', ap._grasped_name(obs))
          15 +for n in ap.names:
          16 +    c,hh,b,t=ap._box(obs,n); print(' ',n,np.round(c,3),np.round(hh,3),round(b,3),round(t,3))
          17 +tests=[('wb up 1cm','wb',(0,0,0.01)),('wb up 2cm','wb',(0,0,0.02)),('wb up 3cm','wb',(0,0,0.03)),('wb up 5cm','wb',(0,0,0.05)),('policy',None,None)]
          18 +for name,mode,d in tests:
          19 +    env.close(); env,obs,ap=replay()
          20 +    a=np.zeros(11,dtype=np.float32)
          21 +    if mode=='bx': a[0]=-0.01
          22 +    elif mode=='by-': a[1]=-0.01
          23 +    elif mode=='by+': a[1]=0.01
          24 +    elif mode=='wb':
          25 +        xn,ok=wb_ik2(x,Tt[:3,3]+np.array(d),down_R(yaw),k_null=0.05,bx_max=-0.09); a[0:10]=np.clip(xn-x,-0.2,0.2)
          26 +    elif mode is None and d is None:
          27 +        a=ap.get_action(obs); print(np.round(a,3))
          28 +    else:
          29 +        q,ok=tool_ik(x[3:],Tt[:3,3]+np.array(d),down_R(yaw),tuple(x[:3])); a[3:10]=np.clip(q-x[3:],-0.2,0.2)
          30 +    obs2,*_=env.step(a); print(name,'moved',not np.allclose(ap._x(obs2),x))
diff --git a/probe_up2.py b/probe_up2.py
new file mode 100644
index 0000000..d121d97
--- /dev/null
+++ b/probe_up2.py
@@ -0,0 +1,12 @@
           1 +import sys, numpy as np
           2 +exec(open('probe_c6.py').read().split('tests=')[0])
           3 +def up(obs,dz,wb):
           4 +    x=ap._x(obs); Tt=wb_fk(x); a=np.zeros(11,dtype=np.float32)
           5 +    if wb: xn,ok=wb_ik2(x,Tt[:3,3]+np.array([0,0,dz]),down_R(yaw),k_null=0.05,bx_max=-0.09); a[0:10]=np.clip(xn-x,-0.2,0.2)
           6 +    else: q,ok=tool_ik(x[3:],Tt[:3,3]+np.array([0,0,dz]),down_R(yaw),tuple(x[:3])); a[3:10]=np.clip(q-x[3:],-0.2,0.2)
           7 +    o2,*_=env.step(a); return o2
           8 +for dz,wb in [(0.01,False),(0.007,False),(0.005,False)]:
           9 +    env.close(); env,obs,ap=replay()
          10 +    for k in range(8):
          11 +        o2=up(obs,dz,wb); mv=not np.allclose(ap._x(o2),ap._x(obs)); obs=o2
          12 +        print(dz,wb,k,mv,np.round(wb_fk(ap._x(obs))[:3,3],3))
diff --git a/res_c1.txt b/res_c1.txt
new file mode 100644
index 0000000..354ead0
--- /dev/null
+++ b/res_c1.txt
@@ -0,0 +1,30 @@
           1 +seed 3: success=True steps=8 time=4.9s ptime=0.1s nobs=1 phase=to_place
           2 +seed 10: success=True steps=16 time=36.1s ptime=0.1s nobs=1 phase=to_place
           3 +seed 2: success=True steps=17 time=43.2s ptime=0.2s nobs=1 phase=to_place
           4 +seed 0: success=True steps=15 time=25.7s ptime=0.2s nobs=1 phase=to_place
           5 +seed 7: success=True steps=17 time=29.4s ptime=0.2s nobs=1 phase=to_place
           6 +seed 9: success=True steps=16 time=33.2s ptime=0.2s nobs=1 phase=to_place
           7 +seed 4: success=True steps=25 time=42.9s ptime=0.3s nobs=1 phase=to_place
           8 +seed 11: success=True steps=17 time=20.8s ptime=0.2s nobs=1 phase=to_place
           9 +seed 6: success=True steps=20 time=39.1s ptime=0.2s nobs=1 phase=to_place
          10 +seed 1: success=True steps=19 time=36.1s ptime=0.2s nobs=1 phase=to_place
          11 +seed 8: success=True steps=18 time=29.0s ptime=0.2s nobs=1 phase=to_place
          12 +seed 5: success=True steps=30 time=59.3s ptime=0.3s nobs=1 phase=to_place
          13 +seed 12: success=True steps=16 time=42.2s ptime=0.2s nobs=1 phase=to_place
          14 +seed 13: success=True steps=15 time=40.7s ptime=0.1s nobs=1 phase=to_place
          15 +seed 18: success=True steps=8 time=21.8s ptime=0.1s nobs=1 phase=to_place
          16 +seed 15: success=True steps=16 time=41.3s ptime=0.2s nobs=1 phase=to_place
          17 +seed 21: success=True steps=9 time=22.1s ptime=0.1s nobs=1 phase=to_place
          18 +seed 14: success=True steps=17 time=47.2s ptime=0.2s nobs=1 phase=to_place
          19 +seed 17: success=True steps=16 time=38.4s ptime=0.2s nobs=1 phase=to_place
          20 +seed 19: success=True steps=15 time=36.6s ptime=0.3s nobs=1 phase=to_place
          21 +seed 16: success=True steps=17 time=45.8s ptime=0.2s nobs=1 phase=to_place
          22 +seed 24: success=True steps=10 time=20.7s ptime=0.1s nobs=1 phase=to_place
          23 +seed 22: success=True steps=16 time=30.7s ptime=0.3s nobs=1 phase=to_place
          24 +seed 20: success=True steps=17 time=37.1s ptime=0.2s nobs=1 phase=to_place
          25 +seed 23: success=True steps=17 time=25.5s ptime=0.3s nobs=1 phase=to_place
          26 +seed 29: success=True steps=7 time=2.9s ptime=0.1s nobs=1 phase=to_place
          27 +seed 25: success=True steps=20 time=16.8s ptime=0.2s nobs=1 phase=to_place
          28 +seed 26: success=True steps=20 time=14.7s ptime=0.3s nobs=1 phase=to_place
          29 +seed 27: success=True steps=19 time=10.3s ptime=0.3s nobs=1 phase=to_place
          30 +seed 28: success=True steps=30 time=7.5s ptime=0.4s nobs=1 phase=to_place
diff --git a/res_c4f.txt b/res_c4f.txt
new file mode 100644
index 0000000..fdea7a0
--- /dev/null
+++ b/res_c4f.txt
@@ -0,0 +1,40 @@
           1 +seed 47: success=True steps=15 time=35.2s ptime=0.2s nobs=4 phase=to_place
           2 +seed 43: success=True steps=25 time=48.3s ptime=0.4s nobs=4 phase=to_place
           3 +seed 48: success=True steps=28 time=37.7s ptime=0.3s nobs=4 phase=to_place
           4 +seed 44: success=True steps=33 time=48.2s ptime=0.5s nobs=4 phase=to_place
           5 +seed 46: success=True steps=33 time=38.2s ptime=0.5s nobs=4 phase=to_place
           6 +seed 45: success=True steps=42 time=72.5s ptime=0.8s nobs=4 phase=to_place
           7 +seed 42: success=True steps=38 time=79.0s ptime=0.6s nobs=4 phase=to_place
           8 +seed 51: success=True steps=39 time=45.5s ptime=0.7s nobs=4 phase=to_place
           9 +seed 49: success=True steps=47 time=64.6s ptime=0.9s nobs=4 phase=to_place
          10 +seed 40: success=True steps=47 time=70.9s ptime=1.0s nobs=4 phase=to_place
          11 +seed 50: success=True steps=47 time=61.1s ptime=0.9s nobs=4 phase=to_place
          12 +seed 41: success=True steps=67 time=98.0s ptime=1.0s nobs=4 phase=to_place
          13 +seed 54: success=True steps=36 time=52.7s ptime=0.6s nobs=4 phase=to_place
          14 +seed 52: success=True steps=54 time=73.6s ptime=0.7s nobs=4 phase=to_place
          15 +seed 58: success=True steps=29 time=41.3s ptime=0.6s nobs=4 phase=to_place
          16 +seed 55: success=True steps=38 time=63.1s ptime=0.7s nobs=4 phase=to_place
          17 +seed 57: success=True steps=38 time=52.5s ptime=0.7s nobs=4 phase=to_place
          18 +seed 53: success=True steps=46 time=74.7s ptime=0.7s nobs=4 phase=to_place
          19 +seed 56: success=True steps=39 time=66.6s ptime=0.7s nobs=4 phase=to_place
          20 +seed 59: success=True steps=34 time=58.8s ptime=0.7s nobs=4 phase=to_place
          21 +seed 60: success=True steps=29 time=51.7s ptime=0.6s nobs=4 phase=to_place
          22 +seed 64: success=True steps=26 time=44.4s ptime=0.5s nobs=4 phase=to_place
          23 +seed 63: success=True steps=30 time=53.2s ptime=0.4s nobs=4 phase=to_place
          24 +seed 69: success=True steps=26 time=29.2s ptime=0.6s nobs=4 phase=to_place
          25 +seed 62: success=True steps=57 time=75.9s ptime=0.8s nobs=4 phase=to_place
          26 +seed 65: success=True steps=36 time=54.8s ptime=0.8s nobs=4 phase=to_place
          27 +seed 68: success=True steps=34 time=47.2s ptime=0.6s nobs=4 phase=to_place
          28 +seed 61: success=True steps=58 time=85.7s ptime=0.9s nobs=4 phase=to_place
          29 +seed 66: success=True steps=43 time=68.0s ptime=0.6s nobs=4 phase=to_place
          30 +seed 67: success=True steps=40 time=61.5s ptime=1.0s nobs=4 phase=to_place
          31 +seed 70: success=True steps=36 time=46.3s ptime=0.6s nobs=4 phase=to_place
          32 +seed 72: success=True steps=41 time=44.8s ptime=0.8s nobs=4 phase=to_place
          33 +seed 73: success=True steps=25 time=31.6s ptime=0.5s nobs=4 phase=to_place
          34 +seed 71: success=True steps=48 time=48.4s ptime=0.8s nobs=4 phase=to_place
          35 +seed 79: success=True steps=25 time=9.5s ptime=0.3s nobs=4 phase=to_place
          36 +seed 78: success=True steps=33 time=14.4s ptime=0.5s nobs=4 phase=to_place
          37 +seed 74: success=True steps=42 time=33.7s ptime=0.7s nobs=4 phase=to_place
          38 +seed 76: success=True steps=48 time=21.8s ptime=0.9s nobs=4 phase=to_place
          39 +seed 77: success=True steps=66 time=22.7s ptime=1.1s nobs=4 phase=to_place
          40 +seed 75: success=True steps=104 time=33.2s ptime=1.3s nobs=4 phase=to_place
diff --git a/res_c6.txt b/res_c6.txt
new file mode 100644
index 0000000..32105b2
--- /dev/null
+++ b/res_c6.txt
@@ -0,0 +1,20 @@
           1 +seed 10: success=True steps=42 time=46.0s ptime=0.8s nobs=6 phase=to_place
           2 +seed 2: success=True steps=35 time=23.8s ptime=0.8s nobs=6 phase=to_place
           3 +seed 3: success=True steps=42 time=39.3s ptime=1.0s nobs=6 phase=to_place
           4 +seed 11: success=True steps=63 time=77.1s ptime=1.5s nobs=6 phase=to_place
           5 +seed 8: success=True steps=60 time=58.1s ptime=1.4s nobs=6 phase=to_place
           6 +seed 7: success=True steps=54 time=61.3s ptime=1.2s nobs=6 phase=to_place
           7 +seed 9: success=True steps=50 time=49.1s ptime=1.3s nobs=6 phase=to_place
           8 +seed 0: success=True steps=71 time=95.0s ptime=1.2s nobs=6 phase=to_place
           9 +seed 1: success=True steps=67 time=67.5s ptime=1.4s nobs=6 phase=to_place
          10 +seed 6: success=True steps=69 time=67.7s ptime=1.6s nobs=6 phase=to_place
          11 +seed 14: success=True steps=38 time=38.8s ptime=0.9s nobs=6 phase=to_place
          12 +seed 12: success=True steps=55 time=54.4s ptime=1.3s nobs=6 phase=to_place
          13 +seed 16: success=True steps=44 time=29.8s ptime=0.9s nobs=6 phase=to_place
          14 +seed 13: success=True steps=63 time=55.1s ptime=1.2s nobs=6 phase=to_place
          15 +seed 5: success=True steps=110 time=106.8s ptime=2.0s nobs=6 phase=to_place
          16 +seed 15: success=True steps=60 time=41.2s ptime=1.2s nobs=6 phase=to_place
          17 +seed 18: success=True steps=49 time=28.5s ptime=1.1s nobs=6 phase=to_place
          18 +seed 17: success=True steps=49 time=31.4s ptime=1.2s nobs=6 phase=to_place
          19 +seed 19: success=True steps=47 time=20.5s ptime=1.1s nobs=6 phase=to_place
          20 +seed 4: success=False steps=1000 time=134.0s ptime=27.1s nobs=6 phase=to_place
diff --git a/res_d8.txt b/res_d8.txt
new file mode 100644
index 0000000..3fec1a2
--- /dev/null
+++ b/res_d8.txt
@@ -0,0 +1,100 @@
           1 +seed 11: success=True steps=8 time=21.0s ptime=0.1s nobs=0 phase=to_place
           2 +seed 9: success=True steps=16 time=32.4s ptime=0.3s nobs=1 phase=to_place
           3 +seed 7: success=True steps=17 time=30.1s ptime=0.3s nobs=2 phase=to_place
           4 +seed 1: success=True steps=19 time=25.4s ptime=0.2s nobs=1 phase=to_place
           5 +seed 6: success=True steps=20 time=25.3s ptime=0.3s nobs=1 phase=to_place
           6 +seed 10: success=True steps=16 time=20.6s ptime=0.2s nobs=2 phase=to_place
           7 +seed 3: success=True steps=20 time=35.7s ptime=0.3s nobs=2 phase=to_place
           8 +seed 12: success=True steps=16 time=16.4s ptime=0.3s nobs=1 phase=to_place
           9 +seed 14: success=True steps=8 time=13.7s ptime=0.0s nobs=0 phase=to_place
          10 +seed 8: success=True steps=26 time=47.2s ptime=0.4s nobs=2 phase=to_place
          11 +seed 0: success=True steps=26 time=36.8s ptime=0.4s nobs=2 phase=to_place
          12 +seed 2: success=True steps=25 time=37.6s ptime=0.5s nobs=2 phase=to_place
          13 +seed 5: success=True steps=37 time=70.5s ptime=0.7s nobs=2 phase=to_place
          14 +seed 4: success=True steps=41 time=58.3s ptime=0.6s nobs=2 phase=to_place
          15 +seed 15: success=True steps=16 time=37.2s ptime=0.2s nobs=2 phase=to_place
          16 +seed 16: success=True steps=17 time=33.5s ptime=0.2s nobs=1 phase=to_place
          17 +seed 21: success=True steps=9 time=19.2s ptime=0.1s nobs=0 phase=to_place
          18 +seed 19: success=True steps=15 time=27.1s ptime=0.3s nobs=1 phase=to_place
          19 +seed 13: success=True steps=23 time=49.0s ptime=0.3s nobs=2 phase=to_place
          20 +seed 23: success=True steps=8 time=16.5s ptime=0.1s nobs=0 phase=to_place
          21 +seed 18: success=True steps=18 time=37.8s ptime=0.3s nobs=2 phase=to_place
          22 +seed 24: success=True steps=10 time=16.5s ptime=0.1s nobs=1 phase=to_place
          23 +seed 17: success=True steps=24 time=49.4s ptime=0.4s nobs=2 phase=to_place
          24 +seed 22: success=True steps=17 time=43.8s ptime=0.3s nobs=2 phase=to_place
          25 +seed 29: success=True steps=7 time=19.3s ptime=0.1s nobs=2 phase=to_place
          26 +seed 27: success=True steps=10 time=29.5s ptime=0.1s nobs=0 phase=to_place
          27 +seed 30: success=True steps=10 time=27.9s ptime=0.1s nobs=0 phase=to_place
          28 +seed 34: success=True steps=9 time=15.8s ptime=0.1s nobs=0 phase=to_place
          29 +seed 26: success=True steps=20 time=45.6s ptime=0.3s nobs=2 phase=to_place
          30 +seed 25: success=True steps=20 time=48.0s ptime=0.3s nobs=1 phase=to_place
          31 +seed 20: success=True steps=28 time=69.2s ptime=0.3s nobs=2 phase=to_place
          32 +seed 31: success=True steps=17 time=30.4s ptime=0.4s nobs=1 phase=to_place
          33 +seed 35: success=True steps=10 time=19.5s ptime=0.1s nobs=0 phase=to_place
          34 +seed 37: success=True steps=9 time=17.4s ptime=0.2s nobs=0 phase=to_place
          35 +seed 36: success=True steps=15 time=28.4s ptime=0.2s nobs=1 phase=to_place
          36 +seed 38: success=True steps=8 time=21.0s ptime=0.1s nobs=0 phase=to_place
          37 +seed 32: success=True steps=25 time=52.9s ptime=0.4s nobs=2 phase=to_place
          38 +seed 28: success=True steps=30 time=66.7s ptime=0.4s nobs=1 phase=to_place
          39 +seed 33: success=True steps=24 time=56.4s ptime=0.4s nobs=2 phase=to_place
          40 +seed 42: success=True steps=10 time=24.4s ptime=0.1s nobs=0 phase=to_place
          41 +seed 40: success=True steps=15 time=41.9s ptime=0.2s nobs=1 phase=to_place
          42 +seed 47: success=True steps=7 time=16.7s ptime=0.1s nobs=0 phase=to_place
          43 +seed 48: success=True steps=7 time=13.6s ptime=0.1s nobs=0 phase=to_place
          44 +seed 49: success=True steps=9 time=16.8s ptime=0.1s nobs=0 phase=to_place
          45 +seed 41: success=True steps=21 time=47.5s ptime=0.4s nobs=1 phase=to_place
          46 +seed 39: success=True steps=26 time=59.4s ptime=0.3s nobs=2 phase=to_place
          47 +seed 43: success=True steps=18 time=43.5s ptime=0.2s nobs=1 phase=to_place
          48 +seed 46: success=True steps=15 time=34.4s ptime=0.2s nobs=1 phase=to_place
          49 +seed 54: success=True steps=9 time=18.7s ptime=0.1s nobs=0 phase=to_place
          50 +seed 44: success=True steps=19 time=56.3s ptime=0.3s nobs=2 phase=to_place
          51 +seed 51: success=True steps=16 time=36.4s ptime=0.2s nobs=1 phase=to_place
          52 +seed 57: success=True steps=8 time=18.5s ptime=0.1s nobs=0 phase=to_place
          53 +seed 58: success=True steps=10 time=21.9s ptime=0.1s nobs=1 phase=to_place
          54 +seed 50: success=True steps=27 time=57.3s ptime=0.4s nobs=2 phase=to_place
          55 +seed 56: success=True steps=16 time=33.5s ptime=0.3s nobs=1 phase=to_place
          56 +seed 60: success=True steps=9 time=16.8s ptime=0.0s nobs=0 phase=to_place
          57 +seed 52: success=True steps=25 time=54.6s ptime=0.7s nobs=2 phase=to_place
          58 +seed 45: success=True steps=36 time=89.6s ptime=0.6s nobs=2 phase=to_place
          59 +seed 62: success=True steps=15 time=29.7s ptime=0.2s nobs=1 phase=to_place
          60 +seed 61: success=True steps=18 time=39.4s ptime=0.2s nobs=1 phase=to_place
          61 +seed 55: success=True steps=29 time=65.4s ptime=0.4s nobs=2 phase=to_place
          62 +seed 68: success=True steps=8 time=11.1s ptime=0.1s nobs=1 phase=to_place
          63 +seed 53: success=True steps=33 time=75.4s ptime=0.4s nobs=2 phase=to_place
          64 +seed 63: success=True steps=18 time=35.1s ptime=0.3s nobs=1 phase=to_place
          65 +seed 59: success=True steps=27 time=54.7s ptime=0.5s nobs=2 phase=to_place
          66 +seed 65: success=True steps=11 time=24.7s ptime=0.1s nobs=0 phase=to_place
          67 +seed 64: success=True steps=17 time=37.8s ptime=0.2s nobs=1 phase=to_place
          68 +seed 69: success=True steps=8 time=17.7s ptime=0.1s nobs=0 phase=to_place
          69 +seed 74: success=True steps=7 time=17.3s ptime=0.1s nobs=0 phase=to_place
          70 +seed 66: success=True steps=22 time=48.7s ptime=0.3s nobs=2 phase=to_place
          71 +seed 67: success=True steps=26 time=52.8s ptime=0.4s nobs=2 phase=to_place
          72 +seed 70: success=True steps=20 time=40.5s ptime=0.3s nobs=1 phase=to_place
          73 +seed 77: success=True steps=8 time=19.5s ptime=0.1s nobs=0 phase=to_place
          74 +seed 79: success=True steps=7 time=12.4s ptime=0.1s nobs=0 phase=to_place
          75 +seed 81: success=True steps=9 time=13.2s ptime=0.1s nobs=0 phase=to_place
          76 +seed 75: success=True steps=17 time=36.0s ptime=0.2s nobs=1 phase=to_place
          77 +seed 73: success=True steps=25 time=51.0s ptime=0.4s nobs=2 phase=to_place
          78 +seed 76: success=True steps=19 time=37.4s ptime=0.3s nobs=1 phase=to_place
          79 +seed 72: success=True steps=27 time=61.5s ptime=0.3s nobs=2 phase=to_place
          80 +seed 71: success=True steps=35 time=68.7s ptime=0.5s nobs=2 phase=to_place
          81 +seed 80: success=True steps=22 time=37.8s ptime=0.3s nobs=2 phase=to_place
          82 +seed 83: success=True steps=17 time=30.1s ptime=0.2s nobs=2 phase=to_place
          83 +seed 78: success=True steps=34 time=48.3s ptime=0.3s nobs=2 phase=to_place
          84 +seed 84: success=True steps=24 time=29.7s ptime=0.2s nobs=1 phase=to_place
          85 +seed 88: success=True steps=17 time=20.9s ptime=0.2s nobs=1 phase=to_place
          86 +seed 85: success=True steps=23 time=43.3s ptime=0.5s nobs=2 phase=to_place
          87 +seed 87: success=True steps=24 time=35.1s ptime=0.3s nobs=1 phase=to_place
          88 +seed 86: success=True steps=23 time=40.4s ptime=0.3s nobs=2 phase=to_place
          89 +seed 90: success=True steps=15 time=20.7s ptime=0.4s nobs=1 phase=to_place
          90 +seed 82: success=True steps=42 time=60.6s ptime=0.5s nobs=2 phase=to_place
          91 +seed 94: success=True steps=9 time=19.0s ptime=0.1s nobs=0 phase=to_place
          92 +seed 91: success=True steps=18 time=29.1s ptime=0.5s nobs=2 phase=to_place
          93 +seed 92: success=True steps=16 time=25.7s ptime=0.2s nobs=1 phase=to_place
          94 +seed 89: success=True steps=26 time=38.9s ptime=0.5s nobs=2 phase=to_place
          95 +seed 97: success=True steps=9 time=6.8s ptime=0.1s nobs=0 phase=to_place
          96 +seed 95: success=True steps=16 time=17.6s ptime=0.2s nobs=1 phase=to_place
          97 +seed 98: success=True steps=24 time=5.3s ptime=0.4s nobs=1 phase=to_place
          98 +seed 96: success=True steps=28 time=17.7s ptime=0.5s nobs=2 phase=to_place
          99 +seed 93: success=True steps=38 time=29.5s ptime=0.4s nobs=2 phase=to_place
         100 +seed 99: success=True steps=31 time=6.2s ptime=0.4s nobs=2 phase=to_place
diff --git a/snap/approach.py b/snap/approach.py
index e410e51..83fd918 100644
--- a/snap/approach.py
+++ b/snap/approach.py
@@ -87,7 +87,7 @@ class GeneratedApproach:
   87     87  
   88     88      def _ik(self, xc, pt, R):
   89     89          if WB:
   90        -            return wb_ik2(xc, pt, R, iters=40)
          90 +            return wb_ik2(xc, pt, R, iters=40, k_null=0.05, bx_max=-0.09)
   91     91          q, ok = tool_ik(xc[3:], pt, R, tuple(xc[:3]), iters=40)
   92     92          return np.concatenate([xc[:3], q]), ok
   93     93  
diff --git a/snap/test_approach.py b/snap/test_approach.py
index d238650..afc13cc 100644
--- a/snap/test_approach.py
+++ b/snap/test_approach.py
@@ -12,22 +12,25 @@ def run(seed, verbose=False, max_steps=None, count=None):
   12     12      ms = max_steps or env.max_steps
   13     13      steps = 0
   14     14      term = False
          15 +    pt = 0.0
   15     16      for steps in range(1, ms + 1):
          17 +        t1 = time.time()
   16     18          a = ap.get_action(obs)
          19 +        pt += time.time() - t1
   17     20          obs, r, term, trunc, info = env.step(a)
   18     21          if term or trunc:
   19     22              break
   20     23      dt = time.time() - t0
   21     24      nobs = len([n for n in obs.get_object_names() if n.startswith('obstruction')])
   22     25      env.close()
   23        -    return term, steps, dt, nobs, ap.phase
          26 +    return term, steps, dt, nobs, ap.phase, pt
   24     27  
   25     28  if __name__ == '__main__':
   26     29      seeds = range(int(sys.argv[1]), int(sys.argv[2]))
   27     30      count = int(sys.argv[3]) if len(sys.argv) > 3 else None
   28     31      ok = 0
   29     32      for s in seeds:
   30        -        term, steps, dt, n, ph = run(s, count=count)
          33 +        term, steps, dt, n, ph, pt = run(s, count=count)
   31     34          ok += term
   32        -        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s nobs={n} phase={ph}', flush=True)
          35 +        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s ptime={pt:.1f}s nobs={n} phase={ph}', flush=True)
   33     36      print(f'{ok}/{len(seeds)}')
```

</details>

<a id="C022"></a>
### C022 · regression results

Commit `2997cec97d4a1758e5756b0f4775938ac533ca92`; parents: 37ffc6ed4efbdc9709aeff4d7c356d17a87d6aa2. Recorded author date: 2026-09-30T23:29:29+02:00.

File roles (automatic): policy, setup/other.

- [E1305](01_timeline.md#E1305): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C022_2997cec.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/r_c4.txt b/r_c4.txt
new file mode 100644
index 0000000..8b6a8ae
--- /dev/null
+++ b/r_c4.txt
@@ -0,0 +1,40 @@
           1 +seed 47: success=True steps=15 time=29.7s ptime=0.2s nobs=4 phase=to_place
           2 +seed 48: success=True steps=28 time=44.7s ptime=0.5s nobs=4 phase=to_place
           3 +seed 43: success=True steps=25 time=24.0s ptime=0.5s nobs=4 phase=to_place
           4 +seed 42: success=True steps=38 time=63.6s ptime=0.8s nobs=4 phase=to_place
           5 +seed 46: success=True steps=33 time=41.3s ptime=0.7s nobs=4 phase=to_place
           6 +seed 44: success=True steps=33 time=36.0s ptime=0.5s nobs=4 phase=to_place
           7 +seed 51: success=True steps=39 time=48.5s ptime=0.7s nobs=4 phase=to_place
           8 +seed 45: success=True steps=42 time=49.9s ptime=0.8s nobs=4 phase=to_place
           9 +seed 40: success=True steps=47 time=80.2s ptime=1.0s nobs=4 phase=to_place
          10 +seed 50: success=True steps=47 time=87.5s ptime=1.0s nobs=4 phase=to_place
          11 +seed 49: success=True steps=47 time=74.2s ptime=1.0s nobs=4 phase=to_place
          12 +seed 54: success=True steps=36 time=48.2s ptime=0.6s nobs=4 phase=to_place
          13 +seed 52: success=True steps=54 time=67.6s ptime=0.9s nobs=4 phase=to_place
          14 +seed 41: success=True steps=83 time=111.0s ptime=1.4s nobs=4 phase=to_place
          15 +seed 55: success=True steps=38 time=50.9s ptime=0.7s nobs=4 phase=to_place
          16 +seed 58: success=True steps=29 time=40.4s ptime=0.6s nobs=4 phase=to_place
          17 +seed 53: success=True steps=46 time=69.8s ptime=0.8s nobs=4 phase=to_place
          18 +seed 56: success=True steps=39 time=55.6s ptime=0.8s nobs=4 phase=to_place
          19 +seed 57: success=True steps=38 time=54.7s ptime=0.7s nobs=4 phase=to_place
          20 +seed 60: success=True steps=29 time=54.6s ptime=0.5s nobs=4 phase=to_place
          21 +seed 59: success=True steps=34 time=61.2s ptime=0.6s nobs=4 phase=to_place
          22 +seed 64: success=True steps=26 time=44.9s ptime=0.5s nobs=4 phase=to_place
          23 +seed 63: success=True steps=30 time=54.5s ptime=0.5s nobs=4 phase=to_place
          24 +seed 69: success=True steps=26 time=30.9s ptime=0.5s nobs=4 phase=to_place
          25 +seed 62: success=True steps=57 time=82.2s ptime=0.9s nobs=4 phase=to_place
          26 +seed 68: success=True steps=34 time=51.1s ptime=0.6s nobs=4 phase=to_place
          27 +seed 61: success=True steps=58 time=94.0s ptime=1.0s nobs=4 phase=to_place
          28 +seed 65: success=True steps=36 time=65.2s ptime=0.7s nobs=4 phase=to_place
          29 +seed 70: success=True steps=36 time=56.8s ptime=0.7s nobs=4 phase=to_place
          30 +seed 67: success=True steps=40 time=68.8s ptime=0.9s nobs=4 phase=to_place
          31 +seed 73: success=True steps=25 time=36.7s ptime=0.4s nobs=4 phase=to_place
          32 +seed 66: success=True steps=43 time=71.0s ptime=0.7s nobs=4 phase=to_place
          33 +seed 72: success=True steps=41 time=50.6s ptime=0.8s nobs=4 phase=to_place
          34 +seed 71: success=True steps=48 time=56.6s ptime=0.8s nobs=4 phase=to_place
          35 +seed 79: success=True steps=25 time=12.6s ptime=0.4s nobs=4 phase=to_place
          36 +seed 74: success=True steps=42 time=39.6s ptime=0.8s nobs=4 phase=to_place
          37 +seed 78: success=True steps=33 time=13.7s ptime=0.5s nobs=4 phase=to_place
          38 +seed 76: success=True steps=48 time=26.9s ptime=0.9s nobs=4 phase=to_place
          39 +seed 77: success=True steps=66 time=24.4s ptime=1.0s nobs=4 phase=to_place
          40 +seed 75: success=True steps=104 time=40.3s ptime=1.6s nobs=4 phase=to_place
diff --git a/r_c6.txt b/r_c6.txt
new file mode 100644
index 0000000..8a7bee2
--- /dev/null
+++ b/r_c6.txt
@@ -0,0 +1,30 @@
           1 +seed 10: success=True steps=45 time=39.9s ptime=0.9s nobs=6 phase=to_place
           2 +seed 2: success=True steps=35 time=24.4s ptime=0.9s nobs=6 phase=to_place
           3 +seed 3: success=True steps=42 time=64.3s ptime=0.8s nobs=6 phase=to_place
           4 +seed 9: success=True steps=50 time=65.4s ptime=1.0s nobs=6 phase=to_place
           5 +seed 8: success=True steps=60 time=71.8s ptime=1.2s nobs=6 phase=to_place
           6 +seed 11: success=True steps=63 time=55.4s ptime=1.6s nobs=6 phase=to_place
           7 +seed 7: success=True steps=54 time=54.7s ptime=1.3s nobs=6 phase=to_place
           8 +seed 0: success=True steps=71 time=76.0s ptime=1.2s nobs=6 phase=to_place
           9 +seed 4: success=True steps=68 time=78.1s ptime=1.4s nobs=6 phase=to_place
          10 +seed 6: success=True steps=69 time=86.9s ptime=1.2s nobs=6 phase=to_place
          11 +seed 1: success=True steps=67 time=105.6s ptime=1.5s nobs=6 phase=to_place
          12 +seed 14: success=True steps=38 time=54.6s ptime=0.8s nobs=6 phase=to_place
          13 +seed 5: success=True steps=110 time=136.4s ptime=1.6s nobs=6 phase=to_place
          14 +seed 12: success=True steps=55 time=83.1s ptime=1.1s nobs=6 phase=to_place
          15 +seed 13: success=True steps=63 time=92.2s ptime=1.4s nobs=6 phase=to_place
          16 +seed 16: success=True steps=44 time=72.5s ptime=1.0s nobs=6 phase=to_place
          17 +seed 19: success=True steps=47 time=67.1s ptime=1.1s nobs=6 phase=to_place
          18 +seed 17: success=True steps=49 time=67.5s ptime=1.1s nobs=6 phase=to_place
          19 +seed 18: success=True steps=49 time=69.5s ptime=1.0s nobs=6 phase=to_place
          20 +seed 15: success=True steps=60 time=91.4s ptime=1.3s nobs=6 phase=to_place
          21 +seed 20: success=True steps=49 time=68.9s ptime=1.1s nobs=6 phase=to_place
          22 +seed 22: success=True steps=53 time=63.2s ptime=1.1s nobs=6 phase=to_place
          23 +seed 25: success=True steps=32 time=36.4s ptime=0.6s nobs=6 phase=to_place
          24 +seed 21: success=True steps=68 time=73.3s ptime=1.0s nobs=6 phase=to_place
          25 +seed 24: success=True steps=47 time=45.5s ptime=1.1s nobs=6 phase=to_place
          26 +seed 23: success=True steps=63 time=61.4s ptime=1.2s nobs=6 phase=to_place
          27 +seed 27: success=True steps=35 time=22.1s ptime=0.7s nobs=6 phase=to_place
          28 +seed 26: success=True steps=38 time=26.7s ptime=0.8s nobs=6 phase=to_place
          29 +seed 29: success=True steps=37 time=12.6s ptime=0.5s nobs=6 phase=to_place
          30 +seed 28: success=True steps=49 time=14.3s ptime=1.1s nobs=6 phase=to_place
diff --git a/r_def.txt b/r_def.txt
new file mode 100644
index 0000000..35ca65a
--- /dev/null
+++ b/r_def.txt
@@ -0,0 +1,100 @@
           1 +seed 11: success=True steps=8 time=20.8s ptime=0.1s nobs=0 phase=to_place
           2 +seed 7: success=True steps=17 time=35.4s ptime=0.2s nobs=2 phase=to_place
           3 +seed 10: success=True steps=16 time=21.3s ptime=0.2s nobs=2 phase=to_place
           4 +seed 1: success=True steps=19 time=29.4s ptime=0.3s nobs=1 phase=to_place
           5 +seed 2: success=True steps=25 time=47.3s ptime=0.5s nobs=2 phase=to_place
           6 +seed 9: success=True steps=16 time=20.9s ptime=0.2s nobs=1 phase=to_place
           7 +seed 6: success=True steps=20 time=30.4s ptime=0.3s nobs=1 phase=to_place
           8 +seed 3: success=True steps=20 time=27.9s ptime=0.2s nobs=2 phase=to_place
           9 +seed 14: success=True steps=8 time=12.6s ptime=0.1s nobs=0 phase=to_place
          10 +seed 0: success=True steps=26 time=48.9s ptime=0.3s nobs=2 phase=to_place
          11 +seed 12: success=True steps=16 time=32.0s ptime=0.2s nobs=1 phase=to_place
          12 +seed 4: success=True steps=41 time=64.6s ptime=0.6s nobs=2 phase=to_place
          13 +seed 8: success=True steps=26 time=52.9s ptime=0.5s nobs=2 phase=to_place
          14 +seed 15: success=True steps=16 time=31.2s ptime=0.2s nobs=2 phase=to_place
          15 +seed 5: success=True steps=37 time=65.7s ptime=0.4s nobs=2 phase=to_place
          16 +seed 21: success=True steps=9 time=18.4s ptime=0.1s nobs=0 phase=to_place
          17 +seed 13: success=True steps=23 time=47.0s ptime=0.4s nobs=2 phase=to_place
          18 +seed 16: success=True steps=17 time=31.8s ptime=0.2s nobs=1 phase=to_place
          19 +seed 19: success=True steps=15 time=27.0s ptime=0.2s nobs=1 phase=to_place
          20 +seed 23: success=True steps=8 time=13.7s ptime=0.1s nobs=0 phase=to_place
          21 +seed 24: success=True steps=10 time=19.7s ptime=0.1s nobs=1 phase=to_place
          22 +seed 18: success=True steps=18 time=41.5s ptime=0.3s nobs=2 phase=to_place
          23 +seed 22: success=True steps=17 time=33.8s ptime=0.3s nobs=2 phase=to_place
          24 +seed 17: success=True steps=24 time=58.0s ptime=0.5s nobs=2 phase=to_place
          25 +seed 29: success=True steps=7 time=19.0s ptime=0.1s nobs=2 phase=to_place
          26 +seed 27: success=True steps=10 time=27.2s ptime=0.1s nobs=0 phase=to_place
          27 +seed 30: success=True steps=10 time=24.8s ptime=0.1s nobs=0 phase=to_place
          28 +seed 34: success=True steps=9 time=16.9s ptime=0.1s nobs=0 phase=to_place
          29 +seed 20: success=True steps=28 time=69.7s ptime=0.4s nobs=2 phase=to_place
          30 +seed 25: success=True steps=20 time=49.2s ptime=0.2s nobs=1 phase=to_place
          31 +seed 35: success=True steps=10 time=19.6s ptime=0.1s nobs=0 phase=to_place
          32 +seed 26: success=True steps=20 time=54.1s ptime=0.3s nobs=2 phase=to_place
          33 +seed 37: success=True steps=9 time=22.3s ptime=0.1s nobs=0 phase=to_place
          34 +seed 31: success=True steps=17 time=47.7s ptime=0.2s nobs=1 phase=to_place
          35 +seed 36: success=True steps=15 time=32.5s ptime=0.2s nobs=1 phase=to_place
          36 +seed 38: success=True steps=8 time=23.5s ptime=0.1s nobs=0 phase=to_place
          37 +seed 28: success=True steps=30 time=66.0s ptime=0.4s nobs=1 phase=to_place
          38 +seed 33: success=True steps=24 time=59.0s ptime=0.4s nobs=2 phase=to_place
          39 +seed 32: success=True steps=25 time=62.5s ptime=0.5s nobs=2 phase=to_place
          40 +seed 42: success=True steps=10 time=21.9s ptime=0.2s nobs=0 phase=to_place
          41 +seed 40: success=True steps=15 time=34.6s ptime=0.3s nobs=1 phase=to_place
          42 +seed 47: success=True steps=7 time=16.0s ptime=0.1s nobs=0 phase=to_place
          43 +seed 48: success=True steps=7 time=16.4s ptime=0.0s nobs=0 phase=to_place
          44 +seed 43: success=True steps=18 time=37.0s ptime=0.2s nobs=1 phase=to_place
          45 +seed 44: success=True steps=19 time=37.6s ptime=0.2s nobs=2 phase=to_place
          46 +seed 41: success=True steps=21 time=50.3s ptime=0.3s nobs=1 phase=to_place
          47 +seed 49: success=True steps=9 time=21.4s ptime=0.1s nobs=0 phase=to_place
          48 +seed 39: success=True steps=26 time=59.9s ptime=0.4s nobs=2 phase=to_place
          49 +seed 46: success=True steps=15 time=34.7s ptime=0.2s nobs=1 phase=to_place
          50 +seed 54: success=True steps=9 time=22.0s ptime=0.1s nobs=0 phase=to_place
          51 +seed 51: success=True steps=16 time=34.5s ptime=0.2s nobs=1 phase=to_place
          52 +seed 57: success=True steps=8 time=16.3s ptime=0.1s nobs=0 phase=to_place
          53 +seed 58: success=True steps=10 time=20.7s ptime=0.1s nobs=1 phase=to_place
          54 +seed 60: success=True steps=9 time=17.6s ptime=0.0s nobs=0 phase=to_place
          55 +seed 50: success=True steps=27 time=60.7s ptime=0.5s nobs=2 phase=to_place
          56 +seed 56: success=True steps=16 time=39.7s ptime=0.2s nobs=1 phase=to_place
          57 +seed 52: success=True steps=25 time=54.2s ptime=0.3s nobs=2 phase=to_place
          58 +seed 45: success=True steps=36 time=89.4s ptime=0.5s nobs=2 phase=to_place
          59 +seed 62: success=True steps=15 time=23.8s ptime=0.2s nobs=1 phase=to_place
          60 +seed 61: success=True steps=18 time=30.0s ptime=0.3s nobs=1 phase=to_place
          61 +seed 65: success=True steps=11 time=14.8s ptime=0.1s nobs=0 phase=to_place
          62 +seed 55: success=True steps=29 time=59.6s ptime=0.4s nobs=2 phase=to_place
          63 +seed 53: success=True steps=33 time=69.5s ptime=0.4s nobs=2 phase=to_place
          64 +seed 64: success=True steps=17 time=27.4s ptime=0.3s nobs=1 phase=to_place
          65 +seed 63: success=True steps=18 time=31.2s ptime=0.3s nobs=1 phase=to_place
          66 +seed 59: success=True steps=27 time=52.0s ptime=0.4s nobs=2 phase=to_place
          67 +seed 68: success=True steps=8 time=10.5s ptime=0.1s nobs=1 phase=to_place
          68 +seed 69: success=True steps=8 time=12.6s ptime=0.1s nobs=0 phase=to_place
          69 +seed 66: success=True steps=22 time=41.5s ptime=0.3s nobs=2 phase=to_place
          70 +seed 74: success=True steps=7 time=20.6s ptime=0.1s nobs=0 phase=to_place
          71 +seed 77: success=True steps=8 time=11.3s ptime=0.1s nobs=0 phase=to_place
          72 +seed 67: success=True steps=26 time=47.7s ptime=0.4s nobs=2 phase=to_place
          73 +seed 79: success=True steps=7 time=8.8s ptime=0.1s nobs=0 phase=to_place
          74 +seed 70: success=True steps=20 time=44.4s ptime=0.4s nobs=1 phase=to_place
          75 +seed 75: success=True steps=17 time=34.9s ptime=0.2s nobs=1 phase=to_place
          76 +seed 81: success=True steps=9 time=14.0s ptime=0.1s nobs=0 phase=to_place
          77 +seed 76: success=True steps=19 time=37.0s ptime=0.3s nobs=1 phase=to_place
          78 +seed 73: success=True steps=25 time=54.1s ptime=0.3s nobs=2 phase=to_place
          79 +seed 80: success=True steps=22 time=35.7s ptime=0.4s nobs=2 phase=to_place
          80 +seed 72: success=True steps=27 time=63.4s ptime=0.5s nobs=2 phase=to_place
          81 +seed 71: success=True steps=35 time=67.5s ptime=0.6s nobs=2 phase=to_place
          82 +seed 83: success=True steps=17 time=30.4s ptime=0.2s nobs=2 phase=to_place
          83 +seed 78: success=True steps=34 time=51.2s ptime=0.4s nobs=2 phase=to_place
          84 +seed 84: success=True steps=24 time=35.0s ptime=0.2s nobs=1 phase=to_place
          85 +seed 88: success=True steps=17 time=26.1s ptime=0.3s nobs=1 phase=to_place
          86 +seed 85: success=True steps=23 time=41.3s ptime=0.3s nobs=2 phase=to_place
          87 +seed 87: success=True steps=24 time=35.6s ptime=0.3s nobs=1 phase=to_place
          88 +seed 90: success=True steps=15 time=28.5s ptime=0.2s nobs=1 phase=to_place
          89 +seed 86: success=True steps=23 time=45.2s ptime=0.4s nobs=2 phase=to_place
          90 +seed 94: success=True steps=9 time=18.7s ptime=0.1s nobs=0 phase=to_place
          91 +seed 92: success=True steps=16 time=25.7s ptime=0.2s nobs=1 phase=to_place
          92 +seed 91: success=True steps=18 time=33.6s ptime=0.4s nobs=2 phase=to_place
          93 +seed 82: success=True steps=42 time=66.9s ptime=0.5s nobs=2 phase=to_place
          94 +seed 97: success=True steps=9 time=9.6s ptime=0.1s nobs=0 phase=to_place
          95 +seed 95: success=True steps=16 time=20.0s ptime=0.3s nobs=1 phase=to_place
          96 +seed 89: success=True steps=26 time=43.3s ptime=0.4s nobs=2 phase=to_place
          97 +seed 98: success=True steps=24 time=5.3s ptime=0.2s nobs=1 phase=to_place
          98 +seed 93: success=True steps=38 time=30.4s ptime=0.4s nobs=2 phase=to_place
          99 +seed 96: success=True steps=28 time=17.4s ptime=0.5s nobs=2 phase=to_place
         100 +seed 99: success=True steps=31 time=6.6s ptime=0.5s nobs=2 phase=to_place
diff --git a/snap/approach.py b/snap/approach.py
index 83fd918..62fd63f 100644
--- a/snap/approach.py
+++ b/snap/approach.py
@@ -131,6 +131,7 @@ class GeneratedApproach:
  131    131          self.fails = {}
  132    132          self.blk_moves = {}
  133    133          self.stuck = 0
         134 +        self.micro = 0
  134    135          self.descent_len = 0
  135    136          self.release_tries = 0
  136    137          self.grasp_attempt = 0
@@ -469,10 +470,19 @@ class GeneratedApproach:
  469    470          if ph == 'to_place':
  470    471              if self._grasped_name(state) is None:
  471    472                  return self._on_released(state)
         473 +            if self.micro > 0:
         474 +                a = self._micro_up(state)
         475 +                if a is not None:
         476 +                    return a
  472    477              if self.blocked:
  473    478                  self.stuck += 1
  474    479                  if len(self.qpath) <= self.descent_len:
  475    480                      self.qpath = []
         481 +                elif self.stuck >= 2 and self.micro == 0 and self._held_low(state):
         482 +                    self.micro = 1
         483 +                    a = self._micro_up(state)
         484 +                    if a is not None:
         485 +                        return a
  476    486                  elif self.stuck >= 3:
  477    487                      self._plan_place(state, replan=True)
  478    488              a = self._track(state)
@@ -535,6 +545,35 @@ class GeneratedApproach:
  535    545                      self.tasks.insert(0, (n, 'clear'))
  536    546          self._start_task(state)
  537    547  
         548 +    def _held_low(self, state):
         549 +        g = self._grasped_name(state)
         550 +        if g is None:
         551 +            return False
         552 +        p, _, h = self._pose(state, g)
         553 +        top = self.table_z
         554 +        for n in self.names:
         555 +            if n == g:
         556 +                continue
         557 +            c, hh, b, t = self._box(state, n)
         558 +            if np.linalg.norm(c[:2] - p[:2]) < 0.1:
         559 +                top = max(top, t)
         560 +        return p[2] - h[2] < top + 0.01
         561 +
         562 +    def _micro_up(self, state):
         563 +        # tiny straight-up steps: large moves get rejected when the held object is wedged
         564 +        if (self.micro > 1 and self.blocked) or self.micro > 60 or not self._held_low(state):
         565 +            self.micro = 0
         566 +            self._plan_place(state, replan=False)
         567 +            return None
         568 +        self.micro += 1
         569 +        x = self._x(state)
         570 +        T = wb_fk(x)
         571 +        yaw = np.arctan2(T[1, 0], T[0, 0])
         572 +        xn, ok = self._ik(x, T[:3, 3] + np.array([0, 0, 0.0045]), down_R(yaw))
         573 +        a = self._noop()
         574 +        a[:10] = np.clip(xn - x, -STEP, STEP)
         575 +        return a
         576 +
  538    577      def _plan_place(self, state, replan=False):
  539    578          name = self.cur_obj
  540    579          p, qo, h = self._pose(state, name)
```

</details>

<a id="C023"></a>
### C023 · Regression results for counts 3/5/8

Commit `7d554d68167a01e575bce0334b97cac55d4b05e3`; parents: 2997cec97d4a1758e5756b0f4775938ac533ca92. Recorded author date: 2026-09-30T23:39:26+02:00.

File roles (automatic): setup/other.

- [E1336](01_timeline.md#E1336): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C023_7d554d6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/r_c3.txt b/r_c3.txt
new file mode 100644
index 0000000..f30a527
--- /dev/null
+++ b/r_c3.txt
@@ -0,0 +1,30 @@
           1 +seed 106: success=True steps=29 time=38.1s ptime=0.6s nobs=3 phase=to_place
           2 +seed 105: success=True steps=34 time=49.5s ptime=0.6s nobs=3 phase=to_place
           3 +seed 102: success=True steps=35 time=49.7s ptime=0.6s nobs=3 phase=to_place
           4 +seed 107: success=True steps=32 time=44.1s ptime=0.4s nobs=3 phase=to_place
           5 +seed 100: success=True steps=35 time=59.6s ptime=0.6s nobs=3 phase=to_place
           6 +seed 103: success=True steps=38 time=60.4s ptime=0.5s nobs=3 phase=to_place
           7 +seed 101: success=True steps=36 time=46.1s ptime=0.6s nobs=3 phase=to_place
           8 +seed 110: success=True steps=40 time=55.9s ptime=0.6s nobs=3 phase=to_place
           9 +seed 109: success=True steps=37 time=44.5s ptime=0.6s nobs=3 phase=to_place
          10 +seed 111: success=True steps=58 time=60.6s ptime=0.8s nobs=3 phase=to_place
          11 +seed 104: success=True steps=46 time=52.1s ptime=0.7s nobs=3 phase=to_place
          12 +seed 116: success=True steps=18 time=30.2s ptime=0.4s nobs=3 phase=to_place
          13 +seed 112: success=True steps=27 time=50.3s ptime=0.6s nobs=3 phase=to_place
          14 +seed 108: success=True steps=60 time=88.3s ptime=0.8s nobs=3 phase=to_place
          15 +seed 113: success=True steps=28 time=52.0s ptime=0.5s nobs=3 phase=to_place
          16 +seed 114: success=True steps=29 time=54.1s ptime=0.4s nobs=3 phase=to_place
          17 +seed 117: success=True steps=33 time=53.2s ptime=0.6s nobs=3 phase=to_place
          18 +seed 115: success=True steps=43 time=65.9s ptime=0.7s nobs=3 phase=to_place
          19 +seed 121: success=True steps=24 time=37.6s ptime=0.4s nobs=3 phase=to_place
          20 +seed 120: success=True steps=30 time=42.7s ptime=0.5s nobs=3 phase=to_place
          21 +seed 118: success=True steps=41 time=58.5s ptime=0.6s nobs=3 phase=to_place
          22 +seed 119: success=True steps=38 time=55.6s ptime=0.9s nobs=3 phase=to_place
          23 +seed 124: success=True steps=24 time=29.2s ptime=0.5s nobs=3 phase=to_place
          24 +seed 127: success=True steps=18 time=18.2s ptime=0.5s nobs=3 phase=to_place
          25 +seed 123: success=True steps=36 time=38.9s ptime=0.7s nobs=3 phase=to_place
          26 +seed 122: success=True steps=45 time=44.9s ptime=1.0s nobs=3 phase=to_place
          27 +seed 129: success=True steps=24 time=7.8s ptime=0.2s nobs=3 phase=to_place
          28 +seed 126: success=True steps=35 time=26.1s ptime=0.7s nobs=3 phase=to_place
          29 +seed 125: success=True steps=52 time=32.0s ptime=1.0s nobs=3 phase=to_place
          30 +seed 128: success=True steps=43 time=16.4s ptime=0.8s nobs=3 phase=to_place
diff --git a/r_c5.txt b/r_c5.txt
new file mode 100644
index 0000000..d4955ad
--- /dev/null
+++ b/r_c5.txt
@@ -0,0 +1,30 @@
           1 +seed 109: success=True steps=37 time=43.4s ptime=0.7s nobs=5 phase=to_place
           2 +seed 101: success=True steps=44 time=69.5s ptime=0.9s nobs=5 phase=to_place
           3 +seed 106: success=True steps=46 time=71.9s ptime=1.1s nobs=5 phase=to_place
           4 +seed 100: success=True steps=48 time=68.4s ptime=1.1s nobs=5 phase=to_place
           5 +seed 103: success=True steps=45 time=62.7s ptime=0.8s nobs=5 phase=to_place
           6 +seed 110: success=True steps=46 time=47.4s ptime=0.8s nobs=5 phase=to_place
           7 +seed 104: success=True steps=61 time=85.4s ptime=1.1s nobs=5 phase=to_place
           8 +seed 102: success=True steps=47 time=76.4s ptime=0.9s nobs=5 phase=to_place
           9 +seed 107: success=True steps=50 time=74.7s ptime=0.9s nobs=5 phase=to_place
          10 +seed 105: success=True steps=53 time=73.2s ptime=1.1s nobs=5 phase=to_place
          11 +seed 108: success=True steps=64 time=81.5s ptime=1.1s nobs=5 phase=to_place
          12 +seed 113: success=True steps=28 time=52.3s ptime=0.5s nobs=5 phase=to_place
          13 +seed 116: success=True steps=27 time=40.3s ptime=0.5s nobs=5 phase=to_place
          14 +seed 111: success=True steps=89 time=100.6s ptime=1.6s nobs=5 phase=to_place
          15 +seed 117: success=True steps=33 time=48.0s ptime=0.8s nobs=5 phase=to_place
          16 +seed 114: success=True steps=36 time=64.6s ptime=0.7s nobs=5 phase=to_place
          17 +seed 112: success=True steps=49 time=84.5s ptime=0.9s nobs=5 phase=to_place
          18 +seed 120: success=True steps=36 time=50.5s ptime=0.8s nobs=5 phase=to_place
          19 +seed 115: success=True steps=51 time=81.6s ptime=1.0s nobs=5 phase=to_place
          20 +seed 121: success=True steps=43 time=59.2s ptime=0.7s nobs=5 phase=to_place
          21 +seed 118: success=True steps=55 time=71.4s ptime=1.2s nobs=5 phase=to_place
          22 +seed 122: success=True steps=52 time=57.4s ptime=0.9s nobs=5 phase=to_place
          23 +seed 123: success=True steps=42 time=44.3s ptime=0.9s nobs=5 phase=to_place
          24 +seed 119: success=True steps=80 time=78.1s ptime=1.4s nobs=5 phase=to_place
          25 +seed 127: success=True steps=38 time=29.6s ptime=0.7s nobs=5 phase=to_place
          26 +seed 124: success=True steps=48 time=43.0s ptime=1.0s nobs=5 phase=to_place
          27 +seed 126: success=True steps=48 time=33.1s ptime=0.7s nobs=5 phase=to_place
          28 +seed 129: success=True steps=37 time=17.2s ptime=0.7s nobs=5 phase=to_place
          29 +seed 128: success=True steps=51 time=25.3s ptime=1.0s nobs=5 phase=to_place
          30 +seed 125: success=True steps=73 time=37.7s ptime=1.5s nobs=5 phase=to_place
diff --git a/r_c8.txt b/r_c8.txt
new file mode 100644
index 0000000..7539619
--- /dev/null
+++ b/r_c8.txt
@@ -0,0 +1,20 @@
           1 +seed 106: success=True steps=51 time=43.6s ptime=1.3s nobs=8 phase=to_place
           2 +seed 102: success=True steps=54 time=64.4s ptime=1.3s nobs=8 phase=to_place
           3 +seed 100: success=True steps=66 time=52.6s ptime=1.7s nobs=8 phase=to_place
           4 +seed 109: success=True steps=61 time=73.0s ptime=1.3s nobs=8 phase=to_place
           5 +seed 107: success=True steps=73 time=65.4s ptime=1.6s nobs=8 phase=to_place
           6 +seed 111: success=True steps=89 time=110.7s ptime=2.0s nobs=8 phase=to_place
           7 +seed 108: success=True steps=76 time=72.8s ptime=2.1s nobs=8 phase=to_place
           8 +seed 101: success=True steps=100 time=95.4s ptime=2.3s nobs=8 phase=to_place
           9 +seed 105: success=True steps=77 time=86.6s ptime=2.0s nobs=8 phase=to_place
          10 +seed 104: success=True steps=81 time=123.2s ptime=2.1s nobs=8 phase=to_place
          11 +seed 103: success=True steps=89 time=114.0s ptime=2.0s nobs=8 phase=to_place
          12 +seed 110: success=True steps=95 time=112.0s ptime=1.8s nobs=8 phase=to_place
          13 +seed 114: success=True steps=40 time=36.8s ptime=1.0s nobs=8 phase=to_place
          14 +seed 112: success=True steps=66 time=65.6s ptime=1.6s nobs=8 phase=to_place
          15 +seed 115: success=True steps=56 time=43.0s ptime=1.4s nobs=8 phase=to_place
          16 +seed 116: success=True steps=55 time=35.9s ptime=1.0s nobs=8 phase=to_place
          17 +seed 113: success=True steps=77 time=60.6s ptime=1.6s nobs=8 phase=to_place
          18 +seed 117: success=True steps=67 time=29.1s ptime=1.6s nobs=8 phase=to_place
          19 +seed 118: success=True steps=102 time=31.3s ptime=2.7s nobs=8 phase=to_place
          20 +seed 119: success=True steps=103 time=27.5s ptime=2.3s nobs=8 phase=to_place
```

</details>

