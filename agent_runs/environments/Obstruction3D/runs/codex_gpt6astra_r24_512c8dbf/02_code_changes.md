# Obstruction3D · gpt-6-astra · replicate 24: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `92a6099` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `c8fd213` | Initialize valid policy and initial state probe | approach.py, probe_initial.py | [E0007](01_timeline.md#E0007) |
| [C003](#C003) · `fb686af` | Add independent control-effect probing script | probe_controls.py | No matched commit command/output |
| [C004](#C004) · `31836f1` | Probe repeated signed controls and gripper behavior | probe_controls.py | No matched commit command/output |
| [C005](#C005) · `699eb0c` | Add independent fixed posture grasp scan experiment | probe_grasp.py | No matched commit command/output |
| [C006](#C006) · `680c6e2` | Add base collision boundary and arm posture probes | probe_boundaries.py | No matched commit command/output |
| [C007](#C007) · `b08da15` | Probe joint limits clear of table | kinematics_probe.py, probe_limits.py | No matched commit command/output |
| [C008](#C008) · `c35e55a` | Add analytic Kinova geometry and empirical grasp calibration probes | kin.py, probe_ik.py | [E0020](01_timeline.md#E0020) |
| [C009](#C009) · `c5be216` | Fix stalled motion comparison in grasp calibration | probe_ik.py | [E0022](01_timeline.md#E0022) |
| [C010](#C010) · `7961dc1` | Implement initial analytic grasp approach for visual calibration | approach.py | [E0024](01_timeline.md#E0024) |
| [C011](#C011) · `cf12688` | Add fine approach grasp threshold probe | probe_fine.py | [E0028](01_timeline.md#E0028) |
| [C012](#C012) · `26cf3aa` | Use gradual Cartesian descent for grasp calibration | approach.py | [E0035](01_timeline.md#E0035) |
| [C013](#C013) · `23f2a80` | Probe local grasp volume and wrist orientation | probe_grid.py | [E0041](01_timeline.md#E0041) |
| [C014](#C014) · `1103f41` | Record additional gripper state diagnostics | probe_close.py | [E0045](01_timeline.md#E0045) |
| [C015](#C015) · `8ea5584` | Add broad fresh-instance grasp offset sweep | probe_wide.py | No matched commit command/output |
| [C016](#C016) · `442c1b3` | Probe systematic tool frame offsets with independent descents | probe_offset.py | [E0047](01_timeline.md#E0047) |
| [C017](#C017) · `6aa1a3c` | Calibrate true tool transform from successful grasp and test release settling | probe_grasp_calibrate.py, probe_wide.out | No matched commit command/output |
| [C018](#C018) · `4ea2488` | Implement calibrated grasp lift transport and release policy | approach.py, test_approach.py | [E0058](01_timeline.md#E0058) |
| [C019](#C019) · `f89f9f5` | Bound diagnostic episodes to expose stalled phases quickly | test_approach.py | [E0055](01_timeline.md#E0055) |
| [C020](#C020) · `ff23967` | Measure release support tolerance above tabletop | probe_release.py | No matched commit command/output |
| [C021](#C021) · `aeeb289` | Measure horizontal and vertical grasp tolerances | probe_grasp_tolerance.py, probe_release.out | No matched commit command/output |
| [C022](#C022) · `60027ab` | Test constant arm reach with mobile base alignment | probe_grasp_tolerance.out, probe_reach.py | [E0062](01_timeline.md#E0062) |
| [C023](#C023) · `cf6dd70` | Probe obstruction placement support on blocks, table and ground | probe_dispose.py | No matched commit command/output |
| [C024](#C024) · `cbc033b` | Make disposal probe stop after reaching each waypoint | probe_dispose.out | No matched commit command/output |
| [C025](#C025) · `d72af45` | Bound each disposal motion by waypoint convergence | probe_dispose.py | No matched commit command/output |
| [C026](#C026) · `b2f17e6` | Clear obstructing blocks and transport with constant reach and vertical wrist | approach.py | [E0068](01_timeline.md#E0068) |
| [C027](#C027) · `b42bb93` | Rotate obstruction grasp to avoid neighboring obstruction | probe_dispose.out, probe_dispose.py | No matched commit command/output |
| [C028](#C028) · `2ca60a6` | Add object-level diagnostics for clearance failures | debug_policy.py, probe_dispose.out | [E0067](01_timeline.md#E0067) |
| [C029](#C029) · `5104aa5` | Descend finely to grasp short obstructions before contact | approach.py, probe_dispose.out, test_approach.py | [E0087](01_timeline.md#E0087) |
| [C030](#C030) · `71c4484` | Add independent seeds20-39 robustness sweep | debug2.txt, test_results.txt, test_sweep_agent.py | No matched commit command/output |
| [C031](#C031) · `b4b99fb` | Retry blocked grasps from perpendicular wrist orientations | approach.py, debug2.txt, test_results.txt, test_sweep_agent.out | [E0089](01_timeline.md#E0089) |
| [C032](#C032) · `b2a9ce7` | Replace iterative inverse kinematics with exact constant-time planar solution | debug2.txt, kin.py, retry_results.txt, test_results.txt, test_sweep_agent.out | [E0095](01_timeline.md#E0095) |
| [C033](#C033) · `3b0865e` | Support explicit object-count robustness sweeps | fast_results.txt, retry_results.txt, test_results.txt, test_sweep_agent.out, test_sweep_agent.py | No matched commit command/output |
| [C034](#C034) · `adf87a6` | Add evaluations for larger variable object counts | fast_results.txt, test_counts.py, test_sweep_fast.out | [E0111](01_timeline.md#E0111) |
| [C035](#C035) · `859a11f` | Handle incidental grasps and adapt obstruction placement to crowded tables | approach.py, count_results.txt, test_sweep_fast.out | [E0103](01_timeline.md#E0103) |
| [C036](#C036) · `7fc3841` | Shorten safe vertical transit paths to reduce episode time | approach.py, approach_safe.py, count_results.txt, test_quick.py, test_sweep_extended.out | [E0123](01_timeline.md#E0123) |
| [C037](#C037) · `eeb5457` | Reserve gripper clearance around obstruction disposal sites | approach.py, debug_policy.py, quick_results.txt, test_sweep_extended.out | [E0120](01_timeline.md#E0120) |
| [C038](#C038) · `7ba3e01` | Park incidentally grasped target until remaining obstructions are cleared | approach.py, count_fast_results.txt, debug_count10.txt, quick_results.txt, test_sweep_extended.out | [E0130](01_timeline.md#E0130) |
| [C039](#C039) · `e42e289` | Add timed high-count stress test for the evaluation deadline | count_fast_results.txt, test_one.py, test_sweep_current.out, test_sweep_extended.out | [E0141](01_timeline.md#E0141) |
| [C040](#C040) · `0f72a23` | Advance completed motion phases without spending idle environment steps | approach.py, stress20.txt, test_sweep_current.out | [E0150](01_timeline.md#E0150) |
| [C041](#C041) · `5ec1010` | Add geometry diagnostics for dense-scene grasp failures | probe_dense.py, stress20.txt, test_sweep_current.out | [E0155](01_timeline.md#E0155) |
| [C042](#C042) · `7026fff` | Clear accessible neighbors before retrying densely surrounded blocks | approach.py, test_sweep_current.out | [E0159](01_timeline.md#E0159) |
| [C043](#C043) · `ae33aac` | Probe collision escape actions after dense-scene disposal | dense_agent_0_50.out, dense_agent_2_20.out, dense_agent_3_20.out, final_regression.txt, probe_escape_dense.py, stress20_reordered.txt | No matched commit command/output |
| [C044](#C044) · `95c2eaa` | Use NumPy-only kinematics and preserve dense-scene validation logs | kin.py, probe_escape_dense.out | [E0178](01_timeline.md#E0178) |
| [C045](#C045) · `59bf82b` | Test reclosing gripper to escape post-release collision | probe_escape_dense.out, probe_escape_dense.py | No matched commit command/output |
| [C046](#C046) · `ad154b2` | Recover trapped release poses by regrasping and relocating the deposited block | approach.py, probe_escape_reclose.out | [E0183](01_timeline.md#E0183) |
| [C047](#C047) · `60df503` | Remember rejected disposal sites across regrasp recovery attempts | approach.py, stress50_recovery.txt | [E0188](01_timeline.md#E0188) |
| [C048](#C048) · `3735a6d` | Record final stress tests and diagnose dense held-object lift collision | final_regression.txt, probe_lift.py, stress50_seed1.txt, stress50_seed2.txt | [E0199](01_timeline.md#E0199) |
| [C049](#C049) · `adb0df5` | Use finer vertical lift steps when dense neighboring objects block a grasped block | approach.py, probe_lift.out | [E0203](01_timeline.md#E0203) |
| [C050](#C050) · `e4d97ea` | Save final successful regression and 50-obstruction validation results | final_dense20.txt, final_dense50.txt, final_targeted.txt, stress50_fine_lift.txt | [E0214](01_timeline.md#E0214) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `92a6099b1a90ac5f3b2ed1c48dfd1c1676b9352d`; parents: none (initial snapshot). Recorded author date: 2026-09-20T02:40:24+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_92a6099.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
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
diff --git a/AGENTS.md b/AGENTS.md
new file mode 100644
index 0000000..76dfa5b
--- /dev/null
+++ b/AGENTS.md
@@ -0,0 +1,13 @@
           1 +You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). This environment's observations are object-centric states (a set of typed objects), not flat vectors, so render_state's arbitrary-state mode does not apply. Both render_state and render_policy take an optional object_count to pin the number of objects. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
           2 +
           3 +Your maximum experiment budget is $20.00; your configured remaining budget for this invocation is $20.00. This budget is shared across the main agent, all subagents, and every continuation. Read `.agent_sessions/codex/budget_status.json` for the live maximum, cumulative estimated spend, and remaining budget. Continue working, testing, and improving the solution to solve as many seeds as possible within this budget. The harness will stop you when the budget is exhausted. Only stop early if you are extremely confident in the solution based on your testing; in that case, create `.agent_sessions/codex/solution_confident` before giving your final response.
           4 +
           5 +Read `.agent_sessions/codex/budget_status.json` before starting further experiments or delegating work. The $2 and $1 warnings change priorities, not permission to work: `wrap_up` is advisory, not an instruction to exit. At most $2 left: preserve and commit your best working approach, avoid broad exploration or new subagents, and use the remaining budget for targeted validation and small fixes. At most $1 left: prioritize essential quick checks, minimal corrections, and saving a valid final policy. If not confident, keep doing useful finishing work within the remaining budget; do not repeatedly return a final answer merely because a warning is active. Keep a valid approach.py on disk throughout: the harness evaluates the last saved code at the hard cutoff, regardless of confidence or whether you made a final commit. Do not modify the status file or usage logs. Before every normal final response, explicitly decide confidence: create the confidence marker only if extremely confident based on tests; otherwise leave it absent. Never claim confidence simply to prevent a continuation.
           6 +
           7 +All files you create MUST use relative paths so they stay in the current working directory (/sandbox). Never write files using absolute paths.
           8 +
           9 +CONTEXT MANAGEMENT: your context window is limited and you MUST protect it aggressively: (1) When running Bash commands, pipe output through `head` or `tail` to limit verbosity if possible. (2) Keep your thinking brief, do not write long reasoning traces. (3) Keep your main conversation focused on writing and testing code, not on reading source or reasoning at length.
          10 +
          11 +The Python interpreter is at /opt/robocode-strict/bin/python
          12 +Run test scripts with:
          13 +    /opt/robocode-strict/bin/python test_approach.py
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
index 0000000..937fe84
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "ff07148c4450258035d72e9b50e72607", "observation_space": {"type": "ObjectCentric", "types": [{"name": "Kinematic3DCuboid", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z"]}, {"name": "Kinematic3DFixture", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]}, {"name": "Kinematic3DPoint", "parent": null, "features": ["x", "y", "z"]}, {"name": "Kinematic3DRobot", "parent": null, "features": ["pos_base_x", "pos_base_y", "pos_base_rot", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7", "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z", "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw"]}, {"name": "Kinematic3DTriangle", "parent": null, "features": ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw", "grasp_active", "triangle_type", "side_a", "side_b", "depth"]}]}, "action_space": {"type": "Box", "shape": [11], "low": [-0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -0.20000000298023224, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Initialize valid policy and initial state probe

Commit `c8fd213af54640dd7990b8aceeb0618ed313179d`; parents: 92a6099b1a90ac5f3b2ed1c48dfd1c1676b9352d. Recorded author date: 2026-09-20T02:40:55+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0007](01_timeline.md#E0007): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_c8fd213_approach.py) · [Exact all-file diff](evidence/diffs/C002_c8fd213.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..eb739fb
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,11 @@
           1 +import numpy as np
           2 +
           3 +class GeneratedApproach:
           4 +    def __init__(self, action_space, observation_space, primitives):
           5 +        self.action_space = action_space
           6 +        self.observation_space = observation_space
           7 +    def reset(self, state, info):
           8 +        self.t = 0
           9 +    def get_action(self, state):
          10 +        self.t += 1
          11 +        return np.zeros(11, dtype=np.float32)
diff --git a/probe_initial.py b/probe_initial.py
new file mode 100644
index 0000000..9c21b03
--- /dev/null
+++ b/probe_initial.py
@@ -0,0 +1,10 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +E=make_env()
           4 +s,i=E.reset(seed=0)
           5 +print('INFO',i,'MAX',E.max_steps)
           6 +for typ in E.observation_space.types:
           7 + print('TYPE',typ)
           8 + for obj in s.get_objects(typ):
           9 +  print(obj, {f:s.get(obj,f) for f in E.observation_space.type_features[typ]})
          10 +E.close()
```

</details>

<a id="C003"></a>
### C003 · Add independent control-effect probing script

Commit `fb686af5772b0053c87cb4838f4e9306bc1a0662`; parents: c8fd213af54640dd7990b8aceeb0618ed313179d. Recorded author date: 2026-09-20T02:41:04+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C003_fb686af.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_controls.py b/probe_controls.py
new file mode 100644
index 0000000..2d1d6ee
--- /dev/null
+++ b/probe_controls.py
@@ -0,0 +1,16 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def dump(e,s):
           5 + for t in e.observation_space.types:
           6 +  for o in s.get_objects(t):
           7 +   print(o.name,{f:round(float(s.get(o,f)),6) for f in e.observation_space.type_features[t]},flush=True)
           8 +e=make_env();s,i=e.reset(seed=0);print('INITIAL',i);dump(e,s)
           9 +for j in range(11):
          10 + s,i=e.reset(seed=0);a=np.zeros(11,dtype=np.float32);a[j]=.2 if j<10 else -1
          11 + t,r,d,tr,i=e.step(a);print('ACTION',j,'r',r,'done',d,i,flush=True)
          12 + for ty in e.observation_space.types:
          13 +  for o in t.get_objects(ty):
          14 +   changed={f:(round(float(s.get(o,f)),5),round(float(t.get(o,f)),5)) for f in e.observation_space.type_features[ty] if abs(s.get(o,f)-t.get(o,f))>1e-7}
          15 +   if changed:print(o.name,changed,flush=True)
          16 +e.close()
```

</details>

<a id="C004"></a>
### C004 · Probe repeated signed controls and gripper behavior

Commit `31836f148705f6c5aa42b10db3bebe66cd55a402`; parents: fb686af5772b0053c87cb4838f4e9306bc1a0662. Recorded author date: 2026-09-20T02:41:30+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C004_31836f1.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_controls.py b/probe_controls.py
index 2d1d6ee..07e5233 100644
--- a/probe_controls.py
+++ b/probe_controls.py
@@ -1,16 +1,14 @@
    1      1  from env_client import make_env
    2      2  import numpy as np
    3      3  
    4        -def dump(e,s):
    5        - for t in e.observation_space.types:
    6        -  for o in s.get_objects(t):
    7        -   print(o.name,{f:round(float(s.get(o,f)),6) for f in e.observation_space.type_features[t]},flush=True)
    8        -e=make_env();s,i=e.reset(seed=0);print('INITIAL',i);dump(e,s)
    9        -for j in range(11):
   10        - s,i=e.reset(seed=0);a=np.zeros(11,dtype=np.float32);a[j]=.2 if j<10 else -1
   11        - t,r,d,tr,i=e.step(a);print('ACTION',j,'r',r,'done',d,i,flush=True)
   12        - for ty in e.observation_space.types:
   13        -  for o in t.get_objects(ty):
   14        -   changed={f:(round(float(s.get(o,f)),5),round(float(t.get(o,f)),5)) for f in e.observation_space.type_features[ty] if abs(s.get(o,f)-t.get(o,f))>1e-7}
   15        -   if changed:print(o.name,changed,flush=True)
           4 +e=make_env()
           5 +for j in [0,1,2,3,4,5,6,7,8,9,10]:
           6 + for direction in [-1,1]:
           7 +  s,_=e.reset(seed=0); rob=s.get_object_from_name('robot');a=np.zeros(11,dtype=np.float32);a[j]=direction*(.2 if j<10 else 1)
           8 +  for k in range(8):
           9 +   t,r,d,tr,i=e.step(a)
          10 +   fields=['pos_base_x','pos_base_y','pos_base_rot']+['joint_'+str(n) for n in range(1,8)]+['finger_state','grasp_active']
          11 +   changes={f:round(float(t.get(rob,f)),5) for f in fields if abs(s.get(rob,f)-t.get(rob,f))>1e-7}
          12 +   print(j,direction,k,changes,flush=True);s=t
          13 +   if not changes: break
   16     14  e.close()
```

</details>

<a id="C005"></a>
### C005 · Add independent fixed posture grasp scan experiment

Commit `699eb0cc571862a3e92ca41c74ff49454d2e753f`; parents: 31836f148705f6c5aa42b10db3bebe66cd55a402. Recorded author date: 2026-09-20T02:41:45+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C005_699eb0c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
new file mode 100644
index 0000000..6e4b169
--- /dev/null
+++ b/probe_grasp.py
@@ -0,0 +1,20 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +import time
           4 +E=make_env();s,_=E.reset(seed=0)
           5 +robot=s.get_object_from_name('robot')
           6 +print('robot', {f:float(s.get(robot,f)) for f in ['pos_base_x','pos_base_y','grasp_tf_x','grasp_tf_y','grasp_tf_z']},flush=True)
           7 +start=time.time()
           8 +for x in np.arange(-.4,.61,.1):
           9 + for y in np.arange(-.4,.61,.1):
          10 +  s,_=E.reset(seed=0)
          11 +  for k in range(10):
          12 +   a=np.zeros(11,dtype=np.float32)
          13 +   a[:2]=np.clip([x-s.get(robot,'pos_base_x'),y-s.get(robot,'pos_base_y')],-.2,.2)
          14 +   if np.linalg.norm(a[:2])<1e-5:break
          15 +   s,*_=E.step(a)
          16 +  a=np.zeros(11,dtype=np.float32);a[-1]=-1;s,r,d,tr,i=E.step(a)
          17 +  if s.get(robot,'grasp_active'):
          18 +   print('GRASP',x,y,{f:float(s.get(robot,f)) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']},flush=True)
          19 + print('row',x,'elapsed',time.time()-start,flush=True)
          20 +E.close()
```

</details>

<a id="C006"></a>
### C006 · Add base collision boundary and arm posture probes

Commit `680c6e2059653ca65fb150c700a6b3b1672f52d0`; parents: 699eb0cc571862a3e92ca41c74ff49454d2e753f. Recorded author date: 2026-09-20T02:41:56+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C006_680c6e2.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_boundaries.py b/probe_boundaries.py
new file mode 100644
index 0000000..c70f3a9
--- /dev/null
+++ b/probe_boundaries.py
@@ -0,0 +1,22 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +e=make_env()
           5 +def act(s,j,v):
           6 + a=np.zeros(11,dtype=np.float32);a[j]=v
           7 + return e.step(a)[0]
           8 +def pos(s):
           9 + r=s.get_object_from_name('robot');return [round(s.get(r,f),4) for f in ['pos_base_x','pos_base_y','joint_2','joint_4','joint_6','finger_state']]
          10 +for y in [-.8,-.6,-.4,-.2,0,.2,.4,.6,.8]:
          11 + s,_=e.reset(seed=0)
          12 + for _ in range(round(abs(y)/.2)):s=act(s,1,np.sign(y)*.2)
          13 + for _ in range(5):s=act(s,0,.1)
          14 + print('BASETEST',y,pos(s),flush=True)
          15 +for j in [4,6,8]:
          16 + for delta in [-1,-.6,-.2,0,.2,.6,1]:
          17 +  s,_=e.reset(seed=0)
          18 +  for _ in range(round(abs(delta)/.2)):s=act(s,j,np.sign(delta)*.2)
          19 +  before=pos(s)
          20 +  for _ in range(3):s=act(s,0,.1)
          21 +  print('JOINTTEST',j,delta,before,pos(s),flush=True)
          22 +e.close()
```

</details>

<a id="C007"></a>
### C007 · Probe joint limits clear of table

Commit `b08da15112e4a7e114bc3c756a6927526d3a3373`; parents: 680c6e2059653ca65fb150c700a6b3b1672f52d0. Recorded author date: 2026-09-20T02:42:38+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C007_b08da15.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/kinematics_probe.py b/kinematics_probe.py
new file mode 100644
index 0000000..41ac332
--- /dev/null
+++ b/kinematics_probe.py
@@ -0,0 +1,10 @@
           1 +import numpy as np
           2 +from scipy.spatial.transform import Rotation as R
           3 +q=[0,-.35,-np.pi,-2.5,0,-.87,np.pi/2]
           4 +origins=[([0,0,.15643],np.pi),([0,.005375,-.12838],np.pi/2),([0,-.21038,-.006375],-np.pi/2),([0,.006375,-.21038],np.pi/2),([0,-.20843,-.006375],-np.pi/2),([0,0,-.10593],np.pi/2),([0,-.10593,0],-np.pi/2)]
           5 +t=np.array([-.12,0,0.]);r=np.eye(3)
           6 +for (p,a),j in zip(origins,q):
           7 + t+=r@p;r=r@R.from_euler('x',a).as_matrix()@R.from_euler('z',j).as_matrix()
           8 + print(t)
           9 +print('orientation',r)
          10 +for d in [.06,.12,.18]: print('ee',d,t+r@[0,0,-d])
diff --git a/probe_limits.py b/probe_limits.py
new file mode 100644
index 0000000..e48d429
--- /dev/null
+++ b/probe_limits.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +e=make_env()
           5 +for j in [4,6,8]:
           6 + for delta in [-.2,.2]:
           7 +  s,_=e.reset(seed=0);a=np.zeros(11,dtype=np.float32);a[0]=-.2
           8 +  for _ in range(5):s=e.step(a)[0]
           9 +  r=s.get_object_from_name('robot');f='joint_'+str(j-2)
          10 +  for k in range(35):
          11 +   old=s.get(r,f);a=np.zeros(11,dtype=np.float32);a[j]=delta;s=e.step(a)[0];new=s.get(r,f)
          12 +   if old==new:break
          13 +  print('LIMIT',j,delta,k,new,flush=True)
          14 +e.close()
```

</details>

<a id="C008"></a>
### C008 · Add analytic Kinova geometry and empirical grasp calibration probes

Commit `c35e55a520541050ae99cac985e6d44745d9e1d6`; parents: b08da15112e4a7e114bc3c756a6927526d3a3373. Recorded author date: 2026-09-20T02:42:53+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

- [E0020](01_timeline.md#E0020): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C008_c35e55a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/kin.py b/kin.py
new file mode 100644
index 0000000..a9ab955
--- /dev/null
+++ b/kin.py
@@ -0,0 +1,22 @@
           1 +import numpy as np
           2 +from scipy.spatial.transform import Rotation
           3 +from scipy.optimize import least_squares
           4 +ORIGINS=[([0,0,.15643],np.pi),([0,.005375,-.12838],np.pi/2),([0,-.21038,-.006375],-np.pi/2),([0,.006375,-.21038],np.pi/2),([0,-.20843,-.006375],-np.pi/2),([0,0,-.10593],np.pi/2),([0,-.10593,0],-np.pi/2)]
           5 +MATS=[Rotation.from_euler('x',a).as_matrix() for p,a in ORIGINS]
           6 +Q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
           7 +def fk(q,d=.18):
           8 + t=np.zeros(3);r=np.eye(3)
           9 + for (p,a),rx,j in zip(ORIGINS,MATS,q):
          10 +  c,s=np.cos(j),np.sin(j)
          11 +  rz=np.array([[c,-s,0],[s,c,0],[0,0,1]])
          12 +  t+=r@p;r=r@rx@rz
          13 + return t-r[:,2]*d,r
          14 +
          15 +def ik(x,z,d=.18):
          16 + def fun(v):
          17 +  q=Q0.copy();q[[1,3,5]]=v
          18 +  p,r=fk(q,d)
          19 +  return [p[0]-x,p[2]-z,r[0,2]]
          20 + fit=least_squares(fun,Q0[[1,3,5]],bounds=([-2,-2.57,-2],[2,2.57,2]),xtol=1e-10,gtol=1e-10,ftol=1e-10)
          21 + q=Q0.copy();q[[1,3,5]]=fit.x
          22 + return q
diff --git a/probe_ik.py b/probe_ik.py
new file mode 100644
index 0000000..e9e702e
--- /dev/null
+++ b/probe_ik.py
@@ -0,0 +1,26 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +E=make_env();s,_=E.reset(seed=0)
           4 +r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           5 +def vals(s,obj,fs):return np.array([s.get(obj,f) for f in fs])
           6 +fs=['joint_'+str(i) for i in range(1,8)]
           7 +x,y,z=vals(s,b,['pose_x','pose_y','pose_z'])
           8 +def move(q,by):
           9 + global s
          10 + for i in range(30):
          11 +  delta=q-vals(s,r,fs);a=np.zeros(11);a[3:10]=np.clip(delta,-.15,.15);a[1]=np.clip(by-s.get(r,'pos_base_y'),-.15,.15)
          12 +  if np.max(np.abs(a))<1e-5:return True
          13 +  old=s;s,*_=E.step(a)
          14 +  if np.max(np.abs(vals(s,r,fs)-vals(old,r,fs)))<1e-7 and abs(s.get(r,'pos_base_y')-s.get(old,r,'pos_base_y'))<1e-7:
          15 +   print('blocked',np.round(vals(s,r,fs),3));return False
          16 + return False
          17 +for d in [.18,.12,.06,.24]:
          18 + s,_=E.reset(seed=0)
          19 + q=ik(x+.12,.25,d);print('high',d,np.round(q,3),move(q,y-.001),flush=True)
          20 + for zt in np.arange(.22,.039,-.015):
          21 +  q=ik(x+.12,zt,d);ok=move(q,y-.001)
          22 +  a=np.zeros(11);a[10]=-1;s,*_=E.step(a)
          23 +  if s.get(r,'grasp_active'):
          24 +   print('GRASP',d,zt,vals(s,r,fs),{f:s.get(r,f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']},flush=True);E.close();raise SystemExit
          25 +  print('try',round(zt,3),ok,flush=True)
          26 +E.close()
```

</details>

<a id="C009"></a>
### C009 · Fix stalled motion comparison in grasp calibration

Commit `c5be2165fe190f26317f71664a2c369cba349211`; parents: c35e55a520541050ae99cac985e6d44745d9e1d6. Recorded author date: 2026-09-20T02:43:03+02:00.

File roles (automatic): diagnostic/test.

- [E0022](01_timeline.md#E0022): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C009_c5be216.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_ik.py b/probe_ik.py
index e9e702e..5a5d640 100644
--- a/probe_ik.py
+++ b/probe_ik.py
@@ -11,7 +11,7 @@ def move(q,by):
   11     11    delta=q-vals(s,r,fs);a=np.zeros(11);a[3:10]=np.clip(delta,-.15,.15);a[1]=np.clip(by-s.get(r,'pos_base_y'),-.15,.15)
   12     12    if np.max(np.abs(a))<1e-5:return True
   13     13    old=s;s,*_=E.step(a)
   14        -  if np.max(np.abs(vals(s,r,fs)-vals(old,r,fs)))<1e-7 and abs(s.get(r,'pos_base_y')-s.get(old,r,'pos_base_y'))<1e-7:
          14 +  if np.max(np.abs(vals(s,r,fs)-vals(old,r,fs)))<1e-7 and abs(s.get(r,'pos_base_y')-old.get(r,'pos_base_y'))<1e-7:
   15     15     print('blocked',np.round(vals(s,r,fs),3));return False
   16     16   return False
   17     17  for d in [.18,.12,.06,.24]:
```

</details>

<a id="C010"></a>
### C010 · Implement initial analytic grasp approach for visual calibration

Commit `7961dc12ea119a056422391be4a9550d0f0c0869`; parents: c5be2165fe190f26317f71664a2c369cba349211. Recorded author date: 2026-09-20T02:43:29+02:00.

File roles (automatic): policy.

- [E0024](01_timeline.md#E0024): commit hash in recorded output.
[Controller after this commit](evidence/versions/C010_7961dc1_approach.py) · [Exact all-file diff](evidence/diffs/C010_7961dc1.diff)

[Previous saved controller snapshot](evidence/versions/C002_c8fd213_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index eb739fb..c2ffcd8 100644
--- a/approach.py
+++ b/approach.py
@@ -1,11 +1,21 @@
    1      1  import numpy as np
           2 +from kin import ik, Q0
    2      3  
    3      4  class GeneratedApproach:
    4      5      def __init__(self, action_space, observation_space, primitives):
    5        -        self.action_space = action_space
    6        -        self.observation_space = observation_space
    7        -    def reset(self, state, info):
    8        -        self.t = 0
    9        -    def get_action(self, state):
   10        -        self.t += 1
   11        -        return np.zeros(11, dtype=np.float32)
           6 +        self.action_space=action_space
           7 +        self.observation_space=observation_space
           8 +    def reset(self,state,info):
           9 +        self.t=0
          10 +        self.robot=state.get_objects(self.observation_space.get_type('Kinematic3DRobot'))[0]
          11 +        self.block=state.get_object_from_name('target_block')
          12 +    def get_action(self,state):
          13 +        self.t+=1;r=self.robot
          14 +        x=state.get(self.block,'pose_x');y=state.get(self.block,'pose_y')
          15 +        z=.25 if self.t<10 else .11
          16 +        q=ik(x-state.get(r,'pos_base_x'),z)
          17 +        a=np.zeros(11,dtype=np.float32)
          18 +        a[1]=y-.001-state.get(r,'pos_base_y')
          19 +        a[3:10]=q-np.array([state.get(r,'joint_'+str(i)) for i in range(1,8)])
          20 +        a[10]=-1 if self.t>=10 else 0
          21 +        return np.clip(a,self.action_space.low,self.action_space.high)
```

</details>

<a id="C011"></a>
### C011 · Add fine approach grasp threshold probe

Commit `cf12688095bcbbd57f6a592447a0bb468d28aeaa`; parents: 7961dc12ea119a056422391be4a9550d0f0c0869. Recorded author date: 2026-09-20T02:43:57+02:00.

File roles (automatic): diagnostic/test.

- [E0028](01_timeline.md#E0028): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C011_cf12688.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_fine.py b/probe_fine.py
new file mode 100644
index 0000000..52faa98
--- /dev/null
+++ b/probe_fine.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +E=make_env();s,_=E.reset(seed=0)
           4 +r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           5 +fs=['joint_'+str(i) for i in range(1,8)]
           6 +def vec(s):return np.array([s.get(r,f) for f in fs])
           7 +x,y,z=[s.get(b,'pose_'+f) for f in 'xyz']
           8 +for k in range(10):
           9 + a=np.zeros(11);a[3:10]=np.clip(ik(x+.12,.25)-vec(s),-.15,.15);a[1]=np.clip(y-.001-s.get(r,'pos_base_y'),-.15,.15);s,*_=E.step(a)
          10 +for zt in np.arange(.23,.080,-.002):
          11 + q=ik(x+.12,zt)
          12 + a=np.zeros(11);a[3:10]=q-vec(s);a[10]=-1
          13 + old=s;s,*_=E.step(a)
          14 + if s.get(r,'grasp_active'):
          15 +  print('GRASP',zt,vec(s),{f:s.get(r,f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']});break
          16 + if np.linalg.norm(vec(s)-vec(old))<1e-7:print('blocked',zt);break
          17 +else:print('no grasp')
          18 +print('last',vec(s),fk(vec(s)))
          19 +E.close()
```

</details>

<a id="C012"></a>
### C012 · Use gradual Cartesian descent for grasp calibration

Commit `26cf3aa962dd72276c0b729321e3324d189d7719`; parents: cf12688095bcbbd57f6a592447a0bb468d28aeaa. Recorded author date: 2026-09-20T02:44:37+02:00.

File roles (automatic): policy.

- [E0035](01_timeline.md#E0035): commit hash in recorded output.
[Controller after this commit](evidence/versions/C012_26cf3aa_approach.py) · [Exact all-file diff](evidence/diffs/C012_26cf3aa.diff)

[Previous saved controller snapshot](evidence/versions/C010_7961dc1_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c2ffcd8..a09d302 100644
--- a/approach.py
+++ b/approach.py
@@ -12,7 +12,7 @@ class GeneratedApproach:
   12     12      def get_action(self,state):
   13     13          self.t+=1;r=self.robot
   14     14          x=state.get(self.block,'pose_x');y=state.get(self.block,'pose_y')
   15        -        z=.25 if self.t<10 else .11
          15 +        z=max(.112,.25-max(0,self.t-10)*.002)
   16     16          q=ik(x-state.get(r,'pos_base_x'),z)
   17     17          a=np.zeros(11,dtype=np.float32)
   18     18          a[1]=y-.001-state.get(r,'pos_base_y')
```

</details>

<a id="C013"></a>
### C013 · Probe local grasp volume and wrist orientation

Commit `23f2a802a960d7c1db8e1ffa92e1d2f456f5b84f`; parents: 26cf3aa962dd72276c0b729321e3324d189d7719. Recorded author date: 2026-09-20T02:45:15+02:00.

File roles (automatic): diagnostic/test.

- [E0041](01_timeline.md#E0041): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C013_23f2a80.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grid.py b/probe_grid.py
new file mode 100644
index 0000000..483d843
--- /dev/null
+++ b/probe_grid.py
@@ -0,0 +1,22 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +E=make_env();s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           4 +fs=['joint_'+str(i) for i in range(1,8)]
           5 +def vec(s):return np.array([s.get(r,f) for f in fs])
           6 +x,y,z=[s.get(b,'pose_'+f) for f in 'xyz']
           7 +n=0
           8 +for angle in [np.pi/2,0]:
           9 + for dx in [0,-.03,.03,-.06,.06]:
          10 +  for zt in np.arange(.25,.09,-.01):
          11 +   for dy in [0,-.02,.02,-.04,.04]:
          12 +    q=ik(x+.12+dx,zt);q[-1]=angle
          13 +    for j in range(20):
          14 +     a=np.zeros(11);a[3:10]=np.clip(q-vec(s),-.1,.1);a[1]=np.clip(y+dy-.001-s.get(r,'pos_base_y'),-.1,.1);a[10]=-1
          15 +     old=s;s,*_=E.step(a);n+=1
          16 +     if s.get(r,'grasp_active'):
          17 +      print('GRASP',dx,dy,zt,angle,'q',vec(s),'base',s.get(r,'pos_base_y'),'tf',[s.get(r,'grasp_tf_'+f) for f in ['x','y','z','qx','qy','qz','qw']],flush=True);E.close();raise SystemExit
          18 +     if np.max(np.abs(a[:10]))<1e-6 or np.linalg.norm(vec(s)-vec(old))<1e-7:break
          19 +   if n>900:
          20 +    s,_=E.reset(seed=0);n=0
          21 +  print('completed',angle,dx,flush=True)
          22 +E.close()
```

</details>

<a id="C014"></a>
### C014 · Record additional gripper state diagnostics

Commit `1103f4154758e86b4c370a9581a31aee8212569b`; parents: 23f2a802a960d7c1db8e1ffa92e1d2f456f5b84f. Recorded author date: 2026-09-20T02:46:31+02:00.

File roles (automatic): diagnostic/test.

- [E0045](01_timeline.md#E0045): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C014_1103f41.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_close.py b/probe_close.py
new file mode 100644
index 0000000..5a71dda
--- /dev/null
+++ b/probe_close.py
@@ -0,0 +1,8 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +E=make_env();s,_=E.reset(seed=1);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           4 +print('block',[s.get(b,'pose_'+f) for f in 'xyz'])
           5 +for i in range(20):
           6 + a=np.zeros(11);a[10]=1 if i%2==0 else -1;s,rew,te,tr,inf=E.step(a)
           7 + print(i,inf, s.get(r,'finger_state'),s.get(r,'grasp_active'))
           8 +E.close()
```

</details>

<a id="C015"></a>
### C015 · Add broad fresh-instance grasp offset sweep

Commit `8ea5584f5d35ba5860136f38bc08f6fe25d9c761`; parents: 1103f4154758e86b4c370a9581a31aee8212569b. Recorded author date: 2026-09-20T02:47:31+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C015_8ea5584.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_wide.py b/probe_wide.py
new file mode 100644
index 0000000..a73f053
--- /dev/null
+++ b/probe_wide.py
@@ -0,0 +1,21 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +from itertools import product
           4 +fields=['joint_'+str(i) for i in range(1,8)]
           5 +found=False
           6 +for dx,dy in product([0,-.06,.06,-.12,.12],[0,-.06,.06,-.12,.12]):
           7 + E=make_env();s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           8 + x,y,z=[s.get(b,'pose_'+f) for f in 'xyz']
           9 + def vec(s):return np.array([s.get(r,f) for f in fields])
          10 + q=ik(x+.12+dx,.30); by=y+dy-fk(q)[0][1]
          11 + for k in range(12):
          12 +  a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.15,.15);a[1]=np.clip(by-s.get(r,'pos_base_y'),-.15,.15);s,*_=E.step(a)
          13 + for zt in np.arange(.3,.09,-.005):
          14 +  q=ik(x+.12+dx,zt);a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.18,.18);a[10]=-1
          15 +  old=s;s,*_=E.step(a)
          16 +  if s.get(r,'grasp_active'):
          17 +   print('GRASP',dx,dy,zt,vec(s),{f:s.get(r,f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']},flush=True);found=True;break
          18 +  if np.linalg.norm(vec(s)-vec(old))<1e-7 and zt<.29:break
          19 + print('END',dx,dy,round(zt,4),'fk',fk(vec(s))[0].round(4).tolist(),'basey',s.get(r,'pos_base_y'),flush=True)
          20 + E.close()
          21 + if found:break
```

</details>

<a id="C016"></a>
### C016 · Probe systematic tool frame offsets with independent descents

Commit `442c1b3f5e4a3c460ca52a591d1442104a6dc2c5`; parents: 8ea5584f5d35ba5860136f38bc08f6fe25d9c761. Recorded author date: 2026-09-20T02:47:31+02:00.

File roles (automatic): diagnostic/test.

- [E0047](01_timeline.md#E0047): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C016_442c1b3.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_offset.py b/probe_offset.py
new file mode 100644
index 0000000..4cdf833
--- /dev/null
+++ b/probe_offset.py
@@ -0,0 +1,17 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +E=make_env()
           4 +for dx in [-.12,-.09,-.15,.09,.12,0]:
           5 + for dy in [0,-.06,.06,-.12,.12]:
           6 +  s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           7 +  fs=['joint_'+str(i) for i in range(1,8)]
           8 +  def vec(s):return np.array([s.get(r,f) for f in fs])
           9 +  x,y,z=[s.get(b,'pose_'+f) for f in 'xyz']
          10 +  for zt in [.32]*15+list(np.arange(.32,.065,-.005)):
          11 +   q=ik(x+.12+dx,zt)
          12 +   a=np.zeros(11);a[3:10]=np.clip(q-vec(s),-.12,.12);a[1]=np.clip(y+dy-.001-s.get(r,'pos_base_y'),-.12,.12);a[10]=-1
          13 +   s,*_=E.step(a)
          14 +   if s.get(r,'grasp_active'):
          15 +    print('GRASP',dx,dy,zt,'q',vec(s),'base',s.get(r,'pos_base_y'),'tf',[s.get(r,'grasp_tf_'+f) for f in ['x','y','z','qx','qy','qz','qw']],flush=True);E.close();raise SystemExit
          16 +  print('no',dx,dy,'last',np.round(fk(vec(s))[0],3),flush=True)
          17 +E.close()
```

</details>

<a id="C017"></a>
### C017 · Calibrate true tool transform from successful grasp and test release settling

Commit `6aa1a3c426cbbba3f2c383dd496e5c8349ee40cc`; parents: 442c1b3f5e4a3c460ca52a591d1442104a6dc2c5. Recorded author date: 2026-09-20T02:48:36+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C017_6aa1a3c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp_calibrate.py b/probe_grasp_calibrate.py
new file mode 100644
index 0000000..0b1c241
--- /dev/null
+++ b/probe_grasp_calibrate.py
@@ -0,0 +1,20 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +from scipy.spatial.transform import Rotation as R
           4 +E=make_env();s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           5 +fs=['joint_'+str(i) for i in range(1,8)]
           6 +def vec(s):return np.array([s.get(r,f) for f in fs])
           7 +def pose(s,o):return np.array([s.get(o,'pose_'+f) for f in ['x','y','z']]),R.from_quat([s.get(o,'pose_'+f) for f in ['qx','qy','qz','qw']]).as_matrix()
           8 +x,y,z=pose(s,b)[0]
           9 +for zt in [.32]*15+list(np.arange(.32,.14,-.005)):
          10 + q=ik(x,zt);a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.12,.12);a[1]=np.clip(y-.001-s.get(r,'pos_base_y'),-.12,.12);a[10]=-1;s,*_=E.step(a)
          11 + if s.get(r,'grasp_active'):break
          12 +print('grabbed',s.get(r,'grasp_active'),flush=True)
          13 +def report(s):
          14 + p,rr=pose(s,b);tf=np.array([s.get(r,'grasp_tf_'+f) for f in ['x','y','z']]);rt=R.from_quat([s.get(r,'grasp_tf_'+f) for f in ['qx','qy','qz','qw']]).as_matrix();eeR=rr@rt.T;ee=p-eeR@tf; pred,pr=fk(vec(s));pred+=np.array([s.get(r,'pos_base_x'),s.get(r,'pos_base_y'),0]);print('CAL',vec(s).round(6).tolist(),'actual',ee.round(8).tolist(),'delta',(ee-pred).round(8).tolist(),'localdelta',(pr.T@(ee-pred-np.array([.12,0,0]))).round(8).tolist(),'rerr',(eeR-pr).round(4).tolist(),flush=True)
          15 +report(s)
          16 +for j,d in [(4,-.1),(4,-.1),(8,.15),(3,.1),(6,.1)]:
          17 + a=np.zeros(11,dtype=np.float32);a[j]=d;s,*_=E.step(a);report(s)
          18 +a=np.zeros(11,dtype=np.float32);a[10]=1;before=pose(s,b)[0];s,reward,done,tr,info=E.step(a);print('RELEASE',before,pose(s,b)[0],s.get(r,'grasp_active'),done,flush=True)
          19 +a[:]=0;s,*_=E.step(a);print('AFTERWAIT',pose(s,b)[0],flush=True)
          20 +E.close()
diff --git a/probe_wide.out b/probe_wide.out
new file mode 100644
index 0000000..f36c3ca
--- /dev/null
+++ b/probe_wide.out
@@ -0,0 +1,10 @@
           1 +END 0 0 0.11 fk [0.456, 0.001, 0.115] basey 0.1722814291715622
           2 +END 0 -0.06 0.11 fk [0.456, 0.001, 0.115] basey 0.112281434237957
           3 +END 0 0.06 0.11 fk [0.456, 0.001, 0.115] basey 0.23228143155574799
           4 +END 0 -0.12 0.11 fk [0.456, 0.001, 0.115] basey 0.05228143185377121
           5 +END 0 0.12 0.11 fk [0.456, 0.001, 0.115] basey 0.29228144884109497
           6 +END -0.06 0 0.11 fk [0.396, 0.001, 0.115] basey 0.1722814291715622
           7 +END -0.06 -0.06 0.11 fk [0.396, 0.001, 0.115] basey 0.112281434237957
           8 +END -0.06 0.06 0.11 fk [0.396, 0.001, 0.115] basey 0.23228143155574799
           9 +END -0.06 -0.12 0.11 fk [0.396, 0.001, 0.115] basey 0.05228143185377121
          10 +END -0.06 0.12 0.11 fk [0.396, 0.001, 0.115] basey 0.29228144884109497
```

</details>

<a id="C018"></a>
### C018 · Implement calibrated grasp lift transport and release policy

Commit `4ea248875fc91de4b78af9b9b3faacbab00abc2b`; parents: 6aa1a3c426cbbba3f2c383dd496e5c8349ee40cc. Recorded author date: 2026-09-20T02:48:39+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0058](01_timeline.md#E0058): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_4ea2488_approach.py) · [Exact all-file diff](evidence/diffs/C018_4ea2488.diff)

[Previous saved controller snapshot](evidence/versions/C012_26cf3aa_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a09d302..c49860e 100644
--- a/approach.py
+++ b/approach.py
@@ -1,21 +1,38 @@
    1      1  import numpy as np
    2        -from kin import ik, Q0
           2 +from kin import ik
    3      3  
    4      4  class GeneratedApproach:
    5      5      def __init__(self, action_space, observation_space, primitives):
    6      6          self.action_space=action_space
    7      7          self.observation_space=observation_space
    8      8      def reset(self,state,info):
    9        -        self.t=0
   10      9          self.robot=state.get_objects(self.observation_space.get_type('Kinematic3DRobot'))[0]
   11     10          self.block=state.get_object_from_name('target_block')
          11 +        self.region=state.get_object_from_name('target_region')
          12 +        self.phase='above';self.t=0;self.stall=0
          13 +    def pos(self,state,obj):
          14 +        return np.array([state.get(obj,'pose_'+f) for f in 'xyz'])
   12     15      def get_action(self,state):
   13        -        self.t+=1;r=self.robot
   14        -        x=state.get(self.block,'pose_x');y=state.get(self.block,'pose_y')
   15        -        z=max(.112,.25-max(0,self.t-10)*.002)
   16        -        q=ik(x-state.get(r,'pos_base_x'),z)
   17        -        a=np.zeros(11,dtype=np.float32)
   18        -        a[1]=y-.001-state.get(r,'pos_base_y')
   19        -        a[3:10]=q-np.array([state.get(r,'joint_'+str(i)) for i in range(1,8)])
   20        -        a[10]=-1 if self.t>=10 else 0
          16 +        self.t+=1;r=self.robot;b=self.block
          17 +        bp=self.pos(state,b);rp=self.pos(state,self.region)
          18 +        qnow=np.array([state.get(r,'joint_'+str(i)) for i in range(1,8)])
          19 +        held=state.get(r,'grasp_active')>0
          20 +        if held and self.phase in ['above','grasp']: self.phase='lift'
          21 +        if self.phase=='above':dest=bp+[0,0,.18];grip=0
          22 +        elif self.phase=='grasp':dest=bp+[0,0,.052];grip=-1
          23 +        elif self.phase=='lift':dest=np.array([bp[0],bp[1],.30]);grip=0
          24 +        elif self.phase=='carry':dest=np.array([rp[0],rp[1],.30]);grip=0
          25 +        elif self.phase=='lower':dest=np.array([rp[0],rp[1],rp[2]+state.get(self.region,'half_extent_z')+state.get(b,'half_extent_z')+.002]);grip=0
          26 +        else:dest=bp;grip=1
          27 +        if held:
          28 +            from kin import fk
          29 +            model,_=fk(qnow)
          30 +            model+=np.array([state.get(r,'pos_base_x')+.12,state.get(r,'pos_base_y'),0])
          31 +            dest=dest+model-bp
          32 +        q=ik(dest[0]-state.get(r,'pos_base_x')-.12,dest[2])
          33 +        by=dest[1]-.001
          34 +        err=max(np.max(np.abs(q-qnow)),abs(by-state.get(r,'pos_base_y')))
          35 +        if err<.002:
          36 +            self.phase={'above':'grasp','grasp':'grasp','lift':'carry','carry':'lower','lower':'release','release':'release'}[self.phase]
          37 +        a=np.zeros(11,dtype=np.float32);a[1]=by-state.get(r,'pos_base_y');a[3:10]=q-qnow;a[10]=grip
   21     38          return np.clip(a,self.action_space.low,self.action_space.high)
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..89889d9
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import time,sys
           4 +for seed in map(int,sys.argv[1:] or ['0','1','2']):
           5 + E=make_env();s,info=E.reset(seed=seed);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info);start=time.monotonic();last=None
           6 + for t in range(E.max_steps):
           7 +  a=p.get_action(s);s,r,term,trunc,inf=E.step(a)
           8 +  if p.phase!=last:
           9 +   print(seed,t,p.phase,'block',p.pos(s,p.block).round(3),'held',s.get(p.robot,'grasp_active'),flush=True);last=p.phase
          10 +  if term or trunc:break
          11 + print('RESULT',seed,info,t+1,term,round(time.monotonic()-start,2),'phase',p.phase,flush=True);E.close()
```

</details>

<a id="C019"></a>
### C019 · Bound diagnostic episodes to expose stalled phases quickly

Commit `f89f9f5e0b7f3b20c1ce9d32d709d14f79d31ee9`; parents: 4ea248875fc91de4b78af9b9b3faacbab00abc2b. Recorded author date: 2026-09-20T02:49:13+02:00.

File roles (automatic): diagnostic/test.

- [E0055](01_timeline.md#E0055): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C019_f89f9f5.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
index 89889d9..8744991 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -3,7 +3,7 @@ from approach import GeneratedApproach
    3      3  import time,sys
    4      4  for seed in map(int,sys.argv[1:] or ['0','1','2']):
    5      5   E=make_env();s,info=E.reset(seed=seed);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info);start=time.monotonic();last=None
    6        - for t in range(E.max_steps):
           6 + for t in range(min(E.max_steps,150)):
    7      7    a=p.get_action(s);s,r,term,trunc,inf=E.step(a)
    8      8    if p.phase!=last:
    9      9     print(seed,t,p.phase,'block',p.pos(s,p.block).round(3),'held',s.get(p.robot,'grasp_active'),flush=True);last=p.phase
```

</details>

<a id="C020"></a>
### C020 · Measure release support tolerance above tabletop

Commit `ff239673d28e35037bce1ff2e248d2a7b3f59395`; parents: f89f9f5e0b7f3b20c1ce9d32d709d14f79d31ee9. Recorded author date: 2026-09-20T02:49:25+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C020_ff23967.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_release.py b/probe_release.py
new file mode 100644
index 0000000..395d16c
--- /dev/null
+++ b/probe_release.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +E=make_env()
           4 +for lift in [0,.001,.003,.005,.01,.02]:
           5 + s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block');fs=['joint_'+str(i) for i in range(1,8)]
           6 + def vec(s):return np.array([s.get(r,f) for f in fs])
           7 + x,y,z=[s.get(b,'pose_'+f) for f in 'xyz']
           8 + for zt in [.32]*15+list(np.arange(.32,.14,-.005)):
           9 +  q=ik(x,zt);a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.12,.12);a[1]=np.clip(y-.001-s.get(r,'pos_base_y'),-.12,.12);a[10]=-1;s,*_=E.step(a)
          10 +  if s.get(r,'grasp_active'):break
          11 + q=ik(x,zt+lift);a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.12,.12);s,*_=E.step(a)
          12 + before=s.get(b,'pose_z');a[:]=0;a[10]=1;s,*_=E.step(a)
          13 + print('RELEASE',lift,'beforez',before,'afterz',s.get(b,'pose_z'),'held',s.get(r,'grasp_active'),'finger',s.get(r,'finger_state'),flush=True)
          14 +E.close()
```

</details>

<a id="C021"></a>
### C021 · Measure horizontal and vertical grasp tolerances

Commit `aeeb2898f042deddcab790a71b3b4b74cc420557`; parents: ff239673d28e35037bce1ff2e248d2a7b3f59395. Recorded author date: 2026-09-20T02:50:09+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C021_aeeb289.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp_tolerance.py b/probe_grasp_tolerance.py
new file mode 100644
index 0000000..86ae624
--- /dev/null
+++ b/probe_grasp_tolerance.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +E=make_env()
           4 +for dx,dy,zz in [(v,0,.155) for v in [0,.005,.01,.02,.03,-.01,-.02]]+[(0,v,.155) for v in [.005,.01,.02,.03,-.01,-.02]]+[(0,0,v) for v in [.17,.165,.16,.15,.14,.13,.12]]:
           5 + s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block');fs=['joint_'+str(i) for i in range(1,8)]
           6 + def vec(s):return np.array([s.get(r,f) for f in fs])
           7 + x,y,z=[s.get(b,'pose_'+f) for f in 'xyz']
           8 + for zt in [.3]*15+list(np.arange(.3,zz,-.005))+[zz]:
           9 +  q=ik(x+dx,zt);a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.12,.12);a[1]=np.clip(y+dy-.001-s.get(r,'pos_base_y'),-.12,.12);s,*_=E.step(a)
          10 + a[:]=0;a[10]=-1;s,*_=E.step(a)
          11 + print('GRASPTEST',dx,dy,zz,s.get(r,'grasp_active'),'fkz',fk(vec(s))[0][2],flush=True)
          12 +E.close()
diff --git a/probe_release.out b/probe_release.out
new file mode 100644
index 0000000..c0c9695
--- /dev/null
+++ b/probe_release.out
@@ -0,0 +1,6 @@
           1 +RELEASE 0 beforez 0.10000000149011612 afterz 0.10000000149011612 held 0.0 finger 0.0
           2 +RELEASE 0.001 beforez 0.10099997371435165 afterz 0.10099997371435165 held 0.0 finger 0.0
           3 +RELEASE 0.003 beforez 0.1029999777674675 afterz 0.1029999777674675 held 0.0 finger 0.0
           4 +RELEASE 0.005 beforez 0.10499998182058334 afterz 0.10499998182058334 held 0.0 finger 0.0
           5 +RELEASE 0.01 beforez 0.10999997705221176 afterz 0.10999997705221176 held 1.0 finger 0.4099999964237213
           6 +RELEASE 0.02 beforez 0.1199999675154686 afterz 0.1199999675154686 held 1.0 finger 0.4099999964237213
```

</details>

<a id="C022"></a>
### C022 · Test constant arm reach with mobile base alignment

Commit `60027abfe5bb3c770cbef28bf7f017645d028ef5`; parents: aeeb2898f042deddcab790a71b3b4b74cc420557. Recorded author date: 2026-09-20T02:50:19+02:00.

File roles (automatic): diagnostic/test.

- [E0062](01_timeline.md#E0062): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C022_60027ab.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp_tolerance.out b/probe_grasp_tolerance.out
new file mode 100644
index 0000000..d8433c6
--- /dev/null
+++ b/probe_grasp_tolerance.out
@@ -0,0 +1,4 @@
           1 +GRASPTEST 0 0 0.155 1.0 fkz 0.15500002318710682
           2 +GRASPTEST 0.005 0 0.155 1.0 fkz 0.1549999797340317
           3 +GRASPTEST 0.01 0 0.155 1.0 fkz 0.15500001015446985
           4 +GRASPTEST 0.02 0 0.155 1.0 fkz 0.155000005855784
diff --git a/probe_reach.py b/probe_reach.py
new file mode 100644
index 0000000..08b1a63
--- /dev/null
+++ b/probe_reach.py
@@ -0,0 +1,10 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +E=make_env()
           4 +for reach in [.4,.45,.5,.55]:
           5 + s,_=E.reset(seed=1);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block');x,y,z=[s.get(b,'pose_'+f) for f in 'xyz'];fs=['joint_'+str(i) for i in range(1,8)]
           6 + for zt in [.28]*15+list(np.arange(.28,.14,-.005)):
           7 +  q=ik(reach,zt);a=np.zeros(11);a[3:10]=np.clip(q-[s.get(r,f) for f in fs],-.1,.1);a[0]=np.clip(x-.12-reach-s.get(r,'pos_base_x'),-.1,.1);a[1]=np.clip(y-.001-s.get(r,'pos_base_y'),-.1,.1);a[10]=-1;s,*_=E.step(a)
           8 +  if s.get(r,'grasp_active'):print('GRASP',reach,zt,flush=True);break
           9 + else:print('FAIL',reach,'q',[s.get(r,f) for f in fs],flush=True)
          10 +E.close()
```

</details>

<a id="C023"></a>
### C023 · Probe obstruction placement support on blocks, table and ground

Commit `cf6dd709c515d0ade31adf98567b6a4e49d44f38`; parents: 60027abfe5bb3c770cbef28bf7f017645d028ef5. Recorded author date: 2026-09-20T02:50:55+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C023_cf6dd70.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dispose.py b/probe_dispose.py
new file mode 100644
index 0000000..a238396
--- /dev/null
+++ b/probe_dispose.py
@@ -0,0 +1,28 @@
           1 +from env_client import make_env
           2 +from kin import *
           3 +E=make_env()
           4 +for dest in ['blocktop','table','offtable075','offtablezero']:
           5 + s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('obstruction0');fs=['joint_'+str(i) for i in range(1,8)]
           6 + def vec(s):return np.array([s.get(r,f) for f in fs])
           7 + def goto(x,y,z,close=False):
           8 +  global s
           9 +  q=ik(.42,z);bx=x-.12-.42;by=y-.001
          10 +  for k in range(16):
          11 +   a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.12,.12);a[0]=np.clip(bx-s.get(r,'pos_base_x'),-.12,.12);a[1]=np.clip(by-s.get(r,'pos_base_y'),-.12,.12);a[10]=-1 if close else 0;s,*_=E.step(a)
          12 + x,y,z=[s.get(b,'pose_'+f) for f in 'xyz'];h=s.get(b,'half_extent_z');goto(x,y,.3)
          13 + for zt in np.arange(.3,.1,-.005):
          14 +  goto(x,y,zt,True)
          15 +  if s.get(r,'grasp_active'):break
          16 + print('GRASP',dest,s.get(r,'grasp_active'),zt,flush=True)
          17 + if not s.get(r,'grasp_active'):continue
          18 + offset=fk(vec(s))[0][2]-s.get(b,'pose_z');goto(x,y,.3)
          19 + if dest=='blocktop':
          20 +  bb=s.get_object_from_name('target_block');dx,dy=[s.get(bb,'pose_'+f) for f in 'xy'];dz=s.get(bb,'pose_z')+s.get(bb,'half_extent_z')+h+.001
          21 + elif dest=='table':dx,dy,dz=.4,-.25,.075+h+.001
          22 + else:dx,dy,dz=.4,-.6,(.075 if dest.endswith('075') else 0)+h+.001
          23 + goto(dx,dy,.3)
          24 + for zt in np.arange(.3,dz+offset,-.01):goto(dx,dy,zt)
          25 + goto(dx,dy,dz+offset)
          26 + before=[s.get(b,'pose_'+f) for f in 'xyz'];a=np.zeros(11,dtype=np.float32);a[10]=1;s,*_=E.step(a)
          27 + print('DROP',dest,'desired',dx,dy,dz,'actual',before,'held',s.get(r,'grasp_active'),flush=True)
          28 +E.close()
```

</details>

<a id="C024"></a>
### C024 · Make disposal probe stop after reaching each waypoint

Commit `cbc033bbcfd662df4bcc70ebd35c2e82c89fc186`; parents: cf6dd709c515d0ade31adf98567b6a4e49d44f38. Recorded author date: 2026-09-20T02:51:08+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C024_cbc033b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dispose.out b/probe_dispose.out
new file mode 100644
index 0000000..14bf409
--- /dev/null
+++ b/probe_dispose.out
@@ -0,0 +1,3 @@
           1 +GRASP blocktop 0.0 0.10499999999999982
           2 +GRASP table 0.0 0.10499999999999982
           3 +GRASP offtable075 0.0 0.10499999999999982
```

</details>

<a id="C025"></a>
### C025 · Bound each disposal motion by waypoint convergence

Commit `d72af45ac6f7ec04c52d53868e2328c9dc0a588c`; parents: cbc033bbcfd662df4bcc70ebd35c2e82c89fc186. Recorded author date: 2026-09-20T02:51:19+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C025_d72af45.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dispose.py b/probe_dispose.py
index a238396..cf5fb56 100644
--- a/probe_dispose.py
+++ b/probe_dispose.py
@@ -9,6 +9,7 @@ for dest in ['blocktop','table','offtable075','offtablezero']:
    9      9    q=ik(.42,z);bx=x-.12-.42;by=y-.001
   10     10    for k in range(16):
   11     11     a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.12,.12);a[0]=np.clip(bx-s.get(r,'pos_base_x'),-.12,.12);a[1]=np.clip(by-s.get(r,'pos_base_y'),-.12,.12);a[10]=-1 if close else 0;s,*_=E.step(a)
          12 +   if np.max(np.abs(q-vec(s)))<1e-5 and abs(bx-s.get(r,'pos_base_x'))<1e-5 and abs(by-s.get(r,'pos_base_y'))<1e-5:break
   12     13   x,y,z=[s.get(b,'pose_'+f) for f in 'xyz'];h=s.get(b,'half_extent_z');goto(x,y,.3)
   13     14   for zt in np.arange(.3,.1,-.005):
   14     15    goto(x,y,zt,True)
```

</details>

<a id="C026"></a>
### C026 · Clear obstructing blocks and transport with constant reach and vertical wrist

Commit `b2f17e6750c46954a44a2d4f53cd96c1b8a24139`; parents: d72af45ac6f7ec04c52d53868e2328c9dc0a588c. Recorded author date: 2026-09-20T02:51:27+02:00.

File roles (automatic): policy.

- [E0068](01_timeline.md#E0068): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C026_b2f17e6_approach.py) · [Exact all-file diff](evidence/diffs/C026_b2f17e6.diff)

[Previous saved controller snapshot](evidence/versions/C018_4ea2488_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c49860e..d239065 100644
--- a/approach.py
+++ b/approach.py
@@ -1,38 +1,84 @@
    1      1  import numpy as np
    2        -from kin import ik
           2 +from kin import ik, fk
    3      3  
    4      4  class GeneratedApproach:
    5      5      def __init__(self, action_space, observation_space, primitives):
    6      6          self.action_space=action_space
    7      7          self.observation_space=observation_space
           8 +        self.cache={}
           9 +    def pos(self,state,obj):
          10 +        return np.array([state.get(obj,'pose_'+f) for f in 'xyz'])
          11 +    def size(self,state,obj):
          12 +        return np.array([state.get(obj,'half_extent_'+f) for f in 'xyz'])
    8     13      def reset(self,state,info):
    9     14          self.robot=state.get_objects(self.observation_space.get_type('Kinematic3DRobot'))[0]
   10     15          self.block=state.get_object_from_name('target_block')
   11     16          self.region=state.get_object_from_name('target_region')
   12        -        self.phase='above';self.t=0;self.stall=0
   13        -    def pos(self,state,obj):
   14        -        return np.array([state.get(obj,'pose_'+f) for f in 'xyz'])
          17 +        self.objects=state.get_objects(self.observation_space.get_type('Kinematic3DCuboid'))
          18 +        rp=self.pos(state,self.region);rs=self.size(state,self.region)
          19 +        obs=[o for o in self.objects if o not in [self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-rp[:2]) < self.size(state,o)[:2]+rs[:2]+.012)]
          20 +        obs.sort(key=lambda o:-self.pos(state,o)[2])
          21 +        self.todo=obs+[self.block];self.index=0;self.phase='above';self.t=0;self.stall=0;self.last=None
          22 +        self.obj=self.todo[0];self.destination=self.choose_destination(state)
          23 +    def choose_destination(self,state):
          24 +        if self.obj==self.block:
          25 +            p=self.pos(state,self.region).copy();p[2]+=self.size(state,self.region)[2]+self.size(state,self.obj)[2]+.001
          26 +            return p
          27 +        h=self.size(state,self.obj)
          28 +        candidates=[]
          29 +        for x in [.135,.2,.265,.33,.395,.465]:
          30 +            for y in [-.36,.36,-.29,.29,-.22,.22,-.15,.15,0]:
          31 +                p=np.array([x,y,.075+h[2]+.001]);free=True
          32 +                for other in self.objects:
          33 +                    if other==self.obj:continue
          34 +                    op=self.pos(state,other);oh=self.size(state,other)
          35 +                    if np.all(np.abs(p[:2]-op[:2]) < h[:2]+oh[:2]+.009):free=False;break
          36 +                if free:candidates.append(p)
          37 +        if candidates:
          38 +            start=self.pos(state,self.obj)
          39 +            return min(candidates,key=lambda p:np.linalg.norm(p[:2]-start[:2]))
          40 +        return np.array([.135,-.36,.076+h[2]])
   15     41      def get_action(self,state):
   16        -        self.t+=1;r=self.robot;b=self.block
   17        -        bp=self.pos(state,b);rp=self.pos(state,self.region)
          42 +        self.t+=1;r=self.robot
   18     43          qnow=np.array([state.get(r,'joint_'+str(i)) for i in range(1,8)])
          44 +        base=np.array([state.get(r,'pos_base_x'),state.get(r,'pos_base_y')])
          45 +        model,_=fk(qnow);model+=np.r_[base+[.12,0],0]
   19     46          held=state.get(r,'grasp_active')>0
   20        -        if held and self.phase in ['above','grasp']: self.phase='lift'
   21        -        if self.phase=='above':dest=bp+[0,0,.18];grip=0
   22        -        elif self.phase=='grasp':dest=bp+[0,0,.052];grip=-1
   23        -        elif self.phase=='lift':dest=np.array([bp[0],bp[1],.30]);grip=0
   24        -        elif self.phase=='carry':dest=np.array([rp[0],rp[1],.30]);grip=0
   25        -        elif self.phase=='lower':dest=np.array([rp[0],rp[1],rp[2]+state.get(self.region,'half_extent_z')+state.get(b,'half_extent_z')+.002]);grip=0
   26        -        else:dest=bp;grip=1
   27        -        if held:
   28        -            from kin import fk
   29        -            model,_=fk(qnow)
   30        -            model+=np.array([state.get(r,'pos_base_x')+.12,state.get(r,'pos_base_y'),0])
   31        -            dest=dest+model-bp
   32        -        q=ik(dest[0]-state.get(r,'pos_base_x')-.12,dest[2])
   33        -        by=dest[1]-.001
   34        -        err=max(np.max(np.abs(q-qnow)),abs(by-state.get(r,'pos_base_y')))
   35        -        if err<.002:
   36        -            self.phase={'above':'grasp','grasp':'grasp','lift':'carry','carry':'lower','lower':'release','release':'release'}[self.phase]
   37        -        a=np.zeros(11,dtype=np.float32);a[1]=by-state.get(r,'pos_base_y');a[3:10]=q-qnow;a[10]=grip
          47 +        bp=self.pos(state,self.obj)
          48 +        signature=np.r_[base,qnow,held]
          49 +        if self.last is not None and np.max(abs(signature-self.last))<1e-6:self.stall+=1
          50 +        else:self.stall=0
          51 +        self.last=signature
          52 +        if held and self.phase in ['above','align','grasp']:
          53 +            grabbed=[o for o in self.objects if state.get(o,'grasp_active')>0]
          54 +            if grabbed and grabbed[0]!=self.obj:
          55 +                self.obj=grabbed[0];self.destination=self.choose_destination(state);bp=self.pos(state,self.obj)
          56 +            self.phase='lift';self.lift_xy=bp[:2].copy()
          57 +        if self.phase=='release' and not held:
          58 +            self.index+=1
          59 +            if self.index>=len(self.todo):self.index=len(self.todo)-1
          60 +            self.obj=self.todo[self.index];self.destination=self.choose_destination(state);self.phase='above';bp=self.pos(state,self.obj)
          61 +        grip=0
          62 +        if self.phase=='above':dest=np.r_[model[:2],.34]
          63 +        elif self.phase=='align':dest=np.r_[bp[:2],.34]
          64 +        elif self.phase=='grasp':dest=bp+[0,0,.055];grip=-1
          65 +        elif self.phase=='lift':dest=np.r_[self.lift_xy,.30]
          66 +        elif self.phase=='carry':dest=np.r_[self.destination[:2],.30]
          67 +        elif self.phase=='lower':dest=self.destination.copy()
          68 +        else:dest=bp.copy();grip=1
          69 +        if held:dest=dest+model-bp
          70 +        if self.phase=='above':dest[2]=.34
          71 +        # Preserve a vertical wrist throughout travel and use the mobile base for XY.
          72 +        dz=np.clip(dest[2]-model[2],-.025,.025)
          73 +        z=model[2]+dz
          74 +        key=round(float(z),7)
          75 +        if key not in self.cache:self.cache[key]=ik(.50,z)
          76 +        q=self.cache[key]
          77 +        targetbase=dest[:2]-[.62,.001]
          78 +        delta=np.r_[targetbase-base,q-qnow]
          79 +        scale=max(1.,np.max(np.abs(delta))/.18)
          80 +        a=np.zeros(11,dtype=np.float32);a[:2]=delta[:2]/scale;a[3:10]=delta[2:]/scale;a[10]=grip
          81 +        error=np.max(np.abs(dest-model))
          82 +        if error<.0015 and np.max(abs(q-qnow))<.006:
          83 +            self.phase={'above':'align','align':'grasp','grasp':'grasp','lift':'carry','carry':'lower','lower':'release','release':'release'}[self.phase]
   38     84          return np.clip(a,self.action_space.low,self.action_space.high)
```

</details>

<a id="C027"></a>
### C027 · Rotate obstruction grasp to avoid neighboring obstruction

Commit `b42bb93b3f0d5cf04b08679b0e65ed49cf0d7e5f`; parents: b2f17e6750c46954a44a2d4f53cd96c1b8a24139. Recorded author date: 2026-09-20T02:51:42+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C027_b42bb93.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dispose.out b/probe_dispose.out
index 14bf409..b585229 100644
--- a/probe_dispose.out
+++ b/probe_dispose.out
@@ -1,3 +1,4 @@
    1      1  GRASP blocktop 0.0 0.10499999999999982
    2      2  GRASP table 0.0 0.10499999999999982
    3      3  GRASP offtable075 0.0 0.10499999999999982
           4 +GRASP offtablezero 0.0 0.10499999999999982
diff --git a/probe_dispose.py b/probe_dispose.py
index cf5fb56..bb44a0d 100644
--- a/probe_dispose.py
+++ b/probe_dispose.py
@@ -6,7 +6,7 @@ for dest in ['blocktop','table','offtable075','offtablezero']:
    6      6   def vec(s):return np.array([s.get(r,f) for f in fs])
    7      7   def goto(x,y,z,close=False):
    8      8    global s
    9        -  q=ik(.42,z);bx=x-.12-.42;by=y-.001
           9 +  q=ik(.42,z);q[-1]=0;bx=x-.12-.42;by=y-.001
   10     10    for k in range(16):
   11     11     a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.12,.12);a[0]=np.clip(bx-s.get(r,'pos_base_x'),-.12,.12);a[1]=np.clip(by-s.get(r,'pos_base_y'),-.12,.12);a[10]=-1 if close else 0;s,*_=E.step(a)
   12     12     if np.max(np.abs(q-vec(s)))<1e-5 and abs(bx-s.get(r,'pos_base_x'))<1e-5 and abs(by-s.get(r,'pos_base_y'))<1e-5:break
@@ -14,7 +14,7 @@ for dest in ['blocktop','table','offtable075','offtablezero']:
   14     14   for zt in np.arange(.3,.1,-.005):
   15     15    goto(x,y,zt,True)
   16     16    if s.get(r,'grasp_active'):break
   17        - print('GRASP',dest,s.get(r,'grasp_active'),zt,flush=True)
          17 + print('GRASP',dest,s.get(r,'grasp_active'),zt,vec(s).round(3),fk(vec(s))[0].round(3),s.get(r,'pos_base_x'),s.get(r,'pos_base_y'),flush=True)
   18     18   if not s.get(r,'grasp_active'):continue
   19     19   offset=fk(vec(s))[0][2]-s.get(b,'pose_z');goto(x,y,.3)
   20     20   if dest=='blocktop':
```

</details>

<a id="C028"></a>
### C028 · Add object-level diagnostics for clearance failures

Commit `2ca60a6ff949247bfa30a5a68f0800aa0fb75dbe`; parents: b42bb93b3f0d5cf04b08679b0e65ed49cf0d7e5f. Recorded author date: 2026-09-20T02:51:57+02:00.

File roles (automatic): diagnostic/test.

- [E0067](01_timeline.md#E0067): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C028_2ca60a6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/debug_policy.py b/debug_policy.py
new file mode 100644
index 0000000..7e2f161
--- /dev/null
+++ b/debug_policy.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +from kin import fk
           4 +import sys,numpy as np
           5 +seed=int(sys.argv[1]) if len(sys.argv)>1 else 0
           6 +E=make_env();s,i=E.reset(seed=seed);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,i)
           7 +for t in range(180):
           8 + a=p.get_action(s);s,rew,te,tr,inf=E.step(a)
           9 + if t%10==0 or te:
          10 +  r=p.robot;q=np.array([s.get(r,'joint_'+str(k)) for k in range(1,8)]);m,_=fk(q);m+=np.array([s.get(r,'pos_base_x')+.12,s.get(r,'pos_base_y'),0])
          11 +  print(t,p.phase,p.obj,'pos',p.pos(s,p.obj).round(4),'model',m.round(4),'a',a.round(4),'stall',p.stall,flush=True)
          12 + if te:print('SUCCESS');break
          13 +E.close()
diff --git a/probe_dispose.out b/probe_dispose.out
index b585229..52e39ea 100644
--- a/probe_dispose.out
+++ b/probe_dispose.out
@@ -1,4 +1,4 @@
    1        -GRASP blocktop 0.0 0.10499999999999982
    2        -GRASP table 0.0 0.10499999999999982
    3        -GRASP offtable075 0.0 0.10499999999999982
    4        -GRASP offtablezero 0.0 0.10499999999999982
           1 +GRASP blocktop 1.0 0.14499999999999985 [ 0.     0.494 -3.142 -1.871  0.    -0.777  0.   ] [0.42  0.001 0.145] -0.4365674555301666 0.2470032125711441
           2 +DROP blocktop desired 0.33598166704177856 0.17328143119812012 0.1360547717884183 actual [0.33598169684410095, 0.17328104376792908, 0.13605476915836334] held 1.0
           3 +GRASP table 1.0 0.14499999999999985 [ 0.     0.494 -3.142 -1.871  0.    -0.777  0.   ] [0.42  0.001 0.145] -0.4365674555301666 0.2470032125711441
           4 +DROP table desired 0.4 -0.25 0.08605476992577314 actual [0.40000003576278687, -0.24999986588954926, 0.08605478703975677] held 0.0
```

</details>

<a id="C029"></a>
### C029 · Descend finely to grasp short obstructions before contact

Commit `5104aa53517f30c5c49f0ae6366a044efb16f2d6`; parents: 2ca60a6ff949247bfa30a5a68f0800aa0fb75dbe. Recorded author date: 2026-09-20T02:52:35+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0087](01_timeline.md#E0087): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C029_5104aa5_approach.py) · [Exact all-file diff](evidence/diffs/C029_5104aa5.diff)

[Previous saved controller snapshot](evidence/versions/C026_b2f17e6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d239065..cb04053 100644
--- a/approach.py
+++ b/approach.py
@@ -61,7 +61,7 @@ class GeneratedApproach:
   61     61          grip=0
   62     62          if self.phase=='above':dest=np.r_[model[:2],.34]
   63     63          elif self.phase=='align':dest=np.r_[bp[:2],.34]
   64        -        elif self.phase=='grasp':dest=bp+[0,0,.055];grip=-1
          64 +        elif self.phase=='grasp':dest=bp+[0,0,.025];grip=-1
   65     65          elif self.phase=='lift':dest=np.r_[self.lift_xy,.30]
   66     66          elif self.phase=='carry':dest=np.r_[self.destination[:2],.30]
   67     67          elif self.phase=='lower':dest=self.destination.copy()
@@ -69,7 +69,7 @@ class GeneratedApproach:
   69     69          if held:dest=dest+model-bp
   70     70          if self.phase=='above':dest[2]=.34
   71     71          # Preserve a vertical wrist throughout travel and use the mobile base for XY.
   72        -        dz=np.clip(dest[2]-model[2],-.025,.025)
          72 +        dz=np.clip(dest[2]-model[2],-.008 if self.phase=='grasp' and model[2]-bp[2]<.09 else -.025,.025)
   73     73          z=model[2]+dz
   74     74          key=round(float(z),7)
   75     75          if key not in self.cache:self.cache[key]=ik(.50,z)
diff --git a/probe_dispose.out b/probe_dispose.out
index 52e39ea..84d6522 100644
--- a/probe_dispose.out
+++ b/probe_dispose.out
@@ -2,3 +2,7 @@ GRASP blocktop 1.0 0.14499999999999985 [ 0.     0.494 -3.142 -1.871  0.    -0.77
    2      2  DROP blocktop desired 0.33598166704177856 0.17328143119812012 0.1360547717884183 actual [0.33598169684410095, 0.17328104376792908, 0.13605476915836334] held 1.0
    3      3  GRASP table 1.0 0.14499999999999985 [ 0.     0.494 -3.142 -1.871  0.    -0.777  0.   ] [0.42  0.001 0.145] -0.4365674555301666 0.2470032125711441
    4      4  DROP table desired 0.4 -0.25 0.08605476992577314 actual [0.40000003576278687, -0.24999986588954926, 0.08605478703975677] held 0.0
           5 +GRASP offtable075 1.0 0.14499999999999985 [ 0.     0.494 -3.142 -1.871  0.    -0.777  0.   ] [0.42  0.001 0.145] -0.4365674555301666 0.2470032125711441
           6 +DROP offtable075 desired 0.4 -0.6 0.08605476992577314 actual [0.4000000059604645, -0.5999999046325684, 0.08605477213859558] held 1.0
           7 +GRASP offtablezero 1.0 0.14499999999999985 [ 0.     0.494 -3.142 -1.871  0.    -0.777  0.   ] [0.42  0.001 0.145] -0.4365674555301666 0.2470032125711441
           8 +DROP offtablezero desired 0.4 -0.6 0.011054769925773145 actual [0.40000003576278687, -0.5999990701675415, 0.011054784059524536] held 1.0
diff --git a/test_approach.py b/test_approach.py
index 8744991..13056a1 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -3,7 +3,7 @@ from approach import GeneratedApproach
    3      3  import time,sys
    4      4  for seed in map(int,sys.argv[1:] or ['0','1','2']):
    5      5   E=make_env();s,info=E.reset(seed=seed);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info);start=time.monotonic();last=None
    6        - for t in range(min(E.max_steps,150)):
           6 + for t in range(min(E.max_steps,350)):
    7      7    a=p.get_action(s);s,r,term,trunc,inf=E.step(a)
    8      8    if p.phase!=last:
    9      9     print(seed,t,p.phase,'block',p.pos(s,p.block).round(3),'held',s.get(p.robot,'grasp_active'),flush=True);last=p.phase
```

</details>

<a id="C030"></a>
### C030 · Add independent seeds20-39 robustness sweep

Commit `71c44847fa0d2e8d6e213d8bbbaa21399ad7d55d`; parents: 5104aa53517f30c5c49f0ae6366a044efb16f2d6. Recorded author date: 2026-09-20T02:53:07+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C030_71c4484.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/debug2.txt b/debug2.txt
new file mode 100644
index 0000000..56a6cb6
--- /dev/null
+++ b/debug2.txt
@@ -0,0 +1,17 @@
           1 +0 above obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.154  0.001  0.2494] a [-0.0584  0.      0.      0.      0.1459  0.      0.18    0.     -0.0546
           2 + -0.      0.    ] stall 0
           3 +10 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.34  ] a [-0.  0.  0.  0. -0. -0. -0.  0. -0.  0.  0.] stall 0
           4 +20 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
           5 + -0.     -1.    ] stall 0
           6 +30 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
           7 + -0.     -1.    ] stall 10
           8 +40 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
           9 + -0.     -1.    ] stall 20
          10 +50 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          11 + -0.     -1.    ] stall 30
          12 +60 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          13 + -0.     -1.    ] stall 40
          14 +70 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          15 + -0.     -1.    ] stall 50
          16 +80 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          17 + -0.     -1.    ] stall 60
diff --git a/test_results.txt b/test_results.txt
new file mode 100644
index 0000000..44c76eb
--- /dev/null
+++ b/test_results.txt
@@ -0,0 +1,43 @@
           1 +0 0 above block [0.336 0.173 0.1  ] held 0.0
           2 +0 8 align block [0.336 0.173 0.1  ] held 0.0
           3 +0 11 grasp block [0.336 0.173 0.1  ] held 0.0
           4 +0 22 lift block [0.336 0.173 0.1  ] held 1.0
           5 +0 30 carry block [0.336 0.173 0.1  ] held 1.0
           6 +0 32 lower block [0.336 0.173 0.1  ] held 1.0
           7 +0 42 release block [0.336 0.173 0.1  ] held 1.0
           8 +0 44 above block [0.336 0.173 0.1  ] held 0.0
           9 +0 52 align block [0.336 0.173 0.1  ] held 0.0
          10 +0 54 grasp block [0.336 0.173 0.1  ] held 0.0
          11 +0 65 lift block [0.336 0.173 0.1  ] held 1.0
          12 +0 74 carry block [0.336 0.173 0.1  ] held 1.0
          13 +0 76 lower block [0.336 0.173 0.1  ] held 1.0
          14 +0 86 release block [0.336 0.173 0.1  ] held 1.0
          15 +0 88 above block [0.336 0.173 0.1  ] held 0.0
          16 +0 97 align block [0.336 0.173 0.1  ] held 0.0
          17 +0 100 grasp block [0.336 0.173 0.1  ] held 0.0
          18 +0 110 lift block [0.336 0.173 0.125] held 1.0
          19 +0 118 carry block [0.336 0.173 0.3  ] held 1.0
          20 +0 121 lower block [0.144 0.233 0.3  ] held 1.0
          21 +0 130 release block [0.144 0.233 0.111] held 1.0
          22 +RESULT 0 {'object_count': 2} 132 True 3.01 phase release
          23 +2 0 above block [ 0.189 -0.335  0.1  ] held 0.0
          24 +2 8 align block [ 0.189 -0.335  0.1  ] held 0.0
          25 +2 10 grasp block [ 0.189 -0.335  0.1  ] held 0.0
          26 +RESULT 2 {'object_count': 2} 350 False 12.36 phase grasp
          27 +5 0 above block [0.464 0.111 0.1  ] held 0.0
          28 +5 8 align block [0.464 0.111 0.1  ] held 0.0
          29 +5 11 grasp block [0.464 0.111 0.1  ] held 0.0
          30 +5 19 lift block [0.464 0.111 0.1  ] held 1.0
          31 +5 27 carry block [0.464 0.111 0.1  ] held 1.0
          32 +5 29 lower block [0.464 0.111 0.1  ] held 1.0
          33 +5 38 release block [0.464 0.111 0.1  ] held 1.0
          34 +5 40 above block [0.464 0.111 0.1  ] held 0.0
          35 +5 47 align block [0.464 0.111 0.1  ] held 0.0
          36 +5 49 grasp block [0.464 0.111 0.1  ] held 0.0
          37 +5 61 lift block [0.464 0.111 0.1  ] held 1.0
          38 +5 69 carry block [0.464 0.111 0.1  ] held 1.0
          39 +5 71 lower block [0.464 0.111 0.1  ] held 1.0
          40 +5 81 release block [0.464 0.111 0.1  ] held 1.0
          41 +5 83 above block [0.464 0.111 0.1  ] held 0.0
          42 +5 91 align block [0.464 0.111 0.1  ] held 0.0
          43 +5 94 grasp block [0.464 0.111 0.1  ] held 0.0
diff --git a/test_sweep_agent.py b/test_sweep_agent.py
new file mode 100644
index 0000000..5686ece
--- /dev/null
+++ b/test_sweep_agent.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import time,json
           4 +import sys
           5 +seeds=list(range(20,40)) if len(sys.argv)<2 else [int(x) for x in sys.argv[1:]]
           6 +for seed in seeds:
           7 + e=make_env();s,i=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i);started=time.monotonic();done=False
           8 + for step in range(300):
           9 +  s,r,done,tr,i=e.step(p.get_action(s))
          10 +  if done or tr or time.monotonic()-started>50:break
          11 + report={'seed':seed,'count':i.get('object_count'),'success':done,'steps':step+1,'sec':round(time.monotonic()-started,2)}
          12 + if not done:
          13 +  report.update(phase=p.phase,obj=p.obj.name,stall=p.stall,base=[s.get(p.robot,f) for f in ['pos_base_x','pos_base_y']],held=s.get(p.robot,'grasp_active'),pos=p.pos(s,p.obj).tolist(),dest=p.destination.tolist())
          14 + print(json.dumps(report),flush=True);e.close()
```

</details>

<a id="C031"></a>
### C031 · Retry blocked grasps from perpendicular wrist orientations

Commit `b4b99fba09f0fc7c0af7537df5b3513144ca14d1`; parents: 71c44847fa0d2e8d6e213d8bbbaa21399ad7d55d. Recorded author date: 2026-09-20T02:53:26+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0089](01_timeline.md#E0089): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C031_b4b99fb_approach.py) · [Exact all-file diff](evidence/diffs/C031_b4b99fb.diff)

[Previous saved controller snapshot](evidence/versions/C029_5104aa5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index cb04053..6b8d102 100644
--- a/approach.py
+++ b/approach.py
@@ -19,7 +19,7 @@ class GeneratedApproach:
   19     19          obs=[o for o in self.objects if o not in [self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-rp[:2]) < self.size(state,o)[:2]+rs[:2]+.012)]
   20     20          obs.sort(key=lambda o:-self.pos(state,o)[2])
   21     21          self.todo=obs+[self.block];self.index=0;self.phase='above';self.t=0;self.stall=0;self.last=None
   22        -        self.obj=self.todo[0];self.destination=self.choose_destination(state)
          22 +        self.attempt=0;self.wrist=np.pi/2;self.obj=self.todo[0];self.destination=self.choose_destination(state)
   23     23      def choose_destination(self,state):
   24     24          if self.obj==self.block:
   25     25              p=self.pos(state,self.region).copy();p[2]+=self.size(state,self.region)[2]+self.size(state,self.obj)[2]+.001
@@ -49,6 +49,8 @@ class GeneratedApproach:
   49     49          if self.last is not None and np.max(abs(signature-self.last))<1e-6:self.stall+=1
   50     50          else:self.stall=0
   51     51          self.last=signature
          52 +        if not held and self.phase=='grasp' and self.stall>=3:
          53 +            self.attempt+=1;self.wrist=[np.pi/2,0,np.pi/4,-np.pi/4][self.attempt%4];self.phase='above';self.stall=0
   52     54          if held and self.phase in ['above','align','grasp']:
   53     55              grabbed=[o for o in self.objects if state.get(o,'grasp_active')>0]
   54     56              if grabbed and grabbed[0]!=self.obj:
@@ -57,7 +59,7 @@ class GeneratedApproach:
   57     59          if self.phase=='release' and not held:
   58     60              self.index+=1
   59     61              if self.index>=len(self.todo):self.index=len(self.todo)-1
   60        -            self.obj=self.todo[self.index];self.destination=self.choose_destination(state);self.phase='above';bp=self.pos(state,self.obj)
          62 +            self.attempt=0;self.wrist=np.pi/2;self.obj=self.todo[self.index];self.destination=self.choose_destination(state);self.phase='above';bp=self.pos(state,self.obj)
   61     63          grip=0
   62     64          if self.phase=='above':dest=np.r_[model[:2],.34]
   63     65          elif self.phase=='align':dest=np.r_[bp[:2],.34]
@@ -73,7 +75,8 @@ class GeneratedApproach:
   73     75          z=model[2]+dz
   74     76          key=round(float(z),7)
   75     77          if key not in self.cache:self.cache[key]=ik(.50,z)
   76        -        q=self.cache[key]
          78 +        q=self.cache[key].copy()
          79 +        q[6]=qnow[6] if self.phase=='above' else self.wrist
   77     80          targetbase=dest[:2]-[.62,.001]
   78     81          delta=np.r_[targetbase-base,q-qnow]
   79     82          scale=max(1.,np.max(np.abs(delta))/.18)
diff --git a/debug2.txt b/debug2.txt
index 56a6cb6..694f79a 100644
--- a/debug2.txt
+++ b/debug2.txt
@@ -15,3 +15,11 @@
   15     15   -0.     -1.    ] stall 50
   16     16  80 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
   17     17   -0.     -1.    ] stall 60
          18 +90 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          19 + -0.     -1.    ] stall 70
          20 +100 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          21 + -0.     -1.    ] stall 80
          22 +110 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          23 + -0.     -1.    ] stall 90
          24 +120 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          25 + -0.     -1.    ] stall 100
diff --git a/test_results.txt b/test_results.txt
index 44c76eb..0aeca3f 100644
--- a/test_results.txt
+++ b/test_results.txt
@@ -41,3 +41,12 @@ RESULT 2 {'object_count': 2} 350 False 12.36 phase grasp
   41     41  5 83 above block [0.464 0.111 0.1  ] held 0.0
   42     42  5 91 align block [0.464 0.111 0.1  ] held 0.0
   43     43  5 94 grasp block [0.464 0.111 0.1  ] held 0.0
          44 +5 102 lift block [0.464 0.111 0.125] held 1.0
          45 +5 110 carry block [0.464 0.111 0.3  ] held 1.0
          46 +5 114 lower block [ 0.233 -0.317  0.3  ] held 1.0
          47 +5 123 release block [ 0.233 -0.317  0.111] held 1.0
          48 +RESULT 5 {'object_count': 2} 125 True 14.87 phase release
          49 +6 0 above block [ 0.36  -0.128  0.1  ] held 0.0
          50 +6 8 align block [ 0.36  -0.128  0.1  ] held 0.0
          51 +6 12 grasp block [ 0.36  -0.128  0.1  ] held 0.0
          52 +6 21 lift block [ 0.36  -0.128  0.1  ] held 1.0
diff --git a/test_sweep_agent.out b/test_sweep_agent.out
new file mode 100644
index 0000000..e69de29
```

</details>

<a id="C032"></a>
### C032 · Replace iterative inverse kinematics with exact constant-time planar solution

Commit `b2a9ce72a6b9d0f57d06c83ef18984398dad6c58`; parents: b4b99fba09f0fc7c0af7537df5b3513144ca14d1. Recorded author date: 2026-09-20T02:54:16+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0095](01_timeline.md#E0095): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C032_b2a9ce7.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/debug2.txt b/debug2.txt
index 694f79a..971a325 100644
--- a/debug2.txt
+++ b/debug2.txt
@@ -23,3 +23,13 @@
   23     23   -0.     -1.    ] stall 90
   24     24  120 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
   25     25   -0.     -1.    ] stall 100
          26 +130 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          27 + -0.     -1.    ] stall 110
          28 +140 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          29 + -0.     -1.    ] stall 120
          30 +150 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          31 + -0.     -1.    ] stall 130
          32 +160 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          33 + -0.     -1.    ] stall 140
          34 +170 grasp obstruction1:Kinematic3DCuboid pos [0.1476 0.1024 0.1028] model [0.1476 0.1024 0.166 ] a [ 0.     -0.      0.      0.      0.0109  0.     -0.0099  0.      0.0208
          35 + -0.     -1.    ] stall 150
diff --git a/kin.py b/kin.py
index a9ab955..b5be755 100644
--- a/kin.py
+++ b/kin.py
@@ -1,6 +1,5 @@
    1      1  import numpy as np
    2      2  from scipy.spatial.transform import Rotation
    3        -from scipy.optimize import least_squares
    4      3  ORIGINS=[([0,0,.15643],np.pi),([0,.005375,-.12838],np.pi/2),([0,-.21038,-.006375],-np.pi/2),([0,.006375,-.21038],np.pi/2),([0,-.20843,-.006375],-np.pi/2),([0,0,-.10593],np.pi/2),([0,-.10593,0],-np.pi/2)]
    5      4  MATS=[Rotation.from_euler('x',a).as_matrix() for p,a in ORIGINS]
    6      5  Q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
@@ -13,10 +12,12 @@ def fk(q,d=.18):
   13     12   return t-r[:,2]*d,r
   14     13  
   15     14  def ik(x,z,d=.18):
   16        - def fun(v):
   17        -  q=Q0.copy();q[[1,3,5]]=v
   18        -  p,r=fk(q,d)
   19        -  return [p[0]-x,p[2]-z,r[0,2]]
   20        - fit=least_squares(fun,Q0[[1,3,5]],bounds=([-2,-2.57,-2],[2,2.57,2]),xtol=1e-10,gtol=1e-10,ftol=1e-10)
   21        - q=Q0.copy();q[[1,3,5]]=fit.x
   22        - return q
          15 +    # Closed-form planar elbow solution with a vertically aligned wrist.
          16 +    l1,l2=.42076,.31436
          17 +    zz=z-(.28481-.10593-d)
          18 +    c=np.clip((x*x+zz*zz-l1*l1-l2*l2)/(2*l1*l2),-1.,1.)
          19 +    beta=np.arccos(c)
          20 +    shoulder=np.arctan2(x,zz)-np.arctan2(l2*np.sin(beta),l1+l2*c)
          21 +    q=Q0.copy()
          22 +    q[1]=shoulder;q[3]=-beta;q[5]=shoulder+beta-np.pi
          23 +    return q
diff --git a/retry_results.txt b/retry_results.txt
new file mode 100644
index 0000000..317991c
--- /dev/null
+++ b/retry_results.txt
@@ -0,0 +1,28 @@
           1 +2 0 above block [ 0.189 -0.335  0.1  ] held 0.0
           2 +2 8 align block [ 0.189 -0.335  0.1  ] held 0.0
           3 +2 10 grasp block [ 0.189 -0.335  0.1  ] held 0.0
           4 +2 23 above block [ 0.189 -0.335  0.1  ] held 0.0
           5 +2 30 align block [ 0.189 -0.335  0.1  ] held 0.0
           6 +2 40 grasp block [ 0.189 -0.335  0.1  ] held 0.0
           7 +2 51 lift block [ 0.189 -0.335  0.1  ] held 1.0
           8 +2 59 carry block [ 0.189 -0.335  0.1  ] held 1.0
           9 +2 61 lower block [ 0.189 -0.335  0.1  ] held 1.0
          10 +2 71 release block [ 0.189 -0.335  0.1  ] held 1.0
          11 +2 73 above block [ 0.189 -0.335  0.1  ] held 0.0
          12 +2 81 align block [ 0.189 -0.335  0.1  ] held 0.0
          13 +2 91 grasp block [ 0.189 -0.335  0.1  ] held 0.0
          14 +2 101 lift block [ 0.189 -0.335  0.1  ] held 1.0
          15 +2 110 carry block [ 0.189 -0.335  0.1  ] held 1.0
          16 +2 112 lower block [ 0.189 -0.335  0.1  ] held 1.0
          17 +2 122 release block [ 0.189 -0.335  0.1  ] held 1.0
          18 +2 124 above block [ 0.189 -0.335  0.1  ] held 0.0
          19 +2 132 align block [ 0.189 -0.335  0.1  ] held 0.0
          20 +2 135 grasp block [ 0.189 -0.335  0.1  ] held 0.0
          21 +2 145 lift block [ 0.189 -0.335  0.125] held 1.0
          22 +2 153 carry block [ 0.189 -0.335  0.3  ] held 1.0
          23 +2 157 lower block [0.159 0.074 0.3  ] held 1.0
          24 +2 166 release block [0.159 0.074 0.111] held 1.0
          25 +RESULT 2 {'object_count': 2} 168 True 36.86 phase release
          26 +10 0 above block [0.361 0.259 0.1  ] held 0.0
          27 +10 8 align block [0.361 0.259 0.1  ] held 0.0
          28 +10 10 grasp block [0.361 0.259 0.1  ] held 0.0
diff --git a/test_results.txt b/test_results.txt
index 0aeca3f..8a600af 100644
--- a/test_results.txt
+++ b/test_results.txt
@@ -50,3 +50,37 @@ RESULT 5 {'object_count': 2} 125 True 14.87 phase release
   50     50  6 8 align block [ 0.36  -0.128  0.1  ] held 0.0
   51     51  6 12 grasp block [ 0.36  -0.128  0.1  ] held 0.0
   52     52  6 21 lift block [ 0.36  -0.128  0.1  ] held 1.0
          53 +6 29 carry block [ 0.36  -0.128  0.1  ] held 1.0
          54 +6 31 lower block [ 0.36  -0.128  0.1  ] held 1.0
          55 +6 40 release block [ 0.36  -0.128  0.1  ] held 1.0
          56 +6 42 above block [ 0.36  -0.128  0.1  ] held 0.0
          57 +6 49 align block [ 0.36  -0.128  0.1  ] held 0.0
          58 +6 53 grasp block [ 0.36  -0.128  0.1  ] held 0.0
          59 +6 61 lift block [ 0.36  -0.128  0.125] held 1.0
          60 +6 69 carry block [ 0.36  -0.128  0.3  ] held 1.0
          61 +6 73 lower block [0.259 0.36  0.3  ] held 1.0
          62 +6 82 release block [0.259 0.36  0.111] held 1.0
          63 +RESULT 6 {'object_count': 1} 84 True 25.36 phase release
          64 +7 0 above block [0.133 0.233 0.1  ] held 0.0
          65 +7 8 align block [0.133 0.233 0.1  ] held 0.0
          66 +7 10 grasp block [0.133 0.233 0.1  ] held 0.0
          67 +7 22 lift block [0.133 0.233 0.1  ] held 1.0
          68 +7 30 carry block [0.133 0.233 0.1  ] held 1.0
          69 +7 32 lower block [0.133 0.233 0.1  ] held 1.0
          70 +7 42 release block [0.133 0.233 0.1  ] held 1.0
          71 +7 44 above block [0.133 0.233 0.1  ] held 0.0
          72 +7 52 align block [0.133 0.233 0.1  ] held 0.0
          73 +7 56 grasp block [0.133 0.233 0.1  ] held 0.0
          74 +7 66 lift block [0.133 0.233 0.125] held 1.0
          75 +7 74 carry block [0.133 0.233 0.3  ] held 1.0
          76 +7 78 lower block [ 0.211 -0.141  0.3  ] held 1.0
          77 +7 87 release block [ 0.211 -0.141  0.111] held 1.0
          78 +RESULT 7 {'object_count': 2} 89 True 18.19 phase release
          79 +8 0 above block [ 0.278 -0.092  0.1  ] held 0.0
          80 +8 8 align block [ 0.278 -0.092  0.1  ] held 0.0
          81 +8 11 grasp block [ 0.278 -0.092  0.1  ] held 0.0
          82 +8 21 lift block [ 0.278 -0.092  0.1  ] held 1.0
          83 +8 29 carry block [ 0.278 -0.092  0.1  ] held 1.0
          84 +8 31 lower block [ 0.278 -0.092  0.1  ] held 1.0
          85 +8 41 release block [ 0.278 -0.092  0.1  ] held 1.0
          86 +8 43 above block [ 0.278 -0.092  0.1  ] held 0.0
diff --git a/test_sweep_agent.out b/test_sweep_agent.out
index e69de29..1875faa 100644
--- a/test_sweep_agent.out
+++ b/test_sweep_agent.out
@@ -0,0 +1,3 @@
           1 +{"seed": 20, "count": 2, "success": true, "steps": 132, "sec": 35.41}
           2 +{"seed": 21, "count": 0, "success": true, "steps": 42, "sec": 7.63}
           3 +{"seed": 22, "count": 2, "success": true, "steps": 88, "sec": 14.99}
```

</details>

<a id="C033"></a>
### C033 · Support explicit object-count robustness sweeps

Commit `3b0865efb246d7e1dec4e1449c4d62440c6d4295`; parents: b2a9ce72a6b9d0f57d06c83ef18984398dad6c58. Recorded author date: 2026-09-20T02:54:52+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C033_3b0865e.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/fast_results.txt b/fast_results.txt
new file mode 100644
index 0000000..ebdd8d1
--- /dev/null
+++ b/fast_results.txt
@@ -0,0 +1,66 @@
           1 +2 0 above block [ 0.189 -0.335  0.1  ] held 0.0
           2 +2 8 align block [ 0.189 -0.335  0.1  ] held 0.0
           3 +2 10 grasp block [ 0.189 -0.335  0.1  ] held 0.0
           4 +2 23 above block [ 0.189 -0.335  0.1  ] held 0.0
           5 +2 30 align block [ 0.189 -0.335  0.1  ] held 0.0
           6 +2 40 grasp block [ 0.189 -0.335  0.1  ] held 0.0
           7 +2 51 lift block [ 0.189 -0.335  0.1  ] held 1.0
           8 +2 59 carry block [ 0.189 -0.335  0.1  ] held 1.0
           9 +2 61 lower block [ 0.189 -0.335  0.1  ] held 1.0
          10 +2 71 release block [ 0.189 -0.335  0.1  ] held 1.0
          11 +2 73 above block [ 0.189 -0.335  0.1  ] held 0.0
          12 +2 81 align block [ 0.189 -0.335  0.1  ] held 0.0
          13 +2 91 grasp block [ 0.189 -0.335  0.1  ] held 0.0
          14 +2 101 lift block [ 0.189 -0.335  0.1  ] held 1.0
          15 +2 110 carry block [ 0.189 -0.335  0.1  ] held 1.0
          16 +2 112 lower block [ 0.189 -0.335  0.1  ] held 1.0
          17 +2 122 release block [ 0.189 -0.335  0.1  ] held 1.0
          18 +2 124 above block [ 0.189 -0.335  0.1  ] held 0.0
          19 +2 132 align block [ 0.189 -0.335  0.1  ] held 0.0
          20 +2 135 grasp block [ 0.189 -0.335  0.1  ] held 0.0
          21 +2 145 lift block [ 0.189 -0.335  0.125] held 1.0
          22 +2 153 carry block [ 0.189 -0.335  0.3  ] held 1.0
          23 +2 157 lower block [0.159 0.074 0.3  ] held 1.0
          24 +2 166 release block [0.159 0.074 0.111] held 1.0
          25 +RESULT 2 {'object_count': 2} 168 True 20.97 phase release
          26 +15 0 above block [ 0.373 -0.113  0.1  ] held 0.0
          27 +15 8 align block [ 0.373 -0.113  0.1  ] held 0.0
          28 +15 10 grasp block [ 0.373 -0.113  0.1  ] held 0.0
          29 +15 19 lift block [ 0.373 -0.113  0.1  ] held 1.0
          30 +15 27 carry block [ 0.373 -0.113  0.1  ] held 1.0
          31 +15 29 lower block [ 0.373 -0.113  0.1  ] held 1.0
          32 +15 38 release block [ 0.373 -0.113  0.1  ] held 1.0
          33 +15 40 above block [ 0.373 -0.113  0.1  ] held 0.0
          34 +15 47 align block [ 0.373 -0.113  0.1  ] held 0.0
          35 +15 49 grasp block [ 0.373 -0.113  0.1  ] held 0.0
          36 +15 59 lift block [ 0.373 -0.113  0.125] held 1.0
          37 +15 67 carry block [ 0.373 -0.113  0.3  ] held 1.0
          38 +15 70 lower block [0.155 0.051 0.3  ] held 1.0
          39 +15 79 release block [0.155 0.051 0.111] held 1.0
          40 +RESULT 15 {'object_count': 2} 81 True 1.37 phase release
          41 +16 0 above block [0.428 0.265 0.1  ] held 0.0
          42 +16 8 align block [0.428 0.265 0.1  ] held 0.0
          43 +16 10 grasp block [0.428 0.265 0.1  ] held 0.0
          44 +16 19 lift block [0.428 0.265 0.1  ] held 1.0
          45 +16 27 carry block [0.428 0.265 0.1  ] held 1.0
          46 +16 29 lower block [0.428 0.265 0.1  ] held 1.0
          47 +16 38 release block [0.428 0.265 0.1  ] held 1.0
          48 +16 40 above block [0.428 0.265 0.1  ] held 0.0
          49 +16 47 align block [0.428 0.265 0.1  ] held 0.0
          50 +16 49 grasp block [0.428 0.265 0.1  ] held 0.0
          51 +16 59 lift block [0.428 0.265 0.125] held 1.0
          52 +16 67 carry block [0.428 0.265 0.3  ] held 1.0
          53 +16 69 lower block [0.25  0.089 0.3  ] held 1.0
          54 +16 78 release block [0.25  0.089 0.111] held 1.0
          55 +RESULT 16 {'object_count': 1} 80 True 1.44 phase release
          56 +17 0 above block [0.276 0.085 0.1  ] held 0.0
          57 +17 8 align block [0.276 0.085 0.1  ] held 0.0
          58 +17 11 grasp block [0.276 0.085 0.1  ] held 0.0
          59 +17 21 lift block [0.276 0.085 0.1  ] held 1.0
          60 +17 29 carry block [0.276 0.085 0.1  ] held 1.0
          61 +17 31 lower block [0.276 0.085 0.1  ] held 1.0
          62 +17 41 release block [0.276 0.085 0.1  ] held 1.0
          63 +17 43 above block [0.276 0.085 0.1  ] held 0.0
          64 +17 51 align block [0.276 0.085 0.1  ] held 0.0
          65 +17 53 grasp block [0.276 0.085 0.1  ] held 0.0
          66 +17 64 lift block [0.276 0.085 0.1  ] held 1.0
diff --git a/retry_results.txt b/retry_results.txt
index 317991c..e509e46 100644
--- a/retry_results.txt
+++ b/retry_results.txt
@@ -26,3 +26,15 @@ RESULT 2 {'object_count': 2} 168 True 36.86 phase release
   26     26  10 0 above block [0.361 0.259 0.1  ] held 0.0
   27     27  10 8 align block [0.361 0.259 0.1  ] held 0.0
   28     28  10 10 grasp block [0.361 0.259 0.1  ] held 0.0
          29 +10 21 lift block [0.361 0.259 0.1  ] held 1.0
          30 +10 29 carry block [0.361 0.259 0.1  ] held 1.0
          31 +10 31 lower block [0.361 0.259 0.1  ] held 1.0
          32 +10 41 release block [0.361 0.259 0.1  ] held 1.0
          33 +10 43 above block [0.361 0.259 0.1  ] held 0.0
          34 +10 51 align block [0.361 0.259 0.1  ] held 0.0
          35 +10 54 grasp block [0.361 0.259 0.1  ] held 0.0
          36 +10 64 lift block [0.361 0.259 0.125] held 1.0
          37 +10 72 carry block [0.361 0.259 0.3  ] held 1.0
          38 +10 75 lower block [0.194 0.01  0.3  ] held 1.0
          39 +10 84 release block [0.194 0.01  0.111] held 1.0
          40 +RESULT 10 {'object_count': 2} 86 True 20.64 phase release
diff --git a/test_results.txt b/test_results.txt
index 8a600af..eba2faf 100644
--- a/test_results.txt
+++ b/test_results.txt
@@ -84,3 +84,12 @@ RESULT 7 {'object_count': 2} 89 True 18.19 phase release
   84     84  8 31 lower block [ 0.278 -0.092  0.1  ] held 1.0
   85     85  8 41 release block [ 0.278 -0.092  0.1  ] held 1.0
   86     86  8 43 above block [ 0.278 -0.092  0.1  ] held 0.0
          87 +8 51 align block [ 0.278 -0.092  0.1  ] held 0.0
          88 +8 53 grasp block [ 0.278 -0.092  0.1  ] held 0.0
          89 +8 65 lift block [ 0.278 -0.092  0.1  ] held 1.0
          90 +8 73 carry block [ 0.278 -0.092  0.1  ] held 1.0
          91 +8 75 lower block [ 0.278 -0.092  0.1  ] held 1.0
          92 +8 85 release block [ 0.278 -0.092  0.1  ] held 1.0
          93 +8 87 above block [ 0.278 -0.092  0.1  ] held 0.0
          94 +8 95 align block [ 0.278 -0.092  0.1  ] held 0.0
          95 +8 99 grasp block [ 0.278 -0.092  0.1  ] held 0.0
diff --git a/test_sweep_agent.out b/test_sweep_agent.out
index 1875faa..8751e37 100644
--- a/test_sweep_agent.out
+++ b/test_sweep_agent.out
@@ -1,3 +1,4 @@
    1      1  {"seed": 20, "count": 2, "success": true, "steps": 132, "sec": 35.41}
    2      2  {"seed": 21, "count": 0, "success": true, "steps": 42, "sec": 7.63}
    3      3  {"seed": 22, "count": 2, "success": true, "steps": 88, "sec": 14.99}
           4 +{"seed": 23, "count": 0, "success": true, "steps": 41, "sec": 8.17}
diff --git a/test_sweep_agent.py b/test_sweep_agent.py
index 5686ece..b34a4d1 100644
--- a/test_sweep_agent.py
+++ b/test_sweep_agent.py
@@ -2,9 +2,12 @@ from env_client import make_env
    2      2  from approach import GeneratedApproach
    3      3  import time,json
    4      4  import sys
    5        -seeds=list(range(20,40)) if len(sys.argv)<2 else [int(x) for x in sys.argv[1:]]
           5 +args=sys.argv[1:]
           6 +count=None
           7 +if args and args[0]=="--count":count=int(args[1]);args=args[2:]
           8 +seeds=list(range(20,40)) if not args else [int(x) for x in args]
    6      9  for seed in seeds:
    7        - e=make_env();s,i=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i);started=time.monotonic();done=False
          10 + e=make_env();s,i=e.reset(seed=seed,options={} if count is None else {"object_count":count});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i);started=time.monotonic();done=False
    8     11   for step in range(300):
    9     12    s,r,done,tr,i=e.step(p.get_action(s))
   10     13    if done or tr or time.monotonic()-started>50:break
```

</details>

<a id="C034"></a>
### C034 · Add evaluations for larger variable object counts

Commit `adf87a607d3d54b880ffd574cb528cad5716c00a`; parents: 3b0865efb246d7e1dec4e1449c4d62440c6d4295. Recorded author date: 2026-09-20T02:55:34+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0111](01_timeline.md#E0111): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C034_adf87a6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/fast_results.txt b/fast_results.txt
index ebdd8d1..9d51b1c 100644
--- a/fast_results.txt
+++ b/fast_results.txt
@@ -64,3 +64,44 @@ RESULT 16 {'object_count': 1} 80 True 1.44 phase release
   64     64  17 51 align block [0.276 0.085 0.1  ] held 0.0
   65     65  17 53 grasp block [0.276 0.085 0.1  ] held 0.0
   66     66  17 64 lift block [0.276 0.085 0.1  ] held 1.0
          67 +17 73 carry block [0.276 0.085 0.1  ] held 1.0
          68 +17 75 lower block [0.276 0.085 0.1  ] held 1.0
          69 +17 85 release block [0.276 0.085 0.1  ] held 1.0
          70 +17 87 above block [0.276 0.085 0.1  ] held 0.0
          71 +17 96 align block [0.276 0.085 0.1  ] held 0.0
          72 +17 99 grasp block [0.276 0.085 0.1  ] held 0.0
          73 +17 107 lift block [0.276 0.085 0.125] held 1.0
          74 +17 115 carry block [0.276 0.085 0.3  ] held 1.0
          75 +17 118 lower block [ 0.259 -0.214  0.3  ] held 1.0
          76 +17 127 release block [ 0.259 -0.214  0.111] held 1.0
          77 +RESULT 17 {'object_count': 2} 129 True 10.42 phase release
          78 +18 0 above block [0.35  0.056 0.1  ] held 0.0
          79 +18 8 align block [0.35  0.056 0.1  ] held 0.0
          80 +18 11 grasp block [0.35  0.056 0.1  ] held 0.0
          81 +18 21 lift block [0.35  0.056 0.1  ] held 1.0
          82 +18 29 carry block [0.35  0.056 0.1  ] held 1.0
          83 +18 31 lower block [0.35  0.056 0.1  ] held 1.0
          84 +18 40 release block [0.35  0.056 0.1  ] held 1.0
          85 +18 42 above block [0.35  0.056 0.1  ] held 0.0
          86 +18 50 align block [0.35  0.056 0.1  ] held 0.0
          87 +18 53 grasp block [0.35  0.056 0.1  ] held 0.0
          88 +18 61 lift block [0.35  0.056 0.125] held 1.0
          89 +18 69 carry block [0.35  0.056 0.3  ] held 1.0
          90 +18 72 lower block [0.16  0.337 0.3  ] held 1.0
          91 +18 81 release block [0.16  0.337 0.111] held 1.0
          92 +RESULT 18 {'object_count': 2} 83 True 5.51 phase release
          93 +19 0 above block [0.398 0.028 0.1  ] held 0.0
          94 +19 8 align block [0.398 0.028 0.1  ] held 0.0
          95 +19 10 grasp block [0.398 0.028 0.1  ] held 0.0
          96 +19 21 lift block [0.398 0.028 0.1  ] held 1.0
          97 +19 29 carry block [0.398 0.028 0.1  ] held 1.0
          98 +19 31 lower block [0.398 0.028 0.1  ] held 1.0
          99 +19 41 release block [0.398 0.028 0.1  ] held 1.0
         100 +19 43 above block [0.398 0.028 0.1  ] held 0.0
         101 +19 51 align block [0.398 0.028 0.1  ] held 0.0
         102 +19 53 grasp block [0.398 0.028 0.1  ] held 0.0
         103 +19 63 lift block [0.398 0.028 0.125] held 1.0
         104 +19 71 carry block [0.398 0.028 0.3  ] held 1.0
         105 +19 74 lower block [ 0.153 -0.133  0.3  ] held 1.0
         106 +19 83 release block [ 0.153 -0.133  0.111] held 1.0
         107 +RESULT 19 {'object_count': 1} 85 True 4.74 phase release
diff --git a/test_counts.py b/test_counts.py
new file mode 100644
index 0000000..beea76b
--- /dev/null
+++ b/test_counts.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import time,json,sys,numpy as np
           4 +for count in map(int,sys.argv[1:] or ['5','10']):
           5 + for seed in range(4):
           6 +  E=make_env();s,info=E.reset(seed=seed,options={'object_count':count});p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info);start=time.monotonic();term=False
           7 +  for t in range(min(1000,100+60*count)):
           8 +   s,rew,term,trunc,info=E.step(p.get_action(s))
           9 +   if term or trunc:break
          10 +  print(json.dumps(dict(seed=seed,count=count,success=term,steps=t+1,seconds=round(time.monotonic()-start,2),phase=p.phase,obj=str(p.obj),index=p.index,todo=len(p.todo),stall=p.stall,attempt=p.attempt,pos=p.pos(s,p.obj).tolist(),dest=p.destination.tolist())),flush=True)
          11 +  E.close()
diff --git a/test_sweep_fast.out b/test_sweep_fast.out
new file mode 100644
index 0000000..48206c9
--- /dev/null
+++ b/test_sweep_fast.out
@@ -0,0 +1,7 @@
           1 +{"seed": 24, "count": 1, "success": true, "steps": 41, "sec": 1.36}
           2 +{"seed": 25, "count": 1, "success": true, "steps": 85, "sec": 8.09}
           3 +{"seed": 26, "count": 2, "success": true, "steps": 89, "sec": 8.91}
           4 +{"seed": 27, "count": 0, "success": true, "steps": 43, "sec": 0.7}
           5 +{"seed": 28, "count": 1, "success": true, "steps": 87, "sec": 1.44}
           6 +{"seed": 29, "count": 2, "success": true, "steps": 41, "sec": 0.74}
           7 +{"seed": 30, "count": 0, "success": true, "steps": 42, "sec": 0.86}
```

</details>

<a id="C035"></a>
### C035 · Handle incidental grasps and adapt obstruction placement to crowded tables

Commit `859a11f7a46b1bd93b1edca232a6064b583d21fb`; parents: adf87a607d3d54b880ffd574cb528cad5716c00a. Recorded author date: 2026-09-20T02:57:02+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0103](01_timeline.md#E0103): commit hash in recorded output.
[Controller after this commit](evidence/versions/C035_859a11f_approach.py) · [Exact all-file diff](evidence/diffs/C035_859a11f.diff)

[Previous saved controller snapshot](evidence/versions/C031_b4b99fb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6b8d102..776945a 100644
--- a/approach.py
+++ b/approach.py
@@ -19,7 +19,7 @@ class GeneratedApproach:
   19     19          obs=[o for o in self.objects if o not in [self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-rp[:2]) < self.size(state,o)[:2]+rs[:2]+.012)]
   20     20          obs.sort(key=lambda o:-self.pos(state,o)[2])
   21     21          self.todo=obs+[self.block];self.index=0;self.phase='above';self.t=0;self.stall=0;self.last=None
   22        -        self.attempt=0;self.wrist=np.pi/2;self.obj=self.todo[0];self.destination=self.choose_destination(state)
          22 +        self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
   23     23      def choose_destination(self,state):
   24     24          if self.obj==self.block:
   25     25              p=self.pos(state,self.region).copy();p[2]+=self.size(state,self.region)[2]+self.size(state,self.obj)[2]+.001
@@ -33,10 +33,25 @@ class GeneratedApproach:
   33     33                      if other==self.obj:continue
   34     34                      op=self.pos(state,other);oh=self.size(state,other)
   35     35                      if np.all(np.abs(p[:2]-op[:2]) < h[:2]+oh[:2]+.009):free=False;break
   36        -                if free:candidates.append(p)
          36 +                if free:
          37 +                    if all(np.linalg.norm(p[:2]-bad)>.025 for bad in self.failed_places):candidates.append(p)
   37     38          if candidates:
   38     39              start=self.pos(state,self.obj)
   39     40              return min(candidates,key=lambda p:np.linalg.norm(p[:2]-start[:2]))
          41 +        # Rectangle-edge candidates provide finer packing as the object count grows.
          42 +        xs=[.103+h[0],.497-h[0]];ys=[-.397+h[1],.397-h[1]]
          43 +        for other in self.objects:
          44 +            if other==self.obj:continue
          45 +            op=self.pos(state,other);oh=self.size(state,other)
          46 +            xs.extend([op[0]-oh[0]-h[0]-.005,op[0]+oh[0]+h[0]+.005])
          47 +            ys.extend([op[1]-oh[1]-h[1]-.005,op[1]+oh[1]+h[1]+.005])
          48 +        for x in xs:
          49 +            if not .1+h[0]<x<.5-h[0]:continue
          50 +            for y in ys:
          51 +                if not -.4+h[1]<y<.4-h[1]:continue
          52 +                p=np.array([x,y,.076+h[2]])
          53 +                if any(np.linalg.norm(p[:2]-bad)<.025 for bad in self.failed_places):continue
          54 +                if all(other==self.obj or np.any(np.abs(p[:2]-self.pos(state,other)[:2])>=h[:2]+self.size(state,other)[:2]+.003) for other in self.objects):return p
   40     55          return np.array([.135,-.36,.076+h[2]])
   41     56      def get_action(self,state):
   42     57          self.t+=1;r=self.robot
@@ -54,12 +69,17 @@ class GeneratedApproach:
   54     69          if held and self.phase in ['above','align','grasp']:
   55     70              grabbed=[o for o in self.objects if state.get(o,'grasp_active')>0]
   56     71              if grabbed and grabbed[0]!=self.obj:
   57        -                self.obj=grabbed[0];self.destination=self.choose_destination(state);bp=self.pos(state,self.obj)
          72 +                actual=grabbed[0]
          73 +                self.todo=[o for j,o in enumerate(self.todo) if o!=actual or j<self.index]
          74 +                self.todo.insert(self.index,actual)
          75 +                self.obj=actual;self.destination=self.choose_destination(state);bp=self.pos(state,self.obj)
   58     76              self.phase='lift';self.lift_xy=bp[:2].copy()
   59     77          if self.phase=='release' and not held:
   60     78              self.index+=1
   61     79              if self.index>=len(self.todo):self.index=len(self.todo)-1
   62        -            self.attempt=0;self.wrist=np.pi/2;self.obj=self.todo[self.index];self.destination=self.choose_destination(state);self.phase='above';bp=self.pos(state,self.obj)
          80 +            self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[self.index];self.destination=self.choose_destination(state);self.phase='above';bp=self.pos(state,self.obj)
          81 +        if held and self.phase=='lower' and self.obj!=self.block and self.stall>=3:
          82 +            self.failed_places.append(self.destination[:2].copy());self.destination=self.choose_destination(state);self.phase='lift';self.lift_xy=bp[:2].copy();self.stall=0
   63     83          grip=0
   64     84          if self.phase=='above':dest=np.r_[model[:2],.34]
   65     85          elif self.phase=='align':dest=np.r_[bp[:2],.34]
diff --git a/count_results.txt b/count_results.txt
new file mode 100644
index 0000000..9c44a2a
--- /dev/null
+++ b/count_results.txt
@@ -0,0 +1,3 @@
           1 +{"seed": 0, "count": 5, "success": true, "steps": 216, "seconds": 19.16, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 4, "todo": 5, "stall": 1, "attempt": 0, "pos": [0.1444271355867386, 0.23301441967487335, 0.11099999397993088], "dest": [0.14442715048789978, 0.23301441967487335, 0.11099999847263098]}
           2 +{"seed": 1, "count": 5, "success": true, "steps": 209, "seconds": 25.18, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 4, "todo": 5, "stall": 1, "attempt": 0, "pos": [0.44773608446121216, -0.132277250289917, 0.11100000143051147], "dest": [0.44773608446121216, -0.132277250289917, 0.11099999847263098]}
           3 +{"seed": 2, "count": 5, "success": true, "steps": 211, "seconds": 25.47, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 3, "todo": 4, "stall": 1, "attempt": 0, "pos": [0.15949536859989166, 0.0742836520075798, 0.11100000143051147], "dest": [0.15949532389640808, 0.0742836520075798, 0.11099999847263098]}
diff --git a/test_sweep_fast.out b/test_sweep_fast.out
index 48206c9..02e927b 100644
--- a/test_sweep_fast.out
+++ b/test_sweep_fast.out
@@ -5,3 +5,12 @@
    5      5  {"seed": 28, "count": 1, "success": true, "steps": 87, "sec": 1.44}
    6      6  {"seed": 29, "count": 2, "success": true, "steps": 41, "sec": 0.74}
    7      7  {"seed": 30, "count": 0, "success": true, "steps": 42, "sec": 0.86}
           8 +{"seed": 31, "count": 1, "success": true, "steps": 83, "sec": 8.48}
           9 +{"seed": 32, "count": 2, "success": true, "steps": 130, "sec": 6.93}
          10 +{"seed": 33, "count": 2, "success": true, "steps": 129, "sec": 13.26}
          11 +{"seed": 34, "count": 0, "success": true, "steps": 41, "sec": 1.73}
          12 +{"seed": 35, "count": 0, "success": true, "steps": 43, "sec": 2.18}
          13 +{"seed": 36, "count": 1, "success": true, "steps": 84, "sec": 10.49}
          14 +{"seed": 37, "count": 0, "success": true, "steps": 41, "sec": 1.79}
          15 +{"seed": 38, "count": 0, "success": true, "steps": 41, "sec": 2.7}
          16 +{"seed": 39, "count": 2, "success": true, "steps": 123, "sec": 8.7}
```

</details>

<a id="C036"></a>
### C036 · Shorten safe vertical transit paths to reduce episode time

Commit `7fc3841901533a22a43085a002237b89b9bf27a0`; parents: 859a11f7a46b1bd93b1edca232a6064b583d21fb. Recorded author date: 2026-09-20T02:57:42+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0123](01_timeline.md#E0123): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C036_7fc3841_approach.py) · [Exact all-file diff](evidence/diffs/C036_7fc3841.diff)

[Previous saved controller snapshot](evidence/versions/C035_859a11f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 776945a..c7bacac 100644
--- a/approach.py
+++ b/approach.py
@@ -81,17 +81,17 @@ class GeneratedApproach:
   81     81          if held and self.phase=='lower' and self.obj!=self.block and self.stall>=3:
   82     82              self.failed_places.append(self.destination[:2].copy());self.destination=self.choose_destination(state);self.phase='lift';self.lift_xy=bp[:2].copy();self.stall=0
   83     83          grip=0
   84        -        if self.phase=='above':dest=np.r_[model[:2],.34]
   85        -        elif self.phase=='align':dest=np.r_[bp[:2],.34]
          84 +        if self.phase=='above':dest=np.r_[model[:2],.30]
          85 +        elif self.phase=='align':dest=np.r_[bp[:2],.30]
   86     86          elif self.phase=='grasp':dest=bp+[0,0,.025];grip=-1
   87        -        elif self.phase=='lift':dest=np.r_[self.lift_xy,.30]
   88        -        elif self.phase=='carry':dest=np.r_[self.destination[:2],.30]
          87 +        elif self.phase=='lift':dest=np.r_[self.lift_xy,.24]
          88 +        elif self.phase=='carry':dest=np.r_[self.destination[:2],.24]
   89     89          elif self.phase=='lower':dest=self.destination.copy()
   90     90          else:dest=bp.copy();grip=1
   91     91          if held:dest=dest+model-bp
   92        -        if self.phase=='above':dest[2]=.34
          92 +        if self.phase=='above':dest[2]=.30
   93     93          # Preserve a vertical wrist throughout travel and use the mobile base for XY.
   94        -        dz=np.clip(dest[2]-model[2],-.008 if self.phase=='grasp' and model[2]-bp[2]<.09 else -.025,.025)
          94 +        dz=np.clip(dest[2]-model[2],-.008 if self.phase=='grasp' and model[2]-bp[2]<.09 else -.04,.04)
   95     95          z=model[2]+dz
   96     96          key=round(float(z),7)
   97     97          if key not in self.cache:self.cache[key]=ik(.50,z)
diff --git a/approach_safe.py b/approach_safe.py
new file mode 100644
index 0000000..776945a
--- /dev/null
+++ b/approach_safe.py
@@ -0,0 +1,107 @@
           1 +import numpy as np
           2 +from kin import ik, fk
           3 +
           4 +class GeneratedApproach:
           5 +    def __init__(self, action_space, observation_space, primitives):
           6 +        self.action_space=action_space
           7 +        self.observation_space=observation_space
           8 +        self.cache={}
           9 +    def pos(self,state,obj):
          10 +        return np.array([state.get(obj,'pose_'+f) for f in 'xyz'])
          11 +    def size(self,state,obj):
          12 +        return np.array([state.get(obj,'half_extent_'+f) for f in 'xyz'])
          13 +    def reset(self,state,info):
          14 +        self.robot=state.get_objects(self.observation_space.get_type('Kinematic3DRobot'))[0]
          15 +        self.block=state.get_object_from_name('target_block')
          16 +        self.region=state.get_object_from_name('target_region')
          17 +        self.objects=state.get_objects(self.observation_space.get_type('Kinematic3DCuboid'))
          18 +        rp=self.pos(state,self.region);rs=self.size(state,self.region)
          19 +        obs=[o for o in self.objects if o not in [self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-rp[:2]) < self.size(state,o)[:2]+rs[:2]+.012)]
          20 +        obs.sort(key=lambda o:-self.pos(state,o)[2])
          21 +        self.todo=obs+[self.block];self.index=0;self.phase='above';self.t=0;self.stall=0;self.last=None
          22 +        self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
          23 +    def choose_destination(self,state):
          24 +        if self.obj==self.block:
          25 +            p=self.pos(state,self.region).copy();p[2]+=self.size(state,self.region)[2]+self.size(state,self.obj)[2]+.001
          26 +            return p
          27 +        h=self.size(state,self.obj)
          28 +        candidates=[]
          29 +        for x in [.135,.2,.265,.33,.395,.465]:
          30 +            for y in [-.36,.36,-.29,.29,-.22,.22,-.15,.15,0]:
          31 +                p=np.array([x,y,.075+h[2]+.001]);free=True
          32 +                for other in self.objects:
          33 +                    if other==self.obj:continue
          34 +                    op=self.pos(state,other);oh=self.size(state,other)
          35 +                    if np.all(np.abs(p[:2]-op[:2]) < h[:2]+oh[:2]+.009):free=False;break
          36 +                if free:
          37 +                    if all(np.linalg.norm(p[:2]-bad)>.025 for bad in self.failed_places):candidates.append(p)
          38 +        if candidates:
          39 +            start=self.pos(state,self.obj)
          40 +            return min(candidates,key=lambda p:np.linalg.norm(p[:2]-start[:2]))
          41 +        # Rectangle-edge candidates provide finer packing as the object count grows.
          42 +        xs=[.103+h[0],.497-h[0]];ys=[-.397+h[1],.397-h[1]]
          43 +        for other in self.objects:
          44 +            if other==self.obj:continue
          45 +            op=self.pos(state,other);oh=self.size(state,other)
          46 +            xs.extend([op[0]-oh[0]-h[0]-.005,op[0]+oh[0]+h[0]+.005])
          47 +            ys.extend([op[1]-oh[1]-h[1]-.005,op[1]+oh[1]+h[1]+.005])
          48 +        for x in xs:
          49 +            if not .1+h[0]<x<.5-h[0]:continue
          50 +            for y in ys:
          51 +                if not -.4+h[1]<y<.4-h[1]:continue
          52 +                p=np.array([x,y,.076+h[2]])
          53 +                if any(np.linalg.norm(p[:2]-bad)<.025 for bad in self.failed_places):continue
          54 +                if all(other==self.obj or np.any(np.abs(p[:2]-self.pos(state,other)[:2])>=h[:2]+self.size(state,other)[:2]+.003) for other in self.objects):return p
          55 +        return np.array([.135,-.36,.076+h[2]])
          56 +    def get_action(self,state):
          57 +        self.t+=1;r=self.robot
          58 +        qnow=np.array([state.get(r,'joint_'+str(i)) for i in range(1,8)])
          59 +        base=np.array([state.get(r,'pos_base_x'),state.get(r,'pos_base_y')])
          60 +        model,_=fk(qnow);model+=np.r_[base+[.12,0],0]
          61 +        held=state.get(r,'grasp_active')>0
          62 +        bp=self.pos(state,self.obj)
          63 +        signature=np.r_[base,qnow,held]
          64 +        if self.last is not None and np.max(abs(signature-self.last))<1e-6:self.stall+=1
          65 +        else:self.stall=0
          66 +        self.last=signature
          67 +        if not held and self.phase=='grasp' and self.stall>=3:
          68 +            self.attempt+=1;self.wrist=[np.pi/2,0,np.pi/4,-np.pi/4][self.attempt%4];self.phase='above';self.stall=0
          69 +        if held and self.phase in ['above','align','grasp']:
          70 +            grabbed=[o for o in self.objects if state.get(o,'grasp_active')>0]
          71 +            if grabbed and grabbed[0]!=self.obj:
          72 +                actual=grabbed[0]
          73 +                self.todo=[o for j,o in enumerate(self.todo) if o!=actual or j<self.index]
          74 +                self.todo.insert(self.index,actual)
          75 +                self.obj=actual;self.destination=self.choose_destination(state);bp=self.pos(state,self.obj)
          76 +            self.phase='lift';self.lift_xy=bp[:2].copy()
          77 +        if self.phase=='release' and not held:
          78 +            self.index+=1
          79 +            if self.index>=len(self.todo):self.index=len(self.todo)-1
          80 +            self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[self.index];self.destination=self.choose_destination(state);self.phase='above';bp=self.pos(state,self.obj)
          81 +        if held and self.phase=='lower' and self.obj!=self.block and self.stall>=3:
          82 +            self.failed_places.append(self.destination[:2].copy());self.destination=self.choose_destination(state);self.phase='lift';self.lift_xy=bp[:2].copy();self.stall=0
          83 +        grip=0
          84 +        if self.phase=='above':dest=np.r_[model[:2],.34]
          85 +        elif self.phase=='align':dest=np.r_[bp[:2],.34]
          86 +        elif self.phase=='grasp':dest=bp+[0,0,.025];grip=-1
          87 +        elif self.phase=='lift':dest=np.r_[self.lift_xy,.30]
          88 +        elif self.phase=='carry':dest=np.r_[self.destination[:2],.30]
          89 +        elif self.phase=='lower':dest=self.destination.copy()
          90 +        else:dest=bp.copy();grip=1
          91 +        if held:dest=dest+model-bp
          92 +        if self.phase=='above':dest[2]=.34
          93 +        # Preserve a vertical wrist throughout travel and use the mobile base for XY.
          94 +        dz=np.clip(dest[2]-model[2],-.008 if self.phase=='grasp' and model[2]-bp[2]<.09 else -.025,.025)
          95 +        z=model[2]+dz
          96 +        key=round(float(z),7)
          97 +        if key not in self.cache:self.cache[key]=ik(.50,z)
          98 +        q=self.cache[key].copy()
          99 +        q[6]=qnow[6] if self.phase=='above' else self.wrist
         100 +        targetbase=dest[:2]-[.62,.001]
         101 +        delta=np.r_[targetbase-base,q-qnow]
         102 +        scale=max(1.,np.max(np.abs(delta))/.18)
         103 +        a=np.zeros(11,dtype=np.float32);a[:2]=delta[:2]/scale;a[3:10]=delta[2:]/scale;a[10]=grip
         104 +        error=np.max(np.abs(dest-model))
         105 +        if error<.0015 and np.max(abs(q-qnow))<.006:
         106 +            self.phase={'above':'align','align':'grasp','grasp':'grasp','lift':'carry','carry':'lower','lower':'release','release':'release'}[self.phase]
         107 +        return np.clip(a,self.action_space.low,self.action_space.high)
diff --git a/count_results.txt b/count_results.txt
index 9c44a2a..994b2bc 100644
--- a/count_results.txt
+++ b/count_results.txt
@@ -1,3 +1,5 @@
    1      1  {"seed": 0, "count": 5, "success": true, "steps": 216, "seconds": 19.16, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 4, "todo": 5, "stall": 1, "attempt": 0, "pos": [0.1444271355867386, 0.23301441967487335, 0.11099999397993088], "dest": [0.14442715048789978, 0.23301441967487335, 0.11099999847263098]}
    2      2  {"seed": 1, "count": 5, "success": true, "steps": 209, "seconds": 25.18, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 4, "todo": 5, "stall": 1, "attempt": 0, "pos": [0.44773608446121216, -0.132277250289917, 0.11100000143051147], "dest": [0.44773608446121216, -0.132277250289917, 0.11099999847263098]}
    3      3  {"seed": 2, "count": 5, "success": true, "steps": 211, "seconds": 25.47, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 3, "todo": 4, "stall": 1, "attempt": 0, "pos": [0.15949536859989166, 0.0742836520075798, 0.11100000143051147], "dest": [0.15949532389640808, 0.0742836520075798, 0.11099999847263098]}
           4 +{"seed": 3, "count": 5, "success": true, "steps": 125, "seconds": 2.16, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 2, "todo": 3, "stall": 1, "attempt": 0, "pos": [0.3291561007499695, -0.3026953637599945, 0.11099997907876968], "dest": [0.3291561007499695, -0.3026953637599945, 0.11099999847263098]}
           5 +{"seed": 0, "count": 10, "success": false, "steps": 700, "seconds": 21.26, "phase": "above", "obj": "obstruction5:Kinematic3DCuboid", "index": 1, "todo": 7, "stall": 655, "attempt": 0, "pos": [0.1584508866071701, 0.1740739494562149, 0.10397887229919434], "dest": [0.135, 0.15, 0.1049788730442524]}
diff --git a/test_quick.py b/test_quick.py
new file mode 100644
index 0000000..a56ff47
--- /dev/null
+++ b/test_quick.py
@@ -0,0 +1,10 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import time,json,sys
           4 +seeds=list(map(int,sys.argv[1:])) or list(range(20))
           5 +for seed in seeds:
           6 + e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info);start=time.monotonic();term=False
           7 + for t in range(400):
           8 +  s,r,term,trunc,_=e.step(p.get_action(s))
           9 +  if term or trunc:break
          10 + print(json.dumps(dict(seed=seed,count=info['object_count'],success=term,steps=t+1,seconds=round(time.monotonic()-start,2),phase=p.phase,obj=str(p.obj),stall=p.stall,attempt=p.attempt)),flush=True);e.close()
diff --git a/test_sweep_extended.out b/test_sweep_extended.out
new file mode 100644
index 0000000..ebce298
--- /dev/null
+++ b/test_sweep_extended.out
@@ -0,0 +1,5 @@
           1 +{"seed": 40, "count": 1, "success": true, "steps": 85, "sec": 2.38}
           2 +{"seed": 41, "count": 1, "success": true, "steps": 80, "sec": 1.94}
           3 +{"seed": 42, "count": 0, "success": true, "steps": 42, "sec": 1.08}
           4 +{"seed": 43, "count": 1, "success": true, "steps": 79, "sec": 5.12}
           5 +{"seed": 44, "count": 2, "success": true, "steps": 84, "sec": 4.0}
```

</details>

<a id="C037"></a>
### C037 · Reserve gripper clearance around obstruction disposal sites

Commit `eeb54576b983f9c3a947b25db741119ccecd8b47`; parents: 7fc3841901533a22a43085a002237b89b9bf27a0. Recorded author date: 2026-09-20T02:58:21+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0120](01_timeline.md#E0120): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C037_eeb5457_approach.py) · [Exact all-file diff](evidence/diffs/C037_eeb5457.diff)

[Previous saved controller snapshot](evidence/versions/C036_7fc3841_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c7bacac..1060e8d 100644
--- a/approach.py
+++ b/approach.py
@@ -32,7 +32,7 @@ class GeneratedApproach:
   32     32                  for other in self.objects:
   33     33                      if other==self.obj:continue
   34     34                      op=self.pos(state,other);oh=self.size(state,other)
   35        -                    if np.all(np.abs(p[:2]-op[:2]) < h[:2]+oh[:2]+.009):free=False;break
          35 +                    if np.all(np.abs(p[:2]-op[:2]) < np.maximum(h[:2],.055)+oh[:2]+.009):free=False;break
   36     36                  if free:
   37     37                      if all(np.linalg.norm(p[:2]-bad)>.025 for bad in self.failed_places):candidates.append(p)
   38     38          if candidates:
diff --git a/debug_policy.py b/debug_policy.py
index 7e2f161..cabbe39 100644
--- a/debug_policy.py
+++ b/debug_policy.py
@@ -3,7 +3,7 @@ from approach import GeneratedApproach
    3      3  from kin import fk
    4      4  import sys,numpy as np
    5      5  seed=int(sys.argv[1]) if len(sys.argv)>1 else 0
    6        -E=make_env();s,i=E.reset(seed=seed);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,i)
           6 +E=make_env();s,i=E.reset(seed=seed,options={'object_count':int(sys.argv[2])}) if len(sys.argv)>2 else E.reset(seed=seed);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,i)
    7      7  for t in range(180):
    8      8   a=p.get_action(s);s,rew,te,tr,inf=E.step(a)
    9      9   if t%10==0 or te:
diff --git a/quick_results.txt b/quick_results.txt
new file mode 100644
index 0000000..a33587f
--- /dev/null
+++ b/quick_results.txt
@@ -0,0 +1,2 @@
           1 +{"seed": 0, "count": 2, "success": true, "steps": 86, "seconds": 12.06, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 1, "attempt": 0}
           2 +{"seed": 1, "count": 1, "success": true, "steps": 58, "seconds": 11.32, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 1, "attempt": 0}
diff --git a/test_sweep_extended.out b/test_sweep_extended.out
index ebce298..8bc1c92 100644
--- a/test_sweep_extended.out
+++ b/test_sweep_extended.out
@@ -3,3 +3,5 @@
    3      3  {"seed": 42, "count": 0, "success": true, "steps": 42, "sec": 1.08}
    4      4  {"seed": 43, "count": 1, "success": true, "steps": 79, "sec": 5.12}
    5      5  {"seed": 44, "count": 2, "success": true, "steps": 84, "sec": 4.0}
           6 +{"seed": 45, "count": 2, "success": true, "steps": 157, "sec": 21.43}
           7 +{"seed": 46, "count": 1, "success": true, "steps": 82, "sec": 10.57}
```

</details>

<a id="C038"></a>
### C038 · Park incidentally grasped target until remaining obstructions are cleared

Commit `7ba3e01ecc6eac6616294cdb0c39b42800026299`; parents: eeb54576b983f9c3a947b25db741119ccecd8b47. Recorded author date: 2026-09-20T03:00:41+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0130](01_timeline.md#E0130): commit hash in recorded output.
[Controller after this commit](evidence/versions/C038_7ba3e01_approach.py) · [Exact all-file diff](evidence/diffs/C038_7ba3e01.diff)

[Previous saved controller snapshot](evidence/versions/C037_eeb5457_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1060e8d..afc47f7 100644
--- a/approach.py
+++ b/approach.py
@@ -21,7 +21,8 @@ class GeneratedApproach:
   21     21          self.todo=obs+[self.block];self.index=0;self.phase='above';self.t=0;self.stall=0;self.last=None
   22     22          self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
   23     23      def choose_destination(self,state):
   24        -        if self.obj==self.block:
          24 +        self.placing_goal=self.obj==self.block and not any(o!=self.block for o in self.todo[self.index+1:])
          25 +        if self.placing_goal:
   25     26              p=self.pos(state,self.region).copy();p[2]+=self.size(state,self.region)[2]+self.size(state,self.obj)[2]+.001
   26     27              return p
   27     28          h=self.size(state,self.obj)
@@ -72,13 +73,14 @@ class GeneratedApproach:
   72     73                  actual=grabbed[0]
   73     74                  self.todo=[o for j,o in enumerate(self.todo) if o!=actual or j<self.index]
   74     75                  self.todo.insert(self.index,actual)
          76 +                if actual==self.block and any(o!=self.block for o in self.todo[self.index+1:]):self.todo.append(self.block)
   75     77                  self.obj=actual;self.destination=self.choose_destination(state);bp=self.pos(state,self.obj)
   76     78              self.phase='lift';self.lift_xy=bp[:2].copy()
   77     79          if self.phase=='release' and not held:
   78     80              self.index+=1
   79     81              if self.index>=len(self.todo):self.index=len(self.todo)-1
   80     82              self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[self.index];self.destination=self.choose_destination(state);self.phase='above';bp=self.pos(state,self.obj)
   81        -        if held and self.phase=='lower' and self.obj!=self.block and self.stall>=3:
          83 +        if held and self.phase=='lower' and not self.placing_goal and self.stall>=3:
   82     84              self.failed_places.append(self.destination[:2].copy());self.destination=self.choose_destination(state);self.phase='lift';self.lift_xy=bp[:2].copy();self.stall=0
   83     85          grip=0
   84     86          if self.phase=='above':dest=np.r_[model[:2],.30]
diff --git a/count_fast_results.txt b/count_fast_results.txt
new file mode 100644
index 0000000..d30d21e
--- /dev/null
+++ b/count_fast_results.txt
@@ -0,0 +1,3 @@
           1 +{"seed": 0, "count": 10, "success": true, "steps": 199, "seconds": 23.99, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 6, "todo": 7, "stall": 1, "attempt": 0, "pos": [0.14442715048789978, 0.23301441967487335, 0.11100000888109207], "dest": [0.14442715048789978, 0.23301441967487335, 0.11099999847263098]}
           2 +{"seed": 1, "count": 10, "success": true, "steps": 186, "seconds": 22.3, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 6, "todo": 7, "stall": 1, "attempt": 0, "pos": [0.44773608446121216, -0.132277250289917, 0.11100002378225327], "dest": [0.44773608446121216, -0.132277250289917, 0.11099999847263098]}
           3 +{"seed": 2, "count": 10, "success": true, "steps": 169, "seconds": 23.67, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 4, "todo": 5, "stall": 1, "attempt": 0, "pos": [0.15949538350105286, 0.0742836594581604, 0.11100000143051147], "dest": [0.15949532389640808, 0.0742836520075798, 0.11099999847263098]}
diff --git a/debug_count10.txt b/debug_count10.txt
new file mode 100644
index 0000000..290d473
--- /dev/null
+++ b/debug_count10.txt
@@ -0,0 +1,30 @@
           1 +0 above obstruction7:Kinematic3DCuboid pos [0.1434 0.2641 0.1046] model [0.1543 0.001  0.2505] a [-0.0568  0.      0.      0.      0.1399  0.      0.18    0.     -0.06
           2 +  0.      0.    ] stall 0
           3 +10 grasp obstruction7:Kinematic3DCuboid pos [0.1434 0.2641 0.1046] model [0.1434 0.2641 0.3   ] a [-0. -0.  0.  0. -0. -0.  0.  0. -0. -0.  0.] stall 0
           4 +20 carry obstruction7:Kinematic3DCuboid pos [0.1434 0.2641 0.24  ] model [0.1434 0.2641 0.2994] a [ 0.  0.  0.  0. -0.  0.  0.  0. -0.  0.  0.] stall 0
           5 +30 above obstruction5:Kinematic3DCuboid pos [0.1585 0.1741 0.104 ] model [0.33  0.29  0.195] a [-0.      0.      0.      0.     -0.0519  0.      0.0533  0.     -0.1052
           6 +  0.      0.    ] stall 0
           7 +40 grasp obstruction5:Kinematic3DCuboid pos [0.1585 0.1741 0.104 ] model [0.1585 0.1741 0.172 ] a [ 0.      0.      0.      0.      0.0103 -0.     -0.0107  0.      0.0211
           8 + -0.     -1.    ] stall 0
           9 +50 lower obstruction5:Kinematic3DCuboid pos [0.135 0.    0.12 ] model [0.135 0.    0.188] a [ 0.     -0.      0.      0.      0.0448  0.     -0.0634  0.      0.1082
          10 +  0.      0.    ] stall 0
          11 +60 align obstruction4:Kinematic3DCuboid pos [0.1843 0.233  0.1022] model [0.1843 0.233  0.3   ] a [ 0.0112  0.053   0.      0.      0.      0.      0.      0.     -0.
          12 +  0.      0.    ] stall 0
          13 +70 lift obstruction4:Kinematic3DCuboid pos [0.1843 0.233  0.2222] model [0.1843 0.233  0.276 ] a [ 0.      0.      0.      0.     -0.0336  0.      0.0787  0.     -0.1123
          14 + -0.      0.    ] stall 0
          15 +80 release obstruction4:Kinematic3DCuboid pos [0.265  0.     0.0932] model [ 0.265 -0.     0.147] a [-0. -0.  0.  0.  0. -0.  0.  0.  0.  0.  0.] stall 0
          16 +90 grasp obstruction1:Kinematic3DCuboid pos [0.1031 0.209  0.101 ] model [0.1031 0.209  0.26  ] a [-0.      0.      0.      0.      0.0277  0.     -0.0868  0.      0.1145
          17 +  0.     -1.    ] stall 1
          18 +100 carry obstruction1:Kinematic3DCuboid pos [0.1031 0.209  0.24  ] model [0.1031 0.209  0.295 ] a [-0.  0.  0.  0.  0. -0. -0.  0. -0. -0.  0.] stall 0
          19 +110 above obstruction3:Kinematic3DCuboid pos [0.1466 0.221  0.0977] model [ 0.395 -0.     0.187] a [-0.      0.      0.      0.     -0.0536  0.      0.0508  0.     -0.1044
          20 +  0.      0.    ] stall 0
          21 +120 grasp obstruction3:Kinematic3DCuboid pos [0.1466 0.221  0.0977] model [0.1466 0.221  0.18  ] a [ 0.      0.      0.      0.      0.0466  0.     -0.0609  0.      0.1075
          22 + -0.     -1.    ] stall 0
          23 +130 carry obstruction3:Kinematic3DCuboid pos [0.3266 0.26   0.24  ] model [0.3266 0.26   0.2903] a [ 0.18   0.039  0.     0.    -0.    -0.     0.     0.     0.     0.
          24 +  0.   ] stall 1
          25 +140 above obstruction0:Kinematic3DCuboid pos [0.1034 0.248  0.0951] model [0.465 0.29  0.219] a [ 0.     -0.      0.      0.     -0.0468 -0.      0.0606  0.     -0.1074
          26 +  0.      0.    ] stall 0
          27 +150 grasp obstruction0:Kinematic3DCuboid pos [0.1034 0.248  0.0951] model [0.1034 0.248  0.18  ] a [ 0.      0.      0.      0.      0.0466  0.     -0.0609  0.      0.1075
          28 + -0.     -1.    ] stall 0
          29 +160 carry obstruction0:Kinematic3DCuboid pos [0.1034 0.248  0.24  ] model [0.1034 0.248  0.2849] a [ 0.  0.  0.  0.  0. -0. -0.  0.  0. -0.  0.] stall 0
          30 +170 release obstruction0:Kinematic3DCuboid pos [ 0.135  -0.15    0.0861] model [ 0.135 -0.15   0.131] a [-0.  0.  0.  0. -0.  0.  0.  0. -0. -0.  1.] stall 1
diff --git a/quick_results.txt b/quick_results.txt
index a33587f..603bb28 100644
--- a/quick_results.txt
+++ b/quick_results.txt
@@ -1,2 +1,5 @@
    1      1  {"seed": 0, "count": 2, "success": true, "steps": 86, "seconds": 12.06, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 1, "attempt": 0}
    2      2  {"seed": 1, "count": 1, "success": true, "steps": 58, "seconds": 11.32, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 1, "attempt": 0}
           3 +{"seed": 2, "count": 2, "success": true, "steps": 115, "seconds": 30.86, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 1, "attempt": 0}
           4 +{"seed": 3, "count": 2, "success": true, "steps": 54, "seconds": 7.43, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 1, "attempt": 0}
           5 +{"seed": 4, "count": 2, "success": true, "steps": 83, "seconds": 12.28, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 1, "attempt": 0}
diff --git a/test_sweep_extended.out b/test_sweep_extended.out
index 8bc1c92..8f7dd5f 100644
--- a/test_sweep_extended.out
+++ b/test_sweep_extended.out
@@ -5,3 +5,17 @@
    5      5  {"seed": 44, "count": 2, "success": true, "steps": 84, "sec": 4.0}
    6      6  {"seed": 45, "count": 2, "success": true, "steps": 157, "sec": 21.43}
    7      7  {"seed": 46, "count": 1, "success": true, "steps": 82, "sec": 10.57}
           8 +{"seed": 47, "count": 0, "success": true, "steps": 40, "sec": 8.17}
           9 +{"seed": 48, "count": 0, "success": true, "steps": 41, "sec": 3.35}
          10 +{"seed": 49, "count": 0, "success": true, "steps": 44, "sec": 5.54}
          11 +{"seed": 50, "count": 2, "success": true, "steps": 130, "sec": 16.06}
          12 +{"seed": 51, "count": 1, "success": true, "steps": 82, "sec": 10.43}
          13 +{"seed": 52, "count": 2, "success": true, "steps": 127, "sec": 10.47}
          14 +{"seed": 53, "count": 2, "success": true, "steps": 130, "sec": 8.23}
          15 +{"seed": 54, "count": 0, "success": true, "steps": 41, "sec": 2.71}
          16 +{"seed": 55, "count": 2, "success": true, "steps": 122, "sec": 10.54}
          17 +{"seed": 56, "count": 1, "success": true, "steps": 83, "sec": 5.43}
          18 +{"seed": 57, "count": 0, "success": true, "steps": 42, "sec": 1.23}
          19 +{"seed": 58, "count": 1, "success": true, "steps": 42, "sec": 5.51}
          20 +{"seed": 59, "count": 2, "success": true, "steps": 128, "sec": 9.12}
          21 +{"seed": 60, "count": 0, "success": true, "steps": 41, "sec": 2.96}
```

</details>

<a id="C039"></a>
### C039 · Add timed high-count stress test for the evaluation deadline

Commit `e42e2891a93f58f9a63eb3b5ec3e9665e13de0be`; parents: 7ba3e01ecc6eac6616294cdb0c39b42800026299. Recorded author date: 2026-09-20T03:02:17+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0141](01_timeline.md#E0141): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C039_e42e289.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/count_fast_results.txt b/count_fast_results.txt
index d30d21e..fddd9a6 100644
--- a/count_fast_results.txt
+++ b/count_fast_results.txt
@@ -1,3 +1,5 @@
    1      1  {"seed": 0, "count": 10, "success": true, "steps": 199, "seconds": 23.99, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 6, "todo": 7, "stall": 1, "attempt": 0, "pos": [0.14442715048789978, 0.23301441967487335, 0.11100000888109207], "dest": [0.14442715048789978, 0.23301441967487335, 0.11099999847263098]}
    2      2  {"seed": 1, "count": 10, "success": true, "steps": 186, "seconds": 22.3, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 6, "todo": 7, "stall": 1, "attempt": 0, "pos": [0.44773608446121216, -0.132277250289917, 0.11100002378225327], "dest": [0.44773608446121216, -0.132277250289917, 0.11099999847263098]}
    3      3  {"seed": 2, "count": 10, "success": true, "steps": 169, "seconds": 23.67, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 4, "todo": 5, "stall": 1, "attempt": 0, "pos": [0.15949538350105286, 0.0742836594581604, 0.11100000143051147], "dest": [0.15949532389640808, 0.0742836520075798, 0.11099999847263098]}
           4 +{"seed": 3, "count": 10, "success": true, "steps": 134, "seconds": 28.68, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 4, "todo": 5, "stall": 1, "attempt": 0, "pos": [0.3291561007499695, -0.3026953637599945, 0.11099997907876968], "dest": [0.3291561007499695, -0.3026953637599945, 0.11099999847263098]}
           5 +{"seed": 0, "count": 20, "success": true, "steps": 203, "seconds": 35.23, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "index": 6, "todo": 7, "stall": 1, "attempt": 0, "pos": [0.14442716538906097, 0.23301441967487335, 0.11100000143051147], "dest": [0.14442715048789978, 0.23301441967487335, 0.11099999847263098]}
diff --git a/test_one.py b/test_one.py
new file mode 100644
index 0000000..a16fcf3
--- /dev/null
+++ b/test_one.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import sys,time,json,numpy as np
           4 +seed=int(sys.argv[1]);count=int(sys.argv[2])
           5 +e=make_env();s,info=e.reset(seed=seed,options={'object_count':count});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info);start=time.monotonic();compute=0;term=False
           6 +for t in range(e.max_steps):
           7 + st=time.monotonic();a=p.get_action(s);compute+=time.monotonic()-st
           8 + s,r,term,trunc,info=e.step(a)
           9 + if t%50==0:print('progress',t,p.phase,str(p.obj),p.index,len(p.todo),p.stall,p.attempt,round(time.monotonic()-start,2),flush=True)
          10 + if term or trunc or time.monotonic()-start>58:break
          11 +print(json.dumps(dict(seed=seed,count=count,success=term,steps=t+1,seconds=round(time.monotonic()-start,2),compute=round(compute,3),phase=p.phase,obj=str(p.obj),stall=p.stall,attempt=p.attempt)),flush=True)
          12 +e.close()
diff --git a/test_sweep_current.out b/test_sweep_current.out
new file mode 100644
index 0000000..a11cb2c
--- /dev/null
+++ b/test_sweep_current.out
@@ -0,0 +1,11 @@
           1 +{"seed": 61, "count": 1, "success": true, "steps": 57, "sec": 4.76}
           2 +{"seed": 62, "count": 1, "success": true, "steps": 58, "sec": 2.8}
           3 +{"seed": 63, "count": 1, "success": true, "steps": 57, "sec": 3.81}
           4 +{"seed": 64, "count": 1, "success": true, "steps": 56, "sec": 7.64}
           5 +{"seed": 65, "count": 0, "success": true, "steps": 32, "sec": 2.8}
           6 +{"seed": 66, "count": 2, "success": true, "steps": 80, "sec": 6.37}
           7 +{"seed": 67, "count": 2, "success": true, "steps": 118, "sec": 12.0}
           8 +{"seed": 68, "count": 1, "success": true, "steps": 29, "sec": 6.04}
           9 +{"seed": 69, "count": 0, "success": true, "steps": 30, "sec": 1.56}
          10 +{"seed": 70, "count": 1, "success": true, "steps": 59, "sec": 4.24}
          11 +{"seed": 71, "count": 2, "success": true, "steps": 83, "sec": 5.49}
diff --git a/test_sweep_extended.out b/test_sweep_extended.out
index 8f7dd5f..c5058d9 100644
--- a/test_sweep_extended.out
+++ b/test_sweep_extended.out
@@ -19,3 +19,4 @@
   19     19  {"seed": 58, "count": 1, "success": true, "steps": 42, "sec": 5.51}
   20     20  {"seed": 59, "count": 2, "success": true, "steps": 128, "sec": 9.12}
   21     21  {"seed": 60, "count": 0, "success": true, "steps": 41, "sec": 2.96}
          22 +{"seed": 61, "count": 1, "success": true, "steps": 86, "sec": 7.81}
```

</details>

<a id="C040"></a>
### C040 · Advance completed motion phases without spending idle environment steps

Commit `0f72a2378935a11acf76220a9454eb66fc1f1451`; parents: e42e2891a93f58f9a63eb3b5ec3e9665e13de0be. Recorded author date: 2026-09-20T03:03:48+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0150](01_timeline.md#E0150): commit hash in recorded output.
[Controller after this commit](evidence/versions/C040_0f72a23_approach.py) · [Exact all-file diff](evidence/diffs/C040_0f72a23.diff)

[Previous saved controller snapshot](evidence/versions/C038_7ba3e01_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index afc47f7..f56f2e5 100644
--- a/approach.py
+++ b/approach.py
@@ -82,28 +82,33 @@ class GeneratedApproach:
   82     82              self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[self.index];self.destination=self.choose_destination(state);self.phase='above';bp=self.pos(state,self.obj)
   83     83          if held and self.phase=='lower' and not self.placing_goal and self.stall>=3:
   84     84              self.failed_places.append(self.destination[:2].copy());self.destination=self.choose_destination(state);self.phase='lift';self.lift_xy=bp[:2].copy();self.stall=0
   85        -        grip=0
   86        -        if self.phase=='above':dest=np.r_[model[:2],.30]
   87        -        elif self.phase=='align':dest=np.r_[bp[:2],.30]
   88        -        elif self.phase=='grasp':dest=bp+[0,0,.025];grip=-1
   89        -        elif self.phase=='lift':dest=np.r_[self.lift_xy,.24]
   90        -        elif self.phase=='carry':dest=np.r_[self.destination[:2],.24]
   91        -        elif self.phase=='lower':dest=self.destination.copy()
   92        -        else:dest=bp.copy();grip=1
   93        -        if held:dest=dest+model-bp
   94        -        if self.phase=='above':dest[2]=.30
   95        -        # Preserve a vertical wrist throughout travel and use the mobile base for XY.
   96        -        dz=np.clip(dest[2]-model[2],-.008 if self.phase=='grasp' and model[2]-bp[2]<.09 else -.04,.04)
   97        -        z=model[2]+dz
   98        -        key=round(float(z),7)
   99        -        if key not in self.cache:self.cache[key]=ik(.50,z)
  100        -        q=self.cache[key].copy()
  101        -        q[6]=qnow[6] if self.phase=='above' else self.wrist
  102        -        targetbase=dest[:2]-[.62,.001]
  103        -        delta=np.r_[targetbase-base,q-qnow]
  104        -        scale=max(1.,np.max(np.abs(delta))/.18)
  105        -        a=np.zeros(11,dtype=np.float32);a[:2]=delta[:2]/scale;a[3:10]=delta[2:]/scale;a[10]=grip
  106        -        error=np.max(np.abs(dest-model))
  107        -        if error<.0015 and np.max(abs(q-qnow))<.006:
  108        -            self.phase={'above':'align','align':'grasp','grasp':'grasp','lift':'carry','carry':'lower','lower':'release','release':'release'}[self.phase]
          85 +        for _ in range(4):
          86 +            grip=0
          87 +            if self.phase=='above':dest=np.r_[model[:2],.30]
          88 +            elif self.phase=='align':dest=np.r_[bp[:2],.30]
          89 +            elif self.phase=='grasp':dest=bp+[0,0,.025];grip=-1
          90 +            elif self.phase=='lift':dest=np.r_[self.lift_xy,.24]
          91 +            elif self.phase=='carry':dest=np.r_[self.destination[:2],.24]
          92 +            elif self.phase=='lower':dest=self.destination.copy()
          93 +            else:dest=bp.copy();grip=1
          94 +            if held:dest=dest+model-bp
          95 +            if self.phase=='above':dest[2]=.30
          96 +            # Preserve a vertical wrist throughout travel and use the mobile base for XY.
          97 +            dz=np.clip(dest[2]-model[2],-.008 if self.phase=='grasp' and model[2]-bp[2]<.09 else -.04,.04)
          98 +            z=model[2]+dz
          99 +            key=round(float(z),7)
         100 +            if key not in self.cache:self.cache[key]=ik(.50,z)
         101 +            q=self.cache[key].copy()
         102 +            q[6]=qnow[6] if self.phase=='above' else self.wrist
         103 +            targetbase=dest[:2]-[.62,.001]
         104 +            delta=np.r_[targetbase-base,q-qnow]
         105 +            scale=max(1.,np.max(np.abs(delta))/.18)
         106 +            a=np.zeros(11,dtype=np.float32);a[:2]=delta[:2]/scale;a[3:10]=delta[2:]/scale;a[10]=grip
         107 +            error=np.max(np.abs(dest-model))
         108 +            if error<.0015 and np.max(abs(q-qnow))<.006:
         109 +                next_phase={'above':'align','align':'grasp','grasp':'grasp','lift':'carry','carry':'lower','lower':'release','release':'release'}[self.phase]
         110 +                if next_phase!=self.phase:
         111 +                    self.phase=next_phase
         112 +                    continue
         113 +            return np.clip(a,self.action_space.low,self.action_space.high)
  109    114          return np.clip(a,self.action_space.low,self.action_space.high)
diff --git a/stress20.txt b/stress20.txt
new file mode 100644
index 0000000..e279836
--- /dev/null
+++ b/stress20.txt
@@ -0,0 +1,4 @@
           1 +progress 0 above obstruction13:Kinematic3DCuboid 0 9 0 0 0.1
           2 +progress 50 above obstruction13:Kinematic3DCuboid 0 9 0 3 13.58
           3 +progress 100 align obstruction13:Kinematic3DCuboid 0 9 0 5 25.09
           4 +progress 150 grasp obstruction13:Kinematic3DCuboid 0 9 2 7 33.85
diff --git a/test_sweep_current.out b/test_sweep_current.out
index a11cb2c..74da5f0 100644
--- a/test_sweep_current.out
+++ b/test_sweep_current.out
@@ -9,3 +9,15 @@
    9      9  {"seed": 69, "count": 0, "success": true, "steps": 30, "sec": 1.56}
   10     10  {"seed": 70, "count": 1, "success": true, "steps": 59, "sec": 4.24}
   11     11  {"seed": 71, "count": 2, "success": true, "steps": 83, "sec": 5.49}
          12 +{"seed": 72, "count": 2, "success": true, "steps": 83, "sec": 6.1}
          13 +{"seed": 73, "count": 2, "success": true, "steps": 87, "sec": 7.25}
          14 +{"seed": 74, "count": 0, "success": true, "steps": 30, "sec": 1.72}
          15 +{"seed": 75, "count": 1, "success": true, "steps": 54, "sec": 4.51}
          16 +{"seed": 76, "count": 1, "success": true, "steps": 62, "sec": 6.27}
          17 +{"seed": 77, "count": 0, "success": true, "steps": 29, "sec": 5.51}
          18 +{"seed": 78, "count": 2, "success": true, "steps": 55, "sec": 4.05}
          19 +{"seed": 79, "count": 0, "success": true, "steps": 29, "sec": 1.1}
          20 +{"seed": 80, "count": 2, "success": true, "steps": 80, "sec": 8.07}
          21 +{"seed": 81, "count": 0, "success": true, "steps": 30, "sec": 2.04}
          22 +{"seed": 82, "count": 2, "success": true, "steps": 81, "sec": 4.75}
          23 +{"seed": 83, "count": 2, "success": true, "steps": 55, "sec": 4.77}
```

</details>

<a id="C041"></a>
### C041 · Add geometry diagnostics for dense-scene grasp failures

Commit `5ec101088ae8c14546dfbb7188934287d0f55cc8`; parents: 0f72a2378935a11acf76220a9454eb66fc1f1451. Recorded author date: 2026-09-20T03:04:05+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0155](01_timeline.md#E0155): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C041_5ec1010.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dense.py b/probe_dense.py
new file mode 100644
index 0000000..137881b
--- /dev/null
+++ b/probe_dense.py
@@ -0,0 +1,6 @@
           1 +from env_client import make_env
           2 +import sys,numpy as np
           3 +E=make_env();s,i=E.reset(seed=int(sys.argv[1]),options={'object_count':int(sys.argv[2])});o=s.get_object_from_name(sys.argv[3]);pos=lambda o:np.array([s.get(o,'pose_'+f) for f in 'xyz']);p=pos(o)
           4 +for x in sorted(s.get_objects(E.observation_space.get_type('Kinematic3DCuboid')),key=lambda x:np.linalg.norm(pos(x)-p)):
           5 + print(x,pos(x).round(4),[round(s.get(x,'half_extent_'+f),4) for f in 'xyz'])
           6 +E.close()
diff --git a/stress20.txt b/stress20.txt
index e279836..07000e0 100644
--- a/stress20.txt
+++ b/stress20.txt
@@ -2,3 +2,6 @@ progress 0 above obstruction13:Kinematic3DCuboid 0 9 0 0 0.1
    2      2  progress 50 above obstruction13:Kinematic3DCuboid 0 9 0 3 13.58
    3      3  progress 100 align obstruction13:Kinematic3DCuboid 0 9 0 5 25.09
    4      4  progress 150 grasp obstruction13:Kinematic3DCuboid 0 9 2 7 33.85
           5 +progress 200 align obstruction13:Kinematic3DCuboid 0 9 0 10 48.74
           6 +progress 250 grasp obstruction13:Kinematic3DCuboid 0 9 0 12 54.08
           7 +{"seed": 1, "count": 20, "success": false, "steps": 274, "seconds": 58.17, "compute": 0.208, "phase": "grasp", "obj": "obstruction13:Kinematic3DCuboid", "stall": 2, "attempt": 13}
diff --git a/test_sweep_current.out b/test_sweep_current.out
index 74da5f0..b29cf81 100644
--- a/test_sweep_current.out
+++ b/test_sweep_current.out
@@ -21,3 +21,6 @@
   21     21  {"seed": 81, "count": 0, "success": true, "steps": 30, "sec": 2.04}
   22     22  {"seed": 82, "count": 2, "success": true, "steps": 81, "sec": 4.75}
   23     23  {"seed": 83, "count": 2, "success": true, "steps": 55, "sec": 4.77}
          24 +{"seed": 84, "count": 1, "success": true, "steps": 54, "sec": 5.1}
          25 +{"seed": 85, "count": 2, "success": true, "steps": 80, "sec": 6.64}
          26 +{"seed": 86, "count": 2, "success": true, "steps": 83, "sec": 3.66}
```

</details>

<a id="C042"></a>
### C042 · Clear accessible neighbors before retrying densely surrounded blocks

Commit `7026fffc7d3ce48e99b1d9051865b8b65723b016`; parents: 5ec101088ae8c14546dfbb7188934287d0f55cc8. Recorded author date: 2026-09-20T03:05:17+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0159](01_timeline.md#E0159): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C042_7026fff_approach.py) · [Exact all-file diff](evidence/diffs/C042_7026fff.diff)

[Previous saved controller snapshot](evidence/versions/C040_0f72a23_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f56f2e5..90147c6 100644
--- a/approach.py
+++ b/approach.py
@@ -19,7 +19,7 @@ class GeneratedApproach:
   19     19          obs=[o for o in self.objects if o not in [self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-rp[:2]) < self.size(state,o)[:2]+rs[:2]+.012)]
   20     20          obs.sort(key=lambda o:-self.pos(state,o)[2])
   21     21          self.todo=obs+[self.block];self.index=0;self.phase='above';self.t=0;self.stall=0;self.last=None
   22        -        self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
          22 +        self.attempts={};self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
   23     23      def choose_destination(self,state):
   24     24          self.placing_goal=self.obj==self.block and not any(o!=self.block for o in self.todo[self.index+1:])
   25     25          if self.placing_goal:
@@ -66,7 +66,19 @@ class GeneratedApproach:
   66     66          else:self.stall=0
   67     67          self.last=signature
   68     68          if not held and self.phase=='grasp' and self.stall>=3:
   69        -            self.attempt+=1;self.wrist=[np.pi/2,0,np.pi/4,-np.pi/4][self.attempt%4];self.phase='above';self.stall=0
          69 +            self.attempt+=1;self.attempts[self.obj]=self.attempt
          70 +            if self.attempt%2==0:
          71 +                pending=[o for o in self.todo[self.index:] if o not in [self.obj,self.block]]
          72 +                if not pending:
          73 +                    pending=[o for o in self.objects if o not in [self.obj,self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-bp[:2])<.095)]
          74 +                    pending.sort(key=lambda o:-self.pos(state,o)[2])
          75 +                if pending:
          76 +                    postponed=[] if self.obj==self.block else [self.obj]
          77 +                    self.todo=self.todo[:self.index]+pending+postponed+[self.block]
          78 +                    self.obj=self.todo[self.index];bp=self.pos(state,self.obj)
          79 +                    self.attempt=self.attempts.get(self.obj,0);self.failed_places=[]
          80 +                    self.destination=self.choose_destination(state)
          81 +            self.wrist=[np.pi/2,0,np.pi/4,-np.pi/4][self.attempt%4];self.phase='above';self.stall=0
   70     82          if held and self.phase in ['above','align','grasp']:
   71     83              grabbed=[o for o in self.objects if state.get(o,'grasp_active')>0]
   72     84              if grabbed and grabbed[0]!=self.obj:
diff --git a/test_sweep_current.out b/test_sweep_current.out
index b29cf81..4ec1abc 100644
--- a/test_sweep_current.out
+++ b/test_sweep_current.out
@@ -24,3 +24,6 @@
   24     24  {"seed": 84, "count": 1, "success": true, "steps": 54, "sec": 5.1}
   25     25  {"seed": 85, "count": 2, "success": true, "steps": 80, "sec": 6.64}
   26     26  {"seed": 86, "count": 2, "success": true, "steps": 83, "sec": 3.66}
          27 +{"seed": 87, "count": 1, "success": true, "steps": 54, "sec": 3.8}
          28 +{"seed": 88, "count": 1, "success": true, "steps": 55, "sec": 0.9}
          29 +{"seed": 89, "count": 2, "success": true, "steps": 78, "sec": 1.52}
```

</details>

<a id="C043"></a>
### C043 · Probe collision escape actions after dense-scene disposal

Commit `ae33aac708924aac7fbe968ac8d36f5537a6f1ff`; parents: 7026fffc7d3ce48e99b1d9051865b8b65723b016. Recorded author date: 2026-09-20T03:07:59+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C043_ae33aac.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/dense_agent_0_50.out b/dense_agent_0_50.out
new file mode 100644
index 0000000..4914f39
--- /dev/null
+++ b/dense_agent_0_50.out
@@ -0,0 +1,21 @@
           1 +progress 0 above obstruction7:Kinematic3DCuboid 0 7 0 0 0.27
           2 +progress 50 above obstruction4:Kinematic3DCuboid 2 7 0 0 19.55
           3 +progress 100 grasp obstruction1:Kinematic3DCuboid 3 7 0 1 26.56
           4 +progress 150 above obstruction0:Kinematic3DCuboid 5 7 5 0 28.65
           5 +progress 200 above obstruction0:Kinematic3DCuboid 5 7 55 0 29.03
           6 +progress 250 above obstruction0:Kinematic3DCuboid 5 7 105 0 29.36
           7 +progress 300 above obstruction0:Kinematic3DCuboid 5 7 155 0 29.68
           8 +progress 350 above obstruction0:Kinematic3DCuboid 5 7 205 0 29.99
           9 +progress 400 above obstruction0:Kinematic3DCuboid 5 7 255 0 30.3
          10 +progress 450 above obstruction0:Kinematic3DCuboid 5 7 305 0 30.6
          11 +progress 500 above obstruction0:Kinematic3DCuboid 5 7 355 0 30.86
          12 +progress 550 above obstruction0:Kinematic3DCuboid 5 7 405 0 31.18
          13 +progress 600 above obstruction0:Kinematic3DCuboid 5 7 455 0 31.51
          14 +progress 650 above obstruction0:Kinematic3DCuboid 5 7 505 0 31.79
          15 +progress 700 above obstruction0:Kinematic3DCuboid 5 7 555 0 32.07
          16 +progress 750 above obstruction0:Kinematic3DCuboid 5 7 605 0 32.3
          17 +progress 800 above obstruction0:Kinematic3DCuboid 5 7 655 0 32.52
          18 +progress 850 above obstruction0:Kinematic3DCuboid 5 7 705 0 32.76
          19 +progress 900 above obstruction0:Kinematic3DCuboid 5 7 755 0 32.99
          20 +progress 950 above obstruction0:Kinematic3DCuboid 5 7 805 0 33.26
          21 +{"seed": 0, "count": 50, "success": false, "steps": 1000, "seconds": 33.55, "compute": 0.796, "phase": "above", "obj": "obstruction0:Kinematic3DCuboid", "stall": 854, "attempt": 0}
diff --git a/dense_agent_2_20.out b/dense_agent_2_20.out
new file mode 100644
index 0000000..eaf8162
--- /dev/null
+++ b/dense_agent_2_20.out
@@ -0,0 +1,4 @@
           1 +progress 0 above obstruction8:Kinematic3DCuboid 0 5 0 0 0.12
           2 +progress 50 grasp obstruction1:Kinematic3DCuboid 1 5 0 1 3.52
           3 +progress 100 align obstruction2:Kinematic3DCuboid 3 5 0 0 5.24
           4 +{"seed": 2, "count": 20, "success": true, "steps": 143, "seconds": 6.41, "compute": 0.127, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
diff --git a/dense_agent_3_20.out b/dense_agent_3_20.out
new file mode 100644
index 0000000..322ab55
--- /dev/null
+++ b/dense_agent_3_20.out
@@ -0,0 +1,4 @@
           1 +progress 0 above obstruction1:Kinematic3DCuboid 0 5 0 0 0.05
           2 +progress 50 grasp obstruction5:Kinematic3DCuboid 2 5 0 0 1.94
           3 +progress 100 align target_block:Kinematic3DCuboid 4 5 0 0 3.71
           4 +{"seed": 3, "count": 20, "success": true, "steps": 119, "seconds": 4.25, "compute": 0.203, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
diff --git a/final_regression.txt b/final_regression.txt
new file mode 100644
index 0000000..41092b1
--- /dev/null
+++ b/final_regression.txt
@@ -0,0 +1,5 @@
           1 +{"seed": 2, "count": 2, "success": true, "steps": 98, "seconds": 2.09, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           2 +{"seed": 8, "count": 2, "success": true, "steps": 68, "seconds": 14.65, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           3 +{"seed": 9, "count": 1, "success": true, "steps": 46, "seconds": 4.15, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           4 +{"seed": 10, "count": 2, "success": true, "steps": 46, "seconds": 5.23, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           5 +{"seed": 11, "count": 0, "success": true, "steps": 24, "seconds": 2.1, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
diff --git a/probe_escape_dense.py b/probe_escape_dense.py
new file mode 100644
index 0000000..4173e00
--- /dev/null
+++ b/probe_escape_dense.py
@@ -0,0 +1,30 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +from kin import fk,ik
           4 +import numpy as np,time
           5 +E=make_env();s,info=E.reset(seed=0,options={'object_count':50});p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info);r=p.robot;fs=['joint_'+str(i) for i in range(1,8)]
           6 +def signature(s):return np.array([s.get(r,f) for f in ['pos_base_x','pos_base_y']+fs])
           7 +for t in range(1000):
           8 + a=p.get_action(s)
           9 + if p.phase=='above' and p.stall>=3:break
          10 + s,rw,done,tr,info=E.step(a)
          11 + if done:print('EARLYSUCCESS');raise SystemExit
          12 +v=signature(s);m,rot=fk(v[2:]);m+=np.r_[v[:2]+[.12,0],0]
          13 +print('STALLED',t,'obj',p.obj.name,'model',m.tolist(),'signature',v.tolist(),flush=True)
          14 +for o in p.objects:
          15 + if np.linalg.norm(p.pos(s,o)[:2]-m[:2])<.12:print('NEAR',o.name,p.pos(s,o).tolist(),p.size(s,o).tolist(),flush=True)
          16 +trials=[]
          17 +for dz in [.1,.2,.04,.01,.005]:
          18 + for dx,dy in [(0,0),(-.05,0),(0,-.05),(0,.05),(.05,0)]:
          19 +  q=ik(.5,m[2]+dz);q[6]=v[-1];a=np.zeros(11,dtype=np.float32);a[0]=dx;a[1]=dy;a[3:10]=q-v[2:];a[:10]/=max(1,np.max(np.abs(a[:10]))/.2);trials.append((str((dz,dx,dy)),a))
          20 +for da in [-.2,.2]:
          21 + q=ik(.5,m[2]+.1);q[6]=v[-1]+da;a=np.zeros(11,dtype=np.float32);a[3:10]=q-v[2:];a[:10]/=max(1,np.max(np.abs(a[:10]))/.2);trials.append(('rotate'+str(da),a))
          22 +for label,a in trials:
          23 + s,rw,done,tr,info=E.step(a);accepted=np.max(abs(signature(s)-v))>1e-6;print('ESCAPE',label,'accepted',accepted,'action',a.tolist(),flush=True)
          24 + if accepted:break
          25 +for k in range(1000-t):
          26 + s,rw,done,tr,info=E.step(p.get_action(s))
          27 + if done or tr:break
          28 + if p.stall>10:break
          29 +print('RESULT',done,'steps',t+k+1,'phase',p.phase,'obj',p.obj.name,'stall',p.stall,flush=True)
          30 +E.close()
diff --git a/stress20_reordered.txt b/stress20_reordered.txt
new file mode 100644
index 0000000..cb1d8fd
--- /dev/null
+++ b/stress20_reordered.txt
@@ -0,0 +1,7 @@
           1 +progress 0 above obstruction13:Kinematic3DCuboid 0 9 0 0 0.05
           2 +progress 50 lower obstruction3:Kinematic3DCuboid 0 9 0 0 2.63
           3 +progress 100 align obstruction4:Kinematic3DCuboid 2 9 0 0 4.53
           4 +progress 150 grasp obstruction18:Kinematic3DCuboid 3 9 1 1 6.11
           5 +progress 200 lower obstruction1:Kinematic3DCuboid 4 9 0 0 7.72
           6 +progress 250 release obstruction13:Kinematic3DCuboid 6 9 0 0 9.3
           7 +{"seed": 1, "count": 20, "success": true, "steps": 298, "seconds": 16.82, "compute": 0.431, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
```

</details>

<a id="C044"></a>
### C044 · Use NumPy-only kinematics and preserve dense-scene validation logs

Commit `95c2eaa64869fcba6174081c7b2c36761c6d9ede`; parents: ae33aac708924aac7fbe968ac8d36f5537a6f1ff. Recorded author date: 2026-09-20T03:08:02+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

- [E0178](01_timeline.md#E0178): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C044_95c2eaa.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/kin.py b/kin.py
index b5be755..f8d95ad 100644
--- a/kin.py
+++ b/kin.py
@@ -1,7 +1,6 @@
    1      1  import numpy as np
    2        -from scipy.spatial.transform import Rotation
    3      2  ORIGINS=[([0,0,.15643],np.pi),([0,.005375,-.12838],np.pi/2),([0,-.21038,-.006375],-np.pi/2),([0,.006375,-.21038],np.pi/2),([0,-.20843,-.006375],-np.pi/2),([0,0,-.10593],np.pi/2),([0,-.10593,0],-np.pi/2)]
    4        -MATS=[Rotation.from_euler('x',a).as_matrix() for p,a in ORIGINS]
           3 +MATS=[np.array([[1.,0.,0.],[0.,np.cos(a),-np.sin(a)],[0.,np.sin(a),np.cos(a)]]) for p,a in ORIGINS]
    5      4  Q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
    6      5  def fk(q,d=.18):
    7      6   t=np.zeros(3);r=np.eye(3)
diff --git a/probe_escape_dense.out b/probe_escape_dense.out
new file mode 100644
index 0000000..e69de29
```

</details>

<a id="C045"></a>
### C045 · Test reclosing gripper to escape post-release collision

Commit `59bf82b13aa45e514fed9ac1e81842c805fdbf95`; parents: 95c2eaa64869fcba6174081c7b2c36761c6d9ede. Recorded author date: 2026-09-20T03:08:50+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C045_59bf82b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_escape_dense.out b/probe_escape_dense.out
index e69de29..c97b8ad 100644
--- a/probe_escape_dense.out
+++ b/probe_escape_dense.out
@@ -0,0 +1,34 @@
           1 +STALLED 148 obj obstruction0 model [0.11988448269304469, -0.22704699737253095, 0.13899999873564506] signature [-0.5001155138015747, -0.22804692387580872, 0.0, 0.6475113034248352, -3.141592502593994, -1.5943396091461182, 0.0, -0.8997417688369751, 1.5707963705062866]
           2 +NEAR obstruction17 [0.12675714492797852, -0.2796808183193207, 0.09376610070466995] [0.014055830426514149, 0.018691936507821083, 0.018766101449728012]
           3 +NEAR obstruction29 [0.1800907999277115, -0.1283237487077713, 0.09960343688726425] [0.013570431619882584, 0.012746535241603851, 0.02460344135761261]
           4 +NEAR obstruction3 [0.11988447606563568, -0.227046936750412, 0.08870194107294083] [0.016884466633200645, 0.013889214023947716, 0.012701930478215218]
           5 +NEAR obstruction41 [0.1450808346271515, -0.1250598132610321, 0.0914498046040535] [0.01841130293905735, 0.011880945414304733, 0.016449805349111557]
           6 +NEAR obstruction8 [0.16071473062038422, -0.3303195536136627, 0.10226240754127502] [0.013088573701679707, 0.012698368169367313, 0.027262404561042786]
           7 +ESCAPE (0.1, 0, 0) accepted False action [0.0, 0.0, 0.0, 0.0, -0.09172327816486359, -1.1351367135148394e-07, 0.10827674716711044, 0.0, -0.20000000298023224, 0.0, 0.0]
           8 +ESCAPE (0.1, -0.05, 0) accepted False action [-0.03758835420012474, 0.0, 0.0, 0.0, -0.09172327816486359, -1.1351367135148394e-07, 0.10827674716711044, 0.0, -0.20000000298023224, 0.0, 0.0]
           9 +ESCAPE (0.1, 0, -0.05) accepted False action [0.0, -0.03758835420012474, 0.0, 0.0, -0.09172327816486359, -1.1351367135148394e-07, 0.10827674716711044, 0.0, -0.20000000298023224, 0.0, 0.0]
          10 +ESCAPE (0.1, 0, 0.05) accepted False action [0.0, 0.03758835420012474, 0.0, 0.0, -0.09172327816486359, -1.1351367135148394e-07, 0.10827674716711044, 0.0, -0.20000000298023224, 0.0, 0.0]
          11 +ESCAPE (0.1, 0.05, 0) accepted False action [0.03758835420012474, 0.0, 0.0, 0.0, -0.09172327816486359, -1.1351367135148394e-07, 0.10827674716711044, 0.0, -0.20000000298023224, 0.0, 0.0]
          12 +ESCAPE (0.2, 0, 0) accepted False action [0.0, 0.0, 0.0, 0.0, -0.06666094809770584, -5.4420407735733534e-08, 0.1333390474319458, 0.0, -0.19999998807907104, 0.0, 0.0]
          13 +ESCAPE (0.2, -0.05, 0) accepted False action [-0.0180205050855875, 0.0, 0.0, 0.0, -0.06666094809770584, -5.4420407735733534e-08, 0.1333390474319458, 0.0, -0.19999998807907104, 0.0, 0.0]
          14 +ESCAPE (0.2, 0, -0.05) accepted False action [0.0, -0.0180205050855875, 0.0, 0.0, -0.06666094809770584, -5.4420407735733534e-08, 0.1333390474319458, 0.0, -0.19999998807907104, 0.0, 0.0]
          15 +ESCAPE (0.2, 0, 0.05) accepted False action [0.0, 0.0180205050855875, 0.0, 0.0, -0.06666094809770584, -5.4420407735733534e-08, 0.1333390474319458, 0.0, -0.19999998807907104, 0.0, 0.0]
          16 +ESCAPE (0.2, 0.05, 0) accepted False action [0.0180205050855875, 0.0, 0.0, 0.0, -0.06666094809770584, -5.4420407735733534e-08, 0.1333390474319458, 0.0, -0.19999998807907104, 0.0, 0.0]
          17 +ESCAPE (0.04, 0, 0) accepted False action [0.0, 0.0, 0.0, 0.0, -0.055185578763484955, -1.5099580252808664e-07, 0.048426855355501175, 0.0, -0.10361240804195404, 0.0, 0.0]
          18 +ESCAPE (0.04, -0.05, 0) accepted False action [-0.05000000074505806, 0.0, 0.0, 0.0, -0.055185578763484955, -1.5099580252808664e-07, 0.048426855355501175, 0.0, -0.10361240804195404, 0.0, 0.0]
          19 +ESCAPE (0.04, 0, -0.05) accepted False action [0.0, -0.05000000074505806, 0.0, 0.0, -0.055185578763484955, -1.5099580252808664e-07, 0.048426855355501175, 0.0, -0.10361240804195404, 0.0, 0.0]
          20 +ESCAPE (0.04, 0, 0.05) accepted False action [0.0, 0.05000000074505806, 0.0, 0.0, -0.055185578763484955, -1.5099580252808664e-07, 0.048426855355501175, 0.0, -0.10361240804195404, 0.0, 0.0]
          21 +ESCAPE (0.04, 0.05, 0) accepted False action [0.05000000074505806, 0.0, 0.0, 0.0, -0.055185578763484955, -1.5099580252808664e-07, 0.048426855355501175, 0.0, -0.10361240804195404, 0.0, 0.0]
          22 +ESCAPE (0.01, 0, 0) accepted False action [0.0, 0.0, 0.0, 0.0, -0.01454215683043003, -1.5099580252808664e-07, 0.010973319411277771, 0.0, -0.025515448302030563, 0.0, 0.0]
          23 +ESCAPE (0.01, -0.05, 0) accepted False action [-0.05000000074505806, 0.0, 0.0, 0.0, -0.01454215683043003, -1.5099580252808664e-07, 0.010973319411277771, 0.0, -0.025515448302030563, 0.0, 0.0]
          24 +ESCAPE (0.01, 0, -0.05) accepted False action [0.0, -0.05000000074505806, 0.0, 0.0, -0.01454215683043003, -1.5099580252808664e-07, 0.010973319411277771, 0.0, -0.025515448302030563, 0.0, 0.0]
          25 +ESCAPE (0.01, 0, 0.05) accepted False action [0.0, 0.05000000074505806, 0.0, 0.0, -0.01454215683043003, -1.5099580252808664e-07, 0.010973319411277771, 0.0, -0.025515448302030563, 0.0, 0.0]
          26 +ESCAPE (0.01, 0.05, 0) accepted False action [0.05000000074505806, 0.0, 0.0, 0.0, -0.01454215683043003, -1.5099580252808664e-07, 0.010973319411277771, 0.0, -0.025515448302030563, 0.0, 0.0]
          27 +ESCAPE (0.005, 0, 0) accepted False action [0.0, 0.0, 0.0, 0.0, -0.00733141228556633, -1.5099580252808664e-07, 0.005392406601458788, 0.0, -0.012723791413009167, 0.0, 0.0]
          28 +ESCAPE (0.005, -0.05, 0) accepted False action [-0.05000000074505806, 0.0, 0.0, 0.0, -0.00733141228556633, -1.5099580252808664e-07, 0.005392406601458788, 0.0, -0.012723791413009167, 0.0, 0.0]
          29 +ESCAPE (0.005, 0, -0.05) accepted False action [0.0, -0.05000000074505806, 0.0, 0.0, -0.00733141228556633, -1.5099580252808664e-07, 0.005392406601458788, 0.0, -0.012723791413009167, 0.0, 0.0]
          30 +ESCAPE (0.005, 0, 0.05) accepted False action [0.0, 0.05000000074505806, 0.0, 0.0, -0.00733141228556633, -1.5099580252808664e-07, 0.005392406601458788, 0.0, -0.012723791413009167, 0.0, 0.0]
          31 +ESCAPE (0.005, 0.05, 0) accepted False action [0.05000000074505806, 0.0, 0.0, 0.0, -0.00733141228556633, -1.5099580252808664e-07, 0.005392406601458788, 0.0, -0.012723791413009167, 0.0, 0.0]
          32 +ESCAPE rotate-0.2 accepted False action [0.0, 0.0, 0.0, 0.0, -0.09172327816486359, -1.1351367135148394e-07, 0.10827674716711044, 0.0, -0.20000000298023224, -0.15035341680049896, 0.0]
          33 +ESCAPE rotate0.2 accepted False action [0.0, 0.0, 0.0, 0.0, -0.09172327816486359, -1.1351367135148394e-07, 0.10827674716711044, 0.0, -0.20000000298023224, 0.15035341680049896, 0.0]
          34 +RESULT False steps 156 phase above obj obstruction0 stall 11
diff --git a/probe_escape_dense.py b/probe_escape_dense.py
index 4173e00..78330ef 100644
--- a/probe_escape_dense.py
+++ b/probe_escape_dense.py
@@ -13,15 +13,15 @@ v=signature(s);m,rot=fk(v[2:]);m+=np.r_[v[:2]+[.12,0],0]
   13     13  print('STALLED',t,'obj',p.obj.name,'model',m.tolist(),'signature',v.tolist(),flush=True)
   14     14  for o in p.objects:
   15     15   if np.linalg.norm(p.pos(s,o)[:2]-m[:2])<.12:print('NEAR',o.name,p.pos(s,o).tolist(),p.size(s,o).tolist(),flush=True)
   16        -trials=[]
   17        -for dz in [.1,.2,.04,.01,.005]:
   18        - for dx,dy in [(0,0),(-.05,0),(0,-.05),(0,.05),(.05,0)]:
   19        -  q=ik(.5,m[2]+dz);q[6]=v[-1];a=np.zeros(11,dtype=np.float32);a[0]=dx;a[1]=dy;a[3:10]=q-v[2:];a[:10]/=max(1,np.max(np.abs(a[:10]))/.2);trials.append((str((dz,dx,dy)),a))
   20        -for da in [-.2,.2]:
   21        - q=ik(.5,m[2]+.1);q[6]=v[-1]+da;a=np.zeros(11,dtype=np.float32);a[3:10]=q-v[2:];a[:10]/=max(1,np.max(np.abs(a[:10]))/.2);trials.append(('rotate'+str(da),a))
   22        -for label,a in trials:
   23        - s,rw,done,tr,info=E.step(a);accepted=np.max(abs(signature(s)-v))>1e-6;print('ESCAPE',label,'accepted',accepted,'action',a.tolist(),flush=True)
   24        - if accepted:break
          16 +a=np.zeros(11,dtype=np.float32);a[10]=-1;s,*_=E.step(a)
          17 +print('RECLOSE',s.get(r,'grasp_active'),[o.name for o in p.objects if s.get(o,'grasp_active')],flush=True)
          18 +if s.get(r,'grasp_active'):
          19 + p.failed_places.append(m[:2].copy())
          20 +for ztarget in [.18,.24,.3]:
          21 + q=ik(.5,ztarget);q[6]=v[-1]
          22 + for _ in range(4):
          23 +  a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-signature(s)[2:],-.2,.2);s,*_=E.step(a)
          24 + print('LIFT',ztarget,'model',fk(signature(s)[2:])[0].tolist(),flush=True)
   25     25  for k in range(1000-t):
   26     26   s,rw,done,tr,info=E.step(p.get_action(s))
   27     27   if done or tr:break
```

</details>

<a id="C046"></a>
### C046 · Recover trapped release poses by regrasping and relocating the deposited block

Commit `ad154b2d422ae6e9b6b25283300553bc60378727`; parents: 59bf82b13aa45e514fed9ac1e81842c805fdbf95. Recorded author date: 2026-09-20T03:09:25+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0183](01_timeline.md#E0183): commit hash in recorded output.
[Controller after this commit](evidence/versions/C046_ad154b2_approach.py) · [Exact all-file diff](evidence/diffs/C046_ad154b2.diff)

[Previous saved controller snapshot](evidence/versions/C042_7026fff_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 90147c6..5e85c01 100644
--- a/approach.py
+++ b/approach.py
@@ -19,7 +19,7 @@ class GeneratedApproach:
   19     19          obs=[o for o in self.objects if o not in [self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-rp[:2]) < self.size(state,o)[:2]+rs[:2]+.012)]
   20     20          obs.sort(key=lambda o:-self.pos(state,o)[2])
   21     21          self.todo=obs+[self.block];self.index=0;self.phase='above';self.t=0;self.stall=0;self.last=None
   22        -        self.attempts={};self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
          22 +        self.last_released=None;self.attempts={};self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
   23     23      def choose_destination(self,state):
   24     24          self.placing_goal=self.obj==self.block and not any(o!=self.block for o in self.todo[self.index+1:])
   25     25          if self.placing_goal:
@@ -89,9 +89,19 @@ class GeneratedApproach:
   89     89                  self.obj=actual;self.destination=self.choose_destination(state);bp=self.pos(state,self.obj)
   90     90              self.phase='lift';self.lift_xy=bp[:2].copy()
   91     91          if self.phase=='release' and not held:
          92 +            self.last_released=self.obj
   92     93              self.index+=1
   93     94              if self.index>=len(self.todo):self.index=len(self.todo)-1
   94     95              self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[self.index];self.destination=self.choose_destination(state);self.phase='above';bp=self.pos(state,self.obj)
          96 +        if not held and self.phase=='above' and self.stall>=3 and self.last_released is not None:
          97 +            released=self.last_released
          98 +            oldpos=self.pos(state,released)
          99 +            if np.linalg.norm(oldpos[:2]-model[:2])<.04:
         100 +                self.todo.insert(self.index,released);self.obj=released
         101 +                self.failed_places.append(oldpos[:2].copy());self.destination=self.choose_destination(state)
         102 +                self.phase='grasp';self.attempt=0;self.wrist=qnow[6];self.stall=0
         103 +                a=np.zeros(11,dtype=np.float32);a[10]=-1
         104 +                return a
   95    105          if held and self.phase=='lower' and not self.placing_goal and self.stall>=3:
   96    106              self.failed_places.append(self.destination[:2].copy());self.destination=self.choose_destination(state);self.phase='lift';self.lift_xy=bp[:2].copy();self.stall=0
   97    107          for _ in range(4):
diff --git a/probe_escape_reclose.out b/probe_escape_reclose.out
new file mode 100644
index 0000000..aba8e85
--- /dev/null
+++ b/probe_escape_reclose.out
@@ -0,0 +1,11 @@
           1 +STALLED 148 obj obstruction0 model [0.11988448269304469, -0.227046997372531, 0.13899999873564506] signature [-0.5001155138015747, -0.22804692387580872, 0.0, 0.6475113034248352, -3.141592502593994, -1.5943396091461182, 0.0, -0.8997417688369751, 1.5707963705062866]
           2 +NEAR obstruction17 [0.12675714492797852, -0.2796808183193207, 0.09376610070466995] [0.014055830426514149, 0.018691936507821083, 0.018766101449728012]
           3 +NEAR obstruction29 [0.1800907999277115, -0.1283237487077713, 0.09960343688726425] [0.013570431619882584, 0.012746535241603851, 0.02460344135761261]
           4 +NEAR obstruction3 [0.11988447606563568, -0.227046936750412, 0.08870194107294083] [0.016884466633200645, 0.013889214023947716, 0.012701930478215218]
           5 +NEAR obstruction41 [0.1450808346271515, -0.1250598132610321, 0.0914498046040535] [0.01841130293905735, 0.011880945414304733, 0.016449805349111557]
           6 +NEAR obstruction8 [0.16071473062038422, -0.3303195536136627, 0.10226240754127502] [0.013088573701679707, 0.012698368169367313, 0.027262404561042786]
           7 +RECLOSE 1.0 ['obstruction3']
           8 +LIFT 0.18 model [0.49999994522727714, 0.0010000414018106465, 0.17999997772391033]
           9 +LIFT 0.24 model [0.5000000160440505, 0.0009999312645461748, 0.24000001731711207]
          10 +LIFT 0.3 model [0.5000000169138609, 0.0010000381728343499, 0.30000002008895343]
          11 +RESULT True steps 266 phase release obj target_block stall 0
```

</details>

<a id="C047"></a>
### C047 · Remember rejected disposal sites across regrasp recovery attempts

Commit `60df503cf7cb73007f0af75d640b38b71ffa3463`; parents: ad154b2d422ae6e9b6b25283300553bc60378727. Recorded author date: 2026-09-20T03:09:57+02:00.

File roles (automatic): policy, setup/other.

- [E0188](01_timeline.md#E0188): commit hash in recorded output.
[Controller after this commit](evidence/versions/C047_60df503_approach.py) · [Exact all-file diff](evidence/diffs/C047_60df503.diff)

[Previous saved controller snapshot](evidence/versions/C046_ad154b2_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5e85c01..c81f023 100644
--- a/approach.py
+++ b/approach.py
@@ -19,8 +19,9 @@ class GeneratedApproach:
   19     19          obs=[o for o in self.objects if o not in [self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-rp[:2]) < self.size(state,o)[:2]+rs[:2]+.012)]
   20     20          obs.sort(key=lambda o:-self.pos(state,o)[2])
   21     21          self.todo=obs+[self.block];self.index=0;self.phase='above';self.t=0;self.stall=0;self.last=None
   22        -        self.last_released=None;self.attempts={};self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
          22 +        self.bad_places={};self.last_released=None;self.attempts={};self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
   23     23      def choose_destination(self,state):
          24 +        self.failed_places=self.bad_places.setdefault(self.obj,[])
   24     25          self.placing_goal=self.obj==self.block and not any(o!=self.block for o in self.todo[self.index+1:])
   25     26          if self.placing_goal:
   26     27              p=self.pos(state,self.region).copy();p[2]+=self.size(state,self.region)[2]+self.size(state,self.obj)[2]+.001
@@ -98,6 +99,7 @@ class GeneratedApproach:
   98     99              oldpos=self.pos(state,released)
   99    100              if np.linalg.norm(oldpos[:2]-model[:2])<.04:
  100    101                  self.todo.insert(self.index,released);self.obj=released
         102 +                self.failed_places=self.bad_places.setdefault(released,[])
  101    103                  self.failed_places.append(oldpos[:2].copy());self.destination=self.choose_destination(state)
  102    104                  self.phase='grasp';self.attempt=0;self.wrist=qnow[6];self.stall=0
  103    105                  a=np.zeros(11,dtype=np.float32);a[10]=-1
diff --git a/stress50_recovery.txt b/stress50_recovery.txt
new file mode 100644
index 0000000..a39f97b
--- /dev/null
+++ b/stress50_recovery.txt
@@ -0,0 +1,7 @@
           1 +progress 0 above obstruction7:Kinematic3DCuboid 0 7 0 0 0.09
           2 +progress 50 above obstruction4:Kinematic3DCuboid 2 7 0 0 2.75
           3 +progress 100 grasp obstruction1:Kinematic3DCuboid 3 7 0 1 5.13
           4 +progress 150 lift obstruction3:Kinematic3DCuboid 5 8 0 0 7.56
           5 +progress 200 grasp obstruction0:Kinematic3DCuboid 6 8 0 0 10.31
           6 +progress 250 align target_block:Kinematic3DCuboid 7 8 0 0 12.54
           7 +{"seed": 0, "count": 50, "success": true, "steps": 270, "seconds": 13.36, "compute": 0.664, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
```

</details>

<a id="C048"></a>
### C048 · Record final stress tests and diagnose dense held-object lift collision

Commit `3735a6da4433180be98a69a52e511df06c04aed9`; parents: 60df503cf7cb73007f0af75d640b38b71ffa3463. Recorded author date: 2026-09-20T03:12:24+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0199](01_timeline.md#E0199): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C048_3735a6d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/final_regression.txt b/final_regression.txt
index 41092b1..b7362c4 100644
--- a/final_regression.txt
+++ b/final_regression.txt
@@ -1,5 +1,10 @@
    1        -{"seed": 2, "count": 2, "success": true, "steps": 98, "seconds": 2.09, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
    2        -{"seed": 8, "count": 2, "success": true, "steps": 68, "seconds": 14.65, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
    3        -{"seed": 9, "count": 1, "success": true, "steps": 46, "seconds": 4.15, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
    4        -{"seed": 10, "count": 2, "success": true, "steps": 46, "seconds": 5.23, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
    5        -{"seed": 11, "count": 0, "success": true, "steps": 24, "seconds": 2.1, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           1 +{"seed": 2, "count": 2, "success": true, "steps": 98, "seconds": 2.57, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           2 +{"seed": 8, "count": 2, "success": true, "steps": 68, "seconds": 1.7, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           3 +{"seed": 9, "count": 1, "success": true, "steps": 46, "seconds": 0.95, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           4 +{"seed": 10, "count": 2, "success": true, "steps": 46, "seconds": 1.16, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           5 +{"seed": 11, "count": 0, "success": true, "steps": 24, "seconds": 0.59, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           6 +{"seed": 12, "count": 1, "success": true, "steps": 43, "seconds": 1.05, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           7 +{"seed": 13, "count": 2, "success": true, "steps": 63, "seconds": 1.51, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           8 +{"seed": 14, "count": 0, "success": true, "steps": 24, "seconds": 0.48, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           9 +{"seed": 45, "count": 2, "success": true, "steps": 93, "seconds": 2.56, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
          10 +{"seed": 67, "count": 2, "success": true, "steps": 101, "seconds": 2.63, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
diff --git a/probe_lift.py b/probe_lift.py
new file mode 100644
index 0000000..348a815
--- /dev/null
+++ b/probe_lift.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +from kin import ik,fk
           4 +import numpy as np
           5 +E=make_env();s,i=E.reset(seed=2,options={'object_count':50});p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,i);r=p.robot
           6 +qs=lambda s:np.array([s.get(r,'joint_'+str(j)) for j in range(1,8)])
           7 +for t in range(200):
           8 + s,_,te,_,_=E.step(p.get_action(s))
           9 + if p.stall>=3 and p.phase=='lift':break
          10 +q=qs(s);m,_=fk(q);base=np.array([s.get(r,'pos_base_x'),s.get(r,'pos_base_y')]);print('STUCK',t,p.obj,p.pos(s,p.obj),'q',q,'model',m,'base',base,'wrist',p.wrist,flush=True)
          11 +for dz,dx,dy in [(v,0,0) for v in [.005,.01,.08,.12,.2]]+[(.1,dx,dy) for dx,dy in [(-.02,0),(.02,0),(0,-.02),(0,.02),(-.05,0),(0,-.05),(0,.05)]]:
          12 + q=qs(s);m,_=fk(q);goal=ik(.5,m[2]+dz);goal[6]=q[6];d=goal-q;scale=max(1,np.max(abs(d))/.2);a=np.zeros(11);a[3:10]=d/scale;a[0]=dx;a[1]=dy
          13 + s,_,te,_,_=E.step(a);change=np.max(abs(qs(s)-q));print('TRY',dz,dx,dy,'CHANGE',change,flush=True)
          14 + if change>1e-6:
          15 +  for k in range(500):
          16 +   s,_,te,_,_=E.step(p.get_action(s))
          17 +   if te:break
          18 +  print('END',te,k,p.phase,p.obj,p.stall,flush=True);break
          19 +E.close()
diff --git a/stress50_seed1.txt b/stress50_seed1.txt
new file mode 100644
index 0000000..2178a7c
--- /dev/null
+++ b/stress50_seed1.txt
@@ -0,0 +1,12 @@
           1 +progress 0 above obstruction13:Kinematic3DCuboid 0 9 0 0 0.07
           2 +progress 50 carry obstruction3:Kinematic3DCuboid 0 9 0 0 3.08
           3 +progress 100 above obstruction4:Kinematic3DCuboid 2 9 0 0 5.47
           4 +progress 150 grasp obstruction18:Kinematic3DCuboid 3 9 0 1 7.97
           5 +progress 200 grasp obstruction1:Kinematic3DCuboid 4 9 0 0 10.27
           6 +progress 250 lift obstruction7:Kinematic3DCuboid 5 9 0 0 12.66
           7 +progress 300 lift obstruction7:Kinematic3DCuboid 5 9 0 0 15.18
           8 +progress 350 lift obstruction7:Kinematic3DCuboid 6 10 0 0 17.69
           9 +progress 400 lower obstruction18:Kinematic3DCuboid 8 10 0 0 20.36
          10 +progress 450 lower obstruction18:Kinematic3DCuboid 8 10 0 0 23.12
          11 +progress 500 release target_block:Kinematic3DCuboid 9 10 0 0 25.35
          12 +{"seed": 1, "count": 50, "success": true, "steps": 501, "seconds": 25.35, "compute": 1.876, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
diff --git a/stress50_seed2.txt b/stress50_seed2.txt
new file mode 100644
index 0000000..6b349c2
--- /dev/null
+++ b/stress50_seed2.txt
@@ -0,0 +1,21 @@
           1 +progress 0 above obstruction43:Kinematic3DCuboid 0 7 0 0 0.07
           2 +progress 50 lift obstruction43:Kinematic3DCuboid 0 7 20 1 1.79
           3 +progress 100 lift obstruction43:Kinematic3DCuboid 0 7 70 1 2.21
           4 +progress 150 lift obstruction43:Kinematic3DCuboid 0 7 120 1 2.63
           5 +progress 200 lift obstruction43:Kinematic3DCuboid 0 7 170 1 3.06
           6 +progress 250 lift obstruction43:Kinematic3DCuboid 0 7 220 1 3.5
           7 +progress 300 lift obstruction43:Kinematic3DCuboid 0 7 270 1 3.9
           8 +progress 350 lift obstruction43:Kinematic3DCuboid 0 7 320 1 4.25
           9 +progress 400 lift obstruction43:Kinematic3DCuboid 0 7 370 1 4.7
          10 +progress 450 lift obstruction43:Kinematic3DCuboid 0 7 420 1 5.18
          11 +progress 500 lift obstruction43:Kinematic3DCuboid 0 7 470 1 5.68
          12 +progress 550 lift obstruction43:Kinematic3DCuboid 0 7 520 1 6.19
          13 +progress 600 lift obstruction43:Kinematic3DCuboid 0 7 570 1 6.62
          14 +progress 650 lift obstruction43:Kinematic3DCuboid 0 7 620 1 6.97
          15 +progress 700 lift obstruction43:Kinematic3DCuboid 0 7 670 1 7.32
          16 +progress 750 lift obstruction43:Kinematic3DCuboid 0 7 720 1 7.69
          17 +progress 800 lift obstruction43:Kinematic3DCuboid 0 7 770 1 8.04
          18 +progress 850 lift obstruction43:Kinematic3DCuboid 0 7 820 1 8.41
          19 +progress 900 lift obstruction43:Kinematic3DCuboid 0 7 870 1 8.79
          20 +progress 950 lift obstruction43:Kinematic3DCuboid 0 7 920 1 9.18
          21 +{"seed": 2, "count": 50, "success": false, "steps": 1000, "seconds": 9.56, "compute": 0.471, "phase": "lift", "obj": "obstruction43:Kinematic3DCuboid", "stall": 969, "attempt": 1}
```

</details>

<a id="C049"></a>
### C049 · Use finer vertical lift steps when dense neighboring objects block a grasped block

Commit `adb0df538ebe7260bc8d9ca90708408e837da354`; parents: 3735a6da4433180be98a69a52e511df06c04aed9. Recorded author date: 2026-09-20T03:13:19+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0203](01_timeline.md#E0203): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C049_adb0df5_approach.py) · [Exact all-file diff](evidence/diffs/C049_adb0df5.diff)

[Previous saved controller snapshot](evidence/versions/C047_60df503_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c81f023..7433fff 100644
--- a/approach.py
+++ b/approach.py
@@ -19,7 +19,7 @@ class GeneratedApproach:
   19     19          obs=[o for o in self.objects if o not in [self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-rp[:2]) < self.size(state,o)[:2]+rs[:2]+.012)]
   20     20          obs.sort(key=lambda o:-self.pos(state,o)[2])
   21     21          self.todo=obs+[self.block];self.index=0;self.phase='above';self.t=0;self.stall=0;self.last=None
   22        -        self.bad_places={};self.last_released=None;self.attempts={};self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
          22 +        self.lift_step=.04;self.bad_places={};self.last_released=None;self.attempts={};self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
   23     23      def choose_destination(self,state):
   24     24          self.failed_places=self.bad_places.setdefault(self.obj,[])
   25     25          self.placing_goal=self.obj==self.block and not any(o!=self.block for o in self.todo[self.index+1:])
@@ -88,7 +88,7 @@ class GeneratedApproach:
   88     88                  self.todo.insert(self.index,actual)
   89     89                  if actual==self.block and any(o!=self.block for o in self.todo[self.index+1:]):self.todo.append(self.block)
   90     90                  self.obj=actual;self.destination=self.choose_destination(state);bp=self.pos(state,self.obj)
   91        -            self.phase='lift';self.lift_xy=bp[:2].copy()
          91 +            self.phase='lift';self.lift_xy=bp[:2].copy();self.lift_step=.04
   92     92          if self.phase=='release' and not held:
   93     93              self.last_released=self.obj
   94     94              self.index+=1
@@ -106,6 +106,8 @@ class GeneratedApproach:
  106    106                  return a
  107    107          if held and self.phase=='lower' and not self.placing_goal and self.stall>=3:
  108    108              self.failed_places.append(self.destination[:2].copy());self.destination=self.choose_destination(state);self.phase='lift';self.lift_xy=bp[:2].copy();self.stall=0
         109 +        if held and self.phase=='lift' and self.stall>=2:
         110 +            self.lift_step=max(.001,self.lift_step/4)
  109    111          for _ in range(4):
  110    112              grip=0
  111    113              if self.phase=='above':dest=np.r_[model[:2],.30]
@@ -118,7 +120,7 @@ class GeneratedApproach:
  118    120              if held:dest=dest+model-bp
  119    121              if self.phase=='above':dest[2]=.30
  120    122              # Preserve a vertical wrist throughout travel and use the mobile base for XY.
  121        -            dz=np.clip(dest[2]-model[2],-.008 if self.phase=='grasp' and model[2]-bp[2]<.09 else -.04,.04)
         123 +            dz=np.clip(dest[2]-model[2],-.008 if self.phase=='grasp' and model[2]-bp[2]<.09 else -.04,self.lift_step if self.phase=='lift' else .04)
  122    124              z=model[2]+dz
  123    125              key=round(float(z),7)
  124    126              if key not in self.cache:self.cache[key]=ik(.50,z)
diff --git a/probe_lift.out b/probe_lift.out
new file mode 100644
index 0000000..0cb65a0
--- /dev/null
+++ b/probe_lift.out
@@ -0,0 +1,4 @@
           1 +STUCK 33 obstruction43:Kinematic3DCuboid [0.17988294 0.10726094 0.10831118] q [ 0.          0.60139829 -3.14159274 -1.55526185  0.         -0.98493248
           2 +  0.        ] model [0.50000001 0.00100004 0.17199994] base [-0.44011706  0.10626096] wrist 0
           3 +TRY 0.005 0 0 CHANGE 0.01314634084701538
           4 +END False 499 lift obstruction43:Kinematic3DCuboid 499
```

</details>

<a id="C050"></a>
### C050 · Save final successful regression and 50-obstruction validation results

Commit `e4d97eadb34486947fe47c881f8fd564d20aab17`; parents: adb0df538ebe7260bc8d9ca90708408e837da354. Recorded author date: 2026-09-20T03:15:28+02:00.

File roles (automatic): setup/other.

- [E0214](01_timeline.md#E0214): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C050_e4d97ea.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/final_dense20.txt b/final_dense20.txt
new file mode 100644
index 0000000..dfce510
--- /dev/null
+++ b/final_dense20.txt
@@ -0,0 +1,7 @@
           1 +progress 0 above obstruction13:Kinematic3DCuboid 0 9 0 0 0.04
           2 +progress 50 lower obstruction3:Kinematic3DCuboid 0 9 0 0 2.02
           3 +progress 100 align obstruction4:Kinematic3DCuboid 2 9 0 0 3.45
           4 +progress 150 grasp obstruction18:Kinematic3DCuboid 3 9 1 1 4.88
           5 +progress 200 lower obstruction1:Kinematic3DCuboid 4 9 0 0 6.38
           6 +progress 250 release obstruction13:Kinematic3DCuboid 6 9 0 0 7.95
           7 +{"seed": 1, "count": 20, "success": true, "steps": 298, "seconds": 9.28, "compute": 0.227, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
diff --git a/final_dense50.txt b/final_dense50.txt
new file mode 100644
index 0000000..facfb12
--- /dev/null
+++ b/final_dense50.txt
@@ -0,0 +1,7 @@
           1 +progress 0 above obstruction7:Kinematic3DCuboid 0 7 0 0 0.07
           2 +progress 50 above obstruction4:Kinematic3DCuboid 2 7 0 0 2.44
           3 +progress 100 grasp obstruction1:Kinematic3DCuboid 3 7 0 1 4.51
           4 +progress 150 lift obstruction3:Kinematic3DCuboid 5 8 0 0 6.78
           5 +progress 200 grasp obstruction0:Kinematic3DCuboid 6 8 0 0 9.3
           6 +progress 250 align target_block:Kinematic3DCuboid 7 8 0 0 11.5
           7 +{"seed": 0, "count": 50, "success": true, "steps": 270, "seconds": 12.28, "compute": 0.755, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
diff --git a/final_targeted.txt b/final_targeted.txt
new file mode 100644
index 0000000..2f7c2f7
--- /dev/null
+++ b/final_targeted.txt
@@ -0,0 +1,3 @@
           1 +{"seed": 2, "count": 2, "success": true, "steps": 98, "seconds": 2.17, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           2 +{"seed": 45, "count": 2, "success": true, "steps": 93, "seconds": 2.53, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
           3 +{"seed": 67, "count": 2, "success": true, "steps": 101, "seconds": 2.14, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
diff --git a/stress50_fine_lift.txt b/stress50_fine_lift.txt
new file mode 100644
index 0000000..182a6a7
--- /dev/null
+++ b/stress50_fine_lift.txt
@@ -0,0 +1,7 @@
           1 +progress 0 above obstruction43:Kinematic3DCuboid 0 7 0 0 0.07
           2 +progress 50 lower obstruction43:Kinematic3DCuboid 0 7 0 1 2.15
           3 +progress 100 align obstruction21:Kinematic3DCuboid 2 7 0 1 4.5
           4 +progress 150 grasp obstruction1:Kinematic3DCuboid 2 7 0 1 6.99
           5 +progress 200 above obstruction2:Kinematic3DCuboid 4 7 0 0 9.37
           6 +progress 250 align obstruction21:Kinematic3DCuboid 5 7 0 0 11.68
           7 +{"seed": 2, "count": 50, "success": true, "steps": 295, "seconds": 13.53, "compute": 0.433, "phase": "release", "obj": "target_block:Kinematic3DCuboid", "stall": 0, "attempt": 0}
```

</details>

