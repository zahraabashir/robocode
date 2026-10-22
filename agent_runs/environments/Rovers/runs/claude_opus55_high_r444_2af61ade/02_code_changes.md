# Rovers · claude-opus-5-5 · replicate 444: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `04e3ac5` | initial sandbox setup | .claude/settings.json, .claude/validate_sandbox.py, .gitignore, CLAUDE.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `54dccfe` | notes and probes | NOTES.md, dump.py, probe1.py, probe2.py | [E0047](01_timeline.md#E0047) |
| [C003](#C003) · `daa839b` | collision notes | NOTES.md, probe_col_an.py, probe_col_arena.py, probe_col_bounds.py, probe_col_dump.py, probe_col_f_0.3927_0.txt, probe_col_f_0.3927_180.txt, probe_col_f_0.3927_270.txt, probe_col_… | [E0450](01_timeline.md#E0450) |
| [C004](#C004) · `db1ff27` | notes | NOTES.md, probe_send_r.py, probe_send_s.py, probe_send_t.py, probe_send_u.py, probe_vis_grid.py, probe_vis_h1.py, probe_vis_h2.py, probe_vis_i.py, probe_vis_j.py, probe_vis_j_-0.3… | [E0047](01_timeline.md#E0047), [E0450](01_timeline.md#E0450), [E0524](01_timeline.md#E0524), [E0611](01_timeline.md#E0611), [E1141](01_timeline.md#E1141), [E1363](01_timeline.md#E1363), [E1464](01_timeline.md#E1464) |
| [C005](#C005) · `948d71b` | notes | NOTES.md, probe_vis_fit3.py, probe_vis_k.py, probe_vis_l.py, probe_vis_m.py, probe_vis_n.py, probe_vis_n_-1.85_0.75.json, probe_vis_n_-2.0_0.75.json, probe_vis_n_-2.1_0.75.json, p… | [E0047](01_timeline.md#E0047), [E0450](01_timeline.md#E0450), [E0524](01_timeline.md#E0524), [E0611](01_timeline.md#E0611), [E1141](01_timeline.md#E1141), [E1363](01_timeline.md#E1363), [E1464](01_timeline.md#E1464) |
| [C006](#C006) · `d4c816c` | v1 staged grid planner | approach.py, test_approach.py | [E0619](01_timeline.md#E0619) |
| [C007](#C007) · `ea4a1c5` | fix sample region ambiguity; stricter deviation checks | approach.py, dbg.py, dbg2.py, dbg3.py | [E0644](01_timeline.md#E0644) |
| [C008](#C008) · `d4dd7ed` | liberal competitor test for image nearest rule | approach.py | [E0657](01_timeline.md#E0657) |
| [C009](#C009) · `b9fe270` | time-aware send stage vs other rover trajectory | approach.py, dbg4.py | [E0666](01_timeline.md#E0666) |
| [C010](#C010) · `64756f6` | lander range from cam too; bigger rover occluder | approach.py | [E0740](01_timeline.md#E0740) |
| [C011](#C011) · `24ccf4a` | backtrack with waiting; timed send stage | approach.py, dbg5.py, probe_occ_fit.py, probe_occ_lib.py, probe_occ_run1.out, probe_occ_run1.py, probe_occ_scan.py, probe_occ_scan2.py, probe_occ_scan3.py, probe_occ_t1.py, probe_… | [E0802](01_timeline.md#E0802) |
| [C012](#C012) · `ab01758` | top-K realized assignment selection; timed send w/o static occluder | approach.py, probe_occ_run1.out, probe_occ_run2.out, probe_occ_run2.py, probe_occ_run3.out, probe_occ_run3.py, probe_occ_run4.out, probe_occ_run4.py | [E0846](01_timeline.md#E0846) |
| [C013](#C013) · `63fca65` | tighter margins | approach.py, probe_occ_pt.out, probe_occ_pt.py, probe_occ_run4.out, probe_occ_run4.py, probe_occ_run4b.out, test_approach.py | [E0860](01_timeline.md#E0860), [E1045](01_timeline.md#E1045) |
| [C014](#C014) · `04610bd` | rover occluder 0.26 | approach.py, res_tight.json | [E0869](01_timeline.md#E0869) |
| [C015](#C015) · `bd3aae9` | timed send checks other rover at t-1 and t (sequential rover update) | approach.py, dbg6.py, dbg7.py, res_occ26.json | [E0892](01_timeline.md#E0892) |
| [C016](#C016) · `e1ead97` | home region radius 0.22 | approach.py, bound.py, res_seq.json | [E0929](01_timeline.md#E0929) |
| [C017](#C017) · `3134153` | imaging heading -pi/2 with rotation schedule | approach.py, approach_fine.py, bound2.py, res_fine.json, res_home.json, test_alt.py | [E0969](01_timeline.md#E0969) |
| [C018](#C018) · `99376f5` | conservative lander footprint; blacklist rejected move targets | approach.py, prof.out, res_rot.json, timeit_.py | [E0988](01_timeline.md#E0988) |
| [C019](#C019) · `92ea16d` | choose imaging heading per rover/task-set among {-pi/2, home} | approach.py, approach_v3.py, big_v3.log, res_rot2.json | [E1014](01_timeline.md#E1014) |
| [C020](#C020) · `f913fe9` | single imaging heading (faster) | approach.py, res_rot3.json | [E1021](01_timeline.md#E1021) |
| [C021](#C021) · `c6213be` | rotate only 1.2 rad (3 steps) toward -pi/2 for imaging | approach.py | [E1032](01_timeline.md#E1032) |
| [C022](#C022) · `711a3f4` | full rotation | approach.py, big_v3.log, res_rot4.json, res_v3_big.json | [E1041](01_timeline.md#E1041) |
| [C023](#C023) · `f673e87` | tighter margins: obj 1.993, lander 3.995, sample 0.246, home 0.235 | approach.py, approach_m.py, res_m.json | [E1045](01_timeline.md#E1045) |
| [C024](#C024) · `aaffb63` | fine-grid refinement of chosen stage sequences | approach.py, approach_fine.py, res_fine2.json | [E1074](01_timeline.md#E1074) |
| [C025](#C025) · `dbc525a` | fine planner cache; time guards | approach.py, prof.out, res_ref.json | [E1085](01_timeline.md#E1085) |
| [C026](#C026) · `52ce3d1` | notes | NOTES.md, prof.out, res_ref400.json, test_cnt.py | [E0047](01_timeline.md#E0047), [E0450](01_timeline.md#E0450), [E0524](01_timeline.md#E0524), [E0611](01_timeline.md#E0611), [E1141](01_timeline.md#E1141), [E1363](01_timeline.md#E1363), [E1464](01_timeline.md#E1464) |
| [C027](#C027) · `52d4e12` | parse state via object names | approach.py, dbg8.py, dbg9.py | [E1162](01_timeline.md#E1162) |
| [C028](#C028) · `fc2cc20` | relaxed fallback when no plan | approach.py, res_n.json | [E1169](01_timeline.md#E1169) |
| [C029](#C029) · `8a6f698` | Model sample markers as lander occluders (seed 549 send failure) | approach.py, dbg10.py, probe549.py, res_final.json, res_n2.json | [E1239](01_timeline.md#E1239) |
| [C030](#C030) · `275ec8a` | Blacklist positions where send/img/cal failed, to avoid replan loops | approach.py | [E1253](01_timeline.md#E1253) |
| [C031](#C031) · `9ade333` | results 400-600 after sample-occluder fix | res_b.json | [E1294](01_timeline.md#E1294) |
| [C032](#C032) · `d7dabcd` | notes | NOTES.md, cnt_near.py, probe_occ.py, res_c.json | [E0047](01_timeline.md#E0047), [E0450](01_timeline.md#E0450), [E0524](01_timeline.md#E0524), [E0611](01_timeline.md#E0611), [E1141](01_timeline.md#E1141), [E1363](01_timeline.md#E1363), [E1464](01_timeline.md#E1464) |
| [C033](#C033) · `f24e3a2` | Experiment notes: less-conservative pillars not adopted; 4-obj test results | NOTES.md, approach_lc.py, res_lc.json, test_cnt.py | [E1464](01_timeline.md#E1464) |
| [C034](#C034) · `1767f02` | Regression check seeds 0-200: 200/200, mean 20.74 | res_final0.json | [E1513](01_timeline.md#E1513) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `04e3ac53f49206001c12b6fd34ec1844072db9b2`; parents: none (initial snapshot). Recorded author date: 2026-10-01T10:41:07+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C001_04e3ac5.diff)

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
index 0000000..b7fe097
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "e07494eee625e16cc56e211934a1b919", "observation_space": {"type": "ObjectCentric", "types": [{"name": "lander", "parent": null, "features": ["x", "y", "z"]}, {"name": "objective", "parent": null, "features": ["x", "y", "z", "have_image_rover0", "have_image_rover1", "received_image"]}, {"name": "obstacle", "parent": null, "features": ["x", "y", "z", "half_x", "half_y", "half_z"]}, {"name": "rover", "parent": null, "features": ["x", "y", "theta", "store_full", "calibrated", "at_home"]}, {"name": "sample", "parent": null, "features": ["x", "y", "z", "is_soil", "analyzed_rover0", "analyzed_rover1", "received_analysis"]}]}, "action_space": {"type": "Box", "shape": [8], "low": [-0.20000000298023224, -0.20000000298023224, -0.4000000059604645, -1.0, -0.20000000298023224, -0.20000000298023224, -0.4000000059604645, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.4000000059604645, 1.0, 0.20000000298023224, 0.20000000298023224, 0.4000000059604645, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · notes and probes

Commit `54dccfe2319e79482258b7e970747e4eaf7bf61b`; parents: 04e3ac53f49206001c12b6fd34ec1844072db9b2. Recorded author date: 2026-10-01T10:42:47+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0047](01_timeline.md#E0047): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C002_54dccfe.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/NOTES.md b/NOTES.md
new file mode 100644
index 0000000..e1e7d87
--- /dev/null
+++ b/NOTES.md
@@ -0,0 +1,9 @@
           1 +# Env notes (Rovers)
           2 +- Use: from env_client import make_env; env=make_env(); obs,info=env.reset(seed=s); obs,r,term,trunc,info=env.step(np.array(8 floats,float32))
           3 +- Iterate objects: `for o in obs:` gives objects (o.name, o.type.name); obs.get(o,'x'); obs.get_object_from_name('rover0').
           4 +- Action per rover: [dx(+-0.2), dy(+-0.2), dtheta(+-0.4), selector]. Selector band centres: sample=-0.8333, calibrate=-0.5, image=-0.1667, noop=0.1667, send=0.5, drop=0.8333. (0 = noop)
           5 +- Rover starts: rover0 (1.0,-1.75,theta=pi), rover1 (-1.0,-1.75,theta=0). Lander fixed (-1.9,-2.0).
           6 +- Mounds: obstacles with half_x=0.25 at (+-2,2),(+-0.5,2), z small. Objectives sit on mounds (z=0.2). Pillars: half 0.05x0.05, height 0.4.
           7 +- A hidden wall (NOT in obs) runs along x=0 for the full arena length -> rover0 confined to x>0, rover1 to x<0. Rover0 min x at y=-1.75 is 0.23 (so wall half-thickness + rover radius = 0.23).
           8 +- Motions that collide are rejected entirely (rover stays put); the operator in that step still applies.
           9 +- Arena is 5m square (approx -2.5..2.5).
diff --git a/dump.py b/dump.py
new file mode 100644
index 0000000..ee6a3f6
--- /dev/null
+++ b/dump.py
@@ -0,0 +1,8 @@
           1 +from env_client import make_env
           2 +env = make_env()
           3 +for seed in [0,1]:
           4 +    obs, info = env.reset(seed=seed)
           5 +    print("seed",seed, info)
           6 +    for o in obs:
           7 +        print(o.name, o.type.name, [round(float(v),3) for v in obs.data[o]])
           8 +env.close()
diff --git a/probe1.py b/probe1.py
new file mode 100644
index 0000000..e375e21
--- /dev/null
+++ b/probe1.py
@@ -0,0 +1,18 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +r0 = obs.get_object_from_name('rover0'); r1=obs.get_object_from_name('rover1')
           6 +def p(o): return tuple(round(obs.get(o,f),3) for f in ['x','y','theta','store_full','calibrated','at_home'])
           7 +# move rover0 -x, rover1 nothing
           8 +for i in range(8):
           9 +    obs,r,te,tr,inf = env.step(np.array([-0.2,0,0,0, 0,0,0,0],dtype=np.float32))
          10 +    print(i,p(r0),p(r1),r,te,tr)
          11 +# try bigger than limits
          12 +obs,r,te,tr,inf = env.step(np.array([0,0.5,0,0, 0,0,0,0],dtype=np.float32)); print('big',p(r0))
          13 +obs,r,te,tr,inf = env.step(np.array([0,0,0.4,0, 0,0,0,0],dtype=np.float32)); print('rot',p(r0))
          14 +# move rover1 +y up the left side
          15 +for i in range(25):
          16 +    obs,r,te,tr,inf = env.step(np.array([0,0,0,0, 0,0.2,0,0],dtype=np.float32))
          17 +print('r1 after up',p(r1))
          18 +env.close()
diff --git a/probe2.py b/probe2.py
new file mode 100644
index 0000000..8f2b65c
--- /dev/null
+++ b/probe2.py
@@ -0,0 +1,20 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env = make_env()
           4 +obs, info = env.reset(seed=0)
           5 +r0 = obs.get_object_from_name('rover0')
           6 +def p(o): return tuple(round(obs.get(o,f),4) for f in ['x','y','theta'])
           7 +# rover0 to the wall with fine steps
           8 +for i in range(200):
           9 +    obs,*_ = env.step(np.array([-0.01,0,0,0, 0,0,0,0],dtype=np.float32))
          10 +print('r0 min x at y=-1.75', p(r0))
          11 +# move up along wall, testing whether wall ends
          12 +xs=[]
          13 +for i in range(40):
          14 +    obs,*_ = env.step(np.array([0,0.1,0,0, 0,0,0,0],dtype=np.float32))
          15 +    # try to move left
          16 +    b=obs.get(r0,'x')
          17 +    obs,*_ = env.step(np.array([-0.05,0,0,0, 0,0,0,0],dtype=np.float32))
          18 +    xs.append((round(obs.get(r0,'y'),2), round(obs.get(r0,'x'),3)))
          19 +print(xs)
          20 +env.close()
```

</details>

<a id="C003"></a>
### C003 · collision notes

Commit `daa839b818855e10b007f2b9bb2756852d12c293`; parents: 54dccfe2319e79482258b7e970747e4eaf7bf61b. Recorded author date: 2026-10-01T10:52:15+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0450](01_timeline.md#E0450): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C003_daa839b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/NOTES.md b/NOTES.md
index e1e7d87..3359768 100644
--- a/NOTES.md
+++ b/NOTES.md
@@ -7,3 +7,9 @@
    7      7  - A hidden wall (NOT in obs) runs along x=0 for the full arena length -> rover0 confined to x>0, rover1 to x<0. Rover0 min x at y=-1.75 is 0.23 (so wall half-thickness + rover radius = 0.23).
    8      8  - Motions that collide are rejected entirely (rover stays put); the operator in that step still applies.
    9      9  - Arena is 5m square (approx -2.5..2.5).
          10 +## Collision (probed)
          11 +- Motion world-frame, exact, clipped. Only end pose checked (no swept). Rotations also collision-checked.
          12 +- Pillars: rover footprint lumpy/heading dependent; safe model: circle r=0.24 vs pillar box (contact range 0.167-0.2375).
          13 +- Mounds: circle r=0.177 vs mound box (half 0.25).
          14 +- Walls (arena edge, middle wall): |x|,|y| <= 2.2729; rover0 x>=0.2271, rover1 x<=-0.2271. No gaps.
          15 +- Lander: safe rule keep rover centre x>=-1.205 or y>=-1.465.
diff --git a/probe_col_an.py b/probe_col_an.py
new file mode 100644
index 0000000..a5b61c9
--- /dev/null
+++ b/probe_col_an.py
@@ -0,0 +1,8 @@
           1 +import numpy as np
           2 +for m in '012':
           3 +    L=[l.split() for l in open(f'probe_col_rays_{m}.txt').read().splitlines()[1:]]
           4 +    d=[]
           5 +    for a,x,y,_ in L:
           6 +        x,y=float(x),float(y)
           7 +        cx,cy=np.clip(x,-.05,.05),np.clip(y,-.05,.05); d.append((np.hypot(x-cx,y-cy),int(a)))
           8 +    d=np.array(d); print(m,'dbox min %.4f max %.4f'%(d[:,0].min(),d[:,0].max()), 'argmax ang',d[d[:,0].argmax(),1],'argmin',d[d[:,0].argmin(),1])
diff --git a/probe_col_arena.py b/probe_col_arena.py
new file mode 100644
index 0000000..1d514b7
--- /dev/null
+++ b/probe_col_arena.py
@@ -0,0 +1,17 @@
           1 +from probe_col_lib import R
           2 +import numpy as np
           3 +r=R(0)
           4 +# rover0: push +x at y=-1.75, -y, then to +y along x=1.0 (avoid obstacles)
           5 +print('r0 +x', r.push(0,1,0))
           6 +print('r0 -y', r.push(0,0,-1))
           7 +r.path(0,[(1.0,-1.75),(1.0,0.5)])
           8 +print('r0 +y at x=1.0',r.push(0,0,1))
           9 +r.path(0,[(1.0,0.5),(0.3,-1.75)])
          10 +print('r0 -x at y=-1.75',r.push(0,-1,0))
          11 +# rover1
          12 +print('r1 -x', r.push(1,-1,0))
          13 +print('r1 -y', r.push(1,0,-1))
          14 +r.path(1,[(-1.0,-1.75),(-1.0,1.3)])
          15 +print('r1 +y at x=-1',r.push(1,0,1))
          16 +r.path(1,[(-1.0,1.3),(-0.3,-1.75)])
          17 +print('r1 +x at y=-1.75',r.push(1,1,0))
diff --git a/probe_col_bounds.py b/probe_col_bounds.py
new file mode 100644
index 0000000..d654bce
--- /dev/null
+++ b/probe_col_bounds.py
@@ -0,0 +1,26 @@
           1 +from probe_col_lib import R
           2 +import numpy as np, sys
           3 +def approach(r,i,target,tol=1e-4):
           4 +    step=0.2
           5 +    while step>tol:
           6 +        p=r.pos(i)[:2]; d=np.array(target)-p; n=np.linalg.norm(d)
           7 +        if n<1e-6: break
           8 +        s=min(step,n); q=r.step(i,*(d/n*s))[:2]
           9 +        if np.allclose(q,p,atol=1e-9): step/=2
          10 +    return r.pos(i)
          11 +def rot(r,i,tot):
          12 +    while abs(tot)>1e-9:
          13 +        d=np.clip(tot,-0.4,0.4); r.step(i,0,0,d); tot-=d
          14 +if __name__=="__main__":
          15 +     for dth in [0,0.4,np.pi/4,np.pi/2,1.0]:
          16 +        r=R(0)
          17 +        rot(r,0,dth); rot(r,1,dth)
          18 +        out=[]
          19 +        r.goto(0,1.0,-1.5); out.append(approach(r,0,(3,-1.5))[0]); r.goto(0,1.0,-1.5)
          20 +        out.append(approach(r,0,(1.0,-3))[1]); r.goto(0,1.0,-1.5)
          21 +        out.append(approach(r,0,(-1,-1.5))[0]); r.goto(0,1.0,-1.5)
          22 +        # rover1: avoid lander; go to (-1,-1.2)
          23 +        r.goto(1,-1.0,-1.2); out.append(approach(r,1,(1,-1.2))[0]); r.goto(1,-1.0,-1.2)
          24 +        out.append(approach(r,1,(-3,-1.2))[0]); r.goto(1,-1.0,-1.2)
          25 +        print('dth %.3f th0 %.3f'%(dth,r.pos(0)[2]),'r0 maxx %.4f miny %.4f minx %.4f | r1 maxx %.4f minx %.4f'%tuple(out))
          26 +        r.env.close()
diff --git a/probe_col_dump.py b/probe_col_dump.py
new file mode 100644
index 0000000..3277a38
--- /dev/null
+++ b/probe_col_dump.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +import numpy as np, sys
           3 +env=make_env()
           4 +for s in [0,1,2]:
           5 +    obs,info=env.reset(seed=s)
           6 +    print('seed',s)
           7 +    for o in obs:
           8 +        feats={}
           9 +        for f in ['x','y','z','theta','half_x','half_y']:
          10 +            try: feats[f]=round(float(obs.get(o,f)),3)
          11 +            except Exception: pass
          12 +        print(' ',o.name,o.type.name,feats)
          13 +env.close()
diff --git a/probe_col_f_0.3927_0.txt b/probe_col_f_0.3927_0.txt
new file mode 100644
index 0000000..38ae266
--- /dev/null
+++ b/probe_col_f_0.3927_0.txt
@@ -0,0 +1,45 @@
           1 +0 0.1831
           2 +2 0.1812
           3 +4 0.1794
           4 +6 0.1777
           5 +8 0.1758
           6 +10 0.1742
           7 +12 0.1725
           8 +14 0.1707
           9 +16 0.1695
          10 +18 0.1685
          11 +20 0.1678
          12 +22 0.1676
          13 +24 0.1678
          14 +26 0.1678
          15 +28 0.1681
          16 +30 0.1689
          17 +32 0.1702
          18 +34 0.1703
          19 +36 0.1706
          20 +38 0.1715
          21 +40 0.1727
          22 +42 0.1731
          23 +44 0.1735
          24 +46 0.1743
          25 +48 0.1756
          26 +50 0.1760
          27 +52 0.1776
          28 +54 0.1831
          29 +56 0.1894
          30 +58 0.1963
          31 +60 0.2041
          32 +62 0.2126
          33 +64 0.2219
          34 +66 0.2323
          35 +68 0.2337
          36 +70 0.2284
          37 +72 0.2236
          38 +74 0.2194
          39 +76 0.2160
          40 +78 0.2132
          41 +80 0.2109
          42 +82 0.2089
          43 +84 0.2067
          44 +86 0.2041
          45 +88 0.2003
diff --git a/probe_col_f_0.3927_180.txt b/probe_col_f_0.3927_180.txt
new file mode 100644
index 0000000..e9758de
--- /dev/null
+++ b/probe_col_f_0.3927_180.txt
@@ -0,0 +1,45 @@
           1 +180 0.2130
           2 +182 0.2097
           3 +184 0.2061
           4 +186 0.2024
           5 +188 0.1990
           6 +190 0.1955
           7 +192 0.1921
           8 +194 0.1891
           9 +196 0.1863
          10 +198 0.1840
          11 +200 0.1820
          12 +202 0.1805
          13 +204 0.1792
          14 +206 0.1785
          15 +208 0.1782
          16 +210 0.1782
          17 +212 0.1786
          18 +214 0.1794
          19 +216 0.1808
          20 +218 0.1826
          21 +220 0.1848
          22 +222 0.1877
          23 +224 0.1909
          24 +226 0.1948
          25 +228 0.1990
          26 +230 0.2041
          27 +232 0.2096
          28 +234 0.2159
          29 +236 0.2229
          30 +238 0.2306
          31 +240 0.2296
          32 +242 0.2215
          33 +244 0.2209
          34 +246 0.2314
          35 +248 0.2333
          36 +250 0.2278
          37 +252 0.2230
          38 +254 0.2191
          39 +256 0.2156
          40 +258 0.2128
          41 +260 0.2105
          42 +262 0.2083
          43 +264 0.2063
          44 +266 0.2038
          45 +268 0.1999
diff --git a/probe_col_f_0.3927_270.txt b/probe_col_f_0.3927_270.txt
new file mode 100644
index 0000000..858da1a
--- /dev/null
+++ b/probe_col_f_0.3927_270.txt
@@ -0,0 +1,45 @@
           1 +270 0.1964
           2 +272 0.1929
           3 +274 0.1895
           4 +276 0.1861
           5 +278 0.1828
           6 +280 0.1795
           7 +282 0.1765
           8 +284 0.1734
           9 +286 0.1708
          10 +288 0.1685
          11 +290 0.1674
          12 +292 0.1672
          13 +294 0.1672
          14 +296 0.1672
          15 +298 0.1675
          16 +300 0.1683
          17 +302 0.1696
          18 +304 0.1699
          19 +306 0.1702
          20 +308 0.1711
          21 +310 0.1723
          22 +312 0.1727
          23 +314 0.1739
          24 +316 0.1774
          25 +318 0.1817
          26 +320 0.1862
          27 +322 0.1916
          28 +324 0.1973
          29 +326 0.2040
          30 +328 0.2113
          31 +330 0.2193
          32 +332 0.2283
          33 +334 0.2344
          34 +336 0.2275
          35 +338 0.2215
          36 +340 0.2162
          37 +342 0.2118
          38 +344 0.2081
          39 +346 0.2048
          40 +348 0.2023
          41 +350 0.2001
          42 +352 0.1976
          43 +354 0.1939
          44 +356 0.1901
          45 +358 0.1867
diff --git a/probe_col_f_0.3927_90.txt b/probe_col_f_0.3927_90.txt
new file mode 100644
index 0000000..8819ac4
--- /dev/null
+++ b/probe_col_f_0.3927_90.txt
@@ -0,0 +1,45 @@
           1 +90 0.1968
           2 +92 0.1931
           3 +94 0.1897
           4 +96 0.1865
           5 +98 0.1831
           6 +100 0.1799
           7 +102 0.1767
           8 +104 0.1738
           9 +106 0.1710
          10 +108 0.1687
          11 +110 0.1678
          12 +112 0.1676
          13 +114 0.1676
          14 +116 0.1676
          15 +118 0.1679
          16 +120 0.1687
          17 +122 0.1700
          18 +124 0.1701
          19 +126 0.1704
          20 +128 0.1713
          21 +130 0.1725
          22 +132 0.1727
          23 +134 0.1743
          24 +136 0.1778
          25 +138 0.1818
          26 +140 0.1866
          27 +142 0.1918
          28 +144 0.1977
          29 +146 0.2044
          30 +148 0.2117
          31 +150 0.2197
          32 +152 0.2287
          33 +154 0.2334
          34 +156 0.2265
          35 +158 0.2207
          36 +160 0.2295
          37 +162 0.2375
          38 +164 0.2332
          39 +166 0.2295
          40 +168 0.2263
          41 +170 0.2238
          42 +172 0.2216
          43 +174 0.2193
          44 +176 0.2172
          45 +178 0.2152
diff --git a/probe_col_f_0_0.txt b/probe_col_f_0_0.txt
new file mode 100644
index 0000000..1a8dc17
--- /dev/null
+++ b/probe_col_f_0_0.txt
@@ -0,0 +1,45 @@
           1 +0 0.1831
           2 +2 0.1812
           3 +4 0.1794
           4 +6 0.1777
           5 +8 0.1758
           6 +10 0.1742
           7 +12 0.1725
           8 +14 0.1707
           9 +16 0.1695
          10 +18 0.1685
          11 +20 0.1697
          12 +22 0.1714
          13 +24 0.1736
          14 +26 0.1763
          15 +28 0.1795
          16 +30 0.1835
          17 +32 0.1871
          18 +34 0.1897
          19 +36 0.1929
          20 +38 0.1967
          21 +40 0.2008
          22 +42 0.2059
          23 +44 0.2114
          24 +46 0.2177
          25 +48 0.2248
          26 +50 0.2297
          27 +52 0.2217
          28 +54 0.2145
          29 +56 0.2083
          30 +58 0.2029
          31 +60 0.1981
          32 +62 0.1939
          33 +64 0.1903
          34 +66 0.1873
          35 +68 0.1849
          36 +70 0.1832
          37 +72 0.1842
          38 +74 0.1848
          39 +76 0.1851
          40 +78 0.1856
          41 +80 0.1865
          42 +82 0.1864
          43 +84 0.1857
          44 +86 0.1849
          45 +88 0.1839
diff --git a/probe_col_f_0_180.txt b/probe_col_f_0_180.txt
new file mode 100644
index 0000000..5d3ecfb
--- /dev/null
+++ b/probe_col_f_0_180.txt
@@ -0,0 +1,45 @@
           1 +180 0.1954
           2 +182 0.1954
           3 +184 0.1954
           4 +186 0.1954
           5 +188 0.1953
           6 +190 0.1953
           7 +192 0.1954
           8 +194 0.1956
           9 +196 0.1965
          10 +198 0.1977
          11 +200 0.1994
          12 +202 0.2015
          13 +204 0.2023
          14 +206 0.2033
          15 +208 0.2046
          16 +210 0.2064
          17 +212 0.2089
          18 +214 0.2118
          19 +216 0.2153
          20 +218 0.2193
          21 +220 0.2241
          22 +222 0.2260
          23 +224 0.2149
          24 +226 0.2169
          25 +228 0.2240
          26 +230 0.2289
          27 +232 0.2211
          28 +234 0.2139
          29 +236 0.2077
          30 +238 0.2021
          31 +240 0.1973
          32 +242 0.1931
          33 +244 0.1897
          34 +246 0.1868
          35 +248 0.1843
          36 +250 0.1824
          37 +252 0.1835
          38 +254 0.1842
          39 +256 0.1843
          40 +258 0.1851
          41 +260 0.1859
          42 +262 0.1860
          43 +264 0.1851
          44 +266 0.1843
          45 +268 0.1835
diff --git a/probe_col_f_0_270.txt b/probe_col_f_0_270.txt
new file mode 100644
index 0000000..9e33122
--- /dev/null
+++ b/probe_col_f_0_270.txt
@@ -0,0 +1,45 @@
           1 +270 0.1825
           2 +272 0.1806
           3 +274 0.1794
           4 +276 0.1793
           5 +278 0.1793
           6 +280 0.1794
           7 +282 0.1793
           8 +284 0.1795
           9 +286 0.1800
          10 +288 0.1810
          11 +290 0.1824
          12 +292 0.1843
          13 +294 0.1868
          14 +296 0.1897
          15 +298 0.1927
          16 +300 0.1946
          17 +302 0.1967
          18 +304 0.1995
          19 +306 0.2028
          20 +308 0.2066
          21 +310 0.2112
          22 +312 0.2162
          23 +314 0.2220
          24 +316 0.2286
          25 +318 0.2217
          26 +320 0.2131
          27 +322 0.2057
          28 +324 0.1989
          29 +326 0.1931
          30 +328 0.1879
          31 +330 0.1835
          32 +332 0.1799
          33 +334 0.1812
          34 +336 0.1819
          35 +338 0.1822
          36 +340 0.1830
          37 +342 0.1840
          38 +344 0.1848
          39 +346 0.1849
          40 +348 0.1856
          41 +350 0.1865
          42 +352 0.1866
          43 +354 0.1857
          44 +356 0.1849
          45 +358 0.1841
diff --git a/probe_col_f_0_90.txt b/probe_col_f_0_90.txt
new file mode 100644
index 0000000..f0fde92
--- /dev/null
+++ b/probe_col_f_0_90.txt
@@ -0,0 +1,45 @@
           1 +90 0.1829
           2 +92 0.1810
           3 +94 0.1800
           4 +96 0.1799
           5 +98 0.1799
           6 +100 0.1799
           7 +102 0.1799
           8 +104 0.1801
           9 +106 0.1806
          10 +108 0.1815
          11 +110 0.1830
          12 +112 0.1849
          13 +114 0.1873
          14 +116 0.1903
          15 +118 0.1931
          16 +120 0.1949
          17 +122 0.1971
          18 +124 0.1999
          19 +126 0.2032
          20 +128 0.2070
          21 +130 0.2116
          22 +132 0.2168
          23 +134 0.2225
          24 +136 0.2290
          25 +138 0.2209
          26 +140 0.2147
          27 +142 0.2230
          28 +144 0.2323
          29 +146 0.2270
          30 +148 0.2210
          31 +150 0.2158
          32 +152 0.2112
          33 +154 0.2074
          34 +156 0.2042
          35 +158 0.2015
          36 +160 0.1994
          37 +162 0.1977
          38 +164 0.1965
          39 +166 0.1956
          40 +168 0.1954
          41 +170 0.1953
          42 +172 0.1953
          43 +174 0.1954
          44 +176 0.1954
          45 +178 0.1954
diff --git a/probe_col_fine.py b/probe_col_fine.py
new file mode 100644
index 0000000..be6315b
--- /dev/null
+++ b/probe_col_fine.py
@@ -0,0 +1,13 @@
           1 +from probe_col_lib import R
           2 +from probe_col_bounds import approach, rot
           3 +import numpy as np, sys
           4 +c=np.array([0.654,-0.199]); RAD=0.42
           5 +th=float(sys.argv[1]); k0=int(sys.argv[2])
           6 +r=R(0); r.path(0,[(1.0,-1.0),(c[0]+RAD,c[1])]); rot(r,0,th)
           7 +for kk in range(0,k0+1,10):
           8 +    r.goto(0,*(c+RAD*np.array([np.cos(np.deg2rad(kk)),np.sin(np.deg2rad(kk))])))
           9 +for k in range(k0,k0+90,2):
          10 +    a=np.deg2rad(k); S=c+RAD*np.array([np.cos(a),np.sin(a)])
          11 +    if not r.goto(0,*S): print('navfail',k); break
          12 +    p=approach(r,0,c,tol=1e-4); rel=p[:2]-c
          13 +    cx,cy=np.clip(rel,-.05,.05); print(k,'%.4f'%np.hypot(rel[0]-cx,rel[1]-cy)); r.goto(0,*S)
diff --git a/probe_col_frame.py b/probe_col_frame.py
new file mode 100644
index 0000000..74b0b36
--- /dev/null
+++ b/probe_col_frame.py
@@ -0,0 +1,5 @@
           1 +from probe_col_lib import R
           2 +r=R(0)
           3 +print(r.pos(0)); print(r.step(0,0.2,0)); print(r.step(0,0,0.2)); print(r.step(0,0,0,0.4)); print(r.step(0,0.2,0))
           4 +print(r.pos(1)); print(r.step(1,0.2,0)); print(r.step(1,0.123,-0.077))
           5 +print(r.step(1,0.5,0))
diff --git a/probe_col_lander.py b/probe_col_lander.py
new file mode 100644
index 0000000..1549a55
--- /dev/null
+++ b/probe_col_lander.py
@@ -0,0 +1,15 @@
           1 +from probe_col_lib import R
           2 +from probe_col_bounds import approach, rot
           3 +import numpy as np, sys
           4 +c=np.array([-1.9,-2.0]); RAD=1.0
           5 +r=R(4)
           6 +print([o for o in r.obst() if o[1]<0 and o[2]<0 and o[3]<0.1])
           7 +rot(r,1,float(sys.argv[1]))
           8 +r.goto(1,-1.0,-1.2)
           9 +for k in range(-30,185,5):
          10 +    a=np.deg2rad(k); S=c+RAD*np.array([np.cos(a),np.sin(a)])
          11 +    S=np.clip(S,-2.26,-0.24)
          12 +    if k>100: r.goto(1,-1.0,-1.2); r.goto(1,-2.0,-1.2)
          13 +    if not r.goto(1,-1.0,-1.2) or not r.goto(1,*S): print(k,'nav fail',r.pos(1)); continue
          14 +    p=approach(r,1,c,tol=2e-4); rel=p[:2]-c
          15 +    print('%4d rel %.4f %.4f  r=%.4f th=%.3f'%(k,rel[0],rel[1],np.hypot(*rel),p[2]))
diff --git a/probe_col_lander_0.txt b/probe_col_lander_0.txt
new file mode 100644
index 0000000..17e3e8f
--- /dev/null
+++ b/probe_col_lander_0.txt
@@ -0,0 +1,44 @@
           1 +[]
           2 + -30 rel 0.6898 -0.2071  r=0.7202 th=0.000
           3 + -25 rel 0.6897 -0.1978  r=0.7175 th=0.000
           4 + -20 rel 0.6897 -0.1908  r=0.7156 th=0.000
           5 + -15 rel 0.6897 -0.1848  r=0.7141 th=0.000
           6 + -10 rel 0.6898 -0.1216  r=0.7004 th=0.000
           7 +  -5 rel 0.6899 -0.0604  r=0.6926 th=0.000
           8 +   0 rel 0.6898 0.0000  r=0.6898 th=0.000
           9 +   5 rel 0.6899 0.0604  r=0.6926 th=0.000
          10 +  10 rel 0.6898 0.1216  r=0.7004 th=0.000
          11 +  15 rel 0.6897 0.1848  r=0.7141 th=0.000
          12 +  20 rel 0.6897 0.2510  r=0.7340 th=0.000
          13 +  25 rel 0.6896 0.3216  r=0.7609 th=0.000
          14 +  30 rel 0.6898 0.3982  r=0.7965 th=0.000
          15 +  35 rel 0.6505 0.4555  r=0.7941 th=0.000
          16 +  40 rel 0.5904 0.4954  r=0.7707 th=0.000
          17 +  45 rel 0.5138 0.5138  r=0.7266 th=0.000
          18 +  50 rel 0.4359 0.5195  r=0.6781 th=0.000
          19 +  55 rel 0.3645 0.5206  r=0.6355 th=0.000
          20 +  60 rel 0.3006 0.5206  r=0.6012 th=0.000
          21 +  65 rel 0.2428 0.5208  r=0.5746 th=0.000
          22 +  70 rel 0.1896 0.5209  r=0.5543 th=0.000
          23 +  75 rel 0.1395 0.5207  r=0.5391 th=0.000
          24 +  80 rel 0.0918 0.5209  r=0.5289 th=0.000
          25 +  85 rel 0.0450 0.5148  r=0.5168 th=0.000
          26 +  90 rel 0.0000 0.5137  r=0.5137 th=0.000
          27 +  95 rel -0.0450 0.5148  r=0.5168 th=0.000
          28 + 100 rel -0.0918 0.5209  r=0.5289 th=0.000
          29 + 105 rel -0.1395 0.5207  r=0.5391 th=0.000
          30 + 110 rel -0.1896 0.5209  r=0.5543 th=0.000
          31 + 115 rel -0.2069 0.5208  r=0.5603 th=0.000
          32 + 120 rel -0.2165 0.5208  r=0.5640 th=0.000
          33 + 125 rel -0.2289 0.5209  r=0.5690 th=0.000
          34 + 130 rel -0.2447 0.5207  r=0.5753 th=0.000
          35 + 135 rel -0.2652 0.5209  r=0.5845 th=0.000
          36 + 140 rel -0.2917 0.5208  r=0.5969 th=0.000
          37 + 145 rel -0.3268 0.5206  r=0.6147 th=0.000
          38 +150 nav fail [-1.20000005 -1.39999998  0.        ]
          39 +155 nav fail [-1.20000005 -1.39999998  0.        ]
          40 +160 nav fail [-1.20000005 -1.4000001   0.        ]
          41 +165 nav fail [-1.20000005 -1.4000001   0.        ]
          42 +170 nav fail [-1.20000005 -1.4000001   0.        ]
          43 +175 nav fail [-1.20000005 -1.4000001   0.        ]
          44 +180 nav fail [-1.20000005 -1.4000001   0.        ]
diff --git a/probe_col_lander_1.txt b/probe_col_lander_1.txt
new file mode 100644
index 0000000..6a3162d
--- /dev/null
+++ b/probe_col_lander_1.txt
@@ -0,0 +1,44 @@
           1 +[]
           2 + -30 rel 0.6737 -0.2023  r=0.7034 th=1.571
           3 + -25 rel 0.6739 -0.1933  r=0.7011 th=1.571
           4 + -20 rel 0.6739 -0.1865  r=0.6992 th=1.571
           5 + -15 rel 0.6739 -0.1806  r=0.6977 th=1.571
           6 + -10 rel 0.6740 -0.1188  r=0.6844 th=1.571
           7 +  -5 rel 0.6740 -0.0590  r=0.6766 th=1.571
           8 +   0 rel 0.6738 0.0000  r=0.6738 th=1.571
           9 +   5 rel 0.6740 0.0590  r=0.6766 th=1.571
          10 +  10 rel 0.6740 0.1188  r=0.6844 th=1.571
          11 +  15 rel 0.6739 0.1806  r=0.6977 th=1.571
          12 +  20 rel 0.6739 0.2453  r=0.7172 th=1.571
          13 +  25 rel 0.6737 0.3142  r=0.7434 th=1.571
          14 +  30 rel 0.6739 0.3891  r=0.7781 th=1.571
          15 +  35 rel 0.6428 0.4501  r=0.7848 th=1.571
          16 +  40 rel 0.5970 0.5009  r=0.7793 th=1.571
          17 +  45 rel 0.5295 0.5295  r=0.7488 th=1.571
          18 +  50 rel 0.4444 0.5296  r=0.6914 th=1.571
          19 +  55 rel 0.3708 0.5296  r=0.6465 th=1.571
          20 +  60 rel 0.3057 0.5294  r=0.6113 th=1.571
          21 +  65 rel 0.2470 0.5296  r=0.5844 th=1.571
          22 +  70 rel 0.1928 0.5297  r=0.5637 th=1.571
          23 +  75 rel 0.1419 0.5297  r=0.5484 th=1.571
          24 +  80 rel 0.0934 0.5297  r=0.5379 th=1.571
          25 +  85 rel 0.0463 0.5296  r=0.5316 th=1.571
          26 +  90 rel 0.0000 0.5297  r=0.5297 th=1.571
          27 +  95 rel -0.0463 0.5296  r=0.5316 th=1.571
          28 + 100 rel -0.0934 0.5297  r=0.5379 th=1.571
          29 + 105 rel -0.1419 0.5297  r=0.5484 th=1.571
          30 + 110 rel -0.1928 0.5297  r=0.5637 th=1.571
          31 + 115 rel -0.2103 0.5295  r=0.5697 th=1.571
          32 + 120 rel -0.2201 0.5295  r=0.5734 th=1.571
          33 + 125 rel -0.2327 0.5295  r=0.5784 th=1.571
          34 + 130 rel -0.2489 0.5295  r=0.5851 th=1.571
          35 + 135 rel -0.2696 0.5296  r=0.5943 th=1.571
          36 + 140 rel -0.2966 0.5296  r=0.6070 th=1.571
          37 + 145 rel -0.3324 0.5296  r=0.6252 th=1.571
          38 +150 nav fail [-1.20000005 -1.39999998  1.57079995]
          39 +155 nav fail [-1.20000005 -1.39999998  1.57079995]
          40 +160 nav fail [-1.20000005 -1.39999998  1.57079995]
          41 +165 nav fail [-1.20000005 -1.4000001   1.57079995]
          42 +170 nav fail [-1.20000005 -1.4000001   1.57079995]
          43 +175 nav fail [-1.20000005 -1.4000001   1.57079995]
          44 +180 nav fail [-1.20000005 -1.4000001   1.57079995]
diff --git a/probe_col_lib.py b/probe_col_lib.py
new file mode 100644
index 0000000..017b37c
--- /dev/null
+++ b/probe_col_lib.py
@@ -0,0 +1,44 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +class R:
           4 +    def __init__(self, seed=0):
           5 +        self.env=make_env(); self.obs,_=self.env.reset(seed=seed)
           6 +    def pos(self,i):
           7 +        o=self.obs.get_object_from_name(f'rover{i}')
           8 +        return np.array([self.obs.get(o,'x'),self.obs.get(o,'y'),self.obs.get(o,'theta')],float)
           9 +    def step(self,i,dx=0,dy=0,dth=0):
          10 +        a=np.zeros(8,np.float32); a[4*i:4*i+3]=[dx,dy,dth]
          11 +        self.obs,*_=self.env.step(a)
          12 +        return self.pos(i)
          13 +    def goto(self,i,x,y,maxit=200):
          14 +        for _ in range(maxit):
          15 +            p=self.pos(i); d=np.array([x,y])-p[:2]
          16 +            if np.linalg.norm(d)<1e-6: return True
          17 +            d=np.clip(d,-0.2,0.2)
          18 +            q=self.step(i,*d)
          19 +            if np.allclose(q[:2],p[:2]): return False
          20 +        return False
          21 +    def path(self,i,pts):
          22 +        for (x,y) in pts:
          23 +            if not self.goto(i,x,y): print('blocked going to',(x,y),'at',self.pos(i)); return False
          24 +        return True
          25 +    def push(self,i,ux,uy,step=0.005,maxit=2000):
          26 +        """move in direction (ux,uy) with given step until blocked; return last pos"""
          27 +        u=np.array([ux,uy],float); u/=np.linalg.norm(u)
          28 +        # coarse
          29 +        for s in [0.05,step]:
          30 +            for _ in range(maxit):
          31 +                p=self.pos(i); q=self.step(i,*(u*s))
          32 +                if np.allclose(q[:2],p[:2],atol=1e-9): break
          33 +        # finer
          34 +        for s in [0.001]:
          35 +            for _ in range(maxit):
          36 +                p=self.pos(i); q=self.step(i,*(u*s))
          37 +                if np.allclose(q[:2],p[:2],atol=1e-9): break
          38 +        return self.pos(i)
          39 +    def obst(self):
          40 +        out=[]
          41 +        for o in self.obs:
          42 +            if o.type.name=='obstacle':
          43 +                out.append((o.name,self.obs.get(o,'x'),self.obs.get(o,'y'),self.obs.get(o,'half_x')))
          44 +        return out
diff --git a/probe_col_m_0_0.5.txt b/probe_col_m_0_0.5.txt
new file mode 100644
index 0000000..0b83155
--- /dev/null
+++ b/probe_col_m_0_0.5.txt
@@ -0,0 +1,19 @@
           1 +180 nav fail [ 0.80000007  1.39999998 -3.14159274]
           2 +190 nav fail [ 0.80000007  1.4000001  -3.14159274]
           3 +200 nav fail [ 0.80000007  1.4000001  -3.14159274]
           4 +210 nav fail [ 0.80000007  1.4000001  -3.14159274]
           5 + 220 rel -0.2303 -0.4271  dbox=0.1771
           6 + 230 rel -0.1933 -0.4272  dbox=0.1772
           7 + 240 rel -0.1710 -0.4272  dbox=0.1772
           8 + 250 rel -0.1555 -0.4273  dbox=0.1773
           9 + 260 rel -0.0753 -0.4270  dbox=0.1770
          10 + 270 rel 0.0000 -0.4273  dbox=0.1773
          11 + 280 rel 0.0753 -0.4270  dbox=0.1770
          12 + 290 rel 0.1555 -0.4273  dbox=0.1773
          13 + 300 rel 0.2467 -0.4273  dbox=0.1773
          14 + 310 rel 0.3377 -0.4025  dbox=0.1759
          15 + 320 rel 0.4025 -0.3377  dbox=0.1759
          16 + 330 rel 0.4273 -0.2467  dbox=0.1773
          17 + 340 rel 0.4273 -0.1555  dbox=0.1773
          18 + 350 rel 0.4270 -0.0753  dbox=0.1770
          19 + 360 rel 0.4273 0.0000  dbox=0.1773
diff --git a/probe_col_m_0_2.0.txt b/probe_col_m_0_2.0.txt
new file mode 100644
index 0000000..c96410d
--- /dev/null
+++ b/probe_col_m_0_2.0.txt
@@ -0,0 +1,19 @@
           1 + 180 rel -0.4273 0.0000  dbox=0.1773
           2 + 190 rel -0.4270 -0.0753  dbox=0.1770
           3 + 200 rel -0.4273 -0.1555  dbox=0.1773
           4 + 210 rel -0.4273 -0.2467  dbox=0.1773
           5 + 220 rel -0.4025 -0.3377  dbox=0.1759
           6 + 230 rel -0.3377 -0.4025  dbox=0.1759
           7 + 240 rel -0.2467 -0.4273  dbox=0.1773
           8 + 250 rel -0.1555 -0.4273  dbox=0.1773
           9 + 260 rel -0.0753 -0.4270  dbox=0.1770
          10 + 270 rel 0.0000 -0.4273  dbox=0.1773
          11 + 280 rel 0.0753 -0.4270  dbox=0.1770
          12 + 290 rel 0.1555 -0.4273  dbox=0.1773
          13 + 300 rel 0.1710 -0.4272  dbox=0.1772
          14 + 310 rel 0.1933 -0.4272  dbox=0.1772
          15 + 320 rel 0.2303 -0.4271  dbox=0.1771
          16 +330 nav fail [ 1.60000002  1.39999998 -3.14159274]
          17 +340 nav fail [ 1.60000002  1.39999998 -3.14159274]
          18 +350 nav fail [ 1.60000002  1.39999998 -3.14159274]
          19 +360 nav fail [ 1.60000002  1.39999998 -3.14159274]
diff --git a/probe_col_m_1.5708_0.5.txt b/probe_col_m_1.5708_0.5.txt
new file mode 100644
index 0000000..ce75427
--- /dev/null
+++ b/probe_col_m_1.5708_0.5.txt
@@ -0,0 +1,19 @@
           1 +180 nav fail [ 0.80000007  1.39999998 -1.57079268]
           2 +190 nav fail [ 0.80000007  1.4000001  -1.57079268]
           3 +200 nav fail [ 0.80000007  1.4000001  -1.57079268]
           4 +210 nav fail [ 0.80000007  1.4000001  -1.57079268]
           5 + 220 rel -0.2303 -0.4271  dbox=0.1771
           6 + 230 rel -0.1933 -0.4272  dbox=0.1772
           7 + 240 rel -0.1710 -0.4272  dbox=0.1772
           8 + 250 rel -0.1555 -0.4273  dbox=0.1773
           9 + 260 rel -0.0753 -0.4270  dbox=0.1770
          10 + 270 rel 0.0000 -0.4273  dbox=0.1773
          11 + 280 rel 0.0753 -0.4270  dbox=0.1770
          12 + 290 rel 0.1555 -0.4273  dbox=0.1773
          13 + 300 rel 0.2467 -0.4273  dbox=0.1773
          14 + 310 rel 0.3377 -0.4025  dbox=0.1759
          15 + 320 rel 0.4025 -0.3377  dbox=0.1759
          16 + 330 rel 0.4273 -0.2467  dbox=0.1773
          17 + 340 rel 0.4273 -0.1555  dbox=0.1773
          18 + 350 rel 0.4270 -0.0753  dbox=0.1770
          19 + 360 rel 0.4273 0.0000  dbox=0.1773
diff --git a/probe_col_m_1.5708_2.0.txt b/probe_col_m_1.5708_2.0.txt
new file mode 100644
index 0000000..775023d
--- /dev/null
+++ b/probe_col_m_1.5708_2.0.txt
@@ -0,0 +1,19 @@
           1 + 180 rel -0.4273 0.0000  dbox=0.1773
           2 + 190 rel -0.4270 -0.0753  dbox=0.1770
           3 + 200 rel -0.4273 -0.1555  dbox=0.1773
           4 + 210 rel -0.4273 -0.2467  dbox=0.1773
           5 + 220 rel -0.4025 -0.3377  dbox=0.1759
           6 + 230 rel -0.3377 -0.4025  dbox=0.1759
           7 + 240 rel -0.2467 -0.4273  dbox=0.1773
           8 + 250 rel -0.1555 -0.4273  dbox=0.1773
           9 + 260 rel -0.0753 -0.4270  dbox=0.1770
          10 + 270 rel 0.0000 -0.4273  dbox=0.1773
          11 + 280 rel 0.0753 -0.4270  dbox=0.1770
          12 + 290 rel 0.1555 -0.4273  dbox=0.1773
          13 + 300 rel 0.1710 -0.4272  dbox=0.1772
          14 + 310 rel 0.1933 -0.4272  dbox=0.1772
          15 + 320 rel 0.2303 -0.4271  dbox=0.1771
          16 +330 nav fail [ 1.60000002  1.39999998 -1.57079268]
          17 +340 nav fail [ 1.60000002  1.39999998 -1.57079268]
          18 +350 nav fail [ 1.60000002  1.39999998 -1.57079268]
          19 +360 nav fail [ 1.60000002  1.39999998 -1.57079268]
diff --git a/probe_col_misc.py b/probe_col_misc.py
new file mode 100644
index 0000000..fd4c107
--- /dev/null
+++ b/probe_col_misc.py
@@ -0,0 +1,17 @@
           1 +from probe_col_lib import R
           2 +from probe_col_bounds import approach, rot
           3 +import numpy as np
           4 +c=np.array([0.654,-0.199])
           5 +r=R(0)
           6 +r.goto(0,1.0,-1.0); r.goto(0,*(c+[0.25,0.08]))
           7 +print('A',r.pos(0)[:2]-c)
           8 +q=r.step(0,-0.17,0.17); print('diag step through corner -> rel',q[:2]-c)
           9 +# rotation in contact
          10 +r.goto(0,1.3,-1.0); r.goto(0,1.3,c[1]); p=approach(r,0,c); print('contact rel',p[:2]-c,p[2])
          11 +for d in [0.4,-0.4,0.2,-0.2]:
          12 +    q=r.step(0,0,0,d); print('rot',d,'->th %.4f pos'%q[2],q[:2]-c)
          13 +# rover-rover: simultaneous moves both toward wall at same y
          14 +r.goto(1,-1.0,-1.75); 
          15 +a=np.array([0,0,0,0,0,0,0,0],np.float32)
          16 +print(r.pos(0),r.pos(1))
          17 +r.env.close()
diff --git a/probe_col_mound.py b/probe_col_mound.py
new file mode 100644
index 0000000..e038f66
--- /dev/null
+++ b/probe_col_mound.py
@@ -0,0 +1,15 @@
           1 +from probe_col_lib import R
           2 +from probe_col_bounds import approach
           3 +import numpy as np
           4 +for seed in [1,2]:
           5 +    r=R(seed)
           6 +    print('seed',seed,[o for o in r.obst() if o[3]<0.1 and o[1]>0])
           7 +    r.goto(0,1.0,-1.5); r.goto(0,1.2,1.2)
           8 +    p=approach(r,0,(1.2,2.5)); print('r0 at x=1.2 up to', p)
           9 +    r.goto(0,1.2,1.2); r.goto(0,2.0,1.2)
          10 +    p=approach(r,0,(2.0,2.5)); print('r0 toward mound (2,2) from below', p)
          11 +    r.goto(0,2.0,1.2); r.goto(0,1.0,1.2); r.goto(0,0.5,1.2)
          12 +    p=approach(r,0,(0.5,2.5)); print('r0 toward mound (0.5,2) from below', p)
          13 +    # clamp vs reject test
          14 +    r.goto(0,1.0,1.2); r.goto(0,1.0,-1.5); r.goto(0,2.2,-1.5); print('at',r.pos(0)); print('step +0.2 ->',r.step(0,0.2,0))
          15 +    r.env.close()
diff --git a/probe_col_mscan.py b/probe_col_mscan.py
new file mode 100644
index 0000000..2ea4ed0
--- /dev/null
+++ b/probe_col_mscan.py
@@ -0,0 +1,14 @@
           1 +from probe_col_lib import R
           2 +from probe_col_bounds import approach, rot
           3 +import numpy as np, sys
           4 +c=np.array([float(sys.argv[2]),2.0]); RAD=0.75
           5 +r=R(2)
           6 +r.goto(0,1.0,-1.0); r.goto(0,1.2,1.0)
           7 +rot(r,0,float(sys.argv[1]))
           8 +for k in range(180,365,10):
           9 +    a=np.deg2rad(k); S=c+RAD*np.array([np.cos(a),np.sin(a)])
          10 +    S=np.clip(S,0.24,2.26)
          11 +    if not r.goto(0,1.2,1.0) or not r.goto(0,*S): print(k,'nav fail',r.pos(0)); continue
          12 +    p=approach(r,0,c,tol=2e-4); rel=p[:2]-c
          13 +    cx,cy=np.clip(rel,-0.25,0.25)
          14 +    print('%4d rel %.4f %.4f  dbox=%.4f'%(k,rel[0],rel[1],np.hypot(rel[0]-cx,rel[1]-cy)))
diff --git a/probe_col_pillar.py b/probe_col_pillar.py
new file mode 100644
index 0000000..c82c298
--- /dev/null
+++ b/probe_col_pillar.py
@@ -0,0 +1,23 @@
           1 +from probe_col_lib import R
           2 +import numpy as np
           3 +px,py=0.654,-0.199; h=0.05
           4 +def run(start,u,dth=None,label=''):
           5 +    r=R(0)
           6 +    r.path(0,[(1.0,-1.0),(1.6,-1.0),(1.6,0.6)] if start[1]>-0.2 else [(1.0,-1.0)])
           7 +    if dth is not None:
           8 +        r.step(0,0,0,dth)
           9 +    if not r.path(0,[start]): return
          10 +    p=r.push(0,*u)
          11 +    # dist from rover center to box
          12 +    cx=np.clip(p[0],px-h,px+h); cy=np.clip(p[1],py-h,py+h)
          13 +    print(label,'stop',np.round(p,4),'dbox=%.4f'%np.hypot(p[0]-cx,p[1]-cy),'dx=%.4f dy=%.4f'%(abs(p[0]-px)-h,abs(p[1]-py)-h))
          14 +    r.env.close()
          15 +run((px,-0.8),(0,1),label='from below')
          16 +run((1.3,py),(-1,0),label='from right')
          17 +run((1.3,py),(-1,0),dth=0.4,label='from right th rot')
          18 +run((px,0.4),(0,-1),label='from above')
          19 +d=0.5
          20 +run((px+h+d,py-h-d),(-1,1),label='diag to corner BR')
          21 +run((px+h+d,py-h-d),(-1,1),dth=0.4,label='diag to corner BR rot')
          22 +run((px+h+d,py-h-d),(-1,1),dth=-0.4,label='diag to corner BR rot-')
          23 +run((px+h+0.4,py-h-0.2),(-2,1),label='dir(-2,1) to corner BR')
diff --git a/probe_col_rays.py b/probe_col_rays.py
new file mode 100644
index 0000000..be238c9
--- /dev/null
+++ b/probe_col_rays.py
@@ -0,0 +1,32 @@
           1 +from probe_col_lib import R
           2 +import numpy as np, sys
           3 +c=np.array([0.654,-0.199]); RAD=0.42
           4 +def approach(r,i,target,tol=1e-4):
           5 +    step=0.2
           6 +    while step>tol:
           7 +        p=r.pos(i)[:2]; d=target-p; n=np.linalg.norm(d)
           8 +        if n<1e-6: break
           9 +        s=min(step,n); q=r.step(i,*(d/n*s))[:2]
          10 +        if np.allclose(q,p,atol=1e-9): step/=2
          11 +    return r.pos(i)
          12 +def run(dths,label):
          13 +    r=R(0)
          14 +    r.path(0,[(1.0,-1.0),(c[0]+RAD,c[1])])
          15 +    for d in dths: r.step(0,0,0,d)
          16 +    th=r.pos(0)[2]
          17 +    res=[]
          18 +    for k in range(0,72):
          19 +        a=np.deg2rad(k*5)
          20 +        S=c+RAD*np.array([np.cos(a),np.sin(a)])
          21 +        if not r.goto(0,*S): print('nav fail',k,r.pos(0)); break
          22 +        p=approach(r,0,c)
          23 +        rel=p[:2]-c
          24 +        res.append((k*5,rel[0],rel[1]))
          25 +        r.goto(0,*S)
          26 +    print(label,'theta=%.4f'%th)
          27 +    for a,x,y in res: print('%3d %.4f %.4f  r=%.4f'%(a,x,y,np.hypot(x,y)))
          28 +    r.env.close()
          29 +mode=sys.argv[1]
          30 +if mode=='0': run([],'th=pi')
          31 +if mode=='1': run([0.4],'th=pi+0.4')
          32 +if mode=='2': run([0.4,0.4,0.4,0.37079633],'th=pi/2 ish')
diff --git a/probe_col_rays_0.txt b/probe_col_rays_0.txt
new file mode 100644
index 0000000..16dcf8a
--- /dev/null
+++ b/probe_col_rays_0.txt
@@ -0,0 +1,73 @@
           1 +th=pi theta=-3.1416
           2 +  0 0.2331 -0.0000  r=0.2331
           3 +  5 0.2285 0.0200  r=0.2294
           4 + 10 0.2242 0.0395  r=0.2276
           5 + 15 0.2199 0.0589  r=0.2276
           6 + 20 0.2172 0.0791  r=0.2311
           7 + 25 0.2173 0.1013  r=0.2397
           8 + 30 0.2173 0.1254  r=0.2509
           9 + 35 0.2133 0.1494  r=0.2604
          10 + 40 0.2077 0.1743  r=0.2712
          11 + 45 0.2017 0.2017  r=0.2852
          12 + 50 0.1929 0.2299  r=0.3001
          13 + 55 0.1609 0.2298  r=0.2805
          14 + 60 0.1328 0.2299  r=0.2655
          15 + 65 0.1072 0.2298  r=0.2536
          16 + 70 0.0837 0.2300  r=0.2448
          17 + 75 0.0628 0.2344  r=0.2427
          18 + 80 0.0417 0.2365  r=0.2401
          19 + 85 0.0206 0.2353  r=0.2362
          20 + 90 -0.0000 0.2329  r=0.2329
          21 + 95 -0.0201 0.2299  r=0.2307
          22 +100 -0.0405 0.2299  r=0.2335
          23 +105 -0.0616 0.2299  r=0.2380
          24 +110 -0.0837 0.2299  r=0.2446
          25 +115 -0.1072 0.2298  r=0.2536
          26 +120 -0.1312 0.2272  r=0.2624
          27 +125 -0.1553 0.2218  r=0.2708
          28 +130 -0.1812 0.2160  r=0.2819
          29 +135 -0.2096 0.2096  r=0.2964
          30 +140 -0.2184 0.1832  r=0.2850
          31 +145 -0.2453 0.1718  r=0.2995
          32 +150 -0.2453 0.1416  r=0.2833
          33 +155 -0.2454 0.1144  r=0.2708
          34 +160 -0.2455 0.0893  r=0.2612
          35 +165 -0.2453 0.0657  r=0.2540
          36 +170 -0.2453 0.0433  r=0.2491
          37 +175 -0.2454 0.0215  r=0.2464
          38 +180 -0.2454 -0.0000  r=0.2454
          39 +185 -0.2454 -0.0215  r=0.2464
          40 +190 -0.2453 -0.0433  r=0.2491
          41 +195 -0.2453 -0.0657  r=0.2540
          42 +200 -0.2455 -0.0893  r=0.2612
          43 +205 -0.2426 -0.1131  r=0.2677
          44 +210 -0.2372 -0.1370  r=0.2739
          45 +215 -0.2316 -0.1621  r=0.2827
          46 +220 -0.2255 -0.1892  r=0.2944
          47 +225 -0.2011 -0.2011  r=0.2845
          48 +230 -0.1924 -0.2293  r=0.2993
          49 +235 -0.1606 -0.2293  r=0.2800
          50 +240 -0.1324 -0.2293  r=0.2647
          51 +245 -0.1069 -0.2293  r=0.2530
          52 +250 -0.0835 -0.2293  r=0.2440
          53 +255 -0.0627 -0.2338  r=0.2421
          54 +260 -0.0416 -0.2359  r=0.2395
          55 +265 -0.0205 -0.2347  r=0.2356
          56 +270 -0.0000 -0.2325  r=0.2325
          57 +275 0.0201 -0.2293  r=0.2302
          58 +280 0.0404 -0.2294  r=0.2329
          59 +285 0.0614 -0.2293  r=0.2374
          60 +290 0.0835 -0.2293  r=0.2440
          61 +295 0.1069 -0.2293  r=0.2530
          62 +300 0.1310 -0.2269  r=0.2620
          63 +305 0.1551 -0.2215  r=0.2704
          64 +310 0.1810 -0.2157  r=0.2815
          65 +315 0.2093 -0.2093  r=0.2960
          66 +320 0.2172 -0.1822  r=0.2835
          67 +325 0.2172 -0.1521  r=0.2651
          68 +330 0.2173 -0.1254  r=0.2509
          69 +335 0.2236 -0.1043  r=0.2468
          70 +340 0.2299 -0.0837  r=0.2446
          71 +345 0.2344 -0.0628  r=0.2427
          72 +350 0.2365 -0.0417  r=0.2401
          73 +355 0.2353 -0.0206  r=0.2362
diff --git a/probe_col_rays_1.txt b/probe_col_rays_1.txt
new file mode 100644
index 0000000..c525854
--- /dev/null
+++ b/probe_col_rays_1.txt
@@ -0,0 +1,73 @@
           1 +th=pi+0.4 theta=-2.7416
           2 +  0 0.2343 -0.0000  r=0.2343
           3 +  5 0.2285 0.0200  r=0.2294
           4 + 10 0.2242 0.0395  r=0.2276
           5 + 15 0.2199 0.0589  r=0.2276
           6 + 20 0.2155 0.0785  r=0.2294
           7 + 25 0.2107 0.0983  r=0.2325
           8 + 30 0.2046 0.1181  r=0.2362
           9 + 35 0.1964 0.1375  r=0.2397
          10 + 40 0.1862 0.1562  r=0.2430
          11 + 45 0.1730 0.1730  r=0.2446
          12 + 50 0.1585 0.1889  r=0.2466
          13 + 55 0.1460 0.2085  r=0.2546
          14 + 60 0.1352 0.2342  r=0.2704
          15 + 65 0.1229 0.2635  r=0.2907
          16 + 70 0.0997 0.2739  r=0.2915
          17 + 75 0.0717 0.2676  r=0.2770
          18 + 80 0.0462 0.2619  r=0.2659
          19 + 85 0.0225 0.2567  r=0.2577
          20 + 90 -0.0000 0.2477  r=0.2477
          21 + 95 -0.0209 0.2390  r=0.2399
          22 +100 -0.0406 0.2305  r=0.2341
          23 +105 -0.0596 0.2225  r=0.2304
          24 +110 -0.0784 0.2154  r=0.2292
          25 +115 -0.0982 0.2105  r=0.2323
          26 +120 -0.1180 0.2044  r=0.2360
          27 +125 -0.1373 0.1961  r=0.2393
          28 +130 -0.1560 0.1859  r=0.2427
          29 +135 -0.1741 0.1741  r=0.2462
          30 +140 -0.1964 0.1648  r=0.2563
          31 +145 -0.2207 0.1545  r=0.2694
          32 +150 -0.2477 0.1430  r=0.2860
          33 +155 -0.2686 0.1253  r=0.2964
          34 +160 -0.2723 0.0991  r=0.2897
          35 +165 -0.2806 0.0752  r=0.2905
          36 +170 -0.2747 0.0484  r=0.2790
          37 +175 -0.2692 0.0235  r=0.2702
          38 +180 -0.2638 -0.0000  r=0.2638
          39 +185 -0.2552 -0.0223  r=0.2561
          40 +190 -0.2463 -0.0434  r=0.2501
          41 +195 -0.2376 -0.0637  r=0.2460
          42 +200 -0.2293 -0.0835  r=0.2440
          43 +205 -0.2210 -0.1030  r=0.2438
          44 +210 -0.2127 -0.1228  r=0.2456
          45 +215 -0.2042 -0.1430  r=0.2493
          46 +220 -0.1953 -0.1639  r=0.2550
          47 +225 -0.1859 -0.1859  r=0.2630
          48 +230 -0.1759 -0.2097  r=0.2737
          49 +235 -0.1649 -0.2356  r=0.2876
          50 +240 -0.1494 -0.2587  r=0.2987
          51 +245 -0.1224 -0.2624  r=0.2895
          52 +250 -0.0995 -0.2734  r=0.2909
          53 +255 -0.0716 -0.2672  r=0.2766
          54 +260 -0.0461 -0.2615  r=0.2655
          55 +265 -0.0224 -0.2561  r=0.2571
          56 +270 -0.0000 -0.2475  r=0.2475
          57 +275 0.0209 -0.2386  r=0.2395
          58 +280 0.0406 -0.2303  r=0.2339
          59 +285 0.0596 -0.2223  r=0.2302
          60 +290 0.0783 -0.2150  r=0.2288
          61 +295 0.0980 -0.2102  r=0.2319
          62 +300 0.1178 -0.2041  r=0.2356
          63 +305 0.1372 -0.1959  r=0.2391
          64 +310 0.1559 -0.1857  r=0.2425
          65 +315 0.1739 -0.1739  r=0.2460
          66 +320 0.1961 -0.1645  r=0.2559
          67 +325 0.2204 -0.1543  r=0.2690
          68 +330 0.2474 -0.1428  r=0.2856
          69 +335 0.2693 -0.1256  r=0.2971
          70 +340 0.2627 -0.0956  r=0.2796
          71 +345 0.2566 -0.0688  r=0.2657
          72 +350 0.2511 -0.0443  r=0.2550
          73 +355 0.2431 -0.0213  r=0.2440
diff --git a/probe_col_rays_2.txt b/probe_col_rays_2.txt
new file mode 100644
index 0000000..0bd3b70
--- /dev/null
+++ b/probe_col_rays_2.txt
@@ -0,0 +1,73 @@
           1 +th=pi/2 ish theta=-1.5708
           2 +  0 0.2331 -0.0000  r=0.2331
           3 +  5 0.2299 0.0201  r=0.2307
           4 + 10 0.2299 0.0405  r=0.2335
           5 + 15 0.2299 0.0616  r=0.2380
           6 + 20 0.2299 0.0837  r=0.2446
           7 + 25 0.2298 0.1072  r=0.2536
           8 + 30 0.2274 0.1313  r=0.2626
           9 + 35 0.2220 0.1554  r=0.2710
          10 + 40 0.2161 0.1813  r=0.2821
          11 + 45 0.2097 0.2097  r=0.2966
          12 + 50 0.1822 0.2172  r=0.2835
          13 + 55 0.1521 0.2172  r=0.2651
          14 + 60 0.1254 0.2173  r=0.2509
          15 + 65 0.1043 0.2236  r=0.2468
          16 + 70 0.0837 0.2300  r=0.2448
          17 + 75 0.0628 0.2344  r=0.2427
          18 + 80 0.0417 0.2365  r=0.2401
          19 + 85 0.0206 0.2353  r=0.2362
          20 + 90 -0.0000 0.2329  r=0.2329
          21 + 95 -0.0200 0.2283  r=0.2292
          22 +100 -0.0395 0.2240  r=0.2274
          23 +105 -0.0589 0.2197  r=0.2274
          24 +110 -0.0791 0.2172  r=0.2311
          25 +115 -0.1012 0.2171  r=0.2395
          26 +120 -0.1254 0.2173  r=0.2509
          27 +125 -0.1494 0.2133  r=0.2604
          28 +130 -0.1743 0.2077  r=0.2712
          29 +135 -0.2016 0.2016  r=0.2850
          30 +140 -0.2293 0.1924  r=0.2993
          31 +145 -0.2293 0.1606  r=0.2800
          32 +150 -0.2293 0.1324  r=0.2647
          33 +155 -0.2293 0.1069  r=0.2530
          34 +160 -0.2295 0.0835  r=0.2442
          35 +165 -0.2338 0.0627  r=0.2421
          36 +170 -0.2359 0.0416  r=0.2395
          37 +175 -0.2347 0.0205  r=0.2356
          38 +180 -0.2323 -0.0000  r=0.2323
          39 +185 -0.2293 -0.0201  r=0.2302
          40 +190 -0.2294 -0.0404  r=0.2329
          41 +195 -0.2293 -0.0614  r=0.2374
          42 +200 -0.2293 -0.0835  r=0.2440
          43 +205 -0.2293 -0.1069  r=0.2530
          44 +210 -0.2267 -0.1309  r=0.2618
          45 +215 -0.2213 -0.1550  r=0.2702
          46 +220 -0.2155 -0.1808  r=0.2813
          47 +225 -0.2091 -0.2091  r=0.2958
          48 +230 -0.1827 -0.2178  r=0.2843
          49 +235 -0.1718 -0.2453  r=0.2995
          50 +240 -0.1416 -0.2453  r=0.2833
          51 +245 -0.1144 -0.2454  r=0.2708
          52 +250 -0.0893 -0.2455  r=0.2612
          53 +255 -0.0657 -0.2453  r=0.2540
          54 +260 -0.0433 -0.2453  r=0.2491
          55 +265 -0.0215 -0.2454  r=0.2464
          56 +270 -0.0000 -0.2454  r=0.2454
          57 +275 0.0215 -0.2454  r=0.2464
          58 +280 0.0433 -0.2453  r=0.2491
          59 +285 0.0657 -0.2453  r=0.2540
          60 +290 0.0893 -0.2455  r=0.2612
          61 +295 0.1132 -0.2428  r=0.2679
          62 +300 0.1371 -0.2374  r=0.2741
          63 +305 0.1623 -0.2317  r=0.2829
          64 +310 0.1894 -0.2257  r=0.2946
          65 +315 0.2011 -0.2011  r=0.2845
          66 +320 0.2299 -0.1929  r=0.3001
          67 +325 0.2300 -0.1610  r=0.2807
          68 +330 0.2299 -0.1328  r=0.2655
          69 +335 0.2298 -0.1072  r=0.2536
          70 +340 0.2299 -0.0837  r=0.2446
          71 +345 0.2344 -0.0628  r=0.2427
          72 +350 0.2365 -0.0417  r=0.2401
          73 +355 0.2353 -0.0206  r=0.2362
diff --git a/probe_col_rr.py b/probe_col_rr.py
new file mode 100644
index 0000000..8dab04a
--- /dev/null
+++ b/probe_col_rr.py
@@ -0,0 +1,5 @@
           1 +from probe_col_lib import R
           2 +from probe_col_bounds import approach
           3 +r=R(2)
           4 +r.goto(0,0.5,-1.75); r.goto(1,-0.5,-1.75)
           5 +print(approach(r,0,(-1,-1.75)), approach(r,1,(1,-1.75)))
diff --git a/probe_col_seeds.py b/probe_col_seeds.py
new file mode 100644
index 0000000..c4cb349
--- /dev/null
+++ b/probe_col_seeds.py
@@ -0,0 +1,8 @@
           1 +from env_client import make_env
           2 +env=make_env()
           3 +for s in range(40):
           4 +    obs,_=env.reset(seed=s)
           5 +    ps=[(obs.get(o,'x'),obs.get(o,'y')) for o in obs if o.type.name=='obstacle' and obs.get(o,'half_x')<0.1]
           6 +    if not any(x<-0.6 and y<-0.3 for x,y in ps): print('lander-clear seed',s)
           7 +    if not any(x>0 and x<0.8 and y>1.0 for x,y in ps) : print('r0 topclear',s)
           8 +env.close()
diff --git a/probe_col_wall.py b/probe_col_wall.py
new file mode 100644
index 0000000..f256633
--- /dev/null
+++ b/probe_col_wall.py
@@ -0,0 +1,19 @@
           1 +from probe_col_lib import R
           2 +from probe_col_bounds import approach
           3 +import numpy as np, sys
           4 +seed=int(sys.argv[1]); i=int(sys.argv[2]); sg=1 if i==0 else -1
           5 +r=R(seed)
           6 +X=0.30*sg; FAR=1.0*sg
           7 +r.goto(i,sg*1.0,-1.2) if i==0 else r.goto(i,-1.0,-1.2)
           8 +r.goto(i,FAR,-2.2); r.goto(i,X,-2.2)
           9 +res=[]
          10 +for y in np.arange(-2.27,1.56,0.05):
          11 +    if not r.goto(i,X,y):
          12 +        # detour
          13 +        r.goto(i,FAR,r.pos(i)[1]); r.goto(i,FAR,y)
          14 +        if not r.goto(i,X,y): res.append((round(y,2),'blk')); continue
          15 +    p=approach(r,i,(-sg*1.0,y),tol=5e-4)
          16 +    res.append((round(y,2),round(p[0],4)))
          17 +    r.goto(i,X,y)
          18 +bad=[t for t in res if t[1]=='blk' or abs(t[1]-sg*0.2271)>0.002]
          19 +print('seed',seed,'rover',i,'n',len(res),'non-standard:',bad)
diff --git a/probe_send_a.py b/probe_send_a.py
new file mode 100644
index 0000000..caa02e3
--- /dev/null
+++ b/probe_send_a.py
@@ -0,0 +1,5 @@
           1 +from probe_send_lib import *
           2 +e=E(0)
           3 +print(e.pose(1)); e.act(1,(0.1,0,0)); print('dx+0.1 at th0',e.pose(1))
           4 +e.act(1,(0,0,0.4)); e.act(1,(0.1,0,0)); print('dx+0.1 at th0.4',e.pose(1))
           5 +print(e.last)
diff --git a/probe_send_b.py b/probe_send_b.py
new file mode 100644
index 0000000..eafd6fa
--- /dev/null
+++ b/probe_send_b.py
@@ -0,0 +1,9 @@
           1 +from probe_send_lib import *
           2 +e=E(0)
           3 +sx,sy=e.g('sample3','x'),e.g('sample3','y'); print('s3',sx,sy)
           4 +ok=e.goto(1,sx-0.5,sy); print('reached',ok,e.pose(1),e.t)
           5 +for d in [0.40,0.35,0.30,0.28,0.26,0.255,0.25,0.245,0.24,0.22,0.2,0.1,0.0]:
           6 +    e.goto(1,sx-d,sy)
           7 +    f0=e.flags(); e.act(1,(0,0,0),SEL['sample']); f1=e.flags()
           8 +    print(d,e.pose(1),diff(f0,f1))
           9 +    if diff(f0,f1): break
diff --git a/probe_send_c.py b/probe_send_c.py
new file mode 100644
index 0000000..9f21ff9
--- /dev/null
+++ b/probe_send_c.py
@@ -0,0 +1,22 @@
           1 +from probe_send_lib import *
           2 +e=E(0)
           3 +sx,sy=e.g('sample3','x'),e.g('sample3','y')
           4 +e.goto(1,sx-0.5,sy)
           5 +e.goto(1,sx-0.4,sy)
           6 +# motion+op same step: move 0.2 into range and sample
           7 +f0=e.flags(); e.act(1,(0.2,0,0),SEL['sample']); f1=e.flags(); print('move-into-range+sample',e.pose(1),diff(f0,f1))
           8 +# sample again with store full
           9 +f0=e.flags(); e.act(1,(0,0,0),SEL['sample']); print('sample when full',diff(f0,e.flags()))
          10 +f0=e.flags(); e.act(1,(0,0,0),SEL['drop']); print('drop',diff(f0,e.flags()))
          11 +f0=e.flags(); e.act(1,(0,0,0),SEL['sample']); print('resample same',diff(f0,e.flags()))
          12 +f0=e.flags(); e.act(1,(0,0,0),SEL['drop']); print('drop',diff(f0,e.flags()))
          13 +# move out of range + sample in same step
          14 +f0=e.flags(); e.act(1,(-0.2,0,0),SEL['sample']); print('move-out+sample',e.pose(1),diff(f0,e.flags()))
          15 +f0=e.flags(); e.act(1,(0,0,0),SEL['drop']); print('drop',diff(f0,e.flags()))
          16 +# drop with empty store
          17 +f0=e.flags(); e.act(1,(0,0,0),SEL['drop']); print('drop empty',diff(f0,e.flags()))
          18 +# selector band test: -0.7, -0.95
          19 +e.goto(1,sx-0.1,sy)
          20 +for v in [-1.0,-0.7,-0.67,-0.66]:
          21 +    f0=e.flags(); e.act(1,(0,0,0),v); d=diff(f0,e.flags()); print('sel',v,d!={} and 'sampled')
          22 +    e.act(1,(0,0,0),SEL['drop'])
diff --git a/probe_send_d.py b/probe_send_d.py
new file mode 100644
index 0000000..c89b48d
--- /dev/null
+++ b/probe_send_d.py
@@ -0,0 +1,17 @@
           1 +from probe_send_lib import *
           2 +import sys
           3 +seed=0; start=(float(sys.argv[1]),float(sys.argv[2])); stepl=float(sys.argv[3]) if len(sys.argv)>3 else 0.02
           4 +e=E(seed)
           5 +sx,sy=e.g('sample3','x'),e.g('sample3','y')
           6 +e.goto(1,sx-0.5,sy); e.goto(1,sx-0.2,sy); e.act(1,(0,0,0),SEL['sample']); e.act(1,(0,0,0),SEL['drop'])
           7 +print('analyzed',e.feats('sample3'))
           8 +for wp in [start]:
           9 +    print("nav",wp,nav(e,1,wp),e.pose(1),e.t)
          10 +L=np.array([-1.9,-2.0])
          11 +p=np.array(e.pose(1)[:2]); dirv=(L-p)/np.linalg.norm(L-p)
          12 +for i in range(400):
          13 +    p=np.array(e.pose(1)[:2]); d=np.linalg.norm(p-L)
          14 +    f0=e.flags(); e.act(1,(0,0,0),SEL['send']); df=diff(f0,e.flags())
          15 +    if df: print('SENT at',p,'dist',round(d,4),df); break
          16 +    mv=dirv*stepl; e.act(1,(mv[0],mv[1],0))
          17 +    if np.linalg.norm(np.array(e.pose(1)[:2])-p)<1e-6: print('blocked at',p,d); break
diff --git a/probe_send_e.py b/probe_send_e.py
new file mode 100644
index 0000000..eb06e21
--- /dev/null
+++ b/probe_send_e.py
@@ -0,0 +1,4 @@
           1 +from probe_send_lib import *
           2 +e=E(0)
           3 +p=plan(e,1,(-1.25,2.25)); print(p is None, p and len(p))
           4 +p=plan(e,1,(-1.25,1.0)); print(p is None, p and len(p))
diff --git a/probe_send_f.py b/probe_send_f.py
new file mode 100644
index 0000000..19a6030
--- /dev/null
+++ b/probe_send_f.py
@@ -0,0 +1,17 @@
           1 +from probe_send_lib import *
           2 +e=E(1)
           3 +sx,sy=e.g('sample3','x'),e.g('sample3','y')
           4 +print('nav',nav(e,0,(sx+0.15,sy)),e.pose(0))
           5 +f0=e.flags(); e.act(0,(0,0,0),SEL['sample']); print(diff(f0,e.flags()))
           6 +e.act(0,(0,0,0),SEL['drop'])
           7 +L=np.array([-1.9,-2.0])
           8 +pts=[(0.24,y) for y in np.arange(-2.25,1.6,0.25)]+[(x,-2.25) for x in (0.5,1.0)]+[(x,-1.0) for x in (0.5,1.0,1.5)]
           9 +pts.sort(key=lambda p:np.hypot(p[0]-L[0],p[1]-L[1]))
          10 +for p in pts:
          11 +    ok=nav(e,0,p)
          12 +    f0=e.flags(); e.act(0,(0,0,0),SEL['send'])
          13 +    for th in (0.0,1.57,3.14,-1.57):
          14 +        e.turn(0,th); e.act(0,(0,0,0),SEL['send'])
          15 +    df=diff(f0,e.flags())
          16 +    print(p,ok,e.pose(0),round(np.hypot(e.pose(0)[0]-L[0],e.pose(0)[1]-L[1]),3),'SENT' if any(k.startswith('sample') for k in df) else '')
          17 +print(e.t)
diff --git a/probe_send_g.py b/probe_send_g.py
new file mode 100644
index 0000000..a1cffcc
--- /dev/null
+++ b/probe_send_g.py
@@ -0,0 +1,20 @@
           1 +from probe_send_lib import *
           2 +import sys
           3 +k=int(sys.argv[1]); tx,ty=float(sys.argv[2]),float(sys.argv[3])
           4 +seed=1 if k==0 else 0; sn='sample3'
           5 +e=E(seed)
           6 +sx,sy=e.g(sn,'x'),e.g(sn,'y')
           7 +off=0.15 if k==0 else -0.15
           8 +nav(e,k,(sx+off,sy)); e.act(k,(0,0,0),SEL['sample']); e.act(k,(0,0,0),SEL['drop'])
           9 +assert e.g(sn,f'analyzed_rover{k}')==1
          10 +import os
          11 +if os.environ.get("MOVE"): print("moved other",nav(e,1-k,tuple(map(float,os.environ["MOVE"].split(",")))))
          12 +ok=nav(e,k,(tx,ty)); L=(-1.9,-2.0)
          13 +res=[]
          14 +for th in eval(sys.argv[4]) if len(sys.argv)>4 else [None,0.0,1.57,3.14,-1.57]:
          15 +    if th is not None: e.turn(k,th)
          16 +    e.act(k,(0,0,0),SEL['send'])
          17 +    if e.g(sn,'received_analysis')==1: res.append(('SENT',e.pose(k)[2])); break
          18 +    res.append(('no',e.pose(k)[2]))
          19 +P=e.pose(k)
          20 +print(f'rover{k} target {(tx,ty)} reached {ok} pose {P} dist {np.hypot(P[0]-L[0],P[1]-L[1]):.3f}',res)
diff --git a/probe_send_k.py b/probe_send_k.py
new file mode 100644
index 0000000..5c25194
--- /dev/null
+++ b/probe_send_k.py
@@ -0,0 +1,12 @@
           1 +from probe_send_lib import *
           2 +e=E(1)
           3 +# at_home tolerance
           4 +for dx in [0.01,0.05,0.1,0.15,0.2,0.25,0.3]:
           5 +    e.goto(1,-1.0+dx,-1.75); print('dx',dx,'at_home',e.g('rover1','at_home'))
           6 +e.goto(1,-1.0,-1.75)
           7 +for dy in [0.05,0.1,0.15,0.2,0.3]:
           8 +    e.goto(1,-1.0,-1.75+dy); print('dy',dy,'at_home',e.g('rover1','at_home'))
           9 +e.goto(1,-1.0,-1.75)
          10 +for th in [0.1,0.3,0.6,1.0,1.57,3.14]:
          11 +    e.turn(1,th); print('th',th,'at_home',e.g('rover1','at_home'))
          12 +e.turn(1,0.0); print('back',e.pose(1),e.g('rover1','at_home'))
diff --git a/probe_send_lib.py b/probe_send_lib.py
new file mode 100644
index 0000000..91afdbc
--- /dev/null
+++ b/probe_send_lib.py
@@ -0,0 +1,82 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +SEL=dict(sample=-0.8333,cal=-0.5,image=-0.1667,noop=0.0,send=0.5,drop=0.8333)
           4 +class E:
           5 +    def __init__(s,seed=0):
           6 +        s.env=make_env(); s.obs,s.info=s.env.reset(seed=seed); s.t=0; s.last=None
           7 +    def g(s,name,f): return float(s.obs.get(s.obs.get_object_from_name(name),f))
           8 +    def objs(s,typ): return [o.name for o in s.obs if o.type.name==typ]
           9 +    def feats(s,name): o=s.obs.get_object_from_name(name); return [round(float(v),4) for v in s.obs.data[o]]
          10 +    def pose(s,k): r=f'rover{k}'; return (round(s.g(r,'x'),4),round(s.g(r,'y'),4),round(s.g(r,'theta'),4))
          11 +    def step(s,a0=(0,0,0,0),a1=(0,0,0,0)):
          12 +        a=np.array(list(a0)+list(a1),dtype=np.float32)
          13 +        s.obs,r,te,tr,inf=s.env.step(a); s.t+=1; s.last=(r,te,tr,inf); return s.last
          14 +    def act(s,k,mv=(0,0,0),sel=0.0):
          15 +        a=list(mv)+[sel]; z=[0,0,0,0]
          16 +        return s.step(a,z) if k==0 else s.step(z,a)
          17 +    def goto(s,k,x,y,tol=0.002,maxit=300):
          18 +        for i in range(maxit):
          19 +            px,py,_=s.pose(k); dx,dy=x-px,y-py
          20 +            if abs(dx)<tol and abs(dy)<tol: return True
          21 +            mx,my=np.clip(dx,-0.2,0.2),np.clip(dy,-0.2,0.2)
          22 +            s.act(k,(mx,my,0))
          23 +            nx,ny,_=s.pose(k)
          24 +            if abs(nx-px)<1e-6 and abs(ny-py)<1e-6:
          25 +                # blocked: try axis separately
          26 +                s.act(k,(mx,0,0)); s.act(k,(0,my,0))
          27 +                nx2,ny2,_=s.pose(k)
          28 +                if abs(nx2-px)<1e-6 and abs(ny2-py)<1e-6: return False
          29 +        return False
          30 +    def turn(s,k,th):
          31 +        for i in range(50):
          32 +            d=(th-s.pose(k)[2]+np.pi)%(2*np.pi)-np.pi
          33 +            if abs(d)<1e-4: return
          34 +            s.act(k,(0,0,np.clip(d,-0.4,0.4)))
          35 +    def flags(s):
          36 +        out={}
          37 +        for o in s.obs:
          38 +            if o.type.name in ('rover','objective','sample'):
          39 +                out[o.name]=s.feats(o.name)
          40 +        return out
          41 +def diff(a,b):
          42 +    return {k:(a[k],b[k]) for k in a if a[k]!=b[k]}
          43 +
          44 +import heapq
          45 +def plan(e,k,goal,clr=0.27,res=0.05):
          46 +    obs=[]
          47 +    for o in e.obs:
          48 +        if o.type.name=='obstacle':
          49 +            n=o.name; obs.append((e.g(n,'x'),e.g(n,'y'),e.g(n,'half_x'),e.g(n,'half_y')))
          50 +    def free(x,y):
          51 +        if abs(x)>2.5-0.2 or abs(y)>2.5-0.2: return False
          52 +        if k==0 and x<0.24: return False
          53 +        if k==1 and x>-0.24: return False
          54 +        for ox,oy,hx,hy in obs:
          55 +            if abs(x-ox)<hx+clr and abs(y-oy)<hy+clr: return False
          56 +        return True
          57 +    st=e.pose(k)[:2]
          58 +    toi=lambda p:(int(round(p[0]/res)),int(round(p[1]/res)))
          59 +    s=toi(st); g=toi(goal)
          60 +    pq=[(0,s)]; came={s:None}; cost={s:0}
          61 +    while pq:
          62 +        _,c=heapq.heappop(pq)
          63 +        if c==g: break
          64 +        for dx in (-1,0,1):
          65 +            for dy in (-1,0,1):
          66 +                if dx==dy==0: continue
          67 +                n=(c[0]+dx,c[1]+dy)
          68 +                if not free(n[0]*res,n[1]*res) and n!=g: continue
          69 +                nc=cost[c]+np.hypot(dx,dy)
          70 +                if n not in cost or nc<cost[n]:
          71 +                    cost[n]=nc; came[n]=c; heapq.heappush(pq,(nc+np.hypot(n[0]-g[0],n[1]-g[1]),n))
          72 +    if g not in came: return None
          73 +    path=[]; c=g
          74 +    while c: path.append((c[0]*res,c[1]*res)); c=came[c]
          75 +    return path[::-1]
          76 +def nav(e,k,goal,clr=0.27):
          77 +    path=plan(e,k,goal,clr)
          78 +    if path is None: return False
          79 +    # compress: follow points
          80 +    for p in path[1:]:
          81 +        e.goto(k,*p,maxit=5)
          82 +    return e.goto(k,*goal,maxit=20)
diff --git a/probe_send_m.py b/probe_send_m.py
new file mode 100644
index 0000000..7509e85
--- /dev/null
+++ b/probe_send_m.py
@@ -0,0 +1,9 @@
           1 +from probe_send_lib import *
           2 +e=E(1)
           3 +for r in [0.2,0.21,0.22,0.23,0.24,0.25]:
           4 +    e.goto(1,-1.0+r,-1.75); a=e.g('rover1','at_home')
           5 +    e.goto(1,-1.0+r/np.sqrt(2),-1.75+r/np.sqrt(2)); b=e.g('rover1','at_home')
           6 +    print('r',r,'axis',a,'diag',b)
           7 +e.goto(1,-1.0,-1.75)
           8 +for th in [0.35,0.4,0.45,0.5,0.55,-0.5,-0.55]:
           9 +    e.turn(1,th); print('th',th,e.g('rover1','at_home'))
diff --git a/probe_send_n.py b/probe_send_n.py
new file mode 100644
index 0000000..429a894
--- /dev/null
+++ b/probe_send_n.py
@@ -0,0 +1,10 @@
           1 +from probe_send_lib import *
           2 +e=E(1)
           3 +ox,oy=e.g('objective1','x'),e.g('objective1','y'); print('obj',ox,oy)
           4 +for p in [(-1.2,0.5),(-1.4,1.3),(-1.5,1.5)]:
           5 +    print('nav',p,nav(e,1,p),e.pose(1))
           6 +    for th in [None,np.arctan2(oy-p[1],ox-p[0]),0.0]:
           7 +        if th is not None: e.turn(1,th)
           8 +        f0=e.flags(); e.act(1,(0,0,0),SEL['cal']); d1=diff(f0,e.flags())
           9 +        f0=e.flags(); e.act(1,(0,0,0),SEL['image']); d2=diff(f0,e.flags())
          10 +        print(' th',e.pose(1)[2],'cal',d1,'img',d2)
diff --git a/probe_send_o.py b/probe_send_o.py
new file mode 100644
index 0000000..34c934c
--- /dev/null
+++ b/probe_send_o.py
@@ -0,0 +1,26 @@
           1 +from probe_send_lib import *
           2 +e=E(1)
           3 +orig=e.step
           4 +log=[]
           5 +def st(a0=(0,0,0,0),a1=(0,0,0,0)):
           6 +    r=orig(a0,a1)
           7 +    if r[1] or r[2]: log.append((e.t,r)); print('TERM/TRUNC at',e.t,r)
           8 +    return r
           9 +e.step=st
          10 +def sendtry(k,names):
          11 +    for th in [None,0.0,1.57,3.14,-1.57]:
          12 +        if th is not None: e.turn(k,th)
          13 +        e.act(k,(0,0,0),SEL['send'])
          14 +def samp(k,n,off):
          15 +    sx,sy=e.g(n,'x'),e.g(n,'y'); print('nav',n,nav(e,k,(sx+off[0],sy+off[1])))
          16 +    e.act(k,(0,0,0),SEL['sample']); e.act(k,(0,0,0),SEL['drop']); print(n,e.feats(n))
          17 +samp(1,'sample1',(0.15,0))
          18 +samp(1,'sample5',(0.15,0))
          19 +print('nav',nav(e,1,(-1.4,1.3))); e.act(1,(0,0,0),SEL['cal']); e.act(1,(0,0,0),SEL['image']); print('obj1',e.feats('objective1'))
          20 +sendtry(1,None); print('after send r1', e.feats('sample1'),e.feats('sample5'),e.feats('objective1'))
          21 +print('nav home',nav(e,1,(-1.0,-1.75))); e.turn(1,0.0); print('r1',e.feats('rover1'),'t',e.t)
          22 +print('nav',nav(e,0,(1.5,1.4))); e.act(0,(0,0,0),SEL['cal']); e.act(0,(0,0,0),SEL['image']); print('obj0',e.feats('objective0'))
          23 +print('nav',nav(e,0,(0.5,-1.5))); sendtry(0,None); print('obj0',e.feats('objective0'))
          24 +print('nav home',nav(e,0,(1.0,-1.75))); print('r0',e.feats('rover0'),e.t,e.last)
          25 +e.turn(0,3.14159); print('r0',e.feats('rover0'),e.t,e.last)
          26 +for i in range(3): e.act(0,(0,0,0),0.0); print(e.t,e.last)
diff --git a/probe_send_p.py b/probe_send_p.py
new file mode 100644
index 0000000..e135c36
--- /dev/null
+++ b/probe_send_p.py
@@ -0,0 +1,8 @@
           1 +from probe_send_lib import *
           2 +for s in range(40):
           3 +    e=E(s)
           4 +    ob=[(e.g(n,'x'),e.g(n,'y')) for n in e.objs('objective')]
           5 +    if all(x<0 for x,y in ob):
           6 +        sm=[(n,round(e.g(n,'x'),2),round(e.g(n,'y'),2),e.g(n,'is_soil')) for n in e.objs('sample')]
           7 +        print(s,ob,sm)
           8 +    e.env.close()
diff --git a/probe_send_q.py b/probe_send_q.py
new file mode 100644
index 0000000..f9713ab
--- /dev/null
+++ b/probe_send_q.py
@@ -0,0 +1,6 @@
           1 +from probe_send_lib import *
           2 +e=E(3)
           3 +for i in range(1005):
           4 +    r=e.act(1,(0,0,0),0.0)
           5 +    if r[1] or r[2] or i>=997: print(e.t,r)
           6 +    if r[1] or r[2]: break
diff --git a/probe_vis_a.py b/probe_vis_a.py
new file mode 100644
index 0000000..4170678
--- /dev/null
+++ b/probe_vis_a.py
@@ -0,0 +1,9 @@
           1 +from probe_vis_lib import *
           2 +e=E(1)
           3 +print(e.rs(0))
           4 +ok=e.path(0,[(1.0,0.0),(2.118,0.0),(2.118,1.0)]); print(ok,e.rs(0))
           5 +# test move frame: does dx move world x with theta=pi?
           6 +for k in range(3):
           7 +    rew=e.step(0,0,0,0,'cal'); print('cal',e.rs(0),rew)
           8 +rew=e.step(0,0,0,0,'img'); print('img',e.rs(0),rew,e.objs())
           9 +rew=e.step(0,0,0,0,'noop'); print(e.rs(0))
diff --git a/probe_vis_b.py b/probe_vis_b.py
new file mode 100644
index 0000000..c4567f2
--- /dev/null
+++ b/probe_vis_b.py
@@ -0,0 +1,12 @@
           1 +from probe_vis_lib import *
           2 +e=E(1)
           3 +e.path(0,[(1.0,0.0),(2.118,0.0),(2.118,0.2)])
           4 +o=e.objs()['objective0']
           5 +y=0.2
           6 +while y>-0.3:
           7 +    e.goto(0,2.118,y)
           8 +    e.step(0,0,0,0,'cal'); c=e.rs(0)['calibrated']
           9 +    e.step(0,0,0,0,'img'); c2=e.rs(0)['calibrated']; hi=e.objs()['objective0']['have_image_rover0']
          10 +    st=e.rs(0); d=math.hypot(o['x']-st['x'],o['y']-st['y'])
          11 +    print('y=%.3f d2=%.4f d3=%.4f cal=%d after_img=%d img=%d'%(st['y'],d,math.sqrt(d*d+o['z']**2),c,c2,hi))
          12 +    y-=0.02
diff --git a/probe_vis_c.py b/probe_vis_c.py
new file mode 100644
index 0000000..f2097ab
--- /dev/null
+++ b/probe_vis_c.py
@@ -0,0 +1,17 @@
           1 +from probe_vis_lib import *
           2 +for k in range(8):
           3 +    th=-math.pi+k*math.pi/4
           4 +    e=E(1)
           5 +    e.path(0,[(1.0,0.0),(2.118,0.0)])
           6 +    e.turn(0,th)
           7 +    o=e.objs()['objective0']
           8 +    lo,hi=0.2,-0.3
           9 +    for it in range(16):
          10 +        y=(lo+hi)/2
          11 +        e.goto(0,2.118,y,tol=1e-7)
          12 +        e.step(0,0,0,0,'cal'); c=e.rs(0)['calibrated']; e.step(0,0,0,0,'img')
          13 +        if c: lo=y
          14 +        else: hi=y
          15 +    st=e.rs(0)
          16 +    print('theta=%.3f y*=%.5f d2=%.5f'%(st['theta'],lo,math.hypot(o['x']-st['x'],o['y']-lo)))
          17 +    e.close()
diff --git a/probe_vis_d.py b/probe_vis_d.py
new file mode 100644
index 0000000..f6593af
--- /dev/null
+++ b/probe_vis_d.py
@@ -0,0 +1,9 @@
           1 +from probe_vis_lib import *
           2 +e=E(1)
           3 +e.path(0,[(1.0,0.0),(2.118,0.0),(2.118,1.0)])
           4 +o=e.objs()['objective0']
           5 +for k in range(16):
           6 +    th=-math.pi+k*2*math.pi/16
           7 +    e.turn(0,th)
           8 +    e.step(0,0,0,0,'cal'); c=e.rs(0)['calibrated']; e.step(0,0,0,0,'img')
           9 +    print('th=%.3f cal=%d'%(e.rs(0)['theta'],c))
diff --git a/probe_vis_d1.json b/probe_vis_d1.json
new file mode 100644
index 0000000..6a737bb
--- /dev/null
+++ b/probe_vis_d1.json
@@ -0,0 +1 @@
           1 +{"seed": 4, "obj": "objective2", "data": [[-2.259999990463257, 0.6200000047683716, 3.141592502593994, 1], [-2.259999990463257, 0.6200000047683716, -2.356194496154785, 1], [-2.259999990463257, 0.6200000047683716, -1.5707963705062866, 1], [-2.259999990463257, 0.6200000047683716, -0.7853981256484985, 1], [-2.259999990463257, 0.6200000047683716, -1.192092824453539e-08, 1], [-2.259999990463257, 0.6200000047683716, 0.7853981852531433, 1], [-2.259999990463257, 0.6200000047683716, 1.570796251296997, 1], [-2.259999990463257, 0.6200000047683716, 2.356194496154785, 0], [-2.240000009536743, 0.6200000047683716, -3.141592502593994, 1], [-2.240000009536743, 0.6200000047683716, -2.356194496154785, 1], [-2.240000009536743, 0.6200000047683716, -1.5707963705062866, 1], [-2.240000009536743, 0.6200000047683716, -0.7853981256484985, 1], [-2.240000009536743, 0.6200000047683716, -3.9683722974359625e-09, 1], [-2.240000009536743, 0.6200000047683716, 0.7853981256484985, 1], [-2.240000009536743, 0.6200000047683716, 1.5707963705062866, 1], [-2.240000009536743, 0.6200000047683716, 2.356194496154785, 0], [-2.2200000286102295, 0.6200000047683716, 3.141592502593994, 1], [-2.2200000286102295, 0.6200000047683716, -2.356194496154785, 1], [-2.2200000286102295, 0.6200000047683716, -1.5707963705062866, 1], [-2.2200000286102295, 0.6200000047683716, -0.7853981256484985, 1], [-2.2200000286102295, 0.6200000047683716, 3.984182317395835e-09, 1], [-2.2200000286102295, 0.6200000047683716, 0.7853981256484985, 1], [-2.2200000286102295, 0.6200000047683716, 1.5707963705062866, 0], [-2.2200000286102295, 0.6200000047683716, 2.356194496154785, 0], [-2.200000047683716, 0.6200000047683716, 3.141592502593994, 1], [-2.200000047683716, 0.6200000047683716, -2.356194496154785, 1], [-2.200000047683716, 0.6200000047683716, -1.5707963705062866, 1], [-2.200000047683716, 0.6200000047683716, -0.7853981256484985, 1], [-2.200000047683716, 0.6200000047683716, 1.1936737820406051e-08, 1], [-2.200000047683716, 0.6200000047683716, 0.7853981852531433, 1], [-2.200000047683716, 0.6200000047683716, 1.570796251296997, 0], [-2.200000047683716, 0.6200000047683716, 2.356194496154785, 0], [-2.180000066757202, 0.6200000047683716, 3.141592502593994, 1], [-2.180000066757202, 0.6200000047683716, -2.356194496154785, 1], [-2.180000066757202, 0.6200000047683716, -1.5707963705062866, 1], [-2.180000066757202, 0.6200000047683716, -0.7853981256484985, 1], [-2.180000066757202, 0.6200000047683716, -9.913028620189834e-09, 1], [-2.180000066757202, 0.6200000047683716, 0.7853981852531433, 1], [-2.180000066757202, 0.6200000047683716, 1.570796251296997, 0], [-2.180000066757202, 0.6200000047683716, 2.356194496154785, 0], [-2.1600000858306885, 0.6200000047683716, -3.141592502593994, 1], [-2.1600000858306885, 0.6200000047683716, -2.356194496154785, 1], [-2.1600000858306885, 0.6200000047683716, -1.5707963705062866, 1], [-2.1600000858306885, 0.6200000047683716, -0.7853981256484985, 1], [-2.1600000858306885, 0.6200000047683716, -1.9604726730904076e-09, 1], [-2.1600000858306885, 0.6200000047683716, 0.7853981256484985, 1], [-2.1600000858306885, 0.6200000047683716, 1.5707963705062866, 0], [-2.1600000858306885, 0.6200000047683716, 2.356194496154785, 0], [-2.0999999046325684, 0.6200000047683716, 3.141592502593994, 1], [-2.0999999046325684, 0.6200000047683716, -2.356194496154785, 1], [-2.0999999046325684, 0.6200000047683716, -1.5707963705062866, 1], [-2.0999999046325684, 0.6200000047683716, -0.7853981256484985, 1], [-2.0999999046325684, 0.6200000047683716, 5.9920819417413895e-09, 1], [-2.0999999046325684, 0.6200000047683716, 0.7853981852531433, 0], [-2.0999999046325684, 0.6200000047683716, 1.5707963705062866, 0], [-2.0999999046325684, 0.6200000047683716, 2.356194496154785, 0], [-2.0799999237060547, 0.6200000047683716, 2.756194591522217, 0], [-2.0799999237060547, 0.6200000047683716, 2.756194591522217, 0], [-2.0799999237060547, 0.6200000047683716, 2.756194591522217, 0], [-2.0799999237060547, 0.6200000047683716, 2.756194591522217, 0], [-2.0799999237060547, 0.6200000047683716, 2.356194496154785, 0], [-2.0799999237060547, 0.6200000047683716, 2.356194496154785, 0], [-2.0799999237060547, 0.6200000047683716, 2.356194496154785, 0], [-2.0799999237060547, 0.6200000047683716, 2.356194496154785, 0], [-2.059999942779541, 0.6199999451637268, 2.756194591522217, 0], [-2.059999942779541, 0.6199999451637268, 2.756194591522217, 0], [-2.059999942779541, 0.6199999451637268, 2.756194591522217, 0], [-2.059999942779541, 0.6199999451637268, 2.756194591522217, 0], [-2.059999942779541, 0.6199999451637268, 2.356194496154785, 0], [-2.059999942779541, 0.6199999451637268, 2.356194496154785, 0], [-2.059999942779541, 0.6199999451637268, 2.356194496154785, 0], [-2.059999942779541, 0.6199999451637268, 2.356194496154785, 0], [-2.0399999618530273, 0.6200000047683716, 2.356194496154785, 0], [-2.0399999618530273, 0.6200000047683716, 2.356194496154785, 0], [-2.0399999618530273, 0.6200000047683716, 2.356194496154785, 0], [-2.0399999618530273, 0.6200000047683716, 2.356194496154785, 0], [-2.0399999618530273, 0.6200000047683716, 2.356194496154785, 0], [-2.0399999618530273, 0.6200000047683716, 2.356194496154785, 0], [-2.0399999618530273, 0.6200000047683716, 2.356194496154785, 0], [-2.0399999618530273, 0.6200000047683716, 2.356194496154785, 0], [-1.5, 0.75, 3.141592502593994, 1], [-1.5, 0.75, -2.356194496154785, 1], [-1.5, 0.75, -1.5707963705062866, 1], [-1.5, 0.75, -0.7853981256484985, 1], [-1.5, 0.75, 1.3944637444751606e-08, 1], [-1.5, 0.75, 0.7853981852531433, 1], [-1.5, 0.75, 1.570796251296997, 1], [-1.5, 0.75, 2.356194496154785, 1], [-1.5199999809265137, 0.75, 3.141592502593994, 1], [-1.5199999809265137, 0.75, -2.356194496154785, 1], [-1.5199999809265137, 0.75, -1.5707963705062866, 1], [-1.5199999809265137, 0.75, -0.7853981256484985, 1], [-1.5199999809265137, 0.75, -7.90512899584428e-09, 1], [-1.5199999809265137, 0.75, 0.7853981256484985, 1], [-1.5199999809265137, 0.75, 1.5707963705062866, 1], [-1.5199999809265137, 0.75, 2.356194496154785, 1], [-1.5399999618530273, 0.75, 3.141592502593994, 1], [-1.5399999618530273, 0.75, -2.356194496154785, 1], [-1.5399999618530273, 0.75, -1.5707963705062866, 1], [-1.5399999618530273, 0.75, -0.7853981256484985, 1], [-1.5399999618530273, 0.75, 4.742739534435714e-11, 1], [-1.5399999618530273, 0.75, 0.7853981256484985, 1], [-1.5399999618530273, 0.75, 1.5707963705062866, 1], [-1.5399999618530273, 0.75, 2.356194496154785, 1], [-1.5600000619888306, 0.75, 3.141592502593994, 1], [-1.5600000619888306, 0.75, -2.356194496154785, 1], [-1.5600000619888306, 0.75, -1.5707963705062866, 1], [-1.5600000619888306, 0.75, -0.7853981256484985, 1], [-1.5600000619888306, 0.75, 7.999982898354574e-09, 1], [-1.5600000619888306, 0.75, 0.7853981852531433, 1], [-1.5600000619888306, 0.75, 1.5707963705062866, 1], [-1.5600000619888306, 0.75, 2.356194496154785, 1], [-1.5799999237060547, 0.75, 3.141592502593994, 1], [-1.5799999237060547, 0.75, -2.356194496154785, 1], [-1.5799999237060547, 0.75, -1.5707963705062866, 1], [-1.5799999237060547, 0.75, -0.7853981256484985, 1], [-1.5799999237060547, 0.75, -1.3849783542241312e-08, 1], [-1.5799999237060547, 0.75, 0.7853981852531433, 1], [-1.5799999237060547, 0.75, 1.570796251296997, 1], [-1.5799999237060547, 0.75, 2.356194496154785, 1], [-1.600000023841858, 0.75, 3.141592502593994, 1], [-1.600000023841858, 0.75, -2.356194496154785, 1], [-1.600000023841858, 0.75, -1.5707963705062866, 1], [-1.600000023841858, 0.75, -0.7853981256484985, 1], [-1.600000023841858, 0.75, -5.897227151052675e-09, 1], [-1.600000023841858, 0.75, 0.7853981256484985, 1], [-1.600000023841858, 0.75, 1.5707963705062866, 1], [-1.600000023841858, 0.75, 2.356194496154785, 1], [-1.6200000047683716, 0.75, 3.141592502593994, 1], [-1.6200000047683716, 0.75, -2.356194496154785, 1], [-1.6200000047683716, 0.75, -1.5707963705062866, 1], [-1.6200000047683716, 0.75, -0.7853981256484985, 1], [-1.6200000047683716, 0.75, 2.0553287960467514e-09, 1], [-1.6200000047683716, 0.75, 0.7853981256484985, 1], [-1.6200000047683716, 0.75, 1.5707963705062866, 1], [-1.6200000047683716, 0.75, 2.356194496154785, 1], [-1.6399999856948853, 0.75, 3.141592502593994, 1], [-1.6399999856948853, 0.75, -2.356194496154785, 1], [-1.6399999856948853, 0.75, -1.5707963705062866, 1], [-1.6399999856948853, 0.75, -0.7853981256484985, 1], [-1.6399999856948853, 0.75, 1.0007884299056968e-08, 1], [-1.6399999856948853, 0.75, 0.7853981852531433, 1], [-1.6399999856948853, 0.75, 1.5707963705062866, 1], [-1.6399999856948853, 0.75, 2.356194496154785, 1], [-1.659999966621399, 0.75, 3.141592502593994, 1], [-1.659999966621399, 0.75, -2.356194496154785, 1], [-1.659999966621399, 0.75, -1.5707963705062866, 1], [-1.659999966621399, 0.75, -0.7853981256484985, 1], [-1.659999966621399, 0.75, -1.1841882141538917e-08, 1], [-1.659999966621399, 0.75, 0.7853981852531433, 1], [-1.659999966621399, 0.75, 1.570796251296997, 1], [-1.659999966621399, 0.75, 2.356194496154785, 1], [-1.6800000667572021, 0.75, -3.141592502593994, 1], [-1.6800000667572021, 0.75, -2.356194496154785, 1], [-1.6800000667572021, 0.75, -1.5707963705062866, 1], [-1.6800000667572021, 0.75, -0.7853981256484985, 1], [-1.6800000667572021, 0.75, -3.889326194439491e-09, 1], [-1.6800000667572021, 0.75, 0.7853981256484985, 1], [-1.6800000667572021, 0.75, 1.5707963705062866, 1], [-1.6800000667572021, 0.75, 2.356194496154785, 1], [-1.6999999284744263, 0.75, 3.141592502593994, 1], [-1.6999999284744263, 0.75, -2.356194496154785, 1], [-1.6999999284744263, 0.75, -1.5707963705062866, 1], [-1.6999999284744263, 0.75, -0.7853981256484985, 1], [-1.6999999284744263, 0.75, 4.063228420392306e-09, 1], [-1.6999999284744263, 0.75, 0.7853981256484985, 1], [-1.6999999284744263, 0.75, 1.5707963705062866, 1], [-1.6999999284744263, 0.75, 2.356194496154785, 1], [-1.7200000286102295, 0.75, 3.141592502593994, 1], [-1.7200000286102295, 0.75, -2.356194496154785, 1], [-1.7200000286102295, 0.75, -1.5707963705062866, 1], [-1.7200000286102295, 0.75, -0.7853981256484985, 1], [-1.7200000286102295, 0.75, 1.2015783923402523e-08, 1], [-1.7200000286102295, 0.75, 0.7853981852531433, 1], [-1.7200000286102295, 0.75, 1.570796251296997, 1], [-1.7200000286102295, 0.75, 2.356194496154785, 1], [-1.7400000095367432, 0.75, 3.141592502593994, 1], [-1.7400000095367432, 0.75, -2.356194496154785, 1], [-1.7400000095367432, 0.75, -1.5707963705062866, 1], [-1.7400000095367432, 0.75, -0.7853981256484985, 1], [-1.7400000095367432, 0.75, -9.833982517193363e-09, 1], [-1.7400000095367432, 0.75, 0.7853981852531433, 1], [-1.7400000095367432, 0.75, 1.570796251296997, 1], [-1.7400000095367432, 0.75, 2.356194496154785, 1], [-1.7599999904632568, 0.75, -3.141592502593994, 1], [-1.7599999904632568, 0.75, -2.356194496154785, 1], [-1.7599999904632568, 0.75, -1.5707963705062866, 1], [-1.7599999904632568, 0.75, -0.7853981256484985, 1], [-1.7599999904632568, 0.75, -1.881426570093936e-09, 1], [-1.7599999904632568, 0.75, 0.7853981256484985, 1], [-1.7599999904632568, 0.75, 1.5707963705062866, 1], [-1.7599999904632568, 0.75, 2.356194496154785, 1], [-1.7799999713897705, 0.75, 3.141592502593994, 1], [-1.7799999713897705, 0.75, -2.356194496154785, 1], [-1.7799999713897705, 0.75, -1.5707963705062866, 1], [-1.7799999713897705, 0.75, -0.7853981256484985, 1], [-1.7799999713897705, 0.75, 6.071128044737861e-09, 1], [-1.7799999713897705, 0.75, 0.7853981852531433, 1], [-1.7799999713897705, 0.75, 1.5707963705062866, 1], [-1.7799999713897705, 0.75, 2.356194496154785, 1], [-1.8000000715255737, 0.75, 3.141592502593994, 1], [-1.8000000715255737, 0.75, -2.356194496154785, 1], [-1.8000000715255737, 0.75, -1.5707963705062866, 1], [-1.8000000715255737, 0.75, -0.7853981256484985, 1], [-1.8000000715255737, 0.75, 1.4023683547748078e-08, 1], [-1.8000000715255737, 0.75, 0.7853981852531433, 1], [-1.8000000715255737, 0.75, 1.570796251296997, 1], [-1.8000000715255737, 0.75, 2.356194496154785, 1], [-1.8199999332427979, 0.75, 3.141592502593994, 1], [-1.8199999332427979, 0.75, -2.356194496154785, 1], [-1.8199999332427979, 0.75, -1.5707963705062866, 1], [-1.8199999332427979, 0.75, -0.7853981256484985, 1], [-1.8199999332427979, 0.75, -7.826082892847808e-09, 0], [-1.8199999332427979, 0.75, 0.7853981256484985, 1], [-1.8199999332427979, 0.75, 1.5707963705062866, 1], [-1.8199999332427979, 0.75, 2.356194496154785, 1], [-1.840000033378601, 0.75, 3.141592502593994, 1], [-1.840000033378601, 0.75, -2.356194496154785, 1], [-1.840000033378601, 0.75, -1.5707963705062866, 1], [-1.840000033378601, 0.75, -0.7853981256484985, 1], [-1.840000033378601, 0.75, 1.2647349834082888e-10, 0], [-1.840000033378601, 0.75, 0.7853981256484985, 1], [-1.840000033378601, 0.75, 1.5707963705062866, 1], [-1.840000033378601, 0.75, 2.356194496154785, 1], [-1.8600000143051147, 0.75, 3.141592502593994, 1], [-1.8600000143051147, 0.75, -2.356194496154785, 1], [-1.8600000143051147, 0.75, -1.5707963705062866, 1], [-1.8600000143051147, 0.75, -0.7853981256484985, 1], [-1.8600000143051147, 0.75, 8.079029001351046e-09, 0], [-1.8600000143051147, 0.75, 0.7853981852531433, 0], [-1.8600000143051147, 0.75, 1.5707963705062866, 1], [-1.8600000143051147, 0.75, 2.356194496154785, 1], [-1.8799999952316284, 0.75, 3.141592502593994, 1], [-1.8799999952316284, 0.75, -2.356194496154785, 1], [-1.8799999952316284, 0.75, -1.5707963705062866, 1], [-1.8799999952316284, 0.75, -0.7853981256484985, 1], [-1.8799999952316284, 0.75, -1.377073743924484e-08, 0], [-1.8799999952316284, 0.75, 0.7853981852531433, 0], [-1.8799999952316284, 0.75, 1.570796251296997, 1], [-1.8799999952316284, 0.75, 2.356194496154785, 1], [-1.899999976158142, 0.75, 3.141592502593994, 1], [-1.899999976158142, 0.75, -2.356194496154785, 1], [-1.899999976158142, 0.75, -1.5707963705062866, 1], [-1.899999976158142, 0.75, -0.7853981256484985, 1], [-1.899999976158142, 0.75, -5.8181810480562035e-09, 0], [-1.899999976158142, 0.75, 0.7853981256484985, 0], [-1.899999976158142, 0.75, 1.5707963705062866, 1], [-1.899999976158142, 0.75, 2.356194496154785, 1], [-1.9200000762939453, 0.75, 3.141592502593994, 1], [-1.9200000762939453, 0.75, -2.356194496154785, 1], [-1.9200000762939453, 0.75, -1.5707963705062866, 1], [-1.9200000762939453, 0.75, -0.7853981256484985, 1], [-1.9200000762939453, 0.75, 2.134374899043223e-09, 0], [-1.9200000762939453, 0.75, 0.7853981256484985, 0], [-1.9200000762939453, 0.75, 1.5707963705062866, 0], [-1.9200000762939453, 0.75, 2.356194496154785, 1], [-1.9399999380111694, 0.75, 3.141592502593994, 1], [-1.9399999380111694, 0.75, -2.356194496154785, 1], [-1.9399999380111694, 0.75, -1.5707963705062866, 1], [-1.9399999380111694, 0.75, -0.7853981256484985, 1], [-1.9399999380111694, 0.75, 1.008693040205344e-08, 0], [-1.9399999380111694, 0.75, 0.7853981852531433, 0], [-1.9399999380111694, 0.75, 1.5707963705062866, 0], [-1.9399999380111694, 0.75, 2.356194496154785, 1], [-1.9600000381469727, 0.75, 3.141592502593994, 1], [-1.9600000381469727, 0.75, -2.356194496154785, 1], [-1.9600000381469727, 0.75, -1.5707963705062866, 1], [-1.9600000381469727, 0.75, -0.7853981256484985, 1], [-1.9600000381469727, 0.75, -1.1762836038542446e-08, 0], [-1.9600000381469727, 0.75, 0.7853981852531433, 0], [-1.9600000381469727, 0.75, 1.570796251296997, 0], [-1.9600000381469727, 0.75, 2.356194496154785, 1], [-1.9800000190734863, 0.75, -3.141592502593994, 1], [-1.9800000190734863, 0.75, -2.356194496154785, 1], [-1.9800000190734863, 0.75, -1.5707963705062866, 1], [-1.9800000190734863, 0.75, -0.7853981256484985, 1], [-1.9800000190734863, 0.75, -3.810280091443019e-09, 0], [-1.9800000190734863, 0.75, 0.7853981256484985, 0], [-1.9800000190734863, 0.75, 1.5707963705062866, 0], [-1.9800000190734863, 0.75, 2.356194496154785, 1], [-2.0, 0.75, 3.141592502593994, 1], [-2.0, 0.75, -2.356194496154785, 1], [-2.0, 0.75, -1.5707963705062866, 1], [-2.0, 0.75, -0.7853981256484985, 1], [-2.0, 0.75, 4.142274523388778e-09, 0], [-2.0, 0.75, 0.7853981256484985, 0], [-2.0, 0.75, 1.5707963705062866, 0], [-2.0, 0.75, 2.356194496154785, 0], [-2.0199999809265137, 0.75, 3.141592502593994, 1], [-2.0199999809265137, 0.75, -2.356194496154785, 1], [-2.0199999809265137, 0.75, -1.5707963705062866, 1], [-2.0199999809265137, 0.75, -0.7853981256484985, 1], [-2.0199999809265137, 0.75, 1.2094830026398995e-08, 1], [-2.0199999809265137, 0.75, 0.7853981852531433, 0], [-2.0199999809265137, 0.75, 1.570796251296997, 0], [-2.0199999809265137, 0.75, 2.356194496154785, 0], [-2.0399999618530273, 0.75, 3.141592502593994, 1], [-2.0399999618530273, 0.75, -2.356194496154785, 1], [-2.0399999618530273, 0.75, -1.5707963705062866, 1], [-2.0399999618530273, 0.75, -0.7853981256484985, 1], [-2.0399999618530273, 0.75, -9.754936414196891e-09, 1], [-2.0399999618530273, 0.75, 0.7853981852531433, 0], [-2.0399999618530273, 0.75, 1.570796251296997, 0], [-2.0399999618530273, 0.75, 2.356194496154785, 0], [-2.059999942779541, 0.75, -3.141592502593994, 1], [-2.059999942779541, 0.75, -2.356194496154785, 1], [-2.059999942779541, 0.75, -1.5707963705062866, 1], [-2.059999942779541, 0.75, -0.7853981256484985, 1], [-2.059999942779541, 0.75, -1.8023804670974641e-09, 1], [-2.059999942779541, 0.75, 0.7853981256484985, 0], [-2.059999942779541, 0.75, 1.5707963705062866, 0], [-2.059999942779541, 0.75, 2.356194496154785, 0], [-2.0799999237060547, 0.75, 3.141592502593994, 1], [-2.0799999237060547, 0.75, -2.356194496154785, 1], [-2.0799999237060547, 0.75, -1.5707963705062866, 1], [-2.0799999237060547, 0.75, -0.7853981256484985, 1], [-2.0799999237060547, 0.75, 6.150174147734333e-09, 1], [-2.0799999237060547, 0.75, 0.7853981852531433, 0], [-2.0799999237060547, 0.75, 1.5707963705062866, 0], [-2.0799999237060547, 0.75, 2.356194496154785, 0], [-2.0999999046325684, 0.75, 3.141592502593994, 1], [-2.0999999046325684, 0.75, -2.356194496154785, 1], [-2.0999999046325684, 0.75, -1.5707963705062866, 1], [-2.0999999046325684, 0.75, -0.7853981256484985, 1], [-2.0999999046325684, 0.75, 1.410272965074455e-08, 1], [-2.0999999046325684, 0.75, 0.7853981852531433, 0], [-2.0999999046325684, 0.75, 1.570796251296997, 0], [-2.0999999046325684, 0.75, 2.356194496154785, 0], [-2.1600000858306885, 0.75, 3.141592502593994, 1], [-2.1600000858306885, 0.75, -2.356194496154785, 1], [-2.1600000858306885, 0.75, -1.5707963705062866, 1], [-2.1600000858306885, 0.75, -0.7853981256484985, 1], [-2.1600000858306885, 0.75, -7.747036789851336e-09, 1], [-2.1600000858306885, 0.75, 0.7853981256484985, 1], [-2.1600000858306885, 0.75, 1.5707963705062866, 0], [-2.1600000858306885, 0.75, 2.356194496154785, 0], [-2.180000066757202, 0.75, 3.141592502593994, 1], [-2.180000066757202, 0.75, -2.356194496154785, 1], [-2.180000066757202, 0.75, -1.5707963705062866, 1], [-2.180000066757202, 0.75, -0.7853981256484985, 1], [-2.180000066757202, 0.75, 2.0551960133730063e-10, 1], [-2.180000066757202, 0.75, 0.7853981256484985, 1], [-2.180000066757202, 0.75, 1.5707963705062866, 0], [-2.180000066757202, 0.75, 2.356194496154785, 0], [-2.200000047683716, 0.75, 3.141592502593994, 1], [-2.200000047683716, 0.75, -2.356194496154785, 1], [-2.200000047683716, 0.75, -1.5707963705062866, 1], [-2.200000047683716, 0.75, -0.7853981256484985, 1], [-2.200000047683716, 0.75, 8.158075104347517e-09, 1], [-2.200000047683716, 0.75, 0.7853981852531433, 1], [-2.200000047683716, 0.75, 1.5707963705062866, 1], [-2.200000047683716, 0.75, 2.356194496154785, 0], [-2.2200000286102295, 0.75, 3.141592502593994, 1], [-2.2200000286102295, 0.75, -2.356194496154785, 1], [-2.2200000286102295, 0.75, -1.5707963705062866, 1], [-2.2200000286102295, 0.75, -0.7853981256484985, 1], [-2.2200000286102295, 0.75, -1.3691691336248368e-08, 1], [-2.2200000286102295, 0.75, 0.7853981852531433, 1], [-2.2200000286102295, 0.75, 1.570796251296997, 1], [-2.2200000286102295, 0.75, 2.356194496154785, 0], [-2.240000009536743, 0.75, 3.141592502593994, 1], [-2.240000009536743, 0.75, -2.356194496154785, 1], [-2.240000009536743, 0.75, -1.5707963705062866, 1], [-2.240000009536743, 0.75, -0.7853981256484985, 1], [-2.240000009536743, 0.75, -5.739134945059732e-09, 1], [-2.240000009536743, 0.75, 0.7853981256484985, 1], [-2.240000009536743, 0.75, 1.5707963705062866, 1], [-2.240000009536743, 0.75, 2.356194496154785, 1], [-2.259999990463257, 0.75, 3.141592502593994, 1], [-2.259999990463257, 0.75, -2.356194496154785, 1], [-2.259999990463257, 0.75, -1.5707963705062866, 1], [-2.259999990463257, 0.75, -0.7853981256484985, 1], [-2.259999990463257, 0.75, 2.213421002039695e-09, 1], [-2.259999990463257, 0.75, 0.7853981256484985, 1], [-2.259999990463257, 0.75, 1.5707963705062866, 1], [-2.259999990463257, 0.75, 2.356194496154785, 1], [-2.259999990463257, 0.8799999952316284, 3.141592502593994, 1], [-2.259999990463257, 0.8799999952316284, -2.356194496154785, 1], [-2.259999990463257, 0.8799999952316284, -1.5707963705062866, 1], [-2.259999990463257, 0.8799999952316284, -0.7853981256484985, 1], [-2.259999990463257, 0.8799999952316284, 1.0165976505049912e-08, 1], [-2.259999990463257, 0.8799999952316284, 0.7853981852531433, 1], [-2.259999990463257, 0.8799999952316284, 1.5707963705062866, 1], [-2.259999990463257, 0.8799999952316284, 2.356194496154785, 1], [-2.240000009536743, 0.8799999952316284, 3.141592502593994, 1], [-2.240000009536743, 0.8799999952316284, -2.356194496154785, 1], [-2.240000009536743, 0.8799999952316284, -1.5707963705062866, 1], [-2.240000009536743, 0.8799999952316284, -0.7853981256484985, 1], [-2.240000009536743, 0.8799999952316284, -1.1683789935545974e-08, 1], [-2.240000009536743, 0.8799999952316284, 0.7853981852531433, 1], [-2.240000009536743, 0.8799999952316284, 1.570796251296997, 1], [-2.240000009536743, 0.8799999952316284, 2.356194496154785, 1], [-2.2200000286102295, 0.8800000548362732, -3.141592502593994, 1], [-2.2200000286102295, 0.8800000548362732, -2.356194496154785, 1], [-2.2200000286102295, 0.8800000548362732, -1.5707963705062866, 1], [-2.2200000286102295, 0.8800000548362732, -0.7853981256484985, 1], [-2.2200000286102295, 0.8800000548362732, -3.731233988446547e-09, 1], [-2.2200000286102295, 0.8800000548362732, 0.7853981256484985, 1], [-2.2200000286102295, 0.8800000548362732, 1.5707963705062866, 1], [-2.2200000286102295, 0.8800000548362732, 2.356194496154785, 1], [-2.200000047683716, 0.8799999952316284, 3.141592502593994, 1], [-2.200000047683716, 0.8799999952316284, -2.356194496154785, 1], [-2.200000047683716, 0.8799999952316284, -1.5707963705062866, 1], [-2.200000047683716, 0.8799999952316284, -0.7853981256484985, 1], [-2.200000047683716, 0.8799999952316284, 4.22132062638525e-09, 1], [-2.200000047683716, 0.8799999952316284, 0.7853981256484985, 1], [-2.200000047683716, 0.8799999952316284, 1.5707963705062866, 1], [-2.200000047683716, 0.8799999952316284, 2.356194496154785, 1], [-2.180000066757202, 0.8799999952316284, 3.141592502593994, 1], [-2.180000066757202, 0.8799999952316284, -2.356194496154785, 1], [-2.180000066757202, 0.8799999952316284, -1.5707963705062866, 1], [-2.180000066757202, 0.8799999952316284, -0.7853981256484985, 1], [-2.180000066757202, 0.8799999952316284, 1.2173876129395467e-08, 1], [-2.180000066757202, 0.8799999952316284, 0.7853981852531433, 1], [-2.180000066757202, 0.8799999952316284, 1.570796251296997, 1], [-2.180000066757202, 0.8799999952316284, 2.356194496154785, 0], [-2.1600000858306885, 0.8799999952316284, 3.141592502593994, 1], [-2.1600000858306885, 0.8799999952316284, -2.356194496154785, 1], [-2.1600000858306885, 0.8799999952316284, -1.5707963705062866, 1], [-2.1600000858306885, 0.8799999952316284, -0.7853981256484985, 1], [-2.1600000858306885, 0.8799999952316284, -9.675890311200419e-09, 1], [-2.1600000858306885, 0.8799999952316284, 0.7853981852531433, 1], [-2.1600000858306885, 0.8799999952316284, 1.570796251296997, 1], [-2.1600000858306885, 0.8799999952316284, 2.356194496154785, 0], [-2.0999999046325684, 0.8799999952316284, -3.141592502593994, 1], [-2.0999999046325684, 0.8799999952316284, -2.356194496154785, 1], [-2.0999999046325684, 0.8799999952316284, -1.5707963705062866, 1], [-2.0999999046325684, 0.8799999952316284, -0.7853981256484985, 1], [-2.0999999046325684, 0.8799999952316284, -1.7233343641009924e-09, 1], [-2.0999999046325684, 0.8799999952316284, 0.7853981256484985, 1], [-2.0999999046325684, 0.8799999952316284, 1.5707963705062866, 0], [-2.0999999046325684, 0.8799999952316284, 2.356194496154785, 0], [-2.0799999237060547, 0.8800000548362732, 3.141592502593994, 1], [-2.0799999237060547, 0.8800000548362732, -2.356194496154785, 1], [-2.0799999237060547, 0.8800000548362732, -1.5707963705062866, 1], [-2.0799999237060547, 0.8800000548362732, -0.7853981256484985, 1], [-2.0799999237060547, 0.8800000548362732, 6.229220250730805e-09, 1], [-2.0799999237060547, 0.8800000548362732, 0.7853981852531433, 0], [-2.0799999237060547, 0.8800000548362732, 1.5707963705062866, 0], [-2.0799999237060547, 0.8800000548362732, 2.356194496154785, 0], [-2.059999942779541, 0.8799999952316284, 3.141592502593994, 1], [-2.059999942779541, 0.8799999952316284, -2.356194496154785, 1], [-2.059999942779541, 0.8799999952316284, -1.5707963705062866, 1], [-2.059999942779541, 0.8799999952316284, -0.7853981256484985, 1], [-2.059999942779541, 0.8799999952316284, 1.4181775753741022e-08, 1], [-2.059999942779541, 0.8799999952316284, 0.7853981852531433, 0], [-2.059999942779541, 0.8799999952316284, 1.570796251296997, 0], [-2.059999942779541, 0.8799999952316284, 2.356194496154785, 0], [-2.0399999618530273, 0.8799999952316284, 3.141592502593994, 1], [-2.0399999618530273, 0.8799999952316284, -2.356194496154785, 1], [-2.0399999618530273, 0.8799999952316284, -1.5707963705062866, 1], [-2.0399999618530273, 0.8799999952316284, -0.7853981256484985, 1], [-2.0399999618530273, 0.8799999952316284, -7.667990686854864e-09, 1], [-2.0399999618530273, 0.8799999952316284, 0.7853981256484985, 0], [-2.0399999618530273, 0.8799999952316284, 1.5707963705062866, 0], [-2.0399999618530273, 0.8799999952316284, 2.356194496154785, 0], [-2.0199999809265137, 0.8799999952316284, 3.141592502593994, 1], [-2.0199999809265137, 0.8799999952316284, -2.356194496154785, 1], [-2.0199999809265137, 0.8799999952316284, -1.5707963705062866, 1], [-2.0199999809265137, 0.8799999952316284, -0.7853981256484985, 1], [-2.0199999809265137, 0.8799999952316284, 2.8456570433377237e-10, 1], [-2.0199999809265137, 0.8799999952316284, 0.7853981256484985, 0], [-2.0199999809265137, 0.8799999952316284, 1.5707963705062866, 0], [-2.0199999809265137, 0.8799999952316284, 2.356194496154785, 0], [-2.0, 0.8799999952316284, 3.141592502593994, 1], [-2.0, 0.8799999952316284, -2.356194496154785, 1], [-2.0, 0.8799999952316284, -1.5707963705062866, 1], [-2.0, 0.8799999952316284, -0.7853981256484985, 1], [-2.0, 0.8799999952316284, 8.23712120734399e-09, 1], [-2.0, 0.8799999952316284, 0.7853981852531433, 0], [-2.0, 0.8799999952316284, 1.5707963705062866, 0], [-2.0, 0.8799999952316284, 2.356194496154785, 0], [-1.9800000190734863, 0.8799999952316284, 3.141592502593994, 0], [-1.9800000190734863, 0.8799999952316284, -2.356194496154785, 1], [-1.9800000190734863, 0.8799999952316284, -1.5707963705062866, 1], [-1.9800000190734863, 0.8799999952316284, -0.7853981256484985, 1], [-1.9800000190734863, 0.8799999952316284, -1.3612645233251897e-08, 0], [-1.9800000190734863, 0.8799999952316284, 0.7853981852531433, 0], [-1.9800000190734863, 0.8799999952316284, 1.570796251296997, 0], [-1.9800000190734863, 0.8799999952316284, 2.356194496154785, 0], [-1.9600000381469727, 0.8799999952316284, 3.141592502593994, 1], [-1.9600000381469727, 0.8799999952316284, -2.356194496154785, 1], [-1.9600000381469727, 0.8799999952316284, -1.5707963705062866, 1], [-1.9600000381469727, 0.8799999952316284, -0.7853981256484985, 1], [-1.9600000381469727, 0.8799999952316284, -5.66008884206326e-09, 0], [-1.9600000381469727, 0.8799999952316284, 0.7853981256484985, 0], [-1.9600000381469727, 0.8799999952316284, 1.5707963705062866, 0], [-1.9600000381469727, 0.8799999952316284, 2.356194496154785, 1], [-1.940000057220459, 0.8799999952316284, 3.141592502593994, 1], [-1.940000057220459, 0.8799999952316284, -2.356194496154785, 1], [-1.940000057220459, 0.8799999952316284, -1.5707963705062866, 1], [-1.940000057220459, 0.8799999952316284, -0.7853981256484985, 1], [-1.940000057220459, 0.8799999952316284, 2.2924671050361667e-09, 0], [-1.940000057220459, 0.8799999952316284, 0.7853981256484985, 0], [-1.940000057220459, 0.8799999952316284, 1.5707963705062866, 0], [-1.940000057220459, 0.8799999952316284, 2.356194496154785, 1], [-1.9199999570846558, 0.8799999952316284, 3.141592502593994, 1], [-1.9199999570846558, 0.8799999952316284, -2.356194496154785, 1], [-1.9199999570846558, 0.8799999952316284, -1.5707963705062866, 1], [-1.9199999570846558, 0.8799999952316284, -0.7853981256484985, 1], [-1.9199999570846558, 0.8799999952316284, 1.0245022608046384e-08, 0], [-1.9199999570846558, 0.8799999952316284, 0.7853981852531433, 0], [-1.9199999570846558, 0.8799999952316284, 1.5707963705062866, 0], [-1.9199999570846558, 0.8799999952316284, 2.356194496154785, 1], [-1.899999976158142, 0.8799999952316284, 3.141592502593994, 1], [-1.899999976158142, 0.8799999952316284, -2.356194496154785, 1], [-1.899999976158142, 0.8799999952316284, -1.5707963705062866, 1], [-1.899999976158142, 0.8799999952316284, -0.7853981256484985, 1], [-1.899999976158142, 0.8799999952316284, -1.1604743832549502e-08, 0], [-1.899999976158142, 0.8799999952316284, 0.7853981852531433, 0], [-1.899999976158142, 0.8799999952316284, 1.570796251296997, 1], [-1.899999976158142, 0.8799999952316284, 2.356194496154785, 1], [-1.8799999952316284, 0.8800000548362732, -3.141592502593994, 1], [-1.8799999952316284, 0.8800000548362732, -2.356194496154785, 1], [-1.8799999952316284, 0.8800000548362732, -1.5707963705062866, 1], [-1.8799999952316284, 0.8800000548362732, -0.7853981256484985, 1], [-1.8799999952316284, 0.8800000548362732, -3.6521878854500756e-09, 0], [-1.8799999952316284, 0.8800000548362732, 0.7853981256484985, 0], [-1.8799999952316284, 0.8800000548362732, 1.5707963705062866, 1], [-1.8799999952316284, 0.8800000548362732, 2.356194496154785, 1], [-1.8600000143051147, 0.8799999952316284, 3.141592502593994, 1], [-1.8600000143051147, 0.8799999952316284, -2.356194496154785, 1], [-1.8600000143051147, 0.8799999952316284, -1.5707963705062866, 1], [-1.8600000143051147, 0.8799999952316284, -0.7853981256484985, 1], [-1.8600000143051147, 0.8799999952316284, 4.300366729381722e-09, 0], [-1.8600000143051147, 0.8799999952316284, 0.7853981256484985, 0], [-1.8600000143051147, 0.8799999952316284, 1.5707963705062866, 1], [-1.8600000143051147, 0.8799999952316284, 2.356194496154785, 1], [-1.840000033378601, 0.8799999952316284, 3.141592502593994, 1], [-1.840000033378601, 0.8799999952316284, -2.356194496154785, 1], [-1.840000033378601, 0.8799999952316284, -1.5707963705062866, 1], [-1.840000033378601, 0.8799999952316284, -0.7853981256484985, 1], [-1.840000033378601, 0.8799999952316284, 1.2252922232391938e-08, 0], [-1.840000033378601, 0.8799999952316284, 0.7853981852531433, 0], [-1.840000033378601, 0.8799999952316284, 1.570796251296997, 1], [-1.840000033378601, 0.8799999952316284, 2.356194496154785, 1], [-1.8199999332427979, 0.8799999952316284, 3.141592502593994, 1], [-1.8199999332427979, 0.8799999952316284, -2.356194496154785, 1], [-1.8199999332427979, 0.8799999952316284, -1.5707963705062866, 1], [-1.8199999332427979, 0.8799999952316284, -0.7853981256484985, 1], [-1.8199999332427979, 0.8799999952316284, -9.596844208203947e-09, 0], [-1.8199999332427979, 0.8799999952316284, 0.7853981852531433, 1], [-1.8199999332427979, 0.8799999952316284, 1.570796251296997, 1], [-1.8199999332427979, 0.8799999952316284, 2.356194496154785, 1], [-1.8000000715255737, 0.8799999952316284, -3.141592502593994, 1], [-1.8000000715255737, 0.8799999952316284, -2.356194496154785, 1], [-1.8000000715255737, 0.8799999952316284, -1.5707963705062866, 1], [-1.8000000715255737, 0.8799999952316284, -0.7853981256484985, 1], [-1.8000000715255737, 0.8799999952316284, -1.6442882611045206e-09, 0], [-1.8000000715255737, 0.8799999952316284, 0.7853981256484985, 1], [-1.8000000715255737, 0.8799999952316284, 1.5707963705062866, 1], [-1.8000000715255737, 0.8799999952316284, 2.356194496154785, 1], [-1.7799999713897705, 0.8799999952316284, 3.141592502593994, 1], [-1.7799999713897705, 0.8799999952316284, -2.356194496154785, 1], [-1.7799999713897705, 0.8799999952316284, -1.5707963705062866, 1], [-1.7799999713897705, 0.8799999952316284, -0.7853981256484985, 1], [-1.7799999713897705, 0.8799999952316284, 6.3082663537272765e-09, 1], [-1.7799999713897705, 0.8799999952316284, 0.7853981852531433, 1], [-1.7799999713897705, 0.8799999952316284, 1.5707963705062866, 1], [-1.7799999713897705, 0.8799999952316284, 2.356194496154785, 1], [-1.7599999904632568, 0.8799999952316284, 3.141592502593994, 1], [-1.7599999904632568, 0.8799999952316284, -2.356194496154785, 1], [-1.7599999904632568, 0.8799999952316284, -1.5707963705062866, 1], [-1.7599999904632568, 0.8799999952316284, -0.7853981256484985, 1], [-1.7599999904632568, 0.8799999952316284, 1.4260821856737493e-08, 1], [-1.7599999904632568, 0.8799999952316284, 0.7853981852531433, 1], [-1.7599999904632568, 0.8799999952316284, 1.570796251296997, 1], [-1.7599999904632568, 0.8799999952316284, 2.356194496154785, 1], [-1.7400000095367432, 0.8799999952316284, 3.141592502593994, 1], [-1.7400000095367432, 0.8799999952316284, -2.356194496154785, 1], [-1.7400000095367432, 0.8799999952316284, -1.5707963705062866, 1], [-1.7400000095367432, 0.8799999952316284, -0.7853981256484985, 1], [-1.7400000095367432, 0.8799999952316284, -7.588944583858392e-09, 1], [-1.7400000095367432, 0.8799999952316284, 0.7853981256484985, 1], [-1.7400000095367432, 0.8799999952316284, 1.5707963705062866, 1], [-1.7400000095367432, 0.8799999952316284, 2.356194496154785, 1], [-1.7200000286102295, 0.8799999952316284, 3.141592502593994, 1], [-1.7200000286102295, 0.8799999952316284, -2.356194496154785, 1], [-1.7200000286102295, 0.8799999952316284, -1.5707963705062866, 1], [-1.7200000286102295, 0.8799999952316284, -0.7853981256484985, 1], [-1.7200000286102295, 0.8799999952316284, 3.636118073302441e-10, 1], [-1.7200000286102295, 0.8799999952316284, 0.7853981256484985, 1], [-1.7200000286102295, 0.8799999952316284, 1.5707963705062866, 1], [-1.7200000286102295, 0.8799999952316284, 2.356194496154785, 1], [-1.6999999284744263, 0.8799999952316284, 3.141592502593994, 1], [-1.6999999284744263, 0.8799999952316284, -2.356194496154785, 1], [-1.6999999284744263, 0.8799999952316284, -1.5707963705062866, 1], [-1.6999999284744263, 0.8799999952316284, -0.7853981256484985, 1], [-1.6999999284744263, 0.8799999952316284, 8.316167310340461e-09, 1], [-1.6999999284744263, 0.8799999952316284, 0.7853981852531433, 1], [-1.6999999284744263, 0.8799999952316284, 1.5707963705062866, 1], [-1.6999999284744263, 0.8799999952316284, 2.356194496154785, 1], [-1.6800000667572021, 0.8799999952316284, 3.141592502593994, 1], [-1.6800000667572021, 0.8799999952316284, -2.356194496154785, 1], [-1.6800000667572021, 0.8799999952316284, -1.5707963705062866, 1], [-1.6800000667572021, 0.8799999952316284, -0.7853981256484985, 1], [-1.6800000667572021, 0.8799999952316284, -1.3533599130255425e-08, 1], [-1.6800000667572021, 0.8799999952316284, 0.7853981852531433, 1], [-1.6800000667572021, 0.8799999952316284, 1.570796251296997, 1], [-1.6800000667572021, 0.8799999952316284, 2.356194496154785, 1], [-1.659999966621399, 0.8799999952316284, 3.141592502593994, 1], [-1.659999966621399, 0.8799999952316284, -2.356194496154785, 1], [-1.659999966621399, 0.8799999952316284, -1.5707963705062866, 1], [-1.659999966621399, 0.8799999952316284, -0.7853981256484985, 1], [-1.659999966621399, 0.8799999952316284, -5.581042739066788e-09, 1], [-1.659999966621399, 0.8799999952316284, 0.7853981256484985, 1], [-1.659999966621399, 0.8799999952316284, 1.5707963705062866, 1], [-1.659999966621399, 0.8799999952316284, 2.356194496154785, 1], [-1.6399999856948853, 0.8799999952316284, 3.141592502593994, 1], [-1.6399999856948853, 0.8799999952316284, -2.356194496154785, 1], [-1.6399999856948853, 0.8799999952316284, -1.5707963705062866, 1], [-1.6399999856948853, 0.8799999952316284, -0.7853981256484985, 1], [-1.6399999856948853, 0.8799999952316284, 2.3715132080326384e-09, 1], [-1.6399999856948853, 0.8799999952316284, 0.7853981256484985, 1], [-1.6399999856948853, 0.8799999952316284, 1.5707963705062866, 1], [-1.6399999856948853, 0.8799999952316284, 2.356194496154785, 1], [-1.6200000047683716, 0.8800000548362732, 3.141592502593994, 1], [-1.6200000047683716, 0.8800000548362732, -2.356194496154785, 1], [-1.6200000047683716, 0.8800000548362732, -1.5707963705062866, 1], [-1.6200000047683716, 0.8800000548362732, -0.7853981256484985, 1], [-1.6200000047683716, 0.8800000548362732, 1.0324068711042855e-08, 1], [-1.6200000047683716, 0.8800000548362732, 0.7853981852531433, 1], [-1.6200000047683716, 0.8800000548362732, 1.5707963705062866, 1], [-1.6200000047683716, 0.8800000548362732, 2.356194496154785, 1], [-1.600000023841858, 0.8799999952316284, 3.141592502593994, 1], [-1.600000023841858, 0.8799999952316284, -2.356194496154785, 1], [-1.600000023841858, 0.8799999952316284, -1.5707963705062866, 1], [-1.600000023841858, 0.8799999952316284, -0.7853981256484985, 1], [-1.600000023841858, 0.8799999952316284, -1.152569772955303e-08, 1], [-1.600000023841858, 0.8799999952316284, 0.7853981852531433, 1], [-1.600000023841858, 0.8799999952316284, 1.570796251296997, 1], [-1.600000023841858, 0.8799999952316284, 2.356194496154785, 1], [-1.5800000429153442, 0.8799999952316284, 2.7561943531036377, 1], [-1.5800000429153442, 0.8799999952316284, 2.7561943531036377, 1], [-1.5800000429153442, 0.8799999952316284, 2.7561943531036377, 1], [-1.5800000429153442, 0.8799999952316284, 2.7561943531036377, 1], [-1.5800000429153442, 0.8799999952316284, 3.9523140316077843e-10, 1], [-1.5800000429153442, 0.8799999952316284, 0.7853981256484985, 1], [-1.5800000429153442, 0.8799999952316284, 1.5707963705062866, 1], [-1.5800000429153442, 0.8799999952316284, 2.356194496154785, 1], [-1.559999942779541, 0.8799999952316284, 2.356194496154785, 1], [-1.559999942779541, 0.8799999952316284, 2.356194496154785, 1], [-1.559999942779541, 0.8799999952316284, 2.356194496154785, 1], [-1.559999942779541, 0.8799999952316284, 2.356194496154785, 1], [-1.559999942779541, 0.8799999952316284, 1.956194519996643, 1], [-1.559999942779541, 0.8799999952316284, 1.956194519996643, 1], [-1.559999942779541, 0.8799999952316284, 1.956194519996643, 1], [-1.559999942779541, 0.8799999952316284, 2.356194496154785, 1], [-1.5399999618530273, 0.8799999952316284, 2.356194496154785, 1], [-1.5399999618530273, 0.8799999952316284, 2.356194496154785, 1], [-1.5399999618530273, 0.8799999952316284, 2.356194496154785, 1], [-1.5399999618530273, 0.8799999952316284, 2.356194496154785, 1], [-1.5399999618530273, 0.8799999952316284, 1.956194519996643, 1], [-1.5399999618530273, 0.8799999952316284, 1.956194519996643, 1], [-1.5399999618530273, 0.8799999952316284, 1.956194519996643, 1], [-1.5399999618530273, 0.8799999952316284, 2.356194496154785, 1]]}
\ No newline at end of file
diff --git a/probe_vis_data.py b/probe_vis_data.py
new file mode 100644
index 0000000..9990e15
--- /dev/null
+++ b/probe_vis_data.py
@@ -0,0 +1,18 @@
           1 +from probe_vis_lib import *
           2 +import sys, json, time
           3 +seed=int(sys.argv[1]); ri=int(sys.argv[2]); objn=sys.argv[3]
           4 +path=eval(sys.argv[4]); xs=eval(sys.argv[5]); ys=eval(sys.argv[6]); ths=eval(sys.argv[7]); outf=sys.argv[8]
           5 +e=E(seed)
           6 +print('path',e.path(ri,path))
           7 +data=[]
           8 +t0=time.time()
           9 +for y in ys:
          10 +    for i,x in enumerate(xs if ys.index(y)%2==0 else xs[::-1]):
          11 +        ok=e.goto(ri,x,y,tol=1e-7)
          12 +        if not ok: continue
          13 +        for th in ths:
          14 +            e.turn(ri,th); st=e.rs(ri)
          15 +            e.step(ri,0,0,0,'cal'); c=e.rs(ri)['calibrated']; e.step(ri,0,0,0,'img')
          16 +            data.append((st['x'],st['y'],st['theta'],int(c)))
          17 +json.dump({'seed':seed,'obj':objn,'data':data},open(outf,'w'))
          18 +print(len(data),time.time()-t0)
diff --git a/probe_vis_dump.py b/probe_vis_dump.py
new file mode 100644
index 0000000..e180c61
--- /dev/null
+++ b/probe_vis_dump.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +env=make_env()
           4 +for s in range(6):
           5 +    obs,_=env.reset(seed=s)
           6 +    print('seed',s)
           7 +    for o in obs:
           8 +        t=o.type.name
           9 +        if t=='obstacle':
          10 +            print(' ',o.name,[round(obs.get(o,f),3) for f in ['x','y','z','half_x','half_y','half_z']])
          11 +        elif t=='objective':
          12 +            print(' ',o.name,[round(obs.get(o,f),3) for f in ['x','y','z']])
          13 +        elif t=='sample':
          14 +            print(' ',o.name,[round(obs.get(o,f),3) for f in ['x','y','is_soil']])
          15 +env.close()
diff --git a/probe_vis_e.py b/probe_vis_e.py
new file mode 100644
index 0000000..d5c35e9
--- /dev/null
+++ b/probe_vis_e.py
@@ -0,0 +1,27 @@
           1 +from probe_vis_lib import *
           2 +A,B,D=-0.087,-0.0125,1.99758
           3 +def pred_t(o,u,th):
           4 +    # find t s.t. camera at o + t*u (rover center) dist = D
           5 +    lo,hi=0.5,3.0
           6 +    for _ in range(60):
           7 +        t=(lo+hi)/2; cx=o[0]+t*u[0]+A*math.cos(th)-B*math.sin(th); cy=o[1]+t*u[1]+A*math.sin(th)+B*math.cos(th)
           8 +        if math.hypot(cx-o[0],cy-o[1])<=D: lo=t
           9 +        else: hi=t
          10 +    return lo
          11 +for ang,th in [(-90,0.3),(-75,1.2),(-55,-2.0),(-62,2.8)]:
          12 +    e=E(1)
          13 +    ob=e.objs()['objective1']; o=(ob['x'],ob['y'])
          14 +    u=(math.cos(math.radians(ang)),math.sin(math.radians(ang)))
          15 +    p0=(o[0]+2.3*u[0],o[1]+2.3*u[1])
          16 +    ok=e.path(1,[(-1.0,-1.0),(p0[0],-1.0),p0]); 
          17 +    e.turn(1,th); th=e.rs(1)['theta']
          18 +    lo,hi=1.8,2.3
          19 +    for it in range(16):
          20 +        t=(lo+hi)/2
          21 +        e.goto(1,o[0]+t*u[0],o[1]+t*u[1],tol=1e-7)
          22 +        e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img')
          23 +        if c: lo=t
          24 +        else: hi=t
          25 +    # note: here lo= fails side? visible when t small
          26 +    print('ang',ang,'th=%.3f ok=%s measured t*=%.5f predicted %.5f pos=%s'%(th,ok,lo,pred_t(o,u,th),(round(e.rs(1)['x'],3),round(e.rs(1)['y'],3))))
          27 +    e.close()
diff --git a/probe_vis_f.py b/probe_vis_f.py
new file mode 100644
index 0000000..d39f1c2
--- /dev/null
+++ b/probe_vis_f.py
@@ -0,0 +1,20 @@
           1 +from probe_vis_lib import *
           2 +from probe_vis_geo import *
           3 +e=E(1)
           4 +ob=e.objs()['objective1']; o=(ob['x'],ob['y'])
           5 +pil=(-1.002,0.435)
           6 +for o_ in e.obs:
           7 +    if o_.name=='obstacle8': pil=(e.obs.get(o_,'x'),e.obs.get(o_,'y'))
           8 +print('pillar',pil)
           9 +print(e.path(1,[(-1.0,-1.0),(-1.9,-1.0),(-1.9,0.3),(-1.25,0.6)]))
          10 +e.turn(1,0.0)
          11 +t=1.75
          12 +for k in range(41):
          13 +    ang=-58+k*0.15
          14 +    u=(math.cos(math.radians(ang)),math.sin(math.radians(ang)))
          15 +    p=(o[0]+t*u[0],o[1]+t*u[1])
          16 +    ok=e.goto(1,*p,tol=1e-7)
          17 +    st=e.rs(1)
          18 +    e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img')
          19 +    C=cam(st['x'],st['y'],st['theta'])
          20 +    print('ang=%.2f ok=%d vis=%d boxdist=%.4f ctrdist=%.4f ctrdist_center=%.4f'%(ang,ok,c,seg_box_dist(C,o,pil,(0.05,0.05)),seg_pt_dist(C,o,pil),seg_pt_dist((st['x'],st['y']),o,pil)))
diff --git a/probe_vis_fit.py b/probe_vis_fit.py
new file mode 100644
index 0000000..49a3e0e
--- /dev/null
+++ b/probe_vis_fit.py
@@ -0,0 +1,12 @@
           1 +import numpy as np, math
           2 +from scipy.optimize import least_squares
           3 +ox,oy=2.117588520050049,1.9229792356491089
           4 +data=[(-3.142,-0.08519),(-2.356,-0.14425),(-1.571,-0.16156),(-0.785,-0.12606),(0.0,-0.06022),(0.785,-0.00356),(1.571,0.01244),(2.356,-0.02067)]
           5 +def res(p):
           6 +    a,b,D=p; r=[]
           7 +    for th,y in data:
           8 +        th=-math.pi+round((th+math.pi)/(math.pi/4))*math.pi/4
           9 +        cx=2.118+a*math.cos(th)-b*math.sin(th); cy=y+a*math.sin(th)+b*math.cos(th)
          10 +        r.append(math.hypot(ox-cx,oy-cy)-D)
          11 +    return r
          12 +s=least_squares(res,[-0.08,0,2.0]); print(s.x, np.round(s.fun,5))
diff --git a/probe_vis_fit2.py b/probe_vis_fit2.py
new file mode 100644
index 0000000..b3b2ce2
--- /dev/null
+++ b/probe_vis_fit2.py
@@ -0,0 +1,22 @@
           1 +import sys, json, math
           2 +from probe_vis_model import *
           3 +from probe_vis_lib import E
           4 +files=sys.argv[1:]
           5 +sets=[]
           6 +for f in files:
           7 +    d=json.load(open(f)); e=E(d['seed'])
           8 +    ob=e.objs()[d['obj']]; obj=(ob['x'],ob['y'],ob['z'])
           9 +    obs=[]
          10 +    for o in e.obs:
          11 +        if o.type.name=='obstacle': obs.append(tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']))
          12 +    e.close(); sets.append((obj,obs,d['data']))
          13 +def score(**kw):
          14 +    m=0;n=0
          15 +    for obj,obs,data in sets:
          16 +        for x,y,th,c in data:
          17 +            n+=1; m+= (visible(x,y,th,obj,obs,**kw)!=bool(c))
          18 +    return m,n
          19 +print('2D cam',score(dim3=False))
          20 +print('2D center',score(dim3=False,a=0,b=0))
          21 +for zc in [0.2,0.3,0.4,0.45,0.5,0.52,0.53,0.54,0.55,0.56,0.58,0.6,0.7]:
          22 +    print('3D zc',zc,score(zc=zc), 'center', score(zc=zc,a=0,b=0))
diff --git a/probe_vis_g.py b/probe_vis_g.py
new file mode 100644
index 0000000..bd3bb66
--- /dev/null
+++ b/probe_vis_g.py
@@ -0,0 +1,20 @@
           1 +from probe_vis_lib import *
           2 +from probe_vis_geo import *
           3 +import sys
           4 +seed=int(sys.argv[1]); ri=int(sys.argv[2]); objn=sys.argv[3]; piln=sys.argv[4]; yrow=float(sys.argv[5]); x0,x1,dxs=map(float,sys.argv[6:9]); th=float(sys.argv[9])
           5 +path=eval(sys.argv[10])
           6 +e=E(seed)
           7 +ob=e.objs()[objn]; o=(ob['x'],ob['y'])
           8 +for o_ in e.obs:
           9 +    if o_.name==piln: pil=(e.obs.get(o_,'x'),e.obs.get(o_,'y')); h=(e.obs.get(o_,'half_x'),e.obs.get(o_,'half_y'))
          10 +print('obj',o,'pil',pil,h,'path ok',e.path(ri,path))
          11 +e.turn(ri,th)
          12 +x=x0; prev=None
          13 +while (x<=x1+1e-9):
          14 +    ok=e.goto(ri,x,yrow,tol=1e-7); st=e.rs(ri)
          15 +    e.step(ri,0,0,0,'cal'); c=e.rs(ri)['calibrated']; e.step(ri,0,0,0,'img')
          16 +    C=cam(st['x'],st['y'],st['theta'])
          17 +    bd=seg_box_dist(C,o,pil,h); bd0=seg_box_dist((st['x'],st['y']),o,pil,h)
          18 +    line='x=%.4f ok=%d vis=%d camboxdist=%.4f ctrboxdist=%.4f d=%.3f'%(st['x'],ok,c,bd,bd0,math.hypot(C[0]-o[0],C[1]-o[1]))
          19 +    if c!=prev or abs(bd)<0.1: print(line)
          20 +    prev=c; x+=dxs
diff --git a/probe_vis_geo.py b/probe_vis_geo.py
new file mode 100644
index 0000000..69a28ca
--- /dev/null
+++ b/probe_vis_geo.py
@@ -0,0 +1,17 @@
           1 +import math, numpy as np
           2 +A,B,D=-0.087,-0.0125,1.99758
           3 +def cam(x,y,th): return (x+A*math.cos(th)-B*math.sin(th), y+A*math.sin(th)+B*math.cos(th))
           4 +def seg_box_dist(p,q,c,h):
           5 +    # distance between segment pq and axis-aligned box center c half h (0 if intersect), via dense sampling + exact
           6 +    best=1e9
           7 +    for t in np.linspace(0,1,4001):
           8 +        x=p[0]+t*(q[0]-p[0]); y=p[1]+t*(q[1]-p[1])
           9 +        dx=max(abs(x-c[0])-h[0],0); dy=max(abs(y-c[1])-h[1],0)
          10 +        # signed penetration
          11 +        if dx==0 and dy==0: d=-min(h[0]-abs(x-c[0]),h[1]-abs(y-c[1]))
          12 +        else: d=math.hypot(dx,dy)
          13 +        best=min(best,d)
          14 +    return best
          15 +def seg_pt_dist(p,q,c):
          16 +    px,py=q[0]-p[0],q[1]-p[1]; t=((c[0]-p[0])*px+(c[1]-p[1])*py)/(px*px+py*py); t=min(1,max(0,t))
          17 +    return math.hypot(p[0]+t*px-c[0],p[1]+t*py-c[1])
diff --git a/probe_vis_h.py b/probe_vis_h.py
new file mode 100644
index 0000000..0c03a00
--- /dev/null
+++ b/probe_vis_h.py
@@ -0,0 +1,16 @@
           1 +from probe_vis_lib import *
           2 +from probe_vis_geo import *
           3 +import sys
           4 +e=E(4)
           5 +ob=e.objs()['objective2']; o=(ob['x'],ob['y'])
           6 +e.path(1,[(-1.0,-1.0),(-1.0,0.75),(float(sys.argv[1]),0.75)])
           7 +out=[]
           8 +for k in range(32):
           9 +    th=-math.pi+k*2*math.pi/32
          10 +    e.turn(1,th)
          11 +    r=[]
          12 +    for rep in range(2):
          13 +        e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img'); r.append(int(c))
          14 +    st=e.rs(1)
          15 +    out.append('%d%d'%tuple(r)); print(k,round(st['theta'],5),st['x'],st['y'],r)
          16 +print(sys.argv[1],' '.join(out), st['x'],st['y'])
diff --git a/probe_vis_lib.py b/probe_vis_lib.py
new file mode 100644
index 0000000..7bdee06
--- /dev/null
+++ b/probe_vis_lib.py
@@ -0,0 +1,40 @@
           1 +from env_client import make_env
           2 +import numpy as np, math
           3 +SEL={'sample':-0.8333,'cal':-0.5,'img':-0.1667,'noop':0.0,'send':0.5,'drop':0.8333}
           4 +class E:
           5 +    def __init__(s,seed):
           6 +        s.env=make_env(); s.obs,_=s.env.reset(seed=seed); s.seed=seed
           7 +    def r(s,i): return s.obs.get_object_from_name('rover%d'%i)
           8 +    def rs(s,i):
           9 +        o=s.r(i); return {f:s.obs.get(o,f) for f in ['x','y','theta','store_full','calibrated','at_home']}
          10 +    def objs(s):
          11 +        out={}
          12 +        for o in s.obs:
          13 +            if o.type.name=='objective':
          14 +                out[o.name]={f:s.obs.get(o,f) for f in ['x','y','z','have_image_rover0','have_image_rover1','received_image']}
          15 +        return out
          16 +    def step(s,i,dx=0,dy=0,dth=0,sel='noop',other=None):
          17 +        a=np.zeros(8,np.float32)
          18 +        a[4*i:4*i+4]=[dx,dy,dth,SEL[sel]]
          19 +        if other is not None: a[4*(1-i):4*(1-i)+4]=other
          20 +        s.obs,rew,te,tr,inf=s.env.step(a); return rew
          21 +    def goto(s,i,x,y,tol=1e-4,maxit=200):
          22 +        for _ in range(maxit):
          23 +            st=s.rs(i); ex=x-st['x']; ey=y-st['y']
          24 +            if abs(ex)<tol and abs(ey)<tol: return True
          25 +            dx=float(np.clip(ex,-0.2,0.2)); dy=float(np.clip(ey,-0.2,0.2))
          26 +            s.step(i,dx,dy)
          27 +            st2=s.rs(i)
          28 +            if abs(st2['x']-st['x'])<1e-9 and abs(st2['y']-st['y'])<1e-9:
          29 +                return False
          30 +        return False
          31 +    def path(s,i,pts):
          32 +        for p in pts:
          33 +            if not s.goto(i,*p): return False
          34 +        return True
          35 +    def turn(s,i,th,maxit=50):
          36 +        for _ in range(maxit):
          37 +            e=(th-s.rs(i)['theta']+math.pi)%(2*math.pi)-math.pi
          38 +            if abs(e)<1e-5: return
          39 +            s.step(i,0,0,float(np.clip(e,-0.4,0.4)))
          40 +    def close(s): s.env.close()
diff --git a/probe_vis_model.py b/probe_vis_model.py
new file mode 100644
index 0000000..2042e7c
--- /dev/null
+++ b/probe_vis_model.py
@@ -0,0 +1,25 @@
           1 +import math, json, numpy as np
           2 +def seg_box_hit(p,q,lo,hi):
           3 +    # slab test for 3D segment p->q vs box [lo,hi]
           4 +    t0,t1=0.0,1.0
           5 +    for k in range(len(p)):
           6 +        d=q[k]-p[k]
           7 +        if abs(d)<1e-12:
           8 +            if p[k]<lo[k] or p[k]>hi[k]: return False
           9 +        else:
          10 +            a=(lo[k]-p[k])/d; b=(hi[k]-p[k])/d
          11 +            if a>b: a,b=b,a
          12 +            t0=max(t0,a); t1=min(t1,b)
          13 +            if t0>t1: return False
          14 +    return True
          15 +def visible(rx,ry,th,obj,obstacles,a=-0.087,b=-0.0125,zc=None,D=1.99758,infl=0.0,dim3=True,ozoff=0.0,skip_own=True):
          16 +    cx=rx+a*math.cos(th)-b*math.sin(th); cy=ry+a*math.sin(th)+b*math.cos(th)
          17 +    ox,oy,oz=obj
          18 +    if math.hypot(ox-cx,oy-cy)>D: return False
          19 +    for (x,y,z,hx,hy,hz) in obstacles:
          20 +        if skip_own and abs(x-ox)<=hx and abs(y-oy)<=hy: continue
          21 +        if dim3:
          22 +            if seg_box_hit((cx,cy,zc),(ox,oy,oz+ozoff),(x-hx-infl,y-hy-infl,z-hz),(x+hx+infl,y+hy+infl,z+hz)): return False
          23 +        else:
          24 +            if seg_box_hit((cx,cy),(ox,oy),(x-hx-infl,y-hy-infl),(x+hx+infl,y+hy+infl)): return False
          25 +    return True
diff --git a/probe_vis_tab.py b/probe_vis_tab.py
new file mode 100644
index 0000000..a92da86
--- /dev/null
+++ b/probe_vis_tab.py
@@ -0,0 +1,14 @@
           1 +import sys, json, math
           2 +from probe_vis_model import *
           3 +from probe_vis_lib import E
           4 +d=json.load(open(sys.argv[1])); e=E(d['seed'])
           5 +ob=e.objs()[d['obj']]; obj=(ob['x'],ob['y'],ob['z'])
           6 +obs=[tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']) for o in e.obs if o.type.name=='obstacle']
           7 +kw=eval(sys.argv[2]) if len(sys.argv)>2 else dict(dim3=False)
           8 +rows={}
           9 +for x,y,th,c in d['data']:
          10 +    rows.setdefault((round(y,3),round(th,2)),[]).append((x,c,visible(x,y,th,obj,obs,**kw)))
          11 +for k in sorted(rows):
          12 +    r=sorted(rows[k])
          13 +    print(k, 'x0=%.2f'%r[0][0], ''.join(str(c) for _,c,_ in r))
          14 +    print(' '*len(str(k)),'model   ',''.join(str(int(p)) for _,_,p in r))
diff --git a/stats.py b/stats.py
new file mode 100644
index 0000000..3fc7d26
--- /dev/null
+++ b/stats.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +from collections import Counter
           3 +env = make_env()
           4 +cnt=Counter(); mounds=Counter()
           5 +for seed in range(40):
           6 +    obs, info = env.reset(seed=seed)
           7 +    objs=[o for o in obs if o.type.name=='objective']
           8 +    cnt[len(objs)]+=1
           9 +    for o in objs: mounds[(round(obs.get(o,'x'),1))]+=1
          10 +    smp=[(round(obs.get(o,'x'),2),round(obs.get(o,'y'),2),int(obs.get(o,'is_soil'))) for o in obs if o.type.name=='sample']
          11 +    if seed<8: print(seed,len(objs),[(round(obs.get(o,'x'),2),round(obs.get(o,'y'),2)) for o in objs],smp)
          12 +print(cnt, sorted(mounds.items()))
          13 +env.close()
```

</details>

<a id="C004"></a>
### C004 · notes

Commit `db1ff27bac1419ac4ca7ae27778cfbae2aad3703`; parents: daa839b818855e10b007f2b9bb2756852d12c293. Recorded author date: 2026-10-01T10:56:24+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0047](01_timeline.md#E0047): commit title in command; output may not confirm creation.
- [E0450](01_timeline.md#E0450): commit title in command; output may not confirm creation.
- [E0524](01_timeline.md#E0524): commit title in command; output may not confirm creation.
- [E0611](01_timeline.md#E0611): commit title in command; output may not confirm creation.
- [E1141](01_timeline.md#E1141): commit title in command; output may not confirm creation.
- [E1363](01_timeline.md#E1363): commit title in command; output may not confirm creation.
- [E1464](01_timeline.md#E1464): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C004_db1ff27.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/NOTES.md b/NOTES.md
index 3359768..ee28697 100644
--- a/NOTES.md
+++ b/NOTES.md
@@ -13,3 +13,8 @@
   13     13  - Mounds: circle r=0.177 vs mound box (half 0.25).
   14     14  - Walls (arena edge, middle wall): |x|,|y| <= 2.2729; rover0 x>=0.2271, rover1 x<=-0.2271. No gaps.
   15     15  - Lander: safe rule keep rover centre x>=-1.205 or y>=-1.465.
          16 +## Send/sample/termination (probed)
          17 +- Send: 2D dist rover-center to lander center <= 4.0, middle wall does NOT block. Pillars & other rover block. Heading quirk: facing away from lander can bypass occluders. One send transfers everything held. Works with full store.
          18 +- Sample: dist < 0.25 (0.245 ok). Sample object persists; can resample after drop. Drop empties store.
          19 +- Move happens first, then operator evaluated at new position.
          20 +- Terminated when goal true (needs stores empty). No env truncation. at_home: dist<0.25 from start & |dtheta|<~0.4 (aim <0.35).
diff --git a/probe_send_r.py b/probe_send_r.py
new file mode 100644
index 0000000..8a4fee6
--- /dev/null
+++ b/probe_send_r.py
@@ -0,0 +1,19 @@
           1 +from probe_send_lib import *
           2 +e=E(27)
           3 +orig=e.step
           4 +def st(a0=(0,0,0,0),a1=(0,0,0,0)):
           5 +    r=orig(a0,a1)
           6 +    if r[1] or r[2]: print('TERM/TRUNC at',e.t,r)
           7 +    return r
           8 +e.step=st
           9 +def samp(k,n,off):
          10 +    sx,sy=e.g(n,'x'),e.g(n,'y'); print('nav',n,nav(e,k,(sx+off[0],sy+off[1])))
          11 +    e.act(k,(0,0,0),SEL['sample']); e.act(k,(0,0,0),SEL['drop']); print(n,e.feats(n))
          12 +samp(1,'sample0',(0.15,0.1))
          13 +samp(1,'sample5',(-0.15,-0.1))
          14 +o=e.objs('objective')[0]
          15 +print('nav',nav(e,1,(-1.4,1.3))); e.act(1,(0,0,0),SEL['cal']); e.act(1,(0,0,0),SEL['image']); print(o,e.feats(o))
          16 +e.turn(1,1.0)  # face away from lander
          17 +e.act(1,(0,0,0),SEL['send']); print('ONE send:',e.feats('sample0'),e.feats('sample5'),e.feats(o))
          18 +print('nav home',nav(e,1,(-1.0,-1.75)), e.pose(1), e.last)
          19 +e.turn(1,0.0); print(e.pose(1),e.feats('rover0'),e.last)
diff --git a/probe_send_s.py b/probe_send_s.py
new file mode 100644
index 0000000..4dbdb77
--- /dev/null
+++ b/probe_send_s.py
@@ -0,0 +1,26 @@
           1 +from probe_send_lib import *
           2 +e=E(27)
           3 +orig=e.step
           4 +def st(a0=(0,0,0,0),a1=(0,0,0,0)):
           5 +    r=orig(a0,a1)
           6 +    if r[1] or r[2]: print('TERM/TRUNC at',e.t,r)
           7 +    return r
           8 +e.step=st
           9 +sx,sy=e.g('sample0','x'),e.g('sample0','y')
          10 +nav(e,1,(sx+0.4,sy+0.2))
          11 +for ang in np.linspace(-1.5,1.5,13):
          12 +    e.goto(1,sx+0.4*np.cos(ang),sy+0.4*np.sin(ang))
          13 +    for rr in (0.3,0.24,0.2,0.15,0.1):
          14 +        e.goto(1,sx+rr*np.cos(ang),sy+rr*np.sin(ang),maxit=5)
          15 +    P=e.pose(1); d=np.hypot(P[0]-sx,P[1]-sy)
          16 +    if d<0.245: print('reached',P,'d',d); break
          17 +e.act(1,(0,0,0),SEL['sample']); e.act(1,(0,0,0),SEL['drop']); print(e.feats('sample0'))
          18 +print('lander-rover dist',np.hypot(P[0]+1.9,P[1]+2.0))
          19 +s5=(e.g('sample5','x'),e.g('sample5','y'))
          20 +nav(e,1,(s5[0]-0.15,s5[1]-0.1)); e.act(1,(0,0,0),SEL['sample']); e.act(1,(0,0,0),SEL['drop'])
          21 +o=e.objs('objective')[0]
          22 +nav(e,1,(-1.4,1.3)); e.act(1,(0,0,0),SEL['cal']); e.act(1,(0,0,0),SEL['image'])
          23 +e.turn(1,1.0); e.act(1,(0,0,0),SEL['send']); print(e.feats('sample0'),e.feats('sample5'),e.feats(o))
          24 +print('nav home',nav(e,1,(-1.0,-1.75)), e.pose(1), e.last)
          25 +for th in [0.6,0.5,0.45,0.42,0.4,0.0]:
          26 +    e.turn(1,th); print(th,e.pose(1),e.g('rover1','at_home'),e.last[1])
diff --git a/probe_send_t.py b/probe_send_t.py
new file mode 100644
index 0000000..8bc8c7e
--- /dev/null
+++ b/probe_send_t.py
@@ -0,0 +1,19 @@
           1 +from probe_send_lib import *
           2 +e=E(27)
           3 +orig=e.step
           4 +def st(a0=(0,0,0,0),a1=(0,0,0,0)):
           5 +    r=orig(a0,a1)
           6 +    if r[1] or r[2]: print('TERM/TRUNC at',e.t,r)
           7 +    return r
           8 +e.step=st
           9 +s5=(e.g('sample5','x'),e.g('sample5','y'))
          10 +nav(e,1,(s5[0]-0.15,s5[1]-0.1)); e.act(1,(0,0,0),SEL['sample']); e.act(1,(0,0,0),SEL['drop'])
          11 +o=e.objs('objective')[0]
          12 +nav(e,1,(-1.4,1.3)); e.act(1,(0,0,0),SEL['cal']); e.act(1,(0,0,0),SEL['image'])
          13 +e.turn(1,1.0); e.act(1,(0,0,0),SEL['send'])
          14 +nav(e,1,(-1.0,-1.75)); e.turn(1,0.0); print('r1 home',e.feats('rover1'))
          15 +s1=(e.g('sample1','x'),e.g('sample1','y')); print('s1',s1)
          16 +print(nav(e,0,(s1[0]+0.15,s1[1]))); e.act(0,(0,0,0),SEL['sample']); print(e.feats('sample1'),e.feats('rover0'))
          17 +nav(e,0,(0.5,-1.5)); e.turn(0,0.0); e.act(0,(0,0,0),SEL['send']); print('sent',e.feats('sample1'))
          18 +nav(e,0,(1.0,-1.75)); e.turn(0,np.pi); print('home w/ full store',e.feats('rover0'),e.last)
          19 +e.act(0,(0,0,0),SEL['drop']); print('after drop',e.feats('rover0'),e.last)
diff --git a/probe_send_u.py b/probe_send_u.py
new file mode 100644
index 0000000..5684a5b
--- /dev/null
+++ b/probe_send_u.py
@@ -0,0 +1,6 @@
           1 +from probe_send_lib import *
           2 +e=E(0)
           3 +sx,sy=e.g('sample3','x'),e.g('sample3','y')
           4 +nav(e,1,(sx-0.2,sy)); 
           5 +for th in [3.14159,1.57]:
           6 +    e.turn(1,th); e.act(1,(0,0,0),SEL['sample']); print('facing',th,e.feats('rover1'),e.feats('sample3')); e.act(1,(0,0,0),SEL['drop'])
diff --git a/probe_vis_grid.py b/probe_vis_grid.py
new file mode 100644
index 0000000..8bb43dd
--- /dev/null
+++ b/probe_vis_grid.py
@@ -0,0 +1,22 @@
           1 +import sys, json, math, itertools
           2 +import numpy as np
           3 +from probe_vis_model import *
           4 +from probe_vis_lib import E
           5 +sets=[]
           6 +for f in sys.argv[1:]:
           7 +    d=json.load(open(f)); e=E(d['seed'])
           8 +    ob=e.objs()[d['obj']]; obj=(ob['x'],ob['y'],ob['z'])
           9 +    obs=[tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']) for o in e.obs if o.type.name=='obstacle']
          10 +    e.close(); sets.append((obj,obs,d['data']))
          11 +def score(**kw):
          12 +    m=0
          13 +    for obj,obs,data in sets:
          14 +        for x,y,th,c in data:
          15 +            m+= (visible(x,y,th,obj,obs,D=9,**kw)!=bool(c))
          16 +    return m
          17 +res=[]
          18 +for a in np.arange(-0.4,0.41,0.05):
          19 +    for b in np.arange(-0.2,0.21,0.05):
          20 +        for zc in list(np.arange(0.25,1.01,0.05)):
          21 +            res.append((score(a=a,b=b,zc=zc),round(a,3),round(b,3),round(zc,3)))
          22 +res.sort(); print(res[:15])
diff --git a/probe_vis_h1.py b/probe_vis_h1.py
new file mode 100644
index 0000000..c2086e5
--- /dev/null
+++ b/probe_vis_h1.py
@@ -0,0 +1,23 @@
           1 +import sys, json, math
           2 +from probe_vis_model import seg_box_hit
           3 +from probe_vis_lib import E
           4 +sets=[]
           5 +for f in sys.argv[1:]:
           6 +    d=json.load(open(f)); e=E(d['seed'])
           7 +    ob=e.objs()[d['obj']]; obj=(ob['x'],ob['y'],ob['z'])
           8 +    obs=[tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']) for o in e.obs if o.type.name=='obstacle']
           9 +    e.close(); sets.append((obj,obs,d['data']))
          10 +def vis(x,y,th,obj,obs,a,b,thr,origin_cam):
          11 +    cx=x+a*math.cos(th)-b*math.sin(th); cy=y+a*math.sin(th)+b*math.cos(th)
          12 +    for (px,py,pz,hx,hy,hz) in obs:
          13 +        if abs(px-obj[0])<=hx and abs(py-obj[1])<=hy: continue
          14 +        if seg_box_hit((cx,cy),obj[:2],(px-hx,py-hy),(px+hx,py+hy)):
          15 +            ox,oy=(cx,cy) if origin_cam else (x,y)
          16 +            rel=math.atan2(py-oy,px-ox)-th; rel=(rel+math.pi)%(2*math.pi)-math.pi
          17 +            if abs(rel)<thr: return False
          18 +    return True
          19 +for oc in [True,False]:
          20 +  for a,b in [(-0.087,-0.0125),(0,0)]:
          21 +    for thr in [1.2,1.4,1.5,1.571,1.65,1.75,1.9,2.2,3.2]:
          22 +        m=sum(vis(x,y,th,obj,obs,a,b,thr,oc)!=bool(c) for obj,obs,data in sets for x,y,th,c in data)
          23 +        print(oc,a,b,thr,m)
diff --git a/probe_vis_h2.py b/probe_vis_h2.py
new file mode 100644
index 0000000..adca868
--- /dev/null
+++ b/probe_vis_h2.py
@@ -0,0 +1,29 @@
           1 +import sys, json, math, glob
           2 +from probe_vis_model import seg_box_hit
           3 +from probe_vis_lib import E
           4 +e=E(4); ob=e.objs()['objective2']; obj=(ob['x'],ob['y'],ob['z'])
           5 +obs=[tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']) for o in e.obs if o.type.name=='obstacle']; e.close()
           6 +data=json.load(open('probe_vis_d1.json'))['data']
           7 +for f in glob.glob('probe_vis_j_*_0.75.json'): data+=json.load(open(f))
           8 +print(len(data))
           9 +def vis(x,y,th,a,b,thr,mode,infl=0.0):
          10 +    cx=x+a*math.cos(th)-b*math.sin(th); cy=y+a*math.sin(th)+b*math.cos(th)
          11 +    for (px,py,pz,hx,hy,hz) in obs:
          12 +        if abs(px-obj[0])<=hx and abs(py-obj[1])<=hy: continue
          13 +        if seg_box_hit((cx,cy),obj[:2],(px-hx-infl,py-hy-infl),(px+hx+infl,py+hy+infl)):
          14 +            if mode=='obj': tx,ty=obj[0],obj[1]
          15 +            else: tx,ty=px,py
          16 +            rel=math.atan2(ty-cy,tx-cx)-th; rel=(rel+math.pi)%(2*math.pi)-math.pi
          17 +            if abs(rel)<thr: return False
          18 +    return True
          19 +best=[]
          20 +for mode in ['obj','pil']:
          21 +  for a in [-0.06,-0.087,-0.1,-0.12,-0.15]:
          22 +    for b in [-0.0125,0.0]:
          23 +      for thr in [1.45,1.5,1.55,1.6,1.65,1.7,1.75]:
          24 +        m=sum(vis(x,y,th,a,b,thr,mode)!=bool(c) for x,y,th,c in data)
          25 +        best.append((m,mode,a,b,thr))
          26 +best.sort(); print(best[:10])
          27 +mm=[(round(th,2),round(x,3),round(y,3),c) for x,y,th,c in data if vis(x,y,th,-0.1,0.0,1.6,'obj')!=bool(c)]
          28 +mm.sort(); 
          29 +for r in mm: print(r)
diff --git a/probe_vis_i.py b/probe_vis_i.py
new file mode 100644
index 0000000..3ea7c60
--- /dev/null
+++ b/probe_vis_i.py
@@ -0,0 +1,16 @@
           1 +from probe_vis_lib import *
           2 +import sys
           3 +e=E(4)
           4 +x,y=float(sys.argv[1]),float(sys.argv[2]); N=int(sys.argv[3])
           5 +print(e.path(1,[(-1.0,-1.0),(-1.0,y),(x,y)]), e.rs(1))
           6 +s=''
           7 +blocked=[]
           8 +for k in range(N):
           9 +    th=-math.pi+k*2*math.pi/N
          10 +    e.turn(1,th)
          11 +    st=e.rs(1)
          12 +    if abs((st['theta']-th+math.pi)%(2*math.pi)-math.pi)>1e-3: s+='?'; continue
          13 +    e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img')
          14 +    s+=str(int(c))
          15 +    if not c: blocked.append(round(math.degrees(th),1))
          16 +print(s); print(blocked)
diff --git a/probe_vis_j.py b/probe_vis_j.py
new file mode 100644
index 0000000..289f004
--- /dev/null
+++ b/probe_vis_j.py
@@ -0,0 +1,14 @@
           1 +from probe_vis_lib import *
           2 +import sys, json
           3 +th=float(sys.argv[1]); y=float(sys.argv[2])
           4 +e=E(4)
           5 +e.path(1,[(-1.0,-1.0),(-1.0,y),(-2.3,y)]); e.turn(1,th)
           6 +res=[]
           7 +x=-2.3
           8 +while x<-1.55:
           9 +    ok=e.goto(1,x,y,tol=1e-7); st=e.rs(1)
          10 +    if ok:
          11 +        e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img'); res.append((st['x'],st['y'],st['theta'],int(c)))
          12 +    x+=0.005
          13 +json.dump(res,open('probe_vis_j_%s_%s.json'%(sys.argv[1],sys.argv[2]),'w'))
          14 +s=''.join(str(r[3]) for r in res); print(th, res[0][0], s)
diff --git a/probe_vis_j_-0.3927_0.75.json b/probe_vis_j_-0.3927_0.75.json
new file mode 100644
index 0000000..f81ac53
--- /dev/null
+++ b/probe_vis_j_-0.3927_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, -0.3926999866962433, 1], [-2.259999990463257, 0.75, -0.3926999866962433, 1], [-2.25, 0.75, -0.3926999866962433, 1], [-2.240000009536743, 0.75, -0.3926999866962433, 1], [-2.2300000190734863, 0.75, -0.3926999866962433, 1], [-2.2249999046325684, 0.75, -0.3926999866962433, 1], [-2.2200000286102295, 0.75, -0.3926999866962433, 1], [-2.2149999141693115, 0.75, -0.3926999866962433, 1], [-2.2100000381469727, 0.75, -0.3926999866962433, 1], [-2.2049999237060547, 0.75, -0.3926999866962433, 1], [-2.200000047683716, 0.75, -0.3926999866962433, 1], [-2.194999933242798, 0.75, -0.3926999866962433, 1], [-2.190000057220459, 0.75, -0.3926999866962433, 1], [-2.184999942779541, 0.75, -0.3926999866962433, 1], [-2.180000066757202, 0.75, -0.3926999866962433, 1], [-2.174999952316284, 0.75, -0.3926999866962433, 1], [-2.1700000762939453, 0.75, -0.3926999866962433, 1], [-2.1649999618530273, 0.75, -0.3926999866962433, 1], [-2.1600000858306885, 0.75, -0.3926999866962433, 1], [-2.1549999713897705, 0.75, -0.3926999866962433, 1], [-2.1500000953674316, 0.75, -0.3926999866962433, 1], [-2.1449999809265137, 0.75, -0.3926999866962433, 1], [-2.134999990463257, 0.75, -0.3926999866962433, 1], [-2.125, 0.75, -0.3926999866962433, 1], [-2.115000009536743, 0.75, -0.3926999866962433, 1], [-2.1050000190734863, 0.75, -0.3926999866962433, 1], [-2.0999999046325684, 0.75, -0.3926999866962433, 1], [-2.0950000286102295, 0.75, -0.3926999866962433, 1], [-2.0899999141693115, 0.75, -0.3926999866962433, 1], [-2.0850000381469727, 0.75, -0.3926999866962433, 1], [-2.0799999237060547, 0.75, -0.3926999866962433, 1], [-2.075000047683716, 0.75, -0.3926999866962433, 1], [-2.069999933242798, 0.75, -0.3926999866962433, 1], [-2.065000057220459, 0.75, -0.3926999866962433, 1], [-2.059999942779541, 0.75, -0.3926999866962433, 1], [-2.055000066757202, 0.75, -0.3926999866962433, 1], [-2.049999952316284, 0.75, -0.3926999866962433, 1], [-2.0450000762939453, 0.75, -0.3926999866962433, 1], [-2.0399999618530273, 0.75, -0.3926999866962433, 1], [-2.0350000858306885, 0.75, -0.3926999866962433, 1], [-2.0299999713897705, 0.75, -0.3926999866962433, 1], [-2.0250000953674316, 0.75, -0.3926999866962433, 1], [-2.0199999809265137, 0.75, -0.3926999866962433, 1], [-2.009999990463257, 0.75, -0.3926999866962433, 1], [-2.0, 0.75, -0.3926999866962433, 1], [-1.9950000047683716, 0.75, -0.3926999866962433, 1], [-1.9900000095367432, 0.75, -0.3926999866962433, 1], [-1.9850000143051147, 0.75, -0.3926999866962433, 1], [-1.9800000190734863, 0.75, -0.3926999866962433, 1], [-1.9749999046325684, 0.75, -0.3926999866962433, 1], [-1.9700000286102295, 0.75, -0.3926999866962433, 1], [-1.965000033378601, 0.75, -0.3926999866962433, 1], [-1.9600000381469727, 0.75, -0.3926999866962433, 1], [-1.9549999237060547, 0.75, -0.3926999866962433, 1], [-1.9500000476837158, 0.75, -0.3926999866962433, 1], [-1.9449999332427979, 0.75, -0.3926999866962433, 1], [-1.940000057220459, 0.75, -0.3926999866962433, 1], [-1.934999942779541, 0.75, -0.3926999866962433, 1], [-1.9300000667572021, 0.75, -0.3926999866962433, 1], [-1.9249999523162842, 0.75, -0.3926999866962433, 1], [-1.9200000762939453, 0.75, -0.3926999866962433, 1], [-1.9149999618530273, 0.75, -0.3926999866962433, 1], [-1.909999966621399, 0.75, -0.3926999866962433, 1], [-1.9049999713897705, 0.75, -0.3926999866962433, 1], [-1.9000000953674316, 0.75, -0.3926999866962433, 1], [-1.8949999809265137, 0.75, -0.3926999866962433, 1], [-1.8899999856948853, 0.75, -0.3926999866962433, 1], [-1.8849999904632568, 0.75, -0.3926999866962433, 1], [-1.8799999952316284, 0.75, -0.3926999866962433, 1], [-1.875, 0.75, -0.3926999866962433, 1], [-1.8700000047683716, 0.75, -0.3926999866962433, 1], [-1.8650000095367432, 0.75, -0.3926999866962433, 1], [-1.8600000143051147, 0.75, -0.3926999866962433, 1], [-1.8550000190734863, 0.75, -0.3926999866962433, 1], [-1.8499999046325684, 0.75, -0.3926999866962433, 1], [-1.8450000286102295, 0.75, -0.3926999866962433, 1], [-1.840000033378601, 0.75, -0.3926999866962433, 1], [-1.8350000381469727, 0.75, -0.3926999866962433, 1], [-1.8299999237060547, 0.75, -0.3926999866962433, 1], [-1.8250000476837158, 0.75, -0.3926999866962433, 1], [-1.8199999332427979, 0.75, -0.3926999866962433, 1], [-1.815000057220459, 0.75, -0.3926999866962433, 1], [-1.809999942779541, 0.75, -0.3926999866962433, 1], [-1.8050000667572021, 0.75, -0.3926999866962433, 1], [-1.7999999523162842, 0.75, -0.3926999866962433, 1], [-1.7950000762939453, 0.75, -0.3926999866962433, 1], [-1.7899999618530273, 0.75, -0.3926999866962433, 1], [-1.784999966621399, 0.75, -0.3926999866962433, 1], [-1.7799999713897705, 0.75, -0.3926999866962433, 1], [-1.7750000953674316, 0.75, -0.3926999866962433, 1], [-1.7699999809265137, 0.75, -0.3926999866962433, 1], [-1.7649999856948853, 0.75, -0.3926999866962433, 1], [-1.7599999904632568, 0.75, -0.3926999866962433, 1], [-1.7549999952316284, 0.75, -0.3926999866962433, 1], [-1.75, 0.75, -0.3926999866962433, 1], [-1.7450000047683716, 0.75, -0.3926999866962433, 1], [-1.7400000095367432, 0.75, -0.3926999866962433, 1], [-1.7350000143051147, 0.75, -0.3926999866962433, 1], [-1.7300000190734863, 0.75, -0.3926999866962433, 1], [-1.7249999046325684, 0.75, -0.3926999866962433, 1], [-1.7200000286102295, 0.75, -0.3926999866962433, 1], [-1.715000033378601, 0.75, -0.3926999866962433, 1], [-1.7100000381469727, 0.75, -0.3926999866962433, 1], [-1.7049999237060547, 0.75, -0.3926999866962433, 1], [-1.7000000476837158, 0.75, -0.3926999866962433, 1], [-1.6949999332427979, 0.75, -0.3926999866962433, 1], [-1.690000057220459, 0.75, -0.3926999866962433, 1], [-1.684999942779541, 0.75, -0.3926999866962433, 1], [-1.6800000667572021, 0.75, -0.3926999866962433, 1], [-1.6749999523162842, 0.75, -0.3926999866962433, 1], [-1.6700000762939453, 0.75, -0.3926999866962433, 1], [-1.6649999618530273, 0.75, -0.3926999866962433, 1], [-1.659999966621399, 0.75, -0.3926999866962433, 1], [-1.6549999713897705, 0.75, -0.3926999866962433, 1], [-1.6500000953674316, 0.75, -0.3926999866962433, 1], [-1.6449999809265137, 0.75, -0.3926999866962433, 1], [-1.6399999856948853, 0.75, -0.3926999866962433, 1], [-1.6349999904632568, 0.75, -0.3926999866962433, 1], [-1.6299999952316284, 0.75, -0.3926999866962433, 1], [-1.625, 0.75, -0.3926999866962433, 1], [-1.6200000047683716, 0.75, -0.3926999866962433, 1], [-1.6150000095367432, 0.75, -0.3926999866962433, 1], [-1.6100000143051147, 0.75, -0.3926999866962433, 1], [-1.6050000190734863, 0.75, -0.3926999866962433, 1], [-1.5999999046325684, 0.75, -0.3926999866962433, 1], [-1.5950000286102295, 0.75, -0.3926999866962433, 1], [-1.590000033378601, 0.75, -0.3926999866962433, 1], [-1.5850000381469727, 0.75, -0.3926999866962433, 1], [-1.5799999237060547, 0.75, -0.3926999866962433, 1], [-1.5750000476837158, 0.75, -0.3926999866962433, 1], [-1.5699999332427979, 0.75, -0.3926999866962433, 1], [-1.565000057220459, 0.75, -0.3926999866962433, 1], [-1.559999942779541, 0.75, -0.3926999866962433, 1], [-1.5550000667572021, 0.75, -0.3926999866962433, 1], [-1.5499999523162842, 0.75, -0.3926999866962433, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_-0.7854_0.75.json b/probe_vis_j_-0.7854_0.75.json
new file mode 100644
index 0000000..a47036e
--- /dev/null
+++ b/probe_vis_j_-0.7854_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, -0.7853999733924866, 1], [-2.259999990463257, 0.75, -0.7853999733924866, 1], [-2.25, 0.75, -0.7853999733924866, 1], [-2.240000009536743, 0.75, -0.7853999733924866, 1], [-2.2300000190734863, 0.75, -0.7853999733924866, 1], [-2.2249999046325684, 0.75, -0.7853999733924866, 1], [-2.2200000286102295, 0.75, -0.7853999733924866, 1], [-2.2149999141693115, 0.75, -0.7853999733924866, 1], [-2.2100000381469727, 0.75, -0.7853999733924866, 1], [-2.2049999237060547, 0.75, -0.7853999733924866, 1], [-2.200000047683716, 0.75, -0.7853999733924866, 1], [-2.194999933242798, 0.75, -0.7853999733924866, 1], [-2.190000057220459, 0.75, -0.7853999733924866, 1], [-2.184999942779541, 0.75, -0.7853999733924866, 1], [-2.180000066757202, 0.75, -0.7853999733924866, 1], [-2.174999952316284, 0.75, -0.7853999733924866, 1], [-2.1700000762939453, 0.75, -0.7853999733924866, 1], [-2.1649999618530273, 0.75, -0.7853999733924866, 1], [-2.1600000858306885, 0.75, -0.7853999733924866, 1], [-2.1549999713897705, 0.75, -0.7853999733924866, 1], [-2.1500000953674316, 0.75, -0.7853999733924866, 1], [-2.1449999809265137, 0.75, -0.7853999733924866, 1], [-2.134999990463257, 0.75, -0.7853999733924866, 1], [-2.125, 0.75, -0.7853999733924866, 1], [-2.115000009536743, 0.75, -0.7853999733924866, 1], [-2.1050000190734863, 0.75, -0.7853999733924866, 1], [-2.0999999046325684, 0.75, -0.7853999733924866, 1], [-2.0950000286102295, 0.75, -0.7853999733924866, 1], [-2.0899999141693115, 0.75, -0.7853999733924866, 1], [-2.0850000381469727, 0.75, -0.7853999733924866, 1], [-2.0799999237060547, 0.75, -0.7853999733924866, 1], [-2.075000047683716, 0.75, -0.7853999733924866, 1], [-2.069999933242798, 0.75, -0.7853999733924866, 1], [-2.065000057220459, 0.75, -0.7853999733924866, 1], [-2.059999942779541, 0.75, -0.7853999733924866, 1], [-2.055000066757202, 0.75, -0.7853999733924866, 1], [-2.049999952316284, 0.75, -0.7853999733924866, 1], [-2.0450000762939453, 0.75, -0.7853999733924866, 1], [-2.0399999618530273, 0.75, -0.7853999733924866, 1], [-2.0350000858306885, 0.75, -0.7853999733924866, 1], [-2.0299999713897705, 0.75, -0.7853999733924866, 1], [-2.0250000953674316, 0.75, -0.7853999733924866, 1], [-2.0199999809265137, 0.75, -0.7853999733924866, 1], [-2.009999990463257, 0.75, -0.7853999733924866, 1], [-2.0, 0.75, -0.7853999733924866, 1], [-1.9950000047683716, 0.75, -0.7853999733924866, 1], [-1.9900000095367432, 0.75, -0.7853999733924866, 1], [-1.9850000143051147, 0.75, -0.7853999733924866, 1], [-1.9800000190734863, 0.75, -0.7853999733924866, 1], [-1.9749999046325684, 0.75, -0.7853999733924866, 1], [-1.9700000286102295, 0.75, -0.7853999733924866, 1], [-1.965000033378601, 0.75, -0.7853999733924866, 1], [-1.9600000381469727, 0.75, -0.7853999733924866, 1], [-1.9549999237060547, 0.75, -0.7853999733924866, 1], [-1.9500000476837158, 0.75, -0.7853999733924866, 1], [-1.9449999332427979, 0.75, -0.7853999733924866, 1], [-1.940000057220459, 0.75, -0.7853999733924866, 1], [-1.934999942779541, 0.75, -0.7853999733924866, 1], [-1.9300000667572021, 0.75, -0.7853999733924866, 1], [-1.9249999523162842, 0.75, -0.7853999733924866, 1], [-1.9200000762939453, 0.75, -0.7853999733924866, 1], [-1.9149999618530273, 0.75, -0.7853999733924866, 1], [-1.909999966621399, 0.75, -0.7853999733924866, 1], [-1.9049999713897705, 0.75, -0.7853999733924866, 1], [-1.9000000953674316, 0.75, -0.7853999733924866, 1], [-1.8949999809265137, 0.75, -0.7853999733924866, 1], [-1.8899999856948853, 0.75, -0.7853999733924866, 1], [-1.8849999904632568, 0.75, -0.7853999733924866, 1], [-1.8799999952316284, 0.75, -0.7853999733924866, 1], [-1.875, 0.75, -0.7853999733924866, 1], [-1.8700000047683716, 0.75, -0.7853999733924866, 1], [-1.8650000095367432, 0.75, -0.7853999733924866, 1], [-1.8600000143051147, 0.75, -0.7853999733924866, 1], [-1.8550000190734863, 0.75, -0.7853999733924866, 1], [-1.8499999046325684, 0.75, -0.7853999733924866, 1], [-1.8450000286102295, 0.75, -0.7853999733924866, 1], [-1.840000033378601, 0.75, -0.7853999733924866, 1], [-1.8350000381469727, 0.75, -0.7853999733924866, 1], [-1.8299999237060547, 0.75, -0.7853999733924866, 1], [-1.8250000476837158, 0.75, -0.7853999733924866, 1], [-1.8199999332427979, 0.75, -0.7853999733924866, 1], [-1.815000057220459, 0.75, -0.7853999733924866, 1], [-1.809999942779541, 0.75, -0.7853999733924866, 1], [-1.8050000667572021, 0.75, -0.7853999733924866, 1], [-1.7999999523162842, 0.75, -0.7853999733924866, 1], [-1.7950000762939453, 0.75, -0.7853999733924866, 1], [-1.7899999618530273, 0.75, -0.7853999733924866, 1], [-1.784999966621399, 0.75, -0.7853999733924866, 1], [-1.7799999713897705, 0.75, -0.7853999733924866, 1], [-1.7750000953674316, 0.75, -0.7853999733924866, 1], [-1.7699999809265137, 0.75, -0.7853999733924866, 1], [-1.7649999856948853, 0.75, -0.7853999733924866, 1], [-1.7599999904632568, 0.75, -0.7853999733924866, 1], [-1.7549999952316284, 0.75, -0.7853999733924866, 1], [-1.75, 0.75, -0.7853999733924866, 1], [-1.7450000047683716, 0.75, -0.7853999733924866, 1], [-1.7400000095367432, 0.75, -0.7853999733924866, 1], [-1.7350000143051147, 0.75, -0.7853999733924866, 1], [-1.7300000190734863, 0.75, -0.7853999733924866, 1], [-1.7249999046325684, 0.75, -0.7853999733924866, 1], [-1.7200000286102295, 0.75, -0.7853999733924866, 1], [-1.715000033378601, 0.75, -0.7853999733924866, 1], [-1.7100000381469727, 0.75, -0.7853999733924866, 1], [-1.7049999237060547, 0.75, -0.7853999733924866, 1], [-1.7000000476837158, 0.75, -0.7853999733924866, 1], [-1.6949999332427979, 0.75, -0.7853999733924866, 1], [-1.690000057220459, 0.75, -0.7853999733924866, 1], [-1.684999942779541, 0.75, -0.7853999733924866, 1], [-1.6800000667572021, 0.75, -0.7853999733924866, 1], [-1.6749999523162842, 0.75, -0.7853999733924866, 1], [-1.6700000762939453, 0.75, -0.7853999733924866, 1], [-1.6649999618530273, 0.75, -0.7853999733924866, 1], [-1.659999966621399, 0.75, -0.7853999733924866, 1], [-1.6549999713897705, 0.75, -0.7853999733924866, 1], [-1.6500000953674316, 0.75, -0.7853999733924866, 1], [-1.6449999809265137, 0.75, -0.7853999733924866, 1], [-1.6399999856948853, 0.75, -0.7853999733924866, 1], [-1.6349999904632568, 0.75, -0.7853999733924866, 1], [-1.6299999952316284, 0.75, -0.7853999733924866, 1], [-1.625, 0.75, -0.7853999733924866, 1], [-1.6200000047683716, 0.75, -0.7853999733924866, 1], [-1.6150000095367432, 0.75, -0.7853999733924866, 1], [-1.6100000143051147, 0.75, -0.7853999733924866, 1], [-1.6050000190734863, 0.75, -0.7853999733924866, 1], [-1.5999999046325684, 0.75, -0.7853999733924866, 1], [-1.5950000286102295, 0.75, -0.7853999733924866, 1], [-1.590000033378601, 0.75, -0.7853999733924866, 1], [-1.5850000381469727, 0.75, -0.7853999733924866, 1], [-1.5799999237060547, 0.75, -0.7853999733924866, 1], [-1.5750000476837158, 0.75, -0.7853999733924866, 1], [-1.5699999332427979, 0.75, -0.7853999733924866, 1], [-1.565000057220459, 0.75, -0.7853999733924866, 1], [-1.559999942779541, 0.75, -0.7853999733924866, 1], [-1.5550000667572021, 0.75, -0.7853999733924866, 1], [-1.5499999523162842, 0.75, -0.7853999733924866, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_-1.1781_0.75.json b/probe_vis_j_-1.1781_0.75.json
new file mode 100644
index 0000000..a978eee
--- /dev/null
+++ b/probe_vis_j_-1.1781_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, -1.1780999898910522, 1], [-2.259999990463257, 0.75, -1.1780999898910522, 1], [-2.25, 0.75, -1.1780999898910522, 1], [-2.240000009536743, 0.75, -1.1780999898910522, 1], [-2.2300000190734863, 0.75, -1.1780999898910522, 1], [-2.2249999046325684, 0.75, -1.1780999898910522, 1], [-2.2200000286102295, 0.75, -1.1780999898910522, 1], [-2.2149999141693115, 0.75, -1.1780999898910522, 1], [-2.2100000381469727, 0.75, -1.1780999898910522, 1], [-2.2049999237060547, 0.75, -1.1780999898910522, 1], [-2.200000047683716, 0.75, -1.1780999898910522, 1], [-2.194999933242798, 0.75, -1.1780999898910522, 1], [-2.190000057220459, 0.75, -1.1780999898910522, 1], [-2.184999942779541, 0.75, -1.1780999898910522, 1], [-2.180000066757202, 0.75, -1.1780999898910522, 1], [-2.174999952316284, 0.75, -1.1780999898910522, 1], [-2.1700000762939453, 0.75, -1.1780999898910522, 1], [-2.1649999618530273, 0.75, -1.1780999898910522, 1], [-2.1600000858306885, 0.75, -1.1780999898910522, 1], [-2.1549999713897705, 0.75, -1.1780999898910522, 1], [-2.1500000953674316, 0.75, -1.1780999898910522, 1], [-2.1449999809265137, 0.75, -1.1780999898910522, 1], [-2.134999990463257, 0.75, -1.1780999898910522, 1], [-2.125, 0.75, -1.1780999898910522, 1], [-2.115000009536743, 0.75, -1.1780999898910522, 1], [-2.1050000190734863, 0.75, -1.1780999898910522, 1], [-2.0999999046325684, 0.75, -1.1780999898910522, 1], [-2.0950000286102295, 0.75, -1.1780999898910522, 1], [-2.0899999141693115, 0.75, -1.1780999898910522, 1], [-2.0850000381469727, 0.75, -1.1780999898910522, 1], [-2.0799999237060547, 0.75, -1.1780999898910522, 1], [-2.075000047683716, 0.75, -1.1780999898910522, 1], [-2.069999933242798, 0.75, -1.1780999898910522, 1], [-2.065000057220459, 0.75, -1.1780999898910522, 1], [-2.059999942779541, 0.75, -1.1780999898910522, 1], [-2.055000066757202, 0.75, -1.1780999898910522, 1], [-2.049999952316284, 0.75, -1.1780999898910522, 1], [-2.0450000762939453, 0.75, -1.1780999898910522, 1], [-2.0399999618530273, 0.75, -1.1780999898910522, 1], [-2.0350000858306885, 0.75, -1.1780999898910522, 1], [-2.0299999713897705, 0.75, -1.1780999898910522, 1], [-2.0250000953674316, 0.75, -1.1780999898910522, 1], [-2.0199999809265137, 0.75, -1.1780999898910522, 1], [-2.009999990463257, 0.75, -1.1780999898910522, 1], [-2.0, 0.75, -1.1780999898910522, 1], [-1.9950000047683716, 0.75, -1.1780999898910522, 1], [-1.9900000095367432, 0.75, -1.1780999898910522, 1], [-1.9850000143051147, 0.75, -1.1780999898910522, 1], [-1.9800000190734863, 0.75, -1.1780999898910522, 1], [-1.9749999046325684, 0.75, -1.1780999898910522, 1], [-1.9700000286102295, 0.75, -1.1780999898910522, 1], [-1.965000033378601, 0.75, -1.1780999898910522, 1], [-1.9600000381469727, 0.75, -1.1780999898910522, 1], [-1.9549999237060547, 0.75, -1.1780999898910522, 1], [-1.9500000476837158, 0.75, -1.1780999898910522, 1], [-1.9449999332427979, 0.75, -1.1780999898910522, 1], [-1.940000057220459, 0.75, -1.1780999898910522, 1], [-1.934999942779541, 0.75, -1.1780999898910522, 1], [-1.9300000667572021, 0.75, -1.1780999898910522, 1], [-1.9249999523162842, 0.75, -1.1780999898910522, 1], [-1.9200000762939453, 0.75, -1.1780999898910522, 1], [-1.9149999618530273, 0.75, -1.1780999898910522, 1], [-1.909999966621399, 0.75, -1.1780999898910522, 1], [-1.9049999713897705, 0.75, -1.1780999898910522, 1], [-1.9000000953674316, 0.75, -1.1780999898910522, 1], [-1.8949999809265137, 0.75, -1.1780999898910522, 1], [-1.8899999856948853, 0.75, -1.1780999898910522, 1], [-1.8849999904632568, 0.75, -1.1780999898910522, 1], [-1.8799999952316284, 0.75, -1.1780999898910522, 1], [-1.875, 0.75, -1.1780999898910522, 1], [-1.8700000047683716, 0.75, -1.1780999898910522, 1], [-1.8650000095367432, 0.75, -1.1780999898910522, 1], [-1.8600000143051147, 0.75, -1.1780999898910522, 1], [-1.8550000190734863, 0.75, -1.1780999898910522, 1], [-1.8499999046325684, 0.75, -1.1780999898910522, 1], [-1.8450000286102295, 0.75, -1.1780999898910522, 1], [-1.840000033378601, 0.75, -1.1780999898910522, 1], [-1.8350000381469727, 0.75, -1.1780999898910522, 1], [-1.8299999237060547, 0.75, -1.1780999898910522, 1], [-1.8250000476837158, 0.75, -1.1780999898910522, 1], [-1.8199999332427979, 0.75, -1.1780999898910522, 1], [-1.815000057220459, 0.75, -1.1780999898910522, 1], [-1.809999942779541, 0.75, -1.1780999898910522, 1], [-1.8050000667572021, 0.75, -1.1780999898910522, 1], [-1.7999999523162842, 0.75, -1.1780999898910522, 1], [-1.7950000762939453, 0.75, -1.1780999898910522, 1], [-1.7899999618530273, 0.75, -1.1780999898910522, 1], [-1.784999966621399, 0.75, -1.1780999898910522, 1], [-1.7799999713897705, 0.75, -1.1780999898910522, 1], [-1.7750000953674316, 0.75, -1.1780999898910522, 1], [-1.7699999809265137, 0.75, -1.1780999898910522, 1], [-1.7649999856948853, 0.75, -1.1780999898910522, 1], [-1.7599999904632568, 0.75, -1.1780999898910522, 1], [-1.7549999952316284, 0.75, -1.1780999898910522, 1], [-1.75, 0.75, -1.1780999898910522, 1], [-1.7450000047683716, 0.75, -1.1780999898910522, 1], [-1.7400000095367432, 0.75, -1.1780999898910522, 1], [-1.7350000143051147, 0.75, -1.1780999898910522, 1], [-1.7300000190734863, 0.75, -1.1780999898910522, 1], [-1.7249999046325684, 0.75, -1.1780999898910522, 1], [-1.7200000286102295, 0.75, -1.1780999898910522, 1], [-1.715000033378601, 0.75, -1.1780999898910522, 1], [-1.7100000381469727, 0.75, -1.1780999898910522, 1], [-1.7049999237060547, 0.75, -1.1780999898910522, 1], [-1.7000000476837158, 0.75, -1.1780999898910522, 1], [-1.6949999332427979, 0.75, -1.1780999898910522, 1], [-1.690000057220459, 0.75, -1.1780999898910522, 1], [-1.684999942779541, 0.75, -1.1780999898910522, 1], [-1.6800000667572021, 0.75, -1.1780999898910522, 1], [-1.6749999523162842, 0.75, -1.1780999898910522, 1], [-1.6700000762939453, 0.75, -1.1780999898910522, 1], [-1.6649999618530273, 0.75, -1.1780999898910522, 1], [-1.659999966621399, 0.75, -1.1780999898910522, 1], [-1.6549999713897705, 0.75, -1.1780999898910522, 1], [-1.6500000953674316, 0.75, -1.1780999898910522, 1], [-1.6449999809265137, 0.75, -1.1780999898910522, 1], [-1.6399999856948853, 0.75, -1.1780999898910522, 1], [-1.6349999904632568, 0.75, -1.1780999898910522, 1], [-1.6299999952316284, 0.75, -1.1780999898910522, 1], [-1.625, 0.75, -1.1780999898910522, 1], [-1.6200000047683716, 0.75, -1.1780999898910522, 1], [-1.6150000095367432, 0.75, -1.1780999898910522, 1], [-1.6100000143051147, 0.75, -1.1780999898910522, 1], [-1.6050000190734863, 0.75, -1.1780999898910522, 1], [-1.5999999046325684, 0.75, -1.1780999898910522, 1], [-1.5950000286102295, 0.75, -1.1780999898910522, 1], [-1.590000033378601, 0.75, -1.1780999898910522, 1], [-1.5850000381469727, 0.75, -1.1780999898910522, 1], [-1.5799999237060547, 0.75, -1.1780999898910522, 1], [-1.5750000476837158, 0.75, -1.1780999898910522, 1], [-1.5699999332427979, 0.75, -1.1780999898910522, 1], [-1.565000057220459, 0.75, -1.1780999898910522, 1], [-1.559999942779541, 0.75, -1.1780999898910522, 1], [-1.5550000667572021, 0.75, -1.1780999898910522, 1], [-1.5499999523162842, 0.75, -1.1780999898910522, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_-1.5708_0.75.json b/probe_vis_j_-1.5708_0.75.json
new file mode 100644
index 0000000..b691494
--- /dev/null
+++ b/probe_vis_j_-1.5708_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, -1.5707999467849731, 1], [-2.259999990463257, 0.75, -1.5707999467849731, 1], [-2.25, 0.75, -1.5707999467849731, 1], [-2.240000009536743, 0.75, -1.5707999467849731, 1], [-2.2300000190734863, 0.75, -1.5707999467849731, 1], [-2.2249999046325684, 0.75, -1.5707999467849731, 1], [-2.2200000286102295, 0.75, -1.5707999467849731, 1], [-2.2149999141693115, 0.75, -1.5707999467849731, 1], [-2.2100000381469727, 0.75, -1.5707999467849731, 1], [-2.2049999237060547, 0.75, -1.5707999467849731, 1], [-2.200000047683716, 0.75, -1.5707999467849731, 1], [-2.194999933242798, 0.75, -1.5707999467849731, 1], [-2.190000057220459, 0.75, -1.5707999467849731, 1], [-2.184999942779541, 0.75, -1.5707999467849731, 1], [-2.180000066757202, 0.75, -1.5707999467849731, 1], [-2.174999952316284, 0.75, -1.5707999467849731, 1], [-2.1700000762939453, 0.75, -1.5707999467849731, 1], [-2.1649999618530273, 0.75, -1.5707999467849731, 1], [-2.1600000858306885, 0.75, -1.5707999467849731, 1], [-2.1549999713897705, 0.75, -1.5707999467849731, 1], [-2.1500000953674316, 0.75, -1.5707999467849731, 1], [-2.1449999809265137, 0.75, -1.5707999467849731, 1], [-2.134999990463257, 0.75, -1.5707999467849731, 1], [-2.125, 0.75, -1.5707999467849731, 1], [-2.115000009536743, 0.75, -1.5707999467849731, 1], [-2.1050000190734863, 0.75, -1.5707999467849731, 1], [-2.0999999046325684, 0.75, -1.5707999467849731, 1], [-2.0950000286102295, 0.75, -1.5707999467849731, 1], [-2.0899999141693115, 0.75, -1.5707999467849731, 1], [-2.0850000381469727, 0.75, -1.5707999467849731, 1], [-2.0799999237060547, 0.75, -1.5707999467849731, 1], [-2.075000047683716, 0.75, -1.5707999467849731, 1], [-2.069999933242798, 0.75, -1.5707999467849731, 1], [-2.065000057220459, 0.75, -1.5707999467849731, 1], [-2.059999942779541, 0.75, -1.5707999467849731, 1], [-2.055000066757202, 0.75, -1.5707999467849731, 1], [-2.049999952316284, 0.75, -1.5707999467849731, 1], [-2.0450000762939453, 0.75, -1.5707999467849731, 1], [-2.0399999618530273, 0.75, -1.5707999467849731, 1], [-2.0350000858306885, 0.75, -1.5707999467849731, 1], [-2.0299999713897705, 0.75, -1.5707999467849731, 1], [-2.0250000953674316, 0.75, -1.5707999467849731, 1], [-2.0199999809265137, 0.75, -1.5707999467849731, 1], [-2.009999990463257, 0.75, -1.5707999467849731, 1], [-2.0, 0.75, -1.5707999467849731, 1], [-1.9950000047683716, 0.75, -1.5707999467849731, 1], [-1.9900000095367432, 0.75, -1.5707999467849731, 1], [-1.9850000143051147, 0.75, -1.5707999467849731, 1], [-1.9800000190734863, 0.75, -1.5707999467849731, 1], [-1.9749999046325684, 0.75, -1.5707999467849731, 1], [-1.9700000286102295, 0.75, -1.5707999467849731, 1], [-1.965000033378601, 0.75, -1.5707999467849731, 1], [-1.9600000381469727, 0.75, -1.5707999467849731, 1], [-1.9549999237060547, 0.75, -1.5707999467849731, 1], [-1.9500000476837158, 0.75, -1.5707999467849731, 1], [-1.9449999332427979, 0.75, -1.5707999467849731, 1], [-1.940000057220459, 0.75, -1.5707999467849731, 1], [-1.934999942779541, 0.75, -1.5707999467849731, 1], [-1.9300000667572021, 0.75, -1.5707999467849731, 1], [-1.9249999523162842, 0.75, -1.5707999467849731, 1], [-1.9200000762939453, 0.75, -1.5707999467849731, 1], [-1.9149999618530273, 0.75, -1.5707999467849731, 1], [-1.909999966621399, 0.75, -1.5707999467849731, 1], [-1.9049999713897705, 0.75, -1.5707999467849731, 1], [-1.9000000953674316, 0.75, -1.5707999467849731, 1], [-1.8949999809265137, 0.75, -1.5707999467849731, 1], [-1.8899999856948853, 0.75, -1.5707999467849731, 1], [-1.8849999904632568, 0.75, -1.5707999467849731, 1], [-1.8799999952316284, 0.75, -1.5707999467849731, 1], [-1.875, 0.75, -1.5707999467849731, 1], [-1.8700000047683716, 0.75, -1.5707999467849731, 1], [-1.8650000095367432, 0.75, -1.5707999467849731, 1], [-1.8600000143051147, 0.75, -1.5707999467849731, 1], [-1.8550000190734863, 0.75, -1.5707999467849731, 1], [-1.8499999046325684, 0.75, -1.5707999467849731, 1], [-1.8450000286102295, 0.75, -1.5707999467849731, 1], [-1.840000033378601, 0.75, -1.5707999467849731, 1], [-1.8350000381469727, 0.75, -1.5707999467849731, 1], [-1.8299999237060547, 0.75, -1.5707999467849731, 1], [-1.8250000476837158, 0.75, -1.5707999467849731, 1], [-1.8199999332427979, 0.75, -1.5707999467849731, 1], [-1.815000057220459, 0.75, -1.5707999467849731, 1], [-1.809999942779541, 0.75, -1.5707999467849731, 1], [-1.8050000667572021, 0.75, -1.5707999467849731, 1], [-1.7999999523162842, 0.75, -1.5707999467849731, 1], [-1.7950000762939453, 0.75, -1.5707999467849731, 1], [-1.7899999618530273, 0.75, -1.5707999467849731, 1], [-1.784999966621399, 0.75, -1.5707999467849731, 1], [-1.7799999713897705, 0.75, -1.5707999467849731, 1], [-1.7750000953674316, 0.75, -1.5707999467849731, 1], [-1.7699999809265137, 0.75, -1.5707999467849731, 1], [-1.7649999856948853, 0.75, -1.5707999467849731, 1], [-1.7599999904632568, 0.75, -1.5707999467849731, 1], [-1.7549999952316284, 0.75, -1.5707999467849731, 1], [-1.75, 0.75, -1.5707999467849731, 1], [-1.7450000047683716, 0.75, -1.5707999467849731, 1], [-1.7400000095367432, 0.75, -1.5707999467849731, 1], [-1.7350000143051147, 0.75, -1.5707999467849731, 1], [-1.7300000190734863, 0.75, -1.5707999467849731, 1], [-1.7249999046325684, 0.75, -1.5707999467849731, 1], [-1.7200000286102295, 0.75, -1.5707999467849731, 1], [-1.715000033378601, 0.75, -1.5707999467849731, 1], [-1.7100000381469727, 0.75, -1.5707999467849731, 1], [-1.7049999237060547, 0.75, -1.5707999467849731, 1], [-1.7000000476837158, 0.75, -1.5707999467849731, 1], [-1.6949999332427979, 0.75, -1.5707999467849731, 1], [-1.690000057220459, 0.75, -1.5707999467849731, 1], [-1.684999942779541, 0.75, -1.5707999467849731, 1], [-1.6800000667572021, 0.75, -1.5707999467849731, 1], [-1.6749999523162842, 0.75, -1.5707999467849731, 1], [-1.6700000762939453, 0.75, -1.5707999467849731, 1], [-1.6649999618530273, 0.75, -1.5707999467849731, 1], [-1.659999966621399, 0.75, -1.5707999467849731, 1], [-1.6549999713897705, 0.75, -1.5707999467849731, 1], [-1.6500000953674316, 0.75, -1.5707999467849731, 1], [-1.6449999809265137, 0.75, -1.5707999467849731, 1], [-1.6399999856948853, 0.75, -1.5707999467849731, 1], [-1.6349999904632568, 0.75, -1.5707999467849731, 1], [-1.6299999952316284, 0.75, -1.5707999467849731, 1], [-1.625, 0.75, -1.5707999467849731, 1], [-1.6200000047683716, 0.75, -1.5707999467849731, 1], [-1.6150000095367432, 0.75, -1.5707999467849731, 1], [-1.6100000143051147, 0.75, -1.5707999467849731, 1], [-1.6050000190734863, 0.75, -1.5707999467849731, 1], [-1.5999999046325684, 0.75, -1.5707999467849731, 1], [-1.5950000286102295, 0.75, -1.5707999467849731, 1], [-1.590000033378601, 0.75, -1.5707999467849731, 1], [-1.5850000381469727, 0.75, -1.5707999467849731, 1], [-1.5799999237060547, 0.75, -1.5707999467849731, 1], [-1.5750000476837158, 0.75, -1.5707999467849731, 1], [-1.5699999332427979, 0.75, -1.5707999467849731, 1], [-1.565000057220459, 0.75, -1.5707999467849731, 1], [-1.559999942779541, 0.75, -1.5707999467849731, 1], [-1.5550000667572021, 0.75, -1.5707999467849731, 1], [-1.5499999523162842, 0.75, -1.5707999467849731, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_-1.9635_0.75.json b/probe_vis_j_-1.9635_0.75.json
new file mode 100644
index 0000000..2b350d8
--- /dev/null
+++ b/probe_vis_j_-1.9635_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, -1.9635000228881836, 1], [-2.259999990463257, 0.75, -1.9635000228881836, 1], [-2.25, 0.75, -1.9635000228881836, 1], [-2.240000009536743, 0.75, -1.9635000228881836, 1], [-2.2300000190734863, 0.75, -1.9635000228881836, 1], [-2.2249999046325684, 0.75, -1.9635000228881836, 1], [-2.2200000286102295, 0.75, -1.9635000228881836, 1], [-2.2149999141693115, 0.75, -1.9635000228881836, 1], [-2.2100000381469727, 0.75, -1.9635000228881836, 1], [-2.2049999237060547, 0.75, -1.9635000228881836, 1], [-2.200000047683716, 0.75, -1.9635000228881836, 1], [-2.194999933242798, 0.75, -1.9635000228881836, 1], [-2.190000057220459, 0.75, -1.9635000228881836, 1], [-2.184999942779541, 0.75, -1.9635000228881836, 1], [-2.180000066757202, 0.75, -1.9635000228881836, 1], [-2.174999952316284, 0.75, -1.9635000228881836, 1], [-2.1700000762939453, 0.75, -1.9635000228881836, 1], [-2.1649999618530273, 0.75, -1.9635000228881836, 1], [-2.1600000858306885, 0.75, -1.9635000228881836, 1], [-2.1549999713897705, 0.75, -1.9635000228881836, 1], [-2.1500000953674316, 0.75, -1.9635000228881836, 1], [-2.1449999809265137, 0.75, -1.9635000228881836, 1], [-2.134999990463257, 0.75, -1.9635000228881836, 1], [-2.125, 0.75, -1.9635000228881836, 1], [-2.115000009536743, 0.75, -1.9635000228881836, 1], [-2.1050000190734863, 0.75, -1.9635000228881836, 1], [-2.0999999046325684, 0.75, -1.9635000228881836, 1], [-2.0950000286102295, 0.75, -1.9635000228881836, 1], [-2.0899999141693115, 0.75, -1.9635000228881836, 1], [-2.0850000381469727, 0.75, -1.9635000228881836, 1], [-2.0799999237060547, 0.75, -1.9635000228881836, 1], [-2.075000047683716, 0.75, -1.9635000228881836, 1], [-2.069999933242798, 0.75, -1.9635000228881836, 1], [-2.065000057220459, 0.75, -1.9635000228881836, 1], [-2.059999942779541, 0.75, -1.9635000228881836, 1], [-2.055000066757202, 0.75, -1.9635000228881836, 1], [-2.049999952316284, 0.75, -1.9635000228881836, 1], [-2.0450000762939453, 0.75, -1.9635000228881836, 1], [-2.0399999618530273, 0.75, -1.9635000228881836, 1], [-2.0350000858306885, 0.75, -1.9635000228881836, 1], [-2.0299999713897705, 0.75, -1.9635000228881836, 1], [-2.0250000953674316, 0.75, -1.9635000228881836, 1], [-2.0199999809265137, 0.75, -1.9635000228881836, 1], [-2.009999990463257, 0.75, -1.9635000228881836, 1], [-2.0, 0.75, -1.9635000228881836, 1], [-1.9950000047683716, 0.75, -1.9635000228881836, 1], [-1.9900000095367432, 0.75, -1.9635000228881836, 1], [-1.9850000143051147, 0.75, -1.9635000228881836, 1], [-1.9800000190734863, 0.75, -1.9635000228881836, 1], [-1.9749999046325684, 0.75, -1.9635000228881836, 1], [-1.9700000286102295, 0.75, -1.9635000228881836, 1], [-1.965000033378601, 0.75, -1.9635000228881836, 1], [-1.9600000381469727, 0.75, -1.9635000228881836, 1], [-1.9549999237060547, 0.75, -1.9635000228881836, 1], [-1.9500000476837158, 0.75, -1.9635000228881836, 1], [-1.9449999332427979, 0.75, -1.9635000228881836, 1], [-1.940000057220459, 0.75, -1.9635000228881836, 1], [-1.934999942779541, 0.75, -1.9635000228881836, 1], [-1.9300000667572021, 0.75, -1.9635000228881836, 1], [-1.9249999523162842, 0.75, -1.9635000228881836, 1], [-1.9200000762939453, 0.75, -1.9635000228881836, 1], [-1.9149999618530273, 0.75, -1.9635000228881836, 1], [-1.909999966621399, 0.75, -1.9635000228881836, 1], [-1.9049999713897705, 0.75, -1.9635000228881836, 1], [-1.9000000953674316, 0.75, -1.9635000228881836, 1], [-1.8949999809265137, 0.75, -1.9635000228881836, 1], [-1.8899999856948853, 0.75, -1.9635000228881836, 1], [-1.8849999904632568, 0.75, -1.9635000228881836, 1], [-1.8799999952316284, 0.75, -1.9635000228881836, 1], [-1.875, 0.75, -1.9635000228881836, 1], [-1.8700000047683716, 0.75, -1.9635000228881836, 1], [-1.8650000095367432, 0.75, -1.9635000228881836, 1], [-1.8600000143051147, 0.75, -1.9635000228881836, 1], [-1.8550000190734863, 0.75, -1.9635000228881836, 1], [-1.8499999046325684, 0.75, -1.9635000228881836, 1], [-1.8450000286102295, 0.75, -1.9635000228881836, 1], [-1.840000033378601, 0.75, -1.9635000228881836, 1], [-1.8350000381469727, 0.75, -1.9635000228881836, 1], [-1.8299999237060547, 0.75, -1.9635000228881836, 1], [-1.8250000476837158, 0.75, -1.9635000228881836, 1], [-1.8199999332427979, 0.75, -1.9635000228881836, 1], [-1.815000057220459, 0.75, -1.9635000228881836, 1], [-1.809999942779541, 0.75, -1.9635000228881836, 1], [-1.8050000667572021, 0.75, -1.9635000228881836, 1], [-1.7999999523162842, 0.75, -1.9635000228881836, 1], [-1.7950000762939453, 0.75, -1.9635000228881836, 1], [-1.7899999618530273, 0.75, -1.9635000228881836, 1], [-1.784999966621399, 0.75, -1.9635000228881836, 1], [-1.7799999713897705, 0.75, -1.9635000228881836, 1], [-1.7750000953674316, 0.75, -1.9635000228881836, 1], [-1.7699999809265137, 0.75, -1.9635000228881836, 1], [-1.7649999856948853, 0.75, -1.9635000228881836, 1], [-1.7599999904632568, 0.75, -1.9635000228881836, 1], [-1.7549999952316284, 0.75, -1.9635000228881836, 1], [-1.75, 0.75, -1.9635000228881836, 1], [-1.7450000047683716, 0.75, -1.9635000228881836, 1], [-1.7400000095367432, 0.75, -1.9635000228881836, 1], [-1.7350000143051147, 0.75, -1.9635000228881836, 1], [-1.7300000190734863, 0.75, -1.9635000228881836, 1], [-1.7249999046325684, 0.75, -1.9635000228881836, 1], [-1.7200000286102295, 0.75, -1.9635000228881836, 1], [-1.715000033378601, 0.75, -1.9635000228881836, 1], [-1.7100000381469727, 0.75, -1.9635000228881836, 1], [-1.7049999237060547, 0.75, -1.9635000228881836, 1], [-1.7000000476837158, 0.75, -1.9635000228881836, 1], [-1.6949999332427979, 0.75, -1.9635000228881836, 1], [-1.690000057220459, 0.75, -1.9635000228881836, 1], [-1.684999942779541, 0.75, -1.9635000228881836, 1], [-1.6800000667572021, 0.75, -1.9635000228881836, 1], [-1.6749999523162842, 0.75, -1.9635000228881836, 1], [-1.6700000762939453, 0.75, -1.9635000228881836, 1], [-1.6649999618530273, 0.75, -1.9635000228881836, 1], [-1.659999966621399, 0.75, -1.9635000228881836, 1], [-1.6549999713897705, 0.75, -1.9635000228881836, 1], [-1.6500000953674316, 0.75, -1.9635000228881836, 1], [-1.6449999809265137, 0.75, -1.9635000228881836, 1], [-1.6399999856948853, 0.75, -1.9635000228881836, 1], [-1.6349999904632568, 0.75, -1.9635000228881836, 1], [-1.6299999952316284, 0.75, -1.9635000228881836, 1], [-1.625, 0.75, -1.9635000228881836, 1], [-1.6200000047683716, 0.75, -1.9635000228881836, 1], [-1.6150000095367432, 0.75, -1.9635000228881836, 1], [-1.6100000143051147, 0.75, -1.9635000228881836, 1], [-1.6050000190734863, 0.75, -1.9635000228881836, 1], [-1.5999999046325684, 0.75, -1.9635000228881836, 1], [-1.5950000286102295, 0.75, -1.9635000228881836, 1], [-1.590000033378601, 0.75, -1.9635000228881836, 1], [-1.5850000381469727, 0.75, -1.9635000228881836, 1], [-1.5799999237060547, 0.75, -1.9635000228881836, 1], [-1.5750000476837158, 0.75, -1.9635000228881836, 1], [-1.5699999332427979, 0.75, -1.9635000228881836, 1], [-1.565000057220459, 0.75, -1.9635000228881836, 1], [-1.559999942779541, 0.75, -1.9635000228881836, 1], [-1.5550000667572021, 0.75, -1.9635000228881836, 1], [-1.5499999523162842, 0.75, -1.9635000228881836, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_-2.35619_0.75.json b/probe_vis_j_-2.35619_0.75.json
new file mode 100644
index 0000000..dfb779a
--- /dev/null
+++ b/probe_vis_j_-2.35619_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, -2.3561899662017822, 1], [-2.259999990463257, 0.75, -2.3561899662017822, 1], [-2.25, 0.75, -2.3561899662017822, 1], [-2.240000009536743, 0.75, -2.3561899662017822, 1], [-2.2300000190734863, 0.75, -2.3561899662017822, 1], [-2.2249999046325684, 0.75, -2.3561899662017822, 1], [-2.2200000286102295, 0.75, -2.3561899662017822, 1], [-2.2149999141693115, 0.75, -2.3561899662017822, 1], [-2.2100000381469727, 0.75, -2.3561899662017822, 1], [-2.2049999237060547, 0.75, -2.3561899662017822, 1], [-2.200000047683716, 0.75, -2.3561899662017822, 1], [-2.194999933242798, 0.75, -2.3561899662017822, 1], [-2.190000057220459, 0.75, -2.3561899662017822, 1], [-2.184999942779541, 0.75, -2.3561899662017822, 1], [-2.180000066757202, 0.75, -2.3561899662017822, 1], [-2.174999952316284, 0.75, -2.3561899662017822, 1], [-2.1700000762939453, 0.75, -2.3561899662017822, 1], [-2.1649999618530273, 0.75, -2.3561899662017822, 1], [-2.1600000858306885, 0.75, -2.3561899662017822, 1], [-2.1549999713897705, 0.75, -2.3561899662017822, 1], [-2.1500000953674316, 0.75, -2.3561899662017822, 1], [-2.1449999809265137, 0.75, -2.3561899662017822, 1], [-2.134999990463257, 0.75, -2.3561899662017822, 1], [-2.125, 0.75, -2.3561899662017822, 1], [-2.115000009536743, 0.75, -2.3561899662017822, 1], [-2.1050000190734863, 0.75, -2.3561899662017822, 1], [-2.0999999046325684, 0.75, -2.3561899662017822, 1], [-2.0950000286102295, 0.75, -2.3561899662017822, 1], [-2.0899999141693115, 0.75, -2.3561899662017822, 1], [-2.0850000381469727, 0.75, -2.3561899662017822, 1], [-2.0799999237060547, 0.75, -2.3561899662017822, 1], [-2.075000047683716, 0.75, -2.3561899662017822, 1], [-2.069999933242798, 0.75, -2.3561899662017822, 1], [-2.065000057220459, 0.75, -2.3561899662017822, 1], [-2.059999942779541, 0.75, -2.3561899662017822, 1], [-2.055000066757202, 0.75, -2.3561899662017822, 1], [-2.049999952316284, 0.75, -2.3561899662017822, 1], [-2.0450000762939453, 0.75, -2.3561899662017822, 1], [-2.0399999618530273, 0.75, -2.3561899662017822, 1], [-2.0350000858306885, 0.75, -2.3561899662017822, 1], [-2.0299999713897705, 0.75, -2.3561899662017822, 1], [-2.0250000953674316, 0.75, -2.3561899662017822, 1], [-2.0199999809265137, 0.75, -2.3561899662017822, 1], [-2.009999990463257, 0.75, -2.3561899662017822, 1], [-2.0, 0.75, -2.3561899662017822, 1], [-1.9950000047683716, 0.75, -2.3561899662017822, 1], [-1.9900000095367432, 0.75, -2.3561899662017822, 1], [-1.9850000143051147, 0.75, -2.3561899662017822, 1], [-1.9800000190734863, 0.75, -2.3561899662017822, 1], [-1.9749999046325684, 0.75, -2.3561899662017822, 1], [-1.9700000286102295, 0.75, -2.3561899662017822, 1], [-1.965000033378601, 0.75, -2.3561899662017822, 1], [-1.9600000381469727, 0.75, -2.3561899662017822, 1], [-1.9549999237060547, 0.75, -2.3561899662017822, 1], [-1.9500000476837158, 0.75, -2.3561899662017822, 1], [-1.9449999332427979, 0.75, -2.3561899662017822, 1], [-1.940000057220459, 0.75, -2.3561899662017822, 1], [-1.934999942779541, 0.75, -2.3561899662017822, 1], [-1.9300000667572021, 0.75, -2.3561899662017822, 1], [-1.9249999523162842, 0.75, -2.3561899662017822, 1], [-1.9200000762939453, 0.75, -2.3561899662017822, 1], [-1.9149999618530273, 0.75, -2.3561899662017822, 1], [-1.909999966621399, 0.75, -2.3561899662017822, 1], [-1.9049999713897705, 0.75, -2.3561899662017822, 1], [-1.9000000953674316, 0.75, -2.3561899662017822, 1], [-1.8949999809265137, 0.75, -2.3561899662017822, 1], [-1.8899999856948853, 0.75, -2.3561899662017822, 1], [-1.8849999904632568, 0.75, -2.3561899662017822, 1], [-1.8799999952316284, 0.75, -2.3561899662017822, 1], [-1.875, 0.75, -2.3561899662017822, 1], [-1.8700000047683716, 0.75, -2.3561899662017822, 1], [-1.8650000095367432, 0.75, -2.3561899662017822, 1], [-1.8600000143051147, 0.75, -2.3561899662017822, 1], [-1.8550000190734863, 0.75, -2.3561899662017822, 1], [-1.8499999046325684, 0.75, -2.3561899662017822, 1], [-1.8450000286102295, 0.75, -2.3561899662017822, 1], [-1.840000033378601, 0.75, -2.3561899662017822, 1], [-1.8350000381469727, 0.75, -2.3561899662017822, 1], [-1.8299999237060547, 0.75, -2.3561899662017822, 1], [-1.8250000476837158, 0.75, -2.3561899662017822, 1], [-1.8199999332427979, 0.75, -2.3561899662017822, 1], [-1.815000057220459, 0.75, -2.3561899662017822, 1], [-1.809999942779541, 0.75, -2.3561899662017822, 1], [-1.8050000667572021, 0.75, -2.3561899662017822, 1], [-1.7999999523162842, 0.75, -2.3561899662017822, 1], [-1.7950000762939453, 0.75, -2.3561899662017822, 1], [-1.7899999618530273, 0.75, -2.3561899662017822, 1], [-1.784999966621399, 0.75, -2.3561899662017822, 1], [-1.7799999713897705, 0.75, -2.3561899662017822, 1], [-1.7750000953674316, 0.75, -2.3561899662017822, 1], [-1.7699999809265137, 0.75, -2.3561899662017822, 1], [-1.7649999856948853, 0.75, -2.3561899662017822, 1], [-1.7599999904632568, 0.75, -2.3561899662017822, 1], [-1.7549999952316284, 0.75, -2.3561899662017822, 1], [-1.75, 0.75, -2.3561899662017822, 1], [-1.7450000047683716, 0.75, -2.3561899662017822, 1], [-1.7400000095367432, 0.75, -2.3561899662017822, 1], [-1.7350000143051147, 0.75, -2.3561899662017822, 1], [-1.7300000190734863, 0.75, -2.3561899662017822, 1], [-1.7249999046325684, 0.75, -2.3561899662017822, 1], [-1.7200000286102295, 0.75, -2.3561899662017822, 1], [-1.715000033378601, 0.75, -2.3561899662017822, 1], [-1.7100000381469727, 0.75, -2.3561899662017822, 1], [-1.7049999237060547, 0.75, -2.3561899662017822, 1], [-1.7000000476837158, 0.75, -2.3561899662017822, 1], [-1.6949999332427979, 0.75, -2.3561899662017822, 1], [-1.690000057220459, 0.75, -2.3561899662017822, 1], [-1.684999942779541, 0.75, -2.3561899662017822, 1], [-1.6800000667572021, 0.75, -2.3561899662017822, 1], [-1.6749999523162842, 0.75, -2.3561899662017822, 1], [-1.6700000762939453, 0.75, -2.3561899662017822, 1], [-1.6649999618530273, 0.75, -2.3561899662017822, 1], [-1.659999966621399, 0.75, -2.3561899662017822, 1], [-1.6549999713897705, 0.75, -2.3561899662017822, 1], [-1.6500000953674316, 0.75, -2.3561899662017822, 1], [-1.6449999809265137, 0.75, -2.3561899662017822, 1], [-1.6399999856948853, 0.75, -2.3561899662017822, 1], [-1.6349999904632568, 0.75, -2.3561899662017822, 1], [-1.6299999952316284, 0.75, -2.3561899662017822, 1], [-1.625, 0.75, -2.3561899662017822, 1], [-1.6200000047683716, 0.75, -2.3561899662017822, 1], [-1.6150000095367432, 0.75, -2.3561899662017822, 1], [-1.6100000143051147, 0.75, -2.3561899662017822, 1], [-1.6050000190734863, 0.75, -2.3561899662017822, 1], [-1.5999999046325684, 0.75, -2.3561899662017822, 1], [-1.5950000286102295, 0.75, -2.3561899662017822, 1], [-1.590000033378601, 0.75, -2.3561899662017822, 1], [-1.5850000381469727, 0.75, -2.3561899662017822, 1], [-1.5799999237060547, 0.75, -2.3561899662017822, 1], [-1.5750000476837158, 0.75, -2.3561899662017822, 1], [-1.5699999332427979, 0.75, -2.3561899662017822, 1], [-1.565000057220459, 0.75, -2.3561899662017822, 1], [-1.559999942779541, 0.75, -2.3561899662017822, 1], [-1.5550000667572021, 0.75, -2.3561899662017822, 1], [-1.5499999523162842, 0.75, -2.3561899662017822, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_-2.74889_0.75.json b/probe_vis_j_-2.74889_0.75.json
new file mode 100644
index 0000000..042d39b
--- /dev/null
+++ b/probe_vis_j_-2.74889_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, -2.748889923095703, 1], [-2.259999990463257, 0.75, -2.748889923095703, 1], [-2.25, 0.75, -2.748889923095703, 1], [-2.240000009536743, 0.75, -2.748889923095703, 1], [-2.2300000190734863, 0.75, -2.748889923095703, 1], [-2.2249999046325684, 0.75, -2.748889923095703, 1], [-2.2200000286102295, 0.75, -2.748889923095703, 1], [-2.2149999141693115, 0.75, -2.748889923095703, 1], [-2.2100000381469727, 0.75, -2.748889923095703, 1], [-2.2049999237060547, 0.75, -2.748889923095703, 1], [-2.200000047683716, 0.75, -2.748889923095703, 1], [-2.194999933242798, 0.75, -2.748889923095703, 1], [-2.190000057220459, 0.75, -2.748889923095703, 1], [-2.184999942779541, 0.75, -2.748889923095703, 1], [-2.180000066757202, 0.75, -2.748889923095703, 1], [-2.174999952316284, 0.75, -2.748889923095703, 1], [-2.1700000762939453, 0.75, -2.748889923095703, 1], [-2.1649999618530273, 0.75, -2.748889923095703, 1], [-2.1600000858306885, 0.75, -2.748889923095703, 1], [-2.1549999713897705, 0.75, -2.748889923095703, 1], [-2.1500000953674316, 0.75, -2.748889923095703, 1], [-2.1449999809265137, 0.75, -2.748889923095703, 1], [-2.134999990463257, 0.75, -2.748889923095703, 1], [-2.125, 0.75, -2.748889923095703, 1], [-2.115000009536743, 0.75, -2.748889923095703, 1], [-2.1050000190734863, 0.75, -2.748889923095703, 1], [-2.0999999046325684, 0.75, -2.748889923095703, 1], [-2.0950000286102295, 0.75, -2.748889923095703, 1], [-2.0899999141693115, 0.75, -2.748889923095703, 1], [-2.0850000381469727, 0.75, -2.748889923095703, 1], [-2.0799999237060547, 0.75, -2.748889923095703, 1], [-2.075000047683716, 0.75, -2.748889923095703, 1], [-2.069999933242798, 0.75, -2.748889923095703, 1], [-2.065000057220459, 0.75, -2.748889923095703, 1], [-2.059999942779541, 0.75, -2.748889923095703, 1], [-2.055000066757202, 0.75, -2.748889923095703, 1], [-2.049999952316284, 0.75, -2.748889923095703, 1], [-2.0450000762939453, 0.75, -2.748889923095703, 1], [-2.0399999618530273, 0.75, -2.748889923095703, 1], [-2.0350000858306885, 0.75, -2.748889923095703, 1], [-2.0299999713897705, 0.75, -2.748889923095703, 1], [-2.0250000953674316, 0.75, -2.748889923095703, 1], [-2.0199999809265137, 0.75, -2.748889923095703, 1], [-2.009999990463257, 0.75, -2.748889923095703, 1], [-2.0, 0.75, -2.748889923095703, 1], [-1.9950000047683716, 0.75, -2.748889923095703, 1], [-1.9900000095367432, 0.75, -2.748889923095703, 1], [-1.9850000143051147, 0.75, -2.748889923095703, 1], [-1.9800000190734863, 0.75, -2.748889923095703, 1], [-1.9749999046325684, 0.75, -2.748889923095703, 1], [-1.9700000286102295, 0.75, -2.748889923095703, 1], [-1.965000033378601, 0.75, -2.748889923095703, 1], [-1.9600000381469727, 0.75, -2.748889923095703, 1], [-1.9549999237060547, 0.75, -2.748889923095703, 1], [-1.9500000476837158, 0.75, -2.748889923095703, 1], [-1.9449999332427979, 0.75, -2.748889923095703, 1], [-1.940000057220459, 0.75, -2.748889923095703, 1], [-1.934999942779541, 0.75, -2.748889923095703, 1], [-1.9300000667572021, 0.75, -2.748889923095703, 1], [-1.9249999523162842, 0.75, -2.748889923095703, 1], [-1.9200000762939453, 0.75, -2.748889923095703, 1], [-1.9149999618530273, 0.75, -2.748889923095703, 1], [-1.909999966621399, 0.75, -2.748889923095703, 1], [-1.9049999713897705, 0.75, -2.748889923095703, 1], [-1.9000000953674316, 0.75, -2.748889923095703, 1], [-1.8949999809265137, 0.75, -2.748889923095703, 1], [-1.8899999856948853, 0.75, -2.748889923095703, 1], [-1.8849999904632568, 0.75, -2.748889923095703, 1], [-1.8799999952316284, 0.75, -2.748889923095703, 1], [-1.875, 0.75, -2.748889923095703, 1], [-1.8700000047683716, 0.75, -2.748889923095703, 1], [-1.8650000095367432, 0.75, -2.748889923095703, 1], [-1.8600000143051147, 0.75, -2.748889923095703, 1], [-1.8550000190734863, 0.75, -2.748889923095703, 1], [-1.8499999046325684, 0.75, -2.748889923095703, 1], [-1.8450000286102295, 0.75, -2.748889923095703, 1], [-1.840000033378601, 0.75, -2.748889923095703, 1], [-1.8350000381469727, 0.75, -2.748889923095703, 1], [-1.8299999237060547, 0.75, -2.748889923095703, 1], [-1.8250000476837158, 0.75, -2.748889923095703, 1], [-1.8199999332427979, 0.75, -2.748889923095703, 1], [-1.815000057220459, 0.75, -2.748889923095703, 1], [-1.809999942779541, 0.75, -2.748889923095703, 1], [-1.8050000667572021, 0.75, -2.748889923095703, 1], [-1.7999999523162842, 0.75, -2.748889923095703, 1], [-1.7950000762939453, 0.75, -2.748889923095703, 1], [-1.7899999618530273, 0.75, -2.748889923095703, 1], [-1.784999966621399, 0.75, -2.748889923095703, 1], [-1.7799999713897705, 0.75, -2.748889923095703, 1], [-1.7750000953674316, 0.75, -2.748889923095703, 1], [-1.7699999809265137, 0.75, -2.748889923095703, 1], [-1.7649999856948853, 0.75, -2.748889923095703, 1], [-1.7599999904632568, 0.75, -2.748889923095703, 1], [-1.7549999952316284, 0.75, -2.748889923095703, 1], [-1.75, 0.75, -2.748889923095703, 1], [-1.7450000047683716, 0.75, -2.748889923095703, 1], [-1.7400000095367432, 0.75, -2.748889923095703, 1], [-1.7350000143051147, 0.75, -2.748889923095703, 1], [-1.7300000190734863, 0.75, -2.748889923095703, 1], [-1.7249999046325684, 0.75, -2.748889923095703, 1], [-1.7200000286102295, 0.75, -2.748889923095703, 1], [-1.715000033378601, 0.75, -2.748889923095703, 1], [-1.7100000381469727, 0.75, -2.748889923095703, 1], [-1.7049999237060547, 0.75, -2.748889923095703, 1], [-1.7000000476837158, 0.75, -2.748889923095703, 1], [-1.6949999332427979, 0.75, -2.748889923095703, 1], [-1.690000057220459, 0.75, -2.748889923095703, 1], [-1.684999942779541, 0.75, -2.748889923095703, 1], [-1.6800000667572021, 0.75, -2.748889923095703, 1], [-1.6749999523162842, 0.75, -2.748889923095703, 1], [-1.6700000762939453, 0.75, -2.748889923095703, 1], [-1.6649999618530273, 0.75, -2.748889923095703, 1], [-1.659999966621399, 0.75, -2.748889923095703, 1], [-1.6549999713897705, 0.75, -2.748889923095703, 1], [-1.6500000953674316, 0.75, -2.748889923095703, 1], [-1.6449999809265137, 0.75, -2.748889923095703, 1], [-1.6399999856948853, 0.75, -2.748889923095703, 1], [-1.6349999904632568, 0.75, -2.748889923095703, 1], [-1.6299999952316284, 0.75, -2.748889923095703, 1], [-1.625, 0.75, -2.748889923095703, 1], [-1.6200000047683716, 0.75, -2.748889923095703, 1], [-1.6150000095367432, 0.75, -2.748889923095703, 1], [-1.6100000143051147, 0.75, -2.748889923095703, 1], [-1.6050000190734863, 0.75, -2.748889923095703, 1], [-1.5999999046325684, 0.75, -2.748889923095703, 1], [-1.5950000286102295, 0.75, -2.748889923095703, 1], [-1.590000033378601, 0.75, -2.748889923095703, 1], [-1.5850000381469727, 0.75, -2.748889923095703, 1], [-1.5799999237060547, 0.75, -2.748889923095703, 1], [-1.5750000476837158, 0.75, -2.748889923095703, 1], [-1.5699999332427979, 0.75, -2.748889923095703, 1], [-1.565000057220459, 0.75, -2.748889923095703, 1], [-1.559999942779541, 0.75, -2.748889923095703, 1], [-1.5550000667572021, 0.75, -2.748889923095703, 1], [-1.5499999523162842, 0.75, -2.748889923095703, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_-3.14159_0.75.json b/probe_vis_j_-3.14159_0.75.json
new file mode 100644
index 0000000..56295f9
--- /dev/null
+++ b/probe_vis_j_-3.14159_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, -3.141590118408203, 1], [-2.259999990463257, 0.75, -3.141590118408203, 1], [-2.25, 0.75, -3.141590118408203, 1], [-2.240000009536743, 0.75, -3.141590118408203, 1], [-2.2300000190734863, 0.75, -3.141590118408203, 1], [-2.2249999046325684, 0.75, -3.141590118408203, 1], [-2.2200000286102295, 0.75, -3.141590118408203, 1], [-2.2149999141693115, 0.75, -3.141590118408203, 1], [-2.2100000381469727, 0.75, -3.141590118408203, 1], [-2.2049999237060547, 0.75, -3.141590118408203, 1], [-2.200000047683716, 0.75, -3.141590118408203, 1], [-2.194999933242798, 0.75, -3.141590118408203, 1], [-2.190000057220459, 0.75, -3.141590118408203, 1], [-2.184999942779541, 0.75, -3.141590118408203, 1], [-2.180000066757202, 0.75, -3.141590118408203, 1], [-2.174999952316284, 0.75, -3.141590118408203, 1], [-2.1700000762939453, 0.75, -3.141590118408203, 1], [-2.1649999618530273, 0.75, -3.141590118408203, 1], [-2.1600000858306885, 0.75, -3.141590118408203, 1], [-2.1549999713897705, 0.75, -3.141590118408203, 1], [-2.1500000953674316, 0.75, -3.141590118408203, 1], [-2.1449999809265137, 0.75, -3.141590118408203, 1], [-2.134999990463257, 0.75, -3.141590118408203, 1], [-2.125, 0.75, -3.141590118408203, 1], [-2.115000009536743, 0.75, -3.141590118408203, 1], [-2.1050000190734863, 0.75, -3.141590118408203, 1], [-2.0999999046325684, 0.75, -3.141590118408203, 1], [-2.0950000286102295, 0.75, -3.141590118408203, 1], [-2.0899999141693115, 0.75, -3.141590118408203, 1], [-2.0850000381469727, 0.75, -3.141590118408203, 1], [-2.0799999237060547, 0.75, -3.141590118408203, 1], [-2.075000047683716, 0.75, -3.141590118408203, 1], [-2.069999933242798, 0.75, -3.141590118408203, 1], [-2.065000057220459, 0.75, -3.141590118408203, 1], [-2.059999942779541, 0.75, -3.141590118408203, 1], [-2.055000066757202, 0.75, -3.141590118408203, 1], [-2.049999952316284, 0.75, -3.141590118408203, 1], [-2.0450000762939453, 0.75, -3.141590118408203, 1], [-2.0399999618530273, 0.75, -3.141590118408203, 1], [-2.0350000858306885, 0.75, -3.141590118408203, 1], [-2.0299999713897705, 0.75, -3.141590118408203, 1], [-2.0250000953674316, 0.75, -3.141590118408203, 1], [-2.0199999809265137, 0.75, -3.141590118408203, 1], [-2.009999990463257, 0.75, -3.141590118408203, 1], [-2.0, 0.75, -3.141590118408203, 1], [-1.9950000047683716, 0.75, -3.141590118408203, 1], [-1.9900000095367432, 0.75, -3.141590118408203, 0], [-1.9850000143051147, 0.75, -3.141590118408203, 0], [-1.9800000190734863, 0.75, -3.141590118408203, 1], [-1.9749999046325684, 0.75, -3.141590118408203, 1], [-1.9700000286102295, 0.75, -3.141590118408203, 1], [-1.965000033378601, 0.75, -3.141590118408203, 1], [-1.9600000381469727, 0.75, -3.141590118408203, 1], [-1.9549999237060547, 0.75, -3.141590118408203, 1], [-1.9500000476837158, 0.75, -3.141590118408203, 1], [-1.9449999332427979, 0.75, -3.141590118408203, 1], [-1.940000057220459, 0.75, -3.141590118408203, 1], [-1.934999942779541, 0.75, -3.141590118408203, 1], [-1.9300000667572021, 0.75, -3.141590118408203, 1], [-1.9249999523162842, 0.75, -3.141590118408203, 1], [-1.9200000762939453, 0.75, -3.141590118408203, 1], [-1.9149999618530273, 0.75, -3.141590118408203, 1], [-1.909999966621399, 0.75, -3.141590118408203, 1], [-1.9049999713897705, 0.75, -3.141590118408203, 1], [-1.9000000953674316, 0.75, -3.141590118408203, 1], [-1.8949999809265137, 0.75, -3.141590118408203, 1], [-1.8899999856948853, 0.75, -3.141590118408203, 1], [-1.8849999904632568, 0.75, -3.141590118408203, 1], [-1.8799999952316284, 0.75, -3.141590118408203, 1], [-1.875, 0.75, -3.141590118408203, 1], [-1.8700000047683716, 0.75, -3.141590118408203, 1], [-1.8650000095367432, 0.75, -3.141590118408203, 1], [-1.8600000143051147, 0.75, -3.141590118408203, 1], [-1.8550000190734863, 0.75, -3.141590118408203, 1], [-1.8499999046325684, 0.75, -3.141590118408203, 1], [-1.8450000286102295, 0.75, -3.141590118408203, 1], [-1.840000033378601, 0.75, -3.141590118408203, 1], [-1.8350000381469727, 0.75, -3.141590118408203, 1], [-1.8299999237060547, 0.75, -3.141590118408203, 1], [-1.8250000476837158, 0.75, -3.141590118408203, 1], [-1.8199999332427979, 0.75, -3.141590118408203, 1], [-1.815000057220459, 0.75, -3.141590118408203, 1], [-1.809999942779541, 0.75, -3.141590118408203, 1], [-1.8050000667572021, 0.75, -3.141590118408203, 1], [-1.7999999523162842, 0.75, -3.141590118408203, 1], [-1.7950000762939453, 0.75, -3.141590118408203, 1], [-1.7899999618530273, 0.75, -3.141590118408203, 1], [-1.784999966621399, 0.75, -3.141590118408203, 1], [-1.7799999713897705, 0.75, -3.141590118408203, 1], [-1.7750000953674316, 0.75, -3.141590118408203, 1], [-1.7699999809265137, 0.75, -3.141590118408203, 1], [-1.7649999856948853, 0.75, -3.141590118408203, 1], [-1.7599999904632568, 0.75, -3.141590118408203, 1], [-1.7549999952316284, 0.75, -3.141590118408203, 1], [-1.75, 0.75, -3.141590118408203, 1], [-1.7450000047683716, 0.75, -3.141590118408203, 1], [-1.7400000095367432, 0.75, -3.141590118408203, 1], [-1.7350000143051147, 0.75, -3.141590118408203, 1], [-1.7300000190734863, 0.75, -3.141590118408203, 1], [-1.7249999046325684, 0.75, -3.141590118408203, 1], [-1.7200000286102295, 0.75, -3.141590118408203, 1], [-1.715000033378601, 0.75, -3.141590118408203, 1], [-1.7100000381469727, 0.75, -3.141590118408203, 1], [-1.7049999237060547, 0.75, -3.141590118408203, 1], [-1.7000000476837158, 0.75, -3.141590118408203, 1], [-1.6949999332427979, 0.75, -3.141590118408203, 1], [-1.690000057220459, 0.75, -3.141590118408203, 1], [-1.684999942779541, 0.75, -3.141590118408203, 1], [-1.6800000667572021, 0.75, -3.141590118408203, 1], [-1.6749999523162842, 0.75, -3.141590118408203, 1], [-1.6700000762939453, 0.75, -3.141590118408203, 1], [-1.6649999618530273, 0.75, -3.141590118408203, 1], [-1.659999966621399, 0.75, -3.141590118408203, 1], [-1.6549999713897705, 0.75, -3.141590118408203, 1], [-1.6500000953674316, 0.75, -3.141590118408203, 1], [-1.6449999809265137, 0.75, -3.141590118408203, 1], [-1.6399999856948853, 0.75, -3.141590118408203, 1], [-1.6349999904632568, 0.75, -3.141590118408203, 1], [-1.6299999952316284, 0.75, -3.141590118408203, 1], [-1.625, 0.75, -3.141590118408203, 1], [-1.6200000047683716, 0.75, -3.141590118408203, 1], [-1.6150000095367432, 0.75, -3.141590118408203, 1], [-1.6100000143051147, 0.75, -3.141590118408203, 1], [-1.6050000190734863, 0.75, -3.141590118408203, 1], [-1.5999999046325684, 0.75, -3.141590118408203, 1], [-1.5950000286102295, 0.75, -3.141590118408203, 1], [-1.590000033378601, 0.75, -3.141590118408203, 1], [-1.5850000381469727, 0.75, -3.141590118408203, 1], [-1.5799999237060547, 0.75, -3.141590118408203, 1], [-1.5750000476837158, 0.75, -3.141590118408203, 1], [-1.5699999332427979, 0.75, -3.141590118408203, 1], [-1.565000057220459, 0.75, -3.141590118408203, 1], [-1.559999942779541, 0.75, -3.141590118408203, 1], [-1.5550000667572021, 0.75, -3.141590118408203, 1], [-1.5499999523162842, 0.75, -3.141590118408203, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_0.0_0.75.json b/probe_vis_j_0.0_0.75.json
new file mode 100644
index 0000000..f085849
--- /dev/null
+++ b/probe_vis_j_0.0_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, 0.0, 1], [-2.259999990463257, 0.75, 0.0, 1], [-2.25, 0.75, 0.0, 1], [-2.240000009536743, 0.75, 0.0, 1], [-2.2300000190734863, 0.75, 0.0, 1], [-2.2249999046325684, 0.75, 0.0, 1], [-2.2200000286102295, 0.75, 0.0, 1], [-2.2149999141693115, 0.75, 0.0, 1], [-2.2100000381469727, 0.75, 0.0, 1], [-2.2049999237060547, 0.75, 0.0, 1], [-2.200000047683716, 0.75, 0.0, 1], [-2.194999933242798, 0.75, 0.0, 1], [-2.190000057220459, 0.75, 0.0, 1], [-2.184999942779541, 0.75, 0.0, 1], [-2.180000066757202, 0.75, 0.0, 1], [-2.174999952316284, 0.75, 0.0, 1], [-2.1700000762939453, 0.75, 0.0, 1], [-2.1649999618530273, 0.75, 0.0, 1], [-2.1600000858306885, 0.75, 0.0, 1], [-2.1549999713897705, 0.75, 0.0, 1], [-2.1500000953674316, 0.75, 0.0, 1], [-2.1449999809265137, 0.75, 0.0, 1], [-2.134999990463257, 0.75, 0.0, 1], [-2.125, 0.75, 0.0, 1], [-2.115000009536743, 0.75, 0.0, 1], [-2.1050000190734863, 0.75, 0.0, 1], [-2.0999999046325684, 0.75, 0.0, 1], [-2.0950000286102295, 0.75, 0.0, 1], [-2.0899999141693115, 0.75, 0.0, 1], [-2.0850000381469727, 0.75, 0.0, 1], [-2.0799999237060547, 0.75, 0.0, 1], [-2.075000047683716, 0.75, 0.0, 1], [-2.069999933242798, 0.75, 0.0, 1], [-2.065000057220459, 0.75, 0.0, 1], [-2.059999942779541, 0.75, 0.0, 1], [-2.055000066757202, 0.75, 0.0, 1], [-2.049999952316284, 0.75, 0.0, 1], [-2.0450000762939453, 0.75, 0.0, 1], [-2.0399999618530273, 0.75, 0.0, 1], [-2.0350000858306885, 0.75, 0.0, 1], [-2.0299999713897705, 0.75, 0.0, 1], [-2.0250000953674316, 0.75, 0.0, 1], [-2.0199999809265137, 0.75, 0.0, 1], [-2.009999990463257, 0.75, 0.0, 0], [-2.0, 0.75, 0.0, 0], [-1.9950000047683716, 0.75, 0.0, 0], [-1.9900000095367432, 0.75, 0.0, 0], [-1.9850000143051147, 0.75, 0.0, 0], [-1.9800000190734863, 0.75, 0.0, 0], [-1.9749999046325684, 0.75, 0.0, 0], [-1.9700000286102295, 0.75, 0.0, 0], [-1.965000033378601, 0.75, 0.0, 0], [-1.9600000381469727, 0.75, 0.0, 0], [-1.9549999237060547, 0.75, 0.0, 0], [-1.9500000476837158, 0.75, 0.0, 0], [-1.9449999332427979, 0.75, 0.0, 0], [-1.940000057220459, 0.75, 0.0, 0], [-1.934999942779541, 0.75, 0.0, 0], [-1.9300000667572021, 0.75, 0.0, 0], [-1.9249999523162842, 0.75, 0.0, 0], [-1.9200000762939453, 0.75, 0.0, 0], [-1.9149999618530273, 0.75, 0.0, 0], [-1.909999966621399, 0.75, 0.0, 0], [-1.9049999713897705, 0.75, 0.0, 0], [-1.9000000953674316, 0.75, 0.0, 0], [-1.8949999809265137, 0.75, 0.0, 0], [-1.8899999856948853, 0.75, 0.0, 0], [-1.8849999904632568, 0.75, 0.0, 0], [-1.8799999952316284, 0.75, 0.0, 0], [-1.875, 0.75, 0.0, 0], [-1.8700000047683716, 0.75, 0.0, 0], [-1.8650000095367432, 0.75, 0.0, 0], [-1.8600000143051147, 0.75, 0.0, 0], [-1.8550000190734863, 0.75, 0.0, 0], [-1.8499999046325684, 0.75, 0.0, 0], [-1.8450000286102295, 0.75, 0.0, 0], [-1.840000033378601, 0.75, 0.0, 0], [-1.8350000381469727, 0.75, 0.0, 0], [-1.8299999237060547, 0.75, 0.0, 0], [-1.8250000476837158, 0.75, 0.0, 0], [-1.8199999332427979, 0.75, 0.0, 0], [-1.815000057220459, 0.75, 0.0, 0], [-1.809999942779541, 0.75, 0.0, 0], [-1.8050000667572021, 0.75, 0.0, 1], [-1.7999999523162842, 0.75, 0.0, 1], [-1.7950000762939453, 0.75, 0.0, 1], [-1.7899999618530273, 0.75, 0.0, 1], [-1.784999966621399, 0.75, 0.0, 1], [-1.7799999713897705, 0.75, 0.0, 1], [-1.7750000953674316, 0.75, 0.0, 1], [-1.7699999809265137, 0.75, 0.0, 1], [-1.7649999856948853, 0.75, 0.0, 1], [-1.7599999904632568, 0.75, 0.0, 1], [-1.7549999952316284, 0.75, 0.0, 1], [-1.75, 0.75, 0.0, 1], [-1.7450000047683716, 0.75, 0.0, 1], [-1.7400000095367432, 0.75, 0.0, 1], [-1.7350000143051147, 0.75, 0.0, 1], [-1.7300000190734863, 0.75, 0.0, 1], [-1.7249999046325684, 0.75, 0.0, 1], [-1.7200000286102295, 0.75, 0.0, 1], [-1.715000033378601, 0.75, 0.0, 1], [-1.7100000381469727, 0.75, 0.0, 1], [-1.7049999237060547, 0.75, 0.0, 1], [-1.7000000476837158, 0.75, 0.0, 1], [-1.6949999332427979, 0.75, 0.0, 1], [-1.690000057220459, 0.75, 0.0, 1], [-1.684999942779541, 0.75, 0.0, 1], [-1.6800000667572021, 0.75, 0.0, 1], [-1.6749999523162842, 0.75, 0.0, 1], [-1.6700000762939453, 0.75, 0.0, 1], [-1.6649999618530273, 0.75, 0.0, 1], [-1.659999966621399, 0.75, 0.0, 1], [-1.6549999713897705, 0.75, 0.0, 1], [-1.6500000953674316, 0.75, 0.0, 1], [-1.6449999809265137, 0.75, 0.0, 1], [-1.6399999856948853, 0.75, 0.0, 1], [-1.6349999904632568, 0.75, 0.0, 1], [-1.6299999952316284, 0.75, 0.0, 1], [-1.625, 0.75, 0.0, 1], [-1.6200000047683716, 0.75, 0.0, 1], [-1.6150000095367432, 0.75, 0.0, 1], [-1.6100000143051147, 0.75, 0.0, 1], [-1.6050000190734863, 0.75, 0.0, 1], [-1.5999999046325684, 0.75, 0.0, 1], [-1.5950000286102295, 0.75, 0.0, 1], [-1.590000033378601, 0.75, 0.0, 1], [-1.5850000381469727, 0.75, 0.0, 1], [-1.5799999237060547, 0.75, 0.0, 1], [-1.5750000476837158, 0.75, 0.0, 1], [-1.5699999332427979, 0.75, 0.0, 1], [-1.565000057220459, 0.75, 0.0, 1], [-1.559999942779541, 0.75, 0.0, 1], [-1.5550000667572021, 0.75, 0.0, 1], [-1.5499999523162842, 0.75, 0.0, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_0.3927_0.75.json b/probe_vis_j_0.3927_0.75.json
new file mode 100644
index 0000000..aa3ad6b
--- /dev/null
+++ b/probe_vis_j_0.3927_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, 0.3926999866962433, 1], [-2.259999990463257, 0.75, 0.3926999866962433, 1], [-2.25, 0.75, 0.3926999866962433, 1], [-2.240000009536743, 0.75, 0.3926999866962433, 1], [-2.2300000190734863, 0.75, 0.3926999866962433, 1], [-2.2249999046325684, 0.75, 0.3926999866962433, 1], [-2.2200000286102295, 0.75, 0.3926999866962433, 1], [-2.2149999141693115, 0.75, 0.3926999866962433, 1], [-2.2100000381469727, 0.75, 0.3926999866962433, 1], [-2.2049999237060547, 0.75, 0.3926999866962433, 1], [-2.200000047683716, 0.75, 0.3926999866962433, 1], [-2.194999933242798, 0.75, 0.3926999866962433, 1], [-2.190000057220459, 0.75, 0.3926999866962433, 1], [-2.184999942779541, 0.75, 0.3926999866962433, 1], [-2.180000066757202, 0.75, 0.3926999866962433, 1], [-2.174999952316284, 0.75, 0.3926999866962433, 1], [-2.1700000762939453, 0.75, 0.3926999866962433, 1], [-2.1649999618530273, 0.75, 0.3926999866962433, 1], [-2.1600000858306885, 0.75, 0.3926999866962433, 1], [-2.1549999713897705, 0.75, 0.3926999866962433, 1], [-2.1500000953674316, 0.75, 0.3926999866962433, 1], [-2.1449999809265137, 0.75, 0.3926999866962433, 1], [-2.134999990463257, 0.75, 0.3926999866962433, 1], [-2.125, 0.75, 0.3926999866962433, 1], [-2.115000009536743, 0.75, 0.3926999866962433, 1], [-2.1050000190734863, 0.75, 0.3926999866962433, 1], [-2.0999999046325684, 0.75, 0.3926999866962433, 1], [-2.0950000286102295, 0.75, 0.3926999866962433, 1], [-2.0899999141693115, 0.75, 0.3926999866962433, 1], [-2.0850000381469727, 0.75, 0.3926999866962433, 1], [-2.0799999237060547, 0.75, 0.3926999866962433, 1], [-2.075000047683716, 0.75, 0.3926999866962433, 1], [-2.069999933242798, 0.75, 0.3926999866962433, 1], [-2.065000057220459, 0.75, 0.3926999866962433, 1], [-2.059999942779541, 0.75, 0.3926999866962433, 1], [-2.055000066757202, 0.75, 0.3926999866962433, 1], [-2.049999952316284, 0.75, 0.3926999866962433, 1], [-2.0450000762939453, 0.75, 0.3926999866962433, 1], [-2.0399999618530273, 0.75, 0.3926999866962433, 1], [-2.0350000858306885, 0.75, 0.3926999866962433, 1], [-2.0299999713897705, 0.75, 0.3926999866962433, 1], [-2.0250000953674316, 0.75, 0.3926999866962433, 1], [-2.0199999809265137, 0.75, 0.3926999866962433, 1], [-2.009999990463257, 0.75, 0.3926999866962433, 1], [-2.0, 0.75, 0.3926999866962433, 0], [-1.9950000047683716, 0.75, 0.3926999866962433, 0], [-1.9900000095367432, 0.75, 0.3926999866962433, 0], [-1.9850000143051147, 0.75, 0.3926999866962433, 0], [-1.9800000190734863, 0.75, 0.3926999866962433, 0], [-1.9749999046325684, 0.75, 0.3926999866962433, 0], [-1.9700000286102295, 0.75, 0.3926999866962433, 0], [-1.965000033378601, 0.75, 0.3926999866962433, 0], [-1.9600000381469727, 0.75, 0.3926999866962433, 0], [-1.9549999237060547, 0.75, 0.3926999866962433, 0], [-1.9500000476837158, 0.75, 0.3926999866962433, 0], [-1.9449999332427979, 0.75, 0.3926999866962433, 0], [-1.940000057220459, 0.75, 0.3926999866962433, 0], [-1.934999942779541, 0.75, 0.3926999866962433, 0], [-1.9300000667572021, 0.75, 0.3926999866962433, 0], [-1.9249999523162842, 0.75, 0.3926999866962433, 0], [-1.9200000762939453, 0.75, 0.3926999866962433, 0], [-1.9149999618530273, 0.75, 0.3926999866962433, 0], [-1.909999966621399, 0.75, 0.3926999866962433, 0], [-1.9049999713897705, 0.75, 0.3926999866962433, 0], [-1.9000000953674316, 0.75, 0.3926999866962433, 0], [-1.8949999809265137, 0.75, 0.3926999866962433, 0], [-1.8899999856948853, 0.75, 0.3926999866962433, 0], [-1.8849999904632568, 0.75, 0.3926999866962433, 0], [-1.8799999952316284, 0.75, 0.3926999866962433, 0], [-1.875, 0.75, 0.3926999866962433, 0], [-1.8700000047683716, 0.75, 0.3926999866962433, 0], [-1.8650000095367432, 0.75, 0.3926999866962433, 0], [-1.8600000143051147, 0.75, 0.3926999866962433, 0], [-1.8550000190734863, 0.75, 0.3926999866962433, 0], [-1.8499999046325684, 0.75, 0.3926999866962433, 0], [-1.8450000286102295, 0.75, 0.3926999866962433, 0], [-1.840000033378601, 0.75, 0.3926999866962433, 0], [-1.8350000381469727, 0.75, 0.3926999866962433, 0], [-1.8299999237060547, 0.75, 0.3926999866962433, 0], [-1.8250000476837158, 0.75, 0.3926999866962433, 0], [-1.8199999332427979, 0.75, 0.3926999866962433, 1], [-1.815000057220459, 0.75, 0.3926999866962433, 1], [-1.809999942779541, 0.75, 0.3926999866962433, 1], [-1.8050000667572021, 0.75, 0.3926999866962433, 1], [-1.7999999523162842, 0.75, 0.3926999866962433, 1], [-1.7950000762939453, 0.75, 0.3926999866962433, 1], [-1.7899999618530273, 0.75, 0.3926999866962433, 1], [-1.784999966621399, 0.75, 0.3926999866962433, 1], [-1.7799999713897705, 0.75, 0.3926999866962433, 1], [-1.7750000953674316, 0.75, 0.3926999866962433, 1], [-1.7699999809265137, 0.75, 0.3926999866962433, 1], [-1.7649999856948853, 0.75, 0.3926999866962433, 1], [-1.7599999904632568, 0.75, 0.3926999866962433, 1], [-1.7549999952316284, 0.75, 0.3926999866962433, 1], [-1.75, 0.75, 0.3926999866962433, 1], [-1.7450000047683716, 0.75, 0.3926999866962433, 1], [-1.7400000095367432, 0.75, 0.3926999866962433, 1], [-1.7350000143051147, 0.75, 0.3926999866962433, 1], [-1.7300000190734863, 0.75, 0.3926999866962433, 1], [-1.7249999046325684, 0.75, 0.3926999866962433, 1], [-1.7200000286102295, 0.75, 0.3926999866962433, 1], [-1.715000033378601, 0.75, 0.3926999866962433, 1], [-1.7100000381469727, 0.75, 0.3926999866962433, 1], [-1.7049999237060547, 0.75, 0.3926999866962433, 1], [-1.7000000476837158, 0.75, 0.3926999866962433, 1], [-1.6949999332427979, 0.75, 0.3926999866962433, 1], [-1.690000057220459, 0.75, 0.3926999866962433, 1], [-1.684999942779541, 0.75, 0.3926999866962433, 1], [-1.6800000667572021, 0.75, 0.3926999866962433, 1], [-1.6749999523162842, 0.75, 0.3926999866962433, 1], [-1.6700000762939453, 0.75, 0.3926999866962433, 1], [-1.6649999618530273, 0.75, 0.3926999866962433, 1], [-1.659999966621399, 0.75, 0.3926999866962433, 1], [-1.6549999713897705, 0.75, 0.3926999866962433, 1], [-1.6500000953674316, 0.75, 0.3926999866962433, 1], [-1.6449999809265137, 0.75, 0.3926999866962433, 1], [-1.6399999856948853, 0.75, 0.3926999866962433, 1], [-1.6349999904632568, 0.75, 0.3926999866962433, 1], [-1.6299999952316284, 0.75, 0.3926999866962433, 1], [-1.625, 0.75, 0.3926999866962433, 1], [-1.6200000047683716, 0.75, 0.3926999866962433, 1], [-1.6150000095367432, 0.75, 0.3926999866962433, 1], [-1.6100000143051147, 0.75, 0.3926999866962433, 1], [-1.6050000190734863, 0.75, 0.3926999866962433, 1], [-1.5999999046325684, 0.75, 0.3926999866962433, 1], [-1.5950000286102295, 0.75, 0.3926999866962433, 1], [-1.590000033378601, 0.75, 0.3926999866962433, 1], [-1.5850000381469727, 0.75, 0.3926999866962433, 1], [-1.5799999237060547, 0.75, 0.3926999866962433, 1], [-1.5750000476837158, 0.75, 0.3926999866962433, 1], [-1.5699999332427979, 0.75, 0.3926999866962433, 1], [-1.565000057220459, 0.75, 0.3926999866962433, 1], [-1.559999942779541, 0.75, 0.3926999866962433, 1], [-1.5550000667572021, 0.75, 0.3926999866962433, 1], [-1.5499999523162842, 0.75, 0.3926999866962433, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_0.7854_0.75.json b/probe_vis_j_0.7854_0.75.json
new file mode 100644
index 0000000..c3a3c5d
--- /dev/null
+++ b/probe_vis_j_0.7854_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, 0.7853999733924866, 1], [-2.259999990463257, 0.75, 0.7853999733924866, 1], [-2.25, 0.75, 0.7853999733924866, 1], [-2.240000009536743, 0.75, 0.7853999733924866, 1], [-2.2300000190734863, 0.75, 0.7853999733924866, 1], [-2.2249999046325684, 0.75, 0.7853999733924866, 1], [-2.2200000286102295, 0.75, 0.7853999733924866, 1], [-2.2149999141693115, 0.75, 0.7853999733924866, 1], [-2.2100000381469727, 0.75, 0.7853999733924866, 1], [-2.2049999237060547, 0.75, 0.7853999733924866, 1], [-2.200000047683716, 0.75, 0.7853999733924866, 1], [-2.194999933242798, 0.75, 0.7853999733924866, 1], [-2.190000057220459, 0.75, 0.7853999733924866, 1], [-2.184999942779541, 0.75, 0.7853999733924866, 1], [-2.180000066757202, 0.75, 0.7853999733924866, 1], [-2.174999952316284, 0.75, 0.7853999733924866, 1], [-2.1700000762939453, 0.75, 0.7853999733924866, 1], [-2.1649999618530273, 0.75, 0.7853999733924866, 1], [-2.1600000858306885, 0.75, 0.7853999733924866, 1], [-2.1549999713897705, 0.75, 0.7853999733924866, 1], [-2.1500000953674316, 0.75, 0.7853999733924866, 1], [-2.1449999809265137, 0.75, 0.7853999733924866, 1], [-2.134999990463257, 0.75, 0.7853999733924866, 1], [-2.125, 0.75, 0.7853999733924866, 1], [-2.115000009536743, 0.75, 0.7853999733924866, 0], [-2.1050000190734863, 0.75, 0.7853999733924866, 0], [-2.0999999046325684, 0.75, 0.7853999733924866, 0], [-2.0950000286102295, 0.75, 0.7853999733924866, 0], [-2.0899999141693115, 0.75, 0.7853999733924866, 0], [-2.0850000381469727, 0.75, 0.7853999733924866, 0], [-2.0799999237060547, 0.75, 0.7853999733924866, 0], [-2.075000047683716, 0.75, 0.7853999733924866, 0], [-2.069999933242798, 0.75, 0.7853999733924866, 0], [-2.065000057220459, 0.75, 0.7853999733924866, 0], [-2.059999942779541, 0.75, 0.7853999733924866, 0], [-2.055000066757202, 0.75, 0.7853999733924866, 0], [-2.049999952316284, 0.75, 0.7853999733924866, 0], [-2.0450000762939453, 0.75, 0.7853999733924866, 0], [-2.0399999618530273, 0.75, 0.7853999733924866, 0], [-2.0350000858306885, 0.75, 0.7853999733924866, 0], [-2.0299999713897705, 0.75, 0.7853999733924866, 0], [-2.0250000953674316, 0.75, 0.7853999733924866, 0], [-2.0199999809265137, 0.75, 0.7853999733924866, 0], [-2.009999990463257, 0.75, 0.7853999733924866, 0], [-2.0, 0.75, 0.7853999733924866, 0], [-1.9950000047683716, 0.75, 0.7853999733924866, 0], [-1.9900000095367432, 0.75, 0.7853999733924866, 0], [-1.9850000143051147, 0.75, 0.7853999733924866, 0], [-1.9800000190734863, 0.75, 0.7853999733924866, 0], [-1.9749999046325684, 0.75, 0.7853999733924866, 0], [-1.9700000286102295, 0.75, 0.7853999733924866, 0], [-1.965000033378601, 0.75, 0.7853999733924866, 0], [-1.9600000381469727, 0.75, 0.7853999733924866, 0], [-1.9549999237060547, 0.75, 0.7853999733924866, 0], [-1.9500000476837158, 0.75, 0.7853999733924866, 0], [-1.9449999332427979, 0.75, 0.7853999733924866, 0], [-1.940000057220459, 0.75, 0.7853999733924866, 0], [-1.934999942779541, 0.75, 0.7853999733924866, 0], [-1.9300000667572021, 0.75, 0.7853999733924866, 0], [-1.9249999523162842, 0.75, 0.7853999733924866, 0], [-1.9200000762939453, 0.75, 0.7853999733924866, 0], [-1.9149999618530273, 0.75, 0.7853999733924866, 0], [-1.909999966621399, 0.75, 0.7853999733924866, 0], [-1.9049999713897705, 0.75, 0.7853999733924866, 0], [-1.9000000953674316, 0.75, 0.7853999733924866, 0], [-1.8949999809265137, 0.75, 0.7853999733924866, 0], [-1.8899999856948853, 0.75, 0.7853999733924866, 0], [-1.8849999904632568, 0.75, 0.7853999733924866, 0], [-1.8799999952316284, 0.75, 0.7853999733924866, 0], [-1.875, 0.75, 0.7853999733924866, 0], [-1.8700000047683716, 0.75, 0.7853999733924866, 0], [-1.8650000095367432, 0.75, 0.7853999733924866, 0], [-1.8600000143051147, 0.75, 0.7853999733924866, 0], [-1.8550000190734863, 0.75, 0.7853999733924866, 0], [-1.8499999046325684, 0.75, 0.7853999733924866, 0], [-1.8450000286102295, 0.75, 0.7853999733924866, 1], [-1.840000033378601, 0.75, 0.7853999733924866, 1], [-1.8350000381469727, 0.75, 0.7853999733924866, 1], [-1.8299999237060547, 0.75, 0.7853999733924866, 1], [-1.8250000476837158, 0.75, 0.7853999733924866, 1], [-1.8199999332427979, 0.75, 0.7853999733924866, 1], [-1.815000057220459, 0.75, 0.7853999733924866, 1], [-1.809999942779541, 0.75, 0.7853999733924866, 1], [-1.8050000667572021, 0.75, 0.7853999733924866, 1], [-1.7999999523162842, 0.75, 0.7853999733924866, 1], [-1.7950000762939453, 0.75, 0.7853999733924866, 1], [-1.7899999618530273, 0.75, 0.7853999733924866, 1], [-1.784999966621399, 0.75, 0.7853999733924866, 1], [-1.7799999713897705, 0.75, 0.7853999733924866, 1], [-1.7750000953674316, 0.75, 0.7853999733924866, 1], [-1.7699999809265137, 0.75, 0.7853999733924866, 1], [-1.7649999856948853, 0.75, 0.7853999733924866, 1], [-1.7599999904632568, 0.75, 0.7853999733924866, 1], [-1.7549999952316284, 0.75, 0.7853999733924866, 1], [-1.75, 0.75, 0.7853999733924866, 1], [-1.7450000047683716, 0.75, 0.7853999733924866, 1], [-1.7400000095367432, 0.75, 0.7853999733924866, 1], [-1.7350000143051147, 0.75, 0.7853999733924866, 1], [-1.7300000190734863, 0.75, 0.7853999733924866, 1], [-1.7249999046325684, 0.75, 0.7853999733924866, 1], [-1.7200000286102295, 0.75, 0.7853999733924866, 1], [-1.715000033378601, 0.75, 0.7853999733924866, 1], [-1.7100000381469727, 0.75, 0.7853999733924866, 1], [-1.7049999237060547, 0.75, 0.7853999733924866, 1], [-1.7000000476837158, 0.75, 0.7853999733924866, 1], [-1.6949999332427979, 0.75, 0.7853999733924866, 1], [-1.690000057220459, 0.75, 0.7853999733924866, 1], [-1.684999942779541, 0.75, 0.7853999733924866, 1], [-1.6800000667572021, 0.75, 0.7853999733924866, 1], [-1.6749999523162842, 0.75, 0.7853999733924866, 1], [-1.6700000762939453, 0.75, 0.7853999733924866, 1], [-1.6649999618530273, 0.75, 0.7853999733924866, 1], [-1.659999966621399, 0.75, 0.7853999733924866, 1], [-1.6549999713897705, 0.75, 0.7853999733924866, 1], [-1.6500000953674316, 0.75, 0.7853999733924866, 1], [-1.6449999809265137, 0.75, 0.7853999733924866, 1], [-1.6399999856948853, 0.75, 0.7853999733924866, 1], [-1.6349999904632568, 0.75, 0.7853999733924866, 1], [-1.6299999952316284, 0.75, 0.7853999733924866, 1], [-1.625, 0.75, 0.7853999733924866, 1], [-1.6200000047683716, 0.75, 0.7853999733924866, 1], [-1.6150000095367432, 0.75, 0.7853999733924866, 1], [-1.6100000143051147, 0.75, 0.7853999733924866, 1], [-1.6050000190734863, 0.75, 0.7853999733924866, 1], [-1.5999999046325684, 0.75, 0.7853999733924866, 1], [-1.5950000286102295, 0.75, 0.7853999733924866, 1], [-1.590000033378601, 0.75, 0.7853999733924866, 1], [-1.5850000381469727, 0.75, 0.7853999733924866, 1], [-1.5799999237060547, 0.75, 0.7853999733924866, 1], [-1.5750000476837158, 0.75, 0.7853999733924866, 1], [-1.5699999332427979, 0.75, 0.7853999733924866, 1], [-1.565000057220459, 0.75, 0.7853999733924866, 1], [-1.559999942779541, 0.75, 0.7853999733924866, 1], [-1.5550000667572021, 0.75, 0.7853999733924866, 1], [-1.5499999523162842, 0.75, 0.7853999733924866, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_1.1781_0.75.json b/probe_vis_j_1.1781_0.75.json
new file mode 100644
index 0000000..565c8ac
--- /dev/null
+++ b/probe_vis_j_1.1781_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, 1.1780999898910522, 1], [-2.259999990463257, 0.75, 1.1780999898910522, 1], [-2.25, 0.75, 1.1780999898910522, 1], [-2.240000009536743, 0.75, 1.1780999898910522, 1], [-2.2300000190734863, 0.75, 1.1780999898910522, 1], [-2.2249999046325684, 0.75, 1.1780999898910522, 1], [-2.2200000286102295, 0.75, 1.1780999898910522, 1], [-2.2149999141693115, 0.75, 1.1780999898910522, 1], [-2.2100000381469727, 0.75, 1.1780999898910522, 1], [-2.2049999237060547, 0.75, 1.1780999898910522, 1], [-2.200000047683716, 0.75, 1.1780999898910522, 1], [-2.194999933242798, 0.75, 1.1780999898910522, 1], [-2.190000057220459, 0.75, 1.1780999898910522, 1], [-2.184999942779541, 0.75, 1.1780999898910522, 1], [-2.180000066757202, 0.75, 1.1780999898910522, 1], [-2.174999952316284, 0.75, 1.1780999898910522, 1], [-2.1700000762939453, 0.75, 1.1780999898910522, 1], [-2.1649999618530273, 0.75, 1.1780999898910522, 1], [-2.1600000858306885, 0.75, 1.1780999898910522, 1], [-2.1549999713897705, 0.75, 1.1780999898910522, 0], [-2.1500000953674316, 0.75, 1.1780999898910522, 0], [-2.1449999809265137, 0.75, 1.1780999898910522, 0], [-2.134999990463257, 0.75, 1.1780999898910522, 0], [-2.125, 0.75, 1.1780999898910522, 0], [-2.115000009536743, 0.75, 1.1780999898910522, 0], [-2.1050000190734863, 0.75, 1.1780999898910522, 0], [-2.0999999046325684, 0.75, 1.1780999898910522, 0], [-2.0950000286102295, 0.75, 1.1780999898910522, 0], [-2.0899999141693115, 0.75, 1.1780999898910522, 0], [-2.0850000381469727, 0.75, 1.1780999898910522, 0], [-2.0799999237060547, 0.75, 1.1780999898910522, 0], [-2.075000047683716, 0.75, 1.1780999898910522, 0], [-2.069999933242798, 0.75, 1.1780999898910522, 0], [-2.065000057220459, 0.75, 1.1780999898910522, 0], [-2.059999942779541, 0.75, 1.1780999898910522, 0], [-2.055000066757202, 0.75, 1.1780999898910522, 0], [-2.049999952316284, 0.75, 1.1780999898910522, 0], [-2.0450000762939453, 0.75, 1.1780999898910522, 0], [-2.0399999618530273, 0.75, 1.1780999898910522, 0], [-2.0350000858306885, 0.75, 1.1780999898910522, 0], [-2.0299999713897705, 0.75, 1.1780999898910522, 0], [-2.0250000953674316, 0.75, 1.1780999898910522, 0], [-2.0199999809265137, 0.75, 1.1780999898910522, 0], [-2.009999990463257, 0.75, 1.1780999898910522, 0], [-2.0, 0.75, 1.1780999898910522, 0], [-1.9950000047683716, 0.75, 1.1780999898910522, 0], [-1.9900000095367432, 0.75, 1.1780999898910522, 0], [-1.9850000143051147, 0.75, 1.1780999898910522, 0], [-1.9800000190734863, 0.75, 1.1780999898910522, 0], [-1.9749999046325684, 0.75, 1.1780999898910522, 0], [-1.9700000286102295, 0.75, 1.1780999898910522, 0], [-1.965000033378601, 0.75, 1.1780999898910522, 0], [-1.9600000381469727, 0.75, 1.1780999898910522, 0], [-1.9549999237060547, 0.75, 1.1780999898910522, 0], [-1.9500000476837158, 0.75, 1.1780999898910522, 0], [-1.9449999332427979, 0.75, 1.1780999898910522, 0], [-1.940000057220459, 0.75, 1.1780999898910522, 0], [-1.934999942779541, 0.75, 1.1780999898910522, 0], [-1.9300000667572021, 0.75, 1.1780999898910522, 0], [-1.9249999523162842, 0.75, 1.1780999898910522, 0], [-1.9200000762939453, 0.75, 1.1780999898910522, 0], [-1.9149999618530273, 0.75, 1.1780999898910522, 0], [-1.909999966621399, 0.75, 1.1780999898910522, 0], [-1.9049999713897705, 0.75, 1.1780999898910522, 0], [-1.9000000953674316, 0.75, 1.1780999898910522, 0], [-1.8949999809265137, 0.75, 1.1780999898910522, 0], [-1.8899999856948853, 0.75, 1.1780999898910522, 0], [-1.8849999904632568, 0.75, 1.1780999898910522, 0], [-1.8799999952316284, 0.75, 1.1780999898910522, 0], [-1.875, 0.75, 1.1780999898910522, 1], [-1.8700000047683716, 0.75, 1.1780999898910522, 1], [-1.8650000095367432, 0.75, 1.1780999898910522, 1], [-1.8600000143051147, 0.75, 1.1780999898910522, 1], [-1.8550000190734863, 0.75, 1.1780999898910522, 1], [-1.8499999046325684, 0.75, 1.1780999898910522, 1], [-1.8450000286102295, 0.75, 1.1780999898910522, 1], [-1.840000033378601, 0.75, 1.1780999898910522, 1], [-1.8350000381469727, 0.75, 1.1780999898910522, 1], [-1.8299999237060547, 0.75, 1.1780999898910522, 1], [-1.8250000476837158, 0.75, 1.1780999898910522, 1], [-1.8199999332427979, 0.75, 1.1780999898910522, 1], [-1.815000057220459, 0.75, 1.1780999898910522, 1], [-1.809999942779541, 0.75, 1.1780999898910522, 1], [-1.8050000667572021, 0.75, 1.1780999898910522, 1], [-1.7999999523162842, 0.75, 1.1780999898910522, 1], [-1.7950000762939453, 0.75, 1.1780999898910522, 1], [-1.7899999618530273, 0.75, 1.1780999898910522, 1], [-1.784999966621399, 0.75, 1.1780999898910522, 1], [-1.7799999713897705, 0.75, 1.1780999898910522, 1], [-1.7750000953674316, 0.75, 1.1780999898910522, 1], [-1.7699999809265137, 0.75, 1.1780999898910522, 1], [-1.7649999856948853, 0.75, 1.1780999898910522, 1], [-1.7599999904632568, 0.75, 1.1780999898910522, 1], [-1.7549999952316284, 0.75, 1.1780999898910522, 1], [-1.75, 0.75, 1.1780999898910522, 1], [-1.7450000047683716, 0.75, 1.1780999898910522, 1], [-1.7400000095367432, 0.75, 1.1780999898910522, 1], [-1.7350000143051147, 0.75, 1.1780999898910522, 1], [-1.7300000190734863, 0.75, 1.1780999898910522, 1], [-1.7249999046325684, 0.75, 1.1780999898910522, 1], [-1.7200000286102295, 0.75, 1.1780999898910522, 1], [-1.715000033378601, 0.75, 1.1780999898910522, 1], [-1.7100000381469727, 0.75, 1.1780999898910522, 1], [-1.7049999237060547, 0.75, 1.1780999898910522, 1], [-1.7000000476837158, 0.75, 1.1780999898910522, 1], [-1.6949999332427979, 0.75, 1.1780999898910522, 1], [-1.690000057220459, 0.75, 1.1780999898910522, 1], [-1.684999942779541, 0.75, 1.1780999898910522, 1], [-1.6800000667572021, 0.75, 1.1780999898910522, 1], [-1.6749999523162842, 0.75, 1.1780999898910522, 1], [-1.6700000762939453, 0.75, 1.1780999898910522, 1], [-1.6649999618530273, 0.75, 1.1780999898910522, 1], [-1.659999966621399, 0.75, 1.1780999898910522, 1], [-1.6549999713897705, 0.75, 1.1780999898910522, 1], [-1.6500000953674316, 0.75, 1.1780999898910522, 1], [-1.6449999809265137, 0.75, 1.1780999898910522, 1], [-1.6399999856948853, 0.75, 1.1780999898910522, 1], [-1.6349999904632568, 0.75, 1.1780999898910522, 1], [-1.6299999952316284, 0.75, 1.1780999898910522, 1], [-1.625, 0.75, 1.1780999898910522, 1], [-1.6200000047683716, 0.75, 1.1780999898910522, 1], [-1.6150000095367432, 0.75, 1.1780999898910522, 1], [-1.6100000143051147, 0.75, 1.1780999898910522, 1], [-1.6050000190734863, 0.75, 1.1780999898910522, 1], [-1.5999999046325684, 0.75, 1.1780999898910522, 1], [-1.5950000286102295, 0.75, 1.1780999898910522, 1], [-1.590000033378601, 0.75, 1.1780999898910522, 1], [-1.5850000381469727, 0.75, 1.1780999898910522, 1], [-1.5799999237060547, 0.75, 1.1780999898910522, 1], [-1.5750000476837158, 0.75, 1.1780999898910522, 1], [-1.5699999332427979, 0.75, 1.1780999898910522, 1], [-1.565000057220459, 0.75, 1.1780999898910522, 1], [-1.559999942779541, 0.75, 1.1780999898910522, 1], [-1.5550000667572021, 0.75, 1.1780999898910522, 1], [-1.5499999523162842, 0.75, 1.1780999898910522, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_1.5708_0.75.json b/probe_vis_j_1.5708_0.75.json
new file mode 100644
index 0000000..5ee0a5f
--- /dev/null
+++ b/probe_vis_j_1.5708_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, 1.5707999467849731, 1], [-2.259999990463257, 0.75, 1.5707999467849731, 1], [-2.25, 0.75, 1.5707999467849731, 1], [-2.240000009536743, 0.75, 1.5707999467849731, 1], [-2.2300000190734863, 0.75, 1.5707999467849731, 1], [-2.2249999046325684, 0.75, 1.5707999467849731, 1], [-2.2200000286102295, 0.75, 1.5707999467849731, 1], [-2.2149999141693115, 0.75, 1.5707999467849731, 1], [-2.2100000381469727, 0.75, 1.5707999467849731, 1], [-2.2049999237060547, 0.75, 1.5707999467849731, 1], [-2.200000047683716, 0.75, 1.5707999467849731, 1], [-2.194999933242798, 0.75, 1.5707999467849731, 1], [-2.190000057220459, 0.75, 1.5707999467849731, 1], [-2.184999942779541, 0.75, 1.5707999467849731, 0], [-2.180000066757202, 0.75, 1.5707999467849731, 0], [-2.174999952316284, 0.75, 1.5707999467849731, 0], [-2.1700000762939453, 0.75, 1.5707999467849731, 0], [-2.1649999618530273, 0.75, 1.5707999467849731, 0], [-2.1600000858306885, 0.75, 1.5707999467849731, 0], [-2.1549999713897705, 0.75, 1.5707999467849731, 0], [-2.1500000953674316, 0.75, 1.5707999467849731, 0], [-2.1449999809265137, 0.75, 1.5707999467849731, 0], [-2.134999990463257, 0.75, 1.5707999467849731, 0], [-2.125, 0.75, 1.5707999467849731, 0], [-2.115000009536743, 0.75, 1.5707999467849731, 0], [-2.1050000190734863, 0.75, 1.5707999467849731, 0], [-2.0999999046325684, 0.75, 1.5707999467849731, 0], [-2.0950000286102295, 0.75, 1.5707999467849731, 0], [-2.0899999141693115, 0.75, 1.5707999467849731, 0], [-2.0850000381469727, 0.75, 1.5707999467849731, 0], [-2.0799999237060547, 0.75, 1.5707999467849731, 0], [-2.075000047683716, 0.75, 1.5707999467849731, 0], [-2.069999933242798, 0.75, 1.5707999467849731, 0], [-2.065000057220459, 0.75, 1.5707999467849731, 0], [-2.059999942779541, 0.75, 1.5707999467849731, 0], [-2.055000066757202, 0.75, 1.5707999467849731, 0], [-2.049999952316284, 0.75, 1.5707999467849731, 0], [-2.0450000762939453, 0.75, 1.5707999467849731, 0], [-2.0399999618530273, 0.75, 1.5707999467849731, 0], [-2.0350000858306885, 0.75, 1.5707999467849731, 0], [-2.0299999713897705, 0.75, 1.5707999467849731, 0], [-2.0250000953674316, 0.75, 1.5707999467849731, 0], [-2.0199999809265137, 0.75, 1.5707999467849731, 0], [-2.009999990463257, 0.75, 1.5707999467849731, 0], [-2.0, 0.75, 1.5707999467849731, 0], [-1.9950000047683716, 0.75, 1.5707999467849731, 0], [-1.9900000095367432, 0.75, 1.5707999467849731, 0], [-1.9850000143051147, 0.75, 1.5707999467849731, 0], [-1.9800000190734863, 0.75, 1.5707999467849731, 0], [-1.9749999046325684, 0.75, 1.5707999467849731, 0], [-1.9700000286102295, 0.75, 1.5707999467849731, 0], [-1.965000033378601, 0.75, 1.5707999467849731, 0], [-1.9600000381469727, 0.75, 1.5707999467849731, 0], [-1.9549999237060547, 0.75, 1.5707999467849731, 0], [-1.9500000476837158, 0.75, 1.5707999467849731, 0], [-1.9449999332427979, 0.75, 1.5707999467849731, 0], [-1.940000057220459, 0.75, 1.5707999467849731, 0], [-1.934999942779541, 0.75, 1.5707999467849731, 0], [-1.9300000667572021, 0.75, 1.5707999467849731, 0], [-1.9249999523162842, 0.75, 1.5707999467849731, 0], [-1.9200000762939453, 0.75, 1.5707999467849731, 0], [-1.9149999618530273, 0.75, 1.5707999467849731, 0], [-1.909999966621399, 0.75, 1.5707999467849731, 1], [-1.9049999713897705, 0.75, 1.5707999467849731, 1], [-1.9000000953674316, 0.75, 1.5707999467849731, 1], [-1.8949999809265137, 0.75, 1.5707999467849731, 1], [-1.8899999856948853, 0.75, 1.5707999467849731, 1], [-1.8849999904632568, 0.75, 1.5707999467849731, 1], [-1.8799999952316284, 0.75, 1.5707999467849731, 1], [-1.875, 0.75, 1.5707999467849731, 1], [-1.8700000047683716, 0.75, 1.5707999467849731, 1], [-1.8650000095367432, 0.75, 1.5707999467849731, 1], [-1.8600000143051147, 0.75, 1.5707999467849731, 1], [-1.8550000190734863, 0.75, 1.5707999467849731, 1], [-1.8499999046325684, 0.75, 1.5707999467849731, 1], [-1.8450000286102295, 0.75, 1.5707999467849731, 1], [-1.840000033378601, 0.75, 1.5707999467849731, 1], [-1.8350000381469727, 0.75, 1.5707999467849731, 1], [-1.8299999237060547, 0.75, 1.5707999467849731, 1], [-1.8250000476837158, 0.75, 1.5707999467849731, 1], [-1.8199999332427979, 0.75, 1.5707999467849731, 1], [-1.815000057220459, 0.75, 1.5707999467849731, 1], [-1.809999942779541, 0.75, 1.5707999467849731, 1], [-1.8050000667572021, 0.75, 1.5707999467849731, 1], [-1.7999999523162842, 0.75, 1.5707999467849731, 1], [-1.7950000762939453, 0.75, 1.5707999467849731, 1], [-1.7899999618530273, 0.75, 1.5707999467849731, 1], [-1.784999966621399, 0.75, 1.5707999467849731, 1], [-1.7799999713897705, 0.75, 1.5707999467849731, 1], [-1.7750000953674316, 0.75, 1.5707999467849731, 1], [-1.7699999809265137, 0.75, 1.5707999467849731, 1], [-1.7649999856948853, 0.75, 1.5707999467849731, 1], [-1.7599999904632568, 0.75, 1.5707999467849731, 1], [-1.7549999952316284, 0.75, 1.5707999467849731, 1], [-1.75, 0.75, 1.5707999467849731, 1], [-1.7450000047683716, 0.75, 1.5707999467849731, 1], [-1.7400000095367432, 0.75, 1.5707999467849731, 1], [-1.7350000143051147, 0.75, 1.5707999467849731, 1], [-1.7300000190734863, 0.75, 1.5707999467849731, 1], [-1.7249999046325684, 0.75, 1.5707999467849731, 1], [-1.7200000286102295, 0.75, 1.5707999467849731, 1], [-1.715000033378601, 0.75, 1.5707999467849731, 1], [-1.7100000381469727, 0.75, 1.5707999467849731, 1], [-1.7049999237060547, 0.75, 1.5707999467849731, 1], [-1.7000000476837158, 0.75, 1.5707999467849731, 1], [-1.6949999332427979, 0.75, 1.5707999467849731, 1], [-1.690000057220459, 0.75, 1.5707999467849731, 1], [-1.684999942779541, 0.75, 1.5707999467849731, 1], [-1.6800000667572021, 0.75, 1.5707999467849731, 1], [-1.6749999523162842, 0.75, 1.5707999467849731, 1], [-1.6700000762939453, 0.75, 1.5707999467849731, 1], [-1.6649999618530273, 0.75, 1.5707999467849731, 1], [-1.659999966621399, 0.75, 1.5707999467849731, 1], [-1.6549999713897705, 0.75, 1.5707999467849731, 1], [-1.6500000953674316, 0.75, 1.5707999467849731, 1], [-1.6449999809265137, 0.75, 1.5707999467849731, 1], [-1.6399999856948853, 0.75, 1.5707999467849731, 1], [-1.6349999904632568, 0.75, 1.5707999467849731, 1], [-1.6299999952316284, 0.75, 1.5707999467849731, 1], [-1.625, 0.75, 1.5707999467849731, 1], [-1.6200000047683716, 0.75, 1.5707999467849731, 1], [-1.6150000095367432, 0.75, 1.5707999467849731, 1], [-1.6100000143051147, 0.75, 1.5707999467849731, 1], [-1.6050000190734863, 0.75, 1.5707999467849731, 1], [-1.5999999046325684, 0.75, 1.5707999467849731, 1], [-1.5950000286102295, 0.75, 1.5707999467849731, 1], [-1.590000033378601, 0.75, 1.5707999467849731, 1], [-1.5850000381469727, 0.75, 1.5707999467849731, 1], [-1.5799999237060547, 0.75, 1.5707999467849731, 1], [-1.5750000476837158, 0.75, 1.5707999467849731, 1], [-1.5699999332427979, 0.75, 1.5707999467849731, 1], [-1.565000057220459, 0.75, 1.5707999467849731, 1], [-1.559999942779541, 0.75, 1.5707999467849731, 1], [-1.5550000667572021, 0.75, 1.5707999467849731, 1], [-1.5499999523162842, 0.75, 1.5707999467849731, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_1.9635_0.75.json b/probe_vis_j_1.9635_0.75.json
new file mode 100644
index 0000000..6946ace
--- /dev/null
+++ b/probe_vis_j_1.9635_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, 1.9635000228881836, 1], [-2.259999990463257, 0.75, 1.9635000228881836, 1], [-2.25, 0.75, 1.9635000228881836, 1], [-2.240000009536743, 0.75, 1.9635000228881836, 1], [-2.2300000190734863, 0.75, 1.9635000228881836, 1], [-2.2249999046325684, 0.75, 1.9635000228881836, 1], [-2.2200000286102295, 0.75, 1.9635000228881836, 1], [-2.2149999141693115, 0.75, 1.9635000228881836, 0], [-2.2100000381469727, 0.75, 1.9635000228881836, 0], [-2.2049999237060547, 0.75, 1.9635000228881836, 0], [-2.200000047683716, 0.75, 1.9635000228881836, 0], [-2.194999933242798, 0.75, 1.9635000228881836, 0], [-2.190000057220459, 0.75, 1.9635000228881836, 0], [-2.184999942779541, 0.75, 1.9635000228881836, 0], [-2.180000066757202, 0.75, 1.9635000228881836, 0], [-2.174999952316284, 0.75, 1.9635000228881836, 0], [-2.1700000762939453, 0.75, 1.9635000228881836, 0], [-2.1649999618530273, 0.75, 1.9635000228881836, 0], [-2.1600000858306885, 0.75, 1.9635000228881836, 0], [-2.1549999713897705, 0.75, 1.9635000228881836, 0], [-2.1500000953674316, 0.75, 1.9635000228881836, 0], [-2.1449999809265137, 0.75, 1.9635000228881836, 0], [-2.134999990463257, 0.75, 1.9635000228881836, 0], [-2.125, 0.75, 1.9635000228881836, 0], [-2.115000009536743, 0.75, 1.9635000228881836, 0], [-2.1050000190734863, 0.75, 1.9635000228881836, 0], [-2.0999999046325684, 0.75, 1.9635000228881836, 0], [-2.0950000286102295, 0.75, 1.9635000228881836, 0], [-2.0899999141693115, 0.75, 1.9635000228881836, 0], [-2.0850000381469727, 0.75, 1.9635000228881836, 0], [-2.0799999237060547, 0.75, 1.9635000228881836, 0], [-2.075000047683716, 0.75, 1.9635000228881836, 0], [-2.069999933242798, 0.75, 1.9635000228881836, 0], [-2.065000057220459, 0.75, 1.9635000228881836, 0], [-2.059999942779541, 0.75, 1.9635000228881836, 0], [-2.055000066757202, 0.75, 1.9635000228881836, 0], [-2.049999952316284, 0.75, 1.9635000228881836, 0], [-2.0450000762939453, 0.75, 1.9635000228881836, 0], [-2.0399999618530273, 0.75, 1.9635000228881836, 0], [-2.0350000858306885, 0.75, 1.9635000228881836, 0], [-2.0299999713897705, 0.75, 1.9635000228881836, 0], [-2.0250000953674316, 0.75, 1.9635000228881836, 0], [-2.0199999809265137, 0.75, 1.9635000228881836, 0], [-2.009999990463257, 0.75, 1.9635000228881836, 0], [-2.0, 0.75, 1.9635000228881836, 0], [-1.9950000047683716, 0.75, 1.9635000228881836, 0], [-1.9900000095367432, 0.75, 1.9635000228881836, 0], [-1.9850000143051147, 0.75, 1.9635000228881836, 0], [-1.9800000190734863, 0.75, 1.9635000228881836, 0], [-1.9749999046325684, 0.75, 1.9635000228881836, 0], [-1.9700000286102295, 0.75, 1.9635000228881836, 0], [-1.965000033378601, 0.75, 1.9635000228881836, 0], [-1.9600000381469727, 0.75, 1.9635000228881836, 0], [-1.9549999237060547, 0.75, 1.9635000228881836, 0], [-1.9500000476837158, 0.75, 1.9635000228881836, 0], [-1.9449999332427979, 0.75, 1.9635000228881836, 1], [-1.940000057220459, 0.75, 1.9635000228881836, 1], [-1.934999942779541, 0.75, 1.9635000228881836, 1], [-1.9300000667572021, 0.75, 1.9635000228881836, 1], [-1.9249999523162842, 0.75, 1.9635000228881836, 1], [-1.9200000762939453, 0.75, 1.9635000228881836, 1], [-1.9149999618530273, 0.75, 1.9635000228881836, 1], [-1.909999966621399, 0.75, 1.9635000228881836, 1], [-1.9049999713897705, 0.75, 1.9635000228881836, 1], [-1.9000000953674316, 0.75, 1.9635000228881836, 1], [-1.8949999809265137, 0.75, 1.9635000228881836, 1], [-1.8899999856948853, 0.75, 1.9635000228881836, 1], [-1.8849999904632568, 0.75, 1.9635000228881836, 1], [-1.8799999952316284, 0.75, 1.9635000228881836, 1], [-1.875, 0.75, 1.9635000228881836, 1], [-1.8700000047683716, 0.75, 1.9635000228881836, 1], [-1.8650000095367432, 0.75, 1.9635000228881836, 1], [-1.8600000143051147, 0.75, 1.9635000228881836, 1], [-1.8550000190734863, 0.75, 1.9635000228881836, 1], [-1.8499999046325684, 0.75, 1.9635000228881836, 1], [-1.8450000286102295, 0.75, 1.9635000228881836, 1], [-1.840000033378601, 0.75, 1.9635000228881836, 1], [-1.8350000381469727, 0.75, 1.9635000228881836, 1], [-1.8299999237060547, 0.75, 1.9635000228881836, 1], [-1.8250000476837158, 0.75, 1.9635000228881836, 1], [-1.8199999332427979, 0.75, 1.9635000228881836, 1], [-1.815000057220459, 0.75, 1.9635000228881836, 1], [-1.809999942779541, 0.75, 1.9635000228881836, 1], [-1.8050000667572021, 0.75, 1.9635000228881836, 1], [-1.7999999523162842, 0.75, 1.9635000228881836, 1], [-1.7950000762939453, 0.75, 1.9635000228881836, 1], [-1.7899999618530273, 0.75, 1.9635000228881836, 1], [-1.784999966621399, 0.75, 1.9635000228881836, 1], [-1.7799999713897705, 0.75, 1.9635000228881836, 1], [-1.7750000953674316, 0.75, 1.9635000228881836, 1], [-1.7699999809265137, 0.75, 1.9635000228881836, 1], [-1.7649999856948853, 0.75, 1.9635000228881836, 1], [-1.7599999904632568, 0.75, 1.9635000228881836, 1], [-1.7549999952316284, 0.75, 1.9635000228881836, 1], [-1.75, 0.75, 1.9635000228881836, 1], [-1.7450000047683716, 0.75, 1.9635000228881836, 1], [-1.7400000095367432, 0.75, 1.9635000228881836, 1], [-1.7350000143051147, 0.75, 1.9635000228881836, 1], [-1.7300000190734863, 0.75, 1.9635000228881836, 1], [-1.7249999046325684, 0.75, 1.9635000228881836, 1], [-1.7200000286102295, 0.75, 1.9635000228881836, 1], [-1.715000033378601, 0.75, 1.9635000228881836, 1], [-1.7100000381469727, 0.75, 1.9635000228881836, 1], [-1.7049999237060547, 0.75, 1.9635000228881836, 1], [-1.7000000476837158, 0.75, 1.9635000228881836, 1], [-1.6949999332427979, 0.75, 1.9635000228881836, 1], [-1.690000057220459, 0.75, 1.9635000228881836, 1], [-1.684999942779541, 0.75, 1.9635000228881836, 1], [-1.6800000667572021, 0.75, 1.9635000228881836, 1], [-1.6749999523162842, 0.75, 1.9635000228881836, 1], [-1.6700000762939453, 0.75, 1.9635000228881836, 1], [-1.6649999618530273, 0.75, 1.9635000228881836, 1], [-1.659999966621399, 0.75, 1.9635000228881836, 1], [-1.6549999713897705, 0.75, 1.9635000228881836, 1], [-1.6500000953674316, 0.75, 1.9635000228881836, 1], [-1.6449999809265137, 0.75, 1.9635000228881836, 1], [-1.6399999856948853, 0.75, 1.9635000228881836, 1], [-1.6349999904632568, 0.75, 1.9635000228881836, 1], [-1.6299999952316284, 0.75, 1.9635000228881836, 1], [-1.625, 0.75, 1.9635000228881836, 1], [-1.6200000047683716, 0.75, 1.9635000228881836, 1], [-1.6150000095367432, 0.75, 1.9635000228881836, 1], [-1.6100000143051147, 0.75, 1.9635000228881836, 1], [-1.6050000190734863, 0.75, 1.9635000228881836, 1], [-1.5999999046325684, 0.75, 1.9635000228881836, 1], [-1.5950000286102295, 0.75, 1.9635000228881836, 1], [-1.590000033378601, 0.75, 1.9635000228881836, 1], [-1.5850000381469727, 0.75, 1.9635000228881836, 1], [-1.5799999237060547, 0.75, 1.9635000228881836, 1], [-1.5750000476837158, 0.75, 1.9635000228881836, 1], [-1.5699999332427979, 0.75, 1.9635000228881836, 1], [-1.565000057220459, 0.75, 1.9635000228881836, 1], [-1.559999942779541, 0.75, 1.9635000228881836, 1], [-1.5550000667572021, 0.75, 1.9635000228881836, 1], [-1.5499999523162842, 0.75, 1.9635000228881836, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_2.35619_0.75.json b/probe_vis_j_2.35619_0.75.json
new file mode 100644
index 0000000..f2b42fa
--- /dev/null
+++ b/probe_vis_j_2.35619_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, 2.3561899662017822, 1], [-2.259999990463257, 0.75, 2.3561899662017822, 1], [-2.25, 0.75, 2.3561899662017822, 1], [-2.240000009536743, 0.75, 2.3561899662017822, 1], [-2.2300000190734863, 0.75, 2.3561899662017822, 0], [-2.2249999046325684, 0.75, 2.3561899662017822, 0], [-2.2200000286102295, 0.75, 2.3561899662017822, 0], [-2.2149999141693115, 0.75, 2.3561899662017822, 0], [-2.2100000381469727, 0.75, 2.3561899662017822, 0], [-2.2049999237060547, 0.75, 2.3561899662017822, 0], [-2.200000047683716, 0.75, 2.3561899662017822, 0], [-2.194999933242798, 0.75, 2.3561899662017822, 0], [-2.190000057220459, 0.75, 2.3561899662017822, 0], [-2.184999942779541, 0.75, 2.3561899662017822, 0], [-2.180000066757202, 0.75, 2.3561899662017822, 0], [-2.174999952316284, 0.75, 2.3561899662017822, 0], [-2.1700000762939453, 0.75, 2.3561899662017822, 0], [-2.1649999618530273, 0.75, 2.3561899662017822, 0], [-2.1600000858306885, 0.75, 2.3561899662017822, 0], [-2.1549999713897705, 0.75, 2.3561899662017822, 0], [-2.1500000953674316, 0.75, 2.3561899662017822, 0], [-2.1449999809265137, 0.75, 2.3561899662017822, 0], [-2.134999990463257, 0.75, 2.3561899662017822, 0], [-2.125, 0.75, 2.3561899662017822, 0], [-2.115000009536743, 0.75, 2.3561899662017822, 0], [-2.1050000190734863, 0.75, 2.3561899662017822, 0], [-2.0999999046325684, 0.75, 2.3561899662017822, 0], [-2.0950000286102295, 0.75, 2.3561899662017822, 0], [-2.0899999141693115, 0.75, 2.3561899662017822, 0], [-2.0850000381469727, 0.75, 2.3561899662017822, 0], [-2.0799999237060547, 0.75, 2.3561899662017822, 0], [-2.075000047683716, 0.75, 2.3561899662017822, 0], [-2.069999933242798, 0.75, 2.3561899662017822, 0], [-2.065000057220459, 0.75, 2.3561899662017822, 0], [-2.059999942779541, 0.75, 2.3561899662017822, 0], [-2.055000066757202, 0.75, 2.3561899662017822, 0], [-2.049999952316284, 0.75, 2.3561899662017822, 0], [-2.0450000762939453, 0.75, 2.3561899662017822, 0], [-2.0399999618530273, 0.75, 2.3561899662017822, 0], [-2.0350000858306885, 0.75, 2.3561899662017822, 0], [-2.0299999713897705, 0.75, 2.3561899662017822, 0], [-2.0250000953674316, 0.75, 2.3561899662017822, 0], [-2.0199999809265137, 0.75, 2.3561899662017822, 0], [-2.009999990463257, 0.75, 2.3561899662017822, 0], [-2.0, 0.75, 2.3561899662017822, 0], [-1.9950000047683716, 0.75, 2.3561899662017822, 0], [-1.9900000095367432, 0.75, 2.3561899662017822, 0], [-1.9850000143051147, 0.75, 2.3561899662017822, 0], [-1.9800000190734863, 0.75, 2.3561899662017822, 1], [-1.9749999046325684, 0.75, 2.3561899662017822, 1], [-1.9700000286102295, 0.75, 2.3561899662017822, 1], [-1.965000033378601, 0.75, 2.3561899662017822, 1], [-1.9600000381469727, 0.75, 2.3561899662017822, 1], [-1.9549999237060547, 0.75, 2.3561899662017822, 1], [-1.9500000476837158, 0.75, 2.3561899662017822, 1], [-1.9449999332427979, 0.75, 2.3561899662017822, 1], [-1.940000057220459, 0.75, 2.3561899662017822, 1], [-1.934999942779541, 0.75, 2.3561899662017822, 1], [-1.9300000667572021, 0.75, 2.3561899662017822, 1], [-1.9249999523162842, 0.75, 2.3561899662017822, 1], [-1.9200000762939453, 0.75, 2.3561899662017822, 1], [-1.9149999618530273, 0.75, 2.3561899662017822, 1], [-1.909999966621399, 0.75, 2.3561899662017822, 1], [-1.9049999713897705, 0.75, 2.3561899662017822, 1], [-1.9000000953674316, 0.75, 2.3561899662017822, 1], [-1.8949999809265137, 0.75, 2.3561899662017822, 1], [-1.8899999856948853, 0.75, 2.3561899662017822, 1], [-1.8849999904632568, 0.75, 2.3561899662017822, 1], [-1.8799999952316284, 0.75, 2.3561899662017822, 1], [-1.875, 0.75, 2.3561899662017822, 1], [-1.8700000047683716, 0.75, 2.3561899662017822, 1], [-1.8650000095367432, 0.75, 2.3561899662017822, 1], [-1.8600000143051147, 0.75, 2.3561899662017822, 1], [-1.8550000190734863, 0.75, 2.3561899662017822, 1], [-1.8499999046325684, 0.75, 2.3561899662017822, 1], [-1.8450000286102295, 0.75, 2.3561899662017822, 1], [-1.840000033378601, 0.75, 2.3561899662017822, 1], [-1.8350000381469727, 0.75, 2.3561899662017822, 1], [-1.8299999237060547, 0.75, 2.3561899662017822, 1], [-1.8250000476837158, 0.75, 2.3561899662017822, 1], [-1.8199999332427979, 0.75, 2.3561899662017822, 1], [-1.815000057220459, 0.75, 2.3561899662017822, 1], [-1.809999942779541, 0.75, 2.3561899662017822, 1], [-1.8050000667572021, 0.75, 2.3561899662017822, 1], [-1.7999999523162842, 0.75, 2.3561899662017822, 1], [-1.7950000762939453, 0.75, 2.3561899662017822, 1], [-1.7899999618530273, 0.75, 2.3561899662017822, 1], [-1.784999966621399, 0.75, 2.3561899662017822, 1], [-1.7799999713897705, 0.75, 2.3561899662017822, 1], [-1.7750000953674316, 0.75, 2.3561899662017822, 1], [-1.7699999809265137, 0.75, 2.3561899662017822, 1], [-1.7649999856948853, 0.75, 2.3561899662017822, 1], [-1.7599999904632568, 0.75, 2.3561899662017822, 1], [-1.7549999952316284, 0.75, 2.3561899662017822, 1], [-1.75, 0.75, 2.3561899662017822, 1], [-1.7450000047683716, 0.75, 2.3561899662017822, 1], [-1.7400000095367432, 0.75, 2.3561899662017822, 1], [-1.7350000143051147, 0.75, 2.3561899662017822, 1], [-1.7300000190734863, 0.75, 2.3561899662017822, 1], [-1.7249999046325684, 0.75, 2.3561899662017822, 1], [-1.7200000286102295, 0.75, 2.3561899662017822, 1], [-1.715000033378601, 0.75, 2.3561899662017822, 1], [-1.7100000381469727, 0.75, 2.3561899662017822, 1], [-1.7049999237060547, 0.75, 2.3561899662017822, 1], [-1.7000000476837158, 0.75, 2.3561899662017822, 1], [-1.6949999332427979, 0.75, 2.3561899662017822, 1], [-1.690000057220459, 0.75, 2.3561899662017822, 1], [-1.684999942779541, 0.75, 2.3561899662017822, 1], [-1.6800000667572021, 0.75, 2.3561899662017822, 1], [-1.6749999523162842, 0.75, 2.3561899662017822, 1], [-1.6700000762939453, 0.75, 2.3561899662017822, 1], [-1.6649999618530273, 0.75, 2.3561899662017822, 1], [-1.659999966621399, 0.75, 2.3561899662017822, 1], [-1.6549999713897705, 0.75, 2.3561899662017822, 1], [-1.6500000953674316, 0.75, 2.3561899662017822, 1], [-1.6449999809265137, 0.75, 2.3561899662017822, 1], [-1.6399999856948853, 0.75, 2.3561899662017822, 1], [-1.6349999904632568, 0.75, 2.3561899662017822, 1], [-1.6299999952316284, 0.75, 2.3561899662017822, 1], [-1.625, 0.75, 2.3561899662017822, 1], [-1.6200000047683716, 0.75, 2.3561899662017822, 1], [-1.6150000095367432, 0.75, 2.3561899662017822, 1], [-1.6100000143051147, 0.75, 2.3561899662017822, 1], [-1.6050000190734863, 0.75, 2.3561899662017822, 1], [-1.5999999046325684, 0.75, 2.3561899662017822, 1], [-1.5950000286102295, 0.75, 2.3561899662017822, 1], [-1.590000033378601, 0.75, 2.3561899662017822, 1], [-1.5850000381469727, 0.75, 2.3561899662017822, 1], [-1.5799999237060547, 0.75, 2.3561899662017822, 1], [-1.5750000476837158, 0.75, 2.3561899662017822, 1], [-1.5699999332427979, 0.75, 2.3561899662017822, 1], [-1.565000057220459, 0.75, 2.3561899662017822, 1], [-1.559999942779541, 0.75, 2.3561899662017822, 1], [-1.5550000667572021, 0.75, 2.3561899662017822, 1], [-1.5499999523162842, 0.75, 2.3561899662017822, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_2.74889_0.75.json b/probe_vis_j_2.74889_0.75.json
new file mode 100644
index 0000000..ef538f0
--- /dev/null
+++ b/probe_vis_j_2.74889_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.2699999809265137, 0.75, 2.748889923095703, 1], [-2.259999990463257, 0.75, 2.748889923095703, 1], [-2.25, 0.75, 2.748889923095703, 1], [-2.240000009536743, 0.75, 2.748889923095703, 0], [-2.2300000190734863, 0.75, 2.748889923095703, 0], [-2.2249999046325684, 0.75, 2.748889923095703, 0], [-2.2200000286102295, 0.75, 2.748889923095703, 0], [-2.2149999141693115, 0.75, 2.748889923095703, 0], [-2.2100000381469727, 0.75, 2.748889923095703, 0], [-2.2049999237060547, 0.75, 2.748889923095703, 0], [-2.200000047683716, 0.75, 2.748889923095703, 0], [-2.194999933242798, 0.75, 2.748889923095703, 0], [-2.190000057220459, 0.75, 2.748889923095703, 0], [-2.184999942779541, 0.75, 2.748889923095703, 0], [-2.180000066757202, 0.75, 2.748889923095703, 0], [-2.174999952316284, 0.75, 2.748889923095703, 0], [-2.1700000762939453, 0.75, 2.748889923095703, 0], [-2.1649999618530273, 0.75, 2.748889923095703, 0], [-2.1600000858306885, 0.75, 2.748889923095703, 0], [-2.1549999713897705, 0.75, 2.748889923095703, 0], [-2.1500000953674316, 0.75, 2.748889923095703, 0], [-2.1449999809265137, 0.75, 2.748889923095703, 0], [-2.134999990463257, 0.75, 2.748889923095703, 0], [-2.125, 0.75, 2.748889923095703, 0], [-2.115000009536743, 0.75, 2.748889923095703, 0], [-2.1050000190734863, 0.75, 2.748889923095703, 0], [-2.0999999046325684, 0.75, 2.748889923095703, 0], [-2.0950000286102295, 0.75, 2.748889923095703, 0], [-2.0899999141693115, 0.75, 2.748889923095703, 0], [-2.0850000381469727, 0.75, 2.748889923095703, 0], [-2.0799999237060547, 0.75, 2.748889923095703, 0], [-2.075000047683716, 0.75, 2.748889923095703, 0], [-2.069999933242798, 0.75, 2.748889923095703, 0], [-2.065000057220459, 0.75, 2.748889923095703, 0], [-2.059999942779541, 0.75, 2.748889923095703, 0], [-2.055000066757202, 0.75, 2.748889923095703, 0], [-2.049999952316284, 0.75, 2.748889923095703, 0], [-2.0450000762939453, 0.75, 2.748889923095703, 0], [-2.0399999618530273, 0.75, 2.748889923095703, 0], [-2.0350000858306885, 0.75, 2.748889923095703, 0], [-2.0299999713897705, 0.75, 2.748889923095703, 0], [-2.0250000953674316, 0.75, 2.748889923095703, 0], [-2.0199999809265137, 0.75, 2.748889923095703, 0], [-2.009999990463257, 0.75, 2.748889923095703, 1], [-2.0, 0.75, 2.748889923095703, 1], [-1.9950000047683716, 0.75, 2.748889923095703, 1], [-1.9900000095367432, 0.75, 2.748889923095703, 1], [-1.9850000143051147, 0.75, 2.748889923095703, 1], [-1.9800000190734863, 0.75, 2.748889923095703, 1], [-1.9749999046325684, 0.75, 2.748889923095703, 1], [-1.9700000286102295, 0.75, 2.748889923095703, 1], [-1.965000033378601, 0.75, 2.748889923095703, 1], [-1.9600000381469727, 0.75, 2.748889923095703, 1], [-1.9549999237060547, 0.75, 2.748889923095703, 1], [-1.9500000476837158, 0.75, 2.748889923095703, 1], [-1.9449999332427979, 0.75, 2.748889923095703, 1], [-1.940000057220459, 0.75, 2.748889923095703, 1], [-1.934999942779541, 0.75, 2.748889923095703, 1], [-1.9300000667572021, 0.75, 2.748889923095703, 1], [-1.9249999523162842, 0.75, 2.748889923095703, 1], [-1.9200000762939453, 0.75, 2.748889923095703, 1], [-1.9149999618530273, 0.75, 2.748889923095703, 1], [-1.909999966621399, 0.75, 2.748889923095703, 1], [-1.9049999713897705, 0.75, 2.748889923095703, 1], [-1.9000000953674316, 0.75, 2.748889923095703, 1], [-1.8949999809265137, 0.75, 2.748889923095703, 1], [-1.8899999856948853, 0.75, 2.748889923095703, 1], [-1.8849999904632568, 0.75, 2.748889923095703, 1], [-1.8799999952316284, 0.75, 2.748889923095703, 1], [-1.875, 0.75, 2.748889923095703, 1], [-1.8700000047683716, 0.75, 2.748889923095703, 1], [-1.8650000095367432, 0.75, 2.748889923095703, 1], [-1.8600000143051147, 0.75, 2.748889923095703, 1], [-1.8550000190734863, 0.75, 2.748889923095703, 1], [-1.8499999046325684, 0.75, 2.748889923095703, 1], [-1.8450000286102295, 0.75, 2.748889923095703, 1], [-1.840000033378601, 0.75, 2.748889923095703, 1], [-1.8350000381469727, 0.75, 2.748889923095703, 1], [-1.8299999237060547, 0.75, 2.748889923095703, 1], [-1.8250000476837158, 0.75, 2.748889923095703, 1], [-1.8199999332427979, 0.75, 2.748889923095703, 1], [-1.815000057220459, 0.75, 2.748889923095703, 1], [-1.809999942779541, 0.75, 2.748889923095703, 1], [-1.8050000667572021, 0.75, 2.748889923095703, 1], [-1.7999999523162842, 0.75, 2.748889923095703, 1], [-1.7950000762939453, 0.75, 2.748889923095703, 1], [-1.7899999618530273, 0.75, 2.748889923095703, 1], [-1.784999966621399, 0.75, 2.748889923095703, 1], [-1.7799999713897705, 0.75, 2.748889923095703, 1], [-1.7750000953674316, 0.75, 2.748889923095703, 1], [-1.7699999809265137, 0.75, 2.748889923095703, 1], [-1.7649999856948853, 0.75, 2.748889923095703, 1], [-1.7599999904632568, 0.75, 2.748889923095703, 1], [-1.7549999952316284, 0.75, 2.748889923095703, 1], [-1.75, 0.75, 2.748889923095703, 1], [-1.7450000047683716, 0.75, 2.748889923095703, 1], [-1.7400000095367432, 0.75, 2.748889923095703, 1], [-1.7350000143051147, 0.75, 2.748889923095703, 1], [-1.7300000190734863, 0.75, 2.748889923095703, 1], [-1.7249999046325684, 0.75, 2.748889923095703, 1], [-1.7200000286102295, 0.75, 2.748889923095703, 1], [-1.715000033378601, 0.75, 2.748889923095703, 1], [-1.7100000381469727, 0.75, 2.748889923095703, 1], [-1.7049999237060547, 0.75, 2.748889923095703, 1], [-1.7000000476837158, 0.75, 2.748889923095703, 1], [-1.6949999332427979, 0.75, 2.748889923095703, 1], [-1.690000057220459, 0.75, 2.748889923095703, 1], [-1.684999942779541, 0.75, 2.748889923095703, 1], [-1.6800000667572021, 0.75, 2.748889923095703, 1], [-1.6749999523162842, 0.75, 2.748889923095703, 1], [-1.6700000762939453, 0.75, 2.748889923095703, 1], [-1.6649999618530273, 0.75, 2.748889923095703, 1], [-1.659999966621399, 0.75, 2.748889923095703, 1], [-1.6549999713897705, 0.75, 2.748889923095703, 1], [-1.6500000953674316, 0.75, 2.748889923095703, 1], [-1.6449999809265137, 0.75, 2.748889923095703, 1], [-1.6399999856948853, 0.75, 2.748889923095703, 1], [-1.6349999904632568, 0.75, 2.748889923095703, 1], [-1.6299999952316284, 0.75, 2.748889923095703, 1], [-1.625, 0.75, 2.748889923095703, 1], [-1.6200000047683716, 0.75, 2.748889923095703, 1], [-1.6150000095367432, 0.75, 2.748889923095703, 1], [-1.6100000143051147, 0.75, 2.748889923095703, 1], [-1.6050000190734863, 0.75, 2.748889923095703, 1], [-1.5999999046325684, 0.75, 2.748889923095703, 1], [-1.5950000286102295, 0.75, 2.748889923095703, 1], [-1.590000033378601, 0.75, 2.748889923095703, 1], [-1.5850000381469727, 0.75, 2.748889923095703, 1], [-1.5799999237060547, 0.75, 2.748889923095703, 1], [-1.5750000476837158, 0.75, 2.748889923095703, 1], [-1.5699999332427979, 0.75, 2.748889923095703, 1], [-1.565000057220459, 0.75, 2.748889923095703, 1], [-1.559999942779541, 0.75, 2.748889923095703, 1], [-1.5550000667572021, 0.75, 2.748889923095703, 1], [-1.5499999523162842, 0.75, 2.748889923095703, 1]]
\ No newline at end of file
diff --git a/probe_vis_j_out_0.txt b/probe_vis_j_out_0.txt
new file mode 100644
index 0000000..ad9c7ac
--- /dev/null
+++ b/probe_vis_j_out_0.txt
@@ -0,0 +1 @@
           1 +-3.14159 -2.2699999809265137 111111111111111111111111111111111111111111111100111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_1.txt b/probe_vis_j_out_1.txt
new file mode 100644
index 0000000..84b1df5
--- /dev/null
+++ b/probe_vis_j_out_1.txt
@@ -0,0 +1 @@
           1 +-2.74889 -2.2699999809265137 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_10.txt b/probe_vis_j_out_10.txt
new file mode 100644
index 0000000..8fb683f
--- /dev/null
+++ b/probe_vis_j_out_10.txt
@@ -0,0 +1 @@
           1 +0.7854 -2.2699999809265137 111111111111111111111111000000000000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_11.txt b/probe_vis_j_out_11.txt
new file mode 100644
index 0000000..c8abd4d
--- /dev/null
+++ b/probe_vis_j_out_11.txt
@@ -0,0 +1 @@
           1 +1.1781 -2.2699999809265137 111111111111111111100000000000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_12.txt b/probe_vis_j_out_12.txt
new file mode 100644
index 0000000..be84764
--- /dev/null
+++ b/probe_vis_j_out_12.txt
@@ -0,0 +1 @@
           1 +1.5708 -2.2699999809265137 111111111111100000000000000000000000000000000000000000000000001111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_13.txt b/probe_vis_j_out_13.txt
new file mode 100644
index 0000000..a92e70c
--- /dev/null
+++ b/probe_vis_j_out_13.txt
@@ -0,0 +1 @@
           1 +1.9635 -2.2699999809265137 111111100000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_14.txt b/probe_vis_j_out_14.txt
new file mode 100644
index 0000000..58c1f9c
--- /dev/null
+++ b/probe_vis_j_out_14.txt
@@ -0,0 +1 @@
           1 +2.35619 -2.2699999809265137 111100000000000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_15.txt b/probe_vis_j_out_15.txt
new file mode 100644
index 0000000..d72f8ed
--- /dev/null
+++ b/probe_vis_j_out_15.txt
@@ -0,0 +1 @@
           1 +2.74889 -2.2699999809265137 111000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_2.txt b/probe_vis_j_out_2.txt
new file mode 100644
index 0000000..6cdb348
--- /dev/null
+++ b/probe_vis_j_out_2.txt
@@ -0,0 +1 @@
           1 +-2.35619 -2.2699999809265137 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_3.txt b/probe_vis_j_out_3.txt
new file mode 100644
index 0000000..f739fa3
--- /dev/null
+++ b/probe_vis_j_out_3.txt
@@ -0,0 +1 @@
           1 +-1.9635 -2.2699999809265137 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_4.txt b/probe_vis_j_out_4.txt
new file mode 100644
index 0000000..a0268ea
--- /dev/null
+++ b/probe_vis_j_out_4.txt
@@ -0,0 +1 @@
           1 +-1.5708 -2.2699999809265137 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_5.txt b/probe_vis_j_out_5.txt
new file mode 100644
index 0000000..c02772e
--- /dev/null
+++ b/probe_vis_j_out_5.txt
@@ -0,0 +1 @@
           1 +-1.1781 -2.2699999809265137 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_6.txt b/probe_vis_j_out_6.txt
new file mode 100644
index 0000000..d307202
--- /dev/null
+++ b/probe_vis_j_out_6.txt
@@ -0,0 +1 @@
           1 +-0.7854 -2.2699999809265137 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_7.txt b/probe_vis_j_out_7.txt
new file mode 100644
index 0000000..ae63830
--- /dev/null
+++ b/probe_vis_j_out_7.txt
@@ -0,0 +1 @@
           1 +-0.3927 -2.2699999809265137 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_8.txt b/probe_vis_j_out_8.txt
new file mode 100644
index 0000000..071b645
--- /dev/null
+++ b/probe_vis_j_out_8.txt
@@ -0,0 +1 @@
           1 +0.0 -2.2699999809265137 111111111111111111111111111111111111111111100000000000000000000000000000000000000001111111111111111111111111111111111111111111111111111
diff --git a/probe_vis_j_out_9.txt b/probe_vis_j_out_9.txt
new file mode 100644
index 0000000..4f7b10d
--- /dev/null
+++ b/probe_vis_j_out_9.txt
@@ -0,0 +1 @@
           1 +0.3927 -2.2699999809265137 111111111111111111111111111111111111111111110000000000000000000000000000000000001111111111111111111111111111111111111111111111111111111
```

</details>

<a id="C005"></a>
### C005 · notes

Commit `948d71b4e9589661ec694b9114d1bfe0f09622ff`; parents: db1ff27bac1419ac4ca7ae27778cfbae2aad3703. Recorded author date: 2026-10-01T11:03:37+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0047](01_timeline.md#E0047): commit title in command; output may not confirm creation.
- [E0450](01_timeline.md#E0450): commit title in command; output may not confirm creation.
- [E0524](01_timeline.md#E0524): commit title in command; output may not confirm creation.
- [E0611](01_timeline.md#E0611): commit title in command; output may not confirm creation.
- [E1141](01_timeline.md#E1141): commit title in command; output may not confirm creation.
- [E1363](01_timeline.md#E1363): commit title in command; output may not confirm creation.
- [E1464](01_timeline.md#E1464): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C005_948d71b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/NOTES.md b/NOTES.md
index ee28697..b32860b 100644
--- a/NOTES.md
+++ b/NOTES.md
@@ -18,3 +18,6 @@
   18     18  - Sample: dist < 0.25 (0.245 ok). Sample object persists; can resample after drop. Drop empties store.
   19     19  - Move happens first, then operator evaluated at new position.
   20     20  - Terminated when goal true (needs stores empty). No env truncation. at_home: dist<0.25 from start & |dtheta|<~0.4 (aim <0.35).
          21 +## Objective visibility (probed)
          22 +- cam = (x,y)+R(theta)(-0.087,-0.0125); visible iff |obj-cam|<=1.9976 and (|rel bearing|>~98deg or segment cam'->obj misses pillar boxes inflated ~0.01). Wall & mounds don't block.
          23 +- calibrated persists through moves until a successful image. Image = nearest visible objective not yet imaged by this rover. Calibrate needs any objective visible.
diff --git a/probe_vis_fit3.py b/probe_vis_fit3.py
new file mode 100644
index 0000000..90f343e
--- /dev/null
+++ b/probe_vis_fit3.py
@@ -0,0 +1,30 @@
           1 +import json, math, glob
           2 +import numpy as np
           3 +from probe_vis_model import seg_box_hit
           4 +from probe_vis_lib import E
           5 +e=E(4); ob=e.objs()['objective2']; obj=(ob['x'],ob['y'])
           6 +obs=[tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']) for o in e.obs if o.type.name=='obstacle']; e.close()
           7 +data=json.load(open('probe_vis_d1.json'))['data']
           8 +for f in glob.glob('probe_vis_j_*_0.75.json')+glob.glob('probe_vis_n_*.json'): data+=json.load(open(f))
           9 +HOLES=[(73.5,80),(52.5,58),(-53.5,-48),(-77.5,-70)]
          10 +def rel(x,y,th):
          11 +    r=math.degrees(math.atan2(obj[1]-y,obj[0]-x)-th); return (r+180)%360-180
          12 +def vis(x,y,th,a,b,infl,thr=97.5,holes=True):
          13 +    r=rel(x,y,th)
          14 +    if abs(r)>thr: return True
          15 +    if holes and any(lo<=r<=hi for lo,hi in HOLES): return True
          16 +    cx=x+a*math.cos(th)-b*math.sin(th); cy=y+a*math.sin(th)+b*math.cos(th)
          17 +    for (px,py,pz,hx,hy,hz) in obs:
          18 +        if abs(px-obj[0])<=hx and abs(py-obj[1])<=hy: continue
          19 +        if seg_box_hit((cx,cy),obj,(px-hx-infl,py-hy-infl),(px+hx+infl,py+hy+infl)): return False
          20 +    return True
          21 +print(len(data))
          22 +res=[]
          23 +for a in np.arange(-0.16,0.061,0.02):
          24 +    for b in np.arange(-0.06,0.061,0.02):
          25 +        for infl in [0,0.01,0.02,0.03]:
          26 +            res.append((sum(vis(x,y,th,a,b,infl)!=bool(c) for x,y,th,c in data),round(a,3),round(b,3),infl))
          27 +res.sort(); print(res[:8])
          28 +m,a,b,infl=res[0]
          29 +mm=[(round(math.degrees(th)),round(x,3),round(y,3),round(rel(x,y,th),1),c) for x,y,th,c in data if vis(x,y,th,a,b,infl)!=bool(c)]
          30 +print(mm[:60])
diff --git a/probe_vis_k.py b/probe_vis_k.py
new file mode 100644
index 0000000..f53d969
--- /dev/null
+++ b/probe_vis_k.py
@@ -0,0 +1,17 @@
           1 +from probe_vis_lib import *
           2 +def flags(e): return {k:(int(v['have_image_rover0']),int(v['have_image_rover1'])) for k,v in e.objs().items()}
           3 +e=E(0)
           4 +print(e.path(0,[(1.0,0.0),(1.3,1.4)]), e.rs(0)['x'],e.rs(0)['y'])
           5 +for k,v in e.objs().items(): print(k, round(math.hypot(v['x']-1.3,v['y']-1.4),3))
           6 +print('img w/o cal:', e.step(0,0,0,0,'img'), e.rs(0)['calibrated'], flags(e))
           7 +e.step(0,0,0,0,'cal'); print('cal',e.rs(0)['calibrated'])
           8 +for i in range(3): e.step(0,0,0,0,'noop')
           9 +print('after 3 noops cal=',e.rs(0)['calibrated'])
          10 +e.step(0,0.2,0,0,'noop'); e.step(0,-0.2,0,0,'noop'); e.step(0,0,0,0.4,'noop')
          11 +print('after moves cal=',e.rs(0)['calibrated'])
          12 +r=e.step(0,0,0,0,'img'); print('img rew',r,flags(e),'cal',e.rs(0)['calibrated'])
          13 +r=e.step(0,0.1,0,0,'cal'); print('cal+move: pos',round(e.rs(0)['x'],3),'cal',e.rs(0)['calibrated'])
          14 +r=e.step(0,-0.1,0,0,'img'); print('img+move: pos',round(e.rs(0)['x'],3),'cal',e.rs(0)['calibrated'],flags(e),r)
          15 +r=e.step(0,0,0,0,'cal'); print('cal when all imaged by r0: cal',e.rs(0)['calibrated'])
          16 +r=e.step(0,0,0,0,'img'); print('img again',flags(e),'cal',e.rs(0)['calibrated'],r)
          17 +# rover1 calibrate while rover0 acts
diff --git a/probe_vis_l.py b/probe_vis_l.py
new file mode 100644
index 0000000..e962e3b
--- /dev/null
+++ b/probe_vis_l.py
@@ -0,0 +1,18 @@
           1 +from probe_vis_lib import *
           2 +def flags(e): return {k:(int(v['have_image_rover0']),int(v['have_image_rover1'])) for k,v in e.objs().items()}
           3 +# pre/post motion evaluation at range boundary (seed1, theta=pi, y*=-0.0852)
           4 +for sel,y0,dy in [('cal',-0.05,-0.1),('cal',-0.15,0.1)]:
           5 +    e=E(1); e.path(0,[(1.0,0.0),(2.118,0.0),(2.118,y0)])
           6 +    e.step(0,0,0,0,sel if False else 'noop')
           7 +    e.step(0,0,dy,0,sel); print(sel,'from y',y0,'to',round(e.rs(0)['y'],3),'cal=',e.rs(0)['calibrated']); e.close()
           8 +# image: calibrate at visible spot then move out of range then image
           9 +e=E(1); e.path(0,[(1.0,0.0),(2.118,0.0)]); e.step(0,0,0,0,'cal'); print('cal at y=0:',e.rs(0)['calibrated'])
          10 +e.goto(0,2.118,-0.3); r=e.step(0,0,0,0,'img'); print('img out of range',flags(e),e.rs(0)['calibrated'],r); e.close()
          11 +# image with move crossing boundary
          12 +for y0,dy in [(-0.05,-0.1),(-0.15,0.1)]:
          13 +    e=E(1); e.path(0,[(1.0,0.0),(2.118,0.0)]); e.step(0,0,0,0,'cal'); e.goto(0,2.118,y0)
          14 +    e.step(0,0,dy,0,'img'); print('img move from',y0,'to',round(e.rs(0)['y'],3),flags(e),e.rs(0)['calibrated']); e.close()
          15 +# nearest choice
          16 +e=E(0); e.path(0,[(1.0,0.0),(1.9,0.0),(1.9,1.5)])
          17 +for k,v in e.objs().items(): print(k, round(math.hypot(v['x']-1.9,v['y']-1.5),3))
          18 +e.step(0,0,0,0,'cal'); e.step(0,0,0,0,'img'); print('nearest test',flags(e))
diff --git a/probe_vis_m.py b/probe_vis_m.py
new file mode 100644
index 0000000..54d6329
--- /dev/null
+++ b/probe_vis_m.py
@@ -0,0 +1,8 @@
           1 +from probe_vis_lib import *
           2 +def flags(e): return {k:(int(v['have_image_rover0']),int(v['have_image_rover1'])) for k,v in e.objs().items()}
           3 +for th in [2.3,-0.84,0.0,math.pi]:
           4 +  for pos in [(0.25,1.2),(0.25,1.45)]:
           5 +    e=E(5); ok=e.path(0,[(0.25,-1.75),pos]); e.turn(0,th)
           6 +    ds={k:round(math.hypot(v['x']-pos[0],v['y']-pos[1]),2) for k,v in e.objs().items()}
           7 +    e.step(0,0,0,0,'cal'); c=e.rs(0)['calibrated']; e.step(0,0,0,0,'img')
           8 +    print('th',th,'pos',pos,ok,'cal',c,flags(e),ds); e.close()
diff --git a/probe_vis_n.py b/probe_vis_n.py
new file mode 100644
index 0000000..2d55f2b
--- /dev/null
+++ b/probe_vis_n.py
@@ -0,0 +1,18 @@
           1 +from probe_vis_lib import *
           2 +import sys, json
           3 +e=E(4)
           4 +x,y=float(sys.argv[1]),float(sys.argv[2]); N=int(sys.argv[3])
           5 +e.path(1,[(-1.0,-1.0),(-1.0,y),(x,y)])
           6 +res=[]
           7 +for k in range(N):
           8 +    th=-math.pi+k*2*math.pi/N
           9 +    e.turn(1,th); st=e.rs(1)
          10 +    e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img')
          11 +    res.append((st['x'],st['y'],st['theta'],int(c)))
          12 +json.dump(res,open('probe_vis_n_%s_%s.json'%(sys.argv[1],sys.argv[2]),'w'))
          13 +s=''.join(str(r[3]) for r in res)
          14 +# print runs
          15 +runs=[];cur=s[0];start=0
          16 +for i,ch in enumerate(s[1:]+'x',1):
          17 +    if ch!=cur: runs.append((cur,round(math.degrees(res[start][2]),1),round(math.degrees(res[i-1][2]),1))); cur=ch; start=i
          18 +print(x,y,runs)
diff --git a/probe_vis_n_-1.85_0.75.json b/probe_vis_n_-1.85_0.75.json
new file mode 100644
index 0000000..c687d7a
--- /dev/null
+++ b/probe_vis_n_-1.85_0.75.json
@@ -0,0 +1 @@
           1 +[[-1.850000023841858, 0.75, 3.141592502593994, 1], [-1.850000023841858, 0.75, -3.1241393089294434, 1], [-1.850000023841858, 0.75, -3.1066861152648926, 1], [-1.850000023841858, 0.75, -3.0892326831817627, 1], [-1.850000023841858, 0.75, -3.071779489517212, 1], [-1.850000023841858, 0.75, -3.054326295852661, 1], [-1.850000023841858, 0.75, -3.0368728637695312, 1], [-1.850000023841858, 0.75, -3.0194194316864014, 1], [-1.850000023841858, 0.75, -3.0019664764404297, 1], [-1.850000023841858, 0.75, -2.9845130443573, 1], [-1.850000023841858, 0.75, -2.96705961227417, 1], [-1.850000023841858, 0.75, -2.949606418609619, 1], [-1.850000023841858, 0.75, -2.9321532249450684, 1], [-1.850000023841858, 0.75, -2.9146997928619385, 1], [-1.850000023841858, 0.75, -2.8972465991973877, 1], [-1.850000023841858, 0.75, -2.879793167114258, 1], [-1.850000023841858, 0.75, -2.862339973449707, 1], [-1.850000023841858, 0.75, -2.8448867797851562, 1], [-1.850000023841858, 0.75, -2.8274333477020264, 1], [-1.850000023841858, 0.75, -2.8099801540374756, 1], [-1.850000023841858, 0.75, -2.7925267219543457, 1], [-1.850000023841858, 0.75, -2.775073528289795, 1], [-1.850000023841858, 0.75, -2.757620334625244, 1], [-1.850000023841858, 0.75, -2.7401669025421143, 1], [-1.850000023841858, 0.75, -2.7227134704589844, 1], [-1.850000023841858, 0.75, -2.7052605152130127, 1], [-1.850000023841858, 0.75, -2.6878068447113037, 1], [-1.850000023841858, 0.75, -2.670353889465332, 1], [-1.850000023841858, 0.75, -2.652900457382202, 1], [-1.850000023841858, 0.75, -2.6354472637176514, 1], [-1.850000023841858, 0.75, -2.6179938316345215, 1], [-1.850000023841858, 0.75, -2.6005406379699707, 1], [-1.850000023841858, 0.75, -2.583087205886841, 1], [-1.850000023841858, 0.75, -2.56563401222229, 1], [-1.850000023841858, 0.75, -2.54818058013916, 1], [-1.850000023841858, 0.75, -2.5307276248931885, 1], [-1.850000023841858, 0.75, -2.5132739543914795, 1], [-1.850000023841858, 0.75, -2.495820999145508, 1], [-1.850000023841858, 0.75, -2.478367328643799, 1], [-1.850000023841858, 0.75, -2.460914373397827, 1], [-1.850000023841858, 0.75, -2.4434609413146973, 1], [-1.850000023841858, 0.75, -2.4260077476501465, 1], [-1.850000023841858, 0.75, -2.4085543155670166, 1], [-1.850000023841858, 0.75, -2.391101121902466, 1], [-1.850000023841858, 0.75, -2.373647689819336, 1], [-1.850000023841858, 0.75, -2.356194496154785, 1], [-1.850000023841858, 0.75, -2.3387410640716553, 1], [-1.850000023841858, 0.75, -2.3212881088256836, 1], [-1.850000023841858, 0.75, -2.3038344383239746, 1], [-1.850000023841858, 0.75, -2.286381483078003, 1], [-1.850000023841858, 0.75, -2.268928050994873, 1], [-1.850000023841858, 0.75, -2.251474618911743, 1], [-1.850000023841858, 0.75, -2.2340214252471924, 1], [-1.850000023841858, 0.75, -2.2165682315826416, 1], [-1.850000023841858, 0.75, -2.1991147994995117, 1], [-1.850000023841858, 0.75, -2.181661605834961, 1], [-1.850000023841858, 0.75, -2.164208173751831, 1], [-1.850000023841858, 0.75, -2.1467549800872803, 1], [-1.850000023841858, 0.75, -2.1293017864227295, 1], [-1.850000023841858, 0.75, -2.1118483543395996, 1], [-1.850000023841858, 0.75, -2.094395160675049, 1], [-1.850000023841858, 0.75, -2.076941728591919, 1], [-1.850000023841858, 0.75, -2.059488534927368, 1], [-1.850000023841858, 0.75, -2.0420353412628174, 1], [-1.850000023841858, 0.75, -2.0245819091796875, 1], [-1.850000023841858, 0.75, -2.0071284770965576, 1], [-1.850000023841858, 0.75, -1.9896754026412964, 1], [-1.850000023841858, 0.75, -1.972222089767456, 1], [-1.850000023841858, 0.75, -1.9547687768936157, 1], [-1.850000023841858, 0.75, -1.9373154640197754, 1], [-1.850000023841858, 0.75, -1.919862151145935, 1], [-1.850000023841858, 0.75, -1.9024088382720947, 1], [-1.850000023841858, 0.75, -1.884955644607544, 1], [-1.850000023841858, 0.75, -1.8675023317337036, 1], [-1.850000023841858, 0.75, -1.8500490188598633, 1], [-1.850000023841858, 0.75, -1.832595705986023, 1], [-1.850000023841858, 0.75, -1.8151423931121826, 1], [-1.850000023841858, 0.75, -1.7976890802383423, 1], [-1.850000023841858, 0.75, -1.7802358865737915, 1], [-1.850000023841858, 0.75, -1.7627825736999512, 1], [-1.850000023841858, 0.75, -1.7453292608261108, 1], [-1.850000023841858, 0.75, -1.7278759479522705, 1], [-1.850000023841858, 0.75, -1.7104226350784302, 1], [-1.850000023841858, 0.75, -1.6929693222045898, 1], [-1.850000023841858, 0.75, -1.675516128540039, 1], [-1.850000023841858, 0.75, -1.6580628156661987, 1], [-1.850000023841858, 0.75, -1.6406095027923584, 1], [-1.850000023841858, 0.75, -1.623156189918518, 1], [-1.850000023841858, 0.75, -1.6057028770446777, 1], [-1.850000023841858, 0.75, -1.588249683380127, 1], [-1.850000023841858, 0.75, -1.570796251296997, 1], [-1.850000023841858, 0.75, -1.5533430576324463, 1], [-1.850000023841858, 0.75, -1.535889744758606, 1], [-1.850000023841858, 0.75, -1.5184364318847656, 1], [-1.850000023841858, 0.75, -1.5009832382202148, 1], [-1.850000023841858, 0.75, -1.483529806137085, 1], [-1.850000023841858, 0.75, -1.4660766124725342, 1], [-1.850000023841858, 0.75, -1.4486232995986938, 1], [-1.850000023841858, 0.75, -1.4311699867248535, 1], [-1.850000023841858, 0.75, -1.4137166738510132, 1], [-1.850000023841858, 0.75, -1.3962633609771729, 1], [-1.850000023841858, 0.75, -1.378810167312622, 1], [-1.850000023841858, 0.75, -1.3613567352294922, 1], [-1.850000023841858, 0.75, -1.3439035415649414, 1], [-1.850000023841858, 0.75, -1.326450228691101, 1], [-1.850000023841858, 0.75, -1.3089969158172607, 1], [-1.850000023841858, 0.75, -1.29154372215271, 1], [-1.850000023841858, 0.75, -1.27409029006958, 1], [-1.850000023841858, 0.75, -1.2566370964050293, 1], [-1.850000023841858, 0.75, -1.239183783531189, 1], [-1.850000023841858, 0.75, -1.2217304706573486, 1], [-1.850000023841858, 0.75, -1.2042771577835083, 1], [-1.850000023841858, 0.75, -1.186823844909668, 1], [-1.850000023841858, 0.75, -1.1693706512451172, 1], [-1.850000023841858, 0.75, -1.1519173383712769, 1], [-1.850000023841858, 0.75, -1.1344640254974365, 1], [-1.850000023841858, 0.75, -1.1170107126235962, 1], [-1.850000023841858, 0.75, -1.0995573997497559, 1], [-1.850000023841858, 0.75, -1.0821040868759155, 1], [-1.850000023841858, 0.75, -1.0646508932113647, 1], [-1.850000023841858, 0.75, -1.0471975803375244, 1], [-1.850000023841858, 0.75, -1.029744267463684, 1], [-1.850000023841858, 0.75, -1.0122909545898438, 1], [-1.850000023841858, 0.75, -0.9948376417160034, 1], [-1.850000023841858, 0.75, -0.9773843884468079, 1], [-1.850000023841858, 0.75, -0.9599310755729675, 1], [-1.850000023841858, 0.75, -0.942477822303772, 1], [-1.850000023841858, 0.75, -0.9250245094299316, 1], [-1.850000023841858, 0.75, -0.9075711965560913, 1], [-1.850000023841858, 0.75, -0.890117883682251, 1], [-1.850000023841858, 0.75, -0.8726646304130554, 1], [-1.850000023841858, 0.75, -0.8552113771438599, 1], [-1.850000023841858, 0.75, -0.8377580046653748, 1], [-1.850000023841858, 0.75, -0.8203047513961792, 1], [-1.850000023841858, 0.75, -0.8028514385223389, 1], [-1.850000023841858, 0.75, -0.7853981852531433, 1], [-1.850000023841858, 0.75, -0.767944872379303, 1], [-1.850000023841858, 0.75, -0.7504915595054626, 1], [-1.850000023841858, 0.75, -0.7330383062362671, 1], [-1.850000023841858, 0.75, -0.7155849933624268, 1], [-1.850000023841858, 0.75, -0.6981316804885864, 1], [-1.850000023841858, 0.75, -0.6806784272193909, 1], [-1.850000023841858, 0.75, -0.6632251143455505, 1], [-1.850000023841858, 0.75, -0.6457718014717102, 1], [-1.850000023841858, 0.75, -0.6283185482025146, 1], [-1.850000023841858, 0.75, -0.6108652353286743, 1], [-1.850000023841858, 0.75, -0.5934119820594788, 1], [-1.850000023841858, 0.75, -0.5759586095809937, 1], [-1.850000023841858, 0.75, -0.5585053563117981, 1], [-1.850000023841858, 0.75, -0.5410521030426025, 1], [-1.850000023841858, 0.75, -0.5235987901687622, 1], [-1.850000023841858, 0.75, -0.5061454772949219, 1], [-1.850000023841858, 0.75, -0.48869216442108154, 1], [-1.850000023841858, 0.75, -0.471238911151886, 1], [-1.850000023841858, 0.75, -0.45378559827804565, 1], [-1.850000023841858, 0.75, -0.4363323152065277, 1], [-1.850000023841858, 0.75, -0.4188790023326874, 1], [-1.850000023841858, 0.75, -0.4014257490634918, 1], [-1.850000023841858, 0.75, -0.3839724361896515, 1], [-1.850000023841858, 0.75, -0.36651912331581116, 1], [-1.850000023841858, 0.75, -0.3490658700466156, 1], [-1.850000023841858, 0.75, -0.33161255717277527, 1], [-1.850000023841858, 0.75, -0.31415924429893494, 1], [-1.850000023841858, 0.75, -0.2967059910297394, 1], [-1.850000023841858, 0.75, -0.27925267815589905, 1], [-1.850000023841858, 0.75, -0.2617993950843811, 1], [-1.850000023841858, 0.75, -0.24434608221054077, 1], [-1.850000023841858, 0.75, -0.22689279913902283, 1], [-1.850000023841858, 0.75, -0.20943951606750488, 1], [-1.850000023841858, 0.75, -0.19198621809482574, 1], [-1.850000023841858, 0.75, -0.1745329201221466, 0], [-1.850000023841858, 0.75, -0.15707963705062866, 0], [-1.850000023841858, 0.75, -0.13962633907794952, 0], [-1.850000023841858, 0.75, -0.12217305600643158, 0], [-1.850000023841858, 0.75, -0.10471975058317184, 0], [-1.850000023841858, 0.75, -0.0872664600610733, 0], [-1.850000023841858, 0.75, -0.06981316953897476, 0], [-1.850000023841858, 0.75, -0.05235987901687622, 0], [-1.850000023841858, 0.75, -0.03490658476948738, 0], [-1.850000023841858, 0.75, -0.01745329424738884, 0], [-1.850000023841858, 0.75, 7.450591255064865e-10, 0], [-1.850000023841858, 0.75, 0.01745329238474369, 0], [-1.850000023841858, 0.75, 0.03490658476948738, 0], [-1.850000023841858, 0.75, 0.05235987901687622, 0], [-1.850000023841858, 0.75, 0.06981316953897476, 0], [-1.850000023841858, 0.75, 0.0872664600610733, 0], [-1.850000023841858, 0.75, 0.10471975803375244, 0], [-1.850000023841858, 0.75, 0.12217304855585098, 0], [-1.850000023841858, 0.75, 0.13962633907794952, 1], [-1.850000023841858, 0.75, 0.15707963705062866, 1], [-1.850000023841858, 0.75, 0.1745329201221466, 1], [-1.850000023841858, 0.75, 0.19198621809482574, 1], [-1.850000023841858, 0.75, 0.20943951606750488, 1], [-1.850000023841858, 0.75, 0.22689279913902283, 1], [-1.850000023841858, 0.75, 0.24434609711170197, 0], [-1.850000023841858, 0.75, 0.2617993950843811, 0], [-1.850000023841858, 0.75, 0.27925267815589905, 0], [-1.850000023841858, 0.75, 0.296705961227417, 0], [-1.850000023841858, 0.75, 0.3141592741012573, 0], [-1.850000023841858, 0.75, 0.33161255717277527, 0], [-1.850000023841858, 0.75, 0.3490658402442932, 0], [-1.850000023841858, 0.75, 0.36651915311813354, 0], [-1.850000023841858, 0.75, 0.3839724361896515, 0], [-1.850000023841858, 0.75, 0.40142571926116943, 0], [-1.850000023841858, 0.75, 0.41887903213500977, 0], [-1.850000023841858, 0.75, 0.4363323152065277, 0], [-1.850000023841858, 0.75, 0.45378559827804565, 0], [-1.850000023841858, 0.75, 0.4712388813495636, 0], [-1.850000023841858, 0.75, 0.48869219422340393, 0], [-1.850000023841858, 0.75, 0.5061454772949219, 0], [-1.850000023841858, 0.75, 0.5235987901687622, 1], [-1.850000023841858, 0.75, 0.5410520434379578, 1], [-1.850000023841858, 0.75, 0.5585053563117981, 1], [-1.850000023841858, 0.75, 0.5759586691856384, 1], [-1.850000023841858, 0.75, 0.5934119820594788, 1], [-1.850000023841858, 0.75, 0.6108652353286743, 0], [-1.850000023841858, 0.75, 0.6283184885978699, 0], [-1.850000023841858, 0.75, 0.645771861076355, 0], [-1.850000023841858, 0.75, 0.6632251143455505, 0], [-1.850000023841858, 0.75, 0.6806783676147461, 0], [-1.850000023841858, 0.75, 0.6981317400932312, 0], [-1.850000023841858, 0.75, 0.7155849933624268, 0], [-1.850000023841858, 0.75, 0.7330382466316223, 0], [-1.850000023841858, 0.75, 0.7504916191101074, 0], [-1.850000023841858, 0.75, 0.767944872379303, 0], [-1.850000023841858, 0.75, 0.7853981256484985, 0], [-1.850000023841858, 0.75, 0.8028514981269836, 0], [-1.850000023841858, 0.75, 0.8203047513961792, 1], [-1.850000023841858, 0.75, 0.8377580046653748, 1], [-1.850000023841858, 0.75, 0.8552113175392151, 1], [-1.850000023841858, 0.75, 0.8726646304130554, 1], [-1.850000023841858, 0.75, 0.8901179432868958, 1], [-1.850000023841858, 0.75, 0.9075711965560913, 1], [-1.850000023841858, 0.75, 0.9250245094299316, 1], [-1.850000023841858, 0.75, 0.942477822303772, 1], [-1.850000023841858, 0.75, 0.9599310755729675, 1], [-1.850000023841858, 0.75, 0.9773843884468079, 1], [-1.850000023841858, 0.75, 0.9948376417160034, 1], [-1.850000023841858, 0.75, 1.0122909545898438, 1], [-1.850000023841858, 0.75, 1.029744267463684, 1], [-1.850000023841858, 0.75, 1.0471975803375244, 1], [-1.850000023841858, 0.75, 1.0646508932113647, 1], [-1.850000023841858, 0.75, 1.0821040868759155, 1], [-1.850000023841858, 0.75, 1.0995573997497559, 1], [-1.850000023841858, 0.75, 1.1170107126235962, 1], [-1.850000023841858, 0.75, 1.1344640254974365, 1], [-1.850000023841858, 0.75, 1.1519173383712769, 1], [-1.850000023841858, 0.75, 1.1693705320358276, 1], [-1.850000023841858, 0.75, 1.1868239641189575, 1], [-1.850000023841858, 0.75, 1.2042771577835083, 1], [-1.850000023841858, 0.75, 1.2217304706573486, 1], [-1.850000023841858, 0.75, 1.239183783531189, 1], [-1.850000023841858, 0.75, 1.2566370964050293, 1], [-1.850000023841858, 0.75, 1.27409029006958, 1], [-1.850000023841858, 0.75, 1.29154372215271, 1], [-1.850000023841858, 0.75, 1.3089969158172607, 1], [-1.850000023841858, 0.75, 1.326450228691101, 1], [-1.850000023841858, 0.75, 1.3439035415649414, 1], [-1.850000023841858, 0.75, 1.3613567352294922, 1], [-1.850000023841858, 0.75, 1.378810167312622, 1], [-1.850000023841858, 0.75, 1.3962633609771729, 1], [-1.850000023841858, 0.75, 1.4137166738510132, 1], [-1.850000023841858, 0.75, 1.4311699867248535, 1], [-1.850000023841858, 0.75, 1.4486232995986938, 1], [-1.850000023841858, 0.75, 1.4660766124725342, 1], [-1.850000023841858, 0.75, 1.483529806137085, 1], [-1.850000023841858, 0.75, 1.5009832382202148, 1], [-1.850000023841858, 0.75, 1.5184364318847656, 1], [-1.850000023841858, 0.75, 1.535889744758606, 1], [-1.850000023841858, 0.75, 1.5533430576324463, 1], [-1.850000023841858, 0.75, 1.570796251296997, 1], [-1.850000023841858, 0.75, 1.588249683380127, 1], [-1.850000023841858, 0.75, 1.6057028770446777, 1], [-1.850000023841858, 0.75, 1.623156189918518, 1], [-1.850000023841858, 0.75, 1.6406095027923584, 1], [-1.850000023841858, 0.75, 1.6580628156661987, 1], [-1.850000023841858, 0.75, 1.6755160093307495, 1], [-1.850000023841858, 0.75, 1.6929694414138794, 1], [-1.850000023841858, 0.75, 1.7104226350784302, 1], [-1.850000023841858, 0.75, 1.7278759479522705, 1], [-1.850000023841858, 0.75, 1.7453292608261108, 1], [-1.850000023841858, 0.75, 1.7627825736999512, 1], [-1.850000023841858, 0.75, 1.780235767364502, 1], [-1.850000023841858, 0.75, 1.7976891994476318, 1], [-1.850000023841858, 0.75, 1.8151423931121826, 1], [-1.850000023841858, 0.75, 1.832595705986023, 1], [-1.850000023841858, 0.75, 1.8500490188598633, 1], [-1.850000023841858, 0.75, 1.8675023317337036, 1], [-1.850000023841858, 0.75, 1.8849555253982544, 1], [-1.850000023841858, 0.75, 1.9024089574813843, 1], [-1.850000023841858, 0.75, 1.919862151145935, 1], [-1.850000023841858, 0.75, 1.9373154640197754, 1], [-1.850000023841858, 0.75, 1.9547687768936157, 1], [-1.850000023841858, 0.75, 1.972222089767456, 1], [-1.850000023841858, 0.75, 1.9896752834320068, 1], [-1.850000023841858, 0.75, 2.0071287155151367, 1], [-1.850000023841858, 0.75, 2.0245819091796875, 1], [-1.850000023841858, 0.75, 2.0420351028442383, 1], [-1.850000023841858, 0.75, 2.059488534927368, 1], [-1.850000023841858, 0.75, 2.076941967010498, 1], [-1.850000023841858, 0.75, 2.0943949222564697, 1], [-1.850000023841858, 0.75, 2.1118485927581787, 1], [-1.850000023841858, 0.75, 2.1293015480041504, 1], [-1.850000023841858, 0.75, 2.1467549800872803, 1], [-1.850000023841858, 0.75, 2.16420841217041, 1], [-1.850000023841858, 0.75, 2.181661367416382, 1], [-1.850000023841858, 0.75, 2.199115037918091, 1], [-1.850000023841858, 0.75, 2.2165679931640625, 1], [-1.850000023841858, 0.75, 2.2340214252471924, 1], [-1.850000023841858, 0.75, 2.2514748573303223, 1], [-1.850000023841858, 0.75, 2.268928050994873, 1], [-1.850000023841858, 0.75, 2.286381244659424, 1], [-1.850000023841858, 0.75, 2.3038346767425537, 1], [-1.850000023841858, 0.75, 2.3212878704071045, 1], [-1.850000023841858, 0.75, 2.3387413024902344, 1], [-1.850000023841858, 0.75, 2.356194496154785, 1], [-1.850000023841858, 0.75, 2.373647689819336, 1], [-1.850000023841858, 0.75, 2.391101121902466, 1], [-1.850000023841858, 0.75, 2.4085543155670166, 1], [-1.850000023841858, 0.75, 2.4260077476501465, 1], [-1.850000023841858, 0.75, 2.4434609413146973, 1], [-1.850000023841858, 0.75, 2.460914134979248, 1], [-1.850000023841858, 0.75, 2.478367567062378, 1], [-1.850000023841858, 0.75, 2.4958207607269287, 1], [-1.850000023841858, 0.75, 2.5132741928100586, 1], [-1.850000023841858, 0.75, 2.5307273864746094, 1], [-1.850000023841858, 0.75, 2.5481808185577393, 1], [-1.850000023841858, 0.75, 2.56563401222229, 1], [-1.850000023841858, 0.75, 2.583087205886841, 1], [-1.850000023841858, 0.75, 2.6005406379699707, 1], [-1.850000023841858, 0.75, 2.6179938316345215, 1], [-1.850000023841858, 0.75, 2.6354470252990723, 1], [-1.850000023841858, 0.75, 2.6529006958007812, 1], [-1.850000023841858, 0.75, 2.670353651046753, 1], [-1.850000023841858, 0.75, 2.687807083129883, 1], [-1.850000023841858, 0.75, 2.7052602767944336, 1], [-1.850000023841858, 0.75, 2.7227137088775635, 1], [-1.850000023841858, 0.75, 2.7401669025421143, 1], [-1.850000023841858, 0.75, 2.757620096206665, 1], [-1.850000023841858, 0.75, 2.775073528289795, 1], [-1.850000023841858, 0.75, 2.792526960372925, 1], [-1.850000023841858, 0.75, 2.8099799156188965, 1], [-1.850000023841858, 0.75, 2.8274335861206055, 1], [-1.850000023841858, 0.75, 2.844886541366577, 1], [-1.850000023841858, 0.75, 2.862339973449707, 1], [-1.850000023841858, 0.75, 2.879793405532837, 1], [-1.850000023841858, 0.75, 2.8972463607788086, 1], [-1.850000023841858, 0.75, 2.9147000312805176, 1], [-1.850000023841858, 0.75, 2.9321529865264893, 1], [-1.850000023841858, 0.75, 2.949606418609619, 1], [-1.850000023841858, 0.75, 2.967059850692749, 1], [-1.850000023841858, 0.75, 2.9845130443573, 1], [-1.850000023841858, 0.75, 3.0019662380218506, 1], [-1.850000023841858, 0.75, 3.0194196701049805, 1], [-1.850000023841858, 0.75, 3.0368728637695312, 1], [-1.850000023841858, 0.75, 3.054326057434082, 1], [-1.850000023841858, 0.75, 3.071779489517212, 1], [-1.850000023841858, 0.75, 3.089232921600342, 1], [-1.850000023841858, 0.75, 3.1066861152648926, 1], [-1.850000023841858, 0.75, 3.1241393089294434, 1]]
\ No newline at end of file
diff --git a/probe_vis_n_-2.0_0.75.json b/probe_vis_n_-2.0_0.75.json
new file mode 100644
index 0000000..0249b9a
--- /dev/null
+++ b/probe_vis_n_-2.0_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.0, 0.75, 3.141592502593994, 1], [-2.0, 0.75, -3.1241393089294434, 1], [-2.0, 0.75, -3.1066861152648926, 1], [-2.0, 0.75, -3.0892326831817627, 1], [-2.0, 0.75, -3.071779489517212, 1], [-2.0, 0.75, -3.054326295852661, 1], [-2.0, 0.75, -3.0368728637695312, 1], [-2.0, 0.75, -3.0194194316864014, 1], [-2.0, 0.75, -3.0019664764404297, 1], [-2.0, 0.75, -2.9845130443573, 1], [-2.0, 0.75, -2.96705961227417, 1], [-2.0, 0.75, -2.949606418609619, 1], [-2.0, 0.75, -2.9321532249450684, 1], [-2.0, 0.75, -2.9146997928619385, 1], [-2.0, 0.75, -2.8972465991973877, 1], [-2.0, 0.75, -2.879793167114258, 1], [-2.0, 0.75, -2.862339973449707, 1], [-2.0, 0.75, -2.8448867797851562, 1], [-2.0, 0.75, -2.8274333477020264, 1], [-2.0, 0.75, -2.8099801540374756, 1], [-2.0, 0.75, -2.7925267219543457, 1], [-2.0, 0.75, -2.775073528289795, 1], [-2.0, 0.75, -2.757620334625244, 1], [-2.0, 0.75, -2.7401669025421143, 1], [-2.0, 0.75, -2.7227134704589844, 1], [-2.0, 0.75, -2.7052605152130127, 1], [-2.0, 0.75, -2.6878068447113037, 1], [-2.0, 0.75, -2.670353889465332, 1], [-2.0, 0.75, -2.652900457382202, 1], [-2.0, 0.75, -2.6354472637176514, 1], [-2.0, 0.75, -2.6179938316345215, 1], [-2.0, 0.75, -2.6005406379699707, 1], [-2.0, 0.75, -2.583087205886841, 1], [-2.0, 0.75, -2.56563401222229, 1], [-2.0, 0.75, -2.54818058013916, 1], [-2.0, 0.75, -2.5307276248931885, 1], [-2.0, 0.75, -2.5132739543914795, 1], [-2.0, 0.75, -2.495820999145508, 1], [-2.0, 0.75, -2.478367328643799, 1], [-2.0, 0.75, -2.460914373397827, 1], [-2.0, 0.75, -2.4434609413146973, 1], [-2.0, 0.75, -2.4260077476501465, 1], [-2.0, 0.75, -2.4085543155670166, 1], [-2.0, 0.75, -2.391101121902466, 1], [-2.0, 0.75, -2.373647689819336, 1], [-2.0, 0.75, -2.356194496154785, 1], [-2.0, 0.75, -2.3387410640716553, 1], [-2.0, 0.75, -2.3212881088256836, 1], [-2.0, 0.75, -2.3038344383239746, 1], [-2.0, 0.75, -2.286381483078003, 1], [-2.0, 0.75, -2.268928050994873, 1], [-2.0, 0.75, -2.251474618911743, 1], [-2.0, 0.75, -2.2340214252471924, 1], [-2.0, 0.75, -2.2165682315826416, 1], [-2.0, 0.75, -2.1991147994995117, 1], [-2.0, 0.75, -2.181661605834961, 1], [-2.0, 0.75, -2.164208173751831, 1], [-2.0, 0.75, -2.1467549800872803, 1], [-2.0, 0.75, -2.1293017864227295, 1], [-2.0, 0.75, -2.1118483543395996, 1], [-2.0, 0.75, -2.094395160675049, 1], [-2.0, 0.75, -2.076941728591919, 1], [-2.0, 0.75, -2.059488534927368, 1], [-2.0, 0.75, -2.0420353412628174, 1], [-2.0, 0.75, -2.0245819091796875, 1], [-2.0, 0.75, -2.0071284770965576, 1], [-2.0, 0.75, -1.9896754026412964, 1], [-2.0, 0.75, -1.972222089767456, 1], [-2.0, 0.75, -1.9547687768936157, 1], [-2.0, 0.75, -1.9373154640197754, 1], [-2.0, 0.75, -1.919862151145935, 1], [-2.0, 0.75, -1.9024088382720947, 1], [-2.0, 0.75, -1.884955644607544, 1], [-2.0, 0.75, -1.8675023317337036, 1], [-2.0, 0.75, -1.8500490188598633, 1], [-2.0, 0.75, -1.832595705986023, 1], [-2.0, 0.75, -1.8151423931121826, 1], [-2.0, 0.75, -1.7976890802383423, 1], [-2.0, 0.75, -1.7802358865737915, 1], [-2.0, 0.75, -1.7627825736999512, 1], [-2.0, 0.75, -1.7453292608261108, 1], [-2.0, 0.75, -1.7278759479522705, 1], [-2.0, 0.75, -1.7104226350784302, 1], [-2.0, 0.75, -1.6929693222045898, 1], [-2.0, 0.75, -1.675516128540039, 1], [-2.0, 0.75, -1.6580628156661987, 1], [-2.0, 0.75, -1.6406095027923584, 1], [-2.0, 0.75, -1.623156189918518, 1], [-2.0, 0.75, -1.6057028770446777, 1], [-2.0, 0.75, -1.588249683380127, 1], [-2.0, 0.75, -1.570796251296997, 1], [-2.0, 0.75, -1.5533430576324463, 1], [-2.0, 0.75, -1.535889744758606, 1], [-2.0, 0.75, -1.5184364318847656, 1], [-2.0, 0.75, -1.5009832382202148, 1], [-2.0, 0.75, -1.483529806137085, 1], [-2.0, 0.75, -1.4660766124725342, 1], [-2.0, 0.75, -1.4486232995986938, 1], [-2.0, 0.75, -1.4311699867248535, 1], [-2.0, 0.75, -1.4137166738510132, 1], [-2.0, 0.75, -1.3962633609771729, 1], [-2.0, 0.75, -1.378810167312622, 1], [-2.0, 0.75, -1.3613567352294922, 1], [-2.0, 0.75, -1.3439035415649414, 1], [-2.0, 0.75, -1.326450228691101, 1], [-2.0, 0.75, -1.3089969158172607, 1], [-2.0, 0.75, -1.29154372215271, 1], [-2.0, 0.75, -1.27409029006958, 1], [-2.0, 0.75, -1.2566370964050293, 1], [-2.0, 0.75, -1.239183783531189, 1], [-2.0, 0.75, -1.2217304706573486, 1], [-2.0, 0.75, -1.2042771577835083, 1], [-2.0, 0.75, -1.186823844909668, 1], [-2.0, 0.75, -1.1693706512451172, 1], [-2.0, 0.75, -1.1519173383712769, 1], [-2.0, 0.75, -1.1344640254974365, 1], [-2.0, 0.75, -1.1170107126235962, 1], [-2.0, 0.75, -1.0995573997497559, 1], [-2.0, 0.75, -1.0821040868759155, 1], [-2.0, 0.75, -1.0646508932113647, 1], [-2.0, 0.75, -1.0471975803375244, 1], [-2.0, 0.75, -1.029744267463684, 1], [-2.0, 0.75, -1.0122909545898438, 1], [-2.0, 0.75, -0.9948376417160034, 1], [-2.0, 0.75, -0.9773843884468079, 1], [-2.0, 0.75, -0.9599310755729675, 1], [-2.0, 0.75, -0.942477822303772, 1], [-2.0, 0.75, -0.9250245094299316, 1], [-2.0, 0.75, -0.9075711965560913, 1], [-2.0, 0.75, -0.890117883682251, 1], [-2.0, 0.75, -0.8726646304130554, 1], [-2.0, 0.75, -0.8552113771438599, 1], [-2.0, 0.75, -0.8377580046653748, 1], [-2.0, 0.75, -0.8203047513961792, 1], [-2.0, 0.75, -0.8028514385223389, 1], [-2.0, 0.75, -0.7853981852531433, 1], [-2.0, 0.75, -0.767944872379303, 1], [-2.0, 0.75, -0.7504915595054626, 1], [-2.0, 0.75, -0.7330383062362671, 1], [-2.0, 0.75, -0.7155849933624268, 1], [-2.0, 0.75, -0.6981316804885864, 1], [-2.0, 0.75, -0.6806784272193909, 1], [-2.0, 0.75, -0.6632251143455505, 1], [-2.0, 0.75, -0.6457718014717102, 1], [-2.0, 0.75, -0.6283185482025146, 1], [-2.0, 0.75, -0.6108652353286743, 1], [-2.0, 0.75, -0.5934119820594788, 1], [-2.0, 0.75, -0.5759586095809937, 1], [-2.0, 0.75, -0.5585053563117981, 1], [-2.0, 0.75, -0.5410521030426025, 1], [-2.0, 0.75, -0.5235987901687622, 1], [-2.0, 0.75, -0.5061454772949219, 1], [-2.0, 0.75, -0.48869216442108154, 1], [-2.0, 0.75, -0.471238911151886, 1], [-2.0, 0.75, -0.45378559827804565, 1], [-2.0, 0.75, -0.4363323152065277, 1], [-2.0, 0.75, -0.4188790023326874, 1], [-2.0, 0.75, -0.4014257490634918, 1], [-2.0, 0.75, -0.3839724361896515, 1], [-2.0, 0.75, -0.36651912331581116, 1], [-2.0, 0.75, -0.3490658700466156, 1], [-2.0, 0.75, -0.33161255717277527, 1], [-2.0, 0.75, -0.31415924429893494, 1], [-2.0, 0.75, -0.2967059910297394, 0], [-2.0, 0.75, -0.27925267815589905, 0], [-2.0, 0.75, -0.2617993950843811, 0], [-2.0, 0.75, -0.24434608221054077, 0], [-2.0, 0.75, -0.22689279913902283, 0], [-2.0, 0.75, -0.20943951606750488, 0], [-2.0, 0.75, -0.19198621809482574, 0], [-2.0, 0.75, -0.1745329201221466, 0], [-2.0, 0.75, -0.15707963705062866, 0], [-2.0, 0.75, -0.13962633907794952, 0], [-2.0, 0.75, -0.12217305600643158, 0], [-2.0, 0.75, -0.10471975058317184, 0], [-2.0, 0.75, -0.0872664600610733, 0], [-2.0, 0.75, -0.06981316953897476, 0], [-2.0, 0.75, -0.05235987901687622, 0], [-2.0, 0.75, -0.03490658476948738, 0], [-2.0, 0.75, -0.01745329424738884, 0], [-2.0, 0.75, 7.450591255064865e-10, 0], [-2.0, 0.75, 0.01745329238474369, 1], [-2.0, 0.75, 0.03490658476948738, 1], [-2.0, 0.75, 0.05235987901687622, 1], [-2.0, 0.75, 0.06981316953897476, 1], [-2.0, 0.75, 0.0872664600610733, 1], [-2.0, 0.75, 0.10471975803375244, 1], [-2.0, 0.75, 0.12217304855585098, 0], [-2.0, 0.75, 0.13962633907794952, 0], [-2.0, 0.75, 0.15707963705062866, 0], [-2.0, 0.75, 0.1745329201221466, 0], [-2.0, 0.75, 0.19198621809482574, 0], [-2.0, 0.75, 0.20943951606750488, 0], [-2.0, 0.75, 0.22689279913902283, 0], [-2.0, 0.75, 0.24434609711170197, 0], [-2.0, 0.75, 0.2617993950843811, 0], [-2.0, 0.75, 0.27925267815589905, 0], [-2.0, 0.75, 0.296705961227417, 0], [-2.0, 0.75, 0.3141592741012573, 0], [-2.0, 0.75, 0.33161255717277527, 0], [-2.0, 0.75, 0.3490658402442932, 0], [-2.0, 0.75, 0.36651915311813354, 0], [-2.0, 0.75, 0.3839724361896515, 0], [-2.0, 0.75, 0.40142571926116943, 1], [-2.0, 0.75, 0.41887903213500977, 1], [-2.0, 0.75, 0.4363323152065277, 1], [-2.0, 0.75, 0.45378559827804565, 1], [-2.0, 0.75, 0.4712388813495636, 1], [-2.0, 0.75, 0.48869219422340393, 0], [-2.0, 0.75, 0.5061454772949219, 0], [-2.0, 0.75, 0.5235987901687622, 0], [-2.0, 0.75, 0.5410520434379578, 0], [-2.0, 0.75, 0.5585053563117981, 0], [-2.0, 0.75, 0.5759586691856384, 0], [-2.0, 0.75, 0.5934119820594788, 0], [-2.0, 0.75, 0.6108652353286743, 0], [-2.0, 0.75, 0.6283184885978699, 0], [-2.0, 0.75, 0.645771861076355, 0], [-2.0, 0.75, 0.6632251143455505, 0], [-2.0, 0.75, 0.6806783676147461, 0], [-2.0, 0.75, 0.6981317400932312, 0], [-2.0, 0.75, 0.7155849933624268, 0], [-2.0, 0.75, 0.7330382466316223, 0], [-2.0, 0.75, 0.7504916191101074, 0], [-2.0, 0.75, 0.767944872379303, 0], [-2.0, 0.75, 0.7853981256484985, 0], [-2.0, 0.75, 0.8028514981269836, 0], [-2.0, 0.75, 0.8203047513961792, 0], [-2.0, 0.75, 0.8377580046653748, 0], [-2.0, 0.75, 0.8552113175392151, 0], [-2.0, 0.75, 0.8726646304130554, 0], [-2.0, 0.75, 0.8901179432868958, 0], [-2.0, 0.75, 0.9075711965560913, 0], [-2.0, 0.75, 0.9250245094299316, 0], [-2.0, 0.75, 0.942477822303772, 0], [-2.0, 0.75, 0.9599310755729675, 0], [-2.0, 0.75, 0.9773843884468079, 0], [-2.0, 0.75, 0.9948376417160034, 0], [-2.0, 0.75, 1.0122909545898438, 0], [-2.0, 0.75, 1.029744267463684, 0], [-2.0, 0.75, 1.0471975803375244, 0], [-2.0, 0.75, 1.0646508932113647, 0], [-2.0, 0.75, 1.0821040868759155, 0], [-2.0, 0.75, 1.0995573997497559, 0], [-2.0, 0.75, 1.1170107126235962, 0], [-2.0, 0.75, 1.1344640254974365, 0], [-2.0, 0.75, 1.1519173383712769, 0], [-2.0, 0.75, 1.1693705320358276, 0], [-2.0, 0.75, 1.1868239641189575, 0], [-2.0, 0.75, 1.2042771577835083, 0], [-2.0, 0.75, 1.2217304706573486, 0], [-2.0, 0.75, 1.239183783531189, 0], [-2.0, 0.75, 1.2566370964050293, 0], [-2.0, 0.75, 1.27409029006958, 0], [-2.0, 0.75, 1.29154372215271, 0], [-2.0, 0.75, 1.3089969158172607, 0], [-2.0, 0.75, 1.326450228691101, 0], [-2.0, 0.75, 1.3439035415649414, 0], [-2.0, 0.75, 1.3613567352294922, 0], [-2.0, 0.75, 1.378810167312622, 0], [-2.0, 0.75, 1.3962633609771729, 0], [-2.0, 0.75, 1.4137166738510132, 0], [-2.0, 0.75, 1.4311699867248535, 0], [-2.0, 0.75, 1.4486232995986938, 0], [-2.0, 0.75, 1.4660766124725342, 0], [-2.0, 0.75, 1.483529806137085, 0], [-2.0, 0.75, 1.5009832382202148, 0], [-2.0, 0.75, 1.5184364318847656, 0], [-2.0, 0.75, 1.535889744758606, 0], [-2.0, 0.75, 1.5533430576324463, 0], [-2.0, 0.75, 1.570796251296997, 0], [-2.0, 0.75, 1.588249683380127, 0], [-2.0, 0.75, 1.6057028770446777, 0], [-2.0, 0.75, 1.623156189918518, 0], [-2.0, 0.75, 1.6406095027923584, 0], [-2.0, 0.75, 1.6580628156661987, 0], [-2.0, 0.75, 1.6755160093307495, 0], [-2.0, 0.75, 1.6929694414138794, 0], [-2.0, 0.75, 1.7104226350784302, 0], [-2.0, 0.75, 1.7278759479522705, 0], [-2.0, 0.75, 1.7453292608261108, 0], [-2.0, 0.75, 1.7627825736999512, 0], [-2.0, 0.75, 1.780235767364502, 0], [-2.0, 0.75, 1.7976891994476318, 0], [-2.0, 0.75, 1.8151423931121826, 0], [-2.0, 0.75, 1.832595705986023, 0], [-2.0, 0.75, 1.8500490188598633, 0], [-2.0, 0.75, 1.8675023317337036, 0], [-2.0, 0.75, 1.8849555253982544, 0], [-2.0, 0.75, 1.9024089574813843, 0], [-2.0, 0.75, 1.919862151145935, 0], [-2.0, 0.75, 1.9373154640197754, 0], [-2.0, 0.75, 1.9547687768936157, 0], [-2.0, 0.75, 1.972222089767456, 0], [-2.0, 0.75, 1.9896752834320068, 0], [-2.0, 0.75, 2.0071287155151367, 0], [-2.0, 0.75, 2.0245819091796875, 0], [-2.0, 0.75, 2.0420351028442383, 0], [-2.0, 0.75, 2.059488534927368, 0], [-2.0, 0.75, 2.076941967010498, 0], [-2.0, 0.75, 2.0943949222564697, 0], [-2.0, 0.75, 2.1118485927581787, 0], [-2.0, 0.75, 2.1293015480041504, 0], [-2.0, 0.75, 2.1467549800872803, 0], [-2.0, 0.75, 2.16420841217041, 0], [-2.0, 0.75, 2.181661367416382, 0], [-2.0, 0.75, 2.199115037918091, 0], [-2.0, 0.75, 2.2165679931640625, 0], [-2.0, 0.75, 2.2340214252471924, 0], [-2.0, 0.75, 2.2514748573303223, 0], [-2.0, 0.75, 2.268928050994873, 1], [-2.0, 0.75, 2.286381244659424, 1], [-2.0, 0.75, 2.3038346767425537, 1], [-2.0, 0.75, 2.3212878704071045, 1], [-2.0, 0.75, 2.3387413024902344, 1], [-2.0, 0.75, 2.356194496154785, 0], [-2.0, 0.75, 2.373647689819336, 0], [-2.0, 0.75, 2.391101121902466, 0], [-2.0, 0.75, 2.4085543155670166, 0], [-2.0, 0.75, 2.4260077476501465, 0], [-2.0, 0.75, 2.4434609413146973, 0], [-2.0, 0.75, 2.460914134979248, 0], [-2.0, 0.75, 2.478367567062378, 0], [-2.0, 0.75, 2.4958207607269287, 0], [-2.0, 0.75, 2.5132741928100586, 0], [-2.0, 0.75, 2.5307273864746094, 0], [-2.0, 0.75, 2.5481808185577393, 0], [-2.0, 0.75, 2.56563401222229, 0], [-2.0, 0.75, 2.583087205886841, 0], [-2.0, 0.75, 2.6005406379699707, 0], [-2.0, 0.75, 2.6179938316345215, 0], [-2.0, 0.75, 2.6354470252990723, 0], [-2.0, 0.75, 2.6529006958007812, 1], [-2.0, 0.75, 2.670353651046753, 1], [-2.0, 0.75, 2.687807083129883, 1], [-2.0, 0.75, 2.7052602767944336, 1], [-2.0, 0.75, 2.7227137088775635, 1], [-2.0, 0.75, 2.7401669025421143, 1], [-2.0, 0.75, 2.757620096206665, 1], [-2.0, 0.75, 2.775073528289795, 0], [-2.0, 0.75, 2.792526960372925, 0], [-2.0, 0.75, 2.8099799156188965, 0], [-2.0, 0.75, 2.8274335861206055, 0], [-2.0, 0.75, 2.844886541366577, 0], [-2.0, 0.75, 2.862339973449707, 0], [-2.0, 0.75, 2.879793405532837, 0], [-2.0, 0.75, 2.8972463607788086, 0], [-2.0, 0.75, 2.9147000312805176, 0], [-2.0, 0.75, 2.9321529865264893, 0], [-2.0, 0.75, 2.949606418609619, 0], [-2.0, 0.75, 2.967059850692749, 0], [-2.0, 0.75, 2.9845130443573, 0], [-2.0, 0.75, 3.0019662380218506, 0], [-2.0, 0.75, 3.0194196701049805, 0], [-2.0, 0.75, 3.0368728637695312, 0], [-2.0, 0.75, 3.054326057434082, 0], [-2.0, 0.75, 3.071779489517212, 0], [-2.0, 0.75, 3.089232921600342, 0], [-2.0, 0.75, 3.1066861152648926, 0], [-2.0, 0.75, 3.1241393089294434, 0]]
\ No newline at end of file
diff --git a/probe_vis_n_-2.1_0.75.json b/probe_vis_n_-2.1_0.75.json
new file mode 100644
index 0000000..e265c5c
--- /dev/null
+++ b/probe_vis_n_-2.1_0.75.json
@@ -0,0 +1 @@
           1 +[[-2.0999999046325684, 0.75, 3.141592502593994, 1], [-2.0999999046325684, 0.75, -3.1241393089294434, 1], [-2.0999999046325684, 0.75, -3.1066861152648926, 1], [-2.0999999046325684, 0.75, -3.0892326831817627, 1], [-2.0999999046325684, 0.75, -3.071779489517212, 1], [-2.0999999046325684, 0.75, -3.054326295852661, 1], [-2.0999999046325684, 0.75, -3.0368728637695312, 1], [-2.0999999046325684, 0.75, -3.0194194316864014, 1], [-2.0999999046325684, 0.75, -3.0019664764404297, 1], [-2.0999999046325684, 0.75, -2.9845130443573, 1], [-2.0999999046325684, 0.75, -2.96705961227417, 1], [-2.0999999046325684, 0.75, -2.949606418609619, 1], [-2.0999999046325684, 0.75, -2.9321532249450684, 1], [-2.0999999046325684, 0.75, -2.9146997928619385, 1], [-2.0999999046325684, 0.75, -2.8972465991973877, 1], [-2.0999999046325684, 0.75, -2.879793167114258, 1], [-2.0999999046325684, 0.75, -2.862339973449707, 1], [-2.0999999046325684, 0.75, -2.8448867797851562, 1], [-2.0999999046325684, 0.75, -2.8274333477020264, 1], [-2.0999999046325684, 0.75, -2.8099801540374756, 1], [-2.0999999046325684, 0.75, -2.7925267219543457, 1], [-2.0999999046325684, 0.75, -2.775073528289795, 1], [-2.0999999046325684, 0.75, -2.757620334625244, 1], [-2.0999999046325684, 0.75, -2.7401669025421143, 1], [-2.0999999046325684, 0.75, -2.7227134704589844, 1], [-2.0999999046325684, 0.75, -2.7052605152130127, 1], [-2.0999999046325684, 0.75, -2.6878068447113037, 1], [-2.0999999046325684, 0.75, -2.670353889465332, 1], [-2.0999999046325684, 0.75, -2.652900457382202, 1], [-2.0999999046325684, 0.75, -2.6354472637176514, 1], [-2.0999999046325684, 0.75, -2.6179938316345215, 1], [-2.0999999046325684, 0.75, -2.6005406379699707, 1], [-2.0999999046325684, 0.75, -2.583087205886841, 1], [-2.0999999046325684, 0.75, -2.56563401222229, 1], [-2.0999999046325684, 0.75, -2.54818058013916, 1], [-2.0999999046325684, 0.75, -2.5307276248931885, 1], [-2.0999999046325684, 0.75, -2.5132739543914795, 1], [-2.0999999046325684, 0.75, -2.495820999145508, 1], [-2.0999999046325684, 0.75, -2.478367328643799, 1], [-2.0999999046325684, 0.75, -2.460914373397827, 1], [-2.0999999046325684, 0.75, -2.4434609413146973, 1], [-2.0999999046325684, 0.75, -2.4260077476501465, 1], [-2.0999999046325684, 0.75, -2.4085543155670166, 1], [-2.0999999046325684, 0.75, -2.391101121902466, 1], [-2.0999999046325684, 0.75, -2.373647689819336, 1], [-2.0999999046325684, 0.75, -2.356194496154785, 1], [-2.0999999046325684, 0.75, -2.3387410640716553, 1], [-2.0999999046325684, 0.75, -2.3212881088256836, 1], [-2.0999999046325684, 0.75, -2.3038344383239746, 1], [-2.0999999046325684, 0.75, -2.286381483078003, 1], [-2.0999999046325684, 0.75, -2.268928050994873, 1], [-2.0999999046325684, 0.75, -2.251474618911743, 1], [-2.0999999046325684, 0.75, -2.2340214252471924, 1], [-2.0999999046325684, 0.75, -2.2165682315826416, 1], [-2.0999999046325684, 0.75, -2.1991147994995117, 1], [-2.0999999046325684, 0.75, -2.181661605834961, 1], [-2.0999999046325684, 0.75, -2.164208173751831, 1], [-2.0999999046325684, 0.75, -2.1467549800872803, 1], [-2.0999999046325684, 0.75, -2.1293017864227295, 1], [-2.0999999046325684, 0.75, -2.1118483543395996, 1], [-2.0999999046325684, 0.75, -2.094395160675049, 1], [-2.0999999046325684, 0.75, -2.076941728591919, 1], [-2.0999999046325684, 0.75, -2.059488534927368, 1], [-2.0999999046325684, 0.75, -2.0420353412628174, 1], [-2.0999999046325684, 0.75, -2.0245819091796875, 1], [-2.0999999046325684, 0.75, -2.0071284770965576, 1], [-2.0999999046325684, 0.75, -1.9896754026412964, 1], [-2.0999999046325684, 0.75, -1.972222089767456, 1], [-2.0999999046325684, 0.75, -1.9547687768936157, 1], [-2.0999999046325684, 0.75, -1.9373154640197754, 1], [-2.0999999046325684, 0.75, -1.919862151145935, 1], [-2.0999999046325684, 0.75, -1.9024088382720947, 1], [-2.0999999046325684, 0.75, -1.884955644607544, 1], [-2.0999999046325684, 0.75, -1.8675023317337036, 1], [-2.0999999046325684, 0.75, -1.8500490188598633, 1], [-2.0999999046325684, 0.75, -1.832595705986023, 1], [-2.0999999046325684, 0.75, -1.8151423931121826, 1], [-2.0999999046325684, 0.75, -1.7976890802383423, 1], [-2.0999999046325684, 0.75, -1.7802358865737915, 1], [-2.0999999046325684, 0.75, -1.7627825736999512, 1], [-2.0999999046325684, 0.75, -1.7453292608261108, 1], [-2.0999999046325684, 0.75, -1.7278759479522705, 1], [-2.0999999046325684, 0.75, -1.7104226350784302, 1], [-2.0999999046325684, 0.75, -1.6929693222045898, 1], [-2.0999999046325684, 0.75, -1.675516128540039, 1], [-2.0999999046325684, 0.75, -1.6580628156661987, 1], [-2.0999999046325684, 0.75, -1.6406095027923584, 1], [-2.0999999046325684, 0.75, -1.623156189918518, 1], [-2.0999999046325684, 0.75, -1.6057028770446777, 1], [-2.0999999046325684, 0.75, -1.588249683380127, 1], [-2.0999999046325684, 0.75, -1.570796251296997, 1], [-2.0999999046325684, 0.75, -1.5533430576324463, 1], [-2.0999999046325684, 0.75, -1.535889744758606, 1], [-2.0999999046325684, 0.75, -1.5184364318847656, 1], [-2.0999999046325684, 0.75, -1.5009832382202148, 1], [-2.0999999046325684, 0.75, -1.483529806137085, 1], [-2.0999999046325684, 0.75, -1.4660766124725342, 1], [-2.0999999046325684, 0.75, -1.4486232995986938, 1], [-2.0999999046325684, 0.75, -1.4311699867248535, 1], [-2.0999999046325684, 0.75, -1.4137166738510132, 1], [-2.0999999046325684, 0.75, -1.3962633609771729, 1], [-2.0999999046325684, 0.75, -1.378810167312622, 1], [-2.0999999046325684, 0.75, -1.3613567352294922, 1], [-2.0999999046325684, 0.75, -1.3439035415649414, 1], [-2.0999999046325684, 0.75, -1.326450228691101, 1], [-2.0999999046325684, 0.75, -1.3089969158172607, 1], [-2.0999999046325684, 0.75, -1.29154372215271, 1], [-2.0999999046325684, 0.75, -1.27409029006958, 1], [-2.0999999046325684, 0.75, -1.2566370964050293, 1], [-2.0999999046325684, 0.75, -1.239183783531189, 1], [-2.0999999046325684, 0.75, -1.2217304706573486, 1], [-2.0999999046325684, 0.75, -1.2042771577835083, 1], [-2.0999999046325684, 0.75, -1.186823844909668, 1], [-2.0999999046325684, 0.75, -1.1693706512451172, 1], [-2.0999999046325684, 0.75, -1.1519173383712769, 1], [-2.0999999046325684, 0.75, -1.1344640254974365, 1], [-2.0999999046325684, 0.75, -1.1170107126235962, 1], [-2.0999999046325684, 0.75, -1.0995573997497559, 1], [-2.0999999046325684, 0.75, -1.0821040868759155, 1], [-2.0999999046325684, 0.75, -1.0646508932113647, 1], [-2.0999999046325684, 0.75, -1.0471975803375244, 1], [-2.0999999046325684, 0.75, -1.029744267463684, 1], [-2.0999999046325684, 0.75, -1.0122909545898438, 1], [-2.0999999046325684, 0.75, -0.9948376417160034, 1], [-2.0999999046325684, 0.75, -0.9773843884468079, 1], [-2.0999999046325684, 0.75, -0.9599310755729675, 1], [-2.0999999046325684, 0.75, -0.942477822303772, 1], [-2.0999999046325684, 0.75, -0.9250245094299316, 1], [-2.0999999046325684, 0.75, -0.9075711965560913, 1], [-2.0999999046325684, 0.75, -0.890117883682251, 1], [-2.0999999046325684, 0.75, -0.8726646304130554, 1], [-2.0999999046325684, 0.75, -0.8552113771438599, 1], [-2.0999999046325684, 0.75, -0.8377580046653748, 1], [-2.0999999046325684, 0.75, -0.8203047513961792, 1], [-2.0999999046325684, 0.75, -0.8028514385223389, 1], [-2.0999999046325684, 0.75, -0.7853981852531433, 1], [-2.0999999046325684, 0.75, -0.767944872379303, 1], [-2.0999999046325684, 0.75, -0.7504915595054626, 1], [-2.0999999046325684, 0.75, -0.7330383062362671, 1], [-2.0999999046325684, 0.75, -0.7155849933624268, 1], [-2.0999999046325684, 0.75, -0.6981316804885864, 1], [-2.0999999046325684, 0.75, -0.6806784272193909, 1], [-2.0999999046325684, 0.75, -0.6632251143455505, 1], [-2.0999999046325684, 0.75, -0.6457718014717102, 1], [-2.0999999046325684, 0.75, -0.6283185482025146, 1], [-2.0999999046325684, 0.75, -0.6108652353286743, 1], [-2.0999999046325684, 0.75, -0.5934119820594788, 1], [-2.0999999046325684, 0.75, -0.5759586095809937, 1], [-2.0999999046325684, 0.75, -0.5585053563117981, 1], [-2.0999999046325684, 0.75, -0.5410521030426025, 1], [-2.0999999046325684, 0.75, -0.5235987901687622, 1], [-2.0999999046325684, 0.75, -0.5061454772949219, 1], [-2.0999999046325684, 0.75, -0.48869216442108154, 1], [-2.0999999046325684, 0.75, -0.471238911151886, 1], [-2.0999999046325684, 0.75, -0.45378559827804565, 1], [-2.0999999046325684, 0.75, -0.4363323152065277, 1], [-2.0999999046325684, 0.75, -0.4188790023326874, 1], [-2.0999999046325684, 0.75, -0.4014257490634918, 1], [-2.0999999046325684, 0.75, -0.3839724361896515, 1], [-2.0999999046325684, 0.75, -0.36651912331581116, 1], [-2.0999999046325684, 0.75, -0.3490658700466156, 1], [-2.0999999046325684, 0.75, -0.33161255717277527, 1], [-2.0999999046325684, 0.75, -0.31415924429893494, 1], [-2.0999999046325684, 0.75, -0.2967059910297394, 1], [-2.0999999046325684, 0.75, -0.27925267815589905, 1], [-2.0999999046325684, 0.75, -0.2617993950843811, 1], [-2.0999999046325684, 0.75, -0.24434608221054077, 1], [-2.0999999046325684, 0.75, -0.22689279913902283, 1], [-2.0999999046325684, 0.75, -0.20943951606750488, 1], [-2.0999999046325684, 0.75, -0.19198621809482574, 1], [-2.0999999046325684, 0.75, -0.1745329201221466, 1], [-2.0999999046325684, 0.75, -0.15707963705062866, 1], [-2.0999999046325684, 0.75, -0.13962633907794952, 1], [-2.0999999046325684, 0.75, -0.12217305600643158, 1], [-2.0999999046325684, 0.75, -0.10471975058317184, 1], [-2.0999999046325684, 0.75, -0.0872664600610733, 1], [-2.0999999046325684, 0.75, -0.06981316953897476, 1], [-2.0999999046325684, 0.75, -0.05235987901687622, 1], [-2.0999999046325684, 0.75, -0.03490658476948738, 1], [-2.0999999046325684, 0.75, -0.01745329424738884, 1], [-2.0999999046325684, 0.75, 7.450591255064865e-10, 1], [-2.0999999046325684, 0.75, 0.01745329238474369, 1], [-2.0999999046325684, 0.75, 0.03490658476948738, 1], [-2.0999999046325684, 0.75, 0.05235987901687622, 1], [-2.0999999046325684, 0.75, 0.06981316953897476, 1], [-2.0999999046325684, 0.75, 0.0872664600610733, 1], [-2.0999999046325684, 0.75, 0.10471975803375244, 1], [-2.0999999046325684, 0.75, 0.12217304855585098, 1], [-2.0999999046325684, 0.75, 0.13962633907794952, 1], [-2.0999999046325684, 0.75, 0.15707963705062866, 1], [-2.0999999046325684, 0.75, 0.1745329201221466, 1], [-2.0999999046325684, 0.75, 0.19198621809482574, 1], [-2.0999999046325684, 0.75, 0.20943951606750488, 1], [-2.0999999046325684, 0.75, 0.22689279913902283, 1], [-2.0999999046325684, 0.75, 0.24434609711170197, 1], [-2.0999999046325684, 0.75, 0.2617993950843811, 1], [-2.0999999046325684, 0.75, 0.27925267815589905, 1], [-2.0999999046325684, 0.75, 0.296705961227417, 1], [-2.0999999046325684, 0.75, 0.3141592741012573, 1], [-2.0999999046325684, 0.75, 0.33161255717277527, 1], [-2.0999999046325684, 0.75, 0.3490658402442932, 1], [-2.0999999046325684, 0.75, 0.36651915311813354, 1], [-2.0999999046325684, 0.75, 0.3839724361896515, 1], [-2.0999999046325684, 0.75, 0.40142571926116943, 1], [-2.0999999046325684, 0.75, 0.41887903213500977, 1], [-2.0999999046325684, 0.75, 0.4363323152065277, 1], [-2.0999999046325684, 0.75, 0.45378559827804565, 1], [-2.0999999046325684, 0.75, 0.4712388813495636, 1], [-2.0999999046325684, 0.75, 0.48869219422340393, 1], [-2.0999999046325684, 0.75, 0.5061454772949219, 1], [-2.0999999046325684, 0.75, 0.5235987901687622, 1], [-2.0999999046325684, 0.75, 0.5410520434379578, 1], [-2.0999999046325684, 0.75, 0.5585053563117981, 0], [-2.0999999046325684, 0.75, 0.5759586691856384, 0], [-2.0999999046325684, 0.75, 0.5934119820594788, 0], [-2.0999999046325684, 0.75, 0.6108652353286743, 0], [-2.0999999046325684, 0.75, 0.6283184885978699, 0], [-2.0999999046325684, 0.75, 0.645771861076355, 0], [-2.0999999046325684, 0.75, 0.6632251143455505, 0], [-2.0999999046325684, 0.75, 0.6806783676147461, 0], [-2.0999999046325684, 0.75, 0.6981317400932312, 0], [-2.0999999046325684, 0.75, 0.7155849933624268, 0], [-2.0999999046325684, 0.75, 0.7330382466316223, 0], [-2.0999999046325684, 0.75, 0.7504916191101074, 0], [-2.0999999046325684, 0.75, 0.767944872379303, 0], [-2.0999999046325684, 0.75, 0.7853981256484985, 0], [-2.0999999046325684, 0.75, 0.8028514981269836, 0], [-2.0999999046325684, 0.75, 0.8203047513961792, 0], [-2.0999999046325684, 0.75, 0.8377580046653748, 0], [-2.0999999046325684, 0.75, 0.8552113175392151, 0], [-2.0999999046325684, 0.75, 0.8726646304130554, 0], [-2.0999999046325684, 0.75, 0.8901179432868958, 0], [-2.0999999046325684, 0.75, 0.9075711965560913, 0], [-2.0999999046325684, 0.75, 0.9250245094299316, 0], [-2.0999999046325684, 0.75, 0.942477822303772, 0], [-2.0999999046325684, 0.75, 0.9599310755729675, 0], [-2.0999999046325684, 0.75, 0.9773843884468079, 0], [-2.0999999046325684, 0.75, 0.9948376417160034, 0], [-2.0999999046325684, 0.75, 1.0122909545898438, 0], [-2.0999999046325684, 0.75, 1.029744267463684, 0], [-2.0999999046325684, 0.75, 1.0471975803375244, 0], [-2.0999999046325684, 0.75, 1.0646508932113647, 0], [-2.0999999046325684, 0.75, 1.0821040868759155, 0], [-2.0999999046325684, 0.75, 1.0995573997497559, 0], [-2.0999999046325684, 0.75, 1.1170107126235962, 0], [-2.0999999046325684, 0.75, 1.1344640254974365, 0], [-2.0999999046325684, 0.75, 1.1519173383712769, 0], [-2.0999999046325684, 0.75, 1.1693705320358276, 0], [-2.0999999046325684, 0.75, 1.1868239641189575, 0], [-2.0999999046325684, 0.75, 1.2042771577835083, 0], [-2.0999999046325684, 0.75, 1.2217304706573486, 0], [-2.0999999046325684, 0.75, 1.239183783531189, 0], [-2.0999999046325684, 0.75, 1.2566370964050293, 0], [-2.0999999046325684, 0.75, 1.27409029006958, 0], [-2.0999999046325684, 0.75, 1.29154372215271, 0], [-2.0999999046325684, 0.75, 1.3089969158172607, 0], [-2.0999999046325684, 0.75, 1.326450228691101, 0], [-2.0999999046325684, 0.75, 1.3439035415649414, 0], [-2.0999999046325684, 0.75, 1.3613567352294922, 0], [-2.0999999046325684, 0.75, 1.378810167312622, 0], [-2.0999999046325684, 0.75, 1.3962633609771729, 0], [-2.0999999046325684, 0.75, 1.4137166738510132, 0], [-2.0999999046325684, 0.75, 1.4311699867248535, 0], [-2.0999999046325684, 0.75, 1.4486232995986938, 0], [-2.0999999046325684, 0.75, 1.4660766124725342, 0], [-2.0999999046325684, 0.75, 1.483529806137085, 0], [-2.0999999046325684, 0.75, 1.5009832382202148, 0], [-2.0999999046325684, 0.75, 1.5184364318847656, 0], [-2.0999999046325684, 0.75, 1.535889744758606, 0], [-2.0999999046325684, 0.75, 1.5533430576324463, 0], [-2.0999999046325684, 0.75, 1.570796251296997, 0], [-2.0999999046325684, 0.75, 1.588249683380127, 0], [-2.0999999046325684, 0.75, 1.6057028770446777, 0], [-2.0999999046325684, 0.75, 1.623156189918518, 0], [-2.0999999046325684, 0.75, 1.6406095027923584, 0], [-2.0999999046325684, 0.75, 1.6580628156661987, 0], [-2.0999999046325684, 0.75, 1.6755160093307495, 0], [-2.0999999046325684, 0.75, 1.6929694414138794, 0], [-2.0999999046325684, 0.75, 1.7104226350784302, 0], [-2.0999999046325684, 0.75, 1.7278759479522705, 0], [-2.0999999046325684, 0.75, 1.7453292608261108, 0], [-2.0999999046325684, 0.75, 1.7627825736999512, 0], [-2.0999999046325684, 0.75, 1.780235767364502, 0], [-2.0999999046325684, 0.75, 1.7976891994476318, 0], [-2.0999999046325684, 0.75, 1.8151423931121826, 0], [-2.0999999046325684, 0.75, 1.832595705986023, 0], [-2.0999999046325684, 0.75, 1.8500490188598633, 0], [-2.0999999046325684, 0.75, 1.8675023317337036, 0], [-2.0999999046325684, 0.75, 1.8849555253982544, 0], [-2.0999999046325684, 0.75, 1.9024089574813843, 0], [-2.0999999046325684, 0.75, 1.919862151145935, 0], [-2.0999999046325684, 0.75, 1.9373154640197754, 0], [-2.0999999046325684, 0.75, 1.9547687768936157, 0], [-2.0999999046325684, 0.75, 1.972222089767456, 0], [-2.0999999046325684, 0.75, 1.9896752834320068, 0], [-2.0999999046325684, 0.75, 2.0071287155151367, 0], [-2.0999999046325684, 0.75, 2.0245819091796875, 0], [-2.0999999046325684, 0.75, 2.0420351028442383, 0], [-2.0999999046325684, 0.75, 2.059488534927368, 0], [-2.0999999046325684, 0.75, 2.076941967010498, 0], [-2.0999999046325684, 0.75, 2.0943949222564697, 0], [-2.0999999046325684, 0.75, 2.1118485927581787, 0], [-2.0999999046325684, 0.75, 2.1293015480041504, 0], [-2.0999999046325684, 0.75, 2.1467549800872803, 0], [-2.0999999046325684, 0.75, 2.16420841217041, 0], [-2.0999999046325684, 0.75, 2.181661367416382, 1], [-2.0999999046325684, 0.75, 2.199115037918091, 1], [-2.0999999046325684, 0.75, 2.2165679931640625, 1], [-2.0999999046325684, 0.75, 2.2340214252471924, 1], [-2.0999999046325684, 0.75, 2.2514748573303223, 1], [-2.0999999046325684, 0.75, 2.268928050994873, 0], [-2.0999999046325684, 0.75, 2.286381244659424, 0], [-2.0999999046325684, 0.75, 2.3038346767425537, 0], [-2.0999999046325684, 0.75, 2.3212878704071045, 0], [-2.0999999046325684, 0.75, 2.3387413024902344, 0], [-2.0999999046325684, 0.75, 2.356194496154785, 0], [-2.0999999046325684, 0.75, 2.373647689819336, 0], [-2.0999999046325684, 0.75, 2.391101121902466, 0], [-2.0999999046325684, 0.75, 2.4085543155670166, 0], [-2.0999999046325684, 0.75, 2.4260077476501465, 0], [-2.0999999046325684, 0.75, 2.4434609413146973, 0], [-2.0999999046325684, 0.75, 2.460914134979248, 0], [-2.0999999046325684, 0.75, 2.478367567062378, 0], [-2.0999999046325684, 0.75, 2.4958207607269287, 0], [-2.0999999046325684, 0.75, 2.5132741928100586, 0], [-2.0999999046325684, 0.75, 2.5307273864746094, 0], [-2.0999999046325684, 0.75, 2.5481808185577393, 0], [-2.0999999046325684, 0.75, 2.56563401222229, 0], [-2.0999999046325684, 0.75, 2.583087205886841, 1], [-2.0999999046325684, 0.75, 2.6005406379699707, 1], [-2.0999999046325684, 0.75, 2.6179938316345215, 1], [-2.0999999046325684, 0.75, 2.6354470252990723, 1], [-2.0999999046325684, 0.75, 2.6529006958007812, 1], [-2.0999999046325684, 0.75, 2.670353651046753, 1], [-2.0999999046325684, 0.75, 2.687807083129883, 0], [-2.0999999046325684, 0.75, 2.7052602767944336, 0], [-2.0999999046325684, 0.75, 2.7227137088775635, 0], [-2.0999999046325684, 0.75, 2.7401669025421143, 0], [-2.0999999046325684, 0.75, 2.757620096206665, 0], [-2.0999999046325684, 0.75, 2.775073528289795, 0], [-2.0999999046325684, 0.75, 2.792526960372925, 0], [-2.0999999046325684, 0.75, 2.8099799156188965, 0], [-2.0999999046325684, 0.75, 2.8274335861206055, 0], [-2.0999999046325684, 0.75, 2.844886541366577, 0], [-2.0999999046325684, 0.75, 2.862339973449707, 0], [-2.0999999046325684, 0.75, 2.879793405532837, 0], [-2.0999999046325684, 0.75, 2.8972463607788086, 0], [-2.0999999046325684, 0.75, 2.9147000312805176, 0], [-2.0999999046325684, 0.75, 2.9321529865264893, 0], [-2.0999999046325684, 0.75, 2.949606418609619, 0], [-2.0999999046325684, 0.75, 2.967059850692749, 0], [-2.0999999046325684, 0.75, 2.9845130443573, 0], [-2.0999999046325684, 0.75, 3.0019662380218506, 0], [-2.0999999046325684, 0.75, 3.0194196701049805, 0], [-2.0999999046325684, 0.75, 3.0368728637695312, 0], [-2.0999999046325684, 0.75, 3.054326057434082, 1], [-2.0999999046325684, 0.75, 3.071779489517212, 1], [-2.0999999046325684, 0.75, 3.089232921600342, 1], [-2.0999999046325684, 0.75, 3.1066861152648926, 1], [-2.0999999046325684, 0.75, 3.1241393089294434, 1]]
\ No newline at end of file
diff --git a/probe_vis_o.py b/probe_vis_o.py
new file mode 100644
index 0000000..43601ec
--- /dev/null
+++ b/probe_vis_o.py
@@ -0,0 +1,16 @@
           1 +from probe_vis_lib import *
           2 +import sys, json
           3 +seed=int(sys.argv[1]); ri=int(sys.argv[2]); x,y=float(sys.argv[3]),float(sys.argv[4]); path=eval(sys.argv[5]); objn=sys.argv[6]
           4 +e=E(seed); print(e.path(ri,path+[(x,y)]), e.rs(ri)['x'], e.rs(ri)['y'])
           5 +o=e.objs()[objn]; brg=math.degrees(math.atan2(o['y']-y,o['x']-x))
           6 +N=360; res=[]
           7 +for k in range(N):
           8 +    th=-math.pi+k*2*math.pi/N
           9 +    e.turn(ri,th); st=e.rs(ri)
          10 +    e.step(ri,0,0,0,'cal'); c=e.rs(ri)['calibrated']; e.step(ri,0,0,0,'img')
          11 +    res.append((st['x'],st['y'],st['theta'],int(c)))
          12 +s=''.join(str(r[3]) for r in res)
          13 +runs=[];cur=s[0];start=0
          14 +for i,ch in enumerate(s[1:]+'x',1):
          15 +    if ch!=cur: runs.append((cur,round(math.degrees(res[start][2])),round(math.degrees(res[i-1][2])))); cur=ch; start=i
          16 +print('bearing to obj %.1f'%brg, runs)
diff --git a/probe_vis_p.py b/probe_vis_p.py
new file mode 100644
index 0000000..9037af3
--- /dev/null
+++ b/probe_vis_p.py
@@ -0,0 +1,14 @@
           1 +from probe_vis_lib import *
           2 +def flags(e): return {k:(int(v['have_image_rover0']),int(v['have_image_rover1'])) for k,v in e.objs().items()}
           3 +# mound occlusion test: seed5 rover0 at (1.0,2.0) viewing obj1 on (-0.5,2) through mound (0.5,2)
           4 +for th in [math.pi, 0.0, -math.pi/2]:
           5 +    e=E(5); ok=e.path(0,[(1.6,-1.75),(1.6,1.0),(1.0,1.5),(1.0,2.0)]); e.turn(0,th)
           6 +    st=e.rs(0); out=[]
           7 +    for i in range(2):
           8 +        e.step(0,0,0,0,'cal'); c=e.rs(0)['calibrated']; e.step(0,0,0,0,'img'); out.append((c,flags(e)))
           9 +    print('mound test th=%.2f'%th, ok, round(st['x'],3), round(st['y'],3), out); e.close()
          10 +# image under bypass: seed4 rover1 deep shadow
          11 +for th in [math.pi/2, -math.pi/2]:
          12 +    e=E(4); e.path(1,[(-1.0,-1.0),(-1.0,0.75),(-1.95,0.75)]); e.turn(1,th)
          13 +    e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img')
          14 +    print('shadow th=%.2f cal=%d'%(th,c), flags(e)); e.close()
```

</details>

<a id="C006"></a>
### C006 · v1 staged grid planner

Commit `d4c816ce110c4e091102cc8f8237a52e37544d78`; parents: 948d71b4e9589661ec694b9114d1bfe0f09622ff. Recorded author date: 2026-10-01T11:05:09+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0619](01_timeline.md#E0619): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_d4c816c_approach.py) · [Exact all-file diff](evidence/diffs/C006_d4c816c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..f58760c
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,472 @@
           1 +"""Rovers approach: staged grid BFS planner per rover + joint task assignment."""
           2 +import itertools
           3 +import math
           4 +
           5 +import numpy as np
           6 +from scipy.ndimage import minimum_filter
           7 +
           8 +INF = 10 ** 6
           9 +RES = 0.05            # grid resolution
          10 +WIN = 4               # max cells per step per axis (0.2 / RES)
          11 +SEL = {"sample": -0.8333, "cal": -0.5, "img": -0.1667, "noop": 0.1667,
          12 +       "send": 0.5, "drop": 0.8333}
          13 +
          14 +# geometry constants (empirically probed)
          15 +WALL_IN = 0.2271 + 0.004
          16 +ARENA = 2.2729 - 0.004
          17 +PILLAR_R = 0.245
          18 +MOUND_R = 0.185
          19 +LANDER_XMIN = -1.195
          20 +LANDER_YMIN = -1.455
          21 +OBJ_RANGE = 1.95
          22 +LANDER_RANGE = 3.95
          23 +SAMPLE_R = 0.235
          24 +PILLAR_INFL_OBJ = 0.03
          25 +PILLAR_INFL_LAND = 0.04
          26 +ROVER_OCC_R = 0.27
          27 +CAM_OFF = (-0.087, -0.0125)
          28 +OBJ_BACK_DEG = 108.0     # if |rel bearing| > this, pillars don't occlude objectives
          29 +LAND_BACK_DEG = 110.0    # same quirk for lander (sending)
          30 +USE_BACK_OBJ = True
          31 +USE_BACK_LAND = True
          32 +
          33 +
          34 +def _wrap(a):
          35 +    return (a + np.pi) % (2 * np.pi) - np.pi
          36 +
          37 +
          38 +def seg_hits_box(px, py, qx, qy, cx, cy, hx, hy):
          39 +    """Vectorised: does segment p->q (p arrays, q scalar) intersect AABB?"""
          40 +    dx = qx - px
          41 +    dy = qy - py
          42 +    t0 = np.zeros_like(px)
          43 +    t1 = np.ones_like(px)
          44 +    ok = np.ones(px.shape, dtype=bool)
          45 +    for d, p, lo, hi in ((dx, px, cx - hx, cx + hx), (dy, py, cy - hy, cy + hy)):
          46 +        small = np.abs(d) < 1e-12
          47 +        ok &= ~(small & ((p < lo) | (p > hi)))
          48 +        with np.errstate(divide="ignore", invalid="ignore"):
          49 +            ta = (lo - p) / d
          50 +            tb = (hi - p) / d
          51 +        tmin = np.where(small, -np.inf, np.minimum(ta, tb))
          52 +        tmax = np.where(small, np.inf, np.maximum(ta, tb))
          53 +        t0 = np.maximum(t0, tmin)
          54 +        t1 = np.minimum(t1, tmax)
          55 +    return ok & (t0 <= t1)
          56 +
          57 +
          58 +def seg_hits_disk(px, py, qx, qy, cx, cy, r):
          59 +    dx = qx - px
          60 +    dy = qy - py
          61 +    L2 = dx * dx + dy * dy + 1e-12
          62 +    t = np.clip(((cx - px) * dx + (cy - py) * dy) / L2, 0, 1)
          63 +    ex = px + t * dx - cx
          64 +    ey = py + t * dy - cy
          65 +    return ex * ex + ey * ey < r * r
          66 +
          67 +
          68 +def box_dist(px, py, cx, cy, hx, hy):
          69 +    ddx = np.maximum(np.abs(px - cx) - hx, 0)
          70 +    ddy = np.maximum(np.abs(py - cy) - hy, 0)
          71 +    return np.hypot(ddx, ddy)
          72 +
          73 +
          74 +def propagate(f, free):
          75 +    f = np.where(free, f, INF)
          76 +    while True:
          77 +        m = minimum_filter(f, size=2 * WIN + 1, mode="constant", cval=INF) + 1
          78 +        nf = np.where(free, np.minimum(f, m), INF)
          79 +        if np.array_equal(nf, f):
          80 +            return f
          81 +        f = nf
          82 +
          83 +
          84 +def op_stage(fprev, region):
          85 +    m = minimum_filter(fprev, size=2 * WIN + 1, mode="constant", cval=INF) + 1
          86 +    return np.where(region, np.minimum(m, INF), INF)
          87 +
          88 +
          89 +class Scene:
          90 +    def __init__(self, state):
          91 +        self.rovers = {}
          92 +        self.objectives = []
          93 +        self.samples = []
          94 +        self.pillars = []
          95 +        self.mounds = []
          96 +        self.lander = (-1.9, -2.0)
          97 +        for o in state:
          98 +            t = o.type.name
          99 +            g = lambda f: state.get(o, f)
         100 +            if t == "rover":
         101 +                self.rovers[o.name] = dict(x=g("x"), y=g("y"), th=g("theta"),
         102 +                                           full=g("store_full") > 0.5,
         103 +                                           cal=g("calibrated") > 0.5)
         104 +            elif t == "lander":
         105 +                self.lander = (g("x"), g("y"))
         106 +            elif t == "objective":
         107 +                self.objectives.append(dict(name=o.name, x=g("x"), y=g("y"),
         108 +                                            img=(g("have_image_rover0") > 0.5,
         109 +                                                 g("have_image_rover1") > 0.5),
         110 +                                            recv=g("received_image") > 0.5))
         111 +            elif t == "sample":
         112 +                self.samples.append(dict(name=o.name, x=g("x"), y=g("y"),
         113 +                                         soil=g("is_soil") > 0.5,
         114 +                                         an=(g("analyzed_rover0") > 0.5,
         115 +                                             g("analyzed_rover1") > 0.5),
         116 +                                         recv=g("received_analysis") > 0.5))
         117 +            elif t == "obstacle":
         118 +                d = (g("x"), g("y"), g("half_x"), g("half_y"))
         119 +                if g("half_x") > 0.15:
         120 +                    self.mounds.append(d)
         121 +                else:
         122 +                    self.pillars.append(d)
         123 +
         124 +
         125 +class RoverPlanner:
         126 +    """Grid + regions for one rover."""
         127 +
         128 +    def __init__(self, idx, home, scene, other_pos_list):
         129 +        self.idx = idx
         130 +        self.home = home  # (x, y, th)
         131 +        hx, hy, th = home
         132 +        self.th = th
         133 +        side = 1 if hx > 0 else -1
         134 +        lo_x, hi_x = (WALL_IN, ARENA) if side > 0 else (-ARENA, -WALL_IN)
         135 +        i0 = math.ceil((lo_x - hx) / RES - 1e-9)
         136 +        i1 = math.floor((hi_x - hx) / RES + 1e-9)
         137 +        j0 = math.ceil((-ARENA - hy) / RES - 1e-9)
         138 +        j1 = math.floor((ARENA - hy) / RES + 1e-9)
         139 +        self.xs = hx + RES * np.arange(i0, i1 + 1)
         140 +        self.ys = hy + RES * np.arange(j0, j1 + 1)
         141 +        self.hi = -i0
         142 +        self.hj = -j0
         143 +        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
         144 +        self.X, self.Y = X, Y
         145 +        free = np.ones(X.shape, dtype=bool)
         146 +        for (cx, cy, ax, ay) in scene.pillars:
         147 +            free &= box_dist(X, Y, cx, cy, ax, ay) > PILLAR_R
         148 +        for (cx, cy, ax, ay) in scene.mounds:
         149 +            free &= box_dist(X, Y, cx, cy, ax, ay) > MOUND_R
         150 +        free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
         151 +        free[self.hi, self.hj] = True
         152 +        self.free = free
         153 +        c, s = math.cos(th), math.sin(th)
         154 +        self.camx = X + c * CAM_OFF[0] - s * CAM_OFF[1]
         155 +        self.camy = Y + s * CAM_OFF[0] + c * CAM_OFF[1]
         156 +        self.scene = scene
         157 +        # objective visibility
         158 +        self.vis = []
         159 +        self.objd = []
         160 +        for ob in scene.objectives:
         161 +            ox, oy = ob["x"], ob["y"]
         162 +            d = np.hypot(ox - self.camx, oy - self.camy)
         163 +            v = (d <= OBJ_RANGE) & (np.hypot(ox - X, oy - Y) <= OBJ_RANGE)
         164 +            occ = np.zeros(X.shape, dtype=bool)
         165 +            for (cx, cy, ax, ay) in scene.pillars:
         166 +                e = PILLAR_INFL_OBJ
         167 +                occ |= seg_hits_box(self.camx, self.camy, ox, oy, cx, cy, ax + e, ay + e)
         168 +                occ |= seg_hits_box(X, Y, ox, oy, cx, cy, ax + e, ay + e)
         169 +            if USE_BACK_OBJ:
         170 +                rel = np.abs(_wrap(np.arctan2(oy - Y, ox - X) - th))
         171 +                back = rel > math.radians(OBJ_BACK_DEG)
         172 +            else:
         173 +                back = np.zeros(X.shape, dtype=bool)
         174 +            occ2 = np.zeros(X.shape, dtype=bool)
         175 +            for (px, py) in other_pos_list:
         176 +                occ2 |= seg_hits_disk(self.camx, self.camy, ox, oy, px, py, ROVER_OCC_R)
         177 +            self.vis.append(v & ((~occ) | back) & ~occ2 & free)
         178 +            self.objd.append(d)
         179 +        self.any_vis = np.zeros(X.shape, dtype=bool)
         180 +        for v in self.vis:
         181 +            self.any_vis |= v
         182 +        # lander visibility
         183 +        lx, ly = scene.lander
         184 +        v = np.hypot(lx - X, ly - Y) <= LANDER_RANGE
         185 +        occ = np.zeros(X.shape, dtype=bool)
         186 +        for (cx, cy, ax, ay) in scene.pillars:
         187 +            e = PILLAR_INFL_LAND
         188 +            occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
         189 +            occ |= seg_hits_box(self.camx, self.camy, lx, ly, cx, cy, ax + e, ay + e)
         190 +        if USE_BACK_LAND:
         191 +            rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - th))
         192 +            back = rel > math.radians(LAND_BACK_DEG)
         193 +        else:
         194 +            back = np.zeros(X.shape, dtype=bool)
         195 +        occ2 = np.zeros(X.shape, dtype=bool)
         196 +        for (px, py) in other_pos_list:
         197 +            occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
         198 +            occ2 |= seg_hits_disk(self.camx, self.camy, lx, ly, px, py, ROVER_OCC_R)
         199 +        self.land = v & ((~occ) | back) & ~occ2 & free
         200 +        # samples
         201 +        self.sreg = {}
         202 +        for kind in ("stone", "soil"):
         203 +            r = np.zeros(X.shape, dtype=bool)
         204 +            for sm in scene.samples:
         205 +                if sm["soil"] == (kind == "soil"):
         206 +                    r |= np.hypot(sm["x"] - X, sm["y"] - Y) <= SAMPLE_R
         207 +            self.sreg[kind] = r & free
         208 +
         209 +    def cell_of(self, x, y):
         210 +        i = int(round((x - self.xs[0]) / RES))
         211 +        j = int(round((y - self.ys[0]) / RES))
         212 +        i = min(max(i, 0), len(self.xs) - 1)
         213 +        j = min(max(j, 0), len(self.ys) - 1)
         214 +        return i, j
         215 +
         216 +    def img_region(self, k, imaged):
         217 +        """cells where image would photograph objective k given set imaged."""
         218 +        reg = self.vis[k].copy()
         219 +        if not reg.any():
         220 +            return reg
         221 +        dk = self.objd[k]
         222 +        for m in range(len(self.vis)):
         223 +            if m == k or m in imaged:
         224 +                continue
         225 +            reg &= ~(self.vis[m] & (self.objd[m] < dk))
         226 +        return reg
         227 +
         228 +
         229 +class GeneratedApproach:
         230 +    def __init__(self, action_space, observation_space, primitives):
         231 +        self.action_space = action_space
         232 +        self.homes = None
         233 +
         234 +    # ------------------------------------------------------------------
         235 +    def reset(self, state, info):
         236 +        sc = Scene(state)
         237 +        self.homes = {n: (r["x"], r["y"], r["th"]) for n, r in sc.rovers.items()}
         238 +        self.replans = 0
         239 +        self.fail_count = 0
         240 +        self.expect = [None, None]
         241 +        self.prev_sc = sc
         242 +        self._plan(state)
         243 +
         244 +    # ------------------------------------------------------------------
         245 +    def _rover_tables(self, ri, sc, need_objs, need_stone, need_soil, pending):
         246 +        name = "rover%d" % ri
         247 +        r = sc.rovers[name]
         248 +        other = sc.rovers["rover%d" % (1 - ri)]
         249 +        ohome = self.homes["rover%d" % (1 - ri)]
         250 +        occl = [(ohome[0], ohome[1])]
         251 +        if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
         252 +            occl.append((other["x"], other["y"]))
         253 +        P = RoverPlanner(ri, self.homes[name], sc, occl)
         254 +        self_planner = P
         255 +        start = P.cell_of(r["x"], r["y"])
         256 +        P.free[start] = True
         257 +        f0 = np.full(P.free.shape, INF, dtype=np.int64)
         258 +        f0[start] = 0
         259 +        stages0 = []
         260 +        F = propagate(f0, P.free)
         261 +        stages0.append(("start", None, f0, F))
         262 +        if r["full"]:
         263 +            G = op_stage(F, P.free)
         264 +            F = propagate(G, P.free)
         265 +            stages0.append(("drop", None, G, F))
         266 +        imaged0 = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
         267 +        tasks = []
         268 +        for k in need_objs:
         269 +            if P.vis[k].any():
         270 +                tasks.append(("obj", k))
         271 +        if need_stone and P.sreg["stone"].any():
         272 +            tasks.append(("stone", None))
         273 +        if need_soil and P.sreg["soil"].any():
         274 +            tasks.append(("soil", None))
         275 +        hcell = (P.hi, P.hj)
         276 +        table = {}  # frozenset(task keys) -> (cost, stages)
         277 +
         278 +        def finish(F, stages, done_keys):
         279 +            if not done_keys and not pending:
         280 +                cost = F[hcell]
         281 +                st = stages
         282 +            else:
         283 +                G = op_stage(F, P.land)
         284 +                F2 = propagate(G, P.free)
         285 +                cost = F2[hcell]
         286 +                st = stages + [("send", None, G, F2)]
         287 +            if cost >= INF:
         288 +                return
         289 +            key = frozenset(done_keys)
         290 +            if key not in table or cost < table[key][0]:
         291 +                table[key] = (int(cost), st)
         292 +
         293 +        def dfs(F, stages, done_keys, imaged, cal):
         294 +            finish(F, stages, done_keys)
         295 +            if F.min() >= INF:
         296 +                return
         297 +            for t in tasks:
         298 +                key = t if t[0] != "obj" else ("obj", t[1])
         299 +                if key in done_keys:
         300 +                    continue
         301 +                if t[0] == "obj":
         302 +                    k = t[1]
         303 +                    st = list(stages)
         304 +                    Fc = F
         305 +                    if not cal:
         306 +                        G = op_stage(F, P.any_vis)
         307 +                        Fc = propagate(G, P.free)
         308 +                        st.append(("cal", None, G, Fc))
         309 +                    reg = P.img_region(k, imaged)
         310 +                    G = op_stage(Fc, reg)
         311 +                    Fi = propagate(G, P.free)
         312 +                    st.append(("img", k, G, Fi))
         313 +                    dfs(Fi, st, done_keys | {key}, imaged | {k}, False)
         314 +                else:
         315 +                    G = op_stage(F, P.sreg[t[0]])
         316 +                    Fs = propagate(G, P.free)
         317 +                    G2 = op_stage(Fs, P.free)
         318 +                    Fd = propagate(G2, P.free)
         319 +                    st = stages + [("sample", t[0], G, Fs), ("drop", None, G2, Fd)]
         320 +                    dfs(Fd, st, done_keys | {key}, imaged, cal)
         321 +
         322 +        dfs(F, stages0, frozenset(), imaged0, r["cal"])
         323 +        return P, table
         324 +
         325 +    def _plan(self, state):
         326 +        sc = Scene(state)
         327 +        self.scene = sc
         328 +        # what is needed
         329 +        need_objs = [k for k, ob in enumerate(sc.objectives)
         330 +                     if not ob["recv"] and not ob["img"][0] and not ob["img"][1]]
         331 +        pending = [False, False]
         332 +        for k, ob in enumerate(sc.objectives):
         333 +            if not ob["recv"]:
         334 +                for ri in range(2):
         335 +                    if ob["img"][ri]:
         336 +                        pending[ri] = True
         337 +        need = {}
         338 +        for kind in ("stone", "soil"):
         339 +            recv = any(s["recv"] for s in sc.samples if s["soil"] == (kind == "soil"))
         340 +            holders = [ri for ri in range(2)
         341 +                       if any(s["an"][ri] for s in sc.samples if s["soil"] == (kind == "soil"))]
         342 +            if recv:
         343 +                need[kind] = False
         344 +            elif holders:
         345 +                need[kind] = False
         346 +                pending[holders[0]] = True
         347 +            else:
         348 +                need[kind] = True
         349 +        tabs = []
         350 +        for ri in range(2):
         351 +            tabs.append(self._rover_tables(ri, sc, need_objs, need["stone"], need["soil"],
         352 +                                           pending[ri]))
         353 +        # joint assignment
         354 +        best = None
         355 +        n = len(need_objs)
         356 +        stone_opts = [0, 1] if need["stone"] else [None]
         357 +        soil_opts = [0, 1] if need["soil"] else [None]
         358 +        for assign in itertools.product([0, 1], repeat=n):
         359 +            for so in stone_opts:
         360 +                for sl in soil_opts:
         361 +                    sets = [set(), set()]
         362 +                    for k, a in zip(need_objs, assign):
         363 +                        sets[a].add(("obj", k))
         364 +                    if so is not None:
         365 +                        sets[so].add(("stone", None))
         366 +                    if sl is not None:
         367 +                        sets[sl].add(("soil", None))
         368 +                    costs = []
         369 +                    for ri in range(2):
         370 +                        e = tabs[ri][1].get(frozenset(sets[ri]))
         371 +                        costs.append(e)
         372 +                    if costs[0] is None or costs[1] is None:
         373 +                        continue
         374 +                    key = (max(costs[0][0], costs[1][0]), costs[0][0] + costs[1][0])
         375 +                    if best is None or key < best[0]:
         376 +                        best = (key, costs)
         377 +        self.actions = [[], []]
         378 +        if best is None:
         379 +            return
         380 +        for ri in range(2):
         381 +            P = tabs[ri][0]
         382 +            self.actions[ri] = self._extract(P, best[1][ri][1])
         383 +
         384 +    def _extract(self, P, stages):
         385 +        """Backtrack through stage fields; returns list of (x,y,op) targets."""
         386 +        hcell = (P.hi, P.hj)
         387 +        cell = hcell
         388 +        k = len(stages) - 1
         389 +        v = stages[k][3][cell]
         390 +        seq = []
         391 +        W = WIN
         392 +        nx, ny = P.free.shape
         393 +        while True:
         394 +            name, arg, G, F = stages[k]
         395 +            if k == 0 and v == 0:
         396 +                break
         397 +            if name != "start" and G[cell] == v:
         398 +                Fp = stages[k - 1][3]
         399 +                op = name
         400 +                k -= 1
         401 +                Fsrc = Fp
         402 +            else:
         403 +                op = None
         404 +                Fsrc = F
         405 +            found = None
         406 +            i, j = cell
         407 +            for di in range(-W, W + 1):
         408 +                for dj in range(-W, W + 1):
         409 +                    a, b = i + di, j + dj
         410 +                    if 0 <= a < nx and 0 <= b < ny and Fsrc[a, b] == v - 1:
         411 +                        if found is None or abs(di) + abs(dj) < found[1]:
         412 +                            found = ((a, b), abs(di) + abs(dj))
         413 +            if found is None:
         414 +                break
         415 +            seq.append((float(P.xs[cell[0]]), float(P.ys[cell[1]]), op))
         416 +            cell = found[0]
         417 +            v -= 1
         418 +        seq.reverse()
         419 +        return seq
         420 +
         421 +    # ------------------------------------------------------------------
         422 +    def get_action(self, state):
         423 +        act = np.zeros(8, dtype=np.float32)
         424 +        sc = Scene(state)
         425 +        if self._deviated(sc) or (not self.actions[0] and not self.actions[1]):
         426 +            self.replans += 1
         427 +            if self.replans < 40:
         428 +                self._plan(state)
         429 +        for ri in range(2):
         430 +            r = sc.rovers["rover%d" % ri]
         431 +            if self.actions[ri]:
         432 +                x, y, op = self.actions[ri].pop(0)
         433 +                dx = float(np.clip(x - r["x"], -0.2, 0.2))
         434 +                dy = float(np.clip(y - r["y"], -0.2, 0.2))
         435 +                act[4 * ri] = dx
         436 +                act[4 * ri + 1] = dy
         437 +                act[4 * ri + 3] = SEL[op] if op else 0.0
         438 +                self.expect[ri] = (x, y, op)
         439 +            else:
         440 +                # at end: if at home do nothing
         441 +                self.expect[ri] = None
         442 +        return act
         443 +
         444 +    def _deviated(self, sc):
         445 +        dev = False
         446 +        for ri in range(2):
         447 +            e = self.expect[ri]
         448 +            if e is None:
         449 +                continue
         450 +            r = sc.rovers["rover%d" % ri]
         451 +            if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3:
         452 +                dev = True
         453 +            op = e[2]
         454 +            pr = self.prev_sc.rovers["rover%d" % ri]
         455 +            if op == "cal" and not r["cal"]:
         456 +                dev = True
         457 +            elif op == "img" and (r["cal"] or not pr["cal"]):
         458 +                dev = True
         459 +            elif op == "sample" and not r["full"]:
         460 +                dev = True
         461 +            elif op == "drop" and r["full"]:
         462 +                dev = True
         463 +            elif op == "send":
         464 +                for ob in sc.objectives:
         465 +                    if ob["img"][ri] and not ob["recv"]:
         466 +                        dev = True
         467 +                for s in sc.samples:
         468 +                    if s["an"][ri] and not s["recv"]:
         469 +                        dev = True
         470 +        self.prev_sc = sc
         471 +        self.expect = [None, None]
         472 +        return dev
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..6c4f3aa
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,26 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +def run(seed, verbose=False):
           6 +    env = make_env()
           7 +    obs, info = env.reset(seed=seed)
           8 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +    t0=time.time(); ap.reset(obs, info); tp=time.time()-t0
          10 +    steps=0; term=False
          11 +    while steps < env.max_steps:
          12 +        a = ap.get_action(obs)
          13 +        obs, r, term, trunc, info = env.step(a)
          14 +        steps += 1
          15 +        if term or trunc: break
          16 +    tt=time.time()-t0
          17 +    env.close()
          18 +    return seed, info.get('object_count') if isinstance(info,dict) else None, term, steps, ap.replans, round(tp,2), round(tt,1)
          19 +if __name__ == "__main__":
          20 +    seeds = range(int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv)>2 else range(10)
          21 +    from concurrent.futures import ThreadPoolExecutor
          22 +    with ThreadPoolExecutor(8) as ex:
          23 +        res = list(ex.map(run, seeds))
          24 +    for r in res: print(r)
          25 +    ok=[r for r in res if r[2]]
          26 +    print("solved", len(ok), "/", len(res), "mean steps", np.mean([r[3] for r in ok]) if ok else None)
```

</details>

<a id="C007"></a>
### C007 · fix sample region ambiguity; stricter deviation checks

Commit `ea4a1c5462a0ba9bbdc452e2c0a2176b665e2b85`; parents: d4c816ce110c4e091102cc8f8237a52e37544d78. Recorded author date: 2026-10-01T11:07:30+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0644](01_timeline.md#E0644): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_ea4a1c5_approach.py) · [Exact all-file diff](evidence/diffs/C007_ea4a1c5.diff)

[Previous saved controller snapshot](evidence/versions/C006_d4c816c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f58760c..b9506c2 100644
--- a/approach.py
+++ b/approach.py
@@ -199,11 +199,15 @@ class RoverPlanner:
  199    199          self.land = v & ((~occ) | back) & ~occ2 & free
  200    200          # samples
  201    201          self.sreg = {}
         202 +        dk = {}
  202    203          for kind in ("stone", "soil"):
  203        -            r = np.zeros(X.shape, dtype=bool)
         204 +            d = np.full(X.shape, 1e9)
  204    205              for sm in scene.samples:
  205    206                  if sm["soil"] == (kind == "soil"):
  206        -                    r |= np.hypot(sm["x"] - X, sm["y"] - Y) <= SAMPLE_R
         207 +                    d = np.minimum(d, np.hypot(sm["x"] - X, sm["y"] - Y))
         208 +            dk[kind] = d
         209 +        for kind, oth in (("stone", "soil"), ("soil", "stone")):
         210 +            r = (dk[kind] <= SAMPLE_R) & ((dk[oth] > 0.26) | (dk[oth] > dk[kind] + 0.03))
  207    211              self.sreg[kind] = r & free
  208    212  
  209    213      def cell_of(self, x, y):
@@ -239,6 +243,7 @@ class GeneratedApproach:
  239    243          self.fail_count = 0
  240    244          self.expect = [None, None]
  241    245          self.prev_sc = sc
         246 +        self.log = []
  242    247          self._plan(state)
  243    248  
  244    249      # ------------------------------------------------------------------
@@ -373,6 +378,7 @@ class GeneratedApproach:
  373    378                          continue
  374    379                      key = (max(costs[0][0], costs[1][0]), costs[0][0] + costs[1][0])
  375    380                      if best is None or key < best[0]:
         381 +                        self.pred = key
  376    382                          best = (key, costs)
  377    383          self.actions = [[], []]
  378    384          if best is None:
@@ -396,7 +402,7 @@ class GeneratedApproach:
  396    402                  break
  397    403              if name != "start" and G[cell] == v:
  398    404                  Fp = stages[k - 1][3]
  399        -                op = name
         405 +                op = (name, arg)
  400    406                  k -= 1
  401    407                  Fsrc = Fp
  402    408              else:
@@ -434,7 +440,7 @@ class GeneratedApproach:
  434    440                  dy = float(np.clip(y - r["y"], -0.2, 0.2))
  435    441                  act[4 * ri] = dx
  436    442                  act[4 * ri + 1] = dy
  437        -                act[4 * ri + 3] = SEL[op] if op else 0.0
         443 +                act[4 * ri + 3] = SEL[op[0]] if op else 0.0
  438    444                  self.expect[ri] = (x, y, op)
  439    445              else:
  440    446                  # at end: if at home do nothing
@@ -450,8 +456,16 @@ class GeneratedApproach:
  450    456              r = sc.rovers["rover%d" % ri]
  451    457              if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3:
  452    458                  dev = True
  453        -            op = e[2]
         459 +                self.log.append(("move", ri, e, r["x"], r["y"]))
         460 +            op, arg = e[2] if e[2] else (None, None)
  454    461              pr = self.prev_sc.rovers["rover%d" % ri]
         462 +            if op == "img":
         463 +                ob = sc.objectives[arg]
         464 +                if not ob["img"][ri]:
         465 +                    dev = True
         466 +            if op == "sample":
         467 +                if not any(s["an"][ri] for s in sc.samples if s["soil"] == (arg == "soil")):
         468 +                    dev = True
  455    469              if op == "cal" and not r["cal"]:
  456    470                  dev = True
  457    471              elif op == "img" and (r["cal"] or not pr["cal"]):
@@ -467,6 +481,8 @@ class GeneratedApproach:
  467    481                  for s in sc.samples:
  468    482                      if s["an"][ri] and not s["recv"]:
  469    483                          dev = True
         484 +        if dev:
         485 +            self.log.append(("dev", ri, e))
  470    486          self.prev_sc = sc
  471    487          self.expect = [None, None]
  472    488          return dev
diff --git a/dbg.py b/dbg.py
new file mode 100644
index 0000000..efd236c
--- /dev/null
+++ b/dbg.py
@@ -0,0 +1,13 @@
           1 +import sys
           2 +from test_approach import *
           3 +import approach
           4 +for seed in map(int, sys.argv[1:]):
           5 +    env = make_env(); obs, info = env.reset(seed=seed)
           6 +    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +    print("seed",seed,"pred",ap.pred, [len(a) for a in ap.actions])
           8 +    steps=0
           9 +    while steps<300:
          10 +        obs,r,term,tr,info=env.step(ap.get_action(obs)); steps+=1
          11 +        if term: break
          12 +    print(" steps",steps,term, "pred", ap.pred, ap.log[:6])
          13 +    env.close()
diff --git a/dbg2.py b/dbg2.py
new file mode 100644
index 0000000..3cac6f0
--- /dev/null
+++ b/dbg2.py
@@ -0,0 +1,15 @@
           1 +import sys
           2 +from test_approach import *
           3 +for seed in map(int, sys.argv[1:]):
           4 +    env = make_env(); obs, info = env.reset(seed=seed)
           5 +    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           6 +    steps=0
           7 +    while True:
           8 +        if not ap.actions[0] and not ap.actions[1]:
           9 +            for o in obs:
          10 +                if o.type.name in ('rover','objective') or (o.type.name=='sample'): print(' ',o.name,[round(float(v),2) for v in obs.data[o]])
          11 +            break
          12 +        obs,r,term,tr,info=env.step(ap.get_action(obs)); steps+=1
          13 +        if term: break
          14 +    print(seed, steps, term)
          15 +    env.close()
diff --git a/dbg3.py b/dbg3.py
new file mode 100644
index 0000000..7aed2d0
--- /dev/null
+++ b/dbg3.py
@@ -0,0 +1,8 @@
           1 +import sys
           2 +from test_approach import *
           3 +seed=int(sys.argv[1])
           4 +env = make_env(); obs, info = env.reset(seed=seed)
           5 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           6 +for ri in range(2):
           7 +    print(ri, [(round(x,2),round(y,2),op) for x,y,op in ap.actions[ri]])
           8 +env.close()
```

</details>

<a id="C008"></a>
### C008 · liberal competitor test for image nearest rule

Commit `d4dd7ed6ae07462d1a0729c58fcc9e0a0ad3e20a`; parents: ea4a1c5462a0ba9bbdc452e2c0a2176b665e2b85. Recorded author date: 2026-10-01T11:08:00+02:00.

File roles (automatic): policy.

- [E0657](01_timeline.md#E0657): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_d4dd7ed_approach.py) · [Exact all-file diff](evidence/diffs/C008_d4dd7ed.diff)

[Previous saved controller snapshot](evidence/versions/C007_ea4a1c5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b9506c2..c62e526 100644
--- a/approach.py
+++ b/approach.py
@@ -226,7 +226,7 @@ class RoverPlanner:
  226    226          for m in range(len(self.vis)):
  227    227              if m == k or m in imaged:
  228    228                  continue
  229        -            reg &= ~(self.vis[m] & (self.objd[m] < dk))
         229 +            reg &= ~((self.objd[m] <= 2.03) & (self.objd[m] < dk + 0.03))
  230    230          return reg
  231    231  
  232    232  
@@ -453,6 +453,8 @@ class GeneratedApproach:
  453    453              e = self.expect[ri]
  454    454              if e is None:
  455    455                  continue
         456 +            d0 = dev
         457 +            dev = False
  456    458              r = sc.rovers["rover%d" % ri]
  457    459              if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3:
  458    460                  dev = True
@@ -481,8 +483,10 @@ class GeneratedApproach:
  481    483                  for s in sc.samples:
  482    484                      if s["an"][ri] and not s["recv"]:
  483    485                          dev = True
  484        -        if dev:
  485        -            self.log.append(("dev", ri, e))
         486 +            if dev:
         487 +                self.log.append(("dev", ri, e, round(r["x"], 3), round(r["y"], 3), r["cal"], pr["cal"],
         488 +                                 [ob["img"][ri] for ob in sc.objectives]))
         489 +            dev = dev or d0
  486    490          self.prev_sc = sc
  487    491          self.expect = [None, None]
  488    492          return dev
```

</details>

<a id="C009"></a>
### C009 · time-aware send stage vs other rover trajectory

Commit `b9fe270b9dae08ac78db8cef02bbfec6f2079400`; parents: d4dd7ed6ae07462d1a0729c58fcc9e0a0ad3e20a. Recorded author date: 2026-10-01T11:09:45+02:00.

File roles (automatic): policy, support code (role needs review).

- [E0666](01_timeline.md#E0666): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_b9fe270_approach.py) · [Exact all-file diff](evidence/diffs/C009_b9fe270.diff)

[Previous saved controller snapshot](evidence/versions/C008_d4dd7ed_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c62e526..cb23b47 100644
--- a/approach.py
+++ b/approach.py
@@ -386,6 +386,41 @@ class GeneratedApproach:
  386    386          for ri in range(2):
  387    387              P = tabs[ri][0]
  388    388              self.actions[ri] = self._extract(P, best[1][ri][1])
         389 +        # time-aware re-plan of final send against other rover's trajectory
         390 +        trajs = []
         391 +        for ri in range(2):
         392 +            r = sc.rovers["rover%d" % ri]
         393 +            trajs.append([(r["x"], r["y"])] + [(a[0], a[1]) for a in self.actions[ri]])
         394 +        new_actions = list(self.actions)
         395 +        for ri in range(2):
         396 +            stages = best[1][ri][1]
         397 +            if stages[-1][0] != "send":
         398 +                continue
         399 +            P = tabs[ri][0]
         400 +            Fprev = stages[-2][3]
         401 +            G0 = op_stage(Fprev, P.land)
         402 +            other = trajs[1 - ri]
         403 +            G = np.full(G0.shape, INF, dtype=G0.dtype)
         404 +            pending_mask = G0 < INF
         405 +            tmin = int(G0[pending_mask].min()) if pending_mask.any() else INF
         406 +            lx, ly = sc.lander
         407 +            t = tmin
         408 +            while pending_mask.any() and t < tmin + 200:
         409 +                ox, oy = other[min(t, len(other) - 1)]
         410 +                blk = seg_hits_disk(P.X, P.Y, lx, ly, ox, oy, ROVER_OCC_R) | \
         411 +                    seg_hits_disk(P.camx, P.camy, lx, ly, ox, oy, ROVER_OCC_R)
         412 +                ok = pending_mask & (G0 <= t) & ~blk
         413 +                G[ok] = t
         414 +                pending_mask &= ~ok
         415 +                if t >= len(other) - 1 and not ok.any() and (G0 <= t).all():
         416 +                    break
         417 +                t += 1
         418 +            F2 = propagate(G, P.free)
         419 +            if F2[(P.hi, P.hj)] >= INF:
         420 +                continue
         421 +            st = stages[:-1] + [("send", None, G, F2)]
         422 +            new_actions[ri] = self._extract(P, st)
         423 +        self.actions = new_actions
  389    424  
  390    425      def _extract(self, P, stages):
  391    426          """Backtrack through stage fields; returns list of (x,y,op) targets."""
diff --git a/dbg4.py b/dbg4.py
new file mode 100644
index 0000000..38f027b
--- /dev/null
+++ b/dbg4.py
@@ -0,0 +1,15 @@
           1 +import sys
           2 +from test_approach import *
           3 +seed=int(sys.argv[1])
           4 +env = make_env(); obs, info = env.reset(seed=seed)
           5 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           6 +for o in obs:
           7 +    if o.type.name=='obstacle' and obs.get(o,'half_x')<0.1: print(o.name, round(obs.get(o,'x'),2), round(obs.get(o,'y'),2))
           8 +steps=0
           9 +while True:
          10 +    n=len(ap.log)
          11 +    a=ap.get_action(obs)
          12 +    if len(ap.log)>n:
          13 +        r1=obs.get_object_from_name('rover1'); print('step',steps,'rover1 at', obs.get(r1,'x'), obs.get(r1,'y'), ap.log[-1]); break
          14 +    obs,r,term,tr,info=env.step(a); steps+=1
          15 +    if term: break
```

</details>

<a id="C010"></a>
### C010 · lander range from cam too; bigger rover occluder

Commit `64756f629d5570c0808d1a1b5e7927b09ca48406`; parents: b9fe270b9dae08ac78db8cef02bbfec6f2079400. Recorded author date: 2026-10-01T11:13:00+02:00.

File roles (automatic): policy.

- [E0740](01_timeline.md#E0740): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_64756f6_approach.py) · [Exact all-file diff](evidence/diffs/C010_64756f6.diff)

[Previous saved controller snapshot](evidence/versions/C009_b9fe270_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index cb23b47..e998528 100644
--- a/approach.py
+++ b/approach.py
@@ -23,7 +23,7 @@ LANDER_RANGE = 3.95
   23     23  SAMPLE_R = 0.235
   24     24  PILLAR_INFL_OBJ = 0.03
   25     25  PILLAR_INFL_LAND = 0.04
   26        -ROVER_OCC_R = 0.27
          26 +ROVER_OCC_R = 0.36
   27     27  CAM_OFF = (-0.087, -0.0125)
   28     28  OBJ_BACK_DEG = 108.0     # if |rel bearing| > this, pillars don't occlude objectives
   29     29  LAND_BACK_DEG = 110.0    # same quirk for lander (sending)
@@ -181,7 +181,8 @@ class RoverPlanner:
  181    181              self.any_vis |= v
  182    182          # lander visibility
  183    183          lx, ly = scene.lander
  184        -        v = np.hypot(lx - X, ly - Y) <= LANDER_RANGE
         184 +        v = (np.hypot(lx - X, ly - Y) <= LANDER_RANGE) & \
         185 +            (np.hypot(lx - self.camx, ly - self.camy) <= LANDER_RANGE)
  185    186          occ = np.zeros(X.shape, dtype=bool)
  186    187          for (cx, cy, ax, ay) in scene.pillars:
  187    188              e = PILLAR_INFL_LAND
```

</details>

<a id="C011"></a>
### C011 · backtrack with waiting; timed send stage

Commit `24ccf4a051fcd084d7dade8297bcfeade432d4db`; parents: 64756f629d5570c0808d1a1b5e7927b09ca48406. Recorded author date: 2026-10-01T11:17:09+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0802](01_timeline.md#E0802): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_24ccf4a_approach.py) · [Exact all-file diff](evidence/diffs/C011_24ccf4a.diff)

[Previous saved controller snapshot](evidence/versions/C010_64756f6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e998528..b32ce48 100644
--- a/approach.py
+++ b/approach.py
@@ -419,43 +419,54 @@ class GeneratedApproach:
  419    419              F2 = propagate(G, P.free)
  420    420              if F2[(P.hi, P.hj)] >= INF:
  421    421                  continue
  422        -            st = stages[:-1] + [("send", None, G, F2)]
         422 +            st = stages[:-1] + [("send_t", None, G, F2)]
  423    423              new_actions[ri] = self._extract(P, st)
  424    424          self.actions = new_actions
  425    425  
  426    426      def _extract(self, P, stages):
  427        -        """Backtrack through stage fields; returns list of (x,y,op) targets."""
  428        -        hcell = (P.hi, P.hj)
  429        -        cell = hcell
         427 +        """Backtrack through stage fields (waiting allowed); list of (x,y,op)."""
         428 +        cell = (P.hi, P.hj)
  430    429          k = len(stages) - 1
  431        -        v = stages[k][3][cell]
         430 +        v = int(stages[k][3][cell])
  432    431          seq = []
  433    432          W = WIN
  434    433          nx, ny = P.free.shape
  435        -        while True:
  436        -            name, arg, G, F = stages[k]
  437        -            if k == 0 and v == 0:
  438        -                break
  439        -            if name != "start" and G[cell] == v:
  440        -                Fp = stages[k - 1][3]
  441        -                op = (name, arg)
  442        -                k -= 1
  443        -                Fsrc = Fp
  444        -            else:
  445        -                op = None
  446        -                Fsrc = F
  447        -            found = None
  448        -            i, j = cell
         434 +
         435 +        def nb(Fsrc, i, j, cond):
         436 +            best = None
  449    437              for di in range(-W, W + 1):
  450    438                  for dj in range(-W, W + 1):
  451    439                      a, b = i + di, j + dj
  452        -                    if 0 <= a < nx and 0 <= b < ny and Fsrc[a, b] == v - 1:
  453        -                        if found is None or abs(di) + abs(dj) < found[1]:
  454        -                            found = ((a, b), abs(di) + abs(dj))
  455        -            if found is None:
         440 +                    if 0 <= a < nx and 0 <= b < ny and cond(Fsrc[a, b]):
         441 +                        c = abs(di) + abs(dj)
         442 +                        if best is None or c < best[1]:
         443 +                            best = ((a, b), c)
         444 +            return best[0] if best else None
         445 +
         446 +        guard = 0
         447 +        while not (k == 0 and v == 0) and guard < 5000:
         448 +            guard += 1
         449 +            name, arg, G, F = stages[k]
         450 +            i, j = cell
         451 +            timed = name == "send_t"
         452 +            choice = None
         453 +            for mode in (0, 1):
         454 +                if k > 0:
         455 +                    okop = (G[cell] == v) if (mode == 0 or timed) else (G[cell] <= v)
         456 +                    if okop:
         457 +                        Fp = stages[k - 1][3]
         458 +                        c = nb(Fp, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
         459 +                        if c is not None:
         460 +                            choice = (c, (name.replace("_t", ""), arg), k - 1)
         461 +                            break
         462 +                c = nb(F, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
         463 +                if c is not None:
         464 +                    choice = (c, None, k)
         465 +                    break
         466 +            if choice is None:
  456    467                  break
  457        -            seq.append((float(P.xs[cell[0]]), float(P.ys[cell[1]]), op))
  458        -            cell = found[0]
         468 +            seq.append((float(P.xs[cell[0]]), float(P.ys[cell[1]]), choice[1]))
         469 +            cell, k = choice[0], choice[2]
  459    470              v -= 1
  460    471          seq.reverse()
  461    472          return seq
diff --git a/dbg5.py b/dbg5.py
new file mode 100644
index 0000000..17410aa
--- /dev/null
+++ b/dbg5.py
@@ -0,0 +1,8 @@
           1 +import sys
           2 +from test_approach import *
           3 +seed=int(sys.argv[1])
           4 +env = make_env(); obs, info = env.reset(seed=seed)
           5 +for o in obs:
           6 +    print(o.name, [round(float(v),2) for v in obs.data[o]])
           7 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           8 +print([len(a) for a in ap.actions], getattr(ap,'pred',None))
diff --git a/probe_occ_fit.py b/probe_occ_fit.py
new file mode 100644
index 0000000..a0020fe
--- /dev/null
+++ b/probe_occ_fit.py
@@ -0,0 +1,18 @@
           1 +import numpy as np, math, re, sys, ast
           2 +recs=[]
           3 +for line in open(sys.argv[1]):
           4 +    if not line.startswith('((('): continue
           5 +    j,r=ast.literal_eval(line.strip())
           6 +    if r.get('i') in (None,0): continue
           7 +    P0,Q,h,d=j; b=((r['p1'][0]+r['prev'][0])/2,(r['p1'][1]+r['prev'][1])/2)
           8 +    recs.append((r['p0'],b,h,d))
           9 +def segd(p,a,b):
          10 +    a,b,p=map(np.array,(a,b,p)); t=np.clip(np.dot(p-a,b-a)/np.dot(b-a,b-a),0,1); 
          11 +    v=p-(a+t*(b-a)); return np.linalg.norm(v), np.sign(np.cross(b-a,p-a))
          12 +def cam(p0):
          13 +    x,y,th=p0; c,s=math.cos(th),math.sin(th); return (x+c*-0.087-s*-0.0125, y+s*-0.087+c*-0.0125)
          14 +L=(-1.9,-2.0)
          15 +for name,src in [('centre',lambda p:p[:2]),('cam',cam)]:
          16 +    print(name)
          17 +    for p0,b,h,d in recs:
          18 +        dist,sg=segd(b,src(p0),L); print('  ',p0[:2],b,h,d,round(dist*sg,4))
diff --git a/probe_occ_lib.py b/probe_occ_lib.py
new file mode 100644
index 0000000..841a475
--- /dev/null
+++ b/probe_occ_lib.py
@@ -0,0 +1,28 @@
           1 +from probe_send_lib import E, SEL
           2 +import numpy as np, math, time
           3 +def setup(seed, P0, th0, Q, h1, wp1=()):
           4 +    e=E(seed)
           5 +    # rover1 to Q via waypoints
           6 +    for w in list(wp1)+[Q]:
           7 +        if not e.goto(1,*w,tol=1e-4,maxit=100): return e,'r1 blocked at %s'%(e.pose(1),)
           8 +    e.turn(1,h1)
           9 +    # rover0 sample
          10 +    if not e.goto(0,1.28,-0.95+0.0,tol=1e-3): return e,'r0 blocked to sample'
          11 +    e.act(0,(0,0,0),SEL['sample'])
          12 +    if e.g('rover0','store_full')<0.5: return e,'sample failed'
          13 +    if not e.goto(0,*P0,tol=1e-4): return e,'r0 blocked to P0 %s'%(e.pose(0),)
          14 +    e.turn(0,th0)
          15 +    return e,None
          16 +def sweep(seed,P0,th0,Q,h1,d,step=0.004,n=60,wp1=()):
          17 +    e,err=setup(seed,P0,th0,Q,h1,wp1)
          18 +    if err: return dict(err=err)
          19 +    p0=e.pose(0); hist=[]
          20 +    for i in range(n):
          21 +        before=e.pose(1)
          22 +        mv=(d[0]*step,d[1]*step,0) if i>0 else (0,0,0)
          23 +        e.step((0,0,0,SEL['send']),mv+(0,))
          24 +        p1=e.pose(1)
          25 +        if i>0 and (d[0] or d[1]) and abs(p1[0]-before[0])+abs(p1[1]-before[1])<1e-7: return dict(err='r1 stuck',p0=p0,p1=p1)
          26 +        if e.feats('sample5')[6]>0.5:
          27 +            return dict(i=i,p0=p0,p1=p1,prev=before if i>0 else None)
          28 +    return dict(i=None,p0=p0,p1=e.pose(1))
diff --git a/probe_occ_run1.out b/probe_occ_run1.out
new file mode 100644
index 0000000..e69de29
diff --git a/probe_occ_run1.py b/probe_occ_run1.py
new file mode 100644
index 0000000..609220b
--- /dev/null
+++ b/probe_occ_run1.py
@@ -0,0 +1,16 @@
           1 +from probe_occ_lib import *
           2 +from concurrent.futures import ThreadPoolExecutor
           3 +import json,sys
           4 +L=(-1.9,-2.0)
           5 +def online(P0,x):
           6 +    t=(x-P0[0])/(L[0]-P0[0]); return (x,round(P0[1]+t*(L[1]-P0[1]),4))
           7 +G=[((0.6,-0.35),-1.0),((0.6,-1.9),-0.8),((1.2,0.0),-0.5),((0.6,-0.35),-1.2),((0.6,-0.35),-0.3)]
           8 +jobs=[]
           9 +for P0,x in G:
          10 +    for dy in (1,-1):
          11 +        jobs.append((P0,online(P0,x),0.0,(0,dy)))
          12 +def f(j):
          13 +    P0,Q,h,d=j
          14 +    return j, sweep(44,P0,math.pi,Q,h,d,step=0.005,n=90)
          15 +with ThreadPoolExecutor(10) as ex:
          16 +    for r in ex.map(f,jobs): print(r,flush=True)
diff --git a/probe_occ_scan.py b/probe_occ_scan.py
new file mode 100644
index 0000000..53c5f52
--- /dev/null
+++ b/probe_occ_scan.py
@@ -0,0 +1,13 @@
           1 +from probe_send_lib import *
           2 +import time
           3 +t=time.time()
           4 +for seed in range(6):
           5 +    e=E(seed)
           6 +    out=[]
           7 +    for o in e.obs:
           8 +        if o.type.name in('sample','obstacle'):
           9 +            out.append((o.name[:6],round(e.g(o.name,'x'),2),round(e.g(o.name,'y'),2)))
          10 +    print(seed,out)
          11 +print(e.feats('rover0'), [o.name for o in e.obs][:3], time.time()-t)
          12 +for o in e.obs:
          13 +    if o.type.name=='sample': print(o.name, e.feats(o.name)); break
diff --git a/probe_occ_scan2.py b/probe_occ_scan2.py
new file mode 100644
index 0000000..fdb008c
--- /dev/null
+++ b/probe_occ_scan2.py
@@ -0,0 +1,15 @@
           1 +from probe_send_lib import *
           2 +from concurrent.futures import ThreadPoolExecutor
           3 +def f(seed):
           4 +    e=E(seed); pil=[];sm=[]
           5 +    for o in e.obs:
           6 +        n=o.name
           7 +        if o.type.name=='obstacle' and e.g(n,'half_x')<0.1: pil.append((round(e.g(n,'x'),2),round(e.g(n,'y'),2)))
           8 +        if o.type.name=='sample': sm.append((round(e.g(n,'x'),2),round(e.g(n,'y'),2)))
           9 +    e.env.close()
          10 +    bad=[p for p in pil if p[0]<1.0 and p[1]<0.3]
          11 +    rs=[s for s in sm if s[0]>0.1 and s[1]<0.5]
          12 +    return seed,len(bad),rs,bad
          13 +with ThreadPoolExecutor(12) as ex:
          14 +    for r in ex.map(f,range(6,66)):
          15 +        if r[1]<=1 and r[2]: print(r)
diff --git a/probe_occ_scan3.py b/probe_occ_scan3.py
new file mode 100644
index 0000000..c841fca
--- /dev/null
+++ b/probe_occ_scan3.py
@@ -0,0 +1,6 @@
           1 +from probe_send_lib import *
           2 +for seed in (44,54,61):
           3 +    e=E(seed)
           4 +    print(seed,[(round(e.g(o.name,'x'),2),round(e.g(o.name,'y'),2)) for o in e.obs if o.type.name=='obstacle' and e.g(o.name,'half_x')<0.1])
           5 +    o=e.obs.get_object_from_name('sample0'); print(e.obs.data[o].shape, [f for f in ['x','y','z']])
           6 +    e.env.close()
diff --git a/probe_occ_t1.py b/probe_occ_t1.py
new file mode 100644
index 0000000..e368d06
--- /dev/null
+++ b/probe_occ_t1.py
@@ -0,0 +1,5 @@
           1 +from probe_occ_lib import *
           2 +import time
           3 +t=time.time()
           4 +r=sweep(44,(0.6,-0.35),math.pi,(-1.0,-1.406),0.0,(0,1),step=0.01,n=40)
           5 +print(r,time.time()-t)
diff --git a/probe_occ_t2.py b/probe_occ_t2.py
new file mode 100644
index 0000000..a3aee48
--- /dev/null
+++ b/probe_occ_t2.py
@@ -0,0 +1,6 @@
           1 +from probe_occ_lib import *
           2 +from concurrent.futures import ThreadPoolExecutor
           3 +jobs=[((0.6,-0.35),(-0.5,0.0)),((0.6,-1.9),(-0.5,0.0)),((1.2,0.0),(-0.5,0.0)),((0.6,-0.35),(-1.0,-1.75))]
           4 +def f(j): return j, sweep(44,j[0],math.pi,j[1],0.0,(0,0),n=2)
           5 +with ThreadPoolExecutor(4) as ex:
           6 +    for r in ex.map(f,jobs): print(r)
diff --git a/probe_occ_t3.py b/probe_occ_t3.py
new file mode 100644
index 0000000..ec01b53
--- /dev/null
+++ b/probe_occ_t3.py
@@ -0,0 +1,7 @@
           1 +from probe_occ_lib import *
           2 +from probe_send_lib import diff
           3 +e,err=setup(44,(0.6,-0.35),math.pi,(-0.5,0.0),0.0)
           4 +print(err,e.feats('rover0'))
           5 +a=e.flags()
           6 +e.step((0,0,0,SEL['send']),(0,0,0,0))
           7 +print(diff(a,e.flags()), e.last[0], e.last[3])
```

</details>

<a id="C012"></a>
### C012 · top-K realized assignment selection; timed send w/o static occluder

Commit `ab01758b6ccbc43055f1f67c3587cb4f466f8c65`; parents: 24ccf4a051fcd084d7dade8297bcfeade432d4db. Recorded author date: 2026-10-01T11:20:27+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0846](01_timeline.md#E0846): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_ab01758_approach.py) · [Exact all-file diff](evidence/diffs/C012_ab01758.diff)

[Previous saved controller snapshot](evidence/versions/C011_24ccf4a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b32ce48..a4d64cf 100644
--- a/approach.py
+++ b/approach.py
@@ -198,6 +198,7 @@ class RoverPlanner:
  198    198              occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
  199    199              occ2 |= seg_hits_disk(self.camx, self.camy, lx, ly, px, py, ROVER_OCC_R)
  200    200          self.land = v & ((~occ) | back) & ~occ2 & free
         201 +        self.land_free = v & ((~occ) | back) & free
  201    202          # samples
  202    203          self.sreg = {}
  203    204          dk = {}
@@ -358,6 +359,7 @@ class GeneratedApproach:
  358    359                                             pending[ri]))
  359    360          # joint assignment
  360    361          best = None
         362 +        cands = []
  361    363          n = len(need_objs)
  362    364          stone_opts = [0, 1] if need["stone"] else [None]
  363    365          soil_opts = [0, 1] if need["soil"] else [None]
@@ -378,28 +380,49 @@ class GeneratedApproach:
  378    380                      if costs[0] is None or costs[1] is None:
  379    381                          continue
  380    382                      key = (max(costs[0][0], costs[1][0]), costs[0][0] + costs[1][0])
         383 +                    cands.append((key, costs))
  381    384                      if best is None or key < best[0]:
  382    385                          self.pred = key
  383    386                          best = (key, costs)
  384    387          self.actions = [[], []]
  385    388          if best is None:
  386    389              return
         390 +        cands.sort(key=lambda c: c[0])
         391 +        seen = set()
         392 +        bestreal = None
         393 +        for key, costs in cands:
         394 +            sig = (id(costs[0][1]), id(costs[1][1]))
         395 +            if sig in seen:
         396 +                continue
         397 +            seen.add(sig)
         398 +            if len(seen) > 6 or (bestreal is not None and key[0] >= bestreal[0][0]):
         399 +                break
         400 +            acts = self._realize(sc, tabs, costs)
         401 +            real = (max(len(acts[0]), len(acts[1])), len(acts[0]) + len(acts[1]))
         402 +            if bestreal is None or real < bestreal[0]:
         403 +                bestreal = (real, acts)
         404 +        self.actions = bestreal[1]
         405 +
         406 +    def _realize(self, sc, tabs, costs):
         407 +        best = (None, costs)
         408 +        actions = [[], []]
         409 +        sc = self.scene
  387    410          for ri in range(2):
  388    411              P = tabs[ri][0]
  389        -            self.actions[ri] = self._extract(P, best[1][ri][1])
         412 +            actions[ri] = self._extract(P, best[1][ri][1])
  390    413          # time-aware re-plan of final send against other rover's trajectory
  391    414          trajs = []
  392    415          for ri in range(2):
  393    416              r = sc.rovers["rover%d" % ri]
  394        -            trajs.append([(r["x"], r["y"])] + [(a[0], a[1]) for a in self.actions[ri]])
  395        -        new_actions = list(self.actions)
         417 +            trajs.append([(r["x"], r["y"])] + [(a[0], a[1]) for a in actions[ri]])
         418 +        new_actions = list(actions)
  396    419          for ri in range(2):
  397    420              stages = best[1][ri][1]
  398    421              if stages[-1][0] != "send":
  399    422                  continue
  400    423              P = tabs[ri][0]
  401    424              Fprev = stages[-2][3]
  402        -            G0 = op_stage(Fprev, P.land)
         425 +            G0 = op_stage(Fprev, P.land_free)
  403    426              other = trajs[1 - ri]
  404    427              G = np.full(G0.shape, INF, dtype=G0.dtype)
  405    428              pending_mask = G0 < INF
@@ -421,7 +444,7 @@ class GeneratedApproach:
  421    444                  continue
  422    445              st = stages[:-1] + [("send_t", None, G, F2)]
  423    446              new_actions[ri] = self._extract(P, st)
  424        -        self.actions = new_actions
         447 +        return new_actions
  425    448  
  426    449      def _extract(self, P, stages):
  427    450          """Backtrack through stage fields (waiting allowed); list of (x,y,op)."""
diff --git a/probe_occ_run1.out b/probe_occ_run1.out
index e69de29..9556cdc 100644
--- a/probe_occ_run1.out
+++ b/probe_occ_run1.out
@@ -0,0 +1,10 @@
           1 +(((0.6, -0.35), (-1.0, -1.406), 0.0, (0, 1)), {'i': 40, 'p0': (0.6, -0.35, -3.1416), 'p1': (-1.0, -1.206, 0.0), 'prev': (-1.0, -1.211, 0.0)})
           2 +(((0.6, -0.35), (-1.0, -1.406), 0.0, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-1.0, -1.641, 0.0), 'prev': (-1.0, -1.636, 0.0)})
           3 +(((0.6, -1.9), (-0.8, -1.956), 0.0, (0, 1)), {'i': 38, 'p0': (0.6, -1.9, -3.1416), 'p1': (-0.8, -1.766, 0.0), 'prev': (-0.8, -1.771, 0.0)})
           4 +(((0.6, -1.9), (-0.8, -1.956), 0.0, (0, -1)), {'i': 36, 'p0': (0.6, -1.9, -3.1416), 'p1': (-0.8, -2.136, 0.0), 'prev': (-0.8, -2.131, 0.0)})
           5 +(((1.2, 0.0), (-0.5, -1.0968), 0.0, (0, 1)), {'i': 49, 'p0': (1.2, 0.0, -3.1416), 'p1': (-0.5, -0.8518, 0.0), 'prev': (-0.5, -0.8568, 0.0)})
           6 +(((1.2, 0.0), (-0.5, -1.0968), 0.0, (0, -1)), {'i': 47, 'p0': (1.2, 0.0, -3.1416), 'p1': (-0.5, -1.3318, 0.0), 'prev': (-0.5, -1.3268, 0.0)})
           7 +(((0.6, -0.35), (-1.2, -1.538), 0.0, (0, 1)), {'i': 41, 'p0': (0.6, -0.35, -3.1416), 'p1': (-1.2, -1.333, 0.0), 'prev': (-1.2, -1.338, 0.0)})
           8 +(((0.6, -0.35), (-1.2, -1.538), 0.0, (0, -1)), {'i': 46, 'p0': (0.6, -0.35, -3.1416), 'p1': (-1.2, -1.768, 0.0), 'prev': (-1.2, -1.763, 0.0)})
           9 +(((0.6, -0.35), (-0.3, -0.944), 0.0, (0, 1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -0.709, 0.0), 'prev': (-0.3, -0.714, 0.0)})
          10 +(((0.6, -0.35), (-0.3, -0.944), 0.0, (0, -1)), {'i': 34, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -1.114, 0.0), 'prev': (-0.3, -1.109, 0.0)})
diff --git a/probe_occ_run2.out b/probe_occ_run2.out
new file mode 100644
index 0000000..a87a5a3
--- /dev/null
+++ b/probe_occ_run2.out
@@ -0,0 +1,18 @@
           1 +(((0.6, -0.35), (-1.0, -1.406), 1.5707963267948966, (0, 1)), {'i': 40, 'p0': (0.6, -0.35, -3.1416), 'p1': (-1.0, -1.206, 1.5708), 'prev': (-1.0, -1.211, 1.5708)})
           2 +(((0.6, -0.35), (-1.0, -1.406), 1.5707963267948966, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-1.0, -1.641, 1.5708), 'prev': (-1.0, -1.636, 1.5708)})
           3 +(((0.6, -0.35), (-1.0, -1.406), 3.141592653589793, (0, 1)), {'i': 40, 'p0': (0.6, -0.35, -3.1416), 'p1': (-1.0, -1.206, -3.1416), 'prev': (-1.0, -1.211, -3.1416)})
           4 +(((0.6, -0.35), (-1.0, -1.406), 3.141592653589793, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-1.0, -1.641, -3.1416), 'prev': (-1.0, -1.636, -3.1416)})
           5 +(((0.6, -0.35), (-1.0, -1.406), -1.5707963267948966, (0, 1)), {'i': 40, 'p0': (0.6, -0.35, -3.1416), 'p1': (-1.0, -1.206, -1.5708), 'prev': (-1.0, -1.211, -1.5708)})
           6 +(((0.6, -0.35), (-1.0, -1.406), -1.5707963267948966, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-1.0, -1.641, -1.5708), 'prev': (-1.0, -1.636, -1.5708)})
           7 +(((1.2, 0.0), (-0.5, -1.0968), 1.5707963267948966, (0, 1)), {'i': 37, 'p0': (1.2, 0.0, -3.1416), 'p1': (-0.5, -0.9118, 1.5708), 'prev': (-0.5, -0.9168, 1.5708)})
           8 +(((1.2, 0.0), (-0.5, -1.0968), 1.5707963267948966, (0, -1)), {'i': 47, 'p0': (1.2, 0.0, -3.1416), 'p1': (-0.5, -1.3318, 1.5708), 'prev': (-0.5, -1.3268, 1.5708)})
           9 +(((1.2, 0.0), (-0.5, -1.0968), 3.141592653589793, (0, 1)), {'i': 46, 'p0': (1.2, 0.0, -3.1416), 'p1': (-0.5, -0.8668, -3.1416), 'prev': (-0.5, -0.8718, -3.1416)})
          10 +(((1.2, 0.0), (-0.5, -1.0968), 3.141592653589793, (0, -1)), {'i': 47, 'p0': (1.2, 0.0, -3.1416), 'p1': (-0.5, -1.3318, -3.1416), 'prev': (-0.5, -1.3268, -3.1416)})
          11 +(((1.2, 0.0), (-0.5, -1.0968), -1.5707963267948966, (0, 1)), {'i': 46, 'p0': (1.2, 0.0, -3.1416), 'p1': (-0.5, -0.8668, -1.5708), 'prev': (-0.5, -0.8718, -1.5708)})
          12 +(((1.2, 0.0), (-0.5, -1.0968), -1.5707963267948966, (0, -1)), {'i': 47, 'p0': (1.2, 0.0, -3.1416), 'p1': (-0.5, -1.3318, -1.5708), 'prev': (-0.5, -1.3268, -1.5708)})
          13 +(((0.6, -0.35), (-0.3, -0.944), 1.5707963267948966, (0, 1)), {'i': 46, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -0.714, 1.5708), 'prev': (-0.3, -0.719, 1.5708)})
          14 +(((0.6, -0.35), (-0.3, -0.944), 1.5707963267948966, (0, -1)), {'i': 22, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -1.054, 1.5708), 'prev': (-0.3, -1.049, 1.5708)})
          15 +(((0.6, -0.35), (-0.3, -0.944), 3.141592653589793, (0, 1)), {'i': 48, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -0.704, -3.1416), 'prev': (-0.3, -0.709, -3.1416)})
          16 +(((0.6, -0.35), (-0.3, -0.944), 3.141592653589793, (0, -1)), {'i': 34, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -1.114, -3.1416), 'prev': (-0.3, -1.109, -3.1416)})
          17 +(((0.6, -0.35), (-0.3, -0.944), -1.5707963267948966, (0, 1)), {'i': 40, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -0.744, -1.5708), 'prev': (-0.3, -0.749, -1.5708)})
          18 +(((0.6, -0.35), (-0.3, -0.944), -1.5707963267948966, (0, -1)), {'i': 28, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -1.084, -1.5708), 'prev': (-0.3, -1.079, -1.5708)})
diff --git a/probe_occ_run2.py b/probe_occ_run2.py
new file mode 100644
index 0000000..5fbc5fa
--- /dev/null
+++ b/probe_occ_run2.py
@@ -0,0 +1,16 @@
           1 +from probe_occ_lib import *
           2 +from concurrent.futures import ThreadPoolExecutor
           3 +L=(-1.9,-2.0)
           4 +def online(P0,x):
           5 +    t=(x-P0[0])/(L[0]-P0[0]); return (x,round(P0[1]+t*(L[1]-P0[1]),4))
           6 +G=[((0.6,-0.35),-1.0),((1.2,0.0),-0.5),((0.6,-0.35),-0.3)]
           7 +jobs=[]
           8 +for P0,x in G:
           9 +  for h in (math.pi/2,math.pi,-math.pi/2):
          10 +    for dy in (1,-1):
          11 +        jobs.append((P0,online(P0,x),h,(0,dy)))
          12 +def f(j):
          13 +    P0,Q,h,d=j
          14 +    return j, sweep(44,P0,math.pi,Q,h,d,step=0.005,n=90)
          15 +with ThreadPoolExecutor(18) as ex:
          16 +    for r in ex.map(f,jobs): print(r,flush=True)
diff --git a/probe_occ_run3.out b/probe_occ_run3.out
new file mode 100644
index 0000000..e1ec254
--- /dev/null
+++ b/probe_occ_run3.out
@@ -0,0 +1,16 @@
           1 +(((0.6, -0.35), (-0.8, -1.274), 0.0, (0, 1)), {'i': 51, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.019, 0.0), 'prev': (-0.8, -1.024, 0.0)})
           2 +(((0.6, -0.35), (-0.8, -1.274), 0.0, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.509, 0.0), 'prev': (-0.8, -1.504, 0.0)})
           3 +(((0.6, -0.35), (-0.8, -1.274), 1.5707963267948966, (0, 1)), {'i': 38, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.084, 1.5708), 'prev': (-0.8, -1.089, 1.5708)})
           4 +(((0.6, -0.35), (-0.8, -1.274), 1.5707963267948966, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.509, 1.5708), 'prev': (-0.8, -1.504, 1.5708)})
           5 +(((0.6, -0.35), (-0.6, -1.142), 0.0, (0, 1)), {'i': 24, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.022, 0.0), 'prev': (-0.6, -1.027, 0.0)})
           6 +(((0.6, -0.35), (-0.6, -1.142), 0.0, (0, -1)), {'i': 54, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.412, 0.0), 'prev': (-0.6, -1.407, 0.0)})
           7 +(((0.6, -0.35), (-0.6, -1.142), 1.5707963267948966, (0, 1)), {'i': 12, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.082, 1.5708), 'prev': (-0.6, -1.087, 1.5708)})
           8 +(((0.6, -0.35), (-0.6, -1.142), 1.5707963267948966, (0, -1)), {'i': 51, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.397, 1.5708), 'prev': (-0.6, -1.392, 1.5708)})
           9 +(((0.6, -0.35), (-0.45, -1.043), 0.0, (0, 1)), {'i': 0, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.45, -1.043, 0.0), 'prev': None})
          10 +(((0.6, -0.35), (-0.45, -1.043), 0.0, (0, -1)), {'i': 0, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.45, -1.043, 0.0), 'prev': None})
          11 +(((0.6, -0.35), (-0.45, -1.043), 1.5707963267948966, (0, 1)), {'i': 0, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.45, -1.043, 1.5708), 'prev': None})
          12 +(((0.6, -0.35), (-0.45, -1.043), 1.5707963267948966, (0, -1)), {'i': 0, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.45, -1.043, 1.5708), 'prev': None})
          13 +(((0.6, -0.35), (-0.38, -0.9968), 0.0, (0, 1)), {'i': 0, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.38, -0.9968, 0.0), 'prev': None})
          14 +(((0.6, -0.35), (-0.38, -0.9968), 0.0, (0, -1)), {'i': 0, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.38, -0.9968, 0.0), 'prev': None})
          15 +(((0.6, -0.35), (-0.38, -0.9968), 1.5707963267948966, (0, 1)), {'i': 50, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.38, -0.7468, 1.5708), 'prev': (-0.38, -0.7518, 1.5708)})
          16 +(((0.6, -0.35), (-0.38, -0.9968), 1.5707963267948966, (0, -1)), {'i': 12, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.38, -1.0568, 1.5708), 'prev': (-0.38, -1.0518, 1.5708)})
diff --git a/probe_occ_run3.py b/probe_occ_run3.py
new file mode 100644
index 0000000..2c37913
--- /dev/null
+++ b/probe_occ_run3.py
@@ -0,0 +1,16 @@
           1 +from probe_occ_lib import *
           2 +from concurrent.futures import ThreadPoolExecutor
           3 +L=(-1.9,-2.0)
           4 +def online(P0,x):
           5 +    t=(x-P0[0])/(L[0]-P0[0]); return (x,round(P0[1]+t*(L[1]-P0[1]),4))
           6 +jobs=[]
           7 +P0=(0.6,-0.35)
           8 +for x in (-0.8,-0.6,-0.45,-0.38):
           9 +  for h in (0.0,math.pi/2):
          10 +    for dy in (1,-1):
          11 +        jobs.append((P0,online(P0,x),h,(0,dy)))
          12 +def f(j):
          13 +    P0,Q,h,d=j
          14 +    return j, sweep(44,P0,math.pi,Q,h,d,step=0.005,n=90)
          15 +with ThreadPoolExecutor(16) as ex:
          16 +    for r in ex.map(f,jobs): print(r,flush=True)
diff --git a/probe_occ_run4.out b/probe_occ_run4.out
new file mode 100644
index 0000000..e69de29
diff --git a/probe_occ_run4.py b/probe_occ_run4.py
new file mode 100644
index 0000000..59d4a59
--- /dev/null
+++ b/probe_occ_run4.py
@@ -0,0 +1,18 @@
           1 +from probe_occ_lib import *
           2 +from concurrent.futures import ThreadPoolExecutor
           3 +L=(-1.9,-2.0)
           4 +def online(P0,x):
           5 +    t=(x-P0[0])/(L[0]-P0[0]); return (x,round(P0[1]+t*(L[1]-P0[1]),4))
           6 +jobs=[]
           7 +P0=(0.6,-0.35)
           8 +for x in (-0.8,-0.6,-0.3):
           9 +  for h in (math.pi/4,3*math.pi/4,-math.pi/4,-3*math.pi/4):
          10 +    for dy in (1,-1):
          11 +        jobs.append((P0,online(P0,x),h,(0,dy)))
          12 +for h in (0.0,math.pi/4,math.pi/2,3*math.pi/4):
          13 +    for dy in (1,-1): jobs.append(((1.6,-0.6),online((1.6,-0.6),-0.4),h,(0,dy)))
          14 +def f(j):
          15 +    P0,Q,h,d=j
          16 +    return j, sweep(44,P0,math.pi,Q,h,d,step=0.005,n=90)
          17 +with ThreadPoolExecutor(32) as ex:
          18 +    for r in ex.map(f,jobs): print(r,flush=True)
```

</details>

<a id="C013"></a>
### C013 · tighter margins

Commit `63fca656031bf5c2fe55525fa9aee82a6ab1385b`; parents: ab01758b6ccbc43055f1f67c3587cb4f466f8c65. Recorded author date: 2026-10-01T11:24:02+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0860](01_timeline.md#E0860): commit title in command; output may not confirm creation.
- [E1045](01_timeline.md#E1045): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_63fca65_approach.py) · [Exact all-file diff](evidence/diffs/C013_63fca65.diff)

[Previous saved controller snapshot](evidence/versions/C012_ab01758_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a4d64cf..cf46e00 100644
--- a/approach.py
+++ b/approach.py
@@ -18,10 +18,10 @@ PILLAR_R = 0.245
   18     18  MOUND_R = 0.185
   19     19  LANDER_XMIN = -1.195
   20     20  LANDER_YMIN = -1.455
   21        -OBJ_RANGE = 1.95
   22        -LANDER_RANGE = 3.95
   23        -SAMPLE_R = 0.235
   24        -PILLAR_INFL_OBJ = 0.03
          21 +OBJ_RANGE = 1.985
          22 +LANDER_RANGE = 3.985
          23 +SAMPLE_R = 0.242
          24 +PILLAR_INFL_OBJ = 0.015
   25     25  PILLAR_INFL_LAND = 0.04
   26     26  ROVER_OCC_R = 0.36
   27     27  CAM_OFF = (-0.087, -0.0125)
@@ -160,7 +160,7 @@ class RoverPlanner:
  160    160          for ob in scene.objectives:
  161    161              ox, oy = ob["x"], ob["y"]
  162    162              d = np.hypot(ox - self.camx, oy - self.camy)
  163        -            v = (d <= OBJ_RANGE) & (np.hypot(ox - X, oy - Y) <= OBJ_RANGE)
         163 +            v = (d <= OBJ_RANGE)
  164    164              occ = np.zeros(X.shape, dtype=bool)
  165    165              for (cx, cy, ax, ay) in scene.pillars:
  166    166                  e = PILLAR_INFL_OBJ
diff --git a/probe_occ_pt.out b/probe_occ_pt.out
new file mode 100644
index 0000000..328b4da
--- /dev/null
+++ b/probe_occ_pt.out
@@ -0,0 +1,56 @@
           1 +(((0.6, -0.35), -0.3, 0.03, 0.7853981633974483), (-0.2838, -0.997), 0)
           2 +(((0.6, -0.35), -0.3, 0.05, 0.7853981633974483), (-0.273, -1.0138), 0)
           3 +(((0.6, -0.35), -0.3, 0.07, 0.7853981633974483), (-0.2622, -1.0307), 0)
           4 +(((0.6, -0.35), -0.3, 0.09, 0.7853981633974483), (-0.2513, -1.0475), 0)
           5 +(((0.6, -0.35), -0.3, 0.11, 0.7853981633974483), (-0.2405, -1.0643), 0)
           6 +(((0.6, -0.35), -0.3, 0.13, 0.7853981633974483), (-0.2297, -1.0811), 0)
           7 +(((0.6, -0.35), -0.3, 0.15, 0.7853981633974483), (-0.2189, -1.098), 'r1 blocked at (-0.4, -1.098, 0.0)')
           8 +(((0.6, -0.35), -0.3, 0.17, 0.7853981633974483), (-0.2081, -1.1148), 'r1 blocked at (-0.4, -1.1148, 0.0)')
           9 +(((0.6, -0.35), -0.3, 0.19, 0.7853981633974483), (-0.1973, -1.1316), 'r1 blocked at (-0.4, -1.1316, 0.0)')
          10 +(((0.6, -0.35), -0.3, 0.21, 0.7853981633974483), (-0.1865, -1.1484), 'r1 blocked at (-0.4, -1.1484, 0.0)')
          11 +(((0.6, -0.35), -0.3, 0.23, 0.7853981633974483), (-0.1757, -1.1653), 'r1 blocked at (-0.4, -1.1653, 0.0)')
          12 +(((0.6, -0.35), -0.3, 0.25, 0.7853981633974483), (-0.1648, -1.1821), 'r1 blocked at (-0.4, -1.1821, 0.0)')
          13 +(((0.6, -0.35), -0.6, -0.05, 0.7853981633974483), (-0.627, -1.1225), 0)
          14 +(((0.6, -0.35), -0.6, -0.07, 0.7853981633974483), (-0.6378, -1.1057), 0)
          15 +(((0.6, -0.35), -0.6, -0.09, 0.7853981633974483), (-0.6487, -1.0889), 0)
          16 +(((0.6, -0.35), -0.6, -0.11, 0.7853981633974483), (-0.6595, -1.072), 0)
          17 +(((0.6, -0.35), -0.6, -0.13, 0.7853981633974483), (-0.6703, -1.0552), 0)
          18 +(((0.6, -0.35), -0.6, -0.15, 0.7853981633974483), (-0.6811, -1.0384), 0)
          19 +(((0.6, -0.35), -0.6, -0.17, 0.7853981633974483), (-0.6919, -1.0216), 0)
          20 +(((0.6, -0.35), -0.6, -0.19, 0.7853981633974483), (-0.7027, -1.0047), 1)
          21 +(((0.6, -0.35), -0.6, -0.21, 0.7853981633974483), (-0.7135, -0.9879), 1)
          22 +(((0.6, -0.35), -0.6, -0.23, 0.7853981633974483), (-0.7243, -0.9711), 1)
          23 +(((0.6, -0.35), -0.6, -0.25, 0.7853981633974483), (-0.7352, -0.9543), 1)
          24 +(((0.6, -0.35), -0.45, -0.25, 0.0), (-0.5852, -0.8579), 1)
          25 +(((0.6, -0.35), -0.45, -0.225, 0.0), (-0.5716, -0.8789), 1)
          26 +(((0.6, -0.35), -0.45, -0.2, 0.0), (-0.5581, -0.8999), 1)
          27 +(((0.6, -0.35), -0.45, -0.175, 0.0), (-0.5446, -0.921), 1)
          28 +(((0.6, -0.35), -0.45, -0.15, 0.0), (-0.5311, -0.942), 0)
          29 +(((0.6, -0.35), -0.45, -0.125, 0.0), (-0.5176, -0.963), 1)
          30 +(((0.6, -0.35), -0.45, -0.1, 0.0), (-0.5041, -0.9841), 0)
          31 +(((0.6, -0.35), -0.45, -0.075, 0.0), (-0.4905, -1.0051), 1)
          32 +(((0.6, -0.35), -0.45, -0.05, 0.0), (-0.477, -1.0261), 1)
          33 +(((0.6, -0.35), -0.45, -0.025, 0.0), (-0.4635, -1.0471), 1)
          34 +(((0.6, -0.35), -0.45, -0.0, 0.0), (-0.45, -1.0682), 1)
          35 +(((0.6, -0.35), -0.45, 0.025, 0.0), (-0.4365, -1.0892), 1)
          36 +(((0.6, -0.35), -0.45, 0.05, 0.0), (-0.423, -1.1102), 1)
          37 +(((0.6, -0.35), -0.45, 0.075, 0.0), (-0.4095, -1.1313), 1)
          38 +(((0.6, -0.35), -0.45, 0.1, 0.0), (-0.3959, -1.1523), 0)
          39 +(((0.6, -0.35), -0.45, 0.125, 0.0), (-0.3824, -1.1733), 1)
          40 +(((0.6, -0.35), -0.45, 0.15, 0.0), (-0.3689, -1.1944), 0)
          41 +(((0.6, -0.35), -0.45, 0.175, 0.0), (-0.3554, -1.2154), 1)
          42 +(((0.6, -0.35), -0.45, 0.2, 0.0), (-0.3419, -1.2364), 1)
          43 +(((0.6, -0.35), -0.45, 0.225, 0.0), (-0.3284, -1.2575), 1)
          44 +(((0.6, -0.35), -0.45, 0.25, 0.0), (-0.3148, -1.2785), 1)
          45 +(((0.6, -0.35), -1.0, 0.15, 0.0), (-0.9189, -1.5478), 0)
          46 +(((0.6, -0.35), -1.0, -0.15, 0.0), (-1.0811, -1.2954), 0)
          47 +(((0.6, -0.35), -1.0, 0.17, 0.0), (-0.9081, -1.5646), 0)
          48 +(((0.6, -0.35), -1.0, -0.17, 0.0), (-1.0919, -1.2786), 0)
          49 +(((0.6, -0.35), -1.0, 0.19, 0.0), (-0.8973, -1.5815), 1)
          50 +(((0.6, -0.35), -1.0, -0.19, 0.0), (-1.1027, -1.2618), 1)
          51 +(((0.6, -0.35), -1.0, 0.21, 0.0), (-0.8865, -1.5983), 1)
          52 +(((0.6, -0.35), -1.0, -0.21, 0.0), (-1.1135, -1.245), 1)
          53 +(((0.6, -0.35), -1.0, 0.23, 0.0), (-0.8757, -1.6151), 1)
          54 +(((0.6, -0.35), -1.0, -0.23, 0.0), (-1.1243, -1.2281), 1)
          55 +(((0.6, -0.35), -1.0, 0.25, 0.0), (-0.8648, -1.6319), 1)
          56 +(((0.6, -0.35), -1.0, -0.25, 0.0), (-1.1352, -1.2113), 1)
diff --git a/probe_occ_pt.py b/probe_occ_pt.py
new file mode 100644
index 0000000..8b20b13
--- /dev/null
+++ b/probe_occ_pt.py
@@ -0,0 +1,26 @@
           1 +from probe_occ_lib import *
           2 +from concurrent.futures import ThreadPoolExecutor
           3 +import sys
           4 +L=np.array((-1.9,-2.0))
           5 +def camp(P0,th=math.pi):
           6 +    c,s=math.cos(th),math.sin(th); return np.array((P0[0]-0.087*c+0.0125*s, P0[1]-0.087*s-0.0125*c))
           7 +def point(P0,x,sd):
           8 +    C=camp(P0); d=L-C; d/=np.linalg.norm(d); n=np.array((-d[1],d[0]))  # cross(d,n)>0
           9 +    t=(x-C[0])/(L[0]-C[0]); base=C+t*(L-C)
          10 +    q=base+sd*n
          11 +    # sign convention: cross(L-C, q-C) = sd*|..| >0 -> check
          12 +    return (round(float(q[0]),4),round(float(q[1]),4))
          13 +def test(job):
          14 +    P0,x,sd,h=job; Q=point(P0,x,sd)
          15 +    e,err=setup(44,P0,math.pi,Q,h)
          16 +    if err: e.env.close(); return job,Q,err
          17 +    e.step((0,0,0,SEL['send']),(0,0,0,0)); ok=e.feats('sample5')[6]>0.5; e.env.close()
          18 +    return job,Q,int(ok)
          19 +if __name__=='__main__':
          20 +    P=(0.6,-0.35); jobs=[]
          21 +    jobs+=[(P,-0.3,round(s,3),math.pi/4) for s in np.arange(0.03,0.26,0.02)]
          22 +    jobs+=[(P,-0.6,round(-s,3),math.pi/4) for s in np.arange(0.05,0.26,0.02)]
          23 +    jobs+=[(P,-0.45,round(s,3),0.0) for s in np.arange(-0.25,0.26,0.025)]
          24 +    jobs+=[(P,-1.0,round(sg*s,3),0.0) for s in np.arange(0.15,0.26,0.02) for sg in (1,-1)]
          25 +    with ThreadPoolExecutor(12) as ex:
          26 +        for r in ex.map(test,jobs): print(r,flush=True)
diff --git a/probe_occ_run4.out b/probe_occ_run4.out
index e69de29..803263f 100644
--- a/probe_occ_run4.out
+++ b/probe_occ_run4.out
@@ -0,0 +1,59 @@
           1 +(((0.6, -0.35), (-0.8, -1.274), 0.7853981633974483, (0, 1)), {'i': 39, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.079, 0.7854), 'prev': (-0.8, -1.084, 0.7854)})
           2 +(((0.6, -0.35), (-0.8, -1.274), 0.7853981633974483, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.509, 0.7854), 'prev': (-0.8, -1.504, 0.7854)})
           3 +(((0.6, -0.35), (-0.8, -1.274), 2.356194490192345, (0, 1)), {'i': 31, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.119, 2.3562), 'prev': (-0.8, -1.124, 2.3562)})
           4 +(((0.6, -0.35), (-0.8, -1.274), 2.356194490192345, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.509, 2.3562), 'prev': (-0.8, -1.504, 2.3562)})
           5 +(((0.6, -0.35), (-0.8, -1.274), -0.7853981633974483, (0, 1)), {'i': 36, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.094, -0.7854), 'prev': (-0.8, -1.099, -0.7854)})
           6 +(((0.6, -0.35), (-0.8, -1.274), -0.7853981633974483, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.509, -0.7854), 'prev': (-0.8, -1.504, -0.7854)})
           7 +(((0.6, -0.35), (-0.8, -1.274), -2.356194490192345, (0, 1)), {'i': 39, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.079, -2.3562), 'prev': (-0.8, -1.084, -2.3562)})
           8 +(((0.6, -0.35), (-0.8, -1.274), -2.356194490192345, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.8, -1.509, -2.3562), 'prev': (-0.8, -1.504, -2.3562)})
           9 +(((0.6, -0.35), (-0.6, -1.142), 0.7853981633974483, (0, 1)), {'i': 10, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.092, 0.7854), 'prev': (-0.6, -1.097, 0.7854)})
          10 +(((0.6, -0.35), (-0.6, -1.142), 0.7853981633974483, (0, -1)), {'i': 50, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.392, 0.7854), 'prev': (-0.6, -1.387, 0.7854)})
          11 +(((0.6, -0.35), (-0.6, -1.142), 2.356194490192345, (0, 1)), {'i': 27, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.007, 2.3562), 'prev': (-0.6, -1.012, 2.3562)})
          12 +(((0.6, -0.35), (-0.6, -1.142), 2.356194490192345, (0, -1)), {'i': 47, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.377, 2.3562), 'prev': (-0.6, -1.372, 2.3562)})
          13 +(((0.6, -0.35), (-0.6, -1.142), -0.7853981633974483, (0, 1)), {'i': 27, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.007, -0.7854), 'prev': (-0.6, -1.012, -0.7854)})
          14 +(((0.6, -0.35), (-0.6, -1.142), -0.7853981633974483, (0, -1)), {'i': 33, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.307, -0.7854), 'prev': (-0.6, -1.302, -0.7854)})
          15 +(((0.6, -0.35), (-0.6, -1.142), -2.356194490192345, (0, 1)), {'i': 24, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.022, -2.3562), 'prev': (-0.6, -1.027, -2.3562)})
          16 +(((0.6, -0.35), (-0.6, -1.142), -2.356194490192345, (0, -1)), {'i': 51, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.6, -1.397, -2.3562), 'prev': (-0.6, -1.392, -2.3562)})
          17 +(((0.6, -0.35), (-0.3, -0.944), 0.7853981633974483, (0, 1)), {'i': 38, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -0.754, 0.7854), 'prev': (-0.3, -0.759, 0.7854)})
          18 +(((0.6, -0.35), (-0.3, -0.944), 0.7853981633974483, (0, -1)), {'i': 16, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -1.024, 0.7854), 'prev': (-0.3, -1.019, 0.7854)})
          19 +(((0.6, -0.35), (-0.3, -0.944), 2.356194490192345, (0, 1)), {'i': 34, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -0.774, 2.3562), 'prev': (-0.3, -0.779, 2.3562)})
          20 +(((0.6, -0.35), (-0.3, -0.944), 2.356194490192345, (0, -1)), {'i': 28, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -1.084, 2.3562), 'prev': (-0.3, -1.079, 2.3562)})
          21 +(((0.6, -0.35), (-0.3, -0.944), -0.7853981633974483, (0, 1)), {'i': 26, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -0.814, -0.7854), 'prev': (-0.3, -0.819, -0.7854)})
          22 +(((0.6, -0.35), (-0.3, -0.944), -0.7853981633974483, (0, -1)), {'i': 28, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -1.084, -0.7854), 'prev': (-0.3, -1.079, -0.7854)})
          23 +(((0.6, -0.35), (-0.3, -0.944), -2.356194490192345, (0, 1)), {'i': 38, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -0.754, -2.3562), 'prev': (-0.3, -0.759, -2.3562)})
          24 +(((0.6, -0.35), (-0.3, -0.944), -2.356194490192345, (0, -1)), {'i': 24, 'p0': (0.6, -0.35, -3.1416), 'p1': (-0.3, -1.064, -2.3562), 'prev': (-0.3, -1.059, -2.3562)})
          25 +Traceback (most recent call last):
          26 +  File "/sandbox/probe_occ_run4.py", line 18, in <module>
          27 +    for r in ex.map(f,jobs): print(r,flush=True)
          28 +  File "/usr/lib/python3.11/concurrent/futures/_base.py", line 619, in result_iterator
          29 +    yield _result_or_cancel(fs.pop())
          30 +          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
          31 +  File "/usr/lib/python3.11/concurrent/futures/_base.py", line 317, in _result_or_cancel
          32 +    return fut.result(timeout)
          33 +           ^^^^^^^^^^^^^^^^^^^
          34 +  File "/usr/lib/python3.11/concurrent/futures/_base.py", line 449, in result
          35 +    return self.__get_result()
          36 +           ^^^^^^^^^^^^^^^^^^^
          37 +  File "/usr/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
          38 +    raise self._exception
          39 +  File "/usr/lib/python3.11/concurrent/futures/thread.py", line 58, in run
          40 +    result = self.fn(*self.args, **self.kwargs)
          41 +             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          42 +  File "/sandbox/probe_occ_run4.py", line 16, in f
          43 +    return j, sweep(44,P0,math.pi,Q,h,d,step=0.005,n=90)
          44 +              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          45 +  File "/sandbox/probe_occ_lib.py", line 17, in sweep
          46 +    e,err=setup(seed,P0,th0,Q,h1,wp1)
          47 +          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
          48 +  File "/sandbox/probe_occ_lib.py", line 4, in setup
          49 +    e=E(seed)
          50 +      ^^^^^^^
          51 +  File "/sandbox/probe_send_lib.py", line 6, in __init__
          52 +    s.env=make_env(); s.obs,s.info=s.env.reset(seed=seed); s.t=0; s.last=None
          53 +                                   ^^^^^^^^^^^^^^^^^^^^^^
          54 +  File "/sandbox/env_client.py", line 525, in reset
          55 +    response = self._request({"cmd": "reset", "seed": seed, "options": options})
          56 +               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          57 +  File "/sandbox/env_client.py", line 478, in _request
          58 +    raise RuntimeError("Connection to the environment server was closed")
          59 +RuntimeError: Connection to the environment server was closed
diff --git a/probe_occ_run4.py b/probe_occ_run4.py
index 59d4a59..acb5245 100644
--- a/probe_occ_run4.py
+++ b/probe_occ_run4.py
@@ -5,7 +5,7 @@ def online(P0,x):
    5      5      t=(x-P0[0])/(L[0]-P0[0]); return (x,round(P0[1]+t*(L[1]-P0[1]),4))
    6      6  jobs=[]
    7      7  P0=(0.6,-0.35)
    8        -for x in (-0.8,-0.6,-0.3):
           8 +for x in ():
    9      9    for h in (math.pi/4,3*math.pi/4,-math.pi/4,-3*math.pi/4):
   10     10      for dy in (1,-1):
   11     11          jobs.append((P0,online(P0,x),h,(0,dy)))
@@ -14,5 +14,5 @@ for h in (0.0,math.pi/4,math.pi/2,3*math.pi/4):
   14     14  def f(j):
   15     15      P0,Q,h,d=j
   16     16      return j, sweep(44,P0,math.pi,Q,h,d,step=0.005,n=90)
   17        -with ThreadPoolExecutor(32) as ex:
          17 +with ThreadPoolExecutor(8) as ex:
   18     18      for r in ex.map(f,jobs): print(r,flush=True)
diff --git a/probe_occ_run4b.out b/probe_occ_run4b.out
new file mode 100644
index 0000000..c75f4a9
--- /dev/null
+++ b/probe_occ_run4b.out
@@ -0,0 +1,8 @@
           1 +(((1.6, -0.6), (-0.4, -1.4), 0.0, (0, 1)), {'i': 46, 'p0': (1.6, -0.6, -3.1416), 'p1': (-0.4, -1.17, 0.0), 'prev': (-0.4, -1.175, 0.0)})
           2 +(((1.6, -0.6), (-0.4, -1.4), 0.0, (0, -1)), {'i': 41, 'p0': (1.6, -0.6, -3.1416), 'p1': (-0.4, -1.605, 0.0), 'prev': (-0.4, -1.6, 0.0)})
           3 +(((1.6, -0.6), (-0.4, -1.4), 0.7853981633974483, (0, 1)), {'i': 35, 'p0': (1.6, -0.6, -3.1416), 'p1': (-0.4, -1.225, 0.7854), 'prev': (-0.4, -1.23, 0.7854)})
           4 +(((1.6, -0.6), (-0.4, -1.4), 0.7853981633974483, (0, -1)), {'i': 41, 'p0': (1.6, -0.6, -3.1416), 'p1': (-0.4, -1.605, 0.7854), 'prev': (-0.4, -1.6, 0.7854)})
           5 +(((1.6, -0.6), (-0.4, -1.4), 1.5707963267948966, (0, 1)), {'i': 35, 'p0': (1.6, -0.6, -3.1416), 'p1': (-0.4, -1.225, 1.5708), 'prev': (-0.4, -1.23, 1.5708)})
           6 +(((1.6, -0.6), (-0.4, -1.4), 1.5707963267948966, (0, -1)), {'i': 41, 'p0': (1.6, -0.6, -3.1416), 'p1': (-0.4, -1.605, 1.5708), 'prev': (-0.4, -1.6, 1.5708)})
           7 +(((1.6, -0.6), (-0.4, -1.4), 2.356194490192345, (0, 1)), {'i': 35, 'p0': (1.6, -0.6, -3.1416), 'p1': (-0.4, -1.225, 2.3562), 'prev': (-0.4, -1.23, 2.3562)})
           8 +(((1.6, -0.6), (-0.4, -1.4), 2.356194490192345, (0, -1)), {'i': 41, 'p0': (1.6, -0.6, -3.1416), 'p1': (-0.4, -1.605, 2.3562), 'prev': (-0.4, -1.6, 2.3562)})
diff --git a/test_approach.py b/test_approach.py
index 6c4f3aa..b2a6dbd 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -21,6 +21,7 @@ if __name__ == "__main__":
   21     21      from concurrent.futures import ThreadPoolExecutor
   22     22      with ThreadPoolExecutor(8) as ex:
   23     23          res = list(ex.map(run, seeds))
          24 +    import json; json.dump(res, open(sys.argv[3] if len(sys.argv)>3 else "last_res.json","w"))
   24     25      for r in res: print(r)
   25     26      ok=[r for r in res if r[2]]
   26     27      print("solved", len(ok), "/", len(res), "mean steps", np.mean([r[3] for r in ok]) if ok else None)
```

</details>

<a id="C014"></a>
### C014 · rover occluder 0.26

Commit `04610bdbe05f46962d4cbec95d8b6501d3580289`; parents: 63fca656031bf5c2fe55525fa9aee82a6ab1385b. Recorded author date: 2026-10-01T11:25:43+02:00.

File roles (automatic): policy, setup/other.

- [E0869](01_timeline.md#E0869): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_04610bd_approach.py) · [Exact all-file diff](evidence/diffs/C014_04610bd.diff)

[Previous saved controller snapshot](evidence/versions/C013_63fca65_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index cf46e00..6f8578b 100644
--- a/approach.py
+++ b/approach.py
@@ -23,7 +23,7 @@ LANDER_RANGE = 3.985
   23     23  SAMPLE_R = 0.242
   24     24  PILLAR_INFL_OBJ = 0.015
   25     25  PILLAR_INFL_LAND = 0.04
   26        -ROVER_OCC_R = 0.36
          26 +ROVER_OCC_R = 0.26
   27     27  CAM_OFF = (-0.087, -0.0125)
   28     28  OBJ_BACK_DEG = 108.0     # if |rel bearing| > this, pillars don't occlude objectives
   29     29  LAND_BACK_DEG = 110.0    # same quirk for lander (sending)
diff --git a/res_tight.json b/res_tight.json
new file mode 100644
index 0000000..114120a
--- /dev/null
+++ b/res_tight.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 26, 0, 0.66, 4.0], [1, 2, true, 21, 0, 0.37, 3.2], [2, 3, true, 21, 0, 1.69, 3.1], [3, 3, true, 22, 0, 1.25, 3.3], [4, 3, true, 21, 0, 0.9, 4.2], [5, 3, true, 30, 0, 2.16, 7.6], [6, 2, true, 21, 0, 0.96, 4.8], [7, 3, true, 22, 0, 2.59, 6.2], [8, 3, true, 22, 0, 0.86, 4.7], [9, 2, true, 23, 0, 0.65, 4.4], [10, 3, true, 22, 0, 1.43, 5.3], [11, 1, true, 20, 0, 0.18, 3.3], [12, 2, true, 24, 0, 0.34, 5.4], [13, 3, true, 25, 0, 0.82, 5.3], [14, 1, true, 30, 0, 0.08, 5.0], [15, 3, true, 23, 0, 0.77, 4.6], [16, 2, true, 30, 0, 0.07, 4.8], [17, 3, true, 22, 0, 2.49, 6.7], [18, 3, true, 22, 0, 0.95, 4.0], [19, 2, true, 27, 0, 0.54, 4.4], [20, 3, true, 28, 0, 0.83, 6.0], [21, 1, true, 21, 0, 0.16, 4.8], [22, 3, true, 24, 0, 0.98, 6.2], [23, 1, true, 18, 0, 0.33, 4.6], [24, 2, true, 20, 0, 0.38, 4.6], [25, 2, true, 20, 0, 0.73, 5.2], [26, 3, true, 23, 0, 1.4, 5.6], [27, 1, true, 22, 0, 0.11, 4.4], [28, 2, true, 23, 0, 0.74, 5.2], [29, 3, true, 23, 0, 0.73, 5.3], [30, 1, true, 20, 0, 0.17, 4.4], [31, 2, true, 26, 0, 0.31, 4.6], [32, 3, true, 21, 0, 0.56, 4.6], [33, 3, true, 24, 0, 0.46, 4.4], [34, 1, true, 21, 0, 0.11, 3.2], [35, 1, true, 20, 0, 0.13, 3.1], [36, 2, true, 23, 0, 0.2, 5.0], [37, 1, true, 21, 0, 0.09, 4.0], [38, 1, true, 21, 0, 0.27, 5.2], [39, 3, true, 23, 0, 0.21, 5.4], [40, 2, true, 21, 0, 0.23, 4.8], [41, 2, true, 20, 0, 0.48, 4.7], [42, 1, true, 21, 0, 0.17, 4.2], [43, 2, true, 25, 0, 0.27, 4.9], [44, 3, true, 21, 0, 0.4, 4.3], [45, 3, true, 22, 0, 0.45, 4.9], [46, 2, true, 20, 0, 0.21, 4.8], [47, 1, true, 24, 0, 0.14, 5.4], [48, 1, true, 19, 0, 0.07, 3.6], [49, 1, true, 23, 0, 0.18, 4.9], [50, 3, true, 22, 0, 0.84, 5.4], [51, 2, true, 22, 0, 0.63, 4.5], [52, 3, true, 22, 0, 1.15, 5.7], [53, 3, true, 22, 0, 1.15, 5.2], [54, 1, true, 21, 0, 0.26, 4.0], [55, 3, true, 27, 0, 1.04, 6.4], [56, 2, true, 23, 0, 0.46, 4.7], [57, 1, true, 19, 0, 0.1, 4.5], [58, 2, true, 25, 0, 0.62, 6.3], [59, 3, true, 22, 0, 1.94, 6.2], [60, 1, true, 24, 0, 0.41, 5.0], [61, 2, true, 22, 0, 0.24, 4.6], [62, 2, true, 26, 0, 0.39, 5.1], [63, 2, true, 22, 0, 0.52, 4.4], [64, 2, true, 23, 0, 0.25, 4.4], [65, 1, true, 18, 0, 0.17, 3.5], [66, 3, true, 22, 0, 0.23, 5.6], [67, 3, true, 22, 0, 0.31, 4.9], [68, 2, true, 21, 0, 0.15, 4.8], [69, 1, true, 21, 0, 0.16, 5.0], [70, 2, true, 21, 0, 0.65, 5.0], [71, 3, true, 22, 0, 1.87, 6.4], [72, 3, true, 21, 0, 1.76, 5.2], [73, 3, true, 22, 0, 0.77, 5.9], [74, 1, true, 21, 0, 0.16, 3.8], [75, 2, true, 19, 0, 0.67, 3.5], [76, 2, true, 23, 0, 0.66, 4.9], [77, 1, true, 21, 0, 0.16, 4.0], [78, 3, true, 23, 0, 0.42, 5.5], [79, 1, true, 23, 0, 0.27, 4.6], [80, 3, true, 21, 0, 1.11, 5.3], [81, 1, true, 22, 0, 0.14, 4.1], [82, 3, true, 21, 0, 0.39, 3.9], [83, 3, true, 22, 0, 0.48, 4.8], [84, 2, true, 23, 0, 0.89, 4.6], [85, 3, true, 21, 0, 1.55, 5.5], [86, 3, true, 21, 0, 0.64, 3.4], [87, 2, true, 23, 0, 0.23, 4.7], [88, 2, true, 21, 0, 0.32, 3.6], [89, 3, true, 30, 0, 0.2, 6.0], [90, 2, true, 22, 0, 0.2, 4.3], [91, 3, true, 24, 0, 0.23, 5.1], [92, 2, true, 24, 0, 0.69, 4.6], [93, 3, true, 24, 0, 0.86, 5.0], [94, 1, true, 20, 0, 0.18, 3.5], [95, 2, true, 22, 0, 0.65, 4.9], [96, 3, true, 22, 0, 0.65, 4.8], [97, 1, true, 28, 0, 0.28, 5.2], [98, 2, true, 24, 0, 0.68, 4.7], [99, 3, true, 24, 0, 0.73, 6.0], [100, 3, true, 25, 0, 0.43, 5.1], [101, 1, true, 19, 0, 0.09, 3.2], [102, 2, true, 23, 0, 0.24, 5.2], [103, 2, true, 21, 0, 0.48, 5.3], [104, 3, true, 22, 0, 0.64, 5.0], [105, 1, true, 21, 0, 0.08, 4.5], [106, 2, true, 21, 0, 0.21, 4.0], [107, 1, true, 22, 0, 0.21, 4.6], [108, 1, true, 19, 0, 0.17, 4.1], [109, 2, true, 21, 0, 0.34, 5.1], [110, 2, true, 23, 0, 0.3, 5.6], [111, 2, true, 21, 0, 0.15, 4.8], [112, 1, true, 22, 0, 0.13, 4.9], [113, 1, true, 20, 0, 0.12, 4.7], [114, 1, true, 21, 0, 0.1, 4.3], [115, 2, true, 22, 0, 0.12, 4.2], [116, 1, true, 22, 0, 0.1, 3.0], [117, 1, true, 26, 0, 0.17, 2.9], [118, 2, true, 24, 0, 0.1, 2.1], [119, 2, true, 22, 0, 0.37, 1.1]]
\ No newline at end of file
```

</details>

<a id="C015"></a>
### C015 · timed send checks other rover at t-1 and t (sequential rover update)

Commit `bd3aae9d34ee3b2da80f409fbbd63bc81e52f0a1`; parents: 04610bdbe05f46962d4cbec95d8b6501d3580289. Recorded author date: 2026-10-01T11:28:15+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0892](01_timeline.md#E0892): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_bd3aae9_approach.py) · [Exact all-file diff](evidence/diffs/C015_bd3aae9.diff)

[Previous saved controller snapshot](evidence/versions/C014_04610bd_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6f8578b..7258b7f 100644
--- a/approach.py
+++ b/approach.py
@@ -430,9 +430,10 @@ class GeneratedApproach:
  430    430              lx, ly = sc.lander
  431    431              t = tmin
  432    432              while pending_mask.any() and t < tmin + 200:
  433        -                ox, oy = other[min(t, len(other) - 1)]
  434        -                blk = seg_hits_disk(P.X, P.Y, lx, ly, ox, oy, ROVER_OCC_R) | \
  435        -                    seg_hits_disk(P.camx, P.camy, lx, ly, ox, oy, ROVER_OCC_R)
         433 +                blk = np.zeros(P.X.shape, dtype=bool)
         434 +                for tt in (t - 1, t):
         435 +                    ox, oy = other[max(0, min(tt, len(other) - 1))]
         436 +                    blk |= seg_hits_disk(P.camx, P.camy, lx, ly, ox, oy, ROVER_OCC_R)
  436    437                  ok = pending_mask & (G0 <= t) & ~blk
  437    438                  G[ok] = t
  438    439                  pending_mask &= ~ok
diff --git a/dbg6.py b/dbg6.py
new file mode 100644
index 0000000..3b5b6e8
--- /dev/null
+++ b/dbg6.py
@@ -0,0 +1,18 @@
           1 +import sys
           2 +import numpy as np
           3 +from test_approach import *
           4 +seed=int(sys.argv[1]); dy=float(sys.argv[2]) if len(sys.argv)>2 else 0.05
           5 +env = make_env(); obs, info = env.reset(seed=seed)
           6 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +steps=0
           8 +while True:
           9 +    n=len(ap.log)
          10 +    a=ap.get_action(obs)
          11 +    if len(ap.log)>n: break
          12 +    obs,r,term,tr,info=env.step(a); steps+=1
          13 +r0=obs.get_object_from_name('rover0'); r1=obs.get_object_from_name('rover1')
          14 +objs=[o for o in obs if o.type.name=='objective']
          15 +print('fail at', obs.get(r0,'x'), obs.get(r0,'y'), obs.get(r0,'theta'))
          16 +for k in range(12):
          17 +    obs,*_=env.step(np.array([0,0,0,0.5, 0,dy,0,0],dtype=np.float32))
          18 +    print(k, round(obs.get(r1,'x'),3), round(obs.get(r1,'y'),3), [obs.get(o,'received_image') for o in objs])
diff --git a/dbg7.py b/dbg7.py
new file mode 100644
index 0000000..b82f421
--- /dev/null
+++ b/dbg7.py
@@ -0,0 +1,15 @@
           1 +import sys
           2 +import numpy as np
           3 +from test_approach import *
           4 +seed=int(sys.argv[1])
           5 +env = make_env(); obs, info = env.reset(seed=seed)
           6 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +r0=obs.get_object_from_name('rover0'); r1=obs.get_object_from_name('rover1')
           8 +hist=[]
           9 +while True:
          10 +    n=len(ap.log)
          11 +    a=ap.get_action(obs)
          12 +    if len(ap.log)>n: break
          13 +    hist.append((round(obs.get(r1,'x'),2), round(obs.get(r1,'y'),2)))
          14 +    obs,r,term,tr,info=env.step(a)
          15 +print(hist[-4:])
diff --git a/res_occ26.json b/res_occ26.json
new file mode 100644
index 0000000..19a6fa4
--- /dev/null
+++ b/res_occ26.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 26, 0, 0.29, 5.3], [1, 2, true, 21, 0, 0.09, 3.5], [2, 3, true, 21, 0, 0.79, 3.3], [3, 3, true, 22, 0, 0.63, 3.7], [4, 3, true, 21, 0, 0.84, 2.8], [5, 3, true, 24, 0, 0.99, 4.9], [6, 2, true, 21, 0, 0.58, 5.1], [7, 3, true, 22, 0, 1.44, 5.6], [8, 3, true, 22, 0, 0.4, 5.2], [9, 2, true, 23, 0, 0.6, 5.1], [10, 3, true, 22, 0, 1.28, 4.9], [11, 1, true, 20, 0, 0.07, 3.9], [12, 2, true, 24, 0, 0.49, 4.9], [13, 3, true, 25, 0, 1.21, 6.2], [14, 1, true, 30, 0, 0.08, 5.9], [15, 3, true, 22, 0, 0.7, 3.9], [16, 2, true, 22, 0, 0.15, 4.0], [17, 3, true, 22, 0, 2.2, 7.2], [18, 3, true, 22, 0, 0.81, 4.6], [19, 2, true, 24, 0, 0.41, 5.2], [20, 3, true, 28, 0, 0.55, 6.3], [21, 1, true, 20, 0, 0.2, 4.9], [22, 3, true, 24, 0, 0.7, 5.8], [23, 1, true, 18, 0, 0.08, 4.3], [24, 2, true, 20, 0, 0.21, 3.8], [25, 2, true, 20, 0, 0.38, 5.6], [26, 3, true, 22, 0, 0.99, 5.9], [27, 1, true, 22, 0, 0.06, 5.4], [28, 2, true, 23, 0, 0.36, 5.8], [29, 3, true, 22, 0, 0.36, 5.3], [30, 1, true, 20, 0, 0.17, 3.8], [31, 2, true, 26, 0, 0.19, 5.3], [32, 3, true, 21, 0, 0.49, 5.1], [33, 3, true, 24, 0, 0.49, 6.8], [34, 1, true, 21, 0, 0.1, 5.7], [35, 1, true, 19, 0, 0.12, 5.3], [36, 2, true, 21, 0, 0.23, 6.0], [37, 1, true, 19, 0, 0.14, 5.2], [38, 1, true, 21, 1, 0.2, 5.2], [39, 3, true, 23, 0, 0.2, 5.6], [40, 2, true, 21, 0, 0.38, 5.5], [41, 2, true, 20, 0, 0.27, 5.2], [42, 1, true, 25, 1, 0.24, 6.0], [43, 2, true, 25, 0, 0.3, 5.7], [44, 3, true, 21, 0, 0.43, 5.4], [45, 3, true, 22, 0, 0.55, 5.2], [46, 2, true, 20, 0, 0.21, 5.0], [47, 1, true, 21, 0, 0.15, 4.6], [48, 1, true, 18, 0, 0.15, 3.6], [49, 1, true, 23, 0, 0.24, 5.0], [50, 3, true, 22, 0, 0.89, 5.4], [51, 2, true, 22, 0, 0.25, 4.4], [52, 3, true, 22, 0, 0.57, 4.9], [53, 3, true, 21, 0, 1.01, 5.4], [54, 1, true, 20, 0, 0.1, 4.8], [55, 3, true, 27, 0, 0.98, 6.6], [56, 2, true, 23, 0, 0.46, 5.7], [57, 1, true, 19, 0, 0.11, 4.8], [58, 2, true, 24, 0, 0.67, 5.4], [59, 3, true, 22, 0, 1.61, 5.3], [60, 1, true, 23, 0, 0.37, 4.2], [61, 2, true, 21, 0, 0.22, 3.6], [62, 2, true, 23, 0, 0.45, 4.3], [63, 2, true, 22, 0, 0.41, 4.5], [64, 2, true, 22, 0, 0.2, 4.8], [65, 1, true, 18, 0, 0.21, 4.3], [66, 3, true, 22, 0, 0.2, 4.8], [67, 3, true, 21, 0, 0.43, 4.7], [68, 2, true, 21, 0, 0.19, 3.7], [69, 1, true, 21, 0, 0.06, 3.4], [70, 2, true, 21, 0, 0.5, 4.0], [71, 3, true, 22, 0, 1.71, 6.8], [72, 3, true, 21, 0, 1.6, 5.9], [73, 3, true, 21, 0, 0.81, 4.7], [74, 1, true, 20, 0, 0.1, 4.0], [75, 2, true, 19, 0, 0.44, 3.9], [76, 2, true, 23, 0, 0.39, 4.9], [77, 1, true, 21, 0, 0.16, 4.1], [78, 3, true, 23, 0, 0.41, 5.6], [79, 1, true, 23, 0, 0.13, 4.8], [80, 3, true, 21, 0, 1.0, 4.1], [81, 1, true, 21, 0, 0.15, 3.5], [82, 3, true, 21, 0, 0.46, 3.9], [83, 3, true, 22, 0, 0.38, 4.4], [84, 2, true, 23, 0, 0.64, 4.7], [85, 3, true, 21, 0, 1.6, 4.7], [86, 3, true, 21, 0, 0.67, 4.0], [87, 2, true, 23, 0, 0.28, 4.0], [88, 2, true, 21, 0, 0.36, 3.6], [89, 3, true, 30, 0, 0.28, 5.6], [90, 2, true, 22, 0, 0.53, 5.0], [91, 3, true, 24, 0, 0.53, 5.5], [92, 2, true, 24, 0, 0.24, 4.8], [93, 3, true, 24, 0, 0.93, 5.0], [94, 1, true, 20, 0, 0.27, 4.0], [95, 2, true, 22, 0, 0.6, 4.6], [96, 3, true, 22, 0, 0.58, 4.3], [97, 1, true, 27, 0, 0.15, 4.9], [98, 2, true, 24, 0, 0.57, 5.2], [99, 3, true, 24, 0, 0.75, 6.2], [100, 3, true, 25, 0, 0.64, 6.2], [101, 1, true, 19, 0, 0.09, 3.0], [102, 2, true, 22, 0, 0.42, 6.1], [103, 2, true, 23, 1, 0.25, 5.9], [104, 3, true, 22, 0, 0.95, 5.3], [105, 1, true, 21, 0, 0.14, 4.7], [106, 2, true, 21, 0, 0.41, 3.9], [107, 1, true, 22, 0, 0.18, 4.2], [108, 1, true, 18, 0, 0.12, 3.0], [109, 2, true, 21, 0, 0.46, 6.1], [110, 2, true, 21, 0, 0.55, 6.6], [111, 2, true, 21, 0, 0.12, 6.5], [112, 1, true, 19, 0, 0.22, 4.9], [113, 1, true, 20, 0, 0.06, 5.0], [114, 1, true, 21, 0, 0.16, 5.8], [115, 2, true, 22, 0, 0.19, 4.3], [116, 1, true, 22, 0, 0.05, 3.8], [117, 1, true, 26, 0, 0.14, 3.1], [118, 2, true, 21, 0, 0.28, 2.1], [119, 2, true, 20, 0, 0.49, 0.9]]
\ No newline at end of file
```

</details>

<a id="C016"></a>
### C016 · home region radius 0.22

Commit `e1ead97c4000536ccca9c5c03643ba6972f87b55`; parents: bd3aae9d34ee3b2da80f409fbbd63bc81e52f0a1. Recorded author date: 2026-10-01T11:36:09+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0929](01_timeline.md#E0929): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_e1ead97_approach.py) · [Exact all-file diff](evidence/diffs/C016_e1ead97.diff)

[Previous saved controller snapshot](evidence/versions/C015_bd3aae9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7258b7f..0c23598 100644
--- a/approach.py
+++ b/approach.py
@@ -21,6 +21,7 @@ LANDER_YMIN = -1.455
   21     21  OBJ_RANGE = 1.985
   22     22  LANDER_RANGE = 3.985
   23     23  SAMPLE_R = 0.242
          24 +HOME_R = 0.22
   24     25  PILLAR_INFL_OBJ = 0.015
   25     26  PILLAR_INFL_LAND = 0.04
   26     27  ROVER_OCC_R = 0.26
@@ -150,6 +151,8 @@ class RoverPlanner:
  150    151          free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
  151    152          free[self.hi, self.hj] = True
  152    153          self.free = free
         154 +        self.home_reg = (np.hypot(X - hx, Y - hy) <= HOME_R) & free
         155 +        self.home_reg[self.hi, self.hj] = True
  153    156          c, s = math.cos(th), math.sin(th)
  154    157          self.camx = X + c * CAM_OFF[0] - s * CAM_OFF[1]
  155    158          self.camy = Y + s * CAM_OFF[0] + c * CAM_OFF[1]
@@ -284,12 +287,12 @@ class GeneratedApproach:
  284    287  
  285    288          def finish(F, stages, done_keys):
  286    289              if not done_keys and not pending:
  287        -                cost = F[hcell]
         290 +                cost = F[P.home_reg].min()
  288    291                  st = stages
  289    292              else:
  290    293                  G = op_stage(F, P.land)
  291    294                  F2 = propagate(G, P.free)
  292        -                cost = F2[hcell]
         295 +                cost = F2[P.home_reg].min()
  293    296                  st = stages + [("send", None, G, F2)]
  294    297              if cost >= INF:
  295    298                  return
@@ -441,7 +444,7 @@ class GeneratedApproach:
  441    444                      break
  442    445                  t += 1
  443    446              F2 = propagate(G, P.free)
  444        -            if F2[(P.hi, P.hj)] >= INF:
         447 +            if F2[P.home_reg].min() >= INF:
  445    448                  continue
  446    449              st = stages[:-1] + [("send_t", None, G, F2)]
  447    450              new_actions[ri] = self._extract(P, st)
@@ -449,8 +452,10 @@ class GeneratedApproach:
  449    452  
  450    453      def _extract(self, P, stages):
  451    454          """Backtrack through stage fields (waiting allowed); list of (x,y,op)."""
  452        -        cell = (P.hi, P.hj)
  453    455          k = len(stages) - 1
         456 +        Ff = np.where(P.home_reg, stages[k][3], INF)
         457 +        cell = np.unravel_index(int(np.argmin(Ff)), Ff.shape)
         458 +        cell = (int(cell[0]), int(cell[1]))
  454    459          v = int(stages[k][3][cell])
  455    460          seq = []
  456    461          W = WIN
diff --git a/bound.py b/bound.py
new file mode 100644
index 0000000..c9863d2
--- /dev/null
+++ b/bound.py
@@ -0,0 +1,20 @@
           1 +import sys, json
           2 +import numpy as np
           3 +from env_client import make_env
           4 +import approach
           5 +from concurrent.futures import ThreadPoolExecutor
           6 +res=json.load(open('res_seq.json'))
           7 +actual={r[0]:r[3] for r in res}
           8 +orig=approach.seg_hits_box
           9 +def f(seed):
          10 +    env=make_env(); obs,info=env.reset(seed=seed); env.close()
          11 +    approach.seg_hits_box=orig
          12 +    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
          13 +    a=max(len(x) for x in ap.actions)
          14 +    approach.seg_hits_box=lambda px,*a: np.zeros(np.shape(px),dtype=bool)
          15 +    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
          16 +    return seed, a, max(len(x) for x in ap.actions)
          17 +with ThreadPoolExecutor(1) as ex: out=list(ex.map(f, range(120)))
          18 +print("mean plan", np.mean([a for s,a,b in out]), "mean bound", np.mean([b for s,a,b in out]))
          19 +print("actual-plan", [(s,actual[s],a) for s,a,b in out if actual[s]!=a])
          20 +print("gaps", [(s,a,b) for s,a,b in out if a!=b])
diff --git a/res_seq.json b/res_seq.json
new file mode 100644
index 0000000..4c09476
--- /dev/null
+++ b/res_seq.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 26, 0, 0.46, 4.9], [1, 2, true, 21, 0, 0.23, 3.7], [2, 3, true, 21, 0, 1.34, 4.1], [3, 3, true, 22, 0, 1.17, 6.4], [4, 3, true, 21, 0, 1.61, 4.5], [5, 3, true, 24, 0, 1.57, 8.2], [6, 2, true, 21, 0, 1.04, 7.9], [7, 3, true, 22, 0, 2.41, 8.5], [8, 3, true, 22, 0, 1.27, 8.2], [9, 2, true, 23, 0, 0.78, 6.0], [10, 3, true, 22, 0, 1.41, 6.3], [11, 1, true, 20, 0, 0.1, 5.3], [12, 2, true, 24, 0, 0.38, 6.9], [13, 3, true, 25, 0, 1.32, 7.0], [14, 1, true, 30, 0, 0.26, 6.6], [15, 3, true, 22, 0, 1.01, 5.8], [16, 2, true, 22, 0, 0.2, 4.7], [17, 3, true, 22, 0, 3.08, 8.8], [18, 3, true, 22, 0, 0.98, 6.9], [19, 2, true, 24, 0, 0.56, 6.4], [20, 3, true, 28, 0, 0.82, 9.3], [21, 1, true, 20, 0, 0.16, 6.8], [22, 3, true, 24, 0, 1.23, 8.3], [23, 1, true, 18, 0, 0.26, 6.2], [24, 2, true, 20, 0, 0.75, 5.9], [25, 2, true, 20, 0, 0.72, 6.6], [26, 3, true, 22, 0, 1.3, 8.4], [27, 1, true, 22, 0, 0.13, 7.1], [28, 2, true, 23, 0, 0.86, 8.4], [29, 3, true, 22, 0, 0.85, 7.5], [30, 1, true, 20, 0, 0.28, 7.1], [31, 2, true, 26, 0, 0.25, 9.4], [32, 3, true, 21, 0, 0.78, 8.1], [33, 3, true, 24, 0, 0.87, 9.8], [34, 1, true, 21, 0, 0.14, 7.7], [35, 1, true, 19, 0, 0.14, 7.3], [36, 2, true, 21, 0, 0.33, 8.5], [37, 1, true, 19, 0, 0.23, 7.0], [38, 1, true, 20, 0, 0.35, 6.8], [39, 3, true, 23, 0, 0.44, 7.3], [40, 2, true, 21, 0, 0.42, 7.1], [41, 2, true, 20, 0, 0.53, 4.7], [42, 1, true, 24, 0, 0.28, 7.3], [43, 2, true, 25, 0, 0.37, 6.9], [44, 3, true, 21, 0, 0.61, 6.2], [45, 3, true, 22, 0, 0.87, 6.8], [46, 2, true, 20, 0, 0.24, 5.9], [47, 1, true, 21, 0, 0.16, 6.2], [48, 1, true, 18, 0, 0.31, 6.0], [49, 1, true, 23, 0, 0.21, 6.5], [50, 3, true, 22, 0, 1.54, 7.8], [51, 2, true, 22, 0, 0.62, 6.2], [52, 3, true, 22, 0, 1.23, 6.5], [53, 3, true, 21, 0, 1.39, 6.4], [54, 1, true, 20, 0, 0.14, 4.4], [55, 3, true, 27, 0, 1.25, 9.1], [56, 2, true, 23, 0, 0.41, 7.0], [57, 1, true, 19, 0, 0.14, 6.4], [58, 2, true, 24, 0, 0.7, 8.8], [59, 3, true, 22, 0, 2.25, 9.2], [60, 1, true, 23, 0, 0.49, 8.3], [61, 2, true, 21, 0, 0.27, 6.2], [62, 2, true, 23, 0, 0.79, 8.0], [63, 2, true, 22, 0, 0.55, 7.1], [64, 2, true, 22, 0, 0.29, 6.1], [65, 1, true, 18, 0, 0.33, 5.4], [66, 3, true, 22, 0, 0.39, 5.3], [67, 3, true, 21, 0, 0.54, 6.7], [68, 2, true, 21, 0, 0.27, 5.0], [69, 1, true, 21, 0, 0.24, 4.5], [70, 2, true, 21, 0, 0.48, 5.0], [71, 3, true, 22, 0, 2.82, 7.2], [72, 3, true, 21, 0, 2.89, 7.7], [73, 3, true, 21, 0, 1.34, 5.8], [74, 1, true, 20, 0, 0.67, 4.8], [75, 2, true, 19, 0, 0.42, 3.6], [76, 2, true, 23, 0, 0.41, 3.9], [77, 1, true, 21, 0, 0.19, 3.8], [78, 3, true, 23, 0, 0.48, 6.3], [79, 1, true, 23, 0, 0.14, 5.1], [80, 3, true, 21, 0, 1.11, 5.4], [81, 1, true, 21, 0, 0.23, 4.2], [82, 3, true, 21, 0, 0.67, 5.2], [83, 3, true, 22, 0, 0.52, 4.8], [84, 2, true, 23, 0, 0.42, 4.5], [85, 3, true, 21, 0, 1.45, 5.4], [86, 3, true, 21, 0, 0.8, 4.7], [87, 2, true, 23, 0, 0.21, 4.6], [88, 2, true, 21, 0, 0.38, 4.0], [89, 3, true, 30, 0, 0.25, 6.9], [90, 2, true, 22, 0, 0.32, 4.6], [91, 3, true, 24, 0, 0.31, 5.7], [92, 2, true, 24, 0, 0.16, 6.5], [93, 3, true, 24, 0, 0.74, 7.0], [94, 1, true, 20, 0, 0.18, 5.0], [95, 2, true, 22, 0, 0.76, 5.9], [96, 3, true, 22, 0, 0.58, 5.2], [97, 1, true, 27, 0, 0.18, 5.8], [98, 2, true, 24, 0, 0.68, 5.0], [99, 3, true, 24, 0, 0.69, 5.5], [100, 3, true, 25, 0, 0.27, 4.8], [101, 1, true, 19, 0, 0.09, 3.5], [102, 2, true, 22, 0, 0.3, 4.5], [103, 2, true, 21, 0, 0.55, 6.0], [104, 3, true, 22, 0, 1.14, 7.0], [105, 1, true, 21, 0, 0.11, 5.5], [106, 2, true, 21, 0, 0.26, 6.2], [107, 1, true, 22, 0, 0.19, 5.7], [108, 1, true, 18, 0, 0.16, 5.1], [109, 2, true, 21, 0, 0.41, 5.7], [110, 2, true, 21, 0, 0.31, 6.0], [111, 2, true, 21, 0, 0.12, 6.1], [112, 1, true, 19, 0, 0.23, 5.5], [113, 1, true, 20, 0, 0.07, 5.4], [114, 1, true, 21, 0, 0.14, 4.6], [115, 2, true, 22, 0, 0.25, 3.9], [116, 1, true, 22, 0, 0.08, 3.3], [117, 1, true, 26, 0, 0.15, 2.9], [118, 2, true, 21, 0, 0.22, 1.8], [119, 2, true, 20, 0, 0.41, 1.0]]
\ No newline at end of file
```

</details>

<a id="C017"></a>
### C017 · imaging heading -pi/2 with rotation schedule

Commit `31341536d0862beb79d5692ae9fb9f4319731314`; parents: e1ead97c4000536ccca9c5c03643ba6972f87b55. Recorded author date: 2026-10-01T11:42:15+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0969](01_timeline.md#E0969): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_3134153_approach.py) · [Exact all-file diff](evidence/diffs/C017_3134153.diff)

[Previous saved controller snapshot](evidence/versions/C016_e1ead97_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0c23598..32bb7d0 100644
--- a/approach.py
+++ b/approach.py
@@ -22,6 +22,7 @@ OBJ_RANGE = 1.985
   22     22  LANDER_RANGE = 3.985
   23     23  SAMPLE_R = 0.242
   24     24  HOME_R = 0.22
          25 +IMG_TH = -math.pi / 2
   25     26  PILLAR_INFL_OBJ = 0.015
   26     27  PILLAR_INFL_LAND = 0.04
   27     28  ROVER_OCC_R = 0.26
@@ -36,6 +37,18 @@ def _wrap(a):
   36     37      return (a + np.pi) % (2 * np.pi) - np.pi
   37     38  
   38     39  
          40 +def rot_steps(a, b):
          41 +    d = abs(float(_wrap(b - a)))
          42 +    return int(math.ceil(d / 0.4 - 1e-6))
          43 +
          44 +
          45 +def approach_angle(a, b, dmax):
          46 +    d = float(_wrap(b - a))
          47 +    if abs(d) <= dmax:
          48 +        return float(_wrap(b))
          49 +    return float(_wrap(a + math.copysign(dmax, d)))
          50 +
          51 +
   39     52  def seg_hits_box(px, py, qx, qy, cx, cy, hx, hy):
   40     53      """Vectorised: does segment p->q (p arrays, q scalar) intersect AABB?"""
   41     54      dx = qx - px
@@ -126,7 +139,7 @@ class Scene:
  126    139  class RoverPlanner:
  127    140      """Grid + regions for one rover."""
  128    141  
  129        -    def __init__(self, idx, home, scene, other_pos_list):
         142 +    def __init__(self, idx, home, scene, other_pos_list, cur_th=None):
  130    143          self.idx = idx
  131    144          self.home = home  # (x, y, th)
  132    145          hx, hy, th = home
@@ -157,51 +170,75 @@ class RoverPlanner:
  157    170          self.camx = X + c * CAM_OFF[0] - s * CAM_OFF[1]
  158    171          self.camy = Y + s * CAM_OFF[0] + c * CAM_OFF[1]
  159    172          self.scene = scene
         173 +        ith = th if IMG_TH is None else IMG_TH
         174 +        self.img_th = ith
         175 +        cur = th if cur_th is None else cur_th
         176 +        self.cur_th = cur
         177 +        self.nrot_in = rot_steps(cur, ith)
         178 +        self.nrot_out = rot_steps(ith, th)
         179 +        hs = [cur, ith, th]
         180 +        for k in range(1, 9):
         181 +            hs.append(approach_angle(cur, ith, 0.4 * k))
         182 +            hs.append(approach_angle(ith, th, 0.4 * k))
         183 +            hs.append(approach_angle(cur, th, 0.4 * k))
         184 +        self.headings = hs
         185 +        ci, si = math.cos(ith), math.sin(ith)
         186 +        camx_i = X + ci * CAM_OFF[0] - si * CAM_OFF[1]
         187 +        camy_i = Y + si * CAM_OFF[0] + ci * CAM_OFF[1]
  160    188          # objective visibility
  161    189          self.vis = []
  162    190          self.objd = []
  163    191          for ob in scene.objectives:
  164    192              ox, oy = ob["x"], ob["y"]
  165        -            d = np.hypot(ox - self.camx, oy - self.camy)
         193 +            d = np.hypot(ox - camx_i, oy - camy_i)
  166    194              v = (d <= OBJ_RANGE)
  167    195              occ = np.zeros(X.shape, dtype=bool)
  168    196              for (cx, cy, ax, ay) in scene.pillars:
  169    197                  e = PILLAR_INFL_OBJ
  170        -                occ |= seg_hits_box(self.camx, self.camy, ox, oy, cx, cy, ax + e, ay + e)
         198 +                occ |= seg_hits_box(camx_i, camy_i, ox, oy, cx, cy, ax + e, ay + e)
  171    199                  occ |= seg_hits_box(X, Y, ox, oy, cx, cy, ax + e, ay + e)
  172    200              if USE_BACK_OBJ:
  173        -                rel = np.abs(_wrap(np.arctan2(oy - Y, ox - X) - th))
         201 +                rel = np.abs(_wrap(np.arctan2(oy - Y, ox - X) - ith))
  174    202                  back = rel > math.radians(OBJ_BACK_DEG)
  175    203              else:
  176    204                  back = np.zeros(X.shape, dtype=bool)
  177    205              occ2 = np.zeros(X.shape, dtype=bool)
  178    206              for (px, py) in other_pos_list:
  179        -                occ2 |= seg_hits_disk(self.camx, self.camy, ox, oy, px, py, ROVER_OCC_R)
         207 +                occ2 |= seg_hits_disk(camx_i, camy_i, ox, oy, px, py, ROVER_OCC_R)
  180    208              self.vis.append(v & ((~occ) | back) & ~occ2 & free)
  181    209              self.objd.append(d)
  182    210          self.any_vis = np.zeros(X.shape, dtype=bool)
  183    211          for v in self.vis:
  184    212              self.any_vis |= v
  185        -        # lander visibility
         213 +        # lander visibility (must hold for every heading along the rotation path)
  186    214          lx, ly = scene.lander
  187        -        v = (np.hypot(lx - X, ly - Y) <= LANDER_RANGE) & \
  188        -            (np.hypot(lx - self.camx, ly - self.camy) <= LANDER_RANGE)
  189        -        occ = np.zeros(X.shape, dtype=bool)
  190        -        for (cx, cy, ax, ay) in scene.pillars:
  191        -            e = PILLAR_INFL_LAND
  192        -            occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
  193        -            occ |= seg_hits_box(self.camx, self.camy, lx, ly, cx, cy, ax + e, ay + e)
  194        -        if USE_BACK_LAND:
  195        -            rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - th))
  196        -            back = rel > math.radians(LAND_BACK_DEG)
  197        -        else:
  198        -            back = np.zeros(X.shape, dtype=bool)
  199        -        occ2 = np.zeros(X.shape, dtype=bool)
  200        -        for (px, py) in other_pos_list:
  201        -            occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
  202        -            occ2 |= seg_hits_disk(self.camx, self.camy, lx, ly, px, py, ROVER_OCC_R)
  203        -        self.land = v & ((~occ) | back) & ~occ2 & free
  204        -        self.land_free = v & ((~occ) | back) & free
         215 +        land = free.copy()
         216 +        land_free = free.copy()
         217 +        for hh in self.headings:
         218 +            ch, sh = math.cos(hh), math.sin(hh)
         219 +            cx_ = X + ch * CAM_OFF[0] - sh * CAM_OFF[1]
         220 +            cy_ = Y + sh * CAM_OFF[0] + ch * CAM_OFF[1]
         221 +            v = (np.hypot(lx - X, ly - Y) <= LANDER_RANGE) & \
         222 +                (np.hypot(lx - cx_, ly - cy_) <= LANDER_RANGE)
         223 +            occ = np.zeros(X.shape, dtype=bool)
         224 +            for (cx, cy, ax, ay) in scene.pillars:
         225 +                e = PILLAR_INFL_LAND
         226 +                occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
         227 +                occ |= seg_hits_box(cx_, cy_, lx, ly, cx, cy, ax + e, ay + e)
         228 +            if USE_BACK_LAND:
         229 +                rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - hh))
         230 +                back = rel > math.radians(LAND_BACK_DEG)
         231 +            else:
         232 +                back = np.zeros(X.shape, dtype=bool)
         233 +            occ2 = np.zeros(X.shape, dtype=bool)
         234 +            for (px, py) in other_pos_list:
         235 +                occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
         236 +                occ2 |= seg_hits_disk(cx_, cy_, lx, ly, px, py, ROVER_OCC_R)
         237 +            land &= v & ((~occ) | back) & ~occ2
         238 +            land_free &= v & ((~occ) | back)
         239 +        self.land = land
         240 +        self.land_free = land_free
         241 +        self.camx_i, self.camy_i = camx_i, camy_i
  205    242          # samples
  206    243          self.sreg = {}
  207    244          dk = {}
@@ -260,7 +297,7 @@ class GeneratedApproach:
  260    297          occl = [(ohome[0], ohome[1])]
  261    298          if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
  262    299              occl.append((other["x"], other["y"]))
  263        -        P = RoverPlanner(ri, self.homes[name], sc, occl)
         300 +        P = RoverPlanner(ri, self.homes[name], sc, occl, r["th"])
  264    301          self_planner = P
  265    302          start = P.cell_of(r["x"], r["y"])
  266    303          P.free[start] = True
@@ -314,10 +351,12 @@ class GeneratedApproach:
  314    351                      Fc = F
  315    352                      if not cal:
  316    353                          G = op_stage(F, P.any_vis)
         354 +                        G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
  317    355                          Fc = propagate(G, P.free)
  318    356                          st.append(("cal", None, G, Fc))
  319    357                      reg = P.img_region(k, imaged)
  320    358                      G = op_stage(Fc, reg)
         359 +                    G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
  321    360                      Fi = propagate(G, P.free)
  322    361                      st.append(("img", k, G, Fi))
  323    362                      dfs(Fi, st, done_keys | {key}, imaged | {k}, False)
@@ -437,6 +476,7 @@ class GeneratedApproach:
  437    476                  for tt in (t - 1, t):
  438    477                      ox, oy = other[max(0, min(tt, len(other) - 1))]
  439    478                      blk |= seg_hits_disk(P.camx, P.camy, lx, ly, ox, oy, ROVER_OCC_R)
         479 +                    blk |= seg_hits_disk(P.camx_i, P.camy_i, lx, ly, ox, oy, ROVER_OCC_R)
  440    480                  ok = pending_mask & (G0 <= t) & ~blk
  441    481                  G[ok] = t
  442    482                  pending_mask &= ~ok
@@ -448,7 +488,33 @@ class GeneratedApproach:
  448    488                  continue
  449    489              st = stages[:-1] + [("send_t", None, G, F2)]
  450    490              new_actions[ri] = self._extract(P, st)
  451        -        return new_actions
         491 +        return [self._schedule(tabs[ri][0], new_actions[ri]) for ri in range(2)]
         492 +
         493 +    def _schedule(self, P, seq):
         494 +        """Attach headings; append waits so the rover can rotate back home."""
         495 +        home_th = P.th
         496 +        t_img = [t for t, a in enumerate(seq, 1) if a[2] and a[2][0] in ("cal", "img")]
         497 +        seq = list(seq)
         498 +        out = []
         499 +        if t_img:
         500 +            last = max(t_img)
         501 +            while len(seq) < last + P.nrot_out:
         502 +                x, y = (seq[-1][0], seq[-1][1])
         503 +                seq.append((x, y, None))
         504 +            T = len(seq)
         505 +            for t, (x, y, op) in enumerate(seq, 1):
         506 +                if t <= T - P.nrot_out:
         507 +                    h = approach_angle(P.cur_th, P.img_th, 0.4 * t)
         508 +                else:
         509 +                    h = approach_angle(P.img_th, home_th, 0.4 * (t - (T - P.nrot_out)))
         510 +                out.append((x, y, op, h))
         511 +        else:
         512 +            while len(seq) < rot_steps(P.cur_th, home_th):
         513 +                x, y = (seq[-1][0], seq[-1][1]) if seq else (float(P.xs[P.hi]), float(P.ys[P.hj]))
         514 +                seq.append((x, y, None))
         515 +            for t, (x, y, op) in enumerate(seq, 1):
         516 +                out.append((x, y, op, approach_angle(P.cur_th, home_th, 0.4 * t)))
         517 +        return out
  452    518  
  453    519      def _extract(self, P, stages):
  454    520          """Backtrack through stage fields (waiting allowed); list of (x,y,op)."""
@@ -511,13 +577,14 @@ class GeneratedApproach:
  511    577          for ri in range(2):
  512    578              r = sc.rovers["rover%d" % ri]
  513    579              if self.actions[ri]:
  514        -                x, y, op = self.actions[ri].pop(0)
         580 +                x, y, op, h = self.actions[ri].pop(0)
  515    581                  dx = float(np.clip(x - r["x"], -0.2, 0.2))
  516    582                  dy = float(np.clip(y - r["y"], -0.2, 0.2))
  517    583                  act[4 * ri] = dx
  518    584                  act[4 * ri + 1] = dy
  519    585                  act[4 * ri + 3] = SEL[op[0]] if op else 0.0
  520        -                self.expect[ri] = (x, y, op)
         586 +                act[4 * ri + 2] = float(np.clip(_wrap(h - r["th"]), -0.4, 0.4))
         587 +                self.expect[ri] = (x, y, op, h)
  521    588              else:
  522    589                  # at end: if at home do nothing
  523    590                  self.expect[ri] = None
@@ -532,7 +599,8 @@ class GeneratedApproach:
  532    599              d0 = dev
  533    600              dev = False
  534    601              r = sc.rovers["rover%d" % ri]
  535        -            if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3:
         602 +            if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3 or \
         603 +                    abs(float(_wrap(r["th"] - e[3]))) > 1e-3:
  536    604                  dev = True
  537    605                  self.log.append(("move", ri, e, r["x"], r["y"]))
  538    606              op, arg = e[2] if e[2] else (None, None)
diff --git a/approach_fine.py b/approach_fine.py
new file mode 100644
index 0000000..e81cbd7
--- /dev/null
+++ b/approach_fine.py
@@ -0,0 +1,568 @@
           1 +"""Rovers approach: staged grid BFS planner per rover + joint task assignment."""
           2 +import itertools
           3 +import math
           4 +
           5 +import numpy as np
           6 +from scipy.ndimage import minimum_filter
           7 +
           8 +INF = 10 ** 6
           9 +RES = 0.025            # grid resolution
          10 +WIN = 8               # max cells per step per axis (0.2 / RES)
          11 +SEL = {"sample": -0.8333, "cal": -0.5, "img": -0.1667, "noop": 0.1667,
          12 +       "send": 0.5, "drop": 0.8333}
          13 +
          14 +# geometry constants (empirically probed)
          15 +WALL_IN = 0.2271 + 0.004
          16 +ARENA = 2.2729 - 0.004
          17 +PILLAR_R = 0.245
          18 +MOUND_R = 0.185
          19 +LANDER_XMIN = -1.195
          20 +LANDER_YMIN = -1.455
          21 +OBJ_RANGE = 1.985
          22 +LANDER_RANGE = 3.985
          23 +SAMPLE_R = 0.242
          24 +HOME_R = 0.22
          25 +PILLAR_INFL_OBJ = 0.015
          26 +PILLAR_INFL_LAND = 0.04
          27 +ROVER_OCC_R = 0.26
          28 +CAM_OFF = (-0.087, -0.0125)
          29 +OBJ_BACK_DEG = 108.0     # if |rel bearing| > this, pillars don't occlude objectives
          30 +LAND_BACK_DEG = 110.0    # same quirk for lander (sending)
          31 +USE_BACK_OBJ = True
          32 +USE_BACK_LAND = True
          33 +
          34 +
          35 +def _wrap(a):
          36 +    return (a + np.pi) % (2 * np.pi) - np.pi
          37 +
          38 +
          39 +def seg_hits_box(px, py, qx, qy, cx, cy, hx, hy):
          40 +    """Vectorised: does segment p->q (p arrays, q scalar) intersect AABB?"""
          41 +    dx = qx - px
          42 +    dy = qy - py
          43 +    t0 = np.zeros_like(px)
          44 +    t1 = np.ones_like(px)
          45 +    ok = np.ones(px.shape, dtype=bool)
          46 +    for d, p, lo, hi in ((dx, px, cx - hx, cx + hx), (dy, py, cy - hy, cy + hy)):
          47 +        small = np.abs(d) < 1e-12
          48 +        ok &= ~(small & ((p < lo) | (p > hi)))
          49 +        with np.errstate(divide="ignore", invalid="ignore"):
          50 +            ta = (lo - p) / d
          51 +            tb = (hi - p) / d
          52 +        tmin = np.where(small, -np.inf, np.minimum(ta, tb))
          53 +        tmax = np.where(small, np.inf, np.maximum(ta, tb))
          54 +        t0 = np.maximum(t0, tmin)
          55 +        t1 = np.minimum(t1, tmax)
          56 +    return ok & (t0 <= t1)
          57 +
          58 +
          59 +def seg_hits_disk(px, py, qx, qy, cx, cy, r):
          60 +    dx = qx - px
          61 +    dy = qy - py
          62 +    L2 = dx * dx + dy * dy + 1e-12
          63 +    t = np.clip(((cx - px) * dx + (cy - py) * dy) / L2, 0, 1)
          64 +    ex = px + t * dx - cx
          65 +    ey = py + t * dy - cy
          66 +    return ex * ex + ey * ey < r * r
          67 +
          68 +
          69 +def box_dist(px, py, cx, cy, hx, hy):
          70 +    ddx = np.maximum(np.abs(px - cx) - hx, 0)
          71 +    ddy = np.maximum(np.abs(py - cy) - hy, 0)
          72 +    return np.hypot(ddx, ddy)
          73 +
          74 +
          75 +def propagate(f, free):
          76 +    f = np.where(free, f, INF)
          77 +    while True:
          78 +        m = minimum_filter(f, size=2 * WIN + 1, mode="constant", cval=INF) + 1
          79 +        nf = np.where(free, np.minimum(f, m), INF)
          80 +        if np.array_equal(nf, f):
          81 +            return f
          82 +        f = nf
          83 +
          84 +
          85 +def op_stage(fprev, region):
          86 +    m = minimum_filter(fprev, size=2 * WIN + 1, mode="constant", cval=INF) + 1
          87 +    return np.where(region, np.minimum(m, INF), INF)
          88 +
          89 +
          90 +class Scene:
          91 +    def __init__(self, state):
          92 +        self.rovers = {}
          93 +        self.objectives = []
          94 +        self.samples = []
          95 +        self.pillars = []
          96 +        self.mounds = []
          97 +        self.lander = (-1.9, -2.0)
          98 +        for o in state:
          99 +            t = o.type.name
         100 +            g = lambda f: state.get(o, f)
         101 +            if t == "rover":
         102 +                self.rovers[o.name] = dict(x=g("x"), y=g("y"), th=g("theta"),
         103 +                                           full=g("store_full") > 0.5,
         104 +                                           cal=g("calibrated") > 0.5)
         105 +            elif t == "lander":
         106 +                self.lander = (g("x"), g("y"))
         107 +            elif t == "objective":
         108 +                self.objectives.append(dict(name=o.name, x=g("x"), y=g("y"),
         109 +                                            img=(g("have_image_rover0") > 0.5,
         110 +                                                 g("have_image_rover1") > 0.5),
         111 +                                            recv=g("received_image") > 0.5))
         112 +            elif t == "sample":
         113 +                self.samples.append(dict(name=o.name, x=g("x"), y=g("y"),
         114 +                                         soil=g("is_soil") > 0.5,
         115 +                                         an=(g("analyzed_rover0") > 0.5,
         116 +                                             g("analyzed_rover1") > 0.5),
         117 +                                         recv=g("received_analysis") > 0.5))
         118 +            elif t == "obstacle":
         119 +                d = (g("x"), g("y"), g("half_x"), g("half_y"))
         120 +                if g("half_x") > 0.15:
         121 +                    self.mounds.append(d)
         122 +                else:
         123 +                    self.pillars.append(d)
         124 +
         125 +
         126 +class RoverPlanner:
         127 +    """Grid + regions for one rover."""
         128 +
         129 +    def __init__(self, idx, home, scene, other_pos_list):
         130 +        self.idx = idx
         131 +        self.home = home  # (x, y, th)
         132 +        hx, hy, th = home
         133 +        self.th = th
         134 +        side = 1 if hx > 0 else -1
         135 +        lo_x, hi_x = (WALL_IN, ARENA) if side > 0 else (-ARENA, -WALL_IN)
         136 +        i0 = math.ceil((lo_x - hx) / RES - 1e-9)
         137 +        i1 = math.floor((hi_x - hx) / RES + 1e-9)
         138 +        j0 = math.ceil((-ARENA - hy) / RES - 1e-9)
         139 +        j1 = math.floor((ARENA - hy) / RES + 1e-9)
         140 +        self.xs = hx + RES * np.arange(i0, i1 + 1)
         141 +        self.ys = hy + RES * np.arange(j0, j1 + 1)
         142 +        self.hi = -i0
         143 +        self.hj = -j0
         144 +        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
         145 +        self.X, self.Y = X, Y
         146 +        free = np.ones(X.shape, dtype=bool)
         147 +        for (cx, cy, ax, ay) in scene.pillars:
         148 +            free &= box_dist(X, Y, cx, cy, ax, ay) > PILLAR_R
         149 +        for (cx, cy, ax, ay) in scene.mounds:
         150 +            free &= box_dist(X, Y, cx, cy, ax, ay) > MOUND_R
         151 +        free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
         152 +        free[self.hi, self.hj] = True
         153 +        self.free = free
         154 +        self.home_reg = (np.hypot(X - hx, Y - hy) <= HOME_R) & free
         155 +        self.home_reg[self.hi, self.hj] = True
         156 +        c, s = math.cos(th), math.sin(th)
         157 +        self.camx = X + c * CAM_OFF[0] - s * CAM_OFF[1]
         158 +        self.camy = Y + s * CAM_OFF[0] + c * CAM_OFF[1]
         159 +        self.scene = scene
         160 +        # objective visibility
         161 +        self.vis = []
         162 +        self.objd = []
         163 +        for ob in scene.objectives:
         164 +            ox, oy = ob["x"], ob["y"]
         165 +            d = np.hypot(ox - self.camx, oy - self.camy)
         166 +            v = (d <= OBJ_RANGE)
         167 +            occ = np.zeros(X.shape, dtype=bool)
         168 +            for (cx, cy, ax, ay) in scene.pillars:
         169 +                e = PILLAR_INFL_OBJ
         170 +                occ |= seg_hits_box(self.camx, self.camy, ox, oy, cx, cy, ax + e, ay + e)
         171 +                occ |= seg_hits_box(X, Y, ox, oy, cx, cy, ax + e, ay + e)
         172 +            if USE_BACK_OBJ:
         173 +                rel = np.abs(_wrap(np.arctan2(oy - Y, ox - X) - th))
         174 +                back = rel > math.radians(OBJ_BACK_DEG)
         175 +            else:
         176 +                back = np.zeros(X.shape, dtype=bool)
         177 +            occ2 = np.zeros(X.shape, dtype=bool)
         178 +            for (px, py) in other_pos_list:
         179 +                occ2 |= seg_hits_disk(self.camx, self.camy, ox, oy, px, py, ROVER_OCC_R)
         180 +            self.vis.append(v & ((~occ) | back) & ~occ2 & free)
         181 +            self.objd.append(d)
         182 +        self.any_vis = np.zeros(X.shape, dtype=bool)
         183 +        for v in self.vis:
         184 +            self.any_vis |= v
         185 +        # lander visibility
         186 +        lx, ly = scene.lander
         187 +        v = (np.hypot(lx - X, ly - Y) <= LANDER_RANGE) & \
         188 +            (np.hypot(lx - self.camx, ly - self.camy) <= LANDER_RANGE)
         189 +        occ = np.zeros(X.shape, dtype=bool)
         190 +        for (cx, cy, ax, ay) in scene.pillars:
         191 +            e = PILLAR_INFL_LAND
         192 +            occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
         193 +            occ |= seg_hits_box(self.camx, self.camy, lx, ly, cx, cy, ax + e, ay + e)
         194 +        if USE_BACK_LAND:
         195 +            rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - th))
         196 +            back = rel > math.radians(LAND_BACK_DEG)
         197 +        else:
         198 +            back = np.zeros(X.shape, dtype=bool)
         199 +        occ2 = np.zeros(X.shape, dtype=bool)
         200 +        for (px, py) in other_pos_list:
         201 +            occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
         202 +            occ2 |= seg_hits_disk(self.camx, self.camy, lx, ly, px, py, ROVER_OCC_R)
         203 +        self.land = v & ((~occ) | back) & ~occ2 & free
         204 +        self.land_free = v & ((~occ) | back) & free
         205 +        # samples
         206 +        self.sreg = {}
         207 +        dk = {}
         208 +        for kind in ("stone", "soil"):
         209 +            d = np.full(X.shape, 1e9)
         210 +            for sm in scene.samples:
         211 +                if sm["soil"] == (kind == "soil"):
         212 +                    d = np.minimum(d, np.hypot(sm["x"] - X, sm["y"] - Y))
         213 +            dk[kind] = d
         214 +        for kind, oth in (("stone", "soil"), ("soil", "stone")):
         215 +            r = (dk[kind] <= SAMPLE_R) & ((dk[oth] > 0.26) | (dk[oth] > dk[kind] + 0.03))
         216 +            self.sreg[kind] = r & free
         217 +
         218 +    def cell_of(self, x, y):
         219 +        i = int(round((x - self.xs[0]) / RES))
         220 +        j = int(round((y - self.ys[0]) / RES))
         221 +        i = min(max(i, 0), len(self.xs) - 1)
         222 +        j = min(max(j, 0), len(self.ys) - 1)
         223 +        return i, j
         224 +
         225 +    def img_region(self, k, imaged):
         226 +        """cells where image would photograph objective k given set imaged."""
         227 +        reg = self.vis[k].copy()
         228 +        if not reg.any():
         229 +            return reg
         230 +        dk = self.objd[k]
         231 +        for m in range(len(self.vis)):
         232 +            if m == k or m in imaged:
         233 +                continue
         234 +            reg &= ~((self.objd[m] <= 2.03) & (self.objd[m] < dk + 0.03))
         235 +        return reg
         236 +
         237 +
         238 +class GeneratedApproach:
         239 +    def __init__(self, action_space, observation_space, primitives):
         240 +        self.action_space = action_space
         241 +        self.homes = None
         242 +
         243 +    # ------------------------------------------------------------------
         244 +    def reset(self, state, info):
         245 +        sc = Scene(state)
         246 +        self.homes = {n: (r["x"], r["y"], r["th"]) for n, r in sc.rovers.items()}
         247 +        self.replans = 0
         248 +        self.fail_count = 0
         249 +        self.expect = [None, None]
         250 +        self.prev_sc = sc
         251 +        self.log = []
         252 +        self._plan(state)
         253 +
         254 +    # ------------------------------------------------------------------
         255 +    def _rover_tables(self, ri, sc, need_objs, need_stone, need_soil, pending):
         256 +        name = "rover%d" % ri
         257 +        r = sc.rovers[name]
         258 +        other = sc.rovers["rover%d" % (1 - ri)]
         259 +        ohome = self.homes["rover%d" % (1 - ri)]
         260 +        occl = [(ohome[0], ohome[1])]
         261 +        if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
         262 +            occl.append((other["x"], other["y"]))
         263 +        P = RoverPlanner(ri, self.homes[name], sc, occl)
         264 +        self_planner = P
         265 +        start = P.cell_of(r["x"], r["y"])
         266 +        P.free[start] = True
         267 +        f0 = np.full(P.free.shape, INF, dtype=np.int64)
         268 +        f0[start] = 0
         269 +        stages0 = []
         270 +        F = propagate(f0, P.free)
         271 +        stages0.append(("start", None, f0, F))
         272 +        if r["full"]:
         273 +            G = op_stage(F, P.free)
         274 +            F = propagate(G, P.free)
         275 +            stages0.append(("drop", None, G, F))
         276 +        imaged0 = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
         277 +        tasks = []
         278 +        for k in need_objs:
         279 +            if P.vis[k].any():
         280 +                tasks.append(("obj", k))
         281 +        if need_stone and P.sreg["stone"].any():
         282 +            tasks.append(("stone", None))
         283 +        if need_soil and P.sreg["soil"].any():
         284 +            tasks.append(("soil", None))
         285 +        hcell = (P.hi, P.hj)
         286 +        table = {}  # frozenset(task keys) -> (cost, stages)
         287 +
         288 +        def finish(F, stages, done_keys):
         289 +            if not done_keys and not pending:
         290 +                cost = F[P.home_reg].min()
         291 +                st = stages
         292 +            else:
         293 +                G = op_stage(F, P.land)
         294 +                F2 = propagate(G, P.free)
         295 +                cost = F2[P.home_reg].min()
         296 +                st = stages + [("send", None, G, F2)]
         297 +            if cost >= INF:
         298 +                return
         299 +            key = frozenset(done_keys)
         300 +            if key not in table or cost < table[key][0]:
         301 +                table[key] = (int(cost), st)
         302 +
         303 +        def dfs(F, stages, done_keys, imaged, cal):
         304 +            finish(F, stages, done_keys)
         305 +            if F.min() >= INF:
         306 +                return
         307 +            for t in tasks:
         308 +                key = t if t[0] != "obj" else ("obj", t[1])
         309 +                if key in done_keys:
         310 +                    continue
         311 +                if t[0] == "obj":
         312 +                    k = t[1]
         313 +                    st = list(stages)
         314 +                    Fc = F
         315 +                    if not cal:
         316 +                        G = op_stage(F, P.any_vis)
         317 +                        Fc = propagate(G, P.free)
         318 +                        st.append(("cal", None, G, Fc))
         319 +                    reg = P.img_region(k, imaged)
         320 +                    G = op_stage(Fc, reg)
         321 +                    Fi = propagate(G, P.free)
         322 +                    st.append(("img", k, G, Fi))
         323 +                    dfs(Fi, st, done_keys | {key}, imaged | {k}, False)
         324 +                else:
         325 +                    G = op_stage(F, P.sreg[t[0]])
         326 +                    Fs = propagate(G, P.free)
         327 +                    G2 = op_stage(Fs, P.free)
         328 +                    Fd = propagate(G2, P.free)
         329 +                    st = stages + [("sample", t[0], G, Fs), ("drop", None, G2, Fd)]
         330 +                    dfs(Fd, st, done_keys | {key}, imaged, cal)
         331 +
         332 +        dfs(F, stages0, frozenset(), imaged0, r["cal"])
         333 +        return P, table
         334 +
         335 +    def _plan(self, state):
         336 +        sc = Scene(state)
         337 +        self.scene = sc
         338 +        # what is needed
         339 +        need_objs = [k for k, ob in enumerate(sc.objectives)
         340 +                     if not ob["recv"] and not ob["img"][0] and not ob["img"][1]]
         341 +        pending = [False, False]
         342 +        for k, ob in enumerate(sc.objectives):
         343 +            if not ob["recv"]:
         344 +                for ri in range(2):
         345 +                    if ob["img"][ri]:
         346 +                        pending[ri] = True
         347 +        need = {}
         348 +        for kind in ("stone", "soil"):
         349 +            recv = any(s["recv"] for s in sc.samples if s["soil"] == (kind == "soil"))
         350 +            holders = [ri for ri in range(2)
         351 +                       if any(s["an"][ri] for s in sc.samples if s["soil"] == (kind == "soil"))]
         352 +            if recv:
         353 +                need[kind] = False
         354 +            elif holders:
         355 +                need[kind] = False
         356 +                pending[holders[0]] = True
         357 +            else:
         358 +                need[kind] = True
         359 +        tabs = []
         360 +        for ri in range(2):
         361 +            tabs.append(self._rover_tables(ri, sc, need_objs, need["stone"], need["soil"],
         362 +                                           pending[ri]))
         363 +        # joint assignment
         364 +        best = None
         365 +        cands = []
         366 +        n = len(need_objs)
         367 +        stone_opts = [0, 1] if need["stone"] else [None]
         368 +        soil_opts = [0, 1] if need["soil"] else [None]
         369 +        for assign in itertools.product([0, 1], repeat=n):
         370 +            for so in stone_opts:
         371 +                for sl in soil_opts:
         372 +                    sets = [set(), set()]
         373 +                    for k, a in zip(need_objs, assign):
         374 +                        sets[a].add(("obj", k))
         375 +                    if so is not None:
         376 +                        sets[so].add(("stone", None))
         377 +                    if sl is not None:
         378 +                        sets[sl].add(("soil", None))
         379 +                    costs = []
         380 +                    for ri in range(2):
         381 +                        e = tabs[ri][1].get(frozenset(sets[ri]))
         382 +                        costs.append(e)
         383 +                    if costs[0] is None or costs[1] is None:
         384 +                        continue
         385 +                    key = (max(costs[0][0], costs[1][0]), costs[0][0] + costs[1][0])
         386 +                    cands.append((key, costs))
         387 +                    if best is None or key < best[0]:
         388 +                        self.pred = key
         389 +                        best = (key, costs)
         390 +        self.actions = [[], []]
         391 +        if best is None:
         392 +            return
         393 +        cands.sort(key=lambda c: c[0])
         394 +        seen = set()
         395 +        bestreal = None
         396 +        for key, costs in cands:
         397 +            sig = (id(costs[0][1]), id(costs[1][1]))
         398 +            if sig in seen:
         399 +                continue
         400 +            seen.add(sig)
         401 +            if len(seen) > 6 or (bestreal is not None and key[0] >= bestreal[0][0]):
         402 +                break
         403 +            acts = self._realize(sc, tabs, costs)
         404 +            real = (max(len(acts[0]), len(acts[1])), len(acts[0]) + len(acts[1]))
         405 +            if bestreal is None or real < bestreal[0]:
         406 +                bestreal = (real, acts)
         407 +        self.actions = bestreal[1]
         408 +
         409 +    def _realize(self, sc, tabs, costs):
         410 +        best = (None, costs)
         411 +        actions = [[], []]
         412 +        sc = self.scene
         413 +        for ri in range(2):
         414 +            P = tabs[ri][0]
         415 +            actions[ri] = self._extract(P, best[1][ri][1])
         416 +        # time-aware re-plan of final send against other rover's trajectory
         417 +        trajs = []
         418 +        for ri in range(2):
         419 +            r = sc.rovers["rover%d" % ri]
         420 +            trajs.append([(r["x"], r["y"])] + [(a[0], a[1]) for a in actions[ri]])
         421 +        new_actions = list(actions)
         422 +        for ri in range(2):
         423 +            stages = best[1][ri][1]
         424 +            if stages[-1][0] != "send":
         425 +                continue
         426 +            P = tabs[ri][0]
         427 +            Fprev = stages[-2][3]
         428 +            G0 = op_stage(Fprev, P.land_free)
         429 +            other = trajs[1 - ri]
         430 +            G = np.full(G0.shape, INF, dtype=G0.dtype)
         431 +            pending_mask = G0 < INF
         432 +            tmin = int(G0[pending_mask].min()) if pending_mask.any() else INF
         433 +            lx, ly = sc.lander
         434 +            t = tmin
         435 +            while pending_mask.any() and t < tmin + 200:
         436 +                blk = np.zeros(P.X.shape, dtype=bool)
         437 +                for tt in (t - 1, t):
         438 +                    ox, oy = other[max(0, min(tt, len(other) - 1))]
         439 +                    blk |= seg_hits_disk(P.camx, P.camy, lx, ly, ox, oy, ROVER_OCC_R)
         440 +                ok = pending_mask & (G0 <= t) & ~blk
         441 +                G[ok] = t
         442 +                pending_mask &= ~ok
         443 +                if t >= len(other) - 1 and not ok.any() and (G0 <= t).all():
         444 +                    break
         445 +                t += 1
         446 +            F2 = propagate(G, P.free)
         447 +            if F2[P.home_reg].min() >= INF:
         448 +                continue
         449 +            st = stages[:-1] + [("send_t", None, G, F2)]
         450 +            new_actions[ri] = self._extract(P, st)
         451 +        return new_actions
         452 +
         453 +    def _extract(self, P, stages):
         454 +        """Backtrack through stage fields (waiting allowed); list of (x,y,op)."""
         455 +        k = len(stages) - 1
         456 +        Ff = np.where(P.home_reg, stages[k][3], INF)
         457 +        cell = np.unravel_index(int(np.argmin(Ff)), Ff.shape)
         458 +        cell = (int(cell[0]), int(cell[1]))
         459 +        v = int(stages[k][3][cell])
         460 +        seq = []
         461 +        W = WIN
         462 +        nx, ny = P.free.shape
         463 +
         464 +        def nb(Fsrc, i, j, cond):
         465 +            best = None
         466 +            for di in range(-W, W + 1):
         467 +                for dj in range(-W, W + 1):
         468 +                    a, b = i + di, j + dj
         469 +                    if 0 <= a < nx and 0 <= b < ny and cond(Fsrc[a, b]):
         470 +                        c = abs(di) + abs(dj)
         471 +                        if best is None or c < best[1]:
         472 +                            best = ((a, b), c)
         473 +            return best[0] if best else None
         474 +
         475 +        guard = 0
         476 +        while not (k == 0 and v == 0) and guard < 5000:
         477 +            guard += 1
         478 +            name, arg, G, F = stages[k]
         479 +            i, j = cell
         480 +            timed = name == "send_t"
         481 +            choice = None
         482 +            for mode in (0, 1):
         483 +                if k > 0:
         484 +                    okop = (G[cell] == v) if (mode == 0 or timed) else (G[cell] <= v)
         485 +                    if okop:
         486 +                        Fp = stages[k - 1][3]
         487 +                        c = nb(Fp, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
         488 +                        if c is not None:
         489 +                            choice = (c, (name.replace("_t", ""), arg), k - 1)
         490 +                            break
         491 +                c = nb(F, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
         492 +                if c is not None:
         493 +                    choice = (c, None, k)
         494 +                    break
         495 +            if choice is None:
         496 +                break
         497 +            seq.append((float(P.xs[cell[0]]), float(P.ys[cell[1]]), choice[1]))
         498 +            cell, k = choice[0], choice[2]
         499 +            v -= 1
         500 +        seq.reverse()
         501 +        return seq
         502 +
         503 +    # ------------------------------------------------------------------
         504 +    def get_action(self, state):
         505 +        act = np.zeros(8, dtype=np.float32)
         506 +        sc = Scene(state)
         507 +        if self._deviated(sc) or (not self.actions[0] and not self.actions[1]):
         508 +            self.replans += 1
         509 +            if self.replans < 40:
         510 +                self._plan(state)
         511 +        for ri in range(2):
         512 +            r = sc.rovers["rover%d" % ri]
         513 +            if self.actions[ri]:
         514 +                x, y, op = self.actions[ri].pop(0)
         515 +                dx = float(np.clip(x - r["x"], -0.2, 0.2))
         516 +                dy = float(np.clip(y - r["y"], -0.2, 0.2))
         517 +                act[4 * ri] = dx
         518 +                act[4 * ri + 1] = dy
         519 +                act[4 * ri + 3] = SEL[op[0]] if op else 0.0
         520 +                self.expect[ri] = (x, y, op)
         521 +            else:
         522 +                # at end: if at home do nothing
         523 +                self.expect[ri] = None
         524 +        return act
         525 +
         526 +    def _deviated(self, sc):
         527 +        dev = False
         528 +        for ri in range(2):
         529 +            e = self.expect[ri]
         530 +            if e is None:
         531 +                continue
         532 +            d0 = dev
         533 +            dev = False
         534 +            r = sc.rovers["rover%d" % ri]
         535 +            if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3:
         536 +                dev = True
         537 +                self.log.append(("move", ri, e, r["x"], r["y"]))
         538 +            op, arg = e[2] if e[2] else (None, None)
         539 +            pr = self.prev_sc.rovers["rover%d" % ri]
         540 +            if op == "img":
         541 +                ob = sc.objectives[arg]
         542 +                if not ob["img"][ri]:
         543 +                    dev = True
         544 +            if op == "sample":
         545 +                if not any(s["an"][ri] for s in sc.samples if s["soil"] == (arg == "soil")):
         546 +                    dev = True
         547 +            if op == "cal" and not r["cal"]:
         548 +                dev = True
         549 +            elif op == "img" and (r["cal"] or not pr["cal"]):
         550 +                dev = True
         551 +            elif op == "sample" and not r["full"]:
         552 +                dev = True
         553 +            elif op == "drop" and r["full"]:
         554 +                dev = True
         555 +            elif op == "send":
         556 +                for ob in sc.objectives:
         557 +                    if ob["img"][ri] and not ob["recv"]:
         558 +                        dev = True
         559 +                for s in sc.samples:
         560 +                    if s["an"][ri] and not s["recv"]:
         561 +                        dev = True
         562 +            if dev:
         563 +                self.log.append(("dev", ri, e, round(r["x"], 3), round(r["y"], 3), r["cal"], pr["cal"],
         564 +                                 [ob["img"][ri] for ob in sc.objectives]))
         565 +            dev = dev or d0
         566 +        self.prev_sc = sc
         567 +        self.expect = [None, None]
         568 +        return dev
diff --git a/bound2.py b/bound2.py
new file mode 100644
index 0000000..6109b7b
--- /dev/null
+++ b/bound2.py
@@ -0,0 +1,16 @@
           1 +import sys, json
           2 +import numpy as np
           3 +from env_client import make_env
           4 +import approach
           5 +from concurrent.futures import ThreadPoolExecutor
           6 +def f(seed):
           7 +    env=make_env(); obs,info=env.reset(seed=seed); env.close()
           8 +    approach.IMG_TH=None
           9 +    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
          10 +    a=max(len(x) for x in ap.actions)
          11 +    approach.IMG_TH=-np.pi/2
          12 +    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
          13 +    return seed, a, max(len(x) for x in ap.actions)
          14 +with ThreadPoolExecutor(1) as ex: out=list(ex.map(f, range(int(sys.argv[1]))))
          15 +print("mean plan", np.mean([a for s,a,b in out]), "mean rot", np.mean([b for s,a,b in out]))
          16 +print("gaps", [(s,a,b) for s,a,b in out if a!=b])
diff --git a/res_fine.json b/res_fine.json
new file mode 100644
index 0000000..604f354
--- /dev/null
+++ b/res_fine.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 2.05, 2.9], [1, 2, true, 20, 0, 0.42, 2.1], [2, 3, true, 20, 0, 5.75, 5.9], [3, 3, true, 22, 0, 3.82, 4.1], [4, 3, true, 21, 0, 2.85, 3.1], [5, 3, true, 24, 0, 6.53, 6.8], [6, 2, true, 20, 0, 2.05, 2.2], [7, 3, true, 22, 0, 8.77, 9.7], [8, 3, true, 21, 0, 6.63, 7.2], [9, 2, true, 22, 0, 4.99, 5.1], [10, 3, true, 22, 0, 9.3, 9.5], [11, 1, true, 19, 0, 1.14, 1.3], [12, 2, true, 23, 0, 3.35, 4.4], [13, 3, true, 24, 0, 8.23, 9.9], [14, 1, true, 29, 0, 1.23, 2.9], [15, 3, true, 22, 0, 7.51, 10.5], [16, 2, true, 21, 0, 1.94, 2.4], [17, 3, true, 21, 0, 10.52, 13.2], [18, 3, true, 22, 0, 4.35, 5.1], [19, 2, true, 24, 0, 2.79, 3.0], [20, 3, true, 27, 0, 4.22, 6.5], [21, 1, true, 20, 0, 2.0, 2.5], [22, 3, true, 23, 0, 4.8, 7.5], [23, 1, true, 18, 0, 1.28, 2.7], [24, 2, true, 19, 0, 2.39, 4.2], [25, 2, true, 20, 0, 2.25, 5.1], [26, 3, true, 22, 0, 4.39, 6.7], [27, 1, true, 21, 0, 0.4, 1.7], [28, 2, true, 22, 0, 1.46, 4.5], [29, 3, true, 22, 0, 1.75, 4.7], [30, 1, true, 20, 0, 0.86, 3.0], [31, 2, true, 25, 0, 0.69, 5.4], [32, 3, true, 20, 0, 1.6, 5.9], [33, 3, true, 23, 0, 1.84, 6.2], [34, 1, true, 20, 0, 0.22, 4.5], [35, 1, true, 18, 0, 0.34, 3.6], [36, 2, true, 20, 0, 0.67, 3.0], [37, 1, true, 18, 0, 0.61, 2.3], [38, 1, true, 20, 0, 0.73, 1.7], [39, 3, true, 23, 0, 0.62, 1.3]]
\ No newline at end of file
diff --git a/res_home.json b/res_home.json
new file mode 100644
index 0000000..e087996
--- /dev/null
+++ b/res_home.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 0.82, 4.2], [1, 2, true, 20, 0, 0.32, 2.3], [2, 3, true, 20, 0, 1.38, 4.3], [3, 3, true, 22, 0, 1.01, 4.3], [4, 3, true, 21, 0, 1.04, 4.5], [5, 3, true, 24, 0, 1.17, 5.0], [6, 2, true, 21, 0, 0.7, 6.1], [7, 3, true, 22, 0, 1.45, 7.2], [8, 3, true, 21, 0, 0.71, 6.0], [9, 2, true, 22, 0, 0.7, 5.8], [10, 3, true, 22, 0, 1.25, 5.6], [11, 1, true, 19, 0, 0.13, 3.9], [12, 2, true, 23, 0, 0.58, 5.8], [13, 3, true, 24, 0, 1.24, 6.8], [14, 1, true, 29, 0, 0.25, 6.4], [15, 3, true, 22, 0, 1.34, 6.1], [16, 2, true, 21, 0, 0.36, 4.6], [17, 3, true, 21, 0, 3.07, 8.2], [18, 3, true, 22, 0, 1.41, 7.3], [19, 2, true, 24, 0, 0.73, 5.3], [20, 3, true, 27, 0, 0.92, 8.4], [21, 1, true, 20, 0, 0.16, 5.1], [22, 3, true, 23, 0, 0.88, 6.6], [23, 1, true, 18, 0, 0.14, 4.6], [24, 2, true, 19, 0, 0.38, 5.8], [25, 2, true, 20, 0, 0.4, 5.9], [26, 3, true, 22, 0, 1.08, 6.8], [27, 1, true, 21, 0, 0.06, 5.8], [28, 2, true, 22, 0, 0.34, 7.2], [29, 3, true, 22, 0, 0.35, 6.2], [30, 1, true, 20, 0, 0.16, 6.2], [31, 2, true, 25, 0, 0.21, 9.0], [32, 3, true, 20, 0, 0.38, 7.3], [33, 3, true, 23, 0, 0.95, 9.9], [34, 1, true, 20, 0, 0.18, 8.1], [35, 1, true, 18, 0, 0.14, 7.3], [36, 2, true, 21, 0, 0.27, 10.0], [37, 1, true, 18, 0, 0.24, 8.3], [38, 1, true, 20, 0, 0.36, 8.1], [39, 3, true, 23, 0, 0.39, 8.6], [40, 2, true, 21, 0, 0.55, 9.6], [41, 2, true, 19, 0, 0.47, 9.8], [42, 1, true, 21, 0, 0.29, 8.9], [43, 2, true, 24, 0, 0.73, 9.8], [44, 3, true, 20, 0, 0.79, 8.3], [45, 3, true, 21, 0, 1.02, 10.0], [46, 2, true, 20, 0, 0.26, 7.9], [47, 1, true, 21, 0, 0.15, 7.3], [48, 1, true, 19, 0, 0.18, 5.6], [49, 1, true, 22, 0, 0.2, 6.0], [50, 3, true, 22, 0, 1.36, 7.7], [51, 2, true, 21, 0, 0.67, 5.7], [52, 3, true, 22, 0, 1.1, 7.6], [53, 3, true, 21, 0, 1.29, 7.6], [54, 1, true, 20, 0, 0.17, 6.3], [55, 3, true, 27, 0, 1.08, 9.4], [56, 2, true, 23, 0, 0.5, 7.2], [57, 1, true, 18, 0, 0.12, 5.8], [58, 2, true, 24, 0, 0.45, 7.4], [59, 3, true, 22, 0, 2.2, 8.0], [60, 1, true, 22, 0, 0.37, 6.8], [61, 2, true, 20, 0, 0.2, 5.2], [62, 2, true, 22, 0, 0.4, 4.9], [63, 2, true, 23, 0, 0.4, 5.4], [64, 2, true, 22, 0, 0.22, 5.2], [65, 1, true, 18, 0, 0.16, 3.3], [66, 3, true, 22, 0, 0.29, 5.8], [67, 3, true, 21, 0, 0.4, 6.1], [68, 2, true, 20, 0, 0.23, 5.8], [69, 1, true, 20, 0, 0.19, 5.6], [70, 2, true, 20, 0, 0.42, 6.2], [71, 3, true, 21, 0, 1.39, 6.8], [72, 3, true, 21, 0, 1.64, 6.0], [73, 3, true, 21, 0, 0.55, 5.2], [74, 1, true, 20, 0, 0.16, 3.9], [75, 2, true, 18, 0, 0.31, 3.4], [76, 2, true, 23, 0, 0.49, 5.5], [77, 1, true, 20, 0, 0.17, 4.9], [78, 3, true, 22, 0, 0.55, 5.5], [79, 1, true, 23, 0, 0.32, 5.1], [80, 3, true, 21, 0, 0.96, 5.7], [81, 1, true, 20, 0, 0.16, 4.4], [82, 3, true, 20, 0, 0.8, 5.7], [83, 3, true, 22, 0, 0.73, 5.7], [84, 2, true, 23, 0, 0.67, 5.8], [85, 3, true, 20, 0, 1.79, 7.0], [86, 3, true, 21, 0, 0.81, 6.6], [87, 2, true, 23, 0, 0.29, 6.3], [88, 2, true, 20, 0, 0.4, 5.6], [89, 3, true, 29, 0, 0.34, 7.6], [90, 2, true, 21, 0, 0.57, 6.2], [91, 3, true, 23, 0, 0.56, 6.6], [92, 2, true, 23, 0, 0.26, 6.4], [93, 3, true, 23, 0, 0.99, 6.8], [94, 1, true, 20, 0, 0.1, 4.6], [95, 2, true, 21, 0, 0.26, 5.1], [96, 3, true, 21, 0, 0.24, 5.1], [97, 1, true, 29, 0, 0.24, 6.0], [98, 2, true, 23, 0, 0.33, 4.8], [99, 3, true, 23, 0, 0.35, 5.7], [100, 3, true, 24, 0, 0.3, 5.9], [101, 1, true, 18, 0, 0.08, 3.8], [102, 2, true, 22, 0, 0.32, 5.8], [103, 2, true, 22, 0, 0.42, 6.6], [104, 3, true, 21, 0, 1.0, 6.5], [105, 1, true, 20, 0, 0.07, 5.7], [106, 2, true, 20, 0, 0.34, 6.1], [107, 1, true, 21, 0, 0.18, 6.1], [108, 1, true, 18, 0, 0.17, 4.8], [109, 2, true, 20, 0, 0.26, 5.5], [110, 2, true, 20, 0, 0.45, 6.8], [111, 2, true, 20, 0, 0.07, 5.5], [112, 1, true, 18, 0, 0.17, 5.4], [113, 1, true, 19, 0, 0.06, 5.4], [114, 1, true, 20, 0, 0.13, 5.0], [115, 2, true, 21, 0, 0.2, 3.8], [116, 1, true, 21, 0, 0.06, 3.1], [117, 1, true, 25, 0, 0.14, 2.8], [118, 2, true, 21, 0, 0.11, 2.0], [119, 2, true, 20, 0, 0.45, 1.1]]
\ No newline at end of file
diff --git a/test_alt.py b/test_alt.py
new file mode 100644
index 0000000..7a31220
--- /dev/null
+++ b/test_alt.py
@@ -0,0 +1,27 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +import os; exec("from " + os.environ.get("APPROACH","approach") + " import GeneratedApproach")
           5 +def run(seed, verbose=False):
           6 +    env = make_env()
           7 +    obs, info = env.reset(seed=seed)
           8 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
           9 +    t0=time.time(); ap.reset(obs, info); tp=time.time()-t0
          10 +    steps=0; term=False
          11 +    while steps < env.max_steps:
          12 +        a = ap.get_action(obs)
          13 +        obs, r, term, trunc, info = env.step(a)
          14 +        steps += 1
          15 +        if term or trunc: break
          16 +    tt=time.time()-t0
          17 +    env.close()
          18 +    return seed, info.get('object_count') if isinstance(info,dict) else None, term, steps, ap.replans, round(tp,2), round(tt,1)
          19 +if __name__ == "__main__":
          20 +    seeds = range(int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv)>2 else range(10)
          21 +    from concurrent.futures import ThreadPoolExecutor
          22 +    with ThreadPoolExecutor(8) as ex:
          23 +        res = list(ex.map(run, seeds))
          24 +    import json; json.dump(res, open(sys.argv[3] if len(sys.argv)>3 else "last_res.json","w"))
          25 +    for r in res: print(r)
          26 +    ok=[r for r in res if r[2]]
          27 +    print("solved", len(ok), "/", len(res), "mean steps", np.mean([r[3] for r in ok]) if ok else None)
```

</details>

<a id="C018"></a>
### C018 · conservative lander footprint; blacklist rejected move targets

Commit `99376f5189e0272ec67bcb6d3c5bfac0c54d5ca7`; parents: 31341536d0862beb79d5692ae9fb9f4319731314. Recorded author date: 2026-10-01T11:45:06+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0988](01_timeline.md#E0988): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_99376f5_approach.py) · [Exact all-file diff](evidence/diffs/C018_99376f5.diff)

[Previous saved controller snapshot](evidence/versions/C017_3134153_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 32bb7d0..9511a9f 100644
--- a/approach.py
+++ b/approach.py
@@ -16,8 +16,8 @@ WALL_IN = 0.2271 + 0.004
   16     16  ARENA = 2.2729 - 0.004
   17     17  PILLAR_R = 0.245
   18     18  MOUND_R = 0.185
   19        -LANDER_XMIN = -1.195
   20        -LANDER_YMIN = -1.455
          19 +LANDER_XMIN = -1.15
          20 +LANDER_YMIN = -1.42
   21     21  OBJ_RANGE = 1.985
   22     22  LANDER_RANGE = 3.985
   23     23  SAMPLE_R = 0.242
@@ -139,7 +139,7 @@ class Scene:
  139    139  class RoverPlanner:
  140    140      """Grid + regions for one rover."""
  141    141  
  142        -    def __init__(self, idx, home, scene, other_pos_list, cur_th=None):
         142 +    def __init__(self, idx, home, scene, other_pos_list, cur_th=None, bad=()):
  143    143          self.idx = idx
  144    144          self.home = home  # (x, y, th)
  145    145          hx, hy, th = home
@@ -162,6 +162,8 @@ class RoverPlanner:
  162    162          for (cx, cy, ax, ay) in scene.mounds:
  163    163              free &= box_dist(X, Y, cx, cy, ax, ay) > MOUND_R
  164    164          free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
         165 +        for (bx, by) in bad:
         166 +            free &= np.hypot(X - bx, Y - by) > 0.03
  165    167          free[self.hi, self.hj] = True
  166    168          self.free = free
  167    169          self.home_reg = (np.hypot(X - hx, Y - hy) <= HOME_R) & free
@@ -286,6 +288,7 @@ class GeneratedApproach:
  286    288          self.expect = [None, None]
  287    289          self.prev_sc = sc
  288    290          self.log = []
         291 +        self.bad = [[], []]
  289    292          self._plan(state)
  290    293  
  291    294      # ------------------------------------------------------------------
@@ -297,7 +300,7 @@ class GeneratedApproach:
  297    300          occl = [(ohome[0], ohome[1])]
  298    301          if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
  299    302              occl.append((other["x"], other["y"]))
  300        -        P = RoverPlanner(ri, self.homes[name], sc, occl, r["th"])
         303 +        P = RoverPlanner(ri, self.homes[name], sc, occl, r["th"], self.bad[ri])
  301    304          self_planner = P
  302    305          start = P.cell_of(r["x"], r["y"])
  303    306          P.free[start] = True
@@ -603,6 +606,7 @@ class GeneratedApproach:
  603    606                      abs(float(_wrap(r["th"] - e[3]))) > 1e-3:
  604    607                  dev = True
  605    608                  self.log.append(("move", ri, e, r["x"], r["y"]))
         609 +                self.bad[ri].append((e[0], e[1]))
  606    610              op, arg = e[2] if e[2] else (None, None)
  607    611              pr = self.prev_sc.rovers["rover%d" % ri]
  608    612              if op == "img":
diff --git a/prof.out b/prof.out
new file mode 100644
index 0000000..cd1aa12
Binary files /dev/null and b/prof.out differ
diff --git a/res_rot.json b/res_rot.json
new file mode 100644
index 0000000..521b3bc
--- /dev/null
+++ b/res_rot.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 1.51, 4.1], [1, 2, true, 18, 0, 2.08, 3.6], [2, 3, true, 19, 0, 2.39, 4.0], [3, 3, true, 21, 0, 2.8, 5.5], [4, 3, true, 20, 0, 0.78, 3.9], [5, 3, true, 23, 0, 6.86, 7.3], [6, 2, true, 19, 0, 4.94, 5.1], [7, 3, true, 22, 0, 8.4, 10.0], [8, 3, true, 20, 0, 6.7, 7.4], [9, 2, true, 22, 0, 5.64, 6.4], [10, 3, true, 21, 0, 9.62, 10.2], [11, 1, true, 19, 0, 2.66, 2.8], [12, 2, true, 22, 0, 4.64, 6.0], [13, 3, true, 24, 0, 8.35, 8.9], [14, 1, true, 29, 0, 2.05, 3.6], [15, 3, true, 24, 0, 8.94, 12.0], [16, 2, true, 22, 0, 2.7, 4.2], [17, 3, true, 20, 0, 12.15, 15.6], [18, 3, true, 22, 0, 5.72, 5.9], [19, 2, true, 25, 0, 4.41, 5.7], [20, 3, true, 27, 0, 5.53, 8.9], [21, 1, true, 19, 0, 3.92, 5.8], [22, 3, true, 21, 0, 6.34, 8.6], [23, 1, true, 17, 0, 3.42, 6.0], [24, 2, true, 18, 0, 2.46, 5.1], [25, 2, true, 18, 0, 2.97, 5.5], [26, 3, true, 21, 0, 4.29, 7.2], [27, 1, true, 21, 0, 1.35, 4.5], [28, 2, true, 21, 0, 1.94, 4.8], [29, 3, true, 20, 0, 2.32, 6.7], [30, 1, true, 20, 0, 1.04, 5.7], [31, 2, true, 25, 0, 0.64, 5.1], [32, 3, true, 18, 0, 0.68, 5.6], [33, 3, true, 22, 0, 1.06, 7.7], [34, 1, true, 18, 0, 0.57, 5.4], [35, 1, true, 18, 0, 0.41, 5.3], [36, 2, true, 20, 0, 0.47, 6.5], [37, 1, true, 18, 0, 0.5, 5.8], [38, 1, true, 20, 0, 0.54, 5.2], [39, 3, true, 22, 0, 0.72, 5.6], [40, 2, true, 21, 0, 0.81, 5.8], [41, 2, true, 19, 0, 0.42, 6.0], [42, 1, true, 20, 0, 0.39, 5.2], [43, 2, true, 24, 0, 1.25, 7.4], [44, 3, true, 20, 0, 1.45, 5.8], [45, 3, true, 21, 0, 1.48, 5.9], [46, 2, true, 18, 0, 0.41, 3.6], [47, 1, true, 20, 0, 0.36, 4.3], [48, 1, true, 19, 0, 0.35, 4.2], [49, 1, true, 20, 0, 0.51, 4.5], [50, 3, true, 21, 0, 1.42, 5.7], [51, 2, true, 20, 0, 1.04, 4.8], [52, 3, true, 22, 0, 1.45, 4.8], [53, 3, true, 19, 0, 3.09, 6.0], [54, 1, true, 19, 0, 1.55, 3.3], [55, 3, true, 27, 0, 8.28, 10.2], [56, 2, true, 23, 0, 3.06, 6.0], [57, 1, true, 16, 0, 2.11, 4.4], [58, 2, true, 23, 0, 3.87, 5.5], [59, 3, false, 1000, 983, 9.5, 78.7], [60, 1, true, 22, 0, 3.06, 4.6], [61, 2, true, 20, 0, 3.58, 4.2], [62, 2, true, 22, 0, 4.64, 5.4], [63, 2, true, 22, 0, 5.94, 6.1], [64, 2, true, 22, 0, 5.49, 7.1], [65, 1, true, 17, 0, 4.18, 5.3], [66, 3, true, 21, 0, 4.42, 5.4], [67, 3, true, 21, 0, 5.35, 6.9], [68, 2, true, 19, 0, 3.92, 5.5], [69, 1, true, 20, 0, 2.55, 3.8], [70, 2, true, 20, 0, 4.69, 4.9], [71, 3, false, 1000, 982, 8.83, 68.1], [72, 3, true, 20, 0, 9.8, 9.9], [73, 3, true, 20, 0, 4.66, 4.8], [74, 1, true, 20, 0, 4.17, 4.6], [75, 2, true, 18, 0, 4.82, 4.9], [76, 2, true, 22, 0, 5.62, 6.1], [77, 1, true, 18, 0, 3.32, 3.5], [78, 3, true, 21, 0, 5.08, 5.3], [79, 1, true, 23, 0, 4.62, 5.0], [80, 3, true, 20, 0, 12.84, 13.0], [81, 1, true, 18, 0, 4.85, 5.0], [82, 3, true, 19, 0, 6.73, 6.9], [83, 3, true, 21, 0, 6.36, 6.5], [84, 2, true, 22, 0, 5.84, 6.2], [85, 3, true, 19, 0, 9.64, 10.0], [86, 3, true, 21, 0, 6.34, 7.2], [87, 2, true, 23, 0, 5.51, 7.5], [88, 2, true, 18, 0, 4.56, 5.8], [89, 3, true, 29, 0, 3.28, 4.9], [90, 2, true, 20, 0, 4.2, 4.7], [91, 3, true, 22, 0, 3.46, 3.6], [92, 2, true, 23, 0, 4.12, 4.3], [93, 3, true, 22, 0, 7.77, 7.9], [94, 1, true, 20, 0, 3.86, 4.0], [95, 2, true, 21, 0, 6.26, 6.9], [96, 3, true, 21, 0, 4.55, 4.7], [97, 1, true, 27, 0, 5.47, 6.6], [98, 2, true, 22, 0, 4.26, 4.9], [99, 3, true, 22, 0, 6.09, 6.2], [100, 3, true, 23, 0, 5.72, 5.9], [101, 1, true, 17, 0, 2.29, 2.4], [102, 2, true, 21, 0, 5.4, 6.3], [103, 2, true, 21, 0, 4.41, 4.9], [104, 3, true, 20, 0, 7.19, 7.5], [105, 1, true, 20, 0, 2.46, 2.7], [106, 2, true, 19, 0, 3.46, 4.2], [107, 1, true, 20, 0, 2.94, 3.1], [108, 1, true, 18, 0, 4.06, 4.2], [109, 2, true, 19, 0, 5.79, 7.7], [110, 2, true, 20, 0, 5.98, 8.6], [111, 2, true, 20, 0, 4.65, 6.0], [112, 1, true, 18, 0, 4.19, 4.6], [113, 1, true, 19, 0, 2.88, 3.0], [114, 1, true, 18, 0, 2.98, 6.1], [115, 2, true, 21, 0, 1.23, 3.6], [116, 1, true, 21, 0, 0.93, 2.5], [117, 1, true, 25, 0, 1.67, 1.8], [118, 2, true, 19, 0, 2.61, 2.7], [119, 2, true, 21, 0, 2.57, 2.7]]
\ No newline at end of file
diff --git a/timeit_.py b/timeit_.py
new file mode 100644
index 0000000..919a709
--- /dev/null
+++ b/timeit_.py
@@ -0,0 +1,10 @@
           1 +import sys, time
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +import cProfile, pstats
           5 +env=make_env(); obs,info=env.reset(seed=int(sys.argv[1])); env.close()
           6 +ap=GeneratedApproach(None,None,{})
           7 +t=time.time()
           8 +cProfile.run('ap.reset(obs,info)','prof.out')
           9 +print('time',time.time()-t)
          10 +pstats.Stats('prof.out').sort_stats('cumtime').print_stats(12)
```

</details>

<a id="C019"></a>
### C019 · choose imaging heading per rover/task-set among {-pi/2, home}

Commit `92ea16d950cf7b845b770a5005439861847c91f4`; parents: 99376f5189e0272ec67bcb6d3c5bfac0c54d5ca7. Recorded author date: 2026-10-01T11:47:20+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E1014](01_timeline.md#E1014): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_92ea16d_approach.py) · [Exact all-file diff](evidence/diffs/C019_92ea16d.diff)

[Previous saved controller snapshot](evidence/versions/C018_99376f5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9511a9f..8206150 100644
--- a/approach.py
+++ b/approach.py
@@ -139,7 +139,7 @@ class Scene:
  139    139  class RoverPlanner:
  140    140      """Grid + regions for one rover."""
  141    141  
  142        -    def __init__(self, idx, home, scene, other_pos_list, cur_th=None, bad=()):
         142 +    def __init__(self, idx, home, scene, other_pos_list, cur_th=None, bad=(), img_th=None):
  143    143          self.idx = idx
  144    144          self.home = home  # (x, y, th)
  145    145          hx, hy, th = home
@@ -172,7 +172,7 @@ class RoverPlanner:
  172    172          self.camx = X + c * CAM_OFF[0] - s * CAM_OFF[1]
  173    173          self.camy = Y + s * CAM_OFF[0] + c * CAM_OFF[1]
  174    174          self.scene = scene
  175        -        ith = th if IMG_TH is None else IMG_TH
         175 +        ith = th if img_th is None else img_th
  176    176          self.img_th = ith
  177    177          cur = th if cur_th is None else cur_th
  178    178          self.cur_th = cur
@@ -300,7 +300,20 @@ class GeneratedApproach:
  300    300          occl = [(ohome[0], ohome[1])]
  301    301          if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
  302    302              occl.append((other["x"], other["y"]))
  303        -        P = RoverPlanner(ri, self.homes[name], sc, occl, r["th"], self.bad[ri])
         303 +        merged = {}
         304 +        ths = [IMG_TH, self.homes[name][2]] if IMG_TH is not None else [self.homes[name][2]]
         305 +        for ith in ths:
         306 +            P, table = self._rover_tables_h(ri, sc, need_objs, need_stone, need_soil,
         307 +                                            pending, occl, ith)
         308 +            for k, (c, st) in table.items():
         309 +                if k not in merged or c < merged[k][0]:
         310 +                    merged[k] = (c, st, P)
         311 +        return None, merged
         312 +
         313 +    def _rover_tables_h(self, ri, sc, need_objs, need_stone, need_soil, pending, occl, ith):
         314 +        name = "rover%d" % ri
         315 +        r = sc.rovers[name]
         316 +        P = RoverPlanner(ri, self.homes[name], sc, occl, r["th"], self.bad[ri], ith)
  304    317          self_planner = P
  305    318          start = P.cell_of(r["x"], r["y"])
  306    319          P.free[start] = True
@@ -453,7 +466,7 @@ class GeneratedApproach:
  453    466          actions = [[], []]
  454    467          sc = self.scene
  455    468          for ri in range(2):
  456        -            P = tabs[ri][0]
         469 +            P = costs[ri][2]
  457    470              actions[ri] = self._extract(P, best[1][ri][1])
  458    471          # time-aware re-plan of final send against other rover's trajectory
  459    472          trajs = []
@@ -465,7 +478,7 @@ class GeneratedApproach:
  465    478              stages = best[1][ri][1]
  466    479              if stages[-1][0] != "send":
  467    480                  continue
  468        -            P = tabs[ri][0]
         481 +            P = costs[ri][2]
  469    482              Fprev = stages[-2][3]
  470    483              G0 = op_stage(Fprev, P.land_free)
  471    484              other = trajs[1 - ri]
@@ -491,7 +504,7 @@ class GeneratedApproach:
  491    504                  continue
  492    505              st = stages[:-1] + [("send_t", None, G, F2)]
  493    506              new_actions[ri] = self._extract(P, st)
  494        -        return [self._schedule(tabs[ri][0], new_actions[ri]) for ri in range(2)]
         507 +        return [self._schedule(costs[ri][2], new_actions[ri]) for ri in range(2)]
  495    508  
  496    509      def _schedule(self, P, seq):
  497    510          """Attach headings; append waits so the rover can rotate back home."""
diff --git a/approach_v3.py b/approach_v3.py
new file mode 100644
index 0000000..9511a9f
--- /dev/null
+++ b/approach_v3.py
@@ -0,0 +1,640 @@
           1 +"""Rovers approach: staged grid BFS planner per rover + joint task assignment."""
           2 +import itertools
           3 +import math
           4 +
           5 +import numpy as np
           6 +from scipy.ndimage import minimum_filter
           7 +
           8 +INF = 10 ** 6
           9 +RES = 0.05            # grid resolution
          10 +WIN = 4               # max cells per step per axis (0.2 / RES)
          11 +SEL = {"sample": -0.8333, "cal": -0.5, "img": -0.1667, "noop": 0.1667,
          12 +       "send": 0.5, "drop": 0.8333}
          13 +
          14 +# geometry constants (empirically probed)
          15 +WALL_IN = 0.2271 + 0.004
          16 +ARENA = 2.2729 - 0.004
          17 +PILLAR_R = 0.245
          18 +MOUND_R = 0.185
          19 +LANDER_XMIN = -1.15
          20 +LANDER_YMIN = -1.42
          21 +OBJ_RANGE = 1.985
          22 +LANDER_RANGE = 3.985
          23 +SAMPLE_R = 0.242
          24 +HOME_R = 0.22
          25 +IMG_TH = -math.pi / 2
          26 +PILLAR_INFL_OBJ = 0.015
          27 +PILLAR_INFL_LAND = 0.04
          28 +ROVER_OCC_R = 0.26
          29 +CAM_OFF = (-0.087, -0.0125)
          30 +OBJ_BACK_DEG = 108.0     # if |rel bearing| > this, pillars don't occlude objectives
          31 +LAND_BACK_DEG = 110.0    # same quirk for lander (sending)
          32 +USE_BACK_OBJ = True
          33 +USE_BACK_LAND = True
          34 +
          35 +
          36 +def _wrap(a):
          37 +    return (a + np.pi) % (2 * np.pi) - np.pi
          38 +
          39 +
          40 +def rot_steps(a, b):
          41 +    d = abs(float(_wrap(b - a)))
          42 +    return int(math.ceil(d / 0.4 - 1e-6))
          43 +
          44 +
          45 +def approach_angle(a, b, dmax):
          46 +    d = float(_wrap(b - a))
          47 +    if abs(d) <= dmax:
          48 +        return float(_wrap(b))
          49 +    return float(_wrap(a + math.copysign(dmax, d)))
          50 +
          51 +
          52 +def seg_hits_box(px, py, qx, qy, cx, cy, hx, hy):
          53 +    """Vectorised: does segment p->q (p arrays, q scalar) intersect AABB?"""
          54 +    dx = qx - px
          55 +    dy = qy - py
          56 +    t0 = np.zeros_like(px)
          57 +    t1 = np.ones_like(px)
          58 +    ok = np.ones(px.shape, dtype=bool)
          59 +    for d, p, lo, hi in ((dx, px, cx - hx, cx + hx), (dy, py, cy - hy, cy + hy)):
          60 +        small = np.abs(d) < 1e-12
          61 +        ok &= ~(small & ((p < lo) | (p > hi)))
          62 +        with np.errstate(divide="ignore", invalid="ignore"):
          63 +            ta = (lo - p) / d
          64 +            tb = (hi - p) / d
          65 +        tmin = np.where(small, -np.inf, np.minimum(ta, tb))
          66 +        tmax = np.where(small, np.inf, np.maximum(ta, tb))
          67 +        t0 = np.maximum(t0, tmin)
          68 +        t1 = np.minimum(t1, tmax)
          69 +    return ok & (t0 <= t1)
          70 +
          71 +
          72 +def seg_hits_disk(px, py, qx, qy, cx, cy, r):
          73 +    dx = qx - px
          74 +    dy = qy - py
          75 +    L2 = dx * dx + dy * dy + 1e-12
          76 +    t = np.clip(((cx - px) * dx + (cy - py) * dy) / L2, 0, 1)
          77 +    ex = px + t * dx - cx
          78 +    ey = py + t * dy - cy
          79 +    return ex * ex + ey * ey < r * r
          80 +
          81 +
          82 +def box_dist(px, py, cx, cy, hx, hy):
          83 +    ddx = np.maximum(np.abs(px - cx) - hx, 0)
          84 +    ddy = np.maximum(np.abs(py - cy) - hy, 0)
          85 +    return np.hypot(ddx, ddy)
          86 +
          87 +
          88 +def propagate(f, free):
          89 +    f = np.where(free, f, INF)
          90 +    while True:
          91 +        m = minimum_filter(f, size=2 * WIN + 1, mode="constant", cval=INF) + 1
          92 +        nf = np.where(free, np.minimum(f, m), INF)
          93 +        if np.array_equal(nf, f):
          94 +            return f
          95 +        f = nf
          96 +
          97 +
          98 +def op_stage(fprev, region):
          99 +    m = minimum_filter(fprev, size=2 * WIN + 1, mode="constant", cval=INF) + 1
         100 +    return np.where(region, np.minimum(m, INF), INF)
         101 +
         102 +
         103 +class Scene:
         104 +    def __init__(self, state):
         105 +        self.rovers = {}
         106 +        self.objectives = []
         107 +        self.samples = []
         108 +        self.pillars = []
         109 +        self.mounds = []
         110 +        self.lander = (-1.9, -2.0)
         111 +        for o in state:
         112 +            t = o.type.name
         113 +            g = lambda f: state.get(o, f)
         114 +            if t == "rover":
         115 +                self.rovers[o.name] = dict(x=g("x"), y=g("y"), th=g("theta"),
         116 +                                           full=g("store_full") > 0.5,
         117 +                                           cal=g("calibrated") > 0.5)
         118 +            elif t == "lander":
         119 +                self.lander = (g("x"), g("y"))
         120 +            elif t == "objective":
         121 +                self.objectives.append(dict(name=o.name, x=g("x"), y=g("y"),
         122 +                                            img=(g("have_image_rover0") > 0.5,
         123 +                                                 g("have_image_rover1") > 0.5),
         124 +                                            recv=g("received_image") > 0.5))
         125 +            elif t == "sample":
         126 +                self.samples.append(dict(name=o.name, x=g("x"), y=g("y"),
         127 +                                         soil=g("is_soil") > 0.5,
         128 +                                         an=(g("analyzed_rover0") > 0.5,
         129 +                                             g("analyzed_rover1") > 0.5),
         130 +                                         recv=g("received_analysis") > 0.5))
         131 +            elif t == "obstacle":
         132 +                d = (g("x"), g("y"), g("half_x"), g("half_y"))
         133 +                if g("half_x") > 0.15:
         134 +                    self.mounds.append(d)
         135 +                else:
         136 +                    self.pillars.append(d)
         137 +
         138 +
         139 +class RoverPlanner:
         140 +    """Grid + regions for one rover."""
         141 +
         142 +    def __init__(self, idx, home, scene, other_pos_list, cur_th=None, bad=()):
         143 +        self.idx = idx
         144 +        self.home = home  # (x, y, th)
         145 +        hx, hy, th = home
         146 +        self.th = th
         147 +        side = 1 if hx > 0 else -1
         148 +        lo_x, hi_x = (WALL_IN, ARENA) if side > 0 else (-ARENA, -WALL_IN)
         149 +        i0 = math.ceil((lo_x - hx) / RES - 1e-9)
         150 +        i1 = math.floor((hi_x - hx) / RES + 1e-9)
         151 +        j0 = math.ceil((-ARENA - hy) / RES - 1e-9)
         152 +        j1 = math.floor((ARENA - hy) / RES + 1e-9)
         153 +        self.xs = hx + RES * np.arange(i0, i1 + 1)
         154 +        self.ys = hy + RES * np.arange(j0, j1 + 1)
         155 +        self.hi = -i0
         156 +        self.hj = -j0
         157 +        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
         158 +        self.X, self.Y = X, Y
         159 +        free = np.ones(X.shape, dtype=bool)
         160 +        for (cx, cy, ax, ay) in scene.pillars:
         161 +            free &= box_dist(X, Y, cx, cy, ax, ay) > PILLAR_R
         162 +        for (cx, cy, ax, ay) in scene.mounds:
         163 +            free &= box_dist(X, Y, cx, cy, ax, ay) > MOUND_R
         164 +        free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
         165 +        for (bx, by) in bad:
         166 +            free &= np.hypot(X - bx, Y - by) > 0.03
         167 +        free[self.hi, self.hj] = True
         168 +        self.free = free
         169 +        self.home_reg = (np.hypot(X - hx, Y - hy) <= HOME_R) & free
         170 +        self.home_reg[self.hi, self.hj] = True
         171 +        c, s = math.cos(th), math.sin(th)
         172 +        self.camx = X + c * CAM_OFF[0] - s * CAM_OFF[1]
         173 +        self.camy = Y + s * CAM_OFF[0] + c * CAM_OFF[1]
         174 +        self.scene = scene
         175 +        ith = th if IMG_TH is None else IMG_TH
         176 +        self.img_th = ith
         177 +        cur = th if cur_th is None else cur_th
         178 +        self.cur_th = cur
         179 +        self.nrot_in = rot_steps(cur, ith)
         180 +        self.nrot_out = rot_steps(ith, th)
         181 +        hs = [cur, ith, th]
         182 +        for k in range(1, 9):
         183 +            hs.append(approach_angle(cur, ith, 0.4 * k))
         184 +            hs.append(approach_angle(ith, th, 0.4 * k))
         185 +            hs.append(approach_angle(cur, th, 0.4 * k))
         186 +        self.headings = hs
         187 +        ci, si = math.cos(ith), math.sin(ith)
         188 +        camx_i = X + ci * CAM_OFF[0] - si * CAM_OFF[1]
         189 +        camy_i = Y + si * CAM_OFF[0] + ci * CAM_OFF[1]
         190 +        # objective visibility
         191 +        self.vis = []
         192 +        self.objd = []
         193 +        for ob in scene.objectives:
         194 +            ox, oy = ob["x"], ob["y"]
         195 +            d = np.hypot(ox - camx_i, oy - camy_i)
         196 +            v = (d <= OBJ_RANGE)
         197 +            occ = np.zeros(X.shape, dtype=bool)
         198 +            for (cx, cy, ax, ay) in scene.pillars:
         199 +                e = PILLAR_INFL_OBJ
         200 +                occ |= seg_hits_box(camx_i, camy_i, ox, oy, cx, cy, ax + e, ay + e)
         201 +                occ |= seg_hits_box(X, Y, ox, oy, cx, cy, ax + e, ay + e)
         202 +            if USE_BACK_OBJ:
         203 +                rel = np.abs(_wrap(np.arctan2(oy - Y, ox - X) - ith))
         204 +                back = rel > math.radians(OBJ_BACK_DEG)
         205 +            else:
         206 +                back = np.zeros(X.shape, dtype=bool)
         207 +            occ2 = np.zeros(X.shape, dtype=bool)
         208 +            for (px, py) in other_pos_list:
         209 +                occ2 |= seg_hits_disk(camx_i, camy_i, ox, oy, px, py, ROVER_OCC_R)
         210 +            self.vis.append(v & ((~occ) | back) & ~occ2 & free)
         211 +            self.objd.append(d)
         212 +        self.any_vis = np.zeros(X.shape, dtype=bool)
         213 +        for v in self.vis:
         214 +            self.any_vis |= v
         215 +        # lander visibility (must hold for every heading along the rotation path)
         216 +        lx, ly = scene.lander
         217 +        land = free.copy()
         218 +        land_free = free.copy()
         219 +        for hh in self.headings:
         220 +            ch, sh = math.cos(hh), math.sin(hh)
         221 +            cx_ = X + ch * CAM_OFF[0] - sh * CAM_OFF[1]
         222 +            cy_ = Y + sh * CAM_OFF[0] + ch * CAM_OFF[1]
         223 +            v = (np.hypot(lx - X, ly - Y) <= LANDER_RANGE) & \
         224 +                (np.hypot(lx - cx_, ly - cy_) <= LANDER_RANGE)
         225 +            occ = np.zeros(X.shape, dtype=bool)
         226 +            for (cx, cy, ax, ay) in scene.pillars:
         227 +                e = PILLAR_INFL_LAND
         228 +                occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
         229 +                occ |= seg_hits_box(cx_, cy_, lx, ly, cx, cy, ax + e, ay + e)
         230 +            if USE_BACK_LAND:
         231 +                rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - hh))
         232 +                back = rel > math.radians(LAND_BACK_DEG)
         233 +            else:
         234 +                back = np.zeros(X.shape, dtype=bool)
         235 +            occ2 = np.zeros(X.shape, dtype=bool)
         236 +            for (px, py) in other_pos_list:
         237 +                occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
         238 +                occ2 |= seg_hits_disk(cx_, cy_, lx, ly, px, py, ROVER_OCC_R)
         239 +            land &= v & ((~occ) | back) & ~occ2
         240 +            land_free &= v & ((~occ) | back)
         241 +        self.land = land
         242 +        self.land_free = land_free
         243 +        self.camx_i, self.camy_i = camx_i, camy_i
         244 +        # samples
         245 +        self.sreg = {}
         246 +        dk = {}
         247 +        for kind in ("stone", "soil"):
         248 +            d = np.full(X.shape, 1e9)
         249 +            for sm in scene.samples:
         250 +                if sm["soil"] == (kind == "soil"):
         251 +                    d = np.minimum(d, np.hypot(sm["x"] - X, sm["y"] - Y))
         252 +            dk[kind] = d
         253 +        for kind, oth in (("stone", "soil"), ("soil", "stone")):
         254 +            r = (dk[kind] <= SAMPLE_R) & ((dk[oth] > 0.26) | (dk[oth] > dk[kind] + 0.03))
         255 +            self.sreg[kind] = r & free
         256 +
         257 +    def cell_of(self, x, y):
         258 +        i = int(round((x - self.xs[0]) / RES))
         259 +        j = int(round((y - self.ys[0]) / RES))
         260 +        i = min(max(i, 0), len(self.xs) - 1)
         261 +        j = min(max(j, 0), len(self.ys) - 1)
         262 +        return i, j
         263 +
         264 +    def img_region(self, k, imaged):
         265 +        """cells where image would photograph objective k given set imaged."""
         266 +        reg = self.vis[k].copy()
         267 +        if not reg.any():
         268 +            return reg
         269 +        dk = self.objd[k]
         270 +        for m in range(len(self.vis)):
         271 +            if m == k or m in imaged:
         272 +                continue
         273 +            reg &= ~((self.objd[m] <= 2.03) & (self.objd[m] < dk + 0.03))
         274 +        return reg
         275 +
         276 +
         277 +class GeneratedApproach:
         278 +    def __init__(self, action_space, observation_space, primitives):
         279 +        self.action_space = action_space
         280 +        self.homes = None
         281 +
         282 +    # ------------------------------------------------------------------
         283 +    def reset(self, state, info):
         284 +        sc = Scene(state)
         285 +        self.homes = {n: (r["x"], r["y"], r["th"]) for n, r in sc.rovers.items()}
         286 +        self.replans = 0
         287 +        self.fail_count = 0
         288 +        self.expect = [None, None]
         289 +        self.prev_sc = sc
         290 +        self.log = []
         291 +        self.bad = [[], []]
         292 +        self._plan(state)
         293 +
         294 +    # ------------------------------------------------------------------
         295 +    def _rover_tables(self, ri, sc, need_objs, need_stone, need_soil, pending):
         296 +        name = "rover%d" % ri
         297 +        r = sc.rovers[name]
         298 +        other = sc.rovers["rover%d" % (1 - ri)]
         299 +        ohome = self.homes["rover%d" % (1 - ri)]
         300 +        occl = [(ohome[0], ohome[1])]
         301 +        if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
         302 +            occl.append((other["x"], other["y"]))
         303 +        P = RoverPlanner(ri, self.homes[name], sc, occl, r["th"], self.bad[ri])
         304 +        self_planner = P
         305 +        start = P.cell_of(r["x"], r["y"])
         306 +        P.free[start] = True
         307 +        f0 = np.full(P.free.shape, INF, dtype=np.int64)
         308 +        f0[start] = 0
         309 +        stages0 = []
         310 +        F = propagate(f0, P.free)
         311 +        stages0.append(("start", None, f0, F))
         312 +        if r["full"]:
         313 +            G = op_stage(F, P.free)
         314 +            F = propagate(G, P.free)
         315 +            stages0.append(("drop", None, G, F))
         316 +        imaged0 = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
         317 +        tasks = []
         318 +        for k in need_objs:
         319 +            if P.vis[k].any():
         320 +                tasks.append(("obj", k))
         321 +        if need_stone and P.sreg["stone"].any():
         322 +            tasks.append(("stone", None))
         323 +        if need_soil and P.sreg["soil"].any():
         324 +            tasks.append(("soil", None))
         325 +        hcell = (P.hi, P.hj)
         326 +        table = {}  # frozenset(task keys) -> (cost, stages)
         327 +
         328 +        def finish(F, stages, done_keys):
         329 +            if not done_keys and not pending:
         330 +                cost = F[P.home_reg].min()
         331 +                st = stages
         332 +            else:
         333 +                G = op_stage(F, P.land)
         334 +                F2 = propagate(G, P.free)
         335 +                cost = F2[P.home_reg].min()
         336 +                st = stages + [("send", None, G, F2)]
         337 +            if cost >= INF:
         338 +                return
         339 +            key = frozenset(done_keys)
         340 +            if key not in table or cost < table[key][0]:
         341 +                table[key] = (int(cost), st)
         342 +
         343 +        def dfs(F, stages, done_keys, imaged, cal):
         344 +            finish(F, stages, done_keys)
         345 +            if F.min() >= INF:
         346 +                return
         347 +            for t in tasks:
         348 +                key = t if t[0] != "obj" else ("obj", t[1])
         349 +                if key in done_keys:
         350 +                    continue
         351 +                if t[0] == "obj":
         352 +                    k = t[1]
         353 +                    st = list(stages)
         354 +                    Fc = F
         355 +                    if not cal:
         356 +                        G = op_stage(F, P.any_vis)
         357 +                        G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
         358 +                        Fc = propagate(G, P.free)
         359 +                        st.append(("cal", None, G, Fc))
         360 +                    reg = P.img_region(k, imaged)
         361 +                    G = op_stage(Fc, reg)
         362 +                    G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
         363 +                    Fi = propagate(G, P.free)
         364 +                    st.append(("img", k, G, Fi))
         365 +                    dfs(Fi, st, done_keys | {key}, imaged | {k}, False)
         366 +                else:
         367 +                    G = op_stage(F, P.sreg[t[0]])
         368 +                    Fs = propagate(G, P.free)
         369 +                    G2 = op_stage(Fs, P.free)
         370 +                    Fd = propagate(G2, P.free)
         371 +                    st = stages + [("sample", t[0], G, Fs), ("drop", None, G2, Fd)]
         372 +                    dfs(Fd, st, done_keys | {key}, imaged, cal)
         373 +
         374 +        dfs(F, stages0, frozenset(), imaged0, r["cal"])
         375 +        return P, table
         376 +
         377 +    def _plan(self, state):
         378 +        sc = Scene(state)
         379 +        self.scene = sc
         380 +        # what is needed
         381 +        need_objs = [k for k, ob in enumerate(sc.objectives)
         382 +                     if not ob["recv"] and not ob["img"][0] and not ob["img"][1]]
         383 +        pending = [False, False]
         384 +        for k, ob in enumerate(sc.objectives):
         385 +            if not ob["recv"]:
         386 +                for ri in range(2):
         387 +                    if ob["img"][ri]:
         388 +                        pending[ri] = True
         389 +        need = {}
         390 +        for kind in ("stone", "soil"):
         391 +            recv = any(s["recv"] for s in sc.samples if s["soil"] == (kind == "soil"))
         392 +            holders = [ri for ri in range(2)
         393 +                       if any(s["an"][ri] for s in sc.samples if s["soil"] == (kind == "soil"))]
         394 +            if recv:
         395 +                need[kind] = False
         396 +            elif holders:
         397 +                need[kind] = False
         398 +                pending[holders[0]] = True
         399 +            else:
         400 +                need[kind] = True
         401 +        tabs = []
         402 +        for ri in range(2):
         403 +            tabs.append(self._rover_tables(ri, sc, need_objs, need["stone"], need["soil"],
         404 +                                           pending[ri]))
         405 +        # joint assignment
         406 +        best = None
         407 +        cands = []
         408 +        n = len(need_objs)
         409 +        stone_opts = [0, 1] if need["stone"] else [None]
         410 +        soil_opts = [0, 1] if need["soil"] else [None]
         411 +        for assign in itertools.product([0, 1], repeat=n):
         412 +            for so in stone_opts:
         413 +                for sl in soil_opts:
         414 +                    sets = [set(), set()]
         415 +                    for k, a in zip(need_objs, assign):
         416 +                        sets[a].add(("obj", k))
         417 +                    if so is not None:
         418 +                        sets[so].add(("stone", None))
         419 +                    if sl is not None:
         420 +                        sets[sl].add(("soil", None))
         421 +                    costs = []
         422 +                    for ri in range(2):
         423 +                        e = tabs[ri][1].get(frozenset(sets[ri]))
         424 +                        costs.append(e)
         425 +                    if costs[0] is None or costs[1] is None:
         426 +                        continue
         427 +                    key = (max(costs[0][0], costs[1][0]), costs[0][0] + costs[1][0])
         428 +                    cands.append((key, costs))
         429 +                    if best is None or key < best[0]:
         430 +                        self.pred = key
         431 +                        best = (key, costs)
         432 +        self.actions = [[], []]
         433 +        if best is None:
         434 +            return
         435 +        cands.sort(key=lambda c: c[0])
         436 +        seen = set()
         437 +        bestreal = None
         438 +        for key, costs in cands:
         439 +            sig = (id(costs[0][1]), id(costs[1][1]))
         440 +            if sig in seen:
         441 +                continue
         442 +            seen.add(sig)
         443 +            if len(seen) > 6 or (bestreal is not None and key[0] >= bestreal[0][0]):
         444 +                break
         445 +            acts = self._realize(sc, tabs, costs)
         446 +            real = (max(len(acts[0]), len(acts[1])), len(acts[0]) + len(acts[1]))
         447 +            if bestreal is None or real < bestreal[0]:
         448 +                bestreal = (real, acts)
         449 +        self.actions = bestreal[1]
         450 +
         451 +    def _realize(self, sc, tabs, costs):
         452 +        best = (None, costs)
         453 +        actions = [[], []]
         454 +        sc = self.scene
         455 +        for ri in range(2):
         456 +            P = tabs[ri][0]
         457 +            actions[ri] = self._extract(P, best[1][ri][1])
         458 +        # time-aware re-plan of final send against other rover's trajectory
         459 +        trajs = []
         460 +        for ri in range(2):
         461 +            r = sc.rovers["rover%d" % ri]
         462 +            trajs.append([(r["x"], r["y"])] + [(a[0], a[1]) for a in actions[ri]])
         463 +        new_actions = list(actions)
         464 +        for ri in range(2):
         465 +            stages = best[1][ri][1]
         466 +            if stages[-1][0] != "send":
         467 +                continue
         468 +            P = tabs[ri][0]
         469 +            Fprev = stages[-2][3]
         470 +            G0 = op_stage(Fprev, P.land_free)
         471 +            other = trajs[1 - ri]
         472 +            G = np.full(G0.shape, INF, dtype=G0.dtype)
         473 +            pending_mask = G0 < INF
         474 +            tmin = int(G0[pending_mask].min()) if pending_mask.any() else INF
         475 +            lx, ly = sc.lander
         476 +            t = tmin
         477 +            while pending_mask.any() and t < tmin + 200:
         478 +                blk = np.zeros(P.X.shape, dtype=bool)
         479 +                for tt in (t - 1, t):
         480 +                    ox, oy = other[max(0, min(tt, len(other) - 1))]
         481 +                    blk |= seg_hits_disk(P.camx, P.camy, lx, ly, ox, oy, ROVER_OCC_R)
         482 +                    blk |= seg_hits_disk(P.camx_i, P.camy_i, lx, ly, ox, oy, ROVER_OCC_R)
         483 +                ok = pending_mask & (G0 <= t) & ~blk
         484 +                G[ok] = t
         485 +                pending_mask &= ~ok
         486 +                if t >= len(other) - 1 and not ok.any() and (G0 <= t).all():
         487 +                    break
         488 +                t += 1
         489 +            F2 = propagate(G, P.free)
         490 +            if F2[P.home_reg].min() >= INF:
         491 +                continue
         492 +            st = stages[:-1] + [("send_t", None, G, F2)]
         493 +            new_actions[ri] = self._extract(P, st)
         494 +        return [self._schedule(tabs[ri][0], new_actions[ri]) for ri in range(2)]
         495 +
         496 +    def _schedule(self, P, seq):
         497 +        """Attach headings; append waits so the rover can rotate back home."""
         498 +        home_th = P.th
         499 +        t_img = [t for t, a in enumerate(seq, 1) if a[2] and a[2][0] in ("cal", "img")]
         500 +        seq = list(seq)
         501 +        out = []
         502 +        if t_img:
         503 +            last = max(t_img)
         504 +            while len(seq) < last + P.nrot_out:
         505 +                x, y = (seq[-1][0], seq[-1][1])
         506 +                seq.append((x, y, None))
         507 +            T = len(seq)
         508 +            for t, (x, y, op) in enumerate(seq, 1):
         509 +                if t <= T - P.nrot_out:
         510 +                    h = approach_angle(P.cur_th, P.img_th, 0.4 * t)
         511 +                else:
         512 +                    h = approach_angle(P.img_th, home_th, 0.4 * (t - (T - P.nrot_out)))
         513 +                out.append((x, y, op, h))
         514 +        else:
         515 +            while len(seq) < rot_steps(P.cur_th, home_th):
         516 +                x, y = (seq[-1][0], seq[-1][1]) if seq else (float(P.xs[P.hi]), float(P.ys[P.hj]))
         517 +                seq.append((x, y, None))
         518 +            for t, (x, y, op) in enumerate(seq, 1):
         519 +                out.append((x, y, op, approach_angle(P.cur_th, home_th, 0.4 * t)))
         520 +        return out
         521 +
         522 +    def _extract(self, P, stages):
         523 +        """Backtrack through stage fields (waiting allowed); list of (x,y,op)."""
         524 +        k = len(stages) - 1
         525 +        Ff = np.where(P.home_reg, stages[k][3], INF)
         526 +        cell = np.unravel_index(int(np.argmin(Ff)), Ff.shape)
         527 +        cell = (int(cell[0]), int(cell[1]))
         528 +        v = int(stages[k][3][cell])
         529 +        seq = []
         530 +        W = WIN
         531 +        nx, ny = P.free.shape
         532 +
         533 +        def nb(Fsrc, i, j, cond):
         534 +            best = None
         535 +            for di in range(-W, W + 1):
         536 +                for dj in range(-W, W + 1):
         537 +                    a, b = i + di, j + dj
         538 +                    if 0 <= a < nx and 0 <= b < ny and cond(Fsrc[a, b]):
         539 +                        c = abs(di) + abs(dj)
         540 +                        if best is None or c < best[1]:
         541 +                            best = ((a, b), c)
         542 +            return best[0] if best else None
         543 +
         544 +        guard = 0
         545 +        while not (k == 0 and v == 0) and guard < 5000:
         546 +            guard += 1
         547 +            name, arg, G, F = stages[k]
         548 +            i, j = cell
         549 +            timed = name == "send_t"
         550 +            choice = None
         551 +            for mode in (0, 1):
         552 +                if k > 0:
         553 +                    okop = (G[cell] == v) if (mode == 0 or timed) else (G[cell] <= v)
         554 +                    if okop:
         555 +                        Fp = stages[k - 1][3]
         556 +                        c = nb(Fp, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
         557 +                        if c is not None:
         558 +                            choice = (c, (name.replace("_t", ""), arg), k - 1)
         559 +                            break
         560 +                c = nb(F, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
         561 +                if c is not None:
         562 +                    choice = (c, None, k)
         563 +                    break
         564 +            if choice is None:
         565 +                break
         566 +            seq.append((float(P.xs[cell[0]]), float(P.ys[cell[1]]), choice[1]))
         567 +            cell, k = choice[0], choice[2]
         568 +            v -= 1
         569 +        seq.reverse()
         570 +        return seq
         571 +
         572 +    # ------------------------------------------------------------------
         573 +    def get_action(self, state):
         574 +        act = np.zeros(8, dtype=np.float32)
         575 +        sc = Scene(state)
         576 +        if self._deviated(sc) or (not self.actions[0] and not self.actions[1]):
         577 +            self.replans += 1
         578 +            if self.replans < 40:
         579 +                self._plan(state)
         580 +        for ri in range(2):
         581 +            r = sc.rovers["rover%d" % ri]
         582 +            if self.actions[ri]:
         583 +                x, y, op, h = self.actions[ri].pop(0)
         584 +                dx = float(np.clip(x - r["x"], -0.2, 0.2))
         585 +                dy = float(np.clip(y - r["y"], -0.2, 0.2))
         586 +                act[4 * ri] = dx
         587 +                act[4 * ri + 1] = dy
         588 +                act[4 * ri + 3] = SEL[op[0]] if op else 0.0
         589 +                act[4 * ri + 2] = float(np.clip(_wrap(h - r["th"]), -0.4, 0.4))
         590 +                self.expect[ri] = (x, y, op, h)
         591 +            else:
         592 +                # at end: if at home do nothing
         593 +                self.expect[ri] = None
         594 +        return act
         595 +
         596 +    def _deviated(self, sc):
         597 +        dev = False
         598 +        for ri in range(2):
         599 +            e = self.expect[ri]
         600 +            if e is None:
         601 +                continue
         602 +            d0 = dev
         603 +            dev = False
         604 +            r = sc.rovers["rover%d" % ri]
         605 +            if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3 or \
         606 +                    abs(float(_wrap(r["th"] - e[3]))) > 1e-3:
         607 +                dev = True
         608 +                self.log.append(("move", ri, e, r["x"], r["y"]))
         609 +                self.bad[ri].append((e[0], e[1]))
         610 +            op, arg = e[2] if e[2] else (None, None)
         611 +            pr = self.prev_sc.rovers["rover%d" % ri]
         612 +            if op == "img":
         613 +                ob = sc.objectives[arg]
         614 +                if not ob["img"][ri]:
         615 +                    dev = True
         616 +            if op == "sample":
         617 +                if not any(s["an"][ri] for s in sc.samples if s["soil"] == (arg == "soil")):
         618 +                    dev = True
         619 +            if op == "cal" and not r["cal"]:
         620 +                dev = True
         621 +            elif op == "img" and (r["cal"] or not pr["cal"]):
         622 +                dev = True
         623 +            elif op == "sample" and not r["full"]:
         624 +                dev = True
         625 +            elif op == "drop" and r["full"]:
         626 +                dev = True
         627 +            elif op == "send":
         628 +                for ob in sc.objectives:
         629 +                    if ob["img"][ri] and not ob["recv"]:
         630 +                        dev = True
         631 +                for s in sc.samples:
         632 +                    if s["an"][ri] and not s["recv"]:
         633 +                        dev = True
         634 +            if dev:
         635 +                self.log.append(("dev", ri, e, round(r["x"], 3), round(r["y"], 3), r["cal"], pr["cal"],
         636 +                                 [ob["img"][ri] for ob in sc.objectives]))
         637 +            dev = dev or d0
         638 +        self.prev_sc = sc
         639 +        self.expect = [None, None]
         640 +        return dev
diff --git a/big_v3.log b/big_v3.log
new file mode 100644
index 0000000..e69de29
diff --git a/res_rot2.json b/res_rot2.json
new file mode 100644
index 0000000..741faeb
--- /dev/null
+++ b/res_rot2.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 1.7, 3.8], [1, 2, true, 18, 0, 2.55, 3.7], [2, 3, true, 19, 0, 7.7, 8.8], [3, 3, true, 21, 0, 4.71, 5.4], [4, 3, true, 20, 0, 4.23, 5.5], [5, 3, true, 23, 0, 2.07, 3.7], [6, 2, true, 19, 0, 5.76, 5.9], [7, 3, true, 22, 0, 9.7, 10.7], [8, 3, true, 20, 0, 6.89, 7.6], [9, 2, true, 22, 0, 5.72, 7.1], [10, 3, true, 21, 0, 10.68, 11.8], [11, 1, true, 19, 0, 2.72, 3.0], [12, 2, true, 22, 0, 4.7, 6.1], [13, 3, true, 24, 0, 9.17, 9.5], [14, 1, true, 29, 0, 2.49, 3.4], [15, 3, true, 24, 0, 9.12, 9.5], [16, 2, true, 22, 0, 3.62, 3.8], [17, 3, true, 22, 0, 12.05, 15.4], [18, 3, true, 22, 0, 6.45, 8.0], [19, 2, true, 25, 0, 5.1, 6.6], [20, 3, true, 27, 0, 6.44, 10.4], [21, 1, true, 19, 0, 3.73, 6.2], [22, 3, true, 21, 0, 5.64, 9.0], [23, 1, true, 17, 0, 2.71, 4.8], [24, 2, true, 18, 0, 1.93, 4.4], [25, 2, true, 18, 0, 2.79, 5.9], [26, 3, true, 21, 0, 4.73, 9.2], [27, 1, true, 21, 0, 1.38, 5.0], [28, 2, true, 21, 0, 2.07, 5.6], [29, 3, true, 20, 0, 2.09, 5.3], [30, 1, true, 20, 0, 1.21, 5.1], [31, 2, true, 25, 0, 0.47, 6.7], [32, 3, true, 18, 0, 0.59, 5.2], [33, 3, true, 22, 0, 0.74, 6.7], [34, 1, true, 18, 0, 0.29, 5.2], [35, 1, true, 18, 0, 0.39, 6.3], [36, 2, true, 20, 0, 0.46, 6.3], [37, 1, true, 18, 0, 0.53, 5.4], [38, 1, true, 20, 0, 0.45, 4.7], [39, 3, true, 22, 0, 0.59, 6.1], [40, 2, true, 21, 0, 0.68, 4.6], [41, 2, true, 19, 0, 0.67, 3.6], [42, 1, true, 20, 0, 0.36, 4.0], [43, 2, true, 24, 0, 0.63, 6.0], [44, 3, true, 20, 0, 1.35, 6.1], [45, 3, true, 21, 0, 1.73, 6.7], [46, 2, true, 18, 0, 0.98, 4.6], [47, 1, true, 20, 0, 0.38, 3.7], [48, 1, true, 19, 0, 0.32, 3.5], [49, 1, true, 20, 0, 0.48, 3.0], [50, 3, true, 21, 0, 1.27, 5.7], [51, 2, true, 20, 0, 0.45, 4.5], [52, 3, true, 22, 0, 0.81, 5.3], [53, 3, true, 19, 0, 2.37, 5.5], [54, 1, true, 19, 0, 1.31, 4.6], [55, 3, true, 27, 0, 4.41, 7.9], [56, 2, true, 23, 0, 2.06, 5.5], [57, 1, true, 16, 0, 1.87, 4.1], [58, 2, true, 23, 0, 2.75, 4.9], [59, 3, true, 20, 0, 6.86, 7.3], [60, 1, true, 22, 0, 2.31, 4.0], [61, 2, true, 20, 0, 3.21, 4.2], [62, 2, true, 22, 0, 3.91, 4.7], [63, 2, true, 21, 0, 4.18, 5.8], [64, 2, true, 21, 0, 3.44, 5.0], [65, 1, true, 17, 0, 2.73, 4.1], [66, 3, true, 21, 0, 2.53, 3.8], [67, 3, true, 21, 0, 3.53, 6.5], [68, 2, true, 19, 0, 2.29, 4.5], [69, 1, true, 20, 0, 1.13, 3.0], [70, 2, true, 20, 0, 1.31, 4.1], [71, 3, true, 20, 0, 2.63, 4.7], [72, 3, true, 20, 0, 3.79, 5.3], [73, 3, true, 20, 0, 2.44, 4.8], [74, 1, true, 20, 0, 1.82, 3.9], [75, 2, true, 18, 0, 1.72, 3.6], [76, 2, true, 22, 0, 2.05, 4.5], [77, 1, true, 18, 0, 1.32, 3.6], [78, 3, true, 21, 0, 2.24, 3.8], [79, 1, true, 23, 0, 1.32, 2.6], [80, 3, true, 20, 0, 4.43, 5.9], [81, 1, true, 18, 0, 1.09, 3.7], [82, 3, true, 19, 0, 2.68, 4.1], [83, 3, true, 21, 0, 3.28, 4.6], [84, 2, true, 22, 0, 4.14, 4.3], [85, 3, true, 19, 0, 7.6, 8.2], [86, 3, true, 21, 0, 4.76, 4.9], [87, 2, true, 23, 0, 4.92, 6.0], [88, 2, true, 18, 0, 4.62, 5.1], [89, 3, true, 29, 0, 3.41, 3.6], [90, 2, true, 20, 0, 4.35, 6.6], [91, 3, true, 22, 0, 3.88, 5.7], [92, 2, true, 23, 0, 3.34, 5.7], [93, 3, true, 22, 0, 5.27, 7.7], [94, 1, true, 20, 0, 2.39, 4.5], [95, 2, true, 21, 0, 2.96, 5.1], [96, 3, true, 21, 0, 2.04, 3.2], [97, 1, true, 27, 0, 2.94, 5.6], [98, 2, true, 22, 0, 2.52, 4.6], [99, 3, true, 22, 0, 3.16, 6.5], [100, 3, true, 23, 0, 2.66, 6.0], [101, 1, true, 17, 0, 1.22, 4.0], [102, 2, true, 21, 0, 1.19, 4.2], [103, 2, true, 21, 0, 0.78, 5.1], [104, 3, true, 20, 0, 1.16, 5.1], [105, 1, true, 20, 0, 0.25, 4.0], [106, 2, true, 19, 0, 0.41, 5.3], [107, 1, true, 20, 0, 0.34, 5.1], [108, 1, true, 18, 0, 0.31, 4.2], [109, 2, true, 19, 0, 0.34, 4.7], [110, 2, true, 20, 0, 0.56, 5.5], [111, 2, true, 20, 0, 0.36, 4.8], [112, 1, true, 18, 0, 0.38, 4.7], [113, 1, true, 19, 0, 0.27, 4.3], [114, 1, true, 18, 0, 0.22, 3.7], [115, 2, true, 21, 0, 0.31, 3.4], [116, 1, true, 21, 0, 0.3, 2.4], [117, 1, true, 25, 0, 0.34, 2.2], [118, 2, true, 19, 0, 0.61, 1.3], [119, 2, true, 21, 0, 0.54, 1.0]]
\ No newline at end of file
```

</details>

<a id="C020"></a>
### C020 · single imaging heading (faster)

Commit `f913fe9defb9d86fb44676fda1ba1f751a8e5f2b`; parents: 92ea16d950cf7b845b770a5005439861847c91f4. Recorded author date: 2026-10-01T11:51:03+02:00.

File roles (automatic): policy, setup/other.

- [E1021](01_timeline.md#E1021): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_f913fe9_approach.py) · [Exact all-file diff](evidence/diffs/C020_f913fe9.diff)

[Previous saved controller snapshot](evidence/versions/C019_92ea16d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8206150..5dcb7ad 100644
--- a/approach.py
+++ b/approach.py
@@ -301,7 +301,7 @@ class GeneratedApproach:
  301    301          if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
  302    302              occl.append((other["x"], other["y"]))
  303    303          merged = {}
  304        -        ths = [IMG_TH, self.homes[name][2]] if IMG_TH is not None else [self.homes[name][2]]
         304 +        ths = [IMG_TH if IMG_TH is not None else self.homes[name][2]]
  305    305          for ith in ths:
  306    306              P, table = self._rover_tables_h(ri, sc, need_objs, need_stone, need_soil,
  307    307                                              pending, occl, ith)
diff --git a/res_rot3.json b/res_rot3.json
new file mode 100644
index 0000000..7bdb4a3
--- /dev/null
+++ b/res_rot3.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 1.46, 8.2], [1, 2, true, 18, 0, 3.23, 7.3], [2, 3, true, 19, 0, 10.97, 16.6], [3, 3, true, 21, 0, 8.16, 13.1], [4, 3, true, 20, 0, 10.5, 15.7], [5, 3, true, 23, 0, 11.3, 18.1], [6, 2, true, 19, 0, 8.07, 12.6], [7, 3, true, 22, 0, 12.28, 19.8], [8, 3, true, 20, 0, 7.0, 13.5], [9, 2, true, 22, 0, 5.44, 12.7], [10, 3, true, 21, 0, 5.19, 11.7], [11, 1, true, 19, 0, 0.54, 5.6], [12, 2, true, 22, 0, 1.88, 7.5], [13, 3, true, 24, 0, 3.66, 9.9], [14, 1, true, 29, 0, 1.23, 8.5], [15, 3, true, 24, 0, 4.23, 10.4], [16, 2, true, 22, 0, 1.96, 6.9], [17, 3, true, 22, 0, 10.23, 16.7], [18, 3, true, 22, 0, 4.38, 10.8], [19, 2, true, 25, 0, 3.08, 11.0], [20, 3, true, 27, 0, 3.59, 11.3], [21, 1, true, 19, 0, 2.18, 8.6], [22, 3, true, 21, 0, 3.52, 9.7], [23, 1, true, 17, 0, 1.51, 6.7], [24, 2, true, 18, 0, 1.14, 6.7], [25, 2, true, 18, 0, 0.92, 5.7], [26, 3, true, 21, 0, 2.16, 8.6], [27, 1, true, 21, 0, 0.6, 7.3], [28, 2, true, 21, 0, 2.37, 8.0], [29, 3, true, 20, 0, 2.54, 8.6], [30, 1, true, 20, 0, 1.26, 7.0], [31, 2, true, 25, 0, 0.84, 8.2], [32, 3, true, 18, 0, 1.06, 6.8], [33, 3, true, 22, 0, 1.49, 9.5], [34, 1, true, 18, 0, 0.74, 7.1], [35, 1, true, 18, 0, 0.75, 6.9], [36, 2, true, 20, 0, 0.87, 6.5], [37, 1, true, 18, 0, 0.64, 5.8], [38, 1, true, 20, 0, 0.61, 5.8], [39, 3, true, 24, 0, 0.91, 7.8], [40, 2, true, 21, 0, 1.03, 6.4], [41, 2, true, 19, 0, 0.92, 5.3], [42, 1, true, 20, 0, 0.5, 6.5], [43, 2, true, 24, 0, 1.03, 8.0], [44, 3, true, 20, 0, 0.78, 7.0], [45, 3, true, 21, 0, 1.63, 7.6], [46, 2, true, 18, 0, 0.43, 5.9], [47, 1, true, 20, 0, 0.75, 5.8], [48, 1, true, 19, 0, 0.61, 5.5], [49, 1, true, 20, 0, 0.82, 5.1], [50, 3, true, 21, 0, 2.17, 6.8], [51, 2, true, 20, 0, 1.95, 7.1], [52, 3, true, 22, 0, 2.64, 8.4], [53, 3, true, 19, 0, 3.28, 8.7], [54, 1, true, 19, 0, 1.36, 6.1], [55, 3, true, 27, 0, 3.03, 9.3], [56, 2, true, 23, 0, 1.91, 7.0], [57, 1, true, 16, 0, 0.59, 3.7], [58, 2, true, 23, 0, 0.65, 5.7], [59, 3, true, 20, 0, 2.16, 6.8], [60, 1, true, 22, 0, 0.55, 6.3], [61, 2, true, 20, 0, 0.48, 5.7], [62, 2, true, 22, 0, 0.74, 6.8], [63, 2, true, 21, 0, 0.71, 6.3], [64, 2, true, 21, 0, 0.46, 5.6], [65, 1, true, 17, 0, 0.49, 4.0], [66, 3, true, 21, 0, 0.51, 6.0], [67, 3, true, 21, 0, 0.79, 5.8], [68, 2, true, 19, 0, 0.55, 5.9], [69, 1, true, 20, 0, 0.4, 5.8], [70, 2, true, 20, 0, 0.66, 6.0], [71, 3, true, 20, 0, 1.5, 7.3], [72, 3, true, 20, 0, 1.59, 7.5], [73, 3, true, 20, 0, 1.53, 8.0], [74, 1, true, 20, 0, 1.1, 7.7], [75, 2, true, 18, 0, 0.77, 5.6], [76, 2, true, 22, 0, 0.72, 5.5], [77, 1, true, 18, 0, 0.57, 4.5], [78, 3, true, 21, 0, 0.87, 5.7], [79, 1, true, 23, 0, 0.59, 5.8], [80, 3, true, 20, 0, 7.73, 13.3], [81, 1, true, 18, 0, 3.89, 7.1], [82, 3, true, 19, 0, 6.57, 10.8], [83, 3, true, 21, 0, 7.57, 13.2], [84, 2, true, 22, 0, 6.89, 13.7], [85, 3, true, 19, 0, 10.07, 15.7], [86, 3, true, 21, 0, 6.04, 13.0], [87, 2, true, 23, 0, 4.42, 11.2], [88, 2, true, 18, 0, 3.39, 8.5], [89, 3, true, 29, 0, 2.22, 9.9], [90, 2, true, 20, 0, 1.55, 7.3], [91, 3, true, 22, 0, 0.89, 6.8], [92, 2, true, 23, 0, 1.38, 7.4], [93, 3, true, 22, 0, 2.22, 8.3], [94, 1, true, 20, 0, 0.64, 6.0], [95, 2, true, 21, 0, 2.02, 8.7], [96, 3, true, 21, 0, 1.91, 8.4], [97, 1, true, 27, 0, 0.55, 9.0], [98, 2, true, 22, 0, 1.8, 8.4], [99, 3, true, 22, 0, 1.87, 8.9], [100, 3, true, 23, 0, 0.89, 6.6], [101, 1, true, 17, 0, 0.49, 4.1], [102, 2, true, 21, 0, 1.05, 6.2], [103, 2, true, 21, 0, 0.47, 5.2], [104, 3, true, 20, 0, 1.71, 7.7], [105, 1, true, 20, 0, 0.43, 6.5], [106, 2, true, 19, 0, 0.91, 6.6], [107, 1, true, 20, 0, 0.66, 7.0], [108, 1, true, 18, 0, 0.73, 5.4], [109, 2, true, 19, 0, 1.02, 6.1], [110, 2, true, 20, 0, 1.38, 7.2], [111, 2, true, 20, 0, 0.83, 6.5], [112, 1, true, 18, 0, 0.78, 5.7], [113, 1, true, 19, 0, 0.46, 5.3], [114, 1, true, 18, 0, 0.72, 5.8], [115, 2, true, 21, 0, 0.6, 6.3], [116, 1, true, 21, 0, 0.51, 6.7], [117, 1, true, 25, 0, 0.49, 7.2], [118, 2, true, 19, 0, 0.49, 5.0], [119, 2, true, 20, 0, 0.91, 5.9]]
\ No newline at end of file
```

</details>

<a id="C021"></a>
### C021 · rotate only 1.2 rad (3 steps) toward -pi/2 for imaging

Commit `c6213beb1f10f8509969c52d6a0e60fbcec75100`; parents: f913fe9defb9d86fb44676fda1ba1f751a8e5f2b. Recorded author date: 2026-10-01T11:51:15+02:00.

File roles (automatic): policy.

- [E1032](01_timeline.md#E1032): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C021_c6213be_approach.py) · [Exact all-file diff](evidence/diffs/C021_c6213be.diff)

[Previous saved controller snapshot](evidence/versions/C020_f913fe9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5dcb7ad..29fdb14 100644
--- a/approach.py
+++ b/approach.py
@@ -23,6 +23,7 @@ LANDER_RANGE = 3.985
   23     23  SAMPLE_R = 0.242
   24     24  HOME_R = 0.22
   25     25  IMG_TH = -math.pi / 2
          26 +ROT_IMG = 1.2
   26     27  PILLAR_INFL_OBJ = 0.015
   27     28  PILLAR_INFL_LAND = 0.04
   28     29  ROVER_OCC_R = 0.26
@@ -301,7 +302,12 @@ class GeneratedApproach:
  301    302          if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
  302    303              occl.append((other["x"], other["y"]))
  303    304          merged = {}
  304        -        ths = [IMG_TH if IMG_TH is not None else self.homes[name][2]]
         305 +        hth = self.homes[name][2]
         306 +        if IMG_TH is None:
         307 +            ths = [hth]
         308 +        else:
         309 +            d = float(_wrap(IMG_TH - hth))
         310 +            ths = [float(_wrap(hth + math.copysign(min(abs(d), ROT_IMG), d)))]
  305    311          for ith in ths:
  306    312              P, table = self._rover_tables_h(ri, sc, need_objs, need_stone, need_soil,
  307    313                                              pending, occl, ith)
```

</details>

<a id="C022"></a>
### C022 · full rotation

Commit `711a3f4a37d23ce2c7c0fea52c64adb5022854c1`; parents: c6213beb1f10f8509969c52d6a0e60fbcec75100. Recorded author date: 2026-10-01T11:53:53+02:00.

File roles (automatic): policy, setup/other.

- [E1041](01_timeline.md#E1041): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C022_711a3f4_approach.py) · [Exact all-file diff](evidence/diffs/C022_711a3f4.diff)

[Previous saved controller snapshot](evidence/versions/C021_c6213be_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 29fdb14..a1e1b94 100644
--- a/approach.py
+++ b/approach.py
@@ -23,7 +23,7 @@ LANDER_RANGE = 3.985
   23     23  SAMPLE_R = 0.242
   24     24  HOME_R = 0.22
   25     25  IMG_TH = -math.pi / 2
   26        -ROT_IMG = 1.2
          26 +ROT_IMG = 4.0
   27     27  PILLAR_INFL_OBJ = 0.015
   28     28  PILLAR_INFL_LAND = 0.04
   29     29  ROVER_OCC_R = 0.26
diff --git a/big_v3.log b/big_v3.log
index e69de29..8b108d2 100644
--- a/big_v3.log
+++ b/big_v3.log
@@ -0,0 +1,281 @@
           1 +(120, 1, True, 18, 0, 0.36, 5.1)
           2 +(121, 1, True, 20, 0, 0.4, 4.8)
           3 +(122, 3, True, 20, 0, 0.63, 5.4)
           4 +(123, 1, True, 21, 0, 0.6, 5.9)
           5 +(124, 3, True, 22, 0, 0.75, 5.5)
           6 +(125, 2, True, 18, 0, 0.52, 4.6)
           7 +(126, 1, True, 18, 0, 0.46, 3.1)
           8 +(127, 2, True, 21, 0, 0.58, 5.8)
           9 +(128, 3, True, 21, 0, 0.74, 5.5)
          10 +(129, 2, True, 21, 0, 1.19, 5.0)
          11 +(130, 3, True, 23, 0, 2.96, 6.7)
          12 +(131, 2, True, 21, 0, 1.7, 5.2)
          13 +(132, 3, True, 24, 0, 7.53, 10.0)
          14 +(133, 2, True, 18, 0, 2.65, 4.9)
          15 +(134, 3, True, 23, 0, 7.99, 9.4)
          16 +(135, 2, True, 18, 0, 4.22, 4.6)
          17 +(136, 3, True, 22, 0, 4.07, 4.4)
          18 +(137, 2, True, 21, 0, 5.15, 6.4)
          19 +(138, 2, True, 22, 0, 4.21, 5.5)
          20 +(139, 2, True, 20, 0, 4.21, 6.1)
          21 +(140, 2, True, 18, 0, 3.69, 7.6)
          22 +(141, 2, True, 18, 0, 2.56, 6.8)
          23 +(142, 1, True, 18, 0, 1.94, 6.7)
          24 +(143, 3, True, 23, 0, 1.62, 7.9)
          25 +(144, 1, True, 19, 0, 0.49, 4.7)
          26 +(145, 2, True, 23, 0, 0.91, 6.8)
          27 +(146, 3, True, 20, 0, 1.02, 5.5)
          28 +(147, 1, True, 17, 0, 0.46, 6.3)
          29 +(148, 1, True, 18, 0, 0.43, 5.7)
          30 +(149, 1, True, 16, 0, 0.26, 4.4)
          31 +(150, 2, True, 20, 0, 0.68, 4.4)
          32 +(151, 3, True, 25, 0, 3.07, 9.3)
          33 +(152, 3, True, 27, 0, 2.58, 8.8)
          34 +(153, 3, True, 22, 0, 2.55, 8.3)
          35 +(154, 1, True, 20, 0, 1.32, 6.2)
          36 +(155, 1, True, 16, 0, 0.95, 5.9)
          37 +(156, 3, True, 20, 0, 1.01, 6.7)
          38 +(157, 1, True, 20, 0, 0.24, 5.0)
          39 +(158, 2, True, 20, 0, 0.43, 6.3)
          40 +(159, 3, True, 20, 0, 0.85, 7.6)
          41 +(160, 1, True, 18, 0, 0.4, 7.2)
          42 +(161, 3, True, 20, 0, 1.44, 7.8)
          43 +(162, 2, True, 27, 0, 0.56, 8.1)
          44 +(163, 2, True, 18, 0, 0.62, 5.9)
          45 +(164, 2, True, 27, 0, 0.37, 7.6)
          46 +(165, 2, True, 19, 0, 0.27, 5.5)
          47 +(166, 3, True, 20, 0, 1.23, 6.7)
          48 +(167, 3, True, 21, 0, 0.92, 6.0)
          49 +(168, 2, True, 20, 0, 0.73, 6.0)
          50 +(169, 3, True, 31, 0, 0.85, 8.0)
          51 +(170, 3, True, 22, 0, 0.72, 6.4)
          52 +(171, 3, True, 21, 0, 0.6, 6.5)
          53 +(172, 2, True, 20, 0, 0.66, 6.2)
          54 +(173, 3, True, 33, 0, 0.71, 10.5)
          55 +(174, 2, True, 20, 0, 0.83, 6.3)
          56 +(175, 3, True, 22, 0, 1.36, 7.3)
          57 +(176, 1, True, 23, 0, 0.37, 7.4)
          58 +(177, 3, True, 21, 0, 1.37, 7.3)
          59 +(178, 2, True, 22, 0, 0.66, 6.4)
          60 +(179, 3, True, 21, 0, 0.64, 6.5)
          61 +(180, 1, True, 19, 0, 0.36, 5.7)
          62 +(181, 3, True, 23, 0, 0.77, 7.8)
          63 +(182, 3, True, 18, 0, 0.94, 6.1)
          64 +(183, 3, True, 22, 0, 1.18, 8.2)
          65 +(184, 2, True, 23, 0, 0.42, 7.4)
          66 +(185, 1, True, 19, 0, 0.36, 5.8)
          67 +(186, 1, True, 37, 0, 0.38, 10.6)
          68 +(187, 2, True, 20, 0, 0.66, 6.7)
          69 +(188, 2, True, 18, 0, 0.59, 6.6)
          70 +(189, 2, True, 29, 0, 0.51, 10.1)
          71 +(190, 1, True, 18, 0, 0.32, 6.3)
          72 +(191, 1, True, 21, 0, 0.95, 8.2)
          73 +(192, 3, True, 22, 0, 1.38, 8.1)
          74 +(193, 2, True, 21, 0, 0.65, 7.2)
          75 +(194, 3, True, 20, 0, 0.94, 7.0)
          76 +(195, 1, True, 18, 0, 0.34, 4.9)
          77 +(196, 1, True, 16, 0, 0.94, 4.6)
          78 +(197, 3, True, 19, 0, 1.11, 5.8)
          79 +(198, 2, True, 21, 0, 0.58, 6.0)
          80 +(199, 2, True, 20, 0, 0.33, 6.1)
          81 +(200, 1, True, 18, 0, 0.35, 5.5)
          82 +(201, 1, True, 21, 0, 0.28, 6.0)
          83 +(202, 1, True, 20, 0, 0.36, 6.4)
          84 +(203, 1, True, 19, 0, 0.26, 5.2)
          85 +(204, 3, True, 20, 0, 0.86, 5.9)
          86 +(205, 2, True, 20, 0, 0.43, 4.8)
          87 +(206, 2, True, 18, 0, 0.59, 4.1)
          88 +(207, 1, True, 19, 0, 0.4, 4.8)
          89 +(208, 3, True, 20, 0, 1.67, 6.6)
          90 +(209, 3, True, 20, 0, 1.29, 6.3)
          91 +(210, 1, True, 19, 0, 0.28, 5.1)
          92 +(211, 1, True, 16, 0, 0.3, 3.8)
          93 +(212, 1, True, 23, 0, 0.22, 5.8)
          94 +(213, 1, True, 18, 0, 0.3, 4.7)
          95 +(214, 1, True, 20, 0, 0.25, 4.5)
          96 +(215, 3, True, 20, 0, 2.56, 7.2)
          97 +(216, 3, True, 21, 0, 3.71, 9.5)
          98 +(217, 3, True, 19, 0, 3.09, 7.5)
          99 +(218, 2, True, 23, 0, 1.41, 7.1)
         100 +(219, 1, True, 27, 0, 0.95, 7.6)
         101 +(220, 3, True, 23, 0, 0.73, 6.7)
         102 +(221, 2, True, 20, 0, 0.45, 5.6)
         103 +(222, 2, True, 18, 0, 0.22, 4.4)
         104 +(223, 2, True, 19, 0, 0.35, 5.4)
         105 +(224, 3, True, 20, 0, 0.56, 5.9)
         106 +(225, 3, True, 20, 0, 0.88, 6.9)
         107 +(226, 3, True, 20, 0, 0.7, 5.7)
         108 +(227, 2, True, 18, 0, 0.45, 4.9)
         109 +(228, 2, True, 18, 0, 0.39, 5.4)
         110 +(229, 2, True, 21, 0, 0.43, 6.5)
         111 +(230, 2, True, 19, 0, 0.49, 6.2)
         112 +(231, 1, True, 24, 0, 0.31, 6.9)
         113 +(232, 2, True, 19, 0, 0.42, 5.7)
         114 +(233, 1, True, 20, 0, 0.22, 5.8)
         115 +(234, 2, True, 21, 0, 0.4, 5.8)
         116 +(235, 3, True, 20, 0, 1.19, 6.0)
         117 +(236, 2, True, 20, 0, 0.43, 4.6)
         118 +(237, 3, True, 23, 0, 0.64, 5.2)
         119 +(238, 2, True, 20, 0, 0.4, 4.0)
         120 +(239, 3, True, 20, 0, 0.57, 4.1)
         121 +(240, 3, True, 20, 0, 0.66, 4.8)
         122 +(241, 2, True, 20, 0, 0.42, 3.8)
         123 +(242, 3, True, 23, 0, 1.24, 6.6)
         124 +(243, 3, True, 22, 0, 0.88, 5.3)
         125 +(244, 3, True, 20, 0, 1.1, 6.9)
         126 +(245, 3, True, 22, 0, 1.37, 8.0)
         127 +(246, 3, True, 20, 0, 1.58, 7.1)
         128 +(247, 1, True, 16, 0, 0.6, 4.8)
         129 +(248, 2, True, 18, 0, 0.41, 5.7)
         130 +(249, 3, True, 20, 0, 1.8, 7.5)
         131 +(250, 2, True, 24, 0, 0.52, 7.3)
         132 +(251, 1, True, 17, 0, 0.39, 5.5)
         133 +(252, 3, True, 22, 0, 0.98, 7.0)
         134 +(253, 2, True, 19, 0, 0.6, 5.5)
         135 +(254, 1, True, 16, 0, 0.15, 4.5)
         136 +(255, 1, True, 30, 0, 0.24, 8.0)
         137 +(256, 2, True, 29, 0, 0.42, 7.9)
         138 +(257, 3, True, 23, 0, 0.49, 6.6)
         139 +(258, 2, True, 21, 0, 0.47, 5.8)
         140 +(259, 1, True, 19, 0, 0.32, 5.1)
         141 +(260, 3, True, 21, 0, 1.33, 7.4)
         142 +(261, 2, True, 22, 0, 0.34, 6.6)
         143 +(262, 3, True, 25, 0, 0.45, 8.5)
         144 +(263, 3, True, 20, 0, 0.46, 6.9)
         145 +(264, 1, True, 18, 0, 0.23, 5.9)
         146 +(265, 3, True, 20, 0, 0.95, 6.6)
         147 +(266, 2, True, 22, 0, 0.31, 6.1)
         148 +(267, 2, True, 19, 0, 0.41, 5.1)
         149 +(268, 3, True, 20, 0, 0.78, 5.8)
         150 +(269, 3, True, 19, 0, 0.52, 5.6)
         151 +(270, 2, True, 18, 0, 0.36, 5.4)
         152 +(271, 3, True, 21, 0, 0.89, 7.4)
         153 +(272, 1, True, 16, 0, 0.25, 6.0)
         154 +(273, 1, True, 20, 0, 0.31, 6.4)
         155 +(274, 2, True, 27, 0, 0.54, 8.8)
         156 +(275, 1, True, 21, 0, 0.33, 5.9)
         157 +(276, 2, True, 20, 0, 0.44, 5.6)
         158 +(277, 1, True, 16, 0, 0.34, 5.6)
         159 +(278, 2, True, 21, 0, 0.4, 6.2)
         160 +(279, 2, True, 20, 0, 0.26, 5.3)
         161 +(280, 2, True, 29, 0, 0.45, 8.5)
         162 +(281, 2, True, 20, 0, 0.52, 6.0)
         163 +(282, 3, True, 20, 0, 1.09, 6.6)
         164 +(283, 1, True, 16, 0, 0.32, 4.2)
         165 +(284, 1, True, 19, 0, 0.24, 5.6)
         166 +(285, 3, True, 20, 0, 0.83, 6.0)
         167 +(286, 1, True, 16, 0, 0.21, 4.9)
         168 +(287, 3, True, 21, 0, 1.0, 5.2)
         169 +(288, 1, True, 18, 0, 0.33, 3.7)
         170 +(289, 2, True, 23, 0, 0.48, 5.6)
         171 +(290, 1, True, 18, 0, 0.24, 3.3)
         172 +(291, 1, True, 18, 0, 0.18, 3.6)
         173 +(292, 3, True, 20, 0, 0.86, 6.3)
         174 +(293, 1, True, 20, 0, 0.35, 5.5)
         175 +(294, 1, True, 27, 0, 0.37, 6.3)
         176 +(295, 1, True, 22, 0, 0.33, 4.9)
         177 +(296, 1, True, 20, 0, 0.4, 3.9)
         178 +(297, 1, True, 18, 0, 0.33, 3.4)
         179 +(298, 2, True, 21, 0, 1.44, 5.0)
         180 +(299, 3, True, 23, 0, 2.12, 6.4)
         181 +(300, 1, True, 18, 0, 1.12, 4.5)
         182 +(301, 1, True, 21, 0, 0.63, 4.1)
         183 +(302, 3, True, 20, 0, 0.75, 4.0)
         184 +(303, 2, True, 23, 0, 0.45, 4.5)
         185 +(304, 3, True, 20, 0, 0.37, 2.8)
         186 +(305, 1, True, 18, 0, 0.38, 4.4)
         187 +(306, 3, True, 22, 0, 1.28, 5.0)
         188 +(307, 3, True, 20, 0, 1.06, 4.9)
         189 +(308, 2, True, 20, 0, 0.63, 4.3)
         190 +(309, 2, True, 20, 0, 0.39, 3.3)
         191 +(310, 1, True, 18, 0, 0.24, 3.2)
         192 +(311, 2, True, 31, 0, 0.34, 5.3)
         193 +(312, 1, True, 16, 0, 0.27, 2.3)
         194 +(313, 1, True, 18, 0, 0.23, 3.2)
         195 +(314, 2, True, 22, 0, 0.25, 4.8)
         196 +(315, 2, True, 19, 0, 0.5, 4.3)
         197 +(316, 1, True, 18, 0, 0.39, 4.3)
         198 +(317, 1, True, 19, 0, 0.19, 4.0)
         199 +(318, 1, True, 17, 0, 0.18, 4.1)
         200 +(319, 3, True, 26, 0, 0.46, 7.3)
         201 +(320, 1, True, 19, 0, 0.28, 5.3)
         202 +(321, 2, True, 20, 0, 0.38, 6.2)
         203 +(322, 1, True, 18, 0, 0.41, 5.3)
         204 +(323, 3, True, 19, 0, 0.8, 6.7)
         205 +(324, 2, True, 22, 0, 0.31, 7.4)
         206 +(325, 1, True, 20, 0, 0.36, 6.2)
         207 +(326, 1, True, 18, 0, 0.34, 5.6)
         208 +(327, 2, True, 21, 0, 0.45, 6.4)
         209 +(328, 1, True, 20, 0, 0.24, 6.0)
         210 +(329, 3, True, 20, 0, 1.08, 6.2)
         211 +(330, 2, True, 20, 0, 0.57, 6.6)
         212 +(331, 1, True, 18, 0, 0.48, 5.3)
         213 +(332, 2, True, 25, 0, 0.44, 7.3)
         214 +(333, 1, True, 18, 0, 0.23, 4.4)
         215 +(334, 2, True, 19, 0, 0.4, 5.2)
         216 +(335, 1, True, 19, 0, 0.33, 4.8)
         217 +(336, 2, True, 21, 0, 0.32, 6.1)
         218 +(337, 1, True, 23, 0, 0.19, 7.2)
         219 +(338, 2, True, 18, 0, 0.51, 5.9)
         220 +(339, 1, True, 18, 0, 0.4, 5.1)
         221 +(340, 1, True, 20, 0, 0.37, 4.7)
         222 +(341, 3, True, 21, 0, 0.54, 5.7)
         223 +(342, 3, True, 23, 0, 0.93, 6.3)
         224 +(343, 1, True, 23, 0, 0.57, 5.8)
         225 +(344, 1, True, 17, 0, 0.27, 4.9)
         226 +(345, 1, True, 16, 0, 0.33, 4.4)
         227 +(346, 2, True, 19, 0, 0.37, 4.2)
         228 +(347, 3, True, 23, 0, 0.47, 6.3)
         229 +(348, 1, True, 21, 0, 0.22, 6.1)
         230 +(349, 3, True, 22, 0, 0.56, 7.9)
         231 +(350, 2, True, 21, 0, 0.45, 7.1)
         232 +(351, 2, True, 27, 0, 0.31, 9.4)
         233 +(352, 1, True, 18, 0, 0.24, 6.1)
         234 +(353, 1, True, 18, 0, 0.3, 5.9)
         235 +(354, 3, True, 23, 0, 0.49, 8.9)
         236 +(355, 2, True, 18, 0, 0.32, 5.8)
         237 +(356, 1, True, 19, 0, 0.27, 6.4)
         238 +(357, 2, True, 25, 0, 0.8, 7.2)
         239 +(358, 3, True, 20, 0, 1.33, 6.3)
         240 +(359, 2, True, 27, 0, 0.26, 6.4)
         241 +(360, 3, True, 20, 0, 2.2, 6.0)
         242 +(361, 3, True, 23, 0, 1.83, 7.5)
         243 +(362, 3, True, 22, 0, 0.67, 6.6)
         244 +(363, 1, True, 16, 0, 0.95, 4.1)
         245 +(364, 2, True, 20, 0, 0.28, 5.7)
         246 +(365, 1, True, 18, 0, 0.26, 4.7)
         247 +(366, 1, True, 16, 0, 0.18, 3.7)
         248 +(367, 3, True, 22, 0, 1.0, 6.1)
         249 +(368, 3, True, 20, 0, 1.55, 6.2)
         250 +(369, 3, True, 24, 0, 0.64, 6.4)
         251 +(370, 2, True, 22, 0, 0.63, 6.3)
         252 +(371, 3, True, 20, 0, 0.68, 5.3)
         253 +(372, 2, True, 18, 0, 0.34, 3.8)
         254 +(373, 2, True, 23, 0, 0.34, 5.6)
         255 +(374, 3, True, 20, 0, 1.05, 5.8)
         256 +(375, 1, True, 18, 0, 0.2, 4.2)
         257 +(376, 2, True, 20, 0, 1.22, 6.6)
         258 +(377, 3, True, 20, 0, 1.08, 6.3)
         259 +(378, 2, True, 21, 0, 0.37, 5.9)
         260 +(379, 3, True, 22, 0, 0.44, 6.8)
         261 +(380, 2, True, 18, 0, 0.35, 5.0)
         262 +(381, 3, True, 21, 0, 0.93, 6.5)
         263 +(382, 1, True, 18, 0, 0.49, 5.2)
         264 +(383, 1, True, 20, 0, 0.39, 5.1)
         265 +(384, 1, True, 18, 0, 0.79, 5.7)
         266 +(385, 3, True, 22, 0, 1.51, 8.4)
         267 +(386, 2, True, 22, 0, 0.42, 6.7)
         268 +(387, 2, True, 19, 0, 0.25, 5.5)
         269 +(388, 2, True, 21, 0, 0.34, 6.8)
         270 +(389, 1, True, 19, 0, 0.31, 4.4)
         271 +(390, 2, True, 21, 0, 0.26, 4.5)
         272 +(391, 1, True, 19, 0, 0.43, 4.1)
         273 +(392, 3, True, 20, 0, 0.73, 6.7)
         274 +(393, 3, True, 23, 0, 0.63, 6.6)
         275 +(394, 1, True, 20, 0, 0.27, 5.5)
         276 +(395, 2, True, 19, 0, 0.38, 5.2)
         277 +(396, 2, True, 24, 0, 0.42, 5.8)
         278 +(397, 3, True, 20, 0, 0.42, 5.8)
         279 +(398, 3, True, 21, 0, 0.53, 6.0)
         280 +(399, 3, True, 21, 0, 0.4, 5.2)
         281 +solved 280 / 280 mean steps 20.557142857142857
diff --git a/res_rot4.json b/res_rot4.json
new file mode 100644
index 0000000..705381a
--- /dev/null
+++ b/res_rot4.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 0.35, 6.9], [1, 2, true, 18, 0, 0.64, 5.1], [2, 3, true, 19, 0, 2.02, 8.0], [3, 3, true, 21, 0, 3.57, 9.6], [4, 3, true, 20, 0, 3.22, 9.1], [5, 3, true, 23, 0, 3.59, 10.3], [6, 2, true, 19, 0, 1.94, 7.7], [7, 3, true, 22, 0, 2.49, 9.7], [8, 3, true, 20, 0, 0.49, 6.2], [9, 2, true, 22, 0, 0.46, 6.5], [10, 3, true, 21, 0, 1.12, 6.8], [11, 1, true, 19, 0, 0.32, 5.6], [12, 2, true, 22, 0, 0.61, 6.5], [13, 3, true, 24, 0, 1.07, 7.3], [14, 1, true, 29, 0, 0.17, 7.1], [15, 3, true, 24, 0, 1.07, 7.6], [16, 2, true, 22, 0, 0.38, 6.2], [17, 3, true, 22, 0, 2.92, 9.0], [18, 3, true, 22, 0, 1.86, 8.4], [19, 2, true, 25, 0, 0.96, 7.9], [20, 3, true, 27, 0, 1.28, 8.3], [21, 1, true, 19, 0, 1.09, 5.6], [22, 3, true, 21, 0, 1.36, 6.8], [23, 1, true, 17, 0, 0.41, 4.4], [24, 2, true, 18, 0, 0.28, 5.3], [25, 2, true, 20, 0, 0.75, 5.4], [26, 3, true, 21, 0, 1.36, 6.6], [27, 1, true, 21, 0, 0.26, 5.5], [28, 2, true, 21, 0, 0.28, 5.8], [29, 3, true, 20, 0, 0.59, 6.0], [30, 1, true, 20, 0, 0.39, 6.6], [31, 2, true, 25, 0, 0.35, 7.9], [32, 3, true, 18, 0, 0.34, 6.6], [33, 3, true, 22, 0, 0.53, 8.5], [34, 1, true, 18, 0, 0.28, 5.7], [35, 1, true, 18, 0, 0.24, 6.3], [36, 2, true, 20, 0, 0.26, 6.6], [37, 1, true, 18, 0, 0.22, 5.7], [38, 1, true, 20, 0, 0.42, 5.9], [39, 3, true, 22, 0, 0.48, 6.0], [40, 2, true, 21, 0, 0.37, 5.7], [41, 2, true, 19, 0, 0.48, 4.2], [42, 1, true, 20, 0, 0.3, 5.8], [43, 2, true, 24, 0, 0.63, 6.6], [44, 3, true, 20, 0, 0.6, 7.1], [45, 3, true, 21, 0, 0.47, 6.6], [46, 2, true, 18, 0, 0.38, 5.8], [47, 1, true, 20, 0, 0.33, 4.6], [48, 1, true, 19, 0, 0.35, 4.5], [49, 1, true, 22, 0, 0.56, 5.3], [50, 3, true, 21, 0, 1.0, 6.3], [51, 2, true, 20, 0, 0.39, 5.3], [52, 3, true, 22, 0, 0.6, 6.4], [53, 3, true, 20, 0, 0.88, 5.3], [54, 1, true, 19, 0, 0.32, 4.6], [55, 3, true, 27, 0, 1.52, 7.5], [56, 2, true, 23, 0, 0.55, 5.4], [57, 1, true, 16, 0, 0.4, 3.7], [58, 2, true, 23, 0, 0.72, 6.2], [59, 3, true, 21, 0, 0.96, 7.0], [60, 1, true, 22, 0, 0.42, 6.4], [61, 2, true, 20, 0, 0.29, 5.9], [62, 2, true, 22, 0, 0.43, 6.0], [63, 2, true, 21, 0, 0.58, 5.6], [64, 2, true, 21, 0, 0.31, 4.9], [65, 1, true, 17, 0, 0.35, 4.2], [66, 3, true, 21, 0, 0.41, 6.5], [67, 3, true, 21, 0, 0.41, 6.7], [68, 2, true, 19, 0, 0.29, 5.4], [69, 1, true, 20, 0, 0.27, 5.3], [70, 2, true, 20, 0, 0.34, 4.6], [71, 3, true, 20, 0, 1.1, 4.6], [72, 3, true, 20, 0, 1.68, 7.4], [73, 3, true, 20, 0, 0.98, 6.6], [74, 1, true, 20, 0, 0.29, 5.6], [75, 2, true, 18, 0, 0.53, 4.4], [76, 2, true, 22, 0, 0.33, 4.6], [77, 1, true, 18, 0, 0.18, 3.4], [78, 3, true, 21, 0, 0.4, 5.8], [79, 1, true, 23, 0, 0.22, 5.3], [80, 3, true, 21, 0, 0.66, 5.8], [81, 1, true, 18, 0, 0.26, 3.5], [82, 3, true, 19, 0, 0.44, 3.7], [83, 3, true, 22, 0, 2.08, 4.8], [84, 2, true, 22, 0, 1.82, 4.2], [85, 3, true, 19, 0, 6.28, 6.7], [86, 3, true, 21, 0, 2.23, 4.1], [87, 2, true, 23, 0, 4.08, 4.2], [88, 2, true, 20, 0, 5.45, 5.8], [89, 3, true, 29, 0, 4.49, 4.7], [90, 2, true, 20, 0, 7.57, 7.7], [91, 3, true, 22, 0, 4.77, 4.9], [92, 2, true, 23, 0, 5.88, 6.0], [93, 3, true, 22, 0, 11.84, 12.2], [94, 1, true, 20, 0, 7.91, 8.0], [95, 2, true, 21, 0, 8.76, 8.9], [96, 3, true, 21, 0, 6.89, 7.1], [97, 1, true, 27, 0, 9.25, 10.2], [98, 2, true, 22, 0, 6.59, 7.2], [99, 3, true, 22, 0, 7.58, 8.8], [100, 3, true, 23, 0, 7.35, 8.8], [101, 1, true, 17, 0, 2.91, 3.1], [102, 2, true, 21, 0, 6.28, 7.1], [103, 2, true, 21, 0, 4.72, 5.3], [104, 3, true, 20, 0, 7.92, 8.2], [105, 1, true, 20, 0, 2.67, 3.3], [106, 2, true, 19, 0, 3.48, 4.3], [107, 1, true, 20, 0, 2.88, 3.7], [108, 1, true, 18, 0, 4.08, 4.2], [109, 2, true, 19, 0, 5.9, 6.0], [110, 2, true, 20, 0, 6.59, 7.6], [111, 2, true, 20, 0, 5.04, 5.2], [112, 1, true, 18, 0, 5.64, 6.1], [113, 1, true, 19, 0, 3.86, 4.2], [114, 1, true, 18, 0, 5.1, 5.2], [115, 2, true, 21, 0, 5.35, 5.7], [116, 1, true, 21, 0, 3.05, 3.7], [117, 1, true, 25, 0, 2.84, 3.1], [118, 2, true, 19, 0, 2.51, 2.7], [119, 2, true, 19, 0, 1.93, 2.1]]
\ No newline at end of file
diff --git a/res_v3_big.json b/res_v3_big.json
new file mode 100644
index 0000000..432b5d9
--- /dev/null
+++ b/res_v3_big.json
@@ -0,0 +1 @@
           1 +[[120, 1, true, 18, 0, 0.36, 5.1], [121, 1, true, 20, 0, 0.4, 4.8], [122, 3, true, 20, 0, 0.63, 5.4], [123, 1, true, 21, 0, 0.6, 5.9], [124, 3, true, 22, 0, 0.75, 5.5], [125, 2, true, 18, 0, 0.52, 4.6], [126, 1, true, 18, 0, 0.46, 3.1], [127, 2, true, 21, 0, 0.58, 5.8], [128, 3, true, 21, 0, 0.74, 5.5], [129, 2, true, 21, 0, 1.19, 5.0], [130, 3, true, 23, 0, 2.96, 6.7], [131, 2, true, 21, 0, 1.7, 5.2], [132, 3, true, 24, 0, 7.53, 10.0], [133, 2, true, 18, 0, 2.65, 4.9], [134, 3, true, 23, 0, 7.99, 9.4], [135, 2, true, 18, 0, 4.22, 4.6], [136, 3, true, 22, 0, 4.07, 4.4], [137, 2, true, 21, 0, 5.15, 6.4], [138, 2, true, 22, 0, 4.21, 5.5], [139, 2, true, 20, 0, 4.21, 6.1], [140, 2, true, 18, 0, 3.69, 7.6], [141, 2, true, 18, 0, 2.56, 6.8], [142, 1, true, 18, 0, 1.94, 6.7], [143, 3, true, 23, 0, 1.62, 7.9], [144, 1, true, 19, 0, 0.49, 4.7], [145, 2, true, 23, 0, 0.91, 6.8], [146, 3, true, 20, 0, 1.02, 5.5], [147, 1, true, 17, 0, 0.46, 6.3], [148, 1, true, 18, 0, 0.43, 5.7], [149, 1, true, 16, 0, 0.26, 4.4], [150, 2, true, 20, 0, 0.68, 4.4], [151, 3, true, 25, 0, 3.07, 9.3], [152, 3, true, 27, 0, 2.58, 8.8], [153, 3, true, 22, 0, 2.55, 8.3], [154, 1, true, 20, 0, 1.32, 6.2], [155, 1, true, 16, 0, 0.95, 5.9], [156, 3, true, 20, 0, 1.01, 6.7], [157, 1, true, 20, 0, 0.24, 5.0], [158, 2, true, 20, 0, 0.43, 6.3], [159, 3, true, 20, 0, 0.85, 7.6], [160, 1, true, 18, 0, 0.4, 7.2], [161, 3, true, 20, 0, 1.44, 7.8], [162, 2, true, 27, 0, 0.56, 8.1], [163, 2, true, 18, 0, 0.62, 5.9], [164, 2, true, 27, 0, 0.37, 7.6], [165, 2, true, 19, 0, 0.27, 5.5], [166, 3, true, 20, 0, 1.23, 6.7], [167, 3, true, 21, 0, 0.92, 6.0], [168, 2, true, 20, 0, 0.73, 6.0], [169, 3, true, 31, 0, 0.85, 8.0], [170, 3, true, 22, 0, 0.72, 6.4], [171, 3, true, 21, 0, 0.6, 6.5], [172, 2, true, 20, 0, 0.66, 6.2], [173, 3, true, 33, 0, 0.71, 10.5], [174, 2, true, 20, 0, 0.83, 6.3], [175, 3, true, 22, 0, 1.36, 7.3], [176, 1, true, 23, 0, 0.37, 7.4], [177, 3, true, 21, 0, 1.37, 7.3], [178, 2, true, 22, 0, 0.66, 6.4], [179, 3, true, 21, 0, 0.64, 6.5], [180, 1, true, 19, 0, 0.36, 5.7], [181, 3, true, 23, 0, 0.77, 7.8], [182, 3, true, 18, 0, 0.94, 6.1], [183, 3, true, 22, 0, 1.18, 8.2], [184, 2, true, 23, 0, 0.42, 7.4], [185, 1, true, 19, 0, 0.36, 5.8], [186, 1, true, 37, 0, 0.38, 10.6], [187, 2, true, 20, 0, 0.66, 6.7], [188, 2, true, 18, 0, 0.59, 6.6], [189, 2, true, 29, 0, 0.51, 10.1], [190, 1, true, 18, 0, 0.32, 6.3], [191, 1, true, 21, 0, 0.95, 8.2], [192, 3, true, 22, 0, 1.38, 8.1], [193, 2, true, 21, 0, 0.65, 7.2], [194, 3, true, 20, 0, 0.94, 7.0], [195, 1, true, 18, 0, 0.34, 4.9], [196, 1, true, 16, 0, 0.94, 4.6], [197, 3, true, 19, 0, 1.11, 5.8], [198, 2, true, 21, 0, 0.58, 6.0], [199, 2, true, 20, 0, 0.33, 6.1], [200, 1, true, 18, 0, 0.35, 5.5], [201, 1, true, 21, 0, 0.28, 6.0], [202, 1, true, 20, 0, 0.36, 6.4], [203, 1, true, 19, 0, 0.26, 5.2], [204, 3, true, 20, 0, 0.86, 5.9], [205, 2, true, 20, 0, 0.43, 4.8], [206, 2, true, 18, 0, 0.59, 4.1], [207, 1, true, 19, 0, 0.4, 4.8], [208, 3, true, 20, 0, 1.67, 6.6], [209, 3, true, 20, 0, 1.29, 6.3], [210, 1, true, 19, 0, 0.28, 5.1], [211, 1, true, 16, 0, 0.3, 3.8], [212, 1, true, 23, 0, 0.22, 5.8], [213, 1, true, 18, 0, 0.3, 4.7], [214, 1, true, 20, 0, 0.25, 4.5], [215, 3, true, 20, 0, 2.56, 7.2], [216, 3, true, 21, 0, 3.71, 9.5], [217, 3, true, 19, 0, 3.09, 7.5], [218, 2, true, 23, 0, 1.41, 7.1], [219, 1, true, 27, 0, 0.95, 7.6], [220, 3, true, 23, 0, 0.73, 6.7], [221, 2, true, 20, 0, 0.45, 5.6], [222, 2, true, 18, 0, 0.22, 4.4], [223, 2, true, 19, 0, 0.35, 5.4], [224, 3, true, 20, 0, 0.56, 5.9], [225, 3, true, 20, 0, 0.88, 6.9], [226, 3, true, 20, 0, 0.7, 5.7], [227, 2, true, 18, 0, 0.45, 4.9], [228, 2, true, 18, 0, 0.39, 5.4], [229, 2, true, 21, 0, 0.43, 6.5], [230, 2, true, 19, 0, 0.49, 6.2], [231, 1, true, 24, 0, 0.31, 6.9], [232, 2, true, 19, 0, 0.42, 5.7], [233, 1, true, 20, 0, 0.22, 5.8], [234, 2, true, 21, 0, 0.4, 5.8], [235, 3, true, 20, 0, 1.19, 6.0], [236, 2, true, 20, 0, 0.43, 4.6], [237, 3, true, 23, 0, 0.64, 5.2], [238, 2, true, 20, 0, 0.4, 4.0], [239, 3, true, 20, 0, 0.57, 4.1], [240, 3, true, 20, 0, 0.66, 4.8], [241, 2, true, 20, 0, 0.42, 3.8], [242, 3, true, 23, 0, 1.24, 6.6], [243, 3, true, 22, 0, 0.88, 5.3], [244, 3, true, 20, 0, 1.1, 6.9], [245, 3, true, 22, 0, 1.37, 8.0], [246, 3, true, 20, 0, 1.58, 7.1], [247, 1, true, 16, 0, 0.6, 4.8], [248, 2, true, 18, 0, 0.41, 5.7], [249, 3, true, 20, 0, 1.8, 7.5], [250, 2, true, 24, 0, 0.52, 7.3], [251, 1, true, 17, 0, 0.39, 5.5], [252, 3, true, 22, 0, 0.98, 7.0], [253, 2, true, 19, 0, 0.6, 5.5], [254, 1, true, 16, 0, 0.15, 4.5], [255, 1, true, 30, 0, 0.24, 8.0], [256, 2, true, 29, 0, 0.42, 7.9], [257, 3, true, 23, 0, 0.49, 6.6], [258, 2, true, 21, 0, 0.47, 5.8], [259, 1, true, 19, 0, 0.32, 5.1], [260, 3, true, 21, 0, 1.33, 7.4], [261, 2, true, 22, 0, 0.34, 6.6], [262, 3, true, 25, 0, 0.45, 8.5], [263, 3, true, 20, 0, 0.46, 6.9], [264, 1, true, 18, 0, 0.23, 5.9], [265, 3, true, 20, 0, 0.95, 6.6], [266, 2, true, 22, 0, 0.31, 6.1], [267, 2, true, 19, 0, 0.41, 5.1], [268, 3, true, 20, 0, 0.78, 5.8], [269, 3, true, 19, 0, 0.52, 5.6], [270, 2, true, 18, 0, 0.36, 5.4], [271, 3, true, 21, 0, 0.89, 7.4], [272, 1, true, 16, 0, 0.25, 6.0], [273, 1, true, 20, 0, 0.31, 6.4], [274, 2, true, 27, 0, 0.54, 8.8], [275, 1, true, 21, 0, 0.33, 5.9], [276, 2, true, 20, 0, 0.44, 5.6], [277, 1, true, 16, 0, 0.34, 5.6], [278, 2, true, 21, 0, 0.4, 6.2], [279, 2, true, 20, 0, 0.26, 5.3], [280, 2, true, 29, 0, 0.45, 8.5], [281, 2, true, 20, 0, 0.52, 6.0], [282, 3, true, 20, 0, 1.09, 6.6], [283, 1, true, 16, 0, 0.32, 4.2], [284, 1, true, 19, 0, 0.24, 5.6], [285, 3, true, 20, 0, 0.83, 6.0], [286, 1, true, 16, 0, 0.21, 4.9], [287, 3, true, 21, 0, 1.0, 5.2], [288, 1, true, 18, 0, 0.33, 3.7], [289, 2, true, 23, 0, 0.48, 5.6], [290, 1, true, 18, 0, 0.24, 3.3], [291, 1, true, 18, 0, 0.18, 3.6], [292, 3, true, 20, 0, 0.86, 6.3], [293, 1, true, 20, 0, 0.35, 5.5], [294, 1, true, 27, 0, 0.37, 6.3], [295, 1, true, 22, 0, 0.33, 4.9], [296, 1, true, 20, 0, 0.4, 3.9], [297, 1, true, 18, 0, 0.33, 3.4], [298, 2, true, 21, 0, 1.44, 5.0], [299, 3, true, 23, 0, 2.12, 6.4], [300, 1, true, 18, 0, 1.12, 4.5], [301, 1, true, 21, 0, 0.63, 4.1], [302, 3, true, 20, 0, 0.75, 4.0], [303, 2, true, 23, 0, 0.45, 4.5], [304, 3, true, 20, 0, 0.37, 2.8], [305, 1, true, 18, 0, 0.38, 4.4], [306, 3, true, 22, 0, 1.28, 5.0], [307, 3, true, 20, 0, 1.06, 4.9], [308, 2, true, 20, 0, 0.63, 4.3], [309, 2, true, 20, 0, 0.39, 3.3], [310, 1, true, 18, 0, 0.24, 3.2], [311, 2, true, 31, 0, 0.34, 5.3], [312, 1, true, 16, 0, 0.27, 2.3], [313, 1, true, 18, 0, 0.23, 3.2], [314, 2, true, 22, 0, 0.25, 4.8], [315, 2, true, 19, 0, 0.5, 4.3], [316, 1, true, 18, 0, 0.39, 4.3], [317, 1, true, 19, 0, 0.19, 4.0], [318, 1, true, 17, 0, 0.18, 4.1], [319, 3, true, 26, 0, 0.46, 7.3], [320, 1, true, 19, 0, 0.28, 5.3], [321, 2, true, 20, 0, 0.38, 6.2], [322, 1, true, 18, 0, 0.41, 5.3], [323, 3, true, 19, 0, 0.8, 6.7], [324, 2, true, 22, 0, 0.31, 7.4], [325, 1, true, 20, 0, 0.36, 6.2], [326, 1, true, 18, 0, 0.34, 5.6], [327, 2, true, 21, 0, 0.45, 6.4], [328, 1, true, 20, 0, 0.24, 6.0], [329, 3, true, 20, 0, 1.08, 6.2], [330, 2, true, 20, 0, 0.57, 6.6], [331, 1, true, 18, 0, 0.48, 5.3], [332, 2, true, 25, 0, 0.44, 7.3], [333, 1, true, 18, 0, 0.23, 4.4], [334, 2, true, 19, 0, 0.4, 5.2], [335, 1, true, 19, 0, 0.33, 4.8], [336, 2, true, 21, 0, 0.32, 6.1], [337, 1, true, 23, 0, 0.19, 7.2], [338, 2, true, 18, 0, 0.51, 5.9], [339, 1, true, 18, 0, 0.4, 5.1], [340, 1, true, 20, 0, 0.37, 4.7], [341, 3, true, 21, 0, 0.54, 5.7], [342, 3, true, 23, 0, 0.93, 6.3], [343, 1, true, 23, 0, 0.57, 5.8], [344, 1, true, 17, 0, 0.27, 4.9], [345, 1, true, 16, 0, 0.33, 4.4], [346, 2, true, 19, 0, 0.37, 4.2], [347, 3, true, 23, 0, 0.47, 6.3], [348, 1, true, 21, 0, 0.22, 6.1], [349, 3, true, 22, 0, 0.56, 7.9], [350, 2, true, 21, 0, 0.45, 7.1], [351, 2, true, 27, 0, 0.31, 9.4], [352, 1, true, 18, 0, 0.24, 6.1], [353, 1, true, 18, 0, 0.3, 5.9], [354, 3, true, 23, 0, 0.49, 8.9], [355, 2, true, 18, 0, 0.32, 5.8], [356, 1, true, 19, 0, 0.27, 6.4], [357, 2, true, 25, 0, 0.8, 7.2], [358, 3, true, 20, 0, 1.33, 6.3], [359, 2, true, 27, 0, 0.26, 6.4], [360, 3, true, 20, 0, 2.2, 6.0], [361, 3, true, 23, 0, 1.83, 7.5], [362, 3, true, 22, 0, 0.67, 6.6], [363, 1, true, 16, 0, 0.95, 4.1], [364, 2, true, 20, 0, 0.28, 5.7], [365, 1, true, 18, 0, 0.26, 4.7], [366, 1, true, 16, 0, 0.18, 3.7], [367, 3, true, 22, 0, 1.0, 6.1], [368, 3, true, 20, 0, 1.55, 6.2], [369, 3, true, 24, 0, 0.64, 6.4], [370, 2, true, 22, 0, 0.63, 6.3], [371, 3, true, 20, 0, 0.68, 5.3], [372, 2, true, 18, 0, 0.34, 3.8], [373, 2, true, 23, 0, 0.34, 5.6], [374, 3, true, 20, 0, 1.05, 5.8], [375, 1, true, 18, 0, 0.2, 4.2], [376, 2, true, 20, 0, 1.22, 6.6], [377, 3, true, 20, 0, 1.08, 6.3], [378, 2, true, 21, 0, 0.37, 5.9], [379, 3, true, 22, 0, 0.44, 6.8], [380, 2, true, 18, 0, 0.35, 5.0], [381, 3, true, 21, 0, 0.93, 6.5], [382, 1, true, 18, 0, 0.49, 5.2], [383, 1, true, 20, 0, 0.39, 5.1], [384, 1, true, 18, 0, 0.79, 5.7], [385, 3, true, 22, 0, 1.51, 8.4], [386, 2, true, 22, 0, 0.42, 6.7], [387, 2, true, 19, 0, 0.25, 5.5], [388, 2, true, 21, 0, 0.34, 6.8], [389, 1, true, 19, 0, 0.31, 4.4], [390, 2, true, 21, 0, 0.26, 4.5], [391, 1, true, 19, 0, 0.43, 4.1], [392, 3, true, 20, 0, 0.73, 6.7], [393, 3, true, 23, 0, 0.63, 6.6], [394, 1, true, 20, 0, 0.27, 5.5], [395, 2, true, 19, 0, 0.38, 5.2], [396, 2, true, 24, 0, 0.42, 5.8], [397, 3, true, 20, 0, 0.42, 5.8], [398, 3, true, 21, 0, 0.53, 6.0], [399, 3, true, 21, 0, 0.4, 5.2]]
\ No newline at end of file
```

</details>

<a id="C023"></a>
### C023 · tighter margins: obj 1.993, lander 3.995, sample 0.246, home 0.235

Commit `f673e87ee7eac74d794df9f810d6d37c61b7ac51`; parents: 711a3f4a37d23ce2c7c0fea52c64adb5022854c1. Recorded author date: 2026-10-01T11:55:40+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E1045](01_timeline.md#E1045): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C023_f673e87_approach.py) · [Exact all-file diff](evidence/diffs/C023_f673e87.diff)

[Previous saved controller snapshot](evidence/versions/C022_711a3f4_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a1e1b94..0a4f791 100644
--- a/approach.py
+++ b/approach.py
@@ -18,10 +18,10 @@ PILLAR_R = 0.245
   18     18  MOUND_R = 0.185
   19     19  LANDER_XMIN = -1.15
   20     20  LANDER_YMIN = -1.42
   21        -OBJ_RANGE = 1.985
   22        -LANDER_RANGE = 3.985
   23        -SAMPLE_R = 0.242
   24        -HOME_R = 0.22
          21 +OBJ_RANGE = 1.993
          22 +LANDER_RANGE = 3.995
          23 +SAMPLE_R = 0.246
          24 +HOME_R = 0.235
   25     25  IMG_TH = -math.pi / 2
   26     26  ROT_IMG = 4.0
   27     27  PILLAR_INFL_OBJ = 0.015
diff --git a/approach_m.py b/approach_m.py
new file mode 100644
index 0000000..0a4f791
--- /dev/null
+++ b/approach_m.py
@@ -0,0 +1,659 @@
           1 +"""Rovers approach: staged grid BFS planner per rover + joint task assignment."""
           2 +import itertools
           3 +import math
           4 +
           5 +import numpy as np
           6 +from scipy.ndimage import minimum_filter
           7 +
           8 +INF = 10 ** 6
           9 +RES = 0.05            # grid resolution
          10 +WIN = 4               # max cells per step per axis (0.2 / RES)
          11 +SEL = {"sample": -0.8333, "cal": -0.5, "img": -0.1667, "noop": 0.1667,
          12 +       "send": 0.5, "drop": 0.8333}
          13 +
          14 +# geometry constants (empirically probed)
          15 +WALL_IN = 0.2271 + 0.004
          16 +ARENA = 2.2729 - 0.004
          17 +PILLAR_R = 0.245
          18 +MOUND_R = 0.185
          19 +LANDER_XMIN = -1.15
          20 +LANDER_YMIN = -1.42
          21 +OBJ_RANGE = 1.993
          22 +LANDER_RANGE = 3.995
          23 +SAMPLE_R = 0.246
          24 +HOME_R = 0.235
          25 +IMG_TH = -math.pi / 2
          26 +ROT_IMG = 4.0
          27 +PILLAR_INFL_OBJ = 0.015
          28 +PILLAR_INFL_LAND = 0.04
          29 +ROVER_OCC_R = 0.26
          30 +CAM_OFF = (-0.087, -0.0125)
          31 +OBJ_BACK_DEG = 108.0     # if |rel bearing| > this, pillars don't occlude objectives
          32 +LAND_BACK_DEG = 110.0    # same quirk for lander (sending)
          33 +USE_BACK_OBJ = True
          34 +USE_BACK_LAND = True
          35 +
          36 +
          37 +def _wrap(a):
          38 +    return (a + np.pi) % (2 * np.pi) - np.pi
          39 +
          40 +
          41 +def rot_steps(a, b):
          42 +    d = abs(float(_wrap(b - a)))
          43 +    return int(math.ceil(d / 0.4 - 1e-6))
          44 +
          45 +
          46 +def approach_angle(a, b, dmax):
          47 +    d = float(_wrap(b - a))
          48 +    if abs(d) <= dmax:
          49 +        return float(_wrap(b))
          50 +    return float(_wrap(a + math.copysign(dmax, d)))
          51 +
          52 +
          53 +def seg_hits_box(px, py, qx, qy, cx, cy, hx, hy):
          54 +    """Vectorised: does segment p->q (p arrays, q scalar) intersect AABB?"""
          55 +    dx = qx - px
          56 +    dy = qy - py
          57 +    t0 = np.zeros_like(px)
          58 +    t1 = np.ones_like(px)
          59 +    ok = np.ones(px.shape, dtype=bool)
          60 +    for d, p, lo, hi in ((dx, px, cx - hx, cx + hx), (dy, py, cy - hy, cy + hy)):
          61 +        small = np.abs(d) < 1e-12
          62 +        ok &= ~(small & ((p < lo) | (p > hi)))
          63 +        with np.errstate(divide="ignore", invalid="ignore"):
          64 +            ta = (lo - p) / d
          65 +            tb = (hi - p) / d
          66 +        tmin = np.where(small, -np.inf, np.minimum(ta, tb))
          67 +        tmax = np.where(small, np.inf, np.maximum(ta, tb))
          68 +        t0 = np.maximum(t0, tmin)
          69 +        t1 = np.minimum(t1, tmax)
          70 +    return ok & (t0 <= t1)
          71 +
          72 +
          73 +def seg_hits_disk(px, py, qx, qy, cx, cy, r):
          74 +    dx = qx - px
          75 +    dy = qy - py
          76 +    L2 = dx * dx + dy * dy + 1e-12
          77 +    t = np.clip(((cx - px) * dx + (cy - py) * dy) / L2, 0, 1)
          78 +    ex = px + t * dx - cx
          79 +    ey = py + t * dy - cy
          80 +    return ex * ex + ey * ey < r * r
          81 +
          82 +
          83 +def box_dist(px, py, cx, cy, hx, hy):
          84 +    ddx = np.maximum(np.abs(px - cx) - hx, 0)
          85 +    ddy = np.maximum(np.abs(py - cy) - hy, 0)
          86 +    return np.hypot(ddx, ddy)
          87 +
          88 +
          89 +def propagate(f, free):
          90 +    f = np.where(free, f, INF)
          91 +    while True:
          92 +        m = minimum_filter(f, size=2 * WIN + 1, mode="constant", cval=INF) + 1
          93 +        nf = np.where(free, np.minimum(f, m), INF)
          94 +        if np.array_equal(nf, f):
          95 +            return f
          96 +        f = nf
          97 +
          98 +
          99 +def op_stage(fprev, region):
         100 +    m = minimum_filter(fprev, size=2 * WIN + 1, mode="constant", cval=INF) + 1
         101 +    return np.where(region, np.minimum(m, INF), INF)
         102 +
         103 +
         104 +class Scene:
         105 +    def __init__(self, state):
         106 +        self.rovers = {}
         107 +        self.objectives = []
         108 +        self.samples = []
         109 +        self.pillars = []
         110 +        self.mounds = []
         111 +        self.lander = (-1.9, -2.0)
         112 +        for o in state:
         113 +            t = o.type.name
         114 +            g = lambda f: state.get(o, f)
         115 +            if t == "rover":
         116 +                self.rovers[o.name] = dict(x=g("x"), y=g("y"), th=g("theta"),
         117 +                                           full=g("store_full") > 0.5,
         118 +                                           cal=g("calibrated") > 0.5)
         119 +            elif t == "lander":
         120 +                self.lander = (g("x"), g("y"))
         121 +            elif t == "objective":
         122 +                self.objectives.append(dict(name=o.name, x=g("x"), y=g("y"),
         123 +                                            img=(g("have_image_rover0") > 0.5,
         124 +                                                 g("have_image_rover1") > 0.5),
         125 +                                            recv=g("received_image") > 0.5))
         126 +            elif t == "sample":
         127 +                self.samples.append(dict(name=o.name, x=g("x"), y=g("y"),
         128 +                                         soil=g("is_soil") > 0.5,
         129 +                                         an=(g("analyzed_rover0") > 0.5,
         130 +                                             g("analyzed_rover1") > 0.5),
         131 +                                         recv=g("received_analysis") > 0.5))
         132 +            elif t == "obstacle":
         133 +                d = (g("x"), g("y"), g("half_x"), g("half_y"))
         134 +                if g("half_x") > 0.15:
         135 +                    self.mounds.append(d)
         136 +                else:
         137 +                    self.pillars.append(d)
         138 +
         139 +
         140 +class RoverPlanner:
         141 +    """Grid + regions for one rover."""
         142 +
         143 +    def __init__(self, idx, home, scene, other_pos_list, cur_th=None, bad=(), img_th=None):
         144 +        self.idx = idx
         145 +        self.home = home  # (x, y, th)
         146 +        hx, hy, th = home
         147 +        self.th = th
         148 +        side = 1 if hx > 0 else -1
         149 +        lo_x, hi_x = (WALL_IN, ARENA) if side > 0 else (-ARENA, -WALL_IN)
         150 +        i0 = math.ceil((lo_x - hx) / RES - 1e-9)
         151 +        i1 = math.floor((hi_x - hx) / RES + 1e-9)
         152 +        j0 = math.ceil((-ARENA - hy) / RES - 1e-9)
         153 +        j1 = math.floor((ARENA - hy) / RES + 1e-9)
         154 +        self.xs = hx + RES * np.arange(i0, i1 + 1)
         155 +        self.ys = hy + RES * np.arange(j0, j1 + 1)
         156 +        self.hi = -i0
         157 +        self.hj = -j0
         158 +        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
         159 +        self.X, self.Y = X, Y
         160 +        free = np.ones(X.shape, dtype=bool)
         161 +        for (cx, cy, ax, ay) in scene.pillars:
         162 +            free &= box_dist(X, Y, cx, cy, ax, ay) > PILLAR_R
         163 +        for (cx, cy, ax, ay) in scene.mounds:
         164 +            free &= box_dist(X, Y, cx, cy, ax, ay) > MOUND_R
         165 +        free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
         166 +        for (bx, by) in bad:
         167 +            free &= np.hypot(X - bx, Y - by) > 0.03
         168 +        free[self.hi, self.hj] = True
         169 +        self.free = free
         170 +        self.home_reg = (np.hypot(X - hx, Y - hy) <= HOME_R) & free
         171 +        self.home_reg[self.hi, self.hj] = True
         172 +        c, s = math.cos(th), math.sin(th)
         173 +        self.camx = X + c * CAM_OFF[0] - s * CAM_OFF[1]
         174 +        self.camy = Y + s * CAM_OFF[0] + c * CAM_OFF[1]
         175 +        self.scene = scene
         176 +        ith = th if img_th is None else img_th
         177 +        self.img_th = ith
         178 +        cur = th if cur_th is None else cur_th
         179 +        self.cur_th = cur
         180 +        self.nrot_in = rot_steps(cur, ith)
         181 +        self.nrot_out = rot_steps(ith, th)
         182 +        hs = [cur, ith, th]
         183 +        for k in range(1, 9):
         184 +            hs.append(approach_angle(cur, ith, 0.4 * k))
         185 +            hs.append(approach_angle(ith, th, 0.4 * k))
         186 +            hs.append(approach_angle(cur, th, 0.4 * k))
         187 +        self.headings = hs
         188 +        ci, si = math.cos(ith), math.sin(ith)
         189 +        camx_i = X + ci * CAM_OFF[0] - si * CAM_OFF[1]
         190 +        camy_i = Y + si * CAM_OFF[0] + ci * CAM_OFF[1]
         191 +        # objective visibility
         192 +        self.vis = []
         193 +        self.objd = []
         194 +        for ob in scene.objectives:
         195 +            ox, oy = ob["x"], ob["y"]
         196 +            d = np.hypot(ox - camx_i, oy - camy_i)
         197 +            v = (d <= OBJ_RANGE)
         198 +            occ = np.zeros(X.shape, dtype=bool)
         199 +            for (cx, cy, ax, ay) in scene.pillars:
         200 +                e = PILLAR_INFL_OBJ
         201 +                occ |= seg_hits_box(camx_i, camy_i, ox, oy, cx, cy, ax + e, ay + e)
         202 +                occ |= seg_hits_box(X, Y, ox, oy, cx, cy, ax + e, ay + e)
         203 +            if USE_BACK_OBJ:
         204 +                rel = np.abs(_wrap(np.arctan2(oy - Y, ox - X) - ith))
         205 +                back = rel > math.radians(OBJ_BACK_DEG)
         206 +            else:
         207 +                back = np.zeros(X.shape, dtype=bool)
         208 +            occ2 = np.zeros(X.shape, dtype=bool)
         209 +            for (px, py) in other_pos_list:
         210 +                occ2 |= seg_hits_disk(camx_i, camy_i, ox, oy, px, py, ROVER_OCC_R)
         211 +            self.vis.append(v & ((~occ) | back) & ~occ2 & free)
         212 +            self.objd.append(d)
         213 +        self.any_vis = np.zeros(X.shape, dtype=bool)
         214 +        for v in self.vis:
         215 +            self.any_vis |= v
         216 +        # lander visibility (must hold for every heading along the rotation path)
         217 +        lx, ly = scene.lander
         218 +        land = free.copy()
         219 +        land_free = free.copy()
         220 +        for hh in self.headings:
         221 +            ch, sh = math.cos(hh), math.sin(hh)
         222 +            cx_ = X + ch * CAM_OFF[0] - sh * CAM_OFF[1]
         223 +            cy_ = Y + sh * CAM_OFF[0] + ch * CAM_OFF[1]
         224 +            v = (np.hypot(lx - X, ly - Y) <= LANDER_RANGE) & \
         225 +                (np.hypot(lx - cx_, ly - cy_) <= LANDER_RANGE)
         226 +            occ = np.zeros(X.shape, dtype=bool)
         227 +            for (cx, cy, ax, ay) in scene.pillars:
         228 +                e = PILLAR_INFL_LAND
         229 +                occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
         230 +                occ |= seg_hits_box(cx_, cy_, lx, ly, cx, cy, ax + e, ay + e)
         231 +            if USE_BACK_LAND:
         232 +                rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - hh))
         233 +                back = rel > math.radians(LAND_BACK_DEG)
         234 +            else:
         235 +                back = np.zeros(X.shape, dtype=bool)
         236 +            occ2 = np.zeros(X.shape, dtype=bool)
         237 +            for (px, py) in other_pos_list:
         238 +                occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
         239 +                occ2 |= seg_hits_disk(cx_, cy_, lx, ly, px, py, ROVER_OCC_R)
         240 +            land &= v & ((~occ) | back) & ~occ2
         241 +            land_free &= v & ((~occ) | back)
         242 +        self.land = land
         243 +        self.land_free = land_free
         244 +        self.camx_i, self.camy_i = camx_i, camy_i
         245 +        # samples
         246 +        self.sreg = {}
         247 +        dk = {}
         248 +        for kind in ("stone", "soil"):
         249 +            d = np.full(X.shape, 1e9)
         250 +            for sm in scene.samples:
         251 +                if sm["soil"] == (kind == "soil"):
         252 +                    d = np.minimum(d, np.hypot(sm["x"] - X, sm["y"] - Y))
         253 +            dk[kind] = d
         254 +        for kind, oth in (("stone", "soil"), ("soil", "stone")):
         255 +            r = (dk[kind] <= SAMPLE_R) & ((dk[oth] > 0.26) | (dk[oth] > dk[kind] + 0.03))
         256 +            self.sreg[kind] = r & free
         257 +
         258 +    def cell_of(self, x, y):
         259 +        i = int(round((x - self.xs[0]) / RES))
         260 +        j = int(round((y - self.ys[0]) / RES))
         261 +        i = min(max(i, 0), len(self.xs) - 1)
         262 +        j = min(max(j, 0), len(self.ys) - 1)
         263 +        return i, j
         264 +
         265 +    def img_region(self, k, imaged):
         266 +        """cells where image would photograph objective k given set imaged."""
         267 +        reg = self.vis[k].copy()
         268 +        if not reg.any():
         269 +            return reg
         270 +        dk = self.objd[k]
         271 +        for m in range(len(self.vis)):
         272 +            if m == k or m in imaged:
         273 +                continue
         274 +            reg &= ~((self.objd[m] <= 2.03) & (self.objd[m] < dk + 0.03))
         275 +        return reg
         276 +
         277 +
         278 +class GeneratedApproach:
         279 +    def __init__(self, action_space, observation_space, primitives):
         280 +        self.action_space = action_space
         281 +        self.homes = None
         282 +
         283 +    # ------------------------------------------------------------------
         284 +    def reset(self, state, info):
         285 +        sc = Scene(state)
         286 +        self.homes = {n: (r["x"], r["y"], r["th"]) for n, r in sc.rovers.items()}
         287 +        self.replans = 0
         288 +        self.fail_count = 0
         289 +        self.expect = [None, None]
         290 +        self.prev_sc = sc
         291 +        self.log = []
         292 +        self.bad = [[], []]
         293 +        self._plan(state)
         294 +
         295 +    # ------------------------------------------------------------------
         296 +    def _rover_tables(self, ri, sc, need_objs, need_stone, need_soil, pending):
         297 +        name = "rover%d" % ri
         298 +        r = sc.rovers[name]
         299 +        other = sc.rovers["rover%d" % (1 - ri)]
         300 +        ohome = self.homes["rover%d" % (1 - ri)]
         301 +        occl = [(ohome[0], ohome[1])]
         302 +        if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
         303 +            occl.append((other["x"], other["y"]))
         304 +        merged = {}
         305 +        hth = self.homes[name][2]
         306 +        if IMG_TH is None:
         307 +            ths = [hth]
         308 +        else:
         309 +            d = float(_wrap(IMG_TH - hth))
         310 +            ths = [float(_wrap(hth + math.copysign(min(abs(d), ROT_IMG), d)))]
         311 +        for ith in ths:
         312 +            P, table = self._rover_tables_h(ri, sc, need_objs, need_stone, need_soil,
         313 +                                            pending, occl, ith)
         314 +            for k, (c, st) in table.items():
         315 +                if k not in merged or c < merged[k][0]:
         316 +                    merged[k] = (c, st, P)
         317 +        return None, merged
         318 +
         319 +    def _rover_tables_h(self, ri, sc, need_objs, need_stone, need_soil, pending, occl, ith):
         320 +        name = "rover%d" % ri
         321 +        r = sc.rovers[name]
         322 +        P = RoverPlanner(ri, self.homes[name], sc, occl, r["th"], self.bad[ri], ith)
         323 +        self_planner = P
         324 +        start = P.cell_of(r["x"], r["y"])
         325 +        P.free[start] = True
         326 +        f0 = np.full(P.free.shape, INF, dtype=np.int64)
         327 +        f0[start] = 0
         328 +        stages0 = []
         329 +        F = propagate(f0, P.free)
         330 +        stages0.append(("start", None, f0, F))
         331 +        if r["full"]:
         332 +            G = op_stage(F, P.free)
         333 +            F = propagate(G, P.free)
         334 +            stages0.append(("drop", None, G, F))
         335 +        imaged0 = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
         336 +        tasks = []
         337 +        for k in need_objs:
         338 +            if P.vis[k].any():
         339 +                tasks.append(("obj", k))
         340 +        if need_stone and P.sreg["stone"].any():
         341 +            tasks.append(("stone", None))
         342 +        if need_soil and P.sreg["soil"].any():
         343 +            tasks.append(("soil", None))
         344 +        hcell = (P.hi, P.hj)
         345 +        table = {}  # frozenset(task keys) -> (cost, stages)
         346 +
         347 +        def finish(F, stages, done_keys):
         348 +            if not done_keys and not pending:
         349 +                cost = F[P.home_reg].min()
         350 +                st = stages
         351 +            else:
         352 +                G = op_stage(F, P.land)
         353 +                F2 = propagate(G, P.free)
         354 +                cost = F2[P.home_reg].min()
         355 +                st = stages + [("send", None, G, F2)]
         356 +            if cost >= INF:
         357 +                return
         358 +            key = frozenset(done_keys)
         359 +            if key not in table or cost < table[key][0]:
         360 +                table[key] = (int(cost), st)
         361 +
         362 +        def dfs(F, stages, done_keys, imaged, cal):
         363 +            finish(F, stages, done_keys)
         364 +            if F.min() >= INF:
         365 +                return
         366 +            for t in tasks:
         367 +                key = t if t[0] != "obj" else ("obj", t[1])
         368 +                if key in done_keys:
         369 +                    continue
         370 +                if t[0] == "obj":
         371 +                    k = t[1]
         372 +                    st = list(stages)
         373 +                    Fc = F
         374 +                    if not cal:
         375 +                        G = op_stage(F, P.any_vis)
         376 +                        G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
         377 +                        Fc = propagate(G, P.free)
         378 +                        st.append(("cal", None, G, Fc))
         379 +                    reg = P.img_region(k, imaged)
         380 +                    G = op_stage(Fc, reg)
         381 +                    G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
         382 +                    Fi = propagate(G, P.free)
         383 +                    st.append(("img", k, G, Fi))
         384 +                    dfs(Fi, st, done_keys | {key}, imaged | {k}, False)
         385 +                else:
         386 +                    G = op_stage(F, P.sreg[t[0]])
         387 +                    Fs = propagate(G, P.free)
         388 +                    G2 = op_stage(Fs, P.free)
         389 +                    Fd = propagate(G2, P.free)
         390 +                    st = stages + [("sample", t[0], G, Fs), ("drop", None, G2, Fd)]
         391 +                    dfs(Fd, st, done_keys | {key}, imaged, cal)
         392 +
         393 +        dfs(F, stages0, frozenset(), imaged0, r["cal"])
         394 +        return P, table
         395 +
         396 +    def _plan(self, state):
         397 +        sc = Scene(state)
         398 +        self.scene = sc
         399 +        # what is needed
         400 +        need_objs = [k for k, ob in enumerate(sc.objectives)
         401 +                     if not ob["recv"] and not ob["img"][0] and not ob["img"][1]]
         402 +        pending = [False, False]
         403 +        for k, ob in enumerate(sc.objectives):
         404 +            if not ob["recv"]:
         405 +                for ri in range(2):
         406 +                    if ob["img"][ri]:
         407 +                        pending[ri] = True
         408 +        need = {}
         409 +        for kind in ("stone", "soil"):
         410 +            recv = any(s["recv"] for s in sc.samples if s["soil"] == (kind == "soil"))
         411 +            holders = [ri for ri in range(2)
         412 +                       if any(s["an"][ri] for s in sc.samples if s["soil"] == (kind == "soil"))]
         413 +            if recv:
         414 +                need[kind] = False
         415 +            elif holders:
         416 +                need[kind] = False
         417 +                pending[holders[0]] = True
         418 +            else:
         419 +                need[kind] = True
         420 +        tabs = []
         421 +        for ri in range(2):
         422 +            tabs.append(self._rover_tables(ri, sc, need_objs, need["stone"], need["soil"],
         423 +                                           pending[ri]))
         424 +        # joint assignment
         425 +        best = None
         426 +        cands = []
         427 +        n = len(need_objs)
         428 +        stone_opts = [0, 1] if need["stone"] else [None]
         429 +        soil_opts = [0, 1] if need["soil"] else [None]
         430 +        for assign in itertools.product([0, 1], repeat=n):
         431 +            for so in stone_opts:
         432 +                for sl in soil_opts:
         433 +                    sets = [set(), set()]
         434 +                    for k, a in zip(need_objs, assign):
         435 +                        sets[a].add(("obj", k))
         436 +                    if so is not None:
         437 +                        sets[so].add(("stone", None))
         438 +                    if sl is not None:
         439 +                        sets[sl].add(("soil", None))
         440 +                    costs = []
         441 +                    for ri in range(2):
         442 +                        e = tabs[ri][1].get(frozenset(sets[ri]))
         443 +                        costs.append(e)
         444 +                    if costs[0] is None or costs[1] is None:
         445 +                        continue
         446 +                    key = (max(costs[0][0], costs[1][0]), costs[0][0] + costs[1][0])
         447 +                    cands.append((key, costs))
         448 +                    if best is None or key < best[0]:
         449 +                        self.pred = key
         450 +                        best = (key, costs)
         451 +        self.actions = [[], []]
         452 +        if best is None:
         453 +            return
         454 +        cands.sort(key=lambda c: c[0])
         455 +        seen = set()
         456 +        bestreal = None
         457 +        for key, costs in cands:
         458 +            sig = (id(costs[0][1]), id(costs[1][1]))
         459 +            if sig in seen:
         460 +                continue
         461 +            seen.add(sig)
         462 +            if len(seen) > 6 or (bestreal is not None and key[0] >= bestreal[0][0]):
         463 +                break
         464 +            acts = self._realize(sc, tabs, costs)
         465 +            real = (max(len(acts[0]), len(acts[1])), len(acts[0]) + len(acts[1]))
         466 +            if bestreal is None or real < bestreal[0]:
         467 +                bestreal = (real, acts)
         468 +        self.actions = bestreal[1]
         469 +
         470 +    def _realize(self, sc, tabs, costs):
         471 +        best = (None, costs)
         472 +        actions = [[], []]
         473 +        sc = self.scene
         474 +        for ri in range(2):
         475 +            P = costs[ri][2]
         476 +            actions[ri] = self._extract(P, best[1][ri][1])
         477 +        # time-aware re-plan of final send against other rover's trajectory
         478 +        trajs = []
         479 +        for ri in range(2):
         480 +            r = sc.rovers["rover%d" % ri]
         481 +            trajs.append([(r["x"], r["y"])] + [(a[0], a[1]) for a in actions[ri]])
         482 +        new_actions = list(actions)
         483 +        for ri in range(2):
         484 +            stages = best[1][ri][1]
         485 +            if stages[-1][0] != "send":
         486 +                continue
         487 +            P = costs[ri][2]
         488 +            Fprev = stages[-2][3]
         489 +            G0 = op_stage(Fprev, P.land_free)
         490 +            other = trajs[1 - ri]
         491 +            G = np.full(G0.shape, INF, dtype=G0.dtype)
         492 +            pending_mask = G0 < INF
         493 +            tmin = int(G0[pending_mask].min()) if pending_mask.any() else INF
         494 +            lx, ly = sc.lander
         495 +            t = tmin
         496 +            while pending_mask.any() and t < tmin + 200:
         497 +                blk = np.zeros(P.X.shape, dtype=bool)
         498 +                for tt in (t - 1, t):
         499 +                    ox, oy = other[max(0, min(tt, len(other) - 1))]
         500 +                    blk |= seg_hits_disk(P.camx, P.camy, lx, ly, ox, oy, ROVER_OCC_R)
         501 +                    blk |= seg_hits_disk(P.camx_i, P.camy_i, lx, ly, ox, oy, ROVER_OCC_R)
         502 +                ok = pending_mask & (G0 <= t) & ~blk
         503 +                G[ok] = t
         504 +                pending_mask &= ~ok
         505 +                if t >= len(other) - 1 and not ok.any() and (G0 <= t).all():
         506 +                    break
         507 +                t += 1
         508 +            F2 = propagate(G, P.free)
         509 +            if F2[P.home_reg].min() >= INF:
         510 +                continue
         511 +            st = stages[:-1] + [("send_t", None, G, F2)]
         512 +            new_actions[ri] = self._extract(P, st)
         513 +        return [self._schedule(costs[ri][2], new_actions[ri]) for ri in range(2)]
         514 +
         515 +    def _schedule(self, P, seq):
         516 +        """Attach headings; append waits so the rover can rotate back home."""
         517 +        home_th = P.th
         518 +        t_img = [t for t, a in enumerate(seq, 1) if a[2] and a[2][0] in ("cal", "img")]
         519 +        seq = list(seq)
         520 +        out = []
         521 +        if t_img:
         522 +            last = max(t_img)
         523 +            while len(seq) < last + P.nrot_out:
         524 +                x, y = (seq[-1][0], seq[-1][1])
         525 +                seq.append((x, y, None))
         526 +            T = len(seq)
         527 +            for t, (x, y, op) in enumerate(seq, 1):
         528 +                if t <= T - P.nrot_out:
         529 +                    h = approach_angle(P.cur_th, P.img_th, 0.4 * t)
         530 +                else:
         531 +                    h = approach_angle(P.img_th, home_th, 0.4 * (t - (T - P.nrot_out)))
         532 +                out.append((x, y, op, h))
         533 +        else:
         534 +            while len(seq) < rot_steps(P.cur_th, home_th):
         535 +                x, y = (seq[-1][0], seq[-1][1]) if seq else (float(P.xs[P.hi]), float(P.ys[P.hj]))
         536 +                seq.append((x, y, None))
         537 +            for t, (x, y, op) in enumerate(seq, 1):
         538 +                out.append((x, y, op, approach_angle(P.cur_th, home_th, 0.4 * t)))
         539 +        return out
         540 +
         541 +    def _extract(self, P, stages):
         542 +        """Backtrack through stage fields (waiting allowed); list of (x,y,op)."""
         543 +        k = len(stages) - 1
         544 +        Ff = np.where(P.home_reg, stages[k][3], INF)
         545 +        cell = np.unravel_index(int(np.argmin(Ff)), Ff.shape)
         546 +        cell = (int(cell[0]), int(cell[1]))
         547 +        v = int(stages[k][3][cell])
         548 +        seq = []
         549 +        W = WIN
         550 +        nx, ny = P.free.shape
         551 +
         552 +        def nb(Fsrc, i, j, cond):
         553 +            best = None
         554 +            for di in range(-W, W + 1):
         555 +                for dj in range(-W, W + 1):
         556 +                    a, b = i + di, j + dj
         557 +                    if 0 <= a < nx and 0 <= b < ny and cond(Fsrc[a, b]):
         558 +                        c = abs(di) + abs(dj)
         559 +                        if best is None or c < best[1]:
         560 +                            best = ((a, b), c)
         561 +            return best[0] if best else None
         562 +
         563 +        guard = 0
         564 +        while not (k == 0 and v == 0) and guard < 5000:
         565 +            guard += 1
         566 +            name, arg, G, F = stages[k]
         567 +            i, j = cell
         568 +            timed = name == "send_t"
         569 +            choice = None
         570 +            for mode in (0, 1):
         571 +                if k > 0:
         572 +                    okop = (G[cell] == v) if (mode == 0 or timed) else (G[cell] <= v)
         573 +                    if okop:
         574 +                        Fp = stages[k - 1][3]
         575 +                        c = nb(Fp, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
         576 +                        if c is not None:
         577 +                            choice = (c, (name.replace("_t", ""), arg), k - 1)
         578 +                            break
         579 +                c = nb(F, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
         580 +                if c is not None:
         581 +                    choice = (c, None, k)
         582 +                    break
         583 +            if choice is None:
         584 +                break
         585 +            seq.append((float(P.xs[cell[0]]), float(P.ys[cell[1]]), choice[1]))
         586 +            cell, k = choice[0], choice[2]
         587 +            v -= 1
         588 +        seq.reverse()
         589 +        return seq
         590 +
         591 +    # ------------------------------------------------------------------
         592 +    def get_action(self, state):
         593 +        act = np.zeros(8, dtype=np.float32)
         594 +        sc = Scene(state)
         595 +        if self._deviated(sc) or (not self.actions[0] and not self.actions[1]):
         596 +            self.replans += 1
         597 +            if self.replans < 40:
         598 +                self._plan(state)
         599 +        for ri in range(2):
         600 +            r = sc.rovers["rover%d" % ri]
         601 +            if self.actions[ri]:
         602 +                x, y, op, h = self.actions[ri].pop(0)
         603 +                dx = float(np.clip(x - r["x"], -0.2, 0.2))
         604 +                dy = float(np.clip(y - r["y"], -0.2, 0.2))
         605 +                act[4 * ri] = dx
         606 +                act[4 * ri + 1] = dy
         607 +                act[4 * ri + 3] = SEL[op[0]] if op else 0.0
         608 +                act[4 * ri + 2] = float(np.clip(_wrap(h - r["th"]), -0.4, 0.4))
         609 +                self.expect[ri] = (x, y, op, h)
         610 +            else:
         611 +                # at end: if at home do nothing
         612 +                self.expect[ri] = None
         613 +        return act
         614 +
         615 +    def _deviated(self, sc):
         616 +        dev = False
         617 +        for ri in range(2):
         618 +            e = self.expect[ri]
         619 +            if e is None:
         620 +                continue
         621 +            d0 = dev
         622 +            dev = False
         623 +            r = sc.rovers["rover%d" % ri]
         624 +            if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3 or \
         625 +                    abs(float(_wrap(r["th"] - e[3]))) > 1e-3:
         626 +                dev = True
         627 +                self.log.append(("move", ri, e, r["x"], r["y"]))
         628 +                self.bad[ri].append((e[0], e[1]))
         629 +            op, arg = e[2] if e[2] else (None, None)
         630 +            pr = self.prev_sc.rovers["rover%d" % ri]
         631 +            if op == "img":
         632 +                ob = sc.objectives[arg]
         633 +                if not ob["img"][ri]:
         634 +                    dev = True
         635 +            if op == "sample":
         636 +                if not any(s["an"][ri] for s in sc.samples if s["soil"] == (arg == "soil")):
         637 +                    dev = True
         638 +            if op == "cal" and not r["cal"]:
         639 +                dev = True
         640 +            elif op == "img" and (r["cal"] or not pr["cal"]):
         641 +                dev = True
         642 +            elif op == "sample" and not r["full"]:
         643 +                dev = True
         644 +            elif op == "drop" and r["full"]:
         645 +                dev = True
         646 +            elif op == "send":
         647 +                for ob in sc.objectives:
         648 +                    if ob["img"][ri] and not ob["recv"]:
         649 +                        dev = True
         650 +                for s in sc.samples:
         651 +                    if s["an"][ri] and not s["recv"]:
         652 +                        dev = True
         653 +            if dev:
         654 +                self.log.append(("dev", ri, e, round(r["x"], 3), round(r["y"], 3), r["cal"], pr["cal"],
         655 +                                 [ob["img"][ri] for ob in sc.objectives]))
         656 +            dev = dev or d0
         657 +        self.prev_sc = sc
         658 +        self.expect = [None, None]
         659 +        return dev
diff --git a/res_m.json b/res_m.json
new file mode 100644
index 0000000..8675399
--- /dev/null
+++ b/res_m.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 1.09, 2.5], [1, 2, true, 18, 0, 0.32, 2.3], [2, 3, true, 19, 0, 6.78, 7.7], [3, 3, true, 21, 0, 6.17, 6.4], [4, 3, true, 20, 0, 6.92, 8.0], [5, 3, true, 23, 0, 8.68, 9.2], [6, 2, true, 19, 0, 5.6, 5.8], [7, 3, true, 22, 0, 10.11, 10.5], [8, 3, true, 20, 0, 8.3, 8.6], [9, 2, true, 22, 0, 6.99, 7.1], [10, 3, true, 20, 0, 9.92, 10.9], [11, 1, true, 19, 0, 3.48, 3.9], [12, 2, true, 22, 0, 4.68, 4.8], [13, 3, true, 23, 0, 9.23, 9.3], [14, 1, true, 29, 0, 3.65, 3.9], [15, 3, true, 24, 0, 8.71, 10.9], [16, 2, true, 21, 0, 5.08, 5.3], [17, 3, true, 22, 0, 11.85, 13.4], [18, 3, true, 22, 0, 6.68, 7.1], [19, 2, true, 25, 0, 4.49, 5.8], [20, 3, true, 27, 0, 5.15, 7.1], [21, 1, true, 19, 0, 2.77, 3.6], [22, 3, true, 21, 0, 5.41, 5.8], [23, 1, true, 16, 0, 2.42, 3.9], [24, 2, true, 18, 0, 2.7, 3.1], [25, 2, true, 18, 0, 3.93, 4.9], [26, 3, true, 21, 0, 6.92, 8.6], [27, 1, true, 21, 0, 2.06, 3.8], [28, 2, true, 21, 0, 3.34, 4.0], [29, 3, true, 20, 0, 4.04, 5.1], [30, 1, true, 20, 0, 2.9, 3.1], [31, 2, true, 24, 0, 3.35, 5.9], [32, 3, true, 18, 0, 3.56, 5.3], [33, 3, true, 22, 0, 3.54, 7.8], [34, 1, true, 18, 0, 2.07, 3.0], [35, 1, true, 18, 0, 1.73, 3.4], [36, 2, true, 20, 0, 1.7, 5.3], [37, 1, true, 18, 0, 0.98, 4.5], [38, 1, true, 20, 0, 0.29, 3.4], [39, 3, true, 22, 0, 0.3, 5.1], [40, 2, true, 21, 0, 0.49, 4.3], [41, 2, true, 19, 0, 0.29, 3.6], [42, 1, true, 20, 0, 0.36, 4.6], [43, 2, true, 24, 0, 0.68, 4.6], [44, 3, true, 20, 0, 1.1, 4.3], [45, 3, true, 20, 0, 1.13, 4.2], [46, 2, true, 18, 0, 0.61, 3.6], [47, 1, true, 20, 0, 0.33, 3.4], [48, 1, true, 19, 0, 0.19, 2.6], [49, 1, true, 20, 0, 0.45, 3.1], [50, 3, true, 21, 0, 1.09, 5.0], [51, 2, true, 20, 0, 0.69, 4.3], [52, 3, true, 22, 0, 1.06, 4.4], [53, 3, true, 20, 0, 1.25, 4.6], [54, 1, true, 20, 0, 0.5, 3.9], [55, 3, true, 27, 0, 1.39, 5.5], [56, 2, true, 23, 0, 1.09, 5.7], [57, 1, true, 16, 0, 0.77, 3.6], [58, 2, true, 23, 0, 0.54, 5.4], [59, 3, true, 20, 0, 1.96, 6.3], [60, 1, true, 22, 0, 0.66, 4.7], [61, 2, true, 20, 0, 0.86, 5.0], [62, 2, true, 22, 0, 0.81, 5.3], [63, 2, true, 21, 0, 0.73, 4.7], [64, 2, true, 21, 0, 0.61, 5.3], [65, 1, true, 17, 0, 0.25, 4.4], [66, 3, true, 21, 0, 0.82, 5.4], [67, 3, true, 20, 0, 0.92, 5.2], [68, 2, true, 19, 0, 0.47, 4.1], [69, 1, true, 20, 0, 0.42, 5.1], [70, 2, true, 20, 0, 1.23, 5.6], [71, 3, true, 20, 0, 2.78, 6.2], [72, 3, true, 20, 0, 3.16, 6.2], [73, 3, true, 20, 0, 2.0, 5.4], [74, 1, true, 20, 0, 1.45, 4.0], [75, 2, true, 18, 0, 0.98, 3.4], [76, 2, true, 22, 0, 0.81, 3.9], [77, 1, true, 18, 0, 0.44, 3.6], [78, 3, true, 21, 0, 0.48, 5.0], [79, 1, true, 23, 0, 0.42, 4.4], [80, 3, true, 20, 0, 4.97, 5.6], [81, 1, true, 18, 0, 2.01, 3.6], [82, 3, true, 19, 0, 4.29, 4.7], [83, 3, true, 21, 0, 4.91, 5.5], [84, 2, true, 22, 0, 7.24, 8.2], [85, 3, true, 19, 0, 9.06, 11.4], [86, 3, true, 20, 0, 5.61, 5.8], [87, 2, true, 23, 0, 6.46, 9.4], [88, 2, true, 18, 0, 5.55, 7.4], [89, 3, true, 29, 0, 4.34, 5.5], [90, 2, true, 20, 0, 5.16, 8.3], [91, 3, true, 22, 0, 4.39, 7.6], [92, 2, true, 23, 0, 2.63, 6.7], [93, 3, true, 22, 0, 3.26, 7.1], [94, 1, true, 20, 0, 1.34, 4.7], [95, 2, true, 21, 0, 1.1, 5.3], [96, 3, true, 21, 0, 0.71, 5.7], [97, 1, true, 27, 0, 0.44, 5.3], [98, 2, true, 22, 0, 0.83, 5.0], [99, 3, true, 22, 0, 1.26, 6.9], [100, 3, true, 23, 0, 0.96, 5.6], [101, 1, true, 17, 0, 0.27, 3.6], [102, 2, true, 21, 0, 0.7, 5.2], [103, 2, true, 21, 0, 0.88, 6.7], [104, 3, true, 19, 0, 1.62, 6.2], [105, 1, true, 20, 0, 0.33, 5.4], [106, 2, true, 19, 0, 0.58, 5.1], [107, 1, true, 20, 0, 0.61, 6.6], [108, 1, true, 18, 0, 0.35, 5.5], [109, 2, true, 19, 0, 0.64, 5.6], [110, 2, true, 20, 0, 0.62, 6.7], [111, 2, true, 20, 0, 0.34, 7.2], [112, 1, true, 18, 0, 0.46, 5.3], [113, 1, true, 19, 0, 0.26, 5.4], [114, 1, true, 18, 0, 0.39, 5.0], [115, 2, true, 21, 0, 0.48, 3.8], [116, 1, true, 21, 0, 0.32, 2.8], [117, 1, true, 25, 0, 0.35, 2.7], [118, 2, true, 19, 0, 0.42, 1.5], [119, 2, true, 20, 0, 0.63, 0.9]]
\ No newline at end of file
```

</details>

<a id="C024"></a>
### C024 · fine-grid refinement of chosen stage sequences

Commit `aaffb63037a2669430a10bc9ac0a39155fb37674`; parents: f673e87ee7eac74d794df9f810d6d37c61b7ac51. Recorded author date: 2026-10-01T11:58:48+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E1074](01_timeline.md#E1074): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C024_aaffb63_approach.py) · [Exact all-file diff](evidence/diffs/C024_aaffb63.diff)

[Previous saved controller snapshot](evidence/versions/C023_f673e87_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0a4f791..6605853 100644
--- a/approach.py
+++ b/approach.py
@@ -24,6 +24,7 @@ SAMPLE_R = 0.246
   24     24  HOME_R = 0.235
   25     25  IMG_TH = -math.pi / 2
   26     26  ROT_IMG = 4.0
          27 +FINE_RES = 0.025
   27     28  PILLAR_INFL_OBJ = 0.015
   28     29  PILLAR_INFL_LAND = 0.04
   29     30  ROVER_OCC_R = 0.26
@@ -86,18 +87,18 @@ def box_dist(px, py, cx, cy, hx, hy):
   86     87      return np.hypot(ddx, ddy)
   87     88  
   88     89  
   89        -def propagate(f, free):
          90 +def propagate(f, free, win=WIN):
   90     91      f = np.where(free, f, INF)
   91     92      while True:
   92        -        m = minimum_filter(f, size=2 * WIN + 1, mode="constant", cval=INF) + 1
          93 +        m = minimum_filter(f, size=2 * win + 1, mode="constant", cval=INF) + 1
   93     94          nf = np.where(free, np.minimum(f, m), INF)
   94     95          if np.array_equal(nf, f):
   95     96              return f
   96     97          f = nf
   97     98  
   98     99  
   99        -def op_stage(fprev, region):
  100        -    m = minimum_filter(fprev, size=2 * WIN + 1, mode="constant", cval=INF) + 1
         100 +def op_stage(fprev, region, win=WIN):
         101 +    m = minimum_filter(fprev, size=2 * win + 1, mode="constant", cval=INF) + 1
  101    102      return np.where(region, np.minimum(m, INF), INF)
  102    103  
  103    104  
@@ -140,19 +141,23 @@ class Scene:
  140    141  class RoverPlanner:
  141    142      """Grid + regions for one rover."""
  142    143  
  143        -    def __init__(self, idx, home, scene, other_pos_list, cur_th=None, bad=(), img_th=None):
         144 +    def __init__(self, idx, home, scene, other_pos_list, cur_th=None, bad=(), img_th=None,
         145 +                 res=RES):
         146 +        self.ctor = (idx, home, scene, other_pos_list, cur_th, bad, img_th)
         147 +        self.res = res
         148 +        self.win = int(round(0.2 / res))
  144    149          self.idx = idx
  145    150          self.home = home  # (x, y, th)
  146    151          hx, hy, th = home
  147    152          self.th = th
  148    153          side = 1 if hx > 0 else -1
  149    154          lo_x, hi_x = (WALL_IN, ARENA) if side > 0 else (-ARENA, -WALL_IN)
  150        -        i0 = math.ceil((lo_x - hx) / RES - 1e-9)
  151        -        i1 = math.floor((hi_x - hx) / RES + 1e-9)
  152        -        j0 = math.ceil((-ARENA - hy) / RES - 1e-9)
  153        -        j1 = math.floor((ARENA - hy) / RES + 1e-9)
  154        -        self.xs = hx + RES * np.arange(i0, i1 + 1)
  155        -        self.ys = hy + RES * np.arange(j0, j1 + 1)
         155 +        i0 = math.ceil((lo_x - hx) / res - 1e-9)
         156 +        i1 = math.floor((hi_x - hx) / res + 1e-9)
         157 +        j0 = math.ceil((-ARENA - hy) / res - 1e-9)
         158 +        j1 = math.floor((ARENA - hy) / res + 1e-9)
         159 +        self.xs = hx + res * np.arange(i0, i1 + 1)
         160 +        self.ys = hy + res * np.arange(j0, j1 + 1)
  156    161          self.hi = -i0
  157    162          self.hj = -j0
  158    163          X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
@@ -256,8 +261,8 @@ class RoverPlanner:
  256    261              self.sreg[kind] = r & free
  257    262  
  258    263      def cell_of(self, x, y):
  259        -        i = int(round((x - self.xs[0]) / RES))
  260        -        j = int(round((y - self.ys[0]) / RES))
         264 +        i = int(round((x - self.xs[0]) / self.res))
         265 +        j = int(round((y - self.ys[0]) / self.res))
  261    266          i = min(max(i, 0), len(self.xs) - 1)
  262    267          j = min(max(j, 0), len(self.ys) - 1)
  263    268          return i, j
@@ -326,11 +331,11 @@ class GeneratedApproach:
  326    331          f0 = np.full(P.free.shape, INF, dtype=np.int64)
  327    332          f0[start] = 0
  328    333          stages0 = []
  329        -        F = propagate(f0, P.free)
         334 +        F = propagate(f0, P.free, P.win)
  330    335          stages0.append(("start", None, f0, F))
  331    336          if r["full"]:
  332        -            G = op_stage(F, P.free)
  333        -            F = propagate(G, P.free)
         337 +            G = op_stage(F, P.free, P.win)
         338 +            F = propagate(G, P.free, P.win)
  334    339              stages0.append(("drop", None, G, F))
  335    340          imaged0 = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
  336    341          tasks = []
@@ -349,8 +354,8 @@ class GeneratedApproach:
  349    354                  cost = F[P.home_reg].min()
  350    355                  st = stages
  351    356              else:
  352        -                G = op_stage(F, P.land)
  353        -                F2 = propagate(G, P.free)
         357 +                G = op_stage(F, P.land, P.win)
         358 +                F2 = propagate(G, P.free, P.win)
  354    359                  cost = F2[P.home_reg].min()
  355    360                  st = stages + [("send", None, G, F2)]
  356    361              if cost >= INF:
@@ -372,21 +377,21 @@ class GeneratedApproach:
  372    377                      st = list(stages)
  373    378                      Fc = F
  374    379                      if not cal:
  375        -                        G = op_stage(F, P.any_vis)
         380 +                        G = op_stage(F, P.any_vis, P.win)
  376    381                          G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
  377        -                        Fc = propagate(G, P.free)
         382 +                        Fc = propagate(G, P.free, P.win)
  378    383                          st.append(("cal", None, G, Fc))
  379    384                      reg = P.img_region(k, imaged)
  380        -                    G = op_stage(Fc, reg)
         385 +                    G = op_stage(Fc, reg, P.win)
  381    386                      G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
  382        -                    Fi = propagate(G, P.free)
         387 +                    Fi = propagate(G, P.free, P.win)
  383    388                      st.append(("img", k, G, Fi))
  384    389                      dfs(Fi, st, done_keys | {key}, imaged | {k}, False)
  385    390                  else:
  386        -                    G = op_stage(F, P.sreg[t[0]])
  387        -                    Fs = propagate(G, P.free)
  388        -                    G2 = op_stage(Fs, P.free)
  389        -                    Fd = propagate(G2, P.free)
         391 +                    G = op_stage(F, P.sreg[t[0]], P.win)
         392 +                    Fs = propagate(G, P.free, P.win)
         393 +                    G2 = op_stage(Fs, P.free, P.win)
         394 +                    Fd = propagate(G2, P.free, P.win)
  390    395                      st = stages + [("sample", t[0], G, Fs), ("drop", None, G2, Fd)]
  391    396                      dfs(Fd, st, done_keys | {key}, imaged, cal)
  392    397  
@@ -467,7 +472,48 @@ class GeneratedApproach:
  467    472                  bestreal = (real, acts)
  468    473          self.actions = bestreal[1]
  469    474  
         475 +    def _refine(self, entry):
         476 +        """Replay a coarse stage sequence on a fine grid."""
         477 +        cost, stages, Pc = entry
         478 +        if FINE_RES is None or FINE_RES >= Pc.res:
         479 +            return entry
         480 +        ri = Pc.ctor[0]
         481 +        P = RoverPlanner(*Pc.ctor, res=FINE_RES)
         482 +        sc = self.scene
         483 +        r = sc.rovers["rover%d" % ri]
         484 +        imaged = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
         485 +        start = P.cell_of(r["x"], r["y"])
         486 +        P.free[start] = True
         487 +        out = []
         488 +        F = None
         489 +        for name, arg, _, _ in stages:
         490 +            if name == "start":
         491 +                G = np.full(P.free.shape, INF, dtype=np.int64)
         492 +                G[start] = 0
         493 +            elif name == "drop":
         494 +                G = op_stage(F, P.free, P.win)
         495 +            elif name == "cal":
         496 +                G = op_stage(F, P.any_vis, P.win)
         497 +                G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
         498 +            elif name == "img":
         499 +                G = op_stage(F, P.img_region(arg, imaged), P.win)
         500 +                G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
         501 +                imaged = imaged | {arg}
         502 +            elif name == "sample":
         503 +                G = op_stage(F, P.sreg[arg], P.win)
         504 +            elif name == "send":
         505 +                G = op_stage(F, P.land, P.win)
         506 +            else:
         507 +                return entry
         508 +            F = propagate(G, P.free, P.win)
         509 +            out.append((name, arg, G, F))
         510 +        c = F[P.home_reg].min()
         511 +        if c >= INF:
         512 +            return entry
         513 +        return (int(c), out, P)
         514 +
  470    515      def _realize(self, sc, tabs, costs):
         516 +        costs = [self._refine(costs[0]), self._refine(costs[1])]
  471    517          best = (None, costs)
  472    518          actions = [[], []]
  473    519          sc = self.scene
@@ -486,7 +532,7 @@ class GeneratedApproach:
  486    532                  continue
  487    533              P = costs[ri][2]
  488    534              Fprev = stages[-2][3]
  489        -            G0 = op_stage(Fprev, P.land_free)
         535 +            G0 = op_stage(Fprev, P.land_free, P.win)
  490    536              other = trajs[1 - ri]
  491    537              G = np.full(G0.shape, INF, dtype=G0.dtype)
  492    538              pending_mask = G0 < INF
@@ -505,7 +551,7 @@ class GeneratedApproach:
  505    551                  if t >= len(other) - 1 and not ok.any() and (G0 <= t).all():
  506    552                      break
  507    553                  t += 1
  508        -            F2 = propagate(G, P.free)
         554 +            F2 = propagate(G, P.free, P.win)
  509    555              if F2[P.home_reg].min() >= INF:
  510    556                  continue
  511    557              st = stages[:-1] + [("send_t", None, G, F2)]
@@ -546,7 +592,7 @@ class GeneratedApproach:
  546    592          cell = (int(cell[0]), int(cell[1]))
  547    593          v = int(stages[k][3][cell])
  548    594          seq = []
  549        -        W = WIN
         595 +        W = P.win
  550    596          nx, ny = P.free.shape
  551    597  
  552    598          def nb(Fsrc, i, j, cond):
diff --git a/approach_fine.py b/approach_fine.py
index e81cbd7..65af559 100644
--- a/approach_fine.py
+++ b/approach_fine.py
@@ -16,12 +16,14 @@ WALL_IN = 0.2271 + 0.004
   16     16  ARENA = 2.2729 - 0.004
   17     17  PILLAR_R = 0.245
   18     18  MOUND_R = 0.185
   19        -LANDER_XMIN = -1.195
   20        -LANDER_YMIN = -1.455
   21        -OBJ_RANGE = 1.985
   22        -LANDER_RANGE = 3.985
   23        -SAMPLE_R = 0.242
   24        -HOME_R = 0.22
          19 +LANDER_XMIN = -1.15
          20 +LANDER_YMIN = -1.42
          21 +OBJ_RANGE = 1.993
          22 +LANDER_RANGE = 3.995
          23 +SAMPLE_R = 0.246
          24 +HOME_R = 0.235
          25 +IMG_TH = -math.pi / 2
          26 +ROT_IMG = 4.0
   25     27  PILLAR_INFL_OBJ = 0.015
   26     28  PILLAR_INFL_LAND = 0.04
   27     29  ROVER_OCC_R = 0.26
@@ -36,6 +38,18 @@ def _wrap(a):
   36     38      return (a + np.pi) % (2 * np.pi) - np.pi
   37     39  
   38     40  
          41 +def rot_steps(a, b):
          42 +    d = abs(float(_wrap(b - a)))
          43 +    return int(math.ceil(d / 0.4 - 1e-6))
          44 +
          45 +
          46 +def approach_angle(a, b, dmax):
          47 +    d = float(_wrap(b - a))
          48 +    if abs(d) <= dmax:
          49 +        return float(_wrap(b))
          50 +    return float(_wrap(a + math.copysign(dmax, d)))
          51 +
          52 +
   39     53  def seg_hits_box(px, py, qx, qy, cx, cy, hx, hy):
   40     54      """Vectorised: does segment p->q (p arrays, q scalar) intersect AABB?"""
   41     55      dx = qx - px
@@ -126,7 +140,7 @@ class Scene:
  126    140  class RoverPlanner:
  127    141      """Grid + regions for one rover."""
  128    142  
  129        -    def __init__(self, idx, home, scene, other_pos_list):
         143 +    def __init__(self, idx, home, scene, other_pos_list, cur_th=None, bad=(), img_th=None):
  130    144          self.idx = idx
  131    145          self.home = home  # (x, y, th)
  132    146          hx, hy, th = home
@@ -149,6 +163,8 @@ class RoverPlanner:
  149    163          for (cx, cy, ax, ay) in scene.mounds:
  150    164              free &= box_dist(X, Y, cx, cy, ax, ay) > MOUND_R
  151    165          free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
         166 +        for (bx, by) in bad:
         167 +            free &= np.hypot(X - bx, Y - by) > 0.03
  152    168          free[self.hi, self.hj] = True
  153    169          self.free = free
  154    170          self.home_reg = (np.hypot(X - hx, Y - hy) <= HOME_R) & free
@@ -157,51 +173,75 @@ class RoverPlanner:
  157    173          self.camx = X + c * CAM_OFF[0] - s * CAM_OFF[1]
  158    174          self.camy = Y + s * CAM_OFF[0] + c * CAM_OFF[1]
  159    175          self.scene = scene
         176 +        ith = th if img_th is None else img_th
         177 +        self.img_th = ith
         178 +        cur = th if cur_th is None else cur_th
         179 +        self.cur_th = cur
         180 +        self.nrot_in = rot_steps(cur, ith)
         181 +        self.nrot_out = rot_steps(ith, th)
         182 +        hs = [cur, ith, th]
         183 +        for k in range(1, 9):
         184 +            hs.append(approach_angle(cur, ith, 0.4 * k))
         185 +            hs.append(approach_angle(ith, th, 0.4 * k))
         186 +            hs.append(approach_angle(cur, th, 0.4 * k))
         187 +        self.headings = hs
         188 +        ci, si = math.cos(ith), math.sin(ith)
         189 +        camx_i = X + ci * CAM_OFF[0] - si * CAM_OFF[1]
         190 +        camy_i = Y + si * CAM_OFF[0] + ci * CAM_OFF[1]
  160    191          # objective visibility
  161    192          self.vis = []
  162    193          self.objd = []
  163    194          for ob in scene.objectives:
  164    195              ox, oy = ob["x"], ob["y"]
  165        -            d = np.hypot(ox - self.camx, oy - self.camy)
         196 +            d = np.hypot(ox - camx_i, oy - camy_i)
  166    197              v = (d <= OBJ_RANGE)
  167    198              occ = np.zeros(X.shape, dtype=bool)
  168    199              for (cx, cy, ax, ay) in scene.pillars:
  169    200                  e = PILLAR_INFL_OBJ
  170        -                occ |= seg_hits_box(self.camx, self.camy, ox, oy, cx, cy, ax + e, ay + e)
         201 +                occ |= seg_hits_box(camx_i, camy_i, ox, oy, cx, cy, ax + e, ay + e)
  171    202                  occ |= seg_hits_box(X, Y, ox, oy, cx, cy, ax + e, ay + e)
  172    203              if USE_BACK_OBJ:
  173        -                rel = np.abs(_wrap(np.arctan2(oy - Y, ox - X) - th))
         204 +                rel = np.abs(_wrap(np.arctan2(oy - Y, ox - X) - ith))
  174    205                  back = rel > math.radians(OBJ_BACK_DEG)
  175    206              else:
  176    207                  back = np.zeros(X.shape, dtype=bool)
  177    208              occ2 = np.zeros(X.shape, dtype=bool)
  178    209              for (px, py) in other_pos_list:
  179        -                occ2 |= seg_hits_disk(self.camx, self.camy, ox, oy, px, py, ROVER_OCC_R)
         210 +                occ2 |= seg_hits_disk(camx_i, camy_i, ox, oy, px, py, ROVER_OCC_R)
  180    211              self.vis.append(v & ((~occ) | back) & ~occ2 & free)
  181    212              self.objd.append(d)
  182    213          self.any_vis = np.zeros(X.shape, dtype=bool)
  183    214          for v in self.vis:
  184    215              self.any_vis |= v
  185        -        # lander visibility
         216 +        # lander visibility (must hold for every heading along the rotation path)
  186    217          lx, ly = scene.lander
  187        -        v = (np.hypot(lx - X, ly - Y) <= LANDER_RANGE) & \
  188        -            (np.hypot(lx - self.camx, ly - self.camy) <= LANDER_RANGE)
  189        -        occ = np.zeros(X.shape, dtype=bool)
  190        -        for (cx, cy, ax, ay) in scene.pillars:
  191        -            e = PILLAR_INFL_LAND
  192        -            occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
  193        -            occ |= seg_hits_box(self.camx, self.camy, lx, ly, cx, cy, ax + e, ay + e)
  194        -        if USE_BACK_LAND:
  195        -            rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - th))
  196        -            back = rel > math.radians(LAND_BACK_DEG)
  197        -        else:
  198        -            back = np.zeros(X.shape, dtype=bool)
  199        -        occ2 = np.zeros(X.shape, dtype=bool)
  200        -        for (px, py) in other_pos_list:
  201        -            occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
  202        -            occ2 |= seg_hits_disk(self.camx, self.camy, lx, ly, px, py, ROVER_OCC_R)
  203        -        self.land = v & ((~occ) | back) & ~occ2 & free
  204        -        self.land_free = v & ((~occ) | back) & free
         218 +        land = free.copy()
         219 +        land_free = free.copy()
         220 +        for hh in self.headings:
         221 +            ch, sh = math.cos(hh), math.sin(hh)
         222 +            cx_ = X + ch * CAM_OFF[0] - sh * CAM_OFF[1]
         223 +            cy_ = Y + sh * CAM_OFF[0] + ch * CAM_OFF[1]
         224 +            v = (np.hypot(lx - X, ly - Y) <= LANDER_RANGE) & \
         225 +                (np.hypot(lx - cx_, ly - cy_) <= LANDER_RANGE)
         226 +            occ = np.zeros(X.shape, dtype=bool)
         227 +            for (cx, cy, ax, ay) in scene.pillars:
         228 +                e = PILLAR_INFL_LAND
         229 +                occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
         230 +                occ |= seg_hits_box(cx_, cy_, lx, ly, cx, cy, ax + e, ay + e)
         231 +            if USE_BACK_LAND:
         232 +                rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - hh))
         233 +                back = rel > math.radians(LAND_BACK_DEG)
         234 +            else:
         235 +                back = np.zeros(X.shape, dtype=bool)
         236 +            occ2 = np.zeros(X.shape, dtype=bool)
         237 +            for (px, py) in other_pos_list:
         238 +                occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
         239 +                occ2 |= seg_hits_disk(cx_, cy_, lx, ly, px, py, ROVER_OCC_R)
         240 +            land &= v & ((~occ) | back) & ~occ2
         241 +            land_free &= v & ((~occ) | back)
         242 +        self.land = land
         243 +        self.land_free = land_free
         244 +        self.camx_i, self.camy_i = camx_i, camy_i
  205    245          # samples
  206    246          self.sreg = {}
  207    247          dk = {}
@@ -249,6 +289,7 @@ class GeneratedApproach:
  249    289          self.expect = [None, None]
  250    290          self.prev_sc = sc
  251    291          self.log = []
         292 +        self.bad = [[], []]
  252    293          self._plan(state)
  253    294  
  254    295      # ------------------------------------------------------------------
@@ -260,7 +301,25 @@ class GeneratedApproach:
  260    301          occl = [(ohome[0], ohome[1])]
  261    302          if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
  262    303              occl.append((other["x"], other["y"]))
  263        -        P = RoverPlanner(ri, self.homes[name], sc, occl)
         304 +        merged = {}
         305 +        hth = self.homes[name][2]
         306 +        if IMG_TH is None:
         307 +            ths = [hth]
         308 +        else:
         309 +            d = float(_wrap(IMG_TH - hth))
         310 +            ths = [float(_wrap(hth + math.copysign(min(abs(d), ROT_IMG), d)))]
         311 +        for ith in ths:
         312 +            P, table = self._rover_tables_h(ri, sc, need_objs, need_stone, need_soil,
         313 +                                            pending, occl, ith)
         314 +            for k, (c, st) in table.items():
         315 +                if k not in merged or c < merged[k][0]:
         316 +                    merged[k] = (c, st, P)
         317 +        return None, merged
         318 +
         319 +    def _rover_tables_h(self, ri, sc, need_objs, need_stone, need_soil, pending, occl, ith):
         320 +        name = "rover%d" % ri
         321 +        r = sc.rovers[name]
         322 +        P = RoverPlanner(ri, self.homes[name], sc, occl, r["th"], self.bad[ri], ith)
  264    323          self_planner = P
  265    324          start = P.cell_of(r["x"], r["y"])
  266    325          P.free[start] = True
@@ -314,10 +373,12 @@ class GeneratedApproach:
  314    373                      Fc = F
  315    374                      if not cal:
  316    375                          G = op_stage(F, P.any_vis)
         376 +                        G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
  317    377                          Fc = propagate(G, P.free)
  318    378                          st.append(("cal", None, G, Fc))
  319    379                      reg = P.img_region(k, imaged)
  320    380                      G = op_stage(Fc, reg)
         381 +                    G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
  321    382                      Fi = propagate(G, P.free)
  322    383                      st.append(("img", k, G, Fi))
  323    384                      dfs(Fi, st, done_keys | {key}, imaged | {k}, False)
@@ -411,7 +472,7 @@ class GeneratedApproach:
  411    472          actions = [[], []]
  412    473          sc = self.scene
  413    474          for ri in range(2):
  414        -            P = tabs[ri][0]
         475 +            P = costs[ri][2]
  415    476              actions[ri] = self._extract(P, best[1][ri][1])
  416    477          # time-aware re-plan of final send against other rover's trajectory
  417    478          trajs = []
@@ -423,7 +484,7 @@ class GeneratedApproach:
  423    484              stages = best[1][ri][1]
  424    485              if stages[-1][0] != "send":
  425    486                  continue
  426        -            P = tabs[ri][0]
         487 +            P = costs[ri][2]
  427    488              Fprev = stages[-2][3]
  428    489              G0 = op_stage(Fprev, P.land_free)
  429    490              other = trajs[1 - ri]
@@ -437,6 +498,7 @@ class GeneratedApproach:
  437    498                  for tt in (t - 1, t):
  438    499                      ox, oy = other[max(0, min(tt, len(other) - 1))]
  439    500                      blk |= seg_hits_disk(P.camx, P.camy, lx, ly, ox, oy, ROVER_OCC_R)
         501 +                    blk |= seg_hits_disk(P.camx_i, P.camy_i, lx, ly, ox, oy, ROVER_OCC_R)
  440    502                  ok = pending_mask & (G0 <= t) & ~blk
  441    503                  G[ok] = t
  442    504                  pending_mask &= ~ok
@@ -448,7 +510,33 @@ class GeneratedApproach:
  448    510                  continue
  449    511              st = stages[:-1] + [("send_t", None, G, F2)]
  450    512              new_actions[ri] = self._extract(P, st)
  451        -        return new_actions
         513 +        return [self._schedule(costs[ri][2], new_actions[ri]) for ri in range(2)]
         514 +
         515 +    def _schedule(self, P, seq):
         516 +        """Attach headings; append waits so the rover can rotate back home."""
         517 +        home_th = P.th
         518 +        t_img = [t for t, a in enumerate(seq, 1) if a[2] and a[2][0] in ("cal", "img")]
         519 +        seq = list(seq)
         520 +        out = []
         521 +        if t_img:
         522 +            last = max(t_img)
         523 +            while len(seq) < last + P.nrot_out:
         524 +                x, y = (seq[-1][0], seq[-1][1])
         525 +                seq.append((x, y, None))
         526 +            T = len(seq)
         527 +            for t, (x, y, op) in enumerate(seq, 1):
         528 +                if t <= T - P.nrot_out:
         529 +                    h = approach_angle(P.cur_th, P.img_th, 0.4 * t)
         530 +                else:
         531 +                    h = approach_angle(P.img_th, home_th, 0.4 * (t - (T - P.nrot_out)))
         532 +                out.append((x, y, op, h))
         533 +        else:
         534 +            while len(seq) < rot_steps(P.cur_th, home_th):
         535 +                x, y = (seq[-1][0], seq[-1][1]) if seq else (float(P.xs[P.hi]), float(P.ys[P.hj]))
         536 +                seq.append((x, y, None))
         537 +            for t, (x, y, op) in enumerate(seq, 1):
         538 +                out.append((x, y, op, approach_angle(P.cur_th, home_th, 0.4 * t)))
         539 +        return out
  452    540  
  453    541      def _extract(self, P, stages):
  454    542          """Backtrack through stage fields (waiting allowed); list of (x,y,op)."""
@@ -511,13 +599,14 @@ class GeneratedApproach:
  511    599          for ri in range(2):
  512    600              r = sc.rovers["rover%d" % ri]
  513    601              if self.actions[ri]:
  514        -                x, y, op = self.actions[ri].pop(0)
         602 +                x, y, op, h = self.actions[ri].pop(0)
  515    603                  dx = float(np.clip(x - r["x"], -0.2, 0.2))
  516    604                  dy = float(np.clip(y - r["y"], -0.2, 0.2))
  517    605                  act[4 * ri] = dx
  518    606                  act[4 * ri + 1] = dy
  519    607                  act[4 * ri + 3] = SEL[op[0]] if op else 0.0
  520        -                self.expect[ri] = (x, y, op)
         608 +                act[4 * ri + 2] = float(np.clip(_wrap(h - r["th"]), -0.4, 0.4))
         609 +                self.expect[ri] = (x, y, op, h)
  521    610              else:
  522    611                  # at end: if at home do nothing
  523    612                  self.expect[ri] = None
@@ -532,9 +621,11 @@ class GeneratedApproach:
  532    621              d0 = dev
  533    622              dev = False
  534    623              r = sc.rovers["rover%d" % ri]
  535        -            if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3:
         624 +            if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3 or \
         625 +                    abs(float(_wrap(r["th"] - e[3]))) > 1e-3:
  536    626                  dev = True
  537    627                  self.log.append(("move", ri, e, r["x"], r["y"]))
         628 +                self.bad[ri].append((e[0], e[1]))
  538    629              op, arg = e[2] if e[2] else (None, None)
  539    630              pr = self.prev_sc.rovers["rover%d" % ri]
  540    631              if op == "img":
diff --git a/res_fine2.json b/res_fine2.json
new file mode 100644
index 0000000..b6f13f9
--- /dev/null
+++ b/res_fine2.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 2.74, 3.5], [1, 2, true, 18, 0, 4.17, 4.3], [2, 3, true, 19, 0, 12.68, 12.8], [3, 3, true, 21, 0, 10.5, 10.6], [4, 3, true, 20, 0, 13.26, 13.4], [5, 3, true, 23, 0, 12.62, 12.8], [6, 2, true, 19, 0, 9.38, 9.7], [7, 3, true, 22, 0, 15.95, 16.3], [8, 3, true, 20, 0, 12.88, 13.0], [9, 2, true, 21, 0, 8.58, 9.0], [10, 3, true, 20, 0, 13.79, 13.9], [11, 1, true, 19, 0, 5.48, 5.6], [12, 2, true, 22, 0, 7.29, 7.6], [13, 3, true, 23, 0, 12.48, 12.6], [14, 1, true, 29, 0, 5.58, 5.7], [15, 3, true, 23, 0, 11.84, 13.4], [16, 2, true, 21, 0, 6.96, 7.1], [17, 3, true, 22, 0, 15.28, 15.5], [18, 3, true, 21, 0, 8.05, 8.3], [19, 2, true, 23, 0, 6.27, 7.1], [20, 3, true, 27, 0, 6.62, 8.0], [21, 1, true, 19, 0, 4.38, 5.6], [22, 3, true, 21, 0, 8.53, 8.6], [23, 1, true, 16, 0, 5.01, 5.1], [24, 2, true, 18, 0, 4.92, 5.0], [25, 2, true, 18, 0, 6.02, 6.2], [26, 3, true, 21, 0, 11.31, 13.0], [27, 1, true, 21, 0, 3.31, 3.5], [28, 2, true, 21, 0, 5.3, 5.4], [29, 3, true, 20, 0, 7.86, 8.8], [30, 1, true, 20, 0, 6.53, 6.6], [31, 2, true, 24, 0, 6.52, 9.0], [32, 3, true, 18, 0, 6.74, 10.6], [33, 3, true, 22, 0, 6.42, 11.5], [34, 1, true, 18, 0, 4.53, 5.4], [35, 1, true, 18, 0, 4.34, 5.2], [36, 2, true, 20, 0, 1.52, 5.9], [37, 1, true, 18, 0, 0.77, 5.1], [38, 1, true, 19, 0, 2.2, 5.7], [39, 3, true, 23, 0, 1.97, 7.2], [40, 2, true, 21, 0, 1.42, 4.8], [41, 2, true, 18, 0, 1.7, 5.0], [42, 1, true, 20, 0, 1.33, 5.2], [43, 2, true, 24, 0, 2.85, 5.3], [44, 3, true, 19, 0, 4.25, 4.7], [45, 3, true, 20, 0, 5.92, 6.1], [46, 2, true, 18, 0, 5.27, 6.6], [47, 1, true, 20, 0, 4.2, 4.9], [48, 1, true, 19, 0, 4.3, 5.4], [49, 1, true, 20, 0, 5.93, 6.1], [50, 3, true, 21, 0, 14.27, 14.9], [51, 2, true, 20, 0, 7.09, 7.2], [52, 3, true, 22, 0, 8.33, 8.5], [53, 3, true, 20, 0, 13.56, 14.4], [54, 1, true, 20, 0, 6.39, 6.8], [55, 3, true, 26, 0, 21.02, 24.2], [56, 2, true, 22, 0, 10.07, 11.0], [57, 1, true, 16, 0, 7.11, 7.2], [58, 2, true, 23, 0, 8.61, 9.3], [59, 3, true, 20, 0, 16.49, 19.5], [60, 1, true, 22, 0, 6.47, 6.8], [61, 2, true, 19, 0, 6.57, 6.7], [62, 2, true, 21, 0, 9.29, 11.1], [63, 2, true, 21, 0, 9.19, 11.5], [64, 2, true, 21, 0, 7.43, 7.6], [65, 1, true, 16, 0, 7.19, 8.0], [66, 3, true, 21, 0, 7.47, 11.2], [67, 3, true, 20, 0, 5.66, 8.3], [68, 2, true, 19, 0, 1.94, 4.3], [69, 1, true, 20, 0, 1.15, 4.8], [70, 2, true, 19, 0, 2.65, 5.2], [71, 3, true, 20, 0, 9.27, 10.0], [72, 3, true, 20, 0, 9.68, 10.0], [73, 3, true, 20, 0, 5.37, 5.6], [74, 1, true, 20, 0, 5.54, 5.7], [75, 2, true, 17, 0, 7.97, 8.1], [76, 2, true, 22, 0, 8.08, 8.7], [77, 1, true, 18, 0, 5.05, 5.2], [78, 3, true, 20, 0, 8.04, 8.2], [79, 1, true, 23, 0, 5.92, 6.1], [80, 3, true, 20, 0, 17.86, 18.0], [81, 1, true, 18, 0, 6.94, 7.1], [82, 3, true, 19, 0, 9.78, 9.9], [83, 3, true, 21, 0, 10.24, 10.4], [84, 2, true, 22, 0, 9.93, 10.6], [85, 3, true, 19, 0, 16.0, 16.1], [86, 3, true, 20, 0, 9.65, 9.9], [87, 2, true, 23, 0, 11.43, 11.6], [88, 2, true, 18, 0, 9.23, 9.4], [89, 3, true, 29, 0, 6.26, 6.8], [90, 2, true, 20, 0, 9.61, 10.3], [91, 3, true, 22, 0, 7.05, 7.2], [92, 2, true, 22, 0, 7.94, 8.2], [93, 3, true, 22, 0, 12.12, 12.9], [94, 1, true, 20, 0, 7.59, 7.7], [95, 2, true, 19, 0, 9.8, 10.5], [96, 3, true, 21, 0, 9.34, 9.5], [97, 1, true, 27, 0, 7.49, 7.7], [98, 2, true, 22, 0, 7.4, 8.1], [99, 3, true, 22, 0, 8.91, 9.8], [100, 3, true, 23, 0, 8.22, 8.5], [101, 1, true, 17, 0, 3.98, 5.2], [102, 2, true, 20, 0, 6.87, 8.0], [103, 2, true, 21, 0, 5.26, 5.5], [104, 3, true, 19, 0, 11.04, 11.2], [105, 1, true, 20, 0, 3.51, 3.8], [106, 2, true, 19, 0, 5.48, 5.7], [107, 1, true, 20, 0, 6.23, 6.4], [108, 1, true, 19, 0, 5.93, 6.4], [109, 2, true, 19, 0, 7.89, 8.5], [110, 2, true, 20, 0, 7.92, 8.7], [111, 2, true, 20, 0, 4.97, 5.5], [112, 1, true, 18, 0, 5.93, 7.6], [113, 1, true, 19, 0, 3.86, 4.7], [114, 1, true, 18, 0, 4.89, 5.3], [115, 2, true, 21, 0, 4.72, 4.9], [116, 1, true, 21, 0, 3.0, 3.3], [117, 1, true, 24, 0, 2.8, 3.0], [118, 2, true, 19, 0, 2.39, 2.6], [119, 2, true, 20, 0, 2.75, 2.9]]
\ No newline at end of file
```

</details>

<a id="C025"></a>
### C025 · fine planner cache; time guards

Commit `dbc525a1bb8ae106d6c54dad4ef4bb5b69d74e80`; parents: aaffb63037a2669430a10bc9ac0a39155fb37674. Recorded author date: 2026-10-01T12:01:57+02:00.

File roles (automatic): policy, setup/other.

- [E1085](01_timeline.md#E1085): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C025_dbc525a_approach.py) · [Exact all-file diff](evidence/diffs/C025_dbc525a.diff)

[Previous saved controller snapshot](evidence/versions/C024_aaffb63_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6605853..97d0449 100644
--- a/approach.py
+++ b/approach.py
@@ -295,6 +295,8 @@ class GeneratedApproach:
  295    295          self.prev_sc = sc
  296    296          self.log = []
  297    297          self.bad = [[], []]
         298 +        import time as _t
         299 +        self.t_start = _t.time()
  298    300          self._plan(state)
  299    301  
  300    302      # ------------------------------------------------------------------
@@ -399,6 +401,9 @@ class GeneratedApproach:
  399    401          return P, table
  400    402  
  401    403      def _plan(self, state):
         404 +        import time as _t
         405 +        self._fine_cache = {}
         406 +        self._fast = (_t.time() - self.t_start) > 20.0
  402    407          sc = Scene(state)
  403    408          self.scene = sc
  404    409          # what is needed
@@ -475,10 +480,17 @@ class GeneratedApproach:
  475    480      def _refine(self, entry):
  476    481          """Replay a coarse stage sequence on a fine grid."""
  477    482          cost, stages, Pc = entry
  478        -        if FINE_RES is None or FINE_RES >= Pc.res:
         483 +        if FINE_RES is None or FINE_RES >= Pc.res or self._fast:
  479    484              return entry
  480    485          ri = Pc.ctor[0]
  481        -        P = RoverPlanner(*Pc.ctor, res=FINE_RES)
         486 +        ck = (ri, Pc.img_th)
         487 +        if ck in self._fine_cache:
         488 +            P = self._fine_cache[ck]
         489 +            P.free = P.free0.copy()
         490 +        else:
         491 +            P = RoverPlanner(*Pc.ctor, res=FINE_RES)
         492 +            P.free0 = P.free.copy()
         493 +            self._fine_cache[ck] = P
  482    494          sc = self.scene
  483    495          r = sc.rovers["rover%d" % ri]
  484    496          imaged = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
@@ -640,7 +652,8 @@ class GeneratedApproach:
  640    652          sc = Scene(state)
  641    653          if self._deviated(sc) or (not self.actions[0] and not self.actions[1]):
  642    654              self.replans += 1
  643        -            if self.replans < 40:
         655 +            import time as _t
         656 +            if self.replans < 60 and (_t.time() - self.t_start) < 45.0:
  644    657                  self._plan(state)
  645    658          for ri in range(2):
  646    659              r = sc.rovers["rover%d" % ri]
diff --git a/prof.out b/prof.out
index cd1aa12..a8cf78d 100644
Binary files a/prof.out and b/prof.out differ
diff --git a/res_ref.json b/res_ref.json
new file mode 100644
index 0000000..e2538be
--- /dev/null
+++ b/res_ref.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 4.74, 4.9], [1, 2, true, 18, 0, 8.6, 8.7], [2, 3, true, 19, 0, 13.17, 13.4], [3, 3, true, 21, 0, 10.97, 11.2], [4, 3, true, 20, 0, 11.5, 11.6], [5, 3, true, 23, 0, 12.92, 13.5], [6, 2, true, 19, 0, 11.39, 11.7], [7, 3, true, 22, 0, 13.84, 14.3], [8, 3, true, 20, 0, 11.3, 11.4], [9, 2, true, 22, 0, 11.17, 11.4], [10, 3, true, 20, 0, 14.42, 14.6], [11, 1, true, 19, 0, 7.42, 7.5], [12, 2, true, 22, 0, 9.08, 9.2], [13, 3, true, 23, 0, 14.98, 15.1], [14, 1, true, 29, 0, 8.47, 9.0], [15, 3, true, 23, 0, 14.39, 14.6], [16, 2, true, 21, 0, 10.58, 10.7], [17, 3, true, 22, 0, 16.61, 16.9], [18, 3, true, 22, 0, 10.81, 10.9], [19, 2, true, 25, 0, 7.5, 7.6], [20, 3, true, 27, 0, 9.66, 10.6], [21, 1, true, 19, 0, 8.42, 8.6], [22, 3, true, 21, 0, 11.53, 12.1], [23, 1, true, 16, 0, 8.0, 8.1], [24, 2, true, 18, 0, 7.6, 8.2], [25, 2, true, 18, 0, 10.13, 10.2], [26, 3, true, 21, 0, 13.0, 13.1], [27, 1, true, 21, 0, 5.8, 5.9], [28, 2, true, 21, 0, 7.82, 7.9], [29, 3, true, 20, 0, 10.38, 10.6], [30, 1, true, 20, 0, 8.67, 8.8], [31, 2, true, 24, 0, 8.57, 9.1], [32, 3, true, 18, 0, 10.0, 11.0], [33, 3, true, 22, 0, 8.85, 9.1], [34, 1, true, 18, 0, 5.67, 6.1], [35, 1, true, 18, 0, 5.65, 7.5], [36, 2, true, 20, 0, 7.27, 7.4], [37, 1, true, 18, 0, 7.09, 7.4], [38, 1, true, 20, 0, 5.75, 6.0], [39, 3, true, 22, 0, 8.54, 8.7], [40, 2, true, 21, 0, 10.49, 10.8], [41, 2, true, 18, 0, 8.47, 8.6], [42, 1, true, 20, 0, 9.0, 9.5], [43, 2, true, 24, 0, 8.62, 9.4], [44, 3, true, 19, 0, 10.15, 10.4], [45, 3, true, 20, 0, 12.35, 12.5], [46, 2, true, 18, 0, 9.06, 9.5], [47, 1, true, 20, 0, 7.36, 7.5], [48, 1, true, 19, 0, 9.11, 9.2], [49, 1, true, 20, 0, 9.45, 9.6], [50, 3, true, 21, 0, 14.64, 14.8], [51, 2, true, 20, 0, 8.09, 8.8], [52, 3, true, 22, 0, 9.34, 9.6], [53, 3, true, 20, 0, 14.41, 14.5], [54, 1, true, 20, 0, 7.99, 8.8], [55, 3, true, 26, 0, 18.52, 18.6], [56, 2, true, 22, 0, 11.76, 12.0], [57, 1, true, 16, 0, 9.98, 10.1], [58, 2, true, 23, 0, 11.79, 12.0], [59, 3, true, 20, 0, 17.72, 17.9], [60, 1, true, 22, 0, 10.25, 10.4], [61, 2, true, 19, 0, 11.4, 11.5], [62, 2, true, 21, 0, 12.16, 13.2], [63, 2, true, 21, 0, 11.72, 13.1], [64, 2, true, 21, 0, 10.67, 12.7], [65, 1, true, 16, 0, 9.08, 10.7], [66, 3, true, 21, 0, 9.39, 10.3], [67, 3, true, 20, 0, 10.47, 10.6], [68, 2, true, 19, 0, 8.61, 9.2], [69, 1, true, 20, 0, 5.16, 5.8], [70, 2, true, 20, 0, 11.77, 11.9], [71, 3, true, 20, 0, 14.22, 15.8], [72, 3, true, 20, 0, 14.78, 15.7], [73, 3, true, 20, 0, 11.46, 12.8], [74, 1, true, 20, 0, 10.45, 11.7], [75, 2, true, 18, 0, 8.77, 9.1], [76, 2, true, 22, 0, 10.56, 11.9], [77, 1, true, 18, 0, 7.54, 9.2], [78, 3, true, 21, 0, 11.18, 11.3], [79, 1, true, 23, 0, 8.97, 9.1], [80, 3, true, 20, 0, 16.82, 17.2], [81, 1, true, 18, 0, 10.7, 10.8], [82, 3, true, 19, 0, 12.42, 12.5], [83, 3, true, 21, 0, 13.27, 13.5], [84, 2, true, 22, 0, 12.67, 12.8], [85, 3, true, 19, 0, 15.47, 15.6], [86, 3, true, 20, 0, 11.37, 11.5], [87, 2, true, 23, 0, 17.74, 18.4], [88, 2, true, 18, 0, 10.21, 10.5], [89, 3, true, 29, 0, 7.89, 8.1], [90, 2, true, 20, 0, 10.81, 11.4], [91, 3, true, 22, 0, 8.51, 8.7], [92, 2, true, 22, 0, 9.08, 9.2], [93, 3, true, 22, 0, 10.71, 11.7], [94, 1, true, 20, 0, 8.73, 9.0], [95, 2, true, 20, 0, 10.61, 10.8], [96, 3, true, 21, 0, 10.7, 11.1], [97, 1, true, 27, 0, 9.13, 9.4], [98, 2, true, 22, 0, 8.12, 8.8], [99, 3, true, 22, 0, 11.13, 11.3], [100, 3, true, 23, 0, 11.16, 11.8], [101, 1, true, 17, 0, 6.23, 6.7], [102, 2, true, 21, 0, 10.75, 10.8], [103, 2, true, 21, 0, 9.35, 9.5], [104, 3, true, 19, 0, 13.11, 13.3], [105, 1, true, 20, 0, 7.04, 7.1], [106, 2, true, 19, 0, 8.25, 8.4], [107, 1, true, 20, 0, 9.62, 9.8], [108, 1, true, 19, 0, 9.09, 9.2], [109, 2, true, 19, 0, 11.16, 11.3], [110, 2, true, 20, 0, 10.93, 11.6], [111, 2, true, 20, 0, 9.33, 10.0], [112, 1, true, 18, 0, 8.88, 9.6], [113, 1, true, 19, 0, 6.54, 6.6], [114, 1, true, 18, 0, 7.87, 8.0], [115, 2, true, 21, 0, 7.49, 7.7], [116, 1, true, 21, 0, 6.12, 6.4], [117, 1, true, 24, 0, 4.44, 4.6], [118, 2, true, 19, 0, 4.53, 4.6], [119, 2, true, 20, 0, 4.13, 4.2]]
\ No newline at end of file
```

</details>

<a id="C026"></a>
### C026 · notes

Commit `52ce3d1d5c10fc0e7e65589d19e946a5401b3b30`; parents: dbc525a1bb8ae106d6c54dad4ef4bb5b69d74e80. Recorded author date: 2026-10-01T12:16:44+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0047](01_timeline.md#E0047): commit title in command; output may not confirm creation.
- [E0450](01_timeline.md#E0450): commit title in command; output may not confirm creation.
- [E0524](01_timeline.md#E0524): commit title in command; output may not confirm creation.
- [E0611](01_timeline.md#E0611): commit title in command; output may not confirm creation.
- [E1141](01_timeline.md#E1141): commit title in command; output may not confirm creation.
- [E1363](01_timeline.md#E1363): commit title in command; output may not confirm creation.
- [E1464](01_timeline.md#E1464): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C026_52ce3d1.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/NOTES.md b/NOTES.md
index b32860b..c1e6ef5 100644
--- a/NOTES.md
+++ b/NOTES.md
@@ -21,3 +21,15 @@
   21     21  ## Objective visibility (probed)
   22     22  - cam = (x,y)+R(theta)(-0.087,-0.0125); visible iff |obj-cam|<=1.9976 and (|rel bearing|>~98deg or segment cam'->obj misses pillar boxes inflated ~0.01). Wall & mounds don't block.
   23     23  - calibrated persists through moves until a successful image. Image = nearest visible objective not yet imaged by this rover. Calibrate needs any objective visible.
          24 +## Later findings
          25 +- Rovers are updated sequentially within a step: rover0 move+op, then rover1 move+op. So rover0's send sees rover1's PREVIOUS position.
          26 +- Rover occluder for send LOS: disk ~0.23 around rover centre vs segment cam->lander centre (use 0.26).
          27 +- Lander send range measured from cam point too.
          28 +- Image picks nearest objective (liberal: any within range) not yet imaged by this rover -> planner excludes cells where another un-imaged objective is nearer.
          29 +- Sample picks nearest sample -> region requires target type strictly nearest.
          30 +- Facing -y (theta=-pi/2) while imaging moves cam 0.087 toward objectives: ~0.7 steps saved.
          31 +- Max objectives = 4 (4 mounds).
          32 +## Approach (approach.py)
          33 +- Per-rover coarse grid (0.05) staged BFS over task orders (DFS trie), joint assignment min makespan,
          34 +  top-K realised on fine grid (0.025) with time-aware send vs other rover trajectory; replan on deviation.
          35 +- Results: seeds 0-400 all solved, mean 20.475 steps.
diff --git a/prof.out b/prof.out
index a8cf78d..1bd2b76 100644
Binary files a/prof.out and b/prof.out differ
diff --git a/res_ref400.json b/res_ref400.json
new file mode 100644
index 0000000..d4078ba
--- /dev/null
+++ b/res_ref400.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 9.04, 9.3], [1, 2, true, 18, 0, 9.81, 9.9], [2, 3, true, 19, 0, 17.15, 17.7], [3, 3, true, 21, 0, 15.57, 15.7], [4, 3, true, 20, 0, 11.46, 11.8], [5, 3, true, 23, 0, 16.65, 17.8], [6, 2, true, 19, 0, 14.89, 15.4], [7, 3, true, 22, 0, 18.15, 18.3], [8, 3, true, 20, 0, 16.0, 16.6], [9, 2, true, 22, 0, 13.99, 14.1], [10, 3, true, 20, 0, 18.84, 19.0], [11, 1, true, 19, 0, 8.98, 9.6], [12, 2, true, 22, 0, 10.87, 11.1], [13, 3, true, 23, 0, 18.2, 18.3], [14, 1, true, 29, 0, 9.66, 10.3], [15, 3, true, 23, 0, 17.18, 17.3], [16, 2, true, 21, 0, 12.31, 13.1], [17, 3, true, 22, 0, 20.9, 21.1], [18, 3, true, 22, 0, 13.2, 13.6], [19, 2, true, 25, 0, 9.0, 10.2], [20, 3, true, 27, 0, 11.15, 11.4], [21, 1, true, 19, 0, 10.85, 11.2], [22, 3, true, 21, 0, 15.12, 15.3], [23, 1, true, 16, 0, 11.56, 11.9], [24, 2, true, 18, 0, 10.1, 10.2], [25, 2, true, 18, 0, 13.75, 14.6], [26, 3, true, 21, 0, 17.38, 17.6], [27, 1, true, 21, 0, 8.58, 9.2], [28, 2, true, 21, 0, 10.58, 10.7], [29, 3, true, 20, 0, 14.04, 14.2], [30, 1, true, 20, 0, 11.81, 12.5], [31, 2, true, 24, 0, 12.32, 13.3], [32, 3, true, 18, 0, 12.75, 14.6], [33, 3, true, 22, 0, 11.31, 13.9], [34, 1, true, 18, 0, 8.63, 9.7], [35, 1, true, 18, 0, 7.65, 8.1], [36, 2, true, 20, 0, 9.66, 9.8], [37, 1, true, 18, 0, 9.52, 9.6], [38, 1, true, 20, 0, 6.49, 6.6], [39, 3, true, 22, 0, 11.44, 11.6], [40, 2, true, 21, 0, 13.12, 13.5], [41, 2, true, 18, 0, 10.4, 10.6], [42, 1, true, 20, 0, 12.16, 13.7], [43, 2, true, 24, 0, 11.09, 12.4], [44, 3, true, 19, 0, 12.2, 12.4], [45, 3, true, 20, 0, 13.72, 13.9], [46, 2, true, 18, 0, 11.28, 11.7], [47, 1, true, 20, 0, 9.8, 9.9], [48, 1, true, 19, 0, 10.59, 10.8], [49, 1, true, 20, 0, 12.88, 13.6], [50, 3, true, 21, 0, 18.13, 18.7], [51, 2, true, 20, 0, 11.08, 11.2], [52, 3, true, 22, 0, 12.73, 12.8], [53, 3, true, 20, 0, 18.48, 18.7], [54, 1, true, 20, 0, 12.55, 12.7], [55, 3, true, 26, 0, 21.89, 22.8], [56, 2, true, 22, 0, 14.22, 15.1], [57, 1, true, 16, 0, 11.8, 11.9], [58, 2, true, 23, 0, 13.91, 14.1], [59, 3, true, 20, 0, 19.97, 20.1], [60, 1, true, 22, 0, 12.46, 12.6], [61, 2, true, 19, 0, 13.09, 13.2], [62, 2, true, 21, 0, 14.92, 15.1], [63, 2, true, 21, 0, 14.54, 15.3], [64, 2, true, 21, 0, 13.73, 14.1], [65, 1, true, 16, 0, 12.82, 12.9], [66, 3, true, 21, 0, 14.27, 14.4], [67, 3, true, 20, 0, 15.77, 16.6], [68, 2, true, 19, 0, 13.52, 13.6], [69, 1, true, 20, 0, 9.78, 9.9], [70, 2, true, 20, 0, 12.76, 12.9], [71, 3, true, 20, 0, 15.03, 16.3], [72, 3, true, 20, 0, 15.25, 15.8], [73, 3, true, 20, 0, 11.61, 11.7], [74, 1, true, 20, 0, 9.69, 10.5], [75, 2, true, 18, 0, 8.21, 8.7], [76, 2, true, 22, 0, 10.09, 10.2], [77, 1, true, 18, 0, 7.07, 7.5], [78, 3, true, 21, 0, 11.1, 11.3], [79, 1, true, 23, 0, 9.61, 9.9], [80, 3, true, 20, 0, 14.32, 14.5], [81, 1, true, 18, 0, 9.85, 10.0], [82, 3, true, 19, 0, 11.09, 11.3], [83, 3, true, 21, 0, 10.96, 11.4], [84, 2, true, 22, 0, 10.96, 11.4], [85, 3, true, 19, 0, 14.03, 14.2], [86, 3, true, 20, 0, 11.34, 11.5], [87, 2, true, 23, 0, 11.51, 11.9], [88, 2, true, 18, 0, 10.44, 11.8], [89, 3, true, 29, 0, 7.93, 8.2], [90, 2, true, 20, 0, 8.98, 10.4], [91, 3, true, 22, 0, 7.11, 8.0], [92, 2, true, 22, 0, 7.26, 9.1], [93, 3, true, 22, 0, 9.06, 9.2], [94, 1, true, 20, 0, 6.61, 7.1], [95, 2, true, 20, 0, 7.74, 7.9], [96, 3, true, 21, 0, 8.89, 9.1], [97, 1, true, 27, 0, 7.6, 7.7], [98, 2, true, 22, 0, 7.45, 8.5], [99, 3, true, 22, 0, 9.73, 10.1], [100, 3, true, 23, 0, 9.28, 10.2], [101, 1, true, 17, 0, 5.77, 5.8], [102, 2, true, 21, 0, 9.72, 11.6], [103, 2, true, 21, 0, 8.15, 8.5], [104, 3, true, 19, 0, 10.68, 11.8], [105, 1, true, 20, 0, 5.87, 6.4], [106, 2, true, 19, 0, 6.62, 8.4], [107, 1, true, 20, 0, 6.65, 7.5], [108, 1, true, 19, 0, 6.15, 7.3], [109, 2, true, 19, 0, 7.26, 8.0], [110, 2, true, 20, 0, 8.71, 9.0], [111, 2, true, 20, 0, 8.11, 9.9], [112, 1, true, 18, 0, 7.42, 8.6], [113, 1, true, 19, 0, 6.02, 6.1], [114, 1, true, 18, 0, 6.71, 8.7], [115, 2, true, 21, 0, 6.74, 9.1], [116, 1, true, 21, 0, 5.17, 7.9], [117, 1, true, 24, 0, 4.7, 8.0], [118, 2, true, 19, 0, 4.65, 5.5], [119, 2, true, 20, 0, 3.88, 4.4], [120, 1, true, 18, 0, 4.26, 5.2], [121, 1, true, 20, 0, 6.43, 6.6], [122, 3, true, 20, 0, 8.65, 8.8], [123, 1, true, 20, 0, 7.63, 7.7], [124, 3, true, 22, 0, 10.07, 10.8], [125, 2, true, 18, 0, 7.98, 8.1], [126, 1, true, 18, 0, 9.48, 9.6], [127, 2, true, 21, 0, 7.55, 7.6], [128, 3, true, 20, 0, 10.34, 10.5], [129, 2, true, 21, 0, 9.53, 9.7], [130, 3, true, 23, 0, 12.02, 12.2], [131, 2, true, 20, 0, 9.62, 9.7], [132, 3, true, 24, 0, 15.26, 16.1], [133, 2, true, 18, 0, 10.17, 10.3], [134, 3, true, 23, 0, 15.96, 16.4], [135, 2, true, 18, 0, 10.28, 10.4], [136, 3, true, 22, 0, 10.59, 10.7], [137, 2, true, 21, 0, 10.02, 10.9], [138, 2, true, 22, 0, 6.69, 7.0], [139, 2, true, 19, 0, 8.24, 8.4], [140, 2, true, 18, 0, 10.36, 10.4], [141, 2, true, 18, 0, 10.31, 10.4], [142, 1, true, 18, 0, 9.07, 9.5], [143, 3, true, 22, 0, 10.16, 11.3], [144, 1, true, 19, 0, 8.45, 9.1], [145, 2, true, 23, 0, 8.14, 8.8], [146, 3, true, 20, 0, 10.5, 10.6], [147, 1, true, 18, 0, 7.26, 7.9], [148, 1, true, 18, 0, 8.17, 8.3], [149, 1, true, 16, 0, 8.28, 8.4], [150, 2, true, 20, 0, 10.23, 10.4], [151, 3, true, 25, 0, 11.96, 13.3], [152, 3, true, 27, 0, 10.91, 12.1], [153, 3, true, 22, 0, 10.05, 10.1], [154, 1, true, 20, 0, 6.74, 6.8], [155, 1, true, 16, 0, 9.01, 9.3], [156, 3, true, 20, 0, 11.1, 11.2], [157, 1, true, 20, 0, 5.49, 6.7], [158, 2, true, 20, 0, 5.86, 6.0], [159, 3, true, 20, 0, 13.43, 13.6], [160, 1, true, 18, 0, 9.98, 10.1], [161, 3, true, 20, 0, 12.82, 13.3], [162, 2, true, 27, 0, 11.59, 13.0], [163, 2, true, 18, 0, 11.73, 12.9], [164, 2, true, 27, 0, 9.65, 10.6], [165, 2, true, 19, 0, 8.41, 8.7], [166, 3, true, 20, 0, 14.29, 14.6], [167, 3, true, 21, 0, 8.01, 8.2], [168, 2, true, 20, 0, 11.1, 11.8], [169, 3, true, 31, 0, 9.68, 9.9], [170, 3, true, 22, 0, 9.33, 10.2], [171, 3, true, 21, 0, 10.03, 10.7], [172, 2, true, 20, 0, 10.79, 10.9], [173, 3, true, 33, 0, 10.99, 11.4], [174, 2, true, 20, 0, 8.67, 8.8], [175, 3, true, 21, 0, 14.19, 14.3], [176, 1, true, 21, 0, 8.8, 8.9], [177, 3, true, 21, 0, 14.55, 14.7], [178, 2, true, 22, 0, 11.29, 11.4], [179, 3, true, 22, 0, 9.48, 10.2], [180, 1, true, 19, 0, 7.62, 8.1], [181, 3, true, 23, 0, 10.04, 10.2], [182, 3, true, 18, 0, 11.87, 11.9], [183, 3, true, 21, 0, 12.53, 14.3], [184, 2, true, 23, 0, 9.87, 10.1], [185, 1, true, 19, 0, 9.21, 9.5], [186, 1, true, 37, 0, 9.12, 12.6], [187, 2, true, 20, 0, 9.22, 9.6], [188, 2, true, 18, 0, 7.94, 9.5], [189, 2, true, 29, 0, 7.72, 10.4], [190, 1, true, 18, 0, 5.72, 8.2], [191, 1, true, 21, 0, 5.67, 5.9], [192, 3, true, 22, 0, 8.99, 9.1], [193, 2, true, 21, 0, 11.38, 12.2], [194, 3, true, 20, 0, 10.62, 10.8], [195, 1, true, 18, 0, 7.37, 7.4], [196, 1, true, 16, 0, 9.27, 10.0], [197, 3, true, 19, 0, 9.63, 10.8], [198, 2, true, 21, 0, 9.67, 10.6], [199, 2, true, 19, 0, 8.59, 9.5], [200, 1, true, 18, 0, 6.58, 6.7], [201, 1, true, 20, 0, 6.5, 6.6], [202, 1, true, 20, 0, 7.34, 7.5], [203, 1, true, 19, 0, 6.3, 7.0], [204, 3, true, 20, 0, 9.9, 10.1], [205, 2, true, 18, 0, 8.34, 8.4], [206, 2, true, 18, 0, 10.96, 11.1], [207, 1, true, 19, 0, 8.18, 8.4], [208, 3, true, 19, 0, 15.74, 16.2], [209, 3, true, 20, 0, 12.44, 13.0], [210, 1, true, 19, 0, 7.82, 8.0], [211, 1, true, 16, 0, 7.41, 7.9], [212, 1, true, 23, 0, 5.43, 5.8], [213, 1, true, 18, 0, 7.97, 8.1], [214, 1, true, 18, 0, 8.48, 8.6], [215, 3, true, 20, 0, 13.52, 13.6], [216, 3, true, 21, 0, 15.11, 15.2], [217, 3, true, 19, 0, 12.16, 12.3], [218, 2, true, 23, 0, 8.72, 8.9], [219, 1, true, 27, 0, 8.52, 8.9], [220, 3, true, 23, 0, 11.75, 12.5], [221, 2, true, 20, 0, 9.55, 9.7], [222, 2, true, 18, 0, 7.83, 7.9], [223, 2, true, 20, 0, 9.29, 9.4], [224, 3, true, 20, 0, 11.79, 11.9], [225, 3, true, 20, 0, 14.37, 15.3], [226, 3, true, 20, 0, 10.1, 10.9], [227, 2, true, 18, 0, 9.23, 9.9], [228, 2, true, 18, 0, 9.98, 10.6], [229, 2, true, 21, 0, 8.48, 9.5], [230, 2, true, 19, 0, 7.97, 8.6], [231, 1, true, 23, 0, 5.8, 7.1], [232, 2, true, 19, 0, 7.18, 7.3], [233, 1, true, 19, 0, 6.93, 7.0], [234, 2, true, 21, 0, 5.65, 6.1], [235, 3, true, 20, 0, 13.49, 13.7], [236, 2, true, 19, 0, 8.8, 8.9], [237, 3, true, 23, 0, 12.8, 13.5], [238, 2, true, 20, 0, 8.21, 8.5], [239, 3, true, 20, 0, 11.01, 11.1], [240, 3, true, 20, 0, 11.17, 12.1], [241, 2, true, 20, 0, 10.54, 10.7], [242, 3, true, 23, 0, 14.22, 14.3], [243, 3, true, 22, 0, 12.27, 12.4], [244, 3, true, 19, 0, 11.47, 12.2], [245, 3, true, 22, 0, 8.91, 9.6], [246, 3, true, 20, 0, 11.19, 11.4], [247, 1, true, 16, 0, 8.7, 8.9], [248, 2, true, 18, 0, 8.43, 9.3], [249, 3, true, 20, 0, 13.4, 13.6], [250, 2, true, 24, 0, 9.79, 10.7], [251, 1, true, 17, 0, 8.06, 8.2], [252, 3, true, 22, 0, 10.84, 11.2], [253, 2, true, 18, 0, 7.62, 9.2], [254, 1, true, 16, 0, 8.45, 9.0], [255, 1, true, 30, 0, 7.74, 8.8], [256, 2, true, 28, 0, 6.17, 7.6], [257, 3, true, 23, 0, 10.12, 10.3], [258, 2, true, 21, 0, 10.01, 10.1], [259, 1, true, 19, 0, 10.01, 10.6], [260, 3, true, 21, 0, 14.96, 15.1], [261, 2, true, 22, 0, 8.2, 8.8], [262, 3, true, 25, 0, 11.05, 11.2], [263, 3, true, 20, 0, 11.79, 11.9], [264, 1, true, 18, 0, 9.08, 9.2], [265, 3, true, 20, 0, 13.54, 14.4], [266, 2, true, 21, 0, 10.86, 11.0], [267, 2, true, 19, 0, 8.83, 9.0], [268, 3, true, 20, 0, 11.67, 13.3], [269, 3, true, 19, 0, 9.84, 10.0], [270, 2, true, 18, 0, 10.7, 11.6], [271, 3, true, 21, 0, 10.62, 11.9], [272, 1, true, 16, 0, 8.65, 9.5], [273, 1, true, 18, 0, 8.92, 9.0], [274, 2, true, 27, 0, 9.8, 10.0], [275, 1, true, 21, 0, 9.39, 9.5], [276, 2, true, 20, 0, 10.49, 10.8], [277, 1, true, 16, 0, 9.42, 9.5], [278, 2, true, 21, 0, 10.05, 10.2], [279, 2, true, 21, 0, 12.77, 12.9], [280, 2, true, 29, 0, 10.18, 10.4], [281, 2, true, 20, 0, 10.88, 11.4], [282, 3, true, 20, 0, 13.33, 13.4], [283, 1, true, 16, 0, 6.79, 6.9], [284, 1, true, 19, 0, 6.67, 6.8], [285, 3, true, 20, 0, 13.94, 15.3], [286, 1, true, 16, 0, 9.39, 9.5], [287, 3, true, 21, 0, 12.47, 14.5], [288, 1, true, 18, 0, 9.01, 9.9], [289, 2, true, 23, 0, 10.87, 12.0], [290, 1, true, 18, 0, 7.33, 7.4], [291, 1, true, 18, 0, 6.95, 8.2], [292, 3, true, 20, 0, 9.17, 9.3], [293, 1, true, 20, 0, 7.17, 7.3], [294, 1, true, 27, 0, 7.1, 7.2], [295, 1, true, 21, 0, 7.8, 7.9], [296, 1, true, 20, 0, 9.13, 9.3], [297, 1, true, 18, 0, 9.17, 9.6], [298, 2, true, 21, 0, 11.31, 11.4], [299, 3, true, 22, 0, 14.62, 14.8], [300, 1, true, 18, 0, 10.52, 10.9], [301, 1, true, 21, 0, 9.52, 9.7], [302, 3, true, 20, 0, 12.81, 13.0], [303, 2, true, 23, 0, 11.13, 11.9], [304, 3, true, 20, 0, 11.03, 11.2], [305, 1, true, 17, 0, 9.6, 9.7], [306, 3, true, 22, 0, 11.36, 12.2], [307, 3, true, 19, 0, 10.18, 10.7], [308, 2, true, 20, 0, 9.33, 9.4], [309, 2, true, 20, 0, 7.4, 8.6], [310, 1, true, 18, 0, 6.99, 7.3], [311, 2, true, 29, 0, 6.15, 7.3], [312, 1, true, 16, 0, 6.51, 6.9], [313, 1, true, 18, 0, 6.21, 6.5], [314, 2, true, 22, 0, 5.0, 5.1], [315, 2, true, 19, 0, 9.0, 9.5], [316, 1, true, 18, 0, 9.62, 9.7], [317, 1, true, 18, 0, 7.64, 7.8], [318, 1, true, 17, 0, 5.93, 6.0], [319, 3, true, 26, 0, 10.69, 10.9], [320, 1, true, 19, 0, 8.16, 8.3], [321, 2, true, 20, 0, 9.89, 10.7], [322, 1, true, 18, 0, 8.41, 9.1], [323, 3, true, 18, 0, 13.07, 13.2], [324, 2, true, 22, 0, 7.12, 7.2], [325, 1, true, 18, 0, 6.87, 7.6], [326, 1, true, 18, 0, 6.84, 7.6], [327, 2, true, 21, 0, 9.75, 10.0], [328, 1, true, 20, 0, 8.67, 9.0], [329, 3, true, 20, 0, 11.47, 12.6], [330, 2, true, 19, 0, 10.02, 10.2], [331, 1, true, 18, 0, 8.46, 9.6], [332, 2, true, 25, 0, 8.06, 10.4], [333, 1, true, 17, 0, 6.76, 7.4], [334, 2, true, 18, 0, 8.65, 9.1], [335, 1, true, 19, 0, 5.59, 6.1], [336, 2, true, 21, 0, 6.08, 6.3], [337, 1, true, 23, 0, 5.6, 6.0], [338, 2, true, 18, 0, 9.92, 10.1], [339, 1, true, 18, 0, 9.36, 9.8], [340, 1, true, 20, 0, 9.92, 11.5], [341, 3, true, 21, 0, 10.97, 12.1], [342, 3, true, 23, 0, 10.79, 12.8], [343, 1, true, 23, 0, 6.7, 7.6], [344, 1, true, 17, 0, 6.48, 7.6], [345, 1, true, 16, 0, 7.63, 8.2], [346, 2, true, 19, 0, 8.52, 9.0], [347, 3, true, 22, 0, 7.37, 7.5], [348, 1, true, 21, 0, 5.77, 5.9], [349, 3, true, 22, 0, 9.57, 9.7], [350, 2, true, 21, 0, 9.63, 10.5], [351, 2, true, 27, 0, 8.02, 9.5], [352, 1, true, 18, 0, 8.07, 9.3], [353, 1, true, 18, 0, 6.3, 7.4], [354, 3, true, 23, 0, 8.99, 9.2], [355, 2, true, 18, 0, 8.28, 9.1], [356, 1, true, 18, 0, 5.4, 5.5], [357, 2, true, 24, 0, 10.43, 10.6], [358, 3, true, 20, 0, 13.0, 13.9], [359, 2, true, 27, 0, 8.03, 8.1], [360, 3, true, 20, 0, 13.34, 16.2], [361, 3, true, 23, 0, 11.58, 12.7], [362, 3, true, 22, 0, 10.58, 12.3], [363, 1, true, 16, 0, 8.37, 8.6], [364, 2, true, 20, 0, 7.63, 9.4], [365, 1, true, 18, 0, 6.79, 8.6], [366, 1, true, 16, 0, 4.12, 6.0], [367, 3, true, 22, 0, 9.89, 10.5], [368, 3, true, 20, 0, 13.05, 13.2], [369, 3, true, 24, 0, 8.14, 8.4], [370, 2, true, 22, 0, 10.56, 10.7], [371, 3, true, 20, 0, 13.61, 14.7], [372, 2, true, 18, 0, 7.76, 7.9], [373, 2, true, 23, 0, 12.02, 13.3], [374, 3, true, 20, 0, 11.68, 11.9], [375, 1, true, 18, 0, 7.37, 8.1], [376, 2, true, 20, 0, 12.57, 13.3], [377, 3, true, 20, 0, 9.0, 9.1], [378, 2, true, 21, 0, 9.23, 9.4], [379, 3, true, 22, 0, 9.44, 9.7], [380, 2, true, 18, 0, 8.66, 8.8], [381, 3, true, 21, 0, 13.12, 13.2], [382, 1, true, 18, 0, 10.43, 10.8], [383, 1, true, 20, 0, 9.05, 9.2], [384, 1, true, 18, 0, 7.65, 8.5], [385, 3, true, 22, 0, 13.9, 14.9], [386, 2, true, 22, 0, 8.22, 8.4], [387, 2, true, 19, 0, 6.73, 6.8], [388, 2, true, 20, 0, 10.06, 10.2], [389, 1, true, 19, 0, 8.17, 8.9], [390, 2, true, 21, 0, 9.31, 9.8], [391, 1, true, 19, 0, 7.32, 8.6], [392, 3, true, 20, 0, 10.47, 10.6], [393, 3, true, 23, 0, 10.03, 10.2], [394, 1, true, 20, 0, 8.69, 8.8], [395, 2, true, 19, 0, 8.09, 8.3], [396, 2, true, 23, 0, 6.54, 6.7], [397, 3, true, 20, 0, 7.33, 7.5], [398, 3, true, 21, 0, 6.67, 6.8], [399, 3, true, 21, 0, 6.43, 6.5]]
\ No newline at end of file
diff --git a/test_cnt.py b/test_cnt.py
new file mode 100644
index 0000000..ce0c010
--- /dev/null
+++ b/test_cnt.py
@@ -0,0 +1,26 @@
           1 +import sys, time
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +cnt=int(sys.argv[1])
           6 +def run(seed):
           7 +    env = make_env()
           8 +    try:
           9 +        obs, info = env.reset(seed=seed, options={"object_count": cnt})
          10 +    except Exception as e:
          11 +        return seed, 'err', str(e)[:100]
          12 +    n=len([o for o in obs if o.type.name=='objective'])
          13 +    ap = GeneratedApproach(env.action_space, env.observation_space, {})
          14 +    t0=time.time(); ap.reset(obs, info); tp=time.time()-t0
          15 +    steps=0
          16 +    while steps < 300:
          17 +        obs, r, term, trunc, info = env.step(ap.get_action(obs)); steps+=1
          18 +        if term: break
          19 +    env.close()
          20 +    return seed, n, term, steps, ap.replans, round(tp,2), round(time.time()-t0,1)
          21 +from concurrent.futures import ThreadPoolExecutor
          22 +with ThreadPoolExecutor(8) as ex: res=list(ex.map(run, range(int(sys.argv[2]), int(sys.argv[3]))))
          23 +for r in res:
          24 +    if len(r)<5 or not r[2] or r[4]: print(r)
          25 +ok=[r for r in res if r[2] is True]
          26 +print('solved',len(ok),len(res),'mean',np.mean([r[3] for r in ok]),'maxplan',max(r[5] for r in ok))
```

</details>

<a id="C027"></a>
### C027 · parse state via object names

Commit `52d4e126afc593a861dfd00b3eae5c930d4670af`; parents: 52ce3d1d5c10fc0e7e65589d19e946a5401b3b30. Recorded author date: 2026-10-01T12:17:30+02:00.

File roles (automatic): policy, support code (role needs review).

- [E1162](01_timeline.md#E1162): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C027_52d4e12_approach.py) · [Exact all-file diff](evidence/diffs/C027_52d4e12.diff)

[Previous saved controller snapshot](evidence/versions/C025_dbc525a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 97d0449..47a3eea 100644
--- a/approach.py
+++ b/approach.py
@@ -110,7 +110,8 @@ class Scene:
  110    110          self.pillars = []
  111    111          self.mounds = []
  112    112          self.lander = (-1.9, -2.0)
  113        -        for o in state:
         113 +        objs = [state.get_object_from_name(nm) for nm in sorted(state.get_object_names())]
         114 +        for o in objs:
  114    115              t = o.type.name
  115    116              g = lambda f: state.get(o, f)
  116    117              if t == "rover":
diff --git a/dbg8.py b/dbg8.py
new file mode 100644
index 0000000..9ac3127
--- /dev/null
+++ b/dbg8.py
@@ -0,0 +1,10 @@
           1 +import sys
           2 +from test_approach import *
           3 +for seed in map(int, sys.argv[1:]):
           4 +    env = make_env(); obs, info = env.reset(seed=seed); env.close()
           5 +    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           6 +    print(seed, 'pred', ap.pred)
           7 +    for ri in range(2):
           8 +        print(' r%d'%ri, len(ap.actions[ri]), [(i+1,round(x,2),round(y,2),op) for i,(x,y,op,h) in enumerate(ap.actions[ri]) if op])
           9 +    for o in obs:
          10 +        if o.type.name in ('objective','sample'): print('  ',o.name,[round(float(v),2) for v in obs.data[o]][:4])
diff --git a/dbg9.py b/dbg9.py
new file mode 100644
index 0000000..fa0a226
--- /dev/null
+++ b/dbg9.py
@@ -0,0 +1,13 @@
           1 +import sys
           2 +from test_approach import *
           3 +import approach
           4 +seed=int(sys.argv[1])
           5 +env = make_env(); obs, info = env.reset(seed=seed); env.close()
           6 +ap = GeneratedApproach(env.action_space, env.observation_space, {})
           7 +orig=ap._rover_tables
           8 +def wrap(*a, **k):
           9 +    P,t=orig(*a,**k)
          10 +    print('rover',a[0], sorted([(tuple(sorted(map(str,key))),v[0]) for key,v in t.items()], key=lambda z:z[1])[:40])
          11 +    return P,t
          12 +ap._rover_tables=wrap
          13 +ap.reset(obs, info)
```

</details>

<a id="C028"></a>
### C028 · relaxed fallback when no plan

Commit `fc2cc208a203b360625355d2632e312e9e5ac788`; parents: 52d4e126afc593a861dfd00b3eae5c930d4670af. Recorded author date: 2026-10-01T12:18:43+02:00.

File roles (automatic): policy, setup/other.

- [E1169](01_timeline.md#E1169): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C028_fc2cc20_approach.py) · [Exact all-file diff](evidence/diffs/C028_fc2cc20.diff)

[Previous saved controller snapshot](evidence/versions/C027_52d4e12_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 47a3eea..e970e9a 100644
--- a/approach.py
+++ b/approach.py
@@ -39,6 +39,9 @@ def _wrap(a):
   39     39      return (a + np.pi) % (2 * np.pi) - np.pi
   40     40  
   41     41  
          42 +RELAX = [False]
          43 +
          44 +
   42     45  def rot_steps(a, b):
   43     46      d = abs(float(_wrap(b - a)))
   44     47      return int(math.ceil(d / 0.4 - 1e-6))
@@ -53,6 +56,8 @@ def approach_angle(a, b, dmax):
   53     56  
   54     57  def seg_hits_box(px, py, qx, qy, cx, cy, hx, hy):
   55     58      """Vectorised: does segment p->q (p arrays, q scalar) intersect AABB?"""
          59 +    if RELAX[0]:
          60 +        return np.zeros(np.shape(px), dtype=bool)
   56     61      dx = qx - px
   57     62      dy = qy - py
   58     63      t0 = np.zeros_like(px)
@@ -165,7 +170,7 @@ class RoverPlanner:
  165    170          self.X, self.Y = X, Y
  166    171          free = np.ones(X.shape, dtype=bool)
  167    172          for (cx, cy, ax, ay) in scene.pillars:
  168        -            free &= box_dist(X, Y, cx, cy, ax, ay) > PILLAR_R
         173 +            free &= box_dist(X, Y, cx, cy, ax, ay) > (0.236 if RELAX[0] else PILLAR_R)
  169    174          for (cx, cy, ax, ay) in scene.mounds:
  170    175              free &= box_dist(X, Y, cx, cy, ax, ay) > MOUND_R
  171    176          free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
@@ -461,6 +466,12 @@ class GeneratedApproach:
  461    466                          best = (key, costs)
  462    467          self.actions = [[], []]
  463    468          if best is None:
         469 +            if not RELAX[0]:
         470 +                RELAX[0] = True
         471 +                try:
         472 +                    self._plan(state)
         473 +                finally:
         474 +                    RELAX[0] = False
  464    475              return
  465    476          cands.sort(key=lambda c: c[0])
  466    477          seen = set()
diff --git a/res_n.json b/res_n.json
new file mode 100644
index 0000000..11d1f99
--- /dev/null
+++ b/res_n.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 4.99, 5.2], [1, 2, true, 18, 0, 10.72, 10.8], [2, 3, true, 19, 0, 15.8, 16.4], [3, 3, true, 21, 0, 13.02, 13.1], [4, 3, true, 20, 0, 15.39, 15.5], [5, 3, true, 23, 0, 16.05, 17.5], [6, 2, true, 19, 0, 12.08, 12.5], [7, 3, true, 22, 0, 16.74, 18.1], [8, 3, true, 20, 0, 13.78, 14.8], [9, 2, true, 22, 0, 9.81, 10.0], [10, 3, true, 20, 0, 12.86, 13.6], [11, 1, true, 19, 0, 6.21, 7.0], [12, 2, true, 22, 0, 7.47, 7.7], [13, 3, true, 23, 0, 12.66, 12.8], [14, 1, true, 29, 0, 7.34, 7.5], [15, 3, true, 23, 0, 13.21, 13.3], [16, 2, true, 21, 0, 9.86, 10.0], [17, 3, true, 22, 0, 17.74, 17.9], [18, 3, true, 22, 0, 11.17, 11.7], [19, 2, true, 25, 0, 7.41, 8.3], [20, 3, true, 27, 0, 9.07, 9.3], [21, 1, true, 19, 0, 9.24, 9.3], [22, 3, true, 21, 0, 14.08, 14.8], [23, 1, true, 16, 0, 10.77, 10.9], [24, 2, true, 18, 0, 10.48, 10.6], [25, 2, true, 18, 0, 12.44, 12.5], [26, 3, true, 21, 0, 16.53, 17.2], [27, 1, true, 21, 0, 8.7, 9.4], [28, 2, true, 21, 0, 10.25, 11.0], [29, 3, true, 20, 0, 12.41, 12.6], [30, 1, true, 20, 0, 9.5, 9.7], [31, 2, true, 24, 0, 10.21, 11.1], [32, 3, true, 18, 0, 10.27, 10.5], [33, 3, true, 22, 0, 9.24, 9.8], [34, 1, true, 18, 0, 6.87, 7.0], [35, 1, true, 18, 0, 6.64, 7.1], [36, 2, true, 20, 0, 5.44, 5.6], [37, 1, true, 18, 0, 4.83, 5.0], [38, 1, true, 20, 0, 3.83, 3.9], [39, 3, true, 22, 0, 3.0, 3.1]]
\ No newline at end of file
```

</details>

<a id="C029"></a>
### C029 · Model sample markers as lander occluders (seed 549 send failure)

Commit `8a6f698e81f70f6a43637556c64adc9594818477`; parents: fc2cc208a203b360625355d2632e312e9e5ac788. Recorded author date: 2026-10-01T12:29:04+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E1239](01_timeline.md#E1239): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C029_8a6f698_approach.py) · [Exact all-file diff](evidence/diffs/C029_8a6f698.diff)

[Previous saved controller snapshot](evidence/versions/C028_fc2cc20_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e970e9a..c27d16f 100644
--- a/approach.py
+++ b/approach.py
@@ -27,6 +27,8 @@ ROT_IMG = 4.0
   27     27  FINE_RES = 0.025
   28     28  PILLAR_INFL_OBJ = 0.015
   29     29  PILLAR_INFL_LAND = 0.04
          30 +LANDER_HALF = 0.06
          31 +SAMPLE_OCC_H = 0.045
   30     32  ROVER_OCC_R = 0.26
   31     33  CAM_OFF = (-0.087, -0.0125)
   32     34  OBJ_BACK_DEG = 108.0     # if |rel bearing| > this, pillars don't occlude objectives
@@ -239,6 +241,18 @@ class RoverPlanner:
  239    241                  e = PILLAR_INFL_LAND
  240    242                  occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
  241    243                  occ |= seg_hits_box(cx_, cy_, lx, ly, cx, cy, ax + e, ay + e)
         244 +            # sample markers occlude the lander (ray ends at lander box boundary)
         245 +            for sm in scene.samples:
         246 +                if abs(sm["x"] - lx) > 4.2 or abs(sm["y"] - ly) > 4.2:
         247 +                    continue
         248 +                for (ppx, ppy) in ((X, Y), (cx_, cy_)):
         249 +                    ddx = ppx - lx
         250 +                    ddy = ppy - ly
         251 +                    tt = LANDER_HALF / np.maximum(np.maximum(np.abs(ddx), np.abs(ddy)), 1e-9)
         252 +                    ex = lx + tt * ddx
         253 +                    ey = ly + tt * ddy
         254 +                    occ |= seg_hits_box(ppx, ppy, ex, ey, sm["x"], sm["y"],
         255 +                                        SAMPLE_OCC_H, SAMPLE_OCC_H)
  242    256              if USE_BACK_LAND:
  243    257                  rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - hh))
  244    258                  back = rel > math.radians(LAND_BACK_DEG)
diff --git a/dbg10.py b/dbg10.py
new file mode 100644
index 0000000..2ef0507
--- /dev/null
+++ b/dbg10.py
@@ -0,0 +1,16 @@
           1 +import sys
           2 +from test_approach import *
           3 +import numpy as np
           4 +seed=int(sys.argv[1]); N=int(sys.argv[2])
           5 +env = make_env(); obs, info = env.reset(seed=seed)
           6 +ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +def show(o):
           8 +    for n in sorted(o.get_object_names()):
           9 +        if n.startswith(('rover','lander','sample','objective')):
          10 +            ob=o.get_object_from_name(n); print(" ",n, dict(zip(o.type_features[ob.type], np.round(o.data[ob],3))))
          11 +for t in range(N):
          12 +    a=ap.get_action(obs); obs,r,term,tr,info=env.step(a)
          13 +print("t",N); 
          14 +try: show(obs)
          15 +except Exception as e: print(e); print(obs)
          16 +print(info)
diff --git a/probe549.py b/probe549.py
new file mode 100644
index 0000000..600b1ee
--- /dev/null
+++ b/probe549.py
@@ -0,0 +1,25 @@
           1 +import sys, numpy as np
           2 +from test_approach import *
           3 +from concurrent.futures import ThreadPoolExecutor
           4 +def trial(tx,ty):
           5 +    env = make_env(); obs, info = env.reset(seed=549)
           6 +    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +    for t in range(12):
           8 +        obs,*_=env.step(ap.get_action(obs))
           9 +    r0=obs.get_object_from_name('rover0')
          10 +    for k in range(40):
          11 +        x,y=obs.get(r0,'x'),obs.get(r0,'y')
          12 +        d=np.array([tx-x,ty-y])
          13 +        if np.abs(d).max()<1e-6: break
          14 +        a=np.zeros(8,dtype=np.float32); a[:2]=np.clip(d,-0.2,0.2); a[3]=0.1667; a[7]=0.1667
          15 +        obs,*_=env.step(a)
          16 +        nx,ny=obs.get(r0,'x'),obs.get(r0,'y')
          17 +        if abs(nx-x)+abs(ny-y)<1e-9: return (tx,ty,'blocked',round(x,3),round(y,3))
          18 +    a=np.zeros(8,dtype=np.float32); a[3]=0.5; a[7]=0.1667
          19 +    obs,*_=env.step(a)
          20 +    s=[obs.get(obs.get_object_from_name(f'sample{i}'),'received_analysis') for i in (1,4)]
          21 +    env.close()
          22 +    return (tx,ty,s)
          23 +pts=[(x,y) for x in (0.4,1.0,1.6,2.2) for y in (-2.2,-1.8,-1.4,-1.0,-0.6,-0.2,0.2,0.6)]
          24 +with ThreadPoolExecutor(8) as ex:
          25 +    for r in ex.map(lambda p: trial(*p), pts): print(r)
diff --git a/res_final.json b/res_final.json
new file mode 100644
index 0000000..f5c983e
--- /dev/null
+++ b/res_final.json
@@ -0,0 +1 @@
           1 +[[400, 3, true, 20, 0, 14.64, 14.8], [401, 2, true, 20, 0, 11.97, 12.1], [402, 3, true, 24, 0, 3.37, 3.6], [403, 2, true, 19, 0, 7.56, 7.7], [404, 3, true, 21, 0, 16.77, 16.9], [405, 2, true, 22, 0, 8.48, 8.6], [406, 3, true, 21, 0, 14.31, 14.4], [407, 1, true, 19, 0, 8.35, 8.5], [408, 2, true, 21, 0, 8.71, 8.9], [409, 1, true, 16, 0, 10.76, 11.2], [410, 2, true, 20, 0, 9.3, 10.6], [411, 1, true, 21, 0, 8.45, 9.8], [412, 3, true, 21, 0, 13.45, 14.1], [413, 1, true, 18, 0, 10.19, 10.3], [414, 3, true, 20, 0, 11.42, 12.1], [415, 2, true, 19, 0, 9.7, 9.8], [416, 2, true, 20, 0, 8.28, 9.1], [417, 1, true, 18, 0, 6.43, 7.7], [418, 2, true, 18, 0, 8.39, 8.8], [419, 3, true, 21, 0, 11.07, 11.2], [420, 2, true, 18, 0, 8.62, 9.1], [421, 1, true, 18, 0, 7.6, 8.6], [422, 1, true, 17, 0, 6.04, 6.2], [423, 2, true, 18, 0, 7.92, 8.0], [424, 1, true, 16, 0, 9.1, 9.2], [425, 1, true, 20, 0, 8.76, 8.9], [426, 1, true, 18, 0, 8.36, 8.8], [427, 3, true, 23, 0, 13.34, 13.6], [428, 1, true, 20, 0, 6.83, 7.0], [429, 1, true, 20, 0, 9.76, 9.9], [430, 1, true, 18, 0, 9.26, 9.4], [431, 3, true, 21, 0, 11.46, 11.7], [432, 3, true, 20, 0, 11.19, 11.4], [433, 1, true, 19, 0, 9.93, 10.0], [434, 3, true, 20, 0, 10.98, 11.1], [435, 2, true, 20, 0, 10.29, 10.4], [436, 3, true, 22, 0, 9.32, 9.5], [437, 2, true, 18, 0, 10.63, 10.8], [438, 3, true, 27, 0, 11.36, 11.7], [439, 2, true, 19, 0, 8.21, 8.9], [440, 1, true, 18, 0, 9.34, 9.4], [441, 2, true, 19, 0, 9.95, 10.1], [442, 2, true, 19, 0, 10.08, 10.8], [443, 1, true, 18, 0, 7.88, 8.1], [444, 3, true, 25, 0, 12.38, 13.0], [445, 1, true, 16, 0, 9.24, 10.0], [446, 1, true, 19, 0, 8.37, 8.5], [447, 2, true, 20, 0, 9.89, 10.4], [448, 3, true, 20, 0, 8.86, 9.3], [449, 3, true, 20, 0, 8.08, 8.6], [450, 1, true, 25, 0, 7.6, 8.7], [451, 3, true, 25, 0, 13.39, 13.5], [452, 2, true, 20, 0, 10.22, 10.3], [453, 3, true, 20, 0, 12.79, 13.5], [454, 2, true, 25, 0, 10.24, 10.5], [455, 3, true, 24, 0, 12.05, 13.0], [456, 2, true, 17, 0, 9.87, 10.2], [457, 1, true, 23, 0, 9.09, 9.3], [458, 1, true, 28, 0, 6.39, 7.2], [459, 2, true, 18, 0, 12.06, 12.2], [460, 1, true, 18, 0, 8.68, 8.8], [461, 3, true, 19, 0, 13.72, 13.9], [462, 2, true, 19, 0, 9.57, 10.3], [463, 3, true, 20, 0, 14.9, 17.3], [464, 1, true, 20, 0, 13.99, 14.1], [465, 1, true, 16, 0, 10.81, 11.3], [466, 2, true, 20, 0, 12.64, 13.7], [467, 1, true, 18, 0, 7.53, 8.3], [468, 1, true, 20, 0, 8.58, 9.2], [469, 1, true, 18, 0, 8.02, 8.3], [470, 3, true, 21, 0, 9.63, 10.7], [471, 1, true, 19, 0, 8.46, 8.7], [472, 1, true, 16, 0, 6.36, 7.2], [473, 1, true, 21, 0, 9.9, 10.0], [474, 1, true, 18, 0, 10.04, 10.5], [475, 2, true, 21, 0, 9.18, 9.3], [476, 3, true, 19, 0, 12.03, 12.2], [477, 2, true, 18, 0, 12.45, 12.6], [478, 1, true, 20, 0, 8.08, 8.2], [479, 3, true, 20, 0, 14.46, 14.6], [480, 3, true, 19, 0, 15.34, 15.5], [481, 2, true, 21, 0, 11.91, 12.4], [482, 1, true, 19, 0, 9.87, 10.3], [483, 1, true, 21, 0, 10.17, 10.7], [484, 3, true, 20, 0, 14.83, 15.1], [485, 3, true, 20, 0, 14.08, 14.2], [486, 2, true, 20, 0, 10.58, 10.8], [487, 2, true, 27, 0, 11.16, 12.2], [488, 3, true, 20, 0, 11.1, 12.4], [489, 3, true, 19, 0, 11.19, 12.5], [490, 2, true, 19, 0, 8.42, 8.6], [491, 2, true, 18, 0, 10.13, 11.5], [492, 3, true, 22, 0, 8.23, 9.7], [493, 3, true, 20, 0, 10.22, 10.4], [494, 2, true, 23, 0, 6.15, 6.8], [495, 1, true, 20, 0, 8.57, 8.7], [496, 1, true, 18, 0, 8.86, 8.9], [497, 1, true, 22, 0, 8.34, 8.7], [498, 2, true, 19, 0, 6.75, 6.8], [499, 3, true, 23, 0, 10.88, 11.6], [500, 2, true, 23, 0, 10.3, 10.5], [501, 3, true, 20, 0, 12.28, 12.4], [502, 1, true, 18, 0, 6.14, 6.2], [503, 1, true, 17, 0, 9.56, 9.7], [504, 3, true, 20, 0, 18.11, 18.2], [505, 3, true, 24, 0, 12.74, 13.5], [506, 2, true, 20, 0, 12.02, 12.1], [507, 3, true, 21, 0, 10.43, 10.7], [508, 2, true, 23, 0, 9.54, 9.7], [509, 3, true, 19, 0, 15.05, 15.6], [510, 1, true, 22, 0, 12.92, 13.0], [511, 3, true, 25, 0, 14.82, 15.0], [512, 2, true, 23, 0, 15.98, 16.6], [513, 3, true, 21, 0, 18.42, 18.6], [514, 3, true, 21, 0, 16.85, 17.0], [515, 1, true, 18, 0, 14.41, 14.5], [516, 1, true, 18, 0, 10.1, 10.2], [517, 2, true, 24, 0, 13.06, 13.2], [518, 1, true, 26, 0, 14.5, 14.7], [519, 3, true, 23, 0, 15.64, 16.1], [520, 1, true, 16, 0, 12.74, 12.8], [521, 1, true, 25, 0, 9.91, 10.1], [522, 2, true, 21, 0, 13.17, 13.3], [523, 1, true, 20, 0, 12.25, 12.9], [524, 1, true, 18, 0, 11.88, 12.3], [525, 3, true, 22, 0, 14.58, 14.7], [526, 2, true, 23, 0, 13.35, 13.7], [527, 3, true, 20, 0, 12.04, 12.7], [528, 1, true, 18, 0, 7.72, 8.3], [529, 1, true, 17, 0, 10.1, 11.2], [530, 1, true, 21, 0, 7.78, 8.0], [531, 2, true, 23, 0, 10.8, 10.9], [532, 3, true, 22, 0, 12.18, 12.3], [533, 2, true, 21, 0, 10.46, 10.6], [534, 3, true, 22, 0, 16.36, 16.5], [535, 1, true, 18, 0, 9.86, 10.2], [536, 3, true, 22, 0, 17.48, 17.6], [537, 1, true, 16, 0, 10.42, 10.8], [538, 1, true, 18, 0, 10.13, 10.8], [539, 1, true, 18, 0, 7.26, 7.4], [540, 1, true, 17, 0, 9.86, 9.9], [541, 2, true, 17, 0, 11.85, 12.5], [542, 3, true, 25, 0, 11.13, 11.3], [543, 3, true, 20, 0, 10.94, 11.2], [544, 1, true, 18, 0, 7.67, 8.3], [545, 2, true, 18, 0, 10.55, 11.3], [546, 1, true, 18, 0, 9.33, 9.5], [547, 1, true, 18, 0, 8.57, 8.7], [548, 2, true, 20, 0, 11.05, 11.2], [549, 2, false, 1000, 987, 10.3, 60.0], [550, 3, true, 27, 0, 9.16, 9.7], [551, 1, true, 27, 0, 8.66, 9.5], [552, 1, true, 16, 0, 7.91, 8.4], [553, 2, true, 19, 0, 6.66, 7.7], [554, 2, true, 20, 0, 9.85, 10.0], [555, 2, true, 20, 0, 6.76, 6.9], [556, 2, true, 19, 0, 8.0, 8.1], [557, 2, true, 19, 0, 7.78, 9.4], [558, 2, true, 18, 0, 6.59, 7.3], [559, 1, true, 19, 0, 5.89, 6.9], [560, 3, true, 21, 0, 8.6, 8.8], [561, 1, true, 21, 0, 8.24, 8.8], [562, 1, true, 16, 0, 7.62, 7.7], [563, 1, true, 18, 0, 8.82, 8.9], [564, 1, true, 19, 0, 8.32, 8.6], [565, 3, true, 20, 0, 13.84, 14.0], [566, 2, true, 18, 0, 10.39, 10.7], [567, 1, true, 20, 0, 8.52, 8.7], [568, 3, true, 20, 0, 11.88, 12.0], [569, 1, true, 27, 0, 8.57, 8.7], [570, 1, true, 20, 0, 6.61, 7.4], [571, 3, true, 20, 0, 9.43, 9.5], [572, 2, true, 16, 0, 9.01, 9.1], [573, 3, true, 22, 0, 11.88, 12.1], [574, 1, true, 29, 0, 6.84, 7.0], [575, 3, true, 20, 0, 8.53, 8.9], [576, 1, true, 27, 0, 7.17, 7.3], [577, 2, true, 19, 0, 7.86, 8.6], [578, 3, true, 21, 0, 9.2, 9.4], [579, 3, true, 22, 0, 8.33, 8.5], [580, 1, true, 18, 0, 8.49, 8.7], [581, 1, true, 23, 0, 6.71, 7.0], [582, 3, true, 21, 0, 10.31, 11.4], [583, 1, true, 16, 0, 9.27, 9.5], [584, 1, true, 18, 0, 9.22, 9.9], [585, 1, true, 16, 0, 8.1, 8.3], [586, 3, true, 20, 0, 9.31, 9.5], [587, 3, true, 21, 0, 11.41, 11.5], [588, 1, true, 18, 0, 5.5, 6.0], [589, 2, true, 20, 0, 7.03, 7.3], [590, 2, true, 21, 0, 10.17, 10.5], [591, 1, true, 19, 0, 9.14, 9.2], [592, 2, true, 16, 0, 9.41, 9.5], [593, 3, true, 20, 0, 12.96, 13.1], [594, 2, true, 27, 0, 10.48, 10.6], [595, 3, true, 19, 0, 10.49, 10.6], [596, 3, true, 20, 0, 9.85, 10.0], [597, 3, true, 20, 0, 9.77, 10.1], [598, 1, true, 19, 0, 6.1, 6.5], [599, 3, true, 21, 0, 5.34, 5.5]]
\ No newline at end of file
diff --git a/res_n2.json b/res_n2.json
new file mode 100644
index 0000000..ce29b25
--- /dev/null
+++ b/res_n2.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 7.12, 7.3], [1, 2, true, 18, 0, 5.53, 5.7], [2, 3, true, 19, 0, 15.7, 16.7], [3, 3, true, 21, 0, 12.71, 12.8], [4, 3, true, 20, 0, 14.83, 15.5], [5, 3, true, 23, 0, 15.55, 16.7], [6, 2, true, 19, 0, 12.86, 13.0], [7, 3, true, 22, 0, 15.69, 15.9], [8, 3, true, 20, 0, 13.02, 13.6], [9, 2, true, 22, 0, 12.58, 12.8], [10, 3, true, 20, 0, 16.29, 16.4], [11, 1, true, 19, 0, 8.54, 8.6], [12, 2, true, 22, 0, 10.1, 10.2], [13, 3, true, 23, 0, 16.09, 16.3], [14, 1, true, 29, 0, 9.31, 9.5], [15, 3, true, 23, 0, 15.59, 15.9], [16, 2, true, 21, 0, 11.93, 12.0], [17, 3, true, 22, 0, 17.74, 17.8], [18, 3, true, 22, 0, 12.25, 12.4], [19, 2, true, 25, 0, 7.77, 7.9], [20, 3, true, 27, 0, 9.13, 9.3], [21, 1, true, 19, 0, 7.73, 7.9], [22, 3, true, 21, 0, 7.54, 7.7], [23, 1, true, 16, 0, 4.34, 4.4]]
\ No newline at end of file
```

</details>

<a id="C030"></a>
### C030 · Blacklist positions where send/img/cal failed, to avoid replan loops

Commit `275ec8a79f49940bc6be53a36f0ea715367a5367`; parents: 8a6f698e81f70f6a43637556c64adc9594818477. Recorded author date: 2026-10-01T12:29:26+02:00.

File roles (automatic): policy.

- [E1253](01_timeline.md#E1253): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C030_275ec8a_approach.py) · [Exact all-file diff](evidence/diffs/C030_275ec8a.diff)

[Previous saved controller snapshot](evidence/versions/C029_8a6f698_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c27d16f..381b531 100644
--- a/approach.py
+++ b/approach.py
@@ -176,8 +176,9 @@ class RoverPlanner:
  176    176          for (cx, cy, ax, ay) in scene.mounds:
  177    177              free &= box_dist(X, Y, cx, cy, ax, ay) > MOUND_R
  178    178          free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
  179        -        for (bx, by) in bad:
  180        -            free &= np.hypot(X - bx, Y - by) > 0.03
         179 +        for b in bad:
         180 +            if len(b) == 2:
         181 +                free &= np.hypot(X - b[0], Y - b[1]) > 0.03
  181    182          free[self.hi, self.hj] = True
  182    183          self.free = free
  183    184          self.home_reg = (np.hypot(X - hx, Y - hy) <= HOME_R) & free
@@ -264,6 +265,16 @@ class RoverPlanner:
  264    265                  occ2 |= seg_hits_disk(cx_, cy_, lx, ly, px, py, ROVER_OCC_R)
  265    266              land &= v & ((~occ) | back) & ~occ2
  266    267              land_free &= v & ((~occ) | back)
         268 +        for b in bad:
         269 +            if len(b) == 4:
         270 +                near = np.hypot(X - b[0], Y - b[1]) <= 0.08
         271 +                if b[2] == "send":
         272 +                    land &= ~near
         273 +                    land_free &= ~near
         274 +                elif b[2] == "img" and b[3] is not None and b[3] < len(self.vis):
         275 +                    self.vis[b[3]] = self.vis[b[3]] & ~near
         276 +                elif b[2] == "cal":
         277 +                    self.any_vis &= ~near
  267    278          self.land = land
  268    279          self.land_free = land_free
  269    280          self.camx_i, self.camy_i = camx_i, camy_i
@@ -735,6 +746,9 @@ class GeneratedApproach:
  735    746                  for s in sc.samples:
  736    747                      if s["an"][ri] and not s["recv"]:
  737    748                          dev = True
         749 +            if dev and op in ("send", "img", "cal") and \
         750 +                    abs(r["x"] - e[0]) <= 1e-3 and abs(r["y"] - e[1]) <= 1e-3:
         751 +                self.bad[ri].append((e[0], e[1], op, arg))
  738    752              if dev:
  739    753                  self.log.append(("dev", ri, e, round(r["x"], 3), round(r["y"], 3), r["cal"], pr["cal"],
  740    754                                   [ob["img"][ri] for ob in sc.objectives]))
```

</details>

<a id="C031"></a>
### C031 · results 400-600 after sample-occluder fix

Commit `9ade333fdee63709cd996e6ba0493fc76b56b19e`; parents: 275ec8a79f49940bc6be53a36f0ea715367a5367. Recorded author date: 2026-10-01T12:39:41+02:00.

File roles (automatic): setup/other.

- [E1294](01_timeline.md#E1294): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C031_9ade333.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/res_b.json b/res_b.json
new file mode 100644
index 0000000..ba4c134
--- /dev/null
+++ b/res_b.json
@@ -0,0 +1 @@
           1 +[[400, 3, true, 20, 0, 12.26, 12.4], [401, 2, true, 20, 0, 16.25, 16.4], [402, 3, true, 24, 0, 12.99, 13.1], [403, 2, true, 19, 0, 12.09, 12.2], [404, 3, true, 21, 0, 19.49, 19.6], [405, 2, true, 22, 0, 13.27, 13.5], [406, 3, true, 21, 0, 18.09, 18.5], [407, 1, true, 19, 0, 8.97, 9.1], [408, 2, true, 21, 0, 13.51, 13.6], [409, 1, true, 16, 0, 16.24, 16.7], [410, 2, true, 20, 0, 14.87, 15.0], [411, 1, true, 21, 0, 14.56, 14.7], [412, 3, true, 21, 0, 20.29, 20.4], [413, 1, true, 18, 0, 13.93, 14.1], [414, 3, true, 20, 0, 16.98, 17.3], [415, 2, true, 19, 0, 15.55, 16.0], [416, 2, true, 20, 0, 14.92, 15.0], [417, 1, true, 18, 0, 11.88, 12.0], [418, 2, true, 18, 0, 13.96, 14.1], [419, 3, true, 21, 0, 17.57, 17.7], [420, 2, true, 18, 0, 14.92, 15.0], [421, 1, true, 18, 0, 15.86, 16.0], [422, 1, true, 17, 0, 12.31, 12.4], [423, 2, true, 18, 0, 16.63, 16.7], [424, 1, true, 16, 0, 15.64, 15.9], [425, 1, true, 20, 0, 15.38, 15.5], [426, 1, true, 18, 0, 15.03, 15.1], [427, 3, true, 23, 0, 21.21, 21.5], [428, 1, true, 20, 0, 14.35, 14.5], [429, 1, true, 20, 0, 16.31, 16.4], [430, 1, true, 18, 0, 15.72, 16.0], [431, 3, true, 21, 0, 18.4, 18.9], [432, 3, true, 20, 0, 17.78, 17.9], [433, 1, true, 19, 0, 14.24, 14.3], [434, 3, true, 20, 0, 14.7, 15.3], [435, 2, true, 20, 0, 16.67, 16.8], [436, 3, true, 22, 0, 15.78, 15.9], [437, 2, true, 18, 0, 16.87, 17.0], [438, 3, true, 27, 0, 16.09, 16.2], [439, 2, true, 19, 0, 15.59, 15.8], [440, 1, true, 18, 0, 15.49, 15.6], [441, 2, true, 19, 0, 15.93, 16.0], [442, 2, true, 19, 0, 16.7, 16.9], [443, 1, true, 18, 0, 15.16, 15.3], [444, 3, true, 25, 0, 18.6, 19.6], [445, 1, true, 16, 0, 14.86, 15.0], [446, 1, true, 19, 0, 14.94, 15.2], [447, 2, true, 20, 0, 16.81, 16.9], [448, 3, true, 20, 0, 16.15, 16.3], [449, 3, true, 20, 0, 14.51, 14.7], [450, 1, true, 25, 0, 13.26, 14.1], [451, 3, true, 25, 0, 18.22, 18.3], [452, 2, true, 20, 0, 14.01, 14.1], [453, 3, true, 20, 0, 16.48, 16.6], [454, 2, true, 25, 0, 15.24, 15.4], [455, 3, true, 24, 0, 16.5, 16.6], [456, 2, true, 17, 0, 14.05, 14.4], [457, 1, true, 23, 0, 13.96, 14.3], [458, 1, true, 28, 0, 9.9, 10.1], [459, 2, true, 18, 0, 13.61, 13.7], [460, 1, true, 18, 0, 12.6, 12.7], [461, 3, true, 19, 0, 16.38, 16.7], [462, 2, true, 19, 0, 12.32, 12.4], [463, 3, true, 20, 0, 17.61, 17.9], [464, 1, true, 20, 0, 17.08, 18.2], [465, 1, true, 16, 0, 12.56, 12.6], [466, 2, true, 20, 0, 16.01, 17.6], [467, 1, true, 18, 0, 12.32, 12.5], [468, 1, true, 20, 0, 19.27, 19.4], [469, 1, true, 18, 0, 20.73, 20.9], [470, 3, true, 21, 0, 25.0, 26.6], [471, 1, true, 19, 0, 24.11, 24.3], [472, 1, true, 16, 0, 20.29, 21.4], [473, 1, true, 21, 0, 28.84, 29.2], [474, 1, true, 18, 0, 28.9, 30.3], [475, 2, true, 21, 0, 25.98, 27.2], [476, 3, true, 19, 0, 32.34, 32.5], [477, 2, true, 18, 0, 31.41, 31.7], [478, 1, true, 20, 0, 20.55, 20.8], [479, 3, true, 20, 0, 36.53, 36.7], [480, 3, true, 19, 0, 38.09, 38.6], [481, 2, true, 21, 0, 29.07, 29.2], [482, 1, true, 19, 0, 28.65, 29.5], [483, 1, true, 21, 0, 30.83, 31.0], [484, 3, true, 20, 0, 38.94, 39.1], [485, 3, true, 20, 0, 36.72, 36.9], [486, 2, true, 20, 0, 31.84, 32.0], [487, 2, true, 27, 0, 27.45, 28.0], [488, 3, true, 20, 0, 27.91, 28.0], [489, 3, true, 19, 0, 28.61, 28.7], [490, 2, true, 19, 0, 23.96, 24.0], [491, 2, true, 18, 0, 23.88, 24.5], [492, 3, true, 22, 0, 17.2, 17.9], [493, 3, true, 20, 0, 18.48, 18.6], [494, 2, true, 23, 0, 14.79, 14.9], [495, 1, true, 20, 0, 15.99, 16.1], [496, 1, true, 18, 0, 16.16, 16.3], [497, 1, true, 22, 0, 15.73, 15.9], [498, 2, true, 19, 0, 13.67, 14.0], [499, 3, true, 23, 0, 18.02, 18.2], [500, 2, true, 23, 0, 19.56, 19.7], [501, 3, true, 20, 0, 21.69, 21.9], [502, 1, true, 18, 0, 17.06, 17.8], [503, 1, true, 17, 0, 18.62, 18.7], [504, 3, true, 20, 0, 25.88, 26.0], [505, 3, true, 24, 0, 21.93, 22.1], [506, 2, true, 20, 0, 21.76, 22.7], [507, 3, true, 21, 0, 17.92, 18.8], [508, 2, true, 23, 0, 13.38, 13.6], [509, 3, true, 19, 0, 22.2, 22.7], [510, 1, true, 22, 0, 19.96, 20.1], [511, 3, true, 25, 0, 20.68, 20.9], [512, 2, true, 23, 0, 22.42, 23.6], [513, 3, true, 21, 0, 25.33, 25.5], [514, 3, true, 21, 0, 21.59, 22.1], [515, 1, true, 18, 0, 19.78, 21.2], [516, 1, true, 18, 0, 17.01, 17.1], [517, 2, true, 24, 0, 19.04, 19.2], [518, 1, true, 26, 0, 20.03, 20.3], [519, 3, true, 23, 0, 21.74, 21.9], [520, 1, true, 16, 0, 17.9, 18.0], [521, 1, true, 25, 0, 15.14, 15.4], [522, 2, true, 21, 0, 19.27, 19.8], [523, 1, true, 20, 0, 17.62, 17.7], [524, 1, true, 18, 0, 16.7, 16.8], [525, 3, true, 22, 0, 16.98, 17.1], [526, 2, true, 23, 0, 16.47, 16.9], [527, 3, true, 20, 0, 17.7, 17.8], [528, 1, true, 18, 0, 11.68, 11.9], [529, 1, true, 17, 0, 12.69, 12.9], [530, 1, true, 21, 0, 10.47, 10.6], [531, 2, true, 23, 0, 16.34, 16.5], [532, 3, true, 22, 0, 17.61, 17.7], [533, 2, true, 21, 0, 12.58, 12.7], [534, 3, true, 22, 0, 20.27, 21.1], [535, 1, true, 18, 0, 14.76, 14.9], [536, 3, true, 22, 0, 19.24, 21.0], [537, 1, true, 16, 0, 14.97, 15.1], [538, 1, true, 18, 0, 15.33, 15.9], [539, 1, true, 18, 0, 10.85, 11.0], [540, 1, true, 17, 0, 13.78, 13.9], [541, 2, true, 17, 0, 13.96, 14.0], [542, 3, true, 25, 0, 15.11, 15.2], [543, 3, true, 20, 0, 14.67, 14.8], [544, 1, true, 18, 0, 10.79, 11.3], [545, 2, true, 18, 0, 17.09, 17.9], [546, 1, true, 22, 0, 16.14, 16.3], [547, 1, true, 18, 0, 16.25, 16.5], [548, 2, true, 20, 0, 16.77, 16.9], [549, 2, true, 21, 0, 14.58, 15.4], [550, 3, true, 27, 0, 15.18, 15.4], [551, 1, true, 27, 0, 16.04, 16.2], [552, 1, true, 16, 0, 16.98, 17.1], [553, 2, true, 19, 0, 16.92, 17.1], [554, 2, true, 20, 0, 21.77, 22.0], [555, 2, true, 20, 0, 19.01, 19.2], [556, 2, true, 19, 0, 20.41, 21.5], [557, 2, true, 19, 0, 19.82, 21.8], [558, 2, true, 18, 0, 15.58, 17.6], [559, 1, true, 19, 0, 14.53, 16.8], [560, 3, true, 21, 0, 18.47, 18.6], [561, 1, true, 21, 0, 17.11, 17.2], [562, 1, true, 16, 0, 16.79, 16.9], [563, 1, true, 18, 0, 17.18, 17.3], [564, 1, true, 19, 0, 18.41, 18.5], [565, 3, true, 20, 0, 23.6, 23.7], [566, 2, true, 18, 0, 19.12, 19.3], [567, 1, true, 20, 0, 17.73, 17.9], [568, 3, true, 20, 0, 21.02, 21.2], [569, 1, true, 27, 0, 20.0, 20.5], [570, 1, true, 20, 0, 17.27, 18.3], [571, 3, true, 20, 0, 24.62, 25.1], [572, 2, true, 16, 0, 26.54, 27.4], [573, 3, true, 22, 0, 29.05, 29.4], [574, 1, true, 29, 0, 16.55, 17.0], [575, 3, true, 20, 0, 18.7, 19.1], [576, 1, true, 27, 0, 19.14, 19.5], [577, 2, true, 19, 0, 22.95, 23.3], [578, 3, true, 21, 0, 25.97, 26.7], [579, 3, true, 22, 0, 19.32, 19.7], [580, 1, true, 18, 0, 21.53, 21.8], [581, 1, true, 23, 0, 14.08, 15.1], [582, 3, true, 21, 0, 32.86, 33.8], [583, 1, true, 16, 0, 26.08, 26.4], [584, 1, true, 18, 0, 18.42, 18.7], [585, 1, true, 16, 0, 26.76, 27.0], [586, 3, true, 20, 0, 22.12, 22.4], [587, 3, true, 21, 0, 37.76, 38.1], [588, 1, true, 18, 0, 16.0, 16.3], [589, 2, true, 20, 0, 23.65, 24.0], [590, 2, true, 21, 0, 23.05, 23.5], [591, 1, true, 19, 0, 31.19, 31.5], [592, 2, true, 16, 0, 20.87, 21.2], [593, 3, true, 20, 0, 35.24, 35.5], [594, 2, true, 27, 0, 20.57, 21.0], [595, 3, true, 19, 0, 29.54, 29.8], [596, 3, true, 20, 0, 27.87, 28.2], [597, 3, true, 20, 0, 24.51, 24.7], [598, 1, true, 19, 0, 18.63, 18.8], [599, 3, true, 21, 0, 15.42, 15.7]]
\ No newline at end of file
```

</details>

<a id="C032"></a>
### C032 · notes

Commit `d7dabcd704f0fea8efcd3cc1a4991180e75b9f38`; parents: 9ade333fdee63709cd996e6ba0493fc76b56b19e. Recorded author date: 2026-10-01T12:53:07+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0047](01_timeline.md#E0047): commit title in command; output may not confirm creation.
- [E0450](01_timeline.md#E0450): commit title in command; output may not confirm creation.
- [E0524](01_timeline.md#E0524): commit title in command; output may not confirm creation.
- [E0611](01_timeline.md#E0611): commit title in command; output may not confirm creation.
- [E1141](01_timeline.md#E1141): commit title in command; output may not confirm creation.
- [E1363](01_timeline.md#E1363): commit title in command; output may not confirm creation.
- [E1464](01_timeline.md#E1464): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C032_d7dabcd.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/NOTES.md b/NOTES.md
index c1e6ef5..6049a68 100644
--- a/NOTES.md
+++ b/NOTES.md
@@ -33,3 +33,9 @@
   33     33  - Per-rover coarse grid (0.05) staged BFS over task orders (DFS trie), joint assignment min makespan,
   34     34    top-K realised on fine grid (0.025) with time-aware send vs other rover trajectory; replan on deviation.
   35     35  - Results: seeds 0-400 all solved, mean 20.475 steps.
          36 +
          37 +## Sample markers near lander (seeds 549, 706)
          38 +- Samples lying within ~0.05 of the lander can occlude sends in strange bearing ranges (probably a 3D raycast). This is rare (~2/800 seeds have a sample within 0.05).
          39 +- Model: each sample is a box (half 0.045) occluding the ray cam->lander, with the ray trimmed at the lander box (half 0.06). This fixed 549 but did not predict 706.
          40 +- Robustness: failed send/img/cal positions are added to self.bad as (x,y,op,arg). The planner then excludes land/vis/any_vis within 0.08 of them, so a replan won't retry the same spot. 706 is now solved in 32 steps, with 2 replans.
          41 +- Results: seeds 400-600 200/200 (mean 20.185); 600-800 200/200 (mean 20.57). Single-thread worst plan time ~7s.
diff --git a/cnt_near.py b/cnt_near.py
new file mode 100644
index 0000000..2b23c02
--- /dev/null
+++ b/cnt_near.py
@@ -0,0 +1,9 @@
           1 +from test_approach import make_env
           2 +import numpy as np
           3 +env=make_env(); c=[]
           4 +for s in range(0,800,4):
           5 +    o,_=env.reset(seed=s)
           6 +    T=o.get_object_from_name('sample0').type
           7 +    d=min(np.hypot(o.get(x,'x')+1.9,o.get(x,'y')+2.0) for x in o.get_objects(T))
           8 +    if d<0.3: c.append((s,round(d,3)))
           9 +print(len(c),c)
diff --git a/probe_occ.py b/probe_occ.py
new file mode 100644
index 0000000..437acbe
--- /dev/null
+++ b/probe_occ.py
@@ -0,0 +1,27 @@
           1 +import sys, numpy as np
           2 +from test_approach import *
           3 +from concurrent.futures import ThreadPoolExecutor
           4 +def trial(tx,ty):
           5 +    env = make_env(); obs, info = env.reset(seed=SEED)
           6 +    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
           7 +    for t in range(NST):
           8 +        obs,*_=env.step(ap.get_action(obs))
           9 +    r0=obs.get_object_from_name('rover0')
          10 +    for k in range(40):
          11 +        x,y=obs.get(r0,'x'),obs.get(r0,'y')
          12 +        d=np.array([tx-x,ty-y])
          13 +        if np.abs(d).max()<1e-6: break
          14 +        a=np.zeros(8,dtype=np.float32); a[:2]=np.clip(d,-0.2,0.2); a[3]=0.1667; a[7]=0.1667
          15 +        obs,*_=env.step(a)
          16 +        nx,ny=obs.get(r0,'x'),obs.get(r0,'y')
          17 +        if abs(nx-x)+abs(ny-y)<1e-9: return (tx,ty,'blocked',round(x,3),round(y,3))
          18 +    a=np.zeros(8,dtype=np.float32); a[3]=0.5; a[7]=0.1667
          19 +    obs,*_=env.step(a)
          20 +    s=[obs.get(o,'received_analysis') for o in obs.get_objects(obs.get_object_from_name('sample0').type)]+[obs.get(o,'received_image') for o in obs.get_objects(obs.get_object_from_name('objective0').type)]
          21 +    env.close()
          22 +    return (tx,ty,round(math.degrees(math.atan2(ty+2,tx+1.9)),1),max(s))
          23 +import math
          24 +SEED=int(sys.argv[1]); NST=int(sys.argv[2]); R=float(sys.argv[3])
          25 +pts=[(round(-1.9+R*math.cos(math.radians(b)),3), round(-2.0+R*math.sin(math.radians(b)),3)) for b in range(0,50,3)]
          26 +with ThreadPoolExecutor(8) as ex:
          27 +    for r in ex.map(lambda p: trial(*p), pts): print(r)
diff --git a/res_c.json b/res_c.json
new file mode 100644
index 0000000..573a024
--- /dev/null
+++ b/res_c.json
@@ -0,0 +1 @@
           1 +[[600, 1, true, 27, 0, 23.71, 24.2], [601, 1, true, 18, 0, 5.34, 7.0], [602, 1, true, 16, 0, 25.13, 25.5], [603, 1, true, 17, 0, 27.16, 27.4], [604, 1, true, 20, 0, 28.61, 30.4], [605, 1, true, 31, 0, 23.18, 23.9], [606, 3, true, 22, 0, 26.15, 27.3], [607, 3, true, 20, 0, 28.31, 30.3], [608, 2, true, 20, 0, 38.89, 39.2], [609, 3, true, 23, 0, 27.79, 29.9], [610, 2, true, 18, 0, 27.43, 28.5], [611, 3, true, 22, 0, 23.97, 24.4], [612, 3, true, 21, 0, 32.5, 33.4], [613, 2, true, 21, 0, 22.82, 25.7], [614, 3, true, 20, 0, 27.87, 28.2], [615, 3, true, 22, 0, 34.62, 35.1], [616, 2, true, 20, 0, 25.44, 25.8], [617, 2, true, 20, 0, 28.51, 28.9], [618, 1, true, 20, 0, 20.27, 22.6], [619, 2, true, 19, 0, 28.95, 29.3], [620, 3, true, 20, 0, 18.26, 18.7], [621, 1, true, 18, 0, 16.55, 17.8], [622, 2, true, 18, 0, 22.76, 24.1], [623, 3, true, 21, 0, 26.71, 27.8], [624, 1, true, 23, 0, 19.81, 20.3], [625, 2, true, 22, 0, 16.62, 17.1], [626, 3, true, 20, 0, 29.14, 29.6], [627, 3, true, 23, 0, 26.46, 26.8], [628, 1, true, 16, 0, 14.67, 15.8], [629, 3, true, 20, 0, 24.91, 25.4], [630, 2, true, 24, 0, 22.65, 24.4], [631, 1, true, 20, 0, 25.51, 26.1], [632, 2, true, 18, 0, 19.65, 20.0], [633, 2, true, 21, 0, 19.97, 20.3], [634, 2, true, 18, 0, 29.66, 30.0], [635, 3, true, 20, 0, 27.03, 27.5], [636, 1, true, 19, 0, 26.31, 27.6], [637, 1, true, 17, 0, 22.45, 24.0], [638, 3, true, 20, 0, 35.6, 35.9], [639, 3, true, 20, 0, 26.52, 26.7], [640, 3, true, 20, 0, 27.02, 27.3], [641, 3, true, 24, 0, 37.37, 38.0], [642, 1, true, 23, 0, 22.82, 23.1], [643, 2, true, 20, 0, 19.99, 20.3], [644, 2, true, 21, 0, 31.55, 31.9], [645, 1, true, 18, 0, 21.46, 21.7], [646, 2, true, 20, 0, 17.86, 18.1], [647, 1, true, 18, 0, 19.21, 19.5], [648, 1, true, 16, 0, 25.11, 25.3], [649, 2, true, 19, 0, 24.04, 24.2], [650, 3, true, 21, 0, 26.14, 26.4], [651, 3, true, 20, 0, 27.66, 28.0], [652, 2, true, 20, 0, 20.56, 21.2], [653, 1, true, 20, 0, 18.05, 18.1], [654, 1, true, 18, 0, 18.12, 18.2], [655, 1, true, 16, 0, 16.31, 16.4], [656, 1, true, 16, 0, 15.89, 16.0], [657, 1, true, 20, 0, 14.98, 15.1], [658, 2, true, 20, 0, 13.57, 13.7], [659, 3, true, 21, 0, 13.91, 14.0], [660, 2, true, 24, 0, 14.87, 15.0], [661, 1, true, 18, 0, 11.4, 11.5], [662, 2, true, 19, 0, 17.84, 18.0], [663, 3, true, 25, 0, 18.23, 20.1], [664, 2, true, 22, 0, 13.03, 13.5], [665, 3, true, 19, 0, 22.96, 23.5], [666, 3, true, 23, 0, 23.61, 23.8], [667, 2, true, 22, 0, 24.29, 24.6], [668, 2, true, 22, 0, 19.33, 19.5], [669, 3, true, 21, 0, 23.52, 23.9], [670, 1, true, 20, 0, 18.6, 19.3], [671, 1, true, 18, 0, 30.64, 31.0], [672, 3, true, 22, 0, 29.2, 29.4], [673, 3, true, 20, 0, 34.39, 34.7], [674, 3, true, 27, 0, 30.06, 30.5], [675, 2, true, 20, 0, 23.73, 23.9], [676, 1, true, 18, 0, 23.23, 23.4], [677, 1, true, 16, 0, 21.62, 22.4], [678, 2, true, 18, 0, 21.06, 21.8], [679, 2, true, 18, 0, 28.45, 28.8], [680, 3, true, 20, 0, 33.16, 34.7], [681, 3, true, 20, 0, 29.96, 30.3], [682, 3, true, 22, 0, 34.68, 35.1], [683, 3, true, 20, 0, 24.31, 24.7], [684, 1, true, 18, 0, 20.64, 21.0], [685, 3, true, 19, 0, 33.05, 33.8], [686, 3, true, 20, 0, 36.3, 37.3], [687, 3, true, 21, 0, 31.98, 32.3], [688, 1, true, 21, 0, 16.15, 17.5], [689, 1, true, 21, 0, 13.75, 14.2], [690, 3, true, 21, 0, 31.84, 32.4], [691, 1, true, 21, 0, 16.85, 17.2], [692, 2, true, 19, 0, 29.98, 30.3], [693, 3, true, 20, 0, 32.59, 32.9], [694, 3, true, 23, 0, 28.36, 29.9], [695, 1, true, 25, 0, 16.6, 17.7], [696, 2, true, 26, 0, 29.81, 30.2], [697, 3, true, 26, 0, 39.63, 41.0], [698, 3, true, 21, 0, 33.89, 34.9], [699, 3, true, 19, 0, 35.3, 35.7], [700, 1, true, 20, 0, 23.37, 23.8], [701, 1, true, 20, 0, 25.72, 26.0], [702, 1, true, 19, 0, 27.68, 28.0], [703, 3, true, 21, 0, 31.98, 33.8], [704, 2, true, 20, 0, 25.91, 26.3], [705, 1, true, 23, 0, 20.88, 21.3], [706, 3, true, 32, 2, 28.05, 40.4], [707, 1, true, 19, 0, 22.94, 23.3], [708, 2, true, 20, 0, 33.18, 33.9], [709, 3, true, 20, 0, 27.15, 27.4], [710, 2, true, 19, 0, 28.78, 30.0], [711, 2, true, 18, 0, 30.49, 30.9], [712, 1, true, 18, 0, 20.39, 20.7], [713, 2, true, 19, 0, 30.97, 31.2], [714, 3, true, 22, 0, 45.25, 47.4], [715, 2, true, 19, 0, 31.67, 31.9], [716, 2, true, 19, 0, 25.32, 25.7], [717, 1, true, 16, 0, 29.06, 29.5], [718, 3, true, 22, 0, 27.72, 28.5], [719, 2, true, 18, 0, 23.8, 24.1], [720, 3, true, 21, 0, 23.52, 25.6], [721, 2, true, 25, 0, 24.72, 25.1], [722, 2, true, 17, 0, 24.45, 24.7], [723, 3, true, 20, 0, 26.08, 28.1], [724, 1, true, 20, 0, 23.55, 25.3], [725, 1, true, 18, 0, 20.41, 20.7], [726, 1, true, 19, 0, 19.79, 20.2], [727, 1, true, 21, 0, 20.85, 22.3], [728, 3, true, 21, 0, 28.41, 28.6], [729, 1, true, 25, 0, 22.78, 23.6], [730, 2, true, 20, 0, 15.86, 16.0], [731, 2, true, 20, 0, 14.39, 14.5], [732, 1, true, 31, 0, 16.05, 17.4], [733, 3, true, 25, 0, 14.94, 15.6], [734, 1, true, 18, 0, 13.43, 13.5], [735, 1, true, 18, 0, 16.13, 16.2], [736, 1, true, 21, 0, 12.73, 12.8], [737, 1, true, 16, 0, 14.76, 14.8], [738, 2, true, 20, 0, 14.92, 15.0], [739, 3, true, 21, 0, 14.58, 15.6], [740, 1, true, 20, 0, 12.89, 14.2], [741, 2, true, 23, 0, 12.32, 13.5], [742, 2, true, 29, 0, 12.78, 13.6], [743, 2, true, 21, 0, 12.92, 13.1], [744, 3, true, 20, 0, 13.62, 13.7], [745, 3, true, 20, 0, 14.25, 14.4], [746, 2, true, 18, 0, 13.34, 13.6], [747, 1, true, 20, 0, 12.58, 13.1], [748, 2, true, 16, 0, 13.0, 13.7], [749, 1, true, 17, 0, 11.9, 13.2], [750, 2, true, 19, 0, 12.16, 13.0], [751, 3, true, 20, 0, 11.41, 12.9], [752, 2, true, 19, 0, 11.26, 11.4], [753, 1, true, 21, 0, 11.41, 11.5], [754, 2, true, 20, 0, 13.47, 13.6], [755, 2, true, 20, 0, 13.76, 13.9], [756, 2, true, 18, 0, 15.3, 15.4], [757, 3, true, 19, 0, 17.36, 17.6], [758, 3, true, 22, 0, 15.53, 15.7], [759, 3, true, 21, 0, 15.74, 15.9], [760, 1, true, 18, 0, 14.49, 15.3], [761, 3, true, 19, 0, 20.55, 20.7], [762, 2, true, 37, 0, 14.62, 15.6], [763, 3, true, 29, 0, 19.79, 20.9], [764, 3, true, 20, 0, 17.48, 18.8], [765, 3, true, 21, 0, 17.07, 19.0], [766, 3, true, 20, 0, 15.98, 17.6], [767, 2, true, 19, 0, 14.54, 14.7], [768, 3, true, 21, 0, 15.81, 17.5], [769, 2, true, 21, 0, 13.9, 14.1], [770, 3, true, 20, 0, 14.09, 14.2], [771, 2, true, 23, 0, 10.06, 10.2], [772, 1, true, 22, 0, 9.52, 9.7], [773, 3, true, 30, 0, 14.12, 14.3], [774, 2, true, 20, 0, 12.05, 12.2], [775, 3, true, 21, 0, 19.8, 20.0], [776, 3, true, 21, 0, 15.34, 15.5], [777, 3, true, 20, 0, 17.89, 18.0], [778, 3, true, 21, 0, 15.72, 15.9], [779, 3, true, 21, 0, 16.35, 16.5], [780, 3, true, 23, 0, 14.13, 14.7], [781, 3, true, 20, 0, 12.81, 13.7], [782, 1, true, 20, 0, 10.86, 11.3], [783, 3, true, 21, 0, 9.01, 10.4], [784, 3, true, 21, 0, 8.21, 8.4], [785, 3, true, 21, 0, 11.33, 11.5], [786, 1, true, 21, 0, 5.96, 6.1], [787, 3, true, 20, 0, 14.1, 14.2], [788, 2, true, 19, 0, 12.71, 12.8], [789, 2, true, 21, 0, 16.31, 16.5], [790, 1, true, 18, 0, 13.03, 13.2], [791, 1, true, 20, 0, 11.77, 12.0], [792, 3, true, 22, 0, 17.31, 17.4], [793, 2, true, 21, 0, 11.36, 11.5], [794, 3, true, 20, 0, 16.16, 16.3], [795, 3, true, 21, 0, 11.8, 11.9], [796, 1, true, 17, 0, 11.34, 11.4], [797, 3, true, 19, 0, 12.34, 12.5], [798, 2, true, 19, 0, 11.1, 11.2], [799, 2, true, 21, 0, 9.22, 9.5]]
\ No newline at end of file
```

</details>

<a id="C033"></a>
### C033 · Experiment notes: less-conservative pillars not adopted; 4-obj test results

Commit `f24e3a234fd70ef1e1cfd31441f506529b817c54`; parents: d7dabcd704f0fea8efcd3cc1a4991180e75b9f38. Recorded author date: 2026-10-01T13:19:52+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E1464](01_timeline.md#E1464): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C033_f24e3a2.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/NOTES.md b/NOTES.md
index 6049a68..bfaae9e 100644
--- a/NOTES.md
+++ b/NOTES.md
@@ -39,3 +39,5 @@
   39     39  - Model: each sample is a box (half 0.045) occluding the ray cam->lander, with the ray trimmed at the lander box (half 0.06). This fixed 549 but did not predict 706.
   40     40  - Robustness: failed send/img/cal positions are added to self.bad as (x,y,op,arg). The planner then excludes land/vis/any_vis within 0.08 of them, so a replan won't retry the same spot. 706 is now solved in 32 steps, with 2 replans.
   41     41  - Results: seeds 400-600 200/200 (mean 20.185); 600-800 200/200 (mean 20.57). Single-thread worst plan time ~7s.
          42 +- Experiment: less conservative pillars (PILLAR_R 0.238, INFL_LAND 0.02, INFL_OBJ 0.005) on 400-600 gave 200/200 and mean 20.16 vs 20.185. The gain is marginal and adds collision risk, so it was not adopted.
          43 +- 4-objective seeds 100-200: 100/100, mean 21.95. Single-thread plan time ~5s (up to ~56s under 8-thread contention).
diff --git a/approach_lc.py b/approach_lc.py
new file mode 100644
index 0000000..7d7659d
--- /dev/null
+++ b/approach_lc.py
@@ -0,0 +1,758 @@
           1 +"""Rovers approach: staged grid BFS planner per rover + joint task assignment."""
           2 +import itertools
           3 +import math
           4 +
           5 +import numpy as np
           6 +from scipy.ndimage import minimum_filter
           7 +
           8 +INF = 10 ** 6
           9 +RES = 0.05            # grid resolution
          10 +WIN = 4               # max cells per step per axis (0.2 / RES)
          11 +SEL = {"sample": -0.8333, "cal": -0.5, "img": -0.1667, "noop": 0.1667,
          12 +       "send": 0.5, "drop": 0.8333}
          13 +
          14 +# geometry constants (empirically probed)
          15 +WALL_IN = 0.2271 + 0.004
          16 +ARENA = 2.2729 - 0.004
          17 +PILLAR_R = 0.238
          18 +MOUND_R = 0.185
          19 +LANDER_XMIN = -1.15
          20 +LANDER_YMIN = -1.42
          21 +OBJ_RANGE = 1.993
          22 +LANDER_RANGE = 3.995
          23 +SAMPLE_R = 0.246
          24 +HOME_R = 0.235
          25 +IMG_TH = -math.pi / 2
          26 +ROT_IMG = 4.0
          27 +FINE_RES = 0.025
          28 +PILLAR_INFL_OBJ = 0.005
          29 +PILLAR_INFL_LAND = 0.02
          30 +LANDER_HALF = 0.06
          31 +SAMPLE_OCC_H = 0.045
          32 +ROVER_OCC_R = 0.26
          33 +CAM_OFF = (-0.087, -0.0125)
          34 +OBJ_BACK_DEG = 108.0     # if |rel bearing| > this, pillars don't occlude objectives
          35 +LAND_BACK_DEG = 110.0    # same quirk for lander (sending)
          36 +USE_BACK_OBJ = True
          37 +USE_BACK_LAND = True
          38 +
          39 +
          40 +def _wrap(a):
          41 +    return (a + np.pi) % (2 * np.pi) - np.pi
          42 +
          43 +
          44 +RELAX = [False]
          45 +
          46 +
          47 +def rot_steps(a, b):
          48 +    d = abs(float(_wrap(b - a)))
          49 +    return int(math.ceil(d / 0.4 - 1e-6))
          50 +
          51 +
          52 +def approach_angle(a, b, dmax):
          53 +    d = float(_wrap(b - a))
          54 +    if abs(d) <= dmax:
          55 +        return float(_wrap(b))
          56 +    return float(_wrap(a + math.copysign(dmax, d)))
          57 +
          58 +
          59 +def seg_hits_box(px, py, qx, qy, cx, cy, hx, hy):
          60 +    """Vectorised: does segment p->q (p arrays, q scalar) intersect AABB?"""
          61 +    if RELAX[0]:
          62 +        return np.zeros(np.shape(px), dtype=bool)
          63 +    dx = qx - px
          64 +    dy = qy - py
          65 +    t0 = np.zeros_like(px)
          66 +    t1 = np.ones_like(px)
          67 +    ok = np.ones(px.shape, dtype=bool)
          68 +    for d, p, lo, hi in ((dx, px, cx - hx, cx + hx), (dy, py, cy - hy, cy + hy)):
          69 +        small = np.abs(d) < 1e-12
          70 +        ok &= ~(small & ((p < lo) | (p > hi)))
          71 +        with np.errstate(divide="ignore", invalid="ignore"):
          72 +            ta = (lo - p) / d
          73 +            tb = (hi - p) / d
          74 +        tmin = np.where(small, -np.inf, np.minimum(ta, tb))
          75 +        tmax = np.where(small, np.inf, np.maximum(ta, tb))
          76 +        t0 = np.maximum(t0, tmin)
          77 +        t1 = np.minimum(t1, tmax)
          78 +    return ok & (t0 <= t1)
          79 +
          80 +
          81 +def seg_hits_disk(px, py, qx, qy, cx, cy, r):
          82 +    dx = qx - px
          83 +    dy = qy - py
          84 +    L2 = dx * dx + dy * dy + 1e-12
          85 +    t = np.clip(((cx - px) * dx + (cy - py) * dy) / L2, 0, 1)
          86 +    ex = px + t * dx - cx
          87 +    ey = py + t * dy - cy
          88 +    return ex * ex + ey * ey < r * r
          89 +
          90 +
          91 +def box_dist(px, py, cx, cy, hx, hy):
          92 +    ddx = np.maximum(np.abs(px - cx) - hx, 0)
          93 +    ddy = np.maximum(np.abs(py - cy) - hy, 0)
          94 +    return np.hypot(ddx, ddy)
          95 +
          96 +
          97 +def propagate(f, free, win=WIN):
          98 +    f = np.where(free, f, INF)
          99 +    while True:
         100 +        m = minimum_filter(f, size=2 * win + 1, mode="constant", cval=INF) + 1
         101 +        nf = np.where(free, np.minimum(f, m), INF)
         102 +        if np.array_equal(nf, f):
         103 +            return f
         104 +        f = nf
         105 +
         106 +
         107 +def op_stage(fprev, region, win=WIN):
         108 +    m = minimum_filter(fprev, size=2 * win + 1, mode="constant", cval=INF) + 1
         109 +    return np.where(region, np.minimum(m, INF), INF)
         110 +
         111 +
         112 +class Scene:
         113 +    def __init__(self, state):
         114 +        self.rovers = {}
         115 +        self.objectives = []
         116 +        self.samples = []
         117 +        self.pillars = []
         118 +        self.mounds = []
         119 +        self.lander = (-1.9, -2.0)
         120 +        objs = [state.get_object_from_name(nm) for nm in sorted(state.get_object_names())]
         121 +        for o in objs:
         122 +            t = o.type.name
         123 +            g = lambda f: state.get(o, f)
         124 +            if t == "rover":
         125 +                self.rovers[o.name] = dict(x=g("x"), y=g("y"), th=g("theta"),
         126 +                                           full=g("store_full") > 0.5,
         127 +                                           cal=g("calibrated") > 0.5)
         128 +            elif t == "lander":
         129 +                self.lander = (g("x"), g("y"))
         130 +            elif t == "objective":
         131 +                self.objectives.append(dict(name=o.name, x=g("x"), y=g("y"),
         132 +                                            img=(g("have_image_rover0") > 0.5,
         133 +                                                 g("have_image_rover1") > 0.5),
         134 +                                            recv=g("received_image") > 0.5))
         135 +            elif t == "sample":
         136 +                self.samples.append(dict(name=o.name, x=g("x"), y=g("y"),
         137 +                                         soil=g("is_soil") > 0.5,
         138 +                                         an=(g("analyzed_rover0") > 0.5,
         139 +                                             g("analyzed_rover1") > 0.5),
         140 +                                         recv=g("received_analysis") > 0.5))
         141 +            elif t == "obstacle":
         142 +                d = (g("x"), g("y"), g("half_x"), g("half_y"))
         143 +                if g("half_x") > 0.15:
         144 +                    self.mounds.append(d)
         145 +                else:
         146 +                    self.pillars.append(d)
         147 +
         148 +
         149 +class RoverPlanner:
         150 +    """Grid + regions for one rover."""
         151 +
         152 +    def __init__(self, idx, home, scene, other_pos_list, cur_th=None, bad=(), img_th=None,
         153 +                 res=RES):
         154 +        self.ctor = (idx, home, scene, other_pos_list, cur_th, bad, img_th)
         155 +        self.res = res
         156 +        self.win = int(round(0.2 / res))
         157 +        self.idx = idx
         158 +        self.home = home  # (x, y, th)
         159 +        hx, hy, th = home
         160 +        self.th = th
         161 +        side = 1 if hx > 0 else -1
         162 +        lo_x, hi_x = (WALL_IN, ARENA) if side > 0 else (-ARENA, -WALL_IN)
         163 +        i0 = math.ceil((lo_x - hx) / res - 1e-9)
         164 +        i1 = math.floor((hi_x - hx) / res + 1e-9)
         165 +        j0 = math.ceil((-ARENA - hy) / res - 1e-9)
         166 +        j1 = math.floor((ARENA - hy) / res + 1e-9)
         167 +        self.xs = hx + res * np.arange(i0, i1 + 1)
         168 +        self.ys = hy + res * np.arange(j0, j1 + 1)
         169 +        self.hi = -i0
         170 +        self.hj = -j0
         171 +        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
         172 +        self.X, self.Y = X, Y
         173 +        free = np.ones(X.shape, dtype=bool)
         174 +        for (cx, cy, ax, ay) in scene.pillars:
         175 +            free &= box_dist(X, Y, cx, cy, ax, ay) > (0.236 if RELAX[0] else PILLAR_R)
         176 +        for (cx, cy, ax, ay) in scene.mounds:
         177 +            free &= box_dist(X, Y, cx, cy, ax, ay) > MOUND_R
         178 +        free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
         179 +        for b in bad:
         180 +            if len(b) == 2:
         181 +                free &= np.hypot(X - b[0], Y - b[1]) > 0.03
         182 +        free[self.hi, self.hj] = True
         183 +        self.free = free
         184 +        self.home_reg = (np.hypot(X - hx, Y - hy) <= HOME_R) & free
         185 +        self.home_reg[self.hi, self.hj] = True
         186 +        c, s = math.cos(th), math.sin(th)
         187 +        self.camx = X + c * CAM_OFF[0] - s * CAM_OFF[1]
         188 +        self.camy = Y + s * CAM_OFF[0] + c * CAM_OFF[1]
         189 +        self.scene = scene
         190 +        ith = th if img_th is None else img_th
         191 +        self.img_th = ith
         192 +        cur = th if cur_th is None else cur_th
         193 +        self.cur_th = cur
         194 +        self.nrot_in = rot_steps(cur, ith)
         195 +        self.nrot_out = rot_steps(ith, th)
         196 +        hs = [cur, ith, th]
         197 +        for k in range(1, 9):
         198 +            hs.append(approach_angle(cur, ith, 0.4 * k))
         199 +            hs.append(approach_angle(ith, th, 0.4 * k))
         200 +            hs.append(approach_angle(cur, th, 0.4 * k))
         201 +        self.headings = hs
         202 +        ci, si = math.cos(ith), math.sin(ith)
         203 +        camx_i = X + ci * CAM_OFF[0] - si * CAM_OFF[1]
         204 +        camy_i = Y + si * CAM_OFF[0] + ci * CAM_OFF[1]
         205 +        # objective visibility
         206 +        self.vis = []
         207 +        self.objd = []
         208 +        for ob in scene.objectives:
         209 +            ox, oy = ob["x"], ob["y"]
         210 +            d = np.hypot(ox - camx_i, oy - camy_i)
         211 +            v = (d <= OBJ_RANGE)
         212 +            occ = np.zeros(X.shape, dtype=bool)
         213 +            for (cx, cy, ax, ay) in scene.pillars:
         214 +                e = PILLAR_INFL_OBJ
         215 +                occ |= seg_hits_box(camx_i, camy_i, ox, oy, cx, cy, ax + e, ay + e)
         216 +                occ |= seg_hits_box(X, Y, ox, oy, cx, cy, ax + e, ay + e)
         217 +            if USE_BACK_OBJ:
         218 +                rel = np.abs(_wrap(np.arctan2(oy - Y, ox - X) - ith))
         219 +                back = rel > math.radians(OBJ_BACK_DEG)
         220 +            else:
         221 +                back = np.zeros(X.shape, dtype=bool)
         222 +            occ2 = np.zeros(X.shape, dtype=bool)
         223 +            for (px, py) in other_pos_list:
         224 +                occ2 |= seg_hits_disk(camx_i, camy_i, ox, oy, px, py, ROVER_OCC_R)
         225 +            self.vis.append(v & ((~occ) | back) & ~occ2 & free)
         226 +            self.objd.append(d)
         227 +        self.any_vis = np.zeros(X.shape, dtype=bool)
         228 +        for v in self.vis:
         229 +            self.any_vis |= v
         230 +        # lander visibility (must hold for every heading along the rotation path)
         231 +        lx, ly = scene.lander
         232 +        land = free.copy()
         233 +        land_free = free.copy()
         234 +        for hh in self.headings:
         235 +            ch, sh = math.cos(hh), math.sin(hh)
         236 +            cx_ = X + ch * CAM_OFF[0] - sh * CAM_OFF[1]
         237 +            cy_ = Y + sh * CAM_OFF[0] + ch * CAM_OFF[1]
         238 +            v = (np.hypot(lx - X, ly - Y) <= LANDER_RANGE) & \
         239 +                (np.hypot(lx - cx_, ly - cy_) <= LANDER_RANGE)
         240 +            occ = np.zeros(X.shape, dtype=bool)
         241 +            for (cx, cy, ax, ay) in scene.pillars:
         242 +                e = PILLAR_INFL_LAND
         243 +                occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
         244 +                occ |= seg_hits_box(cx_, cy_, lx, ly, cx, cy, ax + e, ay + e)
         245 +            # sample markers occlude the lander (ray ends at lander box boundary)
         246 +            for sm in scene.samples:
         247 +                if abs(sm["x"] - lx) > 4.2 or abs(sm["y"] - ly) > 4.2:
         248 +                    continue
         249 +                for (ppx, ppy) in ((X, Y), (cx_, cy_)):
         250 +                    ddx = ppx - lx
         251 +                    ddy = ppy - ly
         252 +                    tt = LANDER_HALF / np.maximum(np.maximum(np.abs(ddx), np.abs(ddy)), 1e-9)
         253 +                    ex = lx + tt * ddx
         254 +                    ey = ly + tt * ddy
         255 +                    occ |= seg_hits_box(ppx, ppy, ex, ey, sm["x"], sm["y"],
         256 +                                        SAMPLE_OCC_H, SAMPLE_OCC_H)
         257 +            if USE_BACK_LAND:
         258 +                rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - hh))
         259 +                back = rel > math.radians(LAND_BACK_DEG)
         260 +            else:
         261 +                back = np.zeros(X.shape, dtype=bool)
         262 +            occ2 = np.zeros(X.shape, dtype=bool)
         263 +            for (px, py) in other_pos_list:
         264 +                occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
         265 +                occ2 |= seg_hits_disk(cx_, cy_, lx, ly, px, py, ROVER_OCC_R)
         266 +            land &= v & ((~occ) | back) & ~occ2
         267 +            land_free &= v & ((~occ) | back)
         268 +        for b in bad:
         269 +            if len(b) == 4:
         270 +                near = np.hypot(X - b[0], Y - b[1]) <= 0.08
         271 +                if b[2] == "send":
         272 +                    land &= ~near
         273 +                    land_free &= ~near
         274 +                elif b[2] == "img" and b[3] is not None and b[3] < len(self.vis):
         275 +                    self.vis[b[3]] = self.vis[b[3]] & ~near
         276 +                elif b[2] == "cal":
         277 +                    self.any_vis &= ~near
         278 +        self.land = land
         279 +        self.land_free = land_free
         280 +        self.camx_i, self.camy_i = camx_i, camy_i
         281 +        # samples
         282 +        self.sreg = {}
         283 +        dk = {}
         284 +        for kind in ("stone", "soil"):
         285 +            d = np.full(X.shape, 1e9)
         286 +            for sm in scene.samples:
         287 +                if sm["soil"] == (kind == "soil"):
         288 +                    d = np.minimum(d, np.hypot(sm["x"] - X, sm["y"] - Y))
         289 +            dk[kind] = d
         290 +        for kind, oth in (("stone", "soil"), ("soil", "stone")):
         291 +            r = (dk[kind] <= SAMPLE_R) & ((dk[oth] > 0.26) | (dk[oth] > dk[kind] + 0.03))
         292 +            self.sreg[kind] = r & free
         293 +
         294 +    def cell_of(self, x, y):
         295 +        i = int(round((x - self.xs[0]) / self.res))
         296 +        j = int(round((y - self.ys[0]) / self.res))
         297 +        i = min(max(i, 0), len(self.xs) - 1)
         298 +        j = min(max(j, 0), len(self.ys) - 1)
         299 +        return i, j
         300 +
         301 +    def img_region(self, k, imaged):
         302 +        """cells where image would photograph objective k given set imaged."""
         303 +        reg = self.vis[k].copy()
         304 +        if not reg.any():
         305 +            return reg
         306 +        dk = self.objd[k]
         307 +        for m in range(len(self.vis)):
         308 +            if m == k or m in imaged:
         309 +                continue
         310 +            reg &= ~((self.objd[m] <= 2.03) & (self.objd[m] < dk + 0.03))
         311 +        return reg
         312 +
         313 +
         314 +class GeneratedApproach:
         315 +    def __init__(self, action_space, observation_space, primitives):
         316 +        self.action_space = action_space
         317 +        self.homes = None
         318 +
         319 +    # ------------------------------------------------------------------
         320 +    def reset(self, state, info):
         321 +        sc = Scene(state)
         322 +        self.homes = {n: (r["x"], r["y"], r["th"]) for n, r in sc.rovers.items()}
         323 +        self.replans = 0
         324 +        self.fail_count = 0
         325 +        self.expect = [None, None]
         326 +        self.prev_sc = sc
         327 +        self.log = []
         328 +        self.bad = [[], []]
         329 +        import time as _t
         330 +        self.t_start = _t.time()
         331 +        self._plan(state)
         332 +
         333 +    # ------------------------------------------------------------------
         334 +    def _rover_tables(self, ri, sc, need_objs, need_stone, need_soil, pending):
         335 +        name = "rover%d" % ri
         336 +        r = sc.rovers[name]
         337 +        other = sc.rovers["rover%d" % (1 - ri)]
         338 +        ohome = self.homes["rover%d" % (1 - ri)]
         339 +        occl = [(ohome[0], ohome[1])]
         340 +        if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
         341 +            occl.append((other["x"], other["y"]))
         342 +        merged = {}
         343 +        hth = self.homes[name][2]
         344 +        if IMG_TH is None:
         345 +            ths = [hth]
         346 +        else:
         347 +            d = float(_wrap(IMG_TH - hth))
         348 +            ths = [float(_wrap(hth + math.copysign(min(abs(d), ROT_IMG), d)))]
         349 +        for ith in ths:
         350 +            P, table = self._rover_tables_h(ri, sc, need_objs, need_stone, need_soil,
         351 +                                            pending, occl, ith)
         352 +            for k, (c, st) in table.items():
         353 +                if k not in merged or c < merged[k][0]:
         354 +                    merged[k] = (c, st, P)
         355 +        return None, merged
         356 +
         357 +    def _rover_tables_h(self, ri, sc, need_objs, need_stone, need_soil, pending, occl, ith):
         358 +        name = "rover%d" % ri
         359 +        r = sc.rovers[name]
         360 +        P = RoverPlanner(ri, self.homes[name], sc, occl, r["th"], self.bad[ri], ith)
         361 +        self_planner = P
         362 +        start = P.cell_of(r["x"], r["y"])
         363 +        P.free[start] = True
         364 +        f0 = np.full(P.free.shape, INF, dtype=np.int64)
         365 +        f0[start] = 0
         366 +        stages0 = []
         367 +        F = propagate(f0, P.free, P.win)
         368 +        stages0.append(("start", None, f0, F))
         369 +        if r["full"]:
         370 +            G = op_stage(F, P.free, P.win)
         371 +            F = propagate(G, P.free, P.win)
         372 +            stages0.append(("drop", None, G, F))
         373 +        imaged0 = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
         374 +        tasks = []
         375 +        for k in need_objs:
         376 +            if P.vis[k].any():
         377 +                tasks.append(("obj", k))
         378 +        if need_stone and P.sreg["stone"].any():
         379 +            tasks.append(("stone", None))
         380 +        if need_soil and P.sreg["soil"].any():
         381 +            tasks.append(("soil", None))
         382 +        hcell = (P.hi, P.hj)
         383 +        table = {}  # frozenset(task keys) -> (cost, stages)
         384 +
         385 +        def finish(F, stages, done_keys):
         386 +            if not done_keys and not pending:
         387 +                cost = F[P.home_reg].min()
         388 +                st = stages
         389 +            else:
         390 +                G = op_stage(F, P.land, P.win)
         391 +                F2 = propagate(G, P.free, P.win)
         392 +                cost = F2[P.home_reg].min()
         393 +                st = stages + [("send", None, G, F2)]
         394 +            if cost >= INF:
         395 +                return
         396 +            key = frozenset(done_keys)
         397 +            if key not in table or cost < table[key][0]:
         398 +                table[key] = (int(cost), st)
         399 +
         400 +        def dfs(F, stages, done_keys, imaged, cal):
         401 +            finish(F, stages, done_keys)
         402 +            if F.min() >= INF:
         403 +                return
         404 +            for t in tasks:
         405 +                key = t if t[0] != "obj" else ("obj", t[1])
         406 +                if key in done_keys:
         407 +                    continue
         408 +                if t[0] == "obj":
         409 +                    k = t[1]
         410 +                    st = list(stages)
         411 +                    Fc = F
         412 +                    if not cal:
         413 +                        G = op_stage(F, P.any_vis, P.win)
         414 +                        G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
         415 +                        Fc = propagate(G, P.free, P.win)
         416 +                        st.append(("cal", None, G, Fc))
         417 +                    reg = P.img_region(k, imaged)
         418 +                    G = op_stage(Fc, reg, P.win)
         419 +                    G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
         420 +                    Fi = propagate(G, P.free, P.win)
         421 +                    st.append(("img", k, G, Fi))
         422 +                    dfs(Fi, st, done_keys | {key}, imaged | {k}, False)
         423 +                else:
         424 +                    G = op_stage(F, P.sreg[t[0]], P.win)
         425 +                    Fs = propagate(G, P.free, P.win)
         426 +                    G2 = op_stage(Fs, P.free, P.win)
         427 +                    Fd = propagate(G2, P.free, P.win)
         428 +                    st = stages + [("sample", t[0], G, Fs), ("drop", None, G2, Fd)]
         429 +                    dfs(Fd, st, done_keys | {key}, imaged, cal)
         430 +
         431 +        dfs(F, stages0, frozenset(), imaged0, r["cal"])
         432 +        return P, table
         433 +
         434 +    def _plan(self, state):
         435 +        import time as _t
         436 +        self._fine_cache = {}
         437 +        self._fast = (_t.time() - self.t_start) > 20.0
         438 +        sc = Scene(state)
         439 +        self.scene = sc
         440 +        # what is needed
         441 +        need_objs = [k for k, ob in enumerate(sc.objectives)
         442 +                     if not ob["recv"] and not ob["img"][0] and not ob["img"][1]]
         443 +        pending = [False, False]
         444 +        for k, ob in enumerate(sc.objectives):
         445 +            if not ob["recv"]:
         446 +                for ri in range(2):
         447 +                    if ob["img"][ri]:
         448 +                        pending[ri] = True
         449 +        need = {}
         450 +        for kind in ("stone", "soil"):
         451 +            recv = any(s["recv"] for s in sc.samples if s["soil"] == (kind == "soil"))
         452 +            holders = [ri for ri in range(2)
         453 +                       if any(s["an"][ri] for s in sc.samples if s["soil"] == (kind == "soil"))]
         454 +            if recv:
         455 +                need[kind] = False
         456 +            elif holders:
         457 +                need[kind] = False
         458 +                pending[holders[0]] = True
         459 +            else:
         460 +                need[kind] = True
         461 +        tabs = []
         462 +        for ri in range(2):
         463 +            tabs.append(self._rover_tables(ri, sc, need_objs, need["stone"], need["soil"],
         464 +                                           pending[ri]))
         465 +        # joint assignment
         466 +        best = None
         467 +        cands = []
         468 +        n = len(need_objs)
         469 +        stone_opts = [0, 1] if need["stone"] else [None]
         470 +        soil_opts = [0, 1] if need["soil"] else [None]
         471 +        for assign in itertools.product([0, 1], repeat=n):
         472 +            for so in stone_opts:
         473 +                for sl in soil_opts:
         474 +                    sets = [set(), set()]
         475 +                    for k, a in zip(need_objs, assign):
         476 +                        sets[a].add(("obj", k))
         477 +                    if so is not None:
         478 +                        sets[so].add(("stone", None))
         479 +                    if sl is not None:
         480 +                        sets[sl].add(("soil", None))
         481 +                    costs = []
         482 +                    for ri in range(2):
         483 +                        e = tabs[ri][1].get(frozenset(sets[ri]))
         484 +                        costs.append(e)
         485 +                    if costs[0] is None or costs[1] is None:
         486 +                        continue
         487 +                    key = (max(costs[0][0], costs[1][0]), costs[0][0] + costs[1][0])
         488 +                    cands.append((key, costs))
         489 +                    if best is None or key < best[0]:
         490 +                        self.pred = key
         491 +                        best = (key, costs)
         492 +        self.actions = [[], []]
         493 +        if best is None:
         494 +            if not RELAX[0]:
         495 +                RELAX[0] = True
         496 +                try:
         497 +                    self._plan(state)
         498 +                finally:
         499 +                    RELAX[0] = False
         500 +            return
         501 +        cands.sort(key=lambda c: c[0])
         502 +        seen = set()
         503 +        bestreal = None
         504 +        for key, costs in cands:
         505 +            sig = (id(costs[0][1]), id(costs[1][1]))
         506 +            if sig in seen:
         507 +                continue
         508 +            seen.add(sig)
         509 +            if len(seen) > 6 or (bestreal is not None and key[0] >= bestreal[0][0]):
         510 +                break
         511 +            acts = self._realize(sc, tabs, costs)
         512 +            real = (max(len(acts[0]), len(acts[1])), len(acts[0]) + len(acts[1]))
         513 +            if bestreal is None or real < bestreal[0]:
         514 +                bestreal = (real, acts)
         515 +        self.actions = bestreal[1]
         516 +
         517 +    def _refine(self, entry):
         518 +        """Replay a coarse stage sequence on a fine grid."""
         519 +        cost, stages, Pc = entry
         520 +        if FINE_RES is None or FINE_RES >= Pc.res or self._fast:
         521 +            return entry
         522 +        ri = Pc.ctor[0]
         523 +        ck = (ri, Pc.img_th)
         524 +        if ck in self._fine_cache:
         525 +            P = self._fine_cache[ck]
         526 +            P.free = P.free0.copy()
         527 +        else:
         528 +            P = RoverPlanner(*Pc.ctor, res=FINE_RES)
         529 +            P.free0 = P.free.copy()
         530 +            self._fine_cache[ck] = P
         531 +        sc = self.scene
         532 +        r = sc.rovers["rover%d" % ri]
         533 +        imaged = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
         534 +        start = P.cell_of(r["x"], r["y"])
         535 +        P.free[start] = True
         536 +        out = []
         537 +        F = None
         538 +        for name, arg, _, _ in stages:
         539 +            if name == "start":
         540 +                G = np.full(P.free.shape, INF, dtype=np.int64)
         541 +                G[start] = 0
         542 +            elif name == "drop":
         543 +                G = op_stage(F, P.free, P.win)
         544 +            elif name == "cal":
         545 +                G = op_stage(F, P.any_vis, P.win)
         546 +                G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
         547 +            elif name == "img":
         548 +                G = op_stage(F, P.img_region(arg, imaged), P.win)
         549 +                G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
         550 +                imaged = imaged | {arg}
         551 +            elif name == "sample":
         552 +                G = op_stage(F, P.sreg[arg], P.win)
         553 +            elif name == "send":
         554 +                G = op_stage(F, P.land, P.win)
         555 +            else:
         556 +                return entry
         557 +            F = propagate(G, P.free, P.win)
         558 +            out.append((name, arg, G, F))
         559 +        c = F[P.home_reg].min()
         560 +        if c >= INF:
         561 +            return entry
         562 +        return (int(c), out, P)
         563 +
         564 +    def _realize(self, sc, tabs, costs):
         565 +        costs = [self._refine(costs[0]), self._refine(costs[1])]
         566 +        best = (None, costs)
         567 +        actions = [[], []]
         568 +        sc = self.scene
         569 +        for ri in range(2):
         570 +            P = costs[ri][2]
         571 +            actions[ri] = self._extract(P, best[1][ri][1])
         572 +        # time-aware re-plan of final send against other rover's trajectory
         573 +        trajs = []
         574 +        for ri in range(2):
         575 +            r = sc.rovers["rover%d" % ri]
         576 +            trajs.append([(r["x"], r["y"])] + [(a[0], a[1]) for a in actions[ri]])
         577 +        new_actions = list(actions)
         578 +        for ri in range(2):
         579 +            stages = best[1][ri][1]
         580 +            if stages[-1][0] != "send":
         581 +                continue
         582 +            P = costs[ri][2]
         583 +            Fprev = stages[-2][3]
         584 +            G0 = op_stage(Fprev, P.land_free, P.win)
         585 +            other = trajs[1 - ri]
         586 +            G = np.full(G0.shape, INF, dtype=G0.dtype)
         587 +            pending_mask = G0 < INF
         588 +            tmin = int(G0[pending_mask].min()) if pending_mask.any() else INF
         589 +            lx, ly = sc.lander
         590 +            t = tmin
         591 +            while pending_mask.any() and t < tmin + 200:
         592 +                blk = np.zeros(P.X.shape, dtype=bool)
         593 +                for tt in (t - 1, t):
         594 +                    ox, oy = other[max(0, min(tt, len(other) - 1))]
         595 +                    blk |= seg_hits_disk(P.camx, P.camy, lx, ly, ox, oy, ROVER_OCC_R)
         596 +                    blk |= seg_hits_disk(P.camx_i, P.camy_i, lx, ly, ox, oy, ROVER_OCC_R)
         597 +                ok = pending_mask & (G0 <= t) & ~blk
         598 +                G[ok] = t
         599 +                pending_mask &= ~ok
         600 +                if t >= len(other) - 1 and not ok.any() and (G0 <= t).all():
         601 +                    break
         602 +                t += 1
         603 +            F2 = propagate(G, P.free, P.win)
         604 +            if F2[P.home_reg].min() >= INF:
         605 +                continue
         606 +            st = stages[:-1] + [("send_t", None, G, F2)]
         607 +            new_actions[ri] = self._extract(P, st)
         608 +        return [self._schedule(costs[ri][2], new_actions[ri]) for ri in range(2)]
         609 +
         610 +    def _schedule(self, P, seq):
         611 +        """Attach headings; append waits so the rover can rotate back home."""
         612 +        home_th = P.th
         613 +        t_img = [t for t, a in enumerate(seq, 1) if a[2] and a[2][0] in ("cal", "img")]
         614 +        seq = list(seq)
         615 +        out = []
         616 +        if t_img:
         617 +            last = max(t_img)
         618 +            while len(seq) < last + P.nrot_out:
         619 +                x, y = (seq[-1][0], seq[-1][1])
         620 +                seq.append((x, y, None))
         621 +            T = len(seq)
         622 +            for t, (x, y, op) in enumerate(seq, 1):
         623 +                if t <= T - P.nrot_out:
         624 +                    h = approach_angle(P.cur_th, P.img_th, 0.4 * t)
         625 +                else:
         626 +                    h = approach_angle(P.img_th, home_th, 0.4 * (t - (T - P.nrot_out)))
         627 +                out.append((x, y, op, h))
         628 +        else:
         629 +            while len(seq) < rot_steps(P.cur_th, home_th):
         630 +                x, y = (seq[-1][0], seq[-1][1]) if seq else (float(P.xs[P.hi]), float(P.ys[P.hj]))
         631 +                seq.append((x, y, None))
         632 +            for t, (x, y, op) in enumerate(seq, 1):
         633 +                out.append((x, y, op, approach_angle(P.cur_th, home_th, 0.4 * t)))
         634 +        return out
         635 +
         636 +    def _extract(self, P, stages):
         637 +        """Backtrack through stage fields (waiting allowed); list of (x,y,op)."""
         638 +        k = len(stages) - 1
         639 +        Ff = np.where(P.home_reg, stages[k][3], INF)
         640 +        cell = np.unravel_index(int(np.argmin(Ff)), Ff.shape)
         641 +        cell = (int(cell[0]), int(cell[1]))
         642 +        v = int(stages[k][3][cell])
         643 +        seq = []
         644 +        W = P.win
         645 +        nx, ny = P.free.shape
         646 +
         647 +        def nb(Fsrc, i, j, cond):
         648 +            best = None
         649 +            for di in range(-W, W + 1):
         650 +                for dj in range(-W, W + 1):
         651 +                    a, b = i + di, j + dj
         652 +                    if 0 <= a < nx and 0 <= b < ny and cond(Fsrc[a, b]):
         653 +                        c = abs(di) + abs(dj)
         654 +                        if best is None or c < best[1]:
         655 +                            best = ((a, b), c)
         656 +            return best[0] if best else None
         657 +
         658 +        guard = 0
         659 +        while not (k == 0 and v == 0) and guard < 5000:
         660 +            guard += 1
         661 +            name, arg, G, F = stages[k]
         662 +            i, j = cell
         663 +            timed = name == "send_t"
         664 +            choice = None
         665 +            for mode in (0, 1):
         666 +                if k > 0:
         667 +                    okop = (G[cell] == v) if (mode == 0 or timed) else (G[cell] <= v)
         668 +                    if okop:
         669 +                        Fp = stages[k - 1][3]
         670 +                        c = nb(Fp, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
         671 +                        if c is not None:
         672 +                            choice = (c, (name.replace("_t", ""), arg), k - 1)
         673 +                            break
         674 +                c = nb(F, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
         675 +                if c is not None:
         676 +                    choice = (c, None, k)
         677 +                    break
         678 +            if choice is None:
         679 +                break
         680 +            seq.append((float(P.xs[cell[0]]), float(P.ys[cell[1]]), choice[1]))
         681 +            cell, k = choice[0], choice[2]
         682 +            v -= 1
         683 +        seq.reverse()
         684 +        return seq
         685 +
         686 +    # ------------------------------------------------------------------
         687 +    def get_action(self, state):
         688 +        act = np.zeros(8, dtype=np.float32)
         689 +        sc = Scene(state)
         690 +        if self._deviated(sc) or (not self.actions[0] and not self.actions[1]):
         691 +            self.replans += 1
         692 +            import time as _t
         693 +            if self.replans < 60 and (_t.time() - self.t_start) < 45.0:
         694 +                self._plan(state)
         695 +        for ri in range(2):
         696 +            r = sc.rovers["rover%d" % ri]
         697 +            if self.actions[ri]:
         698 +                x, y, op, h = self.actions[ri].pop(0)
         699 +                dx = float(np.clip(x - r["x"], -0.2, 0.2))
         700 +                dy = float(np.clip(y - r["y"], -0.2, 0.2))
         701 +                act[4 * ri] = dx
         702 +                act[4 * ri + 1] = dy
         703 +                act[4 * ri + 3] = SEL[op[0]] if op else 0.0
         704 +                act[4 * ri + 2] = float(np.clip(_wrap(h - r["th"]), -0.4, 0.4))
         705 +                self.expect[ri] = (x, y, op, h)
         706 +            else:
         707 +                # at end: if at home do nothing
         708 +                self.expect[ri] = None
         709 +        return act
         710 +
         711 +    def _deviated(self, sc):
         712 +        dev = False
         713 +        for ri in range(2):
         714 +            e = self.expect[ri]
         715 +            if e is None:
         716 +                continue
         717 +            d0 = dev
         718 +            dev = False
         719 +            r = sc.rovers["rover%d" % ri]
         720 +            if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3 or \
         721 +                    abs(float(_wrap(r["th"] - e[3]))) > 1e-3:
         722 +                dev = True
         723 +                self.log.append(("move", ri, e, r["x"], r["y"]))
         724 +                self.bad[ri].append((e[0], e[1]))
         725 +            op, arg = e[2] if e[2] else (None, None)
         726 +            pr = self.prev_sc.rovers["rover%d" % ri]
         727 +            if op == "img":
         728 +                ob = sc.objectives[arg]
         729 +                if not ob["img"][ri]:
         730 +                    dev = True
         731 +            if op == "sample":
         732 +                if not any(s["an"][ri] for s in sc.samples if s["soil"] == (arg == "soil")):
         733 +                    dev = True
         734 +            if op == "cal" and not r["cal"]:
         735 +                dev = True
         736 +            elif op == "img" and (r["cal"] or not pr["cal"]):
         737 +                dev = True
         738 +            elif op == "sample" and not r["full"]:
         739 +                dev = True
         740 +            elif op == "drop" and r["full"]:
         741 +                dev = True
         742 +            elif op == "send":
         743 +                for ob in sc.objectives:
         744 +                    if ob["img"][ri] and not ob["recv"]:
         745 +                        dev = True
         746 +                for s in sc.samples:
         747 +                    if s["an"][ri] and not s["recv"]:
         748 +                        dev = True
         749 +            if dev and op in ("send", "img", "cal") and \
         750 +                    abs(r["x"] - e[0]) <= 1e-3 and abs(r["y"] - e[1]) <= 1e-3:
         751 +                self.bad[ri].append((e[0], e[1], op, arg))
         752 +            if dev:
         753 +                self.log.append(("dev", ri, e, round(r["x"], 3), round(r["y"], 3), r["cal"], pr["cal"],
         754 +                                 [ob["img"][ri] for ob in sc.objectives]))
         755 +            dev = dev or d0
         756 +        self.prev_sc = sc
         757 +        self.expect = [None, None]
         758 +        return dev
diff --git a/res_lc.json b/res_lc.json
new file mode 100644
index 0000000..1029882
--- /dev/null
+++ b/res_lc.json
@@ -0,0 +1 @@
           1 +[[400, 3, true, 20, 0, 37.88, 38.0], [401, 2, true, 20, 0, 31.68, 31.9], [402, 3, true, 24, 0, 20.78, 21.0], [403, 2, true, 19, 0, 27.5, 28.4], [404, 3, true, 21, 0, 43.58, 43.8], [405, 2, true, 22, 0, 26.7, 27.1], [406, 3, true, 21, 0, 36.62, 36.8], [407, 1, true, 19, 0, 25.24, 26.6], [408, 2, true, 21, 0, 25.82, 26.9], [409, 1, true, 16, 0, 29.66, 30.7], [410, 2, true, 20, 0, 26.93, 28.1], [411, 1, true, 21, 0, 25.76, 26.0], [412, 3, true, 21, 0, 35.38, 35.6], [413, 1, true, 18, 0, 22.64, 22.8], [414, 3, true, 20, 0, 35.64, 35.8], [415, 2, true, 19, 0, 22.87, 23.2], [416, 2, true, 20, 0, 31.25, 32.6], [417, 1, true, 18, 0, 21.45, 21.7], [418, 2, true, 18, 0, 27.08, 27.3], [419, 3, true, 21, 0, 36.06, 36.3], [420, 2, true, 18, 0, 21.95, 22.1], [421, 1, true, 18, 0, 22.26, 22.9], [422, 1, true, 17, 0, 18.97, 19.2], [423, 2, true, 18, 0, 27.53, 27.8], [424, 1, true, 16, 0, 27.82, 28.5], [425, 1, true, 20, 0, 26.99, 28.7], [426, 1, true, 18, 0, 23.92, 24.1], [427, 3, true, 23, 0, 37.12, 37.5], [428, 1, true, 20, 0, 19.29, 20.0], [429, 1, true, 20, 0, 24.59, 24.9], [430, 1, true, 18, 0, 20.21, 21.4], [431, 3, true, 21, 0, 33.0, 33.5], [432, 3, true, 20, 0, 30.42, 31.9], [433, 1, true, 19, 0, 23.84, 24.2], [434, 3, true, 20, 0, 27.75, 28.2], [435, 2, true, 20, 0, 19.53, 20.0], [436, 3, true, 22, 0, 26.62, 27.5], [437, 2, true, 18, 0, 23.97, 24.3], [438, 3, true, 27, 0, 27.52, 28.1], [439, 2, true, 19, 0, 15.94, 16.3], [440, 1, true, 18, 0, 26.1, 26.5], [441, 2, true, 19, 0, 25.4, 25.8], [442, 2, true, 19, 0, 30.97, 31.4], [443, 1, true, 18, 0, 23.12, 23.5], [444, 3, true, 25, 0, 35.37, 35.8], [445, 1, true, 16, 0, 24.81, 26.1], [446, 1, true, 19, 0, 16.39, 16.7], [447, 2, true, 20, 0, 29.76, 30.2], [448, 3, true, 20, 0, 30.5, 32.4], [449, 3, true, 20, 0, 26.96, 28.8], [450, 1, true, 25, 0, 23.87, 24.4], [451, 3, true, 25, 0, 31.17, 32.9], [452, 2, true, 20, 0, 26.95, 27.4], [453, 3, true, 20, 0, 33.43, 33.8], [454, 2, true, 25, 0, 26.53, 27.0], [455, 3, true, 23, 0, 35.08, 35.6], [456, 2, true, 17, 0, 22.56, 22.9], [457, 1, true, 23, 0, 22.42, 22.9], [458, 1, true, 28, 0, 16.84, 17.3], [459, 2, true, 17, 0, 22.66, 22.9], [460, 1, true, 18, 0, 16.81, 18.0], [461, 3, true, 19, 0, 27.59, 28.1], [462, 2, true, 19, 0, 20.37, 20.6], [463, 3, true, 20, 0, 33.79, 34.2], [464, 1, true, 20, 0, 20.75, 22.7], [465, 1, true, 16, 0, 22.39, 22.6], [466, 2, true, 20, 0, 29.38, 30.4], [467, 1, true, 18, 0, 13.83, 14.3], [468, 1, true, 20, 0, 25.44, 25.9], [469, 1, true, 18, 0, 23.47, 23.9], [470, 3, true, 20, 0, 24.68, 25.0], [471, 1, true, 19, 0, 17.24, 19.9], [472, 1, true, 16, 0, 14.44, 14.8], [473, 1, true, 22, 0, 21.17, 21.5], [474, 1, true, 18, 0, 18.48, 18.8], [475, 2, true, 21, 0, 23.92, 24.3], [476, 3, true, 19, 0, 27.03, 27.6], [477, 2, true, 18, 0, 25.0, 25.3], [478, 1, true, 20, 0, 26.0, 26.6], [479, 3, true, 20, 0, 30.76, 32.6], [480, 3, true, 19, 0, 31.66, 32.7], [481, 2, true, 21, 0, 24.23, 24.7], [482, 1, true, 19, 0, 19.43, 22.0], [483, 1, true, 21, 0, 26.56, 27.0], [484, 3, true, 20, 0, 36.0, 36.4], [485, 3, true, 20, 0, 35.11, 37.4], [486, 2, true, 20, 0, 27.98, 28.3], [487, 2, true, 27, 0, 27.24, 27.7], [488, 3, true, 20, 0, 26.72, 29.7], [489, 3, true, 19, 0, 30.27, 33.1], [490, 2, true, 19, 0, 23.95, 26.3], [491, 2, true, 18, 0, 25.2, 25.5], [492, 3, true, 22, 0, 22.18, 22.5], [493, 3, true, 20, 0, 28.04, 28.8], [494, 2, true, 23, 0, 21.54, 22.0], [495, 1, true, 20, 0, 21.14, 22.4], [496, 1, true, 18, 0, 22.96, 23.2], [497, 1, true, 22, 0, 16.7, 17.8], [498, 2, true, 18, 0, 24.9, 25.2], [499, 3, true, 23, 0, 29.5, 30.5], [500, 2, true, 23, 0, 25.46, 26.9], [501, 3, true, 20, 0, 30.3, 30.7], [502, 1, true, 18, 0, 16.07, 16.3], [503, 1, true, 17, 0, 16.84, 18.6], [504, 3, true, 20, 0, 39.87, 42.4], [505, 3, true, 22, 0, 36.92, 37.7], [506, 2, true, 20, 0, 29.77, 30.1], [507, 3, true, 21, 0, 22.73, 24.7], [508, 2, true, 23, 0, 21.73, 22.6], [509, 3, true, 19, 0, 29.93, 32.0], [510, 1, true, 23, 0, 27.64, 28.2], [511, 3, true, 25, 0, 31.83, 32.2], [512, 2, true, 23, 0, 27.35, 27.7], [513, 3, true, 21, 0, 28.03, 28.4], [514, 3, true, 21, 0, 28.65, 30.6], [515, 1, true, 18, 0, 27.44, 29.2], [516, 1, true, 18, 0, 16.28, 16.9], [517, 2, true, 24, 0, 23.4, 25.1], [518, 1, true, 26, 0, 26.55, 27.0], [519, 3, true, 23, 0, 28.49, 29.5], [520, 1, true, 16, 0, 25.74, 26.0], [521, 1, true, 25, 0, 17.35, 18.0], [522, 2, true, 21, 0, 28.94, 29.7], [523, 1, true, 20, 0, 25.81, 28.3], [524, 1, true, 18, 0, 23.42, 23.8], [525, 3, true, 22, 0, 27.61, 28.1], [526, 2, true, 23, 0, 29.3, 30.7], [527, 3, true, 20, 0, 27.36, 27.9], [528, 1, true, 18, 0, 19.95, 20.3], [529, 1, true, 17, 0, 20.62, 21.1], [530, 1, true, 21, 0, 16.27, 16.6], [531, 2, true, 23, 0, 22.83, 23.2], [532, 3, true, 22, 0, 30.11, 31.2], [533, 2, true, 21, 0, 16.75, 17.1], [534, 3, true, 22, 0, 35.53, 38.4], [535, 1, true, 18, 0, 16.68, 17.1], [536, 3, true, 22, 0, 32.41, 34.4], [537, 1, true, 16, 0, 17.15, 17.4], [538, 1, true, 18, 0, 22.96, 23.3], [539, 1, true, 18, 0, 13.59, 13.9], [540, 1, true, 17, 0, 16.54, 16.8], [541, 2, true, 17, 0, 18.44, 21.1], [542, 3, true, 25, 0, 26.44, 27.0], [543, 3, true, 20, 0, 29.21, 30.0], [544, 1, true, 18, 0, 11.67, 14.3], [545, 2, true, 18, 0, 23.91, 24.3], [546, 1, true, 22, 0, 15.9, 16.3], [547, 1, true, 18, 0, 21.85, 22.2], [548, 2, true, 20, 0, 26.94, 28.1], [549, 2, true, 21, 0, 22.25, 24.2], [550, 3, true, 27, 0, 20.95, 21.4], [551, 1, true, 27, 0, 16.89, 19.4], [552, 1, true, 16, 0, 21.48, 21.7], [553, 2, true, 19, 0, 20.81, 21.2], [554, 2, true, 20, 0, 28.3, 28.9], [555, 2, true, 20, 0, 23.78, 25.7], [556, 2, true, 19, 0, 24.13, 25.3], [557, 2, true, 19, 0, 22.42, 23.9], [558, 2, true, 18, 0, 27.72, 28.1], [559, 1, true, 19, 0, 15.41, 18.0], [560, 3, true, 21, 0, 28.5, 29.1], [561, 1, true, 21, 0, 21.19, 22.4], [562, 1, true, 16, 0, 25.38, 25.7], [563, 1, true, 18, 0, 27.6, 27.9], [564, 1, true, 19, 0, 20.04, 20.4], [565, 3, true, 20, 0, 38.78, 40.3], [566, 2, true, 18, 0, 31.97, 32.2], [567, 1, true, 20, 0, 30.55, 31.6], [568, 3, true, 20, 0, 34.17, 34.5], [569, 1, true, 27, 0, 21.17, 21.7], [570, 1, true, 20, 0, 16.98, 17.3], [571, 3, true, 20, 0, 30.41, 30.7], [572, 2, true, 16, 0, 29.31, 29.5], [573, 3, true, 22, 0, 37.07, 37.4], [574, 1, true, 29, 0, 21.45, 21.8], [575, 3, true, 20, 0, 28.15, 28.5], [576, 1, true, 27, 0, 23.77, 24.1], [577, 2, true, 19, 0, 26.03, 26.6], [578, 3, true, 21, 0, 30.51, 30.7], [579, 3, true, 22, 0, 32.09, 32.5], [580, 1, true, 18, 0, 32.63, 33.0], [581, 1, true, 23, 0, 22.8, 23.2], [582, 3, true, 21, 0, 34.72, 35.6], [583, 1, true, 16, 0, 21.01, 21.1], [584, 1, true, 18, 0, 29.92, 30.6], [585, 1, true, 16, 0, 26.34, 26.5], [586, 3, true, 20, 0, 28.25, 28.4], [587, 3, true, 21, 0, 27.73, 27.8], [588, 1, true, 18, 0, 18.74, 18.8], [589, 2, true, 20, 0, 18.97, 19.1], [590, 2, true, 21, 0, 22.14, 22.2], [591, 1, true, 19, 0, 16.62, 16.7], [592, 2, true, 16, 0, 16.97, 17.1], [593, 3, true, 20, 0, 20.31, 20.4], [594, 2, true, 26, 0, 15.4, 15.6], [595, 3, true, 19, 0, 16.07, 16.2], [596, 3, true, 20, 0, 14.53, 14.7], [597, 3, true, 20, 0, 13.59, 13.7], [598, 1, true, 19, 0, 10.56, 10.7], [599, 3, true, 21, 0, 8.22, 8.4]]
\ No newline at end of file
diff --git a/test_cnt.py b/test_cnt.py
index ce0c010..abf4ab6 100644
--- a/test_cnt.py
+++ b/test_cnt.py
@@ -19,8 +19,10 @@ def run(seed):
   19     19      env.close()
   20     20      return seed, n, term, steps, ap.replans, round(tp,2), round(time.time()-t0,1)
   21     21  from concurrent.futures import ThreadPoolExecutor
   22        -with ThreadPoolExecutor(8) as ex: res=list(ex.map(run, range(int(sys.argv[2]), int(sys.argv[3]))))
          22 +NT=int(sys.argv[4]) if len(sys.argv)>4 else 8
          23 +with ThreadPoolExecutor(NT) as ex: res=list(ex.map(run, range(int(sys.argv[2]), int(sys.argv[3]))))
   23     24  for r in res:
   24     25      if len(r)<5 or not r[2] or r[4]: print(r)
   25     26  ok=[r for r in res if r[2] is True]
          27 +print(sorted(ok,key=lambda r:-r[5])[:4])
   26     28  print('solved',len(ok),len(res),'mean',np.mean([r[3] for r in ok]),'maxplan',max(r[5] for r in ok))
```

</details>

<a id="C034"></a>
### C034 · Regression check seeds 0-200: 200/200, mean 20.74

Commit `1767f02f9c2c915a6dfdf14f9ab06b30d47db016`; parents: f24e3a234fd70ef1e1cfd31441f506529b817c54. Recorded author date: 2026-10-01T13:34:05+02:00.

File roles (automatic): setup/other.

- [E1513](01_timeline.md#E1513): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C034_1767f02.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/res_final0.json b/res_final0.json
new file mode 100644
index 0000000..502a2b4
--- /dev/null
+++ b/res_final0.json
@@ -0,0 +1 @@
           1 +[[0, 3, true, 25, 0, 9.25, 9.4], [1, 2, true, 18, 0, 14.0, 14.1], [2, 3, true, 19, 0, 19.87, 20.6], [3, 3, true, 21, 0, 17.46, 17.6], [4, 3, true, 20, 0, 19.02, 19.5], [5, 3, true, 23, 0, 19.84, 20.3], [6, 2, true, 19, 0, 18.08, 18.2], [7, 3, true, 22, 0, 20.93, 21.1], [8, 3, true, 20, 0, 19.01, 19.2], [9, 2, true, 22, 0, 17.91, 18.5], [10, 3, true, 20, 0, 30.94, 31.2], [11, 1, true, 19, 0, 13.99, 14.1], [12, 2, true, 22, 0, 21.68, 21.9], [13, 3, true, 23, 0, 30.86, 31.2], [14, 1, true, 29, 0, 15.77, 16.0], [15, 3, true, 23, 0, 32.41, 32.7], [16, 2, true, 21, 0, 32.68, 32.9], [17, 3, true, 22, 0, 50.88, 52.1], [18, 3, true, 22, 0, 37.51, 38.6], [19, 2, true, 25, 0, 21.74, 22.1], [20, 3, true, 27, 0, 30.29, 32.3], [21, 1, true, 19, 0, 21.75, 22.2], [22, 3, true, 21, 0, 37.26, 38.3], [23, 1, true, 16, 0, 27.76, 28.2], [24, 2, true, 18, 0, 26.39, 26.7], [25, 2, true, 18, 0, 30.25, 31.6], [26, 3, true, 21, 0, 35.37, 35.7], [27, 1, true, 21, 0, 16.8, 17.8], [28, 2, true, 21, 0, 23.89, 24.4], [29, 3, true, 20, 0, 27.4, 29.5], [30, 1, true, 20, 0, 15.64, 16.4], [31, 2, true, 24, 0, 21.07, 23.3], [32, 3, true, 18, 0, 25.83, 28.8], [33, 3, true, 22, 0, 23.45, 25.7], [34, 1, true, 18, 0, 15.62, 16.1], [35, 1, true, 18, 0, 14.13, 15.0], [36, 2, true, 20, 0, 19.8, 20.2], [37, 1, true, 18, 0, 15.37, 16.4], [38, 1, true, 20, 0, 16.21, 16.5], [39, 3, true, 22, 0, 22.53, 23.1], [40, 2, true, 21, 0, 27.89, 28.4], [41, 2, true, 18, 0, 20.99, 21.3], [42, 1, true, 20, 0, 25.86, 27.5], [43, 2, true, 24, 0, 24.77, 26.1], [44, 3, true, 19, 0, 28.11, 28.6], [45, 3, true, 20, 0, 28.34, 28.6], [46, 2, true, 18, 0, 24.48, 24.8], [47, 1, true, 20, 0, 22.19, 22.6], [48, 1, true, 19, 0, 23.48, 23.9], [49, 1, true, 20, 0, 29.02, 29.6], [50, 3, true, 21, 0, 36.89, 37.3], [51, 2, true, 20, 0, 23.36, 23.7], [52, 3, true, 22, 0, 27.11, 28.2], [53, 3, true, 20, 0, 33.54, 33.9], [54, 1, true, 20, 0, 23.17, 23.6], [55, 3, true, 26, 0, 36.01, 37.3], [56, 2, true, 22, 0, 27.21, 27.7], [57, 1, true, 16, 0, 21.5, 21.8], [58, 2, true, 23, 0, 26.31, 27.8], [59, 3, true, 20, 0, 35.31, 37.9], [60, 1, true, 22, 0, 19.96, 20.4], [61, 2, true, 19, 0, 24.47, 24.9], [62, 2, true, 21, 0, 25.99, 26.4], [63, 2, true, 21, 0, 28.63, 29.4], [64, 2, true, 21, 0, 25.92, 28.3], [65, 1, true, 16, 0, 22.3, 22.6], [66, 3, true, 21, 0, 24.75, 25.2], [67, 3, true, 20, 0, 28.37, 28.8], [68, 2, true, 19, 0, 21.83, 24.9], [69, 1, true, 20, 0, 12.8, 13.3], [70, 2, true, 20, 0, 25.9, 26.3], [71, 3, true, 20, 0, 32.38, 34.9], [72, 3, true, 20, 0, 32.99, 35.1], [73, 3, true, 20, 0, 28.05, 28.6], [74, 1, true, 20, 0, 21.56, 22.0], [75, 2, true, 18, 0, 22.37, 23.5], [76, 2, true, 22, 0, 28.51, 29.1], [77, 1, true, 18, 0, 21.2, 22.2], [78, 3, true, 21, 0, 28.61, 30.8], [79, 1, true, 23, 0, 20.58, 21.0], [80, 3, true, 20, 0, 36.4, 37.5], [81, 1, true, 18, 0, 16.67, 17.9], [82, 3, true, 19, 0, 29.67, 30.3], [83, 3, true, 21, 0, 27.91, 28.4], [84, 2, true, 22, 0, 28.02, 30.0], [85, 3, true, 19, 0, 35.29, 35.6], [86, 3, true, 20, 0, 27.07, 27.5], [87, 2, true, 23, 0, 29.5, 31.4], [88, 2, true, 18, 0, 27.79, 28.3], [89, 3, true, 29, 0, 23.81, 24.2], [90, 2, true, 20, 0, 26.91, 27.4], [91, 3, true, 22, 0, 21.17, 21.7], [92, 2, true, 22, 0, 23.91, 25.2], [93, 3, true, 22, 0, 28.15, 28.7], [94, 1, true, 20, 0, 26.88, 28.3], [95, 2, true, 20, 0, 23.06, 24.4], [96, 3, true, 21, 0, 27.11, 29.0], [97, 1, true, 27, 0, 21.2, 24.7], [98, 2, true, 22, 0, 17.16, 19.8], [99, 3, true, 22, 0, 27.6, 27.9], [100, 3, true, 23, 0, 27.64, 29.3], [101, 1, true, 17, 0, 10.37, 10.6], [102, 2, true, 21, 0, 27.73, 28.3], [103, 2, true, 21, 0, 27.22, 29.4], [104, 3, true, 19, 0, 28.46, 32.2], [105, 1, true, 20, 0, 20.03, 20.4], [106, 2, true, 19, 0, 22.59, 25.6], [107, 1, true, 20, 0, 24.53, 29.1], [108, 1, true, 19, 0, 19.88, 23.1], [109, 2, true, 19, 0, 24.55, 24.9], [110, 2, true, 20, 0, 23.41, 24.0], [111, 2, true, 20, 0, 24.22, 24.6], [112, 1, true, 18, 0, 23.23, 24.8], [113, 1, true, 19, 0, 20.76, 23.1], [114, 1, true, 18, 0, 21.48, 24.2], [115, 2, true, 21, 0, 21.26, 23.4], [116, 1, true, 21, 0, 18.81, 21.8], [117, 1, true, 24, 0, 14.49, 18.2], [118, 2, true, 19, 0, 21.28, 21.7], [119, 2, true, 20, 0, 22.66, 23.0], [120, 1, true, 18, 0, 24.74, 25.1], [121, 1, true, 20, 0, 22.04, 22.5], [122, 3, true, 20, 0, 28.49, 28.9], [123, 1, true, 20, 0, 26.64, 28.2], [124, 3, true, 22, 0, 28.23, 29.5], [125, 2, true, 18, 0, 27.87, 29.2], [126, 1, true, 18, 0, 22.54, 22.9], [127, 2, true, 21, 0, 21.09, 21.6], [128, 3, true, 20, 0, 24.71, 26.0], [129, 2, true, 21, 0, 22.01, 22.5], [130, 3, true, 23, 0, 25.03, 25.6], [131, 2, true, 20, 0, 28.38, 28.7], [132, 3, true, 24, 0, 37.83, 38.9], [133, 2, true, 18, 0, 20.59, 22.8], [134, 3, true, 23, 0, 39.04, 41.7], [135, 2, true, 18, 0, 25.83, 26.1], [136, 3, true, 22, 0, 24.84, 26.4], [137, 2, true, 21, 0, 25.3, 26.2], [138, 2, true, 22, 0, 18.97, 23.3], [139, 2, true, 19, 0, 19.91, 22.5], [140, 2, true, 18, 0, 25.93, 26.2], [141, 2, true, 18, 0, 21.14, 21.5], [142, 1, true, 18, 0, 24.8, 26.8], [143, 3, true, 22, 0, 26.47, 28.1], [144, 1, true, 19, 0, 18.88, 19.4], [145, 2, true, 23, 0, 22.74, 24.0], [146, 3, true, 20, 0, 25.34, 25.7], [147, 1, true, 18, 0, 16.72, 18.2], [148, 1, true, 18, 0, 23.83, 24.3], [149, 1, true, 16, 0, 13.23, 14.9], [150, 2, true, 20, 0, 26.53, 28.6], [151, 3, true, 25, 0, 33.82, 37.3], [152, 3, true, 27, 0, 30.04, 33.6], [153, 3, true, 22, 0, 26.56, 28.2], [154, 1, true, 20, 0, 19.41, 19.8], [155, 1, true, 16, 0, 22.25, 25.5], [156, 3, true, 20, 0, 28.21, 30.7], [157, 1, true, 20, 0, 14.62, 15.0], [158, 2, true, 20, 0, 18.61, 19.1], [159, 3, true, 20, 0, 27.4, 27.8], [160, 1, true, 18, 0, 23.35, 23.7], [161, 3, true, 20, 0, 28.26, 32.6], [162, 2, true, 27, 0, 25.47, 27.9], [163, 2, true, 18, 0, 22.73, 23.9], [164, 2, true, 27, 0, 20.68, 23.2], [165, 2, true, 19, 0, 15.14, 18.1], [166, 3, true, 20, 0, 22.78, 23.1], [167, 3, true, 21, 0, 19.82, 20.2], [168, 2, true, 20, 0, 24.34, 24.7], [169, 3, true, 31, 0, 24.33, 27.9], [170, 3, true, 22, 0, 21.24, 23.5], [171, 3, true, 21, 0, 24.21, 26.6], [172, 2, true, 20, 0, 26.97, 29.4], [173, 3, true, 33, 0, 23.96, 27.1], [174, 2, true, 20, 0, 16.19, 16.6], [175, 3, true, 21, 0, 32.92, 33.2], [176, 1, true, 21, 0, 12.55, 12.9], [177, 3, true, 21, 0, 33.93, 34.3], [178, 2, true, 22, 0, 27.19, 27.6], [179, 3, true, 22, 0, 25.42, 25.7], [180, 1, true, 19, 0, 20.51, 20.8], [181, 3, true, 23, 0, 23.24, 23.7], [182, 3, true, 18, 0, 29.97, 30.3], [183, 3, true, 21, 0, 35.93, 36.4], [184, 2, true, 23, 0, 29.06, 29.4], [185, 1, true, 19, 0, 26.26, 26.8], [186, 1, true, 37, 0, 27.46, 29.1], [187, 2, true, 20, 0, 21.46, 22.4], [188, 2, true, 18, 0, 30.49, 30.8], [189, 2, true, 29, 0, 31.06, 31.5], [190, 1, true, 18, 0, 18.22, 18.6], [191, 1, true, 21, 0, 27.41, 27.7], [192, 3, true, 22, 0, 33.26, 33.6], [193, 2, true, 21, 0, 34.32, 34.7], [194, 3, true, 20, 0, 29.65, 29.9], [195, 1, true, 18, 0, 22.86, 23.2], [196, 1, true, 16, 0, 28.81, 29.1], [197, 3, true, 19, 0, 27.67, 27.9], [198, 2, true, 22, 0, 24.87, 25.1], [199, 2, true, 19, 0, 15.56, 15.7]]
\ No newline at end of file
```

</details>

