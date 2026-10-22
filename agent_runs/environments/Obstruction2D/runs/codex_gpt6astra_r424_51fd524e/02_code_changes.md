# Obstruction2D · gpt-6-astra · replicate 424: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `abc5086` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `3551a66` | Save initial valid policy and black box state probe | approach.py, probe_states.py | [E0011](01_timeline.md#E0011) |
| [C003](#C003) · `9b01e06` | Add motion probing script for robot and world dynamics | probe_motion.py | No matched commit command/output |
| [C004](#C004) · `c2f1710` | Probe vertical grasp contact and release dynamics | probe_motion.py | No matched commit command/output |
| [C005](#C005) · `e24307b` | Add empirical vacuum contact and lift probe | probe_grasp.py | No matched commit command/output |
| [C006](#C006) · `9b55049` | Add variable object count layout survey | probe_layouts.py | [E0020](01_timeline.md#E0020) |
| [C007](#C007) · `ea9070f` | Measure workspace limits and precise gripper clearance | probe_motion.py | No matched commit command/output |
| [C008](#C008) · `8652fc8` | Add fresh-instance contact threshold probe | probe_grasp_threshold.py | No matched commit command/output |
| [C009](#C009) · `b2a53e6` | Refine robot workspace boundaries with diminishing motion steps | probe_motion.py | No matched commit command/output |
| [C010](#C010) · `86ade72` | Allow boundary probe enough refinement steps | probe_motion.py | No matched commit command/output |
| [C011](#C011) · `785bae8` | Implement staged top grasp, obstruction clearing, and target placement | approach.py, test_approach.py | [E0024](01_timeline.md#E0024) |
| [C012](#C012) · `acf20a5` | Approach grasp contact without penetration and store obstructions in free floor gaps | approach.py | [E0026](01_timeline.md#E0026) |
| [C013](#C013) · `1ec99bb` | Detect early vacuum attachment from blocked descent and verify by lifting | approach.py | [E0029](01_timeline.md#E0029) |
| [C014](#C014) · `eb91d14` | Choose least obstructed target placement and clamp grasps within base bounds | approach.py, test_batch.py | [E0054](01_timeline.md#E0054) |
| [C015](#C015) · `4d9be0c` | Print batch progress to distinguish slow scene generation from policy stalls | test_batch.py | [E0048](01_timeline.md#E0048) |
| [C016](#C016) · `68d8258` | Adapt travel heights to observed object sizes to reduce unnecessary lifting | approach.py | [E0050](01_timeline.md#E0050) |
| [C017](#C017) · `b0fb251` | Respect base reach when choosing target placement and offset grasps near the right wall | approach.py, results_0_100_None.json, results_0_30_3.json | [E0063](01_timeline.md#E0063) |
| [C018](#C018) · `9f7ad8b` | Find exact storage gaps and add bounded elevated storage for crowded scenes | approach.py, results_0_100_None.json, results_30_30_3.json | [E0065](01_timeline.md#E0065) |
| [C019](#C019) · `78e4e2b` | Offset narrow-object grasps to clear taller neighboring rectangles | approach.py, results_0_1_4.json | [E0083](01_timeline.md#E0083) |
| [C020](#C020) · `040eb1e` | Preserve destination reachability when selecting offset target grasps | approach.py, results_42_1_3.json | [E0075](01_timeline.md#E0075) |
| [C021](#C021) · `9f9d821` | Measure policy computation separately from remote environment latency | test_batch.py | [E0072](01_timeline.md#E0072) |
| [C022](#C022) · `9cc4359` | Search adjacent-obstruction robot clearance risks at final placement | probe_adjacent.py | No matched commit command/output |
| [C023](#C023) · `082e08b` | Emit complete failure diagnostics immediately during seed sweeps | test_batch.py | [E0079](01_timeline.md#E0079) |
| [C024](#C024) · `6cb4e13` | Check complete carried geometry for placement and storage, including offset grippers | approach.py, probe_adjacent.log, results_0_30_3.json, results_100_200_None.json, results_1_1_4.json, results_2_1_4.json, results_3_1_4.json, results_4_1_4.json, results_5_1_4.json | [E0088](01_timeline.md#E0088) |
| [C025](#C025) · `14524e5` | Reserve the final base footprint when relocating obstructions | approach.py | [E0091](01_timeline.md#E0091) |
| [C026](#C026) · `2fc1fb2` | Probe sub-millimeter final placement rejection on seed 151 | probe_final_clearance.py | [E0094](01_timeline.md#E0094) |
| [C027](#C027) · `c08b92a` | Allow conservative gripper contact clearance during final descent | approach.py | [E0116](01_timeline.md#E0116) |
| [C028](#C028) · `77929e5` | Add sequential dense-scene validation to avoid concurrent slow resets | results_0_100_None.json, results_2_3_4.json, test_count4_sequential.py | No matched commit command/output |
| [C029](#C029) · `69ec7fa` | Document the geometric controller and remove unused bookkeeping | approach.py, sweep_300_700.log | [E0106](01_timeline.md#E0106) |
| [C030](#C030) · `67048b9` | Report dense-scene validation checkpoint to expose policy stalls | sweep_300_700.log | No matched commit command/output |
| [C031](#C031) · `0891dc1` | Print step 200 phase and position in future sequential validation | results_100_200_None.json, sweep_300_700.log, test_count4_sequential.py | No matched commit command/output |
| [C032](#C032) · `692cf64` | Keep obstruction storage clear of the future target pickup configuration | approach.py, sweep_300_700.log | [E0136](01_timeline.md#E0136) |
| [C033](#C033) · `394488d` | Add carried-block clearance and tighten horizontal placement accuracy | approach.py, results_2_1_4.json, results_sequential_0_10_4.json, sweep_300_700.log | [E0134](01_timeline.md#E0134) |
| [C034](#C034) · `01878e6` | Add reproducible edge-case regression suite and policy documentation | README.md, sweep_300_700.log, test_regression.py | [E0150](01_timeline.md#E0150) |
| [C035](#C035) · `9bc34ce` | Record passing regression suite and add the second storage-order regression | regression_results.json, regression_run.log, test_regression.py | [E0155](01_timeline.md#E0155) |
| [C036](#C036) · `c31a79b` | Save successful unseen-seed and variable-count validation results | final_fresh_sweep.log, results_0_100_3.json, results_0_100_None.json, results_2000_100_None.json, sweep_300_700.log | [E0173](01_timeline.md#E0173) |
| [C037](#C037) · `c167df5` | Preserve current policy and add bounded diagnostics for the remaining dense case | probe_case.py, sweep_300_700.log | [E0186](01_timeline.md#E0186) |
| [C038](#C038) · `5f1766a` | Include circle-tangent and edge-contact grasps around tall neighbors | approach.py, results_100_100_3.json, results_300_700_None.json, sweep_300_700.log | [E0188](01_timeline.md#E0188) |
| [C039](#C039) · `1885889` | Finalize validation documentation and preserve all discovered regression cases | README.md, regression_results.json, regression_run.log, test_regression.py | [E0193](01_timeline.md#E0193) |
| [C040](#C040) · `bfc4b68` | Save final passing regression results and verified policy artifact | regression_results.json, regression_run.log | [E0198](01_timeline.md#E0198) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `abc508612324df53378eb72509d676276915ea01`; parents: none (initial snapshot). Recorded author date: 2026-09-21T22:22:13+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_abc5086.diff)

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
index 0000000..a08739d
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "611c0a9a561c826dbe9b47b8c9ff03a3", "observation_space": {"type": "ObjectCentric", "types": [{"name": "crv_robot", "parent": null, "features": ["x", "y", "theta", "base_radius", "arm_joint", "arm_length", "vacuum", "gripper_height", "gripper_width"]}, {"name": "kinematic2d", "parent": null, "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order"]}, {"name": "circle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "radius"]}, {"name": "double_rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height", "x1", "y1", "theta1", "width1", "height1", "z_order1", "color_r1", "color_g1", "color_b1"]}, {"name": "lobject", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "length_side1", "length_side2"]}, {"name": "rectangle", "parent": "kinematic2d", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_block", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}, {"name": "target_surface", "parent": "rectangle", "features": ["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]}]}, "action_space": {"type": "Box", "shape": [5], "low": [-0.05000000074505806, -0.05000000074505806, -0.19634954631328583, -0.10000000149011612, 0.0], "high": [0.05000000074505806, 0.05000000074505806, 0.19634954631328583, 0.10000000149011612, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Save initial valid policy and black box state probe

Commit `3551a669a95aca53516fbc5d96aec9d94d68c60f`; parents: abc508612324df53378eb72509d676276915ea01. Recorded author date: 2026-09-21T22:22:56+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0011](01_timeline.md#E0011): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C002_3551a66_approach.py) · [Exact all-file diff](evidence/diffs/C002_3551a66.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..c61c0b2
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,9 @@
           1 +import numpy as np
           2 +class GeneratedApproach:
           3 +    def __init__(self, action_space, observation_space, primitives):
           4 +        self.action_space = action_space
           5 +        self.observation_space = observation_space
           6 +    def reset(self, state, info):
           7 +        pass
           8 +    def get_action(self, state):
           9 +        return np.array([0,0,0,0,0], dtype=np.float32)
diff --git a/probe_states.py b/probe_states.py
new file mode 100644
index 0000000..ed591ce
--- /dev/null
+++ b/probe_states.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +import json
           3 +e=make_env()
           4 +print('limit',e.max_steps)
           5 +for seed in range(5):
           6 + s,i=e.reset(seed=seed)
           7 + print('SEED',seed,'INFO',i)
           8 + for n in sorted(s.get_object_names()):
           9 +  o=s.get_object_from_name(n)
          10 +  print(n,o.type.name,{f:round(s.get(o,f),4) for f in e.observation_space.type_features[o.type] if not f.startswith('color') and f!='z_order'})
          11 +e.close()
```

</details>

<a id="C003"></a>
### C003 · Add motion probing script for robot and world dynamics

Commit `9b01e062f3eba2d5621407502bc12b77b2ea7a0b`; parents: 3551a669a95aca53516fbc5d96aec9d94d68c60f. Recorded author date: 2026-09-21T22:22:58+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C003_9b01e06.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_motion.py b/probe_motion.py
new file mode 100644
index 0000000..10e8e8e
--- /dev/null
+++ b/probe_motion.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def desc(e,s):
           5 + for ty in e.observation_space.types:
           6 +  for o in s.get_objects(ty):
           7 +   print(o.name, {f:round(float(s.get(o,f)),4) for f in e.observation_space.type_features[ty]})
           8 +e=make_env();s,i=e.reset(seed=0); print('MAX',e.max_steps,'INFO',i);desc(e,s)
           9 +for a in [[0,0,0,.1,0]]*5+[[0,0,.196,0,0]]*4+[[.05,0,0,0,0]]*3+[[0,-.05,0,0,0]]*3:
          10 + s,r,t,tr,i=e.step(np.array(a,dtype=np.float32));print('ACTION',a,r,t,tr);desc(e,s)
          11 +e.close()
```

</details>

<a id="C004"></a>
### C004 · Probe vertical grasp contact and release dynamics

Commit `c2f1710123af94e107d9d96d159f9ca39beab7a4`; parents: 9b01e062f3eba2d5621407502bc12b77b2ea7a0b. Recorded author date: 2026-09-21T22:23:23+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C004_c2f1710.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_motion.py b/probe_motion.py
index 10e8e8e..b47784c 100644
--- a/probe_motion.py
+++ b/probe_motion.py
@@ -1,11 +1,23 @@
    1      1  from env_client import make_env
    2      2  import numpy as np
    3      3  
    4        -def desc(e,s):
    5        - for ty in e.observation_space.types:
    6        -  for o in s.get_objects(ty):
    7        -   print(o.name, {f:round(float(s.get(o,f)),4) for f in e.observation_space.type_features[ty]})
    8        -e=make_env();s,i=e.reset(seed=0); print('MAX',e.max_steps,'INFO',i);desc(e,s)
    9        -for a in [[0,0,0,.1,0]]*5+[[0,0,.196,0,0]]*4+[[.05,0,0,0,0]]*3+[[0,-.05,0,0,0]]*3:
   10        - s,r,t,tr,i=e.step(np.array(a,dtype=np.float32));print('ACTION',a,r,t,tr);desc(e,s)
   11        -e.close()
           4 +def vals(s,n,fs):
           5 + o=s.get_object_from_name(n);return [round(float(s.get(o,f)),6) for f in fs.split()]
           6 +def run(vac):
           7 + e=make_env();s,_=e.reset(seed=0)
           8 + def step(a,show=True):
           9 +  nonlocal s
          10 +  s,r,t,tr,i=e.step(np.array(a,dtype=np.float32))
          11 +  if show:print(a,'robot',vals(s,'robot','x y arm_joint vacuum'),'block',vals(s,'target_block','x y theta'))
          12 + bx,by,bw,bh=vals(s,'target_block','x y width height');cx=bx+bw/2
          13 + for _ in range(20):
          14 +  rx,ry,arm=vals(s,'robot','x y arm_joint')
          15 +  if abs(rx-cx)<1e-5 and abs(ry-.5)<1e-5:break
          16 +  step([np.clip(cx-rx,-.05,.05),np.clip(.5-ry,-.05,.05),0,.1,0],False)
          17 + print('VAC',vac,'begin',vals(s,'robot','x y arm_joint'))
          18 + for _ in range(25):step([0,-.01,0,0,vac])
          19 + for _ in range(6):step([0,.05,0,0,vac])
          20 + step([0,0,0,0,0])
          21 + for _ in range(3):step([0,0,0,0,0])
          22 + e.close()
          23 +run(0);run(1)
```

</details>

<a id="C005"></a>
### C005 · Add empirical vacuum contact and lift probe

Commit `e24307b4f37f5fbb943d95b95648eaa963995e90`; parents: c2f1710123af94e107d9d96d159f9ca39beab7a4. Recorded author date: 2026-09-21T22:23:30+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C005_e24307b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp.py b/probe_grasp.py
new file mode 100644
index 0000000..57f3504
--- /dev/null
+++ b/probe_grasp.py
@@ -0,0 +1,17 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +e=make_env(); s,_=e.reset(seed=1)
           5 +r=s.get_object_from_name('robot'); b=s.get_object_from_name('target_block')
           6 +def out(tag):
           7 + print(tag, 'r',*[round(s.get(r,k),5) for k in ['x','y','arm_joint','arm_length','vacuum']], 'b',*[round(s.get(b,k),5) for k in ['x','y','theta']])
           8 +def step(a,tag):
           9 + global s
          10 + s,w,t,tr,i=e.step(np.array(a,dtype=np.float32));out(tag)
          11 + return t
          12 +x=s.get(b,'x')+s.get(b,'width')/2
          13 +out('init')
          14 +while abs(s.get(r,'x')-x)>1e-5: step([np.clip(x-s.get(r,'x'),-.05,.05),0,0,0,0],'align')
          15 +for k in range(45): step([0,-.01,0,0,1],'down'+str(k))
          16 +for k in range(12): step([0,.025,0,0,1],'up'+str(k))
          17 +e.close()
```

</details>

<a id="C006"></a>
### C006 · Add variable object count layout survey

Commit `9b55049c9852c4ca7514bc597052728f55671781`; parents: e24307b4f37f5fbb943d95b95648eaa963995e90. Recorded author date: 2026-09-21T22:23:31+02:00.

File roles (automatic): diagnostic/test.

- [E0020](01_timeline.md#E0020): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C006_9b55049.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_layouts.py b/probe_layouts.py
new file mode 100644
index 0000000..d919405
--- /dev/null
+++ b/probe_layouts.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +import json
           3 +e=make_env(); out=[]
           4 +for count in [0,1,2,3,5,10,20]:
           5 + for seed in range(10):
           6 +  s,i=e.reset(seed=seed,options={'object_count':count})
           7 +  rows=[]
           8 +  for o in s.get_objects(e.observation_space.get_type('rectangle')):
           9 +   rows.append(dict(name=o.name,**{f:s.get(o,f) for f in ['x','y','width','height','theta']}))
          10 +  out.append(dict(seed=seed,count=count,rows=rows))
          11 + print('count',count,'last actual',len(rows)-2,flush=True)
          12 +json.dump(out,open('layouts.json','w'));e.close()
```

</details>

<a id="C007"></a>
### C007 · Measure workspace limits and precise gripper clearance

Commit `ea9070f54b05e4430b8cb46e78a5f899d225891c`; parents: 9b55049c9852c4ca7514bc597052728f55671781. Recorded author date: 2026-09-21T22:23:54+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C007_ea9070f.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_motion.py b/probe_motion.py
index b47784c..134e2e2 100644
--- a/probe_motion.py
+++ b/probe_motion.py
@@ -2,22 +2,27 @@ from env_client import make_env
    2      2  import numpy as np
    3      3  
    4      4  def vals(s,n,fs):
    5        - o=s.get_object_from_name(n);return [round(float(s.get(o,f)),6) for f in fs.split()]
    6        -def run(vac):
           5 + o=s.get_object_from_name(n);return [round(float(s.get(o,f)),7) for f in fs.split()]
           6 +def run():
    7      7   e=make_env();s,_=e.reset(seed=0)
    8        - def step(a,show=True):
           8 + def step(a):
    9      9    nonlocal s
   10        -  s,r,t,tr,i=e.step(np.array(a,dtype=np.float32))
   11        -  if show:print(a,'robot',vals(s,'robot','x y arm_joint vacuum'),'block',vals(s,'target_block','x y theta'))
          10 +  s,*_=e.step(np.array(a,dtype=np.float32))
          11 + def show(t):print(t,vals(s,'robot','x y theta arm_joint'),vals(s,'target_block','x y'))
          12 + for label,a,n in [('retract',[0,0,0,-.1,0],5),('left',[-.05,0,0,0,0],20),('up',[0,.05,0,0,0],20),('right',[.05,0,0,0,0],60),('down',[0,-.05,0,0,0],30),('extend',[0,0,0,.1,0],5)]:
          13 +  for _ in range(n):step(a)
          14 +  show(label)
          15 + e.close()
          16 + e=make_env();s,_=e.reset(seed=0)
   12     17   bx,by,bw,bh=vals(s,'target_block','x y width height');cx=bx+bw/2
   13     18   for _ in range(20):
   14     19    rx,ry,arm=vals(s,'robot','x y arm_joint')
   15        -  if abs(rx-cx)<1e-5 and abs(ry-.5)<1e-5:break
   16        -  step([np.clip(cx-rx,-.05,.05),np.clip(.5-ry,-.05,.05),0,.1,0],False)
   17        - print('VAC',vac,'begin',vals(s,'robot','x y arm_joint'))
   18        - for _ in range(25):step([0,-.01,0,0,vac])
   19        - for _ in range(6):step([0,.05,0,0,vac])
   20        - step([0,0,0,0,0])
   21        - for _ in range(3):step([0,0,0,0,0])
          20 +  step([np.clip(cx-rx,-.05,.05),np.clip(.4-ry,-.05,.05),0,.1,0])
          21 + for _ in range(40):step([0,-.001,0,0,0])
          22 + show('precise contact no vac')
          23 + step([0,0,0,0,1]);step([0,.05,0,0,1]);show('lift')
          24 + # Rotate grabbed object to inspect origin convention
          25 + for _ in range(4):step([0,0,.196,0,1])
          26 + show('rotated');print('blocktheta',vals(s,'target_block','theta'))
   22     27   e.close()
   23        -run(0);run(1)
          28 +run()
```

</details>

<a id="C008"></a>
### C008 · Add fresh-instance contact threshold probe

Commit `8652fc820732adeb091273ae8115546c7aa34eb0`; parents: ea9070f54b05e4430b8cb46e78a5f899d225891c. Recorded author date: 2026-09-21T22:23:56+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C008_8652fc8.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_grasp_threshold.py b/probe_grasp_threshold.py
new file mode 100644
index 0000000..e5e8765
--- /dev/null
+++ b/probe_grasp_threshold.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +for jointdelta in [0,.1,-.1]:
           4 + for goal_y in [.58,.50,.48,.46,.44,.42,.40,.38,.36]:
           5 +  e=make_env();s,_=e.reset(seed=1);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           6 +  def step(a):
           7 +   global s
           8 +   s,*_=e.step(np.array(a,dtype=np.float32))
           9 +  x=s.get(b,'x')+s.get(b,'width')/2
          10 +  for _ in range(20):
          11 +   step([np.clip(x-s.get(r,'x'),-.05,.05),0,0,jointdelta,0]);jointdelta=0 if False else jointdelta
          12 +   if abs(s.get(r,'x')-x)<1e-6:break
          13 +  for _ in range(20):
          14 +   step([0,np.clip(goal_y-s.get(r,'y'),-.05,.05),0,0,1])
          15 +   if abs(s.get(r,'y')-goal_y)<1e-6:break
          16 +  before=s.get(b,'y');actual=s.get(r,'y');j=s.get(r,'arm_joint');l=s.get(r,'arm_length')
          17 +  step([0,.02,0,0,1])
          18 +  print(jointdelta,goal_y,'actual',round(actual,4),'joint',j,'len',l,'held',round(s.get(b,'y')-before,4))
          19 +  e.close()
```

</details>

<a id="C009"></a>
### C009 · Refine robot workspace boundaries with diminishing motion steps

Commit `b2a53e6ff9da4e0cb0b4655e9ab3f413c682aa3b`; parents: 8652fc820732adeb091273ae8115546c7aa34eb0. Recorded author date: 2026-09-21T22:24:24+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C009_b2a53e6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_motion.py b/probe_motion.py
index 134e2e2..93481cc 100644
--- a/probe_motion.py
+++ b/probe_motion.py
@@ -26,3 +26,12 @@ def run():
   26     26   show('rotated');print('blocktheta',vals(s,'target_block','theta'))
   27     27   e.close()
   28     28  run()
          29 +e=make_env();s,_=e.reset(seed=0)
          30 +r=s.get_object_from_name('robot')
          31 +for axis,sign in [(0,-1),(1,1),(0,1)]:
          32 + for size in [.05,.005,.0005,.00005]:
          33 +  for _ in range(40 if size==.05 else 12):
          34 +   a=np.zeros(5,dtype=np.float32);a[axis]=sign*size
          35 +   s,*_=e.step(a)
          36 + print('BOUND',axis,sign,vals(s,'robot','x y'))
          37 +e.close()
```

</details>

<a id="C010"></a>
### C010 · Allow boundary probe enough refinement steps

Commit `86ade72043846363b975071c2fe877b9672d0ee9`; parents: b2a53e6ff9da4e0cb0b4655e9ab3f413c682aa3b. Recorded author date: 2026-09-21T22:24:37+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C010_86ade72.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_motion.py b/probe_motion.py
index 93481cc..10e66c6 100644
--- a/probe_motion.py
+++ b/probe_motion.py
@@ -30,7 +30,7 @@ e=make_env();s,_=e.reset(seed=0)
   30     30  r=s.get_object_from_name('robot')
   31     31  for axis,sign in [(0,-1),(1,1),(0,1)]:
   32     32   for size in [.05,.005,.0005,.00005]:
   33        -  for _ in range(40 if size==.05 else 12):
          33 +  for _ in range(60 if size==.05 else 120):
   34     34     a=np.zeros(5,dtype=np.float32);a[axis]=sign*size
   35     35     s,*_=e.step(a)
   36     36   print('BOUND',axis,sign,vals(s,'robot','x y'))
```

</details>

<a id="C011"></a>
### C011 · Implement staged top grasp, obstruction clearing, and target placement

Commit `785bae87c4f4054ad76ca7af8a2d35519d6bf55b`; parents: 86ade72043846363b975071c2fe877b9672d0ee9. Recorded author date: 2026-09-21T22:24:52+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0024](01_timeline.md#E0024): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C011_785bae8_approach.py) · [Exact all-file diff](evidence/diffs/C011_785bae8.diff)

[Previous saved controller snapshot](evidence/versions/C002_3551a66_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c61c0b2..e64de74 100644
--- a/approach.py
+++ b/approach.py
@@ -1,9 +1,81 @@
           1 +import math
    1      2  import numpy as np
           3 +
    2      4  class GeneratedApproach:
    3      5      def __init__(self, action_space, observation_space, primitives):
    4      6          self.action_space = action_space
    5      7          self.observation_space = observation_space
           8 +        self.rt = observation_space.get_type('crv_robot')
           9 +        self.bt = observation_space.get_type('target_block')
          10 +        self.st = observation_space.get_type('target_surface')
          11 +        self.ot = observation_space.get_type('rectangle')
          12 +
    6     13      def reset(self, state, info):
    7        -        pass
    8        -    def get_action(self, state):
    9        -        return np.array([0,0,0,0,0], dtype=np.float32)
          14 +        self.robot = state.get_objects(self.rt)[0]
          15 +        self.block = state.get_objects(self.bt)[0]
          16 +        self.surface = state.get_objects(self.st)[0]
          17 +        self.phase = 'select'
          18 +        self.obj = None
          19 +        self.n = 0
          20 +        self.stashed = []
          21 +
          22 +    def val(self, s, o, f):
          23 +        return s.get(o, f)
          24 +
          25 +    def rect(self, s, o):
          26 +        return [s.get(o,f) for f in ('x','y','width','height')]
          27 +
          28 +    def action(self, s, x=None, y=None, vac=0):
          29 +        r=self.robot
          30 +        return np.array([0 if x is None else np.clip(x-s.get(r,'x'),-.05,.05),
          31 +                         0 if y is None else np.clip(y-s.get(r,'y'),-.05,.05),
          32 +                         np.clip(-math.pi/2-s.get(r,'theta'),-.19634954,.19634954),
          33 +                         np.clip(.2-s.get(r,'arm_joint'),-.1,.1),vac],dtype=np.float32)
          34 +
          35 +    def get_action(self, s):
          36 +        r=self.robot; rx=s.get(r,'x'); ry=s.get(r,'y')
          37 +        for _ in range(10):
          38 +            if self.phase == 'select':
          39 +                bx,by,bw,bh=self.rect(s,self.block)
          40 +                sx,sy,sw,sh=self.rect(s,self.surface)
          41 +                self.destx=sx+(sw-bw)/2
          42 +                obs=[o for o in s.get_objects(self.ot) if o not in (self.block,self.surface)]
          43 +                blocking=[o for o in obs if s.get(o,'x')<self.destx+bw+.004 and s.get(o,'x')+s.get(o,'width')>self.destx-.004 and s.get(o,'y')<sy+sh+bh+.04]
          44 +                self.obj=max(blocking,key=lambda o:s.get(o,'y')+s.get(o,'height')) if blocking else self.block
          45 +                self.phase='above'
          46 +            x,y,w,h=self.rect(s,self.obj)
          47 +            if self.phase == 'above':
          48 +                if ry<.72: return self.action(s,y=.75)
          49 +                if abs(rx-(x+w/2))>.001: return self.action(s,x=x+w/2,y=.75)
          50 +                self.phase='down'; self.n=0
          51 +            if self.phase == 'down':
          52 +                self.n+=1
          53 +                goal=y+h+.2+.004
          54 +                if ry>goal+.001:return self.action(s,y=goal,vac=1)
          55 +                self.pick_y=y; self.phase='lift';self.n=0
          56 +            if self.phase == 'lift':
          57 +                self.n+=1
          58 +                if ry<.749:return self.action(s,y=.75,vac=1)
          59 +                if y < self.pick_y+.02:
          60 +                    self.phase='down'
          61 +                    return self.action(s,y=y+h+.195,vac=1)
          62 +                self.offsetx=x-rx;self.offsety=y-ry
          63 +                if self.obj==self.block:
          64 +                    self.dropx=self.destx
          65 +                else:
          66 +                    self.dropx=.12+len(self.stashed)*.23;self.dropy=.48
          67 +                if self.obj==self.block:self.dropy=s.get(self.surface,'y')+s.get(self.surface,'height')+.001
          68 +                self.phase='carry'
          69 +            if self.phase == 'carry':
          70 +                goal=self.dropx-self.offsetx
          71 +                if abs(rx-goal)>.001:return self.action(s,x=goal,vac=1)
          72 +                self.phase='place'
          73 +            if self.phase == 'place':
          74 +                goal=self.dropy-self.offsety
          75 +                if abs(ry-goal)>.001:return self.action(s,y=goal,vac=1)
          76 +                self.stashed.append(self.obj);self.phase='retreat'
          77 +                return self.action(s,vac=0)
          78 +            if self.phase=='retreat':
          79 +                if ry<.749:return self.action(s,y=.75,vac=0)
          80 +                self.phase='select'
          81 +        return self.action(s)
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..c338257
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import sys,time,json
           4 +seeds=[int(x) for x in sys.argv[1:]] or list(range(10))
           5 +e=make_env()
           6 +for seed in seeds:
           7 + s,i=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i);start=time.time()
           8 + trace=[]
           9 + for t in range(e.max_steps):
          10 +  a=p.get_action(s); s,re,done,trunc,info=e.step(a)
          11 +  if t%20==0:trace.append([t,p.phase,p.obj.name if p.obj else '',*[round(s.get(p.robot,f),3) for f in ['x','y']],*[round(s.get(p.obj,f),3) for f in ['x','y']]])
          12 +  if done or trunc:break
          13 + print(seed,'OK' if done else 'FAIL',t+1,'time',round(time.time()-start,2),flush=True)
          14 + if not done:print(trace[-15:],flush=True)
          15 +e.close()
```

</details>

<a id="C012"></a>
### C012 · Approach grasp contact without penetration and store obstructions in free floor gaps

Commit `acf20a542e1f884c3486ea650c3101a170e52377`; parents: 785bae87c4f4054ad76ca7af8a2d35519d6bf55b. Recorded author date: 2026-09-21T22:25:34+02:00.

File roles (automatic): policy.

- [E0026](01_timeline.md#E0026): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_acf20a5_approach.py) · [Exact all-file diff](evidence/diffs/C012_acf20a5.diff)

[Previous saved controller snapshot](evidence/versions/C011_785bae8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e64de74..7fb8b50 100644
--- a/approach.py
+++ b/approach.py
@@ -50,7 +50,7 @@ class GeneratedApproach:
   50     50                  self.phase='down'; self.n=0
   51     51              if self.phase == 'down':
   52     52                  self.n+=1
   53        -                goal=y+h+.2+.004
          53 +                goal=y+h+.2+.006
   54     54                  if ry>goal+.001:return self.action(s,y=goal,vac=1)
   55     55                  self.pick_y=y; self.phase='lift';self.n=0
   56     56              if self.phase == 'lift':
@@ -63,7 +63,19 @@ class GeneratedApproach:
   63     63                  if self.obj==self.block:
   64     64                      self.dropx=self.destx
   65     65                  else:
   66        -                    self.dropx=.12+len(self.stashed)*.23;self.dropy=.48
          66 +                    occupied=[]
          67 +                    for other in s.get_objects(self.ot):
          68 +                        if other==self.obj:continue
          69 +                        ox,oy,ow,oh=self.rect(s,other)
          70 +                        occupied.append((ox-.012,ox+ow+.012))
          71 +                    candidates=[]
          72 +                    for cx in np.linspace(.101,1.517,220):
          73 +                        left=cx-w/2
          74 +                        if left<.005 or left+w>1.613:continue
          75 +                        if any(left<b and left+w>a for a,b in occupied):continue
          76 +                        candidates.append(left)
          77 +                    self.dropx=min(candidates,key=lambda v:abs(v-x)) if candidates else .01
          78 +                    self.dropy=.101
   67     79                  if self.obj==self.block:self.dropy=s.get(self.surface,'y')+s.get(self.surface,'height')+.001
   68     80                  self.phase='carry'
   69     81              if self.phase == 'carry':
```

</details>

<a id="C013"></a>
### C013 · Detect early vacuum attachment from blocked descent and verify by lifting

Commit `1ec99bbc06b99cdbdd85c44fbfc73be5951b5f37`; parents: acf20a542e1f884c3486ea650c3101a170e52377. Recorded author date: 2026-09-21T22:26:01+02:00.

File roles (automatic): policy.

- [E0029](01_timeline.md#E0029): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_1ec99bb_approach.py) · [Exact all-file diff](evidence/diffs/C013_1ec99bb.diff)

[Previous saved controller snapshot](evidence/versions/C012_acf20a5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7fb8b50..4468226 100644
--- a/approach.py
+++ b/approach.py
@@ -47,17 +47,19 @@ class GeneratedApproach:
   47     47              if self.phase == 'above':
   48     48                  if ry<.72: return self.action(s,y=.75)
   49     49                  if abs(rx-(x+w/2))>.001: return self.action(s,x=x+w/2,y=.75)
   50        -                self.phase='down'; self.n=0
          50 +                self.phase='down'; self.n=0; self.last_down=None
   51     51              if self.phase == 'down':
   52     52                  self.n+=1
   53     53                  goal=y+h+.2+.006
   54        -                if ry>goal+.001:return self.action(s,y=goal,vac=1)
          54 +                if ry>goal+.001 and (self.last_down is None or abs(ry-self.last_down)>.00001):
          55 +                    self.last_down=ry
          56 +                    return self.action(s,y=goal,vac=1)
   55     57                  self.pick_y=y; self.phase='lift';self.n=0
   56     58              if self.phase == 'lift':
   57     59                  self.n+=1
   58     60                  if ry<.749:return self.action(s,y=.75,vac=1)
   59     61                  if y < self.pick_y+.02:
   60        -                    self.phase='down'
          62 +                    self.phase='down'; self.last_down=None
   61     63                      return self.action(s,y=y+h+.195,vac=1)
   62     64                  self.offsetx=x-rx;self.offsety=y-ry
   63     65                  if self.obj==self.block:
```

</details>

<a id="C014"></a>
### C014 · Choose least obstructed target placement and clamp grasps within base bounds

Commit `eb91d14b4525fd8b40ae4b1888406764506db3f9`; parents: 1ec99bbc06b99cdbdd85c44fbfc73be5951b5f37. Recorded author date: 2026-09-21T22:26:46+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0054](01_timeline.md#E0054): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_eb91d14_approach.py) · [Exact all-file diff](evidence/diffs/C014_eb91d14.diff)

[Previous saved controller snapshot](evidence/versions/C013_1ec99bb_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4468226..d5dea37 100644
--- a/approach.py
+++ b/approach.py
@@ -38,15 +38,20 @@ class GeneratedApproach:
   38     38              if self.phase == 'select':
   39     39                  bx,by,bw,bh=self.rect(s,self.block)
   40     40                  sx,sy,sw,sh=self.rect(s,self.surface)
   41        -                self.destx=sx+(sw-bw)/2
   42     41                  obs=[o for o in s.get_objects(self.ot) if o not in (self.block,self.surface)]
          42 +                choices=np.linspace(sx+.001,sx+sw-bw-.001,21)
          43 +                def cost(left):
          44 +                    overlap=[o for o in obs if s.get(o,'x')<left+bw+.004 and s.get(o,'x')+s.get(o,'width')>left-.004 and s.get(o,'y')<sy+sh+bh+.04]
          45 +                    return (len(overlap),abs(left-(sx+(sw-bw)/2)))
          46 +                self.destx=min(choices,key=cost)
   43     47                  blocking=[o for o in obs if s.get(o,'x')<self.destx+bw+.004 and s.get(o,'x')+s.get(o,'width')>self.destx-.004 and s.get(o,'y')<sy+sh+bh+.04]
   44     48                  self.obj=max(blocking,key=lambda o:s.get(o,'y')+s.get(o,'height')) if blocking else self.block
   45     49                  self.phase='above'
   46     50              x,y,w,h=self.rect(s,self.obj)
   47     51              if self.phase == 'above':
   48     52                  if ry<.72: return self.action(s,y=.75)
   49        -                if abs(rx-(x+w/2))>.001: return self.action(s,x=x+w/2,y=.75)
          53 +                grasp_x=float(np.clip(x+w/2,.101,1.517))
          54 +                if abs(rx-grasp_x)>.001: return self.action(s,x=grasp_x,y=.75)
   50     55                  self.phase='down'; self.n=0; self.last_down=None
   51     56              if self.phase == 'down':
   52     57                  self.n+=1
diff --git a/test_batch.py b/test_batch.py
new file mode 100644
index 0000000..b805256
--- /dev/null
+++ b/test_batch.py
@@ -0,0 +1,29 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import sys,time,json,concurrent.futures
           4 +start=int(sys.argv[1]) if len(sys.argv)>1 else 0
           5 +n=int(sys.argv[2]) if len(sys.argv)>2 else 100
           6 +count=int(sys.argv[3]) if len(sys.argv)>3 else None
           7 +
           8 +def run(seed):
           9 + e=make_env()
          10 + try:
          11 +  s,i=e.reset(seed=seed,options={'object_count':count} if count is not None else None)
          12 +  p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
          13 +  st=time.time();trace=[]
          14 +  for t in range(e.max_steps):
          15 +   a=p.get_action(s);s,r,d,tr,i=e.step(a)
          16 +   if t%40==0:trace.append([t,p.phase,p.obj.name if p.obj else '',round(s.get(p.robot,'x'),4),round(s.get(p.robot,'y'),4)])
          17 +   if d or tr:break
          18 +  out=dict(seed=seed,count=count,done=d,steps=t+1,seconds=round(time.time()-st,3))
          19 +  if not d:out['trace']=trace[-4:];out['state']={o.name:{f:s.get(o,f) for f in ('x','y','width','height')} for o in s.get_objects(p.ot)}
          20 +  return out
          21 + except Exception as ex:return dict(seed=seed,count=count,error=str(ex))
          22 + finally:e.close()
          23 +
          24 +with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
          25 + results=list(ex.map(run,range(start,start+n)))
          26 +for r in results:
          27 + if not r.get('done'):print(r)
          28 +print('SUMMARY',len(results),'success',sum(r.get('done',False) for r in results),'mean_steps',round(sum(r.get('steps',0) for r in results)/len(results),2),'max_time',max(r.get('seconds',0) for r in results),flush=True)
          29 +json.dump(results,open('results_%s_%s_%s.json'%(start,n,count),'w'))
```

</details>

<a id="C015"></a>
### C015 · Print batch progress to distinguish slow scene generation from policy stalls

Commit `4d9be0cd5ba4da86bb860dbf8ccbbc22af292202`; parents: eb91d14b4525fd8b40ae4b1888406764506db3f9. Recorded author date: 2026-09-21T22:29:42+02:00.

File roles (automatic): diagnostic/test.

- [E0048](01_timeline.md#E0048): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C015_4d9be0c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_batch.py b/test_batch.py
index b805256..2ac5088 100644
--- a/test_batch.py
+++ b/test_batch.py
@@ -17,6 +17,7 @@ def run(seed):
   17     17     if d or tr:break
   18     18    out=dict(seed=seed,count=count,done=d,steps=t+1,seconds=round(time.time()-st,3))
   19     19    if not d:out['trace']=trace[-4:];out['state']={o.name:{f:s.get(o,f) for f in ('x','y','width','height')} for o in s.get_objects(p.ot)}
          20 +  print(seed, "OK" if d else "FAIL", t+1, flush=True)
   20     21    return out
   21     22   except Exception as ex:return dict(seed=seed,count=count,error=str(ex))
   22     23   finally:e.close()
```

</details>

<a id="C016"></a>
### C016 · Adapt travel heights to observed object sizes to reduce unnecessary lifting

Commit `68d82581c063b5c03d94b7fc7407622d3ab40028`; parents: 4d9be0cd5ba4da86bb860dbf8ccbbc22af292202. Recorded author date: 2026-09-21T22:30:17+02:00.

File roles (automatic): policy.

- [E0050](01_timeline.md#E0050): commit hash in recorded output.
[Controller after this commit](evidence/versions/C016_68d8258_approach.py) · [Exact all-file diff](evidence/diffs/C016_68d8258.diff)

[Previous saved controller snapshot](evidence/versions/C014_eb91d14_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d5dea37..28b482d 100644
--- a/approach.py
+++ b/approach.py
@@ -46,12 +46,14 @@ class GeneratedApproach:
   46     46                  self.destx=min(choices,key=cost)
   47     47                  blocking=[o for o in obs if s.get(o,'x')<self.destx+bw+.004 and s.get(o,'x')+s.get(o,'width')>self.destx-.004 and s.get(o,'y')<sy+sh+bh+.04]
   48     48                  self.obj=max(blocking,key=lambda o:s.get(o,'y')+s.get(o,'height')) if blocking else self.block
          49 +                self.emptyheight=min(.75,max(s.get(o,'y')+s.get(o,'height') for o in s.get_objects(self.ot))+.225)
          50 +                self.carryheight=min(.89,self.emptyheight+s.get(self.obj,'height')+.008)
   49     51                  self.phase='above'
   50     52              x,y,w,h=self.rect(s,self.obj)
   51     53              if self.phase == 'above':
   52        -                if ry<.72: return self.action(s,y=.75)
          54 +                if ry<self.emptyheight-.001: return self.action(s,y=self.emptyheight)
   53     55                  grasp_x=float(np.clip(x+w/2,.101,1.517))
   54        -                if abs(rx-grasp_x)>.001: return self.action(s,x=grasp_x,y=.75)
          56 +                if abs(rx-grasp_x)>.001: return self.action(s,x=grasp_x,y=self.emptyheight)
   55     57                  self.phase='down'; self.n=0; self.last_down=None
   56     58              if self.phase == 'down':
   57     59                  self.n+=1
@@ -62,7 +64,7 @@ class GeneratedApproach:
   62     64                  self.pick_y=y; self.phase='lift';self.n=0
   63     65              if self.phase == 'lift':
   64     66                  self.n+=1
   65        -                if ry<.749:return self.action(s,y=.75,vac=1)
          67 +                if ry<self.carryheight-.001:return self.action(s,y=self.carryheight,vac=1)
   66     68                  if y < self.pick_y+.02:
   67     69                      self.phase='down'; self.last_down=None
   68     70                      return self.action(s,y=y+h+.195,vac=1)
@@ -95,6 +97,6 @@ class GeneratedApproach:
   95     97                  self.stashed.append(self.obj);self.phase='retreat'
   96     98                  return self.action(s,vac=0)
   97     99              if self.phase=='retreat':
   98        -                if ry<.749:return self.action(s,y=.75,vac=0)
         100 +                if ry<self.emptyheight-.001:return self.action(s,y=self.emptyheight,vac=0)
   99    101                  self.phase='select'
  100    102          return self.action(s)
```

</details>

<a id="C017"></a>
### C017 · Respect base reach when choosing target placement and offset grasps near the right wall

Commit `b0fb251ccb6c924f91b47df1acf37e51484549a6`; parents: 68d82581c063b5c03d94b7fc7407622d3ab40028. Recorded author date: 2026-09-21T22:31:47+02:00.

File roles (automatic): policy, setup/other.

- [E0063](01_timeline.md#E0063): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_b0fb251_approach.py) · [Exact all-file diff](evidence/diffs/C017_b0fb251.diff)

[Previous saved controller snapshot](evidence/versions/C016_68d8258_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 28b482d..62a8d4f 100644
--- a/approach.py
+++ b/approach.py
@@ -42,7 +42,7 @@ class GeneratedApproach:
   42     42                  choices=np.linspace(sx+.001,sx+sw-bw-.001,21)
   43     43                  def cost(left):
   44     44                      overlap=[o for o in obs if s.get(o,'x')<left+bw+.004 and s.get(o,'x')+s.get(o,'width')>left-.004 and s.get(o,'y')<sy+sh+bh+.04]
   45        -                    return (len(overlap),abs(left-(sx+(sw-bw)/2)))
          45 +                    return (max(0,left+bw/2-1.516),len(overlap),abs(left-(sx+(sw-bw)/2)))
   46     46                  self.destx=min(choices,key=cost)
   47     47                  blocking=[o for o in obs if s.get(o,'x')<self.destx+bw+.004 and s.get(o,'x')+s.get(o,'width')>self.destx-.004 and s.get(o,'y')<sy+sh+bh+.04]
   48     48                  self.obj=max(blocking,key=lambda o:s.get(o,'y')+s.get(o,'height')) if blocking else self.block
@@ -52,7 +52,8 @@ class GeneratedApproach:
   52     52              x,y,w,h=self.rect(s,self.obj)
   53     53              if self.phase == 'above':
   54     54                  if ry<self.emptyheight-.001: return self.action(s,y=self.emptyheight)
   55        -                grasp_x=float(np.clip(x+w/2,.101,1.517))
          55 +                grasp_shift=min(0,1.516-(self.destx+w/2)) if self.obj==self.block else 0
          56 +                grasp_x=float(np.clip(x+w/2+grasp_shift,.101,1.517))
   56     57                  if abs(rx-grasp_x)>.001: return self.action(s,x=grasp_x,y=self.emptyheight)
   57     58                  self.phase='down'; self.n=0; self.last_down=None
   58     59              if self.phase == 'down':
@@ -80,7 +81,7 @@ class GeneratedApproach:
   80     81                      candidates=[]
   81     82                      for cx in np.linspace(.101,1.517,220):
   82     83                          left=cx-w/2
   83        -                        if left<.005 or left+w>1.613:continue
          84 +                        if left<.005 or left+w>1.613 or not .101<=left-self.offsetx<=1.517:continue
   84     85                          if any(left<b and left+w>a for a,b in occupied):continue
   85     86                          candidates.append(left)
   86     87                      self.dropx=min(candidates,key=lambda v:abs(v-x)) if candidates else .01
diff --git a/results_0_100_None.json b/results_0_100_None.json
new file mode 100644
index 0000000..aaa8c58
--- /dev/null
+++ b/results_0_100_None.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "count": null, "done": true, "steps": 111, "seconds": 4.328}, {"seed": 1, "count": null, "done": true, "steps": 88, "seconds": 3.003}, {"seed": 2, "count": null, "done": true, "steps": 112, "seconds": 4.075}, {"seed": 3, "count": null, "done": true, "steps": 68, "seconds": 2.754}, {"seed": 4, "count": null, "done": true, "steps": 69, "seconds": 2.901}, {"seed": 5, "count": null, "done": true, "steps": 125, "seconds": 5.212}, {"seed": 6, "count": null, "done": true, "steps": 74, "seconds": 2.838}, {"seed": 7, "count": null, "done": true, "steps": 144, "seconds": 6.082}, {"seed": 8, "count": null, "done": true, "steps": 120, "seconds": 5.797}, {"seed": 9, "count": null, "done": true, "steps": 113, "seconds": 4.697}, {"seed": 10, "count": null, "done": true, "steps": 46, "seconds": 2.253}, {"seed": 11, "count": null, "done": true, "steps": 53, "seconds": 2.082}, {"seed": 12, "count": null, "done": true, "steps": 116, "seconds": 4.144}, {"seed": 13, "count": null, "done": true, "steps": 82, "seconds": 2.51}, {"seed": 14, "count": null, "done": true, "steps": 32, "seconds": 0.973}, {"seed": 15, "count": null, "done": true, "steps": 31, "seconds": 0.96}, {"seed": 16, "count": null, "done": true, "steps": 31, "seconds": 1.51}, {"seed": 17, "count": null, "done": true, "steps": 82, "seconds": 3.885}, {"seed": 18, "count": null, "done": true, "steps": 88, "seconds": 4.352}, {"seed": 19, "count": null, "done": true, "steps": 72, "seconds": 3.023}, {"seed": 20, "count": null, "done": true, "steps": 92, "seconds": 4.742}, {"seed": 21, "count": null, "done": false, "steps": 1000, "seconds": 92.914, "trace": [[840, "carry", "target_block", 1.4831, 0.75], [880, "carry", "target_block", 1.4831, 0.75], [920, "carry", "target_block", 1.4831, 0.75], [960, "carry", "target_block", 1.4831, 0.75]], "state": {"target_block": {"x": 1.4263437986373901, "y": 0.47713953256607056, "width": 0.11351077258586884, "height": 0.06686045974493027}, "target_surface": {"x": 1.4588544368743896, "y": 0.0, "width": 0.15367254614830017, "height": 0.10000000149011612}}}, {"seed": 22, "count": null, "done": true, "steps": 118, "seconds": 8.737}, {"seed": 23, "count": null, "done": true, "steps": 56, "seconds": 2.228}, {"seed": 24, "count": null, "done": true, "steps": 95, "seconds": 5.981}, {"seed": 25, "count": null, "done": true, "steps": 68, "seconds": 5.635}, {"seed": 26, "count": null, "done": true, "steps": 65, "seconds": 11.604}, {"seed": 27, "count": null, "done": true, "steps": 35, "seconds": 3.671}, {"seed": 28, "count": null, "done": true, "steps": 53, "seconds": 6.939}, {"seed": 29, "count": null, "done": true, "steps": 66, "seconds": 11.788}, {"seed": 30, "count": null, "done": true, "steps": 42, "seconds": 4.653}, {"seed": 31, "count": null, "done": false, "steps": 1000, "seconds": 112.882, "trace": [[840, "carry", "target_block", 1.4989, 0.75], [880, "carry", "target_block", 1.4989, 0.75], [920, "carry", "target_block", 1.4989, 0.75], [960, "carry", "target_block", 1.4989, 0.75]], "state": {"obstruction0": {"x": 1.3593041896820068, "y": 0.10000099986791611, "width": 0.15576288104057312, "height": 0.08150506764650345}, "target_block": {"x": 1.4700844287872314, "y": 0.46752047538757324, "width": 0.05768163874745369, "height": 0.07647952437400818}, "target_surface": {"x": 1.487786889076233, "y": 0.0, "width": 0.10719655454158783, "height": 0.10000000149011612}}}, {"seed": 32, "count": null, "done": true, "steps": 113, "seconds": 16.855}, {"seed": 33, "count": null, "done": true, "steps": 78, "seconds": 11.654}, {"seed": 34, "count": null, "done": true, "steps": 41, "seconds": 2.889}, {"seed": 35, "count": null, "done": true, "steps": 39, "seconds": 3.598}, {"seed": 36, "count": null, "done": true, "steps": 57, "seconds": 7.85}, {"seed": 37, "count": null, "done": true, "steps": 41, "seconds": 4.536}, {"seed": 38, "count": null, "done": true, "steps": 32, "seconds": 3.133}, {"seed": 39, "count": null, "done": true, "steps": 89, "seconds": 13.977}, {"seed": 40, "count": null, "done": true, "steps": 90, "seconds": 11.852}, {"seed": 41, "count": null, "done": true, "steps": 36, "seconds": 5.124}, {"seed": 42, "count": null, "done": true, "steps": 36, "seconds": 3.948}, {"seed": 43, "count": null, "done": true, "steps": 41, "seconds": 5.006}, {"seed": 44, "count": null, "done": true, "steps": 88, "seconds": 12.753}, {"seed": 45, "count": null, "done": true, "steps": 121, "seconds": 17.448}, {"seed": 46, "count": null, "done": true, "steps": 45, "seconds": 4.987}, {"seed": 47, "count": null, "done": true, "steps": 48, "seconds": 4.407}, {"seed": 48, "count": null, "done": true, "steps": 34, "seconds": 3.336}, {"seed": 49, "count": null, "done": true, "steps": 28, "seconds": 2.543}, {"seed": 50, "count": null, "done": true, "steps": 92, "seconds": 11.663}, {"seed": 51, "count": null, "done": true, "steps": 44, "seconds": 4.109}, {"seed": 52, "count": null, "done": true, "steps": 107, "seconds": 13.937}, {"seed": 53, "count": null, "done": true, "steps": 123, "seconds": 17.15}, {"seed": 54, "count": null, "done": true, "steps": 46, "seconds": 3.698}, {"seed": 55, "count": null, "done": true, "steps": 28, "seconds": 4.916}, {"seed": 56, "count": null, "done": true, "steps": 89, "seconds": 8.3}, {"seed": 57, "count": null, "done": true, "steps": 29, "seconds": 2.193}, {"seed": 58, "count": null, "done": true, "steps": 87, "seconds": 7.668}, {"seed": 59, "count": null, "done": true, "steps": 87, "seconds": 10.064}, {"seed": 60, "count": null, "done": true, "steps": 34, "seconds": 2.774}, {"seed": 61, "count": null, "done": true, "steps": 83, "seconds": 7.592}, {"seed": 62, "count": null, "done": true, "steps": 85, "seconds": 7.367}, {"seed": 63, "count": null, "done": true, "steps": 64, "seconds": 5.653}, {"seed": 64, "count": null, "done": true, "steps": 39, "seconds": 3.534}, {"seed": 65, "count": null, "done": true, "steps": 34, "seconds": 2.886}, {"seed": 66, "count": null, "done": true, "steps": 79, "seconds": 7.151}, {"seed": 67, "count": null, "done": true, "steps": 76, "seconds": 7.283}, {"seed": 68, "count": null, "done": true, "steps": 73, "seconds": 5.787}, {"seed": 69, "count": null, "done": true, "steps": 48, "seconds": 3.175}, {"seed": 70, "count": null, "done": true, "steps": 83, "seconds": 6.783}, {"seed": 71, "count": null, "done": true, "steps": 72, "seconds": 7.374}, {"seed": 72, "count": null, "done": true, "steps": 120, "seconds": 12.4}, {"seed": 73, "count": null, "done": true, "steps": 88, "seconds": 8.724}, {"seed": 74, "count": null, "done": false, "steps": 1000, "seconds": 55.703, "trace": [[840, "carry", "target_block", 1.4742, 0.75], [880, "carry", "target_block", 1.4742, 0.75], [920, "carry", "target_block", 1.4742, 0.75], [960, "carry", "target_block", 1.4742, 0.75]], "state": {"target_block": {"x": 1.4489468336105347, "y": 0.3817436993122101, "width": 0.05059589818120003, "height": 0.16225633025169373}, "target_surface": {"x": 1.4740720987319946, "y": 0.0, "width": 0.09945645928382874, "height": 0.10000000149011612}}}, {"seed": 75, "count": null, "done": true, "steps": 93, "seconds": 8.527}, {"seed": 76, "count": null, "done": true, "steps": 32, "seconds": 2.748}, {"seed": 77, "count": null, "done": true, "steps": 38, "seconds": 2.682}, {"seed": 78, "count": null, "done": true, "steps": 104, "seconds": 10.402}, {"seed": 79, "count": null, "done": true, "steps": 48, "seconds": 3.314}, {"seed": 80, "count": null, "done": true, "steps": 89, "seconds": 8.52}, {"seed": 81, "count": null, "done": true, "steps": 40, "seconds": 2.107}, {"seed": 82, "count": null, "done": true, "steps": 42, "seconds": 4.155}, {"seed": 83, "count": null, "done": true, "steps": 114, "seconds": 10.423}, {"seed": 84, "count": null, "done": true, "steps": 94, "seconds": 7.226}, {"seed": 85, "count": null, "done": true, "steps": 78, "seconds": 6.817}, {"seed": 86, "count": null, "done": true, "steps": 66, "seconds": 4.408}, {"seed": 87, "count": null, "done": true, "steps": 80, "seconds": 3.569}, {"seed": 88, "count": null, "done": true, "steps": 89, "seconds": 4.623}, {"seed": 89, "count": null, "done": true, "steps": 80, "seconds": 5.228}, {"seed": 90, "count": null, "done": true, "steps": 78, "seconds": 4.76}, {"seed": 91, "count": null, "done": true, "steps": 64, "seconds": 4.489}, {"seed": 92, "count": null, "done": true, "steps": 79, "seconds": 5.136}, {"seed": 93, "count": null, "done": true, "steps": 119, "seconds": 8.261}, {"seed": 94, "count": null, "done": true, "steps": 29, "seconds": 1.422}, {"seed": 95, "count": null, "done": true, "steps": 82, "seconds": 5.118}, {"seed": 96, "count": null, "done": true, "steps": 35, "seconds": 2.161}, {"seed": 97, "count": null, "done": true, "steps": 52, "seconds": 2.568}, {"seed": 98, "count": null, "done": true, "steps": 82, "seconds": 4.105}, {"seed": 99, "count": null, "done": true, "steps": 53, "seconds": 2.941}]
\ No newline at end of file
diff --git a/results_0_30_3.json b/results_0_30_3.json
new file mode 100644
index 0000000..9e36a14
--- /dev/null
+++ b/results_0_30_3.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "count": 3, "done": true, "steps": 28, "seconds": 6.726}, {"seed": 1, "count": 3, "done": true, "steps": 134, "seconds": 26.098}, {"seed": 2, "count": 3, "done": true, "steps": 142, "seconds": 29.787}, {"seed": 3, "count": 3, "done": true, "steps": 95, "seconds": 18.011}, {"seed": 4, "count": 3, "done": true, "steps": 89, "seconds": 16.508}, {"seed": 5, "count": 3, "done": true, "steps": 32, "seconds": 5.492}, {"seed": 6, "count": 3, "done": true, "steps": 109, "seconds": 19.7}, {"seed": 7, "count": 3, "done": true, "steps": 112, "seconds": 22.661}, {"seed": 8, "count": 3, "done": true, "steps": 99, "seconds": 20.135}, {"seed": 9, "count": 3, "done": true, "steps": 122, "seconds": 24.609}, {"seed": 10, "count": 3, "done": true, "steps": 88, "seconds": 18.811}, {"seed": 11, "count": 3, "done": true, "steps": 74, "seconds": 14.882}, {"seed": 12, "count": 3, "done": true, "steps": 129, "seconds": 22.898}, {"seed": 13, "count": 3, "done": true, "steps": 125, "seconds": 22.639}, {"seed": 14, "count": 3, "done": true, "steps": 133, "seconds": 23.32}, {"seed": 15, "count": 3, "done": true, "steps": 116, "seconds": 19.871}, {"seed": 16, "count": 3, "done": true, "steps": 81, "seconds": 14.044}, {"seed": 17, "count": 3, "done": true, "steps": 124, "seconds": 19.798}, {"seed": 18, "count": 3, "done": true, "steps": 91, "seconds": 14.896}, {"seed": 19, "count": 3, "done": true, "steps": 126, "seconds": 18.652}, {"seed": 20, "count": 3, "done": true, "steps": 121, "seconds": 16.089}, {"seed": 21, "count": 3, "done": true, "steps": 102, "seconds": 12.396}, {"seed": 22, "count": 3, "done": true, "steps": 82, "seconds": 9.542}, {"seed": 23, "count": 3, "done": true, "steps": 80, "seconds": 9.97}, {"seed": 24, "count": 3, "done": true, "steps": 94, "seconds": 12.042}, {"seed": 25, "count": 3, "done": true, "steps": 149, "seconds": 20.198}, {"seed": 26, "count": 3, "done": true, "steps": 96, "seconds": 13.77}, {"seed": 27, "count": 3, "done": true, "steps": 68, "seconds": 10.102}, {"seed": 28, "count": 3, "done": true, "steps": 126, "seconds": 15.054}, {"seed": 29, "count": 3, "done": true, "steps": 123, "seconds": 13.679}]
\ No newline at end of file
```

</details>

<a id="C018"></a>
### C018 · Find exact storage gaps and add bounded elevated storage for crowded scenes

Commit `9f7ad8bf1d686239e5abac1369bb87e4f86083eb`; parents: b0fb251ccb6c924f91b47df1acf37e51484549a6. Recorded author date: 2026-09-21T22:34:13+02:00.

File roles (automatic): policy, setup/other.

- [E0065](01_timeline.md#E0065): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_9f7ad8b_approach.py) · [Exact all-file diff](evidence/diffs/C018_9f7ad8b.diff)

[Previous saved controller snapshot](evidence/versions/C017_b0fb251_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 62a8d4f..0f5f3c1 100644
--- a/approach.py
+++ b/approach.py
@@ -32,6 +32,42 @@ class GeneratedApproach:
   32     32                           np.clip(-math.pi/2-s.get(r,'theta'),-.19634954,.19634954),
   33     33                           np.clip(.2-s.get(r,'arm_joint'),-.1,.1),vac],dtype=np.float32)
   34     34  
          35 +    def storage(self, s, x, w, h):
          36 +        others=[(o,self.rect(s,o)) for o in s.get_objects(self.ot) if o!=self.obj]
          37 +        low=max(.005,.101+self.offsetx)
          38 +        high=min(1.613-w,1.517+self.offsetx)
          39 +        positions=[low,high,float(np.clip(x,low,high))]
          40 +        for o,(ox,oy,ow,oh) in others:
          41 +            positions.extend([ox+ow+.013,ox-w-.013])
          42 +        def base_clear(left,bottom):
          43 +            cx=left-self.offsetx;cy=bottom-self.offsety
          44 +            for o,(ox,oy,ow,oh) in others:
          45 +                dx=max(ox-cx,0,cx-ox-ow);dy=max(oy-cy,0,cy-oy-oh)
          46 +                if dx*dx+dy*dy<.101**2:return False
          47 +            return True
          48 +        floor=[]
          49 +        for left in positions:
          50 +            if left<low or left>high:continue
          51 +            if any(left<ox+ow+.012 and left+w>ox-.012 for o,(ox,oy,ow,oh) in others):continue
          52 +            if base_clear(left,.101):floor.append(left)
          53 +        if floor:return min(floor,key=lambda left:abs(left-x)),.101
          54 +        # Keep elevated storage outside both the destination and pickup columns.
          55 +        positions.extend(np.linspace(low,high,90))
          56 +        stacks=[]
          57 +        max_height=max([a[3] for o,a in others if o!=self.surface]+[h])
          58 +        ceiling=.89-.24-max_height
          59 +        for left in positions:
          60 +            if left<low or left>high:continue
          61 +            if any(o in (self.surface,self.block) and left<ox+ow+.04 and left+w>ox-.04 for o,(ox,oy,ow,oh) in others):continue
          62 +            bottom=.101
          63 +            for o,(ox,oy,ow,oh) in others:
          64 +                if left<ox+ow+.012 and left+w>ox-.012:bottom=max(bottom,oy+oh+.012)
          65 +            while bottom+h<=ceiling and not base_clear(left,bottom):bottom+=.01
          66 +            if bottom+h<=ceiling and bottom-self.offsety<=.89:stacks.append((left,bottom))
          67 +        if stacks:return min(stacks,key=lambda a:(a[1],abs(a[0]-x)))
          68 +        # Rare densely packed scenes: retain reachable coordinates for recovery.
          69 +        return float(np.clip(x,low,high)),max(.101,ceiling-h)
          70 +
   35     71      def get_action(self, s):
   36     72          r=self.robot; rx=s.get(r,'x'); ry=s.get(r,'y')
   37     73          for _ in range(10):
@@ -73,19 +109,7 @@ class GeneratedApproach:
   73    109                  if self.obj==self.block:
   74    110                      self.dropx=self.destx
   75    111                  else:
   76        -                    occupied=[]
   77        -                    for other in s.get_objects(self.ot):
   78        -                        if other==self.obj:continue
   79        -                        ox,oy,ow,oh=self.rect(s,other)
   80        -                        occupied.append((ox-.012,ox+ow+.012))
   81        -                    candidates=[]
   82        -                    for cx in np.linspace(.101,1.517,220):
   83        -                        left=cx-w/2
   84        -                        if left<.005 or left+w>1.613 or not .101<=left-self.offsetx<=1.517:continue
   85        -                        if any(left<b and left+w>a for a,b in occupied):continue
   86        -                        candidates.append(left)
   87        -                    self.dropx=min(candidates,key=lambda v:abs(v-x)) if candidates else .01
   88        -                    self.dropy=.101
         112 +                    self.dropx,self.dropy=self.storage(s,x,w,h)
   89    113                  if self.obj==self.block:self.dropy=s.get(self.surface,'y')+s.get(self.surface,'height')+.001
   90    114                  self.phase='carry'
   91    115              if self.phase == 'carry':
diff --git a/results_0_100_None.json b/results_0_100_None.json
index aaa8c58..3ac5188 100644
--- a/results_0_100_None.json
+++ b/results_0_100_None.json
@@ -1 +1 @@
    1        -[{"seed": 0, "count": null, "done": true, "steps": 111, "seconds": 4.328}, {"seed": 1, "count": null, "done": true, "steps": 88, "seconds": 3.003}, {"seed": 2, "count": null, "done": true, "steps": 112, "seconds": 4.075}, {"seed": 3, "count": null, "done": true, "steps": 68, "seconds": 2.754}, {"seed": 4, "count": null, "done": true, "steps": 69, "seconds": 2.901}, {"seed": 5, "count": null, "done": true, "steps": 125, "seconds": 5.212}, {"seed": 6, "count": null, "done": true, "steps": 74, "seconds": 2.838}, {"seed": 7, "count": null, "done": true, "steps": 144, "seconds": 6.082}, {"seed": 8, "count": null, "done": true, "steps": 120, "seconds": 5.797}, {"seed": 9, "count": null, "done": true, "steps": 113, "seconds": 4.697}, {"seed": 10, "count": null, "done": true, "steps": 46, "seconds": 2.253}, {"seed": 11, "count": null, "done": true, "steps": 53, "seconds": 2.082}, {"seed": 12, "count": null, "done": true, "steps": 116, "seconds": 4.144}, {"seed": 13, "count": null, "done": true, "steps": 82, "seconds": 2.51}, {"seed": 14, "count": null, "done": true, "steps": 32, "seconds": 0.973}, {"seed": 15, "count": null, "done": true, "steps": 31, "seconds": 0.96}, {"seed": 16, "count": null, "done": true, "steps": 31, "seconds": 1.51}, {"seed": 17, "count": null, "done": true, "steps": 82, "seconds": 3.885}, {"seed": 18, "count": null, "done": true, "steps": 88, "seconds": 4.352}, {"seed": 19, "count": null, "done": true, "steps": 72, "seconds": 3.023}, {"seed": 20, "count": null, "done": true, "steps": 92, "seconds": 4.742}, {"seed": 21, "count": null, "done": false, "steps": 1000, "seconds": 92.914, "trace": [[840, "carry", "target_block", 1.4831, 0.75], [880, "carry", "target_block", 1.4831, 0.75], [920, "carry", "target_block", 1.4831, 0.75], [960, "carry", "target_block", 1.4831, 0.75]], "state": {"target_block": {"x": 1.4263437986373901, "y": 0.47713953256607056, "width": 0.11351077258586884, "height": 0.06686045974493027}, "target_surface": {"x": 1.4588544368743896, "y": 0.0, "width": 0.15367254614830017, "height": 0.10000000149011612}}}, {"seed": 22, "count": null, "done": true, "steps": 118, "seconds": 8.737}, {"seed": 23, "count": null, "done": true, "steps": 56, "seconds": 2.228}, {"seed": 24, "count": null, "done": true, "steps": 95, "seconds": 5.981}, {"seed": 25, "count": null, "done": true, "steps": 68, "seconds": 5.635}, {"seed": 26, "count": null, "done": true, "steps": 65, "seconds": 11.604}, {"seed": 27, "count": null, "done": true, "steps": 35, "seconds": 3.671}, {"seed": 28, "count": null, "done": true, "steps": 53, "seconds": 6.939}, {"seed": 29, "count": null, "done": true, "steps": 66, "seconds": 11.788}, {"seed": 30, "count": null, "done": true, "steps": 42, "seconds": 4.653}, {"seed": 31, "count": null, "done": false, "steps": 1000, "seconds": 112.882, "trace": [[840, "carry", "target_block", 1.4989, 0.75], [880, "carry", "target_block", 1.4989, 0.75], [920, "carry", "target_block", 1.4989, 0.75], [960, "carry", "target_block", 1.4989, 0.75]], "state": {"obstruction0": {"x": 1.3593041896820068, "y": 0.10000099986791611, "width": 0.15576288104057312, "height": 0.08150506764650345}, "target_block": {"x": 1.4700844287872314, "y": 0.46752047538757324, "width": 0.05768163874745369, "height": 0.07647952437400818}, "target_surface": {"x": 1.487786889076233, "y": 0.0, "width": 0.10719655454158783, "height": 0.10000000149011612}}}, {"seed": 32, "count": null, "done": true, "steps": 113, "seconds": 16.855}, {"seed": 33, "count": null, "done": true, "steps": 78, "seconds": 11.654}, {"seed": 34, "count": null, "done": true, "steps": 41, "seconds": 2.889}, {"seed": 35, "count": null, "done": true, "steps": 39, "seconds": 3.598}, {"seed": 36, "count": null, "done": true, "steps": 57, "seconds": 7.85}, {"seed": 37, "count": null, "done": true, "steps": 41, "seconds": 4.536}, {"seed": 38, "count": null, "done": true, "steps": 32, "seconds": 3.133}, {"seed": 39, "count": null, "done": true, "steps": 89, "seconds": 13.977}, {"seed": 40, "count": null, "done": true, "steps": 90, "seconds": 11.852}, {"seed": 41, "count": null, "done": true, "steps": 36, "seconds": 5.124}, {"seed": 42, "count": null, "done": true, "steps": 36, "seconds": 3.948}, {"seed": 43, "count": null, "done": true, "steps": 41, "seconds": 5.006}, {"seed": 44, "count": null, "done": true, "steps": 88, "seconds": 12.753}, {"seed": 45, "count": null, "done": true, "steps": 121, "seconds": 17.448}, {"seed": 46, "count": null, "done": true, "steps": 45, "seconds": 4.987}, {"seed": 47, "count": null, "done": true, "steps": 48, "seconds": 4.407}, {"seed": 48, "count": null, "done": true, "steps": 34, "seconds": 3.336}, {"seed": 49, "count": null, "done": true, "steps": 28, "seconds": 2.543}, {"seed": 50, "count": null, "done": true, "steps": 92, "seconds": 11.663}, {"seed": 51, "count": null, "done": true, "steps": 44, "seconds": 4.109}, {"seed": 52, "count": null, "done": true, "steps": 107, "seconds": 13.937}, {"seed": 53, "count": null, "done": true, "steps": 123, "seconds": 17.15}, {"seed": 54, "count": null, "done": true, "steps": 46, "seconds": 3.698}, {"seed": 55, "count": null, "done": true, "steps": 28, "seconds": 4.916}, {"seed": 56, "count": null, "done": true, "steps": 89, "seconds": 8.3}, {"seed": 57, "count": null, "done": true, "steps": 29, "seconds": 2.193}, {"seed": 58, "count": null, "done": true, "steps": 87, "seconds": 7.668}, {"seed": 59, "count": null, "done": true, "steps": 87, "seconds": 10.064}, {"seed": 60, "count": null, "done": true, "steps": 34, "seconds": 2.774}, {"seed": 61, "count": null, "done": true, "steps": 83, "seconds": 7.592}, {"seed": 62, "count": null, "done": true, "steps": 85, "seconds": 7.367}, {"seed": 63, "count": null, "done": true, "steps": 64, "seconds": 5.653}, {"seed": 64, "count": null, "done": true, "steps": 39, "seconds": 3.534}, {"seed": 65, "count": null, "done": true, "steps": 34, "seconds": 2.886}, {"seed": 66, "count": null, "done": true, "steps": 79, "seconds": 7.151}, {"seed": 67, "count": null, "done": true, "steps": 76, "seconds": 7.283}, {"seed": 68, "count": null, "done": true, "steps": 73, "seconds": 5.787}, {"seed": 69, "count": null, "done": true, "steps": 48, "seconds": 3.175}, {"seed": 70, "count": null, "done": true, "steps": 83, "seconds": 6.783}, {"seed": 71, "count": null, "done": true, "steps": 72, "seconds": 7.374}, {"seed": 72, "count": null, "done": true, "steps": 120, "seconds": 12.4}, {"seed": 73, "count": null, "done": true, "steps": 88, "seconds": 8.724}, {"seed": 74, "count": null, "done": false, "steps": 1000, "seconds": 55.703, "trace": [[840, "carry", "target_block", 1.4742, 0.75], [880, "carry", "target_block", 1.4742, 0.75], [920, "carry", "target_block", 1.4742, 0.75], [960, "carry", "target_block", 1.4742, 0.75]], "state": {"target_block": {"x": 1.4489468336105347, "y": 0.3817436993122101, "width": 0.05059589818120003, "height": 0.16225633025169373}, "target_surface": {"x": 1.4740720987319946, "y": 0.0, "width": 0.09945645928382874, "height": 0.10000000149011612}}}, {"seed": 75, "count": null, "done": true, "steps": 93, "seconds": 8.527}, {"seed": 76, "count": null, "done": true, "steps": 32, "seconds": 2.748}, {"seed": 77, "count": null, "done": true, "steps": 38, "seconds": 2.682}, {"seed": 78, "count": null, "done": true, "steps": 104, "seconds": 10.402}, {"seed": 79, "count": null, "done": true, "steps": 48, "seconds": 3.314}, {"seed": 80, "count": null, "done": true, "steps": 89, "seconds": 8.52}, {"seed": 81, "count": null, "done": true, "steps": 40, "seconds": 2.107}, {"seed": 82, "count": null, "done": true, "steps": 42, "seconds": 4.155}, {"seed": 83, "count": null, "done": true, "steps": 114, "seconds": 10.423}, {"seed": 84, "count": null, "done": true, "steps": 94, "seconds": 7.226}, {"seed": 85, "count": null, "done": true, "steps": 78, "seconds": 6.817}, {"seed": 86, "count": null, "done": true, "steps": 66, "seconds": 4.408}, {"seed": 87, "count": null, "done": true, "steps": 80, "seconds": 3.569}, {"seed": 88, "count": null, "done": true, "steps": 89, "seconds": 4.623}, {"seed": 89, "count": null, "done": true, "steps": 80, "seconds": 5.228}, {"seed": 90, "count": null, "done": true, "steps": 78, "seconds": 4.76}, {"seed": 91, "count": null, "done": true, "steps": 64, "seconds": 4.489}, {"seed": 92, "count": null, "done": true, "steps": 79, "seconds": 5.136}, {"seed": 93, "count": null, "done": true, "steps": 119, "seconds": 8.261}, {"seed": 94, "count": null, "done": true, "steps": 29, "seconds": 1.422}, {"seed": 95, "count": null, "done": true, "steps": 82, "seconds": 5.118}, {"seed": 96, "count": null, "done": true, "steps": 35, "seconds": 2.161}, {"seed": 97, "count": null, "done": true, "steps": 52, "seconds": 2.568}, {"seed": 98, "count": null, "done": true, "steps": 82, "seconds": 4.105}, {"seed": 99, "count": null, "done": true, "steps": 53, "seconds": 2.941}]
\ No newline at end of file
           1 +[{"seed": 0, "count": null, "done": true, "steps": 75, "seconds": 3.233}, {"seed": 1, "count": null, "done": true, "steps": 60, "seconds": 2.544}, {"seed": 2, "count": null, "done": true, "steps": 77, "seconds": 3.379}, {"seed": 3, "count": null, "done": true, "steps": 53, "seconds": 2.905}, {"seed": 4, "count": null, "done": true, "steps": 57, "seconds": 2.843}, {"seed": 5, "count": null, "done": true, "steps": 91, "seconds": 4.274}, {"seed": 6, "count": null, "done": true, "steps": 57, "seconds": 2.413}, {"seed": 7, "count": null, "done": true, "steps": 109, "seconds": 5.31}, {"seed": 8, "count": null, "done": true, "steps": 75, "seconds": 3.583}, {"seed": 9, "count": null, "done": true, "steps": 83, "seconds": 3.205}, {"seed": 10, "count": null, "done": true, "steps": 36, "seconds": 2.382}, {"seed": 11, "count": null, "done": true, "steps": 41, "seconds": 2.174}, {"seed": 12, "count": null, "done": true, "steps": 77, "seconds": 3.689}, {"seed": 13, "count": null, "done": true, "steps": 57, "seconds": 3.314}, {"seed": 14, "count": null, "done": true, "steps": 27, "seconds": 1.311}, {"seed": 15, "count": null, "done": true, "steps": 22, "seconds": 0.929}, {"seed": 16, "count": null, "done": true, "steps": 25, "seconds": 1.208}, {"seed": 17, "count": null, "done": true, "steps": 63, "seconds": 2.59}, {"seed": 18, "count": null, "done": true, "steps": 51, "seconds": 2.179}, {"seed": 19, "count": null, "done": true, "steps": 49, "seconds": 1.544}, {"seed": 20, "count": null, "done": true, "steps": 63, "seconds": 2.337}, {"seed": 21, "count": null, "done": true, "steps": 49, "seconds": 1.518}, {"seed": 22, "count": null, "done": true, "steps": 89, "seconds": 5.272}, {"seed": 23, "count": null, "done": true, "steps": 40, "seconds": 1.805}, {"seed": 24, "count": null, "done": true, "steps": 50, "seconds": 2.876}, {"seed": 25, "count": null, "done": true, "steps": 49, "seconds": 3.123}, {"seed": 26, "count": null, "done": true, "steps": 50, "seconds": 4.454}, {"seed": 27, "count": null, "done": true, "steps": 18, "seconds": 1.019}, {"seed": 28, "count": null, "done": true, "steps": 47, "seconds": 3.086}, {"seed": 29, "count": null, "done": true, "steps": 39, "seconds": 3.788}, {"seed": 30, "count": null, "done": true, "steps": 23, "seconds": 1.233}, {"seed": 31, "count": null, "done": true, "steps": 51, "seconds": 3.933}, {"seed": 32, "count": null, "done": true, "steps": 84, "seconds": 8.966}, {"seed": 33, "count": null, "done": true, "steps": 59, "seconds": 6.527}, {"seed": 34, "count": null, "done": true, "steps": 35, "seconds": 2.214}, {"seed": 35, "count": null, "done": true, "steps": 33, "seconds": 2.29}, {"seed": 36, "count": null, "done": true, "steps": 45, "seconds": 4.108}, {"seed": 37, "count": null, "done": true, "steps": 29, "seconds": 2.155}, {"seed": 38, "count": null, "done": true, "steps": 21, "seconds": 1.401}, {"seed": 39, "count": null, "done": true, "steps": 55, "seconds": 5.246}, {"seed": 40, "count": null, "done": true, "steps": 59, "seconds": 4.315}, {"seed": 41, "count": null, "done": true, "steps": 30, "seconds": 2.61}, {"seed": 42, "count": null, "done": true, "steps": 32, "seconds": 2.221}, {"seed": 43, "count": null, "done": true, "steps": 26, "seconds": 1.551}, {"seed": 44, "count": null, "done": true, "steps": 63, "seconds": 6.5}, {"seed": 45, "count": null, "done": true, "steps": 79, "seconds": 7.5}, {"seed": 46, "count": null, "done": true, "steps": 36, "seconds": 3.161}, {"seed": 47, "count": null, "done": true, "steps": 41, "seconds": 2.885}, {"seed": 48, "count": null, "done": true, "steps": 22, "seconds": 1.111}, {"seed": 49, "count": null, "done": true, "steps": 24, "seconds": 1.036}, {"seed": 50, "count": null, "done": true, "steps": 66, "seconds": 5.796}, {"seed": 51, "count": null, "done": true, "steps": 35, "seconds": 2.529}, {"seed": 52, "count": null, "done": true, "steps": 64, "seconds": 6.595}, {"seed": 53, "count": null, "done": true, "steps": 78, "seconds": 7.849}, {"seed": 54, "count": null, "done": true, "steps": 28, "seconds": 1.97}, {"seed": 55, "count": null, "done": true, "steps": 22, "seconds": 2.634}, {"seed": 56, "count": null, "done": true, "steps": 62, "seconds": 5.011}, {"seed": 57, "count": null, "done": true, "steps": 20, "seconds": 1.336}, {"seed": 58, "count": null, "done": true, "steps": 53, "seconds": 4.204}, {"seed": 59, "count": null, "done": true, "steps": 62, "seconds": 5.858}, {"seed": 60, "count": null, "done": true, "steps": 23, "seconds": 1.447}, {"seed": 61, "count": null, "done": true, "steps": 70, "seconds": 5.928}, {"seed": 62, "count": null, "done": true, "steps": 66, "seconds": 5.443}, {"seed": 63, "count": null, "done": true, "steps": 35, "seconds": 3.271}, {"seed": 64, "count": null, "done": true, "steps": 29, "seconds": 2.093}, {"seed": 65, "count": null, "done": true, "steps": 17, "seconds": 1.001}, {"seed": 66, "count": null, "done": true, "steps": 55, "seconds": 4.992}, {"seed": 67, "count": null, "done": true, "steps": 52, "seconds": 5.352}, {"seed": 68, "count": null, "done": true, "steps": 43, "seconds": 4.186}, {"seed": 69, "count": null, "done": true, "steps": 36, "seconds": 2.941}, {"seed": 70, "count": null, "done": true, "steps": 38, "seconds": 4.331}, {"seed": 71, "count": null, "done": true, "steps": 40, "seconds": 3.909}, {"seed": 72, "count": null, "done": true, "steps": 96, "seconds": 9.054}, {"seed": 73, "count": null, "done": true, "steps": 65, "seconds": 6.339}, {"seed": 74, "count": null, "done": true, "steps": 25, "seconds": 1.678}, {"seed": 75, "count": null, "done": true, "steps": 71, "seconds": 4.967}, {"seed": 76, "count": null, "done": true, "steps": 31, "seconds": 2.283}, {"seed": 77, "count": null, "done": true, "steps": 19, "seconds": 1.07}, {"seed": 78, "count": null, "done": true, "steps": 74, "seconds": 5.837}, {"seed": 79, "count": null, "done": true, "steps": 34, "seconds": 1.609}, {"seed": 80, "count": null, "done": true, "steps": 63, "seconds": 5.295}, {"seed": 81, "count": null, "done": true, "steps": 22, "seconds": 1.052}, {"seed": 82, "count": null, "done": true, "steps": 35, "seconds": 3.906}, {"seed": 83, "count": null, "done": true, "steps": 83, "seconds": 8.428}, {"seed": 84, "count": null, "done": true, "steps": 58, "seconds": 4.456}, {"seed": 85, "count": null, "done": true, "steps": 53, "seconds": 5.372}, {"seed": 86, "count": null, "done": true, "steps": 44, "seconds": 4.436}, {"seed": 87, "count": null, "done": true, "steps": 48, "seconds": 3.155}, {"seed": 88, "count": null, "done": true, "steps": 57, "seconds": 4.411}, {"seed": 89, "count": null, "done": true, "steps": 56, "seconds": 5.168}, {"seed": 90, "count": null, "done": true, "steps": 64, "seconds": 4.991}, {"seed": 91, "count": null, "done": true, "steps": 42, "seconds": 4.244}, {"seed": 92, "count": null, "done": true, "steps": 47, "seconds": 3.469}, {"seed": 93, "count": null, "done": true, "steps": 65, "seconds": 6.069}, {"seed": 94, "count": null, "done": true, "steps": 25, "seconds": 1.755}, {"seed": 95, "count": null, "done": true, "steps": 59, "seconds": 4.336}, {"seed": 96, "count": null, "done": true, "steps": 30, "seconds": 2.922}, {"seed": 97, "count": null, "done": true, "steps": 33, "seconds": 1.845}, {"seed": 98, "count": null, "done": true, "steps": 54, "seconds": 3.998}, {"seed": 99, "count": null, "done": true, "steps": 44, "seconds": 3.579}]
\ No newline at end of file
diff --git a/results_30_30_3.json b/results_30_30_3.json
new file mode 100644
index 0000000..2b5fc1f
--- /dev/null
+++ b/results_30_30_3.json
@@ -0,0 +1 @@
           1 +[{"seed": 30, "count": 3, "done": true, "steps": 36, "seconds": 3.63}, {"seed": 31, "count": 3, "done": true, "steps": 58, "seconds": 6.123}, {"seed": 32, "count": 3, "done": true, "steps": 83, "seconds": 10.254}, {"seed": 33, "count": 3, "done": true, "steps": 51, "seconds": 6.593}, {"seed": 34, "count": 3, "done": true, "steps": 64, "seconds": 7.621}, {"seed": 35, "count": 3, "done": true, "steps": 108, "seconds": 13.979}, {"seed": 36, "count": 3, "done": true, "steps": 104, "seconds": 12.405}, {"seed": 37, "count": 3, "done": true, "steps": 52, "seconds": 6.356}, {"seed": 38, "count": 3, "done": true, "steps": 67, "seconds": 7.769}, {"seed": 39, "count": 3, "done": true, "steps": 102, "seconds": 13.381}, {"seed": 40, "count": 3, "done": true, "steps": 54, "seconds": 6.222}, {"seed": 41, "count": 3, "done": true, "steps": 68, "seconds": 9.101}, {"seed": 42, "count": 3, "done": false, "steps": 1000, "seconds": 83.999, "trace": [[840, "lift", "obstruction2", 1.2585, 0.5931], [880, "lift", "obstruction2", 1.2585, 0.4931], [920, "down", "obstruction2", 1.2585, 0.4431], [960, "down", "obstruction2", 1.2585, 0.5431]], "state": {"obstruction0": {"x": 1.0754507780075073, "y": 0.10100003331899643, "width": 0.06841368973255157, "height": 0.1746668964624405}, "obstruction1": {"x": 1.2862571477890015, "y": 0.10000099986791611, "width": 0.07946520298719406, "height": 0.09654854983091354}, "obstruction2": {"x": 1.2324990034103394, "y": 0.10000099986791611, "width": 0.052090443670749664, "height": 0.08444840461015701}, "target_block": {"x": 0.5479981303215027, "y": 0.10000099986791611, "width": 0.10604865849018097, "height": 0.0641700029373169}, "target_surface": {"x": 1.1589730978012085, "y": 0.0, "width": 0.1332777738571167, "height": 0.10000000149011612}}}, {"seed": 43, "count": 3, "done": true, "steps": 73, "seconds": 9.465}, {"seed": 44, "count": 3, "done": true, "steps": 63, "seconds": 7.603}, {"seed": 45, "count": 3, "done": true, "steps": 87, "seconds": 9.516}, {"seed": 46, "count": 3, "done": true, "steps": 123, "seconds": 13.91}, {"seed": 47, "count": 3, "done": true, "steps": 98, "seconds": 11.332}, {"seed": 48, "count": 3, "done": true, "steps": 57, "seconds": 5.955}, {"seed": 49, "count": 3, "done": true, "steps": 71, "seconds": 7.631}, {"seed": 50, "count": 3, "done": true, "steps": 113, "seconds": 12.469}, {"seed": 51, "count": 3, "done": true, "steps": 96, "seconds": 10.851}, {"seed": 52, "count": 3, "done": true, "steps": 67, "seconds": 7.899}, {"seed": 53, "count": 3, "done": true, "steps": 69, "seconds": 8.099}, {"seed": 54, "count": 3, "done": true, "steps": 95, "seconds": 10.237}, {"seed": 55, "count": 3, "done": true, "steps": 63, "seconds": 6.511}, {"seed": 56, "count": 3, "done": true, "steps": 99, "seconds": 5.058}, {"seed": 57, "count": 3, "done": true, "steps": 100, "seconds": 4.557}, {"seed": 58, "count": 3, "done": true, "steps": 91, "seconds": 3.746}, {"seed": 59, "count": 3, "done": true, "steps": 52, "seconds": 0.936}]
\ No newline at end of file
```

</details>

<a id="C019"></a>
### C019 · Offset narrow-object grasps to clear taller neighboring rectangles

Commit `78e4e2bf8f7a3752880afe0865caa83244da7350`; parents: 9f7ad8bf1d686239e5abac1369bb87e4f86083eb. Recorded author date: 2026-09-21T22:35:14+02:00.

File roles (automatic): policy, setup/other.

- [E0083](01_timeline.md#E0083): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_78e4e2b_approach.py) · [Exact all-file diff](evidence/diffs/C019_78e4e2b.diff)

[Previous saved controller snapshot](evidence/versions/C018_9f7ad8b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0f5f3c1..a4da837 100644
--- a/approach.py
+++ b/approach.py
@@ -32,6 +32,25 @@ class GeneratedApproach:
   32     32                           np.clip(-math.pi/2-s.get(r,'theta'),-.19634954,.19634954),
   33     33                           np.clip(.2-s.get(r,'arm_joint'),-.1,.1),vac],dtype=np.float32)
   34     34  
          35 +    def grasp_position(self, s, obj, preferred):
          36 +        x,y,w,h=self.rect(s,obj)
          37 +        others=[self.rect(s,o) for o in s.get_objects(self.ot) if o!=obj]
          38 +        candidates=[preferred,x+w/2,x+.005,x+w-.005,.101,1.517]
          39 +        for ox,oy,ow,oh in others:
          40 +            candidates.extend([ox-.041,ox+ow+.041])
          41 +        valid=[]
          42 +        for cx in candidates:
          43 +            if not .101<=cx<=1.517 or cx+.035<x+.006 or cx-.035>x+w-.006:continue
          44 +            cy=y+h+.206
          45 +            collision=False
          46 +            for ox,oy,ow,oh in others:
          47 +                dx=max(ox-cx,0,cx-ox-ow);dy=max(oy-cy,0,cy-oy-oh)
          48 +                if dx*dx+dy*dy<.101**2:collision=True;break
          49 +                if ox<cx+.04 and ox+ow>cx-.04 and oy<y+h+.02 and oy+oh>y+h-.005:
          50 +                    collision=True;break
          51 +            if not collision:valid.append(cx)
          52 +        return min(valid,key=lambda cx:abs(cx-preferred)) if valid else float(np.clip(preferred,.101,1.517))
          53 +
   35     54      def storage(self, s, x, w, h):
   36     55          others=[(o,self.rect(s,o)) for o in s.get_objects(self.ot) if o!=self.obj]
   37     56          low=max(.005,.101+self.offsetx)
@@ -89,7 +108,7 @@ class GeneratedApproach:
   89    108              if self.phase == 'above':
   90    109                  if ry<self.emptyheight-.001: return self.action(s,y=self.emptyheight)
   91    110                  grasp_shift=min(0,1.516-(self.destx+w/2)) if self.obj==self.block else 0
   92        -                grasp_x=float(np.clip(x+w/2+grasp_shift,.101,1.517))
         111 +                grasp_x=self.grasp_position(s,self.obj,x+w/2+grasp_shift)
   93    112                  if abs(rx-grasp_x)>.001: return self.action(s,x=grasp_x,y=self.emptyheight)
   94    113                  self.phase='down'; self.n=0; self.last_down=None
   95    114              if self.phase == 'down':
diff --git a/results_0_1_4.json b/results_0_1_4.json
new file mode 100644
index 0000000..4465fdb
--- /dev/null
+++ b/results_0_1_4.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "count": 4, "done": true, "steps": 74, "seconds": 0.368}]
\ No newline at end of file
```

</details>

<a id="C020"></a>
### C020 · Preserve destination reachability when selecting offset target grasps

Commit `040eb1e8dae08155b1c6a8c5559e2a79e1e95e58`; parents: 78e4e2bf8f7a3752880afe0865caa83244da7350. Recorded author date: 2026-09-21T22:35:34+02:00.

File roles (automatic): policy, setup/other.

- [E0075](01_timeline.md#E0075): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_040eb1e_approach.py) · [Exact all-file diff](evidence/diffs/C020_040eb1e.diff)

[Previous saved controller snapshot](evidence/versions/C019_78e4e2b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a4da837..a458773 100644
--- a/approach.py
+++ b/approach.py
@@ -36,11 +36,13 @@ class GeneratedApproach:
   36     36          x,y,w,h=self.rect(s,obj)
   37     37          others=[self.rect(s,o) for o in s.get_objects(self.ot) if o!=obj]
   38     38          candidates=[preferred,x+w/2,x+.005,x+w-.005,.101,1.517]
          39 +        if obj==self.block:candidates.extend([x+1.516-self.destx,x+.102-self.destx])
   39     40          for ox,oy,ow,oh in others:
   40     41              candidates.extend([ox-.041,ox+ow+.041])
   41     42          valid=[]
   42     43          for cx in candidates:
   43     44              if not .101<=cx<=1.517 or cx+.035<x+.006 or cx-.035>x+w-.006:continue
          45 +            if obj==self.block and not .101<=self.destx-x+cx<=1.517:continue
   44     46              cy=y+h+.206
   45     47              collision=False
   46     48              for ox,oy,ow,oh in others:
diff --git a/results_42_1_3.json b/results_42_1_3.json
new file mode 100644
index 0000000..7d1d202
--- /dev/null
+++ b/results_42_1_3.json
@@ -0,0 +1 @@
           1 +[{"seed": 42, "count": 3, "done": true, "steps": 81, "seconds": 0.439}]
\ No newline at end of file
```

</details>

<a id="C021"></a>
### C021 · Measure policy computation separately from remote environment latency

Commit `9f9d82105d22817d4b76068845c7ee06149a185a`; parents: 040eb1e8dae08155b1c6a8c5559e2a79e1e95e58. Recorded author date: 2026-09-21T22:35:57+02:00.

File roles (automatic): diagnostic/test.

- [E0072](01_timeline.md#E0072): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C021_9f9d821.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_batch.py b/test_batch.py
index 2ac5088..83fb6f6 100644
--- a/test_batch.py
+++ b/test_batch.py
@@ -10,12 +10,13 @@ def run(seed):
   10     10   try:
   11     11    s,i=e.reset(seed=seed,options={'object_count':count} if count is not None else None)
   12     12    p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
   13        -  st=time.time();trace=[]
          13 +  st=time.time();trace=[];policy_seconds=0.0
   14     14    for t in range(e.max_steps):
   15        -   a=p.get_action(s);s,r,d,tr,i=e.step(a)
          15 +   tick=time.perf_counter();a=p.get_action(s);policy_seconds+=time.perf_counter()-tick
          16 +   s,r,d,tr,i=e.step(a)
   16     17     if t%40==0:trace.append([t,p.phase,p.obj.name if p.obj else '',round(s.get(p.robot,'x'),4),round(s.get(p.robot,'y'),4)])
   17     18     if d or tr:break
   18        -  out=dict(seed=seed,count=count,done=d,steps=t+1,seconds=round(time.time()-st,3))
          19 +  out=dict(seed=seed,count=count,done=d,steps=t+1,seconds=round(time.time()-st,3),policy_seconds=round(policy_seconds,4))
   19     20    if not d:out['trace']=trace[-4:];out['state']={o.name:{f:s.get(o,f) for f in ('x','y','width','height')} for o in s.get_objects(p.ot)}
   20     21    print(seed, "OK" if d else "FAIL", t+1, flush=True)
   21     22    return out
```

</details>

<a id="C022"></a>
### C022 · Search adjacent-obstruction robot clearance risks at final placement

Commit `9cc4359ae6be444b999d672b0d53fd18dd80ee7e`; parents: 9f9d82105d22817d4b76068845c7ee06149a185a. Recorded author date: 2026-09-21T22:38:13+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C022_9cc4359.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_adjacent.py b/probe_adjacent.py
new file mode 100644
index 0000000..f190994
--- /dev/null
+++ b/probe_adjacent.py
@@ -0,0 +1,27 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import json
           4 +
           5 +e=make_env(); cases=[]
           6 +for seed in range(1000,1201):
           7 + s,_=e.reset(seed=seed)
           8 + p=GeneratedApproach(e.action_space,e.observation_space,{})
           9 + p.reset(s,{})
          10 + p.get_action(s)
          11 + bx,by,bw,bh=p.rect(s,p.block)
          12 + cx=min(1.516,p.destx+bw/2);cy=.1+bh+.206
          13 + for o in s.get_objects(p.ot):
          14 +  if o in (p.block,p.surface):continue
          15 +  ox,oy,ow,oh=p.rect(s,o)
          16 +  if ox<p.destx+bw+.004 and ox+ow>p.destx-.004:continue
          17 +  dx=max(ox-cx,0,cx-ox-ow);dy=max(oy-cy,0,cy-oy-oh)
          18 +  if dx*dx+dy*dy<.101**2:
          19 +   cases.append(seed);print('CASE',seed,'target',bw,bh,'dest',p.destx,'neighbor',o.name,[ox,oy,ow,oh],flush=True);break
          20 +print('FOUND',cases,flush=True)
          21 +for seed in cases[:5]:
          22 + s,_=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,{})
          23 + for t in range(e.max_steps):
          24 +  a=p.get_action(s);s,r,term,trunc,_=e.step(a)
          25 +  if term or trunc:break
          26 + print('RESULT',seed,term,t+1,p.phase,flush=True)
          27 +e.close()
```

</details>

<a id="C023"></a>
### C023 · Emit complete failure diagnostics immediately during seed sweeps

Commit `082e08bdb48075087702a9db5278ad88a0ca1516`; parents: 9cc4359ae6be444b999d672b0d53fd18dd80ee7e. Recorded author date: 2026-09-21T22:38:22+02:00.

File roles (automatic): diagnostic/test.

- [E0079](01_timeline.md#E0079): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C023_082e08b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_batch.py b/test_batch.py
index 83fb6f6..74f8e72 100644
--- a/test_batch.py
+++ b/test_batch.py
@@ -19,6 +19,7 @@ def run(seed):
   19     19    out=dict(seed=seed,count=count,done=d,steps=t+1,seconds=round(time.time()-st,3),policy_seconds=round(policy_seconds,4))
   20     20    if not d:out['trace']=trace[-4:];out['state']={o.name:{f:s.get(o,f) for f in ('x','y','width','height')} for o in s.get_objects(p.ot)}
   21     21    print(seed, "OK" if d else "FAIL", t+1, flush=True)
          22 +  if not d:print(out,flush=True)
   22     23    return out
   23     24   except Exception as ex:return dict(seed=seed,count=count,error=str(ex))
   24     25   finally:e.close()
```

</details>

<a id="C024"></a>
### C024 · Check complete carried geometry for placement and storage, including offset grippers

Commit `6cb4e133921a64475bda4ef9793dca12762318d8`; parents: 082e08bdb48075087702a9db5278ad88a0ca1516. Recorded author date: 2026-09-21T22:41:34+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0088](01_timeline.md#E0088): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C024_6cb4e13_approach.py) · [Exact all-file diff](evidence/diffs/C024_6cb4e13.diff)

[Previous saved controller snapshot](evidence/versions/C020_040eb1e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a458773..389a116 100644
--- a/approach.py
+++ b/approach.py
@@ -53,22 +53,41 @@ class GeneratedApproach:
   53     53              if not collision:valid.append(cx)
   54     54          return min(valid,key=lambda cx:abs(cx-preferred)) if valid else float(np.clip(preferred,.101,1.517))
   55     55  
          56 +    def placement_collisions(self, s, obj, left, bottom, offsetx, offsety):
          57 +        _,_,w,h=self.rect(s,obj)
          58 +        cx=left-offsetx;cy=bottom-offsety
          59 +        parts=[(left,bottom,left+w,bottom+h),
          60 +               (cx-.037,cy-.207,cx+.037,cy-.193),
          61 +               (cx-.008,cy-.2,cx+.008,cy)]
          62 +        blocked=[]
          63 +        for other in s.get_objects(self.ot):
          64 +            if other==obj:continue
          65 +            ox,oy,ow,oh=self.rect(s,other)
          66 +            dx=max(ox-cx,0,cx-ox-ow);dy=max(oy-cy,0,cy-oy-oh)
          67 +            collision=dx*dx+dy*dy<.101**2
          68 +            for x0,y0,x1,y1 in parts:
          69 +                if x0<ox+ow and x1>ox and y0<oy+oh and y1>oy:
          70 +                    collision=True;break
          71 +            if collision:blocked.append(other)
          72 +        return blocked
          73 +
   56     74      def storage(self, s, x, w, h):
   57     75          others=[(o,self.rect(s,o)) for o in s.get_objects(self.ot) if o!=self.obj]
          76 +        bx,by,bw,bh=self.rect(s,self.block)
          77 +        goalcx=self.destx-bx+self.target_grasp
          78 +        reserve_left=min(self.destx,goalcx-.042)
          79 +        reserve_right=max(self.destx+bw,goalcx+.042)
   58     80          low=max(.005,.101+self.offsetx)
   59     81          high=min(1.613-w,1.517+self.offsetx)
   60     82          positions=[low,high,float(np.clip(x,low,high))]
   61     83          for o,(ox,oy,ow,oh) in others:
   62     84              positions.extend([ox+ow+.013,ox-w-.013])
   63     85          def base_clear(left,bottom):
   64        -            cx=left-self.offsetx;cy=bottom-self.offsety
   65        -            for o,(ox,oy,ow,oh) in others:
   66        -                dx=max(ox-cx,0,cx-ox-ow);dy=max(oy-cy,0,cy-oy-oh)
   67        -                if dx*dx+dy*dy<.101**2:return False
   68        -            return True
          86 +            return not self.placement_collisions(s,self.obj,left,bottom,self.offsetx,self.offsety)
   69     87          floor=[]
   70     88          for left in positions:
   71     89              if left<low or left>high:continue
          90 +            if left<reserve_right+.008 and left+w>reserve_left-.008:continue
   72     91              if any(left<ox+ow+.012 and left+w>ox-.012 for o,(ox,oy,ow,oh) in others):continue
   73     92              if base_clear(left,.101):floor.append(left)
   74     93          if floor:return min(floor,key=lambda left:abs(left-x)),.101
@@ -79,6 +98,7 @@ class GeneratedApproach:
   79     98          ceiling=.89-.24-max_height
   80     99          for left in positions:
   81    100              if left<low or left>high:continue
         101 +            if left<reserve_right+.02 and left+w>reserve_left-.02:continue
   82    102              if any(o in (self.surface,self.block) and left<ox+ow+.04 and left+w>ox-.04 for o,(ox,oy,ow,oh) in others):continue
   83    103              bottom=.101
   84    104              for o,(ox,oy,ow,oh) in others:
@@ -95,13 +115,16 @@ class GeneratedApproach:
   95    115              if self.phase == 'select':
   96    116                  bx,by,bw,bh=self.rect(s,self.block)
   97    117                  sx,sy,sw,sh=self.rect(s,self.surface)
   98        -                obs=[o for o in s.get_objects(self.ot) if o not in (self.block,self.surface)]
   99    118                  choices=np.linspace(sx+.001,sx+sw-bw-.001,21)
  100        -                def cost(left):
  101        -                    overlap=[o for o in obs if s.get(o,'x')<left+bw+.004 and s.get(o,'x')+s.get(o,'width')>left-.004 and s.get(o,'y')<sy+sh+bh+.04]
  102        -                    return (max(0,left+bw/2-1.516),len(overlap),abs(left-(sx+(sw-bw)/2)))
  103        -                self.destx=min(choices,key=cost)
  104        -                blocking=[o for o in obs if s.get(o,'x')<self.destx+bw+.004 and s.get(o,'x')+s.get(o,'width')>self.destx-.004 and s.get(o,'y')<sy+sh+bh+.04]
         119 +                plans=[]
         120 +                for left in choices:
         121 +                    self.destx=left
         122 +                    preferred=bx+bw/2+min(0,1.516-(left+bw/2))
         123 +                    gx=self.grasp_position(s,self.block,preferred)
         124 +                    blocked=[o for o in self.placement_collisions(s,self.block,left,sy+sh+.021,bx-gx,-bh-.206) if o!=self.surface]
         125 +                    reach=max(0,left-bx+gx-1.517,.101-(left-bx+gx))
         126 +                    plans.append(((reach,len(blocked),abs(left-(sx+(sw-bw)/2))),left,gx,blocked))
         127 +                _,self.destx,self.target_grasp,blocking=min(plans,key=lambda p:p[0])
  105    128                  self.obj=max(blocking,key=lambda o:s.get(o,'y')+s.get(o,'height')) if blocking else self.block
  106    129                  self.emptyheight=min(.75,max(s.get(o,'y')+s.get(o,'height') for o in s.get_objects(self.ot))+.225)
  107    130                  self.carryheight=min(.89,self.emptyheight+s.get(self.obj,'height')+.008)
@@ -110,7 +133,7 @@ class GeneratedApproach:
  110    133              if self.phase == 'above':
  111    134                  if ry<self.emptyheight-.001: return self.action(s,y=self.emptyheight)
  112    135                  grasp_shift=min(0,1.516-(self.destx+w/2)) if self.obj==self.block else 0
  113        -                grasp_x=self.grasp_position(s,self.obj,x+w/2+grasp_shift)
         136 +                grasp_x=self.target_grasp if self.obj==self.block else self.grasp_position(s,self.obj,x+w/2)
  114    137                  if abs(rx-grasp_x)>.001: return self.action(s,x=grasp_x,y=self.emptyheight)
  115    138                  self.phase='down'; self.n=0; self.last_down=None
  116    139              if self.phase == 'down':
@@ -131,7 +154,7 @@ class GeneratedApproach:
  131    154                      self.dropx=self.destx
  132    155                  else:
  133    156                      self.dropx,self.dropy=self.storage(s,x,w,h)
  134        -                if self.obj==self.block:self.dropy=s.get(self.surface,'y')+s.get(self.surface,'height')+.001
         157 +                if self.obj==self.block:self.dropy=s.get(self.surface,'y')+s.get(self.surface,'height')+.021
  135    158                  self.phase='carry'
  136    159              if self.phase == 'carry':
  137    160                  goal=self.dropx-self.offsetx
diff --git a/probe_adjacent.log b/probe_adjacent.log
new file mode 100644
index 0000000..c7d8fdf
--- /dev/null
+++ b/probe_adjacent.log
@@ -0,0 +1,5 @@
           1 +CASE 1002 target 0.07808276265859604 0.0679478570818901 dest 1.3068632706999779 neighbor obstruction0 [1.1935958862304688, 0.10000099986791611, 0.10489305853843689, 0.19846290349960327]
           2 +CASE 1052 target 0.1265658289194107 0.05019199475646019 dest 0.37262771278619766 neighbor obstruction0 [0.2837442457675934, 0.10000099986791611, 0.08334893733263016, 0.18373318016529083]
           3 +FOUND [1002, 1052]
           4 +RESULT 1002 True 33 place
           5 +RESULT 1052 True 54 place
diff --git a/results_0_30_3.json b/results_0_30_3.json
index 9e36a14..ca616b1 100644
--- a/results_0_30_3.json
+++ b/results_0_30_3.json
@@ -1 +1 @@
    1        -[{"seed": 0, "count": 3, "done": true, "steps": 28, "seconds": 6.726}, {"seed": 1, "count": 3, "done": true, "steps": 134, "seconds": 26.098}, {"seed": 2, "count": 3, "done": true, "steps": 142, "seconds": 29.787}, {"seed": 3, "count": 3, "done": true, "steps": 95, "seconds": 18.011}, {"seed": 4, "count": 3, "done": true, "steps": 89, "seconds": 16.508}, {"seed": 5, "count": 3, "done": true, "steps": 32, "seconds": 5.492}, {"seed": 6, "count": 3, "done": true, "steps": 109, "seconds": 19.7}, {"seed": 7, "count": 3, "done": true, "steps": 112, "seconds": 22.661}, {"seed": 8, "count": 3, "done": true, "steps": 99, "seconds": 20.135}, {"seed": 9, "count": 3, "done": true, "steps": 122, "seconds": 24.609}, {"seed": 10, "count": 3, "done": true, "steps": 88, "seconds": 18.811}, {"seed": 11, "count": 3, "done": true, "steps": 74, "seconds": 14.882}, {"seed": 12, "count": 3, "done": true, "steps": 129, "seconds": 22.898}, {"seed": 13, "count": 3, "done": true, "steps": 125, "seconds": 22.639}, {"seed": 14, "count": 3, "done": true, "steps": 133, "seconds": 23.32}, {"seed": 15, "count": 3, "done": true, "steps": 116, "seconds": 19.871}, {"seed": 16, "count": 3, "done": true, "steps": 81, "seconds": 14.044}, {"seed": 17, "count": 3, "done": true, "steps": 124, "seconds": 19.798}, {"seed": 18, "count": 3, "done": true, "steps": 91, "seconds": 14.896}, {"seed": 19, "count": 3, "done": true, "steps": 126, "seconds": 18.652}, {"seed": 20, "count": 3, "done": true, "steps": 121, "seconds": 16.089}, {"seed": 21, "count": 3, "done": true, "steps": 102, "seconds": 12.396}, {"seed": 22, "count": 3, "done": true, "steps": 82, "seconds": 9.542}, {"seed": 23, "count": 3, "done": true, "steps": 80, "seconds": 9.97}, {"seed": 24, "count": 3, "done": true, "steps": 94, "seconds": 12.042}, {"seed": 25, "count": 3, "done": true, "steps": 149, "seconds": 20.198}, {"seed": 26, "count": 3, "done": true, "steps": 96, "seconds": 13.77}, {"seed": 27, "count": 3, "done": true, "steps": 68, "seconds": 10.102}, {"seed": 28, "count": 3, "done": true, "steps": 126, "seconds": 15.054}, {"seed": 29, "count": 3, "done": true, "steps": 123, "seconds": 13.679}]
\ No newline at end of file
           1 +[{"seed": 0, "count": 3, "done": true, "steps": 23, "seconds": 3.756}, {"seed": 1, "count": 3, "done": true, "steps": 92, "seconds": 10.84}, {"seed": 2, "count": 3, "done": true, "steps": 93, "seconds": 10.756}, {"seed": 3, "count": 3, "done": true, "steps": 73, "seconds": 8.441}, {"seed": 4, "count": 3, "done": true, "steps": 61, "seconds": 5.952}, {"seed": 5, "count": 3, "done": true, "steps": 22, "seconds": 1.211}, {"seed": 6, "count": 3, "done": true, "steps": 75, "seconds": 6.619}, {"seed": 7, "count": 3, "done": true, "steps": 57, "seconds": 5.154}, {"seed": 8, "count": 3, "done": true, "steps": 67, "seconds": 5.665}, {"seed": 9, "count": 3, "done": true, "steps": 81, "seconds": 9.422}, {"seed": 10, "count": 3, "done": true, "steps": 61, "seconds": 7.676}, {"seed": 11, "count": 3, "done": true, "steps": 57, "seconds": 6.535}, {"seed": 12, "count": 3, "done": true, "steps": 91, "seconds": 11.845}, {"seed": 13, "count": 3, "done": true, "steps": 82, "seconds": 10.633}, {"seed": 14, "count": 3, "done": true, "steps": 84, "seconds": 12.136}, {"seed": 15, "count": 3, "done": true, "steps": 86, "seconds": 12.171}, {"seed": 16, "count": 3, "done": true, "steps": 57, "seconds": 8.114}, {"seed": 17, "count": 3, "done": true, "steps": 81, "seconds": 10.887}, {"seed": 18, "count": 3, "done": true, "steps": 73, "seconds": 9.806}, {"seed": 19, "count": 3, "done": true, "steps": 85, "seconds": 11.699}, {"seed": 20, "count": 3, "done": true, "steps": 80, "seconds": 10.68}, {"seed": 21, "count": 3, "done": true, "steps": 71, "seconds": 9.742}, {"seed": 22, "count": 3, "done": true, "steps": 59, "seconds": 7.447}, {"seed": 23, "count": 3, "done": true, "steps": 57, "seconds": 7.185}, {"seed": 24, "count": 3, "done": true, "steps": 80, "seconds": 11.299}, {"seed": 25, "count": 3, "done": true, "steps": 106, "seconds": 14.274}, {"seed": 26, "count": 3, "done": true, "steps": 69, "seconds": 9.154}, {"seed": 27, "count": 3, "done": true, "steps": 48, "seconds": 7.133}, {"seed": 28, "count": 3, "done": true, "steps": 91, "seconds": 10.564}, {"seed": 29, "count": 3, "done": true, "steps": 84, "seconds": 9.612}]
\ No newline at end of file
diff --git a/results_100_200_None.json b/results_100_200_None.json
new file mode 100644
index 0000000..8f7fe55
--- /dev/null
+++ b/results_100_200_None.json
@@ -0,0 +1 @@
           1 +[{"seed": 100, "count": null, "done": true, "steps": 83, "seconds": 3.669}, {"seed": 101, "count": null, "done": true, "steps": 16, "seconds": 0.424}, {"seed": 102, "count": null, "done": true, "steps": 62, "seconds": 2.22}, {"seed": 103, "count": null, "done": true, "steps": 32, "seconds": 1.452}, {"seed": 104, "count": null, "done": true, "steps": 73, "seconds": 2.861}, {"seed": 105, "count": null, "done": true, "steps": 20, "seconds": 0.571}, {"seed": 106, "count": null, "done": true, "steps": 24, "seconds": 0.919}, {"seed": 107, "count": null, "done": true, "steps": 33, "seconds": 1.16}, {"seed": 108, "count": null, "done": true, "steps": 27, "seconds": 1.068}, {"seed": 109, "count": null, "done": true, "steps": 48, "seconds": 2.416}, {"seed": 110, "count": null, "done": true, "steps": 67, "seconds": 3.287}, {"seed": 111, "count": null, "done": true, "steps": 38, "seconds": 1.953}, {"seed": 112, "count": null, "done": true, "steps": 24, "seconds": 0.998}, {"seed": 113, "count": null, "done": true, "steps": 39, "seconds": 1.26}, {"seed": 114, "count": null, "done": true, "steps": 21, "seconds": 0.447}, {"seed": 115, "count": null, "done": true, "steps": 63, "seconds": 2.758}, {"seed": 116, "count": null, "done": true, "steps": 50, "seconds": 1.978}, {"seed": 117, "count": null, "done": true, "steps": 26, "seconds": 1.01}, {"seed": 118, "count": null, "done": true, "steps": 58, "seconds": 2.355}, {"seed": 119, "count": null, "done": true, "steps": 59, "seconds": 2.763}, {"seed": 120, "count": null, "done": true, "steps": 23, "seconds": 0.842}, {"seed": 121, "count": null, "done": true, "steps": 25, "seconds": 0.649}, {"seed": 122, "count": null, "done": true, "steps": 68, "seconds": 3.269}, {"seed": 123, "count": null, "done": true, "steps": 38, "seconds": 1.65}, {"seed": 124, "count": null, "done": true, "steps": 49, "seconds": 2.193}, {"seed": 125, "count": null, "done": true, "steps": 77, "seconds": 2.391}, {"seed": 126, "count": null, "done": true, "steps": 18, "seconds": 0.446}, {"seed": 127, "count": null, "done": true, "steps": 73, "seconds": 2.925}, {"seed": 128, "count": null, "done": true, "steps": 90, "seconds": 4.577}, {"seed": 129, "count": null, "done": true, "steps": 37, "seconds": 1.556}, {"seed": 130, "count": null, "done": true, "steps": 57, "seconds": 3.281}, {"seed": 131, "count": null, "done": true, "steps": 36, "seconds": 1.751}, {"seed": 132, "count": null, "done": true, "steps": 80, "seconds": 6.808}, {"seed": 133, "count": null, "done": true, "steps": 63, "seconds": 4.371}, {"seed": 134, "count": null, "done": true, "steps": 24, "seconds": 2.389}, {"seed": 135, "count": null, "done": true, "steps": 20, "seconds": 1.298}, {"seed": 136, "count": null, "done": true, "steps": 45, "seconds": 3.913}, {"seed": 137, "count": null, "done": true, "steps": 72, "seconds": 5.598}, {"seed": 138, "count": null, "done": true, "steps": 84, "seconds": 6.415}, {"seed": 139, "count": null, "done": true, "steps": 85, "seconds": 6.831}, {"seed": 140, "count": null, "done": true, "steps": 20, "seconds": 1.804}, {"seed": 141, "count": null, "done": true, "steps": 51, "seconds": 3.587}, {"seed": 142, "count": null, "done": true, "steps": 51, "seconds": 3.142}, {"seed": 143, "count": null, "done": true, "steps": 50, "seconds": 4.237}, {"seed": 144, "count": null, "done": true, "steps": 39, "seconds": 2.751}, {"seed": 145, "count": null, "done": true, "steps": 39, "seconds": 2.971}, {"seed": 146, "count": null, "done": true, "steps": 53, "seconds": 4.189}, {"seed": 147, "count": null, "done": true, "steps": 25, "seconds": 1.027}, {"seed": 148, "count": null, "done": true, "steps": 17, "seconds": 0.848}, {"seed": 149, "count": null, "done": true, "steps": 32, "seconds": 1.143}, {"seed": 150, "count": null, "done": true, "steps": 33, "seconds": 1.941}, {"seed": 151, "count": null, "done": false, "steps": 1000, "seconds": 103.878, "trace": [[840, "place", "target_block", 0.7788, 0.5182], [880, "place", "target_block", 0.7788, 0.5182], [920, "place", "target_block", 0.7788, 0.5182], [960, "place", "target_block", 0.7788, 0.5182]], "state": {"obstruction0": {"x": 0.8107884526252747, "y": 0.10000099986791611, "width": 0.1386185884475708, "height": 0.11362678557634354}, "obstruction1": {"x": 0.693976104259491, "y": 0.10000099986791611, "width": 0.05311352387070656, "height": 0.19954173266887665}, "target_block": {"x": 0.7532491087913513, "y": 0.12654274702072144, "width": 0.05102952942252159, "height": 0.18566597998142242}, "target_surface": {"x": 0.7150579690933228, "y": 0.0, "width": 0.09951850026845932, "height": 0.10000000149011612}}}, {"seed": 152, "count": null, "done": true, "steps": 39, "seconds": 3.248}, {"seed": 153, "count": null, "done": true, "steps": 65, "seconds": 6.169}, {"seed": 154, "count": null, "done": true, "steps": 41, "seconds": 2.63}, {"seed": 155, "count": null, "done": true, "steps": 29, "seconds": 1.787}, {"seed": 156, "count": null, "done": true, "steps": 71, "seconds": 6.784}, {"seed": 157, "count": null, "done": true, "steps": 37, "seconds": 2.639}, {"seed": 158, "count": null, "done": true, "steps": 84, "seconds": 5.325}, {"seed": 159, "count": null, "done": true, "steps": 51, "seconds": 4.743}, {"seed": 160, "count": null, "done": true, "steps": 20, "seconds": 1.322}, {"seed": 161, "count": null, "done": true, "steps": 44, "seconds": 4.037}, {"seed": 162, "count": null, "done": true, "steps": 59, "seconds": 5.063}, {"seed": 163, "count": null, "done": true, "steps": 38, "seconds": 3.401}, {"seed": 164, "count": null, "done": true, "steps": 52, "seconds": 4.734}, {"seed": 165, "count": null, "done": true, "steps": 66, "seconds": 6.429}, {"seed": 166, "count": null, "done": true, "steps": 47, "seconds": 5.833}, {"seed": 167, "count": null, "done": true, "steps": 70, "seconds": 6.838}, {"seed": 168, "count": null, "done": true, "steps": 43, "seconds": 3.039}, {"seed": 169, "count": null, "done": true, "steps": 75, "seconds": 7.314}, {"seed": 170, "count": null, "done": true, "steps": 48, "seconds": 5.681}, {"seed": 171, "count": null, "done": true, "steps": 63, "seconds": 6.923}, {"seed": 172, "count": null, "done": true, "steps": 42, "seconds": 3.571}, {"seed": 173, "count": null, "done": true, "steps": 70, "seconds": 7.286}, {"seed": 174, "count": null, "done": true, "steps": 61, "seconds": 6.039}, {"seed": 175, "count": null, "done": true, "steps": 46, "seconds": 5.631}, {"seed": 176, "count": null, "done": true, "steps": 33, "seconds": 2.629}, {"seed": 177, "count": null, "done": true, "steps": 52, "seconds": 5.26}, {"seed": 178, "count": null, "done": true, "steps": 83, "seconds": 6.561}, {"seed": 179, "count": null, "done": true, "steps": 58, "seconds": 5.683}, {"seed": 180, "count": null, "done": true, "steps": 39, "seconds": 2.489}, {"seed": 181, "count": null, "done": true, "steps": 59, "seconds": 5.814}, {"seed": 182, "count": null, "done": true, "steps": 101, "seconds": 11.229}, {"seed": 183, "count": null, "done": true, "steps": 63, "seconds": 6.44}, {"seed": 184, "count": null, "done": true, "steps": 53, "seconds": 5.376}, {"seed": 185, "count": null, "done": true, "steps": 25, "seconds": 2.233}, {"seed": 186, "count": null, "done": true, "steps": 23, "seconds": 1.188}, {"seed": 187, "count": null, "done": true, "steps": 55, "seconds": 4.541}, {"seed": 188, "count": null, "done": true, "steps": 22, "seconds": 1.779}, {"seed": 189, "count": null, "done": true, "steps": 35, "seconds": 2.658}, {"seed": 190, "count": null, "done": true, "steps": 17, "seconds": 0.805}, {"seed": 191, "count": null, "done": true, "steps": 33, "seconds": 2.053}, {"seed": 192, "count": null, "done": true, "steps": 49, "seconds": 4.106}, {"seed": 193, "count": null, "done": true, "steps": 59, "seconds": 3.925}, {"seed": 194, "count": null, "done": true, "steps": 74, "seconds": 6.377}, {"seed": 195, "count": null, "done": true, "steps": 26, "seconds": 1.638}, {"seed": 196, "count": null, "done": true, "steps": 39, "seconds": 2.337}, {"seed": 197, "count": null, "done": true, "steps": 90, "seconds": 6.173}, {"seed": 198, "count": null, "done": true, "steps": 61, "seconds": 2.884}, {"seed": 199, "count": null, "done": true, "steps": 49, "seconds": 2.48}, {"seed": 200, "count": null, "done": true, "steps": 23, "seconds": 1.018}, {"seed": 201, "count": null, "done": true, "steps": 28, "seconds": 1.056}, {"seed": 202, "count": null, "done": true, "steps": 36, "seconds": 1.224}, {"seed": 203, "count": null, "done": true, "steps": 36, "seconds": 1.367}, {"seed": 204, "count": null, "done": true, "steps": 48, "seconds": 2.859}, {"seed": 205, "count": null, "done": true, "steps": 38, "seconds": 1.579}, {"seed": 206, "count": null, "done": true, "steps": 62, "seconds": 3.172}, {"seed": 207, "count": null, "done": true, "steps": 20, "seconds": 0.814}, {"seed": 208, "count": null, "done": true, "steps": 28, "seconds": 2.062}, {"seed": 209, "count": null, "done": true, "steps": 42, "seconds": 2.807}, {"seed": 210, "count": null, "done": true, "steps": 21, "seconds": 1.418}, {"seed": 211, "count": null, "done": true, "steps": 31, "seconds": 1.514}, {"seed": 212, "count": null, "done": true, "steps": 33, "seconds": 1.618}, {"seed": 213, "count": null, "done": true, "steps": 19, "seconds": 0.908}, {"seed": 214, "count": null, "done": true, "steps": 43, "seconds": 2.059}, {"seed": 215, "count": null, "done": true, "steps": 70, "seconds": 4.696}, {"seed": 216, "count": null, "done": true, "steps": 31, "seconds": 2.063}, {"seed": 217, "count": null, "done": true, "steps": 53, "seconds": 3.447}, {"seed": 218, "count": null, "done": true, "steps": 44, "seconds": 2.352}, {"seed": 219, "count": null, "done": true, "steps": 23, "seconds": 1.256}, {"seed": 220, "count": null, "done": true, "steps": 48, "seconds": 3.109}, {"seed": 221, "count": null, "done": true, "steps": 57, "seconds": 3.668}, {"seed": 222, "count": null, "done": true, "steps": 47, "seconds": 2.951}, {"seed": 223, "count": null, "done": true, "steps": 33, "seconds": 1.855}, {"seed": 224, "count": null, "done": true, "steps": 52, "seconds": 3.143}, {"seed": 225, "count": null, "done": true, "steps": 92, "seconds": 5.74}, {"seed": 226, "count": null, "done": true, "steps": 76, "seconds": 4.641}, {"seed": 227, "count": null, "done": true, "steps": 57, "seconds": 3.049}, {"seed": 228, "count": null, "done": true, "steps": 59, "seconds": 3.061}, {"seed": 229, "count": null, "done": true, "steps": 30, "seconds": 1.813}, {"seed": 230, "count": null, "done": true, "steps": 40, "seconds": 1.961}, {"seed": 231, "count": null, "done": true, "steps": 31, "seconds": 1.324}, {"seed": 232, "count": null, "done": true, "steps": 25, "seconds": 1.635}, {"seed": 233, "count": null, "done": true, "steps": 25, "seconds": 1.346}, {"seed": 234, "count": null, "done": true, "steps": 46, "seconds": 2.795}, {"seed": 235, "count": null, "done": true, "steps": 65, "seconds": 4.046}, {"seed": 236, "count": null, "done": true, "steps": 75, "seconds": 3.809}, {"seed": 237, "count": null, "done": true, "steps": 90, "seconds": 7.009}, {"seed": 238, "count": null, "done": true, "steps": 19, "seconds": 0.962}, {"seed": 239, "count": null, "done": false, "steps": 1000, "seconds": 85.894, "trace": [[840, "place", "target_block", 0.1854, 0.4726], [880, "place", "target_block", 0.1854, 0.4726], [920, "place", "target_block", 0.1854, 0.4726], [960, "place", "target_block", 0.1854, 0.4726]], "state": {"obstruction0": {"x": 0.3029325008392334, "y": 0.10100004076957703, "width": 0.08481914550065994, "height": 0.11373668164014816}, "obstruction1": {"x": 0.2174888253211975, "y": 0.10000099986791611, "width": 0.07244367152452469, "height": 0.12870042026042938}, "target_block": {"x": 0.15883193910121918, "y": 0.20570142567157745, "width": 0.054496027529239655, "height": 0.06093798950314522}, "target_surface": {"x": 0.1535184234380722, "y": 0.0, "width": 0.09963131695985794, "height": 0.10000000149011612}}}, {"seed": 240, "count": null, "done": true, "steps": 83, "seconds": 7.283}, {"seed": 241, "count": null, "done": true, "steps": 18, "seconds": 0.998}, {"seed": 242, "count": null, "done": true, "steps": 74, "seconds": 7.018}, {"seed": 243, "count": null, "done": true, "steps": 34, "seconds": 3.187}, {"seed": 244, "count": null, "done": true, "steps": 49, "seconds": 4.66}, {"seed": 245, "count": null, "done": true, "steps": 42, "seconds": 3.582}, {"seed": 246, "count": null, "done": true, "steps": 71, "seconds": 6.489}, {"seed": 247, "count": null, "done": true, "steps": 33, "seconds": 2.103}, {"seed": 248, "count": null, "done": true, "steps": 53, "seconds": 3.826}, {"seed": 249, "count": null, "done": true, "steps": 48, "seconds": 4.005}, {"seed": 250, "count": null, "done": true, "steps": 78, "seconds": 5.597}, {"seed": 251, "count": null, "done": true, "steps": 18, "seconds": 1.11}, {"seed": 252, "count": null, "done": true, "steps": 95, "seconds": 9.471}, {"seed": 253, "count": null, "done": true, "steps": 56, "seconds": 4.683}, {"seed": 254, "count": null, "done": true, "steps": 31, "seconds": 2.293}, {"seed": 255, "count": null, "done": true, "steps": 27, "seconds": 1.775}, {"seed": 256, "count": null, "done": true, "steps": 33, "seconds": 2.589}, {"seed": 257, "count": null, "done": true, "steps": 40, "seconds": 4.227}, {"seed": 258, "count": null, "done": true, "steps": 45, "seconds": 4.295}, {"seed": 259, "count": null, "done": true, "steps": 20, "seconds": 1.562}, {"seed": 260, "count": null, "done": true, "steps": 48, "seconds": 3.92}, {"seed": 261, "count": null, "done": true, "steps": 81, "seconds": 5.021}, {"seed": 262, "count": null, "done": true, "steps": 61, "seconds": 5.02}, {"seed": 263, "count": null, "done": true, "steps": 58, "seconds": 4.778}, {"seed": 264, "count": null, "done": true, "steps": 44, "seconds": 2.382}, {"seed": 265, "count": null, "done": true, "steps": 64, "seconds": 5.46}, {"seed": 266, "count": null, "done": true, "steps": 53, "seconds": 3.771}, {"seed": 267, "count": null, "done": true, "steps": 52, "seconds": 3.5}, {"seed": 268, "count": null, "done": true, "steps": 98, "seconds": 7.981}, {"seed": 269, "count": null, "done": true, "steps": 54, "seconds": 4.941}, {"seed": 270, "count": null, "done": true, "steps": 43, "seconds": 2.812}, {"seed": 271, "count": null, "done": true, "steps": 54, "seconds": 4.286}, {"seed": 272, "count": null, "done": true, "steps": 20, "seconds": 1.04}, {"seed": 273, "count": null, "done": true, "steps": 31, "seconds": 1.739}, {"seed": 274, "count": null, "done": true, "steps": 38, "seconds": 2.366}, {"seed": 275, "count": null, "done": true, "steps": 34, "seconds": 1.543}, {"seed": 276, "count": null, "done": true, "steps": 24, "seconds": 1.51}, {"seed": 277, "count": null, "done": true, "steps": 31, "seconds": 1.743}, {"seed": 278, "count": null, "done": true, "steps": 26, "seconds": 1.107}, {"seed": 279, "count": null, "done": true, "steps": 47, "seconds": 2.979}, {"seed": 280, "count": null, "done": true, "steps": 30, "seconds": 2.076}, {"seed": 281, "count": null, "done": true, "steps": 43, "seconds": 2.544}, {"seed": 282, "count": null, "done": true, "steps": 46, "seconds": 3.17}, {"seed": 283, "count": null, "done": true, "steps": 52, "seconds": 2.771}, {"seed": 284, "count": null, "done": true, "steps": 23, "seconds": 1.073}, {"seed": 285, "count": null, "done": true, "steps": 77, "seconds": 4.874}, {"seed": 286, "count": null, "done": true, "steps": 29, "seconds": 1.407}, {"seed": 287, "count": null, "done": true, "steps": 87, "seconds": 5.782}, {"seed": 288, "count": null, "done": true, "steps": 21, "seconds": 0.792}, {"seed": 289, "count": null, "done": true, "steps": 33, "seconds": 2.063}, {"seed": 290, "count": null, "done": true, "steps": 36, "seconds": 2.243}, {"seed": 291, "count": null, "done": true, "steps": 31, "seconds": 1.907}, {"seed": 292, "count": null, "done": true, "steps": 90, "seconds": 6.855}, {"seed": 293, "count": null, "done": true, "steps": 33, "seconds": 1.683}, {"seed": 294, "count": null, "done": true, "steps": 29, "seconds": 1.943}, {"seed": 295, "count": null, "done": true, "steps": 51, "seconds": 3.142}, {"seed": 296, "count": null, "done": true, "steps": 27, "seconds": 1.245}, {"seed": 297, "count": null, "done": true, "steps": 35, "seconds": 1.737}, {"seed": 298, "count": null, "done": true, "steps": 46, "seconds": 1.031}, {"seed": 299, "count": null, "done": true, "steps": 71, "seconds": 1.256}]
\ No newline at end of file
diff --git a/results_1_1_4.json b/results_1_1_4.json
new file mode 100644
index 0000000..b019ad0
--- /dev/null
+++ b/results_1_1_4.json
@@ -0,0 +1 @@
           1 +[{"seed": 1, "count": 4, "done": true, "steps": 79, "seconds": 13.503, "policy_seconds": 0.0168}]
\ No newline at end of file
diff --git a/results_2_1_4.json b/results_2_1_4.json
new file mode 100644
index 0000000..5351e56
--- /dev/null
+++ b/results_2_1_4.json
@@ -0,0 +1 @@
           1 +[{"seed": 2, "count": 4, "done": false, "steps": 1000, "seconds": 102.677, "policy_seconds": 0.1575, "trace": [[840, "place", "target_block", 1.06, 0.439], [880, "place", "target_block", 1.06, 0.439], [920, "place", "target_block", 1.06, 0.439], [960, "place", "target_block", 1.06, 0.439]], "state": {"obstruction0": {"x": 0.41724511981010437, "y": 0.10000099986791611, "width": 0.16559429466724396, "height": 0.19393038749694824}, "obstruction1": {"x": 1.1710095405578613, "y": 0.10099999606609344, "width": 0.18252427875995636, "height": 0.16370268166065216}, "obstruction2": {"x": 0.6930773258209229, "y": 0.10000099986791611, "width": 0.19260691106319427, "height": 0.13893510401248932}, "obstruction3": {"x": 0.9658926725387573, "y": 0.10000099986791611, "width": 0.06577402353286743, "height": 0.09953121095895767}, "target_block": {"x": 1.0440634489059448, "y": 0.1701126992702484, "width": 0.0980890691280365, "height": 0.06211165711283684}, "target_surface": {"x": 1.0282063484191895, "y": 0.0, "width": 0.1298033446073532, "height": 0.10000000149011612}}}]
\ No newline at end of file
diff --git a/results_3_1_4.json b/results_3_1_4.json
new file mode 100644
index 0000000..1797ee9
--- /dev/null
+++ b/results_3_1_4.json
@@ -0,0 +1 @@
           1 +[{"seed": 3, "count": 4, "done": false, "steps": 1000, "seconds": 5.522, "policy_seconds": 0.1028, "trace": [[840, "place", "target_block", 1.3354, 0.5069], [880, "place", "target_block", 1.3354, 0.5069], [920, "place", "target_block", 1.3354, 0.5069], [960, "place", "target_block", 1.3354, 0.5069]], "state": {"obstruction0": {"x": 1.152086615562439, "y": 0.10000099986791611, "width": 0.1514977365732193, "height": 0.15962274372577667}, "obstruction1": {"x": 1.3890105485916138, "y": 0.10099998116493225, "width": 0.08749981224536896, "height": 0.19032169878482819}, "obstruction2": {"x": 0.43964964151382446, "y": 0.10000099986791611, "width": 0.1306634545326233, "height": 0.1996031254529953}, "obstruction3": {"x": 0.7467350363731384, "y": 0.10000099986791611, "width": 0.1965513676404953, "height": 0.15759406983852386}, "target_block": {"x": 1.3082562685012817, "y": 0.22660410404205322, "width": 0.05419572442770004, "height": 0.07431439310312271}, "target_surface": {"x": 1.2884182929992676, "y": 0.0, "width": 0.08759234845638275, "height": 0.10000000149011612}}}]
\ No newline at end of file
diff --git a/results_4_1_4.json b/results_4_1_4.json
new file mode 100644
index 0000000..72ea1c4
--- /dev/null
+++ b/results_4_1_4.json
@@ -0,0 +1 @@
           1 +[{"seed": 4, "count": 4, "done": false, "steps": 1000, "seconds": 5.497, "policy_seconds": 0.1098, "trace": [[840, "place", "obstruction2", 1.1379, 0.4016], [880, "place", "obstruction2", 1.1379, 0.4016], [920, "place", "obstruction2", 1.1379, 0.4016], [960, "place", "obstruction2", 1.1379, 0.4016]], "state": {"obstruction0": {"x": 1.1559269428253174, "y": 0.10100000351667404, "width": 0.06802277266979218, "height": 0.05388985574245453}, "obstruction1": {"x": 1.4920032024383545, "y": 0.10000099986791611, "width": 0.07113966345787048, "height": 0.12770894169807434}, "obstruction2": {"x": 1.0861551761627197, "y": 0.1451493799686432, "width": 0.05677169933915138, "height": 0.05042976886034012}, "obstruction3": {"x": 1.2369496822357178, "y": 0.10000099986791611, "width": 0.08748079836368561, "height": 0.16814841330051422}, "target_block": {"x": 0.27295616269111633, "y": 0.10000099986791611, "width": 0.14293360710144043, "height": 0.1114027351140976}, "target_surface": {"x": 1.3184852600097656, "y": 0.0, "width": 0.18072666227817535, "height": 0.10000000149011612}}}]
\ No newline at end of file
diff --git a/results_5_1_4.json b/results_5_1_4.json
new file mode 100644
index 0000000..04f9e8d
--- /dev/null
+++ b/results_5_1_4.json
@@ -0,0 +1 @@
           1 +[{"seed": 5, "count": 4, "done": true, "steps": 83, "seconds": 0.419, "policy_seconds": 0.0117}]
\ No newline at end of file
```

</details>

<a id="C025"></a>
### C025 · Reserve the final base footprint when relocating obstructions

Commit `14524e536e14a6a86370efb42a57a618e171daa7`; parents: 6cb4e133921a64475bda4ef9793dca12762318d8. Recorded author date: 2026-09-21T22:41:57+02:00.

File roles (automatic): policy.

- [E0091](01_timeline.md#E0091): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C025_14524e5_approach.py) · [Exact all-file diff](evidence/diffs/C025_14524e5.diff)

[Previous saved controller snapshot](evidence/versions/C024_6cb4e13_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 389a116..bd237ad 100644
--- a/approach.py
+++ b/approach.py
@@ -75,8 +75,8 @@ class GeneratedApproach:
   75     75          others=[(o,self.rect(s,o)) for o in s.get_objects(self.ot) if o!=self.obj]
   76     76          bx,by,bw,bh=self.rect(s,self.block)
   77     77          goalcx=self.destx-bx+self.target_grasp
   78        -        reserve_left=min(self.destx,goalcx-.042)
   79        -        reserve_right=max(self.destx+bw,goalcx+.042)
          78 +        reserve_left=min(self.destx,goalcx-.105)
          79 +        reserve_right=max(self.destx+bw,goalcx+.105)
   80     80          low=max(.005,.101+self.offsetx)
   81     81          high=min(1.613-w,1.517+self.offsetx)
   82     82          positions=[low,high,float(np.clip(x,low,high))]
```

</details>

<a id="C026"></a>
### C026 · Probe sub-millimeter final placement rejection on seed 151

Commit `2fc1fb229608de4ed5722b31225dcab2e90ef912`; parents: 14524e536e14a6a86370efb42a57a618e171daa7. Recorded author date: 2026-09-21T22:43:49+02:00.

File roles (automatic): diagnostic/test.

- [E0094](01_timeline.md#E0094): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C026_2fc1fb2.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_final_clearance.py b/probe_final_clearance.py
new file mode 100644
index 0000000..2492664
--- /dev/null
+++ b/probe_final_clearance.py
@@ -0,0 +1,9 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import numpy as np
           4 +e=make_env();s,_=e.reset(seed=151);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,{})
           5 +for t in range(80):s,r,d,tr,i=e.step(p.get_action(s))
           6 +for action in [[0,-.001,0,0,1]]*10+[[.003,0,0,0,1],[0,-.001,0,0,1]]*6:
           7 + s,r,d,tr,i=e.step(np.array(action,dtype=np.float32));print('step',action,'robot',[s.get(p.robot,k) for k in ['x','y']],'block',p.rect(s,p.block),'done',d,flush=True)
           8 + if d:break
           9 +e.close()
```

</details>

<a id="C027"></a>
### C027 · Allow conservative gripper contact clearance during final descent

Commit `c08b92a21ef8a873ff43c67416dc74d3e1070d97`; parents: 2fc1fb229608de4ed5722b31225dcab2e90ef912. Recorded author date: 2026-09-21T22:44:00+02:00.

File roles (automatic): policy.

- [E0116](01_timeline.md#E0116): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C027_c08b92a_approach.py) · [Exact all-file diff](evidence/diffs/C027_c08b92a.diff)

[Previous saved controller snapshot](evidence/versions/C025_14524e5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index bd237ad..faf35ae 100644
--- a/approach.py
+++ b/approach.py
@@ -57,7 +57,7 @@ class GeneratedApproach:
   57     57          _,_,w,h=self.rect(s,obj)
   58     58          cx=left-offsetx;cy=bottom-offsety
   59     59          parts=[(left,bottom,left+w,bottom+h),
   60        -               (cx-.037,cy-.207,cx+.037,cy-.193),
          60 +               (cx-.055,cy-.225,cx+.055,cy-.185),
   61     61                 (cx-.008,cy-.2,cx+.008,cy)]
   62     62          blocked=[]
   63     63          for other in s.get_objects(self.ot):
```

</details>

<a id="C028"></a>
### C028 · Add sequential dense-scene validation to avoid concurrent slow resets

Commit `77929e5c766f6a95f3c74b81897c925127c9ab2a`; parents: c08b92a21ef8a873ff43c67416dc74d3e1070d97. Recorded author date: 2026-09-21T22:44:32+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C028_77929e5.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/results_0_100_None.json b/results_0_100_None.json
index 3ac5188..7afc334 100644
--- a/results_0_100_None.json
+++ b/results_0_100_None.json
@@ -1 +1 @@
    1        -[{"seed": 0, "count": null, "done": true, "steps": 75, "seconds": 3.233}, {"seed": 1, "count": null, "done": true, "steps": 60, "seconds": 2.544}, {"seed": 2, "count": null, "done": true, "steps": 77, "seconds": 3.379}, {"seed": 3, "count": null, "done": true, "steps": 53, "seconds": 2.905}, {"seed": 4, "count": null, "done": true, "steps": 57, "seconds": 2.843}, {"seed": 5, "count": null, "done": true, "steps": 91, "seconds": 4.274}, {"seed": 6, "count": null, "done": true, "steps": 57, "seconds": 2.413}, {"seed": 7, "count": null, "done": true, "steps": 109, "seconds": 5.31}, {"seed": 8, "count": null, "done": true, "steps": 75, "seconds": 3.583}, {"seed": 9, "count": null, "done": true, "steps": 83, "seconds": 3.205}, {"seed": 10, "count": null, "done": true, "steps": 36, "seconds": 2.382}, {"seed": 11, "count": null, "done": true, "steps": 41, "seconds": 2.174}, {"seed": 12, "count": null, "done": true, "steps": 77, "seconds": 3.689}, {"seed": 13, "count": null, "done": true, "steps": 57, "seconds": 3.314}, {"seed": 14, "count": null, "done": true, "steps": 27, "seconds": 1.311}, {"seed": 15, "count": null, "done": true, "steps": 22, "seconds": 0.929}, {"seed": 16, "count": null, "done": true, "steps": 25, "seconds": 1.208}, {"seed": 17, "count": null, "done": true, "steps": 63, "seconds": 2.59}, {"seed": 18, "count": null, "done": true, "steps": 51, "seconds": 2.179}, {"seed": 19, "count": null, "done": true, "steps": 49, "seconds": 1.544}, {"seed": 20, "count": null, "done": true, "steps": 63, "seconds": 2.337}, {"seed": 21, "count": null, "done": true, "steps": 49, "seconds": 1.518}, {"seed": 22, "count": null, "done": true, "steps": 89, "seconds": 5.272}, {"seed": 23, "count": null, "done": true, "steps": 40, "seconds": 1.805}, {"seed": 24, "count": null, "done": true, "steps": 50, "seconds": 2.876}, {"seed": 25, "count": null, "done": true, "steps": 49, "seconds": 3.123}, {"seed": 26, "count": null, "done": true, "steps": 50, "seconds": 4.454}, {"seed": 27, "count": null, "done": true, "steps": 18, "seconds": 1.019}, {"seed": 28, "count": null, "done": true, "steps": 47, "seconds": 3.086}, {"seed": 29, "count": null, "done": true, "steps": 39, "seconds": 3.788}, {"seed": 30, "count": null, "done": true, "steps": 23, "seconds": 1.233}, {"seed": 31, "count": null, "done": true, "steps": 51, "seconds": 3.933}, {"seed": 32, "count": null, "done": true, "steps": 84, "seconds": 8.966}, {"seed": 33, "count": null, "done": true, "steps": 59, "seconds": 6.527}, {"seed": 34, "count": null, "done": true, "steps": 35, "seconds": 2.214}, {"seed": 35, "count": null, "done": true, "steps": 33, "seconds": 2.29}, {"seed": 36, "count": null, "done": true, "steps": 45, "seconds": 4.108}, {"seed": 37, "count": null, "done": true, "steps": 29, "seconds": 2.155}, {"seed": 38, "count": null, "done": true, "steps": 21, "seconds": 1.401}, {"seed": 39, "count": null, "done": true, "steps": 55, "seconds": 5.246}, {"seed": 40, "count": null, "done": true, "steps": 59, "seconds": 4.315}, {"seed": 41, "count": null, "done": true, "steps": 30, "seconds": 2.61}, {"seed": 42, "count": null, "done": true, "steps": 32, "seconds": 2.221}, {"seed": 43, "count": null, "done": true, "steps": 26, "seconds": 1.551}, {"seed": 44, "count": null, "done": true, "steps": 63, "seconds": 6.5}, {"seed": 45, "count": null, "done": true, "steps": 79, "seconds": 7.5}, {"seed": 46, "count": null, "done": true, "steps": 36, "seconds": 3.161}, {"seed": 47, "count": null, "done": true, "steps": 41, "seconds": 2.885}, {"seed": 48, "count": null, "done": true, "steps": 22, "seconds": 1.111}, {"seed": 49, "count": null, "done": true, "steps": 24, "seconds": 1.036}, {"seed": 50, "count": null, "done": true, "steps": 66, "seconds": 5.796}, {"seed": 51, "count": null, "done": true, "steps": 35, "seconds": 2.529}, {"seed": 52, "count": null, "done": true, "steps": 64, "seconds": 6.595}, {"seed": 53, "count": null, "done": true, "steps": 78, "seconds": 7.849}, {"seed": 54, "count": null, "done": true, "steps": 28, "seconds": 1.97}, {"seed": 55, "count": null, "done": true, "steps": 22, "seconds": 2.634}, {"seed": 56, "count": null, "done": true, "steps": 62, "seconds": 5.011}, {"seed": 57, "count": null, "done": true, "steps": 20, "seconds": 1.336}, {"seed": 58, "count": null, "done": true, "steps": 53, "seconds": 4.204}, {"seed": 59, "count": null, "done": true, "steps": 62, "seconds": 5.858}, {"seed": 60, "count": null, "done": true, "steps": 23, "seconds": 1.447}, {"seed": 61, "count": null, "done": true, "steps": 70, "seconds": 5.928}, {"seed": 62, "count": null, "done": true, "steps": 66, "seconds": 5.443}, {"seed": 63, "count": null, "done": true, "steps": 35, "seconds": 3.271}, {"seed": 64, "count": null, "done": true, "steps": 29, "seconds": 2.093}, {"seed": 65, "count": null, "done": true, "steps": 17, "seconds": 1.001}, {"seed": 66, "count": null, "done": true, "steps": 55, "seconds": 4.992}, {"seed": 67, "count": null, "done": true, "steps": 52, "seconds": 5.352}, {"seed": 68, "count": null, "done": true, "steps": 43, "seconds": 4.186}, {"seed": 69, "count": null, "done": true, "steps": 36, "seconds": 2.941}, {"seed": 70, "count": null, "done": true, "steps": 38, "seconds": 4.331}, {"seed": 71, "count": null, "done": true, "steps": 40, "seconds": 3.909}, {"seed": 72, "count": null, "done": true, "steps": 96, "seconds": 9.054}, {"seed": 73, "count": null, "done": true, "steps": 65, "seconds": 6.339}, {"seed": 74, "count": null, "done": true, "steps": 25, "seconds": 1.678}, {"seed": 75, "count": null, "done": true, "steps": 71, "seconds": 4.967}, {"seed": 76, "count": null, "done": true, "steps": 31, "seconds": 2.283}, {"seed": 77, "count": null, "done": true, "steps": 19, "seconds": 1.07}, {"seed": 78, "count": null, "done": true, "steps": 74, "seconds": 5.837}, {"seed": 79, "count": null, "done": true, "steps": 34, "seconds": 1.609}, {"seed": 80, "count": null, "done": true, "steps": 63, "seconds": 5.295}, {"seed": 81, "count": null, "done": true, "steps": 22, "seconds": 1.052}, {"seed": 82, "count": null, "done": true, "steps": 35, "seconds": 3.906}, {"seed": 83, "count": null, "done": true, "steps": 83, "seconds": 8.428}, {"seed": 84, "count": null, "done": true, "steps": 58, "seconds": 4.456}, {"seed": 85, "count": null, "done": true, "steps": 53, "seconds": 5.372}, {"seed": 86, "count": null, "done": true, "steps": 44, "seconds": 4.436}, {"seed": 87, "count": null, "done": true, "steps": 48, "seconds": 3.155}, {"seed": 88, "count": null, "done": true, "steps": 57, "seconds": 4.411}, {"seed": 89, "count": null, "done": true, "steps": 56, "seconds": 5.168}, {"seed": 90, "count": null, "done": true, "steps": 64, "seconds": 4.991}, {"seed": 91, "count": null, "done": true, "steps": 42, "seconds": 4.244}, {"seed": 92, "count": null, "done": true, "steps": 47, "seconds": 3.469}, {"seed": 93, "count": null, "done": true, "steps": 65, "seconds": 6.069}, {"seed": 94, "count": null, "done": true, "steps": 25, "seconds": 1.755}, {"seed": 95, "count": null, "done": true, "steps": 59, "seconds": 4.336}, {"seed": 96, "count": null, "done": true, "steps": 30, "seconds": 2.922}, {"seed": 97, "count": null, "done": true, "steps": 33, "seconds": 1.845}, {"seed": 98, "count": null, "done": true, "steps": 54, "seconds": 3.998}, {"seed": 99, "count": null, "done": true, "steps": 44, "seconds": 3.579}]
\ No newline at end of file
           1 +[{"seed": 0, "count": null, "done": true, "steps": 79, "seconds": 3.837, "policy_seconds": 0.0253}, {"seed": 1, "count": null, "done": true, "steps": 60, "seconds": 2.363, "policy_seconds": 0.0176}, {"seed": 2, "count": null, "done": true, "steps": 55, "seconds": 2.975, "policy_seconds": 0.0166}, {"seed": 3, "count": null, "done": true, "steps": 53, "seconds": 2.948, "policy_seconds": 0.0172}, {"seed": 4, "count": null, "done": true, "steps": 57, "seconds": 2.329, "policy_seconds": 0.0085}, {"seed": 5, "count": null, "done": true, "steps": 93, "seconds": 3.944, "policy_seconds": 0.0223}, {"seed": 6, "count": null, "done": true, "steps": 66, "seconds": 2.525, "policy_seconds": 0.0147}, {"seed": 7, "count": null, "done": true, "steps": 149, "seconds": 7.675, "policy_seconds": 0.0357}, {"seed": 8, "count": null, "done": true, "steps": 91, "seconds": 4.355, "policy_seconds": 0.0266}, {"seed": 9, "count": null, "done": true, "steps": 83, "seconds": 3.635, "policy_seconds": 0.022}, {"seed": 10, "count": null, "done": true, "steps": 36, "seconds": 1.468, "policy_seconds": 0.0082}, {"seed": 11, "count": null, "done": true, "steps": 41, "seconds": 1.908, "policy_seconds": 0.0071}, {"seed": 12, "count": null, "done": true, "steps": 78, "seconds": 4.341, "policy_seconds": 0.0183}, {"seed": 13, "count": null, "done": true, "steps": 57, "seconds": 3.068, "policy_seconds": 0.0176}, {"seed": 14, "count": null, "done": true, "steps": 27, "seconds": 0.935, "policy_seconds": 0.0054}, {"seed": 15, "count": null, "done": true, "steps": 22, "seconds": 1.359, "policy_seconds": 0.0074}, {"seed": 16, "count": null, "done": true, "steps": 25, "seconds": 1.509, "policy_seconds": 0.0051}, {"seed": 17, "count": null, "done": true, "steps": 70, "seconds": 3.233, "policy_seconds": 0.016}, {"seed": 18, "count": null, "done": true, "steps": 51, "seconds": 2.066, "policy_seconds": 0.0199}, {"seed": 19, "count": null, "done": true, "steps": 49, "seconds": 1.933, "policy_seconds": 0.0159}, {"seed": 20, "count": null, "done": true, "steps": 65, "seconds": 3.419, "policy_seconds": 0.0294}, {"seed": 21, "count": null, "done": true, "steps": 50, "seconds": 2.287, "policy_seconds": 0.0112}, {"seed": 22, "count": null, "done": true, "steps": 89, "seconds": 5.101, "policy_seconds": 0.0276}, {"seed": 23, "count": null, "done": true, "steps": 40, "seconds": 1.426, "policy_seconds": 0.0089}, {"seed": 24, "count": null, "done": true, "steps": 50, "seconds": 1.514, "policy_seconds": 0.0098}, {"seed": 25, "count": null, "done": true, "steps": 49, "seconds": 2.09, "policy_seconds": 0.0123}, {"seed": 26, "count": null, "done": true, "steps": 50, "seconds": 2.809, "policy_seconds": 0.0116}, {"seed": 27, "count": null, "done": true, "steps": 18, "seconds": 0.982, "policy_seconds": 0.003}, {"seed": 28, "count": null, "done": true, "steps": 47, "seconds": 2.306, "policy_seconds": 0.009}, {"seed": 29, "count": null, "done": true, "steps": 42, "seconds": 2.845, "policy_seconds": 0.0102}, {"seed": 30, "count": null, "done": true, "steps": 23, "seconds": 1.174, "policy_seconds": 0.0027}, {"seed": 31, "count": null, "done": true, "steps": 34, "seconds": 1.896, "policy_seconds": 0.0082}, {"seed": 32, "count": null, "done": true, "steps": 87, "seconds": 5.267, "policy_seconds": 0.0264}, {"seed": 33, "count": null, "done": true, "steps": 59, "seconds": 3.303, "policy_seconds": 0.0178}, {"seed": 34, "count": null, "done": true, "steps": 35, "seconds": 1.231, "policy_seconds": 0.0084}, {"seed": 35, "count": null, "done": true, "steps": 33, "seconds": 1.037, "policy_seconds": 0.0082}, {"seed": 36, "count": null, "done": true, "steps": 55, "seconds": 2.646, "policy_seconds": 0.0145}, {"seed": 37, "count": null, "done": true, "steps": 29, "seconds": 1.298, "policy_seconds": 0.0051}, {"seed": 38, "count": null, "done": true, "steps": 21, "seconds": 0.838, "policy_seconds": 0.0051}, {"seed": 39, "count": null, "done": true, "steps": 63, "seconds": 3.764, "policy_seconds": 0.019}, {"seed": 40, "count": null, "done": true, "steps": 80, "seconds": 4.572, "policy_seconds": 0.0198}, {"seed": 41, "count": null, "done": true, "steps": 30, "seconds": 1.592, "policy_seconds": 0.0068}, {"seed": 42, "count": null, "done": true, "steps": 32, "seconds": 1.681, "policy_seconds": 0.0084}, {"seed": 43, "count": null, "done": true, "steps": 26, "seconds": 1.433, "policy_seconds": 0.006}, {"seed": 44, "count": null, "done": true, "steps": 64, "seconds": 3.881, "policy_seconds": 0.0137}, {"seed": 45, "count": null, "done": true, "steps": 49, "seconds": 2.375, "policy_seconds": 0.0155}, {"seed": 46, "count": null, "done": true, "steps": 36, "seconds": 1.563, "policy_seconds": 0.0059}, {"seed": 47, "count": null, "done": true, "steps": 41, "seconds": 1.738, "policy_seconds": 0.0062}, {"seed": 48, "count": null, "done": true, "steps": 22, "seconds": 1.104, "policy_seconds": 0.0064}, {"seed": 49, "count": null, "done": true, "steps": 24, "seconds": 1.069, "policy_seconds": 0.0049}, {"seed": 50, "count": null, "done": true, "steps": 63, "seconds": 3.597, "policy_seconds": 0.0253}, {"seed": 51, "count": null, "done": true, "steps": 35, "seconds": 1.575, "policy_seconds": 0.0094}, {"seed": 52, "count": null, "done": true, "steps": 78, "seconds": 4.024, "policy_seconds": 0.0227}, {"seed": 53, "count": null, "done": true, "steps": 78, "seconds": 3.595, "policy_seconds": 0.0264}, {"seed": 54, "count": null, "done": true, "steps": 28, "seconds": 1.064, "policy_seconds": 0.0074}, {"seed": 55, "count": null, "done": true, "steps": 22, "seconds": 0.983, "policy_seconds": 0.0052}, {"seed": 56, "count": null, "done": true, "steps": 62, "seconds": 3.43, "policy_seconds": 0.0149}, {"seed": 57, "count": null, "done": true, "steps": 20, "seconds": 0.833, "policy_seconds": 0.0059}, {"seed": 58, "count": null, "done": true, "steps": 47, "seconds": 2.718, "policy_seconds": 0.0186}, {"seed": 59, "count": null, "done": true, "steps": 62, "seconds": 4.177, "policy_seconds": 0.0233}, {"seed": 60, "count": null, "done": true, "steps": 23, "seconds": 1.052, "policy_seconds": 0.0062}, {"seed": 61, "count": null, "done": true, "steps": 70, "seconds": 3.406, "policy_seconds": 0.0159}, {"seed": 62, "count": null, "done": true, "steps": 73, "seconds": 3.674, "policy_seconds": 0.0166}, {"seed": 63, "count": null, "done": true, "steps": 37, "seconds": 1.481, "policy_seconds": 0.0136}, {"seed": 64, "count": null, "done": true, "steps": 29, "seconds": 0.976, "policy_seconds": 0.0075}, {"seed": 65, "count": null, "done": true, "steps": 17, "seconds": 0.675, "policy_seconds": 0.0047}, {"seed": 66, "count": null, "done": true, "steps": 55, "seconds": 2.588, "policy_seconds": 0.021}, {"seed": 67, "count": null, "done": true, "steps": 54, "seconds": 2.724, "policy_seconds": 0.0106}, {"seed": 68, "count": null, "done": true, "steps": 47, "seconds": 1.8, "policy_seconds": 0.0163}, {"seed": 69, "count": null, "done": true, "steps": 36, "seconds": 1.157, "policy_seconds": 0.0057}, {"seed": 70, "count": null, "done": true, "steps": 81, "seconds": 3.848, "policy_seconds": 0.0177}, {"seed": 71, "count": null, "done": true, "steps": 42, "seconds": 2.269, "policy_seconds": 0.0097}, {"seed": 72, "count": null, "done": true, "steps": 96, "seconds": 5.037, "policy_seconds": 0.0217}, {"seed": 73, "count": null, "done": true, "steps": 73, "seconds": 3.902, "policy_seconds": 0.0198}, {"seed": 74, "count": null, "done": true, "steps": 25, "seconds": 1.168, "policy_seconds": 0.0053}, {"seed": 75, "count": null, "done": true, "steps": 71, "seconds": 3.465, "policy_seconds": 0.0203}, {"seed": 76, "count": null, "done": true, "steps": 31, "seconds": 1.412, "policy_seconds": 0.0072}, {"seed": 77, "count": null, "done": true, "steps": 19, "seconds": 0.441, "policy_seconds": 0.0052}, {"seed": 78, "count": null, "done": true, "steps": 114, "seconds": 7.469, "policy_seconds": 0.0327}, {"seed": 79, "count": null, "done": true, "steps": 34, "seconds": 1.244, "policy_seconds": 0.0074}, {"seed": 80, "count": null, "done": true, "steps": 63, "seconds": 4.07, "policy_seconds": 0.0193}, {"seed": 81, "count": null, "done": true, "steps": 22, "seconds": 0.954, "policy_seconds": 0.0058}, {"seed": 82, "count": null, "done": true, "steps": 35, "seconds": 2.503, "policy_seconds": 0.007}, {"seed": 83, "count": null, "done": true, "steps": 47, "seconds": 2.929, "policy_seconds": 0.0154}, {"seed": 84, "count": null, "done": true, "steps": 81, "seconds": 3.986, "policy_seconds": 0.0187}, {"seed": 85, "count": null, "done": true, "steps": 53, "seconds": 2.803, "policy_seconds": 0.0133}, {"seed": 86, "count": null, "done": true, "steps": 44, "seconds": 2.738, "policy_seconds": 0.0167}, {"seed": 87, "count": null, "done": true, "steps": 56, "seconds": 2.551, "policy_seconds": 0.0139}, {"seed": 88, "count": null, "done": true, "steps": 65, "seconds": 3.071, "policy_seconds": 0.0167}, {"seed": 89, "count": null, "done": true, "steps": 56, "seconds": 2.541, "policy_seconds": 0.0217}, {"seed": 90, "count": null, "done": true, "steps": 64, "seconds": 2.992, "policy_seconds": 0.0151}, {"seed": 91, "count": null, "done": true, "steps": 45, "seconds": 2.58, "policy_seconds": 0.0222}, {"seed": 92, "count": null, "done": true, "steps": 44, "seconds": 2.584, "policy_seconds": 0.0114}, {"seed": 93, "count": null, "done": true, "steps": 46, "seconds": 2.975, "policy_seconds": 0.0163}, {"seed": 94, "count": null, "done": true, "steps": 25, "seconds": 0.831, "policy_seconds": 0.0059}, {"seed": 95, "count": null, "done": true, "steps": 64, "seconds": 3.635, "policy_seconds": 0.018}, {"seed": 96, "count": null, "done": true, "steps": 30, "seconds": 1.901, "policy_seconds": 0.0126}, {"seed": 97, "count": null, "done": true, "steps": 33, "seconds": 1.456, "policy_seconds": 0.0071}, {"seed": 98, "count": null, "done": true, "steps": 53, "seconds": 2.399, "policy_seconds": 0.0158}, {"seed": 99, "count": null, "done": true, "steps": 44, "seconds": 1.622, "policy_seconds": 0.0105}]
\ No newline at end of file
diff --git a/results_2_3_4.json b/results_2_3_4.json
new file mode 100644
index 0000000..7ea599c
--- /dev/null
+++ b/results_2_3_4.json
@@ -0,0 +1 @@
           1 +[{"seed": 2, "count": 4, "done": true, "steps": 49, "seconds": 0.736, "policy_seconds": 0.0135}, {"seed": 3, "count": 4, "done": true, "steps": 86, "seconds": 2.492, "policy_seconds": 0.0201}, {"seed": 4, "count": 4, "done": true, "steps": 115, "seconds": 1.378, "policy_seconds": 0.0305}]
\ No newline at end of file
diff --git a/test_count4_sequential.py b/test_count4_sequential.py
new file mode 100644
index 0000000..82a6b7d
--- /dev/null
+++ b/test_count4_sequential.py
@@ -0,0 +1,32 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import sys,time,json,concurrent.futures
           4 +start=int(sys.argv[1]) if len(sys.argv)>1 else 0
           5 +n=int(sys.argv[2]) if len(sys.argv)>2 else 100
           6 +count=int(sys.argv[3]) if len(sys.argv)>3 else None
           7 +
           8 +def run(seed):
           9 + e=make_env()
          10 + try:
          11 +  s,i=e.reset(seed=seed,options={'object_count':count} if count is not None else None)
          12 +  p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
          13 +  st=time.time();trace=[];policy_seconds=0.0
          14 +  for t in range(e.max_steps):
          15 +   tick=time.perf_counter();a=p.get_action(s);policy_seconds+=time.perf_counter()-tick
          16 +   s,r,d,tr,i=e.step(a)
          17 +   if t%40==0:trace.append([t,p.phase,p.obj.name if p.obj else '',round(s.get(p.robot,'x'),4),round(s.get(p.robot,'y'),4)])
          18 +   if d or tr:break
          19 +  out=dict(seed=seed,count=count,done=d,steps=t+1,seconds=round(time.time()-st,3),policy_seconds=round(policy_seconds,4))
          20 +  if not d:out['trace']=trace[-4:];out['state']={o.name:{f:s.get(o,f) for f in ('x','y','width','height')} for o in s.get_objects(p.ot)}
          21 +  print(seed, "OK" if d else "FAIL", t+1, flush=True)
          22 +  if not d:print(out,flush=True)
          23 +  return out
          24 + except Exception as ex:return dict(seed=seed,count=count,error=str(ex))
          25 + finally:e.close()
          26 +
          27 +with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
          28 + results=list(ex.map(run,range(start,start+n)))
          29 +for r in results:
          30 + if not r.get('done'):print(r)
          31 +print('SUMMARY',len(results),'success',sum(r.get('done',False) for r in results),'mean_steps',round(sum(r.get('steps',0) for r in results)/len(results),2),'max_time',max(r.get('seconds',0) for r in results),flush=True)
          32 +json.dump(results,open('results_sequential_%s_%s_%s.json'%(start,n,count),'w'))
```

</details>

<a id="C029"></a>
### C029 · Document the geometric controller and remove unused bookkeeping

Commit `69ec7fab76f1715a9db7392925db98d45ab984ce`; parents: 77929e5c766f6a95f3c74b81897c925127c9ab2a. Recorded author date: 2026-09-21T22:46:23+02:00.

File roles (automatic): policy, setup/other.

- [E0106](01_timeline.md#E0106): commit hash in recorded output.
[Controller after this commit](evidence/versions/C029_69ec7fa_approach.py) · [Exact all-file diff](evidence/diffs/C029_69ec7fa.diff)

[Previous saved controller snapshot](evidence/versions/C027_c08b92a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index faf35ae..774cf04 100644
--- a/approach.py
+++ b/approach.py
@@ -2,6 +2,12 @@ import math
    2      2  import numpy as np
    3      3  
    4      4  class GeneratedApproach:
           5 +    """Geometric pick-and-place controller for a variable-size object set.
           6 +
           7 +    All scene geometry comes from the object-centric observation. The robot
           8 +    remains upright with its arm pointing down; obstructions are moved only
           9 +    when they interfere with the complete final placement configuration.
          10 +    """
    5     11      def __init__(self, action_space, observation_space, primitives):
    6     12          self.action_space = action_space
    7     13          self.observation_space = observation_space
@@ -16,11 +22,6 @@ class GeneratedApproach:
   16     22          self.surface = state.get_objects(self.st)[0]
   17     23          self.phase = 'select'
   18     24          self.obj = None
   19        -        self.n = 0
   20        -        self.stashed = []
   21        -
   22        -    def val(self, s, o, f):
   23        -        return s.get(o, f)
   24     25  
   25     26      def rect(self, s, o):
   26     27          return [s.get(o,f) for f in ('x','y','width','height')]
@@ -106,7 +107,7 @@ class GeneratedApproach:
  106    107              while bottom+h<=ceiling and not base_clear(left,bottom):bottom+=.01
  107    108              if bottom+h<=ceiling and bottom-self.offsety<=.89:stacks.append((left,bottom))
  108    109          if stacks:return min(stacks,key=lambda a:(a[1],abs(a[0]-x)))
  109        -        # Rare densely packed scenes: retain reachable coordinates for recovery.
         110 +        # If geometric candidates are exhausted, retain a legal base position.
  110    111          return float(np.clip(x,low,high)),max(.101,ceiling-h)
  111    112  
  112    113      def get_action(self, s):
@@ -132,19 +133,16 @@ class GeneratedApproach:
  132    133              x,y,w,h=self.rect(s,self.obj)
  133    134              if self.phase == 'above':
  134    135                  if ry<self.emptyheight-.001: return self.action(s,y=self.emptyheight)
  135        -                grasp_shift=min(0,1.516-(self.destx+w/2)) if self.obj==self.block else 0
  136    136                  grasp_x=self.target_grasp if self.obj==self.block else self.grasp_position(s,self.obj,x+w/2)
  137    137                  if abs(rx-grasp_x)>.001: return self.action(s,x=grasp_x,y=self.emptyheight)
  138        -                self.phase='down'; self.n=0; self.last_down=None
         138 +                self.phase='down'; self.last_down=None
  139    139              if self.phase == 'down':
  140        -                self.n+=1
  141    140                  goal=y+h+.2+.006
  142    141                  if ry>goal+.001 and (self.last_down is None or abs(ry-self.last_down)>.00001):
  143    142                      self.last_down=ry
  144    143                      return self.action(s,y=goal,vac=1)
  145        -                self.pick_y=y; self.phase='lift';self.n=0
         144 +                self.pick_y=y; self.phase='lift'
  146    145              if self.phase == 'lift':
  147        -                self.n+=1
  148    146                  if ry<self.carryheight-.001:return self.action(s,y=self.carryheight,vac=1)
  149    147                  if y < self.pick_y+.02:
  150    148                      self.phase='down'; self.last_down=None
@@ -163,7 +161,7 @@ class GeneratedApproach:
  163    161              if self.phase == 'place':
  164    162                  goal=self.dropy-self.offsety
  165    163                  if abs(ry-goal)>.001:return self.action(s,y=goal,vac=1)
  166        -                self.stashed.append(self.obj);self.phase='retreat'
         164 +                self.phase='retreat'
  167    165                  return self.action(s,vac=0)
  168    166              if self.phase=='retreat':
  169    167                  if ry<self.emptyheight-.001:return self.action(s,y=self.emptyheight,vac=0)
diff --git a/sweep_300_700.log b/sweep_300_700.log
new file mode 100644
index 0000000..8635201
--- /dev/null
+++ b/sweep_300_700.log
@@ -0,0 +1,56 @@
           1 +300 OK 28
           2 +301 OK 47
           3 +302 OK 54
           4 +303 OK 80
           5 +305 OK 29
           6 +304 OK 51
           7 +307 OK 38
           8 +306 OK 62
           9 +310 OK 24
          10 +308 OK 57
          11 +309 OK 79
          12 +311 OK 50
          13 +313 OK 27
          14 +312 OK 50
          15 +314 OK 37
          16 +315 OK 27
          17 +316 OK 29
          18 +317 OK 17
          19 +318 OK 48
          20 +320 OK 21
          21 +322 OK 27
          22 +321 OK 44
          23 +319 OK 72
          24 +323 OK 43
          25 +325 OK 23
          26 +324 OK 84
          27 +328 OK 21
          28 +326 OK 52
          29 +327 OK 34
          30 +329 OK 63
          31 +331 OK 22
          32 +330 OK 56
          33 +333 OK 17
          34 +334 OK 24
          35 +332 OK 51
          36 +335 OK 23
          37 +338 OK 21
          38 +336 OK 54
          39 +339 OK 37
          40 +337 OK 62
          41 +340 OK 16
          42 +343 OK 27
          43 +341 OK 56
          44 +344 OK 28
          45 +345 OK 36
          46 +342 OK 77
          47 +348 OK 32
          48 +347 OK 49
          49 +346 OK 94
          50 +349 OK 40
          51 +352 OK 38
          52 +350 OK 42
          53 +353 OK 31
          54 +351 OK 92
          55 +355 OK 29
          56 +356 OK 29
```

</details>

<a id="C030"></a>
### C030 · Report dense-scene validation checkpoint to expose policy stalls

Commit `67048b9fca41e0ccdb0652292cd24165b6780dcb`; parents: 69ec7fab76f1715a9db7392925db98d45ab984ce. Recorded author date: 2026-09-21T22:48:17+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C030_67048b9.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/sweep_300_700.log b/sweep_300_700.log
index 8635201..dc109d9 100644
--- a/sweep_300_700.log
+++ b/sweep_300_700.log
@@ -54,3 +54,62 @@
   54     54  351 OK 92
   55     55  355 OK 29
   56     56  356 OK 29
          57 +358 OK 46
          58 +354 OK 98
          59 +357 OK 75
          60 +359 OK 83
          61 +363 OK 48
          62 +361 OK 65
          63 +360 OK 72
          64 +362 OK 65
          65 +364 OK 30
          66 +365 OK 40
          67 +366 OK 26
          68 +370 OK 52
          69 +367 OK 97
          70 +368 OK 89
          71 +371 OK 20
          72 +369 OK 90
          73 +375 OK 33
          74 +373 OK 60
          75 +372 OK 79
          76 +374 OK 49
          77 +376 OK 78
          78 +379 OK 55
          79 +377 OK 64
          80 +378 OK 89
          81 +380 OK 49
          82 +382 OK 48
          83 +383 OK 36
          84 +384 OK 38
          85 +381 OK 84
          86 +386 OK 54
          87 +387 OK 61
          88 +389 OK 32
          89 +385 OK 90
          90 +388 OK 38
          91 +391 OK 41
          92 +390 OK 65
          93 +393 OK 23
          94 +394 OK 17
          95 +392 OK 47
          96 +395 OK 44
          97 +397 OK 48
          98 +398 OK 46
          99 +396 OK 80
         100 +401 OK 47
         101 +399 OK 101
         102 +403 OK 31
         103 +400 OK 100
         104 +402 OK 87
         105 +405 OK 37
         106 +404 OK 47
         107 +407 OK 30
         108 +406 OK 56
         109 +408 OK 21
         110 +409 OK 37
         111 +411 OK 32
         112 +410 OK 56
         113 +413 OK 24
         114 +412 OK 67
         115 +414 OK 52
```

</details>

<a id="C031"></a>
### C031 · Print step 200 phase and position in future sequential validation

Commit `0891dc101057f612d1d3b250ba190e3018152f10`; parents: 67048b9fca41e0ccdb0652292cd24165b6780dcb. Recorded author date: 2026-09-21T22:49:15+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C031_0891dc1.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/results_100_200_None.json b/results_100_200_None.json
index 8f7fe55..90a37e7 100644
--- a/results_100_200_None.json
+++ b/results_100_200_None.json
@@ -1 +1 @@
    1        -[{"seed": 100, "count": null, "done": true, "steps": 83, "seconds": 3.669}, {"seed": 101, "count": null, "done": true, "steps": 16, "seconds": 0.424}, {"seed": 102, "count": null, "done": true, "steps": 62, "seconds": 2.22}, {"seed": 103, "count": null, "done": true, "steps": 32, "seconds": 1.452}, {"seed": 104, "count": null, "done": true, "steps": 73, "seconds": 2.861}, {"seed": 105, "count": null, "done": true, "steps": 20, "seconds": 0.571}, {"seed": 106, "count": null, "done": true, "steps": 24, "seconds": 0.919}, {"seed": 107, "count": null, "done": true, "steps": 33, "seconds": 1.16}, {"seed": 108, "count": null, "done": true, "steps": 27, "seconds": 1.068}, {"seed": 109, "count": null, "done": true, "steps": 48, "seconds": 2.416}, {"seed": 110, "count": null, "done": true, "steps": 67, "seconds": 3.287}, {"seed": 111, "count": null, "done": true, "steps": 38, "seconds": 1.953}, {"seed": 112, "count": null, "done": true, "steps": 24, "seconds": 0.998}, {"seed": 113, "count": null, "done": true, "steps": 39, "seconds": 1.26}, {"seed": 114, "count": null, "done": true, "steps": 21, "seconds": 0.447}, {"seed": 115, "count": null, "done": true, "steps": 63, "seconds": 2.758}, {"seed": 116, "count": null, "done": true, "steps": 50, "seconds": 1.978}, {"seed": 117, "count": null, "done": true, "steps": 26, "seconds": 1.01}, {"seed": 118, "count": null, "done": true, "steps": 58, "seconds": 2.355}, {"seed": 119, "count": null, "done": true, "steps": 59, "seconds": 2.763}, {"seed": 120, "count": null, "done": true, "steps": 23, "seconds": 0.842}, {"seed": 121, "count": null, "done": true, "steps": 25, "seconds": 0.649}, {"seed": 122, "count": null, "done": true, "steps": 68, "seconds": 3.269}, {"seed": 123, "count": null, "done": true, "steps": 38, "seconds": 1.65}, {"seed": 124, "count": null, "done": true, "steps": 49, "seconds": 2.193}, {"seed": 125, "count": null, "done": true, "steps": 77, "seconds": 2.391}, {"seed": 126, "count": null, "done": true, "steps": 18, "seconds": 0.446}, {"seed": 127, "count": null, "done": true, "steps": 73, "seconds": 2.925}, {"seed": 128, "count": null, "done": true, "steps": 90, "seconds": 4.577}, {"seed": 129, "count": null, "done": true, "steps": 37, "seconds": 1.556}, {"seed": 130, "count": null, "done": true, "steps": 57, "seconds": 3.281}, {"seed": 131, "count": null, "done": true, "steps": 36, "seconds": 1.751}, {"seed": 132, "count": null, "done": true, "steps": 80, "seconds": 6.808}, {"seed": 133, "count": null, "done": true, "steps": 63, "seconds": 4.371}, {"seed": 134, "count": null, "done": true, "steps": 24, "seconds": 2.389}, {"seed": 135, "count": null, "done": true, "steps": 20, "seconds": 1.298}, {"seed": 136, "count": null, "done": true, "steps": 45, "seconds": 3.913}, {"seed": 137, "count": null, "done": true, "steps": 72, "seconds": 5.598}, {"seed": 138, "count": null, "done": true, "steps": 84, "seconds": 6.415}, {"seed": 139, "count": null, "done": true, "steps": 85, "seconds": 6.831}, {"seed": 140, "count": null, "done": true, "steps": 20, "seconds": 1.804}, {"seed": 141, "count": null, "done": true, "steps": 51, "seconds": 3.587}, {"seed": 142, "count": null, "done": true, "steps": 51, "seconds": 3.142}, {"seed": 143, "count": null, "done": true, "steps": 50, "seconds": 4.237}, {"seed": 144, "count": null, "done": true, "steps": 39, "seconds": 2.751}, {"seed": 145, "count": null, "done": true, "steps": 39, "seconds": 2.971}, {"seed": 146, "count": null, "done": true, "steps": 53, "seconds": 4.189}, {"seed": 147, "count": null, "done": true, "steps": 25, "seconds": 1.027}, {"seed": 148, "count": null, "done": true, "steps": 17, "seconds": 0.848}, {"seed": 149, "count": null, "done": true, "steps": 32, "seconds": 1.143}, {"seed": 150, "count": null, "done": true, "steps": 33, "seconds": 1.941}, {"seed": 151, "count": null, "done": false, "steps": 1000, "seconds": 103.878, "trace": [[840, "place", "target_block", 0.7788, 0.5182], [880, "place", "target_block", 0.7788, 0.5182], [920, "place", "target_block", 0.7788, 0.5182], [960, "place", "target_block", 0.7788, 0.5182]], "state": {"obstruction0": {"x": 0.8107884526252747, "y": 0.10000099986791611, "width": 0.1386185884475708, "height": 0.11362678557634354}, "obstruction1": {"x": 0.693976104259491, "y": 0.10000099986791611, "width": 0.05311352387070656, "height": 0.19954173266887665}, "target_block": {"x": 0.7532491087913513, "y": 0.12654274702072144, "width": 0.05102952942252159, "height": 0.18566597998142242}, "target_surface": {"x": 0.7150579690933228, "y": 0.0, "width": 0.09951850026845932, "height": 0.10000000149011612}}}, {"seed": 152, "count": null, "done": true, "steps": 39, "seconds": 3.248}, {"seed": 153, "count": null, "done": true, "steps": 65, "seconds": 6.169}, {"seed": 154, "count": null, "done": true, "steps": 41, "seconds": 2.63}, {"seed": 155, "count": null, "done": true, "steps": 29, "seconds": 1.787}, {"seed": 156, "count": null, "done": true, "steps": 71, "seconds": 6.784}, {"seed": 157, "count": null, "done": true, "steps": 37, "seconds": 2.639}, {"seed": 158, "count": null, "done": true, "steps": 84, "seconds": 5.325}, {"seed": 159, "count": null, "done": true, "steps": 51, "seconds": 4.743}, {"seed": 160, "count": null, "done": true, "steps": 20, "seconds": 1.322}, {"seed": 161, "count": null, "done": true, "steps": 44, "seconds": 4.037}, {"seed": 162, "count": null, "done": true, "steps": 59, "seconds": 5.063}, {"seed": 163, "count": null, "done": true, "steps": 38, "seconds": 3.401}, {"seed": 164, "count": null, "done": true, "steps": 52, "seconds": 4.734}, {"seed": 165, "count": null, "done": true, "steps": 66, "seconds": 6.429}, {"seed": 166, "count": null, "done": true, "steps": 47, "seconds": 5.833}, {"seed": 167, "count": null, "done": true, "steps": 70, "seconds": 6.838}, {"seed": 168, "count": null, "done": true, "steps": 43, "seconds": 3.039}, {"seed": 169, "count": null, "done": true, "steps": 75, "seconds": 7.314}, {"seed": 170, "count": null, "done": true, "steps": 48, "seconds": 5.681}, {"seed": 171, "count": null, "done": true, "steps": 63, "seconds": 6.923}, {"seed": 172, "count": null, "done": true, "steps": 42, "seconds": 3.571}, {"seed": 173, "count": null, "done": true, "steps": 70, "seconds": 7.286}, {"seed": 174, "count": null, "done": true, "steps": 61, "seconds": 6.039}, {"seed": 175, "count": null, "done": true, "steps": 46, "seconds": 5.631}, {"seed": 176, "count": null, "done": true, "steps": 33, "seconds": 2.629}, {"seed": 177, "count": null, "done": true, "steps": 52, "seconds": 5.26}, {"seed": 178, "count": null, "done": true, "steps": 83, "seconds": 6.561}, {"seed": 179, "count": null, "done": true, "steps": 58, "seconds": 5.683}, {"seed": 180, "count": null, "done": true, "steps": 39, "seconds": 2.489}, {"seed": 181, "count": null, "done": true, "steps": 59, "seconds": 5.814}, {"seed": 182, "count": null, "done": true, "steps": 101, "seconds": 11.229}, {"seed": 183, "count": null, "done": true, "steps": 63, "seconds": 6.44}, {"seed": 184, "count": null, "done": true, "steps": 53, "seconds": 5.376}, {"seed": 185, "count": null, "done": true, "steps": 25, "seconds": 2.233}, {"seed": 186, "count": null, "done": true, "steps": 23, "seconds": 1.188}, {"seed": 187, "count": null, "done": true, "steps": 55, "seconds": 4.541}, {"seed": 188, "count": null, "done": true, "steps": 22, "seconds": 1.779}, {"seed": 189, "count": null, "done": true, "steps": 35, "seconds": 2.658}, {"seed": 190, "count": null, "done": true, "steps": 17, "seconds": 0.805}, {"seed": 191, "count": null, "done": true, "steps": 33, "seconds": 2.053}, {"seed": 192, "count": null, "done": true, "steps": 49, "seconds": 4.106}, {"seed": 193, "count": null, "done": true, "steps": 59, "seconds": 3.925}, {"seed": 194, "count": null, "done": true, "steps": 74, "seconds": 6.377}, {"seed": 195, "count": null, "done": true, "steps": 26, "seconds": 1.638}, {"seed": 196, "count": null, "done": true, "steps": 39, "seconds": 2.337}, {"seed": 197, "count": null, "done": true, "steps": 90, "seconds": 6.173}, {"seed": 198, "count": null, "done": true, "steps": 61, "seconds": 2.884}, {"seed": 199, "count": null, "done": true, "steps": 49, "seconds": 2.48}, {"seed": 200, "count": null, "done": true, "steps": 23, "seconds": 1.018}, {"seed": 201, "count": null, "done": true, "steps": 28, "seconds": 1.056}, {"seed": 202, "count": null, "done": true, "steps": 36, "seconds": 1.224}, {"seed": 203, "count": null, "done": true, "steps": 36, "seconds": 1.367}, {"seed": 204, "count": null, "done": true, "steps": 48, "seconds": 2.859}, {"seed": 205, "count": null, "done": true, "steps": 38, "seconds": 1.579}, {"seed": 206, "count": null, "done": true, "steps": 62, "seconds": 3.172}, {"seed": 207, "count": null, "done": true, "steps": 20, "seconds": 0.814}, {"seed": 208, "count": null, "done": true, "steps": 28, "seconds": 2.062}, {"seed": 209, "count": null, "done": true, "steps": 42, "seconds": 2.807}, {"seed": 210, "count": null, "done": true, "steps": 21, "seconds": 1.418}, {"seed": 211, "count": null, "done": true, "steps": 31, "seconds": 1.514}, {"seed": 212, "count": null, "done": true, "steps": 33, "seconds": 1.618}, {"seed": 213, "count": null, "done": true, "steps": 19, "seconds": 0.908}, {"seed": 214, "count": null, "done": true, "steps": 43, "seconds": 2.059}, {"seed": 215, "count": null, "done": true, "steps": 70, "seconds": 4.696}, {"seed": 216, "count": null, "done": true, "steps": 31, "seconds": 2.063}, {"seed": 217, "count": null, "done": true, "steps": 53, "seconds": 3.447}, {"seed": 218, "count": null, "done": true, "steps": 44, "seconds": 2.352}, {"seed": 219, "count": null, "done": true, "steps": 23, "seconds": 1.256}, {"seed": 220, "count": null, "done": true, "steps": 48, "seconds": 3.109}, {"seed": 221, "count": null, "done": true, "steps": 57, "seconds": 3.668}, {"seed": 222, "count": null, "done": true, "steps": 47, "seconds": 2.951}, {"seed": 223, "count": null, "done": true, "steps": 33, "seconds": 1.855}, {"seed": 224, "count": null, "done": true, "steps": 52, "seconds": 3.143}, {"seed": 225, "count": null, "done": true, "steps": 92, "seconds": 5.74}, {"seed": 226, "count": null, "done": true, "steps": 76, "seconds": 4.641}, {"seed": 227, "count": null, "done": true, "steps": 57, "seconds": 3.049}, {"seed": 228, "count": null, "done": true, "steps": 59, "seconds": 3.061}, {"seed": 229, "count": null, "done": true, "steps": 30, "seconds": 1.813}, {"seed": 230, "count": null, "done": true, "steps": 40, "seconds": 1.961}, {"seed": 231, "count": null, "done": true, "steps": 31, "seconds": 1.324}, {"seed": 232, "count": null, "done": true, "steps": 25, "seconds": 1.635}, {"seed": 233, "count": null, "done": true, "steps": 25, "seconds": 1.346}, {"seed": 234, "count": null, "done": true, "steps": 46, "seconds": 2.795}, {"seed": 235, "count": null, "done": true, "steps": 65, "seconds": 4.046}, {"seed": 236, "count": null, "done": true, "steps": 75, "seconds": 3.809}, {"seed": 237, "count": null, "done": true, "steps": 90, "seconds": 7.009}, {"seed": 238, "count": null, "done": true, "steps": 19, "seconds": 0.962}, {"seed": 239, "count": null, "done": false, "steps": 1000, "seconds": 85.894, "trace": [[840, "place", "target_block", 0.1854, 0.4726], [880, "place", "target_block", 0.1854, 0.4726], [920, "place", "target_block", 0.1854, 0.4726], [960, "place", "target_block", 0.1854, 0.4726]], "state": {"obstruction0": {"x": 0.3029325008392334, "y": 0.10100004076957703, "width": 0.08481914550065994, "height": 0.11373668164014816}, "obstruction1": {"x": 0.2174888253211975, "y": 0.10000099986791611, "width": 0.07244367152452469, "height": 0.12870042026042938}, "target_block": {"x": 0.15883193910121918, "y": 0.20570142567157745, "width": 0.054496027529239655, "height": 0.06093798950314522}, "target_surface": {"x": 0.1535184234380722, "y": 0.0, "width": 0.09963131695985794, "height": 0.10000000149011612}}}, {"seed": 240, "count": null, "done": true, "steps": 83, "seconds": 7.283}, {"seed": 241, "count": null, "done": true, "steps": 18, "seconds": 0.998}, {"seed": 242, "count": null, "done": true, "steps": 74, "seconds": 7.018}, {"seed": 243, "count": null, "done": true, "steps": 34, "seconds": 3.187}, {"seed": 244, "count": null, "done": true, "steps": 49, "seconds": 4.66}, {"seed": 245, "count": null, "done": true, "steps": 42, "seconds": 3.582}, {"seed": 246, "count": null, "done": true, "steps": 71, "seconds": 6.489}, {"seed": 247, "count": null, "done": true, "steps": 33, "seconds": 2.103}, {"seed": 248, "count": null, "done": true, "steps": 53, "seconds": 3.826}, {"seed": 249, "count": null, "done": true, "steps": 48, "seconds": 4.005}, {"seed": 250, "count": null, "done": true, "steps": 78, "seconds": 5.597}, {"seed": 251, "count": null, "done": true, "steps": 18, "seconds": 1.11}, {"seed": 252, "count": null, "done": true, "steps": 95, "seconds": 9.471}, {"seed": 253, "count": null, "done": true, "steps": 56, "seconds": 4.683}, {"seed": 254, "count": null, "done": true, "steps": 31, "seconds": 2.293}, {"seed": 255, "count": null, "done": true, "steps": 27, "seconds": 1.775}, {"seed": 256, "count": null, "done": true, "steps": 33, "seconds": 2.589}, {"seed": 257, "count": null, "done": true, "steps": 40, "seconds": 4.227}, {"seed": 258, "count": null, "done": true, "steps": 45, "seconds": 4.295}, {"seed": 259, "count": null, "done": true, "steps": 20, "seconds": 1.562}, {"seed": 260, "count": null, "done": true, "steps": 48, "seconds": 3.92}, {"seed": 261, "count": null, "done": true, "steps": 81, "seconds": 5.021}, {"seed": 262, "count": null, "done": true, "steps": 61, "seconds": 5.02}, {"seed": 263, "count": null, "done": true, "steps": 58, "seconds": 4.778}, {"seed": 264, "count": null, "done": true, "steps": 44, "seconds": 2.382}, {"seed": 265, "count": null, "done": true, "steps": 64, "seconds": 5.46}, {"seed": 266, "count": null, "done": true, "steps": 53, "seconds": 3.771}, {"seed": 267, "count": null, "done": true, "steps": 52, "seconds": 3.5}, {"seed": 268, "count": null, "done": true, "steps": 98, "seconds": 7.981}, {"seed": 269, "count": null, "done": true, "steps": 54, "seconds": 4.941}, {"seed": 270, "count": null, "done": true, "steps": 43, "seconds": 2.812}, {"seed": 271, "count": null, "done": true, "steps": 54, "seconds": 4.286}, {"seed": 272, "count": null, "done": true, "steps": 20, "seconds": 1.04}, {"seed": 273, "count": null, "done": true, "steps": 31, "seconds": 1.739}, {"seed": 274, "count": null, "done": true, "steps": 38, "seconds": 2.366}, {"seed": 275, "count": null, "done": true, "steps": 34, "seconds": 1.543}, {"seed": 276, "count": null, "done": true, "steps": 24, "seconds": 1.51}, {"seed": 277, "count": null, "done": true, "steps": 31, "seconds": 1.743}, {"seed": 278, "count": null, "done": true, "steps": 26, "seconds": 1.107}, {"seed": 279, "count": null, "done": true, "steps": 47, "seconds": 2.979}, {"seed": 280, "count": null, "done": true, "steps": 30, "seconds": 2.076}, {"seed": 281, "count": null, "done": true, "steps": 43, "seconds": 2.544}, {"seed": 282, "count": null, "done": true, "steps": 46, "seconds": 3.17}, {"seed": 283, "count": null, "done": true, "steps": 52, "seconds": 2.771}, {"seed": 284, "count": null, "done": true, "steps": 23, "seconds": 1.073}, {"seed": 285, "count": null, "done": true, "steps": 77, "seconds": 4.874}, {"seed": 286, "count": null, "done": true, "steps": 29, "seconds": 1.407}, {"seed": 287, "count": null, "done": true, "steps": 87, "seconds": 5.782}, {"seed": 288, "count": null, "done": true, "steps": 21, "seconds": 0.792}, {"seed": 289, "count": null, "done": true, "steps": 33, "seconds": 2.063}, {"seed": 290, "count": null, "done": true, "steps": 36, "seconds": 2.243}, {"seed": 291, "count": null, "done": true, "steps": 31, "seconds": 1.907}, {"seed": 292, "count": null, "done": true, "steps": 90, "seconds": 6.855}, {"seed": 293, "count": null, "done": true, "steps": 33, "seconds": 1.683}, {"seed": 294, "count": null, "done": true, "steps": 29, "seconds": 1.943}, {"seed": 295, "count": null, "done": true, "steps": 51, "seconds": 3.142}, {"seed": 296, "count": null, "done": true, "steps": 27, "seconds": 1.245}, {"seed": 297, "count": null, "done": true, "steps": 35, "seconds": 1.737}, {"seed": 298, "count": null, "done": true, "steps": 46, "seconds": 1.031}, {"seed": 299, "count": null, "done": true, "steps": 71, "seconds": 1.256}]
\ No newline at end of file
           1 +[{"seed": 100, "count": null, "done": true, "steps": 85, "seconds": 4.225, "policy_seconds": 0.0268}, {"seed": 101, "count": null, "done": true, "steps": 16, "seconds": 0.531, "policy_seconds": 0.0024}, {"seed": 102, "count": null, "done": true, "steps": 72, "seconds": 3.753, "policy_seconds": 0.0176}, {"seed": 103, "count": null, "done": true, "steps": 32, "seconds": 1.249, "policy_seconds": 0.0052}, {"seed": 104, "count": null, "done": true, "steps": 73, "seconds": 3.947, "policy_seconds": 0.0199}, {"seed": 105, "count": null, "done": true, "steps": 20, "seconds": 0.793, "policy_seconds": 0.0054}, {"seed": 106, "count": null, "done": true, "steps": 24, "seconds": 1.037, "policy_seconds": 0.0072}, {"seed": 107, "count": null, "done": true, "steps": 33, "seconds": 1.453, "policy_seconds": 0.0056}, {"seed": 108, "count": null, "done": true, "steps": 27, "seconds": 1.021, "policy_seconds": 0.0067}, {"seed": 109, "count": null, "done": true, "steps": 45, "seconds": 2.11, "policy_seconds": 0.0105}, {"seed": 110, "count": null, "done": true, "steps": 75, "seconds": 3.473, "policy_seconds": 0.0188}, {"seed": 111, "count": null, "done": true, "steps": 38, "seconds": 1.717, "policy_seconds": 0.0084}, {"seed": 112, "count": null, "done": true, "steps": 24, "seconds": 0.868, "policy_seconds": 0.0059}, {"seed": 113, "count": null, "done": true, "steps": 39, "seconds": 1.691, "policy_seconds": 0.0044}, {"seed": 114, "count": null, "done": true, "steps": 21, "seconds": 0.987, "policy_seconds": 0.0053}, {"seed": 115, "count": null, "done": true, "steps": 80, "seconds": 4.103, "policy_seconds": 0.0209}, {"seed": 116, "count": null, "done": true, "steps": 50, "seconds": 2.111, "policy_seconds": 0.0103}, {"seed": 117, "count": null, "done": true, "steps": 26, "seconds": 1.002, "policy_seconds": 0.0065}, {"seed": 118, "count": null, "done": true, "steps": 59, "seconds": 3.296, "policy_seconds": 0.0176}, {"seed": 119, "count": null, "done": true, "steps": 59, "seconds": 3.047, "policy_seconds": 0.0166}, {"seed": 120, "count": null, "done": true, "steps": 23, "seconds": 0.981, "policy_seconds": 0.006}, {"seed": 121, "count": null, "done": true, "steps": 25, "seconds": 1.199, "policy_seconds": 0.0055}, {"seed": 122, "count": null, "done": true, "steps": 83, "seconds": 3.081, "policy_seconds": 0.0214}, {"seed": 123, "count": null, "done": true, "steps": 38, "seconds": 1.396, "policy_seconds": 0.0077}, {"seed": 124, "count": null, "done": true, "steps": 48, "seconds": 1.998, "policy_seconds": 0.0145}, {"seed": 125, "count": null, "done": true, "steps": 79, "seconds": 3.792, "policy_seconds": 0.0199}, {"seed": 126, "count": null, "done": true, "steps": 18, "seconds": 0.402, "policy_seconds": 0.0027}, {"seed": 127, "count": null, "done": true, "steps": 73, "seconds": 3.421, "policy_seconds": 0.0155}, {"seed": 128, "count": null, "done": true, "steps": 90, "seconds": 4.418, "policy_seconds": 0.0306}, {"seed": 129, "count": null, "done": true, "steps": 37, "seconds": 1.503, "policy_seconds": 0.0081}, {"seed": 130, "count": null, "done": true, "steps": 65, "seconds": 2.974, "policy_seconds": 0.0173}, {"seed": 131, "count": null, "done": true, "steps": 36, "seconds": 1.633, "policy_seconds": 0.0086}, {"seed": 132, "count": null, "done": true, "steps": 88, "seconds": 4.2, "policy_seconds": 0.0237}, {"seed": 133, "count": null, "done": true, "steps": 79, "seconds": 3.229, "policy_seconds": 0.018}, {"seed": 134, "count": null, "done": true, "steps": 24, "seconds": 1.147, "policy_seconds": 0.004}, {"seed": 135, "count": null, "done": true, "steps": 20, "seconds": 0.681, "policy_seconds": 0.0027}, {"seed": 136, "count": null, "done": true, "steps": 45, "seconds": 2.064, "policy_seconds": 0.0156}, {"seed": 137, "count": null, "done": true, "steps": 73, "seconds": 3.002, "policy_seconds": 0.0121}, {"seed": 138, "count": null, "done": true, "steps": 87, "seconds": 3.435, "policy_seconds": 0.0194}, {"seed": 139, "count": null, "done": true, "steps": 86, "seconds": 3.064, "policy_seconds": 0.0204}, {"seed": 140, "count": null, "done": true, "steps": 21, "seconds": 0.455, "policy_seconds": 0.0032}, {"seed": 141, "count": null, "done": true, "steps": 50, "seconds": 2.406, "policy_seconds": 0.0109}, {"seed": 142, "count": null, "done": true, "steps": 51, "seconds": 2.034, "policy_seconds": 0.0091}, {"seed": 143, "count": null, "done": true, "steps": 49, "seconds": 2.095, "policy_seconds": 0.0146}, {"seed": 144, "count": null, "done": true, "steps": 39, "seconds": 1.15, "policy_seconds": 0.0052}, {"seed": 145, "count": null, "done": true, "steps": 38, "seconds": 1.226, "policy_seconds": 0.0102}, {"seed": 146, "count": null, "done": true, "steps": 48, "seconds": 1.997, "policy_seconds": 0.0101}, {"seed": 147, "count": null, "done": true, "steps": 25, "seconds": 1.727, "policy_seconds": 0.0048}, {"seed": 148, "count": null, "done": true, "steps": 17, "seconds": 0.741, "policy_seconds": 0.0047}, {"seed": 149, "count": null, "done": true, "steps": 32, "seconds": 1.343, "policy_seconds": 0.0052}, {"seed": 150, "count": null, "done": true, "steps": 33, "seconds": 1.771, "policy_seconds": 0.004}, {"seed": 151, "count": null, "done": true, "steps": 46, "seconds": 3.148, "policy_seconds": 0.0173}, {"seed": 152, "count": null, "done": true, "steps": 39, "seconds": 2.959, "policy_seconds": 0.0172}, {"seed": 153, "count": null, "done": true, "steps": 69, "seconds": 5.54, "policy_seconds": 0.0213}, {"seed": 154, "count": null, "done": true, "steps": 41, "seconds": 2.541, "policy_seconds": 0.0084}, {"seed": 155, "count": null, "done": true, "steps": 29, "seconds": 2.137, "policy_seconds": 0.0072}, {"seed": 156, "count": null, "done": true, "steps": 67, "seconds": 5.351, "policy_seconds": 0.0262}, {"seed": 157, "count": null, "done": true, "steps": 37, "seconds": 2.658, "policy_seconds": 0.0077}, {"seed": 158, "count": null, "done": true, "steps": 34, "seconds": 2.414, "policy_seconds": 0.0091}, {"seed": 159, "count": null, "done": true, "steps": 47, "seconds": 3.66, "policy_seconds": 0.0151}, {"seed": 160, "count": null, "done": true, "steps": 20, "seconds": 1.112, "policy_seconds": 0.004}, {"seed": 161, "count": null, "done": true, "steps": 43, "seconds": 3.217, "policy_seconds": 0.0147}, {"seed": 162, "count": null, "done": true, "steps": 55, "seconds": 3.632, "policy_seconds": 0.0216}, {"seed": 163, "count": null, "done": true, "steps": 38, "seconds": 2.654, "policy_seconds": 0.0111}, {"seed": 164, "count": null, "done": true, "steps": 52, "seconds": 2.921, "policy_seconds": 0.0162}, {"seed": 165, "count": null, "done": true, "steps": 67, "seconds": 3.76, "policy_seconds": 0.0155}, {"seed": 166, "count": null, "done": true, "steps": 75, "seconds": 4.869, "policy_seconds": 0.0195}, {"seed": 167, "count": null, "done": true, "steps": 80, "seconds": 5.582, "policy_seconds": 0.02}, {"seed": 168, "count": null, "done": true, "steps": 43, "seconds": 2.189, "policy_seconds": 0.0079}, {"seed": 169, "count": null, "done": true, "steps": 81, "seconds": 8.919, "policy_seconds": 0.0213}, {"seed": 170, "count": null, "done": true, "steps": 54, "seconds": 6.135, "policy_seconds": 0.0155}, {"seed": 171, "count": null, "done": true, "steps": 62, "seconds": 6.938, "policy_seconds": 0.0122}, {"seed": 172, "count": null, "done": true, "steps": 21, "seconds": 2.076, "policy_seconds": 0.0069}, {"seed": 173, "count": null, "done": true, "steps": 83, "seconds": 7.593, "policy_seconds": 0.0195}, {"seed": 174, "count": null, "done": true, "steps": 61, "seconds": 4.889, "policy_seconds": 0.0129}, {"seed": 175, "count": null, "done": true, "steps": 46, "seconds": 4.53, "policy_seconds": 0.0135}, {"seed": 176, "count": null, "done": true, "steps": 33, "seconds": 2.257, "policy_seconds": 0.0069}, {"seed": 177, "count": null, "done": true, "steps": 52, "seconds": 5.108, "policy_seconds": 0.0173}, {"seed": 178, "count": null, "done": true, "steps": 83, "seconds": 6.475, "policy_seconds": 0.0179}, {"seed": 179, "count": null, "done": true, "steps": 58, "seconds": 5.915, "policy_seconds": 0.0133}, {"seed": 180, "count": null, "done": true, "steps": 39, "seconds": 2.46, "policy_seconds": 0.0052}, {"seed": 181, "count": null, "done": true, "steps": 59, "seconds": 4.917, "policy_seconds": 0.0259}, {"seed": 182, "count": null, "done": true, "steps": 77, "seconds": 7.977, "policy_seconds": 0.0217}, {"seed": 183, "count": null, "done": true, "steps": 63, "seconds": 6.938, "policy_seconds": 0.0173}, {"seed": 184, "count": null, "done": true, "steps": 70, "seconds": 6.132, "policy_seconds": 0.0145}, {"seed": 185, "count": null, "done": true, "steps": 25, "seconds": 1.723, "policy_seconds": 0.007}, {"seed": 186, "count": null, "done": true, "steps": 23, "seconds": 1.401, "policy_seconds": 0.0052}, {"seed": 187, "count": null, "done": true, "steps": 72, "seconds": 4.506, "policy_seconds": 0.0139}, {"seed": 188, "count": null, "done": true, "steps": 22, "seconds": 1.155, "policy_seconds": 0.0052}, {"seed": 189, "count": null, "done": true, "steps": 34, "seconds": 2.373, "policy_seconds": 0.0079}, {"seed": 190, "count": null, "done": true, "steps": 17, "seconds": 1.421, "policy_seconds": 0.0052}, {"seed": 191, "count": null, "done": true, "steps": 33, "seconds": 2.799, "policy_seconds": 0.0066}, {"seed": 192, "count": null, "done": true, "steps": 45, "seconds": 4.301, "policy_seconds": 0.0165}, {"seed": 193, "count": null, "done": true, "steps": 74, "seconds": 6.117, "policy_seconds": 0.0132}, {"seed": 194, "count": null, "done": true, "steps": 74, "seconds": 6.157, "policy_seconds": 0.0227}, {"seed": 195, "count": null, "done": true, "steps": 26, "seconds": 2.216, "policy_seconds": 0.0062}, {"seed": 196, "count": null, "done": true, "steps": 39, "seconds": 3.592, "policy_seconds": 0.0083}, {"seed": 197, "count": null, "done": true, "steps": 90, "seconds": 10.77, "policy_seconds": 0.0292}, {"seed": 198, "count": null, "done": true, "steps": 73, "seconds": 7.29, "policy_seconds": 0.0206}, {"seed": 199, "count": null, "done": true, "steps": 49, "seconds": 5.693, "policy_seconds": 0.014}, {"seed": 200, "count": null, "done": true, "steps": 23, "seconds": 1.959, "policy_seconds": 0.0061}, {"seed": 201, "count": null, "done": true, "steps": 28, "seconds": 1.7, "policy_seconds": 0.0059}, {"seed": 202, "count": null, "done": true, "steps": 36, "seconds": 2.059, "policy_seconds": 0.0071}, {"seed": 203, "count": null, "done": true, "steps": 36, "seconds": 2.063, "policy_seconds": 0.0079}, {"seed": 204, "count": null, "done": true, "steps": 48, "seconds": 3.924, "policy_seconds": 0.0169}, {"seed": 205, "count": null, "done": true, "steps": 38, "seconds": 2.868, "policy_seconds": 0.009}, {"seed": 206, "count": null, "done": true, "steps": 62, "seconds": 5.843, "policy_seconds": 0.0148}, {"seed": 207, "count": null, "done": true, "steps": 20, "seconds": 1.707, "policy_seconds": 0.0056}, {"seed": 208, "count": null, "done": true, "steps": 28, "seconds": 3.214, "policy_seconds": 0.0078}, {"seed": 209, "count": null, "done": true, "steps": 42, "seconds": 4.737, "policy_seconds": 0.0159}, {"seed": 210, "count": null, "done": true, "steps": 21, "seconds": 1.411, "policy_seconds": 0.0059}, {"seed": 211, "count": null, "done": true, "steps": 31, "seconds": 2.145, "policy_seconds": 0.0074}, {"seed": 212, "count": null, "done": true, "steps": 33, "seconds": 1.828, "policy_seconds": 0.0074}, {"seed": 213, "count": null, "done": true, "steps": 19, "seconds": 1.13, "policy_seconds": 0.0046}, {"seed": 214, "count": null, "done": true, "steps": 43, "seconds": 2.316, "policy_seconds": 0.0074}, {"seed": 215, "count": null, "done": true, "steps": 70, "seconds": 8.853, "policy_seconds": 0.0197}, {"seed": 216, "count": null, "done": true, "steps": 31, "seconds": 4.057, "policy_seconds": 0.0089}, {"seed": 217, "count": null, "done": true, "steps": 66, "seconds": 7.915, "policy_seconds": 0.0181}, {"seed": 218, "count": null, "done": true, "steps": 43, "seconds": 4.292, "policy_seconds": 0.014}, {"seed": 219, "count": null, "done": true, "steps": 23, "seconds": 1.505, "policy_seconds": 0.0056}, {"seed": 220, "count": null, "done": true, "steps": 48, "seconds": 4.934, "policy_seconds": 0.0174}, {"seed": 221, "count": null, "done": true, "steps": 65, "seconds": 6.386, "policy_seconds": 0.0158}, {"seed": 222, "count": null, "done": true, "steps": 47, "seconds": 4.363, "policy_seconds": 0.0152}, {"seed": 223, "count": null, "done": true, "steps": 33, "seconds": 2.902, "policy_seconds": 0.0066}, {"seed": 224, "count": null, "done": true, "steps": 49, "seconds": 5.238, "policy_seconds": 0.0108}, {"seed": 225, "count": null, "done": true, "steps": 92, "seconds": 10.286, "policy_seconds": 0.0281}, {"seed": 226, "count": null, "done": true, "steps": 81, "seconds": 9.204, "policy_seconds": 0.0276}, {"seed": 227, "count": null, "done": true, "steps": 61, "seconds": 5.21, "policy_seconds": 0.0127}, {"seed": 228, "count": null, "done": true, "steps": 62, "seconds": 5.261, "policy_seconds": 0.0146}, {"seed": 229, "count": null, "done": true, "steps": 30, "seconds": 2.197, "policy_seconds": 0.0087}, {"seed": 230, "count": null, "done": true, "steps": 44, "seconds": 2.917, "policy_seconds": 0.0081}, {"seed": 231, "count": null, "done": true, "steps": 31, "seconds": 2.241, "policy_seconds": 0.0062}, {"seed": 232, "count": null, "done": true, "steps": 25, "seconds": 1.527, "policy_seconds": 0.0038}, {"seed": 233, "count": null, "done": true, "steps": 25, "seconds": 1.72, "policy_seconds": 0.0054}, {"seed": 234, "count": null, "done": true, "steps": 46, "seconds": 4.018, "policy_seconds": 0.0108}, {"seed": 235, "count": null, "done": true, "steps": 65, "seconds": 7.411, "policy_seconds": 0.0107}, {"seed": 236, "count": null, "done": true, "steps": 84, "seconds": 6.939, "policy_seconds": 0.0166}, {"seed": 237, "count": null, "done": true, "steps": 101, "seconds": 10.706, "policy_seconds": 0.032}, {"seed": 238, "count": null, "done": true, "steps": 19, "seconds": 2.395, "policy_seconds": 0.0062}, {"seed": 239, "count": null, "done": true, "steps": 94, "seconds": 10.361, "policy_seconds": 0.0286}, {"seed": 240, "count": null, "done": true, "steps": 97, "seconds": 9.877, "policy_seconds": 0.0368}, {"seed": 241, "count": null, "done": true, "steps": 18, "seconds": 1.313, "policy_seconds": 0.0053}, {"seed": 242, "count": null, "done": true, "steps": 90, "seconds": 9.901, "policy_seconds": 0.0246}, {"seed": 243, "count": null, "done": true, "steps": 34, "seconds": 3.141, "policy_seconds": 0.0049}, {"seed": 244, "count": null, "done": true, "steps": 76, "seconds": 8.52, "policy_seconds": 0.02}, {"seed": 245, "count": null, "done": true, "steps": 43, "seconds": 5.235, "policy_seconds": 0.0102}, {"seed": 246, "count": null, "done": true, "steps": 71, "seconds": 7.624, "policy_seconds": 0.0196}, {"seed": 247, "count": null, "done": true, "steps": 33, "seconds": 2.183, "policy_seconds": 0.0078}, {"seed": 248, "count": null, "done": true, "steps": 53, "seconds": 3.97, "policy_seconds": 0.0116}, {"seed": 249, "count": null, "done": true, "steps": 57, "seconds": 5.596, "policy_seconds": 0.011}, {"seed": 250, "count": null, "done": true, "steps": 82, "seconds": 6.474, "policy_seconds": 0.019}, {"seed": 251, "count": null, "done": true, "steps": 18, "seconds": 1.567, "policy_seconds": 0.005}, {"seed": 252, "count": null, "done": true, "steps": 95, "seconds": 8.437, "policy_seconds": 0.0249}, {"seed": 253, "count": null, "done": true, "steps": 74, "seconds": 5.408, "policy_seconds": 0.0153}, {"seed": 254, "count": null, "done": true, "steps": 31, "seconds": 2.282, "policy_seconds": 0.0067}, {"seed": 255, "count": null, "done": true, "steps": 27, "seconds": 1.497, "policy_seconds": 0.0065}, {"seed": 256, "count": null, "done": true, "steps": 33, "seconds": 2.607, "policy_seconds": 0.0068}, {"seed": 257, "count": null, "done": true, "steps": 61, "seconds": 5.96, "policy_seconds": 0.0158}, {"seed": 258, "count": null, "done": true, "steps": 46, "seconds": 4.312, "policy_seconds": 0.0091}, {"seed": 259, "count": null, "done": true, "steps": 20, "seconds": 1.736, "policy_seconds": 0.0069}, {"seed": 260, "count": null, "done": true, "steps": 48, "seconds": 5.279, "policy_seconds": 0.0138}, {"seed": 261, "count": null, "done": true, "steps": 81, "seconds": 7.186, "policy_seconds": 0.0223}, {"seed": 262, "count": null, "done": true, "steps": 77, "seconds": 7.381, "policy_seconds": 0.0164}, {"seed": 263, "count": null, "done": true, "steps": 58, "seconds": 6.124, "policy_seconds": 0.0138}, {"seed": 264, "count": null, "done": true, "steps": 44, "seconds": 3.156, "policy_seconds": 0.007}, {"seed": 265, "count": null, "done": true, "steps": 77, "seconds": 8.161, "policy_seconds": 0.024}, {"seed": 266, "count": null, "done": true, "steps": 49, "seconds": 4.516, "policy_seconds": 0.0138}, {"seed": 267, "count": null, "done": true, "steps": 49, "seconds": 4.268, "policy_seconds": 0.0139}, {"seed": 268, "count": null, "done": true, "steps": 101, "seconds": 9.375, "policy_seconds": 0.0248}, {"seed": 269, "count": null, "done": true, "steps": 54, "seconds": 5.179, "policy_seconds": 0.0174}, {"seed": 270, "count": null, "done": true, "steps": 43, "seconds": 3.165, "policy_seconds": 0.0133}, {"seed": 271, "count": null, "done": true, "steps": 56, "seconds": 5.034, "policy_seconds": 0.0176}, {"seed": 272, "count": null, "done": true, "steps": 20, "seconds": 1.235, "policy_seconds": 0.0047}, {"seed": 273, "count": null, "done": true, "steps": 31, "seconds": 2.572, "policy_seconds": 0.0082}, {"seed": 274, "count": null, "done": true, "steps": 38, "seconds": 2.759, "policy_seconds": 0.0087}, {"seed": 275, "count": null, "done": true, "steps": 34, "seconds": 2.025, "policy_seconds": 0.007}, {"seed": 276, "count": null, "done": true, "steps": 24, "seconds": 1.647, "policy_seconds": 0.0055}, {"seed": 277, "count": null, "done": true, "steps": 31, "seconds": 1.985, "policy_seconds": 0.0063}, {"seed": 278, "count": null, "done": true, "steps": 26, "seconds": 2.405, "policy_seconds": 0.0061}, {"seed": 279, "count": null, "done": true, "steps": 46, "seconds": 5.014, "policy_seconds": 0.0164}, {"seed": 280, "count": null, "done": true, "steps": 29, "seconds": 2.992, "policy_seconds": 0.007}, {"seed": 281, "count": null, "done": true, "steps": 43, "seconds": 4.053, "policy_seconds": 0.011}, {"seed": 282, "count": null, "done": true, "steps": 46, "seconds": 4.385, "policy_seconds": 0.0115}, {"seed": 283, "count": null, "done": true, "steps": 52, "seconds": 3.332, "policy_seconds": 0.0091}, {"seed": 284, "count": null, "done": true, "steps": 23, "seconds": 1.938, "policy_seconds": 0.0034}, {"seed": 285, "count": null, "done": true, "steps": 73, "seconds": 7.15, "policy_seconds": 0.0186}, {"seed": 286, "count": null, "done": true, "steps": 29, "seconds": 3.369, "policy_seconds": 0.006}, {"seed": 287, "count": null, "done": true, "steps": 87, "seconds": 7.863, "policy_seconds": 0.021}, {"seed": 288, "count": null, "done": true, "steps": 21, "seconds": 1.896, "policy_seconds": 0.0056}, {"seed": 289, "count": null, "done": true, "steps": 33, "seconds": 2.235, "policy_seconds": 0.0084}, {"seed": 290, "count": null, "done": true, "steps": 36, "seconds": 2.543, "policy_seconds": 0.0079}, {"seed": 291, "count": null, "done": true, "steps": 31, "seconds": 1.825, "policy_seconds": 0.0071}, {"seed": 292, "count": null, "done": true, "steps": 89, "seconds": 8.472, "policy_seconds": 0.0253}, {"seed": 293, "count": null, "done": true, "steps": 33, "seconds": 2.191, "policy_seconds": 0.0063}, {"seed": 294, "count": null, "done": true, "steps": 29, "seconds": 1.479, "policy_seconds": 0.0069}, {"seed": 295, "count": null, "done": true, "steps": 51, "seconds": 3.964, "policy_seconds": 0.008}, {"seed": 296, "count": null, "done": true, "steps": 27, "seconds": 2.137, "policy_seconds": 0.0059}, {"seed": 297, "count": null, "done": true, "steps": 35, "seconds": 2.25, "policy_seconds": 0.0057}, {"seed": 298, "count": null, "done": true, "steps": 44, "seconds": 3.904, "policy_seconds": 0.0112}, {"seed": 299, "count": null, "done": true, "steps": 71, "seconds": 5.527, "policy_seconds": 0.0131}]
\ No newline at end of file
diff --git a/sweep_300_700.log b/sweep_300_700.log
index dc109d9..3b0d199 100644
--- a/sweep_300_700.log
+++ b/sweep_300_700.log
@@ -113,3 +113,61 @@
  113    113  413 OK 24
  114    114  412 OK 67
  115    115  414 OK 52
         116 +415 OK 70
         117 +417 OK 30
         118 +416 OK 68
         119 +418 OK 25
         120 +419 OK 26
         121 +420 OK 43
         122 +421 OK 45
         123 +422 OK 35
         124 +424 OK 20
         125 +423 OK 35
         126 +425 OK 32
         127 +426 OK 25
         128 +428 OK 24
         129 +429 OK 30
         130 +427 OK 48
         131 +430 OK 32
         132 +433 OK 33
         133 +431 OK 58
         134 +432 OK 43
         135 +434 OK 27
         136 +435 OK 47
         137 +438 OK 41
         138 +437 OK 57
         139 +436 OK 72
         140 +439 OK 34
         141 +440 OK 23
         142 +442 OK 21
         143 +443 OK 39
         144 +445 OK 28
         145 +441 OK 85
         146 +444 OK 64
         147 +446 OK 47
         148 +450 OK 28
         149 +448 OK 46
         150 +447 OK 58
         151 +449 OK 59
         152 +451 OK 22
         153 +452 OK 72
         154 +453 OK 80
         155 +454 OK 65
         156 +455 OK 69
         157 +457 OK 28
         158 +458 OK 41
         159 +456 OK 49
         160 +460 OK 29
         161 +459 OK 51
         162 +461 OK 34
         163 +464 OK 27
         164 +465 OK 29
         165 +463 OK 66
         166 +467 OK 25
         167 +462 OK 91
         168 +469 OK 18
         169 +466 OK 75
         170 +468 OK 56
         171 +473 OK 22
         172 +470 OK 43
         173 +471 OK 35
diff --git a/test_count4_sequential.py b/test_count4_sequential.py
index 82a6b7d..bd70fdd 100644
--- a/test_count4_sequential.py
+++ b/test_count4_sequential.py
@@ -14,6 +14,7 @@ def run(seed):
   14     14    for t in range(e.max_steps):
   15     15     tick=time.perf_counter();a=p.get_action(s);policy_seconds+=time.perf_counter()-tick
   16     16     s,r,d,tr,i=e.step(a)
          17 +   if t==199:print('CHECKPOINT',seed,t+1,p.phase,p.obj.name,round(s.get(p.robot,'x'),4),round(s.get(p.robot,'y'),4),flush=True)
   17     18     if t%40==0:trace.append([t,p.phase,p.obj.name if p.obj else '',round(s.get(p.robot,'x'),4),round(s.get(p.robot,'y'),4)])
   18     19     if d or tr:break
   19     20    out=dict(seed=seed,count=count,done=d,steps=t+1,seconds=round(time.time()-st,3),policy_seconds=round(policy_seconds,4))
```

</details>

<a id="C032"></a>
### C032 · Keep obstruction storage clear of the future target pickup configuration

Commit `692cf64c5da43c2dfbd4fa3891913450f14677b7`; parents: 0891dc101057f612d1d3b250ba190e3018152f10. Recorded author date: 2026-09-21T22:49:25+02:00.

File roles (automatic): policy, setup/other.

- [E0136](01_timeline.md#E0136): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C032_692cf64_approach.py) · [Exact all-file diff](evidence/diffs/C032_692cf64.diff)

[Previous saved controller snapshot](evidence/versions/C029_69ec7fa_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 774cf04..b1d624a 100644
--- a/approach.py
+++ b/approach.py
@@ -78,6 +78,8 @@ class GeneratedApproach:
   78     78          goalcx=self.destx-bx+self.target_grasp
   79     79          reserve_left=min(self.destx,goalcx-.105)
   80     80          reserve_right=max(self.destx+bw,goalcx+.105)
          81 +        pickup_left=min(bx,self.target_grasp-.105)
          82 +        pickup_right=max(bx+bw,self.target_grasp+.105)
   81     83          low=max(.005,.101+self.offsetx)
   82     84          high=min(1.613-w,1.517+self.offsetx)
   83     85          positions=[low,high,float(np.clip(x,low,high))]
@@ -89,6 +91,7 @@ class GeneratedApproach:
   89     91          for left in positions:
   90     92              if left<low or left>high:continue
   91     93              if left<reserve_right+.008 and left+w>reserve_left-.008:continue
          94 +            if left<pickup_right+.008 and left+w>pickup_left-.008:continue
   92     95              if any(left<ox+ow+.012 and left+w>ox-.012 for o,(ox,oy,ow,oh) in others):continue
   93     96              if base_clear(left,.101):floor.append(left)
   94     97          if floor:return min(floor,key=lambda left:abs(left-x)),.101
@@ -100,6 +103,7 @@ class GeneratedApproach:
  100    103          for left in positions:
  101    104              if left<low or left>high:continue
  102    105              if left<reserve_right+.02 and left+w>reserve_left-.02:continue
         106 +            if left<pickup_right+.02 and left+w>pickup_left-.02:continue
  103    107              if any(o in (self.surface,self.block) and left<ox+ow+.04 and left+w>ox-.04 for o,(ox,oy,ow,oh) in others):continue
  104    108              bottom=.101
  105    109              for o,(ox,oy,ow,oh) in others:
diff --git a/sweep_300_700.log b/sweep_300_700.log
index 3b0d199..d1cee4f 100644
--- a/sweep_300_700.log
+++ b/sweep_300_700.log
@@ -171,3 +171,14 @@
  171    171  473 OK 22
  172    172  470 OK 43
  173    173  471 OK 35
         174 +472 OK 38
         175 +474 OK 27
         176 +478 OK 19
         177 +476 OK 78
         178 +475 OK 82
         179 +477 OK 71
         180 +482 OK 22
         181 +479 OK 87
         182 +481 OK 42
         183 +483 OK 21
         184 +485 OK 18
```

</details>

<a id="C033"></a>
### C033 · Add carried-block clearance and tighten horizontal placement accuracy

Commit `394488db6e0d8aebb580af5b333be38bcd35cd88`; parents: 692cf64c5da43c2dfbd4fa3891913450f14677b7. Recorded author date: 2026-09-21T22:52:38+02:00.

File roles (automatic): policy, setup/other.

- [E0134](01_timeline.md#E0134): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C033_394488d_approach.py) · [Exact all-file diff](evidence/diffs/C033_394488d.diff)

[Previous saved controller snapshot](evidence/versions/C032_692cf64_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b1d624a..f3fb83c 100644
--- a/approach.py
+++ b/approach.py
@@ -57,7 +57,7 @@ class GeneratedApproach:
   57     57      def placement_collisions(self, s, obj, left, bottom, offsetx, offsety):
   58     58          _,_,w,h=self.rect(s,obj)
   59     59          cx=left-offsetx;cy=bottom-offsety
   60        -        parts=[(left,bottom,left+w,bottom+h),
          60 +        parts=[(left-.003,bottom,left+w+.003,bottom+h),
   61     61                 (cx-.055,cy-.225,cx+.055,cy-.185),
   62     62                 (cx-.008,cy-.2,cx+.008,cy)]
   63     63          blocked=[]
@@ -160,7 +160,7 @@ class GeneratedApproach:
  160    160                  self.phase='carry'
  161    161              if self.phase == 'carry':
  162    162                  goal=self.dropx-self.offsetx
  163        -                if abs(rx-goal)>.001:return self.action(s,x=goal,vac=1)
         163 +                if abs(rx-goal)>.0001:return self.action(s,x=goal,vac=1)
  164    164                  self.phase='place'
  165    165              if self.phase == 'place':
  166    166                  goal=self.dropy-self.offsety
diff --git a/results_2_1_4.json b/results_2_1_4.json
index 5351e56..e6aad0c 100644
--- a/results_2_1_4.json
+++ b/results_2_1_4.json
@@ -1 +1 @@
    1        -[{"seed": 2, "count": 4, "done": false, "steps": 1000, "seconds": 102.677, "policy_seconds": 0.1575, "trace": [[840, "place", "target_block", 1.06, 0.439], [880, "place", "target_block", 1.06, 0.439], [920, "place", "target_block", 1.06, 0.439], [960, "place", "target_block", 1.06, 0.439]], "state": {"obstruction0": {"x": 0.41724511981010437, "y": 0.10000099986791611, "width": 0.16559429466724396, "height": 0.19393038749694824}, "obstruction1": {"x": 1.1710095405578613, "y": 0.10099999606609344, "width": 0.18252427875995636, "height": 0.16370268166065216}, "obstruction2": {"x": 0.6930773258209229, "y": 0.10000099986791611, "width": 0.19260691106319427, "height": 0.13893510401248932}, "obstruction3": {"x": 0.9658926725387573, "y": 0.10000099986791611, "width": 0.06577402353286743, "height": 0.09953121095895767}, "target_block": {"x": 1.0440634489059448, "y": 0.1701126992702484, "width": 0.0980890691280365, "height": 0.06211165711283684}, "target_surface": {"x": 1.0282063484191895, "y": 0.0, "width": 0.1298033446073532, "height": 0.10000000149011612}}}]
\ No newline at end of file
           1 +[{"seed": 2, "count": 4, "done": true, "steps": 137, "seconds": 12.336, "policy_seconds": 0.0332}]
\ No newline at end of file
diff --git a/results_sequential_0_10_4.json b/results_sequential_0_10_4.json
new file mode 100644
index 0000000..6ee07ba
--- /dev/null
+++ b/results_sequential_0_10_4.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "count": 4, "done": true, "steps": 51, "seconds": 4.431, "policy_seconds": 0.0176}, {"seed": 1, "count": 4, "done": true, "steps": 79, "seconds": 10.312, "policy_seconds": 0.0261}, {"seed": 2, "count": 4, "done": false, "steps": 1000, "seconds": 136.432, "policy_seconds": 0.1705, "trace": [[840, "down", "target_block", 1.517, 0.489], [880, "down", "target_block", 1.517, 0.489], [920, "down", "target_block", 1.517, 0.489], [960, "down", "target_block", 1.517, 0.489]], "state": {"obstruction0": {"x": 0.41724511981010437, "y": 0.10000099986791611, "width": 0.16559429466724396, "height": 0.19393038749694824}, "obstruction1": {"x": 1.3055542707443237, "y": 0.10099999606609344, "width": 0.18252427875995636, "height": 0.16370268166065216}, "obstruction2": {"x": 0.6930773258209229, "y": 0.10000099986791611, "width": 0.19260691106319427, "height": 0.13893510401248932}, "obstruction3": {"x": 0.06811296939849854, "y": 0.10100000351667404, "width": 0.06577402353286743, "height": 0.09953121095895767}, "target_block": {"x": 1.5010786056518555, "y": 0.10000099986791611, "width": 0.0980890691280365, "height": 0.06211165711283684}, "target_surface": {"x": 1.0282063484191895, "y": 0.0, "width": 0.1298033446073532, "height": 0.10000000149011612}}}, {"seed": 3, "count": 4, "done": true, "steps": 101, "seconds": 12.335, "policy_seconds": 0.0343}, {"seed": 4, "count": 4, "done": true, "steps": 158, "seconds": 10.732, "policy_seconds": 0.033}, {"seed": 5, "count": 4, "done": true, "steps": 83, "seconds": 5.098, "policy_seconds": 0.0155}, {"seed": 6, "count": 4, "done": true, "steps": 115, "seconds": 10.369, "policy_seconds": 0.0351}, {"seed": 7, "count": 4, "done": true, "steps": 91, "seconds": 9.357, "policy_seconds": 0.0253}, {"seed": 8, "count": 4, "done": true, "steps": 102, "seconds": 14.707, "policy_seconds": 0.0215}, {"seed": 9, "count": 4, "done": true, "steps": 79, "seconds": 9.597, "policy_seconds": 0.0256}]
\ No newline at end of file
diff --git a/sweep_300_700.log b/sweep_300_700.log
index d1cee4f..4276ca6 100644
--- a/sweep_300_700.log
+++ b/sweep_300_700.log
@@ -182,3 +182,110 @@
  182    182  481 OK 42
  183    183  483 OK 21
  184    184  485 OK 18
         185 +486 OK 24
         186 +484 OK 67
         187 +480 OK 104
         188 +487 OK 26
         189 +490 OK 57
         190 +491 OK 56
         191 +488 OK 92
         192 +493 OK 48
         193 +494 OK 45
         194 +492 OK 70
         195 +495 OK 27
         196 +497 OK 25
         197 +496 OK 33
         198 +500 OK 18
         199 +498 OK 61
         200 +502 OK 26
         201 +501 OK 64
         202 +503 OK 24
         203 +499 OK 109
         204 +506 OK 50
         205 +504 OK 80
         206 +505 OK 84
         207 +508 OK 49
         208 +507 OK 78
         209 +510 OK 27
         210 +509 OK 68
         211 +512 OK 26
         212 +511 OK 70
         213 +513 OK 46
         214 +515 OK 41
         215 +516 OK 34
         216 +514 OK 74
         217 +518 OK 41
         218 +517 OK 71
         219 +519 OK 28
         220 +520 OK 21
         221 +521 OK 35
         222 +522 OK 53
         223 +524 OK 20
         224 +523 OK 41
         225 +526 OK 33
         226 +489 FAIL 1000
         227 +{'seed': 489, 'count': None, 'done': False, 'steps': 1000, 'seconds': 68.581, 'policy_seconds': 0.1308, 'trace': [[840, 'place', 'target_block', 0.5194, 0.4876], [880, 'place', 'target_block', 0.5194, 0.4876], [920, 'place', 'target_block', 0.5194, 0.4876], [960, 'place', 'target_block', 0.5194, 0.4876]], 'state': {'obstruction0': {'x': 0.6125882863998413, 'y': 0.10000099986791611, 'width': 0.08571477979421616, 'height': 0.09336432069540024}, 'obstruction1': {'x': 0.8762147426605225, 'y': 0.10100002586841583, 'width': 0.07839120179414749, 'height': 0.1896573305130005}, 'target_block': {'x': 0.5144228339195251, 'y': 0.21765734255313873, 'width': 0.09879190474748611, 'height': 0.06392852216959}, 'target_surface': {'x': 0.5127172470092773, 'y': 0.0, 'width': 0.12958014011383057, 'height': 0.10000000149011612}}}
         228 +528 OK 17
         229 +527 OK 59
         230 +525 OK 80
         231 +529 OK 23
         232 +530 OK 30
         233 +531 OK 51
         234 +533 OK 31
         235 +535 OK 21
         236 +532 OK 67
         237 +537 OK 22
         238 +534 OK 78
         239 +538 OK 29
         240 +539 OK 24
         241 +536 OK 90
         242 +540 OK 20
         243 +541 OK 72
         244 +544 OK 27
         245 +542 OK 85
         246 +543 OK 64
         247 +546 OK 29
         248 +547 OK 24
         249 +545 OK 80
         250 +548 OK 44
         251 +549 OK 53
         252 +551 OK 33
         253 +552 OK 30
         254 +554 OK 19
         255 +550 OK 95
         256 +553 OK 85
         257 +555 OK 56
         258 +558 OK 28
         259 +556 OK 56
         260 +559 OK 27
         261 +557 OK 52
         262 +561 OK 19
         263 +562 OK 30
         264 +564 OK 19
         265 +563 OK 30
         266 +560 OK 77
         267 +567 OK 26
         268 +565 OK 76
         269 +566 OK 60
         270 +569 OK 23
         271 +570 OK 36
         272 +568 OK 72
         273 +571 OK 47
         274 +572 OK 48
         275 +574 OK 22
         276 +573 OK 61
         277 +576 OK 36
         278 +575 OK 58
         279 +577 OK 69
         280 +580 OK 33
         281 +579 OK 77
         282 +578 OK 76
         283 +581 OK 19
         284 +582 OK 61
         285 +583 OK 30
         286 +585 OK 29
         287 +584 OK 33
         288 +587 OK 47
         289 +586 OK 54
         290 +588 OK 44
         291 +589 OK 31
```

</details>

<a id="C034"></a>
### C034 · Add reproducible edge-case regression suite and policy documentation

Commit `01878e6afd3a5760a3e58f05bcbca5df9bce98f3`; parents: 394488db6e0d8aebb580af5b333be38bcd35cd88. Recorded author date: 2026-09-21T22:53:40+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0150](01_timeline.md#E0150): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C034_01878e6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

````text
 OLD   NEW   CHANGE
diff --git a/README.md b/README.md
new file mode 100644
index 0000000..deee1b8
--- /dev/null
+++ b/README.md
@@ -0,0 +1,16 @@
           1 +# Black-box Obstruction2D policy
           2 +
           3 +`approach.py` contains `GeneratedApproach` and imports only the standard library and NumPy. It reads typed objects directly and makes no assumptions about the number or ordering of obstructions.
           4 +
           5 +The controller chooses a target placement, removes interfering obstructions, grasps from above, and carries the target to the surface. Planning accounts for the carried block, gripper, arm, base, room boundaries, and the future target pickup. Obstruction storage uses free floor gaps, with low elevated placements when necessary. Motion is checked through observed progress and grasp success through lifting. Planning uses bounded geometric candidate sets rather than a simulator or exhaustive action search.
           6 +
           7 +Run tests with the supplied interpreter:
           8 +
           9 +```sh
          10 +/opt/robocode-strict/bin/python test_approach.py 0 1 2 3 4
          11 +/opt/robocode-strict/bin/python test_batch.py 0 100
          12 +/opt/robocode-strict/bin/python test_batch.py 0 100 3
          13 +/opt/robocode-strict/bin/python test_regression.py
          14 +```
          15 +
          16 +The optional third batch argument pins the obstruction count. Each test environment is a fresh live-server instance. The regression suite covers wall reach, narrow grasp clearances, gripper placement collisions, and storage that could obstruct a later pickup. Policy computation is timed separately from environment generation and remote stepping.
diff --git a/sweep_300_700.log b/sweep_300_700.log
index 4276ca6..3675dd6 100644
--- a/sweep_300_700.log
+++ b/sweep_300_700.log
@@ -289,3 +289,24 @@
  289    289  586 OK 54
  290    290  588 OK 44
  291    291  589 OK 31
         292 +591 OK 24
         293 +590 OK 86
         294 +592 OK 27
         295 +593 OK 62
         296 +594 OK 74
         297 +596 OK 62
         298 +595 OK 120
         299 +598 OK 52
         300 +597 OK 83
         301 +599 OK 53
         302 +600 OK 50
         303 +601 OK 30
         304 +602 OK 21
         305 +603 OK 20
         306 +604 OK 18
         307 +605 OK 26
         308 +607 OK 58
         309 +608 OK 34
         310 +606 OK 93
         311 +609 OK 62
         312 +610 OK 35
diff --git a/test_regression.py b/test_regression.py
new file mode 100644
index 0000000..579f864
--- /dev/null
+++ b/test_regression.py
@@ -0,0 +1,24 @@
           1 +"""Reproduce the edge cases discovered during black-box exploration."""
           2 +import hashlib
           3 +import json
           4 +import time
           5 +from env_client import make_env
           6 +from approach import GeneratedApproach
           7 +
           8 +cases=[(21,None),(31,None),(74,None),(151,None),(489,None),(42,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4)]
           9 +policy_hash=hashlib.sha256(open('approach.py','rb').read()).hexdigest()
          10 +results=[]
          11 +e=make_env()
          12 +for seed,count in cases:
          13 +    s,info=e.reset(seed=seed,options={'object_count':count} if count is not None else None)
          14 +    policy=GeneratedApproach(e.action_space,e.observation_space,{})
          15 +    tick=time.perf_counter();policy.reset(s,info);cpu=time.perf_counter()-tick
          16 +    for step in range(e.max_steps):
          17 +        tick=time.perf_counter();action=policy.get_action(s);cpu+=time.perf_counter()-tick
          18 +        s,reward,done,truncated,info=e.step(action)
          19 +        if done or truncated:break
          20 +    result=dict(seed=seed,count=count,done=done,steps=step+1,policy_seconds=cpu,policy_hash=policy_hash)
          21 +    results.append(result);print(result,flush=True)
          22 +    json.dump(results,open('regression_results.json','w'),indent=2)
          23 +e.close()
          24 +assert all(r['done'] for r in results)
````

</details>

<a id="C035"></a>
### C035 · Record passing regression suite and add the second storage-order regression

Commit `9bc34ce52df20f8c43a7c1166f48a7091648749f`; parents: 01878e6afd3a5760a3e58f05bcbca5df9bce98f3. Recorded author date: 2026-09-21T22:57:58+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0155](01_timeline.md#E0155): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C035_9bc34ce.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/regression_results.json b/regression_results.json
new file mode 100644
index 0000000..e14a8e6
--- /dev/null
+++ b/regression_results.json
@@ -0,0 +1,98 @@
           1 +[
           2 +  {
           3 +    "seed": 21,
           4 +    "count": null,
           5 +    "done": true,
           6 +    "steps": 50,
           7 +    "policy_seconds": 0.009710075333714485,
           8 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
           9 +  },
          10 +  {
          11 +    "seed": 31,
          12 +    "count": null,
          13 +    "done": true,
          14 +    "steps": 79,
          15 +    "policy_seconds": 0.0202472060918808,
          16 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          17 +  },
          18 +  {
          19 +    "seed": 74,
          20 +    "count": null,
          21 +    "done": true,
          22 +    "steps": 25,
          23 +    "policy_seconds": 0.006569691002368927,
          24 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          25 +  },
          26 +  {
          27 +    "seed": 151,
          28 +    "count": null,
          29 +    "done": true,
          30 +    "steps": 71,
          31 +    "policy_seconds": 0.014874584041535854,
          32 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          33 +  },
          34 +  {
          35 +    "seed": 489,
          36 +    "count": null,
          37 +    "done": true,
          38 +    "steps": 111,
          39 +    "policy_seconds": 0.02264695893973112,
          40 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          41 +  },
          42 +  {
          43 +    "seed": 42,
          44 +    "count": 3,
          45 +    "done": true,
          46 +    "steps": 93,
          47 +    "policy_seconds": 0.029996491968631744,
          48 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          49 +  },
          50 +  {
          51 +    "seed": 0,
          52 +    "count": 4,
          53 +    "done": true,
          54 +    "steps": 95,
          55 +    "policy_seconds": 0.036820714361965656,
          56 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          57 +  },
          58 +  {
          59 +    "seed": 1,
          60 +    "count": 4,
          61 +    "done": true,
          62 +    "steps": 79,
          63 +    "policy_seconds": 0.028981699608266354,
          64 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          65 +  },
          66 +  {
          67 +    "seed": 2,
          68 +    "count": 4,
          69 +    "done": true,
          70 +    "steps": 137,
          71 +    "policy_seconds": 0.03913711290806532,
          72 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          73 +  },
          74 +  {
          75 +    "seed": 3,
          76 +    "count": 4,
          77 +    "done": true,
          78 +    "steps": 101,
          79 +    "policy_seconds": 0.03482349868863821,
          80 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          81 +  },
          82 +  {
          83 +    "seed": 4,
          84 +    "count": 4,
          85 +    "done": true,
          86 +    "steps": 165,
          87 +    "policy_seconds": 0.050516946241259575,
          88 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          89 +  },
          90 +  {
          91 +    "seed": 5,
          92 +    "count": 4,
          93 +    "done": true,
          94 +    "steps": 83,
          95 +    "policy_seconds": 0.022572549059987068,
          96 +    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          97 +  }
          98 +]
\ No newline at end of file
diff --git a/regression_run.log b/regression_run.log
new file mode 100644
index 0000000..b7a6917
--- /dev/null
+++ b/regression_run.log
@@ -0,0 +1,12 @@
           1 +{'seed': 21, 'count': None, 'done': True, 'steps': 50, 'policy_seconds': 0.009710075333714485, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
           2 +{'seed': 31, 'count': None, 'done': True, 'steps': 79, 'policy_seconds': 0.0202472060918808, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
           3 +{'seed': 74, 'count': None, 'done': True, 'steps': 25, 'policy_seconds': 0.006569691002368927, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
           4 +{'seed': 151, 'count': None, 'done': True, 'steps': 71, 'policy_seconds': 0.014874584041535854, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
           5 +{'seed': 489, 'count': None, 'done': True, 'steps': 111, 'policy_seconds': 0.02264695893973112, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
           6 +{'seed': 42, 'count': 3, 'done': True, 'steps': 93, 'policy_seconds': 0.029996491968631744, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
           7 +{'seed': 0, 'count': 4, 'done': True, 'steps': 95, 'policy_seconds': 0.036820714361965656, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
           8 +{'seed': 1, 'count': 4, 'done': True, 'steps': 79, 'policy_seconds': 0.028981699608266354, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
           9 +{'seed': 2, 'count': 4, 'done': True, 'steps': 137, 'policy_seconds': 0.03913711290806532, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
          10 +{'seed': 3, 'count': 4, 'done': True, 'steps': 101, 'policy_seconds': 0.03482349868863821, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
          11 +{'seed': 4, 'count': 4, 'done': True, 'steps': 165, 'policy_seconds': 0.050516946241259575, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
          12 +{'seed': 5, 'count': 4, 'done': True, 'steps': 83, 'policy_seconds': 0.022572549059987068, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
diff --git a/test_regression.py b/test_regression.py
index 579f864..50df6df 100644
--- a/test_regression.py
+++ b/test_regression.py
@@ -5,7 +5,7 @@ import time
    5      5  from env_client import make_env
    6      6  from approach import GeneratedApproach
    7      7  
    8        -cases=[(21,None),(31,None),(74,None),(151,None),(489,None),(42,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4)]
           8 +cases=[(21,None),(31,None),(74,None),(151,None),(489,None),(627,None),(42,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4)]
    9      9  policy_hash=hashlib.sha256(open('approach.py','rb').read()).hexdigest()
   10     10  results=[]
   11     11  e=make_env()
```

</details>

<a id="C036"></a>
### C036 · Save successful unseen-seed and variable-count validation results

Commit `c31a79bc47df67c90635a7deb725ead6a146e618`; parents: 9bc34ce52df20f8c43a7c1166f48a7091648749f. Recorded author date: 2026-09-21T23:02:36+02:00.

File roles (automatic): setup/other.

- [E0173](01_timeline.md#E0173): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C036_c31a79b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/final_fresh_sweep.log b/final_fresh_sweep.log
new file mode 100644
index 0000000..2a792ae
--- /dev/null
+++ b/final_fresh_sweep.log
@@ -0,0 +1,101 @@
           1 +2000 OK 17
           2 +2001 OK 20
           3 +2003 OK 96
           4 +2002 OK 136
           5 +2005 OK 42
           6 +2004 OK 97
           7 +2006 OK 38
           8 +2007 OK 61
           9 +2009 OK 86
          10 +2008 OK 100
          11 +2010 OK 93
          12 +2011 OK 94
          13 +2012 OK 81
          14 +2014 OK 55
          15 +2013 OK 100
          16 +2016 OK 25
          17 +2015 OK 58
          18 +2018 OK 28
          19 +2017 OK 75
          20 +2019 OK 41
          21 +2020 OK 18
          22 +2021 OK 82
          23 +2023 OK 70
          24 +2024 OK 27
          25 +2022 OK 99
          26 +2025 OK 21
          27 +2027 OK 26
          28 +2028 OK 37
          29 +2029 OK 20
          30 +2026 OK 79
          31 +2030 OK 25
          32 +2031 OK 31
          33 +2032 OK 90
          34 +2033 OK 64
          35 +2035 OK 20
          36 +2034 OK 51
          37 +2036 OK 31
          38 +2038 OK 64
          39 +2037 OK 80
          40 +2040 OK 74
          41 +2039 OK 144
          42 +2041 OK 57
          43 +2042 OK 93
          44 +2044 OK 24
          45 +2045 OK 21
          46 +2043 OK 75
          47 +2046 OK 32
          48 +2047 OK 24
          49 +2049 OK 20
          50 +2048 OK 69
          51 +2052 OK 23
          52 +2051 OK 34
          53 +2050 OK 81
          54 +2053 OK 19
          55 +2055 OK 21
          56 +2056 OK 48
          57 +2057 OK 37
          58 +2054 OK 106
          59 +2058 OK 67
          60 +2060 OK 36
          61 +2059 OK 86
          62 +2061 OK 34
          63 +2063 OK 27
          64 +2062 OK 77
          65 +2065 OK 21
          66 +2064 OK 66
          67 +2067 OK 24
          68 +2066 OK 84
          69 +2068 OK 49
          70 +2069 OK 77
          71 +2071 OK 31
          72 +2070 OK 68
          73 +2072 OK 45
          74 +2073 OK 48
          75 +2074 OK 25
          76 +2075 OK 26
          77 +2076 OK 51
          78 +2079 OK 18
          79 +2078 OK 42
          80 +2077 OK 68
          81 +2080 OK 31
          82 +2081 OK 19
          83 +2082 OK 19
          84 +2083 OK 32
          85 +2084 OK 77
          86 +2085 OK 83
          87 +2086 OK 95
          88 +2087 OK 100
          89 +2088 OK 29
          90 +2090 OK 22
          91 +2089 OK 72
          92 +2091 OK 28
          93 +2093 OK 36
          94 +2095 OK 15
          95 +2092 OK 88
          96 +2094 OK 99
          97 +2097 OK 20
          98 +2098 OK 23
          99 +2096 OK 114
         100 +2099 OK 75
         101 +SUMMARY 100 success 100 mean_steps 54.27 max_time 17.259
diff --git a/results_0_100_3.json b/results_0_100_3.json
new file mode 100644
index 0000000..76b5173
--- /dev/null
+++ b/results_0_100_3.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "count": 3, "done": true, "steps": 23, "seconds": 3.549, "policy_seconds": 0.0049}, {"seed": 1, "count": 3, "done": true, "steps": 116, "seconds": 15.24, "policy_seconds": 0.0342}, {"seed": 2, "count": 3, "done": true, "steps": 113, "seconds": 15.809, "policy_seconds": 0.0292}, {"seed": 3, "count": 3, "done": true, "steps": 73, "seconds": 10.165, "policy_seconds": 0.0195}, {"seed": 4, "count": 3, "done": true, "steps": 59, "seconds": 8.185, "policy_seconds": 0.0161}, {"seed": 5, "count": 3, "done": true, "steps": 22, "seconds": 1.897, "policy_seconds": 0.0092}, {"seed": 6, "count": 3, "done": true, "steps": 75, "seconds": 9.292, "policy_seconds": 0.0253}, {"seed": 7, "count": 3, "done": true, "steps": 96, "seconds": 11.631, "policy_seconds": 0.0282}, {"seed": 8, "count": 3, "done": true, "steps": 97, "seconds": 12.003, "policy_seconds": 0.0257}, {"seed": 9, "count": 3, "done": true, "steps": 99, "seconds": 12.419, "policy_seconds": 0.0296}, {"seed": 10, "count": 3, "done": true, "steps": 93, "seconds": 11.969, "policy_seconds": 0.0304}, {"seed": 11, "count": 3, "done": true, "steps": 53, "seconds": 7.056, "policy_seconds": 0.0154}, {"seed": 12, "count": 3, "done": true, "steps": 93, "seconds": 12.65, "policy_seconds": 0.0279}, {"seed": 13, "count": 3, "done": true, "steps": 48, "seconds": 7.445, "policy_seconds": 0.0197}, {"seed": 14, "count": 3, "done": true, "steps": 84, "seconds": 12.909, "policy_seconds": 0.0331}, {"seed": 15, "count": 3, "done": true, "steps": 100, "seconds": 14.981, "policy_seconds": 0.0258}, {"seed": 16, "count": 3, "done": true, "steps": 64, "seconds": 10.169, "policy_seconds": 0.0151}, {"seed": 17, "count": 3, "done": true, "steps": 106, "seconds": 13.563, "policy_seconds": 0.0269}, {"seed": 18, "count": 3, "done": true, "steps": 69, "seconds": 7.768, "policy_seconds": 0.0132}, {"seed": 19, "count": 3, "done": true, "steps": 85, "seconds": 9.92, "policy_seconds": 0.0218}, {"seed": 20, "count": 3, "done": true, "steps": 93, "seconds": 10.545, "policy_seconds": 0.0299}, {"seed": 21, "count": 3, "done": true, "steps": 71, "seconds": 8.221, "policy_seconds": 0.015}, {"seed": 22, "count": 3, "done": true, "steps": 76, "seconds": 9.996, "policy_seconds": 0.0207}, {"seed": 23, "count": 3, "done": true, "steps": 57, "seconds": 7.459, "policy_seconds": 0.0157}, {"seed": 24, "count": 3, "done": true, "steps": 80, "seconds": 11.789, "policy_seconds": 0.0217}, {"seed": 25, "count": 3, "done": true, "steps": 106, "seconds": 14.459, "policy_seconds": 0.0359}, {"seed": 26, "count": 3, "done": true, "steps": 75, "seconds": 10.232, "policy_seconds": 0.0238}, {"seed": 27, "count": 3, "done": true, "steps": 66, "seconds": 8.94, "policy_seconds": 0.0184}, {"seed": 28, "count": 3, "done": true, "steps": 92, "seconds": 11.795, "policy_seconds": 0.0337}, {"seed": 29, "count": 3, "done": true, "steps": 92, "seconds": 11.433, "policy_seconds": 0.025}, {"seed": 30, "count": 3, "done": true, "steps": 36, "seconds": 4.563, "policy_seconds": 0.0061}, {"seed": 31, "count": 3, "done": true, "steps": 84, "seconds": 10.914, "policy_seconds": 0.0226}, {"seed": 32, "count": 3, "done": true, "steps": 110, "seconds": 15.044, "policy_seconds": 0.0345}, {"seed": 33, "count": 3, "done": true, "steps": 51, "seconds": 7.012, "policy_seconds": 0.0145}, {"seed": 34, "count": 3, "done": true, "steps": 82, "seconds": 10.991, "policy_seconds": 0.0227}, {"seed": 35, "count": 3, "done": true, "steps": 125, "seconds": 19.161, "policy_seconds": 0.0372}, {"seed": 36, "count": 3, "done": true, "steps": 137, "seconds": 18.8, "policy_seconds": 0.0343}, {"seed": 37, "count": 3, "done": true, "steps": 71, "seconds": 8.883, "policy_seconds": 0.0158}, {"seed": 38, "count": 3, "done": true, "steps": 82, "seconds": 10.469, "policy_seconds": 0.0229}, {"seed": 39, "count": 3, "done": true, "steps": 130, "seconds": 16.159, "policy_seconds": 0.0424}, {"seed": 40, "count": 3, "done": true, "steps": 64, "seconds": 8.049, "policy_seconds": 0.0222}, {"seed": 41, "count": 3, "done": true, "steps": 44, "seconds": 5.19, "policy_seconds": 0.0112}, {"seed": 42, "count": 3, "done": true, "steps": 93, "seconds": 11.497, "policy_seconds": 0.0295}, {"seed": 43, "count": 3, "done": true, "steps": 84, "seconds": 10.718, "policy_seconds": 0.0263}, {"seed": 44, "count": 3, "done": true, "steps": 79, "seconds": 8.97, "policy_seconds": 0.0226}, {"seed": 45, "count": 3, "done": true, "steps": 87, "seconds": 11.482, "policy_seconds": 0.0268}, {"seed": 46, "count": 3, "done": true, "steps": 123, "seconds": 14.467, "policy_seconds": 0.0371}, {"seed": 47, "count": 3, "done": true, "steps": 110, "seconds": 12.844, "policy_seconds": 0.0302}, {"seed": 48, "count": 3, "done": true, "steps": 57, "seconds": 6.935, "policy_seconds": 0.0116}, {"seed": 49, "count": 3, "done": true, "steps": 100, "seconds": 13.692, "policy_seconds": 0.0302}, {"seed": 50, "count": 3, "done": true, "steps": 87, "seconds": 14.281, "policy_seconds": 0.0237}, {"seed": 51, "count": 3, "done": true, "steps": 96, "seconds": 15.99, "policy_seconds": 0.0241}, {"seed": 52, "count": 3, "done": true, "steps": 98, "seconds": 16.732, "policy_seconds": 0.0334}, {"seed": 53, "count": 3, "done": true, "steps": 69, "seconds": 11.033, "policy_seconds": 0.0194}, {"seed": 54, "count": 3, "done": true, "steps": 95, "seconds": 14.85, "policy_seconds": 0.0349}, {"seed": 55, "count": 3, "done": true, "steps": 101, "seconds": 16.786, "policy_seconds": 0.0324}, {"seed": 56, "count": 3, "done": true, "steps": 99, "seconds": 16.174, "policy_seconds": 0.0336}, {"seed": 57, "count": 3, "done": true, "steps": 100, "seconds": 14.951, "policy_seconds": 0.0312}, {"seed": 58, "count": 3, "done": true, "steps": 91, "seconds": 13.007, "policy_seconds": 0.0353}, {"seed": 59, "count": 3, "done": true, "steps": 54, "seconds": 6.538, "policy_seconds": 0.0196}, {"seed": 60, "count": 3, "done": true, "steps": 86, "seconds": 10.135, "policy_seconds": 0.024}, {"seed": 61, "count": 3, "done": true, "steps": 110, "seconds": 14.078, "policy_seconds": 0.0248}, {"seed": 62, "count": 3, "done": true, "steps": 92, "seconds": 13.603, "policy_seconds": 0.0282}, {"seed": 63, "count": 3, "done": true, "steps": 86, "seconds": 12.441, "policy_seconds": 0.0236}, {"seed": 64, "count": 3, "done": true, "steps": 112, "seconds": 13.63, "policy_seconds": 0.0324}, {"seed": 65, "count": 3, "done": true, "steps": 28, "seconds": 3.129, "policy_seconds": 0.0066}, {"seed": 66, "count": 3, "done": true, "steps": 125, "seconds": 15.786, "policy_seconds": 0.0331}, {"seed": 67, "count": 3, "done": true, "steps": 110, "seconds": 16.433, "policy_seconds": 0.0362}, {"seed": 68, "count": 3, "done": true, "steps": 105, "seconds": 15.688, "policy_seconds": 0.0377}, {"seed": 69, "count": 3, "done": true, "steps": 103, "seconds": 13.839, "policy_seconds": 0.0333}, {"seed": 70, "count": 3, "done": true, "steps": 77, "seconds": 9.199, "policy_seconds": 0.0228}, {"seed": 71, "count": 3, "done": true, "steps": 69, "seconds": 6.953, "policy_seconds": 0.0177}, {"seed": 72, "count": 3, "done": true, "steps": 29, "seconds": 2.894, "policy_seconds": 0.0091}, {"seed": 73, "count": 3, "done": true, "steps": 65, "seconds": 7.21, "policy_seconds": 0.018}, {"seed": 74, "count": 3, "done": true, "steps": 71, "seconds": 8.201, "policy_seconds": 0.027}, {"seed": 75, "count": 3, "done": true, "steps": 64, "seconds": 7.464, "policy_seconds": 0.017}, {"seed": 76, "count": 3, "done": true, "steps": 76, "seconds": 8.564, "policy_seconds": 0.0188}, {"seed": 77, "count": 3, "done": true, "steps": 53, "seconds": 6.117, "policy_seconds": 0.0206}, {"seed": 78, "count": 3, "done": true, "steps": 56, "seconds": 6.683, "policy_seconds": 0.0192}, {"seed": 79, "count": 3, "done": true, "steps": 54, "seconds": 6.14, "policy_seconds": 0.0106}, {"seed": 80, "count": 3, "done": true, "steps": 82, "seconds": 8.571, "policy_seconds": 0.0168}, {"seed": 81, "count": 3, "done": true, "steps": 75, "seconds": 8.119, "policy_seconds": 0.0226}, {"seed": 82, "count": 3, "done": true, "steps": 57, "seconds": 5.197, "policy_seconds": 0.0157}, {"seed": 83, "count": 3, "done": true, "steps": 88, "seconds": 11.372, "policy_seconds": 0.0279}, {"seed": 84, "count": 3, "done": true, "steps": 34, "seconds": 3.267, "policy_seconds": 0.0059}, {"seed": 85, "count": 3, "done": true, "steps": 91, "seconds": 11.679, "policy_seconds": 0.029}, {"seed": 86, "count": 3, "done": true, "steps": 87, "seconds": 9.644, "policy_seconds": 0.0289}, {"seed": 87, "count": 3, "done": true, "steps": 104, "seconds": 11.171, "policy_seconds": 0.022}, {"seed": 88, "count": 3, "done": true, "steps": 97, "seconds": 10.58, "policy_seconds": 0.0235}, {"seed": 89, "count": 3, "done": true, "steps": 58, "seconds": 6.667, "policy_seconds": 0.0166}, {"seed": 90, "count": 3, "done": true, "steps": 104, "seconds": 10.939, "policy_seconds": 0.0281}, {"seed": 91, "count": 3, "done": true, "steps": 46, "seconds": 4.941, "policy_seconds": 0.0187}, {"seed": 92, "count": 3, "done": true, "steps": 20, "seconds": 2.69, "policy_seconds": 0.0071}, {"seed": 93, "count": 3, "done": true, "steps": 99, "seconds": 11.214, "policy_seconds": 0.0307}, {"seed": 94, "count": 3, "done": true, "steps": 103, "seconds": 11.586, "policy_seconds": 0.0308}, {"seed": 95, "count": 3, "done": true, "steps": 58, "seconds": 6.836, "policy_seconds": 0.015}, {"seed": 96, "count": 3, "done": true, "steps": 148, "seconds": 15.099, "policy_seconds": 0.0348}, {"seed": 97, "count": 3, "done": true, "steps": 87, "seconds": 9.135, "policy_seconds": 0.0226}, {"seed": 98, "count": 3, "done": true, "steps": 77, "seconds": 9.963, "policy_seconds": 0.021}, {"seed": 99, "count": 3, "done": true, "steps": 49, "seconds": 5.204, "policy_seconds": 0.0182}]
\ No newline at end of file
diff --git a/results_0_100_None.json b/results_0_100_None.json
index 7afc334..3dd3754 100644
--- a/results_0_100_None.json
+++ b/results_0_100_None.json
@@ -1 +1 @@
    1        -[{"seed": 0, "count": null, "done": true, "steps": 79, "seconds": 3.837, "policy_seconds": 0.0253}, {"seed": 1, "count": null, "done": true, "steps": 60, "seconds": 2.363, "policy_seconds": 0.0176}, {"seed": 2, "count": null, "done": true, "steps": 55, "seconds": 2.975, "policy_seconds": 0.0166}, {"seed": 3, "count": null, "done": true, "steps": 53, "seconds": 2.948, "policy_seconds": 0.0172}, {"seed": 4, "count": null, "done": true, "steps": 57, "seconds": 2.329, "policy_seconds": 0.0085}, {"seed": 5, "count": null, "done": true, "steps": 93, "seconds": 3.944, "policy_seconds": 0.0223}, {"seed": 6, "count": null, "done": true, "steps": 66, "seconds": 2.525, "policy_seconds": 0.0147}, {"seed": 7, "count": null, "done": true, "steps": 149, "seconds": 7.675, "policy_seconds": 0.0357}, {"seed": 8, "count": null, "done": true, "steps": 91, "seconds": 4.355, "policy_seconds": 0.0266}, {"seed": 9, "count": null, "done": true, "steps": 83, "seconds": 3.635, "policy_seconds": 0.022}, {"seed": 10, "count": null, "done": true, "steps": 36, "seconds": 1.468, "policy_seconds": 0.0082}, {"seed": 11, "count": null, "done": true, "steps": 41, "seconds": 1.908, "policy_seconds": 0.0071}, {"seed": 12, "count": null, "done": true, "steps": 78, "seconds": 4.341, "policy_seconds": 0.0183}, {"seed": 13, "count": null, "done": true, "steps": 57, "seconds": 3.068, "policy_seconds": 0.0176}, {"seed": 14, "count": null, "done": true, "steps": 27, "seconds": 0.935, "policy_seconds": 0.0054}, {"seed": 15, "count": null, "done": true, "steps": 22, "seconds": 1.359, "policy_seconds": 0.0074}, {"seed": 16, "count": null, "done": true, "steps": 25, "seconds": 1.509, "policy_seconds": 0.0051}, {"seed": 17, "count": null, "done": true, "steps": 70, "seconds": 3.233, "policy_seconds": 0.016}, {"seed": 18, "count": null, "done": true, "steps": 51, "seconds": 2.066, "policy_seconds": 0.0199}, {"seed": 19, "count": null, "done": true, "steps": 49, "seconds": 1.933, "policy_seconds": 0.0159}, {"seed": 20, "count": null, "done": true, "steps": 65, "seconds": 3.419, "policy_seconds": 0.0294}, {"seed": 21, "count": null, "done": true, "steps": 50, "seconds": 2.287, "policy_seconds": 0.0112}, {"seed": 22, "count": null, "done": true, "steps": 89, "seconds": 5.101, "policy_seconds": 0.0276}, {"seed": 23, "count": null, "done": true, "steps": 40, "seconds": 1.426, "policy_seconds": 0.0089}, {"seed": 24, "count": null, "done": true, "steps": 50, "seconds": 1.514, "policy_seconds": 0.0098}, {"seed": 25, "count": null, "done": true, "steps": 49, "seconds": 2.09, "policy_seconds": 0.0123}, {"seed": 26, "count": null, "done": true, "steps": 50, "seconds": 2.809, "policy_seconds": 0.0116}, {"seed": 27, "count": null, "done": true, "steps": 18, "seconds": 0.982, "policy_seconds": 0.003}, {"seed": 28, "count": null, "done": true, "steps": 47, "seconds": 2.306, "policy_seconds": 0.009}, {"seed": 29, "count": null, "done": true, "steps": 42, "seconds": 2.845, "policy_seconds": 0.0102}, {"seed": 30, "count": null, "done": true, "steps": 23, "seconds": 1.174, "policy_seconds": 0.0027}, {"seed": 31, "count": null, "done": true, "steps": 34, "seconds": 1.896, "policy_seconds": 0.0082}, {"seed": 32, "count": null, "done": true, "steps": 87, "seconds": 5.267, "policy_seconds": 0.0264}, {"seed": 33, "count": null, "done": true, "steps": 59, "seconds": 3.303, "policy_seconds": 0.0178}, {"seed": 34, "count": null, "done": true, "steps": 35, "seconds": 1.231, "policy_seconds": 0.0084}, {"seed": 35, "count": null, "done": true, "steps": 33, "seconds": 1.037, "policy_seconds": 0.0082}, {"seed": 36, "count": null, "done": true, "steps": 55, "seconds": 2.646, "policy_seconds": 0.0145}, {"seed": 37, "count": null, "done": true, "steps": 29, "seconds": 1.298, "policy_seconds": 0.0051}, {"seed": 38, "count": null, "done": true, "steps": 21, "seconds": 0.838, "policy_seconds": 0.0051}, {"seed": 39, "count": null, "done": true, "steps": 63, "seconds": 3.764, "policy_seconds": 0.019}, {"seed": 40, "count": null, "done": true, "steps": 80, "seconds": 4.572, "policy_seconds": 0.0198}, {"seed": 41, "count": null, "done": true, "steps": 30, "seconds": 1.592, "policy_seconds": 0.0068}, {"seed": 42, "count": null, "done": true, "steps": 32, "seconds": 1.681, "policy_seconds": 0.0084}, {"seed": 43, "count": null, "done": true, "steps": 26, "seconds": 1.433, "policy_seconds": 0.006}, {"seed": 44, "count": null, "done": true, "steps": 64, "seconds": 3.881, "policy_seconds": 0.0137}, {"seed": 45, "count": null, "done": true, "steps": 49, "seconds": 2.375, "policy_seconds": 0.0155}, {"seed": 46, "count": null, "done": true, "steps": 36, "seconds": 1.563, "policy_seconds": 0.0059}, {"seed": 47, "count": null, "done": true, "steps": 41, "seconds": 1.738, "policy_seconds": 0.0062}, {"seed": 48, "count": null, "done": true, "steps": 22, "seconds": 1.104, "policy_seconds": 0.0064}, {"seed": 49, "count": null, "done": true, "steps": 24, "seconds": 1.069, "policy_seconds": 0.0049}, {"seed": 50, "count": null, "done": true, "steps": 63, "seconds": 3.597, "policy_seconds": 0.0253}, {"seed": 51, "count": null, "done": true, "steps": 35, "seconds": 1.575, "policy_seconds": 0.0094}, {"seed": 52, "count": null, "done": true, "steps": 78, "seconds": 4.024, "policy_seconds": 0.0227}, {"seed": 53, "count": null, "done": true, "steps": 78, "seconds": 3.595, "policy_seconds": 0.0264}, {"seed": 54, "count": null, "done": true, "steps": 28, "seconds": 1.064, "policy_seconds": 0.0074}, {"seed": 55, "count": null, "done": true, "steps": 22, "seconds": 0.983, "policy_seconds": 0.0052}, {"seed": 56, "count": null, "done": true, "steps": 62, "seconds": 3.43, "policy_seconds": 0.0149}, {"seed": 57, "count": null, "done": true, "steps": 20, "seconds": 0.833, "policy_seconds": 0.0059}, {"seed": 58, "count": null, "done": true, "steps": 47, "seconds": 2.718, "policy_seconds": 0.0186}, {"seed": 59, "count": null, "done": true, "steps": 62, "seconds": 4.177, "policy_seconds": 0.0233}, {"seed": 60, "count": null, "done": true, "steps": 23, "seconds": 1.052, "policy_seconds": 0.0062}, {"seed": 61, "count": null, "done": true, "steps": 70, "seconds": 3.406, "policy_seconds": 0.0159}, {"seed": 62, "count": null, "done": true, "steps": 73, "seconds": 3.674, "policy_seconds": 0.0166}, {"seed": 63, "count": null, "done": true, "steps": 37, "seconds": 1.481, "policy_seconds": 0.0136}, {"seed": 64, "count": null, "done": true, "steps": 29, "seconds": 0.976, "policy_seconds": 0.0075}, {"seed": 65, "count": null, "done": true, "steps": 17, "seconds": 0.675, "policy_seconds": 0.0047}, {"seed": 66, "count": null, "done": true, "steps": 55, "seconds": 2.588, "policy_seconds": 0.021}, {"seed": 67, "count": null, "done": true, "steps": 54, "seconds": 2.724, "policy_seconds": 0.0106}, {"seed": 68, "count": null, "done": true, "steps": 47, "seconds": 1.8, "policy_seconds": 0.0163}, {"seed": 69, "count": null, "done": true, "steps": 36, "seconds": 1.157, "policy_seconds": 0.0057}, {"seed": 70, "count": null, "done": true, "steps": 81, "seconds": 3.848, "policy_seconds": 0.0177}, {"seed": 71, "count": null, "done": true, "steps": 42, "seconds": 2.269, "policy_seconds": 0.0097}, {"seed": 72, "count": null, "done": true, "steps": 96, "seconds": 5.037, "policy_seconds": 0.0217}, {"seed": 73, "count": null, "done": true, "steps": 73, "seconds": 3.902, "policy_seconds": 0.0198}, {"seed": 74, "count": null, "done": true, "steps": 25, "seconds": 1.168, "policy_seconds": 0.0053}, {"seed": 75, "count": null, "done": true, "steps": 71, "seconds": 3.465, "policy_seconds": 0.0203}, {"seed": 76, "count": null, "done": true, "steps": 31, "seconds": 1.412, "policy_seconds": 0.0072}, {"seed": 77, "count": null, "done": true, "steps": 19, "seconds": 0.441, "policy_seconds": 0.0052}, {"seed": 78, "count": null, "done": true, "steps": 114, "seconds": 7.469, "policy_seconds": 0.0327}, {"seed": 79, "count": null, "done": true, "steps": 34, "seconds": 1.244, "policy_seconds": 0.0074}, {"seed": 80, "count": null, "done": true, "steps": 63, "seconds": 4.07, "policy_seconds": 0.0193}, {"seed": 81, "count": null, "done": true, "steps": 22, "seconds": 0.954, "policy_seconds": 0.0058}, {"seed": 82, "count": null, "done": true, "steps": 35, "seconds": 2.503, "policy_seconds": 0.007}, {"seed": 83, "count": null, "done": true, "steps": 47, "seconds": 2.929, "policy_seconds": 0.0154}, {"seed": 84, "count": null, "done": true, "steps": 81, "seconds": 3.986, "policy_seconds": 0.0187}, {"seed": 85, "count": null, "done": true, "steps": 53, "seconds": 2.803, "policy_seconds": 0.0133}, {"seed": 86, "count": null, "done": true, "steps": 44, "seconds": 2.738, "policy_seconds": 0.0167}, {"seed": 87, "count": null, "done": true, "steps": 56, "seconds": 2.551, "policy_seconds": 0.0139}, {"seed": 88, "count": null, "done": true, "steps": 65, "seconds": 3.071, "policy_seconds": 0.0167}, {"seed": 89, "count": null, "done": true, "steps": 56, "seconds": 2.541, "policy_seconds": 0.0217}, {"seed": 90, "count": null, "done": true, "steps": 64, "seconds": 2.992, "policy_seconds": 0.0151}, {"seed": 91, "count": null, "done": true, "steps": 45, "seconds": 2.58, "policy_seconds": 0.0222}, {"seed": 92, "count": null, "done": true, "steps": 44, "seconds": 2.584, "policy_seconds": 0.0114}, {"seed": 93, "count": null, "done": true, "steps": 46, "seconds": 2.975, "policy_seconds": 0.0163}, {"seed": 94, "count": null, "done": true, "steps": 25, "seconds": 0.831, "policy_seconds": 0.0059}, {"seed": 95, "count": null, "done": true, "steps": 64, "seconds": 3.635, "policy_seconds": 0.018}, {"seed": 96, "count": null, "done": true, "steps": 30, "seconds": 1.901, "policy_seconds": 0.0126}, {"seed": 97, "count": null, "done": true, "steps": 33, "seconds": 1.456, "policy_seconds": 0.0071}, {"seed": 98, "count": null, "done": true, "steps": 53, "seconds": 2.399, "policy_seconds": 0.0158}, {"seed": 99, "count": null, "done": true, "steps": 44, "seconds": 1.622, "policy_seconds": 0.0105}]
\ No newline at end of file
           1 +[{"seed": 0, "count": null, "done": true, "steps": 106, "seconds": 11.859, "policy_seconds": 0.0238}, {"seed": 1, "count": null, "done": true, "steps": 60, "seconds": 5.546, "policy_seconds": 0.016}, {"seed": 2, "count": null, "done": true, "steps": 71, "seconds": 7.387, "policy_seconds": 0.0184}, {"seed": 3, "count": null, "done": true, "steps": 81, "seconds": 9.158, "policy_seconds": 0.02}, {"seed": 4, "count": null, "done": true, "steps": 57, "seconds": 5.715, "policy_seconds": 0.008}, {"seed": 5, "count": null, "done": true, "steps": 162, "seconds": 17.024, "policy_seconds": 0.0389}, {"seed": 6, "count": null, "done": true, "steps": 66, "seconds": 5.059, "policy_seconds": 0.0142}, {"seed": 7, "count": null, "done": true, "steps": 111, "seconds": 11.776, "policy_seconds": 0.0313}, {"seed": 8, "count": null, "done": true, "steps": 123, "seconds": 12.99, "policy_seconds": 0.0307}, {"seed": 9, "count": null, "done": true, "steps": 100, "seconds": 8.945, "policy_seconds": 0.0265}, {"seed": 10, "count": null, "done": true, "steps": 61, "seconds": 6.47, "policy_seconds": 0.0204}, {"seed": 11, "count": null, "done": true, "steps": 41, "seconds": 3.061, "policy_seconds": 0.006}, {"seed": 12, "count": null, "done": true, "steps": 91, "seconds": 7.47, "policy_seconds": 0.0207}, {"seed": 13, "count": null, "done": true, "steps": 57, "seconds": 5.903, "policy_seconds": 0.0121}, {"seed": 14, "count": null, "done": true, "steps": 27, "seconds": 2.406, "policy_seconds": 0.0037}, {"seed": 15, "count": null, "done": true, "steps": 22, "seconds": 2.54, "policy_seconds": 0.0066}, {"seed": 16, "count": null, "done": true, "steps": 25, "seconds": 2.621, "policy_seconds": 0.0037}, {"seed": 17, "count": null, "done": true, "steps": 70, "seconds": 7.239, "policy_seconds": 0.0191}, {"seed": 18, "count": null, "done": true, "steps": 51, "seconds": 4.695, "policy_seconds": 0.019}, {"seed": 19, "count": null, "done": true, "steps": 49, "seconds": 4.0, "policy_seconds": 0.0138}, {"seed": 20, "count": null, "done": true, "steps": 65, "seconds": 7.38, "policy_seconds": 0.0137}, {"seed": 21, "count": null, "done": true, "steps": 50, "seconds": 4.391, "policy_seconds": 0.0105}, {"seed": 22, "count": null, "done": true, "steps": 105, "seconds": 10.598, "policy_seconds": 0.0283}, {"seed": 23, "count": null, "done": true, "steps": 40, "seconds": 3.636, "policy_seconds": 0.0081}, {"seed": 24, "count": null, "done": true, "steps": 50, "seconds": 2.843, "policy_seconds": 0.0123}, {"seed": 25, "count": null, "done": true, "steps": 49, "seconds": 3.893, "policy_seconds": 0.0127}, {"seed": 26, "count": null, "done": true, "steps": 60, "seconds": 5.441, "policy_seconds": 0.0163}, {"seed": 27, "count": null, "done": true, "steps": 18, "seconds": 1.29, "policy_seconds": 0.0054}, {"seed": 28, "count": null, "done": true, "steps": 47, "seconds": 3.878, "policy_seconds": 0.0102}, {"seed": 29, "count": null, "done": true, "steps": 76, "seconds": 9.067, "policy_seconds": 0.018}, {"seed": 30, "count": null, "done": true, "steps": 23, "seconds": 1.725, "policy_seconds": 0.0058}, {"seed": 31, "count": null, "done": true, "steps": 79, "seconds": 7.365, "policy_seconds": 0.016}, {"seed": 32, "count": null, "done": true, "steps": 111, "seconds": 12.785, "policy_seconds": 0.0255}, {"seed": 33, "count": null, "done": true, "steps": 59, "seconds": 6.584, "policy_seconds": 0.013}, {"seed": 34, "count": null, "done": true, "steps": 35, "seconds": 2.206, "policy_seconds": 0.0076}, {"seed": 35, "count": null, "done": true, "steps": 33, "seconds": 2.087, "policy_seconds": 0.0073}, {"seed": 36, "count": null, "done": true, "steps": 55, "seconds": 4.647, "policy_seconds": 0.0194}, {"seed": 37, "count": null, "done": true, "steps": 29, "seconds": 2.797, "policy_seconds": 0.0072}, {"seed": 38, "count": null, "done": true, "steps": 21, "seconds": 1.936, "policy_seconds": 0.0057}, {"seed": 39, "count": null, "done": true, "steps": 63, "seconds": 6.2, "policy_seconds": 0.0204}, {"seed": 40, "count": null, "done": true, "steps": 80, "seconds": 6.652, "policy_seconds": 0.0195}, {"seed": 41, "count": null, "done": true, "steps": 30, "seconds": 2.944, "policy_seconds": 0.0059}, {"seed": 42, "count": null, "done": true, "steps": 32, "seconds": 2.296, "policy_seconds": 0.0057}, {"seed": 43, "count": null, "done": true, "steps": 26, "seconds": 2.049, "policy_seconds": 0.0044}, {"seed": 44, "count": null, "done": true, "steps": 79, "seconds": 7.098, "policy_seconds": 0.0203}, {"seed": 45, "count": null, "done": true, "steps": 63, "seconds": 6.345, "policy_seconds": 0.018}, {"seed": 46, "count": null, "done": true, "steps": 36, "seconds": 3.498, "policy_seconds": 0.0049}, {"seed": 47, "count": null, "done": true, "steps": 41, "seconds": 3.752, "policy_seconds": 0.0084}, {"seed": 48, "count": null, "done": true, "steps": 22, "seconds": 1.412, "policy_seconds": 0.0031}, {"seed": 49, "count": null, "done": true, "steps": 24, "seconds": 1.045, "policy_seconds": 0.0055}, {"seed": 50, "count": null, "done": true, "steps": 63, "seconds": 4.977, "policy_seconds": 0.0167}, {"seed": 51, "count": null, "done": true, "steps": 35, "seconds": 3.43, "policy_seconds": 0.0087}, {"seed": 52, "count": null, "done": true, "steps": 82, "seconds": 7.134, "policy_seconds": 0.0181}, {"seed": 53, "count": null, "done": true, "steps": 90, "seconds": 7.464, "policy_seconds": 0.0199}, {"seed": 54, "count": null, "done": true, "steps": 28, "seconds": 1.932, "policy_seconds": 0.0045}, {"seed": 55, "count": null, "done": true, "steps": 22, "seconds": 1.698, "policy_seconds": 0.0063}, {"seed": 56, "count": null, "done": true, "steps": 97, "seconds": 7.751, "policy_seconds": 0.018}, {"seed": 57, "count": null, "done": true, "steps": 20, "seconds": 1.07, "policy_seconds": 0.003}, {"seed": 58, "count": null, "done": true, "steps": 70, "seconds": 6.721, "policy_seconds": 0.0183}, {"seed": 59, "count": null, "done": true, "steps": 77, "seconds": 9.346, "policy_seconds": 0.0197}, {"seed": 60, "count": null, "done": true, "steps": 23, "seconds": 1.768, "policy_seconds": 0.0056}, {"seed": 61, "count": null, "done": true, "steps": 70, "seconds": 6.339, "policy_seconds": 0.0139}, {"seed": 62, "count": null, "done": true, "steps": 73, "seconds": 6.656, "policy_seconds": 0.0196}, {"seed": 63, "count": null, "done": true, "steps": 57, "seconds": 4.61, "policy_seconds": 0.014}, {"seed": 64, "count": null, "done": true, "steps": 29, "seconds": 1.882, "policy_seconds": 0.0042}, {"seed": 65, "count": null, "done": true, "steps": 17, "seconds": 0.738, "policy_seconds": 0.0051}, {"seed": 66, "count": null, "done": true, "steps": 55, "seconds": 4.954, "policy_seconds": 0.0215}, {"seed": 67, "count": null, "done": true, "steps": 54, "seconds": 6.906, "policy_seconds": 0.0119}, {"seed": 68, "count": null, "done": true, "steps": 49, "seconds": 5.077, "policy_seconds": 0.0154}, {"seed": 69, "count": null, "done": true, "steps": 36, "seconds": 2.66, "policy_seconds": 0.0074}, {"seed": 70, "count": null, "done": true, "steps": 81, "seconds": 6.272, "policy_seconds": 0.023}, {"seed": 71, "count": null, "done": true, "steps": 53, "seconds": 5.809, "policy_seconds": 0.0223}, {"seed": 72, "count": null, "done": true, "steps": 96, "seconds": 9.586, "policy_seconds": 0.0174}, {"seed": 73, "count": null, "done": true, "steps": 73, "seconds": 6.439, "policy_seconds": 0.0171}, {"seed": 74, "count": null, "done": true, "steps": 25, "seconds": 1.391, "policy_seconds": 0.0054}, {"seed": 75, "count": null, "done": true, "steps": 107, "seconds": 8.143, "policy_seconds": 0.0261}, {"seed": 76, "count": null, "done": true, "steps": 31, "seconds": 2.75, "policy_seconds": 0.008}, {"seed": 77, "count": null, "done": true, "steps": 19, "seconds": 1.334, "policy_seconds": 0.0058}, {"seed": 78, "count": null, "done": true, "steps": 114, "seconds": 13.754, "policy_seconds": 0.034}, {"seed": 79, "count": null, "done": true, "steps": 34, "seconds": 2.776, "policy_seconds": 0.0067}, {"seed": 80, "count": null, "done": true, "steps": 63, "seconds": 7.9, "policy_seconds": 0.0176}, {"seed": 81, "count": null, "done": true, "steps": 22, "seconds": 1.873, "policy_seconds": 0.0083}, {"seed": 82, "count": null, "done": true, "steps": 35, "seconds": 4.453, "policy_seconds": 0.0086}, {"seed": 83, "count": null, "done": true, "steps": 85, "seconds": 9.869, "policy_seconds": 0.0182}, {"seed": 84, "count": null, "done": true, "steps": 81, "seconds": 7.55, "policy_seconds": 0.0184}, {"seed": 85, "count": null, "done": true, "steps": 53, "seconds": 6.525, "policy_seconds": 0.0165}, {"seed": 86, "count": null, "done": true, "steps": 44, "seconds": 4.631, "policy_seconds": 0.0103}, {"seed": 87, "count": null, "done": true, "steps": 56, "seconds": 4.052, "policy_seconds": 0.0157}, {"seed": 88, "count": null, "done": true, "steps": 65, "seconds": 5.047, "policy_seconds": 0.0142}, {"seed": 89, "count": null, "done": true, "steps": 56, "seconds": 5.637, "policy_seconds": 0.016}, {"seed": 90, "count": null, "done": true, "steps": 98, "seconds": 7.222, "policy_seconds": 0.0192}, {"seed": 91, "count": null, "done": true, "steps": 50, "seconds": 5.402, "policy_seconds": 0.0179}, {"seed": 92, "count": null, "done": true, "steps": 61, "seconds": 4.709, "policy_seconds": 0.0141}, {"seed": 93, "count": null, "done": true, "steps": 63, "seconds": 5.743, "policy_seconds": 0.0197}, {"seed": 94, "count": null, "done": true, "steps": 25, "seconds": 1.392, "policy_seconds": 0.0042}, {"seed": 95, "count": null, "done": true, "steps": 64, "seconds": 5.894, "policy_seconds": 0.017}, {"seed": 96, "count": null, "done": true, "steps": 30, "seconds": 3.473, "policy_seconds": 0.0088}, {"seed": 97, "count": null, "done": true, "steps": 33, "seconds": 2.278, "policy_seconds": 0.0073}, {"seed": 98, "count": null, "done": true, "steps": 79, "seconds": 9.118, "policy_seconds": 0.0172}, {"seed": 99, "count": null, "done": true, "steps": 44, "seconds": 6.285, "policy_seconds": 0.0108}]
\ No newline at end of file
diff --git a/results_2000_100_None.json b/results_2000_100_None.json
new file mode 100644
index 0000000..b3665ed
--- /dev/null
+++ b/results_2000_100_None.json
@@ -0,0 +1 @@
           1 +[{"seed": 2000, "count": null, "done": true, "steps": 17, "seconds": 0.951, "policy_seconds": 0.003}, {"seed": 2001, "count": null, "done": true, "steps": 20, "seconds": 1.407, "policy_seconds": 0.0051}, {"seed": 2002, "count": null, "done": true, "steps": 136, "seconds": 16.189, "policy_seconds": 0.0419}, {"seed": 2003, "count": null, "done": true, "steps": 96, "seconds": 11.8, "policy_seconds": 0.0223}, {"seed": 2004, "count": null, "done": true, "steps": 97, "seconds": 13.3, "policy_seconds": 0.0394}, {"seed": 2005, "count": null, "done": true, "steps": 42, "seconds": 4.16, "policy_seconds": 0.0101}, {"seed": 2006, "count": null, "done": true, "steps": 38, "seconds": 3.095, "policy_seconds": 0.008}, {"seed": 2007, "count": null, "done": true, "steps": 61, "seconds": 6.722, "policy_seconds": 0.017}, {"seed": 2008, "count": null, "done": true, "steps": 100, "seconds": 13.371, "policy_seconds": 0.0283}, {"seed": 2009, "count": null, "done": true, "steps": 86, "seconds": 11.299, "policy_seconds": 0.0301}, {"seed": 2010, "count": null, "done": true, "steps": 93, "seconds": 11.987, "policy_seconds": 0.0295}, {"seed": 2011, "count": null, "done": true, "steps": 94, "seconds": 11.108, "policy_seconds": 0.029}, {"seed": 2012, "count": null, "done": true, "steps": 81, "seconds": 10.869, "policy_seconds": 0.0171}, {"seed": 2013, "count": null, "done": true, "steps": 100, "seconds": 10.851, "policy_seconds": 0.0231}, {"seed": 2014, "count": null, "done": true, "steps": 55, "seconds": 5.774, "policy_seconds": 0.012}, {"seed": 2015, "count": null, "done": true, "steps": 58, "seconds": 7.145, "policy_seconds": 0.018}, {"seed": 2016, "count": null, "done": true, "steps": 25, "seconds": 1.633, "policy_seconds": 0.0066}, {"seed": 2017, "count": null, "done": true, "steps": 75, "seconds": 8.356, "policy_seconds": 0.0221}, {"seed": 2018, "count": null, "done": true, "steps": 28, "seconds": 2.87, "policy_seconds": 0.0072}, {"seed": 2019, "count": null, "done": true, "steps": 41, "seconds": 2.98, "policy_seconds": 0.0074}, {"seed": 2020, "count": null, "done": true, "steps": 18, "seconds": 1.084, "policy_seconds": 0.0055}, {"seed": 2021, "count": null, "done": true, "steps": 82, "seconds": 7.381, "policy_seconds": 0.0227}, {"seed": 2022, "count": null, "done": true, "steps": 99, "seconds": 9.348, "policy_seconds": 0.0199}, {"seed": 2023, "count": null, "done": true, "steps": 70, "seconds": 5.603, "policy_seconds": 0.015}, {"seed": 2024, "count": null, "done": true, "steps": 27, "seconds": 2.145, "policy_seconds": 0.0092}, {"seed": 2025, "count": null, "done": true, "steps": 21, "seconds": 1.667, "policy_seconds": 0.0052}, {"seed": 2026, "count": null, "done": true, "steps": 79, "seconds": 8.764, "policy_seconds": 0.0265}, {"seed": 2027, "count": null, "done": true, "steps": 26, "seconds": 1.904, "policy_seconds": 0.0056}, {"seed": 2028, "count": null, "done": true, "steps": 37, "seconds": 3.585, "policy_seconds": 0.0048}, {"seed": 2029, "count": null, "done": true, "steps": 20, "seconds": 2.09, "policy_seconds": 0.0058}, {"seed": 2030, "count": null, "done": true, "steps": 25, "seconds": 2.13, "policy_seconds": 0.006}, {"seed": 2031, "count": null, "done": true, "steps": 31, "seconds": 2.336, "policy_seconds": 0.0052}, {"seed": 2032, "count": null, "done": true, "steps": 90, "seconds": 7.248, "policy_seconds": 0.0201}, {"seed": 2033, "count": null, "done": true, "steps": 64, "seconds": 7.045, "policy_seconds": 0.02}, {"seed": 2034, "count": null, "done": true, "steps": 51, "seconds": 3.547, "policy_seconds": 0.0136}, {"seed": 2035, "count": null, "done": true, "steps": 20, "seconds": 1.109, "policy_seconds": 0.0034}, {"seed": 2036, "count": null, "done": true, "steps": 31, "seconds": 2.362, "policy_seconds": 0.0061}, {"seed": 2037, "count": null, "done": true, "steps": 80, "seconds": 9.268, "policy_seconds": 0.0244}, {"seed": 2038, "count": null, "done": true, "steps": 64, "seconds": 6.596, "policy_seconds": 0.0199}, {"seed": 2039, "count": null, "done": true, "steps": 144, "seconds": 17.259, "policy_seconds": 0.0434}, {"seed": 2040, "count": null, "done": true, "steps": 74, "seconds": 7.22, "policy_seconds": 0.0151}, {"seed": 2041, "count": null, "done": true, "steps": 57, "seconds": 5.658, "policy_seconds": 0.0191}, {"seed": 2042, "count": null, "done": true, "steps": 93, "seconds": 9.645, "policy_seconds": 0.0319}, {"seed": 2043, "count": null, "done": true, "steps": 75, "seconds": 5.781, "policy_seconds": 0.0219}, {"seed": 2044, "count": null, "done": true, "steps": 24, "seconds": 2.076, "policy_seconds": 0.0072}, {"seed": 2045, "count": null, "done": true, "steps": 21, "seconds": 1.584, "policy_seconds": 0.0058}, {"seed": 2046, "count": null, "done": true, "steps": 32, "seconds": 2.066, "policy_seconds": 0.0066}, {"seed": 2047, "count": null, "done": true, "steps": 24, "seconds": 1.055, "policy_seconds": 0.0055}, {"seed": 2048, "count": null, "done": true, "steps": 69, "seconds": 6.277, "policy_seconds": 0.0148}, {"seed": 2049, "count": null, "done": true, "steps": 20, "seconds": 0.962, "policy_seconds": 0.0033}, {"seed": 2050, "count": null, "done": true, "steps": 81, "seconds": 6.525, "policy_seconds": 0.0217}, {"seed": 2051, "count": null, "done": true, "steps": 34, "seconds": 3.165, "policy_seconds": 0.0076}, {"seed": 2052, "count": null, "done": true, "steps": 23, "seconds": 1.613, "policy_seconds": 0.0045}, {"seed": 2053, "count": null, "done": true, "steps": 19, "seconds": 1.109, "policy_seconds": 0.0051}, {"seed": 2054, "count": null, "done": true, "steps": 106, "seconds": 10.032, "policy_seconds": 0.0303}, {"seed": 2055, "count": null, "done": true, "steps": 21, "seconds": 1.495, "policy_seconds": 0.0058}, {"seed": 2056, "count": null, "done": true, "steps": 48, "seconds": 3.99, "policy_seconds": 0.0085}, {"seed": 2057, "count": null, "done": true, "steps": 37, "seconds": 3.101, "policy_seconds": 0.0128}, {"seed": 2058, "count": null, "done": true, "steps": 67, "seconds": 4.792, "policy_seconds": 0.0185}, {"seed": 2059, "count": null, "done": true, "steps": 86, "seconds": 6.127, "policy_seconds": 0.0233}, {"seed": 2060, "count": null, "done": true, "steps": 36, "seconds": 2.229, "policy_seconds": 0.0085}, {"seed": 2061, "count": null, "done": true, "steps": 34, "seconds": 2.171, "policy_seconds": 0.0067}, {"seed": 2062, "count": null, "done": true, "steps": 77, "seconds": 6.862, "policy_seconds": 0.0224}, {"seed": 2063, "count": null, "done": true, "steps": 27, "seconds": 1.588, "policy_seconds": 0.006}, {"seed": 2064, "count": null, "done": true, "steps": 66, "seconds": 4.949, "policy_seconds": 0.0166}, {"seed": 2065, "count": null, "done": true, "steps": 21, "seconds": 1.306, "policy_seconds": 0.0027}, {"seed": 2066, "count": null, "done": true, "steps": 84, "seconds": 6.45, "policy_seconds": 0.0195}, {"seed": 2067, "count": null, "done": true, "steps": 24, "seconds": 1.687, "policy_seconds": 0.0067}, {"seed": 2068, "count": null, "done": true, "steps": 49, "seconds": 5.654, "policy_seconds": 0.0092}, {"seed": 2069, "count": null, "done": true, "steps": 77, "seconds": 7.199, "policy_seconds": 0.0199}, {"seed": 2070, "count": null, "done": true, "steps": 68, "seconds": 5.979, "policy_seconds": 0.0155}, {"seed": 2071, "count": null, "done": true, "steps": 31, "seconds": 2.587, "policy_seconds": 0.0062}, {"seed": 2072, "count": null, "done": true, "steps": 45, "seconds": 4.742, "policy_seconds": 0.0147}, {"seed": 2073, "count": null, "done": true, "steps": 48, "seconds": 3.029, "policy_seconds": 0.0109}, {"seed": 2074, "count": null, "done": true, "steps": 25, "seconds": 1.376, "policy_seconds": 0.0043}, {"seed": 2075, "count": null, "done": true, "steps": 26, "seconds": 1.959, "policy_seconds": 0.0049}, {"seed": 2076, "count": null, "done": true, "steps": 51, "seconds": 4.217, "policy_seconds": 0.0127}, {"seed": 2077, "count": null, "done": true, "steps": 68, "seconds": 6.264, "policy_seconds": 0.0203}, {"seed": 2078, "count": null, "done": true, "steps": 42, "seconds": 3.804, "policy_seconds": 0.006}, {"seed": 2079, "count": null, "done": true, "steps": 18, "seconds": 1.422, "policy_seconds": 0.0054}, {"seed": 2080, "count": null, "done": true, "steps": 31, "seconds": 2.384, "policy_seconds": 0.0053}, {"seed": 2081, "count": null, "done": true, "steps": 19, "seconds": 1.151, "policy_seconds": 0.0058}, {"seed": 2082, "count": null, "done": true, "steps": 19, "seconds": 1.202, "policy_seconds": 0.0029}, {"seed": 2083, "count": null, "done": true, "steps": 32, "seconds": 2.07, "policy_seconds": 0.0092}, {"seed": 2084, "count": null, "done": true, "steps": 77, "seconds": 5.878, "policy_seconds": 0.0182}, {"seed": 2085, "count": null, "done": true, "steps": 83, "seconds": 6.306, "policy_seconds": 0.0187}, {"seed": 2086, "count": null, "done": true, "steps": 95, "seconds": 6.566, "policy_seconds": 0.0206}, {"seed": 2087, "count": null, "done": true, "steps": 100, "seconds": 9.757, "policy_seconds": 0.0291}, {"seed": 2088, "count": null, "done": true, "steps": 29, "seconds": 1.678, "policy_seconds": 0.0041}, {"seed": 2089, "count": null, "done": true, "steps": 72, "seconds": 6.706, "policy_seconds": 0.0225}, {"seed": 2090, "count": null, "done": true, "steps": 22, "seconds": 1.783, "policy_seconds": 0.0071}, {"seed": 2091, "count": null, "done": true, "steps": 28, "seconds": 1.315, "policy_seconds": 0.0059}, {"seed": 2092, "count": null, "done": true, "steps": 88, "seconds": 7.024, "policy_seconds": 0.0217}, {"seed": 2093, "count": null, "done": true, "steps": 36, "seconds": 1.816, "policy_seconds": 0.0054}, {"seed": 2094, "count": null, "done": true, "steps": 99, "seconds": 8.233, "policy_seconds": 0.032}, {"seed": 2095, "count": null, "done": true, "steps": 15, "seconds": 0.784, "policy_seconds": 0.0034}, {"seed": 2096, "count": null, "done": true, "steps": 114, "seconds": 11.692, "policy_seconds": 0.0257}, {"seed": 2097, "count": null, "done": true, "steps": 20, "seconds": 1.573, "policy_seconds": 0.0046}, {"seed": 2098, "count": null, "done": true, "steps": 23, "seconds": 1.794, "policy_seconds": 0.0059}, {"seed": 2099, "count": null, "done": true, "steps": 75, "seconds": 5.372, "policy_seconds": 0.0179}]
\ No newline at end of file
diff --git a/sweep_300_700.log b/sweep_300_700.log
index 3675dd6..84f5ede 100644
--- a/sweep_300_700.log
+++ b/sweep_300_700.log
@@ -310,3 +310,260 @@
  310    310  606 OK 93
  311    311  609 OK 62
  312    312  610 OK 35
         313 +611 OK 61
         314 +613 OK 56
         315 +614 OK 68
         316 +612 OK 116
         317 +616 OK 55
         318 +618 OK 21
         319 +615 OK 96
         320 +617 OK 62
         321 +619 OK 19
         322 +621 OK 22
         323 +620 OK 53
         324 +623 OK 19
         325 +622 OK 60
         326 +624 OK 44
         327 +625 OK 53
         328 +626 OK 54
         329 +628 OK 36
         330 +631 OK 30
         331 +629 OK 64
         332 +630 OK 76
         333 +632 OK 31
         334 +633 OK 26
         335 +636 OK 27
         336 +634 OK 50
         337 +637 OK 16
         338 +638 OK 23
         339 +635 OK 120
         340 +639 OK 97
         341 +640 OK 79
         342 +642 OK 21
         343 +643 OK 44
         344 +644 OK 45
         345 +645 OK 22
         346 +641 OK 103
         347 +647 OK 34
         348 +648 OK 32
         349 +646 OK 87
         350 +651 OK 27
         351 +649 OK 78
         352 +650 OK 42
         353 +652 OK 20
         354 +653 OK 15
         355 +654 OK 26
         356 +655 OK 27
         357 +656 OK 16
         358 +657 OK 21
         359 +658 OK 59
         360 +660 OK 56
         361 +659 OK 59
         362 +661 OK 37
         363 +662 OK 27
         364 +664 OK 42
         365 +663 OK 96
         366 +665 OK 63
         367 +666 OK 49
         368 +667 OK 39
         369 +668 OK 79
         370 +669 OK 77
         371 +670 OK 27
         372 +671 OK 29
         373 +672 OK 62
         374 +674 OK 50
         375 +673 OK 75
         376 +676 OK 24
         377 +675 OK 46
         378 +677 OK 35
         379 +627 FAIL 1000
         380 +{'seed': 627, 'count': None, 'done': False, 'steps': 1000, 'seconds': 128.098, 'policy_seconds': 0.1434, 'trace': [[840, 'down', 'target_block', 0.5233, 0.5412], [880, 'down', 'target_block', 0.5233, 0.3912], [920, 'lift', 'target_block', 0.5233, 0.5912], [960, 'down', 'target_block', 0.5233, 0.3912]], 'state': {'obstruction0': {'x': 1.070956826210022, 'y': 0.10000099986791611, 'width': 0.10327284038066864, 'height': 0.06639733165502548}, 'obstruction1': {'x': 0.5642479658126831, 'y': 0.10099996626377106, 'width': 0.1490718424320221, 'height': 0.1984524130821228}, 'target_block': {'x': 0.4953683614730835, 'y': 0.10000099986791611, 'width': 0.055879540741443634, 'height': 0.058782048523426056}, 'target_surface': {'x': 0.8293163180351257, 'y': 0.0, 'width': 0.09297315031290054, 'height': 0.10000000149011612}}}
         381 +678 OK 26
         382 +679 OK 60
         383 +680 OK 88
         384 +681 OK 78
         385 +682 OK 52
         386 +684 OK 34
         387 +683 OK 71
         388 +685 OK 96
         389 +686 OK 69
         390 +688 OK 24
         391 +687 OK 43
         392 +689 OK 31
         393 +690 OK 22
         394 +691 OK 17
         395 +692 OK 57
         396 +693 OK 61
         397 +694 OK 51
         398 +695 OK 38
         399 +696 OK 78
         400 +697 OK 86
         401 +698 OK 67
         402 +699 OK 74
         403 +700 OK 17
         404 +701 OK 17
         405 +702 OK 32
         406 +705 OK 36
         407 +704 OK 43
         408 +703 OK 78
         409 +707 OK 30
         410 +706 OK 56
         411 +708 OK 39
         412 +709 OK 42
         413 +710 OK 21
         414 +712 OK 29
         415 +711 OK 44
         416 +713 OK 64
         417 +715 OK 45
         418 +716 OK 46
         419 +714 OK 105
         420 +717 OK 22
         421 +718 OK 35
         422 +719 OK 61
         423 +721 OK 47
         424 +720 OK 72
         425 +722 OK 20
         426 +723 OK 24
         427 +724 OK 22
         428 +725 OK 28
         429 +726 OK 39
         430 +727 OK 22
         431 +728 OK 59
         432 +729 OK 30
         433 +730 OK 53
         434 +731 OK 42
         435 +732 OK 35
         436 +734 OK 19
         437 +735 OK 26
         438 +733 OK 90
         439 +736 OK 18
         440 +737 OK 25
         441 +738 OK 48
         442 +740 OK 44
         443 +739 OK 72
         444 +741 OK 44
         445 +742 OK 52
         446 +743 OK 42
         447 +744 OK 62
         448 +745 OK 63
         449 +747 OK 29
         450 +746 OK 73
         451 +749 OK 32
         452 +748 OK 63
         453 +750 OK 38
         454 +751 OK 65
         455 +753 OK 24
         456 +752 OK 63
         457 +754 OK 71
         458 +755 OK 61
         459 +756 OK 45
         460 +758 OK 18
         461 +757 OK 101
         462 +760 OK 36
         463 +759 OK 70
         464 +761 OK 56
         465 +762 OK 30
         466 +763 OK 31
         467 +767 OK 34
         468 +764 OK 87
         469 +766 OK 89
         470 +765 OK 117
         471 +769 OK 63
         472 +771 OK 33
         473 +772 OK 19
         474 +770 OK 74
         475 +768 OK 111
         476 +773 OK 71
         477 +774 OK 57
         478 +777 OK 54
         479 +775 OK 81
         480 +776 OK 101
         481 +778 OK 84
         482 +779 OK 66
         483 +780 OK 68
         484 +782 OK 43
         485 +781 OK 91
         486 +783 OK 66
         487 +786 OK 22
         488 +784 OK 80
         489 +785 OK 71
         490 +788 OK 49
         491 +790 OK 38
         492 +791 OK 33
         493 +787 OK 95
         494 +789 OK 87
         495 +792 OK 27
         496 +796 OK 18
         497 +793 OK 56
         498 +797 OK 31
         499 +795 OK 86
         500 +794 OK 97
         501 +798 OK 58
         502 +799 OK 54
         503 +800 OK 28
         504 +801 OK 68
         505 +802 OK 48
         506 +805 OK 28
         507 +804 OK 60
         508 +803 OK 90
         509 +806 OK 53
         510 +807 OK 18
         511 +810 OK 19
         512 +809 OK 49
         513 +811 OK 31
         514 +808 OK 68
         515 +814 OK 19
         516 +815 OK 22
         517 +813 OK 58
         518 +816 OK 16
         519 +812 OK 97
         520 +818 OK 44
         521 +821 OK 29
         522 +817 OK 85
         523 +820 OK 53
         524 +819 OK 74
         525 +823 OK 21
         526 +822 OK 79
         527 +824 OK 59
         528 +825 OK 48
         529 +827 OK 23
         530 +828 OK 53
         531 +830 OK 22
         532 +826 OK 113
         533 +831 OK 36
         534 +829 OK 70
         535 +833 OK 35
         536 +835 OK 50
         537 +834 OK 58
         538 +832 OK 110
         539 +836 OK 51
         540 +838 OK 25
         541 +837 OK 64
         542 +840 OK 44
         543 +842 OK 24
         544 +839 OK 87
         545 +841 OK 63
         546 +844 OK 58
         547 +845 OK 49
         548 +846 OK 33
         549 +847 OK 25
         550 +848 OK 19
         551 +843 OK 107
         552 +850 OK 34
         553 +851 OK 31
         554 +852 OK 29
         555 +849 OK 69
         556 +853 OK 42
         557 +854 OK 34
         558 +858 OK 19
         559 +859 OK 27
         560 +856 OK 82
         561 +857 OK 62
         562 +855 OK 104
         563 +862 OK 53
         564 +860 OK 87
         565 +863 OK 64
         566 +861 OK 88
         567 +865 OK 29
         568 +864 OK 86
         569 +867 OK 27
```

</details>

<a id="C037"></a>
### C037 · Preserve current policy and add bounded diagnostics for the remaining dense case

Commit `c167df52f32c0e1722684ef99e486cc1d127869f`; parents: c31a79bc47df67c90635a7deb725ead6a146e618. Recorded author date: 2026-09-21T23:05:53+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0186](01_timeline.md#E0186): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C037_c167df5.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_case.py b/probe_case.py
new file mode 100644
index 0000000..e8eb752
--- /dev/null
+++ b/probe_case.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import sys
           4 +e=make_env();s,i=e.reset(seed=int(sys.argv[1]),options={'object_count':int(sys.argv[2])});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
           5 +for t in range(200):
           6 + s,r,d,tr,i=e.step(p.get_action(s))
           7 + if d:break
           8 +print('done',d,'step',t+1,'phase',p.phase,'obj',p.obj,flush=True)
           9 +print('robot',[s.get(p.robot,f) for f in ['x','y','arm_joint']],flush=True)
          10 +for o in s.get_objects(p.ot):print(o.name,p.rect(s,o),flush=True)
          11 +print({k:v for k,v in p.__dict__.items() if k in ['destx','target_grasp','offsetx','offsety','dropx','dropy','emptyheight','carryheight','pick_y']},flush=True)
          12 +e.close()
diff --git a/sweep_300_700.log b/sweep_300_700.log
index 84f5ede..4921214 100644
--- a/sweep_300_700.log
+++ b/sweep_300_700.log
@@ -567,3 +567,134 @@
  567    567  865 OK 29
  568    568  864 OK 86
  569    569  867 OK 27
         570 +866 OK 72
         571 +868 OK 70
         572 +869 OK 62
         573 +871 OK 47
         574 +873 OK 27
         575 +870 OK 98
         576 +872 OK 65
         577 +874 OK 77
         578 +875 OK 56
         579 +876 OK 85
         580 +877 OK 63
         581 +879 OK 44
         582 +878 OK 78
         583 +881 OK 33
         584 +880 OK 71
         585 +882 OK 72
         586 +884 OK 31
         587 +883 OK 46
         588 +885 OK 20
         589 +887 OK 24
         590 +888 OK 29
         591 +890 OK 24
         592 +889 OK 56
         593 +886 OK 89
         594 +892 OK 26
         595 +893 OK 49
         596 +894 OK 46
         597 +891 OK 81
         598 +896 OK 19
         599 +895 OK 76
         600 +897 OK 41
         601 +898 OK 43
         602 +901 OK 33
         603 +899 OK 53
         604 +900 OK 62
         605 +904 OK 50
         606 +902 OK 90
         607 +905 OK 85
         608 +903 OK 97
         609 +906 OK 48
         610 +909 OK 18
         611 +907 OK 75
         612 +908 OK 65
         613 +911 OK 53
         614 +910 OK 82
         615 +912 OK 60
         616 +913 OK 46
         617 +916 OK 41
         618 +915 OK 68
         619 +917 OK 57
         620 +914 OK 97
         621 +921 OK 35
         622 +919 OK 69
         623 +920 OK 62
         624 +918 OK 111
         625 +925 OK 28
         626 +923 OK 62
         627 +922 OK 92
         628 +924 OK 79
         629 +928 OK 29
         630 +926 OK 52
         631 +927 OK 48
         632 +929 OK 23
         633 +932 OK 17
         634 +930 OK 51
         635 +931 OK 49
         636 +933 OK 74
         637 +934 OK 93
         638 +935 OK 63
         639 +936 OK 62
         640 +938 OK 24
         641 +939 OK 35
         642 +940 OK 19
         643 +941 OK 27
         644 +937 OK 94
         645 +942 OK 31
         646 +943 OK 31
         647 +944 OK 30
         648 +947 OK 20
         649 +946 OK 42
         650 +945 OK 59
         651 +948 OK 57
         652 +949 OK 47
         653 +950 OK 81
         654 +951 OK 92
         655 +952 OK 84
         656 +953 OK 69
         657 +955 OK 23
         658 +957 OK 20
         659 +956 OK 66
         660 +958 OK 50
         661 +959 OK 26
         662 +954 OK 101
         663 +961 OK 21
         664 +962 OK 23
         665 +963 OK 24
         666 +964 OK 25
         667 +960 OK 92
         668 +965 OK 50
         669 +967 OK 22
         670 +966 OK 50
         671 +969 OK 21
         672 +968 OK 55
         673 +971 OK 33
         674 +972 OK 38
         675 +973 OK 24
         676 +970 OK 66
         677 +976 OK 20
         678 +974 OK 77
         679 +975 OK 62
         680 +978 OK 27
         681 +977 OK 53
         682 +980 OK 22
         683 +981 OK 29
         684 +979 OK 58
         685 +982 OK 51
         686 +984 OK 25
         687 +983 OK 55
         688 +985 OK 40
         689 +986 OK 25
         690 +988 OK 27
         691 +987 OK 44
         692 +992 OK 23
         693 +989 OK 57
         694 +991 OK 46
         695 +990 OK 82
         696 +994 OK 20
         697 +993 OK 54
         698 +995 OK 58
         699 +996 OK 46
         700 +997 OK 77
```

</details>

<a id="C038"></a>
### C038 · Include circle-tangent and edge-contact grasps around tall neighbors

Commit `5f1766ad5616a95b45e3437b782ad057710c1560`; parents: c167df52f32c0e1722684ef99e486cc1d127869f. Recorded author date: 2026-09-21T23:06:55+02:00.

File roles (automatic): policy, setup/other.

- [E0188](01_timeline.md#E0188): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C038_5f1766a_approach.py) · [Exact all-file diff](evidence/diffs/C038_5f1766a.diff)

[Previous saved controller snapshot](evidence/versions/C033_394488d_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f3fb83c..90ae232 100644
--- a/approach.py
+++ b/approach.py
@@ -36,10 +36,15 @@ class GeneratedApproach:
   36     36      def grasp_position(self, s, obj, preferred):
   37     37          x,y,w,h=self.rect(s,obj)
   38     38          others=[self.rect(s,o) for o in s.get_objects(self.ot) if o!=obj]
   39        -        candidates=[preferred,x+w/2,x+.005,x+w-.005,.101,1.517]
          39 +        candidates=[preferred,x+w/2,x+.005,x+w-.005,x-.025,x+w+.025,.101,1.517]
   40     40          if obj==self.block:candidates.extend([x+1.516-self.destx,x+.102-self.destx])
   41     41          for ox,oy,ow,oh in others:
   42     42              candidates.extend([ox-.041,ox+ow+.041])
          43 +            cy=y+h+.206
          44 +            dy=max(oy-cy,0,cy-oy-oh)
          45 +            if dy<.102:
          46 +                reach=math.sqrt(.102**2-dy**2)+.002
          47 +                candidates.extend([ox-reach,ox+ow+reach])
   43     48          valid=[]
   44     49          for cx in candidates:
   45     50              if not .101<=cx<=1.517 or cx+.035<x+.006 or cx-.035>x+w-.006:continue
diff --git a/results_100_100_3.json b/results_100_100_3.json
new file mode 100644
index 0000000..f0e79eb
--- /dev/null
+++ b/results_100_100_3.json
@@ -0,0 +1 @@
           1 +[{"seed": 100, "count": 3, "done": true, "steps": 96, "seconds": 11.429, "policy_seconds": 0.0246}, {"seed": 101, "count": 3, "done": true, "steps": 81, "seconds": 9.405, "policy_seconds": 0.0228}, {"seed": 102, "count": 3, "done": true, "steps": 93, "seconds": 11.735, "policy_seconds": 0.0297}, {"seed": 103, "count": 3, "done": true, "steps": 63, "seconds": 7.753, "policy_seconds": 0.0172}, {"seed": 104, "count": 3, "done": true, "steps": 90, "seconds": 11.216, "policy_seconds": 0.0264}, {"seed": 105, "count": 3, "done": true, "steps": 86, "seconds": 10.266, "policy_seconds": 0.0243}, {"seed": 106, "count": 3, "done": true, "steps": 57, "seconds": 6.797, "policy_seconds": 0.0148}, {"seed": 107, "count": 3, "done": true, "steps": 88, "seconds": 10.254, "policy_seconds": 0.0239}, {"seed": 108, "count": 3, "done": true, "steps": 110, "seconds": 12.337, "policy_seconds": 0.0333}, {"seed": 109, "count": 3, "done": true, "steps": 73, "seconds": 8.246, "policy_seconds": 0.0183}, {"seed": 110, "count": 3, "done": true, "steps": 98, "seconds": 11.107, "policy_seconds": 0.0307}, {"seed": 111, "count": 3, "done": true, "steps": 110, "seconds": 12.227, "policy_seconds": 0.0255}, {"seed": 112, "count": 3, "done": true, "steps": 70, "seconds": 7.636, "policy_seconds": 0.0242}, {"seed": 113, "count": 3, "done": true, "steps": 80, "seconds": 8.624, "policy_seconds": 0.0191}, {"seed": 114, "count": 3, "done": true, "steps": 133, "seconds": 13.47, "policy_seconds": 0.0337}, {"seed": 115, "count": 3, "done": true, "steps": 145, "seconds": 17.509, "policy_seconds": 0.0293}, {"seed": 116, "count": 3, "done": true, "steps": 53, "seconds": 6.141, "policy_seconds": 0.0158}, {"seed": 117, "count": 3, "done": true, "steps": 91, "seconds": 11.222, "policy_seconds": 0.0322}, {"seed": 118, "count": 3, "done": true, "steps": 70, "seconds": 7.89, "policy_seconds": 0.0194}, {"seed": 119, "count": 3, "done": true, "steps": 80, "seconds": 8.878, "policy_seconds": 0.027}, {"seed": 120, "count": 3, "done": true, "steps": 68, "seconds": 7.132, "policy_seconds": 0.0223}, {"seed": 121, "count": 3, "done": true, "steps": 109, "seconds": 10.642, "policy_seconds": 0.0299}, {"seed": 122, "count": 3, "done": true, "steps": 76, "seconds": 8.371, "policy_seconds": 0.0255}, {"seed": 123, "count": 3, "done": true, "steps": 97, "seconds": 10.533, "policy_seconds": 0.0292}, {"seed": 124, "count": 3, "done": true, "steps": 95, "seconds": 11.054, "policy_seconds": 0.0201}, {"seed": 125, "count": 3, "done": true, "steps": 102, "seconds": 10.964, "policy_seconds": 0.0288}, {"seed": 126, "count": 3, "done": true, "steps": 54, "seconds": 6.132, "policy_seconds": 0.0146}, {"seed": 127, "count": 3, "done": true, "steps": 91, "seconds": 9.444, "policy_seconds": 0.023}, {"seed": 128, "count": 3, "done": true, "steps": 152, "seconds": 14.574, "policy_seconds": 0.0444}, {"seed": 129, "count": 3, "done": true, "steps": 97, "seconds": 9.837, "policy_seconds": 0.0285}, {"seed": 130, "count": 3, "done": true, "steps": 92, "seconds": 8.021, "policy_seconds": 0.0257}, {"seed": 131, "count": 3, "done": true, "steps": 76, "seconds": 7.669, "policy_seconds": 0.0208}, {"seed": 132, "count": 3, "done": true, "steps": 122, "seconds": 12.936, "policy_seconds": 0.0378}, {"seed": 133, "count": 3, "done": true, "steps": 75, "seconds": 9.179, "policy_seconds": 0.0265}, {"seed": 134, "count": 3, "done": true, "steps": 104, "seconds": 11.945, "policy_seconds": 0.025}, {"seed": 135, "count": 3, "done": true, "steps": 120, "seconds": 14.229, "policy_seconds": 0.033}, {"seed": 136, "count": 3, "done": true, "steps": 67, "seconds": 7.179, "policy_seconds": 0.025}, {"seed": 137, "count": 3, "done": true, "steps": 82, "seconds": 8.028, "policy_seconds": 0.0233}, {"seed": 138, "count": 3, "done": true, "steps": 112, "seconds": 11.554, "policy_seconds": 0.0289}, {"seed": 139, "count": 3, "done": true, "steps": 53, "seconds": 5.535, "policy_seconds": 0.0155}, {"seed": 140, "count": 3, "done": true, "steps": 76, "seconds": 7.225, "policy_seconds": 0.0196}, {"seed": 141, "count": 3, "done": true, "steps": 55, "seconds": 5.922, "policy_seconds": 0.0141}, {"seed": 142, "count": 3, "done": true, "steps": 73, "seconds": 8.933, "policy_seconds": 0.0217}, {"seed": 143, "count": 3, "done": true, "steps": 114, "seconds": 13.013, "policy_seconds": 0.0297}, {"seed": 144, "count": 3, "done": true, "steps": 58, "seconds": 7.028, "policy_seconds": 0.0194}, {"seed": 145, "count": 3, "done": true, "steps": 97, "seconds": 11.55, "policy_seconds": 0.0241}, {"seed": 146, "count": 3, "done": true, "steps": 69, "seconds": 7.637, "policy_seconds": 0.0215}, {"seed": 147, "count": 3, "done": true, "steps": 66, "seconds": 8.124, "policy_seconds": 0.0173}, {"seed": 148, "count": 3, "done": true, "steps": 88, "seconds": 8.024, "policy_seconds": 0.0258}, {"seed": 149, "count": 3, "done": true, "steps": 58, "seconds": 5.389, "policy_seconds": 0.0162}, {"seed": 150, "count": 3, "done": true, "steps": 89, "seconds": 9.567, "policy_seconds": 0.0274}, {"seed": 151, "count": 3, "done": true, "steps": 65, "seconds": 7.531, "policy_seconds": 0.0223}, {"seed": 152, "count": 3, "done": true, "steps": 91, "seconds": 9.421, "policy_seconds": 0.0265}, {"seed": 153, "count": 3, "done": true, "steps": 110, "seconds": 13.16, "policy_seconds": 0.0342}, {"seed": 154, "count": 3, "done": false, "steps": 1000, "seconds": 119.072, "policy_seconds": 0.1433, "trace": [[840, "lift", "obstruction2", 0.8709, 0.5685], [880, "down", "obstruction2", 0.8709, 0.5185], [920, "down", "obstruction2", 0.8709, 0.5185], [960, "lift", "obstruction2", 0.8709, 0.5685]], "state": {"obstruction0": {"x": 1.261906385421753, "y": 0.10000099986791611, "width": 0.11977946758270264, "height": 0.09862594306468964}, "obstruction1": {"x": 0.897899866104126, "y": 0.10000099986791611, "width": 0.1302715241909027, "height": 0.1840483695268631}, "obstruction2": {"x": 0.8444396257400513, "y": 0.10000099986791611, "width": 0.0528520867228508, "height": 0.051484327763319016}, "target_block": {"x": 0.4272967278957367, "y": 0.10000099986791611, "width": 0.1980142444372177, "height": 0.09921976923942566}, "target_surface": {"x": 0.6849659085273743, "y": 0.0, "width": 0.24095721542835236, "height": 0.10000000149011612}}}, {"seed": 155, "count": 3, "done": true, "steps": 94, "seconds": 11.177, "policy_seconds": 0.0287}, {"seed": 156, "count": 3, "done": true, "steps": 65, "seconds": 7.177, "policy_seconds": 0.0179}, {"seed": 157, "count": 3, "done": true, "steps": 64, "seconds": 7.103, "policy_seconds": 0.0226}, {"seed": 158, "count": 3, "done": true, "steps": 48, "seconds": 4.384, "policy_seconds": 0.0164}, {"seed": 159, "count": 3, "done": true, "steps": 55, "seconds": 4.694, "policy_seconds": 0.0139}, {"seed": 160, "count": 3, "done": true, "steps": 83, "seconds": 9.638, "policy_seconds": 0.0209}, {"seed": 161, "count": 3, "done": true, "steps": 67, "seconds": 8.046, "policy_seconds": 0.0145}, {"seed": 162, "count": 3, "done": true, "steps": 60, "seconds": 6.855, "policy_seconds": 0.0208}, {"seed": 163, "count": 3, "done": true, "steps": 56, "seconds": 4.896, "policy_seconds": 0.0174}, {"seed": 164, "count": 3, "done": true, "steps": 122, "seconds": 13.295, "policy_seconds": 0.0387}, {"seed": 165, "count": 3, "done": true, "steps": 98, "seconds": 11.67, "policy_seconds": 0.0314}, {"seed": 166, "count": 3, "done": true, "steps": 105, "seconds": 13.57, "policy_seconds": 0.0265}, {"seed": 167, "count": 3, "done": true, "steps": 57, "seconds": 7.77, "policy_seconds": 0.02}, {"seed": 168, "count": 3, "done": true, "steps": 65, "seconds": 8.328, "policy_seconds": 0.0212}, {"seed": 169, "count": 3, "done": true, "steps": 44, "seconds": 4.217, "policy_seconds": 0.0188}, {"seed": 170, "count": 3, "done": true, "steps": 83, "seconds": 11.083, "policy_seconds": 0.0206}, {"seed": 171, "count": 3, "done": true, "steps": 28, "seconds": 3.009, "policy_seconds": 0.0139}, {"seed": 172, "count": 3, "done": true, "steps": 67, "seconds": 8.164, "policy_seconds": 0.0215}, {"seed": 173, "count": 3, "done": true, "steps": 108, "seconds": 12.455, "policy_seconds": 0.0327}, {"seed": 174, "count": 3, "done": true, "steps": 54, "seconds": 6.673, "policy_seconds": 0.0152}, {"seed": 175, "count": 3, "done": true, "steps": 69, "seconds": 7.084, "policy_seconds": 0.0212}, {"seed": 176, "count": 3, "done": true, "steps": 76, "seconds": 7.821, "policy_seconds": 0.0215}, {"seed": 177, "count": 3, "done": true, "steps": 47, "seconds": 5.36, "policy_seconds": 0.0122}, {"seed": 178, "count": 3, "done": true, "steps": 86, "seconds": 8.226, "policy_seconds": 0.0226}, {"seed": 179, "count": 3, "done": true, "steps": 53, "seconds": 4.528, "policy_seconds": 0.0142}, {"seed": 180, "count": 3, "done": true, "steps": 96, "seconds": 8.251, "policy_seconds": 0.0305}, {"seed": 181, "count": 3, "done": true, "steps": 69, "seconds": 5.376, "policy_seconds": 0.0189}, {"seed": 182, "count": 3, "done": true, "steps": 113, "seconds": 8.267, "policy_seconds": 0.0316}, {"seed": 183, "count": 3, "done": true, "steps": 81, "seconds": 5.137, "policy_seconds": 0.0289}, {"seed": 184, "count": 3, "done": true, "steps": 111, "seconds": 7.434, "policy_seconds": 0.032}, {"seed": 185, "count": 3, "done": true, "steps": 77, "seconds": 4.999, "policy_seconds": 0.0239}, {"seed": 186, "count": 3, "done": true, "steps": 82, "seconds": 5.28, "policy_seconds": 0.026}, {"seed": 187, "count": 3, "done": true, "steps": 82, "seconds": 5.569, "policy_seconds": 0.0242}, {"seed": 188, "count": 3, "done": true, "steps": 92, "seconds": 4.751, "policy_seconds": 0.0223}, {"seed": 189, "count": 3, "done": true, "steps": 106, "seconds": 5.268, "policy_seconds": 0.0273}, {"seed": 190, "count": 3, "done": true, "steps": 73, "seconds": 2.972, "policy_seconds": 0.0252}, {"seed": 191, "count": 3, "done": true, "steps": 109, "seconds": 5.837, "policy_seconds": 0.0262}, {"seed": 192, "count": 3, "done": true, "steps": 68, "seconds": 2.993, "policy_seconds": 0.0195}, {"seed": 193, "count": 3, "done": true, "steps": 116, "seconds": 5.749, "policy_seconds": 0.0337}, {"seed": 194, "count": 3, "done": true, "steps": 113, "seconds": 5.662, "policy_seconds": 0.0297}, {"seed": 195, "count": 3, "done": true, "steps": 65, "seconds": 2.797, "policy_seconds": 0.0143}, {"seed": 196, "count": 3, "done": true, "steps": 46, "seconds": 2.031, "policy_seconds": 0.0186}, {"seed": 197, "count": 3, "done": true, "steps": 122, "seconds": 3.732, "policy_seconds": 0.0328}, {"seed": 198, "count": 3, "done": true, "steps": 100, "seconds": 3.299, "policy_seconds": 0.0218}, {"seed": 199, "count": 3, "done": true, "steps": 76, "seconds": 1.956, "policy_seconds": 0.0193}]
\ No newline at end of file
diff --git a/results_300_700_None.json b/results_300_700_None.json
new file mode 100644
index 0000000..e2965bf
--- /dev/null
+++ b/results_300_700_None.json
@@ -0,0 +1 @@
           1 +[{"seed": 300, "count": null, "done": true, "steps": 28, "seconds": 2.375, "policy_seconds": 0.0063}, {"seed": 301, "count": null, "done": true, "steps": 47, "seconds": 3.398, "policy_seconds": 0.0101}, {"seed": 302, "count": null, "done": true, "steps": 54, "seconds": 5.825, "policy_seconds": 0.0185}, {"seed": 303, "count": null, "done": true, "steps": 80, "seconds": 6.759, "policy_seconds": 0.0224}, {"seed": 304, "count": null, "done": true, "steps": 51, "seconds": 6.039, "policy_seconds": 0.02}, {"seed": 305, "count": null, "done": true, "steps": 29, "seconds": 2.483, "policy_seconds": 0.0058}, {"seed": 306, "count": null, "done": true, "steps": 62, "seconds": 6.05, "policy_seconds": 0.0183}, {"seed": 307, "count": null, "done": true, "steps": 38, "seconds": 3.534, "policy_seconds": 0.0112}, {"seed": 308, "count": null, "done": true, "steps": 57, "seconds": 4.964, "policy_seconds": 0.0157}, {"seed": 309, "count": null, "done": true, "steps": 79, "seconds": 5.763, "policy_seconds": 0.0193}, {"seed": 310, "count": null, "done": true, "steps": 24, "seconds": 1.594, "policy_seconds": 0.0062}, {"seed": 311, "count": null, "done": true, "steps": 50, "seconds": 3.74, "policy_seconds": 0.0143}, {"seed": 312, "count": null, "done": true, "steps": 50, "seconds": 3.705, "policy_seconds": 0.0077}, {"seed": 313, "count": null, "done": true, "steps": 27, "seconds": 2.059, "policy_seconds": 0.0063}, {"seed": 314, "count": null, "done": true, "steps": 37, "seconds": 2.872, "policy_seconds": 0.0094}, {"seed": 315, "count": null, "done": true, "steps": 27, "seconds": 1.928, "policy_seconds": 0.007}, {"seed": 316, "count": null, "done": true, "steps": 29, "seconds": 1.715, "policy_seconds": 0.0044}, {"seed": 317, "count": null, "done": true, "steps": 17, "seconds": 0.824, "policy_seconds": 0.005}, {"seed": 318, "count": null, "done": true, "steps": 48, "seconds": 3.148, "policy_seconds": 0.0097}, {"seed": 319, "count": null, "done": true, "steps": 72, "seconds": 8.002, "policy_seconds": 0.017}, {"seed": 320, "count": null, "done": true, "steps": 21, "seconds": 1.764, "policy_seconds": 0.0063}, {"seed": 321, "count": null, "done": true, "steps": 44, "seconds": 4.486, "policy_seconds": 0.0151}, {"seed": 322, "count": null, "done": true, "steps": 27, "seconds": 2.252, "policy_seconds": 0.0067}, {"seed": 323, "count": null, "done": true, "steps": 43, "seconds": 3.445, "policy_seconds": 0.0072}, {"seed": 324, "count": null, "done": true, "steps": 84, "seconds": 5.229, "policy_seconds": 0.0185}, {"seed": 325, "count": null, "done": true, "steps": 23, "seconds": 1.024, "policy_seconds": 0.0045}, {"seed": 326, "count": null, "done": true, "steps": 52, "seconds": 4.428, "policy_seconds": 0.0078}, {"seed": 327, "count": null, "done": true, "steps": 34, "seconds": 2.85, "policy_seconds": 0.0084}, {"seed": 328, "count": null, "done": true, "steps": 21, "seconds": 1.672, "policy_seconds": 0.0063}, {"seed": 329, "count": null, "done": true, "steps": 63, "seconds": 5.122, "policy_seconds": 0.0192}, {"seed": 330, "count": null, "done": true, "steps": 56, "seconds": 4.673, "policy_seconds": 0.019}, {"seed": 331, "count": null, "done": true, "steps": 22, "seconds": 1.826, "policy_seconds": 0.0057}, {"seed": 332, "count": null, "done": true, "steps": 51, "seconds": 4.902, "policy_seconds": 0.0152}, {"seed": 333, "count": null, "done": true, "steps": 17, "seconds": 1.054, "policy_seconds": 0.0051}, {"seed": 334, "count": null, "done": true, "steps": 24, "seconds": 1.703, "policy_seconds": 0.0069}, {"seed": 335, "count": null, "done": true, "steps": 23, "seconds": 1.739, "policy_seconds": 0.0061}, {"seed": 336, "count": null, "done": true, "steps": 54, "seconds": 5.041, "policy_seconds": 0.0179}, {"seed": 337, "count": null, "done": true, "steps": 62, "seconds": 4.793, "policy_seconds": 0.0106}, {"seed": 338, "count": null, "done": true, "steps": 21, "seconds": 2.255, "policy_seconds": 0.0063}, {"seed": 339, "count": null, "done": true, "steps": 37, "seconds": 2.495, "policy_seconds": 0.0075}, {"seed": 340, "count": null, "done": true, "steps": 16, "seconds": 0.884, "policy_seconds": 0.0044}, {"seed": 341, "count": null, "done": true, "steps": 56, "seconds": 4.79, "policy_seconds": 0.0184}, {"seed": 342, "count": null, "done": true, "steps": 77, "seconds": 8.158, "policy_seconds": 0.0241}, {"seed": 343, "count": null, "done": true, "steps": 27, "seconds": 1.897, "policy_seconds": 0.0063}, {"seed": 344, "count": null, "done": true, "steps": 28, "seconds": 2.464, "policy_seconds": 0.0095}, {"seed": 345, "count": null, "done": true, "steps": 36, "seconds": 2.997, "policy_seconds": 0.0087}, {"seed": 346, "count": null, "done": true, "steps": 94, "seconds": 7.604, "policy_seconds": 0.0248}, {"seed": 347, "count": null, "done": true, "steps": 49, "seconds": 5.031, "policy_seconds": 0.0161}, {"seed": 348, "count": null, "done": true, "steps": 32, "seconds": 2.004, "policy_seconds": 0.0072}, {"seed": 349, "count": null, "done": true, "steps": 40, "seconds": 3.603, "policy_seconds": 0.0108}, {"seed": 350, "count": null, "done": true, "steps": 42, "seconds": 3.575, "policy_seconds": 0.0128}, {"seed": 351, "count": null, "done": true, "steps": 92, "seconds": 8.436, "policy_seconds": 0.02}, {"seed": 352, "count": null, "done": true, "steps": 38, "seconds": 2.679, "policy_seconds": 0.0084}, {"seed": 353, "count": null, "done": true, "steps": 31, "seconds": 2.745, "policy_seconds": 0.0073}, {"seed": 354, "count": null, "done": true, "steps": 98, "seconds": 11.905, "policy_seconds": 0.0304}, {"seed": 355, "count": null, "done": true, "steps": 29, "seconds": 2.827, "policy_seconds": 0.0076}, {"seed": 356, "count": null, "done": true, "steps": 29, "seconds": 2.192, "policy_seconds": 0.0042}, {"seed": 357, "count": null, "done": true, "steps": 75, "seconds": 6.957, "policy_seconds": 0.0143}, {"seed": 358, "count": null, "done": true, "steps": 46, "seconds": 5.651, "policy_seconds": 0.011}, {"seed": 359, "count": null, "done": true, "steps": 83, "seconds": 8.723, "policy_seconds": 0.0198}, {"seed": 360, "count": null, "done": true, "steps": 72, "seconds": 8.731, "policy_seconds": 0.0191}, {"seed": 361, "count": null, "done": true, "steps": 65, "seconds": 7.313, "policy_seconds": 0.0197}, {"seed": 362, "count": null, "done": true, "steps": 65, "seconds": 7.12, "policy_seconds": 0.0202}, {"seed": 363, "count": null, "done": true, "steps": 48, "seconds": 3.289, "policy_seconds": 0.0096}, {"seed": 364, "count": null, "done": true, "steps": 30, "seconds": 2.337, "policy_seconds": 0.0077}, {"seed": 365, "count": null, "done": true, "steps": 40, "seconds": 2.566, "policy_seconds": 0.0072}, {"seed": 366, "count": null, "done": true, "steps": 26, "seconds": 1.372, "policy_seconds": 0.0058}, {"seed": 367, "count": null, "done": true, "steps": 97, "seconds": 8.439, "policy_seconds": 0.022}, {"seed": 368, "count": null, "done": true, "steps": 89, "seconds": 7.277, "policy_seconds": 0.0189}, {"seed": 369, "count": null, "done": true, "steps": 90, "seconds": 8.881, "policy_seconds": 0.0259}, {"seed": 370, "count": null, "done": true, "steps": 52, "seconds": 3.877, "policy_seconds": 0.0107}, {"seed": 371, "count": null, "done": true, "steps": 20, "seconds": 2.007, "policy_seconds": 0.0065}, {"seed": 372, "count": null, "done": true, "steps": 79, "seconds": 7.489, "policy_seconds": 0.0182}, {"seed": 373, "count": null, "done": true, "steps": 60, "seconds": 5.317, "policy_seconds": 0.0159}, {"seed": 374, "count": null, "done": true, "steps": 49, "seconds": 5.233, "policy_seconds": 0.0133}, {"seed": 375, "count": null, "done": true, "steps": 33, "seconds": 2.002, "policy_seconds": 0.0075}, {"seed": 376, "count": null, "done": true, "steps": 78, "seconds": 6.691, "policy_seconds": 0.0188}, {"seed": 377, "count": null, "done": true, "steps": 64, "seconds": 7.002, "policy_seconds": 0.0199}, {"seed": 378, "count": null, "done": true, "steps": 89, "seconds": 7.094, "policy_seconds": 0.0222}, {"seed": 379, "count": null, "done": true, "steps": 55, "seconds": 5.699, "policy_seconds": 0.0178}, {"seed": 380, "count": null, "done": true, "steps": 49, "seconds": 4.052, "policy_seconds": 0.0104}, {"seed": 381, "count": null, "done": true, "steps": 84, "seconds": 9.261, "policy_seconds": 0.0196}, {"seed": 382, "count": null, "done": true, "steps": 48, "seconds": 3.572, "policy_seconds": 0.0099}, {"seed": 383, "count": null, "done": true, "steps": 36, "seconds": 2.233, "policy_seconds": 0.0074}, {"seed": 384, "count": null, "done": true, "steps": 38, "seconds": 2.58, "policy_seconds": 0.0065}, {"seed": 385, "count": null, "done": true, "steps": 90, "seconds": 8.879, "policy_seconds": 0.0153}, {"seed": 386, "count": null, "done": true, "steps": 54, "seconds": 3.89, "policy_seconds": 0.0127}, {"seed": 387, "count": null, "done": true, "steps": 61, "seconds": 5.116, "policy_seconds": 0.0153}, {"seed": 388, "count": null, "done": true, "steps": 38, "seconds": 3.543, "policy_seconds": 0.0111}, {"seed": 389, "count": null, "done": true, "steps": 32, "seconds": 2.026, "policy_seconds": 0.0062}, {"seed": 390, "count": null, "done": true, "steps": 65, "seconds": 4.98, "policy_seconds": 0.0165}, {"seed": 391, "count": null, "done": true, "steps": 41, "seconds": 2.58, "policy_seconds": 0.0085}, {"seed": 392, "count": null, "done": true, "steps": 47, "seconds": 4.016, "policy_seconds": 0.0151}, {"seed": 393, "count": null, "done": true, "steps": 23, "seconds": 1.839, "policy_seconds": 0.0082}, {"seed": 394, "count": null, "done": true, "steps": 17, "seconds": 1.018, "policy_seconds": 0.0047}, {"seed": 395, "count": null, "done": true, "steps": 44, "seconds": 4.352, "policy_seconds": 0.0101}, {"seed": 396, "count": null, "done": true, "steps": 80, "seconds": 7.699, "policy_seconds": 0.0192}, {"seed": 397, "count": null, "done": true, "steps": 48, "seconds": 5.472, "policy_seconds": 0.0173}, {"seed": 398, "count": null, "done": true, "steps": 46, "seconds": 5.099, "policy_seconds": 0.0168}, {"seed": 399, "count": null, "done": true, "steps": 101, "seconds": 10.492, "policy_seconds": 0.0281}, {"seed": 400, "count": null, "done": true, "steps": 100, "seconds": 11.134, "policy_seconds": 0.0236}, {"seed": 401, "count": null, "done": true, "steps": 47, "seconds": 4.002, "policy_seconds": 0.0137}, {"seed": 402, "count": null, "done": true, "steps": 87, "seconds": 9.156, "policy_seconds": 0.0249}, {"seed": 403, "count": null, "done": true, "steps": 31, "seconds": 2.082, "policy_seconds": 0.0078}, {"seed": 404, "count": null, "done": true, "steps": 47, "seconds": 4.033, "policy_seconds": 0.0167}, {"seed": 405, "count": null, "done": true, "steps": 37, "seconds": 2.553, "policy_seconds": 0.0069}, {"seed": 406, "count": null, "done": true, "steps": 56, "seconds": 4.977, "policy_seconds": 0.0151}, {"seed": 407, "count": null, "done": true, "steps": 30, "seconds": 1.646, "policy_seconds": 0.0048}, {"seed": 408, "count": null, "done": true, "steps": 21, "seconds": 1.901, "policy_seconds": 0.0046}, {"seed": 409, "count": null, "done": true, "steps": 37, "seconds": 2.704, "policy_seconds": 0.0088}, {"seed": 410, "count": null, "done": true, "steps": 56, "seconds": 4.786, "policy_seconds": 0.018}, {"seed": 411, "count": null, "done": true, "steps": 32, "seconds": 2.162, "policy_seconds": 0.0075}, {"seed": 412, "count": null, "done": true, "steps": 67, "seconds": 6.115, "policy_seconds": 0.0188}, {"seed": 413, "count": null, "done": true, "steps": 24, "seconds": 1.558, "policy_seconds": 0.0039}, {"seed": 414, "count": null, "done": true, "steps": 52, "seconds": 5.89, "policy_seconds": 0.0205}, {"seed": 415, "count": null, "done": true, "steps": 70, "seconds": 6.712, "policy_seconds": 0.0201}, {"seed": 416, "count": null, "done": true, "steps": 68, "seconds": 6.08, "policy_seconds": 0.017}, {"seed": 417, "count": null, "done": true, "steps": 30, "seconds": 2.683, "policy_seconds": 0.0042}, {"seed": 418, "count": null, "done": true, "steps": 25, "seconds": 1.667, "policy_seconds": 0.0047}, {"seed": 419, "count": null, "done": true, "steps": 26, "seconds": 2.763, "policy_seconds": 0.0081}, {"seed": 420, "count": null, "done": true, "steps": 43, "seconds": 3.404, "policy_seconds": 0.0094}, {"seed": 421, "count": null, "done": true, "steps": 45, "seconds": 3.083, "policy_seconds": 0.0091}, {"seed": 422, "count": null, "done": true, "steps": 35, "seconds": 3.105, "policy_seconds": 0.0071}, {"seed": 423, "count": null, "done": true, "steps": 35, "seconds": 2.253, "policy_seconds": 0.0083}, {"seed": 424, "count": null, "done": true, "steps": 20, "seconds": 1.373, "policy_seconds": 0.0051}, {"seed": 425, "count": null, "done": true, "steps": 32, "seconds": 1.212, "policy_seconds": 0.0068}, {"seed": 426, "count": null, "done": true, "steps": 25, "seconds": 1.388, "policy_seconds": 0.004}, {"seed": 427, "count": null, "done": true, "steps": 48, "seconds": 4.379, "policy_seconds": 0.0173}, {"seed": 428, "count": null, "done": true, "steps": 24, "seconds": 1.293, "policy_seconds": 0.0058}, {"seed": 429, "count": null, "done": true, "steps": 30, "seconds": 1.273, "policy_seconds": 0.0052}, {"seed": 430, "count": null, "done": true, "steps": 32, "seconds": 2.114, "policy_seconds": 0.0071}, {"seed": 431, "count": null, "done": true, "steps": 58, "seconds": 5.261, "policy_seconds": 0.0186}, {"seed": 432, "count": null, "done": true, "steps": 43, "seconds": 4.816, "policy_seconds": 0.0136}, {"seed": 433, "count": null, "done": true, "steps": 33, "seconds": 2.347, "policy_seconds": 0.0076}, {"seed": 434, "count": null, "done": true, "steps": 27, "seconds": 3.177, "policy_seconds": 0.0079}, {"seed": 435, "count": null, "done": true, "steps": 47, "seconds": 2.671, "policy_seconds": 0.0145}, {"seed": 436, "count": null, "done": true, "steps": 72, "seconds": 5.95, "policy_seconds": 0.0202}, {"seed": 437, "count": null, "done": true, "steps": 57, "seconds": 4.775, "policy_seconds": 0.0157}, {"seed": 438, "count": null, "done": true, "steps": 41, "seconds": 3.174, "policy_seconds": 0.0086}, {"seed": 439, "count": null, "done": true, "steps": 34, "seconds": 2.764, "policy_seconds": 0.0067}, {"seed": 440, "count": null, "done": true, "steps": 23, "seconds": 0.812, "policy_seconds": 0.0031}, {"seed": 441, "count": null, "done": true, "steps": 85, "seconds": 4.851, "policy_seconds": 0.0167}, {"seed": 442, "count": null, "done": true, "steps": 21, "seconds": 1.499, "policy_seconds": 0.0062}, {"seed": 443, "count": null, "done": true, "steps": 39, "seconds": 1.921, "policy_seconds": 0.008}, {"seed": 444, "count": null, "done": true, "steps": 64, "seconds": 3.673, "policy_seconds": 0.0115}, {"seed": 445, "count": null, "done": true, "steps": 28, "seconds": 1.411, "policy_seconds": 0.0063}, {"seed": 446, "count": null, "done": true, "steps": 47, "seconds": 2.43, "policy_seconds": 0.0091}, {"seed": 447, "count": null, "done": true, "steps": 58, "seconds": 3.278, "policy_seconds": 0.0144}, {"seed": 448, "count": null, "done": true, "steps": 46, "seconds": 2.105, "policy_seconds": 0.013}, {"seed": 449, "count": null, "done": true, "steps": 59, "seconds": 2.668, "policy_seconds": 0.0092}, {"seed": 450, "count": null, "done": true, "steps": 28, "seconds": 1.036, "policy_seconds": 0.0043}, {"seed": 451, "count": null, "done": true, "steps": 22, "seconds": 1.289, "policy_seconds": 0.0038}, {"seed": 452, "count": null, "done": true, "steps": 72, "seconds": 3.399, "policy_seconds": 0.0146}, {"seed": 453, "count": null, "done": true, "steps": 80, "seconds": 3.774, "policy_seconds": 0.0217}, {"seed": 454, "count": null, "done": true, "steps": 65, "seconds": 3.389, "policy_seconds": 0.0182}, {"seed": 455, "count": null, "done": true, "steps": 69, "seconds": 3.622, "policy_seconds": 0.0139}, {"seed": 456, "count": null, "done": true, "steps": 49, "seconds": 2.705, "policy_seconds": 0.0108}, {"seed": 457, "count": null, "done": true, "steps": 28, "seconds": 1.362, "policy_seconds": 0.0057}, {"seed": 458, "count": null, "done": true, "steps": 41, "seconds": 1.646, "policy_seconds": 0.0079}, {"seed": 459, "count": null, "done": true, "steps": 51, "seconds": 3.049, "policy_seconds": 0.0139}, {"seed": 460, "count": null, "done": true, "steps": 29, "seconds": 1.275, "policy_seconds": 0.0056}, {"seed": 461, "count": null, "done": true, "steps": 34, "seconds": 2.365, "policy_seconds": 0.0088}, {"seed": 462, "count": null, "done": true, "steps": 91, "seconds": 6.208, "policy_seconds": 0.0226}, {"seed": 463, "count": null, "done": true, "steps": 66, "seconds": 4.128, "policy_seconds": 0.0195}, {"seed": 464, "count": null, "done": true, "steps": 27, "seconds": 1.599, "policy_seconds": 0.0044}, {"seed": 465, "count": null, "done": true, "steps": 29, "seconds": 1.292, "policy_seconds": 0.0048}, {"seed": 466, "count": null, "done": true, "steps": 75, "seconds": 4.193, "policy_seconds": 0.0158}, {"seed": 467, "count": null, "done": true, "steps": 25, "seconds": 1.395, "policy_seconds": 0.003}, {"seed": 468, "count": null, "done": true, "steps": 56, "seconds": 2.682, "policy_seconds": 0.0094}, {"seed": 469, "count": null, "done": true, "steps": 18, "seconds": 1.046, "policy_seconds": 0.0047}, {"seed": 470, "count": null, "done": true, "steps": 43, "seconds": 2.71, "policy_seconds": 0.0116}, {"seed": 471, "count": null, "done": true, "steps": 35, "seconds": 2.143, "policy_seconds": 0.006}, {"seed": 472, "count": null, "done": true, "steps": 38, "seconds": 2.49, "policy_seconds": 0.0082}, {"seed": 473, "count": null, "done": true, "steps": 22, "seconds": 1.129, "policy_seconds": 0.0056}, {"seed": 474, "count": null, "done": true, "steps": 27, "seconds": 1.465, "policy_seconds": 0.0069}, {"seed": 475, "count": null, "done": true, "steps": 82, "seconds": 3.961, "policy_seconds": 0.0169}, {"seed": 476, "count": null, "done": true, "steps": 78, "seconds": 3.562, "policy_seconds": 0.0263}, {"seed": 477, "count": null, "done": true, "steps": 71, "seconds": 3.244, "policy_seconds": 0.0165}, {"seed": 478, "count": null, "done": true, "steps": 19, "seconds": 0.601, "policy_seconds": 0.0046}, {"seed": 479, "count": null, "done": true, "steps": 87, "seconds": 4.73, "policy_seconds": 0.0233}, {"seed": 480, "count": null, "done": true, "steps": 104, "seconds": 6.969, "policy_seconds": 0.0279}, {"seed": 481, "count": null, "done": true, "steps": 42, "seconds": 2.745, "policy_seconds": 0.0144}, {"seed": 482, "count": null, "done": true, "steps": 22, "seconds": 1.242, "policy_seconds": 0.0035}, {"seed": 483, "count": null, "done": true, "steps": 21, "seconds": 0.936, "policy_seconds": 0.0062}, {"seed": 484, "count": null, "done": true, "steps": 67, "seconds": 3.124, "policy_seconds": 0.0196}, {"seed": 485, "count": null, "done": true, "steps": 18, "seconds": 0.83, "policy_seconds": 0.0066}, {"seed": 486, "count": null, "done": true, "steps": 24, "seconds": 0.909, "policy_seconds": 0.0059}, {"seed": 487, "count": null, "done": true, "steps": 26, "seconds": 1.885, "policy_seconds": 0.0053}, {"seed": 488, "count": null, "done": true, "steps": 92, "seconds": 6.673, "policy_seconds": 0.0264}, {"seed": 489, "count": null, "done": false, "steps": 1000, "seconds": 68.581, "policy_seconds": 0.1308, "trace": [[840, "place", "target_block", 0.5194, 0.4876], [880, "place", "target_block", 0.5194, 0.4876], [920, "place", "target_block", 0.5194, 0.4876], [960, "place", "target_block", 0.5194, 0.4876]], "state": {"obstruction0": {"x": 0.6125882863998413, "y": 0.10000099986791611, "width": 0.08571477979421616, "height": 0.09336432069540024}, "obstruction1": {"x": 0.8762147426605225, "y": 0.10100002586841583, "width": 0.07839120179414749, "height": 0.1896573305130005}, "target_block": {"x": 0.5144228339195251, "y": 0.21765734255313873, "width": 0.09879190474748611, "height": 0.06392852216959}, "target_surface": {"x": 0.5127172470092773, "y": 0.0, "width": 0.12958014011383057, "height": 0.10000000149011612}}}, {"seed": 490, "count": null, "done": true, "steps": 57, "seconds": 2.882, "policy_seconds": 0.0168}, {"seed": 491, "count": null, "done": true, "steps": 56, "seconds": 3.374, "policy_seconds": 0.0134}, {"seed": 492, "count": null, "done": true, "steps": 70, "seconds": 5.693, "policy_seconds": 0.0211}, {"seed": 493, "count": null, "done": true, "steps": 48, "seconds": 3.561, "policy_seconds": 0.011}, {"seed": 494, "count": null, "done": true, "steps": 45, "seconds": 3.059, "policy_seconds": 0.0118}, {"seed": 495, "count": null, "done": true, "steps": 27, "seconds": 1.9, "policy_seconds": 0.0062}, {"seed": 496, "count": null, "done": true, "steps": 33, "seconds": 2.182, "policy_seconds": 0.0071}, {"seed": 497, "count": null, "done": true, "steps": 25, "seconds": 1.603, "policy_seconds": 0.006}, {"seed": 498, "count": null, "done": true, "steps": 61, "seconds": 3.971, "policy_seconds": 0.0136}, {"seed": 499, "count": null, "done": true, "steps": 109, "seconds": 8.189, "policy_seconds": 0.0262}, {"seed": 500, "count": null, "done": true, "steps": 18, "seconds": 0.801, "policy_seconds": 0.0059}, {"seed": 501, "count": null, "done": true, "steps": 64, "seconds": 4.609, "policy_seconds": 0.0173}, {"seed": 502, "count": null, "done": true, "steps": 26, "seconds": 1.133, "policy_seconds": 0.0046}, {"seed": 503, "count": null, "done": true, "steps": 24, "seconds": 1.514, "policy_seconds": 0.0057}, {"seed": 504, "count": null, "done": true, "steps": 80, "seconds": 5.578, "policy_seconds": 0.0217}, {"seed": 505, "count": null, "done": true, "steps": 84, "seconds": 6.865, "policy_seconds": 0.0238}, {"seed": 506, "count": null, "done": true, "steps": 50, "seconds": 2.961, "policy_seconds": 0.015}, {"seed": 507, "count": null, "done": true, "steps": 78, "seconds": 6.8, "policy_seconds": 0.0238}, {"seed": 508, "count": null, "done": true, "steps": 49, "seconds": 2.962, "policy_seconds": 0.0118}, {"seed": 509, "count": null, "done": true, "steps": 68, "seconds": 5.428, "policy_seconds": 0.0108}, {"seed": 510, "count": null, "done": true, "steps": 27, "seconds": 2.033, "policy_seconds": 0.0058}, {"seed": 511, "count": null, "done": true, "steps": 70, "seconds": 7.193, "policy_seconds": 0.0255}, {"seed": 512, "count": null, "done": true, "steps": 26, "seconds": 2.622, "policy_seconds": 0.0076}, {"seed": 513, "count": null, "done": true, "steps": 46, "seconds": 5.205, "policy_seconds": 0.0077}, {"seed": 514, "count": null, "done": true, "steps": 74, "seconds": 7.918, "policy_seconds": 0.0177}, {"seed": 515, "count": null, "done": true, "steps": 41, "seconds": 2.295, "policy_seconds": 0.0064}, {"seed": 516, "count": null, "done": true, "steps": 34, "seconds": 2.221, "policy_seconds": 0.0062}, {"seed": 517, "count": null, "done": true, "steps": 71, "seconds": 6.197, "policy_seconds": 0.0166}, {"seed": 518, "count": null, "done": true, "steps": 41, "seconds": 3.169, "policy_seconds": 0.0085}, {"seed": 519, "count": null, "done": true, "steps": 28, "seconds": 2.886, "policy_seconds": 0.009}, {"seed": 520, "count": null, "done": true, "steps": 21, "seconds": 1.794, "policy_seconds": 0.0057}, {"seed": 521, "count": null, "done": true, "steps": 35, "seconds": 2.119, "policy_seconds": 0.0057}, {"seed": 522, "count": null, "done": true, "steps": 53, "seconds": 4.591, "policy_seconds": 0.0174}, {"seed": 523, "count": null, "done": true, "steps": 41, "seconds": 3.278, "policy_seconds": 0.0082}, {"seed": 524, "count": null, "done": true, "steps": 20, "seconds": 1.658, "policy_seconds": 0.0045}, {"seed": 525, "count": null, "done": true, "steps": 80, "seconds": 8.66, "policy_seconds": 0.0214}, {"seed": 526, "count": null, "done": true, "steps": 33, "seconds": 2.846, "policy_seconds": 0.0078}, {"seed": 527, "count": null, "done": true, "steps": 59, "seconds": 6.754, "policy_seconds": 0.0172}, {"seed": 528, "count": null, "done": true, "steps": 17, "seconds": 1.508, "policy_seconds": 0.0066}, {"seed": 529, "count": null, "done": true, "steps": 23, "seconds": 1.72, "policy_seconds": 0.0065}, {"seed": 530, "count": null, "done": true, "steps": 30, "seconds": 2.145, "policy_seconds": 0.0068}, {"seed": 531, "count": null, "done": true, "steps": 51, "seconds": 4.775, "policy_seconds": 0.0143}, {"seed": 532, "count": null, "done": true, "steps": 67, "seconds": 7.92, "policy_seconds": 0.0197}, {"seed": 533, "count": null, "done": true, "steps": 31, "seconds": 2.95, "policy_seconds": 0.0089}, {"seed": 534, "count": null, "done": true, "steps": 78, "seconds": 8.322, "policy_seconds": 0.0232}, {"seed": 535, "count": null, "done": true, "steps": 21, "seconds": 1.757, "policy_seconds": 0.0032}, {"seed": 536, "count": null, "done": true, "steps": 90, "seconds": 8.817, "policy_seconds": 0.0237}, {"seed": 537, "count": null, "done": true, "steps": 22, "seconds": 1.384, "policy_seconds": 0.0037}, {"seed": 538, "count": null, "done": true, "steps": 29, "seconds": 1.603, "policy_seconds": 0.0082}, {"seed": 539, "count": null, "done": true, "steps": 24, "seconds": 1.982, "policy_seconds": 0.0058}, {"seed": 540, "count": null, "done": true, "steps": 20, "seconds": 1.135, "policy_seconds": 0.004}, {"seed": 541, "count": null, "done": true, "steps": 72, "seconds": 6.231, "policy_seconds": 0.0197}, {"seed": 542, "count": null, "done": true, "steps": 85, "seconds": 8.268, "policy_seconds": 0.0173}, {"seed": 543, "count": null, "done": true, "steps": 64, "seconds": 7.521, "policy_seconds": 0.0158}, {"seed": 544, "count": null, "done": true, "steps": 27, "seconds": 2.513, "policy_seconds": 0.0093}, {"seed": 545, "count": null, "done": true, "steps": 80, "seconds": 6.799, "policy_seconds": 0.0168}, {"seed": 546, "count": null, "done": true, "steps": 29, "seconds": 1.909, "policy_seconds": 0.0054}, {"seed": 547, "count": null, "done": true, "steps": 24, "seconds": 1.687, "policy_seconds": 0.0067}, {"seed": 548, "count": null, "done": true, "steps": 44, "seconds": 4.032, "policy_seconds": 0.0125}, {"seed": 549, "count": null, "done": true, "steps": 53, "seconds": 4.361, "policy_seconds": 0.0162}, {"seed": 550, "count": null, "done": true, "steps": 95, "seconds": 10.104, "policy_seconds": 0.0229}, {"seed": 551, "count": null, "done": true, "steps": 33, "seconds": 2.225, "policy_seconds": 0.008}, {"seed": 552, "count": null, "done": true, "steps": 30, "seconds": 2.601, "policy_seconds": 0.006}, {"seed": 553, "count": null, "done": true, "steps": 85, "seconds": 6.732, "policy_seconds": 0.0212}, {"seed": 554, "count": null, "done": true, "steps": 19, "seconds": 1.226, "policy_seconds": 0.0038}, {"seed": 555, "count": null, "done": true, "steps": 56, "seconds": 4.647, "policy_seconds": 0.0162}, {"seed": 556, "count": null, "done": true, "steps": 56, "seconds": 4.327, "policy_seconds": 0.0134}, {"seed": 557, "count": null, "done": true, "steps": 52, "seconds": 3.75, "policy_seconds": 0.012}, {"seed": 558, "count": null, "done": true, "steps": 28, "seconds": 2.106, "policy_seconds": 0.0058}, {"seed": 559, "count": null, "done": true, "steps": 27, "seconds": 1.73, "policy_seconds": 0.0062}, {"seed": 560, "count": null, "done": true, "steps": 77, "seconds": 7.65, "policy_seconds": 0.021}, {"seed": 561, "count": null, "done": true, "steps": 19, "seconds": 1.583, "policy_seconds": 0.0037}, {"seed": 562, "count": null, "done": true, "steps": 30, "seconds": 2.681, "policy_seconds": 0.0071}, {"seed": 563, "count": null, "done": true, "steps": 30, "seconds": 2.934, "policy_seconds": 0.0073}, {"seed": 564, "count": null, "done": true, "steps": 19, "seconds": 1.269, "policy_seconds": 0.0055}, {"seed": 565, "count": null, "done": true, "steps": 76, "seconds": 6.76, "policy_seconds": 0.0228}, {"seed": 566, "count": null, "done": true, "steps": 60, "seconds": 5.931, "policy_seconds": 0.0171}, {"seed": 567, "count": null, "done": true, "steps": 26, "seconds": 2.465, "policy_seconds": 0.0065}, {"seed": 568, "count": null, "done": true, "steps": 72, "seconds": 5.814, "policy_seconds": 0.0137}, {"seed": 569, "count": null, "done": true, "steps": 23, "seconds": 1.568, "policy_seconds": 0.006}, {"seed": 570, "count": null, "done": true, "steps": 36, "seconds": 1.629, "policy_seconds": 0.006}, {"seed": 571, "count": null, "done": true, "steps": 47, "seconds": 3.518, "policy_seconds": 0.0146}, {"seed": 572, "count": null, "done": true, "steps": 48, "seconds": 3.376, "policy_seconds": 0.0115}, {"seed": 573, "count": null, "done": true, "steps": 61, "seconds": 7.562, "policy_seconds": 0.0166}, {"seed": 574, "count": null, "done": true, "steps": 22, "seconds": 1.992, "policy_seconds": 0.0032}, {"seed": 575, "count": null, "done": true, "steps": 58, "seconds": 6.713, "policy_seconds": 0.016}, {"seed": 576, "count": null, "done": true, "steps": 36, "seconds": 2.557, "policy_seconds": 0.0084}, {"seed": 577, "count": null, "done": true, "steps": 69, "seconds": 5.597, "policy_seconds": 0.0115}, {"seed": 578, "count": null, "done": true, "steps": 76, "seconds": 8.971, "policy_seconds": 0.0178}, {"seed": 579, "count": null, "done": true, "steps": 77, "seconds": 7.706, "policy_seconds": 0.0189}, {"seed": 580, "count": null, "done": true, "steps": 33, "seconds": 1.67, "policy_seconds": 0.0064}, {"seed": 581, "count": null, "done": true, "steps": 19, "seconds": 0.955, "policy_seconds": 0.003}, {"seed": 582, "count": null, "done": true, "steps": 61, "seconds": 5.944, "policy_seconds": 0.0185}, {"seed": 583, "count": null, "done": true, "steps": 30, "seconds": 2.342, "policy_seconds": 0.006}, {"seed": 584, "count": null, "done": true, "steps": 33, "seconds": 3.379, "policy_seconds": 0.0071}, {"seed": 585, "count": null, "done": true, "steps": 29, "seconds": 2.543, "policy_seconds": 0.0057}, {"seed": 586, "count": null, "done": true, "steps": 54, "seconds": 6.099, "policy_seconds": 0.0173}, {"seed": 587, "count": null, "done": true, "steps": 47, "seconds": 4.683, "policy_seconds": 0.0143}, {"seed": 588, "count": null, "done": true, "steps": 44, "seconds": 3.304, "policy_seconds": 0.0095}, {"seed": 589, "count": null, "done": true, "steps": 31, "seconds": 2.929, "policy_seconds": 0.009}, {"seed": 590, "count": null, "done": true, "steps": 86, "seconds": 7.0, "policy_seconds": 0.0177}, {"seed": 591, "count": null, "done": true, "steps": 24, "seconds": 1.679, "policy_seconds": 0.005}, {"seed": 592, "count": null, "done": true, "steps": 27, "seconds": 2.331, "policy_seconds": 0.0085}, {"seed": 593, "count": null, "done": true, "steps": 62, "seconds": 6.308, "policy_seconds": 0.0163}, {"seed": 594, "count": null, "done": true, "steps": 74, "seconds": 6.277, "policy_seconds": 0.016}, {"seed": 595, "count": null, "done": true, "steps": 120, "seconds": 14.97, "policy_seconds": 0.0347}, {"seed": 596, "count": null, "done": true, "steps": 62, "seconds": 7.749, "policy_seconds": 0.0128}, {"seed": 597, "count": null, "done": true, "steps": 83, "seconds": 10.632, "policy_seconds": 0.0218}, {"seed": 598, "count": null, "done": true, "steps": 52, "seconds": 4.227, "policy_seconds": 0.0108}, {"seed": 599, "count": null, "done": true, "steps": 53, "seconds": 6.117, "policy_seconds": 0.0101}, {"seed": 600, "count": null, "done": true, "steps": 50, "seconds": 3.697, "policy_seconds": 0.0072}, {"seed": 601, "count": null, "done": true, "steps": 30, "seconds": 2.597, "policy_seconds": 0.0051}, {"seed": 602, "count": null, "done": true, "steps": 21, "seconds": 1.684, "policy_seconds": 0.006}, {"seed": 603, "count": null, "done": true, "steps": 20, "seconds": 1.557, "policy_seconds": 0.0054}, {"seed": 604, "count": null, "done": true, "steps": 18, "seconds": 1.007, "policy_seconds": 0.003}, {"seed": 605, "count": null, "done": true, "steps": 26, "seconds": 1.007, "policy_seconds": 0.0051}, {"seed": 606, "count": null, "done": true, "steps": 93, "seconds": 8.096, "policy_seconds": 0.0291}, {"seed": 607, "count": null, "done": true, "steps": 58, "seconds": 5.712, "policy_seconds": 0.015}, {"seed": 608, "count": null, "done": true, "steps": 34, "seconds": 2.901, "policy_seconds": 0.0083}, {"seed": 609, "count": null, "done": true, "steps": 62, "seconds": 6.314, "policy_seconds": 0.0153}, {"seed": 610, "count": null, "done": true, "steps": 35, "seconds": 3.007, "policy_seconds": 0.0084}, {"seed": 611, "count": null, "done": true, "steps": 61, "seconds": 5.374, "policy_seconds": 0.0167}, {"seed": 612, "count": null, "done": true, "steps": 116, "seconds": 12.204, "policy_seconds": 0.0328}, {"seed": 613, "count": null, "done": true, "steps": 56, "seconds": 4.052, "policy_seconds": 0.0131}, {"seed": 614, "count": null, "done": true, "steps": 68, "seconds": 7.261, "policy_seconds": 0.0217}, {"seed": 615, "count": null, "done": true, "steps": 96, "seconds": 11.975, "policy_seconds": 0.0254}, {"seed": 616, "count": null, "done": true, "steps": 55, "seconds": 5.594, "policy_seconds": 0.0182}, {"seed": 617, "count": null, "done": true, "steps": 62, "seconds": 6.25, "policy_seconds": 0.0172}, {"seed": 618, "count": null, "done": true, "steps": 21, "seconds": 2.369, "policy_seconds": 0.0059}, {"seed": 619, "count": null, "done": true, "steps": 19, "seconds": 1.521, "policy_seconds": 0.008}, {"seed": 620, "count": null, "done": true, "steps": 53, "seconds": 4.694, "policy_seconds": 0.0117}, {"seed": 621, "count": null, "done": true, "steps": 22, "seconds": 1.604, "policy_seconds": 0.0056}, {"seed": 622, "count": null, "done": true, "steps": 60, "seconds": 4.729, "policy_seconds": 0.0162}, {"seed": 623, "count": null, "done": true, "steps": 19, "seconds": 1.827, "policy_seconds": 0.0102}, {"seed": 624, "count": null, "done": true, "steps": 44, "seconds": 2.989, "policy_seconds": 0.0118}, {"seed": 625, "count": null, "done": true, "steps": 53, "seconds": 4.703, "policy_seconds": 0.0107}, {"seed": 626, "count": null, "done": true, "steps": 54, "seconds": 5.966, "policy_seconds": 0.014}, {"seed": 627, "count": null, "done": false, "steps": 1000, "seconds": 128.098, "policy_seconds": 0.1434, "trace": [[840, "down", "target_block", 0.5233, 0.5412], [880, "down", "target_block", 0.5233, 0.3912], [920, "lift", "target_block", 0.5233, 0.5912], [960, "down", "target_block", 0.5233, 0.3912]], "state": {"obstruction0": {"x": 1.070956826210022, "y": 0.10000099986791611, "width": 0.10327284038066864, "height": 0.06639733165502548}, "obstruction1": {"x": 0.5642479658126831, "y": 0.10099996626377106, "width": 0.1490718424320221, "height": 0.1984524130821228}, "target_block": {"x": 0.4953683614730835, "y": 0.10000099986791611, "width": 0.055879540741443634, "height": 0.058782048523426056}, "target_surface": {"x": 0.8293163180351257, "y": 0.0, "width": 0.09297315031290054, "height": 0.10000000149011612}}}, {"seed": 628, "count": null, "done": true, "steps": 36, "seconds": 2.568, "policy_seconds": 0.0076}, {"seed": 629, "count": null, "done": true, "steps": 64, "seconds": 6.481, "policy_seconds": 0.0185}, {"seed": 630, "count": null, "done": true, "steps": 76, "seconds": 6.277, "policy_seconds": 0.0153}, {"seed": 631, "count": null, "done": true, "steps": 30, "seconds": 2.02, "policy_seconds": 0.0059}, {"seed": 632, "count": null, "done": true, "steps": 31, "seconds": 2.206, "policy_seconds": 0.0077}, {"seed": 633, "count": null, "done": true, "steps": 26, "seconds": 2.125, "policy_seconds": 0.0072}, {"seed": 634, "count": null, "done": true, "steps": 50, "seconds": 4.805, "policy_seconds": 0.0158}, {"seed": 635, "count": null, "done": true, "steps": 120, "seconds": 13.925, "policy_seconds": 0.0316}, {"seed": 636, "count": null, "done": true, "steps": 27, "seconds": 2.331, "policy_seconds": 0.0072}, {"seed": 637, "count": null, "done": true, "steps": 16, "seconds": 1.091, "policy_seconds": 0.0049}, {"seed": 638, "count": null, "done": true, "steps": 23, "seconds": 2.285, "policy_seconds": 0.0099}, {"seed": 639, "count": null, "done": true, "steps": 97, "seconds": 10.289, "policy_seconds": 0.0294}, {"seed": 640, "count": null, "done": true, "steps": 79, "seconds": 9.182, "policy_seconds": 0.0232}, {"seed": 641, "count": null, "done": true, "steps": 103, "seconds": 12.491, "policy_seconds": 0.0278}, {"seed": 642, "count": null, "done": true, "steps": 21, "seconds": 1.425, "policy_seconds": 0.0055}, {"seed": 643, "count": null, "done": true, "steps": 44, "seconds": 3.118, "policy_seconds": 0.0089}, {"seed": 644, "count": null, "done": true, "steps": 45, "seconds": 3.901, "policy_seconds": 0.0129}, {"seed": 645, "count": null, "done": true, "steps": 22, "seconds": 1.731, "policy_seconds": 0.0064}, {"seed": 646, "count": null, "done": true, "steps": 87, "seconds": 6.717, "policy_seconds": 0.0197}, {"seed": 647, "count": null, "done": true, "steps": 34, "seconds": 2.087, "policy_seconds": 0.0059}, {"seed": 648, "count": null, "done": true, "steps": 32, "seconds": 2.386, "policy_seconds": 0.0083}, {"seed": 649, "count": null, "done": true, "steps": 78, "seconds": 5.822, "policy_seconds": 0.0181}, {"seed": 650, "count": null, "done": true, "steps": 42, "seconds": 4.109, "policy_seconds": 0.0171}, {"seed": 651, "count": null, "done": true, "steps": 27, "seconds": 2.664, "policy_seconds": 0.0067}, {"seed": 652, "count": null, "done": true, "steps": 20, "seconds": 1.583, "policy_seconds": 0.006}, {"seed": 653, "count": null, "done": true, "steps": 15, "seconds": 1.19, "policy_seconds": 0.0027}, {"seed": 654, "count": null, "done": true, "steps": 26, "seconds": 1.638, "policy_seconds": 0.0062}, {"seed": 655, "count": null, "done": true, "steps": 27, "seconds": 1.901, "policy_seconds": 0.0036}, {"seed": 656, "count": null, "done": true, "steps": 16, "seconds": 1.106, "policy_seconds": 0.0031}, {"seed": 657, "count": null, "done": true, "steps": 21, "seconds": 1.21, "policy_seconds": 0.0041}, {"seed": 658, "count": null, "done": true, "steps": 59, "seconds": 4.773, "policy_seconds": 0.0132}, {"seed": 659, "count": null, "done": true, "steps": 59, "seconds": 6.21, "policy_seconds": 0.0123}, {"seed": 660, "count": null, "done": true, "steps": 56, "seconds": 4.249, "policy_seconds": 0.0118}, {"seed": 661, "count": null, "done": true, "steps": 37, "seconds": 2.435, "policy_seconds": 0.0071}, {"seed": 662, "count": null, "done": true, "steps": 27, "seconds": 2.253, "policy_seconds": 0.0075}, {"seed": 663, "count": null, "done": true, "steps": 96, "seconds": 9.953, "policy_seconds": 0.0244}, {"seed": 664, "count": null, "done": true, "steps": 42, "seconds": 3.645, "policy_seconds": 0.01}, {"seed": 665, "count": null, "done": true, "steps": 63, "seconds": 6.487, "policy_seconds": 0.0255}, {"seed": 666, "count": null, "done": true, "steps": 49, "seconds": 4.437, "policy_seconds": 0.0096}, {"seed": 667, "count": null, "done": true, "steps": 39, "seconds": 3.483, "policy_seconds": 0.0075}, {"seed": 668, "count": null, "done": true, "steps": 79, "seconds": 5.78, "policy_seconds": 0.0133}, {"seed": 669, "count": null, "done": true, "steps": 77, "seconds": 7.813, "policy_seconds": 0.0229}, {"seed": 670, "count": null, "done": true, "steps": 27, "seconds": 1.671, "policy_seconds": 0.006}, {"seed": 671, "count": null, "done": true, "steps": 29, "seconds": 2.399, "policy_seconds": 0.0042}, {"seed": 672, "count": null, "done": true, "steps": 62, "seconds": 9.029, "policy_seconds": 0.0183}, {"seed": 673, "count": null, "done": true, "steps": 75, "seconds": 10.436, "policy_seconds": 0.0163}, {"seed": 674, "count": null, "done": true, "steps": 50, "seconds": 7.77, "policy_seconds": 0.0125}, {"seed": 675, "count": null, "done": true, "steps": 46, "seconds": 5.414, "policy_seconds": 0.013}, {"seed": 676, "count": null, "done": true, "steps": 24, "seconds": 1.944, "policy_seconds": 0.0035}, {"seed": 677, "count": null, "done": true, "steps": 35, "seconds": 2.765, "policy_seconds": 0.0075}, {"seed": 678, "count": null, "done": true, "steps": 26, "seconds": 2.579, "policy_seconds": 0.0044}, {"seed": 679, "count": null, "done": true, "steps": 60, "seconds": 5.272, "policy_seconds": 0.0137}, {"seed": 680, "count": null, "done": true, "steps": 88, "seconds": 11.61, "policy_seconds": 0.021}, {"seed": 681, "count": null, "done": true, "steps": 78, "seconds": 11.326, "policy_seconds": 0.0209}, {"seed": 682, "count": null, "done": true, "steps": 52, "seconds": 7.207, "policy_seconds": 0.0143}, {"seed": 683, "count": null, "done": true, "steps": 71, "seconds": 7.964, "policy_seconds": 0.0179}, {"seed": 684, "count": null, "done": true, "steps": 34, "seconds": 2.734, "policy_seconds": 0.0076}, {"seed": 685, "count": null, "done": true, "steps": 96, "seconds": 11.725, "policy_seconds": 0.0275}, {"seed": 686, "count": null, "done": true, "steps": 69, "seconds": 9.362, "policy_seconds": 0.0183}, {"seed": 687, "count": null, "done": true, "steps": 43, "seconds": 6.001, "policy_seconds": 0.0146}, {"seed": 688, "count": null, "done": true, "steps": 24, "seconds": 1.502, "policy_seconds": 0.0053}, {"seed": 689, "count": null, "done": true, "steps": 31, "seconds": 2.18, "policy_seconds": 0.0074}, {"seed": 690, "count": null, "done": true, "steps": 22, "seconds": 1.981, "policy_seconds": 0.0041}, {"seed": 691, "count": null, "done": true, "steps": 17, "seconds": 1.372, "policy_seconds": 0.0051}, {"seed": 692, "count": null, "done": true, "steps": 57, "seconds": 4.444, "policy_seconds": 0.0184}, {"seed": 693, "count": null, "done": true, "steps": 61, "seconds": 5.634, "policy_seconds": 0.0163}, {"seed": 694, "count": null, "done": true, "steps": 51, "seconds": 5.187, "policy_seconds": 0.0121}, {"seed": 695, "count": null, "done": true, "steps": 38, "seconds": 2.398, "policy_seconds": 0.0082}, {"seed": 696, "count": null, "done": true, "steps": 78, "seconds": 7.236, "policy_seconds": 0.0188}, {"seed": 697, "count": null, "done": true, "steps": 86, "seconds": 10.403, "policy_seconds": 0.0262}, {"seed": 698, "count": null, "done": true, "steps": 67, "seconds": 7.242, "policy_seconds": 0.0214}, {"seed": 699, "count": null, "done": true, "steps": 74, "seconds": 7.816, "policy_seconds": 0.0214}, {"seed": 700, "count": null, "done": true, "steps": 17, "seconds": 1.372, "policy_seconds": 0.0037}, {"seed": 701, "count": null, "done": true, "steps": 17, "seconds": 1.336, "policy_seconds": 0.0063}, {"seed": 702, "count": null, "done": true, "steps": 32, "seconds": 1.439, "policy_seconds": 0.004}, {"seed": 703, "count": null, "done": true, "steps": 78, "seconds": 8.448, "policy_seconds": 0.0254}, {"seed": 704, "count": null, "done": true, "steps": 43, "seconds": 3.885, "policy_seconds": 0.012}, {"seed": 705, "count": null, "done": true, "steps": 36, "seconds": 2.898, "policy_seconds": 0.0071}, {"seed": 706, "count": null, "done": true, "steps": 56, "seconds": 7.25, "policy_seconds": 0.0092}, {"seed": 707, "count": null, "done": true, "steps": 30, "seconds": 2.325, "policy_seconds": 0.0086}, {"seed": 708, "count": null, "done": true, "steps": 39, "seconds": 3.999, "policy_seconds": 0.0141}, {"seed": 709, "count": null, "done": true, "steps": 42, "seconds": 4.802, "policy_seconds": 0.0118}, {"seed": 710, "count": null, "done": true, "steps": 21, "seconds": 2.012, "policy_seconds": 0.0083}, {"seed": 711, "count": null, "done": true, "steps": 44, "seconds": 3.513, "policy_seconds": 0.0083}, {"seed": 712, "count": null, "done": true, "steps": 29, "seconds": 1.904, "policy_seconds": 0.0075}, {"seed": 713, "count": null, "done": true, "steps": 64, "seconds": 4.942, "policy_seconds": 0.0234}, {"seed": 714, "count": null, "done": true, "steps": 105, "seconds": 8.462, "policy_seconds": 0.028}, {"seed": 715, "count": null, "done": true, "steps": 45, "seconds": 3.262, "policy_seconds": 0.0107}, {"seed": 716, "count": null, "done": true, "steps": 46, "seconds": 3.598, "policy_seconds": 0.0112}, {"seed": 717, "count": null, "done": true, "steps": 22, "seconds": 2.083, "policy_seconds": 0.0055}, {"seed": 718, "count": null, "done": true, "steps": 35, "seconds": 3.599, "policy_seconds": 0.0109}, {"seed": 719, "count": null, "done": true, "steps": 61, "seconds": 5.103, "policy_seconds": 0.0172}, {"seed": 720, "count": null, "done": true, "steps": 72, "seconds": 6.899, "policy_seconds": 0.0206}, {"seed": 721, "count": null, "done": true, "steps": 47, "seconds": 3.469, "policy_seconds": 0.0094}, {"seed": 722, "count": null, "done": true, "steps": 20, "seconds": 1.71, "policy_seconds": 0.0045}, {"seed": 723, "count": null, "done": true, "steps": 24, "seconds": 2.602, "policy_seconds": 0.0083}, {"seed": 724, "count": null, "done": true, "steps": 22, "seconds": 1.669, "policy_seconds": 0.0063}, {"seed": 725, "count": null, "done": true, "steps": 28, "seconds": 1.217, "policy_seconds": 0.0063}, {"seed": 726, "count": null, "done": true, "steps": 39, "seconds": 2.565, "policy_seconds": 0.0068}, {"seed": 727, "count": null, "done": true, "steps": 22, "seconds": 1.578, "policy_seconds": 0.0062}, {"seed": 728, "count": null, "done": true, "steps": 59, "seconds": 5.471, "policy_seconds": 0.0183}, {"seed": 729, "count": null, "done": true, "steps": 30, "seconds": 1.475, "policy_seconds": 0.0071}, {"seed": 730, "count": null, "done": true, "steps": 53, "seconds": 4.228, "policy_seconds": 0.0143}, {"seed": 731, "count": null, "done": true, "steps": 42, "seconds": 2.803, "policy_seconds": 0.0129}, {"seed": 732, "count": null, "done": true, "steps": 35, "seconds": 2.143, "policy_seconds": 0.0086}, {"seed": 733, "count": null, "done": true, "steps": 90, "seconds": 7.488, "policy_seconds": 0.0255}, {"seed": 734, "count": null, "done": true, "steps": 19, "seconds": 0.937, "policy_seconds": 0.0046}, {"seed": 735, "count": null, "done": true, "steps": 26, "seconds": 1.424, "policy_seconds": 0.0034}, {"seed": 736, "count": null, "done": true, "steps": 18, "seconds": 0.764, "policy_seconds": 0.0039}, {"seed": 737, "count": null, "done": true, "steps": 25, "seconds": 1.871, "policy_seconds": 0.0049}, {"seed": 738, "count": null, "done": true, "steps": 48, "seconds": 4.695, "policy_seconds": 0.0123}, {"seed": 739, "count": null, "done": true, "steps": 72, "seconds": 8.176, "policy_seconds": 0.0185}, {"seed": 740, "count": null, "done": true, "steps": 44, "seconds": 3.375, "policy_seconds": 0.008}, {"seed": 741, "count": null, "done": true, "steps": 44, "seconds": 4.529, "policy_seconds": 0.0116}, {"seed": 742, "count": null, "done": true, "steps": 52, "seconds": 4.463, "policy_seconds": 0.0173}, {"seed": 743, "count": null, "done": true, "steps": 42, "seconds": 3.836, "policy_seconds": 0.014}, {"seed": 744, "count": null, "done": true, "steps": 62, "seconds": 4.733, "policy_seconds": 0.015}, {"seed": 745, "count": null, "done": true, "steps": 63, "seconds": 5.348, "policy_seconds": 0.0139}, {"seed": 746, "count": null, "done": true, "steps": 73, "seconds": 5.531, "policy_seconds": 0.0158}, {"seed": 747, "count": null, "done": true, "steps": 29, "seconds": 1.801, "policy_seconds": 0.0069}, {"seed": 748, "count": null, "done": true, "steps": 63, "seconds": 3.343, "policy_seconds": 0.0159}, {"seed": 749, "count": null, "done": true, "steps": 32, "seconds": 1.471, "policy_seconds": 0.0079}, {"seed": 750, "count": null, "done": true, "steps": 38, "seconds": 2.24, "policy_seconds": 0.012}, {"seed": 751, "count": null, "done": true, "steps": 65, "seconds": 5.443, "policy_seconds": 0.0165}, {"seed": 752, "count": null, "done": true, "steps": 63, "seconds": 4.973, "policy_seconds": 0.0172}, {"seed": 753, "count": null, "done": true, "steps": 24, "seconds": 1.768, "policy_seconds": 0.0032}, {"seed": 754, "count": null, "done": true, "steps": 71, "seconds": 4.939, "policy_seconds": 0.0138}, {"seed": 755, "count": null, "done": true, "steps": 61, "seconds": 4.786, "policy_seconds": 0.0114}, {"seed": 756, "count": null, "done": true, "steps": 45, "seconds": 3.116, "policy_seconds": 0.0098}, {"seed": 757, "count": null, "done": true, "steps": 101, "seconds": 9.264, "policy_seconds": 0.021}, {"seed": 758, "count": null, "done": true, "steps": 18, "seconds": 1.504, "policy_seconds": 0.0048}, {"seed": 759, "count": null, "done": true, "steps": 70, "seconds": 6.622, "policy_seconds": 0.0237}, {"seed": 760, "count": null, "done": true, "steps": 36, "seconds": 2.524, "policy_seconds": 0.007}, {"seed": 761, "count": null, "done": true, "steps": 56, "seconds": 4.755, "policy_seconds": 0.0155}, {"seed": 762, "count": null, "done": true, "steps": 30, "seconds": 1.619, "policy_seconds": 0.0077}, {"seed": 763, "count": null, "done": true, "steps": 31, "seconds": 2.085, "policy_seconds": 0.008}, {"seed": 764, "count": null, "done": true, "steps": 87, "seconds": 8.732, "policy_seconds": 0.0187}, {"seed": 765, "count": null, "done": true, "steps": 117, "seconds": 11.215, "policy_seconds": 0.0255}, {"seed": 766, "count": null, "done": true, "steps": 89, "seconds": 8.35, "policy_seconds": 0.0168}, {"seed": 767, "count": null, "done": true, "steps": 34, "seconds": 3.251, "policy_seconds": 0.0055}, {"seed": 768, "count": null, "done": true, "steps": 111, "seconds": 6.442, "policy_seconds": 0.0237}, {"seed": 769, "count": null, "done": true, "steps": 63, "seconds": 3.679, "policy_seconds": 0.0155}, {"seed": 770, "count": null, "done": true, "steps": 74, "seconds": 4.029, "policy_seconds": 0.0175}, {"seed": 771, "count": null, "done": true, "steps": 33, "seconds": 1.607, "policy_seconds": 0.0074}, {"seed": 772, "count": null, "done": true, "steps": 19, "seconds": 0.486, "policy_seconds": 0.0026}, {"seed": 773, "count": null, "done": true, "steps": 71, "seconds": 2.033, "policy_seconds": 0.0156}, {"seed": 774, "count": null, "done": true, "steps": 57, "seconds": 1.595, "policy_seconds": 0.0113}, {"seed": 775, "count": null, "done": true, "steps": 81, "seconds": 3.25, "policy_seconds": 0.021}, {"seed": 776, "count": null, "done": true, "steps": 101, "seconds": 4.108, "policy_seconds": 0.0204}, {"seed": 777, "count": null, "done": true, "steps": 54, "seconds": 2.065, "policy_seconds": 0.013}, {"seed": 778, "count": null, "done": true, "steps": 84, "seconds": 2.919, "policy_seconds": 0.0177}, {"seed": 779, "count": null, "done": true, "steps": 66, "seconds": 2.148, "policy_seconds": 0.0105}, {"seed": 780, "count": null, "done": true, "steps": 68, "seconds": 2.346, "policy_seconds": 0.0169}, {"seed": 781, "count": null, "done": true, "steps": 91, "seconds": 5.223, "policy_seconds": 0.0179}, {"seed": 782, "count": null, "done": true, "steps": 43, "seconds": 1.287, "policy_seconds": 0.0053}, {"seed": 783, "count": null, "done": true, "steps": 66, "seconds": 5.248, "policy_seconds": 0.0159}, {"seed": 784, "count": null, "done": true, "steps": 80, "seconds": 7.92, "policy_seconds": 0.0242}, {"seed": 785, "count": null, "done": true, "steps": 71, "seconds": 7.351, "policy_seconds": 0.0247}, {"seed": 786, "count": null, "done": true, "steps": 22, "seconds": 1.395, "policy_seconds": 0.0059}, {"seed": 787, "count": null, "done": true, "steps": 95, "seconds": 10.129, "policy_seconds": 0.0248}, {"seed": 788, "count": null, "done": true, "steps": 49, "seconds": 4.437, "policy_seconds": 0.0169}, {"seed": 789, "count": null, "done": true, "steps": 87, "seconds": 5.681, "policy_seconds": 0.0202}, {"seed": 790, "count": null, "done": true, "steps": 38, "seconds": 2.26, "policy_seconds": 0.0072}, {"seed": 791, "count": null, "done": true, "steps": 33, "seconds": 1.742, "policy_seconds": 0.0068}, {"seed": 792, "count": null, "done": true, "steps": 27, "seconds": 3.18, "policy_seconds": 0.0047}, {"seed": 793, "count": null, "done": true, "steps": 56, "seconds": 5.407, "policy_seconds": 0.0196}, {"seed": 794, "count": null, "done": true, "steps": 97, "seconds": 10.644, "policy_seconds": 0.025}, {"seed": 795, "count": null, "done": true, "steps": 86, "seconds": 8.255, "policy_seconds": 0.0239}, {"seed": 796, "count": null, "done": true, "steps": 18, "seconds": 1.397, "policy_seconds": 0.0026}, {"seed": 797, "count": null, "done": true, "steps": 31, "seconds": 2.365, "policy_seconds": 0.0054}, {"seed": 798, "count": null, "done": true, "steps": 58, "seconds": 3.844, "policy_seconds": 0.0163}, {"seed": 799, "count": null, "done": true, "steps": 54, "seconds": 2.666, "policy_seconds": 0.01}, {"seed": 800, "count": null, "done": true, "steps": 28, "seconds": 1.084, "policy_seconds": 0.0051}, {"seed": 801, "count": null, "done": true, "steps": 68, "seconds": 5.508, "policy_seconds": 0.0191}, {"seed": 802, "count": null, "done": true, "steps": 48, "seconds": 3.696, "policy_seconds": 0.0151}, {"seed": 803, "count": null, "done": true, "steps": 90, "seconds": 8.13, "policy_seconds": 0.0252}, {"seed": 804, "count": null, "done": true, "steps": 60, "seconds": 4.597, "policy_seconds": 0.0191}, {"seed": 805, "count": null, "done": true, "steps": 28, "seconds": 2.068, "policy_seconds": 0.0066}, {"seed": 806, "count": null, "done": true, "steps": 53, "seconds": 3.616, "policy_seconds": 0.012}, {"seed": 807, "count": null, "done": true, "steps": 18, "seconds": 1.32, "policy_seconds": 0.004}, {"seed": 808, "count": null, "done": true, "steps": 68, "seconds": 6.219, "policy_seconds": 0.0247}, {"seed": 809, "count": null, "done": true, "steps": 49, "seconds": 3.689, "policy_seconds": 0.0112}, {"seed": 810, "count": null, "done": true, "steps": 19, "seconds": 1.16, "policy_seconds": 0.0052}, {"seed": 811, "count": null, "done": true, "steps": 31, "seconds": 1.993, "policy_seconds": 0.0069}, {"seed": 812, "count": null, "done": true, "steps": 97, "seconds": 8.035, "policy_seconds": 0.0256}, {"seed": 813, "count": null, "done": true, "steps": 58, "seconds": 4.227, "policy_seconds": 0.0142}, {"seed": 814, "count": null, "done": true, "steps": 19, "seconds": 1.363, "policy_seconds": 0.0031}, {"seed": 815, "count": null, "done": true, "steps": 22, "seconds": 2.104, "policy_seconds": 0.0071}, {"seed": 816, "count": null, "done": true, "steps": 16, "seconds": 0.766, "policy_seconds": 0.0029}, {"seed": 817, "count": null, "done": true, "steps": 85, "seconds": 7.12, "policy_seconds": 0.0181}, {"seed": 818, "count": null, "done": true, "steps": 44, "seconds": 2.457, "policy_seconds": 0.0096}, {"seed": 819, "count": null, "done": true, "steps": 74, "seconds": 7.047, "policy_seconds": 0.0206}, {"seed": 820, "count": null, "done": true, "steps": 53, "seconds": 3.832, "policy_seconds": 0.0155}, {"seed": 821, "count": null, "done": true, "steps": 29, "seconds": 1.509, "policy_seconds": 0.0045}, {"seed": 822, "count": null, "done": true, "steps": 79, "seconds": 6.201, "policy_seconds": 0.0261}, {"seed": 823, "count": null, "done": true, "steps": 21, "seconds": 0.898, "policy_seconds": 0.0038}, {"seed": 824, "count": null, "done": true, "steps": 59, "seconds": 5.238, "policy_seconds": 0.0218}, {"seed": 825, "count": null, "done": true, "steps": 48, "seconds": 4.284, "policy_seconds": 0.0149}, {"seed": 826, "count": null, "done": true, "steps": 113, "seconds": 11.244, "policy_seconds": 0.0371}, {"seed": 827, "count": null, "done": true, "steps": 23, "seconds": 1.377, "policy_seconds": 0.0063}, {"seed": 828, "count": null, "done": true, "steps": 53, "seconds": 3.621, "policy_seconds": 0.0113}, {"seed": 829, "count": null, "done": true, "steps": 70, "seconds": 6.745, "policy_seconds": 0.0244}, {"seed": 830, "count": null, "done": true, "steps": 22, "seconds": 1.721, "policy_seconds": 0.0055}, {"seed": 831, "count": null, "done": true, "steps": 36, "seconds": 2.167, "policy_seconds": 0.006}, {"seed": 832, "count": null, "done": true, "steps": 110, "seconds": 8.987, "policy_seconds": 0.0294}, {"seed": 833, "count": null, "done": true, "steps": 35, "seconds": 2.003, "policy_seconds": 0.0112}, {"seed": 834, "count": null, "done": true, "steps": 58, "seconds": 5.122, "policy_seconds": 0.0164}, {"seed": 835, "count": null, "done": true, "steps": 50, "seconds": 4.16, "policy_seconds": 0.0169}, {"seed": 836, "count": null, "done": true, "steps": 51, "seconds": 3.418, "policy_seconds": 0.0132}, {"seed": 837, "count": null, "done": true, "steps": 64, "seconds": 4.04, "policy_seconds": 0.0156}, {"seed": 838, "count": null, "done": true, "steps": 25, "seconds": 1.121, "policy_seconds": 0.0054}, {"seed": 839, "count": null, "done": true, "steps": 87, "seconds": 7.736, "policy_seconds": 0.0278}, {"seed": 840, "count": null, "done": true, "steps": 44, "seconds": 2.393, "policy_seconds": 0.0073}, {"seed": 841, "count": null, "done": true, "steps": 63, "seconds": 5.788, "policy_seconds": 0.0193}, {"seed": 842, "count": null, "done": true, "steps": 24, "seconds": 1.823, "policy_seconds": 0.0052}, {"seed": 843, "count": null, "done": true, "steps": 107, "seconds": 10.405, "policy_seconds": 0.0268}, {"seed": 844, "count": null, "done": true, "steps": 58, "seconds": 4.361, "policy_seconds": 0.0135}, {"seed": 845, "count": null, "done": true, "steps": 49, "seconds": 2.895, "policy_seconds": 0.0094}, {"seed": 846, "count": null, "done": true, "steps": 33, "seconds": 3.002, "policy_seconds": 0.0084}, {"seed": 847, "count": null, "done": true, "steps": 25, "seconds": 1.143, "policy_seconds": 0.0045}, {"seed": 848, "count": null, "done": true, "steps": 19, "seconds": 1.132, "policy_seconds": 0.0046}, {"seed": 849, "count": null, "done": true, "steps": 69, "seconds": 5.794, "policy_seconds": 0.0152}, {"seed": 850, "count": null, "done": true, "steps": 34, "seconds": 2.678, "policy_seconds": 0.0079}, {"seed": 851, "count": null, "done": true, "steps": 31, "seconds": 1.902, "policy_seconds": 0.0049}, {"seed": 852, "count": null, "done": true, "steps": 29, "seconds": 1.504, "policy_seconds": 0.0058}, {"seed": 853, "count": null, "done": true, "steps": 42, "seconds": 2.508, "policy_seconds": 0.007}, {"seed": 854, "count": null, "done": true, "steps": 34, "seconds": 2.134, "policy_seconds": 0.006}, {"seed": 855, "count": null, "done": true, "steps": 104, "seconds": 8.452, "policy_seconds": 0.0327}, {"seed": 856, "count": null, "done": true, "steps": 82, "seconds": 5.577, "policy_seconds": 0.0138}, {"seed": 857, "count": null, "done": true, "steps": 62, "seconds": 4.866, "policy_seconds": 0.0121}, {"seed": 858, "count": null, "done": true, "steps": 19, "seconds": 1.163, "policy_seconds": 0.0077}, {"seed": 859, "count": null, "done": true, "steps": 27, "seconds": 1.439, "policy_seconds": 0.0064}, {"seed": 860, "count": null, "done": true, "steps": 87, "seconds": 7.037, "policy_seconds": 0.0173}, {"seed": 861, "count": null, "done": true, "steps": 88, "seconds": 7.437, "policy_seconds": 0.0184}, {"seed": 862, "count": null, "done": true, "steps": 53, "seconds": 5.258, "policy_seconds": 0.0136}, {"seed": 863, "count": null, "done": true, "steps": 64, "seconds": 4.69, "policy_seconds": 0.0142}, {"seed": 864, "count": null, "done": true, "steps": 86, "seconds": 4.984, "policy_seconds": 0.0213}, {"seed": 865, "count": null, "done": true, "steps": 29, "seconds": 1.62, "policy_seconds": 0.004}, {"seed": 866, "count": null, "done": true, "steps": 72, "seconds": 5.733, "policy_seconds": 0.017}, {"seed": 867, "count": null, "done": true, "steps": 27, "seconds": 1.9, "policy_seconds": 0.007}, {"seed": 868, "count": null, "done": true, "steps": 70, "seconds": 4.497, "policy_seconds": 0.0137}, {"seed": 869, "count": null, "done": true, "steps": 62, "seconds": 4.462, "policy_seconds": 0.0161}, {"seed": 870, "count": null, "done": true, "steps": 98, "seconds": 9.779, "policy_seconds": 0.0217}, {"seed": 871, "count": null, "done": true, "steps": 47, "seconds": 2.77, "policy_seconds": 0.0093}, {"seed": 872, "count": null, "done": true, "steps": 65, "seconds": 6.741, "policy_seconds": 0.0188}, {"seed": 873, "count": null, "done": true, "steps": 27, "seconds": 1.579, "policy_seconds": 0.0057}, {"seed": 874, "count": null, "done": true, "steps": 77, "seconds": 6.251, "policy_seconds": 0.0175}, {"seed": 875, "count": null, "done": true, "steps": 56, "seconds": 5.73, "policy_seconds": 0.0159}, {"seed": 876, "count": null, "done": true, "steps": 85, "seconds": 5.436, "policy_seconds": 0.0181}, {"seed": 877, "count": null, "done": true, "steps": 63, "seconds": 5.241, "policy_seconds": 0.0144}, {"seed": 878, "count": null, "done": true, "steps": 78, "seconds": 6.441, "policy_seconds": 0.015}, {"seed": 879, "count": null, "done": true, "steps": 44, "seconds": 2.684, "policy_seconds": 0.0049}, {"seed": 880, "count": null, "done": true, "steps": 71, "seconds": 6.44, "policy_seconds": 0.0127}, {"seed": 881, "count": null, "done": true, "steps": 33, "seconds": 1.999, "policy_seconds": 0.0043}, {"seed": 882, "count": null, "done": true, "steps": 72, "seconds": 4.928, "policy_seconds": 0.0139}, {"seed": 883, "count": null, "done": true, "steps": 46, "seconds": 3.876, "policy_seconds": 0.0104}, {"seed": 884, "count": null, "done": true, "steps": 31, "seconds": 2.238, "policy_seconds": 0.0053}, {"seed": 885, "count": null, "done": true, "steps": 20, "seconds": 0.671, "policy_seconds": 0.0042}, {"seed": 886, "count": null, "done": true, "steps": 89, "seconds": 6.549, "policy_seconds": 0.0174}, {"seed": 887, "count": null, "done": true, "steps": 24, "seconds": 2.326, "policy_seconds": 0.0054}, {"seed": 888, "count": null, "done": true, "steps": 29, "seconds": 2.452, "policy_seconds": 0.0083}, {"seed": 889, "count": null, "done": true, "steps": 56, "seconds": 3.492, "policy_seconds": 0.0119}, {"seed": 890, "count": null, "done": true, "steps": 24, "seconds": 1.265, "policy_seconds": 0.0036}, {"seed": 891, "count": null, "done": true, "steps": 81, "seconds": 6.915, "policy_seconds": 0.0222}, {"seed": 892, "count": null, "done": true, "steps": 26, "seconds": 2.372, "policy_seconds": 0.0057}, {"seed": 893, "count": null, "done": true, "steps": 49, "seconds": 3.73, "policy_seconds": 0.0144}, {"seed": 894, "count": null, "done": true, "steps": 46, "seconds": 2.967, "policy_seconds": 0.0116}, {"seed": 895, "count": null, "done": true, "steps": 76, "seconds": 5.968, "policy_seconds": 0.0233}, {"seed": 896, "count": null, "done": true, "steps": 19, "seconds": 1.542, "policy_seconds": 0.0065}, {"seed": 897, "count": null, "done": true, "steps": 41, "seconds": 2.992, "policy_seconds": 0.0085}, {"seed": 898, "count": null, "done": true, "steps": 43, "seconds": 3.081, "policy_seconds": 0.0087}, {"seed": 899, "count": null, "done": true, "steps": 53, "seconds": 4.488, "policy_seconds": 0.0153}, {"seed": 900, "count": null, "done": true, "steps": 62, "seconds": 4.838, "policy_seconds": 0.0159}, {"seed": 901, "count": null, "done": true, "steps": 33, "seconds": 2.419, "policy_seconds": 0.0061}, {"seed": 902, "count": null, "done": true, "steps": 90, "seconds": 8.836, "policy_seconds": 0.0203}, {"seed": 903, "count": null, "done": true, "steps": 97, "seconds": 8.933, "policy_seconds": 0.0212}, {"seed": 904, "count": null, "done": true, "steps": 50, "seconds": 5.511, "policy_seconds": 0.0124}, {"seed": 905, "count": null, "done": true, "steps": 85, "seconds": 6.08, "policy_seconds": 0.0191}, {"seed": 906, "count": null, "done": true, "steps": 48, "seconds": 2.752, "policy_seconds": 0.012}, {"seed": 907, "count": null, "done": true, "steps": 75, "seconds": 4.816, "policy_seconds": 0.0179}, {"seed": 908, "count": null, "done": true, "steps": 65, "seconds": 5.692, "policy_seconds": 0.0183}, {"seed": 909, "count": null, "done": true, "steps": 18, "seconds": 0.974, "policy_seconds": 0.0028}, {"seed": 910, "count": null, "done": true, "steps": 82, "seconds": 8.304, "policy_seconds": 0.0229}, {"seed": 911, "count": null, "done": true, "steps": 53, "seconds": 5.451, "policy_seconds": 0.0125}, {"seed": 912, "count": null, "done": true, "steps": 60, "seconds": 5.491, "policy_seconds": 0.0185}, {"seed": 913, "count": null, "done": true, "steps": 46, "seconds": 2.633, "policy_seconds": 0.0072}, {"seed": 914, "count": null, "done": true, "steps": 97, "seconds": 8.02, "policy_seconds": 0.0266}, {"seed": 915, "count": null, "done": true, "steps": 68, "seconds": 6.663, "policy_seconds": 0.0164}, {"seed": 916, "count": null, "done": true, "steps": 41, "seconds": 3.482, "policy_seconds": 0.0102}, {"seed": 917, "count": null, "done": true, "steps": 57, "seconds": 5.477, "policy_seconds": 0.0175}, {"seed": 918, "count": null, "done": true, "steps": 111, "seconds": 10.855, "policy_seconds": 0.0243}, {"seed": 919, "count": null, "done": true, "steps": 69, "seconds": 5.959, "policy_seconds": 0.0186}, {"seed": 920, "count": null, "done": true, "steps": 62, "seconds": 5.24, "policy_seconds": 0.0179}, {"seed": 921, "count": null, "done": true, "steps": 35, "seconds": 2.646, "policy_seconds": 0.007}, {"seed": 922, "count": null, "done": true, "steps": 92, "seconds": 8.327, "policy_seconds": 0.0267}, {"seed": 923, "count": null, "done": true, "steps": 62, "seconds": 5.926, "policy_seconds": 0.0176}, {"seed": 924, "count": null, "done": true, "steps": 79, "seconds": 7.367, "policy_seconds": 0.0197}, {"seed": 925, "count": null, "done": true, "steps": 28, "seconds": 1.791, "policy_seconds": 0.0056}, {"seed": 926, "count": null, "done": true, "steps": 52, "seconds": 5.294, "policy_seconds": 0.0153}, {"seed": 927, "count": null, "done": true, "steps": 48, "seconds": 3.141, "policy_seconds": 0.0094}, {"seed": 928, "count": null, "done": true, "steps": 29, "seconds": 1.207, "policy_seconds": 0.0058}, {"seed": 929, "count": null, "done": true, "steps": 23, "seconds": 0.947, "policy_seconds": 0.0037}, {"seed": 930, "count": null, "done": true, "steps": 51, "seconds": 2.139, "policy_seconds": 0.0065}, {"seed": 931, "count": null, "done": true, "steps": 49, "seconds": 3.039, "policy_seconds": 0.0082}, {"seed": 932, "count": null, "done": true, "steps": 17, "seconds": 0.919, "policy_seconds": 0.0049}, {"seed": 933, "count": null, "done": true, "steps": 74, "seconds": 6.801, "policy_seconds": 0.0183}, {"seed": 934, "count": null, "done": true, "steps": 93, "seconds": 6.801, "policy_seconds": 0.0214}, {"seed": 935, "count": null, "done": true, "steps": 63, "seconds": 6.144, "policy_seconds": 0.0188}, {"seed": 936, "count": null, "done": true, "steps": 62, "seconds": 6.56, "policy_seconds": 0.0167}, {"seed": 937, "count": null, "done": true, "steps": 94, "seconds": 8.505, "policy_seconds": 0.0279}, {"seed": 938, "count": null, "done": true, "steps": 24, "seconds": 1.448, "policy_seconds": 0.0066}, {"seed": 939, "count": null, "done": true, "steps": 35, "seconds": 2.136, "policy_seconds": 0.0095}, {"seed": 940, "count": null, "done": true, "steps": 19, "seconds": 1.566, "policy_seconds": 0.0041}, {"seed": 941, "count": null, "done": true, "steps": 27, "seconds": 1.751, "policy_seconds": 0.0071}, {"seed": 942, "count": null, "done": true, "steps": 31, "seconds": 2.841, "policy_seconds": 0.0063}, {"seed": 943, "count": null, "done": true, "steps": 31, "seconds": 2.116, "policy_seconds": 0.0079}, {"seed": 944, "count": null, "done": true, "steps": 30, "seconds": 1.546, "policy_seconds": 0.0068}, {"seed": 945, "count": null, "done": true, "steps": 59, "seconds": 4.935, "policy_seconds": 0.016}, {"seed": 946, "count": null, "done": true, "steps": 42, "seconds": 3.087, "policy_seconds": 0.0136}, {"seed": 947, "count": null, "done": true, "steps": 20, "seconds": 1.116, "policy_seconds": 0.0051}, {"seed": 948, "count": null, "done": true, "steps": 57, "seconds": 4.41, "policy_seconds": 0.0153}, {"seed": 949, "count": null, "done": true, "steps": 47, "seconds": 4.336, "policy_seconds": 0.0145}, {"seed": 950, "count": null, "done": true, "steps": 81, "seconds": 8.629, "policy_seconds": 0.0198}, {"seed": 951, "count": null, "done": true, "steps": 92, "seconds": 9.075, "policy_seconds": 0.0278}, {"seed": 952, "count": null, "done": true, "steps": 84, "seconds": 6.72, "policy_seconds": 0.0186}, {"seed": 953, "count": null, "done": true, "steps": 69, "seconds": 7.225, "policy_seconds": 0.0144}, {"seed": 954, "count": null, "done": true, "steps": 101, "seconds": 10.062, "policy_seconds": 0.0299}, {"seed": 955, "count": null, "done": true, "steps": 23, "seconds": 1.337, "policy_seconds": 0.0046}, {"seed": 956, "count": null, "done": true, "steps": 66, "seconds": 6.116, "policy_seconds": 0.0175}, {"seed": 957, "count": null, "done": true, "steps": 20, "seconds": 1.616, "policy_seconds": 0.006}, {"seed": 958, "count": null, "done": true, "steps": 50, "seconds": 4.533, "policy_seconds": 0.0144}, {"seed": 959, "count": null, "done": true, "steps": 26, "seconds": 2.138, "policy_seconds": 0.0066}, {"seed": 960, "count": null, "done": true, "steps": 92, "seconds": 6.545, "policy_seconds": 0.0211}, {"seed": 961, "count": null, "done": true, "steps": 21, "seconds": 1.229, "policy_seconds": 0.0061}, {"seed": 962, "count": null, "done": true, "steps": 23, "seconds": 1.794, "policy_seconds": 0.0056}, {"seed": 963, "count": null, "done": true, "steps": 24, "seconds": 1.291, "policy_seconds": 0.0053}, {"seed": 964, "count": null, "done": true, "steps": 25, "seconds": 1.408, "policy_seconds": 0.0059}, {"seed": 965, "count": null, "done": true, "steps": 50, "seconds": 3.5, "policy_seconds": 0.0123}, {"seed": 966, "count": null, "done": true, "steps": 50, "seconds": 4.51, "policy_seconds": 0.0131}, {"seed": 967, "count": null, "done": true, "steps": 22, "seconds": 1.288, "policy_seconds": 0.0058}, {"seed": 968, "count": null, "done": true, "steps": 55, "seconds": 4.238, "policy_seconds": 0.0145}, {"seed": 969, "count": null, "done": true, "steps": 21, "seconds": 1.284, "policy_seconds": 0.0059}, {"seed": 970, "count": null, "done": true, "steps": 66, "seconds": 6.176, "policy_seconds": 0.0156}, {"seed": 971, "count": null, "done": true, "steps": 33, "seconds": 2.204, "policy_seconds": 0.0062}, {"seed": 972, "count": null, "done": true, "steps": 38, "seconds": 3.309, "policy_seconds": 0.009}, {"seed": 973, "count": null, "done": true, "steps": 24, "seconds": 2.085, "policy_seconds": 0.0066}, {"seed": 974, "count": null, "done": true, "steps": 77, "seconds": 4.762, "policy_seconds": 0.018}, {"seed": 975, "count": null, "done": true, "steps": 62, "seconds": 4.7, "policy_seconds": 0.014}, {"seed": 976, "count": null, "done": true, "steps": 20, "seconds": 1.531, "policy_seconds": 0.0041}, {"seed": 977, "count": null, "done": true, "steps": 53, "seconds": 4.878, "policy_seconds": 0.0138}, {"seed": 978, "count": null, "done": true, "steps": 27, "seconds": 1.496, "policy_seconds": 0.0045}, {"seed": 979, "count": null, "done": true, "steps": 58, "seconds": 6.206, "policy_seconds": 0.0152}, {"seed": 980, "count": null, "done": true, "steps": 22, "seconds": 1.448, "policy_seconds": 0.0068}, {"seed": 981, "count": null, "done": true, "steps": 29, "seconds": 1.948, "policy_seconds": 0.0049}, {"seed": 982, "count": null, "done": true, "steps": 51, "seconds": 3.933, "policy_seconds": 0.0117}, {"seed": 983, "count": null, "done": true, "steps": 55, "seconds": 3.897, "policy_seconds": 0.0138}, {"seed": 984, "count": null, "done": true, "steps": 25, "seconds": 1.164, "policy_seconds": 0.004}, {"seed": 985, "count": null, "done": true, "steps": 40, "seconds": 1.78, "policy_seconds": 0.0108}, {"seed": 986, "count": null, "done": true, "steps": 25, "seconds": 1.292, "policy_seconds": 0.0045}, {"seed": 987, "count": null, "done": true, "steps": 44, "seconds": 3.653, "policy_seconds": 0.0096}, {"seed": 988, "count": null, "done": true, "steps": 27, "seconds": 2.353, "policy_seconds": 0.0071}, {"seed": 989, "count": null, "done": true, "steps": 57, "seconds": 5.72, "policy_seconds": 0.0153}, {"seed": 990, "count": null, "done": true, "steps": 82, "seconds": 6.483, "policy_seconds": 0.0257}, {"seed": 991, "count": null, "done": true, "steps": 46, "seconds": 3.386, "policy_seconds": 0.0155}, {"seed": 992, "count": null, "done": true, "steps": 23, "seconds": 1.437, "policy_seconds": 0.0048}, {"seed": 993, "count": null, "done": true, "steps": 54, "seconds": 3.042, "policy_seconds": 0.0104}, {"seed": 994, "count": null, "done": true, "steps": 20, "seconds": 1.619, "policy_seconds": 0.005}, {"seed": 995, "count": null, "done": true, "steps": 58, "seconds": 4.233, "policy_seconds": 0.0146}, {"seed": 996, "count": null, "done": true, "steps": 46, "seconds": 3.643, "policy_seconds": 0.0133}, {"seed": 997, "count": null, "done": true, "steps": 77, "seconds": 5.49, "policy_seconds": 0.0183}, {"seed": 998, "count": null, "done": true, "steps": 98, "seconds": 7.064, "policy_seconds": 0.0222}, {"seed": 999, "count": null, "done": true, "steps": 120, "seconds": 8.01, "policy_seconds": 0.0282}]
\ No newline at end of file
diff --git a/sweep_300_700.log b/sweep_300_700.log
index 4921214..947beb4 100644
--- a/sweep_300_700.log
+++ b/sweep_300_700.log
@@ -698,3 +698,8 @@
  698    698  995 OK 58
  699    699  996 OK 46
  700    700  997 OK 77
         701 +998 OK 98
         702 +999 OK 120
         703 +{'seed': 489, 'count': None, 'done': False, 'steps': 1000, 'seconds': 68.581, 'policy_seconds': 0.1308, 'trace': [[840, 'place', 'target_block', 0.5194, 0.4876], [880, 'place', 'target_block', 0.5194, 0.4876], [920, 'place', 'target_block', 0.5194, 0.4876], [960, 'place', 'target_block', 0.5194, 0.4876]], 'state': {'obstruction0': {'x': 0.6125882863998413, 'y': 0.10000099986791611, 'width': 0.08571477979421616, 'height': 0.09336432069540024}, 'obstruction1': {'x': 0.8762147426605225, 'y': 0.10100002586841583, 'width': 0.07839120179414749, 'height': 0.1896573305130005}, 'target_block': {'x': 0.5144228339195251, 'y': 0.21765734255313873, 'width': 0.09879190474748611, 'height': 0.06392852216959}, 'target_surface': {'x': 0.5127172470092773, 'y': 0.0, 'width': 0.12958014011383057, 'height': 0.10000000149011612}}}
         704 +{'seed': 627, 'count': None, 'done': False, 'steps': 1000, 'seconds': 128.098, 'policy_seconds': 0.1434, 'trace': [[840, 'down', 'target_block', 0.5233, 0.5412], [880, 'down', 'target_block', 0.5233, 0.3912], [920, 'lift', 'target_block', 0.5233, 0.5912], [960, 'down', 'target_block', 0.5233, 0.3912]], 'state': {'obstruction0': {'x': 1.070956826210022, 'y': 0.10000099986791611, 'width': 0.10327284038066864, 'height': 0.06639733165502548}, 'obstruction1': {'x': 0.5642479658126831, 'y': 0.10099996626377106, 'width': 0.1490718424320221, 'height': 0.1984524130821228}, 'target_block': {'x': 0.4953683614730835, 'y': 0.10000099986791611, 'width': 0.055879540741443634, 'height': 0.058782048523426056}, 'target_surface': {'x': 0.8293163180351257, 'y': 0.0, 'width': 0.09297315031290054, 'height': 0.10000000149011612}}}
         705 +SUMMARY 700 success 698 mean_steps 52.6 max_time 128.098
```

</details>

<a id="C039"></a>
### C039 · Finalize validation documentation and preserve all discovered regression cases

Commit `1885889b53fee99a21e307f2ee39315c2fe73c72`; parents: 5f1766ad5616a95b45e3437b782ad057710c1560. Recorded author date: 2026-09-21T23:07:41+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0193](01_timeline.md#E0193): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C039_1885889.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

````text
 OLD   NEW   CHANGE
diff --git a/README.md b/README.md
index deee1b8..474a1b1 100644
--- a/README.md
+++ b/README.md
@@ -14,3 +14,9 @@ Run tests with the supplied interpreter:
   14     14  ```
   15     15  
   16     16  The optional third batch argument pins the obstruction count. Each test environment is a fresh live-server instance. The regression suite covers wall reach, narrow grasp clearances, gripper placement collisions, and storage that could obstruct a later pickup. Policy computation is timed separately from environment generation and remote stepping.
          17 +
          18 +## Validation
          19 +
          20 +Development testing covered default-count seeds 0–999 and 2000–2099, three-obstruction seeds 0–199, and four-obstruction seeds 0–9. Historical sweep files include failures from earlier policy revisions; each discovered failure was replayed successfully after its corresponding fix.
          21 +
          22 +The final regression suite covers 14 previously difficult or representative cases. `regression_results.json` records results, policy computation time, and the exact policy SHA-256. Policy computation in the final regression suite is far below the 60-second allowance; remote test latency also includes server stepping and contention between independent test instances.
diff --git a/regression_results.json b/regression_results.json
index e14a8e6..6fd3517 100644
--- a/regression_results.json
+++ b/regression_results.json
@@ -4,95 +4,103 @@
    4      4      "count": null,
    5      5      "done": true,
    6      6      "steps": 50,
    7        -    "policy_seconds": 0.009710075333714485,
    8        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
           7 +    "policy_seconds": 0.005131836049258709,
           8 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
    9      9    },
   10     10    {
   11     11      "seed": 31,
   12     12      "count": null,
   13     13      "done": true,
   14     14      "steps": 79,
   15        -    "policy_seconds": 0.0202472060918808,
   16        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          15 +    "policy_seconds": 0.013064275495707989,
          16 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   17     17    },
   18     18    {
   19     19      "seed": 74,
   20     20      "count": null,
   21     21      "done": true,
   22     22      "steps": 25,
   23        -    "policy_seconds": 0.006569691002368927,
   24        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          23 +    "policy_seconds": 0.005541585385799408,
          24 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   25     25    },
   26     26    {
   27     27      "seed": 151,
   28     28      "count": null,
   29     29      "done": true,
   30     30      "steps": 71,
   31        -    "policy_seconds": 0.014874584041535854,
   32        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          31 +    "policy_seconds": 0.01696677040308714,
          32 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   33     33    },
   34     34    {
   35     35      "seed": 489,
   36     36      "count": null,
   37     37      "done": true,
   38     38      "steps": 111,
   39        -    "policy_seconds": 0.02264695893973112,
   40        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          39 +    "policy_seconds": 0.026794604025781155,
          40 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
          41 +  },
          42 +  {
          43 +    "seed": 627,
          44 +    "count": null,
          45 +    "done": true,
          46 +    "steps": 70,
          47 +    "policy_seconds": 0.01879723183810711,
          48 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   41     49    },
   42     50    {
   43     51      "seed": 42,
   44     52      "count": 3,
   45     53      "done": true,
   46     54      "steps": 93,
   47        -    "policy_seconds": 0.029996491968631744,
   48        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          55 +    "policy_seconds": 0.028547299094498158,
          56 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   49     57    },
   50     58    {
   51     59      "seed": 0,
   52     60      "count": 4,
   53     61      "done": true,
   54     62      "steps": 95,
   55        -    "policy_seconds": 0.036820714361965656,
   56        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          63 +    "policy_seconds": 0.030501403845846653,
          64 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   57     65    },
   58     66    {
   59     67      "seed": 1,
   60     68      "count": 4,
   61     69      "done": true,
   62     70      "steps": 79,
   63        -    "policy_seconds": 0.028981699608266354,
   64        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          71 +    "policy_seconds": 0.02996176667511463,
          72 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   65     73    },
   66     74    {
   67     75      "seed": 2,
   68     76      "count": 4,
   69     77      "done": true,
   70     78      "steps": 137,
   71        -    "policy_seconds": 0.03913711290806532,
   72        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          79 +    "policy_seconds": 0.032656130380928516,
          80 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   73     81    },
   74     82    {
   75     83      "seed": 3,
   76     84      "count": 4,
   77     85      "done": true,
   78     86      "steps": 101,
   79        -    "policy_seconds": 0.03482349868863821,
   80        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          87 +    "policy_seconds": 0.031625750474631786,
          88 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   81     89    },
   82     90    {
   83     91      "seed": 4,
   84     92      "count": 4,
   85     93      "done": true,
   86     94      "steps": 165,
   87        -    "policy_seconds": 0.050516946241259575,
   88        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
          95 +    "policy_seconds": 0.023875144310295582,
          96 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   89     97    },
   90     98    {
   91     99      "seed": 5,
   92    100      "count": 4,
   93    101      "done": true,
   94    102      "steps": 83,
   95        -    "policy_seconds": 0.022572549059987068,
   96        -    "policy_hash": "d522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb"
         103 +    "policy_seconds": 0.009609416127204895,
         104 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   97    105    }
   98    106  ]
\ No newline at end of file
diff --git a/regression_run.log b/regression_run.log
index b7a6917..8a83bb9 100644
--- a/regression_run.log
+++ b/regression_run.log
@@ -1,12 +1,13 @@
    1        -{'seed': 21, 'count': None, 'done': True, 'steps': 50, 'policy_seconds': 0.009710075333714485, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
    2        -{'seed': 31, 'count': None, 'done': True, 'steps': 79, 'policy_seconds': 0.0202472060918808, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
    3        -{'seed': 74, 'count': None, 'done': True, 'steps': 25, 'policy_seconds': 0.006569691002368927, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
    4        -{'seed': 151, 'count': None, 'done': True, 'steps': 71, 'policy_seconds': 0.014874584041535854, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
    5        -{'seed': 489, 'count': None, 'done': True, 'steps': 111, 'policy_seconds': 0.02264695893973112, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
    6        -{'seed': 42, 'count': 3, 'done': True, 'steps': 93, 'policy_seconds': 0.029996491968631744, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
    7        -{'seed': 0, 'count': 4, 'done': True, 'steps': 95, 'policy_seconds': 0.036820714361965656, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
    8        -{'seed': 1, 'count': 4, 'done': True, 'steps': 79, 'policy_seconds': 0.028981699608266354, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
    9        -{'seed': 2, 'count': 4, 'done': True, 'steps': 137, 'policy_seconds': 0.03913711290806532, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
   10        -{'seed': 3, 'count': 4, 'done': True, 'steps': 101, 'policy_seconds': 0.03482349868863821, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
   11        -{'seed': 4, 'count': 4, 'done': True, 'steps': 165, 'policy_seconds': 0.050516946241259575, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
   12        -{'seed': 5, 'count': 4, 'done': True, 'steps': 83, 'policy_seconds': 0.022572549059987068, 'policy_hash': 'd522957da88d0ba0d7935d2d11dd603d808ef58ff57706a6179563b6395addfb'}
           1 +{'seed': 21, 'count': None, 'done': True, 'steps': 50, 'policy_seconds': 0.005131836049258709, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           2 +{'seed': 31, 'count': None, 'done': True, 'steps': 79, 'policy_seconds': 0.013064275495707989, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           3 +{'seed': 74, 'count': None, 'done': True, 'steps': 25, 'policy_seconds': 0.005541585385799408, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           4 +{'seed': 151, 'count': None, 'done': True, 'steps': 71, 'policy_seconds': 0.01696677040308714, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           5 +{'seed': 489, 'count': None, 'done': True, 'steps': 111, 'policy_seconds': 0.026794604025781155, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           6 +{'seed': 627, 'count': None, 'done': True, 'steps': 70, 'policy_seconds': 0.01879723183810711, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           7 +{'seed': 42, 'count': 3, 'done': True, 'steps': 93, 'policy_seconds': 0.028547299094498158, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           8 +{'seed': 0, 'count': 4, 'done': True, 'steps': 95, 'policy_seconds': 0.030501403845846653, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           9 +{'seed': 1, 'count': 4, 'done': True, 'steps': 79, 'policy_seconds': 0.02996176667511463, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
          10 +{'seed': 2, 'count': 4, 'done': True, 'steps': 137, 'policy_seconds': 0.032656130380928516, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
          11 +{'seed': 3, 'count': 4, 'done': True, 'steps': 101, 'policy_seconds': 0.031625750474631786, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
          12 +{'seed': 4, 'count': 4, 'done': True, 'steps': 165, 'policy_seconds': 0.023875144310295582, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
          13 +{'seed': 5, 'count': 4, 'done': True, 'steps': 83, 'policy_seconds': 0.009609416127204895, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
diff --git a/test_regression.py b/test_regression.py
index 50df6df..7dd15b8 100644
--- a/test_regression.py
+++ b/test_regression.py
@@ -5,7 +5,7 @@ import time
    5      5  from env_client import make_env
    6      6  from approach import GeneratedApproach
    7      7  
    8        -cases=[(21,None),(31,None),(74,None),(151,None),(489,None),(627,None),(42,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4)]
           8 +cases=[(21,None),(31,None),(74,None),(151,None),(489,None),(627,None),(42,3),(154,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4)]
    9      9  policy_hash=hashlib.sha256(open('approach.py','rb').read()).hexdigest()
   10     10  results=[]
   11     11  e=make_env()
````

</details>

<a id="C040"></a>
### C040 · Save final passing regression results and verified policy artifact

Commit `bfc4b68e9d1e694a3bf0bc0d379c24ed4308d91b`; parents: 1885889b53fee99a21e307f2ee39315c2fe73c72. Recorded author date: 2026-09-21T23:08:12+02:00.

File roles (automatic): setup/other.

- [E0198](01_timeline.md#E0198): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C040_bfc4b68.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/regression_results.json b/regression_results.json
index 6fd3517..32cf5b6 100644
--- a/regression_results.json
+++ b/regression_results.json
@@ -4,7 +4,7 @@
    4      4      "count": null,
    5      5      "done": true,
    6      6      "steps": 50,
    7        -    "policy_seconds": 0.005131836049258709,
           7 +    "policy_seconds": 0.00503266416490078,
    8      8      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
    9      9    },
   10     10    {
@@ -12,7 +12,7 @@
   12     12      "count": null,
   13     13      "done": true,
   14     14      "steps": 79,
   15        -    "policy_seconds": 0.013064275495707989,
          15 +    "policy_seconds": 0.009087708778679371,
   16     16      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   17     17    },
   18     18    {
@@ -20,7 +20,7 @@
   20     20      "count": null,
   21     21      "done": true,
   22     22      "steps": 25,
   23        -    "policy_seconds": 0.005541585385799408,
          23 +    "policy_seconds": 0.0033139344304800034,
   24     24      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   25     25    },
   26     26    {
@@ -28,7 +28,7 @@
   28     28      "count": null,
   29     29      "done": true,
   30     30      "steps": 71,
   31        -    "policy_seconds": 0.01696677040308714,
          31 +    "policy_seconds": 0.018764402717351913,
   32     32      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   33     33    },
   34     34    {
@@ -36,7 +36,7 @@
   36     36      "count": null,
   37     37      "done": true,
   38     38      "steps": 111,
   39        -    "policy_seconds": 0.026794604025781155,
          39 +    "policy_seconds": 0.03076502401381731,
   40     40      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   41     41    },
   42     42    {
@@ -44,7 +44,7 @@
   44     44      "count": null,
   45     45      "done": true,
   46     46      "steps": 70,
   47        -    "policy_seconds": 0.01879723183810711,
          47 +    "policy_seconds": 0.019007197581231594,
   48     48      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   49     49    },
   50     50    {
@@ -52,7 +52,15 @@
   52     52      "count": 3,
   53     53      "done": true,
   54     54      "steps": 93,
   55        -    "policy_seconds": 0.028547299094498158,
          55 +    "policy_seconds": 0.02859614696353674,
          56 +    "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
          57 +  },
          58 +  {
          59 +    "seed": 154,
          60 +    "count": 3,
          61 +    "done": true,
          62 +    "steps": 69,
          63 +    "policy_seconds": 0.020431329496204853,
   56     64      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   57     65    },
   58     66    {
@@ -60,7 +68,7 @@
   60     68      "count": 4,
   61     69      "done": true,
   62     70      "steps": 95,
   63        -    "policy_seconds": 0.030501403845846653,
          71 +    "policy_seconds": 0.032867164351046085,
   64     72      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   65     73    },
   66     74    {
@@ -68,7 +76,7 @@
   68     76      "count": 4,
   69     77      "done": true,
   70     78      "steps": 79,
   71        -    "policy_seconds": 0.02996176667511463,
          79 +    "policy_seconds": 0.026706818491220474,
   72     80      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   73     81    },
   74     82    {
@@ -76,7 +84,7 @@
   76     84      "count": 4,
   77     85      "done": true,
   78     86      "steps": 137,
   79        -    "policy_seconds": 0.032656130380928516,
          87 +    "policy_seconds": 0.016411777585744858,
   80     88      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   81     89    },
   82     90    {
@@ -84,7 +92,7 @@
   84     92      "count": 4,
   85     93      "done": true,
   86     94      "steps": 101,
   87        -    "policy_seconds": 0.031625750474631786,
          95 +    "policy_seconds": 0.028363442048430443,
   88     96      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   89     97    },
   90     98    {
@@ -92,7 +100,7 @@
   92    100      "count": 4,
   93    101      "done": true,
   94    102      "steps": 165,
   95        -    "policy_seconds": 0.023875144310295582,
         103 +    "policy_seconds": 0.018700494430959225,
   96    104      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
   97    105    },
   98    106    {
@@ -100,7 +108,7 @@
  100    108      "count": 4,
  101    109      "done": true,
  102    110      "steps": 83,
  103        -    "policy_seconds": 0.009609416127204895,
         111 +    "policy_seconds": 0.024076828733086586,
  104    112      "policy_hash": "76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2"
  105    113    }
  106    114  ]
\ No newline at end of file
diff --git a/regression_run.log b/regression_run.log
index 8a83bb9..298dfa3 100644
--- a/regression_run.log
+++ b/regression_run.log
@@ -1,13 +1,14 @@
    1        -{'seed': 21, 'count': None, 'done': True, 'steps': 50, 'policy_seconds': 0.005131836049258709, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
    2        -{'seed': 31, 'count': None, 'done': True, 'steps': 79, 'policy_seconds': 0.013064275495707989, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
    3        -{'seed': 74, 'count': None, 'done': True, 'steps': 25, 'policy_seconds': 0.005541585385799408, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
    4        -{'seed': 151, 'count': None, 'done': True, 'steps': 71, 'policy_seconds': 0.01696677040308714, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
    5        -{'seed': 489, 'count': None, 'done': True, 'steps': 111, 'policy_seconds': 0.026794604025781155, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
    6        -{'seed': 627, 'count': None, 'done': True, 'steps': 70, 'policy_seconds': 0.01879723183810711, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
    7        -{'seed': 42, 'count': 3, 'done': True, 'steps': 93, 'policy_seconds': 0.028547299094498158, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
    8        -{'seed': 0, 'count': 4, 'done': True, 'steps': 95, 'policy_seconds': 0.030501403845846653, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
    9        -{'seed': 1, 'count': 4, 'done': True, 'steps': 79, 'policy_seconds': 0.02996176667511463, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
   10        -{'seed': 2, 'count': 4, 'done': True, 'steps': 137, 'policy_seconds': 0.032656130380928516, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
   11        -{'seed': 3, 'count': 4, 'done': True, 'steps': 101, 'policy_seconds': 0.031625750474631786, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
   12        -{'seed': 4, 'count': 4, 'done': True, 'steps': 165, 'policy_seconds': 0.023875144310295582, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
   13        -{'seed': 5, 'count': 4, 'done': True, 'steps': 83, 'policy_seconds': 0.009609416127204895, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           1 +{'seed': 21, 'count': None, 'done': True, 'steps': 50, 'policy_seconds': 0.00503266416490078, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           2 +{'seed': 31, 'count': None, 'done': True, 'steps': 79, 'policy_seconds': 0.009087708778679371, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           3 +{'seed': 74, 'count': None, 'done': True, 'steps': 25, 'policy_seconds': 0.0033139344304800034, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           4 +{'seed': 151, 'count': None, 'done': True, 'steps': 71, 'policy_seconds': 0.018764402717351913, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           5 +{'seed': 489, 'count': None, 'done': True, 'steps': 111, 'policy_seconds': 0.03076502401381731, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           6 +{'seed': 627, 'count': None, 'done': True, 'steps': 70, 'policy_seconds': 0.019007197581231594, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           7 +{'seed': 42, 'count': 3, 'done': True, 'steps': 93, 'policy_seconds': 0.02859614696353674, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           8 +{'seed': 154, 'count': 3, 'done': True, 'steps': 69, 'policy_seconds': 0.020431329496204853, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
           9 +{'seed': 0, 'count': 4, 'done': True, 'steps': 95, 'policy_seconds': 0.032867164351046085, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
          10 +{'seed': 1, 'count': 4, 'done': True, 'steps': 79, 'policy_seconds': 0.026706818491220474, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
          11 +{'seed': 2, 'count': 4, 'done': True, 'steps': 137, 'policy_seconds': 0.016411777585744858, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
          12 +{'seed': 3, 'count': 4, 'done': True, 'steps': 101, 'policy_seconds': 0.028363442048430443, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
          13 +{'seed': 4, 'count': 4, 'done': True, 'steps': 165, 'policy_seconds': 0.018700494430959225, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
          14 +{'seed': 5, 'count': 4, 'done': True, 'steps': 83, 'policy_seconds': 0.024076828733086586, 'policy_hash': '76a785db8796febc9c10d2ab83f6ceeff9d454a9459bb9ff283beed0e26b54d2'}
```

</details>

