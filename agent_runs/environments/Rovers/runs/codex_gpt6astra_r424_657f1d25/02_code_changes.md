# Rovers · gpt-6-astra · replicate 424: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `7701bbc` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `378927f` | Add independent visibility and operator probe | inspect_env.py, probe_motion.py, probe_shape.py, probe_visibility.py | No matched commit command/output |
| [C003](#C003) · `18ba3c4` | Probe cross-divider camera visibility | probe_crosslos.py | No matched commit command/output |
| [C004](#C004) · `a7bf7fd` | Implement initial object-centric navigation and cooperative task policy | approach.py | [E0018](01_timeline.md#E0018) |
| [C005](#C005) · `1d68b46` | Use measured circular clearance and ignore divider for visibility | test_approach.py | [E0020](01_timeline.md#E0020) |
| [C006](#C006) · `b6f4ab5` | Correct measured collision model and waypoint advancement | approach.py | [E0022](01_timeline.md#E0022) |
| [C007](#C007) · `49b61ec` | Add targeted LOS failure probes | probe_los_details.py | No matched commit command/output |
| [C008](#C008) · `a826852` | Replan after refused camera and radio operators | approach.py | [E0026](01_timeline.md#E0026) |
| [C009](#C009) · `6f08fb9` | Correct operator recovery dispatch and syntax | approach.py, test_results.txt | [E0031](01_timeline.md#E0031) |
| [C010](#C010) · `4581e65` | Measure LOS clearance at failed viewpoints | probe_los_threshold.py, test_results.txt | No matched commit command/output |
| [C011](#C011) · `bffd3d5` | Freeze failing policy for reproducible LOS probes | debug_policy.py, probe_los_threshold.py, probe_policy_old.py, test_results.txt | No matched commit command/output |
| [C012](#C012) · `269b560` | Abandon inaccessible sample targets after collision recovery | approach.py, probe_lander.py | [E0052](01_timeline.md#E0052) |
| [C013](#C013) · `439dd02` | Test other rover as radio occluder | probe_rover_los.py, test_results_more.txt | No matched commit command/output |
| [C014](#C014) · `54bd720` | Measure radio distance cutoff and complete obstacle clearances | probe_lander_exact.py, probe_send_distance.py, test_results_more.txt | No matched commit command/output |
| [C015](#C015) · `6649200` | Refine lander footprint and sight clearance; shorten return paths | approach.py, approach_backup.py, probe_lander_exact.py, test_results_more.txt | [E0065](01_timeline.md#E0065) |
| [C016](#C016) · `cd725ec` | Record lander footprint probes for accurate rover navigation | test_many.txt, test_refined.txt, test_results_more.txt | No matched commit command/output |
| [C017](#C017) · `85c2ab8` | Avoid ambiguous sample pickups and clear stores before resampling | approach.py, test_many.txt, test_refined.txt, test_results_more.txt | [E0054](01_timeline.md#E0054) |
| [C018](#C018) · `d8327f3` | Add seed-sweep diagnostics for rejected operators and policy time | test_many.txt, test_refined.txt, test_stats.py | [E0094](01_timeline.md#E0094) |
| [C019](#C019) · `26c1504` | Plan cooperative task tours to balance rover completion times | approach.py, approach_greedy.py, stats200.txt, task_planner.py, test_many.txt, test_refined.txt | [E0091](01_timeline.md#E0091) |
| [C020](#C020) · `3c218ac` | Keep viewpoints beside objectives near pillars and plan consecutive samples | approach.py, inspect_seed.py, stats200.txt, stats_planned.txt | [E0080](01_timeline.md#E0080) |
| [C021](#C021) · `f656838` | Add controlled comparison against updated greedy task allocation | approach_no_plan.py, stats200.txt, stats_planned.txt, test_stats.py | [E0109](01_timeline.md#E0109) |
| [C022](#C022) · `a0bdce6` | Reassign work globally when a scheduled route proves inaccessible | approach.py, inspect_collision.py, probe_pillar.py, stats200.json, stats200.txt, stats_greedy.txt, stats_planned.json, stats_planned.txt, stats_planned2.txt | [E0096](01_timeline.md#E0096) |
| [C023](#C023) · `71a6844` | Pipeline photographs and transmissions into travel toward home | approach.py, approach_planned_before_pipeline.py, stats_greedy.txt, stats_planned2.txt | [E0111](01_timeline.md#E0111) |
| [C024](#C024) · `e59551b` | Add black-box probes of tall pillar collision footprint | probe_pillar_axis.py, probe_pillar_shape.py, stats_greedy.json, stats_greedy.txt, stats_pipeline.txt, stats_planned2.json, stats_planned2.txt | No matched commit command/output |
| [C025](#C025) · `fb1bd76` | Model the measured octagonal rover clearance around tall pillars | approach.py, approach_pipeline.py, stats_pipeline.json, stats_pipeline.txt | [E0126](01_timeline.md#E0126) |
| [C026](#C026) · `f862c53` | Bound tour enumeration for larger objective-count variants | stats_final2000.txt, stats_final4.txt, stats_final400.txt, stats_octagon.txt, task_planner.py | [E0124](01_timeline.md#E0124) |
| [C027](#C027) · `fc2780d` | Add reset-state screening for tight or unreachable configurations | scan_states.py, stats_final2000.txt, stats_final4.txt, stats_final400.txt, stats_octagon.txt | [E0136](01_timeline.md#E0136) |
| [C028](#C028) · `26a6f98` | Recover from exhausted viewpoints and stalled local navigation | approach.py, scan_results.json, scan_results.txt, stats_final2000.json, stats_final2000.txt, stats_final4.json, stats_final4.txt, stats_final400.txt, stats_octagon.json, stats_oct… | [E0140](01_timeline.md#E0140) |
| [C029](#C029) · `614fb3c` | Probe lander-trapped stones across rover headings on seed 5828 | probe_trapped_samples.py, stats_final400.json, stats_final400.txt, stats_recovery.txt | No matched commit command/output |
| [C030](#C030) · `460ec4f` | Remember successful radio locations for later sample transmissions | approach.py, stats_recovery.json, stats_recovery.txt | [E0170](01_timeline.md#E0170) |
| [C031](#C031) · `1829c5e` | Attribute confirmed radio visibility only to uniquely held results | approach.py | [E0172](01_timeline.md#E0172) |
| [C032](#C032) · `adfe956` | Distinguish opportunistic radio attempts from failures at planned viewpoints | approach.py, probe_dynamic_radio.py, probe_radio_memory.py | [E0178](01_timeline.md#E0178) |
| [C033](#C033) · `637c0df` | Verify radio viewpoints remain valid with second rover parked at home | probe_dynamic_radio.py | No matched commit command/output |
| [C034](#C034) · `3bb0c61` | Add action-contract and repeated-reset validation | stats_final_latest.txt, stats_final_latest4.txt, test_reuse.py | [E0187](01_timeline.md#E0187) |
| [C035](#C035) · `2e04144` | Keep final policy, reproducible tests, and validation evidence | approach_backup.py, approach_greedy.py, approach_no_plan.py, approach_pipeline.py, approach_planned_before_pipeline.py, debug_policy.py, inspect_collision.py, inspect_env.py, insp… | [E0191](01_timeline.md#E0191) |
| [C036](#C036) · `59cede1` | Try nearby radio alternatives before revisiting a distant confirmed location | approach.py, stats_final_latest.json, stats_final_latest.txt, stats_final_latest4.json, stats_final_latest4.txt | [E0200](01_timeline.md#E0200) |
| [C037](#C037) · `b628d28` | Record final release validation and the empirically infeasible sample layout | VALIDATION.md, stats_final_latest.json, stats_final_latest.txt, stats_final_latest4.json, stats_final_latest4.txt, stats_release.json, stats_release4.json | [E0215](01_timeline.md#E0215) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `7701bbc3292d4f83d0d0cddefa29dd28a5e26eb2`; parents: none (initial snapshot). Recorded author date: 2026-09-21T22:01:48+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_7701bbc.diff)

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
index 0000000..a2e6047
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "8b6eedde3cb14cc8483f40c5cec19341", "observation_space": {"type": "ObjectCentric", "types": [{"name": "lander", "parent": null, "features": ["x", "y", "z"]}, {"name": "objective", "parent": null, "features": ["x", "y", "z", "have_image_rover0", "have_image_rover1", "received_image"]}, {"name": "obstacle", "parent": null, "features": ["x", "y", "z", "half_x", "half_y", "half_z"]}, {"name": "rover", "parent": null, "features": ["x", "y", "theta", "store_full", "calibrated", "at_home"]}, {"name": "sample", "parent": null, "features": ["x", "y", "z", "is_soil", "analyzed_rover0", "analyzed_rover1", "received_analysis"]}]}, "action_space": {"type": "Box", "shape": [8], "low": [-0.20000000298023224, -0.20000000298023224, -0.4000000059604645, -1.0, -0.20000000298023224, -0.20000000298023224, -0.4000000059604645, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.4000000059604645, 1.0, 0.20000000298023224, 0.20000000298023224, 0.4000000059604645, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Add independent visibility and operator probe

Commit `378927f98bb60d2e18ec47e6e6f56cbc688b2c7a`; parents: 7701bbc3292d4f83d0d0cddefa29dd28a5e26eb2. Recorded author date: 2026-09-21T22:03:40+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C002_378927f.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/inspect_env.py b/inspect_env.py
new file mode 100644
index 0000000..12ec7cb
--- /dev/null
+++ b/inspect_env.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +E=make_env(); s,i=E.reset(seed=0)
           4 +print('INFO',i,'max',E.max_steps)
           5 +for name in s.get_object_names():
           6 + o=s.get_object_from_name(name)
           7 + print(name,{f:s.get(o,f) for f in E.observation_space.type_features[o.type]})
           8 +for op in [-.5,-1/6,.5]:
           9 + a=np.zeros(8);a[3]=a[7]=op
          10 + s,r,t,tr,i=E.step(a)
          11 + print('OP',op,[(n, {f:s.get(s.get_object_from_name(n),f) for f in E.observation_space.type_features[s.get_object_from_name(n).type]}) for n in s.get_object_names() if n.startswith(('rover','objective'))])
          12 +E.close()
diff --git a/probe_motion.py b/probe_motion.py
new file mode 100644
index 0000000..d6c986d
--- /dev/null
+++ b/probe_motion.py
@@ -0,0 +1,28 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def vals(s,n='rover0'):
           5 + o=s.get_object_from_name(n);return [s.get(o,f) for f in ['x','y','theta','at_home']]
           6 +def step(e,dx=0,dy=0,dt=0):
           7 + a=np.zeros(8);a[:3]=[dx,dy,dt];t,*_=e.step(a);return t
           8 +for y in [-2.30,-2.25,-2.2,-2,-1.5,-1,-.5,0,.5,1,1.5,1.75,2,2.25,2.3]:
           9 + e=make_env();s,_=e.reset(seed=0)
          10 + while abs(vals(s)[1]-y)>.001:
          11 +  old=vals(s);s=step(e,dy=np.clip(y-old[1],-.2,.2))
          12 +  if vals(s)==old:break
          13 + for _ in range(20):
          14 +  old=vals(s);s=step(e,dx=-.05)
          15 +  if vals(s)==old:break
          16 + print('wall scan',y,vals(s))
          17 + e.close()
          18 +for mode in ['east','south','wall','home']:
          19 + e=make_env();s,_=e.reset(seed=0)
          20 + for k in range(160):
          21 +  old=vals(s)
          22 +  if mode=='east':s=step(e,dx=.01)
          23 +  if mode=='south':s=step(e,dy=-.01)
          24 +  if mode=='wall':s=step(e,dx=-.01)
          25 +  if mode=='home':s=step(e,dx=.01)
          26 +  if vals(s)==old or (mode=='home' and vals(s)[-1]==0):break
          27 + print('exact',mode,vals(s),k)
          28 + e.close()
diff --git a/probe_shape.py b/probe_shape.py
new file mode 100644
index 0000000..7327995
--- /dev/null
+++ b/probe_shape.py
@@ -0,0 +1,18 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def p(s):
           5 + o=s.get_object_from_name('rover0');return np.array([s.get(o,'x'),s.get(o,'y')])
           6 +def step(e,s,dx=0,dy=0):
           7 + a=np.zeros(8);a[:2]=[dx,dy];t,*_=e.step(a);return t
           8 +for y in [-.1987184,.0312816,.0212816,.0112816,-.4287184,1.60,1.57,1.58,1.59,1.60,1.62,1.64,1.68,1.70,1.73,1.75,2.0]:
           9 + e=make_env();s,_=e.reset(seed=0)
          10 + for k in range(30):
          11 +  d=np.clip(y-p(s)[1],-.2,.2)
          12 +  if abs(d)<1e-6:break
          13 +  s=step(e,s,dy=d)
          14 + for k in range(130):
          15 +  old=p(s);s=step(e,s,dx=-.005)
          16 +  if np.allclose(p(s),old):break
          17 + print(y,p(s))
          18 + e.close()
diff --git a/probe_visibility.py b/probe_visibility.py
new file mode 100644
index 0000000..ebfbe1d
--- /dev/null
+++ b/probe_visibility.py
@@ -0,0 +1,28 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +
           4 +def run(seed=0):
           5 + env=make_env(); s,_=env.reset(seed=seed)
           6 + rs=[s.get_object_from_name('rover'+str(i)) for i in range(2)]
           7 + def xy(i):return np.array([s.get(rs[i],f) for f in ('x','y')])
           8 + def step(i,op=0,d=(0,0)):
           9 +  nonlocal s
          10 +  a=np.zeros(8,np.float32);a[4*i:4*i+2]=d;a[4*i+3]=op
          11 +  s,*_=env.step(a)
          12 + def go(i,target):
          13 +  for _ in range(50):
          14 +   p=xy(i);d=np.clip(np.array(target)-p,-.2,.2)
          15 +   if np.max(np.abs(d))<1e-5:return True
          16 +   step(i,d=d)
          17 +   if np.linalg.norm(xy(i)-p)<1e-5:print('blocked',i,xy(i),target);return False
          18 + def ims():return [(o.name,int(s.get(o,'have_image_rover0')),int(s.get(o,'have_image_rover1')),int(s.get(o,'received_image'))) for o in s.get_objects(env.observation_space.get_type('objective'))]
          19 + go(0,(1,.5));step(0,-.5);step(0,-1/6);step(0,-.5);step(0,-1/6);print('photo',xy(0),ims())
          20 + step(0,.5);print('send high',ims())
          21 + go(0,(1,-1.75));step(0,.5);print('send home',ims())
          22 + go(1,(-1.4,-.1));step(1,-5/6);print('sample at',xy(1),[(o.name,int(s.get(o,'analyzed_rover1'))) for o in s.get_objects(env.observation_space.get_type('sample'))])
          23 + go(1,(-1.4,0));step(1,-5/6);step(1,.5);print('sample/send',xy(1),[(o.name,int(s.get(o,'analyzed_rover1')),int(s.get(o,'received_analysis'))) for o in s.get_objects(env.observation_space.get_type('sample'))])
          24 + step(1,5/6);print('drop',s.get(rs[1],'store_full'))
          25 + go(1,(-1.8,.35));step(1,-.5);step(1,-1/6);print('left photo',xy(1),ims())
          26 + go(0,(.4,-1.75));go(0,(-.4,-1.75));print('cross bottom',xy(0))
          27 + env.close()
          28 +run()
```

</details>

<a id="C003"></a>
### C003 · Probe cross-divider camera visibility

Commit `18ba3c49b0fb0791a401f4a7ff6c873ee09f0611`; parents: 378927f98bb60d2e18ec47e6e6f56cbc688b2c7a. Recorded author date: 2026-09-21T22:04:07+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C003_18ba3c4.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_crosslos.py b/probe_crosslos.py
new file mode 100644
index 0000000..b227ce0
--- /dev/null
+++ b/probe_crosslos.py
@@ -0,0 +1,18 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +e=make_env();s,_=e.reset(seed=0);rs=[s.get_object_from_name('rover'+str(i)) for i in range(2)]
           4 +def xy(i):return np.array([s.get(rs[i],f) for f in ('x','y')])
           5 +def st(i,op=0,d=(0,0)):
           6 + global s
           7 + a=np.zeros(8,np.float32);a[4*i:4*i+2]=d;a[4*i+3]=op;s,*_=e.step(a)
           8 +def go(i,p):
           9 + for t in range(40):
          10 +  d=np.clip(np.array(p)-xy(i),-.2,.2)
          11 +  if np.max(abs(d))<1e-5:return
          12 +  old=xy(i);st(i,d=d)
          13 +  if np.linalg.norm(xy(i)-old)<1e-5:print('blocked',old,p);return
          14 +for p in [(-1.5,-.3),(-1.8,.8),(-1.1,1.2),(-.4,1.2)]:go(1,p)
          15 +for j in range(5):
          16 + st(1,-.5);st(1,-1/6)
          17 + print('cross photos',xy(1),[(o.name,s.get(o,'have_image_rover1')) for o in s.get_objects(e.observation_space.get_type('objective'))])
          18 +e.close()
```

</details>

<a id="C004"></a>
### C004 · Implement initial object-centric navigation and cooperative task policy

Commit `a7bf7fd9a6e6a29b23e8478d2abb92c0b964399c`; parents: 18ba3c49b0fb0791a401f4a7ff6c873ee09f0611. Recorded author date: 2026-09-21T22:04:30+02:00.

File roles (automatic): policy.

- [E0018](01_timeline.md#E0018): commit hash in recorded output.
[Controller after this commit](evidence/versions/C004_a7bf7fd_approach.py) · [Exact all-file diff](evidence/diffs/C004_a7bf7fd.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..52884a2
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,182 @@
           1 +import math
           2 +import heapq
           3 +import numpy as np
           4 +
           5 +
           6 +class GeneratedApproach:
           7 +    """Feedback navigation and task allocation for the two rovers."""
           8 +    def __init__(self, action_space, observation_space, primitives):
           9 +        self.space = observation_space
          10 +        self.types = {t.name: t for t in observation_space.types}
          11 +
          12 +    def objects(self, state, kind):
          13 +        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
          14 +
          15 +    def xy(self, state, obj):
          16 +        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
          17 +
          18 +    def reset(self, state, info):
          19 +        self.rovers = self.objects(state, 'rover')
          20 +        self.objectives = self.objects(state, 'objective')
          21 +        self.samples = self.objects(state, 'sample')
          22 +        self.home = [self.xy(state, r) for r in self.rovers]
          23 +        self.lander = self.xy(state, self.objects(state, 'lander')[0])
          24 +        self.rects = []
          25 +        self.occluders = []
          26 +        for o in self.objects(state, 'obstacle'):
          27 +            p = self.xy(state, o)
          28 +            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
          29 +            self.rects.append((p-h-.19, p+h+.19))
          30 +            if state.get(o, 'half_z') > .1:
          31 +                self.occluders.append((p-h, p+h))
          32 +        self.rects.append((np.array([-.24, -1.69]), np.array([.24, 1.69])))
          33 +        self.occluders.append((np.array([-.05,-1.5]),np.array([.05,1.5])))
          34 +        self.rects.append((self.lander-np.array([.5,.4]),self.lander+np.array([.5,.4])))
          35 +        axis = np.arange(-2.3, 2.301, .1)
          36 +        self.size = len(axis)
          37 +        xx, yy = np.meshgrid(axis, axis)
          38 +        self.points = np.column_stack([xx.ravel(), yy.ravel()])
          39 +        self.free = self.valid(self.points)
          40 +        self.masks = {}
          41 +        for k, o in enumerate(self.objectives):
          42 +            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
          43 +        for k, o in enumerate(self.samples):
          44 +            self.masks[('sample',k)] = self.free & (np.linalg.norm(self.points-self.xy(state,o),axis=1)<.235)
          45 +        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.95)
          46 +        self.tasks = [None,None]
          47 +        self.paths = [[],[]]
          48 +        self.previous = [None,None]
          49 +        self.fail = [0,0]
          50 +        self.tick = 0
          51 +
          52 +    def valid(self, pts):
          53 +        good = np.all(np.abs(pts) <= 2.31, axis=-1)
          54 +        for lo,hi in self.rects:
          55 +            good &= ~np.all((pts >= lo) & (pts <= hi),axis=-1)
          56 +        return good
          57 +
          58 +    def visible(self, pts, target, radius):
          59 +        good = np.linalg.norm(pts-target,axis=1)<radius
          60 +        d = target-pts
          61 +        for lo,hi in self.occluders:
          62 +            inv = np.divide(1.,d,out=np.full_like(d,1e10),where=np.abs(d)>1e-10)
          63 +            a=(lo-pts)*inv; b=(hi-pts)*inv
          64 +            enter=np.max(np.minimum(a,b),axis=1)
          65 +            leave=np.min(np.maximum(a,b),axis=1)
          66 +            good &= ~((leave>=np.maximum(enter,0)) & (enter<=1) & (leave>=0))
          67 +        return good
          68 +
          69 +    def route(self, start, mask, other=None):
          70 +        # A multi-goal Dijkstra on a small occupancy grid.
          71 +        free=self.free.copy()
          72 +        if other is not None:
          73 +            free &= np.linalg.norm(self.points-other,axis=1)>.4
          74 +        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
          75 +        root=next((int(j) for j in starts if free[j]),int(starts[0]))
          76 +        dist={root:0.}; parent={}; queue=[(0.,root)]
          77 +        n=self.size
          78 +        end=None
          79 +        while queue:
          80 +            cost,j=heapq.heappop(queue)
          81 +            if cost!=dist[j]: continue
          82 +            if mask[j]: end=j;break
          83 +            x=j%n;y=j//n
          84 +            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
          85 +                nx=x+dx;ny=y+dy
          86 +                if nx<0 or nx>=n or ny<0 or ny>=n:continue
          87 +                k=ny*n+nx
          88 +                if not free[k]:continue
          89 +                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
          90 +                v=cost+1.
          91 +                if v<dist.get(k,1e9):
          92 +                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
          93 +        if end is None:return [],1e6
          94 +        path=[end]
          95 +        while path[-1]!=root:path.append(parent[path[-1]])
          96 +        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
          97 +
          98 +    def have(self,s,k):
          99 +        o=self.objectives[k]
         100 +        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
         101 +
         102 +    def needed(self,s):
         103 +        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
         104 +
         105 +    def pending(self,s,r):
         106 +        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
         107 +
         108 +    def completed(self,s,r,task):
         109 +        kind,k=task
         110 +        if kind=='image':return self.have(s,k)
         111 +        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
         112 +        if kind=='send':return not self.pending(s,r)
         113 +        return s.get(self.rovers[r],'at_home')>.5
         114 +
         115 +    def choose(self,s,r,p,other):
         116 +        candidates=[]
         117 +        reserved=self.tasks[1-r]
         118 +        need=self.needed(s)
         119 +        for k,o in enumerate(self.objectives):
         120 +            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
         121 +        if s.get(self.rovers[r],'store_full')<.5:
         122 +            for k,o in enumerate(self.samples):
         123 +                soil=int(s.get(o,'is_soil'))
         124 +                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
         125 +        best=None;score=1e9;path=[]
         126 +        for task in candidates:
         127 +            pp,cost=self.route(p,self.masks[task],other)
         128 +            cost+=2 if task[0]=='image' else 0
         129 +            if cost<score:best=task;score=cost;path=pp
         130 +        if best is None:
         131 +            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
         132 +            else:
         133 +                best=('home',r)
         134 +                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
         135 +                path,_=self.route(p,mask,other)
         136 +                path.append(self.home[r].copy())
         137 +        self.tasks[r]=best;self.paths[r]=path
         138 +
         139 +    def get_action(self, state):
         140 +        s=state; self.tick+=1
         141 +        action=np.zeros(8,dtype=np.float32)
         142 +        pos=[self.xy(s,r) for r in self.rovers]
         143 +        for r in range(2):
         144 +            p=pos[r];rob=self.rovers[r]
         145 +            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
         146 +                self.fail[r]+=1
         147 +            else:self.fail[r]=0
         148 +            task=self.tasks[r]
         149 +            if task is None or self.completed(s,r,task):
         150 +                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         151 +            if self.fail[r]>=2:
         152 +                self.paths[r]=[]
         153 +                # Infer blocked configuration and route around it.
         154 +                blocked=p+self.previous[r][1]
         155 +                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
         156 +                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
         157 +                else:mask=self.masks[task]
         158 +                self.paths[r],_=self.route(p,mask,pos[1-r])
         159 +                if task[0]=='home':self.paths[r].append(self.home[r].copy())
         160 +                self.fail[r]=0
         161 +            path=self.paths[r]
         162 +            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
         163 +            dest=p.copy()
         164 +            for point in path[:5]:
         165 +                d=point-p
         166 +                if np.max(np.abs(d))>.20001:break
         167 +                probes=p+np.linspace(0,1,5)[:,None]*d
         168 +                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy()
         169 +                else:break
         170 +            d=np.clip(dest-p,-.2,.2)
         171 +            q=p+d
         172 +            op=0.
         173 +            kind,k=task
         174 +            if kind=='sample' and np.linalg.norm(q-self.xy(s,self.samples[k]))<.247:op=-5/6
         175 +            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
         176 +                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
         177 +            elif kind=='send' and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
         178 +            if op==0 and s.get(rob,'store_full')>.5:op=5/6
         179 +            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
         180 +            action[r*4:r*4+2]=d;action[r*4+3]=op
         181 +            self.previous[r]=(p.copy(),d.copy())
         182 +        return action
```

</details>

<a id="C005"></a>
### C005 · Use measured circular clearance and ignore divider for visibility

Commit `1d68b469bdfbc952768e2221ec21d6f027e4f5f1`; parents: a7bf7fd9a6e6a29b23e8478d2abb92c0b964399c. Recorded author date: 2026-09-21T22:05:00+02:00.

File roles (automatic): diagnostic/test.

- [E0020](01_timeline.md#E0020): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C005_1d68b46.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..9bc5eea
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,18 @@
           1 +import time
           2 +import argparse
           3 +import json
           4 +from env_client import make_env
           5 +from approach import GeneratedApproach
           6 +p=argparse.ArgumentParser();p.add_argument('--start',type=int,default=0);p.add_argument('--n',type=int,default=10);p.add_argument('--count',type=int);p.add_argument('--limit',type=int,default=250);p.add_argument('--verbose',action='store_true');args=p.parse_args()
           7 +for seed in range(args.start,args.start+args.n):
           8 + e=make_env();s,info=e.reset(seed=seed,options={'object_count':args.count} if args.count is not None else None);a=GeneratedApproach(e.action_space,e.observation_space,{})
           9 + t=time.time();a.reset(s,info);success=False
          10 + for k in range(args.limit):
          11 +  ac=a.get_action(s);s,r,term,trunc,i=e.step(ac)
          12 +  if args.verbose and (k%10==0 or term):
          13 +   print(seed,k,'pos',[a.xy(s,ro).round(3).tolist() for ro in a.rovers],'task',a.tasks,'ops',ac[[3,7]].round(2),'images',[(o.name,int(s.get(o,'received_image'))) for o in a.objectives],flush=True)
          14 +  if term or trunc:success=term;break
          15 + print('RESULT',seed,info,success,k+1,round(time.time()-t,3),flush=True)
          16 + if not success:
          17 +  print('FAILED',a.tasks,[(o.name,{f:s.get(o,f) for f in e.observation_space.type_features[o.type]}) for o in a.rovers+a.objectives+a.samples],flush=True)
          18 + e.close()
```

</details>

<a id="C006"></a>
### C006 · Correct measured collision model and waypoint advancement

Commit `b6f4ab5dd349144cc916babddd5bcce53b6d150e`; parents: 1d68b469bdfbc952768e2221ec21d6f027e4f5f1. Recorded author date: 2026-09-21T22:05:28+02:00.

File roles (automatic): policy.

- [E0022](01_timeline.md#E0022): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_b6f4ab5_approach.py) · [Exact all-file diff](evidence/diffs/C006_b6f4ab5.diff)

[Previous saved controller snapshot](evidence/versions/C004_a7bf7fd_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 52884a2..e24294f 100644
--- a/approach.py
+++ b/approach.py
@@ -26,13 +26,12 @@ class GeneratedApproach:
   26     26          for o in self.objects(state, 'obstacle'):
   27     27              p = self.xy(state, o)
   28     28              h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
   29        -            self.rects.append((p-h-.19, p+h+.19))
          29 +            self.rects.append((p-h, p+h))
   30     30              if state.get(o, 'half_z') > .1:
   31     31                  self.occluders.append((p-h, p+h))
   32        -        self.rects.append((np.array([-.24, -1.69]), np.array([.24, 1.69])))
   33        -        self.occluders.append((np.array([-.05,-1.5]),np.array([.05,1.5])))
   34        -        self.rects.append((self.lander-np.array([.5,.4]),self.lander+np.array([.5,.4])))
   35        -        axis = np.arange(-2.3, 2.301, .1)
          32 +        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
          33 +        self.rects.append((self.lander-np.array([.3,.25]),self.lander+np.array([.3,.25])))
          34 +        axis = np.arange(-2.2, 2.201, .1)
   36     35          self.size = len(axis)
   37     36          xx, yy = np.meshgrid(axis, axis)
   38     37          self.points = np.column_stack([xx.ravel(), yy.ravel()])
@@ -50,9 +49,9 @@ class GeneratedApproach:
   50     49          self.tick = 0
   51     50  
   52     51      def valid(self, pts):
   53        -        good = np.all(np.abs(pts) <= 2.31, axis=-1)
          52 +        good = np.all(np.abs(pts) <= 2.265, axis=-1)
   54     53          for lo,hi in self.rects:
   55        -            good &= ~np.all((pts >= lo) & (pts <= hi),axis=-1)
          54 +            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
   56     55          return good
   57     56  
   58     57      def visible(self, pts, target, radius):
@@ -126,7 +125,7 @@ class GeneratedApproach:
  126    125          for task in candidates:
  127    126              pp,cost=self.route(p,self.masks[task],other)
  128    127              cost+=2 if task[0]=='image' else 0
  129        -            if cost<score:best=task;score=cost;path=pp
         128 +            if cost<score and cost<1e5:best=task;score=cost;path=pp
  130    129          if best is None:
  131    130              if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
  132    131              else:
@@ -161,12 +160,14 @@ class GeneratedApproach:
  161    160              path=self.paths[r]
  162    161              while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
  163    162              dest=p.copy()
  164        -            for point in path[:5]:
         163 +            selected=-1
         164 +            for pi,point in enumerate(path[:5]):
  165    165                  d=point-p
  166    166                  if np.max(np.abs(d))>.20001:break
  167    167                  probes=p+np.linspace(0,1,5)[:,None]*d
  168        -                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy()
         168 +                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
  169    169                  else:break
         170 +            if selected>0:del path[:selected]
  170    171              d=np.clip(dest-p,-.2,.2)
  171    172              q=p+d
  172    173              op=0.
```

</details>

<a id="C007"></a>
### C007 · Add targeted LOS failure probes

Commit `49b61ec7cf7b038108ad1f8971d959c615428e9d`; parents: b6f4ab5dd349144cc916babddd5bcce53b6d150e. Recorded author date: 2026-09-21T22:06:24+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C007_49b61ec.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_los_details.py b/probe_los_details.py
new file mode 100644
index 0000000..f493bbb
--- /dev/null
+++ b/probe_los_details.py
@@ -0,0 +1,20 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +for seed in [2,3,4]:
           5 + e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
           6 + for t in range(65):s,*_=e.step(p.get_action(s))
           7 + print('\nSEED',seed,'tasks',p.tasks)
           8 + for r,rob in enumerate(p.rovers):
           9 +  x=p.xy(s,rob);print('rover',r,x,'cal',s.get(rob,'calibrated'))
          10 +  task=p.tasks[r]
          11 +  target=p.lander if task[0]=='send' else p.xy(s,p.objectives[task[1]]) if task[0]=='image' else x
          12 +  d=target-x;print('target',target,'dist',np.linalg.norm(d))
          13 +  for ob in p.objects(s,'obstacle'):
          14 +   q=p.xy(s,ob);a=np.clip(np.dot(q-x,d)/(np.dot(d,d)+1e-20),0,1);dl=np.linalg.norm(q-x-a*d)
          15 +   if dl<.5:print('near LOS',ob.name,q,'distance',dl,'t',a,'half',s.get(ob,'half_x'),s.get(ob,'half_z'))
          16 +  for delta in [(0,0),(.1,0),(.1,0),(0,.1),(-.1,0),(-.1,0),(-.1,0),(0,-.1),(0,-.1)]:
          17 +   a=np.zeros(8,np.float32);a[r*4:r*4+2]=delta;a[r*4+3]=-.5 if task[0]=='image' else .5
          18 +   s,*_=e.step(a)
          19 +   print('probe',r,p.xy(s,rob),'cal',s.get(rob,'calibrated'),'pending',p.pending(s,r))
          20 + e.close()
```

</details>

<a id="C008"></a>
### C008 · Replan after refused camera and radio operators

Commit `a8268521380e8410f70f4de5064ba1446e852ee6`; parents: 49b61ec7cf7b038108ad1f8971d959c615428e9d. Recorded author date: 2026-09-21T22:06:26+02:00.

File roles (automatic): policy.

- [E0026](01_timeline.md#E0026): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_a826852_approach.py) · [Exact all-file diff](evidence/diffs/C008_a826852.diff)

[Previous saved controller snapshot](evidence/versions/C006_b6f4ab5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e24294f..ac5c7f3 100644
--- a/approach.py
+++ b/approach.py
@@ -47,6 +47,8 @@ class GeneratedApproach:
   47     47          self.previous = [None,None]
   48     48          self.fail = [0,0]
   49     49          self.tick = 0
          50 +        self.last_op = [None, None]
          51 +        self.bad_views = {}
   50     52  
   51     53      def valid(self, pts):
   52     54          good = np.all(np.abs(pts) <= 2.265, axis=-1)
@@ -135,6 +137,9 @@ class GeneratedApproach:
  135    137                  path.append(self.home[r].copy())
  136    138          self.tasks[r]=best;self.paths[r]=path
  137    139  
         140 +    def result_count(self, s, r):
         141 +        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
         142 +
  138    143      def get_action(self, state):
  139    144          s=state; self.tick+=1
  140    145          action=np.zeros(8,dtype=np.float32)
@@ -145,6 +150,15 @@ class GeneratedApproach:
  145    150                  self.fail[r]+=1
  146    151              else:self.fail[r]=0
  147    152              task=self.tasks[r]
         153 +            last=self.last_op[r]
         154 +            if last is not None:
         155 +                old_task, old_p, old_op, old_count = last
         156 +                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
         157 +                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
         158 +                          (old_op == .5 and self.pending(s,r)))
         159 +                if failed and task==old_task and task[0] in ('image','send'):
         160 +                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
         161 +                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
  148    162              if task is None or self.completed(s,r,task):
  149    163                  self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  150    164              if self.fail[r]>=2:
@@ -175,9 +189,12 @@ class GeneratedApproach:
  175    189              if kind=='sample' and np.linalg.norm(q-self.xy(s,self.samples[k]))<.247:op=-5/6
  176    190              elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
  177    191                  op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
         192 +                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
  178    193              elif kind=='send' and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
         194 +                if path and np.linalg.norm(q-path[-1])>.06:op=0.
  179    195              if op==0 and s.get(rob,'store_full')>.5:op=5/6
  180    196              elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
  181    197              action[r*4:r*4+2]=d;action[r*4+3]=op
  182    198              self.previous[r]=(p.copy(),d.copy())
         199 +            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
  183    200          return action
```

</details>

<a id="C009"></a>
### C009 · Correct operator recovery dispatch and syntax

Commit `6f08fb938dca82e5e4bd83a862dae0772733d474`; parents: a8268521380e8410f70f4de5064ba1446e852ee6. Recorded author date: 2026-09-21T22:06:43+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0031](01_timeline.md#E0031): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_6f08fb9_approach.py) · [Exact all-file diff](evidence/diffs/C009_6f08fb9.diff)

[Previous saved controller snapshot](evidence/versions/C008_a826852_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ac5c7f3..37b0767 100644
--- a/approach.py
+++ b/approach.py
@@ -155,7 +155,7 @@ class GeneratedApproach:
  155    155                  old_task, old_p, old_op, old_count = last
  156    156                  failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
  157    157                            (old_op == -1/6 and self.result_count(s,r)<=old_count) or
  158        -                          (old_op == .5 and self.pending(s,r)))
         158 +                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
  159    159                  if failed and task==old_task and task[0] in ('image','send'):
  160    160                      self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
  161    161                      self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
@@ -190,7 +190,8 @@ class GeneratedApproach:
  190    190              elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
  191    191                  op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  192    192                  if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
  193        -            elif kind=='send' and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
         193 +            elif kind=='send' and self.visible(q[None,:],self.lander,3.99)[0]:
         194 +                op=.5
  194    195                  if path and np.linalg.norm(q-path[-1])>.06:op=0.
  195    196              if op==0 and s.get(rob,'store_full')>.5:op=5/6
  196    197              elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
diff --git a/test_results.txt b/test_results.txt
new file mode 100644
index 0000000..e69de29
```

</details>

<a id="C010"></a>
### C010 · Measure LOS clearance at failed viewpoints

Commit `4581e651025a7513e21f15a918cd728c1da73649`; parents: 6f08fb938dca82e5e4bd83a862dae0772733d474. Recorded author date: 2026-09-21T22:07:10+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C010_4581e65.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_los_threshold.py b/probe_los_threshold.py
new file mode 100644
index 0000000..a9d4f7b
--- /dev/null
+++ b/probe_los_threshold.py
@@ -0,0 +1,18 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +for seed,rr,points in [(4,1,[(-1.8,0),(-1.75,0),(-1.7,0),(-1.65,0),(-1.6,0)]),(3,0,[(1.4,.1),(1.3,.1),(1.3,.2),(1.2,.1)])]:
           5 + for pt in points:
           6 +  e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
           7 +  for t in range(55):s,*_=e.step(p.get_action(s))
           8 +  rob=p.rovers[rr]
           9 +  for t in range(6):
          10 +   a=np.zeros(8,np.float32);a[rr*4:rr*4+2]=np.clip(np.array(pt)-p.xy(s,rob),-.2,.2);a[rr*4+3]=-.5 if seed==4 else .5;s,*_=e.step(a)
          11 +  target=p.xy(s,p.objectives[2]) if seed==4 else p.lander
          12 +  start=p.xy(s,rob);d=target-start
          13 +  distances=[]
          14 +  for ob in p.objects(s,'obstacle')+p.rovers:
          15 +   if ob==rob:continue
          16 +   q=p.xy(s,ob);u=np.clip(np.dot(q-start,d)/np.dot(d,d),0,1);distances.append((round(np.linalg.norm(q-start-u*d),3),ob.name))
          17 +  print(seed,pt,'cal',s.get(rob,'calibrated'),'pending',p.pending(s,rr),'near',sorted(distances)[:4])
          18 +  e.close()
diff --git a/test_results.txt b/test_results.txt
index e69de29..f73d24f 100644
--- a/test_results.txt
+++ b/test_results.txt
@@ -0,0 +1,29 @@
           1 +RESULT 0 {'object_count': 3} True 35 0.459
           2 +RESULT 1 {'object_count': 2} True 22 0.304
           3 +RESULT 2 {'object_count': 3} True 22 0.231
           4 +RESULT 3 {'object_count': 3} True 30 0.413
           5 +RESULT 4 {'object_count': 3} True 25 0.399
           6 +RESULT 5 {'object_count': 3} True 41 0.625
           7 +RESULT 6 {'object_count': 2} True 21 0.251
           8 +RESULT 7 {'object_count': 3} True 32 0.338
           9 +RESULT 8 {'object_count': 3} True 29 0.427
          10 +RESULT 9 {'object_count': 2} True 29 0.476
          11 +RESULT 10 {'object_count': 3} True 28 0.408
          12 +RESULT 11 {'object_count': 1} True 21 0.308
          13 +RESULT 12 {'object_count': 2} True 27 0.252
          14 +RESULT 13 {'object_count': 3} True 36 0.492
          15 +RESULT 14 {'object_count': 1} True 34 0.432
          16 +RESULT 15 {'object_count': 3} True 25 0.331
          17 +RESULT 16 {'object_count': 2} True 26 0.347
          18 +RESULT 17 {'object_count': 3} True 32 0.489
          19 +RESULT 18 {'object_count': 3} True 25 0.37
          20 +RESULT 19 {'object_count': 2} True 30 0.431
          21 +RESULT 20 {'object_count': 3} True 30 0.19
          22 +RESULT 21 {'object_count': 1} True 23 0.402
          23 +RESULT 22 {'object_count': 3} True 26 0.304
          24 +RESULT 23 {'object_count': 1} True 19 0.237
          25 +RESULT 24 {'object_count': 2} True 26 0.357
          26 +RESULT 25 {'object_count': 2} True 23 0.3
          27 +RESULT 26 {'object_count': 3} True 28 0.43
          28 +RESULT 27 {'object_count': 1} True 24 0.32
          29 +RESULT 28 {'object_count': 2} True 44 0.502
```

</details>

<a id="C011"></a>
### C011 · Freeze failing policy for reproducible LOS probes

Commit `bffd3d54005bbc2dd748c49b87ffa4dffd17ebec`; parents: 4581e651025a7513e21f15a918cd728c1da73649. Recorded author date: 2026-09-21T22:07:33+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C011_bffd3d5.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/debug_policy.py b/debug_policy.py
new file mode 100644
index 0000000..c67a0cb
--- /dev/null
+++ b/debug_policy.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import sys
           4 +E=make_env();s,info=E.reset(seed=int(sys.argv[1]));A=GeneratedApproach(E.action_space,E.observation_space,{})
           5 +A.reset(s,info)
           6 +for t in range(80):
           7 + ac=A.get_action(s)
           8 + if t<15 or t%5==0:print(t, [A.xy(s,r).round(3).tolist() for r in A.rovers], A.tasks,ac.round(3).tolist(),[[(p.round(3)).tolist() for p in path[:3]] for path in A.paths],flush=True)
           9 + s,r,d,tr,i=E.step(ac)
          10 + if d:break
          11 +E.close()
diff --git a/probe_los_threshold.py b/probe_los_threshold.py
index a9d4f7b..4816ba7 100644
--- a/probe_los_threshold.py
+++ b/probe_los_threshold.py
@@ -1,6 +1,6 @@
    1      1  import numpy as np
    2      2  from env_client import make_env
    3        -from approach import GeneratedApproach
           3 +from probe_policy_old import GeneratedApproach
    4      4  for seed,rr,points in [(4,1,[(-1.8,0),(-1.75,0),(-1.7,0),(-1.65,0),(-1.6,0)]),(3,0,[(1.4,.1),(1.3,.1),(1.3,.2),(1.2,.1)])]:
    5      5   for pt in points:
    6      6    e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
diff --git a/probe_policy_old.py b/probe_policy_old.py
new file mode 100644
index 0000000..e24294f
--- /dev/null
+++ b/probe_policy_old.py
@@ -0,0 +1,183 @@
           1 +import math
           2 +import heapq
           3 +import numpy as np
           4 +
           5 +
           6 +class GeneratedApproach:
           7 +    """Feedback navigation and task allocation for the two rovers."""
           8 +    def __init__(self, action_space, observation_space, primitives):
           9 +        self.space = observation_space
          10 +        self.types = {t.name: t for t in observation_space.types}
          11 +
          12 +    def objects(self, state, kind):
          13 +        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
          14 +
          15 +    def xy(self, state, obj):
          16 +        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
          17 +
          18 +    def reset(self, state, info):
          19 +        self.rovers = self.objects(state, 'rover')
          20 +        self.objectives = self.objects(state, 'objective')
          21 +        self.samples = self.objects(state, 'sample')
          22 +        self.home = [self.xy(state, r) for r in self.rovers]
          23 +        self.lander = self.xy(state, self.objects(state, 'lander')[0])
          24 +        self.rects = []
          25 +        self.occluders = []
          26 +        for o in self.objects(state, 'obstacle'):
          27 +            p = self.xy(state, o)
          28 +            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
          29 +            self.rects.append((p-h, p+h))
          30 +            if state.get(o, 'half_z') > .1:
          31 +                self.occluders.append((p-h, p+h))
          32 +        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
          33 +        self.rects.append((self.lander-np.array([.3,.25]),self.lander+np.array([.3,.25])))
          34 +        axis = np.arange(-2.2, 2.201, .1)
          35 +        self.size = len(axis)
          36 +        xx, yy = np.meshgrid(axis, axis)
          37 +        self.points = np.column_stack([xx.ravel(), yy.ravel()])
          38 +        self.free = self.valid(self.points)
          39 +        self.masks = {}
          40 +        for k, o in enumerate(self.objectives):
          41 +            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
          42 +        for k, o in enumerate(self.samples):
          43 +            self.masks[('sample',k)] = self.free & (np.linalg.norm(self.points-self.xy(state,o),axis=1)<.235)
          44 +        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.95)
          45 +        self.tasks = [None,None]
          46 +        self.paths = [[],[]]
          47 +        self.previous = [None,None]
          48 +        self.fail = [0,0]
          49 +        self.tick = 0
          50 +
          51 +    def valid(self, pts):
          52 +        good = np.all(np.abs(pts) <= 2.265, axis=-1)
          53 +        for lo,hi in self.rects:
          54 +            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
          55 +        return good
          56 +
          57 +    def visible(self, pts, target, radius):
          58 +        good = np.linalg.norm(pts-target,axis=1)<radius
          59 +        d = target-pts
          60 +        for lo,hi in self.occluders:
          61 +            inv = np.divide(1.,d,out=np.full_like(d,1e10),where=np.abs(d)>1e-10)
          62 +            a=(lo-pts)*inv; b=(hi-pts)*inv
          63 +            enter=np.max(np.minimum(a,b),axis=1)
          64 +            leave=np.min(np.maximum(a,b),axis=1)
          65 +            good &= ~((leave>=np.maximum(enter,0)) & (enter<=1) & (leave>=0))
          66 +        return good
          67 +
          68 +    def route(self, start, mask, other=None):
          69 +        # A multi-goal Dijkstra on a small occupancy grid.
          70 +        free=self.free.copy()
          71 +        if other is not None:
          72 +            free &= np.linalg.norm(self.points-other,axis=1)>.4
          73 +        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
          74 +        root=next((int(j) for j in starts if free[j]),int(starts[0]))
          75 +        dist={root:0.}; parent={}; queue=[(0.,root)]
          76 +        n=self.size
          77 +        end=None
          78 +        while queue:
          79 +            cost,j=heapq.heappop(queue)
          80 +            if cost!=dist[j]: continue
          81 +            if mask[j]: end=j;break
          82 +            x=j%n;y=j//n
          83 +            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
          84 +                nx=x+dx;ny=y+dy
          85 +                if nx<0 or nx>=n or ny<0 or ny>=n:continue
          86 +                k=ny*n+nx
          87 +                if not free[k]:continue
          88 +                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
          89 +                v=cost+1.
          90 +                if v<dist.get(k,1e9):
          91 +                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
          92 +        if end is None:return [],1e6
          93 +        path=[end]
          94 +        while path[-1]!=root:path.append(parent[path[-1]])
          95 +        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
          96 +
          97 +    def have(self,s,k):
          98 +        o=self.objectives[k]
          99 +        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
         100 +
         101 +    def needed(self,s):
         102 +        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
         103 +
         104 +    def pending(self,s,r):
         105 +        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
         106 +
         107 +    def completed(self,s,r,task):
         108 +        kind,k=task
         109 +        if kind=='image':return self.have(s,k)
         110 +        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
         111 +        if kind=='send':return not self.pending(s,r)
         112 +        return s.get(self.rovers[r],'at_home')>.5
         113 +
         114 +    def choose(self,s,r,p,other):
         115 +        candidates=[]
         116 +        reserved=self.tasks[1-r]
         117 +        need=self.needed(s)
         118 +        for k,o in enumerate(self.objectives):
         119 +            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
         120 +        if s.get(self.rovers[r],'store_full')<.5:
         121 +            for k,o in enumerate(self.samples):
         122 +                soil=int(s.get(o,'is_soil'))
         123 +                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
         124 +        best=None;score=1e9;path=[]
         125 +        for task in candidates:
         126 +            pp,cost=self.route(p,self.masks[task],other)
         127 +            cost+=2 if task[0]=='image' else 0
         128 +            if cost<score and cost<1e5:best=task;score=cost;path=pp
         129 +        if best is None:
         130 +            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
         131 +            else:
         132 +                best=('home',r)
         133 +                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
         134 +                path,_=self.route(p,mask,other)
         135 +                path.append(self.home[r].copy())
         136 +        self.tasks[r]=best;self.paths[r]=path
         137 +
         138 +    def get_action(self, state):
         139 +        s=state; self.tick+=1
         140 +        action=np.zeros(8,dtype=np.float32)
         141 +        pos=[self.xy(s,r) for r in self.rovers]
         142 +        for r in range(2):
         143 +            p=pos[r];rob=self.rovers[r]
         144 +            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
         145 +                self.fail[r]+=1
         146 +            else:self.fail[r]=0
         147 +            task=self.tasks[r]
         148 +            if task is None or self.completed(s,r,task):
         149 +                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         150 +            if self.fail[r]>=2:
         151 +                self.paths[r]=[]
         152 +                # Infer blocked configuration and route around it.
         153 +                blocked=p+self.previous[r][1]
         154 +                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
         155 +                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
         156 +                else:mask=self.masks[task]
         157 +                self.paths[r],_=self.route(p,mask,pos[1-r])
         158 +                if task[0]=='home':self.paths[r].append(self.home[r].copy())
         159 +                self.fail[r]=0
         160 +            path=self.paths[r]
         161 +            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
         162 +            dest=p.copy()
         163 +            selected=-1
         164 +            for pi,point in enumerate(path[:5]):
         165 +                d=point-p
         166 +                if np.max(np.abs(d))>.20001:break
         167 +                probes=p+np.linspace(0,1,5)[:,None]*d
         168 +                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
         169 +                else:break
         170 +            if selected>0:del path[:selected]
         171 +            d=np.clip(dest-p,-.2,.2)
         172 +            q=p+d
         173 +            op=0.
         174 +            kind,k=task
         175 +            if kind=='sample' and np.linalg.norm(q-self.xy(s,self.samples[k]))<.247:op=-5/6
         176 +            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
         177 +                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
         178 +            elif kind=='send' and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
         179 +            if op==0 and s.get(rob,'store_full')>.5:op=5/6
         180 +            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
         181 +            action[r*4:r*4+2]=d;action[r*4+3]=op
         182 +            self.previous[r]=(p.copy(),d.copy())
         183 +        return action
diff --git a/test_results.txt b/test_results.txt
index f73d24f..3ffde72 100644
--- a/test_results.txt
+++ b/test_results.txt
@@ -27,3 +27,5 @@ RESULT 25 {'object_count': 2} True 23 0.3
   27     27  RESULT 26 {'object_count': 3} True 28 0.43
   28     28  RESULT 27 {'object_count': 1} True 24 0.32
   29     29  RESULT 28 {'object_count': 2} True 44 0.502
          30 +RESULT 29 {'object_count': 3} False 250 5.23
          31 +FAILED [('home', 0), ('sample', 4)] [('rover0', {'x': 1.0, 'y': -1.75, 'theta': -3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}), ('rover1', {'x': -2.0, 'y': -1.399999976158142, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 0.0}), ('objective0', {'x': -0.5211005806922913, 'y': 2.0225868225097656, 'z': 0.20100000500679016, 'have_image_rover0': 1.0, 'have_image_rover1': 0.0, 'received_image': 1.0}), ('objective1', {'x': -1.959802269935608, 'y': 2.032264471054077, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}), ('objective2', {'x': 0.5849767923355103, 'y': 1.883683443069458, 'z': 0.20100000500679016, 'have_image_rover0': 1.0, 'have_image_rover1': 0.0, 'received_image': 1.0}), ('sample0', {'x': 0.7705432772636414, 'y': 0.23597754538059235, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample1', {'x': 1.6593462228775024, 'y': -0.3176131248474121, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 1.0, 'analyzed_rover1': 0.0, 'received_analysis': 1.0}), ('sample2', {'x': 2.14742112159729, 'y': 1.3751660585403442, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample3', {'x': -1.9218065738677979, 'y': 0.9597395658493042, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample4', {'x': -2.344602584838867, 'y': -1.656410813331604, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample5', {'x': 0.237486332654953, 'y': -0.09099745005369186, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0})]
```

</details>

<a id="C012"></a>
### C012 · Abandon inaccessible sample targets after collision recovery

Commit `269b560e32832bf6ddcecf3a34d078aaf75a4d82`; parents: bffd3d54005bbc2dd748c49b87ffa4dffd17ebec. Recorded author date: 2026-09-21T22:07:45+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0052](01_timeline.md#E0052): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_269b560_approach.py) · [Exact all-file diff](evidence/diffs/C012_269b560.diff)

[Previous saved controller snapshot](evidence/versions/C009_6f08fb9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 37b0767..e06bda3 100644
--- a/approach.py
+++ b/approach.py
@@ -170,6 +170,9 @@ class GeneratedApproach:
  170    170                  else:mask=self.masks[task]
  171    171                  self.paths[r],_=self.route(p,mask,pos[1-r])
  172    172                  if task[0]=='home':self.paths[r].append(self.home[r].copy())
         173 +                elif not self.paths[r]:
         174 +                    self.tasks[r]=None
         175 +                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  173    176                  self.fail[r]=0
  174    177              path=self.paths[r]
  175    178              while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
diff --git a/probe_lander.py b/probe_lander.py
new file mode 100644
index 0000000..b5251fd
--- /dev/null
+++ b/probe_lander.py
@@ -0,0 +1,31 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def p(s):
           5 + o=s.get_object_from_name('rover1');return np.array([s.get(o,'x'),s.get(o,'y')])
           6 +def st(e,s,dx=0,dy=0):
           7 + a=np.zeros(8);a[4:6]=[dx,dy];t,*_=e.step(a);return t
           8 +
           9 +def goto(e,s,target):
          10 + for _ in range(50):
          11 +  d=np.clip(np.array(target)-p(s),-.1,.1)
          12 +  if np.linalg.norm(d)<1e-5:break
          13 +  old=p(s);s=st(e,s,*d)
          14 +  if np.allclose(old,p(s)):break
          15 + return s
          16 +for x in [-2.25,-2.2,-2.1,-2,-1.9,-1.8,-1.7,-1.6,-1.5,-1.4,-1.3,-1.2,-1.1]:
          17 + e=make_env();s,_=e.reset(seed=29)
          18 + s=goto(e,s,[-1,-1]);s=goto(e,s,[x,-1])
          19 + for _ in range(160):
          20 +  old=p(s);s=st(e,s,dy=-.01)
          21 +  if np.allclose(old,p(s)):break
          22 + print('vertical',x,p(s))
          23 + e.close()
          24 +for y in [-2.25,-2.2,-2.1,-2,-1.9,-1.8,-1.7,-1.6,-1.5,-1.4,-1.3]:
          25 + e=make_env();s,_=e.reset(seed=29)
          26 + s=goto(e,s,[-1,y])
          27 + for _ in range(140):
          28 +  old=p(s);s=st(e,s,dx=-.01)
          29 +  if np.allclose(old,p(s)):break
          30 + print('horizontal',y,p(s))
          31 + e.close()
```

</details>

<a id="C013"></a>
### C013 · Test other rover as radio occluder

Commit `439dd02e5a24e3c67ac01de7468b1eae99f66292`; parents: 269b560e32832bf6ddcecf3a34d078aaf75a4d82. Recorded author date: 2026-09-21T22:07:53+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C013_439dd02.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_rover_los.py b/probe_rover_los.py
new file mode 100644
index 0000000..c5ac47c
--- /dev/null
+++ b/probe_rover_los.py
@@ -0,0 +1,9 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +from probe_policy_old import GeneratedApproach
           4 +e=make_env();s,info=e.reset(seed=3);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
           5 +for _ in range(55):s,*_=e.step(p.get_action(s))
           6 +for d in [(0,0),(0,-.1),(0,-.1),(.1,0),(.1,0)]:
           7 + a=np.zeros(8,np.float32);a[4:6]=d;a[3]=.5;s,*_=e.step(a)
           8 + print(p.xy(s,p.rovers[0]),p.xy(s,p.rovers[1]),'pending',p.pending(s,0))
           9 +e.close()
diff --git a/test_results_more.txt b/test_results_more.txt
new file mode 100644
index 0000000..e543dba
--- /dev/null
+++ b/test_results_more.txt
@@ -0,0 +1,6 @@
           1 +RESULT 29 {'object_count': 3} True 34 0.645
           2 +RESULT 30 {'object_count': 1} True 22 0.367
           3 +RESULT 31 {'object_count': 2} True 32 0.92
           4 +RESULT 32 {'object_count': 3} True 28 0.923
           5 +RESULT 33 {'object_count': 3} True 34 1.012
           6 +RESULT 34 {'object_count': 1} True 21 0.805
```

</details>

<a id="C014"></a>
### C014 · Measure radio distance cutoff and complete obstacle clearances

Commit `54bd720c7e2f22cb31c900febe88a4f00a2b030e`; parents: 439dd02e5a24e3c67ac01de7468b1eae99f66292. Recorded author date: 2026-09-21T22:08:52+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C014_54bd720.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_lander_exact.py b/probe_lander_exact.py
new file mode 100644
index 0000000..5b438da
--- /dev/null
+++ b/probe_lander_exact.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +for mode in ['front','side']:
           4 + e=make_env();s,_=e.reset(seed=29);o=s.get_object_from_name('rover1')
           5 + def p():return np.array([s.get(o,'x'),s.get(o,'y')])
           6 + def st(d):
           7 +  global s
           8 +  a=np.zeros(8);a[4:6]=d;s,*_=e.step(a)
           9 + targets=[[-1,-1],[-1.9,-1],[-1.9,-1.46]] if mode=='front' else [[-1.19,-1.75]]
          10 + for target in targets:
          11 +  for k in range(50):
          12 +   d=np.clip(np.array(target)-p(),-.1,.1)
          13 +   if np.linalg.norm(d)<1e-6:break
          14 +   st(d)
          15 + for k in range(100):
          16 +  old=p();st([0,-.0001] if mode=='front' else [-.0001,0])
          17 +  if np.allclose(p(),old,atol=1e-7,rtol=0):break
          18 + print(mode,p(),k)
          19 + e.close()
diff --git a/probe_send_distance.py b/probe_send_distance.py
new file mode 100644
index 0000000..ca8481c
--- /dev/null
+++ b/probe_send_distance.py
@@ -0,0 +1,13 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +from probe_policy_old import GeneratedApproach
           4 +for pt in [(1.4,0),(1.3,.2),(1.39,.1),(1.38,.1),(1.37,.1),(1.36,.1)]:
           5 + e=make_env();s,info=e.reset(seed=3);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
           6 + for _ in range(55):s,*_=e.step(p.get_action(s))
           7 + a=np.zeros(8,np.float32);a[:2]=np.array(pt)-p.xy(s,p.rovers[0]);a[3]=.5;s,*_=e.step(a)
           8 + print(pt,'dist',np.linalg.norm(np.array(pt)-p.lander),'pending',p.pending(s,0))
           9 + if pt==(1.4,0):
          10 +  x=np.array([1.4,.1]);d=p.lander-x
          11 +  for o in p.objects(s,'obstacle'):
          12 +   q=p.xy(s,o);u=np.clip(np.dot(q-x,d)/np.dot(d,d),0,1);print(o.name,q,'dist',np.linalg.norm(q-x-u*d),'half',s.get(o,'half_x'),s.get(o,'half_z'))
          13 + e.close()
diff --git a/test_results_more.txt b/test_results_more.txt
index e543dba..a85a9c6 100644
--- a/test_results_more.txt
+++ b/test_results_more.txt
@@ -4,3 +4,62 @@ RESULT 31 {'object_count': 2} True 32 0.92
    4      4  RESULT 32 {'object_count': 3} True 28 0.923
    5      5  RESULT 33 {'object_count': 3} True 34 1.012
    6      6  RESULT 34 {'object_count': 1} True 21 0.805
           7 +RESULT 35 {'object_count': 1} True 21 0.9
           8 +RESULT 36 {'object_count': 2} True 22 0.801
           9 +RESULT 37 {'object_count': 1} True 24 0.919
          10 +RESULT 38 {'object_count': 1} True 22 0.422
          11 +RESULT 39 {'object_count': 3} True 27 0.871
          12 +RESULT 40 {'object_count': 2} True 34 0.591
          13 +RESULT 41 {'object_count': 2} True 21 0.834
          14 +RESULT 42 {'object_count': 1} True 28 0.543
          15 +RESULT 43 {'object_count': 2} True 34 0.85
          16 +RESULT 44 {'object_count': 3} True 24 0.828
          17 +RESULT 45 {'object_count': 3} True 30 1.27
          18 +RESULT 46 {'object_count': 2} True 23 0.767
          19 +RESULT 47 {'object_count': 1} True 26 1.056
          20 +RESULT 48 {'object_count': 1} True 21 0.649
          21 +RESULT 49 {'object_count': 1} True 38 1.174
          22 +RESULT 50 {'object_count': 3} True 30 0.638
          23 +RESULT 51 {'object_count': 2} True 23 0.428
          24 +RESULT 52 {'object_count': 3} True 28 0.851
          25 +RESULT 53 {'object_count': 3} True 25 0.466
          26 +RESULT 54 {'object_count': 1} True 22 0.488
          27 +RESULT 55 {'object_count': 3} True 29 0.498
          28 +RESULT 56 {'object_count': 2} True 27 0.372
          29 +RESULT 57 {'object_count': 1} True 19 0.257
          30 +RESULT 58 {'object_count': 2} True 30 0.416
          31 +RESULT 59 {'object_count': 3} True 27 0.353
          32 +RESULT 60 {'object_count': 1} True 23 0.309
          33 +RESULT 61 {'object_count': 2} True 27 0.386
          34 +RESULT 62 {'object_count': 2} True 29 0.406
          35 +RESULT 63 {'object_count': 2} True 30 0.426
          36 +RESULT 64 {'object_count': 2} True 27 0.362
          37 +RESULT 65 {'object_count': 1} True 20 0.276
          38 +RESULT 66 {'object_count': 3} True 27 0.445
          39 +RESULT 67 {'object_count': 3} True 25 0.357
          40 +RESULT 68 {'object_count': 2} True 25 0.346
          41 +RESULT 69 {'object_count': 1} True 29 0.406
          42 +RESULT 70 {'object_count': 2} True 25 0.36
          43 +RESULT 71 {'object_count': 3} True 31 0.434
          44 +RESULT 72 {'object_count': 3} True 29 0.413
          45 +RESULT 73 {'object_count': 3} True 24 0.367
          46 +RESULT 74 {'object_count': 1} True 23 0.302
          47 +RESULT 75 {'object_count': 2} True 26 0.357
          48 +RESULT 76 {'object_count': 2} True 27 0.384
          49 +RESULT 77 {'object_count': 1} True 23 0.31
          50 +RESULT 78 {'object_count': 3} True 27 0.398
          51 +RESULT 79 {'object_count': 1} True 35 0.465
          52 +RESULT 80 {'object_count': 3} True 26 0.397
          53 +RESULT 81 {'object_count': 1} True 23 0.354
          54 +RESULT 82 {'object_count': 3} True 32 0.487
          55 +RESULT 83 {'object_count': 3} True 28 0.431
          56 +RESULT 84 {'object_count': 2} True 26 0.59
          57 +RESULT 85 {'object_count': 3} True 23 0.528
          58 +RESULT 86 {'object_count': 3} True 23 0.487
          59 +RESULT 87 {'object_count': 2} True 35 1.007
          60 +RESULT 88 {'object_count': 2} True 25 0.507
          61 +RESULT 89 {'object_count': 3} True 37 0.726
          62 +RESULT 90 {'object_count': 2} True 32 0.393
          63 +RESULT 91 {'object_count': 3} True 30 0.385
          64 +RESULT 92 {'object_count': 2} True 25 0.298
          65 +RESULT 93 {'object_count': 3} True 30 0.406
```

</details>

<a id="C015"></a>
### C015 · Refine lander footprint and sight clearance; shorten return paths

Commit `664920063601e1cededb90bea4f888f3c00af913`; parents: 54bd720c7e2f22cb31c900febe88a4f00a2b030e. Recorded author date: 2026-09-21T22:09:06+02:00.

File roles (automatic): diagnostic/test, policy, support code (role needs review).

- [E0065](01_timeline.md#E0065): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_6649200_approach.py) · [Exact all-file diff](evidence/diffs/C015_6649200.diff)

[Previous saved controller snapshot](evidence/versions/C012_269b560_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e06bda3..0c73de7 100644
--- a/approach.py
+++ b/approach.py
@@ -30,7 +30,7 @@ class GeneratedApproach:
   30     30              if state.get(o, 'half_z') > .1:
   31     31                  self.occluders.append((p-h, p+h))
   32     32          self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
   33        -        self.rects.append((self.lander-np.array([.3,.25]),self.lander+np.array([.3,.25])))
          33 +        self.rects.append((self.lander-np.array([.50,.35]),self.lander+np.array([.50,.35])))
   34     34          axis = np.arange(-2.2, 2.201, .1)
   35     35          self.size = len(axis)
   36     36          xx, yy = np.meshgrid(axis, axis)
@@ -41,7 +41,7 @@ class GeneratedApproach:
   41     41              self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
   42     42          for k, o in enumerate(self.samples):
   43     43              self.masks[('sample',k)] = self.free & (np.linalg.norm(self.points-self.xy(state,o),axis=1)<.235)
   44        -        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.95)
          44 +        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
   45     45          self.tasks = [None,None]
   46     46          self.paths = [[],[]]
   47     47          self.previous = [None,None]
@@ -59,12 +59,12 @@ class GeneratedApproach:
   59     59      def visible(self, pts, target, radius):
   60     60          good = np.linalg.norm(pts-target,axis=1)<radius
   61     61          d = target-pts
          62 +        length2 = np.maximum(np.sum(d*d,axis=1),1e-12)
   62     63          for lo,hi in self.occluders:
   63        -            inv = np.divide(1.,d,out=np.full_like(d,1e10),where=np.abs(d)>1e-10)
   64        -            a=(lo-pts)*inv; b=(hi-pts)*inv
   65        -            enter=np.max(np.minimum(a,b),axis=1)
   66        -            leave=np.min(np.maximum(a,b),axis=1)
   67        -            good &= ~((leave>=np.maximum(enter,0)) & (enter<=1) & (leave>=0))
          64 +            center=(lo+hi)*.5
          65 +            t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
          66 +            closest=pts+t[:,None]*d
          67 +            good &= np.linalg.norm(closest-center,axis=1)>.155
   68     68          return good
   69     69  
   70     70      def route(self, start, mask, other=None):
@@ -88,7 +88,7 @@ class GeneratedApproach:
   88     88                  k=ny*n+nx
   89     89                  if not free[k]:continue
   90     90                  if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
   91        -                v=cost+1.
          91 +                v=cost+1.+(.001 if dx and dy else 0.)
   92     92                  if v<dist.get(k,1e9):
   93     93                      dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
   94     94          if end is None:return [],1e6
@@ -132,9 +132,9 @@ class GeneratedApproach:
  132    132              if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
  133    133              else:
  134    134                  best=('home',r)
  135        -                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
         135 +                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  136    136                  path,_=self.route(p,mask,other)
  137        -                path.append(self.home[r].copy())
         137 +                if s.get(self.rovers[r],'at_home')>.5:path=[]
  138    138          self.tasks[r]=best;self.paths[r]=path
  139    139  
  140    140      def result_count(self, s, r):
@@ -166,11 +166,10 @@ class GeneratedApproach:
  166    166                  # Infer blocked configuration and route around it.
  167    167                  blocked=p+self.previous[r][1]
  168    168                  self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
  169        -                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
         169 +                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  170    170                  else:mask=self.masks[task]
  171    171                  self.paths[r],_=self.route(p,mask,pos[1-r])
  172        -                if task[0]=='home':self.paths[r].append(self.home[r].copy())
  173        -                elif not self.paths[r]:
         172 +                if task[0]!='home' and not self.paths[r]:
  174    173                      self.tasks[r]=None
  175    174                      self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  176    175                  self.fail[r]=0
@@ -193,11 +192,11 @@ class GeneratedApproach:
  193    192              elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
  194    193                  op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  195    194                  if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
  196        -            elif kind=='send' and self.visible(q[None,:],self.lander,3.99)[0]:
         195 +            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
  197    196                  op=.5
  198    197                  if path and np.linalg.norm(q-path[-1])>.06:op=0.
  199    198              if op==0 and s.get(rob,'store_full')>.5:op=5/6
  200        -            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
         199 +            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
  201    200              action[r*4:r*4+2]=d;action[r*4+3]=op
  202    201              self.previous[r]=(p.copy(),d.copy())
  203    202              self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
diff --git a/approach_backup.py b/approach_backup.py
new file mode 100644
index 0000000..e06bda3
--- /dev/null
+++ b/approach_backup.py
@@ -0,0 +1,204 @@
           1 +import math
           2 +import heapq
           3 +import numpy as np
           4 +
           5 +
           6 +class GeneratedApproach:
           7 +    """Feedback navigation and task allocation for the two rovers."""
           8 +    def __init__(self, action_space, observation_space, primitives):
           9 +        self.space = observation_space
          10 +        self.types = {t.name: t for t in observation_space.types}
          11 +
          12 +    def objects(self, state, kind):
          13 +        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
          14 +
          15 +    def xy(self, state, obj):
          16 +        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
          17 +
          18 +    def reset(self, state, info):
          19 +        self.rovers = self.objects(state, 'rover')
          20 +        self.objectives = self.objects(state, 'objective')
          21 +        self.samples = self.objects(state, 'sample')
          22 +        self.home = [self.xy(state, r) for r in self.rovers]
          23 +        self.lander = self.xy(state, self.objects(state, 'lander')[0])
          24 +        self.rects = []
          25 +        self.occluders = []
          26 +        for o in self.objects(state, 'obstacle'):
          27 +            p = self.xy(state, o)
          28 +            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
          29 +            self.rects.append((p-h, p+h))
          30 +            if state.get(o, 'half_z') > .1:
          31 +                self.occluders.append((p-h, p+h))
          32 +        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
          33 +        self.rects.append((self.lander-np.array([.3,.25]),self.lander+np.array([.3,.25])))
          34 +        axis = np.arange(-2.2, 2.201, .1)
          35 +        self.size = len(axis)
          36 +        xx, yy = np.meshgrid(axis, axis)
          37 +        self.points = np.column_stack([xx.ravel(), yy.ravel()])
          38 +        self.free = self.valid(self.points)
          39 +        self.masks = {}
          40 +        for k, o in enumerate(self.objectives):
          41 +            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
          42 +        for k, o in enumerate(self.samples):
          43 +            self.masks[('sample',k)] = self.free & (np.linalg.norm(self.points-self.xy(state,o),axis=1)<.235)
          44 +        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.95)
          45 +        self.tasks = [None,None]
          46 +        self.paths = [[],[]]
          47 +        self.previous = [None,None]
          48 +        self.fail = [0,0]
          49 +        self.tick = 0
          50 +        self.last_op = [None, None]
          51 +        self.bad_views = {}
          52 +
          53 +    def valid(self, pts):
          54 +        good = np.all(np.abs(pts) <= 2.265, axis=-1)
          55 +        for lo,hi in self.rects:
          56 +            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
          57 +        return good
          58 +
          59 +    def visible(self, pts, target, radius):
          60 +        good = np.linalg.norm(pts-target,axis=1)<radius
          61 +        d = target-pts
          62 +        for lo,hi in self.occluders:
          63 +            inv = np.divide(1.,d,out=np.full_like(d,1e10),where=np.abs(d)>1e-10)
          64 +            a=(lo-pts)*inv; b=(hi-pts)*inv
          65 +            enter=np.max(np.minimum(a,b),axis=1)
          66 +            leave=np.min(np.maximum(a,b),axis=1)
          67 +            good &= ~((leave>=np.maximum(enter,0)) & (enter<=1) & (leave>=0))
          68 +        return good
          69 +
          70 +    def route(self, start, mask, other=None):
          71 +        # A multi-goal Dijkstra on a small occupancy grid.
          72 +        free=self.free.copy()
          73 +        if other is not None:
          74 +            free &= np.linalg.norm(self.points-other,axis=1)>.4
          75 +        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
          76 +        root=next((int(j) for j in starts if free[j]),int(starts[0]))
          77 +        dist={root:0.}; parent={}; queue=[(0.,root)]
          78 +        n=self.size
          79 +        end=None
          80 +        while queue:
          81 +            cost,j=heapq.heappop(queue)
          82 +            if cost!=dist[j]: continue
          83 +            if mask[j]: end=j;break
          84 +            x=j%n;y=j//n
          85 +            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
          86 +                nx=x+dx;ny=y+dy
          87 +                if nx<0 or nx>=n or ny<0 or ny>=n:continue
          88 +                k=ny*n+nx
          89 +                if not free[k]:continue
          90 +                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
          91 +                v=cost+1.
          92 +                if v<dist.get(k,1e9):
          93 +                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
          94 +        if end is None:return [],1e6
          95 +        path=[end]
          96 +        while path[-1]!=root:path.append(parent[path[-1]])
          97 +        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
          98 +
          99 +    def have(self,s,k):
         100 +        o=self.objectives[k]
         101 +        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
         102 +
         103 +    def needed(self,s):
         104 +        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
         105 +
         106 +    def pending(self,s,r):
         107 +        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
         108 +
         109 +    def completed(self,s,r,task):
         110 +        kind,k=task
         111 +        if kind=='image':return self.have(s,k)
         112 +        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
         113 +        if kind=='send':return not self.pending(s,r)
         114 +        return s.get(self.rovers[r],'at_home')>.5
         115 +
         116 +    def choose(self,s,r,p,other):
         117 +        candidates=[]
         118 +        reserved=self.tasks[1-r]
         119 +        need=self.needed(s)
         120 +        for k,o in enumerate(self.objectives):
         121 +            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
         122 +        if s.get(self.rovers[r],'store_full')<.5:
         123 +            for k,o in enumerate(self.samples):
         124 +                soil=int(s.get(o,'is_soil'))
         125 +                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
         126 +        best=None;score=1e9;path=[]
         127 +        for task in candidates:
         128 +            pp,cost=self.route(p,self.masks[task],other)
         129 +            cost+=2 if task[0]=='image' else 0
         130 +            if cost<score and cost<1e5:best=task;score=cost;path=pp
         131 +        if best is None:
         132 +            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
         133 +            else:
         134 +                best=('home',r)
         135 +                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
         136 +                path,_=self.route(p,mask,other)
         137 +                path.append(self.home[r].copy())
         138 +        self.tasks[r]=best;self.paths[r]=path
         139 +
         140 +    def result_count(self, s, r):
         141 +        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
         142 +
         143 +    def get_action(self, state):
         144 +        s=state; self.tick+=1
         145 +        action=np.zeros(8,dtype=np.float32)
         146 +        pos=[self.xy(s,r) for r in self.rovers]
         147 +        for r in range(2):
         148 +            p=pos[r];rob=self.rovers[r]
         149 +            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
         150 +                self.fail[r]+=1
         151 +            else:self.fail[r]=0
         152 +            task=self.tasks[r]
         153 +            last=self.last_op[r]
         154 +            if last is not None:
         155 +                old_task, old_p, old_op, old_count = last
         156 +                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
         157 +                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
         158 +                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
         159 +                if failed and task==old_task and task[0] in ('image','send'):
         160 +                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
         161 +                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
         162 +            if task is None or self.completed(s,r,task):
         163 +                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         164 +            if self.fail[r]>=2:
         165 +                self.paths[r]=[]
         166 +                # Infer blocked configuration and route around it.
         167 +                blocked=p+self.previous[r][1]
         168 +                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
         169 +                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
         170 +                else:mask=self.masks[task]
         171 +                self.paths[r],_=self.route(p,mask,pos[1-r])
         172 +                if task[0]=='home':self.paths[r].append(self.home[r].copy())
         173 +                elif not self.paths[r]:
         174 +                    self.tasks[r]=None
         175 +                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         176 +                self.fail[r]=0
         177 +            path=self.paths[r]
         178 +            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
         179 +            dest=p.copy()
         180 +            selected=-1
         181 +            for pi,point in enumerate(path[:5]):
         182 +                d=point-p
         183 +                if np.max(np.abs(d))>.20001:break
         184 +                probes=p+np.linspace(0,1,5)[:,None]*d
         185 +                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
         186 +                else:break
         187 +            if selected>0:del path[:selected]
         188 +            d=np.clip(dest-p,-.2,.2)
         189 +            q=p+d
         190 +            op=0.
         191 +            kind,k=task
         192 +            if kind=='sample' and np.linalg.norm(q-self.xy(s,self.samples[k]))<.247:op=-5/6
         193 +            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
         194 +                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
         195 +                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
         196 +            elif kind=='send' and self.visible(q[None,:],self.lander,3.99)[0]:
         197 +                op=.5
         198 +                if path and np.linalg.norm(q-path[-1])>.06:op=0.
         199 +            if op==0 and s.get(rob,'store_full')>.5:op=5/6
         200 +            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
         201 +            action[r*4:r*4+2]=d;action[r*4+3]=op
         202 +            self.previous[r]=(p.copy(),d.copy())
         203 +            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
         204 +        return action
diff --git a/probe_lander_exact.py b/probe_lander_exact.py
index 5b438da..0404383 100644
--- a/probe_lander_exact.py
+++ b/probe_lander_exact.py
@@ -12,7 +12,7 @@ for mode in ['front','side']:
   12     12     d=np.clip(np.array(target)-p(),-.1,.1)
   13     13     if np.linalg.norm(d)<1e-6:break
   14     14     st(d)
   15        - for k in range(100):
          15 + for k in range(400):
   16     16    old=p();st([0,-.0001] if mode=='front' else [-.0001,0])
   17     17    if np.allclose(p(),old,atol=1e-7,rtol=0):break
   18     18   print(mode,p(),k)
diff --git a/test_results_more.txt b/test_results_more.txt
index a85a9c6..fa7b275 100644
--- a/test_results_more.txt
+++ b/test_results_more.txt
@@ -63,3 +63,10 @@ RESULT 90 {'object_count': 2} True 32 0.393
   63     63  RESULT 91 {'object_count': 3} True 30 0.385
   64     64  RESULT 92 {'object_count': 2} True 25 0.298
   65     65  RESULT 93 {'object_count': 3} True 30 0.406
          66 +RESULT 94 {'object_count': 1} True 24 0.673
          67 +RESULT 95 {'object_count': 2} True 25 0.995
          68 +RESULT 96 {'object_count': 3} True 32 1.2
          69 +RESULT 97 {'object_count': 1} True 49 2.105
          70 +RESULT 98 {'object_count': 2} True 25 1.228
          71 +RESULT 99 {'object_count': 3} True 28 1.095
          72 +RESULT 100 {'object_count': 3} True 37 1.394
```

</details>

<a id="C016"></a>
### C016 · Record lander footprint probes for accurate rover navigation

Commit `cd725ec000d10e9ec0e6dab50a666f3a39c08ab1`; parents: 664920063601e1cededb90bea4f888f3c00af913. Recorded author date: 2026-09-21T22:09:35+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C016_cd725ec.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_many.txt b/test_many.txt
new file mode 100644
index 0000000..4d73660
--- /dev/null
+++ b/test_many.txt
@@ -0,0 +1 @@
           1 +RESULT 1000 {'object_count': 4} True 31 1.739
diff --git a/test_refined.txt b/test_refined.txt
new file mode 100644
index 0000000..03b3320
--- /dev/null
+++ b/test_refined.txt
@@ -0,0 +1,14 @@
           1 +RESULT 0 {'object_count': 3} True 36 2.5
           2 +RESULT 1 {'object_count': 2} True 22 1.041
           3 +RESULT 2 {'object_count': 3} True 22 1.062
           4 +RESULT 3 {'object_count': 3} True 36 1.911
           5 +RESULT 4 {'object_count': 3} True 25 1.362
           6 +RESULT 5 {'object_count': 3} True 38 1.79
           7 +RESULT 6 {'object_count': 2} True 26 1.049
           8 +RESULT 7 {'object_count': 3} True 32 1.281
           9 +RESULT 8 {'object_count': 3} True 24 1.222
          10 +RESULT 9 {'object_count': 2} True 29 1.167
          11 +RESULT 10 {'object_count': 3} True 25 1.169
          12 +RESULT 11 {'object_count': 1} True 21 0.992
          13 +RESULT 12 {'object_count': 2} True 26 1.752
          14 +RESULT 13 {'object_count': 3} True 30 2.0
diff --git a/test_results_more.txt b/test_results_more.txt
index fa7b275..e63760f 100644
--- a/test_results_more.txt
+++ b/test_results_more.txt
@@ -70,3 +70,18 @@ RESULT 97 {'object_count': 1} True 49 2.105
   70     70  RESULT 98 {'object_count': 2} True 25 1.228
   71     71  RESULT 99 {'object_count': 3} True 28 1.095
   72     72  RESULT 100 {'object_count': 3} True 37 1.394
          73 +RESULT 101 {'object_count': 1} True 23 1.671
          74 +RESULT 102 {'object_count': 2} True 27 1.291
          75 +RESULT 103 {'object_count': 2} True 26 1.465
          76 +RESULT 104 {'object_count': 3} True 25 1.166
          77 +RESULT 105 {'object_count': 1} True 25 0.97
          78 +RESULT 106 {'object_count': 2} True 23 1.046
          79 +RESULT 107 {'object_count': 1} True 23 1.081
          80 +RESULT 108 {'object_count': 1} True 22 1.106
          81 +RESULT 109 {'object_count': 2} True 26 0.967
          82 +RESULT 110 {'object_count': 2} True 24 0.955
          83 +RESULT 111 {'object_count': 2} True 23 1.196
          84 +RESULT 112 {'object_count': 1} True 29 1.045
          85 +RESULT 113 {'object_count': 1} True 24 1.129
          86 +RESULT 114 {'object_count': 1} True 29 1.097
          87 +RESULT 115 {'object_count': 2} True 31 1.352
```

</details>

<a id="C017"></a>
### C017 · Avoid ambiguous sample pickups and clear stores before resampling

Commit `85c2ab808c7d046a7d4a55d15017f6b747814855`; parents: cd725ec000d10e9ec0e6dab50a666f3a39c08ab1. Recorded author date: 2026-09-21T22:10:40+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0054](01_timeline.md#E0054): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_85c2ab8_approach.py) · [Exact all-file diff](evidence/diffs/C017_85c2ab8.diff)

[Previous saved controller snapshot](evidence/versions/C015_6649200_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0c73de7..922b727 100644
--- a/approach.py
+++ b/approach.py
@@ -30,7 +30,7 @@ class GeneratedApproach:
   30     30              if state.get(o, 'half_z') > .1:
   31     31                  self.occluders.append((p-h, p+h))
   32     32          self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
   33        -        self.rects.append((self.lander-np.array([.50,.35]),self.lander+np.array([.50,.35])))
          33 +        self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
   34     34          axis = np.arange(-2.2, 2.201, .1)
   35     35          self.size = len(axis)
   36     36          xx, yy = np.meshgrid(axis, axis)
@@ -40,7 +40,7 @@ class GeneratedApproach:
   40     40          for k, o in enumerate(self.objectives):
   41     41              self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
   42     42          for k, o in enumerate(self.samples):
   43        -            self.masks[('sample',k)] = self.free & (np.linalg.norm(self.points-self.xy(state,o),axis=1)<.235)
          43 +            self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
   44     44          self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
   45     45          self.tasks = [None,None]
   46     46          self.paths = [[],[]]
@@ -50,6 +50,14 @@ class GeneratedApproach:
   50     50          self.last_op = [None, None]
   51     51          self.bad_views = {}
   52     52  
          53 +    def sample_safe(self, state, pts, k):
          54 +        target=self.samples[k]
          55 +        good=np.linalg.norm(pts-self.xy(state,target),axis=1)<.242
          56 +        for obj in self.samples:
          57 +            if state.get(obj,'is_soil')!=state.get(target,'is_soil'):
          58 +                good &= np.linalg.norm(pts-self.xy(state,obj),axis=1)>.255
          59 +        return good
          60 +
   53     61      def valid(self, pts):
   54     62          good = np.all(np.abs(pts) <= 2.265, axis=-1)
   55     63          for lo,hi in self.rects:
@@ -188,7 +196,7 @@ class GeneratedApproach:
  188    196              q=p+d
  189    197              op=0.
  190    198              kind,k=task
  191        -            if kind=='sample' and np.linalg.norm(q-self.xy(s,self.samples[k]))<.247:op=-5/6
         199 +            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
  192    200              elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
  193    201                  op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  194    202                  if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
diff --git a/test_many.txt b/test_many.txt
index 4d73660..c2323f1 100644
--- a/test_many.txt
+++ b/test_many.txt
@@ -1 +1,29 @@
    1      1  RESULT 1000 {'object_count': 4} True 31 1.739
           2 +RESULT 1001 {'object_count': 4} True 33 1.545
           3 +RESULT 1002 {'object_count': 4} True 26 1.307
           4 +RESULT 1003 {'object_count': 4} True 31 1.565
           5 +RESULT 1004 {'object_count': 4} True 31 1.403
           6 +RESULT 1005 {'object_count': 4} True 26 1.235
           7 +RESULT 1006 {'object_count': 4} True 30 1.668
           8 +RESULT 1007 {'object_count': 4} True 28 1.632
           9 +RESULT 1008 {'object_count': 4} True 31 1.951
          10 +RESULT 1009 {'object_count': 4} True 25 1.711
          11 +RESULT 1010 {'object_count': 4} True 40 2.848
          12 +RESULT 1011 {'object_count': 4} True 28 2.18
          13 +RESULT 1012 {'object_count': 4} True 34 1.981
          14 +RESULT 1013 {'object_count': 4} True 27 1.437
          15 +RESULT 1014 {'object_count': 4} True 29 1.946
          16 +RESULT 1015 {'object_count': 4} True 30 2.258
          17 +RESULT 1016 {'object_count': 4} True 31 2.827
          18 +RESULT 1017 {'object_count': 4} True 27 1.333
          19 +RESULT 1018 {'object_count': 4} True 33 1.189
          20 +RESULT 1019 {'object_count': 4} True 27 0.667
          21 +RESULT 1020 {'object_count': 4} True 25 1.11
          22 +RESULT 1021 {'object_count': 4} True 29 1.456
          23 +RESULT 1022 {'object_count': 4} True 29 1.239
          24 +RESULT 1023 {'object_count': 4} True 36 1.633
          25 +RESULT 1024 {'object_count': 4} True 29 1.218
          26 +RESULT 1025 {'object_count': 4} True 32 1.322
          27 +RESULT 1026 {'object_count': 4} True 29 1.187
          28 +RESULT 1027 {'object_count': 4} True 26 0.743
          29 +RESULT 1028 {'object_count': 4} True 42 1.501
diff --git a/test_refined.txt b/test_refined.txt
index 03b3320..597cbcf 100644
--- a/test_refined.txt
+++ b/test_refined.txt
@@ -12,3 +12,34 @@ RESULT 10 {'object_count': 3} True 25 1.169
   12     12  RESULT 11 {'object_count': 1} True 21 0.992
   13     13  RESULT 12 {'object_count': 2} True 26 1.752
   14     14  RESULT 13 {'object_count': 3} True 30 2.0
          15 +RESULT 14 {'object_count': 1} True 34 1.552
          16 +RESULT 15 {'object_count': 3} True 29 1.514
          17 +RESULT 16 {'object_count': 2} True 26 1.382
          18 +RESULT 17 {'object_count': 3} True 33 1.73
          19 +RESULT 18 {'object_count': 3} True 27 1.328
          20 +RESULT 19 {'object_count': 2} True 30 1.563
          21 +RESULT 20 {'object_count': 3} True 33 1.949
          22 +RESULT 21 {'object_count': 1} True 23 1.962
          23 +RESULT 22 {'object_count': 3} True 28 2.07
          24 +RESULT 23 {'object_count': 1} True 19 1.207
          25 +RESULT 24 {'object_count': 2} True 26 1.816
          26 +RESULT 25 {'object_count': 2} True 23 1.446
          27 +RESULT 26 {'object_count': 3} True 31 1.648
          28 +RESULT 27 {'object_count': 1} True 24 1.176
          29 +RESULT 28 {'object_count': 2} True 42 3.474
          30 +RESULT 29 {'object_count': 3} True 25 2.071
          31 +RESULT 30 {'object_count': 1} True 22 1.438
          32 +RESULT 31 {'object_count': 2} True 29 1.847
          33 +RESULT 32 {'object_count': 3} True 28 1.38
          34 +RESULT 33 {'object_count': 3} True 34 1.813
          35 +RESULT 34 {'object_count': 1} True 21 0.518
          36 +RESULT 35 {'object_count': 1} True 22 0.542
          37 +RESULT 36 {'object_count': 2} True 21 0.937
          38 +RESULT 37 {'object_count': 1} True 23 0.92
          39 +RESULT 38 {'object_count': 1} True 22 0.449
          40 +RESULT 39 {'object_count': 3} True 32 1.309
          41 +RESULT 40 {'object_count': 2} True 29 1.087
          42 +RESULT 41 {'object_count': 2} True 21 1.041
          43 +RESULT 42 {'object_count': 1} True 28 0.88
          44 +RESULT 43 {'object_count': 2} True 34 1.224
          45 +RESULT 44 {'object_count': 3} True 24 0.595
diff --git a/test_results_more.txt b/test_results_more.txt
index e63760f..30cf7eb 100644
--- a/test_results_more.txt
+++ b/test_results_more.txt
@@ -85,3 +85,17 @@ RESULT 112 {'object_count': 1} True 29 1.045
   85     85  RESULT 113 {'object_count': 1} True 24 1.129
   86     86  RESULT 114 {'object_count': 1} True 29 1.097
   87     87  RESULT 115 {'object_count': 2} True 31 1.352
          88 +RESULT 116 {'object_count': 1} False 250 13.889
          89 +FAILED [('home', 0), ('sample', 5)] [('rover0', {'x': 1.0, 'y': -1.75, 'theta': -3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}), ('rover1', {'x': -1.5, 'y': 0.3999998867511749, 'theta': 0.0, 'store_full': 1.0, 'calibrated': 0.0, 'at_home': 0.0}), ('objective0', {'x': 0.3243560194969177, 'y': 1.8972790241241455, 'z': 0.20100000500679016, 'have_image_rover0': 1.0, 'have_image_rover1': 0.0, 'received_image': 1.0}), ('sample0', {'x': -0.9633942246437073, 'y': -2.3797810077667236, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 1.0, 'received_analysis': 1.0}), ('sample1', {'x': -1.9395066499710083, 'y': -0.37688443064689636, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample2', {'x': -1.3768526315689087, 'y': 0.30743154883384705, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 1.0, 'received_analysis': 0.0}), ('sample3', {'x': -1.8997358083724976, 'y': 1.3095738887786865, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample4', {'x': -0.1688850373029709, 'y': 1.3331273794174194, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample5', {'x': -1.4924739599227905, 'y': 0.6196938753128052, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0})]
          90 +RESULT 117 {'object_count': 1} True 33 2.036
          91 +RESULT 118 {'object_count': 2} True 30 1.838
          92 +RESULT 119 {'object_count': 2} True 22 1.861
          93 +RESULT 120 {'object_count': 1} True 24 1.882
          94 +RESULT 121 {'object_count': 1} True 22 1.418
          95 +RESULT 122 {'object_count': 3} True 26 1.122
          96 +RESULT 123 {'object_count': 1} True 30 2.132
          97 +RESULT 124 {'object_count': 3} True 28 2.825
          98 +RESULT 125 {'object_count': 2} True 23 1.838
          99 +RESULT 126 {'object_count': 1} True 22 2.261
         100 +RESULT 127 {'object_count': 2} True 35 2.355
         101 +RESULT 128 {'object_count': 3} True 36 1.905
```

</details>

<a id="C018"></a>
### C018 · Add seed-sweep diagnostics for rejected operators and policy time

Commit `d8327f3677a399c5526266a3bc4c31b66682e6e3`; parents: 85c2ab808c7d046a7d4a55d15017f6b747814855. Recorded author date: 2026-09-21T22:11:35+02:00.

File roles (automatic): diagnostic/test.

- [E0094](01_timeline.md#E0094): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C018_d8327f3.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_many.txt b/test_many.txt
index c2323f1..c257a17 100644
--- a/test_many.txt
+++ b/test_many.txt
@@ -27,3 +27,32 @@ RESULT 1025 {'object_count': 4} True 32 1.322
   27     27  RESULT 1026 {'object_count': 4} True 29 1.187
   28     28  RESULT 1027 {'object_count': 4} True 26 0.743
   29     29  RESULT 1028 {'object_count': 4} True 42 1.501
          30 +RESULT 1029 {'object_count': 4} True 33 1.779
          31 +RESULT 1030 {'object_count': 4} True 32 1.654
          32 +RESULT 1031 {'object_count': 4} True 30 1.289
          33 +RESULT 1032 {'object_count': 4} True 31 1.158
          34 +RESULT 1033 {'object_count': 4} True 25 0.817
          35 +RESULT 1034 {'object_count': 4} True 32 1.37
          36 +RESULT 1035 {'object_count': 4} True 30 1.002
          37 +RESULT 1036 {'object_count': 4} True 31 1.031
          38 +RESULT 1037 {'object_count': 4} True 26 1.023
          39 +RESULT 1038 {'object_count': 4} True 26 1.144
          40 +RESULT 1039 {'object_count': 4} True 35 1.546
          41 +RESULT 1040 {'object_count': 4} True 28 1.006
          42 +RESULT 1041 {'object_count': 4} True 28 1.111
          43 +RESULT 1042 {'object_count': 4} True 33 1.342
          44 +RESULT 1043 {'object_count': 4} True 29 1.178
          45 +RESULT 1044 {'object_count': 4} True 26 1.189
          46 +RESULT 1045 {'object_count': 4} True 29 1.297
          47 +RESULT 1046 {'object_count': 4} True 26 0.904
          48 +RESULT 1047 {'object_count': 4} True 33 1.568
          49 +RESULT 1048 {'object_count': 4} True 27 1.129
          50 +RESULT 1049 {'object_count': 4} True 32 1.174
          51 +RESULT 1050 {'object_count': 4} True 29 0.886
          52 +RESULT 1051 {'object_count': 4} True 36 1.491
          53 +RESULT 1052 {'object_count': 4} True 39 1.194
          54 +RESULT 1053 {'object_count': 4} True 29 1.031
          55 +RESULT 1054 {'object_count': 4} True 28 1.298
          56 +RESULT 1055 {'object_count': 4} True 27 1.168
          57 +RESULT 1056 {'object_count': 4} True 37 1.421
          58 +RESULT 1057 {'object_count': 4} True 29 1.069
diff --git a/test_refined.txt b/test_refined.txt
index 597cbcf..ca9db6a 100644
--- a/test_refined.txt
+++ b/test_refined.txt
@@ -43,3 +43,39 @@ RESULT 41 {'object_count': 2} True 21 1.041
   43     43  RESULT 42 {'object_count': 1} True 28 0.88
   44     44  RESULT 43 {'object_count': 2} True 34 1.224
   45     45  RESULT 44 {'object_count': 3} True 24 0.595
          46 +RESULT 45 {'object_count': 3} True 29 1.218
          47 +RESULT 46 {'object_count': 2} True 24 1.584
          48 +RESULT 47 {'object_count': 1} True 26 1.292
          49 +RESULT 48 {'object_count': 1} True 21 0.576
          50 +RESULT 49 {'object_count': 1} True 42 1.431
          51 +RESULT 50 {'object_count': 3} True 28 1.212
          52 +RESULT 51 {'object_count': 2} True 23 1.149
          53 +RESULT 52 {'object_count': 3} True 27 1.267
          54 +RESULT 53 {'object_count': 3} True 26 0.64
          55 +RESULT 54 {'object_count': 1} True 21 0.575
          56 +RESULT 55 {'object_count': 3} True 29 1.279
          57 +RESULT 56 {'object_count': 2} True 28 1.159
          58 +RESULT 57 {'object_count': 1} True 18 0.49
          59 +RESULT 58 {'object_count': 2} True 33 0.862
          60 +RESULT 59 {'object_count': 3} True 24 1.097
          61 +RESULT 60 {'object_count': 1} True 28 0.951
          62 +RESULT 61 {'object_count': 2} True 25 0.673
          63 +RESULT 62 {'object_count': 2} True 27 0.594
          64 +RESULT 63 {'object_count': 2} True 30 0.91
          65 +RESULT 64 {'object_count': 2} True 27 0.997
          66 +RESULT 65 {'object_count': 1} True 20 0.852
          67 +RESULT 66 {'object_count': 3} True 27 1.079
          68 +RESULT 67 {'object_count': 3} True 25 0.486
          69 +RESULT 68 {'object_count': 2} True 25 1.04
          70 +RESULT 69 {'object_count': 1} True 24 1.172
          71 +RESULT 70 {'object_count': 2} True 25 0.989
          72 +RESULT 71 {'object_count': 3} True 26 1.007
          73 +RESULT 72 {'object_count': 3} True 30 0.701
          74 +RESULT 73 {'object_count': 3} True 24 0.907
          75 +RESULT 74 {'object_count': 1} True 24 1.082
          76 +RESULT 75 {'object_count': 2} True 24 1.036
          77 +RESULT 76 {'object_count': 2} True 27 1.18
          78 +RESULT 77 {'object_count': 1} True 23 0.508
          79 +RESULT 78 {'object_count': 3} True 27 1.111
          80 +RESULT 79 {'object_count': 1} True 32 1.215
          81 +RESULT 80 {'object_count': 3} True 28 1.194
diff --git a/test_stats.py b/test_stats.py
new file mode 100644
index 0000000..2601c23
--- /dev/null
+++ b/test_stats.py
@@ -0,0 +1,30 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import numpy as np
           4 +import time,json,argparse
           5 +P=argparse.ArgumentParser();P.add_argument('--start',type=int,default=0);P.add_argument('--n',type=int,default=100);P.add_argument('--count',type=int);P.add_argument('--out',default='stats.json');a=P.parse_args();out=[]
           6 +for seed in range(a.start,a.start+a.n):
           7 + e=make_env();s,info=e.reset(seed=seed,options={'object_count':a.count} if a.count else None);ap=GeneratedApproach(e.action_space,e.observation_space,{});st=time.time();ap.reset(s,info);tm=time.time()-st
           8 + bad=[0,0,0];ops=[0,0,0,0,0];success=False
           9 + for t in range(200):
          10 +  st=time.time();act=ap.get_action(s);tm+=time.time()-st
          11 +  s2,_,done,trunc,_=e.step(act)
          12 +  for r in range(2):
          13 +   op=act[4*r+3];rob=ap.rovers[r]
          14 +   if np.linalg.norm(act[4*r:4*r+2])>.01 and np.linalg.norm(ap.xy(s,rob)-ap.xy(s2,rob))<1e-6:bad[0]+=1
          15 +   if abs(op+.5)<1e-4:
          16 +    ops[0]+=1
          17 +    if s2.get(rob,'calibrated')<.5:bad[1]+=1
          18 +   if abs(op+.166666)<1e-4:ops[1]+=1
          19 +   if abs(op-.5)<1e-4:
          20 +    ops[2]+=1
          21 +    if ap.pending(s2,r):bad[2]+=1
          22 +   if abs(op+.83333)<1e-4:ops[3]+=1
          23 +   if abs(op-.83333)<1e-4:ops[4]+=1
          24 +  s=s2
          25 +  if done or trunc:success=done;break
          26 + rec={'seed':seed,'n':info.get('object_count'),'success':success,'steps':t+1,'time':round(tm,3),'bad':bad,'ops':ops};out.append(rec)
          27 + if not success or seed%10==0:print(rec,flush=True)
          28 + e.close()
          29 +open(a.out,'w').write(json.dumps(out))
          30 +print('SUMMARY',sum(r['success'] for r in out),len(out),'mean',np.mean([r['steps'] for r in out]),'max_time',max(r['time'] for r in out),flush=True)
```

</details>

<a id="C019"></a>
### C019 · Plan cooperative task tours to balance rover completion times

Commit `26c1504e34cf137c2c31527fbe83ca5651a80dad`; parents: d8327f3677a399c5526266a3bc4c31b66682e6e3. Recorded author date: 2026-09-21T22:13:55+02:00.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0091](01_timeline.md#E0091): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_26c1504_approach.py) · [Exact all-file diff](evidence/diffs/C019_26c1504.diff)

[Previous saved controller snapshot](evidence/versions/C017_85c2ab8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 922b727..cc17717 100644
--- a/approach.py
+++ b/approach.py
@@ -1,6 +1,7 @@
    1      1  import math
    2      2  import heapq
    3      3  import numpy as np
           4 +from task_planner import assign_tasks
    4      5  
    5      6  
    6      7  class GeneratedApproach:
@@ -49,6 +50,7 @@ class GeneratedApproach:
   49     50          self.tick = 0
   50     51          self.last_op = [None, None]
   51     52          self.bad_views = {}
          53 +        self.schedule = assign_tasks(self,state)
   52     54  
   53     55      def sample_safe(self, state, pts, k):
   54     56          target=self.samples[k]
@@ -131,6 +133,17 @@ class GeneratedApproach:
  131    133              for k,o in enumerate(self.samples):
  132    134                  soil=int(s.get(o,'is_soil'))
  133    135                  if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
         136 +        if self.schedule is not None:
         137 +            schedule=self.schedule[r]
         138 +            while schedule:
         139 +                kind,k=schedule[0]
         140 +                if (kind=='image' and self.have(s,k)) or (kind=='soil' and not need[k]):schedule.pop(0)
         141 +                else:break
         142 +            if schedule:
         143 +                kind,k=schedule[0]
         144 +                planned=[t for t in candidates if t==schedule[0] or (kind=='soil' and t[0]=='sample' and int(s.get(self.samples[t[1]],'is_soil'))==k)]
         145 +                if planned:candidates=planned
         146 +            else:candidates=[]
  134    147          best=None;score=1e9;path=[]
  135    148          for task in candidates:
  136    149              pp,cost=self.route(p,self.masks[task],other)
diff --git a/approach_greedy.py b/approach_greedy.py
new file mode 100644
index 0000000..922b727
--- /dev/null
+++ b/approach_greedy.py
@@ -0,0 +1,211 @@
           1 +import math
           2 +import heapq
           3 +import numpy as np
           4 +
           5 +
           6 +class GeneratedApproach:
           7 +    """Feedback navigation and task allocation for the two rovers."""
           8 +    def __init__(self, action_space, observation_space, primitives):
           9 +        self.space = observation_space
          10 +        self.types = {t.name: t for t in observation_space.types}
          11 +
          12 +    def objects(self, state, kind):
          13 +        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
          14 +
          15 +    def xy(self, state, obj):
          16 +        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
          17 +
          18 +    def reset(self, state, info):
          19 +        self.rovers = self.objects(state, 'rover')
          20 +        self.objectives = self.objects(state, 'objective')
          21 +        self.samples = self.objects(state, 'sample')
          22 +        self.home = [self.xy(state, r) for r in self.rovers]
          23 +        self.lander = self.xy(state, self.objects(state, 'lander')[0])
          24 +        self.rects = []
          25 +        self.occluders = []
          26 +        for o in self.objects(state, 'obstacle'):
          27 +            p = self.xy(state, o)
          28 +            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
          29 +            self.rects.append((p-h, p+h))
          30 +            if state.get(o, 'half_z') > .1:
          31 +                self.occluders.append((p-h, p+h))
          32 +        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
          33 +        self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
          34 +        axis = np.arange(-2.2, 2.201, .1)
          35 +        self.size = len(axis)
          36 +        xx, yy = np.meshgrid(axis, axis)
          37 +        self.points = np.column_stack([xx.ravel(), yy.ravel()])
          38 +        self.free = self.valid(self.points)
          39 +        self.masks = {}
          40 +        for k, o in enumerate(self.objectives):
          41 +            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
          42 +        for k, o in enumerate(self.samples):
          43 +            self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
          44 +        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
          45 +        self.tasks = [None,None]
          46 +        self.paths = [[],[]]
          47 +        self.previous = [None,None]
          48 +        self.fail = [0,0]
          49 +        self.tick = 0
          50 +        self.last_op = [None, None]
          51 +        self.bad_views = {}
          52 +
          53 +    def sample_safe(self, state, pts, k):
          54 +        target=self.samples[k]
          55 +        good=np.linalg.norm(pts-self.xy(state,target),axis=1)<.242
          56 +        for obj in self.samples:
          57 +            if state.get(obj,'is_soil')!=state.get(target,'is_soil'):
          58 +                good &= np.linalg.norm(pts-self.xy(state,obj),axis=1)>.255
          59 +        return good
          60 +
          61 +    def valid(self, pts):
          62 +        good = np.all(np.abs(pts) <= 2.265, axis=-1)
          63 +        for lo,hi in self.rects:
          64 +            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
          65 +        return good
          66 +
          67 +    def visible(self, pts, target, radius):
          68 +        good = np.linalg.norm(pts-target,axis=1)<radius
          69 +        d = target-pts
          70 +        length2 = np.maximum(np.sum(d*d,axis=1),1e-12)
          71 +        for lo,hi in self.occluders:
          72 +            center=(lo+hi)*.5
          73 +            t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
          74 +            closest=pts+t[:,None]*d
          75 +            good &= np.linalg.norm(closest-center,axis=1)>.155
          76 +        return good
          77 +
          78 +    def route(self, start, mask, other=None):
          79 +        # A multi-goal Dijkstra on a small occupancy grid.
          80 +        free=self.free.copy()
          81 +        if other is not None:
          82 +            free &= np.linalg.norm(self.points-other,axis=1)>.4
          83 +        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
          84 +        root=next((int(j) for j in starts if free[j]),int(starts[0]))
          85 +        dist={root:0.}; parent={}; queue=[(0.,root)]
          86 +        n=self.size
          87 +        end=None
          88 +        while queue:
          89 +            cost,j=heapq.heappop(queue)
          90 +            if cost!=dist[j]: continue
          91 +            if mask[j]: end=j;break
          92 +            x=j%n;y=j//n
          93 +            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
          94 +                nx=x+dx;ny=y+dy
          95 +                if nx<0 or nx>=n or ny<0 or ny>=n:continue
          96 +                k=ny*n+nx
          97 +                if not free[k]:continue
          98 +                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
          99 +                v=cost+1.+(.001 if dx and dy else 0.)
         100 +                if v<dist.get(k,1e9):
         101 +                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
         102 +        if end is None:return [],1e6
         103 +        path=[end]
         104 +        while path[-1]!=root:path.append(parent[path[-1]])
         105 +        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
         106 +
         107 +    def have(self,s,k):
         108 +        o=self.objectives[k]
         109 +        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
         110 +
         111 +    def needed(self,s):
         112 +        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
         113 +
         114 +    def pending(self,s,r):
         115 +        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
         116 +
         117 +    def completed(self,s,r,task):
         118 +        kind,k=task
         119 +        if kind=='image':return self.have(s,k)
         120 +        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
         121 +        if kind=='send':return not self.pending(s,r)
         122 +        return s.get(self.rovers[r],'at_home')>.5
         123 +
         124 +    def choose(self,s,r,p,other):
         125 +        candidates=[]
         126 +        reserved=self.tasks[1-r]
         127 +        need=self.needed(s)
         128 +        for k,o in enumerate(self.objectives):
         129 +            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
         130 +        if s.get(self.rovers[r],'store_full')<.5:
         131 +            for k,o in enumerate(self.samples):
         132 +                soil=int(s.get(o,'is_soil'))
         133 +                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
         134 +        best=None;score=1e9;path=[]
         135 +        for task in candidates:
         136 +            pp,cost=self.route(p,self.masks[task],other)
         137 +            cost+=2 if task[0]=='image' else 0
         138 +            if cost<score and cost<1e5:best=task;score=cost;path=pp
         139 +        if best is None:
         140 +            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
         141 +            else:
         142 +                best=('home',r)
         143 +                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
         144 +                path,_=self.route(p,mask,other)
         145 +                if s.get(self.rovers[r],'at_home')>.5:path=[]
         146 +        self.tasks[r]=best;self.paths[r]=path
         147 +
         148 +    def result_count(self, s, r):
         149 +        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
         150 +
         151 +    def get_action(self, state):
         152 +        s=state; self.tick+=1
         153 +        action=np.zeros(8,dtype=np.float32)
         154 +        pos=[self.xy(s,r) for r in self.rovers]
         155 +        for r in range(2):
         156 +            p=pos[r];rob=self.rovers[r]
         157 +            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
         158 +                self.fail[r]+=1
         159 +            else:self.fail[r]=0
         160 +            task=self.tasks[r]
         161 +            last=self.last_op[r]
         162 +            if last is not None:
         163 +                old_task, old_p, old_op, old_count = last
         164 +                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
         165 +                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
         166 +                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
         167 +                if failed and task==old_task and task[0] in ('image','send'):
         168 +                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
         169 +                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
         170 +            if task is None or self.completed(s,r,task):
         171 +                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         172 +            if self.fail[r]>=2:
         173 +                self.paths[r]=[]
         174 +                # Infer blocked configuration and route around it.
         175 +                blocked=p+self.previous[r][1]
         176 +                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
         177 +                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
         178 +                else:mask=self.masks[task]
         179 +                self.paths[r],_=self.route(p,mask,pos[1-r])
         180 +                if task[0]!='home' and not self.paths[r]:
         181 +                    self.tasks[r]=None
         182 +                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         183 +                self.fail[r]=0
         184 +            path=self.paths[r]
         185 +            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
         186 +            dest=p.copy()
         187 +            selected=-1
         188 +            for pi,point in enumerate(path[:5]):
         189 +                d=point-p
         190 +                if np.max(np.abs(d))>.20001:break
         191 +                probes=p+np.linspace(0,1,5)[:,None]*d
         192 +                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
         193 +                else:break
         194 +            if selected>0:del path[:selected]
         195 +            d=np.clip(dest-p,-.2,.2)
         196 +            q=p+d
         197 +            op=0.
         198 +            kind,k=task
         199 +            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
         200 +            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
         201 +                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
         202 +                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
         203 +            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
         204 +                op=.5
         205 +                if path and np.linalg.norm(q-path[-1])>.06:op=0.
         206 +            if op==0 and s.get(rob,'store_full')>.5:op=5/6
         207 +            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
         208 +            action[r*4:r*4+2]=d;action[r*4+3]=op
         209 +            self.previous[r]=(p.copy(),d.copy())
         210 +            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
         211 +        return action
diff --git a/stats200.txt b/stats200.txt
new file mode 100644
index 0000000..08a69da
--- /dev/null
+++ b/stats200.txt
@@ -0,0 +1,11 @@
           1 +{'seed': 200, 'n': 1, 'success': True, 'steps': 21, 'time': 0.103, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
           2 +{'seed': 210, 'n': 1, 'success': True, 'steps': 23, 'time': 0.165, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
           3 +{'seed': 220, 'n': 3, 'success': True, 'steps': 37, 'time': 0.284, 'bad': [4, 1, 1], 'ops': [4, 3, 4, 4, 2]}
           4 +{'seed': 230, 'n': 2, 'success': True, 'steps': 33, 'time': 0.232, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
           5 +{'seed': 240, 'n': 3, 'success': True, 'steps': 26, 'time': 0.153, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
           6 +{'seed': 250, 'n': 2, 'success': True, 'steps': 39, 'time': 0.236, 'bad': [4, 0, 0], 'ops': [2, 2, 3, 4, 2]}
           7 +{'seed': 260, 'n': 3, 'success': True, 'steps': 32, 'time': 0.214, 'bad': [2, 2, 3], 'ops': [5, 3, 8, 2, 2]}
           8 +{'seed': 262, 'n': 3, 'success': False, 'steps': 200, 'time': 2.204, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
           9 +{'seed': 270, 'n': 2, 'success': True, 'steps': 20, 'time': 0.143, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
          10 +{'seed': 280, 'n': 2, 'success': True, 'steps': 35, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
          11 +{'seed': 290, 'n': 1, 'success': True, 'steps': 22, 'time': 0.137, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
diff --git a/task_planner.py b/task_planner.py
new file mode 100644
index 0000000..daac8ed
--- /dev/null
+++ b/task_planner.py
@@ -0,0 +1,63 @@
           1 +"""Small cooperative task-tour planner using grid distance transforms."""
           2 +import math
           3 +import numpy as np
           4 +from scipy.sparse import csr_matrix
           5 +from scipy.sparse.csgraph import dijkstra
           6 +
           7 +
           8 +def assign_tasks(policy, state):
           9 +    n=policy.size
          10 +    free=policy.free.reshape(n,n)
          11 +    ids=np.arange(n*n).reshape(n,n)
          12 +    rows=[];cols=[];weights=[]
          13 +    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
          14 +        ya=slice(max(0,-dy),min(n,n-dy));xa=slice(max(0,-dx),min(n,n-dx))
          15 +        yb=slice(max(0,dy),min(n,n+dy));xb=slice(max(0,dx),min(n,n+dx))
          16 +        ok=free[ya,xa]&free[yb,xb]
          17 +        if dx and dy:ok &= free[ya,xb]&free[yb,xa]
          18 +        src=ids[ya,xa][ok];dst=ids[yb,xb][ok]
          19 +        rows.extend(src);cols.extend(dst);weights.extend([.5+(.0005 if dx and dy else 0.)]*len(src))
          20 +    graph=csr_matrix((weights,(rows,cols)),shape=(n*n,n*n))
          21 +    tasks=[('image',k) for k in range(len(policy.objectives))]+[('soil',0),('soil',1)]
          22 +    masks=[]
          23 +    for kind,k in tasks:
          24 +        if kind=='image':masks.append(policy.masks[(kind,k)])
          25 +        else:
          26 +            mask=np.zeros(n*n,dtype=bool)
          27 +            for j,o in enumerate(policy.samples):
          28 +                if int(state.get(o,'is_soil'))==k:mask |= policy.masks[('sample',j)]
          29 +            masks.append(mask)
          30 +    def field(mask):
          31 +        goals=np.flatnonzero(mask & policy.free)
          32 +        if len(goals)==0:return np.full(n*n,np.inf),np.zeros(n*n,dtype=int)
          33 +        d,_,sources=dijkstra(graph,directed=False,indices=goals,return_predecessors=True,min_only=True)
          34 +        return d,sources
          35 +    fields=[field(m) for m in masks]
          36 +    count=len(tasks)
          37 +    full=(1<<count)-1
          38 +    results=[]
          39 +    for r in range(2):
          40 +        back,_=field(np.linalg.norm(policy.points-policy.home[r],axis=1)<.24)
          41 +        root=int(np.argmin(np.linalg.norm(policy.points-policy.home[r],axis=1)+(~policy.free)*100))
          42 +        best=np.full(1<<count,np.inf);paths=[[] for _ in best];cache={}
          43 +        def visit(at, mask, cost, seq):
          44 +            total=cost+back[at]
          45 +            if total<best[mask]:best[mask]=total;paths[mask]=seq
          46 +            for k,(dist,target) in enumerate(fields):
          47 +                if mask & (1<<k) or not np.isfinite(dist[at]):continue
          48 +                nxt=int(target[at]);bits=mask|(1<<k)
          49 +                service=1.2 if tasks[k][0]=='image' else .2
          50 +                new=cost+max(0.,dist[at])+service
          51 +                key=(nxt,bits)
          52 +                if new>=cache.get(key,1e20):continue
          53 +                cache[key]=new
          54 +                visit(nxt,bits,new,seq+[tasks[k]])
          55 +        visit(root,0,0.,[])
          56 +        results.append((best,paths))
          57 +    options=[]
          58 +    for mask in range(full+1):
          59 +        c0=results[0][0][mask];c1=results[1][0][full^mask]
          60 +        if np.isfinite(c0+c1):options.append((max(c0,c1)+.05*(c0+c1),mask))
          61 +    if not options:return None
          62 +    _,mask=min(options)
          63 +    return [results[0][1][mask],results[1][1][full^mask]]
diff --git a/test_many.txt b/test_many.txt
index c257a17..ed68f53 100644
--- a/test_many.txt
+++ b/test_many.txt
@@ -56,3 +56,45 @@ RESULT 1054 {'object_count': 4} True 28 1.298
   56     56  RESULT 1055 {'object_count': 4} True 27 1.168
   57     57  RESULT 1056 {'object_count': 4} True 37 1.421
   58     58  RESULT 1057 {'object_count': 4} True 29 1.069
          59 +RESULT 1058 {'object_count': 4} True 39 3.17
          60 +RESULT 1059 {'object_count': 4} True 29 1.463
          61 +RESULT 1060 {'object_count': 4} True 29 2.188
          62 +RESULT 1061 {'object_count': 4} True 31 2.024
          63 +RESULT 1062 {'object_count': 4} True 28 1.644
          64 +RESULT 1063 {'object_count': 4} True 26 2.027
          65 +RESULT 1064 {'object_count': 4} True 39 2.745
          66 +RESULT 1065 {'object_count': 4} True 32 2.617
          67 +RESULT 1066 {'object_count': 4} True 28 2.739
          68 +RESULT 1067 {'object_count': 4} True 30 2.436
          69 +RESULT 1068 {'object_count': 4} True 27 1.846
          70 +RESULT 1069 {'object_count': 4} True 33 2.191
          71 +RESULT 1070 {'object_count': 4} True 30 2.156
          72 +RESULT 1071 {'object_count': 4} True 26 1.245
          73 +RESULT 1072 {'object_count': 4} True 32 1.927
          74 +RESULT 1073 {'object_count': 4} True 27 2.066
          75 +RESULT 1074 {'object_count': 4} True 33 1.913
          76 +RESULT 1075 {'object_count': 4} True 28 1.159
          77 +RESULT 1076 {'object_count': 4} True 33 1.312
          78 +RESULT 1077 {'object_count': 4} True 28 1.181
          79 +RESULT 1078 {'object_count': 4} True 29 1.2
          80 +RESULT 1079 {'object_count': 4} True 33 1.112
          81 +RESULT 1080 {'object_count': 4} True 27 0.985
          82 +RESULT 1081 {'object_count': 4} True 29 1.06
          83 +RESULT 1082 {'object_count': 4} True 27 1.198
          84 +RESULT 1083 {'object_count': 4} True 31 1.61
          85 +RESULT 1084 {'object_count': 4} True 27 1.241
          86 +RESULT 1085 {'object_count': 4} True 32 1.326
          87 +RESULT 1086 {'object_count': 4} True 27 0.963
          88 +RESULT 1087 {'object_count': 4} True 32 1.188
          89 +RESULT 1088 {'object_count': 4} True 24 1.059
          90 +RESULT 1089 {'object_count': 4} True 26 0.833
          91 +RESULT 1090 {'object_count': 4} True 28 1.208
          92 +RESULT 1091 {'object_count': 4} True 27 0.954
          93 +RESULT 1092 {'object_count': 4} True 28 1.118
          94 +RESULT 1093 {'object_count': 4} True 35 1.145
          95 +RESULT 1094 {'object_count': 4} True 28 0.904
          96 +RESULT 1095 {'object_count': 4} True 34 1.315
          97 +RESULT 1096 {'object_count': 4} True 34 1.127
          98 +RESULT 1097 {'object_count': 4} True 28 0.811
          99 +RESULT 1098 {'object_count': 4} True 33 1.101
         100 +RESULT 1099 {'object_count': 4} True 36 1.082
diff --git a/test_refined.txt b/test_refined.txt
index ca9db6a..7b5e3a7 100644
--- a/test_refined.txt
+++ b/test_refined.txt
@@ -79,3 +79,22 @@ RESULT 77 {'object_count': 1} True 23 0.508
   79     79  RESULT 78 {'object_count': 3} True 27 1.111
   80     80  RESULT 79 {'object_count': 1} True 32 1.215
   81     81  RESULT 80 {'object_count': 3} True 28 1.194
          82 +RESULT 81 {'object_count': 1} True 24 1.588
          83 +RESULT 82 {'object_count': 3} True 32 1.635
          84 +RESULT 83 {'object_count': 3} True 27 2.003
          85 +RESULT 84 {'object_count': 2} True 27 2.134
          86 +RESULT 85 {'object_count': 3} True 23 1.459
          87 +RESULT 86 {'object_count': 3} True 23 1.577
          88 +RESULT 87 {'object_count': 2} True 33 2.287
          89 +RESULT 88 {'object_count': 2} True 24 1.429
          90 +RESULT 89 {'object_count': 3} True 37 3.407
          91 +RESULT 90 {'object_count': 2} True 31 2.851
          92 +RESULT 91 {'object_count': 3} True 30 2.424
          93 +RESULT 92 {'object_count': 2} True 26 2.167
          94 +RESULT 93 {'object_count': 3} True 30 2.011
          95 +RESULT 94 {'object_count': 1} True 25 1.403
          96 +RESULT 95 {'object_count': 2} True 24 1.842
          97 +RESULT 96 {'object_count': 3} True 32 2.013
          98 +RESULT 97 {'object_count': 1} True 47 2.412
          99 +RESULT 98 {'object_count': 2} True 25 1.781
         100 +RESULT 99 {'object_count': 3} True 31 2.06
```

</details>

<a id="C020"></a>
### C020 · Keep viewpoints beside objectives near pillars and plan consecutive samples

Commit `3c218ac1b7ecaf788fb7134393be700c39bd8ee2`; parents: 26c1504e34cf137c2c31527fbe83ca5651a80dad. Recorded author date: 2026-09-21T22:15:24+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0080](01_timeline.md#E0080): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_3c218ac_approach.py) · [Exact all-file diff](evidence/diffs/C020_3c218ac.diff)

[Previous saved controller snapshot](evidence/versions/C019_26c1504_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index cc17717..48f333b 100644
--- a/approach.py
+++ b/approach.py
@@ -74,7 +74,8 @@ class GeneratedApproach:
   74     74              center=(lo+hi)*.5
   75     75              t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
   76     76              closest=pts+t[:,None]*d
   77        -            good &= np.linalg.norm(closest-center,axis=1)>.155
          77 +            clearance=min(.155,float(np.linalg.norm(target-center))*.85)
          78 +            good &= np.linalg.norm(closest-center,axis=1)>clearance
   78     79          return good
   79     80  
   80     81      def route(self, start, mask, other=None):
@@ -129,7 +130,7 @@ class GeneratedApproach:
  129    130          need=self.needed(s)
  130    131          for k,o in enumerate(self.objectives):
  131    132              if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
  132        -        if s.get(self.rovers[r],'store_full')<.5:
         133 +        if True:
  133    134              for k,o in enumerate(self.samples):
  134    135                  soil=int(s.get(o,'is_soil'))
  135    136                  if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
diff --git a/inspect_seed.py b/inspect_seed.py
new file mode 100644
index 0000000..68d4e30
--- /dev/null
+++ b/inspect_seed.py
@@ -0,0 +1,10 @@
           1 +import sys,numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +E=make_env();s,i=E.reset(seed=int(sys.argv[1]));A=GeneratedApproach(E.action_space,E.observation_space,{});A.reset(s,i)
           5 +print('schedule',A.schedule)
           6 +for o in A.objectives:
           7 + p=A.xy(s,o);print(o.name,p,'mask',np.sum(A.masks[('image',A.objectives.index(o))]))
           8 + for ob in A.objects(s,'obstacle'):
           9 +  if np.linalg.norm(p-A.xy(s,ob))<.5:print('near',ob.name,A.xy(s,ob),s.get(ob,'half_x'),np.linalg.norm(p-A.xy(s,ob)))
          10 +E.close()
diff --git a/stats200.txt b/stats200.txt
index 08a69da..0e82d05 100644
--- a/stats200.txt
+++ b/stats200.txt
@@ -9,3 +9,8 @@
    9      9  {'seed': 270, 'n': 2, 'success': True, 'steps': 20, 'time': 0.143, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
   10     10  {'seed': 280, 'n': 2, 'success': True, 'steps': 35, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
   11     11  {'seed': 290, 'n': 1, 'success': True, 'steps': 22, 'time': 0.137, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
          12 +{'seed': 300, 'n': 1, 'success': True, 'steps': 23, 'time': 0.151, 'bad': [0, 0, 4], 'ops': [1, 1, 7, 2, 2]}
          13 +{'seed': 310, 'n': 1, 'success': True, 'steps': 24, 'time': 0.17, 'bad': [0, 0, 7], 'ops': [1, 1, 9, 2, 2]}
          14 +{'seed': 320, 'n': 1, 'success': True, 'steps': 35, 'time': 0.186, 'bad': [0, 0, 13], 'ops': [1, 1, 16, 2, 2]}
          15 +{'seed': 330, 'n': 2, 'success': True, 'steps': 40, 'time': 0.269, 'bad': [0, 1, 0], 'ops': [3, 2, 4, 2, 2]}
          16 +{'seed': 340, 'n': 1, 'success': True, 'steps': 26, 'time': 0.167, 'bad': [0, 0, 6], 'ops': [1, 1, 8, 2, 2]}
diff --git a/stats_planned.txt b/stats_planned.txt
new file mode 100644
index 0000000..6bd506f
--- /dev/null
+++ b/stats_planned.txt
@@ -0,0 +1,6 @@
           1 +{'seed': 0, 'n': 3, 'success': True, 'steps': 40, 'time': 0.233, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
           2 +{'seed': 10, 'n': 3, 'success': True, 'steps': 23, 'time': 0.171, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           3 +{'seed': 20, 'n': 3, 'success': True, 'steps': 34, 'time': 0.204, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
           4 +{'seed': 30, 'n': 1, 'success': True, 'steps': 27, 'time': 0.176, 'bad': [0, 0, 7], 'ops': [1, 1, 9, 2, 2]}
           5 +{'seed': 40, 'n': 2, 'success': True, 'steps': 28, 'time': 0.206, 'bad': [2, 0, 0], 'ops': [2, 2, 4, 2, 2]}
           6 +{'seed': 50, 'n': 3, 'success': True, 'steps': 39, 'time': 0.248, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
```

</details>

<a id="C021"></a>
### C021 · Add controlled comparison against updated greedy task allocation

Commit `f656838f0d4fc308be2f74b9215c0fb5ed56b076`; parents: 3c218ac1b7ecaf788fb7134393be700c39bd8ee2. Recorded author date: 2026-09-21T22:15:47+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0109](01_timeline.md#E0109): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C021_f656838.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_no_plan.py b/approach_no_plan.py
new file mode 100644
index 0000000..14427d7
--- /dev/null
+++ b/approach_no_plan.py
@@ -0,0 +1,225 @@
           1 +import math
           2 +import heapq
           3 +import numpy as np
           4 +from task_planner import assign_tasks
           5 +
           6 +
           7 +class GeneratedApproach:
           8 +    """Feedback navigation and task allocation for the two rovers."""
           9 +    def __init__(self, action_space, observation_space, primitives):
          10 +        self.space = observation_space
          11 +        self.types = {t.name: t for t in observation_space.types}
          12 +
          13 +    def objects(self, state, kind):
          14 +        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
          15 +
          16 +    def xy(self, state, obj):
          17 +        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
          18 +
          19 +    def reset(self, state, info):
          20 +        self.rovers = self.objects(state, 'rover')
          21 +        self.objectives = self.objects(state, 'objective')
          22 +        self.samples = self.objects(state, 'sample')
          23 +        self.home = [self.xy(state, r) for r in self.rovers]
          24 +        self.lander = self.xy(state, self.objects(state, 'lander')[0])
          25 +        self.rects = []
          26 +        self.occluders = []
          27 +        for o in self.objects(state, 'obstacle'):
          28 +            p = self.xy(state, o)
          29 +            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
          30 +            self.rects.append((p-h, p+h))
          31 +            if state.get(o, 'half_z') > .1:
          32 +                self.occluders.append((p-h, p+h))
          33 +        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
          34 +        self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
          35 +        axis = np.arange(-2.2, 2.201, .1)
          36 +        self.size = len(axis)
          37 +        xx, yy = np.meshgrid(axis, axis)
          38 +        self.points = np.column_stack([xx.ravel(), yy.ravel()])
          39 +        self.free = self.valid(self.points)
          40 +        self.masks = {}
          41 +        for k, o in enumerate(self.objectives):
          42 +            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
          43 +        for k, o in enumerate(self.samples):
          44 +            self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
          45 +        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
          46 +        self.tasks = [None,None]
          47 +        self.paths = [[],[]]
          48 +        self.previous = [None,None]
          49 +        self.fail = [0,0]
          50 +        self.tick = 0
          51 +        self.last_op = [None, None]
          52 +        self.bad_views = {}
          53 +        self.schedule = None
          54 +
          55 +    def sample_safe(self, state, pts, k):
          56 +        target=self.samples[k]
          57 +        good=np.linalg.norm(pts-self.xy(state,target),axis=1)<.242
          58 +        for obj in self.samples:
          59 +            if state.get(obj,'is_soil')!=state.get(target,'is_soil'):
          60 +                good &= np.linalg.norm(pts-self.xy(state,obj),axis=1)>.255
          61 +        return good
          62 +
          63 +    def valid(self, pts):
          64 +        good = np.all(np.abs(pts) <= 2.265, axis=-1)
          65 +        for lo,hi in self.rects:
          66 +            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
          67 +        return good
          68 +
          69 +    def visible(self, pts, target, radius):
          70 +        good = np.linalg.norm(pts-target,axis=1)<radius
          71 +        d = target-pts
          72 +        length2 = np.maximum(np.sum(d*d,axis=1),1e-12)
          73 +        for lo,hi in self.occluders:
          74 +            center=(lo+hi)*.5
          75 +            t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
          76 +            closest=pts+t[:,None]*d
          77 +            clearance=min(.155,float(np.linalg.norm(target-center))*.85)
          78 +            good &= np.linalg.norm(closest-center,axis=1)>clearance
          79 +        return good
          80 +
          81 +    def route(self, start, mask, other=None):
          82 +        # A multi-goal Dijkstra on a small occupancy grid.
          83 +        free=self.free.copy()
          84 +        if other is not None:
          85 +            free &= np.linalg.norm(self.points-other,axis=1)>.4
          86 +        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
          87 +        root=next((int(j) for j in starts if free[j]),int(starts[0]))
          88 +        dist={root:0.}; parent={}; queue=[(0.,root)]
          89 +        n=self.size
          90 +        end=None
          91 +        while queue:
          92 +            cost,j=heapq.heappop(queue)
          93 +            if cost!=dist[j]: continue
          94 +            if mask[j]: end=j;break
          95 +            x=j%n;y=j//n
          96 +            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
          97 +                nx=x+dx;ny=y+dy
          98 +                if nx<0 or nx>=n or ny<0 or ny>=n:continue
          99 +                k=ny*n+nx
         100 +                if not free[k]:continue
         101 +                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
         102 +                v=cost+1.+(.001 if dx and dy else 0.)
         103 +                if v<dist.get(k,1e9):
         104 +                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
         105 +        if end is None:return [],1e6
         106 +        path=[end]
         107 +        while path[-1]!=root:path.append(parent[path[-1]])
         108 +        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
         109 +
         110 +    def have(self,s,k):
         111 +        o=self.objectives[k]
         112 +        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
         113 +
         114 +    def needed(self,s):
         115 +        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
         116 +
         117 +    def pending(self,s,r):
         118 +        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
         119 +
         120 +    def completed(self,s,r,task):
         121 +        kind,k=task
         122 +        if kind=='image':return self.have(s,k)
         123 +        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
         124 +        if kind=='send':return not self.pending(s,r)
         125 +        return s.get(self.rovers[r],'at_home')>.5
         126 +
         127 +    def choose(self,s,r,p,other):
         128 +        candidates=[]
         129 +        reserved=self.tasks[1-r]
         130 +        need=self.needed(s)
         131 +        for k,o in enumerate(self.objectives):
         132 +            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
         133 +        if True:
         134 +            for k,o in enumerate(self.samples):
         135 +                soil=int(s.get(o,'is_soil'))
         136 +                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
         137 +        if self.schedule is not None:
         138 +            schedule=self.schedule[r]
         139 +            while schedule:
         140 +                kind,k=schedule[0]
         141 +                if (kind=='image' and self.have(s,k)) or (kind=='soil' and not need[k]):schedule.pop(0)
         142 +                else:break
         143 +            if schedule:
         144 +                kind,k=schedule[0]
         145 +                planned=[t for t in candidates if t==schedule[0] or (kind=='soil' and t[0]=='sample' and int(s.get(self.samples[t[1]],'is_soil'))==k)]
         146 +                if planned:candidates=planned
         147 +            else:candidates=[]
         148 +        best=None;score=1e9;path=[]
         149 +        for task in candidates:
         150 +            pp,cost=self.route(p,self.masks[task],other)
         151 +            cost+=2 if task[0]=='image' else 0
         152 +            if cost<score and cost<1e5:best=task;score=cost;path=pp
         153 +        if best is None:
         154 +            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
         155 +            else:
         156 +                best=('home',r)
         157 +                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
         158 +                path,_=self.route(p,mask,other)
         159 +                if s.get(self.rovers[r],'at_home')>.5:path=[]
         160 +        self.tasks[r]=best;self.paths[r]=path
         161 +
         162 +    def result_count(self, s, r):
         163 +        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
         164 +
         165 +    def get_action(self, state):
         166 +        s=state; self.tick+=1
         167 +        action=np.zeros(8,dtype=np.float32)
         168 +        pos=[self.xy(s,r) for r in self.rovers]
         169 +        for r in range(2):
         170 +            p=pos[r];rob=self.rovers[r]
         171 +            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
         172 +                self.fail[r]+=1
         173 +            else:self.fail[r]=0
         174 +            task=self.tasks[r]
         175 +            last=self.last_op[r]
         176 +            if last is not None:
         177 +                old_task, old_p, old_op, old_count = last
         178 +                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
         179 +                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
         180 +                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
         181 +                if failed and task==old_task and task[0] in ('image','send'):
         182 +                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
         183 +                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
         184 +            if task is None or self.completed(s,r,task):
         185 +                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         186 +            if self.fail[r]>=2:
         187 +                self.paths[r]=[]
         188 +                # Infer blocked configuration and route around it.
         189 +                blocked=p+self.previous[r][1]
         190 +                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
         191 +                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
         192 +                else:mask=self.masks[task]
         193 +                self.paths[r],_=self.route(p,mask,pos[1-r])
         194 +                if task[0]!='home' and not self.paths[r]:
         195 +                    self.tasks[r]=None
         196 +                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         197 +                self.fail[r]=0
         198 +            path=self.paths[r]
         199 +            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
         200 +            dest=p.copy()
         201 +            selected=-1
         202 +            for pi,point in enumerate(path[:5]):
         203 +                d=point-p
         204 +                if np.max(np.abs(d))>.20001:break
         205 +                probes=p+np.linspace(0,1,5)[:,None]*d
         206 +                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
         207 +                else:break
         208 +            if selected>0:del path[:selected]
         209 +            d=np.clip(dest-p,-.2,.2)
         210 +            q=p+d
         211 +            op=0.
         212 +            kind,k=task
         213 +            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
         214 +            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
         215 +                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
         216 +                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
         217 +            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
         218 +                op=.5
         219 +                if path and np.linalg.norm(q-path[-1])>.06:op=0.
         220 +            if op==0 and s.get(rob,'store_full')>.5:op=5/6
         221 +            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
         222 +            action[r*4:r*4+2]=d;action[r*4+3]=op
         223 +            self.previous[r]=(p.copy(),d.copy())
         224 +            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
         225 +        return action
diff --git a/stats200.txt b/stats200.txt
index 0e82d05..b836228 100644
--- a/stats200.txt
+++ b/stats200.txt
@@ -14,3 +14,6 @@
   14     14  {'seed': 320, 'n': 1, 'success': True, 'steps': 35, 'time': 0.186, 'bad': [0, 0, 13], 'ops': [1, 1, 16, 2, 2]}
   15     15  {'seed': 330, 'n': 2, 'success': True, 'steps': 40, 'time': 0.269, 'bad': [0, 1, 0], 'ops': [3, 2, 4, 2, 2]}
   16     16  {'seed': 340, 'n': 1, 'success': True, 'steps': 26, 'time': 0.167, 'bad': [0, 0, 6], 'ops': [1, 1, 8, 2, 2]}
          17 +{'seed': 349, 'n': 3, 'success': False, 'steps': 200, 'time': 3.08, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
          18 +{'seed': 350, 'n': 2, 'success': True, 'steps': 31, 'time': 0.181, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
          19 +{'seed': 360, 'n': 3, 'success': True, 'steps': 31, 'time': 0.238, 'bad': [2, 0, 0], 'ops': [4, 4, 3, 2, 2]}
diff --git a/stats_planned.txt b/stats_planned.txt
index 6bd506f..1b83781 100644
--- a/stats_planned.txt
+++ b/stats_planned.txt
@@ -4,3 +4,5 @@
    4      4  {'seed': 30, 'n': 1, 'success': True, 'steps': 27, 'time': 0.176, 'bad': [0, 0, 7], 'ops': [1, 1, 9, 2, 2]}
    5      5  {'seed': 40, 'n': 2, 'success': True, 'steps': 28, 'time': 0.206, 'bad': [2, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    6      6  {'seed': 50, 'n': 3, 'success': True, 'steps': 39, 'time': 0.248, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
           7 +{'seed': 60, 'n': 1, 'success': True, 'steps': 28, 'time': 0.186, 'bad': [2, 0, 2], 'ops': [1, 1, 4, 2, 2]}
           8 +{'seed': 70, 'n': 2, 'success': True, 'steps': 23, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
diff --git a/test_stats.py b/test_stats.py
index 2601c23..6e15b72 100644
--- a/test_stats.py
+++ b/test_stats.py
@@ -2,7 +2,9 @@ from env_client import make_env
    2      2  from approach import GeneratedApproach
    3      3  import numpy as np
    4      4  import time,json,argparse
    5        -P=argparse.ArgumentParser();P.add_argument('--start',type=int,default=0);P.add_argument('--n',type=int,default=100);P.add_argument('--count',type=int);P.add_argument('--out',default='stats.json');a=P.parse_args();out=[]
           5 +P=argparse.ArgumentParser();P.add_argument('--no-plan',action='store_true');P.add_argument('--start',type=int,default=0);P.add_argument('--n',type=int,default=100);P.add_argument('--count',type=int);P.add_argument('--out',default='stats.json');a=P.parse_args();out=[]
           6 +if a.no_plan:
           7 + from approach_no_plan import GeneratedApproach
    6      8  for seed in range(a.start,a.start+a.n):
    7      9   e=make_env();s,info=e.reset(seed=seed,options={'object_count':a.count} if a.count else None);ap=GeneratedApproach(e.action_space,e.observation_space,{});st=time.time();ap.reset(s,info);tm=time.time()-st
    8     10   bad=[0,0,0];ops=[0,0,0,0,0];success=False
```

</details>

<a id="C022"></a>
### C022 · Reassign work globally when a scheduled route proves inaccessible

Commit `a0bdce6b2f38af51632f7b6271413bc176de4892`; parents: f656838f0d4fc308be2f74b9215c0fb5ed56b076. Recorded author date: 2026-09-21T22:17:45+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0096](01_timeline.md#E0096): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C022_a0bdce6_approach.py) · [Exact all-file diff](evidence/diffs/C022_a0bdce6.diff)

[Previous saved controller snapshot](evidence/versions/C020_3c218ac_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 48f333b..8bdab39 100644
--- a/approach.py
+++ b/approach.py
@@ -150,6 +150,10 @@ class GeneratedApproach:
  150    150              pp,cost=self.route(p,self.masks[task],other)
  151    151              cost+=2 if task[0]=='image' else 0
  152    152              if cost<score and cost<1e5:best=task;score=cost;path=pp
         153 +        if best is None and candidates and self.schedule is not None:
         154 +            self.schedule=None
         155 +            self.choose(s,r,p,other)
         156 +            return
  153    157          if best is None:
  154    158              if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
  155    159              else:
diff --git a/inspect_collision.py b/inspect_collision.py
new file mode 100644
index 0000000..22be539
--- /dev/null
+++ b/inspect_collision.py
@@ -0,0 +1,14 @@
           1 +import sys,numpy as np
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +E=make_env();s,i=E.reset(seed=int(sys.argv[1]));A=GeneratedApproach(E.action_space,E.observation_space,{});A.reset(s,i)
           5 +for t in range(100):
           6 + a=A.get_action(s);ss,_,done,tr,_=E.step(a)
           7 + for r,rob in enumerate(A.rovers):
           8 +  p=A.xy(s,rob);q=p+a[r*4:r*4+2]
           9 +  if np.linalg.norm(q-p)>.01 and np.linalg.norm(A.xy(ss,rob)-p)<1e-5:
          10 +   print('COLLISION',t,r,'from',p,'to',q,'task',A.tasks[r])
          11 +   print('nearest',sorted([(float(np.linalg.norm(np.maximum(np.maximum(lo-q,q-hi),0))),lo.tolist(),hi.tolist()) for lo,hi in A.rects])[:3])
          12 + s=ss
          13 + if done:break
          14 +E.close()
diff --git a/probe_pillar.py b/probe_pillar.py
new file mode 100644
index 0000000..9e7e3f4
--- /dev/null
+++ b/probe_pillar.py
@@ -0,0 +1,40 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def p(s):
           5 + o=s.get_object_from_name('rover0');return np.array([s.get(o,'x'),s.get(o,'y')])
           6 +def st(e,s,d):
           7 + a=np.zeros(8);a[:2]=d;t,*_=e.step(a);return t
           8 +
           9 +def go(e,s,target):
          10 + for _ in range(60):
          11 +  d=np.clip(np.array(target)-p(s),-.1,.1)
          12 +  if np.linalg.norm(d)<1e-5:break
          13 +  old=p(s);s=st(e,s,d)
          14 +  if np.allclose(old,p(s)): print('STUCK',p(s),'towards',target);break
          15 + return s
          16 +for mode in ['diag','left','front','right']:
          17 + e=make_env();s,_=e.reset(seed=60)
          18 + if mode=='diag':
          19 +  for o in s.get_objects(e.observation_space.get_type('obstacle')):
          20 +   print(str(o),[s.get(o,f) for f in ['x','y','half_x','half_y']])
          21 +  s=go(e,s,[1.,.4]);s=go(e,s,[1.5,.2]);print('start',p(s));s=st(e,s,[-.2,-.2]);print('diag',p(s))
          22 + elif mode=='front':
          23 +  s=go(e,s,[1.,.4]);s=go(e,s,[1.45038712,.4])
          24 +  for _ in range(500):
          25 +   old=p(s);s=st(e,s,[0,-.001])
          26 +   if np.allclose(old,p(s)):break
          27 +  print(mode,p(s))
          28 + elif mode=='right':
          29 +  s=go(e,s,[2.,-1.75]);s=go(e,s,[2.,-.21976596])
          30 +  for _ in range(600):
          31 +   old=p(s);s=st(e,s,[-.001,0])
          32 +   if np.allclose(old,p(s)):break
          33 +  print(mode,p(s))
          34 + elif mode=='left':
          35 +  s=go(e,s,[1.,.4]);s=go(e,s,[1.30000012,.4])
          36 +  for _ in range(500):
          37 +   old=p(s);s=st(e,s,[0,-.001])
          38 +   if np.allclose(old,p(s)):break
          39 +  print(mode,p(s))
          40 + e.close()
diff --git a/stats200.json b/stats200.json
new file mode 100644
index 0000000..7635566
--- /dev/null
+++ b/stats200.json
@@ -0,0 +1 @@
           1 +[{"seed": 200, "n": 1, "success": true, "steps": 21, "time": 0.103, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 201, "n": 1, "success": true, "steps": 60, "time": 0.333, "bad": [2, 0, 29], "ops": [1, 1, 31, 2, 2]}, {"seed": 202, "n": 1, "success": true, "steps": 30, "time": 0.195, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 203, "n": 1, "success": true, "steps": 29, "time": 0.181, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 204, "n": 3, "success": true, "steps": 22, "time": 0.19, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 205, "n": 2, "success": true, "steps": 30, "time": 0.188, "bad": [2, 0, 8], "ops": [2, 2, 11, 2, 2]}, {"seed": 206, "n": 2, "success": true, "steps": 21, "time": 0.106, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 207, "n": 1, "success": true, "steps": 25, "time": 0.116, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 208, "n": 3, "success": true, "steps": 27, "time": 0.226, "bad": [0, 1, 0], "ops": [4, 3, 5, 2, 2]}, {"seed": 209, "n": 3, "success": true, "steps": 26, "time": 0.164, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 210, "n": 1, "success": true, "steps": 23, "time": 0.165, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 211, "n": 1, "success": true, "steps": 19, "time": 0.149, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 212, "n": 1, "success": true, "steps": 29, "time": 0.348, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 213, "n": 1, "success": true, "steps": 27, "time": 0.219, "bad": [2, 2, 0], "ops": [3, 1, 2, 2, 2]}, {"seed": 214, "n": 1, "success": true, "steps": 23, "time": 0.175, "bad": [0, 0, 7], "ops": [1, 1, 9, 2, 2]}, {"seed": 215, "n": 3, "success": true, "steps": 33, "time": 0.276, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 216, "n": 3, "success": true, "steps": 25, "time": 0.199, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 217, "n": 3, "success": true, "steps": 27, "time": 0.181, "bad": [2, 0, 0], "ops": [4, 4, 4, 4, 2]}, {"seed": 218, "n": 2, "success": true, "steps": 28, "time": 0.217, "bad": [2, 2, 0], "ops": [4, 2, 4, 2, 2]}, {"seed": 219, "n": 1, "success": true, "steps": 39, "time": 0.213, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 220, "n": 3, "success": true, "steps": 37, "time": 0.284, "bad": [4, 1, 1], "ops": [4, 3, 4, 4, 2]}, {"seed": 221, "n": 2, "success": true, "steps": 23, "time": 0.193, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 222, "n": 2, "success": true, "steps": 26, "time": 0.207, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 223, "n": 2, "success": true, "steps": 34, "time": 0.228, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 224, "n": 3, "success": true, "steps": 23, "time": 0.203, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 225, "n": 3, "success": true, "steps": 28, "time": 0.199, "bad": [0, 1, 0], "ops": [5, 4, 2, 2, 2]}, {"seed": 226, "n": 3, "success": true, "steps": 23, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 227, "n": 2, "success": true, "steps": 21, "time": 0.201, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 228, "n": 2, "success": true, "steps": 25, "time": 0.121, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 229, "n": 2, "success": true, "steps": 26, "time": 0.221, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 230, "n": 2, "success": true, "steps": 33, "time": 0.232, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 231, "n": 1, "success": true, "steps": 27, "time": 0.261, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 232, "n": 2, "success": true, "steps": 26, "time": 0.182, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 233, "n": 1, "success": true, "steps": 22, "time": 0.156, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 234, "n": 2, "success": true, "steps": 28, "time": 0.195, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 235, "n": 3, "success": true, "steps": 38, "time": 0.226, "bad": [4, 0, 0], "ops": [4, 4, 4, 6, 2]}, {"seed": 236, "n": 2, "success": true, "steps": 21, "time": 0.137, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 237, "n": 3, "success": true, "steps": 30, "time": 0.226, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 238, "n": 2, "success": true, "steps": 21, "time": 0.153, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 239, "n": 3, "success": true, "steps": 28, "time": 0.214, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 240, "n": 3, "success": true, "steps": 26, "time": 0.153, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 241, "n": 2, "success": true, "steps": 28, "time": 0.203, "bad": [0, 2, 0], "ops": [4, 2, 3, 2, 2]}, {"seed": 242, "n": 3, "success": true, "steps": 31, "time": 0.238, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 243, "n": 3, "success": true, "steps": 34, "time": 0.269, "bad": [2, 2, 0], "ops": [5, 3, 3, 2, 2]}, {"seed": 244, "n": 3, "success": true, "steps": 24, "time": 0.203, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 245, "n": 3, "success": true, "steps": 32, "time": 0.215, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 246, "n": 3, "success": true, "steps": 29, "time": 0.226, "bad": [2, 0, 0], "ops": [3, 3, 4, 4, 2]}, {"seed": 247, "n": 1, "success": true, "steps": 24, "time": 0.157, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 248, "n": 2, "success": true, "steps": 26, "time": 0.181, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 249, "n": 3, "success": true, "steps": 24, "time": 0.183, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 250, "n": 2, "success": true, "steps": 39, "time": 0.236, "bad": [4, 0, 0], "ops": [2, 2, 3, 4, 2]}, {"seed": 251, "n": 1, "success": true, "steps": 20, "time": 0.148, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 252, "n": 3, "success": true, "steps": 28, "time": 0.193, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 253, "n": 2, "success": true, "steps": 22, "time": 0.166, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 254, "n": 1, "success": true, "steps": 19, "time": 0.14, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 255, "n": 1, "success": true, "steps": 38, "time": 0.231, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 256, "n": 2, "success": true, "steps": 36, "time": 0.181, "bad": [2, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 257, "n": 3, "success": true, "steps": 29, "time": 0.211, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 258, "n": 2, "success": true, "steps": 26, "time": 0.184, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 259, "n": 1, "success": true, "steps": 27, "time": 0.182, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 260, "n": 3, "success": true, "steps": 32, "time": 0.214, "bad": [2, 2, 3], "ops": [5, 3, 8, 2, 2]}, {"seed": 261, "n": 2, "success": true, "steps": 29, "time": 0.102, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 262, "n": 3, "success": false, "steps": 200, "time": 2.204, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 263, "n": 3, "success": true, "steps": 25, "time": 0.17, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 264, "n": 1, "success": true, "steps": 22, "time": 0.143, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 265, "n": 3, "success": true, "steps": 34, "time": 0.19, "bad": [5, 2, 0], "ops": [6, 4, 5, 2, 2]}, {"seed": 266, "n": 2, "success": true, "steps": 29, "time": 0.123, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 267, "n": 2, "success": true, "steps": 22, "time": 0.183, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 268, "n": 3, "success": true, "steps": 31, "time": 0.145, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 269, "n": 3, "success": true, "steps": 24, "time": 0.187, "bad": [0, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 270, "n": 2, "success": true, "steps": 20, "time": 0.143, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 271, "n": 3, "success": true, "steps": 24, "time": 0.163, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 272, "n": 1, "success": true, "steps": 22, "time": 0.164, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 273, "n": 1, "success": true, "steps": 24, "time": 0.156, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 274, "n": 2, "success": true, "steps": 38, "time": 0.214, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 275, "n": 1, "success": true, "steps": 22, "time": 0.134, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 276, "n": 2, "success": true, "steps": 24, "time": 0.128, "bad": [1, 1, 0], "ops": [3, 2, 2, 2, 2]}, {"seed": 277, "n": 1, "success": true, "steps": 24, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 278, "n": 2, "success": true, "steps": 26, "time": 0.133, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 279, "n": 2, "success": true, "steps": 24, "time": 0.126, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 280, "n": 2, "success": true, "steps": 35, "time": 0.206, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 281, "n": 2, "success": true, "steps": 26, "time": 0.184, "bad": [2, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 282, "n": 3, "success": true, "steps": 25, "time": 0.163, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 283, "n": 1, "success": true, "steps": 20, "time": 0.143, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 284, "n": 1, "success": true, "steps": 35, "time": 0.216, "bad": [2, 0, 0], "ops": [1, 1, 3, 4, 2]}, {"seed": 285, "n": 3, "success": true, "steps": 28, "time": 0.182, "bad": [0, 0, 1], "ops": [3, 3, 4, 2, 2]}, {"seed": 286, "n": 1, "success": true, "steps": 20, "time": 0.13, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 287, "n": 3, "success": true, "steps": 27, "time": 0.208, "bad": [2, 3, 0], "ops": [6, 3, 4, 2, 2]}, {"seed": 288, "n": 1, "success": true, "steps": 21, "time": 0.148, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 289, "n": 2, "success": true, "steps": 27, "time": 0.199, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 290, "n": 1, "success": true, "steps": 22, "time": 0.137, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 291, "n": 1, "success": true, "steps": 25, "time": 0.157, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 292, "n": 3, "success": true, "steps": 26, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 293, "n": 1, "success": true, "steps": 22, "time": 0.164, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 294, "n": 1, "success": true, "steps": 36, "time": 0.205, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 295, "n": 1, "success": true, "steps": 23, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 296, "n": 1, "success": true, "steps": 24, "time": 0.169, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 297, "n": 1, "success": true, "steps": 20, "time": 0.08, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 298, "n": 2, "success": true, "steps": 23, "time": 0.137, "bad": [2, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 299, "n": 3, "success": true, "steps": 26, "time": 0.195, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 300, "n": 1, "success": true, "steps": 23, "time": 0.151, "bad": [0, 0, 4], "ops": [1, 1, 7, 2, 2]}, {"seed": 301, "n": 1, "success": true, "steps": 34, "time": 0.212, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 302, "n": 3, "success": true, "steps": 24, "time": 0.197, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 303, "n": 2, "success": true, "steps": 36, "time": 0.244, "bad": [5, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 304, "n": 3, "success": true, "steps": 27, "time": 0.217, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 305, "n": 1, "success": true, "steps": 21, "time": 0.17, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 306, "n": 3, "success": true, "steps": 33, "time": 0.253, "bad": [4, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 307, "n": 3, "success": true, "steps": 29, "time": 0.252, "bad": [2, 0, 0], "ops": [3, 3, 5, 4, 2]}, {"seed": 308, "n": 2, "success": true, "steps": 27, "time": 0.2, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 309, "n": 2, "success": true, "steps": 22, "time": 0.177, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 310, "n": 1, "success": true, "steps": 24, "time": 0.17, "bad": [0, 0, 7], "ops": [1, 1, 9, 2, 2]}, {"seed": 311, "n": 2, "success": true, "steps": 35, "time": 0.243, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 312, "n": 1, "success": true, "steps": 25, "time": 0.153, "bad": [0, 0, 2], "ops": [1, 1, 5, 2, 2]}, {"seed": 313, "n": 1, "success": true, "steps": 23, "time": 0.147, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 314, "n": 2, "success": true, "steps": 27, "time": 0.247, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 315, "n": 2, "success": true, "steps": 22, "time": 0.166, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 316, "n": 1, "success": true, "steps": 21, "time": 0.138, "bad": [0, 0, 5], "ops": [1, 1, 8, 2, 2]}, {"seed": 317, "n": 1, "success": true, "steps": 23, "time": 0.16, "bad": [0, 0, 8], "ops": [1, 1, 11, 2, 2]}, {"seed": 318, "n": 1, "success": true, "steps": 21, "time": 0.151, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 319, "n": 3, "success": true, "steps": 33, "time": 0.276, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 320, "n": 1, "success": true, "steps": 35, "time": 0.186, "bad": [0, 0, 13], "ops": [1, 1, 16, 2, 2]}, {"seed": 321, "n": 2, "success": true, "steps": 23, "time": 0.184, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 322, "n": 1, "success": true, "steps": 22, "time": 0.121, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 323, "n": 3, "success": true, "steps": 25, "time": 0.178, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 324, "n": 2, "success": true, "steps": 25, "time": 0.198, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 325, "n": 1, "success": true, "steps": 25, "time": 0.172, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 326, "n": 1, "success": true, "steps": 23, "time": 0.157, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 327, "n": 2, "success": true, "steps": 25, "time": 0.171, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 328, "n": 1, "success": true, "steps": 28, "time": 0.166, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 329, "n": 3, "success": true, "steps": 26, "time": 0.179, "bad": [2, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 330, "n": 2, "success": true, "steps": 40, "time": 0.269, "bad": [0, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 331, "n": 1, "success": true, "steps": 30, "time": 0.188, "bad": [0, 2, 0], "ops": [3, 1, 3, 2, 2]}, {"seed": 332, "n": 2, "success": true, "steps": 29, "time": 0.219, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 333, "n": 1, "success": true, "steps": 26, "time": 0.142, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 334, "n": 2, "success": true, "steps": 24, "time": 0.194, "bad": [0, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 335, "n": 1, "success": true, "steps": 22, "time": 0.172, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 336, "n": 2, "success": true, "steps": 29, "time": 0.211, "bad": [2, 2, 0], "ops": [4, 2, 3, 2, 2]}, {"seed": 337, "n": 1, "success": true, "steps": 24, "time": 0.165, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 338, "n": 2, "success": true, "steps": 25, "time": 0.206, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 339, "n": 1, "success": true, "steps": 23, "time": 0.116, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 340, "n": 1, "success": true, "steps": 26, "time": 0.167, "bad": [0, 0, 6], "ops": [1, 1, 8, 2, 2]}, {"seed": 341, "n": 3, "success": true, "steps": 25, "time": 0.229, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 342, "n": 3, "success": true, "steps": 32, "time": 0.24, "bad": [0, 0, 1], "ops": [3, 3, 5, 2, 2]}, {"seed": 343, "n": 1, "success": true, "steps": 25, "time": 0.282, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 344, "n": 1, "success": true, "steps": 25, "time": 0.159, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 345, "n": 1, "success": true, "steps": 19, "time": 0.147, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 346, "n": 2, "success": true, "steps": 23, "time": 0.181, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 347, "n": 3, "success": true, "steps": 27, "time": 0.209, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 348, "n": 1, "success": true, "steps": 27, "time": 0.34, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 349, "n": 3, "success": false, "steps": 200, "time": 3.08, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 350, "n": 2, "success": true, "steps": 31, "time": 0.181, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 351, "n": 2, "success": true, "steps": 47, "time": 0.282, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 352, "n": 1, "success": true, "steps": 24, "time": 0.18, "bad": [2, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 353, "n": 1, "success": true, "steps": 29, "time": 0.17, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 354, "n": 3, "success": true, "steps": 27, "time": 0.231, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 355, "n": 2, "success": true, "steps": 22, "time": 0.167, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 356, "n": 1, "success": true, "steps": 25, "time": 0.185, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 357, "n": 2, "success": true, "steps": 32, "time": 0.257, "bad": [0, 1, 3], "ops": [4, 3, 5, 2, 2]}, {"seed": 358, "n": 3, "success": true, "steps": 27, "time": 0.216, "bad": [2, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 359, "n": 2, "success": true, "steps": 29, "time": 0.21, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 360, "n": 3, "success": true, "steps": 31, "time": 0.238, "bad": [2, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 361, "n": 3, "success": true, "steps": 29, "time": 0.241, "bad": [0, 0, 4], "ops": [3, 3, 8, 2, 2]}, {"seed": 362, "n": 3, "success": true, "steps": 31, "time": 0.184, "bad": [2, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 363, "n": 1, "success": true, "steps": 20, "time": 0.162, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 364, "n": 2, "success": true, "steps": 24, "time": 0.183, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 365, "n": 1, "success": true, "steps": 23, "time": 0.167, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 366, "n": 1, "success": true, "steps": 21, "time": 0.147, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 367, "n": 3, "success": true, "steps": 30, "time": 0.244, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 368, "n": 3, "success": true, "steps": 28, "time": 0.227, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 369, "n": 3, "success": true, "steps": 35, "time": 0.282, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 370, "n": 2, "success": true, "steps": 39, "time": 0.266, "bad": [0, 0, 1], "ops": [2, 2, 4, 2, 2]}, {"seed": 371, "n": 3, "success": true, "steps": 30, "time": 0.223, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 372, "n": 2, "success": true, "steps": 38, "time": 0.249, "bad": [2, 1, 9], "ops": [3, 2, 12, 2, 2]}, {"seed": 373, "n": 2, "success": true, "steps": 28, "time": 0.192, "bad": [2, 2, 0], "ops": [4, 2, 3, 2, 2]}, {"seed": 374, "n": 3, "success": true, "steps": 27, "time": 0.204, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 375, "n": 1, "success": true, "steps": 21, "time": 0.118, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 376, "n": 2, "success": true, "steps": 23, "time": 0.189, "bad": [2, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 377, "n": 3, "success": true, "steps": 31, "time": 0.217, "bad": [0, 0, 2], "ops": [3, 3, 7, 2, 2]}, {"seed": 378, "n": 2, "success": true, "steps": 37, "time": 0.236, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 379, "n": 3, "success": true, "steps": 30, "time": 0.234, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 380, "n": 2, "success": true, "steps": 22, "time": 0.142, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 381, "n": 3, "success": true, "steps": 25, "time": 0.209, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 382, "n": 1, "success": true, "steps": 26, "time": 0.175, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 383, "n": 1, "success": true, "steps": 26, "time": 0.171, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 384, "n": 1, "success": true, "steps": 31, "time": 0.195, "bad": [2, 0, 11], "ops": [1, 1, 13, 2, 2]}, {"seed": 385, "n": 3, "success": true, "steps": 28, "time": 0.208, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 386, "n": 2, "success": true, "steps": 30, "time": 0.207, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 387, "n": 2, "success": true, "steps": 37, "time": 0.254, "bad": [1, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 388, "n": 2, "success": true, "steps": 24, "time": 0.187, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 389, "n": 1, "success": true, "steps": 24, "time": 0.184, "bad": [0, 0, 5], "ops": [1, 1, 7, 2, 2]}, {"seed": 390, "n": 2, "success": true, "steps": 22, "time": 0.157, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 391, "n": 1, "success": true, "steps": 32, "time": 0.223, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 392, "n": 3, "success": true, "steps": 27, "time": 0.213, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 393, "n": 3, "success": true, "steps": 27, "time": 0.212, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 394, "n": 1, "success": true, "steps": 21, "time": 0.125, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 395, "n": 2, "success": true, "steps": 27, "time": 0.194, "bad": [2, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 396, "n": 2, "success": true, "steps": 27, "time": 0.205, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 397, "n": 3, "success": true, "steps": 27, "time": 0.208, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 398, "n": 3, "success": true, "steps": 27, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 399, "n": 3, "success": true, "steps": 26, "time": 0.179, "bad": [2, 0, 0], "ops": [3, 3, 3, 4, 2]}]
\ No newline at end of file
diff --git a/stats200.txt b/stats200.txt
index b836228..7788e14 100644
--- a/stats200.txt
+++ b/stats200.txt
@@ -17,3 +17,7 @@
   17     17  {'seed': 349, 'n': 3, 'success': False, 'steps': 200, 'time': 3.08, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
   18     18  {'seed': 350, 'n': 2, 'success': True, 'steps': 31, 'time': 0.181, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
   19     19  {'seed': 360, 'n': 3, 'success': True, 'steps': 31, 'time': 0.238, 'bad': [2, 0, 0], 'ops': [4, 4, 3, 2, 2]}
          20 +{'seed': 370, 'n': 2, 'success': True, 'steps': 39, 'time': 0.266, 'bad': [0, 0, 1], 'ops': [2, 2, 4, 2, 2]}
          21 +{'seed': 380, 'n': 2, 'success': True, 'steps': 22, 'time': 0.142, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
          22 +{'seed': 390, 'n': 2, 'success': True, 'steps': 22, 'time': 0.157, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
          23 +SUMMARY 198 200 mean 28.83 max_time 3.08
diff --git a/stats_greedy.txt b/stats_greedy.txt
new file mode 100644
index 0000000..ab8508e
--- /dev/null
+++ b/stats_greedy.txt
@@ -0,0 +1,4 @@
           1 +{'seed': 0, 'n': 3, 'success': True, 'steps': 36, 'time': 0.199, 'bad': [0, 0, 3], 'ops': [3, 3, 6, 2, 2]}
           2 +{'seed': 10, 'n': 3, 'success': True, 'steps': 25, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           3 +{'seed': 20, 'n': 3, 'success': True, 'steps': 33, 'time': 0.293, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
           4 +{'seed': 30, 'n': 1, 'success': True, 'steps': 22, 'time': 0.191, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
diff --git a/stats_planned.json b/stats_planned.json
new file mode 100644
index 0000000..cbd360a
--- /dev/null
+++ b/stats_planned.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "n": 3, "success": true, "steps": 40, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 22, "time": 0.132, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 26, "time": 0.193, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 24, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 24, "time": 0.179, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 32, "time": 0.208, "bad": [2, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 27, "time": 0.186, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 26, "time": 0.194, "bad": [2, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 27, "time": 0.199, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 25, "time": 0.18, "bad": [0, 0, 2], "ops": [2, 2, 5, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 23, "time": 0.171, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 21, "time": 0.136, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 25, "time": 0.185, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 28, "time": 0.188, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 42, "time": 0.249, "bad": [0, 0, 3], "ops": [1, 1, 6, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 28, "time": 0.182, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 24, "time": 0.172, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 39, "time": 0.243, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 27, "time": 0.18, "bad": [2, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 29, "time": 0.199, "bad": [2, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 34, "time": 0.204, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 23, "time": 0.139, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 26, "time": 0.169, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 21, "time": 0.159, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 21, "time": 0.162, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 26, "time": 0.198, "bad": [2, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 28, "time": 0.194, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 23, "time": 0.122, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 25, "time": 0.146, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 24, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 27, "time": 0.176, "bad": [0, 0, 7], "ops": [1, 1, 9, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 30, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 22, "time": 0.182, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 28, "time": 0.155, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 23, "time": 0.18, "bad": [0, 0, 8], "ops": [1, 1, 11, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 21, "time": 0.167, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.157, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 21, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 22, "time": 0.16, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 30, "time": 0.182, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 28, "time": 0.206, "bad": [2, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 22, "time": 0.129, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 24, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 32, "time": 0.218, "bad": [4, 1, 0], "ops": [4, 2, 2, 4, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 24, "time": 0.172, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 25, "time": 0.188, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 23, "time": 0.191, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 24, "time": 0.164, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 21, "time": 0.14, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 23, "time": 0.178, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 39, "time": 0.248, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 28, "time": 0.193, "bad": [2, 0, 6], "ops": [2, 2, 10, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 31, "time": 0.23, "bad": [2, 0, 4], "ops": [3, 3, 8, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 32, "time": 0.213, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 22, "time": 0.159, "bad": [0, 0, 6], "ops": [1, 1, 8, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 33, "time": 0.205, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 26, "time": 0.153, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 19, "time": 0.139, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 33, "time": 0.15, "bad": [2, 0, 4], "ops": [2, 2, 7, 4, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 24, "time": 0.189, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 28, "time": 0.186, "bad": [2, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 22, "time": 0.167, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 26, "time": 0.161, "bad": [0, 0, 7], "ops": [2, 2, 9, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 30, "time": 0.173, "bad": [0, 0, 5], "ops": [2, 2, 8, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 26, "time": 0.185, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 20, "time": 0.129, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 24, "time": 0.177, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 25, "time": 0.134, "bad": [0, 2, 0], "ops": [5, 3, 4, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 25, "time": 0.108, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 29, "time": 0.151, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 23, "time": 0.178, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 30, "time": 0.177, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 25, "time": 0.19, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 34, "time": 0.189, "bad": [2, 1, 6], "ops": [5, 4, 9, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 23, "time": 0.129, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 20, "time": 0.12, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 26, "time": 0.168, "bad": [0, 0, 8], "ops": [2, 2, 11, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 21, "time": 0.128, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 27, "time": 0.119, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 26, "time": 0.161, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 28, "time": 0.203, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 21, "time": 0.136, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 34, "time": 0.229, "bad": [2, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 25, "time": 0.188, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 27, "time": 0.179, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 23, "time": 0.151, "bad": [1, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 23, "time": 0.183, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 29, "time": 0.193, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 24, "time": 0.169, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 89, "n": 3, "success": false, "steps": 200, "time": 4.042, "bad": [6, 0, 0], "ops": [5, 5, 4, 3, 1]}, {"seed": 90, "n": 2, "success": true, "steps": 30, "time": 0.167, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 25, "time": 0.154, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 25, "time": 0.163, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 29, "time": 0.22, "bad": [2, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 24, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 23, "time": 0.203, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 39, "time": 0.215, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 28, "time": 0.18, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 26, "time": 0.175, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 28, "time": 0.173, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_planned.txt b/stats_planned.txt
index 1b83781..c1fcaa5 100644
--- a/stats_planned.txt
+++ b/stats_planned.txt
@@ -6,3 +6,7 @@
    6      6  {'seed': 50, 'n': 3, 'success': True, 'steps': 39, 'time': 0.248, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    7      7  {'seed': 60, 'n': 1, 'success': True, 'steps': 28, 'time': 0.186, 'bad': [2, 0, 2], 'ops': [1, 1, 4, 2, 2]}
    8      8  {'seed': 70, 'n': 2, 'success': True, 'steps': 23, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
           9 +{'seed': 80, 'n': 3, 'success': True, 'steps': 28, 'time': 0.203, 'bad': [0, 1, 0], 'ops': [5, 4, 3, 2, 2]}
          10 +{'seed': 89, 'n': 3, 'success': False, 'steps': 200, 'time': 4.042, 'bad': [6, 0, 0], 'ops': [5, 5, 4, 3, 1]}
          11 +{'seed': 90, 'n': 2, 'success': True, 'steps': 30, 'time': 0.167, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
          12 +SUMMARY 99 100 mean 28.09 max_time 4.042
diff --git a/stats_planned2.txt b/stats_planned2.txt
new file mode 100644
index 0000000..0277846
--- /dev/null
+++ b/stats_planned2.txt
@@ -0,0 +1,5 @@
           1 +{'seed': 0, 'n': 3, 'success': True, 'steps': 32, 'time': 0.185, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
           2 +{'seed': 10, 'n': 3, 'success': True, 'steps': 23, 'time': 0.176, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           3 +{'seed': 20, 'n': 3, 'success': True, 'steps': 34, 'time': 0.226, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
           4 +{'seed': 30, 'n': 1, 'success': True, 'steps': 27, 'time': 0.183, 'bad': [0, 0, 7], 'ops': [1, 1, 9, 2, 2]}
           5 +{'seed': 40, 'n': 2, 'success': True, 'steps': 26, 'time': 0.182, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
```

</details>

<a id="C023"></a>
### C023 · Pipeline photographs and transmissions into travel toward home

Commit `71a6844130c1f5f22c09a0ffc7064940e9284f9b`; parents: a0bdce6b2f38af51632f7b6271413bc176de4892. Recorded author date: 2026-09-21T22:18:37+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0111](01_timeline.md#E0111): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C023_71a6844_approach.py) · [Exact all-file diff](evidence/diffs/C023_71a6844.diff)

[Previous saved controller snapshot](evidence/versions/C022_a0bdce6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8bdab39..8fffc9c 100644
--- a/approach.py
+++ b/approach.py
@@ -155,7 +155,7 @@ class GeneratedApproach:
  155    155              self.choose(s,r,p,other)
  156    156              return
  157    157          if best is None:
  158        -            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
         158 +            if self.pending(s,r) and s.get(self.rovers[r],'at_home')>.5:best=('send',0);path,_=self.route(p,self.masks[best],other)
  159    159              else:
  160    160                  best=('home',r)
  161    161                  mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
@@ -179,8 +179,8 @@ class GeneratedApproach:
  179    179              last=self.last_op[r]
  180    180              if last is not None:
  181    181                  old_task, old_p, old_op, old_count = last
  182        -                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
  183        -                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
         182 +                failed = ((old_task[0]=='image' and old_op == -.5 and s.get(rob,'calibrated')<.5) or
         183 +                          (old_task[0]=='image' and old_op == -1/6 and self.result_count(s,r)<=old_count) or
  184    184                            (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
  185    185                  if failed and task==old_task and task[0] in ('image','send'):
  186    186                      self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
@@ -223,6 +223,15 @@ class GeneratedApproach:
  223    223                  if path and np.linalg.norm(q-path[-1])>.06:op=0.
  224    224              if op==0 and s.get(rob,'store_full')>.5:op=5/6
  225    225              elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
         226 +            # Use otherwise idle travel steps for camera work.
         227 +            if op in (0.,.5) and np.linalg.norm(d)>.01:
         228 +                visible=[]
         229 +                for j,o in enumerate(self.objectives):
         230 +                    if s.get(o,'have_image_rover%d'%r)<.5 and self.visible(q[None,:],self.xy(s,o),1.97)[0]:
         231 +                        visible.append((float(np.linalg.norm(q-self.xy(s,o))),j))
         232 +                if visible:
         233 +                    _,j=min(visible)
         234 +                    if not self.have(s,j):op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  226    235              action[r*4:r*4+2]=d;action[r*4+3]=op
  227    236              self.previous[r]=(p.copy(),d.copy())
  228    237              self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
diff --git a/approach_planned_before_pipeline.py b/approach_planned_before_pipeline.py
new file mode 100644
index 0000000..8bdab39
--- /dev/null
+++ b/approach_planned_before_pipeline.py
@@ -0,0 +1,229 @@
           1 +import math
           2 +import heapq
           3 +import numpy as np
           4 +from task_planner import assign_tasks
           5 +
           6 +
           7 +class GeneratedApproach:
           8 +    """Feedback navigation and task allocation for the two rovers."""
           9 +    def __init__(self, action_space, observation_space, primitives):
          10 +        self.space = observation_space
          11 +        self.types = {t.name: t for t in observation_space.types}
          12 +
          13 +    def objects(self, state, kind):
          14 +        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
          15 +
          16 +    def xy(self, state, obj):
          17 +        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
          18 +
          19 +    def reset(self, state, info):
          20 +        self.rovers = self.objects(state, 'rover')
          21 +        self.objectives = self.objects(state, 'objective')
          22 +        self.samples = self.objects(state, 'sample')
          23 +        self.home = [self.xy(state, r) for r in self.rovers]
          24 +        self.lander = self.xy(state, self.objects(state, 'lander')[0])
          25 +        self.rects = []
          26 +        self.occluders = []
          27 +        for o in self.objects(state, 'obstacle'):
          28 +            p = self.xy(state, o)
          29 +            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
          30 +            self.rects.append((p-h, p+h))
          31 +            if state.get(o, 'half_z') > .1:
          32 +                self.occluders.append((p-h, p+h))
          33 +        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
          34 +        self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
          35 +        axis = np.arange(-2.2, 2.201, .1)
          36 +        self.size = len(axis)
          37 +        xx, yy = np.meshgrid(axis, axis)
          38 +        self.points = np.column_stack([xx.ravel(), yy.ravel()])
          39 +        self.free = self.valid(self.points)
          40 +        self.masks = {}
          41 +        for k, o in enumerate(self.objectives):
          42 +            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
          43 +        for k, o in enumerate(self.samples):
          44 +            self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
          45 +        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
          46 +        self.tasks = [None,None]
          47 +        self.paths = [[],[]]
          48 +        self.previous = [None,None]
          49 +        self.fail = [0,0]
          50 +        self.tick = 0
          51 +        self.last_op = [None, None]
          52 +        self.bad_views = {}
          53 +        self.schedule = assign_tasks(self,state)
          54 +
          55 +    def sample_safe(self, state, pts, k):
          56 +        target=self.samples[k]
          57 +        good=np.linalg.norm(pts-self.xy(state,target),axis=1)<.242
          58 +        for obj in self.samples:
          59 +            if state.get(obj,'is_soil')!=state.get(target,'is_soil'):
          60 +                good &= np.linalg.norm(pts-self.xy(state,obj),axis=1)>.255
          61 +        return good
          62 +
          63 +    def valid(self, pts):
          64 +        good = np.all(np.abs(pts) <= 2.265, axis=-1)
          65 +        for lo,hi in self.rects:
          66 +            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
          67 +        return good
          68 +
          69 +    def visible(self, pts, target, radius):
          70 +        good = np.linalg.norm(pts-target,axis=1)<radius
          71 +        d = target-pts
          72 +        length2 = np.maximum(np.sum(d*d,axis=1),1e-12)
          73 +        for lo,hi in self.occluders:
          74 +            center=(lo+hi)*.5
          75 +            t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
          76 +            closest=pts+t[:,None]*d
          77 +            clearance=min(.155,float(np.linalg.norm(target-center))*.85)
          78 +            good &= np.linalg.norm(closest-center,axis=1)>clearance
          79 +        return good
          80 +
          81 +    def route(self, start, mask, other=None):
          82 +        # A multi-goal Dijkstra on a small occupancy grid.
          83 +        free=self.free.copy()
          84 +        if other is not None:
          85 +            free &= np.linalg.norm(self.points-other,axis=1)>.4
          86 +        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
          87 +        root=next((int(j) for j in starts if free[j]),int(starts[0]))
          88 +        dist={root:0.}; parent={}; queue=[(0.,root)]
          89 +        n=self.size
          90 +        end=None
          91 +        while queue:
          92 +            cost,j=heapq.heappop(queue)
          93 +            if cost!=dist[j]: continue
          94 +            if mask[j]: end=j;break
          95 +            x=j%n;y=j//n
          96 +            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
          97 +                nx=x+dx;ny=y+dy
          98 +                if nx<0 or nx>=n or ny<0 or ny>=n:continue
          99 +                k=ny*n+nx
         100 +                if not free[k]:continue
         101 +                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
         102 +                v=cost+1.+(.001 if dx and dy else 0.)
         103 +                if v<dist.get(k,1e9):
         104 +                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
         105 +        if end is None:return [],1e6
         106 +        path=[end]
         107 +        while path[-1]!=root:path.append(parent[path[-1]])
         108 +        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
         109 +
         110 +    def have(self,s,k):
         111 +        o=self.objectives[k]
         112 +        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
         113 +
         114 +    def needed(self,s):
         115 +        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
         116 +
         117 +    def pending(self,s,r):
         118 +        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
         119 +
         120 +    def completed(self,s,r,task):
         121 +        kind,k=task
         122 +        if kind=='image':return self.have(s,k)
         123 +        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
         124 +        if kind=='send':return not self.pending(s,r)
         125 +        return s.get(self.rovers[r],'at_home')>.5
         126 +
         127 +    def choose(self,s,r,p,other):
         128 +        candidates=[]
         129 +        reserved=self.tasks[1-r]
         130 +        need=self.needed(s)
         131 +        for k,o in enumerate(self.objectives):
         132 +            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
         133 +        if True:
         134 +            for k,o in enumerate(self.samples):
         135 +                soil=int(s.get(o,'is_soil'))
         136 +                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
         137 +        if self.schedule is not None:
         138 +            schedule=self.schedule[r]
         139 +            while schedule:
         140 +                kind,k=schedule[0]
         141 +                if (kind=='image' and self.have(s,k)) or (kind=='soil' and not need[k]):schedule.pop(0)
         142 +                else:break
         143 +            if schedule:
         144 +                kind,k=schedule[0]
         145 +                planned=[t for t in candidates if t==schedule[0] or (kind=='soil' and t[0]=='sample' and int(s.get(self.samples[t[1]],'is_soil'))==k)]
         146 +                if planned:candidates=planned
         147 +            else:candidates=[]
         148 +        best=None;score=1e9;path=[]
         149 +        for task in candidates:
         150 +            pp,cost=self.route(p,self.masks[task],other)
         151 +            cost+=2 if task[0]=='image' else 0
         152 +            if cost<score and cost<1e5:best=task;score=cost;path=pp
         153 +        if best is None and candidates and self.schedule is not None:
         154 +            self.schedule=None
         155 +            self.choose(s,r,p,other)
         156 +            return
         157 +        if best is None:
         158 +            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
         159 +            else:
         160 +                best=('home',r)
         161 +                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
         162 +                path,_=self.route(p,mask,other)
         163 +                if s.get(self.rovers[r],'at_home')>.5:path=[]
         164 +        self.tasks[r]=best;self.paths[r]=path
         165 +
         166 +    def result_count(self, s, r):
         167 +        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
         168 +
         169 +    def get_action(self, state):
         170 +        s=state; self.tick+=1
         171 +        action=np.zeros(8,dtype=np.float32)
         172 +        pos=[self.xy(s,r) for r in self.rovers]
         173 +        for r in range(2):
         174 +            p=pos[r];rob=self.rovers[r]
         175 +            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
         176 +                self.fail[r]+=1
         177 +            else:self.fail[r]=0
         178 +            task=self.tasks[r]
         179 +            last=self.last_op[r]
         180 +            if last is not None:
         181 +                old_task, old_p, old_op, old_count = last
         182 +                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
         183 +                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
         184 +                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
         185 +                if failed and task==old_task and task[0] in ('image','send'):
         186 +                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
         187 +                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
         188 +            if task is None or self.completed(s,r,task):
         189 +                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         190 +            if self.fail[r]>=2:
         191 +                self.paths[r]=[]
         192 +                # Infer blocked configuration and route around it.
         193 +                blocked=p+self.previous[r][1]
         194 +                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
         195 +                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
         196 +                else:mask=self.masks[task]
         197 +                self.paths[r],_=self.route(p,mask,pos[1-r])
         198 +                if task[0]!='home' and not self.paths[r]:
         199 +                    self.tasks[r]=None
         200 +                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         201 +                self.fail[r]=0
         202 +            path=self.paths[r]
         203 +            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
         204 +            dest=p.copy()
         205 +            selected=-1
         206 +            for pi,point in enumerate(path[:5]):
         207 +                d=point-p
         208 +                if np.max(np.abs(d))>.20001:break
         209 +                probes=p+np.linspace(0,1,5)[:,None]*d
         210 +                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
         211 +                else:break
         212 +            if selected>0:del path[:selected]
         213 +            d=np.clip(dest-p,-.2,.2)
         214 +            q=p+d
         215 +            op=0.
         216 +            kind,k=task
         217 +            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
         218 +            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
         219 +                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
         220 +                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
         221 +            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
         222 +                op=.5
         223 +                if path and np.linalg.norm(q-path[-1])>.06:op=0.
         224 +            if op==0 and s.get(rob,'store_full')>.5:op=5/6
         225 +            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
         226 +            action[r*4:r*4+2]=d;action[r*4+3]=op
         227 +            self.previous[r]=(p.copy(),d.copy())
         228 +            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
         229 +        return action
diff --git a/stats_greedy.txt b/stats_greedy.txt
index ab8508e..64ce567 100644
--- a/stats_greedy.txt
+++ b/stats_greedy.txt
@@ -2,3 +2,6 @@
    2      2  {'seed': 10, 'n': 3, 'success': True, 'steps': 25, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    3      3  {'seed': 20, 'n': 3, 'success': True, 'steps': 33, 'time': 0.293, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    4      4  {'seed': 30, 'n': 1, 'success': True, 'steps': 22, 'time': 0.191, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
           5 +{'seed': 40, 'n': 2, 'success': True, 'steps': 26, 'time': 0.21, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           6 +{'seed': 50, 'n': 3, 'success': True, 'steps': 28, 'time': 0.187, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
           7 +{'seed': 60, 'n': 1, 'success': True, 'steps': 28, 'time': 0.17, 'bad': [2, 0, 2], 'ops': [1, 1, 4, 2, 2]}
diff --git a/stats_planned2.txt b/stats_planned2.txt
index 0277846..3da78c9 100644
--- a/stats_planned2.txt
+++ b/stats_planned2.txt
@@ -3,3 +3,6 @@
    3      3  {'seed': 20, 'n': 3, 'success': True, 'steps': 34, 'time': 0.226, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    4      4  {'seed': 30, 'n': 1, 'success': True, 'steps': 27, 'time': 0.183, 'bad': [0, 0, 7], 'ops': [1, 1, 9, 2, 2]}
    5      5  {'seed': 40, 'n': 2, 'success': True, 'steps': 26, 'time': 0.182, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           6 +{'seed': 50, 'n': 3, 'success': True, 'steps': 24, 'time': 0.147, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
           7 +{'seed': 60, 'n': 1, 'success': True, 'steps': 28, 'time': 0.189, 'bad': [2, 0, 2], 'ops': [1, 1, 4, 2, 2]}
           8 +{'seed': 70, 'n': 2, 'success': True, 'steps': 23, 'time': 0.182, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
```

</details>

<a id="C024"></a>
### C024 · Add black-box probes of tall pillar collision footprint

Commit `e59551ba7b1f59471e14be0b5f22ca496a3fc8e2`; parents: 71a6844130c1f5f22c09a0ffc7064940e9284f9b. Recorded author date: 2026-09-21T22:20:43+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C024_e59551b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_pillar_axis.py b/probe_pillar_axis.py
new file mode 100644
index 0000000..4e53ca6
--- /dev/null
+++ b/probe_pillar_axis.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +for dy in [-.27,-.24,-.2,-.1,0,.1,.2,.24,.27]:
           4 + e=make_env();s,_=e.reset(seed=60);o=s.get_object_from_name('rover0')
           5 + def p():return np.array([s.get(o,'x'),s.get(o,'y')])
           6 + def st(d):
           7 +  global s
           8 +  a=np.zeros(8);a[:2]=d;s,*_=e.step(a)
           9 + for target in [[1.,-.21976596+dy],[1.15,-.21976596+dy]]:
          10 +  for k in range(40):
          11 +   d=np.clip(np.array(target)-p(),-.2,.2)
          12 +   if np.linalg.norm(d)<1e-5:break
          13 +   old=p();st(d)
          14 +   if np.allclose(old,p()):break
          15 + for k in range(40):
          16 +  old=p();st([.005,0])
          17 +  if np.allclose(old,p()):break
          18 + print(dy,p(),flush=True)
          19 + e.close()
diff --git a/probe_pillar_shape.py b/probe_pillar_shape.py
new file mode 100644
index 0000000..724f56c
--- /dev/null
+++ b/probe_pillar_shape.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +for dx in [-.3,-.27,-.25,-.23,-.21,-.18,-.15,-.1,-.05,0,.05,.10,.15]:
           4 + e=make_env();s,_=e.reset(seed=60);o=s.get_object_from_name('rover0')
           5 + def p():return np.array([s.get(o,'x'),s.get(o,'y')])
           6 + def st(d):
           7 +  global s
           8 +  a=np.zeros(8);a[:2]=d;s,*_=e.step(a)
           9 + for target in [[1.,.4],[1.45038712+dx,.4],[1.45038712+dx,.1]]:
          10 +  for k in range(40):
          11 +   d=np.clip(np.array(target)-p(),-.2,.2)
          12 +   if np.linalg.norm(d)<1e-5:break
          13 +   old=p();st(d)
          14 +   if np.allclose(old,p()):break
          15 + for k in range(50):
          16 +  old=p();st([0,-.01])
          17 +  if np.allclose(old,p()):break
          18 + print(dx,p(),flush=True)
          19 + e.close()
diff --git a/stats_greedy.json b/stats_greedy.json
new file mode 100644
index 0000000..1575c3d
--- /dev/null
+++ b/stats_greedy.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "n": 3, "success": true, "steps": 36, "time": 0.199, "bad": [0, 0, 3], "ops": [3, 3, 6, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 22, "time": 0.125, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 22, "time": 0.193, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 26, "time": 0.221, "bad": [2, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 25, "time": 0.204, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 28, "time": 0.211, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 26, "time": 0.193, "bad": [0, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 32, "time": 0.214, "bad": [2, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 24, "time": 0.193, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 29, "time": 0.265, "bad": [0, 0, 1], "ops": [2, 2, 4, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 25, "time": 0.178, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 21, "time": 0.111, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 25, "time": 0.159, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 30, "time": 0.223, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 31, "time": 0.215, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 31, "time": 0.222, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 26, "time": 0.155, "bad": [0, 0, 3], "ops": [2, 2, 7, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 33, "time": 0.223, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 27, "time": 0.21, "bad": [2, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 30, "time": 0.244, "bad": [2, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 33, "time": 0.293, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 22, "time": 0.218, "bad": [0, 0, 0], "ops": [1, 1, 1, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 28, "time": 0.175, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 19, "time": 0.148, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 26, "time": 0.168, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 21, "time": 0.111, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 32, "time": 0.236, "bad": [2, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 24, "time": 0.156, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 42, "time": 0.272, "bad": [4, 4, 2], "ops": [6, 2, 5, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 25, "time": 0.238, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 22, "time": 0.191, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 27, "time": 0.217, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 28, "time": 0.219, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 30, "time": 0.252, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 22, "time": 0.155, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 22, "time": 0.125, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.175, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 23, "time": 0.182, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 22, "time": 0.157, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 32, "time": 0.244, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 26, "time": 0.21, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 21, "time": 0.174, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 28, "time": 0.197, "bad": [2, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 29, "time": 0.213, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 24, "time": 0.212, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 29, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 24, "time": 0.126, "bad": [0, 0, 1], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 26, "time": 0.178, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 21, "time": 0.153, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 23, "time": 0.169, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 28, "time": 0.187, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 23, "time": 0.169, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 25, "time": 0.196, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 26, "time": 0.173, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 21, "time": 0.157, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 29, "time": 0.256, "bad": [0, 0, 1], "ops": [3, 3, 5, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 28, "time": 0.222, "bad": [2, 3, 0], "ops": [5, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 18, "time": 0.147, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 32, "time": 0.234, "bad": [2, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 24, "time": 0.182, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 28, "time": 0.17, "bad": [2, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 25, "time": 0.185, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 26, "time": 0.202, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 30, "time": 0.156, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 27, "time": 0.178, "bad": [0, 0, 1], "ops": [2, 2, 5, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 20, "time": 0.138, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 27, "time": 0.24, "bad": [0, 2, 0], "ops": [5, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 25, "time": 0.114, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 25, "time": 0.119, "bad": [2, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 24, "time": 0.19, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 25, "time": 0.198, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 26, "time": 0.21, "bad": [0, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 30, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 24, "time": 0.19, "bad": [0, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 24, "time": 0.174, "bad": [0, 0, 9], "ops": [1, 1, 12, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 24, "time": 0.168, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 27, "time": 0.195, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 23, "time": 0.164, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 27, "time": 0.208, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 32, "time": 0.191, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 27, "time": 0.174, "bad": [0, 1, 0], "ops": [5, 4, 2, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 23, "time": 0.203, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 27, "time": 0.227, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 27, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 29, "time": 0.187, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 23, "time": 0.175, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 23, "time": 0.189, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 25, "time": 0.184, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 24, "time": 0.127, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 89, "n": 3, "success": true, "steps": 37, "time": 0.309, "bad": [4, 0, 0], "ops": [5, 5, 4, 4, 2]}, {"seed": 90, "n": 2, "success": true, "steps": 31, "time": 0.214, "bad": [0, 1, 1], "ops": [3, 2, 4, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 30, "time": 0.228, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 26, "time": 0.222, "bad": [2, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 30, "time": 0.234, "bad": [2, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 25, "time": 0.132, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 24, "time": 0.196, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 32, "time": 0.225, "bad": [2, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 28, "time": 0.2, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 25, "time": 0.183, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 31, "time": 0.237, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_greedy.txt b/stats_greedy.txt
index 64ce567..a179298 100644
--- a/stats_greedy.txt
+++ b/stats_greedy.txt
@@ -5,3 +5,7 @@
    5      5  {'seed': 40, 'n': 2, 'success': True, 'steps': 26, 'time': 0.21, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    6      6  {'seed': 50, 'n': 3, 'success': True, 'steps': 28, 'time': 0.187, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    7      7  {'seed': 60, 'n': 1, 'success': True, 'steps': 28, 'time': 0.17, 'bad': [2, 0, 2], 'ops': [1, 1, 4, 2, 2]}
           8 +{'seed': 70, 'n': 2, 'success': True, 'steps': 25, 'time': 0.198, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
           9 +{'seed': 80, 'n': 3, 'success': True, 'steps': 27, 'time': 0.174, 'bad': [0, 1, 0], 'ops': [5, 4, 2, 2, 2]}
          10 +{'seed': 90, 'n': 2, 'success': True, 'steps': 31, 'time': 0.214, 'bad': [0, 1, 1], 'ops': [3, 2, 4, 2, 2]}
          11 +SUMMARY 100 100 mean 26.41 max_time 0.309
diff --git a/stats_pipeline.txt b/stats_pipeline.txt
new file mode 100644
index 0000000..5398c70
--- /dev/null
+++ b/stats_pipeline.txt
@@ -0,0 +1,9 @@
           1 +{'seed': 0, 'n': 3, 'success': True, 'steps': 28, 'time': 0.211, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
           2 +{'seed': 10, 'n': 3, 'success': True, 'steps': 22, 'time': 0.212, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           3 +{'seed': 20, 'n': 3, 'success': True, 'steps': 27, 'time': 0.163, 'bad': [0, 0, 0], 'ops': [4, 3, 2, 2, 2]}
           4 +{'seed': 30, 'n': 1, 'success': True, 'steps': 24, 'time': 0.142, 'bad': [0, 0, 4], 'ops': [1, 1, 6, 2, 2]}
           5 +{'seed': 40, 'n': 2, 'success': True, 'steps': 25, 'time': 0.19, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           6 +{'seed': 50, 'n': 3, 'success': True, 'steps': 23, 'time': 0.168, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
           7 +{'seed': 60, 'n': 1, 'success': True, 'steps': 22, 'time': 0.16, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
           8 +{'seed': 70, 'n': 2, 'success': True, 'steps': 22, 'time': 0.104, 'bad': [0, 1, 0], 'ops': [3, 2, 3, 2, 2]}
           9 +{'seed': 80, 'n': 3, 'success': True, 'steps': 23, 'time': 0.197, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
diff --git a/stats_planned2.json b/stats_planned2.json
new file mode 100644
index 0000000..379fd40
--- /dev/null
+++ b/stats_planned2.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "n": 3, "success": true, "steps": 32, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 22, "time": 0.171, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 23, "time": 0.184, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 24, "time": 0.189, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 24, "time": 0.176, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 26, "time": 0.143, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 23, "time": 0.155, "bad": [0, 0, 2], "ops": [2, 2, 5, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 26, "time": 0.177, "bad": [2, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 27, "time": 0.224, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 25, "time": 0.19, "bad": [0, 0, 2], "ops": [2, 2, 5, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 23, "time": 0.176, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 21, "time": 0.109, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 25, "time": 0.09, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 28, "time": 0.123, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 31, "time": 0.108, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 28, "time": 0.12, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 24, "time": 0.131, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 24, "time": 0.149, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 27, "time": 0.176, "bad": [2, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 29, "time": 0.184, "bad": [2, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 34, "time": 0.226, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 23, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 26, "time": 0.144, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 21, "time": 0.17, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 21, "time": 0.154, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 21, "time": 0.149, "bad": [2, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 28, "time": 0.217, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 23, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 25, "time": 0.15, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 24, "time": 0.158, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 27, "time": 0.183, "bad": [0, 0, 7], "ops": [1, 1, 9, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 28, "time": 0.196, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 22, "time": 0.149, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 28, "time": 0.14, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 21, "time": 0.085, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 21, "time": 0.089, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.135, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 21, "time": 0.124, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 22, "time": 0.121, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 30, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 26, "time": 0.182, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 22, "time": 0.118, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 24, "time": 0.122, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 32, "time": 0.209, "bad": [4, 1, 0], "ops": [4, 2, 2, 4, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 24, "time": 0.178, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 25, "time": 0.197, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 23, "time": 0.147, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 24, "time": 0.161, "bad": [0, 0, 0], "ops": [1, 1, 1, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 21, "time": 0.145, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 23, "time": 0.162, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 24, "time": 0.147, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 28, "time": 0.165, "bad": [2, 0, 6], "ops": [2, 2, 10, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 25, "time": 0.146, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 32, "time": 0.197, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 22, "time": 0.16, "bad": [0, 0, 6], "ops": [1, 1, 8, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 33, "time": 0.21, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 26, "time": 0.172, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 19, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 33, "time": 0.209, "bad": [2, 0, 4], "ops": [2, 2, 7, 4, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 24, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 28, "time": 0.189, "bad": [2, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 22, "time": 0.169, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 26, "time": 0.164, "bad": [0, 0, 7], "ops": [2, 2, 9, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 30, "time": 0.185, "bad": [0, 0, 5], "ops": [2, 2, 8, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 25, "time": 0.172, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 20, "time": 0.132, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 24, "time": 0.191, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 25, "time": 0.191, "bad": [0, 2, 0], "ops": [5, 3, 4, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 25, "time": 0.144, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 23, "time": 0.171, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 23, "time": 0.182, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 24, "time": 0.196, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 25, "time": 0.194, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 34, "time": 0.235, "bad": [2, 1, 6], "ops": [5, 4, 9, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 23, "time": 0.11, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 20, "time": 0.173, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 26, "time": 0.163, "bad": [0, 0, 8], "ops": [2, 2, 11, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 21, "time": 0.153, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 27, "time": 0.197, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 26, "time": 0.149, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 25, "time": 0.181, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 21, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 34, "time": 0.199, "bad": [2, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 25, "time": 0.145, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 27, "time": 0.186, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 23, "time": 0.17, "bad": [1, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 23, "time": 0.195, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 24, "time": 0.156, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 24, "time": 0.171, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 89, "n": 3, "success": false, "steps": 200, "time": 4.43, "bad": [6, 0, 0], "ops": [5, 5, 4, 3, 1]}, {"seed": 90, "n": 2, "success": true, "steps": 30, "time": 0.173, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 25, "time": 0.188, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 25, "time": 0.18, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 30, "time": 0.199, "bad": [2, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 24, "time": 0.15, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 23, "time": 0.197, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 26, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 28, "time": 0.181, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 26, "time": 0.185, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 28, "time": 0.192, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_planned2.txt b/stats_planned2.txt
index 3da78c9..649db49 100644
--- a/stats_planned2.txt
+++ b/stats_planned2.txt
@@ -6,3 +6,7 @@
    6      6  {'seed': 50, 'n': 3, 'success': True, 'steps': 24, 'time': 0.147, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    7      7  {'seed': 60, 'n': 1, 'success': True, 'steps': 28, 'time': 0.189, 'bad': [2, 0, 2], 'ops': [1, 1, 4, 2, 2]}
    8      8  {'seed': 70, 'n': 2, 'success': True, 'steps': 23, 'time': 0.182, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
           9 +{'seed': 80, 'n': 3, 'success': True, 'steps': 25, 'time': 0.181, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
          10 +{'seed': 89, 'n': 3, 'success': False, 'steps': 200, 'time': 4.43, 'bad': [6, 0, 0], 'ops': [5, 5, 4, 3, 1]}
          11 +{'seed': 90, 'n': 2, 'success': True, 'steps': 30, 'time': 0.173, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
          12 +SUMMARY 99 100 mean 26.97 max_time 4.43
```

</details>

<a id="C025"></a>
### C025 · Model the measured octagonal rover clearance around tall pillars

Commit `fb1bd7628ea108fa7f0014b6bf2dffb3ff448d74`; parents: e59551ba7b1f59471e14be0b5f22ca496a3fc8e2. Recorded author date: 2026-09-21T22:21:04+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0126](01_timeline.md#E0126): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C025_fb1bd76_approach.py) · [Exact all-file diff](evidence/diffs/C025_fb1bd76.diff)

[Previous saved controller snapshot](evidence/versions/C023_71a6844_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8fffc9c..6f78e04 100644
--- a/approach.py
+++ b/approach.py
@@ -1,4 +1,3 @@
    1        -import math
    2      1  import heapq
    3      2  import numpy as np
    4      3  from task_planner import assign_tasks
@@ -24,12 +23,15 @@ class GeneratedApproach:
   24     23          self.lander = self.xy(state, self.objects(state, 'lander')[0])
   25     24          self.rects = []
   26     25          self.occluders = []
          26 +        self.pillars = []
   27     27          for o in self.objects(state, 'obstacle'):
   28     28              p = self.xy(state, o)
   29     29              h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
   30        -            self.rects.append((p-h, p+h))
   31     30              if state.get(o, 'half_z') > .1:
   32     31                  self.occluders.append((p-h, p+h))
          32 +                self.pillars.append(p)
          33 +            else:
          34 +                self.rects.append((p-h, p+h))
   33     35          self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
   34     36          self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
   35     37          axis = np.arange(-2.2, 2.201, .1)
@@ -49,7 +51,6 @@ class GeneratedApproach:
   49     51          self.fail = [0,0]
   50     52          self.tick = 0
   51     53          self.last_op = [None, None]
   52        -        self.bad_views = {}
   53     54          self.schedule = assign_tasks(self,state)
   54     55  
   55     56      def sample_safe(self, state, pts, k):
@@ -64,6 +65,9 @@ class GeneratedApproach:
   64     65          good = np.all(np.abs(pts) <= 2.265, axis=-1)
   65     66          for lo,hi in self.rects:
   66     67              good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
          68 +        for center in self.pillars:
          69 +            delta=np.abs(pts-center)
          70 +            good &= ~((delta[...,0]<.265)&(delta[...,1]<.25)&(np.sum(delta,axis=-1)<.405))
   67     71          return good
   68     72  
   69     73      def visible(self, pts, target, radius):
@@ -130,10 +134,9 @@ class GeneratedApproach:
  130    134          need=self.needed(s)
  131    135          for k,o in enumerate(self.objectives):
  132    136              if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
  133        -        if True:
  134        -            for k,o in enumerate(self.samples):
  135        -                soil=int(s.get(o,'is_soil'))
  136        -                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
         137 +        for k,o in enumerate(self.samples):
         138 +            soil=int(s.get(o,'is_soil'))
         139 +            if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
  137    140          if self.schedule is not None:
  138    141              schedule=self.schedule[r]
  139    142              while schedule:
@@ -207,7 +210,7 @@ class GeneratedApproach:
  207    210                  d=point-p
  208    211                  if np.max(np.abs(d))>.20001:break
  209    212                  probes=p+np.linspace(0,1,5)[:,None]*d
  210        -                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
         213 +                if (np.all(self.valid(probes)) or (not self.valid(p[None,:])[0] and self.valid(point[None,:])[0])) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
  211    214                  else:break
  212    215              if selected>0:del path[:selected]
  213    216              d=np.clip(dest-p,-.2,.2)
diff --git a/approach_pipeline.py b/approach_pipeline.py
new file mode 100644
index 0000000..8fffc9c
--- /dev/null
+++ b/approach_pipeline.py
@@ -0,0 +1,238 @@
           1 +import math
           2 +import heapq
           3 +import numpy as np
           4 +from task_planner import assign_tasks
           5 +
           6 +
           7 +class GeneratedApproach:
           8 +    """Feedback navigation and task allocation for the two rovers."""
           9 +    def __init__(self, action_space, observation_space, primitives):
          10 +        self.space = observation_space
          11 +        self.types = {t.name: t for t in observation_space.types}
          12 +
          13 +    def objects(self, state, kind):
          14 +        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
          15 +
          16 +    def xy(self, state, obj):
          17 +        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
          18 +
          19 +    def reset(self, state, info):
          20 +        self.rovers = self.objects(state, 'rover')
          21 +        self.objectives = self.objects(state, 'objective')
          22 +        self.samples = self.objects(state, 'sample')
          23 +        self.home = [self.xy(state, r) for r in self.rovers]
          24 +        self.lander = self.xy(state, self.objects(state, 'lander')[0])
          25 +        self.rects = []
          26 +        self.occluders = []
          27 +        for o in self.objects(state, 'obstacle'):
          28 +            p = self.xy(state, o)
          29 +            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
          30 +            self.rects.append((p-h, p+h))
          31 +            if state.get(o, 'half_z') > .1:
          32 +                self.occluders.append((p-h, p+h))
          33 +        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
          34 +        self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
          35 +        axis = np.arange(-2.2, 2.201, .1)
          36 +        self.size = len(axis)
          37 +        xx, yy = np.meshgrid(axis, axis)
          38 +        self.points = np.column_stack([xx.ravel(), yy.ravel()])
          39 +        self.free = self.valid(self.points)
          40 +        self.masks = {}
          41 +        for k, o in enumerate(self.objectives):
          42 +            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
          43 +        for k, o in enumerate(self.samples):
          44 +            self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
          45 +        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
          46 +        self.tasks = [None,None]
          47 +        self.paths = [[],[]]
          48 +        self.previous = [None,None]
          49 +        self.fail = [0,0]
          50 +        self.tick = 0
          51 +        self.last_op = [None, None]
          52 +        self.bad_views = {}
          53 +        self.schedule = assign_tasks(self,state)
          54 +
          55 +    def sample_safe(self, state, pts, k):
          56 +        target=self.samples[k]
          57 +        good=np.linalg.norm(pts-self.xy(state,target),axis=1)<.242
          58 +        for obj in self.samples:
          59 +            if state.get(obj,'is_soil')!=state.get(target,'is_soil'):
          60 +                good &= np.linalg.norm(pts-self.xy(state,obj),axis=1)>.255
          61 +        return good
          62 +
          63 +    def valid(self, pts):
          64 +        good = np.all(np.abs(pts) <= 2.265, axis=-1)
          65 +        for lo,hi in self.rects:
          66 +            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
          67 +        return good
          68 +
          69 +    def visible(self, pts, target, radius):
          70 +        good = np.linalg.norm(pts-target,axis=1)<radius
          71 +        d = target-pts
          72 +        length2 = np.maximum(np.sum(d*d,axis=1),1e-12)
          73 +        for lo,hi in self.occluders:
          74 +            center=(lo+hi)*.5
          75 +            t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
          76 +            closest=pts+t[:,None]*d
          77 +            clearance=min(.155,float(np.linalg.norm(target-center))*.85)
          78 +            good &= np.linalg.norm(closest-center,axis=1)>clearance
          79 +        return good
          80 +
          81 +    def route(self, start, mask, other=None):
          82 +        # A multi-goal Dijkstra on a small occupancy grid.
          83 +        free=self.free.copy()
          84 +        if other is not None:
          85 +            free &= np.linalg.norm(self.points-other,axis=1)>.4
          86 +        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
          87 +        root=next((int(j) for j in starts if free[j]),int(starts[0]))
          88 +        dist={root:0.}; parent={}; queue=[(0.,root)]
          89 +        n=self.size
          90 +        end=None
          91 +        while queue:
          92 +            cost,j=heapq.heappop(queue)
          93 +            if cost!=dist[j]: continue
          94 +            if mask[j]: end=j;break
          95 +            x=j%n;y=j//n
          96 +            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
          97 +                nx=x+dx;ny=y+dy
          98 +                if nx<0 or nx>=n or ny<0 or ny>=n:continue
          99 +                k=ny*n+nx
         100 +                if not free[k]:continue
         101 +                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
         102 +                v=cost+1.+(.001 if dx and dy else 0.)
         103 +                if v<dist.get(k,1e9):
         104 +                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
         105 +        if end is None:return [],1e6
         106 +        path=[end]
         107 +        while path[-1]!=root:path.append(parent[path[-1]])
         108 +        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
         109 +
         110 +    def have(self,s,k):
         111 +        o=self.objectives[k]
         112 +        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
         113 +
         114 +    def needed(self,s):
         115 +        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
         116 +
         117 +    def pending(self,s,r):
         118 +        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
         119 +
         120 +    def completed(self,s,r,task):
         121 +        kind,k=task
         122 +        if kind=='image':return self.have(s,k)
         123 +        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
         124 +        if kind=='send':return not self.pending(s,r)
         125 +        return s.get(self.rovers[r],'at_home')>.5
         126 +
         127 +    def choose(self,s,r,p,other):
         128 +        candidates=[]
         129 +        reserved=self.tasks[1-r]
         130 +        need=self.needed(s)
         131 +        for k,o in enumerate(self.objectives):
         132 +            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
         133 +        if True:
         134 +            for k,o in enumerate(self.samples):
         135 +                soil=int(s.get(o,'is_soil'))
         136 +                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
         137 +        if self.schedule is not None:
         138 +            schedule=self.schedule[r]
         139 +            while schedule:
         140 +                kind,k=schedule[0]
         141 +                if (kind=='image' and self.have(s,k)) or (kind=='soil' and not need[k]):schedule.pop(0)
         142 +                else:break
         143 +            if schedule:
         144 +                kind,k=schedule[0]
         145 +                planned=[t for t in candidates if t==schedule[0] or (kind=='soil' and t[0]=='sample' and int(s.get(self.samples[t[1]],'is_soil'))==k)]
         146 +                if planned:candidates=planned
         147 +            else:candidates=[]
         148 +        best=None;score=1e9;path=[]
         149 +        for task in candidates:
         150 +            pp,cost=self.route(p,self.masks[task],other)
         151 +            cost+=2 if task[0]=='image' else 0
         152 +            if cost<score and cost<1e5:best=task;score=cost;path=pp
         153 +        if best is None and candidates and self.schedule is not None:
         154 +            self.schedule=None
         155 +            self.choose(s,r,p,other)
         156 +            return
         157 +        if best is None:
         158 +            if self.pending(s,r) and s.get(self.rovers[r],'at_home')>.5:best=('send',0);path,_=self.route(p,self.masks[best],other)
         159 +            else:
         160 +                best=('home',r)
         161 +                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
         162 +                path,_=self.route(p,mask,other)
         163 +                if s.get(self.rovers[r],'at_home')>.5:path=[]
         164 +        self.tasks[r]=best;self.paths[r]=path
         165 +
         166 +    def result_count(self, s, r):
         167 +        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
         168 +
         169 +    def get_action(self, state):
         170 +        s=state; self.tick+=1
         171 +        action=np.zeros(8,dtype=np.float32)
         172 +        pos=[self.xy(s,r) for r in self.rovers]
         173 +        for r in range(2):
         174 +            p=pos[r];rob=self.rovers[r]
         175 +            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
         176 +                self.fail[r]+=1
         177 +            else:self.fail[r]=0
         178 +            task=self.tasks[r]
         179 +            last=self.last_op[r]
         180 +            if last is not None:
         181 +                old_task, old_p, old_op, old_count = last
         182 +                failed = ((old_task[0]=='image' and old_op == -.5 and s.get(rob,'calibrated')<.5) or
         183 +                          (old_task[0]=='image' and old_op == -1/6 and self.result_count(s,r)<=old_count) or
         184 +                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
         185 +                if failed and task==old_task and task[0] in ('image','send'):
         186 +                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
         187 +                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
         188 +            if task is None or self.completed(s,r,task):
         189 +                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         190 +            if self.fail[r]>=2:
         191 +                self.paths[r]=[]
         192 +                # Infer blocked configuration and route around it.
         193 +                blocked=p+self.previous[r][1]
         194 +                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
         195 +                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
         196 +                else:mask=self.masks[task]
         197 +                self.paths[r],_=self.route(p,mask,pos[1-r])
         198 +                if task[0]!='home' and not self.paths[r]:
         199 +                    self.tasks[r]=None
         200 +                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         201 +                self.fail[r]=0
         202 +            path=self.paths[r]
         203 +            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
         204 +            dest=p.copy()
         205 +            selected=-1
         206 +            for pi,point in enumerate(path[:5]):
         207 +                d=point-p
         208 +                if np.max(np.abs(d))>.20001:break
         209 +                probes=p+np.linspace(0,1,5)[:,None]*d
         210 +                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
         211 +                else:break
         212 +            if selected>0:del path[:selected]
         213 +            d=np.clip(dest-p,-.2,.2)
         214 +            q=p+d
         215 +            op=0.
         216 +            kind,k=task
         217 +            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
         218 +            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
         219 +                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
         220 +                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
         221 +            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
         222 +                op=.5
         223 +                if path and np.linalg.norm(q-path[-1])>.06:op=0.
         224 +            if op==0 and s.get(rob,'store_full')>.5:op=5/6
         225 +            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
         226 +            # Use otherwise idle travel steps for camera work.
         227 +            if op in (0.,.5) and np.linalg.norm(d)>.01:
         228 +                visible=[]
         229 +                for j,o in enumerate(self.objectives):
         230 +                    if s.get(o,'have_image_rover%d'%r)<.5 and self.visible(q[None,:],self.xy(s,o),1.97)[0]:
         231 +                        visible.append((float(np.linalg.norm(q-self.xy(s,o))),j))
         232 +                if visible:
         233 +                    _,j=min(visible)
         234 +                    if not self.have(s,j):op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
         235 +            action[r*4:r*4+2]=d;action[r*4+3]=op
         236 +            self.previous[r]=(p.copy(),d.copy())
         237 +            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
         238 +        return action
diff --git a/stats_pipeline.json b/stats_pipeline.json
new file mode 100644
index 0000000..b1b43f6
--- /dev/null
+++ b/stats_pipeline.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "n": 3, "success": true, "steps": 28, "time": 0.211, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 21, "time": 0.198, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 21, "time": 0.219, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 24, "time": 0.236, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 23, "time": 0.22, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 25, "time": 0.27, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 21, "time": 0.197, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 27, "time": 0.246, "bad": [2, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 26, "time": 0.204, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 28, "time": 0.253, "bad": [4, 0, 2], "ops": [2, 2, 5, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 22, "time": 0.212, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 20, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 24, "time": 0.19, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 27, "time": 0.272, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 31, "time": 0.227, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 27, "time": 0.28, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 23, "time": 0.209, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 23, "time": 0.239, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 24, "time": 0.223, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 30, "time": 0.243, "bad": [4, 0, 5], "ops": [2, 2, 7, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 27, "time": 0.163, "bad": [0, 0, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 23, "time": 0.155, "bad": [0, 0, 6], "ops": [1, 1, 8, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 24, "time": 0.246, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 20, "time": 0.162, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 20, "time": 0.193, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 20, "time": 0.183, "bad": [2, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 26, "time": 0.253, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 22, "time": 0.166, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 24, "time": 0.158, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 23, "time": 0.204, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 24, "time": 0.142, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 27, "time": 0.236, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 21, "time": 0.227, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 27, "time": 0.236, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 20, "time": 0.084, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 20, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.168, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 20, "time": 0.156, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 21, "time": 0.167, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 25, "time": 0.203, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 25, "time": 0.19, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 21, "time": 0.179, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 23, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 29, "time": 0.208, "bad": [4, 0, 0], "ops": [2, 2, 2, 4, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 23, "time": 0.195, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 24, "time": 0.207, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 21, "time": 0.18, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 25, "time": 0.169, "bad": [0, 0, 6], "ops": [1, 1, 7, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 20, "time": 0.128, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 22, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 23, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 25, "time": 0.105, "bad": [2, 0, 4], "ops": [2, 2, 8, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 23, "time": 0.154, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 30, "time": 0.137, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 21, "time": 0.131, "bad": [0, 0, 5], "ops": [1, 1, 7, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 27, "time": 0.215, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 25, "time": 0.178, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 18, "time": 0.117, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 32, "time": 0.218, "bad": [2, 0, 4], "ops": [2, 2, 7, 4, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 23, "time": 0.209, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 22, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 21, "time": 0.175, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 25, "time": 0.164, "bad": [0, 0, 5], "ops": [2, 2, 7, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 26, "time": 0.18, "bad": [0, 0, 4], "ops": [2, 2, 7, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 23, "time": 0.163, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 19, "time": 0.137, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 23, "time": 0.175, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 24, "time": 0.171, "bad": [0, 2, 0], "ops": [5, 3, 4, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 22, "time": 0.135, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 22, "time": 0.146, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 22, "time": 0.104, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 23, "time": 0.16, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 23, "time": 0.194, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 34, "time": 0.259, "bad": [2, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 24, "time": 0.162, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 19, "time": 0.169, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 24, "time": 0.166, "bad": [0, 0, 6], "ops": [2, 2, 9, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 20, "time": 0.146, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 26, "time": 0.212, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 24, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 23, "time": 0.197, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 20, "time": 0.146, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 34, "time": 0.268, "bad": [2, 0, 6], "ops": [3, 3, 8, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 24, "time": 0.209, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 25, "time": 0.189, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 22, "time": 0.203, "bad": [1, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 22, "time": 0.199, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 23, "time": 0.189, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 22, "time": 0.183, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 89, "n": 3, "success": true, "steps": 58, "time": 0.432, "bad": [6, 0, 0], "ops": [5, 5, 5, 4, 2]}, {"seed": 90, "n": 2, "success": true, "steps": 29, "time": 0.172, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 24, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 24, "time": 0.192, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 27, "time": 0.215, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 22, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 22, "time": 0.102, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 25, "time": 0.163, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 27, "time": 0.182, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 24, "time": 0.199, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 26, "time": 0.209, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_pipeline.txt b/stats_pipeline.txt
index 5398c70..7c7e334 100644
--- a/stats_pipeline.txt
+++ b/stats_pipeline.txt
@@ -7,3 +7,5 @@
    7      7  {'seed': 60, 'n': 1, 'success': True, 'steps': 22, 'time': 0.16, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
    8      8  {'seed': 70, 'n': 2, 'success': True, 'steps': 22, 'time': 0.104, 'bad': [0, 1, 0], 'ops': [3, 2, 3, 2, 2]}
    9      9  {'seed': 80, 'n': 3, 'success': True, 'steps': 23, 'time': 0.197, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
          10 +{'seed': 90, 'n': 2, 'success': True, 'steps': 29, 'time': 0.172, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
          11 +SUMMARY 100 100 mean 24.19 max_time 0.432
```

</details>

<a id="C026"></a>
### C026 · Bound tour enumeration for larger objective-count variants

Commit `f862c530b34f0fa06ba64fc7a8541b3df13b55be`; parents: fb1bd7628ea108fa7f0014b6bf2dffb3ff448d74. Recorded author date: 2026-09-21T22:22:56+02:00.

File roles (automatic): setup/other, support code (role needs review).

- [E0124](01_timeline.md#E0124): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C026_f862c53.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/stats_final2000.txt b/stats_final2000.txt
new file mode 100644
index 0000000..45f3fab
--- /dev/null
+++ b/stats_final2000.txt
@@ -0,0 +1,3 @@
           1 +{'seed': 2000, 'n': 1, 'success': True, 'steps': 22, 'time': 0.105, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
           2 +{'seed': 2010, 'n': 3, 'success': True, 'steps': 24, 'time': 0.222, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
           3 +{'seed': 2020, 'n': 1, 'success': True, 'steps': 23, 'time': 0.103, 'bad': [0, 0, 7], 'ops': [1, 1, 10, 2, 2]}
diff --git a/stats_final4.txt b/stats_final4.txt
new file mode 100644
index 0000000..303c1bc
--- /dev/null
+++ b/stats_final4.txt
@@ -0,0 +1,2 @@
           1 +{'seed': 1200, 'n': 4, 'success': True, 'steps': 26, 'time': 0.169, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
           2 +{'seed': 1210, 'n': 4, 'success': True, 'steps': 24, 'time': 0.292, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
diff --git a/stats_final400.txt b/stats_final400.txt
new file mode 100644
index 0000000..5afcaa4
--- /dev/null
+++ b/stats_final400.txt
@@ -0,0 +1,3 @@
           1 +{'seed': 400, 'n': 3, 'success': True, 'steps': 23, 'time': 0.191, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
           2 +{'seed': 410, 'n': 2, 'success': True, 'steps': 22, 'time': 0.217, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
           3 +{'seed': 420, 'n': 2, 'success': True, 'steps': 21, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [2, 2, 2, 2, 2]}
diff --git a/stats_octagon.txt b/stats_octagon.txt
new file mode 100644
index 0000000..ba0999d
--- /dev/null
+++ b/stats_octagon.txt
@@ -0,0 +1,9 @@
           1 +{'seed': 0, 'n': 3, 'success': True, 'steps': 28, 'time': 0.138, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
           2 +{'seed': 10, 'n': 3, 'success': True, 'steps': 22, 'time': 0.171, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           3 +{'seed': 20, 'n': 3, 'success': True, 'steps': 27, 'time': 0.222, 'bad': [0, 0, 0], 'ops': [4, 3, 2, 2, 2]}
           4 +{'seed': 30, 'n': 1, 'success': True, 'steps': 24, 'time': 0.163, 'bad': [0, 0, 4], 'ops': [1, 1, 6, 2, 2]}
           5 +{'seed': 40, 'n': 2, 'success': True, 'steps': 25, 'time': 0.151, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           6 +{'seed': 50, 'n': 3, 'success': True, 'steps': 24, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
           7 +{'seed': 60, 'n': 1, 'success': True, 'steps': 22, 'time': 0.174, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
           8 +{'seed': 70, 'n': 2, 'success': True, 'steps': 22, 'time': 0.218, 'bad': [0, 1, 0], 'ops': [3, 2, 3, 2, 2]}
           9 +{'seed': 80, 'n': 3, 'success': True, 'steps': 23, 'time': 0.214, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
diff --git a/task_planner.py b/task_planner.py
index daac8ed..24a28ae 100644
--- a/task_planner.py
+++ b/task_planner.py
@@ -1,11 +1,13 @@
    1      1  """Small cooperative task-tour planner using grid distance transforms."""
    2        -import math
    3      2  import numpy as np
    4      3  from scipy.sparse import csr_matrix
    5      4  from scipy.sparse.csgraph import dijkstra
    6      5  
    7      6  
    8      7  def assign_tasks(policy, state):
           8 +    # Keep planning bounded if a future variant adds many more objectives.
           9 +    if len(policy.objectives)>5:
          10 +        return None
    9     11      n=policy.size
   10     12      free=policy.free.reshape(n,n)
   11     13      ids=np.arange(n*n).reshape(n,n)
```

</details>

<a id="C027"></a>
### C027 · Add reset-state screening for tight or unreachable configurations

Commit `fc2780d0093a9fe680dbde5af036d9fd8793fffc`; parents: f862c530b34f0fa06ba64fc7a8541b3df13b55be. Recorded author date: 2026-09-21T22:23:36+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0136](01_timeline.md#E0136): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C027_fc2780d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/scan_states.py b/scan_states.py
new file mode 100644
index 0000000..0a082c7
--- /dev/null
+++ b/scan_states.py
@@ -0,0 +1,22 @@
           1 +import numpy as np
           2 +import scipy.ndimage as ndi
           3 +import json
           4 +import approach
           5 +from env_client import make_env
           6 +approach.assign_tasks=lambda policy,state: None
           7 +E=make_env();out=[]
           8 +for seed in range(5000,6000):
           9 + s,info=E.reset(seed=seed);A=approach.GeneratedApproach(E.action_space,E.observation_space,{});A.reset(s,info)
          10 + labels,_=ndi.label(A.free.reshape(A.size,A.size));labels=labels.ravel();reachable=np.zeros(len(labels),bool);why=[]
          11 + for r in range(2):
          12 +  if not A.valid(A.home[r][None,:])[0]:why.append('home%d_inside_margin'%r)
          13 +  root=np.argmin(np.linalg.norm(A.points-A.home[r],axis=1)+(~A.free)*100)
          14 +  reachable |= labels==labels[root]
          15 + for k,o in enumerate(A.objectives):
          16 +  if not np.any(A.masks[('image',k)]&reachable):why.append('image%d_unreachable'%k)
          17 + for soil in range(2):
          18 +  if not any(np.any(A.masks[('sample',k)]&reachable) for k,o in enumerate(A.samples) if int(s.get(o,'is_soil'))==soil):why.append('sample%d_unreachable'%soil)
          19 + if why:
          20 +  print(seed,why,flush=True);out.append((seed,why))
          21 + if seed%100==0:print('PROGRESS',seed,flush=True)
          22 +open('scan_results.json','w').write(json.dumps(out));E.close();print('DONE',len(out),flush=True)
diff --git a/stats_final2000.txt b/stats_final2000.txt
index 45f3fab..ff9053f 100644
--- a/stats_final2000.txt
+++ b/stats_final2000.txt
@@ -1,3 +1,4 @@
    1      1  {'seed': 2000, 'n': 1, 'success': True, 'steps': 22, 'time': 0.105, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    2      2  {'seed': 2010, 'n': 3, 'success': True, 'steps': 24, 'time': 0.222, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    3      3  {'seed': 2020, 'n': 1, 'success': True, 'steps': 23, 'time': 0.103, 'bad': [0, 0, 7], 'ops': [1, 1, 10, 2, 2]}
           4 +{'seed': 2030, 'n': 1, 'success': True, 'steps': 19, 'time': 0.106, 'bad': [0, 0, 6], 'ops': [1, 1, 9, 2, 2]}
diff --git a/stats_final4.txt b/stats_final4.txt
index 303c1bc..443f633 100644
--- a/stats_final4.txt
+++ b/stats_final4.txt
@@ -1,2 +1,3 @@
    1      1  {'seed': 1200, 'n': 4, 'success': True, 'steps': 26, 'time': 0.169, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
    2      2  {'seed': 1210, 'n': 4, 'success': True, 'steps': 24, 'time': 0.292, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
           3 +{'seed': 1220, 'n': 4, 'success': True, 'steps': 23, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [5, 5, 3, 2, 2]}
diff --git a/stats_final400.txt b/stats_final400.txt
index 5afcaa4..4b720b5 100644
--- a/stats_final400.txt
+++ b/stats_final400.txt
@@ -1,3 +1,4 @@
    1      1  {'seed': 400, 'n': 3, 'success': True, 'steps': 23, 'time': 0.191, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    2      2  {'seed': 410, 'n': 2, 'success': True, 'steps': 22, 'time': 0.217, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    3      3  {'seed': 420, 'n': 2, 'success': True, 'steps': 21, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [2, 2, 2, 2, 2]}
           4 +{'seed': 430, 'n': 1, 'success': True, 'steps': 22, 'time': 0.17, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
diff --git a/stats_octagon.txt b/stats_octagon.txt
index ba0999d..218b3e7 100644
--- a/stats_octagon.txt
+++ b/stats_octagon.txt
@@ -7,3 +7,4 @@
    7      7  {'seed': 60, 'n': 1, 'success': True, 'steps': 22, 'time': 0.174, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
    8      8  {'seed': 70, 'n': 2, 'success': True, 'steps': 22, 'time': 0.218, 'bad': [0, 1, 0], 'ops': [3, 2, 3, 2, 2]}
    9      9  {'seed': 80, 'n': 3, 'success': True, 'steps': 23, 'time': 0.214, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
          10 +{'seed': 90, 'n': 2, 'success': True, 'steps': 29, 'time': 0.187, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
```

</details>

<a id="C028"></a>
### C028 · Recover from exhausted viewpoints and stalled local navigation

Commit `26a6f98d7bc8ecf6b12afbccc663d3f851c37a0e`; parents: fc2780d0093a9fe680dbde5af036d9fd8793fffc. Recorded author date: 2026-09-21T22:27:00+02:00.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0140](01_timeline.md#E0140): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C028_26a6f98_approach.py) · [Exact all-file diff](evidence/diffs/C028_26a6f98.diff)

[Previous saved controller snapshot](evidence/versions/C025_fb1bd76_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6f78e04..3fb7d96 100644
--- a/approach.py
+++ b/approach.py
@@ -52,6 +52,10 @@ class GeneratedApproach:
   52     52          self.tick = 0
   53     53          self.last_op = [None, None]
   54     54          self.schedule = assign_tasks(self,state)
          55 +        self.loose_views = set()
          56 +        self.rejected_views = {}
          57 +        self.still = [0,0]
          58 +        self.signatures = [None,None]
   55     59  
   56     60      def sample_safe(self, state, pts, k):
   57     61          target=self.samples[k]
@@ -169,12 +173,37 @@ class GeneratedApproach:
  169    173      def result_count(self, s, r):
  170    174          return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
  171    175  
         176 +    def replan(self,s,r,p,other,explore=False):
         177 +        task=self.tasks[r]
         178 +        kind,k=task
         179 +        mask=(np.linalg.norm(self.points-self.home[r],axis=1)<.24) if kind=='home' else self.masks[task]
         180 +        path,_=self.route(p,mask,other)
         181 +        if kind in ('image','send') and (explore or not path):
         182 +            # If the conservative sight model runs out of positions, use
         183 +            # direct operator feedback to explore nearby untested viewpoints.
         184 +            target=self.xy(s,self.objectives[k]) if kind=='image' else self.lander
         185 +            radius=1.9 if kind=='image' else 3.8
         186 +            mask=self.free & (np.linalg.norm(self.points-target,axis=1)<radius)
         187 +            for failed in self.rejected_views.get(task,[]):
         188 +                mask &= np.linalg.norm(self.points-failed,axis=1)>.085
         189 +            self.masks[task]=mask
         190 +            self.loose_views.add(task)
         191 +            path,_=self.route(p,mask,other)
         192 +        self.paths[r]=path
         193 +        if not path and kind!='home':
         194 +            self.schedule=None
         195 +            self.tasks[r]=None
         196 +            self.choose(s,r,p,other)
         197 +
  172    198      def get_action(self, state):
  173    199          s=state; self.tick+=1
  174    200          action=np.zeros(8,dtype=np.float32)
  175    201          pos=[self.xy(s,r) for r in self.rovers]
  176    202          for r in range(2):
  177    203              p=pos[r];rob=self.rovers[r]
         204 +            signature=(tuple(p),s.get(rob,'store_full'),s.get(rob,'calibrated'),self.result_count(s,r))
         205 +            self.still[r]=self.still[r]+1 if signature==self.signatures[r] else 0
         206 +            self.signatures[r]=signature
  178    207              if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
  179    208                  self.fail[r]+=1
  180    209              else:self.fail[r]=0
@@ -186,8 +215,10 @@ class GeneratedApproach:
  186    215                            (old_task[0]=='image' and old_op == -1/6 and self.result_count(s,r)<=old_count) or
  187    216                            (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
  188    217                  if failed and task==old_task and task[0] in ('image','send'):
  189        -                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
  190        -                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
         218 +                    self.rejected_views.setdefault(task,[]).append(p.copy())
         219 +                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>(.085 if task in self.loose_views else .22)
         220 +                    self.replan(s,r,p,pos[1-r])
         221 +                    task=self.tasks[r]
  191    222              if task is None or self.completed(s,r,task):
  192    223                  self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  193    224              if self.fail[r]>=2:
@@ -195,20 +226,23 @@ class GeneratedApproach:
  195    226                  # Infer blocked configuration and route around it.
  196    227                  blocked=p+self.previous[r][1]
  197    228                  self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
  198        -                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  199        -                else:mask=self.masks[task]
  200        -                self.paths[r],_=self.route(p,mask,pos[1-r])
  201        -                if task[0]!='home' and not self.paths[r]:
  202        -                    self.tasks[r]=None
  203        -                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
         229 +                self.replan(s,r,p,pos[1-r]);task=self.tasks[r]
  204    230                  self.fail[r]=0
         231 +            if self.still[r]>=6 and not self.completed(s,r,task):
         232 +                if task[0]=='sample':
         233 +                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.12
         234 +                self.replan(s,r,p,pos[1-r],explore=True);task=self.tasks[r]
         235 +                self.still[r]=0
  205    236              path=self.paths[r]
  206    237              while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
  207    238              dest=p.copy()
  208    239              selected=-1
  209    240              for pi,point in enumerate(path[:5]):
  210    241                  d=point-p
  211        -                if np.max(np.abs(d))>.20001:break
         242 +                if np.max(np.abs(d))>.20001:
         243 +                    if pi:break
         244 +                    point=p+np.clip(d,-.2,.2)
         245 +                    d=point-p
  212    246                  probes=p+np.linspace(0,1,5)[:,None]*d
  213    247                  if (np.all(self.valid(probes)) or (not self.valid(p[None,:])[0] and self.valid(point[None,:])[0])) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
  214    248                  else:break
@@ -218,10 +252,10 @@ class GeneratedApproach:
  218    252              op=0.
  219    253              kind,k=task
  220    254              if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
  221        -            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
         255 +            elif kind=='image' and ((task in self.loose_views and np.linalg.norm(q-self.xy(s,self.objectives[k]))<1.99) or self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]):
  222    256                  op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  223    257                  if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
  224        -            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
         258 +            elif kind=='send' and ((task in self.loose_views and np.linalg.norm(q-self.lander)<3.85) or self.visible(q[None,:],self.lander,3.85)[0]):
  225    259                  op=.5
  226    260                  if path and np.linalg.norm(q-path[-1])>.06:op=0.
  227    261              if op==0 and s.get(rob,'store_full')>.5:op=5/6
diff --git a/scan_results.json b/scan_results.json
new file mode 100644
index 0000000..e09d547
--- /dev/null
+++ b/scan_results.json
@@ -0,0 +1 @@
           1 +[[5828, ["sample0_unreachable"]]]
\ No newline at end of file
diff --git a/scan_results.txt b/scan_results.txt
new file mode 100644
index 0000000..61d17e9
--- /dev/null
+++ b/scan_results.txt
@@ -0,0 +1,12 @@
           1 +PROGRESS 5000
           2 +PROGRESS 5100
           3 +PROGRESS 5200
           4 +PROGRESS 5300
           5 +PROGRESS 5400
           6 +PROGRESS 5500
           7 +PROGRESS 5600
           8 +PROGRESS 5700
           9 +PROGRESS 5800
          10 +5828 ['sample0_unreachable']
          11 +PROGRESS 5900
          12 +DONE 1
diff --git a/stats_final2000.json b/stats_final2000.json
new file mode 100644
index 0000000..cf8917b
--- /dev/null
+++ b/stats_final2000.json
@@ -0,0 +1 @@
           1 +[{"seed": 2000, "n": 1, "success": true, "steps": 22, "time": 0.105, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2001, "n": 1, "success": true, "steps": 23, "time": 0.204, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2002, "n": 3, "success": true, "steps": 24, "time": 0.235, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 2003, "n": 3, "success": true, "steps": 22, "time": 0.234, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 2004, "n": 3, "success": true, "steps": 27, "time": 0.271, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 2005, "n": 1, "success": true, "steps": 20, "time": 0.178, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2006, "n": 1, "success": true, "steps": 20, "time": 0.156, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 2007, "n": 2, "success": true, "steps": 21, "time": 0.183, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 2008, "n": 3, "success": true, "steps": 24, "time": 0.24, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 2009, "n": 3, "success": true, "steps": 24, "time": 0.242, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 2010, "n": 3, "success": true, "steps": 24, "time": 0.222, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 2011, "n": 3, "success": true, "steps": 25, "time": 0.27, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 2012, "n": 3, "success": true, "steps": 22, "time": 0.236, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 2013, "n": 2, "success": true, "steps": 28, "time": 0.199, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 2014, "n": 2, "success": true, "steps": 23, "time": 0.208, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 2015, "n": 3, "success": true, "steps": 24, "time": 0.216, "bad": [0, 0, 6], "ops": [3, 3, 9, 2, 2]}, {"seed": 2016, "n": 1, "success": true, "steps": 20, "time": 0.108, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2017, "n": 2, "success": true, "steps": 21, "time": 0.195, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 2018, "n": 1, "success": true, "steps": 21, "time": 0.098, "bad": [0, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 2019, "n": 1, "success": true, "steps": 21, "time": 0.087, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 2020, "n": 1, "success": true, "steps": 23, "time": 0.103, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 2021, "n": 3, "success": true, "steps": 24, "time": 0.129, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 2022, "n": 3, "success": true, "steps": 23, "time": 0.177, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 2023, "n": 2, "success": true, "steps": 28, "time": 0.188, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 2024, "n": 1, "success": true, "steps": 21, "time": 0.156, "bad": [0, 0, 0], "ops": [1, 1, 1, 2, 2]}, {"seed": 2025, "n": 2, "success": true, "steps": 20, "time": 0.135, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 2026, "n": 3, "success": true, "steps": 24, "time": 0.235, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 2027, "n": 2, "success": true, "steps": 26, "time": 0.201, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 2028, "n": 2, "success": true, "steps": 24, "time": 0.209, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 2029, "n": 1, "success": true, "steps": 22, "time": 0.147, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 2030, "n": 1, "success": true, "steps": 19, "time": 0.106, "bad": [0, 0, 6], "ops": [1, 1, 9, 2, 2]}, {"seed": 2031, "n": 2, "success": true, "steps": 21, "time": 0.151, "bad": [0, 0, 3], "ops": [2, 2, 7, 2, 2]}, {"seed": 2032, "n": 2, "success": true, "steps": 31, "time": 0.262, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 2033, "n": 3, "success": true, "steps": 31, "time": 0.182, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 2034, "n": 2, "success": true, "steps": 21, "time": 0.184, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2035, "n": 1, "success": true, "steps": 20, "time": 0.161, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 2036, "n": 1, "success": true, "steps": 20, "time": 0.167, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 2037, "n": 3, "success": true, "steps": 23, "time": 0.191, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 2038, "n": 3, "success": true, "steps": 25, "time": 0.207, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 2039, "n": 3, "success": true, "steps": 24, "time": 0.138, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 2040, "n": 2, "success": true, "steps": 21, "time": 0.143, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 2041, "n": 2, "success": true, "steps": 25, "time": 0.222, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 2042, "n": 3, "success": true, "steps": 26, "time": 0.244, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 2043, "n": 2, "success": true, "steps": 22, "time": 0.13, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2044, "n": 2, "success": true, "steps": 26, "time": 0.173, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2045, "n": 1, "success": true, "steps": 25, "time": 0.17, "bad": [0, 1, 5], "ops": [2, 1, 6, 2, 2]}, {"seed": 2046, "n": 1, "success": true, "steps": 18, "time": 0.118, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2047, "n": 1, "success": true, "steps": 21, "time": 0.149, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2048, "n": 3, "success": true, "steps": 26, "time": 0.254, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 2049, "n": 1, "success": true, "steps": 22, "time": 0.15, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2050, "n": 2, "success": true, "steps": 22, "time": 0.182, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 2051, "n": 2, "success": true, "steps": 25, "time": 0.113, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 2052, "n": 1, "success": true, "steps": 22, "time": 0.112, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 2053, "n": 1, "success": true, "steps": 24, "time": 0.18, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 2054, "n": 3, "success": true, "steps": 24, "time": 0.219, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 2055, "n": 1, "success": true, "steps": 46, "time": 0.269, "bad": [0, 0, 22], "ops": [1, 1, 25, 2, 2]}, {"seed": 2056, "n": 2, "success": true, "steps": 24, "time": 0.203, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 2057, "n": 2, "success": true, "steps": 22, "time": 0.214, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 2058, "n": 2, "success": true, "steps": 25, "time": 0.238, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 2059, "n": 2, "success": true, "steps": 25, "time": 0.213, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2060, "n": 1, "success": true, "steps": 23, "time": 0.189, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2061, "n": 1, "success": true, "steps": 23, "time": 0.151, "bad": [0, 0, 5], "ops": [1, 1, 7, 2, 2]}, {"seed": 2062, "n": 3, "success": true, "steps": 25, "time": 0.236, "bad": [0, 3, 0], "ops": [6, 3, 3, 2, 2]}, {"seed": 2063, "n": 1, "success": true, "steps": 21, "time": 0.139, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2064, "n": 2, "success": true, "steps": 21, "time": 0.149, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 2065, "n": 1, "success": true, "steps": 22, "time": 0.154, "bad": [0, 0, 0], "ops": [1, 1, 1, 2, 2]}, {"seed": 2066, "n": 3, "success": true, "steps": 27, "time": 0.241, "bad": [0, 0, 0], "ops": [6, 5, 4, 2, 2]}, {"seed": 2067, "n": 2, "success": true, "steps": 26, "time": 0.192, "bad": [0, 0, 3], "ops": [2, 2, 5, 2, 2]}, {"seed": 2068, "n": 3, "success": true, "steps": 23, "time": 0.232, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 2069, "n": 2, "success": true, "steps": 21, "time": 0.208, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 2070, "n": 2, "success": true, "steps": 24, "time": 0.22, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 2071, "n": 1, "success": true, "steps": 39, "time": 0.245, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 2072, "n": 3, "success": true, "steps": 22, "time": 0.224, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 2073, "n": 1, "success": true, "steps": 20, "time": 0.171, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 2074, "n": 1, "success": true, "steps": 19, "time": 0.122, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2075, "n": 2, "success": true, "steps": 25, "time": 0.225, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 2076, "n": 3, "success": true, "steps": 24, "time": 0.209, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 2077, "n": 3, "success": true, "steps": 27, "time": 0.268, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 2078, "n": 3, "success": true, "steps": 22, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 2079, "n": 1, "success": true, "steps": 18, "time": 0.107, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 2080, "n": 3, "success": true, "steps": 26, "time": 0.241, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 2081, "n": 2, "success": true, "steps": 22, "time": 0.215, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 2082, "n": 1, "success": true, "steps": 22, "time": 0.161, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 2083, "n": 2, "success": true, "steps": 25, "time": 0.167, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 2084, "n": 2, "success": true, "steps": 25, "time": 0.169, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 2085, "n": 2, "success": true, "steps": 21, "time": 0.21, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 2086, "n": 2, "success": true, "steps": 20, "time": 0.165, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 2087, "n": 3, "success": true, "steps": 26, "time": 0.26, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 2088, "n": 1, "success": true, "steps": 26, "time": 0.166, "bad": [0, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 2089, "n": 3, "success": true, "steps": 23, "time": 0.211, "bad": [0, 0, 1], "ops": [3, 3, 6, 2, 2]}, {"seed": 2090, "n": 2, "success": true, "steps": 23, "time": 0.167, "bad": [0, 0, 7], "ops": [2, 2, 9, 2, 2]}, {"seed": 2091, "n": 1, "success": true, "steps": 25, "time": 0.192, "bad": [0, 2, 0], "ops": [3, 1, 3, 2, 2]}, {"seed": 2092, "n": 3, "success": true, "steps": 25, "time": 0.227, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 2093, "n": 1, "success": true, "steps": 19, "time": 0.171, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 2094, "n": 3, "success": true, "steps": 24, "time": 0.229, "bad": [0, 2, 0], "ops": [5, 3, 2, 2, 2]}, {"seed": 2095, "n": 1, "success": true, "steps": 20, "time": 0.144, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 2096, "n": 3, "success": true, "steps": 27, "time": 0.18, "bad": [0, 1, 0], "ops": [5, 4, 4, 2, 2]}, {"seed": 2097, "n": 1, "success": true, "steps": 25, "time": 0.158, "bad": [0, 0, 6], "ops": [1, 1, 7, 2, 2]}, {"seed": 2098, "n": 1, "success": true, "steps": 21, "time": 0.141, "bad": [0, 2, 0], "ops": [3, 1, 3, 2, 2]}, {"seed": 2099, "n": 2, "success": true, "steps": 20, "time": 0.2, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_final2000.txt b/stats_final2000.txt
index ff9053f..444e391 100644
--- a/stats_final2000.txt
+++ b/stats_final2000.txt
@@ -2,3 +2,10 @@
    2      2  {'seed': 2010, 'n': 3, 'success': True, 'steps': 24, 'time': 0.222, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    3      3  {'seed': 2020, 'n': 1, 'success': True, 'steps': 23, 'time': 0.103, 'bad': [0, 0, 7], 'ops': [1, 1, 10, 2, 2]}
    4      4  {'seed': 2030, 'n': 1, 'success': True, 'steps': 19, 'time': 0.106, 'bad': [0, 0, 6], 'ops': [1, 1, 9, 2, 2]}
           5 +{'seed': 2040, 'n': 2, 'success': True, 'steps': 21, 'time': 0.143, 'bad': [0, 0, 0], 'ops': [2, 2, 2, 2, 2]}
           6 +{'seed': 2050, 'n': 2, 'success': True, 'steps': 22, 'time': 0.182, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
           7 +{'seed': 2060, 'n': 1, 'success': True, 'steps': 23, 'time': 0.189, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
           8 +{'seed': 2070, 'n': 2, 'success': True, 'steps': 24, 'time': 0.22, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
           9 +{'seed': 2080, 'n': 3, 'success': True, 'steps': 26, 'time': 0.241, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
          10 +{'seed': 2090, 'n': 2, 'success': True, 'steps': 23, 'time': 0.167, 'bad': [0, 0, 7], 'ops': [2, 2, 9, 2, 2]}
          11 +SUMMARY 100 100 mean 23.54 max_time 0.271
diff --git a/stats_final4.json b/stats_final4.json
new file mode 100644
index 0000000..3fb4d0f
--- /dev/null
+++ b/stats_final4.json
@@ -0,0 +1 @@
           1 +[{"seed": 1200, "n": 4, "success": true, "steps": 26, "time": 0.169, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1201, "n": 4, "success": true, "steps": 26, "time": 0.234, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1202, "n": 4, "success": true, "steps": 29, "time": 0.206, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1203, "n": 4, "success": true, "steps": 27, "time": 0.28, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1204, "n": 4, "success": true, "steps": 26, "time": 0.282, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1205, "n": 4, "success": true, "steps": 32, "time": 0.286, "bad": [0, 1, 0], "ops": [6, 5, 4, 2, 2]}, {"seed": 1206, "n": 4, "success": true, "steps": 25, "time": 0.275, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1207, "n": 4, "success": true, "steps": 22, "time": 0.266, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1208, "n": 4, "success": true, "steps": 30, "time": 0.33, "bad": [0, 1, 1], "ops": [5, 4, 3, 2, 2]}, {"seed": 1209, "n": 4, "success": true, "steps": 24, "time": 0.313, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1210, "n": 4, "success": true, "steps": 24, "time": 0.292, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1211, "n": 4, "success": true, "steps": 24, "time": 0.226, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1212, "n": 4, "success": true, "steps": 68, "time": 0.384, "bad": [0, 0, 44], "ops": [4, 4, 47, 2, 2]}, {"seed": 1213, "n": 4, "success": true, "steps": 27, "time": 0.226, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1214, "n": 4, "success": true, "steps": 26, "time": 0.241, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1215, "n": 4, "success": true, "steps": 24, "time": 0.261, "bad": [0, 1, 0], "ops": [5, 4, 2, 2, 2]}, {"seed": 1216, "n": 4, "success": true, "steps": 24, "time": 0.2, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1217, "n": 4, "success": true, "steps": 28, "time": 0.257, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1218, "n": 4, "success": true, "steps": 26, "time": 0.268, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1219, "n": 4, "success": true, "steps": 29, "time": 0.294, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1220, "n": 4, "success": true, "steps": 23, "time": 0.206, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1221, "n": 4, "success": true, "steps": 30, "time": 0.288, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1222, "n": 4, "success": true, "steps": 29, "time": 0.259, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1223, "n": 4, "success": true, "steps": 29, "time": 0.265, "bad": [0, 0, 0], "ops": [5, 5, 5, 2, 2]}, {"seed": 1224, "n": 4, "success": true, "steps": 24, "time": 0.261, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1225, "n": 4, "success": true, "steps": 24, "time": 0.258, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1226, "n": 4, "success": true, "steps": 29, "time": 0.297, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1227, "n": 4, "success": true, "steps": 24, "time": 0.199, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1228, "n": 4, "success": true, "steps": 25, "time": 0.155, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1229, "n": 4, "success": true, "steps": 30, "time": 0.198, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1230, "n": 4, "success": true, "steps": 29, "time": 0.306, "bad": [0, 1, 0], "ops": [5, 4, 4, 2, 2]}, {"seed": 1231, "n": 4, "success": true, "steps": 29, "time": 0.202, "bad": [0, 0, 0], "ops": [5, 5, 5, 2, 2]}, {"seed": 1232, "n": 4, "success": true, "steps": 26, "time": 0.258, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1233, "n": 4, "success": true, "steps": 27, "time": 0.28, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1234, "n": 4, "success": true, "steps": 27, "time": 0.257, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1235, "n": 4, "success": true, "steps": 25, "time": 0.265, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1236, "n": 4, "success": true, "steps": 26, "time": 0.241, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1237, "n": 4, "success": true, "steps": 28, "time": 0.28, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1238, "n": 4, "success": true, "steps": 31, "time": 0.27, "bad": [0, 0, 0], "ops": [6, 6, 5, 2, 2]}, {"seed": 1239, "n": 4, "success": true, "steps": 25, "time": 0.222, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1240, "n": 4, "success": true, "steps": 26, "time": 0.271, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1241, "n": 4, "success": true, "steps": 28, "time": 0.264, "bad": [0, 0, 2], "ops": [6, 6, 6, 2, 2]}, {"seed": 1242, "n": 4, "success": true, "steps": 25, "time": 0.221, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1243, "n": 4, "success": true, "steps": 27, "time": 0.22, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1244, "n": 4, "success": true, "steps": 25, "time": 0.244, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1245, "n": 4, "success": true, "steps": 25, "time": 0.22, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1246, "n": 4, "success": true, "steps": 27, "time": 0.166, "bad": [0, 1, 0], "ops": [7, 6, 3, 2, 2]}, {"seed": 1247, "n": 4, "success": true, "steps": 25, "time": 0.265, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1248, "n": 4, "success": true, "steps": 27, "time": 0.288, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1249, "n": 4, "success": true, "steps": 30, "time": 0.264, "bad": [0, 0, 5], "ops": [5, 5, 8, 2, 2]}, {"seed": 1250, "n": 4, "success": true, "steps": 24, "time": 0.227, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1251, "n": 4, "success": true, "steps": 31, "time": 0.271, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1252, "n": 4, "success": true, "steps": 26, "time": 0.239, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1253, "n": 4, "success": true, "steps": 24, "time": 0.191, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1254, "n": 4, "success": true, "steps": 25, "time": 0.209, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1255, "n": 4, "success": true, "steps": 28, "time": 0.296, "bad": [0, 0, 1], "ops": [5, 4, 3, 2, 2]}, {"seed": 1256, "n": 4, "success": true, "steps": 31, "time": 0.282, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1257, "n": 4, "success": true, "steps": 28, "time": 0.264, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1258, "n": 4, "success": true, "steps": 24, "time": 0.229, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1259, "n": 4, "success": true, "steps": 29, "time": 0.283, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 1260, "n": 4, "success": true, "steps": 28, "time": 0.211, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1261, "n": 4, "success": true, "steps": 26, "time": 0.282, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1262, "n": 4, "success": true, "steps": 29, "time": 0.292, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 1263, "n": 4, "success": true, "steps": 24, "time": 0.248, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1264, "n": 4, "success": true, "steps": 30, "time": 0.31, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1265, "n": 4, "success": true, "steps": 26, "time": 0.249, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1266, "n": 4, "success": true, "steps": 31, "time": 0.257, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1267, "n": 4, "success": true, "steps": 25, "time": 0.18, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1268, "n": 4, "success": true, "steps": 24, "time": 0.205, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1269, "n": 4, "success": true, "steps": 25, "time": 0.275, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1270, "n": 4, "success": true, "steps": 28, "time": 0.302, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1271, "n": 4, "success": true, "steps": 24, "time": 0.194, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1272, "n": 4, "success": true, "steps": 26, "time": 0.271, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1273, "n": 4, "success": true, "steps": 25, "time": 0.257, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1274, "n": 4, "success": true, "steps": 28, "time": 0.266, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1275, "n": 4, "success": true, "steps": 28, "time": 0.271, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1276, "n": 4, "success": true, "steps": 25, "time": 0.264, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1277, "n": 4, "success": true, "steps": 25, "time": 0.258, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1278, "n": 4, "success": true, "steps": 29, "time": 0.239, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1279, "n": 4, "success": true, "steps": 24, "time": 0.263, "bad": [0, 1, 0], "ops": [5, 4, 5, 2, 2]}, {"seed": 1280, "n": 4, "success": true, "steps": 24, "time": 0.234, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1281, "n": 4, "success": true, "steps": 24, "time": 0.236, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1282, "n": 4, "success": true, "steps": 25, "time": 0.281, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1283, "n": 4, "success": true, "steps": 24, "time": 0.161, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1284, "n": 4, "success": true, "steps": 28, "time": 0.229, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1285, "n": 4, "success": true, "steps": 25, "time": 0.192, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1286, "n": 4, "success": true, "steps": 28, "time": 0.284, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1287, "n": 4, "success": true, "steps": 24, "time": 0.206, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1288, "n": 4, "success": true, "steps": 24, "time": 0.241, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1289, "n": 4, "success": true, "steps": 29, "time": 0.262, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1290, "n": 4, "success": true, "steps": 26, "time": 0.265, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 1291, "n": 4, "success": true, "steps": 26, "time": 0.255, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 1292, "n": 4, "success": true, "steps": 24, "time": 0.253, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1293, "n": 4, "success": true, "steps": 26, "time": 0.18, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1294, "n": 4, "success": true, "steps": 24, "time": 0.24, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1295, "n": 4, "success": true, "steps": 29, "time": 0.26, "bad": [0, 0, 2], "ops": [5, 5, 6, 2, 2]}, {"seed": 1296, "n": 4, "success": true, "steps": 26, "time": 0.25, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1297, "n": 4, "success": true, "steps": 26, "time": 0.266, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1298, "n": 4, "success": true, "steps": 24, "time": 0.227, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1299, "n": 4, "success": true, "steps": 30, "time": 0.251, "bad": [0, 0, 0], "ops": [7, 7, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_final4.txt b/stats_final4.txt
index 443f633..d61343e 100644
--- a/stats_final4.txt
+++ b/stats_final4.txt
@@ -1,3 +1,11 @@
    1      1  {'seed': 1200, 'n': 4, 'success': True, 'steps': 26, 'time': 0.169, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
    2      2  {'seed': 1210, 'n': 4, 'success': True, 'steps': 24, 'time': 0.292, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
    3      3  {'seed': 1220, 'n': 4, 'success': True, 'steps': 23, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [5, 5, 3, 2, 2]}
           4 +{'seed': 1230, 'n': 4, 'success': True, 'steps': 29, 'time': 0.306, 'bad': [0, 1, 0], 'ops': [5, 4, 4, 2, 2]}
           5 +{'seed': 1240, 'n': 4, 'success': True, 'steps': 26, 'time': 0.271, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
           6 +{'seed': 1250, 'n': 4, 'success': True, 'steps': 24, 'time': 0.227, 'bad': [0, 0, 0], 'ops': [4, 4, 4, 2, 2]}
           7 +{'seed': 1260, 'n': 4, 'success': True, 'steps': 28, 'time': 0.211, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
           8 +{'seed': 1270, 'n': 4, 'success': True, 'steps': 28, 'time': 0.302, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
           9 +{'seed': 1280, 'n': 4, 'success': True, 'steps': 24, 'time': 0.234, 'bad': [0, 0, 0], 'ops': [4, 4, 4, 2, 2]}
          10 +{'seed': 1290, 'n': 4, 'success': True, 'steps': 26, 'time': 0.265, 'bad': [0, 1, 0], 'ops': [5, 4, 3, 2, 2]}
          11 +SUMMARY 100 100 mean 26.88 max_time 0.384
diff --git a/stats_final400.txt b/stats_final400.txt
index 4b720b5..0e66040 100644
--- a/stats_final400.txt
+++ b/stats_final400.txt
@@ -2,3 +2,13 @@
    2      2  {'seed': 410, 'n': 2, 'success': True, 'steps': 22, 'time': 0.217, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    3      3  {'seed': 420, 'n': 2, 'success': True, 'steps': 21, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [2, 2, 2, 2, 2]}
    4      4  {'seed': 430, 'n': 1, 'success': True, 'steps': 22, 'time': 0.17, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
           5 +{'seed': 440, 'n': 1, 'success': True, 'steps': 20, 'time': 0.117, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
           6 +{'seed': 450, 'n': 1, 'success': True, 'steps': 25, 'time': 0.175, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
           7 +{'seed': 460, 'n': 1, 'success': True, 'steps': 21, 'time': 0.129, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
           8 +{'seed': 470, 'n': 3, 'success': True, 'steps': 27, 'time': 0.254, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
           9 +{'seed': 480, 'n': 3, 'success': True, 'steps': 21, 'time': 0.228, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
          10 +{'seed': 490, 'n': 2, 'success': True, 'steps': 21, 'time': 0.212, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
          11 +{'seed': 500, 'n': 2, 'success': True, 'steps': 25, 'time': 0.18, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
          12 +{'seed': 510, 'n': 1, 'success': True, 'steps': 24, 'time': 0.145, 'bad': [0, 0, 4], 'ops': [1, 1, 7, 2, 2]}
          13 +{'seed': 520, 'n': 1, 'success': True, 'steps': 18, 'time': 0.147, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
          14 +{'seed': 530, 'n': 1, 'success': True, 'steps': 23, 'time': 0.101, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
diff --git a/stats_octagon.json b/stats_octagon.json
new file mode 100644
index 0000000..e5c4226
--- /dev/null
+++ b/stats_octagon.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "n": 3, "success": true, "steps": 28, "time": 0.138, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 21, "time": 0.162, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 21, "time": 0.179, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 24, "time": 0.207, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 23, "time": 0.193, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 25, "time": 0.222, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 21, "time": 0.159, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 24, "time": 0.195, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 26, "time": 0.189, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 24, "time": 0.159, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 22, "time": 0.171, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 20, "time": 0.103, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 24, "time": 0.186, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 28, "time": 0.203, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 31, "time": 0.119, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 27, "time": 0.135, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 23, "time": 0.181, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 26, "time": 0.182, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 24, "time": 0.19, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 31, "time": 0.22, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 27, "time": 0.222, "bad": [0, 0, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 23, "time": 0.152, "bad": [0, 0, 7], "ops": [1, 1, 8, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 24, "time": 0.205, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 18, "time": 0.122, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 20, "time": 0.163, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 20, "time": 0.171, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 26, "time": 0.219, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 22, "time": 0.153, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 24, "time": 0.151, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 23, "time": 0.191, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 24, "time": 0.163, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 27, "time": 0.214, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 21, "time": 0.192, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 27, "time": 0.19, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 20, "time": 0.126, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 20, "time": 0.101, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.13, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 20, "time": 0.112, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 21, "time": 0.068, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 25, "time": 0.181, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 25, "time": 0.151, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 21, "time": 0.179, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 23, "time": 0.153, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 27, "time": 0.19, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 23, "time": 0.19, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 24, "time": 0.207, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 21, "time": 0.177, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 25, "time": 0.165, "bad": [0, 0, 6], "ops": [1, 1, 7, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 20, "time": 0.123, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 22, "time": 0.175, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 24, "time": 0.206, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 22, "time": 0.123, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 23, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 30, "time": 0.239, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 21, "time": 0.156, "bad": [0, 0, 5], "ops": [1, 1, 7, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 27, "time": 0.219, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 25, "time": 0.204, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 18, "time": 0.141, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 26, "time": 0.191, "bad": [0, 0, 2], "ops": [2, 2, 4, 2, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 23, "time": 0.2, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 22, "time": 0.174, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 21, "time": 0.142, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 25, "time": 0.16, "bad": [0, 0, 5], "ops": [2, 2, 7, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 26, "time": 0.182, "bad": [0, 0, 4], "ops": [2, 2, 7, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 23, "time": 0.17, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 19, "time": 0.116, "bad": [0, 0, 2], "ops": [1, 1, 5, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 23, "time": 0.23, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 24, "time": 0.196, "bad": [0, 2, 0], "ops": [5, 3, 4, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 22, "time": 0.164, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 23, "time": 0.154, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 22, "time": 0.218, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 23, "time": 0.234, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 23, "time": 0.237, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 26, "time": 0.21, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 24, "time": 0.164, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 19, "time": 0.2, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 24, "time": 0.143, "bad": [0, 0, 6], "ops": [2, 2, 9, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 20, "time": 0.101, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 26, "time": 0.187, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 24, "time": 0.17, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 23, "time": 0.214, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 20, "time": 0.101, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 25, "time": 0.19, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 24, "time": 0.24, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 25, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 22, "time": 0.218, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 22, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 23, "time": 0.218, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 22, "time": 0.204, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 89, "n": 3, "success": true, "steps": 31, "time": 0.262, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 90, "n": 2, "success": true, "steps": 29, "time": 0.187, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 24, "time": 0.197, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 24, "time": 0.194, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 27, "time": 0.267, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 22, "time": 0.135, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 22, "time": 0.244, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 25, "time": 0.202, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 27, "time": 0.13, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 24, "time": 0.158, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 27, "time": 0.254, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_octagon.txt b/stats_octagon.txt
index 218b3e7..9ab335d 100644
--- a/stats_octagon.txt
+++ b/stats_octagon.txt
@@ -8,3 +8,4 @@
    8      8  {'seed': 70, 'n': 2, 'success': True, 'steps': 22, 'time': 0.218, 'bad': [0, 1, 0], 'ops': [3, 2, 3, 2, 2]}
    9      9  {'seed': 80, 'n': 3, 'success': True, 'steps': 23, 'time': 0.214, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
   10     10  {'seed': 90, 'n': 2, 'success': True, 'steps': 29, 'time': 0.187, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
          11 +SUMMARY 100 100 mean 23.63 max_time 0.267
```

</details>

<a id="C029"></a>
### C029 · Probe lander-trapped stones across rover headings on seed 5828

Commit `614fb3cb82fe599ac3eebc7e77870c6e0a535cb9`; parents: 26a6f98d7bc8ecf6b12afbccc663d3f851c37a0e. Recorded author date: 2026-09-21T22:29:55+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C029_614fb3c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_trapped_samples.py b/probe_trapped_samples.py
new file mode 100644
index 0000000..5e88e67
--- /dev/null
+++ b/probe_trapped_samples.py
@@ -0,0 +1,25 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import numpy as np
           4 +
           5 +e=make_env();s,i=e.reset(seed=5828);a=GeneratedApproach(e.action_space,e.observation_space,{});a.reset(s,i);r=s.get_object_from_name('rover1')
           6 +def p(): return np.array([s.get(r,'x'),s.get(r,'y')])
           7 +def st(d=(0,0),theta=0,op=0):
           8 + global s
           9 + act=np.zeros(8);act[4:6]=d;act[6:8]=[theta,op];s,*_=e.step(act)
          10 +def go(target):
          11 + for _ in range(50):
          12 +  d=np.clip(np.array(target)-p(),-.1,.1)
          13 +  if np.linalg.norm(d)<1e-5:break
          14 +  old=p();st(d)
          15 +  if np.linalg.norm(old-p())<1e-5:print('stuck',p(),target,flush=True);break
          16 +print('samples',[(str(o),a.xy(s,o).tolist()) for o in a.samples],flush=True)
          17 +go([-1,-1.3]);go([-2.25,-1.3])
          18 +for k in range(18):
          19 + go([-2.0,-1.1]);st(theta=.4);go([-2.25,-1.1])
          20 + for _ in range(80):
          21 +  old=p();st((0,-.005),op=-.833333)
          22 +  if np.linalg.norm(old-p())<1e-5:break
          23 + print('angle',s.get(r,'theta'),'pos',p(),'sampled',[s.get(o,'analyzed_rover1') for o in a.samples],flush=True)
          24 +
          25 +e.close()
diff --git a/stats_final400.json b/stats_final400.json
new file mode 100644
index 0000000..280de6d
--- /dev/null
+++ b/stats_final400.json
@@ -0,0 +1 @@
           1 +[{"seed": 400, "n": 3, "success": true, "steps": 23, "time": 0.191, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 401, "n": 2, "success": true, "steps": 22, "time": 0.21, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 402, "n": 3, "success": true, "steps": 26, "time": 0.183, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 403, "n": 2, "success": true, "steps": 22, "time": 0.219, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 404, "n": 3, "success": true, "steps": 25, "time": 0.247, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 405, "n": 2, "success": true, "steps": 25, "time": 0.223, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 406, "n": 3, "success": true, "steps": 23, "time": 0.212, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 407, "n": 1, "success": true, "steps": 22, "time": 0.185, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 408, "n": 2, "success": true, "steps": 24, "time": 0.161, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 409, "n": 1, "success": true, "steps": 20, "time": 0.137, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 410, "n": 2, "success": true, "steps": 22, "time": 0.217, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 411, "n": 1, "success": true, "steps": 21, "time": 0.173, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 412, "n": 3, "success": true, "steps": 24, "time": 0.238, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 413, "n": 1, "success": true, "steps": 20, "time": 0.166, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 414, "n": 3, "success": true, "steps": 26, "time": 0.267, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 415, "n": 2, "success": true, "steps": 22, "time": 0.205, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 416, "n": 2, "success": true, "steps": 22, "time": 0.151, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 417, "n": 1, "success": true, "steps": 20, "time": 0.131, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 418, "n": 2, "success": true, "steps": 21, "time": 0.196, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 419, "n": 3, "success": true, "steps": 23, "time": 0.22, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 420, "n": 2, "success": true, "steps": 21, "time": 0.178, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 421, "n": 1, "success": true, "steps": 18, "time": 0.142, "bad": [0, 0, 5], "ops": [1, 1, 8, 2, 2]}, {"seed": 422, "n": 1, "success": true, "steps": 20, "time": 0.142, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 423, "n": 2, "success": true, "steps": 20, "time": 0.201, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 424, "n": 1, "success": true, "steps": 18, "time": 0.138, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 425, "n": 1, "success": true, "steps": 22, "time": 0.158, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 426, "n": 1, "success": true, "steps": 20, "time": 0.156, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 427, "n": 3, "success": true, "steps": 26, "time": 0.255, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 428, "n": 1, "success": true, "steps": 22, "time": 0.121, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 429, "n": 1, "success": true, "steps": 24, "time": 0.139, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 430, "n": 1, "success": true, "steps": 22, "time": 0.17, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 431, "n": 3, "success": true, "steps": 26, "time": 0.232, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 432, "n": 3, "success": true, "steps": 24, "time": 0.18, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 433, "n": 1, "success": true, "steps": 20, "time": 0.127, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 434, "n": 3, "success": true, "steps": 23, "time": 0.229, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 435, "n": 2, "success": true, "steps": 23, "time": 0.169, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 436, "n": 3, "success": true, "steps": 24, "time": 0.244, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 437, "n": 2, "success": true, "steps": 26, "time": 0.151, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 438, "n": 3, "success": true, "steps": 30, "time": 0.163, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 439, "n": 2, "success": true, "steps": 23, "time": 0.148, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 440, "n": 1, "success": true, "steps": 20, "time": 0.117, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 441, "n": 2, "success": true, "steps": 22, "time": 0.203, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 442, "n": 2, "success": true, "steps": 22, "time": 0.208, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 443, "n": 1, "success": true, "steps": 22, "time": 0.122, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 444, "n": 3, "success": true, "steps": 27, "time": 0.273, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 445, "n": 1, "success": true, "steps": 18, "time": 0.152, "bad": [0, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 446, "n": 1, "success": true, "steps": 22, "time": 0.141, "bad": [0, 0, 6], "ops": [1, 1, 7, 2, 2]}, {"seed": 447, "n": 2, "success": true, "steps": 22, "time": 0.208, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 448, "n": 3, "success": true, "steps": 24, "time": 0.211, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 449, "n": 3, "success": true, "steps": 22, "time": 0.225, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 450, "n": 1, "success": true, "steps": 25, "time": 0.175, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 451, "n": 3, "success": true, "steps": 30, "time": 0.201, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 452, "n": 2, "success": true, "steps": 22, "time": 0.16, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 453, "n": 3, "success": true, "steps": 23, "time": 0.234, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 454, "n": 2, "success": true, "steps": 26, "time": 0.162, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 455, "n": 3, "success": true, "steps": 26, "time": 0.205, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 456, "n": 2, "success": true, "steps": 21, "time": 0.171, "bad": [0, 0, 4], "ops": [2, 2, 6, 2, 2]}, {"seed": 457, "n": 1, "success": true, "steps": 25, "time": 0.186, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 458, "n": 1, "success": true, "steps": 30, "time": 0.222, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 459, "n": 2, "success": true, "steps": 21, "time": 0.176, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 460, "n": 1, "success": true, "steps": 21, "time": 0.129, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 461, "n": 3, "success": true, "steps": 21, "time": 0.162, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 462, "n": 2, "success": true, "steps": 20, "time": 0.18, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 463, "n": 3, "success": true, "steps": 27, "time": 0.229, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 464, "n": 1, "success": true, "steps": 20, "time": 0.163, "bad": [0, 0, 5], "ops": [1, 1, 8, 2, 2]}, {"seed": 465, "n": 1, "success": true, "steps": 20, "time": 0.119, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 466, "n": 2, "success": true, "steps": 22, "time": 0.191, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 467, "n": 1, "success": true, "steps": 20, "time": 0.122, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 468, "n": 1, "success": true, "steps": 26, "time": 0.187, "bad": [0, 0, 3], "ops": [1, 1, 4, 2, 2]}, {"seed": 469, "n": 1, "success": true, "steps": 20, "time": 0.134, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 470, "n": 3, "success": true, "steps": 27, "time": 0.254, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 471, "n": 1, "success": true, "steps": 20, "time": 0.165, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 472, "n": 1, "success": true, "steps": 18, "time": 0.121, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 473, "n": 1, "success": true, "steps": 23, "time": 0.124, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 474, "n": 1, "success": true, "steps": 20, "time": 0.154, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 475, "n": 2, "success": true, "steps": 22, "time": 0.215, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 476, "n": 3, "success": true, "steps": 23, "time": 0.253, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 477, "n": 2, "success": true, "steps": 21, "time": 0.194, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 478, "n": 1, "success": true, "steps": 22, "time": 0.149, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 479, "n": 3, "success": true, "steps": 23, "time": 0.211, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 480, "n": 3, "success": true, "steps": 21, "time": 0.228, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 481, "n": 2, "success": true, "steps": 23, "time": 0.168, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 482, "n": 1, "success": true, "steps": 22, "time": 0.155, "bad": [0, 0, 3], "ops": [1, 1, 5, 2, 2]}, {"seed": 483, "n": 1, "success": true, "steps": 24, "time": 0.191, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 484, "n": 3, "success": true, "steps": 28, "time": 0.206, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 485, "n": 3, "success": true, "steps": 25, "time": 0.267, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 486, "n": 2, "success": true, "steps": 22, "time": 0.207, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 487, "n": 2, "success": true, "steps": 27, "time": 0.221, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 488, "n": 3, "success": true, "steps": 23, "time": 0.226, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 489, "n": 3, "success": true, "steps": 24, "time": 0.219, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 490, "n": 2, "success": true, "steps": 21, "time": 0.212, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 491, "n": 2, "success": true, "steps": 20, "time": 0.194, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 492, "n": 3, "success": true, "steps": 25, "time": 0.249, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 493, "n": 3, "success": true, "steps": 22, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 494, "n": 2, "success": true, "steps": 24, "time": 0.192, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 495, "n": 1, "success": true, "steps": 25, "time": 0.211, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 496, "n": 1, "success": true, "steps": 22, "time": 0.147, "bad": [0, 0, 2], "ops": [1, 1, 3, 2, 2]}, {"seed": 497, "n": 1, "success": true, "steps": 29, "time": 0.187, "bad": [0, 1, 2], "ops": [2, 1, 5, 2, 2]}, {"seed": 498, "n": 2, "success": true, "steps": 21, "time": 0.206, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 499, "n": 3, "success": true, "steps": 26, "time": 0.223, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 500, "n": 2, "success": true, "steps": 25, "time": 0.18, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 501, "n": 3, "success": true, "steps": 26, "time": 0.227, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 502, "n": 1, "success": true, "steps": 18, "time": 0.152, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 503, "n": 1, "success": true, "steps": 19, "time": 0.175, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 504, "n": 3, "success": true, "steps": 28, "time": 0.183, "bad": [0, 0, 0], "ops": [5, 5, 5, 2, 2]}, {"seed": 505, "n": 3, "success": true, "steps": 26, "time": 0.254, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 506, "n": 2, "success": true, "steps": 24, "time": 0.219, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 507, "n": 3, "success": true, "steps": 24, "time": 0.239, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 508, "n": 2, "success": true, "steps": 23, "time": 0.181, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 509, "n": 3, "success": true, "steps": 21, "time": 0.203, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 510, "n": 1, "success": true, "steps": 24, "time": 0.145, "bad": [0, 0, 4], "ops": [1, 1, 7, 2, 2]}, {"seed": 511, "n": 3, "success": true, "steps": 28, "time": 0.236, "bad": [0, 0, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 512, "n": 2, "success": true, "steps": 25, "time": 0.225, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 513, "n": 3, "success": true, "steps": 26, "time": 0.228, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 514, "n": 3, "success": true, "steps": 26, "time": 0.249, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 515, "n": 1, "success": true, "steps": 20, "time": 0.127, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 516, "n": 1, "success": true, "steps": 21, "time": 0.145, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 517, "n": 2, "success": true, "steps": 24, "time": 0.151, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 518, "n": 1, "success": true, "steps": 27, "time": 0.166, "bad": [0, 1, 0], "ops": [3, 1, 2, 2, 2]}, {"seed": 519, "n": 3, "success": true, "steps": 25, "time": 0.141, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 520, "n": 1, "success": true, "steps": 18, "time": 0.147, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 521, "n": 1, "success": true, "steps": 25, "time": 0.141, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 522, "n": 2, "success": true, "steps": 26, "time": 0.202, "bad": [0, 2, 0], "ops": [4, 2, 3, 2, 2]}, {"seed": 523, "n": 1, "success": true, "steps": 24, "time": 0.182, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 524, "n": 1, "success": true, "steps": 20, "time": 0.139, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 525, "n": 3, "success": true, "steps": 25, "time": 0.216, "bad": [0, 0, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 526, "n": 2, "success": true, "steps": 25, "time": 0.196, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 527, "n": 3, "success": true, "steps": 22, "time": 0.218, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 528, "n": 1, "success": true, "steps": 20, "time": 0.137, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 529, "n": 1, "success": true, "steps": 22, "time": 0.144, "bad": [0, 0, 5], "ops": [1, 1, 6, 2, 2]}, {"seed": 530, "n": 1, "success": true, "steps": 23, "time": 0.101, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 531, "n": 2, "success": true, "steps": 25, "time": 0.137, "bad": [0, 0, 4], "ops": [2, 2, 8, 2, 2]}, {"seed": 532, "n": 3, "success": true, "steps": 26, "time": 0.194, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 533, "n": 2, "success": true, "steps": 27, "time": 0.18, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 534, "n": 3, "success": true, "steps": 24, "time": 0.215, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 535, "n": 1, "success": true, "steps": 20, "time": 0.14, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 536, "n": 3, "success": true, "steps": 26, "time": 0.225, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 537, "n": 1, "success": true, "steps": 22, "time": 0.157, "bad": [0, 0, 5], "ops": [1, 1, 8, 2, 2]}, {"seed": 538, "n": 1, "success": true, "steps": 20, "time": 0.142, "bad": [0, 0, 1], "ops": [1, 1, 3, 2, 2]}, {"seed": 539, "n": 1, "success": true, "steps": 18, "time": 0.117, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 540, "n": 1, "success": true, "steps": 19, "time": 0.127, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 541, "n": 2, "success": true, "steps": 20, "time": 0.124, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 542, "n": 3, "success": true, "steps": 30, "time": 0.242, "bad": [0, 0, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 543, "n": 3, "success": true, "steps": 22, "time": 0.139, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 544, "n": 1, "success": true, "steps": 20, "time": 0.13, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 545, "n": 2, "success": true, "steps": 21, "time": 0.162, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 546, "n": 1, "success": true, "steps": 22, "time": 0.155, "bad": [0, 0, 8], "ops": [1, 1, 10, 2, 2]}, {"seed": 547, "n": 1, "success": true, "steps": 21, "time": 0.13, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 548, "n": 2, "success": true, "steps": 22, "time": 0.174, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 549, "n": 2, "success": true, "steps": 92, "time": 0.496, "bad": [0, 0, 70], "ops": [2, 2, 74, 2, 2]}, {"seed": 550, "n": 3, "success": true, "steps": 29, "time": 0.178, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 551, "n": 1, "success": true, "steps": 28, "time": 0.068, "bad": [0, 0, 8], "ops": [1, 1, 10, 2, 2]}, {"seed": 552, "n": 1, "success": true, "steps": 20, "time": 0.126, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 553, "n": 2, "success": true, "steps": 20, "time": 0.17, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 554, "n": 2, "success": true, "steps": 24, "time": 0.209, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 555, "n": 2, "success": true, "steps": 24, "time": 0.204, "bad": [0, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 556, "n": 2, "success": true, "steps": 22, "time": 0.178, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 557, "n": 2, "success": true, "steps": 22, "time": 0.163, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 558, "n": 2, "success": true, "steps": 20, "time": 0.172, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 559, "n": 1, "success": true, "steps": 22, "time": 0.143, "bad": [0, 0, 0], "ops": [1, 1, 1, 2, 2]}, {"seed": 560, "n": 3, "success": true, "steps": 23, "time": 0.197, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 561, "n": 1, "success": true, "steps": 21, "time": 0.169, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 562, "n": 1, "success": true, "steps": 19, "time": 0.149, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 563, "n": 1, "success": true, "steps": 21, "time": 0.167, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 564, "n": 1, "success": true, "steps": 20, "time": 0.155, "bad": [0, 0, 1], "ops": [1, 1, 3, 2, 2]}, {"seed": 565, "n": 3, "success": true, "steps": 24, "time": 0.232, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 566, "n": 2, "success": true, "steps": 21, "time": 0.183, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 567, "n": 1, "success": true, "steps": 22, "time": 0.127, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 568, "n": 3, "success": true, "steps": 23, "time": 0.208, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 569, "n": 1, "success": true, "steps": 28, "time": 0.165, "bad": [0, 0, 0], "ops": [1, 1, 1, 2, 2]}, {"seed": 570, "n": 1, "success": true, "steps": 22, "time": 0.172, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 571, "n": 3, "success": true, "steps": 25, "time": 0.209, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 572, "n": 2, "success": true, "steps": 18, "time": 0.183, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 573, "n": 3, "success": true, "steps": 24, "time": 0.249, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 574, "n": 1, "success": true, "steps": 29, "time": 0.199, "bad": [0, 0, 0], "ops": [2, 1, 2, 2, 2]}, {"seed": 575, "n": 3, "success": true, "steps": 23, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 576, "n": 1, "success": true, "steps": 29, "time": 0.231, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 577, "n": 2, "success": true, "steps": 24, "time": 0.206, "bad": [0, 1, 0], "ops": [3, 2, 2, 2, 2]}, {"seed": 578, "n": 3, "success": true, "steps": 26, "time": 0.207, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 579, "n": 3, "success": true, "steps": 24, "time": 0.166, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 580, "n": 1, "success": true, "steps": 21, "time": 0.156, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 581, "n": 1, "success": true, "steps": 31, "time": 0.217, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 582, "n": 3, "success": true, "steps": 25, "time": 0.215, "bad": [2, 2, 0], "ops": [5, 3, 3, 2, 2]}, {"seed": 583, "n": 1, "success": true, "steps": 20, "time": 0.155, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 584, "n": 1, "success": true, "steps": 21, "time": 0.149, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 585, "n": 1, "success": true, "steps": 18, "time": 0.139, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 586, "n": 3, "success": true, "steps": 26, "time": 0.22, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 587, "n": 3, "success": true, "steps": 24, "time": 0.176, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 588, "n": 1, "success": true, "steps": 21, "time": 0.099, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 589, "n": 2, "success": true, "steps": 22, "time": 0.13, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 590, "n": 2, "success": true, "steps": 23, "time": 0.195, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 591, "n": 1, "success": true, "steps": 23, "time": 0.179, "bad": [0, 0, 3], "ops": [1, 1, 5, 2, 2]}, {"seed": 592, "n": 2, "success": true, "steps": 18, "time": 0.096, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 593, "n": 3, "success": true, "steps": 24, "time": 0.197, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 594, "n": 2, "success": true, "steps": 27, "time": 0.133, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 595, "n": 3, "success": true, "steps": 26, "time": 0.186, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 596, "n": 3, "success": true, "steps": 23, "time": 0.199, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 597, "n": 3, "success": true, "steps": 23, "time": 0.19, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 598, "n": 1, "success": true, "steps": 20, "time": 0.167, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 599, "n": 3, "success": true, "steps": 25, "time": 0.163, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}]
\ No newline at end of file
diff --git a/stats_final400.txt b/stats_final400.txt
index 0e66040..433c359 100644
--- a/stats_final400.txt
+++ b/stats_final400.txt
@@ -12,3 +12,10 @@
   12     12  {'seed': 510, 'n': 1, 'success': True, 'steps': 24, 'time': 0.145, 'bad': [0, 0, 4], 'ops': [1, 1, 7, 2, 2]}
   13     13  {'seed': 520, 'n': 1, 'success': True, 'steps': 18, 'time': 0.147, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
   14     14  {'seed': 530, 'n': 1, 'success': True, 'steps': 23, 'time': 0.101, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
          15 +{'seed': 540, 'n': 1, 'success': True, 'steps': 19, 'time': 0.127, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
          16 +{'seed': 550, 'n': 3, 'success': True, 'steps': 29, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
          17 +{'seed': 560, 'n': 3, 'success': True, 'steps': 23, 'time': 0.197, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
          18 +{'seed': 570, 'n': 1, 'success': True, 'steps': 22, 'time': 0.172, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
          19 +{'seed': 580, 'n': 1, 'success': True, 'steps': 21, 'time': 0.156, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
          20 +{'seed': 590, 'n': 2, 'success': True, 'steps': 23, 'time': 0.195, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
          21 +SUMMARY 200 200 mean 23.35 max_time 0.496
diff --git a/stats_recovery.txt b/stats_recovery.txt
new file mode 100644
index 0000000..8e38b11
--- /dev/null
+++ b/stats_recovery.txt
@@ -0,0 +1 @@
           1 +{'seed': 600, 'n': 1, 'success': True, 'steps': 27, 'time': 0.102, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
```

</details>

<a id="C030"></a>
### C030 · Remember successful radio locations for later sample transmissions

Commit `460ec4ff028f6d224da92eb198f38a5e427ab0ae`; parents: 614fb3cb82fe599ac3eebc7e77870c6e0a535cb9. Recorded author date: 2026-09-21T22:34:22+02:00.

File roles (automatic): policy, setup/other.

- [E0170](01_timeline.md#E0170): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C030_460ec4f_approach.py) · [Exact all-file diff](evidence/diffs/C030_460ec4f.diff)

[Previous saved controller snapshot](evidence/versions/C028_26a6f98_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3fb7d96..1d07d65 100644
--- a/approach.py
+++ b/approach.py
@@ -45,6 +45,8 @@ class GeneratedApproach:
   45     45          for k, o in enumerate(self.samples):
   46     46              self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
   47     47          self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
          48 +        self.masks[('send',1)] = self.masks[('send',0)].copy()
          49 +        self.good_radio = [[],[]]
   48     50          self.tasks = [None,None]
   49     51          self.paths = [[],[]]
   50     52          self.previous = [None,None]
@@ -162,7 +164,16 @@ class GeneratedApproach:
  162    164              self.choose(s,r,p,other)
  163    165              return
  164    166          if best is None:
  165        -            if self.pending(s,r) and s.get(self.rovers[r],'at_home')>.5:best=('send',0);path,_=self.route(p,self.masks[best],other)
         167 +            if self.pending(s,r) and s.get(self.rovers[r],'at_home')>.5:
         168 +                best=('send',r)
         169 +                mask=self.masks[best]
         170 +                if self.good_radio[r]:
         171 +                    known=np.zeros(len(self.points),dtype=bool)
         172 +                    for point in self.good_radio[r]:known |= np.linalg.norm(self.points-point,axis=1)<.075
         173 +                    pp,cost=self.route(p,known & self.free,other)
         174 +                    if cost<1e5:mask=known & self.free
         175 +                self.masks[best]=mask
         176 +                path,_=self.route(p,mask,other)
  166    177              else:
  167    178                  best=('home',r)
  168    179                  mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
@@ -210,7 +221,9 @@ class GeneratedApproach:
  210    221              task=self.tasks[r]
  211    222              last=self.last_op[r]
  212    223              if last is not None:
  213        -                old_task, old_p, old_op, old_count = last
         224 +                old_task, old_p, old_op, old_count, old_pending = last
         225 +                if old_op==.5 and old_pending and not self.pending(s,r):
         226 +                    if all(np.linalg.norm(p-v)>.1 for v in self.good_radio[r]):self.good_radio[r].append(p.copy())
  214    227                  failed = ((old_task[0]=='image' and old_op == -.5 and s.get(rob,'calibrated')<.5) or
  215    228                            (old_task[0]=='image' and old_op == -1/6 and self.result_count(s,r)<=old_count) or
  216    229                            (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
@@ -271,5 +284,5 @@ class GeneratedApproach:
  271    284                      if not self.have(s,j):op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  272    285              action[r*4:r*4+2]=d;action[r*4+3]=op
  273    286              self.previous[r]=(p.copy(),d.copy())
  274        -            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
         287 +            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r),self.pending(s,r))
  275    288          return action
diff --git a/stats_recovery.json b/stats_recovery.json
new file mode 100644
index 0000000..707e050
--- /dev/null
+++ b/stats_recovery.json
@@ -0,0 +1 @@
           1 +[{"seed": 600, "n": 1, "success": true, "steps": 27, "time": 0.102, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 601, "n": 1, "success": true, "steps": 21, "time": 0.138, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 602, "n": 1, "success": true, "steps": 23, "time": 0.148, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 603, "n": 1, "success": true, "steps": 19, "time": 0.075, "bad": [0, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 604, "n": 1, "success": true, "steps": 20, "time": 0.126, "bad": [0, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 605, "n": 1, "success": true, "steps": 33, "time": 0.209, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 606, "n": 3, "success": true, "steps": 30, "time": 0.25, "bad": [0, 1, 0], "ops": [6, 5, 4, 2, 2]}, {"seed": 607, "n": 3, "success": true, "steps": 23, "time": 0.182, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 608, "n": 2, "success": true, "steps": 23, "time": 0.178, "bad": [0, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 609, "n": 3, "success": true, "steps": 25, "time": 0.149, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 610, "n": 2, "success": true, "steps": 22, "time": 0.161, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 611, "n": 3, "success": true, "steps": 27, "time": 0.225, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 612, "n": 3, "success": true, "steps": 24, "time": 0.121, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 613, "n": 2, "success": true, "steps": 21, "time": 0.165, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 614, "n": 3, "success": true, "steps": 23, "time": 0.205, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 615, "n": 3, "success": true, "steps": 26, "time": 0.214, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 616, "n": 2, "success": true, "steps": 23, "time": 0.176, "bad": [0, 0, 2], "ops": [2, 2, 5, 2, 2]}, {"seed": 617, "n": 2, "success": true, "steps": 21, "time": 0.176, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 618, "n": 1, "success": true, "steps": 22, "time": 0.109, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 619, "n": 2, "success": true, "steps": 20, "time": 0.16, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 620, "n": 3, "success": true, "steps": 24, "time": 0.191, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 621, "n": 1, "success": true, "steps": 23, "time": 0.175, "bad": [0, 2, 0], "ops": [3, 1, 2, 2, 2]}, {"seed": 622, "n": 2, "success": true, "steps": 21, "time": 0.121, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 623, "n": 3, "success": true, "steps": 25, "time": 0.204, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 624, "n": 1, "success": true, "steps": 24, "time": 0.148, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 625, "n": 2, "success": true, "steps": 26, "time": 0.179, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 626, "n": 3, "success": true, "steps": 24, "time": 0.208, "bad": [0, 0, 4], "ops": [3, 3, 7, 2, 2]}, {"seed": 627, "n": 3, "success": true, "steps": 30, "time": 0.257, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 628, "n": 1, "success": true, "steps": 19, "time": 0.093, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 629, "n": 3, "success": true, "steps": 24, "time": 0.2, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 630, "n": 2, "success": true, "steps": 25, "time": 0.153, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 631, "n": 1, "success": true, "steps": 22, "time": 0.135, "bad": [0, 0, 4], "ops": [1, 1, 7, 2, 2]}, {"seed": 632, "n": 2, "success": true, "steps": 21, "time": 0.179, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 633, "n": 2, "success": true, "steps": 23, "time": 0.202, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 634, "n": 2, "success": true, "steps": 21, "time": 0.174, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 635, "n": 3, "success": true, "steps": 26, "time": 0.241, "bad": [0, 0, 2], "ops": [3, 3, 5, 2, 2]}, {"seed": 636, "n": 1, "success": true, "steps": 22, "time": 0.157, "bad": [0, 0, 5], "ops": [1, 1, 6, 2, 2]}, {"seed": 637, "n": 1, "success": true, "steps": 18, "time": 0.124, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 638, "n": 3, "success": true, "steps": 25, "time": 0.207, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 639, "n": 3, "success": true, "steps": 23, "time": 0.183, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 640, "n": 3, "success": true, "steps": 23, "time": 0.212, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 641, "n": 3, "success": true, "steps": 26, "time": 0.226, "bad": [0, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 642, "n": 1, "success": true, "steps": 24, "time": 0.16, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 643, "n": 2, "success": true, "steps": 22, "time": 0.124, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 644, "n": 2, "success": true, "steps": 24, "time": 0.175, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 645, "n": 1, "success": true, "steps": 22, "time": 0.169, "bad": [0, 1, 0], "ops": [2, 1, 2, 2, 2]}, {"seed": 646, "n": 2, "success": true, "steps": 22, "time": 0.18, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 647, "n": 1, "success": true, "steps": 19, "time": 0.138, "bad": [0, 0, 6], "ops": [1, 1, 8, 2, 2]}, {"seed": 648, "n": 1, "success": true, "steps": 18, "time": 0.088, "bad": [0, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 649, "n": 2, "success": true, "steps": 22, "time": 0.136, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 650, "n": 3, "success": true, "steps": 24, "time": 0.191, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 651, "n": 3, "success": true, "steps": 24, "time": 0.225, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 652, "n": 2, "success": true, "steps": 22, "time": 0.149, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 653, "n": 1, "success": true, "steps": 21, "time": 0.156, "bad": [0, 0, 5], "ops": [1, 1, 7, 2, 2]}, {"seed": 654, "n": 1, "success": true, "steps": 20, "time": 0.167, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 655, "n": 1, "success": true, "steps": 23, "time": 0.15, "bad": [0, 2, 0], "ops": [3, 1, 3, 2, 2]}, {"seed": 656, "n": 1, "success": true, "steps": 18, "time": 0.148, "bad": [0, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 657, "n": 1, "success": true, "steps": 25, "time": 0.163, "bad": [0, 0, 6], "ops": [1, 1, 7, 2, 2]}, {"seed": 658, "n": 2, "success": true, "steps": 21, "time": 0.143, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 659, "n": 3, "success": true, "steps": 24, "time": 0.178, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 660, "n": 2, "success": true, "steps": 28, "time": 0.213, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 661, "n": 1, "success": true, "steps": 22, "time": 0.146, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 662, "n": 2, "success": true, "steps": 21, "time": 0.178, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 663, "n": 3, "success": true, "steps": 27, "time": 0.207, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 664, "n": 2, "success": true, "steps": 29, "time": 0.148, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 665, "n": 3, "success": true, "steps": 22, "time": 0.184, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 666, "n": 3, "success": true, "steps": 26, "time": 0.216, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 667, "n": 2, "success": true, "steps": 25, "time": 0.071, "bad": [0, 0, 7], "ops": [2, 2, 10, 2, 2]}, {"seed": 668, "n": 2, "success": true, "steps": 24, "time": 0.146, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 669, "n": 3, "success": true, "steps": 24, "time": 0.203, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 670, "n": 1, "success": true, "steps": 22, "time": 0.154, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 671, "n": 1, "success": true, "steps": 20, "time": 0.165, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 672, "n": 3, "success": true, "steps": 26, "time": 0.223, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 673, "n": 3, "success": true, "steps": 26, "time": 0.218, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 674, "n": 3, "success": true, "steps": 28, "time": 0.217, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 675, "n": 2, "success": true, "steps": 22, "time": 0.19, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 676, "n": 1, "success": true, "steps": 20, "time": 0.132, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 677, "n": 1, "success": true, "steps": 18, "time": 0.129, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 678, "n": 2, "success": true, "steps": 21, "time": 0.174, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 679, "n": 2, "success": true, "steps": 19, "time": 0.138, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 680, "n": 3, "success": true, "steps": 27, "time": 0.151, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 681, "n": 3, "success": true, "steps": 24, "time": 0.224, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 682, "n": 3, "success": true, "steps": 30, "time": 0.26, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 683, "n": 3, "success": true, "steps": 24, "time": 0.122, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 684, "n": 1, "success": true, "steps": 25, "time": 0.161, "bad": [0, 3, 0], "ops": [4, 1, 3, 2, 2]}, {"seed": 685, "n": 3, "success": true, "steps": 21, "time": 0.204, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 686, "n": 3, "success": true, "steps": 24, "time": 0.207, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 687, "n": 3, "success": true, "steps": 31, "time": 0.197, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 688, "n": 1, "success": true, "steps": 23, "time": 0.116, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 689, "n": 1, "success": true, "steps": 24, "time": 0.158, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 690, "n": 3, "success": true, "steps": 24, "time": 0.206, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 691, "n": 1, "success": true, "steps": 25, "time": 0.171, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 692, "n": 2, "success": true, "steps": 21, "time": 0.186, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 693, "n": 3, "success": true, "steps": 23, "time": 0.131, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 694, "n": 3, "success": true, "steps": 27, "time": 0.214, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 695, "n": 1, "success": true, "steps": 25, "time": 0.174, "bad": [0, 0, 0], "ops": [2, 1, 2, 2, 2]}, {"seed": 696, "n": 2, "success": true, "steps": 29, "time": 0.149, "bad": [0, 2, 0], "ops": [4, 2, 3, 2, 2]}, {"seed": 697, "n": 3, "success": true, "steps": 29, "time": 0.235, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 698, "n": 3, "success": true, "steps": 24, "time": 0.182, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 699, "n": 3, "success": true, "steps": 22, "time": 0.182, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}]
\ No newline at end of file
diff --git a/stats_recovery.txt b/stats_recovery.txt
index 8e38b11..b621d07 100644
--- a/stats_recovery.txt
+++ b/stats_recovery.txt
@@ -1 +1,11 @@
    1      1  {'seed': 600, 'n': 1, 'success': True, 'steps': 27, 'time': 0.102, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
           2 +{'seed': 610, 'n': 2, 'success': True, 'steps': 22, 'time': 0.161, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
           3 +{'seed': 620, 'n': 3, 'success': True, 'steps': 24, 'time': 0.191, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
           4 +{'seed': 630, 'n': 2, 'success': True, 'steps': 25, 'time': 0.153, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
           5 +{'seed': 640, 'n': 3, 'success': True, 'steps': 23, 'time': 0.212, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
           6 +{'seed': 650, 'n': 3, 'success': True, 'steps': 24, 'time': 0.191, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           7 +{'seed': 660, 'n': 2, 'success': True, 'steps': 28, 'time': 0.213, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
           8 +{'seed': 670, 'n': 1, 'success': True, 'steps': 22, 'time': 0.154, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
           9 +{'seed': 680, 'n': 3, 'success': True, 'steps': 27, 'time': 0.151, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
          10 +{'seed': 690, 'n': 3, 'success': True, 'steps': 24, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
          11 +SUMMARY 100 100 mean 23.55 max_time 0.26
```

</details>

<a id="C031"></a>
### C031 · Attribute confirmed radio visibility only to uniquely held results

Commit `1829c5e3d78f639633465da743ee0806204eead6`; parents: 460ec4ff028f6d224da92eb198f38a5e427ab0ae. Recorded author date: 2026-09-21T22:35:04+02:00.

File roles (automatic): policy.

- [E0172](01_timeline.md#E0172): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C031_1829c5e_approach.py) · [Exact all-file diff](evidence/diffs/C031_1829c5e.diff)

[Previous saved controller snapshot](evidence/versions/C030_460ec4f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1d07d65..adf6019 100644
--- a/approach.py
+++ b/approach.py
@@ -181,6 +181,14 @@ class GeneratedApproach:
  181    181                  if s.get(self.rovers[r],'at_home')>.5:path=[]
  182    182          self.tasks[r]=best;self.paths[r]=path
  183    183  
         184 +    def radio_evidence(self,s,r):
         185 +        evidence=[]
         186 +        for objects,own,received in ((self.objectives,'have_image_rover','received_image'),(self.samples,'analyzed_rover','received_analysis')):
         187 +            for o in objects:
         188 +                if s.get(o,own+str(r))>.5 and s.get(o,own+str(1-r))<.5 and s.get(o,received)<.5:
         189 +                    evidence.append((o,received))
         190 +        return evidence
         191 +
  184    192      def result_count(self, s, r):
  185    193          return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
  186    194  
@@ -221,8 +229,8 @@ class GeneratedApproach:
  221    229              task=self.tasks[r]
  222    230              last=self.last_op[r]
  223    231              if last is not None:
  224        -                old_task, old_p, old_op, old_count, old_pending = last
  225        -                if old_op==.5 and old_pending and not self.pending(s,r):
         232 +                old_task, old_p, old_op, old_count, old_evidence = last
         233 +                if old_op==.5 and any(s.get(obj,feature)>.5 for obj,feature in old_evidence):
  226    234                      if all(np.linalg.norm(p-v)>.1 for v in self.good_radio[r]):self.good_radio[r].append(p.copy())
  227    235                  failed = ((old_task[0]=='image' and old_op == -.5 and s.get(rob,'calibrated')<.5) or
  228    236                            (old_task[0]=='image' and old_op == -1/6 and self.result_count(s,r)<=old_count) or
@@ -284,5 +292,5 @@ class GeneratedApproach:
  284    292                      if not self.have(s,j):op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  285    293              action[r*4:r*4+2]=d;action[r*4+3]=op
  286    294              self.previous[r]=(p.copy(),d.copy())
  287        -            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r),self.pending(s,r))
         295 +            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r),self.radio_evidence(s,r) if op==.5 else [])
  288    296          return action
```

</details>

<a id="C032"></a>
### C032 · Distinguish opportunistic radio attempts from failures at planned viewpoints

Commit `adfe95630c555598fc1e63f2322eb05264c4aaa1`; parents: 1829c5e3d78f639633465da743ee0806204eead6. Recorded author date: 2026-09-21T22:36:35+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0178](01_timeline.md#E0178): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C032_adfe956_approach.py) · [Exact all-file diff](evidence/diffs/C032_adfe956.diff)

[Previous saved controller snapshot](evidence/versions/C031_1829c5e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index adf6019..d34eb20 100644
--- a/approach.py
+++ b/approach.py
@@ -229,13 +229,13 @@ class GeneratedApproach:
  229    229              task=self.tasks[r]
  230    230              last=self.last_op[r]
  231    231              if last is not None:
  232        -                old_task, old_p, old_op, old_count, old_evidence = last
         232 +                old_task, old_p, old_op, old_count, old_evidence, at_goal = last
  233    233                  if old_op==.5 and any(s.get(obj,feature)>.5 for obj,feature in old_evidence):
  234    234                      if all(np.linalg.norm(p-v)>.1 for v in self.good_radio[r]):self.good_radio[r].append(p.copy())
  235    235                  failed = ((old_task[0]=='image' and old_op == -.5 and s.get(rob,'calibrated')<.5) or
  236    236                            (old_task[0]=='image' and old_op == -1/6 and self.result_count(s,r)<=old_count) or
  237    237                            (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
  238        -                if failed and task==old_task and task[0] in ('image','send'):
         238 +                if failed and at_goal and task==old_task and task[0] in ('image','send'):
  239    239                      self.rejected_views.setdefault(task,[]).append(p.copy())
  240    240                      self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>(.085 if task in self.loose_views else .22)
  241    241                      self.replan(s,r,p,pos[1-r])
@@ -292,5 +292,6 @@ class GeneratedApproach:
  292    292                      if not self.have(s,j):op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  293    293              action[r*4:r*4+2]=d;action[r*4+3]=op
  294    294              self.previous[r]=(p.copy(),d.copy())
  295        -            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r),self.radio_evidence(s,r) if op==.5 else [])
         295 +            at_goal=not path or np.linalg.norm(q-path[-1])<.025
         296 +            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r),self.radio_evidence(s,r) if op==.5 else [],at_goal)
  296    297          return action
diff --git a/probe_dynamic_radio.py b/probe_dynamic_radio.py
new file mode 100644
index 0000000..ac087e9
--- /dev/null
+++ b/probe_dynamic_radio.py
@@ -0,0 +1,21 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import numpy as np
           4 +for seed in [1212,549]:
           5 + e=make_env();s,i=e.reset(seed=seed,options={'object_count':4});a=GeneratedApproach(e.action_space,e.observation_space,{});a.reset(s,i)
           6 + def p(r):return a.xy(s,a.rovers[r])
           7 + def pending():return [(str(o),f) for o,f in a.radio_evidence(s,0)]
           8 + for t in range(180):
           9 +  ev=a.radio_evidence(s,0);act=a.get_action(s);s,*_=e.step(act)
          10 +  if act[3]>.4 and act[3]<.6 and ev:
          11 +   success=any(s.get(o,f)>.5 for o,f in ev)
          12 +   print(seed,t,'send',p(0),p(1),success,'pending',pending(),flush=True)
          13 +   if t>22 and not success and s.get(a.rovers[1],'at_home')>.5:break
          14 + else:e.close();continue
          15 + for dest in [(-1,-1.51),(-1,-1),(-.6,-1),(-1,-1.75)]:
          16 +  for k in range(20):
          17 +   d=np.clip(np.array(dest)-p(1),-.2,.2);act=np.zeros(8);act[3]=.5;act[4:6]=d
          18 +   s,*_=e.step(act)
          19 +   print(seed,'intervene',p(0),p(1),'pending',pending(),flush=True)
          20 +   if np.max(np.abs(d))<.005:break
          21 + e.close()
diff --git a/probe_radio_memory.py b/probe_radio_memory.py
new file mode 100644
index 0000000..bbad7bd
--- /dev/null
+++ b/probe_radio_memory.py
@@ -0,0 +1,10 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import sys
           4 +E=make_env();s,i=E.reset(seed=int(sys.argv[1]),options={'object_count':4} if len(sys.argv)>2 else None);A=GeneratedApproach(E.action_space,E.observation_space,{});A.reset(s,i)
           5 +for t in range(180):
           6 + ac=A.get_action(s)
           7 + if t<30 or t%10==0:print(t,[A.xy(s,r).round(3).tolist() for r in A.rovers],A.tasks,ac[[3,7]].round(2).tolist(),'good',[[p.round(3).tolist() for p in ps] for ps in A.good_radio],flush=True)
           8 + s,_,term,tr,_=E.step(ac)
           9 + if term:break
          10 +E.close()
```

</details>

<a id="C033"></a>
### C033 · Verify radio viewpoints remain valid with second rover parked at home

Commit `637c0df37ef8cff40e5654710f94e8d8bde04a28`; parents: adfe95630c555598fc1e63f2322eb05264c4aaa1. Recorded author date: 2026-09-21T22:37:08+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C033_637c0df.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_dynamic_radio.py b/probe_dynamic_radio.py
index ac087e9..a79110b 100644
--- a/probe_dynamic_radio.py
+++ b/probe_dynamic_radio.py
@@ -12,6 +12,10 @@ for seed in [1212,549]:
   12     12     print(seed,t,'send',p(0),p(1),success,'pending',pending(),flush=True)
   13     13     if t>22 and not success and s.get(a.rovers[1],'at_home')>.5:break
   14     14   else:e.close();continue
          15 + for k in range(15):
          16 +  target=np.array([.9,0]) if seed==1212 else np.array([.7,.1]);d=np.clip(target-p(0),-.2,.2);act=np.zeros(8);act[:2]=d;act[3]=.5;s,*_=e.step(act)
          17 +  print(seed,'known',p(0),p(1),'pending',pending(),flush=True)
          18 +  if np.max(np.abs(d))<.005:break
   15     19   for dest in [(-1,-1.51),(-1,-1),(-.6,-1),(-1,-1.75)]:
   16     20    for k in range(20):
   17     21     d=np.clip(np.array(dest)-p(1),-.2,.2);act=np.zeros(8);act[3]=.5;act[4:6]=d
```

</details>

<a id="C034"></a>
### C034 · Add action-contract and repeated-reset validation

Commit `3bb0c6108ad22c6ad73458be12e600ac565fb824`; parents: 637c0df37ef8cff40e5654710f94e8d8bde04a28. Recorded author date: 2026-09-21T22:38:31+02:00.

File roles (automatic): diagnostic/test.

- [E0187](01_timeline.md#E0187): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C034_3bb0c61.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/stats_final_latest.txt b/stats_final_latest.txt
new file mode 100644
index 0000000..9f32b6c
--- /dev/null
+++ b/stats_final_latest.txt
@@ -0,0 +1,4 @@
           1 +{'seed': 0, 'n': 3, 'success': True, 'steps': 28, 'time': 0.196, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
           2 +{'seed': 10, 'n': 3, 'success': True, 'steps': 22, 'time': 0.194, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           3 +{'seed': 20, 'n': 3, 'success': True, 'steps': 27, 'time': 0.266, 'bad': [0, 0, 0], 'ops': [4, 3, 2, 2, 2]}
           4 +{'seed': 30, 'n': 1, 'success': True, 'steps': 34, 'time': 0.24, 'bad': [0, 0, 4], 'ops': [1, 1, 6, 2, 2]}
diff --git a/stats_final_latest4.txt b/stats_final_latest4.txt
new file mode 100644
index 0000000..ca24e99
--- /dev/null
+++ b/stats_final_latest4.txt
@@ -0,0 +1,4 @@
           1 +{'seed': 1200, 'n': 4, 'success': True, 'steps': 26, 'time': 0.164, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
           2 +{'seed': 1210, 'n': 4, 'success': True, 'steps': 24, 'time': 0.253, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
           3 +{'seed': 1220, 'n': 4, 'success': True, 'steps': 23, 'time': 0.201, 'bad': [0, 0, 0], 'ops': [5, 5, 3, 2, 2]}
           4 +{'seed': 1230, 'n': 4, 'success': True, 'steps': 29, 'time': 0.261, 'bad': [0, 1, 0], 'ops': [5, 4, 4, 2, 2]}
diff --git a/test_reuse.py b/test_reuse.py
new file mode 100644
index 0000000..d0017b9
--- /dev/null
+++ b/test_reuse.py
@@ -0,0 +1,20 @@
           1 +"""Check repeated resets, variable object counts, and the action contract."""
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +env=make_env()
           7 +policy=GeneratedApproach(env.action_space,env.observation_space,{})
           8 +for seed,count in ((0,1),(89,3),(1212,4),(349,2)):
           9 + state,info=env.reset(seed=seed,options={'object_count':count})
          10 + policy.reset(state,info)
          11 + for step in range(200):
          12 +  action=policy.get_action(state)
          13 +  assert action.shape==(8,) and action.dtype==np.float32
          14 +  assert np.isfinite(action).all()
          15 +  assert (action>=env.action_space.low).all() and (action<=env.action_space.high).all()
          16 +  state,_,terminated,truncated,_=env.step(action)
          17 +  if terminated or truncated:break
          18 + assert terminated,(seed,count)
          19 + print('PASS',seed,count,step+1,flush=True)
          20 +env.close()
```

</details>

<a id="C035"></a>
### C035 · Keep final policy, reproducible tests, and validation evidence

Commit `2e041446fb4c20abbfb43617f36c0d85d060e7b8`; parents: 3bb0c6108ad22c6ad73458be12e600ac565fb824. Recorded author date: 2026-09-21T22:39:24+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0191](01_timeline.md#E0191): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C035_2e04144.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach_backup.py b/approach_backup.py
deleted file mode 100644
index e06bda3..0000000
--- a/approach_backup.py
+++ /dev/null
@@ -1,204 +0,0 @@
    1        -import math
    2        -import heapq
    3        -import numpy as np
    4        -
    5        -
    6        -class GeneratedApproach:
    7        -    """Feedback navigation and task allocation for the two rovers."""
    8        -    def __init__(self, action_space, observation_space, primitives):
    9        -        self.space = observation_space
   10        -        self.types = {t.name: t for t in observation_space.types}
   11        -
   12        -    def objects(self, state, kind):
   13        -        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
   14        -
   15        -    def xy(self, state, obj):
   16        -        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
   17        -
   18        -    def reset(self, state, info):
   19        -        self.rovers = self.objects(state, 'rover')
   20        -        self.objectives = self.objects(state, 'objective')
   21        -        self.samples = self.objects(state, 'sample')
   22        -        self.home = [self.xy(state, r) for r in self.rovers]
   23        -        self.lander = self.xy(state, self.objects(state, 'lander')[0])
   24        -        self.rects = []
   25        -        self.occluders = []
   26        -        for o in self.objects(state, 'obstacle'):
   27        -            p = self.xy(state, o)
   28        -            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
   29        -            self.rects.append((p-h, p+h))
   30        -            if state.get(o, 'half_z') > .1:
   31        -                self.occluders.append((p-h, p+h))
   32        -        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
   33        -        self.rects.append((self.lander-np.array([.3,.25]),self.lander+np.array([.3,.25])))
   34        -        axis = np.arange(-2.2, 2.201, .1)
   35        -        self.size = len(axis)
   36        -        xx, yy = np.meshgrid(axis, axis)
   37        -        self.points = np.column_stack([xx.ravel(), yy.ravel()])
   38        -        self.free = self.valid(self.points)
   39        -        self.masks = {}
   40        -        for k, o in enumerate(self.objectives):
   41        -            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
   42        -        for k, o in enumerate(self.samples):
   43        -            self.masks[('sample',k)] = self.free & (np.linalg.norm(self.points-self.xy(state,o),axis=1)<.235)
   44        -        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.95)
   45        -        self.tasks = [None,None]
   46        -        self.paths = [[],[]]
   47        -        self.previous = [None,None]
   48        -        self.fail = [0,0]
   49        -        self.tick = 0
   50        -        self.last_op = [None, None]
   51        -        self.bad_views = {}
   52        -
   53        -    def valid(self, pts):
   54        -        good = np.all(np.abs(pts) <= 2.265, axis=-1)
   55        -        for lo,hi in self.rects:
   56        -            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
   57        -        return good
   58        -
   59        -    def visible(self, pts, target, radius):
   60        -        good = np.linalg.norm(pts-target,axis=1)<radius
   61        -        d = target-pts
   62        -        for lo,hi in self.occluders:
   63        -            inv = np.divide(1.,d,out=np.full_like(d,1e10),where=np.abs(d)>1e-10)
   64        -            a=(lo-pts)*inv; b=(hi-pts)*inv
   65        -            enter=np.max(np.minimum(a,b),axis=1)
   66        -            leave=np.min(np.maximum(a,b),axis=1)
   67        -            good &= ~((leave>=np.maximum(enter,0)) & (enter<=1) & (leave>=0))
   68        -        return good
   69        -
   70        -    def route(self, start, mask, other=None):
   71        -        # A multi-goal Dijkstra on a small occupancy grid.
   72        -        free=self.free.copy()
   73        -        if other is not None:
   74        -            free &= np.linalg.norm(self.points-other,axis=1)>.4
   75        -        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
   76        -        root=next((int(j) for j in starts if free[j]),int(starts[0]))
   77        -        dist={root:0.}; parent={}; queue=[(0.,root)]
   78        -        n=self.size
   79        -        end=None
   80        -        while queue:
   81        -            cost,j=heapq.heappop(queue)
   82        -            if cost!=dist[j]: continue
   83        -            if mask[j]: end=j;break
   84        -            x=j%n;y=j//n
   85        -            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
   86        -                nx=x+dx;ny=y+dy
   87        -                if nx<0 or nx>=n or ny<0 or ny>=n:continue
   88        -                k=ny*n+nx
   89        -                if not free[k]:continue
   90        -                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
   91        -                v=cost+1.
   92        -                if v<dist.get(k,1e9):
   93        -                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
   94        -        if end is None:return [],1e6
   95        -        path=[end]
   96        -        while path[-1]!=root:path.append(parent[path[-1]])
   97        -        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
   98        -
   99        -    def have(self,s,k):
  100        -        o=self.objectives[k]
  101        -        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
  102        -
  103        -    def needed(self,s):
  104        -        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
  105        -
  106        -    def pending(self,s,r):
  107        -        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
  108        -
  109        -    def completed(self,s,r,task):
  110        -        kind,k=task
  111        -        if kind=='image':return self.have(s,k)
  112        -        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
  113        -        if kind=='send':return not self.pending(s,r)
  114        -        return s.get(self.rovers[r],'at_home')>.5
  115        -
  116        -    def choose(self,s,r,p,other):
  117        -        candidates=[]
  118        -        reserved=self.tasks[1-r]
  119        -        need=self.needed(s)
  120        -        for k,o in enumerate(self.objectives):
  121        -            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
  122        -        if s.get(self.rovers[r],'store_full')<.5:
  123        -            for k,o in enumerate(self.samples):
  124        -                soil=int(s.get(o,'is_soil'))
  125        -                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
  126        -        best=None;score=1e9;path=[]
  127        -        for task in candidates:
  128        -            pp,cost=self.route(p,self.masks[task],other)
  129        -            cost+=2 if task[0]=='image' else 0
  130        -            if cost<score and cost<1e5:best=task;score=cost;path=pp
  131        -        if best is None:
  132        -            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
  133        -            else:
  134        -                best=('home',r)
  135        -                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
  136        -                path,_=self.route(p,mask,other)
  137        -                path.append(self.home[r].copy())
  138        -        self.tasks[r]=best;self.paths[r]=path
  139        -
  140        -    def result_count(self, s, r):
  141        -        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
  142        -
  143        -    def get_action(self, state):
  144        -        s=state; self.tick+=1
  145        -        action=np.zeros(8,dtype=np.float32)
  146        -        pos=[self.xy(s,r) for r in self.rovers]
  147        -        for r in range(2):
  148        -            p=pos[r];rob=self.rovers[r]
  149        -            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
  150        -                self.fail[r]+=1
  151        -            else:self.fail[r]=0
  152        -            task=self.tasks[r]
  153        -            last=self.last_op[r]
  154        -            if last is not None:
  155        -                old_task, old_p, old_op, old_count = last
  156        -                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
  157        -                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
  158        -                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
  159        -                if failed and task==old_task and task[0] in ('image','send'):
  160        -                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
  161        -                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
  162        -            if task is None or self.completed(s,r,task):
  163        -                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  164        -            if self.fail[r]>=2:
  165        -                self.paths[r]=[]
  166        -                # Infer blocked configuration and route around it.
  167        -                blocked=p+self.previous[r][1]
  168        -                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
  169        -                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
  170        -                else:mask=self.masks[task]
  171        -                self.paths[r],_=self.route(p,mask,pos[1-r])
  172        -                if task[0]=='home':self.paths[r].append(self.home[r].copy())
  173        -                elif not self.paths[r]:
  174        -                    self.tasks[r]=None
  175        -                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  176        -                self.fail[r]=0
  177        -            path=self.paths[r]
  178        -            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
  179        -            dest=p.copy()
  180        -            selected=-1
  181        -            for pi,point in enumerate(path[:5]):
  182        -                d=point-p
  183        -                if np.max(np.abs(d))>.20001:break
  184        -                probes=p+np.linspace(0,1,5)[:,None]*d
  185        -                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
  186        -                else:break
  187        -            if selected>0:del path[:selected]
  188        -            d=np.clip(dest-p,-.2,.2)
  189        -            q=p+d
  190        -            op=0.
  191        -            kind,k=task
  192        -            if kind=='sample' and np.linalg.norm(q-self.xy(s,self.samples[k]))<.247:op=-5/6
  193        -            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
  194        -                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  195        -                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
  196        -            elif kind=='send' and self.visible(q[None,:],self.lander,3.99)[0]:
  197        -                op=.5
  198        -                if path and np.linalg.norm(q-path[-1])>.06:op=0.
  199        -            if op==0 and s.get(rob,'store_full')>.5:op=5/6
  200        -            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
  201        -            action[r*4:r*4+2]=d;action[r*4+3]=op
  202        -            self.previous[r]=(p.copy(),d.copy())
  203        -            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
  204        -        return action
diff --git a/approach_greedy.py b/approach_greedy.py
deleted file mode 100644
index 922b727..0000000
--- a/approach_greedy.py
+++ /dev/null
@@ -1,211 +0,0 @@
    1        -import math
    2        -import heapq
    3        -import numpy as np
    4        -
    5        -
    6        -class GeneratedApproach:
    7        -    """Feedback navigation and task allocation for the two rovers."""
    8        -    def __init__(self, action_space, observation_space, primitives):
    9        -        self.space = observation_space
   10        -        self.types = {t.name: t for t in observation_space.types}
   11        -
   12        -    def objects(self, state, kind):
   13        -        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
   14        -
   15        -    def xy(self, state, obj):
   16        -        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
   17        -
   18        -    def reset(self, state, info):
   19        -        self.rovers = self.objects(state, 'rover')
   20        -        self.objectives = self.objects(state, 'objective')
   21        -        self.samples = self.objects(state, 'sample')
   22        -        self.home = [self.xy(state, r) for r in self.rovers]
   23        -        self.lander = self.xy(state, self.objects(state, 'lander')[0])
   24        -        self.rects = []
   25        -        self.occluders = []
   26        -        for o in self.objects(state, 'obstacle'):
   27        -            p = self.xy(state, o)
   28        -            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
   29        -            self.rects.append((p-h, p+h))
   30        -            if state.get(o, 'half_z') > .1:
   31        -                self.occluders.append((p-h, p+h))
   32        -        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
   33        -        self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
   34        -        axis = np.arange(-2.2, 2.201, .1)
   35        -        self.size = len(axis)
   36        -        xx, yy = np.meshgrid(axis, axis)
   37        -        self.points = np.column_stack([xx.ravel(), yy.ravel()])
   38        -        self.free = self.valid(self.points)
   39        -        self.masks = {}
   40        -        for k, o in enumerate(self.objectives):
   41        -            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
   42        -        for k, o in enumerate(self.samples):
   43        -            self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
   44        -        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
   45        -        self.tasks = [None,None]
   46        -        self.paths = [[],[]]
   47        -        self.previous = [None,None]
   48        -        self.fail = [0,0]
   49        -        self.tick = 0
   50        -        self.last_op = [None, None]
   51        -        self.bad_views = {}
   52        -
   53        -    def sample_safe(self, state, pts, k):
   54        -        target=self.samples[k]
   55        -        good=np.linalg.norm(pts-self.xy(state,target),axis=1)<.242
   56        -        for obj in self.samples:
   57        -            if state.get(obj,'is_soil')!=state.get(target,'is_soil'):
   58        -                good &= np.linalg.norm(pts-self.xy(state,obj),axis=1)>.255
   59        -        return good
   60        -
   61        -    def valid(self, pts):
   62        -        good = np.all(np.abs(pts) <= 2.265, axis=-1)
   63        -        for lo,hi in self.rects:
   64        -            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
   65        -        return good
   66        -
   67        -    def visible(self, pts, target, radius):
   68        -        good = np.linalg.norm(pts-target,axis=1)<radius
   69        -        d = target-pts
   70        -        length2 = np.maximum(np.sum(d*d,axis=1),1e-12)
   71        -        for lo,hi in self.occluders:
   72        -            center=(lo+hi)*.5
   73        -            t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
   74        -            closest=pts+t[:,None]*d
   75        -            good &= np.linalg.norm(closest-center,axis=1)>.155
   76        -        return good
   77        -
   78        -    def route(self, start, mask, other=None):
   79        -        # A multi-goal Dijkstra on a small occupancy grid.
   80        -        free=self.free.copy()
   81        -        if other is not None:
   82        -            free &= np.linalg.norm(self.points-other,axis=1)>.4
   83        -        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
   84        -        root=next((int(j) for j in starts if free[j]),int(starts[0]))
   85        -        dist={root:0.}; parent={}; queue=[(0.,root)]
   86        -        n=self.size
   87        -        end=None
   88        -        while queue:
   89        -            cost,j=heapq.heappop(queue)
   90        -            if cost!=dist[j]: continue
   91        -            if mask[j]: end=j;break
   92        -            x=j%n;y=j//n
   93        -            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
   94        -                nx=x+dx;ny=y+dy
   95        -                if nx<0 or nx>=n or ny<0 or ny>=n:continue
   96        -                k=ny*n+nx
   97        -                if not free[k]:continue
   98        -                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
   99        -                v=cost+1.+(.001 if dx and dy else 0.)
  100        -                if v<dist.get(k,1e9):
  101        -                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
  102        -        if end is None:return [],1e6
  103        -        path=[end]
  104        -        while path[-1]!=root:path.append(parent[path[-1]])
  105        -        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
  106        -
  107        -    def have(self,s,k):
  108        -        o=self.objectives[k]
  109        -        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
  110        -
  111        -    def needed(self,s):
  112        -        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
  113        -
  114        -    def pending(self,s,r):
  115        -        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
  116        -
  117        -    def completed(self,s,r,task):
  118        -        kind,k=task
  119        -        if kind=='image':return self.have(s,k)
  120        -        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
  121        -        if kind=='send':return not self.pending(s,r)
  122        -        return s.get(self.rovers[r],'at_home')>.5
  123        -
  124        -    def choose(self,s,r,p,other):
  125        -        candidates=[]
  126        -        reserved=self.tasks[1-r]
  127        -        need=self.needed(s)
  128        -        for k,o in enumerate(self.objectives):
  129        -            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
  130        -        if s.get(self.rovers[r],'store_full')<.5:
  131        -            for k,o in enumerate(self.samples):
  132        -                soil=int(s.get(o,'is_soil'))
  133        -                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
  134        -        best=None;score=1e9;path=[]
  135        -        for task in candidates:
  136        -            pp,cost=self.route(p,self.masks[task],other)
  137        -            cost+=2 if task[0]=='image' else 0
  138        -            if cost<score and cost<1e5:best=task;score=cost;path=pp
  139        -        if best is None:
  140        -            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
  141        -            else:
  142        -                best=('home',r)
  143        -                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  144        -                path,_=self.route(p,mask,other)
  145        -                if s.get(self.rovers[r],'at_home')>.5:path=[]
  146        -        self.tasks[r]=best;self.paths[r]=path
  147        -
  148        -    def result_count(self, s, r):
  149        -        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
  150        -
  151        -    def get_action(self, state):
  152        -        s=state; self.tick+=1
  153        -        action=np.zeros(8,dtype=np.float32)
  154        -        pos=[self.xy(s,r) for r in self.rovers]
  155        -        for r in range(2):
  156        -            p=pos[r];rob=self.rovers[r]
  157        -            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
  158        -                self.fail[r]+=1
  159        -            else:self.fail[r]=0
  160        -            task=self.tasks[r]
  161        -            last=self.last_op[r]
  162        -            if last is not None:
  163        -                old_task, old_p, old_op, old_count = last
  164        -                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
  165        -                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
  166        -                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
  167        -                if failed and task==old_task and task[0] in ('image','send'):
  168        -                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
  169        -                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
  170        -            if task is None or self.completed(s,r,task):
  171        -                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  172        -            if self.fail[r]>=2:
  173        -                self.paths[r]=[]
  174        -                # Infer blocked configuration and route around it.
  175        -                blocked=p+self.previous[r][1]
  176        -                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
  177        -                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  178        -                else:mask=self.masks[task]
  179        -                self.paths[r],_=self.route(p,mask,pos[1-r])
  180        -                if task[0]!='home' and not self.paths[r]:
  181        -                    self.tasks[r]=None
  182        -                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  183        -                self.fail[r]=0
  184        -            path=self.paths[r]
  185        -            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
  186        -            dest=p.copy()
  187        -            selected=-1
  188        -            for pi,point in enumerate(path[:5]):
  189        -                d=point-p
  190        -                if np.max(np.abs(d))>.20001:break
  191        -                probes=p+np.linspace(0,1,5)[:,None]*d
  192        -                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
  193        -                else:break
  194        -            if selected>0:del path[:selected]
  195        -            d=np.clip(dest-p,-.2,.2)
  196        -            q=p+d
  197        -            op=0.
  198        -            kind,k=task
  199        -            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
  200        -            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
  201        -                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  202        -                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
  203        -            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
  204        -                op=.5
  205        -                if path and np.linalg.norm(q-path[-1])>.06:op=0.
  206        -            if op==0 and s.get(rob,'store_full')>.5:op=5/6
  207        -            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
  208        -            action[r*4:r*4+2]=d;action[r*4+3]=op
  209        -            self.previous[r]=(p.copy(),d.copy())
  210        -            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
  211        -        return action
diff --git a/approach_no_plan.py b/approach_no_plan.py
deleted file mode 100644
index 14427d7..0000000
--- a/approach_no_plan.py
+++ /dev/null
@@ -1,225 +0,0 @@
    1        -import math
    2        -import heapq
    3        -import numpy as np
    4        -from task_planner import assign_tasks
    5        -
    6        -
    7        -class GeneratedApproach:
    8        -    """Feedback navigation and task allocation for the two rovers."""
    9        -    def __init__(self, action_space, observation_space, primitives):
   10        -        self.space = observation_space
   11        -        self.types = {t.name: t for t in observation_space.types}
   12        -
   13        -    def objects(self, state, kind):
   14        -        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
   15        -
   16        -    def xy(self, state, obj):
   17        -        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
   18        -
   19        -    def reset(self, state, info):
   20        -        self.rovers = self.objects(state, 'rover')
   21        -        self.objectives = self.objects(state, 'objective')
   22        -        self.samples = self.objects(state, 'sample')
   23        -        self.home = [self.xy(state, r) for r in self.rovers]
   24        -        self.lander = self.xy(state, self.objects(state, 'lander')[0])
   25        -        self.rects = []
   26        -        self.occluders = []
   27        -        for o in self.objects(state, 'obstacle'):
   28        -            p = self.xy(state, o)
   29        -            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
   30        -            self.rects.append((p-h, p+h))
   31        -            if state.get(o, 'half_z') > .1:
   32        -                self.occluders.append((p-h, p+h))
   33        -        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
   34        -        self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
   35        -        axis = np.arange(-2.2, 2.201, .1)
   36        -        self.size = len(axis)
   37        -        xx, yy = np.meshgrid(axis, axis)
   38        -        self.points = np.column_stack([xx.ravel(), yy.ravel()])
   39        -        self.free = self.valid(self.points)
   40        -        self.masks = {}
   41        -        for k, o in enumerate(self.objectives):
   42        -            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
   43        -        for k, o in enumerate(self.samples):
   44        -            self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
   45        -        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
   46        -        self.tasks = [None,None]
   47        -        self.paths = [[],[]]
   48        -        self.previous = [None,None]
   49        -        self.fail = [0,0]
   50        -        self.tick = 0
   51        -        self.last_op = [None, None]
   52        -        self.bad_views = {}
   53        -        self.schedule = None
   54        -
   55        -    def sample_safe(self, state, pts, k):
   56        -        target=self.samples[k]
   57        -        good=np.linalg.norm(pts-self.xy(state,target),axis=1)<.242
   58        -        for obj in self.samples:
   59        -            if state.get(obj,'is_soil')!=state.get(target,'is_soil'):
   60        -                good &= np.linalg.norm(pts-self.xy(state,obj),axis=1)>.255
   61        -        return good
   62        -
   63        -    def valid(self, pts):
   64        -        good = np.all(np.abs(pts) <= 2.265, axis=-1)
   65        -        for lo,hi in self.rects:
   66        -            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
   67        -        return good
   68        -
   69        -    def visible(self, pts, target, radius):
   70        -        good = np.linalg.norm(pts-target,axis=1)<radius
   71        -        d = target-pts
   72        -        length2 = np.maximum(np.sum(d*d,axis=1),1e-12)
   73        -        for lo,hi in self.occluders:
   74        -            center=(lo+hi)*.5
   75        -            t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
   76        -            closest=pts+t[:,None]*d
   77        -            clearance=min(.155,float(np.linalg.norm(target-center))*.85)
   78        -            good &= np.linalg.norm(closest-center,axis=1)>clearance
   79        -        return good
   80        -
   81        -    def route(self, start, mask, other=None):
   82        -        # A multi-goal Dijkstra on a small occupancy grid.
   83        -        free=self.free.copy()
   84        -        if other is not None:
   85        -            free &= np.linalg.norm(self.points-other,axis=1)>.4
   86        -        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
   87        -        root=next((int(j) for j in starts if free[j]),int(starts[0]))
   88        -        dist={root:0.}; parent={}; queue=[(0.,root)]
   89        -        n=self.size
   90        -        end=None
   91        -        while queue:
   92        -            cost,j=heapq.heappop(queue)
   93        -            if cost!=dist[j]: continue
   94        -            if mask[j]: end=j;break
   95        -            x=j%n;y=j//n
   96        -            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
   97        -                nx=x+dx;ny=y+dy
   98        -                if nx<0 or nx>=n or ny<0 or ny>=n:continue
   99        -                k=ny*n+nx
  100        -                if not free[k]:continue
  101        -                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
  102        -                v=cost+1.+(.001 if dx and dy else 0.)
  103        -                if v<dist.get(k,1e9):
  104        -                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
  105        -        if end is None:return [],1e6
  106        -        path=[end]
  107        -        while path[-1]!=root:path.append(parent[path[-1]])
  108        -        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
  109        -
  110        -    def have(self,s,k):
  111        -        o=self.objectives[k]
  112        -        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
  113        -
  114        -    def needed(self,s):
  115        -        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
  116        -
  117        -    def pending(self,s,r):
  118        -        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
  119        -
  120        -    def completed(self,s,r,task):
  121        -        kind,k=task
  122        -        if kind=='image':return self.have(s,k)
  123        -        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
  124        -        if kind=='send':return not self.pending(s,r)
  125        -        return s.get(self.rovers[r],'at_home')>.5
  126        -
  127        -    def choose(self,s,r,p,other):
  128        -        candidates=[]
  129        -        reserved=self.tasks[1-r]
  130        -        need=self.needed(s)
  131        -        for k,o in enumerate(self.objectives):
  132        -            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
  133        -        if True:
  134        -            for k,o in enumerate(self.samples):
  135        -                soil=int(s.get(o,'is_soil'))
  136        -                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
  137        -        if self.schedule is not None:
  138        -            schedule=self.schedule[r]
  139        -            while schedule:
  140        -                kind,k=schedule[0]
  141        -                if (kind=='image' and self.have(s,k)) or (kind=='soil' and not need[k]):schedule.pop(0)
  142        -                else:break
  143        -            if schedule:
  144        -                kind,k=schedule[0]
  145        -                planned=[t for t in candidates if t==schedule[0] or (kind=='soil' and t[0]=='sample' and int(s.get(self.samples[t[1]],'is_soil'))==k)]
  146        -                if planned:candidates=planned
  147        -            else:candidates=[]
  148        -        best=None;score=1e9;path=[]
  149        -        for task in candidates:
  150        -            pp,cost=self.route(p,self.masks[task],other)
  151        -            cost+=2 if task[0]=='image' else 0
  152        -            if cost<score and cost<1e5:best=task;score=cost;path=pp
  153        -        if best is None:
  154        -            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
  155        -            else:
  156        -                best=('home',r)
  157        -                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  158        -                path,_=self.route(p,mask,other)
  159        -                if s.get(self.rovers[r],'at_home')>.5:path=[]
  160        -        self.tasks[r]=best;self.paths[r]=path
  161        -
  162        -    def result_count(self, s, r):
  163        -        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
  164        -
  165        -    def get_action(self, state):
  166        -        s=state; self.tick+=1
  167        -        action=np.zeros(8,dtype=np.float32)
  168        -        pos=[self.xy(s,r) for r in self.rovers]
  169        -        for r in range(2):
  170        -            p=pos[r];rob=self.rovers[r]
  171        -            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
  172        -                self.fail[r]+=1
  173        -            else:self.fail[r]=0
  174        -            task=self.tasks[r]
  175        -            last=self.last_op[r]
  176        -            if last is not None:
  177        -                old_task, old_p, old_op, old_count = last
  178        -                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
  179        -                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
  180        -                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
  181        -                if failed and task==old_task and task[0] in ('image','send'):
  182        -                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
  183        -                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
  184        -            if task is None or self.completed(s,r,task):
  185        -                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  186        -            if self.fail[r]>=2:
  187        -                self.paths[r]=[]
  188        -                # Infer blocked configuration and route around it.
  189        -                blocked=p+self.previous[r][1]
  190        -                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
  191        -                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  192        -                else:mask=self.masks[task]
  193        -                self.paths[r],_=self.route(p,mask,pos[1-r])
  194        -                if task[0]!='home' and not self.paths[r]:
  195        -                    self.tasks[r]=None
  196        -                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  197        -                self.fail[r]=0
  198        -            path=self.paths[r]
  199        -            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
  200        -            dest=p.copy()
  201        -            selected=-1
  202        -            for pi,point in enumerate(path[:5]):
  203        -                d=point-p
  204        -                if np.max(np.abs(d))>.20001:break
  205        -                probes=p+np.linspace(0,1,5)[:,None]*d
  206        -                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
  207        -                else:break
  208        -            if selected>0:del path[:selected]
  209        -            d=np.clip(dest-p,-.2,.2)
  210        -            q=p+d
  211        -            op=0.
  212        -            kind,k=task
  213        -            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
  214        -            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
  215        -                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  216        -                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
  217        -            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
  218        -                op=.5
  219        -                if path and np.linalg.norm(q-path[-1])>.06:op=0.
  220        -            if op==0 and s.get(rob,'store_full')>.5:op=5/6
  221        -            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
  222        -            action[r*4:r*4+2]=d;action[r*4+3]=op
  223        -            self.previous[r]=(p.copy(),d.copy())
  224        -            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
  225        -        return action
diff --git a/approach_pipeline.py b/approach_pipeline.py
deleted file mode 100644
index 8fffc9c..0000000
--- a/approach_pipeline.py
+++ /dev/null
@@ -1,238 +0,0 @@
    1        -import math
    2        -import heapq
    3        -import numpy as np
    4        -from task_planner import assign_tasks
    5        -
    6        -
    7        -class GeneratedApproach:
    8        -    """Feedback navigation and task allocation for the two rovers."""
    9        -    def __init__(self, action_space, observation_space, primitives):
   10        -        self.space = observation_space
   11        -        self.types = {t.name: t for t in observation_space.types}
   12        -
   13        -    def objects(self, state, kind):
   14        -        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
   15        -
   16        -    def xy(self, state, obj):
   17        -        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
   18        -
   19        -    def reset(self, state, info):
   20        -        self.rovers = self.objects(state, 'rover')
   21        -        self.objectives = self.objects(state, 'objective')
   22        -        self.samples = self.objects(state, 'sample')
   23        -        self.home = [self.xy(state, r) for r in self.rovers]
   24        -        self.lander = self.xy(state, self.objects(state, 'lander')[0])
   25        -        self.rects = []
   26        -        self.occluders = []
   27        -        for o in self.objects(state, 'obstacle'):
   28        -            p = self.xy(state, o)
   29        -            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
   30        -            self.rects.append((p-h, p+h))
   31        -            if state.get(o, 'half_z') > .1:
   32        -                self.occluders.append((p-h, p+h))
   33        -        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
   34        -        self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
   35        -        axis = np.arange(-2.2, 2.201, .1)
   36        -        self.size = len(axis)
   37        -        xx, yy = np.meshgrid(axis, axis)
   38        -        self.points = np.column_stack([xx.ravel(), yy.ravel()])
   39        -        self.free = self.valid(self.points)
   40        -        self.masks = {}
   41        -        for k, o in enumerate(self.objectives):
   42        -            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
   43        -        for k, o in enumerate(self.samples):
   44        -            self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
   45        -        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
   46        -        self.tasks = [None,None]
   47        -        self.paths = [[],[]]
   48        -        self.previous = [None,None]
   49        -        self.fail = [0,0]
   50        -        self.tick = 0
   51        -        self.last_op = [None, None]
   52        -        self.bad_views = {}
   53        -        self.schedule = assign_tasks(self,state)
   54        -
   55        -    def sample_safe(self, state, pts, k):
   56        -        target=self.samples[k]
   57        -        good=np.linalg.norm(pts-self.xy(state,target),axis=1)<.242
   58        -        for obj in self.samples:
   59        -            if state.get(obj,'is_soil')!=state.get(target,'is_soil'):
   60        -                good &= np.linalg.norm(pts-self.xy(state,obj),axis=1)>.255
   61        -        return good
   62        -
   63        -    def valid(self, pts):
   64        -        good = np.all(np.abs(pts) <= 2.265, axis=-1)
   65        -        for lo,hi in self.rects:
   66        -            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
   67        -        return good
   68        -
   69        -    def visible(self, pts, target, radius):
   70        -        good = np.linalg.norm(pts-target,axis=1)<radius
   71        -        d = target-pts
   72        -        length2 = np.maximum(np.sum(d*d,axis=1),1e-12)
   73        -        for lo,hi in self.occluders:
   74        -            center=(lo+hi)*.5
   75        -            t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
   76        -            closest=pts+t[:,None]*d
   77        -            clearance=min(.155,float(np.linalg.norm(target-center))*.85)
   78        -            good &= np.linalg.norm(closest-center,axis=1)>clearance
   79        -        return good
   80        -
   81        -    def route(self, start, mask, other=None):
   82        -        # A multi-goal Dijkstra on a small occupancy grid.
   83        -        free=self.free.copy()
   84        -        if other is not None:
   85        -            free &= np.linalg.norm(self.points-other,axis=1)>.4
   86        -        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
   87        -        root=next((int(j) for j in starts if free[j]),int(starts[0]))
   88        -        dist={root:0.}; parent={}; queue=[(0.,root)]
   89        -        n=self.size
   90        -        end=None
   91        -        while queue:
   92        -            cost,j=heapq.heappop(queue)
   93        -            if cost!=dist[j]: continue
   94        -            if mask[j]: end=j;break
   95        -            x=j%n;y=j//n
   96        -            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
   97        -                nx=x+dx;ny=y+dy
   98        -                if nx<0 or nx>=n or ny<0 or ny>=n:continue
   99        -                k=ny*n+nx
  100        -                if not free[k]:continue
  101        -                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
  102        -                v=cost+1.+(.001 if dx and dy else 0.)
  103        -                if v<dist.get(k,1e9):
  104        -                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
  105        -        if end is None:return [],1e6
  106        -        path=[end]
  107        -        while path[-1]!=root:path.append(parent[path[-1]])
  108        -        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
  109        -
  110        -    def have(self,s,k):
  111        -        o=self.objectives[k]
  112        -        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
  113        -
  114        -    def needed(self,s):
  115        -        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
  116        -
  117        -    def pending(self,s,r):
  118        -        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
  119        -
  120        -    def completed(self,s,r,task):
  121        -        kind,k=task
  122        -        if kind=='image':return self.have(s,k)
  123        -        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
  124        -        if kind=='send':return not self.pending(s,r)
  125        -        return s.get(self.rovers[r],'at_home')>.5
  126        -
  127        -    def choose(self,s,r,p,other):
  128        -        candidates=[]
  129        -        reserved=self.tasks[1-r]
  130        -        need=self.needed(s)
  131        -        for k,o in enumerate(self.objectives):
  132        -            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
  133        -        if True:
  134        -            for k,o in enumerate(self.samples):
  135        -                soil=int(s.get(o,'is_soil'))
  136        -                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
  137        -        if self.schedule is not None:
  138        -            schedule=self.schedule[r]
  139        -            while schedule:
  140        -                kind,k=schedule[0]
  141        -                if (kind=='image' and self.have(s,k)) or (kind=='soil' and not need[k]):schedule.pop(0)
  142        -                else:break
  143        -            if schedule:
  144        -                kind,k=schedule[0]
  145        -                planned=[t for t in candidates if t==schedule[0] or (kind=='soil' and t[0]=='sample' and int(s.get(self.samples[t[1]],'is_soil'))==k)]
  146        -                if planned:candidates=planned
  147        -            else:candidates=[]
  148        -        best=None;score=1e9;path=[]
  149        -        for task in candidates:
  150        -            pp,cost=self.route(p,self.masks[task],other)
  151        -            cost+=2 if task[0]=='image' else 0
  152        -            if cost<score and cost<1e5:best=task;score=cost;path=pp
  153        -        if best is None and candidates and self.schedule is not None:
  154        -            self.schedule=None
  155        -            self.choose(s,r,p,other)
  156        -            return
  157        -        if best is None:
  158        -            if self.pending(s,r) and s.get(self.rovers[r],'at_home')>.5:best=('send',0);path,_=self.route(p,self.masks[best],other)
  159        -            else:
  160        -                best=('home',r)
  161        -                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  162        -                path,_=self.route(p,mask,other)
  163        -                if s.get(self.rovers[r],'at_home')>.5:path=[]
  164        -        self.tasks[r]=best;self.paths[r]=path
  165        -
  166        -    def result_count(self, s, r):
  167        -        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
  168        -
  169        -    def get_action(self, state):
  170        -        s=state; self.tick+=1
  171        -        action=np.zeros(8,dtype=np.float32)
  172        -        pos=[self.xy(s,r) for r in self.rovers]
  173        -        for r in range(2):
  174        -            p=pos[r];rob=self.rovers[r]
  175        -            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
  176        -                self.fail[r]+=1
  177        -            else:self.fail[r]=0
  178        -            task=self.tasks[r]
  179        -            last=self.last_op[r]
  180        -            if last is not None:
  181        -                old_task, old_p, old_op, old_count = last
  182        -                failed = ((old_task[0]=='image' and old_op == -.5 and s.get(rob,'calibrated')<.5) or
  183        -                          (old_task[0]=='image' and old_op == -1/6 and self.result_count(s,r)<=old_count) or
  184        -                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
  185        -                if failed and task==old_task and task[0] in ('image','send'):
  186        -                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
  187        -                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
  188        -            if task is None or self.completed(s,r,task):
  189        -                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  190        -            if self.fail[r]>=2:
  191        -                self.paths[r]=[]
  192        -                # Infer blocked configuration and route around it.
  193        -                blocked=p+self.previous[r][1]
  194        -                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
  195        -                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  196        -                else:mask=self.masks[task]
  197        -                self.paths[r],_=self.route(p,mask,pos[1-r])
  198        -                if task[0]!='home' and not self.paths[r]:
  199        -                    self.tasks[r]=None
  200        -                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  201        -                self.fail[r]=0
  202        -            path=self.paths[r]
  203        -            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
  204        -            dest=p.copy()
  205        -            selected=-1
  206        -            for pi,point in enumerate(path[:5]):
  207        -                d=point-p
  208        -                if np.max(np.abs(d))>.20001:break
  209        -                probes=p+np.linspace(0,1,5)[:,None]*d
  210        -                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
  211        -                else:break
  212        -            if selected>0:del path[:selected]
  213        -            d=np.clip(dest-p,-.2,.2)
  214        -            q=p+d
  215        -            op=0.
  216        -            kind,k=task
  217        -            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
  218        -            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
  219        -                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  220        -                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
  221        -            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
  222        -                op=.5
  223        -                if path and np.linalg.norm(q-path[-1])>.06:op=0.
  224        -            if op==0 and s.get(rob,'store_full')>.5:op=5/6
  225        -            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
  226        -            # Use otherwise idle travel steps for camera work.
  227        -            if op in (0.,.5) and np.linalg.norm(d)>.01:
  228        -                visible=[]
  229        -                for j,o in enumerate(self.objectives):
  230        -                    if s.get(o,'have_image_rover%d'%r)<.5 and self.visible(q[None,:],self.xy(s,o),1.97)[0]:
  231        -                        visible.append((float(np.linalg.norm(q-self.xy(s,o))),j))
  232        -                if visible:
  233        -                    _,j=min(visible)
  234        -                    if not self.have(s,j):op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  235        -            action[r*4:r*4+2]=d;action[r*4+3]=op
  236        -            self.previous[r]=(p.copy(),d.copy())
  237        -            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
  238        -        return action
diff --git a/approach_planned_before_pipeline.py b/approach_planned_before_pipeline.py
deleted file mode 100644
index 8bdab39..0000000
--- a/approach_planned_before_pipeline.py
+++ /dev/null
@@ -1,229 +0,0 @@
    1        -import math
    2        -import heapq
    3        -import numpy as np
    4        -from task_planner import assign_tasks
    5        -
    6        -
    7        -class GeneratedApproach:
    8        -    """Feedback navigation and task allocation for the two rovers."""
    9        -    def __init__(self, action_space, observation_space, primitives):
   10        -        self.space = observation_space
   11        -        self.types = {t.name: t for t in observation_space.types}
   12        -
   13        -    def objects(self, state, kind):
   14        -        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
   15        -
   16        -    def xy(self, state, obj):
   17        -        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
   18        -
   19        -    def reset(self, state, info):
   20        -        self.rovers = self.objects(state, 'rover')
   21        -        self.objectives = self.objects(state, 'objective')
   22        -        self.samples = self.objects(state, 'sample')
   23        -        self.home = [self.xy(state, r) for r in self.rovers]
   24        -        self.lander = self.xy(state, self.objects(state, 'lander')[0])
   25        -        self.rects = []
   26        -        self.occluders = []
   27        -        for o in self.objects(state, 'obstacle'):
   28        -            p = self.xy(state, o)
   29        -            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
   30        -            self.rects.append((p-h, p+h))
   31        -            if state.get(o, 'half_z') > .1:
   32        -                self.occluders.append((p-h, p+h))
   33        -        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
   34        -        self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
   35        -        axis = np.arange(-2.2, 2.201, .1)
   36        -        self.size = len(axis)
   37        -        xx, yy = np.meshgrid(axis, axis)
   38        -        self.points = np.column_stack([xx.ravel(), yy.ravel()])
   39        -        self.free = self.valid(self.points)
   40        -        self.masks = {}
   41        -        for k, o in enumerate(self.objectives):
   42        -            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
   43        -        for k, o in enumerate(self.samples):
   44        -            self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
   45        -        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
   46        -        self.tasks = [None,None]
   47        -        self.paths = [[],[]]
   48        -        self.previous = [None,None]
   49        -        self.fail = [0,0]
   50        -        self.tick = 0
   51        -        self.last_op = [None, None]
   52        -        self.bad_views = {}
   53        -        self.schedule = assign_tasks(self,state)
   54        -
   55        -    def sample_safe(self, state, pts, k):
   56        -        target=self.samples[k]
   57        -        good=np.linalg.norm(pts-self.xy(state,target),axis=1)<.242
   58        -        for obj in self.samples:
   59        -            if state.get(obj,'is_soil')!=state.get(target,'is_soil'):
   60        -                good &= np.linalg.norm(pts-self.xy(state,obj),axis=1)>.255
   61        -        return good
   62        -
   63        -    def valid(self, pts):
   64        -        good = np.all(np.abs(pts) <= 2.265, axis=-1)
   65        -        for lo,hi in self.rects:
   66        -            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
   67        -        return good
   68        -
   69        -    def visible(self, pts, target, radius):
   70        -        good = np.linalg.norm(pts-target,axis=1)<radius
   71        -        d = target-pts
   72        -        length2 = np.maximum(np.sum(d*d,axis=1),1e-12)
   73        -        for lo,hi in self.occluders:
   74        -            center=(lo+hi)*.5
   75        -            t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
   76        -            closest=pts+t[:,None]*d
   77        -            clearance=min(.155,float(np.linalg.norm(target-center))*.85)
   78        -            good &= np.linalg.norm(closest-center,axis=1)>clearance
   79        -        return good
   80        -
   81        -    def route(self, start, mask, other=None):
   82        -        # A multi-goal Dijkstra on a small occupancy grid.
   83        -        free=self.free.copy()
   84        -        if other is not None:
   85        -            free &= np.linalg.norm(self.points-other,axis=1)>.4
   86        -        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
   87        -        root=next((int(j) for j in starts if free[j]),int(starts[0]))
   88        -        dist={root:0.}; parent={}; queue=[(0.,root)]
   89        -        n=self.size
   90        -        end=None
   91        -        while queue:
   92        -            cost,j=heapq.heappop(queue)
   93        -            if cost!=dist[j]: continue
   94        -            if mask[j]: end=j;break
   95        -            x=j%n;y=j//n
   96        -            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
   97        -                nx=x+dx;ny=y+dy
   98        -                if nx<0 or nx>=n or ny<0 or ny>=n:continue
   99        -                k=ny*n+nx
  100        -                if not free[k]:continue
  101        -                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
  102        -                v=cost+1.+(.001 if dx and dy else 0.)
  103        -                if v<dist.get(k,1e9):
  104        -                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
  105        -        if end is None:return [],1e6
  106        -        path=[end]
  107        -        while path[-1]!=root:path.append(parent[path[-1]])
  108        -        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
  109        -
  110        -    def have(self,s,k):
  111        -        o=self.objectives[k]
  112        -        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
  113        -
  114        -    def needed(self,s):
  115        -        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
  116        -
  117        -    def pending(self,s,r):
  118        -        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
  119        -
  120        -    def completed(self,s,r,task):
  121        -        kind,k=task
  122        -        if kind=='image':return self.have(s,k)
  123        -        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
  124        -        if kind=='send':return not self.pending(s,r)
  125        -        return s.get(self.rovers[r],'at_home')>.5
  126        -
  127        -    def choose(self,s,r,p,other):
  128        -        candidates=[]
  129        -        reserved=self.tasks[1-r]
  130        -        need=self.needed(s)
  131        -        for k,o in enumerate(self.objectives):
  132        -            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
  133        -        if True:
  134        -            for k,o in enumerate(self.samples):
  135        -                soil=int(s.get(o,'is_soil'))
  136        -                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
  137        -        if self.schedule is not None:
  138        -            schedule=self.schedule[r]
  139        -            while schedule:
  140        -                kind,k=schedule[0]
  141        -                if (kind=='image' and self.have(s,k)) or (kind=='soil' and not need[k]):schedule.pop(0)
  142        -                else:break
  143        -            if schedule:
  144        -                kind,k=schedule[0]
  145        -                planned=[t for t in candidates if t==schedule[0] or (kind=='soil' and t[0]=='sample' and int(s.get(self.samples[t[1]],'is_soil'))==k)]
  146        -                if planned:candidates=planned
  147        -            else:candidates=[]
  148        -        best=None;score=1e9;path=[]
  149        -        for task in candidates:
  150        -            pp,cost=self.route(p,self.masks[task],other)
  151        -            cost+=2 if task[0]=='image' else 0
  152        -            if cost<score and cost<1e5:best=task;score=cost;path=pp
  153        -        if best is None and candidates and self.schedule is not None:
  154        -            self.schedule=None
  155        -            self.choose(s,r,p,other)
  156        -            return
  157        -        if best is None:
  158        -            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
  159        -            else:
  160        -                best=('home',r)
  161        -                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  162        -                path,_=self.route(p,mask,other)
  163        -                if s.get(self.rovers[r],'at_home')>.5:path=[]
  164        -        self.tasks[r]=best;self.paths[r]=path
  165        -
  166        -    def result_count(self, s, r):
  167        -        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)
  168        -
  169        -    def get_action(self, state):
  170        -        s=state; self.tick+=1
  171        -        action=np.zeros(8,dtype=np.float32)
  172        -        pos=[self.xy(s,r) for r in self.rovers]
  173        -        for r in range(2):
  174        -            p=pos[r];rob=self.rovers[r]
  175        -            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
  176        -                self.fail[r]+=1
  177        -            else:self.fail[r]=0
  178        -            task=self.tasks[r]
  179        -            last=self.last_op[r]
  180        -            if last is not None:
  181        -                old_task, old_p, old_op, old_count = last
  182        -                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
  183        -                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
  184        -                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
  185        -                if failed and task==old_task and task[0] in ('image','send'):
  186        -                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
  187        -                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
  188        -            if task is None or self.completed(s,r,task):
  189        -                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  190        -            if self.fail[r]>=2:
  191        -                self.paths[r]=[]
  192        -                # Infer blocked configuration and route around it.
  193        -                blocked=p+self.previous[r][1]
  194        -                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
  195        -                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
  196        -                else:mask=self.masks[task]
  197        -                self.paths[r],_=self.route(p,mask,pos[1-r])
  198        -                if task[0]!='home' and not self.paths[r]:
  199        -                    self.tasks[r]=None
  200        -                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  201        -                self.fail[r]=0
  202        -            path=self.paths[r]
  203        -            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
  204        -            dest=p.copy()
  205        -            selected=-1
  206        -            for pi,point in enumerate(path[:5]):
  207        -                d=point-p
  208        -                if np.max(np.abs(d))>.20001:break
  209        -                probes=p+np.linspace(0,1,5)[:,None]*d
  210        -                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
  211        -                else:break
  212        -            if selected>0:del path[:selected]
  213        -            d=np.clip(dest-p,-.2,.2)
  214        -            q=p+d
  215        -            op=0.
  216        -            kind,k=task
  217        -            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
  218        -            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
  219        -                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  220        -                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
  221        -            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
  222        -                op=.5
  223        -                if path and np.linalg.norm(q-path[-1])>.06:op=0.
  224        -            if op==0 and s.get(rob,'store_full')>.5:op=5/6
  225        -            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
  226        -            action[r*4:r*4+2]=d;action[r*4+3]=op
  227        -            self.previous[r]=(p.copy(),d.copy())
  228        -            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
  229        -        return action
diff --git a/debug_policy.py b/debug_policy.py
deleted file mode 100644
index c67a0cb..0000000
--- a/debug_policy.py
+++ /dev/null
@@ -1,11 +0,0 @@
    1        -from env_client import make_env
    2        -from approach import GeneratedApproach
    3        -import sys
    4        -E=make_env();s,info=E.reset(seed=int(sys.argv[1]));A=GeneratedApproach(E.action_space,E.observation_space,{})
    5        -A.reset(s,info)
    6        -for t in range(80):
    7        - ac=A.get_action(s)
    8        - if t<15 or t%5==0:print(t, [A.xy(s,r).round(3).tolist() for r in A.rovers], A.tasks,ac.round(3).tolist(),[[(p.round(3)).tolist() for p in path[:3]] for path in A.paths],flush=True)
    9        - s,r,d,tr,i=E.step(ac)
   10        - if d:break
   11        -E.close()
diff --git a/inspect_collision.py b/inspect_collision.py
deleted file mode 100644
index 22be539..0000000
--- a/inspect_collision.py
+++ /dev/null
@@ -1,14 +0,0 @@
    1        -import sys,numpy as np
    2        -from env_client import make_env
    3        -from approach import GeneratedApproach
    4        -E=make_env();s,i=E.reset(seed=int(sys.argv[1]));A=GeneratedApproach(E.action_space,E.observation_space,{});A.reset(s,i)
    5        -for t in range(100):
    6        - a=A.get_action(s);ss,_,done,tr,_=E.step(a)
    7        - for r,rob in enumerate(A.rovers):
    8        -  p=A.xy(s,rob);q=p+a[r*4:r*4+2]
    9        -  if np.linalg.norm(q-p)>.01 and np.linalg.norm(A.xy(ss,rob)-p)<1e-5:
   10        -   print('COLLISION',t,r,'from',p,'to',q,'task',A.tasks[r])
   11        -   print('nearest',sorted([(float(np.linalg.norm(np.maximum(np.maximum(lo-q,q-hi),0))),lo.tolist(),hi.tolist()) for lo,hi in A.rects])[:3])
   12        - s=ss
   13        - if done:break
   14        -E.close()
diff --git a/inspect_env.py b/inspect_env.py
deleted file mode 100644
index 12ec7cb..0000000
--- a/inspect_env.py
+++ /dev/null
@@ -1,12 +0,0 @@
    1        -from env_client import make_env
    2        -import numpy as np
    3        -E=make_env(); s,i=E.reset(seed=0)
    4        -print('INFO',i,'max',E.max_steps)
    5        -for name in s.get_object_names():
    6        - o=s.get_object_from_name(name)
    7        - print(name,{f:s.get(o,f) for f in E.observation_space.type_features[o.type]})
    8        -for op in [-.5,-1/6,.5]:
    9        - a=np.zeros(8);a[3]=a[7]=op
   10        - s,r,t,tr,i=E.step(a)
   11        - print('OP',op,[(n, {f:s.get(s.get_object_from_name(n),f) for f in E.observation_space.type_features[s.get_object_from_name(n).type]}) for n in s.get_object_names() if n.startswith(('rover','objective'))])
   12        -E.close()
diff --git a/inspect_seed.py b/inspect_seed.py
deleted file mode 100644
index 68d4e30..0000000
--- a/inspect_seed.py
+++ /dev/null
@@ -1,10 +0,0 @@
    1        -import sys,numpy as np
    2        -from env_client import make_env
    3        -from approach import GeneratedApproach
    4        -E=make_env();s,i=E.reset(seed=int(sys.argv[1]));A=GeneratedApproach(E.action_space,E.observation_space,{});A.reset(s,i)
    5        -print('schedule',A.schedule)
    6        -for o in A.objectives:
    7        - p=A.xy(s,o);print(o.name,p,'mask',np.sum(A.masks[('image',A.objectives.index(o))]))
    8        - for ob in A.objects(s,'obstacle'):
    9        -  if np.linalg.norm(p-A.xy(s,ob))<.5:print('near',ob.name,A.xy(s,ob),s.get(ob,'half_x'),np.linalg.norm(p-A.xy(s,ob)))
   10        -E.close()
diff --git a/probe_crosslos.py b/probe_crosslos.py
deleted file mode 100644
index b227ce0..0000000
--- a/probe_crosslos.py
+++ /dev/null
@@ -1,18 +0,0 @@
    1        -import numpy as np
    2        -from env_client import make_env
    3        -e=make_env();s,_=e.reset(seed=0);rs=[s.get_object_from_name('rover'+str(i)) for i in range(2)]
    4        -def xy(i):return np.array([s.get(rs[i],f) for f in ('x','y')])
    5        -def st(i,op=0,d=(0,0)):
    6        - global s
    7        - a=np.zeros(8,np.float32);a[4*i:4*i+2]=d;a[4*i+3]=op;s,*_=e.step(a)
    8        -def go(i,p):
    9        - for t in range(40):
   10        -  d=np.clip(np.array(p)-xy(i),-.2,.2)
   11        -  if np.max(abs(d))<1e-5:return
   12        -  old=xy(i);st(i,d=d)
   13        -  if np.linalg.norm(xy(i)-old)<1e-5:print('blocked',old,p);return
   14        -for p in [(-1.5,-.3),(-1.8,.8),(-1.1,1.2),(-.4,1.2)]:go(1,p)
   15        -for j in range(5):
   16        - st(1,-.5);st(1,-1/6)
   17        - print('cross photos',xy(1),[(o.name,s.get(o,'have_image_rover1')) for o in s.get_objects(e.observation_space.get_type('objective'))])
   18        -e.close()
diff --git a/probe_dynamic_radio.py b/probe_dynamic_radio.py
deleted file mode 100644
index a79110b..0000000
--- a/probe_dynamic_radio.py
+++ /dev/null
@@ -1,25 +0,0 @@
    1        -from env_client import make_env
    2        -from approach import GeneratedApproach
    3        -import numpy as np
    4        -for seed in [1212,549]:
    5        - e=make_env();s,i=e.reset(seed=seed,options={'object_count':4});a=GeneratedApproach(e.action_space,e.observation_space,{});a.reset(s,i)
    6        - def p(r):return a.xy(s,a.rovers[r])
    7        - def pending():return [(str(o),f) for o,f in a.radio_evidence(s,0)]
    8        - for t in range(180):
    9        -  ev=a.radio_evidence(s,0);act=a.get_action(s);s,*_=e.step(act)
   10        -  if act[3]>.4 and act[3]<.6 and ev:
   11        -   success=any(s.get(o,f)>.5 for o,f in ev)
   12        -   print(seed,t,'send',p(0),p(1),success,'pending',pending(),flush=True)
   13        -   if t>22 and not success and s.get(a.rovers[1],'at_home')>.5:break
   14        - else:e.close();continue
   15        - for k in range(15):
   16        -  target=np.array([.9,0]) if seed==1212 else np.array([.7,.1]);d=np.clip(target-p(0),-.2,.2);act=np.zeros(8);act[:2]=d;act[3]=.5;s,*_=e.step(act)
   17        -  print(seed,'known',p(0),p(1),'pending',pending(),flush=True)
   18        -  if np.max(np.abs(d))<.005:break
   19        - for dest in [(-1,-1.51),(-1,-1),(-.6,-1),(-1,-1.75)]:
   20        -  for k in range(20):
   21        -   d=np.clip(np.array(dest)-p(1),-.2,.2);act=np.zeros(8);act[3]=.5;act[4:6]=d
   22        -   s,*_=e.step(act)
   23        -   print(seed,'intervene',p(0),p(1),'pending',pending(),flush=True)
   24        -   if np.max(np.abs(d))<.005:break
   25        - e.close()
diff --git a/probe_lander.py b/probe_lander.py
deleted file mode 100644
index b5251fd..0000000
--- a/probe_lander.py
+++ /dev/null
@@ -1,31 +0,0 @@
    1        -from env_client import make_env
    2        -import numpy as np
    3        -
    4        -def p(s):
    5        - o=s.get_object_from_name('rover1');return np.array([s.get(o,'x'),s.get(o,'y')])
    6        -def st(e,s,dx=0,dy=0):
    7        - a=np.zeros(8);a[4:6]=[dx,dy];t,*_=e.step(a);return t
    8        -
    9        -def goto(e,s,target):
   10        - for _ in range(50):
   11        -  d=np.clip(np.array(target)-p(s),-.1,.1)
   12        -  if np.linalg.norm(d)<1e-5:break
   13        -  old=p(s);s=st(e,s,*d)
   14        -  if np.allclose(old,p(s)):break
   15        - return s
   16        -for x in [-2.25,-2.2,-2.1,-2,-1.9,-1.8,-1.7,-1.6,-1.5,-1.4,-1.3,-1.2,-1.1]:
   17        - e=make_env();s,_=e.reset(seed=29)
   18        - s=goto(e,s,[-1,-1]);s=goto(e,s,[x,-1])
   19        - for _ in range(160):
   20        -  old=p(s);s=st(e,s,dy=-.01)
   21        -  if np.allclose(old,p(s)):break
   22        - print('vertical',x,p(s))
   23        - e.close()
   24        -for y in [-2.25,-2.2,-2.1,-2,-1.9,-1.8,-1.7,-1.6,-1.5,-1.4,-1.3]:
   25        - e=make_env();s,_=e.reset(seed=29)
   26        - s=goto(e,s,[-1,y])
   27        - for _ in range(140):
   28        -  old=p(s);s=st(e,s,dx=-.01)
   29        -  if np.allclose(old,p(s)):break
   30        - print('horizontal',y,p(s))
   31        - e.close()
diff --git a/probe_lander_exact.py b/probe_lander_exact.py
deleted file mode 100644
index 0404383..0000000
--- a/probe_lander_exact.py
+++ /dev/null
@@ -1,19 +0,0 @@
    1        -from env_client import make_env
    2        -import numpy as np
    3        -for mode in ['front','side']:
    4        - e=make_env();s,_=e.reset(seed=29);o=s.get_object_from_name('rover1')
    5        - def p():return np.array([s.get(o,'x'),s.get(o,'y')])
    6        - def st(d):
    7        -  global s
    8        -  a=np.zeros(8);a[4:6]=d;s,*_=e.step(a)
    9        - targets=[[-1,-1],[-1.9,-1],[-1.9,-1.46]] if mode=='front' else [[-1.19,-1.75]]
   10        - for target in targets:
   11        -  for k in range(50):
   12        -   d=np.clip(np.array(target)-p(),-.1,.1)
   13        -   if np.linalg.norm(d)<1e-6:break
   14        -   st(d)
   15        - for k in range(400):
   16        -  old=p();st([0,-.0001] if mode=='front' else [-.0001,0])
   17        -  if np.allclose(p(),old,atol=1e-7,rtol=0):break
   18        - print(mode,p(),k)
   19        - e.close()
diff --git a/probe_los_details.py b/probe_los_details.py
deleted file mode 100644
index f493bbb..0000000
--- a/probe_los_details.py
+++ /dev/null
@@ -1,20 +0,0 @@
    1        -import numpy as np
    2        -from env_client import make_env
    3        -from approach import GeneratedApproach
    4        -for seed in [2,3,4]:
    5        - e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
    6        - for t in range(65):s,*_=e.step(p.get_action(s))
    7        - print('\nSEED',seed,'tasks',p.tasks)
    8        - for r,rob in enumerate(p.rovers):
    9        -  x=p.xy(s,rob);print('rover',r,x,'cal',s.get(rob,'calibrated'))
   10        -  task=p.tasks[r]
   11        -  target=p.lander if task[0]=='send' else p.xy(s,p.objectives[task[1]]) if task[0]=='image' else x
   12        -  d=target-x;print('target',target,'dist',np.linalg.norm(d))
   13        -  for ob in p.objects(s,'obstacle'):
   14        -   q=p.xy(s,ob);a=np.clip(np.dot(q-x,d)/(np.dot(d,d)+1e-20),0,1);dl=np.linalg.norm(q-x-a*d)
   15        -   if dl<.5:print('near LOS',ob.name,q,'distance',dl,'t',a,'half',s.get(ob,'half_x'),s.get(ob,'half_z'))
   16        -  for delta in [(0,0),(.1,0),(.1,0),(0,.1),(-.1,0),(-.1,0),(-.1,0),(0,-.1),(0,-.1)]:
   17        -   a=np.zeros(8,np.float32);a[r*4:r*4+2]=delta;a[r*4+3]=-.5 if task[0]=='image' else .5
   18        -   s,*_=e.step(a)
   19        -   print('probe',r,p.xy(s,rob),'cal',s.get(rob,'calibrated'),'pending',p.pending(s,r))
   20        - e.close()
diff --git a/probe_los_threshold.py b/probe_los_threshold.py
deleted file mode 100644
index 4816ba7..0000000
--- a/probe_los_threshold.py
+++ /dev/null
@@ -1,18 +0,0 @@
    1        -import numpy as np
    2        -from env_client import make_env
    3        -from probe_policy_old import GeneratedApproach
    4        -for seed,rr,points in [(4,1,[(-1.8,0),(-1.75,0),(-1.7,0),(-1.65,0),(-1.6,0)]),(3,0,[(1.4,.1),(1.3,.1),(1.3,.2),(1.2,.1)])]:
    5        - for pt in points:
    6        -  e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
    7        -  for t in range(55):s,*_=e.step(p.get_action(s))
    8        -  rob=p.rovers[rr]
    9        -  for t in range(6):
   10        -   a=np.zeros(8,np.float32);a[rr*4:rr*4+2]=np.clip(np.array(pt)-p.xy(s,rob),-.2,.2);a[rr*4+3]=-.5 if seed==4 else .5;s,*_=e.step(a)
   11        -  target=p.xy(s,p.objectives[2]) if seed==4 else p.lander
   12        -  start=p.xy(s,rob);d=target-start
   13        -  distances=[]
   14        -  for ob in p.objects(s,'obstacle')+p.rovers:
   15        -   if ob==rob:continue
   16        -   q=p.xy(s,ob);u=np.clip(np.dot(q-start,d)/np.dot(d,d),0,1);distances.append((round(np.linalg.norm(q-start-u*d),3),ob.name))
   17        -  print(seed,pt,'cal',s.get(rob,'calibrated'),'pending',p.pending(s,rr),'near',sorted(distances)[:4])
   18        -  e.close()
diff --git a/probe_motion.py b/probe_motion.py
deleted file mode 100644
index d6c986d..0000000
--- a/probe_motion.py
+++ /dev/null
@@ -1,28 +0,0 @@
    1        -from env_client import make_env
    2        -import numpy as np
    3        -
    4        -def vals(s,n='rover0'):
    5        - o=s.get_object_from_name(n);return [s.get(o,f) for f in ['x','y','theta','at_home']]
    6        -def step(e,dx=0,dy=0,dt=0):
    7        - a=np.zeros(8);a[:3]=[dx,dy,dt];t,*_=e.step(a);return t
    8        -for y in [-2.30,-2.25,-2.2,-2,-1.5,-1,-.5,0,.5,1,1.5,1.75,2,2.25,2.3]:
    9        - e=make_env();s,_=e.reset(seed=0)
   10        - while abs(vals(s)[1]-y)>.001:
   11        -  old=vals(s);s=step(e,dy=np.clip(y-old[1],-.2,.2))
   12        -  if vals(s)==old:break
   13        - for _ in range(20):
   14        -  old=vals(s);s=step(e,dx=-.05)
   15        -  if vals(s)==old:break
   16        - print('wall scan',y,vals(s))
   17        - e.close()
   18        -for mode in ['east','south','wall','home']:
   19        - e=make_env();s,_=e.reset(seed=0)
   20        - for k in range(160):
   21        -  old=vals(s)
   22        -  if mode=='east':s=step(e,dx=.01)
   23        -  if mode=='south':s=step(e,dy=-.01)
   24        -  if mode=='wall':s=step(e,dx=-.01)
   25        -  if mode=='home':s=step(e,dx=.01)
   26        -  if vals(s)==old or (mode=='home' and vals(s)[-1]==0):break
   27        - print('exact',mode,vals(s),k)
   28        - e.close()
diff --git a/probe_pillar.py b/probe_pillar.py
deleted file mode 100644
index 9e7e3f4..0000000
--- a/probe_pillar.py
+++ /dev/null
@@ -1,40 +0,0 @@
    1        -from env_client import make_env
    2        -import numpy as np
    3        -
    4        -def p(s):
    5        - o=s.get_object_from_name('rover0');return np.array([s.get(o,'x'),s.get(o,'y')])
    6        -def st(e,s,d):
    7        - a=np.zeros(8);a[:2]=d;t,*_=e.step(a);return t
    8        -
    9        -def go(e,s,target):
   10        - for _ in range(60):
   11        -  d=np.clip(np.array(target)-p(s),-.1,.1)
   12        -  if np.linalg.norm(d)<1e-5:break
   13        -  old=p(s);s=st(e,s,d)
   14        -  if np.allclose(old,p(s)): print('STUCK',p(s),'towards',target);break
   15        - return s
   16        -for mode in ['diag','left','front','right']:
   17        - e=make_env();s,_=e.reset(seed=60)
   18        - if mode=='diag':
   19        -  for o in s.get_objects(e.observation_space.get_type('obstacle')):
   20        -   print(str(o),[s.get(o,f) for f in ['x','y','half_x','half_y']])
   21        -  s=go(e,s,[1.,.4]);s=go(e,s,[1.5,.2]);print('start',p(s));s=st(e,s,[-.2,-.2]);print('diag',p(s))
   22        - elif mode=='front':
   23        -  s=go(e,s,[1.,.4]);s=go(e,s,[1.45038712,.4])
   24        -  for _ in range(500):
   25        -   old=p(s);s=st(e,s,[0,-.001])
   26        -   if np.allclose(old,p(s)):break
   27        -  print(mode,p(s))
   28        - elif mode=='right':
   29        -  s=go(e,s,[2.,-1.75]);s=go(e,s,[2.,-.21976596])
   30        -  for _ in range(600):
   31        -   old=p(s);s=st(e,s,[-.001,0])
   32        -   if np.allclose(old,p(s)):break
   33        -  print(mode,p(s))
   34        - elif mode=='left':
   35        -  s=go(e,s,[1.,.4]);s=go(e,s,[1.30000012,.4])
   36        -  for _ in range(500):
   37        -   old=p(s);s=st(e,s,[0,-.001])
   38        -   if np.allclose(old,p(s)):break
   39        -  print(mode,p(s))
   40        - e.close()
diff --git a/probe_pillar_axis.py b/probe_pillar_axis.py
deleted file mode 100644
index 4e53ca6..0000000
--- a/probe_pillar_axis.py
+++ /dev/null
@@ -1,19 +0,0 @@
    1        -from env_client import make_env
    2        -import numpy as np
    3        -for dy in [-.27,-.24,-.2,-.1,0,.1,.2,.24,.27]:
    4        - e=make_env();s,_=e.reset(seed=60);o=s.get_object_from_name('rover0')
    5        - def p():return np.array([s.get(o,'x'),s.get(o,'y')])
    6        - def st(d):
    7        -  global s
    8        -  a=np.zeros(8);a[:2]=d;s,*_=e.step(a)
    9        - for target in [[1.,-.21976596+dy],[1.15,-.21976596+dy]]:
   10        -  for k in range(40):
   11        -   d=np.clip(np.array(target)-p(),-.2,.2)
   12        -   if np.linalg.norm(d)<1e-5:break
   13        -   old=p();st(d)
   14        -   if np.allclose(old,p()):break
   15        - for k in range(40):
   16        -  old=p();st([.005,0])
   17        -  if np.allclose(old,p()):break
   18        - print(dy,p(),flush=True)
   19        - e.close()
diff --git a/probe_pillar_shape.py b/probe_pillar_shape.py
deleted file mode 100644
index 724f56c..0000000
--- a/probe_pillar_shape.py
+++ /dev/null
@@ -1,19 +0,0 @@
    1        -from env_client import make_env
    2        -import numpy as np
    3        -for dx in [-.3,-.27,-.25,-.23,-.21,-.18,-.15,-.1,-.05,0,.05,.10,.15]:
    4        - e=make_env();s,_=e.reset(seed=60);o=s.get_object_from_name('rover0')
    5        - def p():return np.array([s.get(o,'x'),s.get(o,'y')])
    6        - def st(d):
    7        -  global s
    8        -  a=np.zeros(8);a[:2]=d;s,*_=e.step(a)
    9        - for target in [[1.,.4],[1.45038712+dx,.4],[1.45038712+dx,.1]]:
   10        -  for k in range(40):
   11        -   d=np.clip(np.array(target)-p(),-.2,.2)
   12        -   if np.linalg.norm(d)<1e-5:break
   13        -   old=p();st(d)
   14        -   if np.allclose(old,p()):break
   15        - for k in range(50):
   16        -  old=p();st([0,-.01])
   17        -  if np.allclose(old,p()):break
   18        - print(dx,p(),flush=True)
   19        - e.close()
diff --git a/probe_policy_old.py b/probe_policy_old.py
deleted file mode 100644
index e24294f..0000000
--- a/probe_policy_old.py
+++ /dev/null
@@ -1,183 +0,0 @@
    1        -import math
    2        -import heapq
    3        -import numpy as np
    4        -
    5        -
    6        -class GeneratedApproach:
    7        -    """Feedback navigation and task allocation for the two rovers."""
    8        -    def __init__(self, action_space, observation_space, primitives):
    9        -        self.space = observation_space
   10        -        self.types = {t.name: t for t in observation_space.types}
   11        -
   12        -    def objects(self, state, kind):
   13        -        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)
   14        -
   15        -    def xy(self, state, obj):
   16        -        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)
   17        -
   18        -    def reset(self, state, info):
   19        -        self.rovers = self.objects(state, 'rover')
   20        -        self.objectives = self.objects(state, 'objective')
   21        -        self.samples = self.objects(state, 'sample')
   22        -        self.home = [self.xy(state, r) for r in self.rovers]
   23        -        self.lander = self.xy(state, self.objects(state, 'lander')[0])
   24        -        self.rects = []
   25        -        self.occluders = []
   26        -        for o in self.objects(state, 'obstacle'):
   27        -            p = self.xy(state, o)
   28        -            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
   29        -            self.rects.append((p-h, p+h))
   30        -            if state.get(o, 'half_z') > .1:
   31        -                self.occluders.append((p-h, p+h))
   32        -        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
   33        -        self.rects.append((self.lander-np.array([.3,.25]),self.lander+np.array([.3,.25])))
   34        -        axis = np.arange(-2.2, 2.201, .1)
   35        -        self.size = len(axis)
   36        -        xx, yy = np.meshgrid(axis, axis)
   37        -        self.points = np.column_stack([xx.ravel(), yy.ravel()])
   38        -        self.free = self.valid(self.points)
   39        -        self.masks = {}
   40        -        for k, o in enumerate(self.objectives):
   41        -            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
   42        -        for k, o in enumerate(self.samples):
   43        -            self.masks[('sample',k)] = self.free & (np.linalg.norm(self.points-self.xy(state,o),axis=1)<.235)
   44        -        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.95)
   45        -        self.tasks = [None,None]
   46        -        self.paths = [[],[]]
   47        -        self.previous = [None,None]
   48        -        self.fail = [0,0]
   49        -        self.tick = 0
   50        -
   51        -    def valid(self, pts):
   52        -        good = np.all(np.abs(pts) <= 2.265, axis=-1)
   53        -        for lo,hi in self.rects:
   54        -            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
   55        -        return good
   56        -
   57        -    def visible(self, pts, target, radius):
   58        -        good = np.linalg.norm(pts-target,axis=1)<radius
   59        -        d = target-pts
   60        -        for lo,hi in self.occluders:
   61        -            inv = np.divide(1.,d,out=np.full_like(d,1e10),where=np.abs(d)>1e-10)
   62        -            a=(lo-pts)*inv; b=(hi-pts)*inv
   63        -            enter=np.max(np.minimum(a,b),axis=1)
   64        -            leave=np.min(np.maximum(a,b),axis=1)
   65        -            good &= ~((leave>=np.maximum(enter,0)) & (enter<=1) & (leave>=0))
   66        -        return good
   67        -
   68        -    def route(self, start, mask, other=None):
   69        -        # A multi-goal Dijkstra on a small occupancy grid.
   70        -        free=self.free.copy()
   71        -        if other is not None:
   72        -            free &= np.linalg.norm(self.points-other,axis=1)>.4
   73        -        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
   74        -        root=next((int(j) for j in starts if free[j]),int(starts[0]))
   75        -        dist={root:0.}; parent={}; queue=[(0.,root)]
   76        -        n=self.size
   77        -        end=None
   78        -        while queue:
   79        -            cost,j=heapq.heappop(queue)
   80        -            if cost!=dist[j]: continue
   81        -            if mask[j]: end=j;break
   82        -            x=j%n;y=j//n
   83        -            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
   84        -                nx=x+dx;ny=y+dy
   85        -                if nx<0 or nx>=n or ny<0 or ny>=n:continue
   86        -                k=ny*n+nx
   87        -                if not free[k]:continue
   88        -                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
   89        -                v=cost+1.
   90        -                if v<dist.get(k,1e9):
   91        -                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
   92        -        if end is None:return [],1e6
   93        -        path=[end]
   94        -        while path[-1]!=root:path.append(parent[path[-1]])
   95        -        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5
   96        -
   97        -    def have(self,s,k):
   98        -        o=self.objectives[k]
   99        -        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))
  100        -
  101        -    def needed(self,s):
  102        -        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]
  103        -
  104        -    def pending(self,s,r):
  105        -        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)
  106        -
  107        -    def completed(self,s,r,task):
  108        -        kind,k=task
  109        -        if kind=='image':return self.have(s,k)
  110        -        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
  111        -        if kind=='send':return not self.pending(s,r)
  112        -        return s.get(self.rovers[r],'at_home')>.5
  113        -
  114        -    def choose(self,s,r,p,other):
  115        -        candidates=[]
  116        -        reserved=self.tasks[1-r]
  117        -        need=self.needed(s)
  118        -        for k,o in enumerate(self.objectives):
  119        -            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
  120        -        if s.get(self.rovers[r],'store_full')<.5:
  121        -            for k,o in enumerate(self.samples):
  122        -                soil=int(s.get(o,'is_soil'))
  123        -                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
  124        -        best=None;score=1e9;path=[]
  125        -        for task in candidates:
  126        -            pp,cost=self.route(p,self.masks[task],other)
  127        -            cost+=2 if task[0]=='image' else 0
  128        -            if cost<score and cost<1e5:best=task;score=cost;path=pp
  129        -        if best is None:
  130        -            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
  131        -            else:
  132        -                best=('home',r)
  133        -                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
  134        -                path,_=self.route(p,mask,other)
  135        -                path.append(self.home[r].copy())
  136        -        self.tasks[r]=best;self.paths[r]=path
  137        -
  138        -    def get_action(self, state):
  139        -        s=state; self.tick+=1
  140        -        action=np.zeros(8,dtype=np.float32)
  141        -        pos=[self.xy(s,r) for r in self.rovers]
  142        -        for r in range(2):
  143        -            p=pos[r];rob=self.rovers[r]
  144        -            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
  145        -                self.fail[r]+=1
  146        -            else:self.fail[r]=0
  147        -            task=self.tasks[r]
  148        -            if task is None or self.completed(s,r,task):
  149        -                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
  150        -            if self.fail[r]>=2:
  151        -                self.paths[r]=[]
  152        -                # Infer blocked configuration and route around it.
  153        -                blocked=p+self.previous[r][1]
  154        -                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
  155        -                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.08
  156        -                else:mask=self.masks[task]
  157        -                self.paths[r],_=self.route(p,mask,pos[1-r])
  158        -                if task[0]=='home':self.paths[r].append(self.home[r].copy())
  159        -                self.fail[r]=0
  160        -            path=self.paths[r]
  161        -            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
  162        -            dest=p.copy()
  163        -            selected=-1
  164        -            for pi,point in enumerate(path[:5]):
  165        -                d=point-p
  166        -                if np.max(np.abs(d))>.20001:break
  167        -                probes=p+np.linspace(0,1,5)[:,None]*d
  168        -                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
  169        -                else:break
  170        -            if selected>0:del path[:selected]
  171        -            d=np.clip(dest-p,-.2,.2)
  172        -            q=p+d
  173        -            op=0.
  174        -            kind,k=task
  175        -            if kind=='sample' and np.linalg.norm(q-self.xy(s,self.samples[k]))<.247:op=-5/6
  176        -            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
  177        -                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
  178        -            elif kind=='send' and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
  179        -            if op==0 and s.get(rob,'store_full')>.5:op=5/6
  180        -            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.99)[0]:op=.5
  181        -            action[r*4:r*4+2]=d;action[r*4+3]=op
  182        -            self.previous[r]=(p.copy(),d.copy())
  183        -        return action
diff --git a/probe_radio_memory.py b/probe_radio_memory.py
deleted file mode 100644
index bbad7bd..0000000
--- a/probe_radio_memory.py
+++ /dev/null
@@ -1,10 +0,0 @@
    1        -from env_client import make_env
    2        -from approach import GeneratedApproach
    3        -import sys
    4        -E=make_env();s,i=E.reset(seed=int(sys.argv[1]),options={'object_count':4} if len(sys.argv)>2 else None);A=GeneratedApproach(E.action_space,E.observation_space,{});A.reset(s,i)
    5        -for t in range(180):
    6        - ac=A.get_action(s)
    7        - if t<30 or t%10==0:print(t,[A.xy(s,r).round(3).tolist() for r in A.rovers],A.tasks,ac[[3,7]].round(2).tolist(),'good',[[p.round(3).tolist() for p in ps] for ps in A.good_radio],flush=True)
    8        - s,_,term,tr,_=E.step(ac)
    9        - if term:break
   10        -E.close()
diff --git a/probe_rover_los.py b/probe_rover_los.py
deleted file mode 100644
index c5ac47c..0000000
--- a/probe_rover_los.py
+++ /dev/null
@@ -1,9 +0,0 @@
    1        -import numpy as np
    2        -from env_client import make_env
    3        -from probe_policy_old import GeneratedApproach
    4        -e=make_env();s,info=e.reset(seed=3);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
    5        -for _ in range(55):s,*_=e.step(p.get_action(s))
    6        -for d in [(0,0),(0,-.1),(0,-.1),(.1,0),(.1,0)]:
    7        - a=np.zeros(8,np.float32);a[4:6]=d;a[3]=.5;s,*_=e.step(a)
    8        - print(p.xy(s,p.rovers[0]),p.xy(s,p.rovers[1]),'pending',p.pending(s,0))
    9        -e.close()
diff --git a/probe_send_distance.py b/probe_send_distance.py
deleted file mode 100644
index ca8481c..0000000
--- a/probe_send_distance.py
+++ /dev/null
@@ -1,13 +0,0 @@
    1        -import numpy as np
    2        -from env_client import make_env
    3        -from probe_policy_old import GeneratedApproach
    4        -for pt in [(1.4,0),(1.3,.2),(1.39,.1),(1.38,.1),(1.37,.1),(1.36,.1)]:
    5        - e=make_env();s,info=e.reset(seed=3);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
    6        - for _ in range(55):s,*_=e.step(p.get_action(s))
    7        - a=np.zeros(8,np.float32);a[:2]=np.array(pt)-p.xy(s,p.rovers[0]);a[3]=.5;s,*_=e.step(a)
    8        - print(pt,'dist',np.linalg.norm(np.array(pt)-p.lander),'pending',p.pending(s,0))
    9        - if pt==(1.4,0):
   10        -  x=np.array([1.4,.1]);d=p.lander-x
   11        -  for o in p.objects(s,'obstacle'):
   12        -   q=p.xy(s,o);u=np.clip(np.dot(q-x,d)/np.dot(d,d),0,1);print(o.name,q,'dist',np.linalg.norm(q-x-u*d),'half',s.get(o,'half_x'),s.get(o,'half_z'))
   13        - e.close()
diff --git a/probe_shape.py b/probe_shape.py
deleted file mode 100644
index 7327995..0000000
--- a/probe_shape.py
+++ /dev/null
@@ -1,18 +0,0 @@
    1        -from env_client import make_env
    2        -import numpy as np
    3        -
    4        -def p(s):
    5        - o=s.get_object_from_name('rover0');return np.array([s.get(o,'x'),s.get(o,'y')])
    6        -def step(e,s,dx=0,dy=0):
    7        - a=np.zeros(8);a[:2]=[dx,dy];t,*_=e.step(a);return t
    8        -for y in [-.1987184,.0312816,.0212816,.0112816,-.4287184,1.60,1.57,1.58,1.59,1.60,1.62,1.64,1.68,1.70,1.73,1.75,2.0]:
    9        - e=make_env();s,_=e.reset(seed=0)
   10        - for k in range(30):
   11        -  d=np.clip(y-p(s)[1],-.2,.2)
   12        -  if abs(d)<1e-6:break
   13        -  s=step(e,s,dy=d)
   14        - for k in range(130):
   15        -  old=p(s);s=step(e,s,dx=-.005)
   16        -  if np.allclose(p(s),old):break
   17        - print(y,p(s))
   18        - e.close()
diff --git a/probe_visibility.py b/probe_visibility.py
deleted file mode 100644
index ebfbe1d..0000000
--- a/probe_visibility.py
+++ /dev/null
@@ -1,28 +0,0 @@
    1        -import numpy as np
    2        -from env_client import make_env
    3        -
    4        -def run(seed=0):
    5        - env=make_env(); s,_=env.reset(seed=seed)
    6        - rs=[s.get_object_from_name('rover'+str(i)) for i in range(2)]
    7        - def xy(i):return np.array([s.get(rs[i],f) for f in ('x','y')])
    8        - def step(i,op=0,d=(0,0)):
    9        -  nonlocal s
   10        -  a=np.zeros(8,np.float32);a[4*i:4*i+2]=d;a[4*i+3]=op
   11        -  s,*_=env.step(a)
   12        - def go(i,target):
   13        -  for _ in range(50):
   14        -   p=xy(i);d=np.clip(np.array(target)-p,-.2,.2)
   15        -   if np.max(np.abs(d))<1e-5:return True
   16        -   step(i,d=d)
   17        -   if np.linalg.norm(xy(i)-p)<1e-5:print('blocked',i,xy(i),target);return False
   18        - def ims():return [(o.name,int(s.get(o,'have_image_rover0')),int(s.get(o,'have_image_rover1')),int(s.get(o,'received_image'))) for o in s.get_objects(env.observation_space.get_type('objective'))]
   19        - go(0,(1,.5));step(0,-.5);step(0,-1/6);step(0,-.5);step(0,-1/6);print('photo',xy(0),ims())
   20        - step(0,.5);print('send high',ims())
   21        - go(0,(1,-1.75));step(0,.5);print('send home',ims())
   22        - go(1,(-1.4,-.1));step(1,-5/6);print('sample at',xy(1),[(o.name,int(s.get(o,'analyzed_rover1'))) for o in s.get_objects(env.observation_space.get_type('sample'))])
   23        - go(1,(-1.4,0));step(1,-5/6);step(1,.5);print('sample/send',xy(1),[(o.name,int(s.get(o,'analyzed_rover1')),int(s.get(o,'received_analysis'))) for o in s.get_objects(env.observation_space.get_type('sample'))])
   24        - step(1,5/6);print('drop',s.get(rs[1],'store_full'))
   25        - go(1,(-1.8,.35));step(1,-.5);step(1,-1/6);print('left photo',xy(1),ims())
   26        - go(0,(.4,-1.75));go(0,(-.4,-1.75));print('cross bottom',xy(0))
   27        - env.close()
   28        -run()
diff --git a/scan_results.txt b/scan_results.txt
deleted file mode 100644
index 61d17e9..0000000
--- a/scan_results.txt
+++ /dev/null
@@ -1,12 +0,0 @@
    1        -PROGRESS 5000
    2        -PROGRESS 5100
    3        -PROGRESS 5200
    4        -PROGRESS 5300
    5        -PROGRESS 5400
    6        -PROGRESS 5500
    7        -PROGRESS 5600
    8        -PROGRESS 5700
    9        -PROGRESS 5800
   10        -5828 ['sample0_unreachable']
   11        -PROGRESS 5900
   12        -DONE 1
diff --git a/stats200.json b/stats200.json
deleted file mode 100644
index 7635566..0000000
--- a/stats200.json
+++ /dev/null
@@ -1 +0,0 @@
    1        -[{"seed": 200, "n": 1, "success": true, "steps": 21, "time": 0.103, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 201, "n": 1, "success": true, "steps": 60, "time": 0.333, "bad": [2, 0, 29], "ops": [1, 1, 31, 2, 2]}, {"seed": 202, "n": 1, "success": true, "steps": 30, "time": 0.195, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 203, "n": 1, "success": true, "steps": 29, "time": 0.181, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 204, "n": 3, "success": true, "steps": 22, "time": 0.19, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 205, "n": 2, "success": true, "steps": 30, "time": 0.188, "bad": [2, 0, 8], "ops": [2, 2, 11, 2, 2]}, {"seed": 206, "n": 2, "success": true, "steps": 21, "time": 0.106, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 207, "n": 1, "success": true, "steps": 25, "time": 0.116, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 208, "n": 3, "success": true, "steps": 27, "time": 0.226, "bad": [0, 1, 0], "ops": [4, 3, 5, 2, 2]}, {"seed": 209, "n": 3, "success": true, "steps": 26, "time": 0.164, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 210, "n": 1, "success": true, "steps": 23, "time": 0.165, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 211, "n": 1, "success": true, "steps": 19, "time": 0.149, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 212, "n": 1, "success": true, "steps": 29, "time": 0.348, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 213, "n": 1, "success": true, "steps": 27, "time": 0.219, "bad": [2, 2, 0], "ops": [3, 1, 2, 2, 2]}, {"seed": 214, "n": 1, "success": true, "steps": 23, "time": 0.175, "bad": [0, 0, 7], "ops": [1, 1, 9, 2, 2]}, {"seed": 215, "n": 3, "success": true, "steps": 33, "time": 0.276, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 216, "n": 3, "success": true, "steps": 25, "time": 0.199, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 217, "n": 3, "success": true, "steps": 27, "time": 0.181, "bad": [2, 0, 0], "ops": [4, 4, 4, 4, 2]}, {"seed": 218, "n": 2, "success": true, "steps": 28, "time": 0.217, "bad": [2, 2, 0], "ops": [4, 2, 4, 2, 2]}, {"seed": 219, "n": 1, "success": true, "steps": 39, "time": 0.213, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 220, "n": 3, "success": true, "steps": 37, "time": 0.284, "bad": [4, 1, 1], "ops": [4, 3, 4, 4, 2]}, {"seed": 221, "n": 2, "success": true, "steps": 23, "time": 0.193, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 222, "n": 2, "success": true, "steps": 26, "time": 0.207, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 223, "n": 2, "success": true, "steps": 34, "time": 0.228, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 224, "n": 3, "success": true, "steps": 23, "time": 0.203, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 225, "n": 3, "success": true, "steps": 28, "time": 0.199, "bad": [0, 1, 0], "ops": [5, 4, 2, 2, 2]}, {"seed": 226, "n": 3, "success": true, "steps": 23, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 227, "n": 2, "success": true, "steps": 21, "time": 0.201, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 228, "n": 2, "success": true, "steps": 25, "time": 0.121, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 229, "n": 2, "success": true, "steps": 26, "time": 0.221, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 230, "n": 2, "success": true, "steps": 33, "time": 0.232, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 231, "n": 1, "success": true, "steps": 27, "time": 0.261, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 232, "n": 2, "success": true, "steps": 26, "time": 0.182, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 233, "n": 1, "success": true, "steps": 22, "time": 0.156, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 234, "n": 2, "success": true, "steps": 28, "time": 0.195, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 235, "n": 3, "success": true, "steps": 38, "time": 0.226, "bad": [4, 0, 0], "ops": [4, 4, 4, 6, 2]}, {"seed": 236, "n": 2, "success": true, "steps": 21, "time": 0.137, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 237, "n": 3, "success": true, "steps": 30, "time": 0.226, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 238, "n": 2, "success": true, "steps": 21, "time": 0.153, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 239, "n": 3, "success": true, "steps": 28, "time": 0.214, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 240, "n": 3, "success": true, "steps": 26, "time": 0.153, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 241, "n": 2, "success": true, "steps": 28, "time": 0.203, "bad": [0, 2, 0], "ops": [4, 2, 3, 2, 2]}, {"seed": 242, "n": 3, "success": true, "steps": 31, "time": 0.238, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 243, "n": 3, "success": true, "steps": 34, "time": 0.269, "bad": [2, 2, 0], "ops": [5, 3, 3, 2, 2]}, {"seed": 244, "n": 3, "success": true, "steps": 24, "time": 0.203, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 245, "n": 3, "success": true, "steps": 32, "time": 0.215, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 246, "n": 3, "success": true, "steps": 29, "time": 0.226, "bad": [2, 0, 0], "ops": [3, 3, 4, 4, 2]}, {"seed": 247, "n": 1, "success": true, "steps": 24, "time": 0.157, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 248, "n": 2, "success": true, "steps": 26, "time": 0.181, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 249, "n": 3, "success": true, "steps": 24, "time": 0.183, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 250, "n": 2, "success": true, "steps": 39, "time": 0.236, "bad": [4, 0, 0], "ops": [2, 2, 3, 4, 2]}, {"seed": 251, "n": 1, "success": true, "steps": 20, "time": 0.148, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 252, "n": 3, "success": true, "steps": 28, "time": 0.193, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 253, "n": 2, "success": true, "steps": 22, "time": 0.166, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 254, "n": 1, "success": true, "steps": 19, "time": 0.14, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 255, "n": 1, "success": true, "steps": 38, "time": 0.231, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 256, "n": 2, "success": true, "steps": 36, "time": 0.181, "bad": [2, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 257, "n": 3, "success": true, "steps": 29, "time": 0.211, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 258, "n": 2, "success": true, "steps": 26, "time": 0.184, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 259, "n": 1, "success": true, "steps": 27, "time": 0.182, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 260, "n": 3, "success": true, "steps": 32, "time": 0.214, "bad": [2, 2, 3], "ops": [5, 3, 8, 2, 2]}, {"seed": 261, "n": 2, "success": true, "steps": 29, "time": 0.102, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 262, "n": 3, "success": false, "steps": 200, "time": 2.204, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 263, "n": 3, "success": true, "steps": 25, "time": 0.17, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 264, "n": 1, "success": true, "steps": 22, "time": 0.143, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 265, "n": 3, "success": true, "steps": 34, "time": 0.19, "bad": [5, 2, 0], "ops": [6, 4, 5, 2, 2]}, {"seed": 266, "n": 2, "success": true, "steps": 29, "time": 0.123, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 267, "n": 2, "success": true, "steps": 22, "time": 0.183, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 268, "n": 3, "success": true, "steps": 31, "time": 0.145, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 269, "n": 3, "success": true, "steps": 24, "time": 0.187, "bad": [0, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 270, "n": 2, "success": true, "steps": 20, "time": 0.143, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 271, "n": 3, "success": true, "steps": 24, "time": 0.163, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 272, "n": 1, "success": true, "steps": 22, "time": 0.164, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 273, "n": 1, "success": true, "steps": 24, "time": 0.156, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 274, "n": 2, "success": true, "steps": 38, "time": 0.214, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 275, "n": 1, "success": true, "steps": 22, "time": 0.134, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 276, "n": 2, "success": true, "steps": 24, "time": 0.128, "bad": [1, 1, 0], "ops": [3, 2, 2, 2, 2]}, {"seed": 277, "n": 1, "success": true, "steps": 24, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 278, "n": 2, "success": true, "steps": 26, "time": 0.133, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 279, "n": 2, "success": true, "steps": 24, "time": 0.126, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 280, "n": 2, "success": true, "steps": 35, "time": 0.206, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 281, "n": 2, "success": true, "steps": 26, "time": 0.184, "bad": [2, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 282, "n": 3, "success": true, "steps": 25, "time": 0.163, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 283, "n": 1, "success": true, "steps": 20, "time": 0.143, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 284, "n": 1, "success": true, "steps": 35, "time": 0.216, "bad": [2, 0, 0], "ops": [1, 1, 3, 4, 2]}, {"seed": 285, "n": 3, "success": true, "steps": 28, "time": 0.182, "bad": [0, 0, 1], "ops": [3, 3, 4, 2, 2]}, {"seed": 286, "n": 1, "success": true, "steps": 20, "time": 0.13, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 287, "n": 3, "success": true, "steps": 27, "time": 0.208, "bad": [2, 3, 0], "ops": [6, 3, 4, 2, 2]}, {"seed": 288, "n": 1, "success": true, "steps": 21, "time": 0.148, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 289, "n": 2, "success": true, "steps": 27, "time": 0.199, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 290, "n": 1, "success": true, "steps": 22, "time": 0.137, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 291, "n": 1, "success": true, "steps": 25, "time": 0.157, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 292, "n": 3, "success": true, "steps": 26, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 293, "n": 1, "success": true, "steps": 22, "time": 0.164, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 294, "n": 1, "success": true, "steps": 36, "time": 0.205, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 295, "n": 1, "success": true, "steps": 23, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 296, "n": 1, "success": true, "steps": 24, "time": 0.169, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 297, "n": 1, "success": true, "steps": 20, "time": 0.08, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 298, "n": 2, "success": true, "steps": 23, "time": 0.137, "bad": [2, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 299, "n": 3, "success": true, "steps": 26, "time": 0.195, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 300, "n": 1, "success": true, "steps": 23, "time": 0.151, "bad": [0, 0, 4], "ops": [1, 1, 7, 2, 2]}, {"seed": 301, "n": 1, "success": true, "steps": 34, "time": 0.212, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 302, "n": 3, "success": true, "steps": 24, "time": 0.197, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 303, "n": 2, "success": true, "steps": 36, "time": 0.244, "bad": [5, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 304, "n": 3, "success": true, "steps": 27, "time": 0.217, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 305, "n": 1, "success": true, "steps": 21, "time": 0.17, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 306, "n": 3, "success": true, "steps": 33, "time": 0.253, "bad": [4, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 307, "n": 3, "success": true, "steps": 29, "time": 0.252, "bad": [2, 0, 0], "ops": [3, 3, 5, 4, 2]}, {"seed": 308, "n": 2, "success": true, "steps": 27, "time": 0.2, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 309, "n": 2, "success": true, "steps": 22, "time": 0.177, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 310, "n": 1, "success": true, "steps": 24, "time": 0.17, "bad": [0, 0, 7], "ops": [1, 1, 9, 2, 2]}, {"seed": 311, "n": 2, "success": true, "steps": 35, "time": 0.243, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 312, "n": 1, "success": true, "steps": 25, "time": 0.153, "bad": [0, 0, 2], "ops": [1, 1, 5, 2, 2]}, {"seed": 313, "n": 1, "success": true, "steps": 23, "time": 0.147, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 314, "n": 2, "success": true, "steps": 27, "time": 0.247, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 315, "n": 2, "success": true, "steps": 22, "time": 0.166, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 316, "n": 1, "success": true, "steps": 21, "time": 0.138, "bad": [0, 0, 5], "ops": [1, 1, 8, 2, 2]}, {"seed": 317, "n": 1, "success": true, "steps": 23, "time": 0.16, "bad": [0, 0, 8], "ops": [1, 1, 11, 2, 2]}, {"seed": 318, "n": 1, "success": true, "steps": 21, "time": 0.151, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 319, "n": 3, "success": true, "steps": 33, "time": 0.276, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 320, "n": 1, "success": true, "steps": 35, "time": 0.186, "bad": [0, 0, 13], "ops": [1, 1, 16, 2, 2]}, {"seed": 321, "n": 2, "success": true, "steps": 23, "time": 0.184, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 322, "n": 1, "success": true, "steps": 22, "time": 0.121, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 323, "n": 3, "success": true, "steps": 25, "time": 0.178, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 324, "n": 2, "success": true, "steps": 25, "time": 0.198, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 325, "n": 1, "success": true, "steps": 25, "time": 0.172, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 326, "n": 1, "success": true, "steps": 23, "time": 0.157, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 327, "n": 2, "success": true, "steps": 25, "time": 0.171, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 328, "n": 1, "success": true, "steps": 28, "time": 0.166, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 329, "n": 3, "success": true, "steps": 26, "time": 0.179, "bad": [2, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 330, "n": 2, "success": true, "steps": 40, "time": 0.269, "bad": [0, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 331, "n": 1, "success": true, "steps": 30, "time": 0.188, "bad": [0, 2, 0], "ops": [3, 1, 3, 2, 2]}, {"seed": 332, "n": 2, "success": true, "steps": 29, "time": 0.219, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 333, "n": 1, "success": true, "steps": 26, "time": 0.142, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 334, "n": 2, "success": true, "steps": 24, "time": 0.194, "bad": [0, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 335, "n": 1, "success": true, "steps": 22, "time": 0.172, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 336, "n": 2, "success": true, "steps": 29, "time": 0.211, "bad": [2, 2, 0], "ops": [4, 2, 3, 2, 2]}, {"seed": 337, "n": 1, "success": true, "steps": 24, "time": 0.165, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 338, "n": 2, "success": true, "steps": 25, "time": 0.206, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 339, "n": 1, "success": true, "steps": 23, "time": 0.116, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 340, "n": 1, "success": true, "steps": 26, "time": 0.167, "bad": [0, 0, 6], "ops": [1, 1, 8, 2, 2]}, {"seed": 341, "n": 3, "success": true, "steps": 25, "time": 0.229, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 342, "n": 3, "success": true, "steps": 32, "time": 0.24, "bad": [0, 0, 1], "ops": [3, 3, 5, 2, 2]}, {"seed": 343, "n": 1, "success": true, "steps": 25, "time": 0.282, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 344, "n": 1, "success": true, "steps": 25, "time": 0.159, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 345, "n": 1, "success": true, "steps": 19, "time": 0.147, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 346, "n": 2, "success": true, "steps": 23, "time": 0.181, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 347, "n": 3, "success": true, "steps": 27, "time": 0.209, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 348, "n": 1, "success": true, "steps": 27, "time": 0.34, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 349, "n": 3, "success": false, "steps": 200, "time": 3.08, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 350, "n": 2, "success": true, "steps": 31, "time": 0.181, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 351, "n": 2, "success": true, "steps": 47, "time": 0.282, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 352, "n": 1, "success": true, "steps": 24, "time": 0.18, "bad": [2, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 353, "n": 1, "success": true, "steps": 29, "time": 0.17, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 354, "n": 3, "success": true, "steps": 27, "time": 0.231, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 355, "n": 2, "success": true, "steps": 22, "time": 0.167, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 356, "n": 1, "success": true, "steps": 25, "time": 0.185, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 357, "n": 2, "success": true, "steps": 32, "time": 0.257, "bad": [0, 1, 3], "ops": [4, 3, 5, 2, 2]}, {"seed": 358, "n": 3, "success": true, "steps": 27, "time": 0.216, "bad": [2, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 359, "n": 2, "success": true, "steps": 29, "time": 0.21, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 360, "n": 3, "success": true, "steps": 31, "time": 0.238, "bad": [2, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 361, "n": 3, "success": true, "steps": 29, "time": 0.241, "bad": [0, 0, 4], "ops": [3, 3, 8, 2, 2]}, {"seed": 362, "n": 3, "success": true, "steps": 31, "time": 0.184, "bad": [2, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 363, "n": 1, "success": true, "steps": 20, "time": 0.162, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 364, "n": 2, "success": true, "steps": 24, "time": 0.183, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 365, "n": 1, "success": true, "steps": 23, "time": 0.167, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 366, "n": 1, "success": true, "steps": 21, "time": 0.147, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 367, "n": 3, "success": true, "steps": 30, "time": 0.244, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 368, "n": 3, "success": true, "steps": 28, "time": 0.227, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 369, "n": 3, "success": true, "steps": 35, "time": 0.282, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 370, "n": 2, "success": true, "steps": 39, "time": 0.266, "bad": [0, 0, 1], "ops": [2, 2, 4, 2, 2]}, {"seed": 371, "n": 3, "success": true, "steps": 30, "time": 0.223, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 372, "n": 2, "success": true, "steps": 38, "time": 0.249, "bad": [2, 1, 9], "ops": [3, 2, 12, 2, 2]}, {"seed": 373, "n": 2, "success": true, "steps": 28, "time": 0.192, "bad": [2, 2, 0], "ops": [4, 2, 3, 2, 2]}, {"seed": 374, "n": 3, "success": true, "steps": 27, "time": 0.204, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 375, "n": 1, "success": true, "steps": 21, "time": 0.118, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 376, "n": 2, "success": true, "steps": 23, "time": 0.189, "bad": [2, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 377, "n": 3, "success": true, "steps": 31, "time": 0.217, "bad": [0, 0, 2], "ops": [3, 3, 7, 2, 2]}, {"seed": 378, "n": 2, "success": true, "steps": 37, "time": 0.236, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 379, "n": 3, "success": true, "steps": 30, "time": 0.234, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 380, "n": 2, "success": true, "steps": 22, "time": 0.142, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 381, "n": 3, "success": true, "steps": 25, "time": 0.209, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 382, "n": 1, "success": true, "steps": 26, "time": 0.175, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 383, "n": 1, "success": true, "steps": 26, "time": 0.171, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 384, "n": 1, "success": true, "steps": 31, "time": 0.195, "bad": [2, 0, 11], "ops": [1, 1, 13, 2, 2]}, {"seed": 385, "n": 3, "success": true, "steps": 28, "time": 0.208, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 386, "n": 2, "success": true, "steps": 30, "time": 0.207, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 387, "n": 2, "success": true, "steps": 37, "time": 0.254, "bad": [1, 1, 0], "ops": [3, 2, 4, 2, 2]}, {"seed": 388, "n": 2, "success": true, "steps": 24, "time": 0.187, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 389, "n": 1, "success": true, "steps": 24, "time": 0.184, "bad": [0, 0, 5], "ops": [1, 1, 7, 2, 2]}, {"seed": 390, "n": 2, "success": true, "steps": 22, "time": 0.157, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 391, "n": 1, "success": true, "steps": 32, "time": 0.223, "bad": [0, 1, 0], "ops": [2, 1, 3, 2, 2]}, {"seed": 392, "n": 3, "success": true, "steps": 27, "time": 0.213, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 393, "n": 3, "success": true, "steps": 27, "time": 0.212, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 394, "n": 1, "success": true, "steps": 21, "time": 0.125, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 395, "n": 2, "success": true, "steps": 27, "time": 0.194, "bad": [2, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 396, "n": 2, "success": true, "steps": 27, "time": 0.205, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 397, "n": 3, "success": true, "steps": 27, "time": 0.208, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 398, "n": 3, "success": true, "steps": 27, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 399, "n": 3, "success": true, "steps": 26, "time": 0.179, "bad": [2, 0, 0], "ops": [3, 3, 3, 4, 2]}]
\ No newline at end of file
diff --git a/stats200.txt b/stats200.txt
deleted file mode 100644
index 7788e14..0000000
--- a/stats200.txt
+++ /dev/null
@@ -1,23 +0,0 @@
    1        -{'seed': 200, 'n': 1, 'success': True, 'steps': 21, 'time': 0.103, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    2        -{'seed': 210, 'n': 1, 'success': True, 'steps': 23, 'time': 0.165, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    3        -{'seed': 220, 'n': 3, 'success': True, 'steps': 37, 'time': 0.284, 'bad': [4, 1, 1], 'ops': [4, 3, 4, 4, 2]}
    4        -{'seed': 230, 'n': 2, 'success': True, 'steps': 33, 'time': 0.232, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    5        -{'seed': 240, 'n': 3, 'success': True, 'steps': 26, 'time': 0.153, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    6        -{'seed': 250, 'n': 2, 'success': True, 'steps': 39, 'time': 0.236, 'bad': [4, 0, 0], 'ops': [2, 2, 3, 4, 2]}
    7        -{'seed': 260, 'n': 3, 'success': True, 'steps': 32, 'time': 0.214, 'bad': [2, 2, 3], 'ops': [5, 3, 8, 2, 2]}
    8        -{'seed': 262, 'n': 3, 'success': False, 'steps': 200, 'time': 2.204, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    9        -{'seed': 270, 'n': 2, 'success': True, 'steps': 20, 'time': 0.143, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
   10        -{'seed': 280, 'n': 2, 'success': True, 'steps': 35, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
   11        -{'seed': 290, 'n': 1, 'success': True, 'steps': 22, 'time': 0.137, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
   12        -{'seed': 300, 'n': 1, 'success': True, 'steps': 23, 'time': 0.151, 'bad': [0, 0, 4], 'ops': [1, 1, 7, 2, 2]}
   13        -{'seed': 310, 'n': 1, 'success': True, 'steps': 24, 'time': 0.17, 'bad': [0, 0, 7], 'ops': [1, 1, 9, 2, 2]}
   14        -{'seed': 320, 'n': 1, 'success': True, 'steps': 35, 'time': 0.186, 'bad': [0, 0, 13], 'ops': [1, 1, 16, 2, 2]}
   15        -{'seed': 330, 'n': 2, 'success': True, 'steps': 40, 'time': 0.269, 'bad': [0, 1, 0], 'ops': [3, 2, 4, 2, 2]}
   16        -{'seed': 340, 'n': 1, 'success': True, 'steps': 26, 'time': 0.167, 'bad': [0, 0, 6], 'ops': [1, 1, 8, 2, 2]}
   17        -{'seed': 349, 'n': 3, 'success': False, 'steps': 200, 'time': 3.08, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
   18        -{'seed': 350, 'n': 2, 'success': True, 'steps': 31, 'time': 0.181, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
   19        -{'seed': 360, 'n': 3, 'success': True, 'steps': 31, 'time': 0.238, 'bad': [2, 0, 0], 'ops': [4, 4, 3, 2, 2]}
   20        -{'seed': 370, 'n': 2, 'success': True, 'steps': 39, 'time': 0.266, 'bad': [0, 0, 1], 'ops': [2, 2, 4, 2, 2]}
   21        -{'seed': 380, 'n': 2, 'success': True, 'steps': 22, 'time': 0.142, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
   22        -{'seed': 390, 'n': 2, 'success': True, 'steps': 22, 'time': 0.157, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
   23        -SUMMARY 198 200 mean 28.83 max_time 3.08
diff --git a/stats_final2000.txt b/stats_final2000.txt
deleted file mode 100644
index 444e391..0000000
--- a/stats_final2000.txt
+++ /dev/null
@@ -1,11 +0,0 @@
    1        -{'seed': 2000, 'n': 1, 'success': True, 'steps': 22, 'time': 0.105, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    2        -{'seed': 2010, 'n': 3, 'success': True, 'steps': 24, 'time': 0.222, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    3        -{'seed': 2020, 'n': 1, 'success': True, 'steps': 23, 'time': 0.103, 'bad': [0, 0, 7], 'ops': [1, 1, 10, 2, 2]}
    4        -{'seed': 2030, 'n': 1, 'success': True, 'steps': 19, 'time': 0.106, 'bad': [0, 0, 6], 'ops': [1, 1, 9, 2, 2]}
    5        -{'seed': 2040, 'n': 2, 'success': True, 'steps': 21, 'time': 0.143, 'bad': [0, 0, 0], 'ops': [2, 2, 2, 2, 2]}
    6        -{'seed': 2050, 'n': 2, 'success': True, 'steps': 22, 'time': 0.182, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
    7        -{'seed': 2060, 'n': 1, 'success': True, 'steps': 23, 'time': 0.189, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    8        -{'seed': 2070, 'n': 2, 'success': True, 'steps': 24, 'time': 0.22, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
    9        -{'seed': 2080, 'n': 3, 'success': True, 'steps': 26, 'time': 0.241, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
   10        -{'seed': 2090, 'n': 2, 'success': True, 'steps': 23, 'time': 0.167, 'bad': [0, 0, 7], 'ops': [2, 2, 9, 2, 2]}
   11        -SUMMARY 100 100 mean 23.54 max_time 0.271
diff --git a/stats_final4.txt b/stats_final4.txt
deleted file mode 100644
index d61343e..0000000
--- a/stats_final4.txt
+++ /dev/null
@@ -1,11 +0,0 @@
    1        -{'seed': 1200, 'n': 4, 'success': True, 'steps': 26, 'time': 0.169, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
    2        -{'seed': 1210, 'n': 4, 'success': True, 'steps': 24, 'time': 0.292, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
    3        -{'seed': 1220, 'n': 4, 'success': True, 'steps': 23, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [5, 5, 3, 2, 2]}
    4        -{'seed': 1230, 'n': 4, 'success': True, 'steps': 29, 'time': 0.306, 'bad': [0, 1, 0], 'ops': [5, 4, 4, 2, 2]}
    5        -{'seed': 1240, 'n': 4, 'success': True, 'steps': 26, 'time': 0.271, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
    6        -{'seed': 1250, 'n': 4, 'success': True, 'steps': 24, 'time': 0.227, 'bad': [0, 0, 0], 'ops': [4, 4, 4, 2, 2]}
    7        -{'seed': 1260, 'n': 4, 'success': True, 'steps': 28, 'time': 0.211, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
    8        -{'seed': 1270, 'n': 4, 'success': True, 'steps': 28, 'time': 0.302, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
    9        -{'seed': 1280, 'n': 4, 'success': True, 'steps': 24, 'time': 0.234, 'bad': [0, 0, 0], 'ops': [4, 4, 4, 2, 2]}
   10        -{'seed': 1290, 'n': 4, 'success': True, 'steps': 26, 'time': 0.265, 'bad': [0, 1, 0], 'ops': [5, 4, 3, 2, 2]}
   11        -SUMMARY 100 100 mean 26.88 max_time 0.384
diff --git a/stats_final400.txt b/stats_final400.txt
deleted file mode 100644
index 433c359..0000000
--- a/stats_final400.txt
+++ /dev/null
@@ -1,21 +0,0 @@
    1        -{'seed': 400, 'n': 3, 'success': True, 'steps': 23, 'time': 0.191, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    2        -{'seed': 410, 'n': 2, 'success': True, 'steps': 22, 'time': 0.217, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    3        -{'seed': 420, 'n': 2, 'success': True, 'steps': 21, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [2, 2, 2, 2, 2]}
    4        -{'seed': 430, 'n': 1, 'success': True, 'steps': 22, 'time': 0.17, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    5        -{'seed': 440, 'n': 1, 'success': True, 'steps': 20, 'time': 0.117, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    6        -{'seed': 450, 'n': 1, 'success': True, 'steps': 25, 'time': 0.175, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
    7        -{'seed': 460, 'n': 1, 'success': True, 'steps': 21, 'time': 0.129, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    8        -{'seed': 470, 'n': 3, 'success': True, 'steps': 27, 'time': 0.254, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
    9        -{'seed': 480, 'n': 3, 'success': True, 'steps': 21, 'time': 0.228, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
   10        -{'seed': 490, 'n': 2, 'success': True, 'steps': 21, 'time': 0.212, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
   11        -{'seed': 500, 'n': 2, 'success': True, 'steps': 25, 'time': 0.18, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
   12        -{'seed': 510, 'n': 1, 'success': True, 'steps': 24, 'time': 0.145, 'bad': [0, 0, 4], 'ops': [1, 1, 7, 2, 2]}
   13        -{'seed': 520, 'n': 1, 'success': True, 'steps': 18, 'time': 0.147, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
   14        -{'seed': 530, 'n': 1, 'success': True, 'steps': 23, 'time': 0.101, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
   15        -{'seed': 540, 'n': 1, 'success': True, 'steps': 19, 'time': 0.127, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
   16        -{'seed': 550, 'n': 3, 'success': True, 'steps': 29, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
   17        -{'seed': 560, 'n': 3, 'success': True, 'steps': 23, 'time': 0.197, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
   18        -{'seed': 570, 'n': 1, 'success': True, 'steps': 22, 'time': 0.172, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
   19        -{'seed': 580, 'n': 1, 'success': True, 'steps': 21, 'time': 0.156, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
   20        -{'seed': 590, 'n': 2, 'success': True, 'steps': 23, 'time': 0.195, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
   21        -SUMMARY 200 200 mean 23.35 max_time 0.496
diff --git a/stats_final_latest.txt b/stats_final_latest.txt
index 9f32b6c..6c09e4a 100644
--- a/stats_final_latest.txt
+++ b/stats_final_latest.txt
@@ -2,3 +2,7 @@
    2      2  {'seed': 10, 'n': 3, 'success': True, 'steps': 22, 'time': 0.194, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    3      3  {'seed': 20, 'n': 3, 'success': True, 'steps': 27, 'time': 0.266, 'bad': [0, 0, 0], 'ops': [4, 3, 2, 2, 2]}
    4      4  {'seed': 30, 'n': 1, 'success': True, 'steps': 34, 'time': 0.24, 'bad': [0, 0, 4], 'ops': [1, 1, 6, 2, 2]}
           5 +{'seed': 40, 'n': 2, 'success': True, 'steps': 25, 'time': 0.201, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
           6 +{'seed': 50, 'n': 3, 'success': True, 'steps': 24, 'time': 0.233, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
           7 +{'seed': 60, 'n': 1, 'success': True, 'steps': 22, 'time': 0.138, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
           8 +{'seed': 70, 'n': 2, 'success': True, 'steps': 22, 'time': 0.135, 'bad': [0, 1, 0], 'ops': [3, 2, 3, 2, 2]}
diff --git a/stats_final_latest4.txt b/stats_final_latest4.txt
index ca24e99..7786e47 100644
--- a/stats_final_latest4.txt
+++ b/stats_final_latest4.txt
@@ -2,3 +2,5 @@
    2      2  {'seed': 1210, 'n': 4, 'success': True, 'steps': 24, 'time': 0.253, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
    3      3  {'seed': 1220, 'n': 4, 'success': True, 'steps': 23, 'time': 0.201, 'bad': [0, 0, 0], 'ops': [5, 5, 3, 2, 2]}
    4      4  {'seed': 1230, 'n': 4, 'success': True, 'steps': 29, 'time': 0.261, 'bad': [0, 1, 0], 'ops': [5, 4, 4, 2, 2]}
           5 +{'seed': 1240, 'n': 4, 'success': True, 'steps': 26, 'time': 0.245, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
           6 +{'seed': 1250, 'n': 4, 'success': True, 'steps': 24, 'time': 0.243, 'bad': [0, 0, 0], 'ops': [4, 4, 4, 2, 2]}
diff --git a/stats_greedy.txt b/stats_greedy.txt
deleted file mode 100644
index a179298..0000000
--- a/stats_greedy.txt
+++ /dev/null
@@ -1,11 +0,0 @@
    1        -{'seed': 0, 'n': 3, 'success': True, 'steps': 36, 'time': 0.199, 'bad': [0, 0, 3], 'ops': [3, 3, 6, 2, 2]}
    2        -{'seed': 10, 'n': 3, 'success': True, 'steps': 25, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    3        -{'seed': 20, 'n': 3, 'success': True, 'steps': 33, 'time': 0.293, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    4        -{'seed': 30, 'n': 1, 'success': True, 'steps': 22, 'time': 0.191, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    5        -{'seed': 40, 'n': 2, 'success': True, 'steps': 26, 'time': 0.21, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    6        -{'seed': 50, 'n': 3, 'success': True, 'steps': 28, 'time': 0.187, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    7        -{'seed': 60, 'n': 1, 'success': True, 'steps': 28, 'time': 0.17, 'bad': [2, 0, 2], 'ops': [1, 1, 4, 2, 2]}
    8        -{'seed': 70, 'n': 2, 'success': True, 'steps': 25, 'time': 0.198, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
    9        -{'seed': 80, 'n': 3, 'success': True, 'steps': 27, 'time': 0.174, 'bad': [0, 1, 0], 'ops': [5, 4, 2, 2, 2]}
   10        -{'seed': 90, 'n': 2, 'success': True, 'steps': 31, 'time': 0.214, 'bad': [0, 1, 1], 'ops': [3, 2, 4, 2, 2]}
   11        -SUMMARY 100 100 mean 26.41 max_time 0.309
diff --git a/stats_octagon.txt b/stats_octagon.txt
deleted file mode 100644
index 9ab335d..0000000
--- a/stats_octagon.txt
+++ /dev/null
@@ -1,11 +0,0 @@
    1        -{'seed': 0, 'n': 3, 'success': True, 'steps': 28, 'time': 0.138, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    2        -{'seed': 10, 'n': 3, 'success': True, 'steps': 22, 'time': 0.171, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    3        -{'seed': 20, 'n': 3, 'success': True, 'steps': 27, 'time': 0.222, 'bad': [0, 0, 0], 'ops': [4, 3, 2, 2, 2]}
    4        -{'seed': 30, 'n': 1, 'success': True, 'steps': 24, 'time': 0.163, 'bad': [0, 0, 4], 'ops': [1, 1, 6, 2, 2]}
    5        -{'seed': 40, 'n': 2, 'success': True, 'steps': 25, 'time': 0.151, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    6        -{'seed': 50, 'n': 3, 'success': True, 'steps': 24, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    7        -{'seed': 60, 'n': 1, 'success': True, 'steps': 22, 'time': 0.174, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
    8        -{'seed': 70, 'n': 2, 'success': True, 'steps': 22, 'time': 0.218, 'bad': [0, 1, 0], 'ops': [3, 2, 3, 2, 2]}
    9        -{'seed': 80, 'n': 3, 'success': True, 'steps': 23, 'time': 0.214, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
   10        -{'seed': 90, 'n': 2, 'success': True, 'steps': 29, 'time': 0.187, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
   11        -SUMMARY 100 100 mean 23.63 max_time 0.267
diff --git a/stats_pipeline.json b/stats_pipeline.json
deleted file mode 100644
index b1b43f6..0000000
--- a/stats_pipeline.json
+++ /dev/null
@@ -1 +0,0 @@
    1        -[{"seed": 0, "n": 3, "success": true, "steps": 28, "time": 0.211, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 21, "time": 0.198, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 21, "time": 0.219, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 24, "time": 0.236, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 23, "time": 0.22, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 25, "time": 0.27, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 21, "time": 0.197, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 27, "time": 0.246, "bad": [2, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 26, "time": 0.204, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 28, "time": 0.253, "bad": [4, 0, 2], "ops": [2, 2, 5, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 22, "time": 0.212, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 20, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 24, "time": 0.19, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 27, "time": 0.272, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 31, "time": 0.227, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 27, "time": 0.28, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 23, "time": 0.209, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 23, "time": 0.239, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 24, "time": 0.223, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 30, "time": 0.243, "bad": [4, 0, 5], "ops": [2, 2, 7, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 27, "time": 0.163, "bad": [0, 0, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 23, "time": 0.155, "bad": [0, 0, 6], "ops": [1, 1, 8, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 24, "time": 0.246, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 20, "time": 0.162, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 20, "time": 0.193, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 20, "time": 0.183, "bad": [2, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 26, "time": 0.253, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 22, "time": 0.166, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 24, "time": 0.158, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 23, "time": 0.204, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 24, "time": 0.142, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 27, "time": 0.236, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 21, "time": 0.227, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 27, "time": 0.236, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 20, "time": 0.084, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 20, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.168, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 20, "time": 0.156, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 21, "time": 0.167, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 25, "time": 0.203, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 25, "time": 0.19, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 21, "time": 0.179, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 23, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 29, "time": 0.208, "bad": [4, 0, 0], "ops": [2, 2, 2, 4, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 23, "time": 0.195, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 24, "time": 0.207, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 21, "time": 0.18, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 25, "time": 0.169, "bad": [0, 0, 6], "ops": [1, 1, 7, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 20, "time": 0.128, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 22, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 23, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 25, "time": 0.105, "bad": [2, 0, 4], "ops": [2, 2, 8, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 23, "time": 0.154, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 30, "time": 0.137, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 21, "time": 0.131, "bad": [0, 0, 5], "ops": [1, 1, 7, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 27, "time": 0.215, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 25, "time": 0.178, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 18, "time": 0.117, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 32, "time": 0.218, "bad": [2, 0, 4], "ops": [2, 2, 7, 4, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 23, "time": 0.209, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 22, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 21, "time": 0.175, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 25, "time": 0.164, "bad": [0, 0, 5], "ops": [2, 2, 7, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 26, "time": 0.18, "bad": [0, 0, 4], "ops": [2, 2, 7, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 23, "time": 0.163, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 19, "time": 0.137, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 23, "time": 0.175, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 24, "time": 0.171, "bad": [0, 2, 0], "ops": [5, 3, 4, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 22, "time": 0.135, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 22, "time": 0.146, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 22, "time": 0.104, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 23, "time": 0.16, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 23, "time": 0.194, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 34, "time": 0.259, "bad": [2, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 24, "time": 0.162, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 19, "time": 0.169, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 24, "time": 0.166, "bad": [0, 0, 6], "ops": [2, 2, 9, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 20, "time": 0.146, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 26, "time": 0.212, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 24, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 23, "time": 0.197, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 20, "time": 0.146, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 34, "time": 0.268, "bad": [2, 0, 6], "ops": [3, 3, 8, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 24, "time": 0.209, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 25, "time": 0.189, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 22, "time": 0.203, "bad": [1, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 22, "time": 0.199, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 23, "time": 0.189, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 22, "time": 0.183, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 89, "n": 3, "success": true, "steps": 58, "time": 0.432, "bad": [6, 0, 0], "ops": [5, 5, 5, 4, 2]}, {"seed": 90, "n": 2, "success": true, "steps": 29, "time": 0.172, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 24, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 24, "time": 0.192, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 27, "time": 0.215, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 22, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 22, "time": 0.102, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 25, "time": 0.163, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 27, "time": 0.182, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 24, "time": 0.199, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 26, "time": 0.209, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_pipeline.txt b/stats_pipeline.txt
deleted file mode 100644
index 7c7e334..0000000
--- a/stats_pipeline.txt
+++ /dev/null
@@ -1,11 +0,0 @@
    1        -{'seed': 0, 'n': 3, 'success': True, 'steps': 28, 'time': 0.211, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    2        -{'seed': 10, 'n': 3, 'success': True, 'steps': 22, 'time': 0.212, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    3        -{'seed': 20, 'n': 3, 'success': True, 'steps': 27, 'time': 0.163, 'bad': [0, 0, 0], 'ops': [4, 3, 2, 2, 2]}
    4        -{'seed': 30, 'n': 1, 'success': True, 'steps': 24, 'time': 0.142, 'bad': [0, 0, 4], 'ops': [1, 1, 6, 2, 2]}
    5        -{'seed': 40, 'n': 2, 'success': True, 'steps': 25, 'time': 0.19, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    6        -{'seed': 50, 'n': 3, 'success': True, 'steps': 23, 'time': 0.168, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    7        -{'seed': 60, 'n': 1, 'success': True, 'steps': 22, 'time': 0.16, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
    8        -{'seed': 70, 'n': 2, 'success': True, 'steps': 22, 'time': 0.104, 'bad': [0, 1, 0], 'ops': [3, 2, 3, 2, 2]}
    9        -{'seed': 80, 'n': 3, 'success': True, 'steps': 23, 'time': 0.197, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
   10        -{'seed': 90, 'n': 2, 'success': True, 'steps': 29, 'time': 0.172, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
   11        -SUMMARY 100 100 mean 24.19 max_time 0.432
diff --git a/stats_planned.json b/stats_planned.json
deleted file mode 100644
index cbd360a..0000000
--- a/stats_planned.json
+++ /dev/null
@@ -1 +0,0 @@
    1        -[{"seed": 0, "n": 3, "success": true, "steps": 40, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 22, "time": 0.132, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 26, "time": 0.193, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 24, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 24, "time": 0.179, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 32, "time": 0.208, "bad": [2, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 27, "time": 0.186, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 26, "time": 0.194, "bad": [2, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 27, "time": 0.199, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 25, "time": 0.18, "bad": [0, 0, 2], "ops": [2, 2, 5, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 23, "time": 0.171, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 21, "time": 0.136, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 25, "time": 0.185, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 28, "time": 0.188, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 42, "time": 0.249, "bad": [0, 0, 3], "ops": [1, 1, 6, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 28, "time": 0.182, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 24, "time": 0.172, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 39, "time": 0.243, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 27, "time": 0.18, "bad": [2, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 29, "time": 0.199, "bad": [2, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 34, "time": 0.204, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 23, "time": 0.139, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 26, "time": 0.169, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 21, "time": 0.159, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 21, "time": 0.162, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 26, "time": 0.198, "bad": [2, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 28, "time": 0.194, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 23, "time": 0.122, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 25, "time": 0.146, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 24, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 27, "time": 0.176, "bad": [0, 0, 7], "ops": [1, 1, 9, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 30, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 22, "time": 0.182, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 28, "time": 0.155, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 23, "time": 0.18, "bad": [0, 0, 8], "ops": [1, 1, 11, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 21, "time": 0.167, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.157, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 21, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 22, "time": 0.16, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 30, "time": 0.182, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 28, "time": 0.206, "bad": [2, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 22, "time": 0.129, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 24, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 32, "time": 0.218, "bad": [4, 1, 0], "ops": [4, 2, 2, 4, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 24, "time": 0.172, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 25, "time": 0.188, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 23, "time": 0.191, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 24, "time": 0.164, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 21, "time": 0.14, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 23, "time": 0.178, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 39, "time": 0.248, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 28, "time": 0.193, "bad": [2, 0, 6], "ops": [2, 2, 10, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 31, "time": 0.23, "bad": [2, 0, 4], "ops": [3, 3, 8, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 32, "time": 0.213, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 22, "time": 0.159, "bad": [0, 0, 6], "ops": [1, 1, 8, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 33, "time": 0.205, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 26, "time": 0.153, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 19, "time": 0.139, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 33, "time": 0.15, "bad": [2, 0, 4], "ops": [2, 2, 7, 4, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 24, "time": 0.189, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 28, "time": 0.186, "bad": [2, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 22, "time": 0.167, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 26, "time": 0.161, "bad": [0, 0, 7], "ops": [2, 2, 9, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 30, "time": 0.173, "bad": [0, 0, 5], "ops": [2, 2, 8, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 26, "time": 0.185, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 20, "time": 0.129, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 24, "time": 0.177, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 25, "time": 0.134, "bad": [0, 2, 0], "ops": [5, 3, 4, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 25, "time": 0.108, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 29, "time": 0.151, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 23, "time": 0.178, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 30, "time": 0.177, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 25, "time": 0.19, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 34, "time": 0.189, "bad": [2, 1, 6], "ops": [5, 4, 9, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 23, "time": 0.129, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 20, "time": 0.12, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 26, "time": 0.168, "bad": [0, 0, 8], "ops": [2, 2, 11, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 21, "time": 0.128, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 27, "time": 0.119, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 26, "time": 0.161, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 28, "time": 0.203, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 21, "time": 0.136, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 34, "time": 0.229, "bad": [2, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 25, "time": 0.188, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 27, "time": 0.179, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 23, "time": 0.151, "bad": [1, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 23, "time": 0.183, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 29, "time": 0.193, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 24, "time": 0.169, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 89, "n": 3, "success": false, "steps": 200, "time": 4.042, "bad": [6, 0, 0], "ops": [5, 5, 4, 3, 1]}, {"seed": 90, "n": 2, "success": true, "steps": 30, "time": 0.167, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 25, "time": 0.154, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 25, "time": 0.163, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 29, "time": 0.22, "bad": [2, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 24, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 23, "time": 0.203, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 39, "time": 0.215, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 28, "time": 0.18, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 26, "time": 0.175, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 28, "time": 0.173, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_planned.txt b/stats_planned.txt
deleted file mode 100644
index c1fcaa5..0000000
--- a/stats_planned.txt
+++ /dev/null
@@ -1,12 +0,0 @@
    1        -{'seed': 0, 'n': 3, 'success': True, 'steps': 40, 'time': 0.233, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    2        -{'seed': 10, 'n': 3, 'success': True, 'steps': 23, 'time': 0.171, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    3        -{'seed': 20, 'n': 3, 'success': True, 'steps': 34, 'time': 0.204, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    4        -{'seed': 30, 'n': 1, 'success': True, 'steps': 27, 'time': 0.176, 'bad': [0, 0, 7], 'ops': [1, 1, 9, 2, 2]}
    5        -{'seed': 40, 'n': 2, 'success': True, 'steps': 28, 'time': 0.206, 'bad': [2, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    6        -{'seed': 50, 'n': 3, 'success': True, 'steps': 39, 'time': 0.248, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    7        -{'seed': 60, 'n': 1, 'success': True, 'steps': 28, 'time': 0.186, 'bad': [2, 0, 2], 'ops': [1, 1, 4, 2, 2]}
    8        -{'seed': 70, 'n': 2, 'success': True, 'steps': 23, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    9        -{'seed': 80, 'n': 3, 'success': True, 'steps': 28, 'time': 0.203, 'bad': [0, 1, 0], 'ops': [5, 4, 3, 2, 2]}
   10        -{'seed': 89, 'n': 3, 'success': False, 'steps': 200, 'time': 4.042, 'bad': [6, 0, 0], 'ops': [5, 5, 4, 3, 1]}
   11        -{'seed': 90, 'n': 2, 'success': True, 'steps': 30, 'time': 0.167, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
   12        -SUMMARY 99 100 mean 28.09 max_time 4.042
diff --git a/stats_planned2.json b/stats_planned2.json
deleted file mode 100644
index 379fd40..0000000
--- a/stats_planned2.json
+++ /dev/null
@@ -1 +0,0 @@
    1        -[{"seed": 0, "n": 3, "success": true, "steps": 32, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 22, "time": 0.171, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 23, "time": 0.184, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 24, "time": 0.189, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 24, "time": 0.176, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 26, "time": 0.143, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 23, "time": 0.155, "bad": [0, 0, 2], "ops": [2, 2, 5, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 26, "time": 0.177, "bad": [2, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 27, "time": 0.224, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 25, "time": 0.19, "bad": [0, 0, 2], "ops": [2, 2, 5, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 23, "time": 0.176, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 21, "time": 0.109, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 25, "time": 0.09, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 28, "time": 0.123, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 31, "time": 0.108, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 28, "time": 0.12, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 24, "time": 0.131, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 24, "time": 0.149, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 27, "time": 0.176, "bad": [2, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 29, "time": 0.184, "bad": [2, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 34, "time": 0.226, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 23, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 26, "time": 0.144, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 21, "time": 0.17, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 21, "time": 0.154, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 21, "time": 0.149, "bad": [2, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 28, "time": 0.217, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 23, "time": 0.16, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 25, "time": 0.15, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 24, "time": 0.158, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 27, "time": 0.183, "bad": [0, 0, 7], "ops": [1, 1, 9, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 28, "time": 0.196, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 22, "time": 0.149, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 28, "time": 0.14, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 21, "time": 0.085, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 21, "time": 0.089, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.135, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 21, "time": 0.124, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 22, "time": 0.121, "bad": [2, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 30, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 26, "time": 0.182, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 22, "time": 0.118, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 24, "time": 0.122, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 32, "time": 0.209, "bad": [4, 1, 0], "ops": [4, 2, 2, 4, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 24, "time": 0.178, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 25, "time": 0.197, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 23, "time": 0.147, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 24, "time": 0.161, "bad": [0, 0, 0], "ops": [1, 1, 1, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 21, "time": 0.145, "bad": [0, 0, 1], "ops": [1, 1, 4, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 23, "time": 0.162, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 24, "time": 0.147, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 28, "time": 0.165, "bad": [2, 0, 6], "ops": [2, 2, 10, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 25, "time": 0.146, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 32, "time": 0.197, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 22, "time": 0.16, "bad": [0, 0, 6], "ops": [1, 1, 8, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 33, "time": 0.21, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 26, "time": 0.172, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 19, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 33, "time": 0.209, "bad": [2, 0, 4], "ops": [2, 2, 7, 4, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 24, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 28, "time": 0.189, "bad": [2, 0, 2], "ops": [1, 1, 4, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 22, "time": 0.169, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 26, "time": 0.164, "bad": [0, 0, 7], "ops": [2, 2, 9, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 30, "time": 0.185, "bad": [0, 0, 5], "ops": [2, 2, 8, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 25, "time": 0.172, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 20, "time": 0.132, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 24, "time": 0.191, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 25, "time": 0.191, "bad": [0, 2, 0], "ops": [5, 3, 4, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 25, "time": 0.144, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 23, "time": 0.171, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 23, "time": 0.182, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 24, "time": 0.196, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 25, "time": 0.194, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 34, "time": 0.235, "bad": [2, 1, 6], "ops": [5, 4, 9, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 23, "time": 0.11, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 20, "time": 0.173, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 26, "time": 0.163, "bad": [0, 0, 8], "ops": [2, 2, 11, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 21, "time": 0.153, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 27, "time": 0.197, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 26, "time": 0.149, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 25, "time": 0.181, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 21, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 34, "time": 0.199, "bad": [2, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 25, "time": 0.145, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 27, "time": 0.186, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 23, "time": 0.17, "bad": [1, 1, 0], "ops": [4, 3, 4, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 23, "time": 0.195, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 24, "time": 0.156, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 24, "time": 0.171, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 89, "n": 3, "success": false, "steps": 200, "time": 4.43, "bad": [6, 0, 0], "ops": [5, 5, 4, 3, 1]}, {"seed": 90, "n": 2, "success": true, "steps": 30, "time": 0.173, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 25, "time": 0.188, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 25, "time": 0.18, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 30, "time": 0.199, "bad": [2, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 24, "time": 0.15, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 23, "time": 0.197, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 26, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 28, "time": 0.181, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 26, "time": 0.185, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 28, "time": 0.192, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_planned2.txt b/stats_planned2.txt
deleted file mode 100644
index 649db49..0000000
--- a/stats_planned2.txt
+++ /dev/null
@@ -1,12 +0,0 @@
    1        -{'seed': 0, 'n': 3, 'success': True, 'steps': 32, 'time': 0.185, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    2        -{'seed': 10, 'n': 3, 'success': True, 'steps': 23, 'time': 0.176, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    3        -{'seed': 20, 'n': 3, 'success': True, 'steps': 34, 'time': 0.226, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    4        -{'seed': 30, 'n': 1, 'success': True, 'steps': 27, 'time': 0.183, 'bad': [0, 0, 7], 'ops': [1, 1, 9, 2, 2]}
    5        -{'seed': 40, 'n': 2, 'success': True, 'steps': 26, 'time': 0.182, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    6        -{'seed': 50, 'n': 3, 'success': True, 'steps': 24, 'time': 0.147, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    7        -{'seed': 60, 'n': 1, 'success': True, 'steps': 28, 'time': 0.189, 'bad': [2, 0, 2], 'ops': [1, 1, 4, 2, 2]}
    8        -{'seed': 70, 'n': 2, 'success': True, 'steps': 23, 'time': 0.182, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    9        -{'seed': 80, 'n': 3, 'success': True, 'steps': 25, 'time': 0.181, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
   10        -{'seed': 89, 'n': 3, 'success': False, 'steps': 200, 'time': 4.43, 'bad': [6, 0, 0], 'ops': [5, 5, 4, 3, 1]}
   11        -{'seed': 90, 'n': 2, 'success': True, 'steps': 30, 'time': 0.173, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
   12        -SUMMARY 99 100 mean 26.97 max_time 4.43
diff --git a/stats_recovery.txt b/stats_recovery.txt
deleted file mode 100644
index b621d07..0000000
--- a/stats_recovery.txt
+++ /dev/null
@@ -1,11 +0,0 @@
    1        -{'seed': 600, 'n': 1, 'success': True, 'steps': 27, 'time': 0.102, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    2        -{'seed': 610, 'n': 2, 'success': True, 'steps': 22, 'time': 0.161, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    3        -{'seed': 620, 'n': 3, 'success': True, 'steps': 24, 'time': 0.191, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
    4        -{'seed': 630, 'n': 2, 'success': True, 'steps': 25, 'time': 0.153, 'bad': [0, 0, 0], 'ops': [2, 2, 4, 2, 2]}
    5        -{'seed': 640, 'n': 3, 'success': True, 'steps': 23, 'time': 0.212, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    6        -{'seed': 650, 'n': 3, 'success': True, 'steps': 24, 'time': 0.191, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    7        -{'seed': 660, 'n': 2, 'success': True, 'steps': 28, 'time': 0.213, 'bad': [0, 0, 0], 'ops': [2, 2, 3, 2, 2]}
    8        -{'seed': 670, 'n': 1, 'success': True, 'steps': 22, 'time': 0.154, 'bad': [0, 0, 0], 'ops': [1, 1, 3, 2, 2]}
    9        -{'seed': 680, 'n': 3, 'success': True, 'steps': 27, 'time': 0.151, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
   10        -{'seed': 690, 'n': 3, 'success': True, 'steps': 24, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
   11        -SUMMARY 100 100 mean 23.55 max_time 0.26
diff --git a/test_many.txt b/test_many.txt
deleted file mode 100644
index ed68f53..0000000
--- a/test_many.txt
+++ /dev/null
@@ -1,100 +0,0 @@
    1        -RESULT 1000 {'object_count': 4} True 31 1.739
    2        -RESULT 1001 {'object_count': 4} True 33 1.545
    3        -RESULT 1002 {'object_count': 4} True 26 1.307
    4        -RESULT 1003 {'object_count': 4} True 31 1.565
    5        -RESULT 1004 {'object_count': 4} True 31 1.403
    6        -RESULT 1005 {'object_count': 4} True 26 1.235
    7        -RESULT 1006 {'object_count': 4} True 30 1.668
    8        -RESULT 1007 {'object_count': 4} True 28 1.632
    9        -RESULT 1008 {'object_count': 4} True 31 1.951
   10        -RESULT 1009 {'object_count': 4} True 25 1.711
   11        -RESULT 1010 {'object_count': 4} True 40 2.848
   12        -RESULT 1011 {'object_count': 4} True 28 2.18
   13        -RESULT 1012 {'object_count': 4} True 34 1.981
   14        -RESULT 1013 {'object_count': 4} True 27 1.437
   15        -RESULT 1014 {'object_count': 4} True 29 1.946
   16        -RESULT 1015 {'object_count': 4} True 30 2.258
   17        -RESULT 1016 {'object_count': 4} True 31 2.827
   18        -RESULT 1017 {'object_count': 4} True 27 1.333
   19        -RESULT 1018 {'object_count': 4} True 33 1.189
   20        -RESULT 1019 {'object_count': 4} True 27 0.667
   21        -RESULT 1020 {'object_count': 4} True 25 1.11
   22        -RESULT 1021 {'object_count': 4} True 29 1.456
   23        -RESULT 1022 {'object_count': 4} True 29 1.239
   24        -RESULT 1023 {'object_count': 4} True 36 1.633
   25        -RESULT 1024 {'object_count': 4} True 29 1.218
   26        -RESULT 1025 {'object_count': 4} True 32 1.322
   27        -RESULT 1026 {'object_count': 4} True 29 1.187
   28        -RESULT 1027 {'object_count': 4} True 26 0.743
   29        -RESULT 1028 {'object_count': 4} True 42 1.501
   30        -RESULT 1029 {'object_count': 4} True 33 1.779
   31        -RESULT 1030 {'object_count': 4} True 32 1.654
   32        -RESULT 1031 {'object_count': 4} True 30 1.289
   33        -RESULT 1032 {'object_count': 4} True 31 1.158
   34        -RESULT 1033 {'object_count': 4} True 25 0.817
   35        -RESULT 1034 {'object_count': 4} True 32 1.37
   36        -RESULT 1035 {'object_count': 4} True 30 1.002
   37        -RESULT 1036 {'object_count': 4} True 31 1.031
   38        -RESULT 1037 {'object_count': 4} True 26 1.023
   39        -RESULT 1038 {'object_count': 4} True 26 1.144
   40        -RESULT 1039 {'object_count': 4} True 35 1.546
   41        -RESULT 1040 {'object_count': 4} True 28 1.006
   42        -RESULT 1041 {'object_count': 4} True 28 1.111
   43        -RESULT 1042 {'object_count': 4} True 33 1.342
   44        -RESULT 1043 {'object_count': 4} True 29 1.178
   45        -RESULT 1044 {'object_count': 4} True 26 1.189
   46        -RESULT 1045 {'object_count': 4} True 29 1.297
   47        -RESULT 1046 {'object_count': 4} True 26 0.904
   48        -RESULT 1047 {'object_count': 4} True 33 1.568
   49        -RESULT 1048 {'object_count': 4} True 27 1.129
   50        -RESULT 1049 {'object_count': 4} True 32 1.174
   51        -RESULT 1050 {'object_count': 4} True 29 0.886
   52        -RESULT 1051 {'object_count': 4} True 36 1.491
   53        -RESULT 1052 {'object_count': 4} True 39 1.194
   54        -RESULT 1053 {'object_count': 4} True 29 1.031
   55        -RESULT 1054 {'object_count': 4} True 28 1.298
   56        -RESULT 1055 {'object_count': 4} True 27 1.168
   57        -RESULT 1056 {'object_count': 4} True 37 1.421
   58        -RESULT 1057 {'object_count': 4} True 29 1.069
   59        -RESULT 1058 {'object_count': 4} True 39 3.17
   60        -RESULT 1059 {'object_count': 4} True 29 1.463
   61        -RESULT 1060 {'object_count': 4} True 29 2.188
   62        -RESULT 1061 {'object_count': 4} True 31 2.024
   63        -RESULT 1062 {'object_count': 4} True 28 1.644
   64        -RESULT 1063 {'object_count': 4} True 26 2.027
   65        -RESULT 1064 {'object_count': 4} True 39 2.745
   66        -RESULT 1065 {'object_count': 4} True 32 2.617
   67        -RESULT 1066 {'object_count': 4} True 28 2.739
   68        -RESULT 1067 {'object_count': 4} True 30 2.436
   69        -RESULT 1068 {'object_count': 4} True 27 1.846
   70        -RESULT 1069 {'object_count': 4} True 33 2.191
   71        -RESULT 1070 {'object_count': 4} True 30 2.156
   72        -RESULT 1071 {'object_count': 4} True 26 1.245
   73        -RESULT 1072 {'object_count': 4} True 32 1.927
   74        -RESULT 1073 {'object_count': 4} True 27 2.066
   75        -RESULT 1074 {'object_count': 4} True 33 1.913
   76        -RESULT 1075 {'object_count': 4} True 28 1.159
   77        -RESULT 1076 {'object_count': 4} True 33 1.312
   78        -RESULT 1077 {'object_count': 4} True 28 1.181
   79        -RESULT 1078 {'object_count': 4} True 29 1.2
   80        -RESULT 1079 {'object_count': 4} True 33 1.112
   81        -RESULT 1080 {'object_count': 4} True 27 0.985
   82        -RESULT 1081 {'object_count': 4} True 29 1.06
   83        -RESULT 1082 {'object_count': 4} True 27 1.198
   84        -RESULT 1083 {'object_count': 4} True 31 1.61
   85        -RESULT 1084 {'object_count': 4} True 27 1.241
   86        -RESULT 1085 {'object_count': 4} True 32 1.326
   87        -RESULT 1086 {'object_count': 4} True 27 0.963
   88        -RESULT 1087 {'object_count': 4} True 32 1.188
   89        -RESULT 1088 {'object_count': 4} True 24 1.059
   90        -RESULT 1089 {'object_count': 4} True 26 0.833
   91        -RESULT 1090 {'object_count': 4} True 28 1.208
   92        -RESULT 1091 {'object_count': 4} True 27 0.954
   93        -RESULT 1092 {'object_count': 4} True 28 1.118
   94        -RESULT 1093 {'object_count': 4} True 35 1.145
   95        -RESULT 1094 {'object_count': 4} True 28 0.904
   96        -RESULT 1095 {'object_count': 4} True 34 1.315
   97        -RESULT 1096 {'object_count': 4} True 34 1.127
   98        -RESULT 1097 {'object_count': 4} True 28 0.811
   99        -RESULT 1098 {'object_count': 4} True 33 1.101
  100        -RESULT 1099 {'object_count': 4} True 36 1.082
diff --git a/test_refined.txt b/test_refined.txt
deleted file mode 100644
index 7b5e3a7..0000000
--- a/test_refined.txt
+++ /dev/null
@@ -1,100 +0,0 @@
    1        -RESULT 0 {'object_count': 3} True 36 2.5
    2        -RESULT 1 {'object_count': 2} True 22 1.041
    3        -RESULT 2 {'object_count': 3} True 22 1.062
    4        -RESULT 3 {'object_count': 3} True 36 1.911
    5        -RESULT 4 {'object_count': 3} True 25 1.362
    6        -RESULT 5 {'object_count': 3} True 38 1.79
    7        -RESULT 6 {'object_count': 2} True 26 1.049
    8        -RESULT 7 {'object_count': 3} True 32 1.281
    9        -RESULT 8 {'object_count': 3} True 24 1.222
   10        -RESULT 9 {'object_count': 2} True 29 1.167
   11        -RESULT 10 {'object_count': 3} True 25 1.169
   12        -RESULT 11 {'object_count': 1} True 21 0.992
   13        -RESULT 12 {'object_count': 2} True 26 1.752
   14        -RESULT 13 {'object_count': 3} True 30 2.0
   15        -RESULT 14 {'object_count': 1} True 34 1.552
   16        -RESULT 15 {'object_count': 3} True 29 1.514
   17        -RESULT 16 {'object_count': 2} True 26 1.382
   18        -RESULT 17 {'object_count': 3} True 33 1.73
   19        -RESULT 18 {'object_count': 3} True 27 1.328
   20        -RESULT 19 {'object_count': 2} True 30 1.563
   21        -RESULT 20 {'object_count': 3} True 33 1.949
   22        -RESULT 21 {'object_count': 1} True 23 1.962
   23        -RESULT 22 {'object_count': 3} True 28 2.07
   24        -RESULT 23 {'object_count': 1} True 19 1.207
   25        -RESULT 24 {'object_count': 2} True 26 1.816
   26        -RESULT 25 {'object_count': 2} True 23 1.446
   27        -RESULT 26 {'object_count': 3} True 31 1.648
   28        -RESULT 27 {'object_count': 1} True 24 1.176
   29        -RESULT 28 {'object_count': 2} True 42 3.474
   30        -RESULT 29 {'object_count': 3} True 25 2.071
   31        -RESULT 30 {'object_count': 1} True 22 1.438
   32        -RESULT 31 {'object_count': 2} True 29 1.847
   33        -RESULT 32 {'object_count': 3} True 28 1.38
   34        -RESULT 33 {'object_count': 3} True 34 1.813
   35        -RESULT 34 {'object_count': 1} True 21 0.518
   36        -RESULT 35 {'object_count': 1} True 22 0.542
   37        -RESULT 36 {'object_count': 2} True 21 0.937
   38        -RESULT 37 {'object_count': 1} True 23 0.92
   39        -RESULT 38 {'object_count': 1} True 22 0.449
   40        -RESULT 39 {'object_count': 3} True 32 1.309
   41        -RESULT 40 {'object_count': 2} True 29 1.087
   42        -RESULT 41 {'object_count': 2} True 21 1.041
   43        -RESULT 42 {'object_count': 1} True 28 0.88
   44        -RESULT 43 {'object_count': 2} True 34 1.224
   45        -RESULT 44 {'object_count': 3} True 24 0.595
   46        -RESULT 45 {'object_count': 3} True 29 1.218
   47        -RESULT 46 {'object_count': 2} True 24 1.584
   48        -RESULT 47 {'object_count': 1} True 26 1.292
   49        -RESULT 48 {'object_count': 1} True 21 0.576
   50        -RESULT 49 {'object_count': 1} True 42 1.431
   51        -RESULT 50 {'object_count': 3} True 28 1.212
   52        -RESULT 51 {'object_count': 2} True 23 1.149
   53        -RESULT 52 {'object_count': 3} True 27 1.267
   54        -RESULT 53 {'object_count': 3} True 26 0.64
   55        -RESULT 54 {'object_count': 1} True 21 0.575
   56        -RESULT 55 {'object_count': 3} True 29 1.279
   57        -RESULT 56 {'object_count': 2} True 28 1.159
   58        -RESULT 57 {'object_count': 1} True 18 0.49
   59        -RESULT 58 {'object_count': 2} True 33 0.862
   60        -RESULT 59 {'object_count': 3} True 24 1.097
   61        -RESULT 60 {'object_count': 1} True 28 0.951
   62        -RESULT 61 {'object_count': 2} True 25 0.673
   63        -RESULT 62 {'object_count': 2} True 27 0.594
   64        -RESULT 63 {'object_count': 2} True 30 0.91
   65        -RESULT 64 {'object_count': 2} True 27 0.997
   66        -RESULT 65 {'object_count': 1} True 20 0.852
   67        -RESULT 66 {'object_count': 3} True 27 1.079
   68        -RESULT 67 {'object_count': 3} True 25 0.486
   69        -RESULT 68 {'object_count': 2} True 25 1.04
   70        -RESULT 69 {'object_count': 1} True 24 1.172
   71        -RESULT 70 {'object_count': 2} True 25 0.989
   72        -RESULT 71 {'object_count': 3} True 26 1.007
   73        -RESULT 72 {'object_count': 3} True 30 0.701
   74        -RESULT 73 {'object_count': 3} True 24 0.907
   75        -RESULT 74 {'object_count': 1} True 24 1.082
   76        -RESULT 75 {'object_count': 2} True 24 1.036
   77        -RESULT 76 {'object_count': 2} True 27 1.18
   78        -RESULT 77 {'object_count': 1} True 23 0.508
   79        -RESULT 78 {'object_count': 3} True 27 1.111
   80        -RESULT 79 {'object_count': 1} True 32 1.215
   81        -RESULT 80 {'object_count': 3} True 28 1.194
   82        -RESULT 81 {'object_count': 1} True 24 1.588
   83        -RESULT 82 {'object_count': 3} True 32 1.635
   84        -RESULT 83 {'object_count': 3} True 27 2.003
   85        -RESULT 84 {'object_count': 2} True 27 2.134
   86        -RESULT 85 {'object_count': 3} True 23 1.459
   87        -RESULT 86 {'object_count': 3} True 23 1.577
   88        -RESULT 87 {'object_count': 2} True 33 2.287
   89        -RESULT 88 {'object_count': 2} True 24 1.429
   90        -RESULT 89 {'object_count': 3} True 37 3.407
   91        -RESULT 90 {'object_count': 2} True 31 2.851
   92        -RESULT 91 {'object_count': 3} True 30 2.424
   93        -RESULT 92 {'object_count': 2} True 26 2.167
   94        -RESULT 93 {'object_count': 3} True 30 2.011
   95        -RESULT 94 {'object_count': 1} True 25 1.403
   96        -RESULT 95 {'object_count': 2} True 24 1.842
   97        -RESULT 96 {'object_count': 3} True 32 2.013
   98        -RESULT 97 {'object_count': 1} True 47 2.412
   99        -RESULT 98 {'object_count': 2} True 25 1.781
  100        -RESULT 99 {'object_count': 3} True 31 2.06
diff --git a/test_results.txt b/test_results.txt
deleted file mode 100644
index 3ffde72..0000000
--- a/test_results.txt
+++ /dev/null
@@ -1,31 +0,0 @@
    1        -RESULT 0 {'object_count': 3} True 35 0.459
    2        -RESULT 1 {'object_count': 2} True 22 0.304
    3        -RESULT 2 {'object_count': 3} True 22 0.231
    4        -RESULT 3 {'object_count': 3} True 30 0.413
    5        -RESULT 4 {'object_count': 3} True 25 0.399
    6        -RESULT 5 {'object_count': 3} True 41 0.625
    7        -RESULT 6 {'object_count': 2} True 21 0.251
    8        -RESULT 7 {'object_count': 3} True 32 0.338
    9        -RESULT 8 {'object_count': 3} True 29 0.427
   10        -RESULT 9 {'object_count': 2} True 29 0.476
   11        -RESULT 10 {'object_count': 3} True 28 0.408
   12        -RESULT 11 {'object_count': 1} True 21 0.308
   13        -RESULT 12 {'object_count': 2} True 27 0.252
   14        -RESULT 13 {'object_count': 3} True 36 0.492
   15        -RESULT 14 {'object_count': 1} True 34 0.432
   16        -RESULT 15 {'object_count': 3} True 25 0.331
   17        -RESULT 16 {'object_count': 2} True 26 0.347
   18        -RESULT 17 {'object_count': 3} True 32 0.489
   19        -RESULT 18 {'object_count': 3} True 25 0.37
   20        -RESULT 19 {'object_count': 2} True 30 0.431
   21        -RESULT 20 {'object_count': 3} True 30 0.19
   22        -RESULT 21 {'object_count': 1} True 23 0.402
   23        -RESULT 22 {'object_count': 3} True 26 0.304
   24        -RESULT 23 {'object_count': 1} True 19 0.237
   25        -RESULT 24 {'object_count': 2} True 26 0.357
   26        -RESULT 25 {'object_count': 2} True 23 0.3
   27        -RESULT 26 {'object_count': 3} True 28 0.43
   28        -RESULT 27 {'object_count': 1} True 24 0.32
   29        -RESULT 28 {'object_count': 2} True 44 0.502
   30        -RESULT 29 {'object_count': 3} False 250 5.23
   31        -FAILED [('home', 0), ('sample', 4)] [('rover0', {'x': 1.0, 'y': -1.75, 'theta': -3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}), ('rover1', {'x': -2.0, 'y': -1.399999976158142, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 0.0}), ('objective0', {'x': -0.5211005806922913, 'y': 2.0225868225097656, 'z': 0.20100000500679016, 'have_image_rover0': 1.0, 'have_image_rover1': 0.0, 'received_image': 1.0}), ('objective1', {'x': -1.959802269935608, 'y': 2.032264471054077, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}), ('objective2', {'x': 0.5849767923355103, 'y': 1.883683443069458, 'z': 0.20100000500679016, 'have_image_rover0': 1.0, 'have_image_rover1': 0.0, 'received_image': 1.0}), ('sample0', {'x': 0.7705432772636414, 'y': 0.23597754538059235, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample1', {'x': 1.6593462228775024, 'y': -0.3176131248474121, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 1.0, 'analyzed_rover1': 0.0, 'received_analysis': 1.0}), ('sample2', {'x': 2.14742112159729, 'y': 1.3751660585403442, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample3', {'x': -1.9218065738677979, 'y': 0.9597395658493042, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample4', {'x': -2.344602584838867, 'y': -1.656410813331604, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample5', {'x': 0.237486332654953, 'y': -0.09099745005369186, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0})]
diff --git a/test_results_more.txt b/test_results_more.txt
deleted file mode 100644
index 30cf7eb..0000000
--- a/test_results_more.txt
+++ /dev/null
@@ -1,101 +0,0 @@
    1        -RESULT 29 {'object_count': 3} True 34 0.645
    2        -RESULT 30 {'object_count': 1} True 22 0.367
    3        -RESULT 31 {'object_count': 2} True 32 0.92
    4        -RESULT 32 {'object_count': 3} True 28 0.923
    5        -RESULT 33 {'object_count': 3} True 34 1.012
    6        -RESULT 34 {'object_count': 1} True 21 0.805
    7        -RESULT 35 {'object_count': 1} True 21 0.9
    8        -RESULT 36 {'object_count': 2} True 22 0.801
    9        -RESULT 37 {'object_count': 1} True 24 0.919
   10        -RESULT 38 {'object_count': 1} True 22 0.422
   11        -RESULT 39 {'object_count': 3} True 27 0.871
   12        -RESULT 40 {'object_count': 2} True 34 0.591
   13        -RESULT 41 {'object_count': 2} True 21 0.834
   14        -RESULT 42 {'object_count': 1} True 28 0.543
   15        -RESULT 43 {'object_count': 2} True 34 0.85
   16        -RESULT 44 {'object_count': 3} True 24 0.828
   17        -RESULT 45 {'object_count': 3} True 30 1.27
   18        -RESULT 46 {'object_count': 2} True 23 0.767
   19        -RESULT 47 {'object_count': 1} True 26 1.056
   20        -RESULT 48 {'object_count': 1} True 21 0.649
   21        -RESULT 49 {'object_count': 1} True 38 1.174
   22        -RESULT 50 {'object_count': 3} True 30 0.638
   23        -RESULT 51 {'object_count': 2} True 23 0.428
   24        -RESULT 52 {'object_count': 3} True 28 0.851
   25        -RESULT 53 {'object_count': 3} True 25 0.466
   26        -RESULT 54 {'object_count': 1} True 22 0.488
   27        -RESULT 55 {'object_count': 3} True 29 0.498
   28        -RESULT 56 {'object_count': 2} True 27 0.372
   29        -RESULT 57 {'object_count': 1} True 19 0.257
   30        -RESULT 58 {'object_count': 2} True 30 0.416
   31        -RESULT 59 {'object_count': 3} True 27 0.353
   32        -RESULT 60 {'object_count': 1} True 23 0.309
   33        -RESULT 61 {'object_count': 2} True 27 0.386
   34        -RESULT 62 {'object_count': 2} True 29 0.406
   35        -RESULT 63 {'object_count': 2} True 30 0.426
   36        -RESULT 64 {'object_count': 2} True 27 0.362
   37        -RESULT 65 {'object_count': 1} True 20 0.276
   38        -RESULT 66 {'object_count': 3} True 27 0.445
   39        -RESULT 67 {'object_count': 3} True 25 0.357
   40        -RESULT 68 {'object_count': 2} True 25 0.346
   41        -RESULT 69 {'object_count': 1} True 29 0.406
   42        -RESULT 70 {'object_count': 2} True 25 0.36
   43        -RESULT 71 {'object_count': 3} True 31 0.434
   44        -RESULT 72 {'object_count': 3} True 29 0.413
   45        -RESULT 73 {'object_count': 3} True 24 0.367
   46        -RESULT 74 {'object_count': 1} True 23 0.302
   47        -RESULT 75 {'object_count': 2} True 26 0.357
   48        -RESULT 76 {'object_count': 2} True 27 0.384
   49        -RESULT 77 {'object_count': 1} True 23 0.31
   50        -RESULT 78 {'object_count': 3} True 27 0.398
   51        -RESULT 79 {'object_count': 1} True 35 0.465
   52        -RESULT 80 {'object_count': 3} True 26 0.397
   53        -RESULT 81 {'object_count': 1} True 23 0.354
   54        -RESULT 82 {'object_count': 3} True 32 0.487
   55        -RESULT 83 {'object_count': 3} True 28 0.431
   56        -RESULT 84 {'object_count': 2} True 26 0.59
   57        -RESULT 85 {'object_count': 3} True 23 0.528
   58        -RESULT 86 {'object_count': 3} True 23 0.487
   59        -RESULT 87 {'object_count': 2} True 35 1.007
   60        -RESULT 88 {'object_count': 2} True 25 0.507
   61        -RESULT 89 {'object_count': 3} True 37 0.726
   62        -RESULT 90 {'object_count': 2} True 32 0.393
   63        -RESULT 91 {'object_count': 3} True 30 0.385
   64        -RESULT 92 {'object_count': 2} True 25 0.298
   65        -RESULT 93 {'object_count': 3} True 30 0.406
   66        -RESULT 94 {'object_count': 1} True 24 0.673
   67        -RESULT 95 {'object_count': 2} True 25 0.995
   68        -RESULT 96 {'object_count': 3} True 32 1.2
   69        -RESULT 97 {'object_count': 1} True 49 2.105
   70        -RESULT 98 {'object_count': 2} True 25 1.228
   71        -RESULT 99 {'object_count': 3} True 28 1.095
   72        -RESULT 100 {'object_count': 3} True 37 1.394
   73        -RESULT 101 {'object_count': 1} True 23 1.671
   74        -RESULT 102 {'object_count': 2} True 27 1.291
   75        -RESULT 103 {'object_count': 2} True 26 1.465
   76        -RESULT 104 {'object_count': 3} True 25 1.166
   77        -RESULT 105 {'object_count': 1} True 25 0.97
   78        -RESULT 106 {'object_count': 2} True 23 1.046
   79        -RESULT 107 {'object_count': 1} True 23 1.081
   80        -RESULT 108 {'object_count': 1} True 22 1.106
   81        -RESULT 109 {'object_count': 2} True 26 0.967
   82        -RESULT 110 {'object_count': 2} True 24 0.955
   83        -RESULT 111 {'object_count': 2} True 23 1.196
   84        -RESULT 112 {'object_count': 1} True 29 1.045
   85        -RESULT 113 {'object_count': 1} True 24 1.129
   86        -RESULT 114 {'object_count': 1} True 29 1.097
   87        -RESULT 115 {'object_count': 2} True 31 1.352
   88        -RESULT 116 {'object_count': 1} False 250 13.889
   89        -FAILED [('home', 0), ('sample', 5)] [('rover0', {'x': 1.0, 'y': -1.75, 'theta': -3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}), ('rover1', {'x': -1.5, 'y': 0.3999998867511749, 'theta': 0.0, 'store_full': 1.0, 'calibrated': 0.0, 'at_home': 0.0}), ('objective0', {'x': 0.3243560194969177, 'y': 1.8972790241241455, 'z': 0.20100000500679016, 'have_image_rover0': 1.0, 'have_image_rover1': 0.0, 'received_image': 1.0}), ('sample0', {'x': -0.9633942246437073, 'y': -2.3797810077667236, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 1.0, 'received_analysis': 1.0}), ('sample1', {'x': -1.9395066499710083, 'y': -0.37688443064689636, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample2', {'x': -1.3768526315689087, 'y': 0.30743154883384705, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 1.0, 'received_analysis': 0.0}), ('sample3', {'x': -1.8997358083724976, 'y': 1.3095738887786865, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample4', {'x': -0.1688850373029709, 'y': 1.3331273794174194, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}), ('sample5', {'x': -1.4924739599227905, 'y': 0.6196938753128052, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0})]
   90        -RESULT 117 {'object_count': 1} True 33 2.036
   91        -RESULT 118 {'object_count': 2} True 30 1.838
   92        -RESULT 119 {'object_count': 2} True 22 1.861
   93        -RESULT 120 {'object_count': 1} True 24 1.882
   94        -RESULT 121 {'object_count': 1} True 22 1.418
   95        -RESULT 122 {'object_count': 3} True 26 1.122
   96        -RESULT 123 {'object_count': 1} True 30 2.132
   97        -RESULT 124 {'object_count': 3} True 28 2.825
   98        -RESULT 125 {'object_count': 2} True 23 1.838
   99        -RESULT 126 {'object_count': 1} True 22 2.261
  100        -RESULT 127 {'object_count': 2} True 35 2.355
  101        -RESULT 128 {'object_count': 3} True 36 1.905
diff --git a/test_stats.py b/test_stats.py
index 6e15b72..2601c23 100644
--- a/test_stats.py
+++ b/test_stats.py
@@ -2,9 +2,7 @@ from env_client import make_env
    2      2  from approach import GeneratedApproach
    3      3  import numpy as np
    4      4  import time,json,argparse
    5        -P=argparse.ArgumentParser();P.add_argument('--no-plan',action='store_true');P.add_argument('--start',type=int,default=0);P.add_argument('--n',type=int,default=100);P.add_argument('--count',type=int);P.add_argument('--out',default='stats.json');a=P.parse_args();out=[]
    6        -if a.no_plan:
    7        - from approach_no_plan import GeneratedApproach
           5 +P=argparse.ArgumentParser();P.add_argument('--start',type=int,default=0);P.add_argument('--n',type=int,default=100);P.add_argument('--count',type=int);P.add_argument('--out',default='stats.json');a=P.parse_args();out=[]
    8      6  for seed in range(a.start,a.start+a.n):
    9      7   e=make_env();s,info=e.reset(seed=seed,options={'object_count':a.count} if a.count else None);ap=GeneratedApproach(e.action_space,e.observation_space,{});st=time.time();ap.reset(s,info);tm=time.time()-st
   10      8   bad=[0,0,0];ops=[0,0,0,0,0];success=False
```

</details>

<a id="C036"></a>
### C036 · Try nearby radio alternatives before revisiting a distant confirmed location

Commit `59cede108d9b8ec993ea1bcbee23185ea28a15dd`; parents: 2e041446fb4c20abbfb43617f36c0d85d060e7b8. Recorded author date: 2026-09-21T22:41:31+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0200](01_timeline.md#E0200): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C036_59cede1_approach.py) · [Exact all-file diff](evidence/diffs/C036_59cede1.diff)

[Previous saved controller snapshot](evidence/versions/C032_adfe956_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d34eb20..b224337 100644
--- a/approach.py
+++ b/approach.py
@@ -47,6 +47,7 @@ class GeneratedApproach:
   47     47          self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
   48     48          self.masks[('send',1)] = self.masks[('send',0)].copy()
   49     49          self.good_radio = [[],[]]
          50 +        self.radio_failures = [0,0]
   50     51          self.tasks = [None,None]
   51     52          self.paths = [[],[]]
   52     53          self.previous = [None,None]
@@ -167,11 +168,7 @@ class GeneratedApproach:
  167    168              if self.pending(s,r) and s.get(self.rovers[r],'at_home')>.5:
  168    169                  best=('send',r)
  169    170                  mask=self.masks[best]
  170        -                if self.good_radio[r]:
  171        -                    known=np.zeros(len(self.points),dtype=bool)
  172        -                    for point in self.good_radio[r]:known |= np.linalg.norm(self.points-point,axis=1)<.075
  173        -                    pp,cost=self.route(p,known & self.free,other)
  174        -                    if cost<1e5:mask=known & self.free
         171 +                self.radio_failures[r]=0
  175    172                  self.masks[best]=mask
  176    173                  path,_=self.route(p,mask,other)
  177    174              else:
@@ -196,6 +193,15 @@ class GeneratedApproach:
  196    193          task=self.tasks[r]
  197    194          kind,k=task
  198    195          mask=(np.linalg.norm(self.points-self.home[r],axis=1)<.24) if kind=='home' else self.masks[task]
         196 +        if kind=='send' and self.radio_failures[r]>=3 and self.good_radio[r]:
         197 +            known=np.zeros(len(self.points),dtype=bool)
         198 +            for point in self.good_radio[r]:known |= np.linalg.norm(self.points-point,axis=1)<.075
         199 +            known &= self.free
         200 +            for failed in self.rejected_views.get(task,[]):
         201 +                known &= np.linalg.norm(self.points-failed,axis=1)>.085
         202 +            if np.any(known):
         203 +                mask=known
         204 +                self.masks[task]=mask
  199    205          path,_=self.route(p,mask,other)
  200    206          if kind in ('image','send') and (explore or not path):
  201    207              # If the conservative sight model runs out of positions, use
@@ -236,6 +242,7 @@ class GeneratedApproach:
  236    242                            (old_task[0]=='image' and old_op == -1/6 and self.result_count(s,r)<=old_count) or
  237    243                            (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
  238    244                  if failed and at_goal and task==old_task and task[0] in ('image','send'):
         245 +                    if task[0]=='send':self.radio_failures[r]+=1
  239    246                      self.rejected_views.setdefault(task,[]).append(p.copy())
  240    247                      self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>(.085 if task in self.loose_views else .22)
  241    248                      self.replan(s,r,p,pos[1-r])
diff --git a/stats_final_latest.json b/stats_final_latest.json
new file mode 100644
index 0000000..8139e59
--- /dev/null
+++ b/stats_final_latest.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "n": 3, "success": true, "steps": 28, "time": 0.196, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 21, "time": 0.21, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 21, "time": 0.226, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 24, "time": 0.188, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 23, "time": 0.213, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 25, "time": 0.214, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 21, "time": 0.147, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 24, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 26, "time": 0.136, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 24, "time": 0.23, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 22, "time": 0.194, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 20, "time": 0.137, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 24, "time": 0.202, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 28, "time": 0.293, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 31, "time": 0.172, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 27, "time": 0.293, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 23, "time": 0.167, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 26, "time": 0.244, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 24, "time": 0.23, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 31, "time": 0.271, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 27, "time": 0.266, "bad": [0, 0, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 23, "time": 0.136, "bad": [0, 0, 7], "ops": [1, 1, 8, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 24, "time": 0.213, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 18, "time": 0.105, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 20, "time": 0.214, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 20, "time": 0.208, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 26, "time": 0.245, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 22, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 24, "time": 0.135, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 23, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 34, "time": 0.24, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 27, "time": 0.242, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 21, "time": 0.139, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 27, "time": 0.202, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 20, "time": 0.145, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 20, "time": 0.143, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.162, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 20, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 21, "time": 0.192, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 25, "time": 0.242, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 25, "time": 0.201, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 21, "time": 0.198, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 23, "time": 0.199, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 27, "time": 0.237, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 23, "time": 0.221, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 24, "time": 0.244, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 21, "time": 0.203, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 25, "time": 0.208, "bad": [0, 0, 6], "ops": [1, 1, 7, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 20, "time": 0.162, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 22, "time": 0.208, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 24, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 22, "time": 0.16, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 23, "time": 0.247, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 30, "time": 0.285, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 21, "time": 0.172, "bad": [0, 0, 5], "ops": [1, 1, 7, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 27, "time": 0.243, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 25, "time": 0.198, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 18, "time": 0.161, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 26, "time": 0.203, "bad": [0, 0, 2], "ops": [2, 2, 4, 2, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 23, "time": 0.237, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 22, "time": 0.138, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 21, "time": 0.2, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 25, "time": 0.178, "bad": [0, 0, 5], "ops": [2, 2, 7, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 26, "time": 0.209, "bad": [0, 0, 4], "ops": [2, 2, 7, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 23, "time": 0.189, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 19, "time": 0.152, "bad": [0, 0, 2], "ops": [1, 1, 5, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 23, "time": 0.202, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 24, "time": 0.201, "bad": [0, 2, 0], "ops": [5, 3, 4, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 22, "time": 0.164, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 23, "time": 0.127, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 22, "time": 0.135, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 23, "time": 0.234, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 23, "time": 0.235, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 26, "time": 0.232, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 34, "time": 0.242, "bad": [0, 0, 11], "ops": [1, 1, 14, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 19, "time": 0.135, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 24, "time": 0.183, "bad": [0, 0, 6], "ops": [2, 2, 9, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 20, "time": 0.181, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 26, "time": 0.226, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 24, "time": 0.178, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 23, "time": 0.173, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 20, "time": 0.162, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 25, "time": 0.24, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 24, "time": 0.174, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 25, "time": 0.125, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 22, "time": 0.178, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 22, "time": 0.212, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 23, "time": 0.162, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 22, "time": 0.155, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 89, "n": 3, "success": true, "steps": 31, "time": 0.246, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 90, "n": 2, "success": true, "steps": 29, "time": 0.173, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 24, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 24, "time": 0.223, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 27, "time": 0.151, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 22, "time": 0.116, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 22, "time": 0.205, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 25, "time": 0.303, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 27, "time": 0.202, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 24, "time": 0.171, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 27, "time": 0.211, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_final_latest.txt b/stats_final_latest.txt
index 6c09e4a..5e4837f 100644
--- a/stats_final_latest.txt
+++ b/stats_final_latest.txt
@@ -6,3 +6,6 @@
    6      6  {'seed': 50, 'n': 3, 'success': True, 'steps': 24, 'time': 0.233, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    7      7  {'seed': 60, 'n': 1, 'success': True, 'steps': 22, 'time': 0.138, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
    8      8  {'seed': 70, 'n': 2, 'success': True, 'steps': 22, 'time': 0.135, 'bad': [0, 1, 0], 'ops': [3, 2, 3, 2, 2]}
           9 +{'seed': 80, 'n': 3, 'success': True, 'steps': 23, 'time': 0.173, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
          10 +{'seed': 90, 'n': 2, 'success': True, 'steps': 29, 'time': 0.173, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
          11 +SUMMARY 100 100 mean 23.83 max_time 0.303
diff --git a/stats_final_latest4.json b/stats_final_latest4.json
new file mode 100644
index 0000000..34ef00b
--- /dev/null
+++ b/stats_final_latest4.json
@@ -0,0 +1 @@
           1 +[{"seed": 1200, "n": 4, "success": true, "steps": 26, "time": 0.164, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1201, "n": 4, "success": true, "steps": 26, "time": 0.268, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1202, "n": 4, "success": true, "steps": 29, "time": 0.253, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1203, "n": 4, "success": true, "steps": 27, "time": 0.204, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1204, "n": 4, "success": true, "steps": 26, "time": 0.272, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1205, "n": 4, "success": true, "steps": 32, "time": 0.278, "bad": [0, 1, 0], "ops": [6, 5, 4, 2, 2]}, {"seed": 1206, "n": 4, "success": true, "steps": 25, "time": 0.235, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1207, "n": 4, "success": true, "steps": 22, "time": 0.208, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1208, "n": 4, "success": true, "steps": 30, "time": 0.321, "bad": [0, 1, 1], "ops": [5, 4, 3, 2, 2]}, {"seed": 1209, "n": 4, "success": true, "steps": 24, "time": 0.237, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1210, "n": 4, "success": true, "steps": 24, "time": 0.253, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1211, "n": 4, "success": true, "steps": 24, "time": 0.269, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1212, "n": 4, "success": true, "steps": 37, "time": 0.317, "bad": [0, 0, 13], "ops": [4, 4, 16, 2, 2]}, {"seed": 1213, "n": 4, "success": true, "steps": 27, "time": 0.197, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1214, "n": 4, "success": true, "steps": 26, "time": 0.237, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1215, "n": 4, "success": true, "steps": 24, "time": 0.25, "bad": [0, 1, 0], "ops": [5, 4, 2, 2, 2]}, {"seed": 1216, "n": 4, "success": true, "steps": 24, "time": 0.229, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1217, "n": 4, "success": true, "steps": 28, "time": 0.259, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1218, "n": 4, "success": true, "steps": 26, "time": 0.258, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1219, "n": 4, "success": true, "steps": 29, "time": 0.273, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1220, "n": 4, "success": true, "steps": 23, "time": 0.201, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1221, "n": 4, "success": true, "steps": 30, "time": 0.292, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1222, "n": 4, "success": true, "steps": 29, "time": 0.252, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1223, "n": 4, "success": true, "steps": 29, "time": 0.262, "bad": [0, 0, 0], "ops": [5, 5, 5, 2, 2]}, {"seed": 1224, "n": 4, "success": true, "steps": 24, "time": 0.249, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1225, "n": 4, "success": true, "steps": 24, "time": 0.228, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1226, "n": 4, "success": true, "steps": 29, "time": 0.239, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1227, "n": 4, "success": true, "steps": 24, "time": 0.189, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1228, "n": 4, "success": true, "steps": 25, "time": 0.169, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1229, "n": 4, "success": true, "steps": 30, "time": 0.309, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1230, "n": 4, "success": true, "steps": 29, "time": 0.261, "bad": [0, 1, 0], "ops": [5, 4, 4, 2, 2]}, {"seed": 1231, "n": 4, "success": true, "steps": 45, "time": 0.412, "bad": [0, 0, 12], "ops": [5, 5, 17, 2, 2]}, {"seed": 1232, "n": 4, "success": true, "steps": 26, "time": 0.303, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1233, "n": 4, "success": true, "steps": 27, "time": 0.246, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1234, "n": 4, "success": true, "steps": 27, "time": 0.187, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1235, "n": 4, "success": true, "steps": 25, "time": 0.238, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1236, "n": 4, "success": true, "steps": 26, "time": 0.284, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1237, "n": 4, "success": true, "steps": 28, "time": 0.272, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1238, "n": 4, "success": true, "steps": 31, "time": 0.286, "bad": [0, 0, 0], "ops": [6, 6, 5, 2, 2]}, {"seed": 1239, "n": 4, "success": true, "steps": 25, "time": 0.255, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1240, "n": 4, "success": true, "steps": 26, "time": 0.245, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1241, "n": 4, "success": true, "steps": 28, "time": 0.235, "bad": [0, 0, 2], "ops": [6, 6, 6, 2, 2]}, {"seed": 1242, "n": 4, "success": true, "steps": 25, "time": 0.238, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1243, "n": 4, "success": true, "steps": 27, "time": 0.303, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1244, "n": 4, "success": true, "steps": 25, "time": 0.201, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1245, "n": 4, "success": true, "steps": 25, "time": 0.249, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1246, "n": 4, "success": true, "steps": 27, "time": 0.25, "bad": [0, 1, 0], "ops": [7, 6, 3, 2, 2]}, {"seed": 1247, "n": 4, "success": true, "steps": 25, "time": 0.258, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1248, "n": 4, "success": true, "steps": 27, "time": 0.318, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1249, "n": 4, "success": true, "steps": 30, "time": 0.249, "bad": [0, 0, 5], "ops": [5, 5, 8, 2, 2]}, {"seed": 1250, "n": 4, "success": true, "steps": 24, "time": 0.243, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1251, "n": 4, "success": true, "steps": 31, "time": 0.337, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1252, "n": 4, "success": true, "steps": 26, "time": 0.237, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1253, "n": 4, "success": true, "steps": 24, "time": 0.252, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1254, "n": 4, "success": true, "steps": 25, "time": 0.166, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1255, "n": 4, "success": true, "steps": 28, "time": 0.272, "bad": [0, 0, 1], "ops": [5, 4, 3, 2, 2]}, {"seed": 1256, "n": 4, "success": true, "steps": 31, "time": 0.305, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1257, "n": 4, "success": true, "steps": 28, "time": 0.24, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1258, "n": 4, "success": true, "steps": 24, "time": 0.164, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1259, "n": 4, "success": true, "steps": 29, "time": 0.251, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 1260, "n": 4, "success": true, "steps": 28, "time": 0.206, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1261, "n": 4, "success": true, "steps": 26, "time": 0.254, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1262, "n": 4, "success": true, "steps": 29, "time": 0.297, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 1263, "n": 4, "success": true, "steps": 24, "time": 0.214, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1264, "n": 4, "success": true, "steps": 30, "time": 0.283, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1265, "n": 4, "success": true, "steps": 26, "time": 0.287, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1266, "n": 4, "success": true, "steps": 31, "time": 0.271, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1267, "n": 4, "success": true, "steps": 25, "time": 0.284, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1268, "n": 4, "success": true, "steps": 24, "time": 0.165, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1269, "n": 4, "success": true, "steps": 25, "time": 0.257, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1270, "n": 4, "success": true, "steps": 28, "time": 0.176, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1271, "n": 4, "success": true, "steps": 24, "time": 0.231, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1272, "n": 4, "success": true, "steps": 26, "time": 0.256, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1273, "n": 4, "success": true, "steps": 25, "time": 0.255, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1274, "n": 4, "success": true, "steps": 28, "time": 0.263, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1275, "n": 4, "success": true, "steps": 28, "time": 0.27, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1276, "n": 4, "success": true, "steps": 25, "time": 0.26, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1277, "n": 4, "success": true, "steps": 25, "time": 0.247, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1278, "n": 4, "success": true, "steps": 29, "time": 0.18, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1279, "n": 4, "success": true, "steps": 24, "time": 0.208, "bad": [0, 1, 0], "ops": [5, 4, 5, 2, 2]}, {"seed": 1280, "n": 4, "success": true, "steps": 24, "time": 0.178, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1281, "n": 4, "success": true, "steps": 24, "time": 0.224, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1282, "n": 4, "success": true, "steps": 25, "time": 0.244, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1283, "n": 4, "success": true, "steps": 24, "time": 0.211, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1284, "n": 4, "success": true, "steps": 28, "time": 0.234, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1285, "n": 4, "success": true, "steps": 25, "time": 0.179, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1286, "n": 4, "success": true, "steps": 28, "time": 0.206, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1287, "n": 4, "success": true, "steps": 24, "time": 0.175, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1288, "n": 4, "success": true, "steps": 24, "time": 0.227, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1289, "n": 4, "success": true, "steps": 29, "time": 0.189, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1290, "n": 4, "success": true, "steps": 26, "time": 0.185, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 1291, "n": 4, "success": true, "steps": 26, "time": 0.169, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 1292, "n": 4, "success": true, "steps": 24, "time": 0.207, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1293, "n": 4, "success": true, "steps": 26, "time": 0.228, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1294, "n": 4, "success": true, "steps": 24, "time": 0.124, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1295, "n": 4, "success": true, "steps": 29, "time": 0.214, "bad": [0, 0, 2], "ops": [5, 5, 6, 2, 2]}, {"seed": 1296, "n": 4, "success": true, "steps": 26, "time": 0.239, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1297, "n": 4, "success": true, "steps": 26, "time": 0.214, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1298, "n": 4, "success": true, "steps": 24, "time": 0.194, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1299, "n": 4, "success": true, "steps": 30, "time": 0.144, "bad": [0, 0, 0], "ops": [7, 7, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_final_latest4.txt b/stats_final_latest4.txt
index 7786e47..ba4bd7c 100644
--- a/stats_final_latest4.txt
+++ b/stats_final_latest4.txt
@@ -4,3 +4,8 @@
    4      4  {'seed': 1230, 'n': 4, 'success': True, 'steps': 29, 'time': 0.261, 'bad': [0, 1, 0], 'ops': [5, 4, 4, 2, 2]}
    5      5  {'seed': 1240, 'n': 4, 'success': True, 'steps': 26, 'time': 0.245, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
    6      6  {'seed': 1250, 'n': 4, 'success': True, 'steps': 24, 'time': 0.243, 'bad': [0, 0, 0], 'ops': [4, 4, 4, 2, 2]}
           7 +{'seed': 1260, 'n': 4, 'success': True, 'steps': 28, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
           8 +{'seed': 1270, 'n': 4, 'success': True, 'steps': 28, 'time': 0.176, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
           9 +{'seed': 1280, 'n': 4, 'success': True, 'steps': 24, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [4, 4, 4, 2, 2]}
          10 +{'seed': 1290, 'n': 4, 'success': True, 'steps': 26, 'time': 0.185, 'bad': [0, 1, 0], 'ops': [5, 4, 3, 2, 2]}
          11 +SUMMARY 100 100 mean 26.73 max_time 0.412
```

</details>

<a id="C037"></a>
### C037 · Record final release validation and the empirically infeasible sample layout

Commit `b628d28c623684c715c78b2e702a5d8c7f273a4d`; parents: 59cede108d9b8ec993ea1bcbee23185ea28a15dd. Recorded author date: 2026-09-21T22:45:05+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0215](01_timeline.md#E0215): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C037_b628d28.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

````text
 OLD   NEW   CHANGE
diff --git a/VALIDATION.md b/VALIDATION.md
new file mode 100644
index 0000000..5c1099d
--- /dev/null
+++ b/VALIDATION.md
@@ -0,0 +1,46 @@
           1 +# Rovers policy validation
           2 +
           3 +`approach.py` implements `GeneratedApproach`; it requires the sibling `task_planner.py`.
           4 +Both use only NumPy, SciPy, and the Python standard library. The policy iterates typed
           5 +objects and supports changing objective counts. A bounded task-tour planner splits
           6 +work between the rovers; grid navigation, operator feedback, and remembered radio
           7 +positions handle collision and visibility constraints. Operators run during travel
           8 +where possible. Large objective-count variants fall back to greedy task allocation.
           9 +
          10 +## Final release tests
          11 +
          12 +| Test set | Solved | Mean steps | Maximum policy computation per episode |
          13 +| --- | ---: | ---: | ---: |
          14 +| Seeds 0–99, sampled objective count | 100/100 | 23.63 | 0.290 s |
          15 +| Seeds 1200–1299, four objectives | 100/100 | 26.62 | 0.366 s |
          16 +
          17 +Policy computation includes reset planning and all action selection, excluding
          18 +client/server stepping latency. The environment allows 60 seconds per episode.
          19 +`test_reuse.py` also passed four successive resets of the same policy instance with
          20 +one through four objectives, checking action shape, dtype, bounds, and finite values.
          21 +
          22 +An earlier stress sweep passed 600/600 episodes; the retained `stats_octagon.json`,
          23 +`stats_final400.json`, `stats_final4.json`, `stats_final2000.json`, and
          24 +`stats_recovery.json` contain those results. The final radio recovery improvements
          25 +reduced the separately retested outliers: seed 549 from 92 to 45 steps, seed 1212
          26 +with four objectives from 68 to 42, and seed 2055 from 46 to 31.
          27 +
          28 +## Apparent infeasible layout
          29 +
          30 +Screening reset seeds 5000–5999 found one layout with no reachable stone pickup
          31 +position under the measured geometry: seed **5828**. Two stones lie inside the
          32 +lander's collision footprint; the third is behind the rear-left mound in the
          33 +arena corner. Direct approach attempts and a full rover heading sweep failed;
          34 +the closest tested approach to the lander-side stone remained about 0.368 m away,
          35 +outside the 0.25 m pickup range. The corner stone's entire pickup neighborhood
          36 +intersects the mound or arena walls under the measured rover radius. This seed
          37 +remains unsolved and appears physically infeasible. `probe_trapped_samples.py`
          38 +reproduces the lander-side probe; `scan_results.json` records the screening result.
          39 +
          40 +## Reproduce
          41 +
          42 +```bash
          43 +/opt/robocode-strict/bin/python test_stats.py --n 100 --out results.json
          44 +/opt/robocode-strict/bin/python test_stats.py --start 1200 --n 100 --count 4 --out results4.json
          45 +/opt/robocode-strict/bin/python test_reuse.py
          46 +```
diff --git a/stats_final_latest.json b/stats_final_latest.json
deleted file mode 100644
index 8139e59..0000000
--- a/stats_final_latest.json
+++ /dev/null
@@ -1 +0,0 @@
    1        -[{"seed": 0, "n": 3, "success": true, "steps": 28, "time": 0.196, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 21, "time": 0.21, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 21, "time": 0.226, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 24, "time": 0.188, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 23, "time": 0.213, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 25, "time": 0.214, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 21, "time": 0.147, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 24, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 26, "time": 0.136, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 24, "time": 0.23, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 22, "time": 0.194, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 20, "time": 0.137, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 24, "time": 0.202, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 28, "time": 0.293, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 31, "time": 0.172, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 27, "time": 0.293, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 23, "time": 0.167, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 26, "time": 0.244, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 24, "time": 0.23, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 31, "time": 0.271, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 27, "time": 0.266, "bad": [0, 0, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 23, "time": 0.136, "bad": [0, 0, 7], "ops": [1, 1, 8, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 24, "time": 0.213, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 18, "time": 0.105, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 20, "time": 0.214, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 20, "time": 0.208, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 26, "time": 0.245, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 22, "time": 0.144, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 24, "time": 0.135, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 23, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 34, "time": 0.24, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 27, "time": 0.242, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 21, "time": 0.139, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 27, "time": 0.202, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 20, "time": 0.145, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 20, "time": 0.143, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.162, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 20, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 21, "time": 0.192, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 25, "time": 0.242, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 25, "time": 0.201, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 21, "time": 0.198, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 23, "time": 0.199, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 27, "time": 0.237, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 23, "time": 0.221, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 24, "time": 0.244, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 21, "time": 0.203, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 25, "time": 0.208, "bad": [0, 0, 6], "ops": [1, 1, 7, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 20, "time": 0.162, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 22, "time": 0.208, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 24, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 22, "time": 0.16, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 23, "time": 0.247, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 30, "time": 0.285, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 21, "time": 0.172, "bad": [0, 0, 5], "ops": [1, 1, 7, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 27, "time": 0.243, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 25, "time": 0.198, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 18, "time": 0.161, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 26, "time": 0.203, "bad": [0, 0, 2], "ops": [2, 2, 4, 2, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 23, "time": 0.237, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 22, "time": 0.138, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 21, "time": 0.2, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 25, "time": 0.178, "bad": [0, 0, 5], "ops": [2, 2, 7, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 26, "time": 0.209, "bad": [0, 0, 4], "ops": [2, 2, 7, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 23, "time": 0.189, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 19, "time": 0.152, "bad": [0, 0, 2], "ops": [1, 1, 5, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 23, "time": 0.202, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 24, "time": 0.201, "bad": [0, 2, 0], "ops": [5, 3, 4, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 22, "time": 0.164, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 23, "time": 0.127, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 22, "time": 0.135, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 23, "time": 0.234, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 23, "time": 0.235, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 26, "time": 0.232, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 34, "time": 0.242, "bad": [0, 0, 11], "ops": [1, 1, 14, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 19, "time": 0.135, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 24, "time": 0.183, "bad": [0, 0, 6], "ops": [2, 2, 9, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 20, "time": 0.181, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 26, "time": 0.226, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 24, "time": 0.178, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 23, "time": 0.173, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 20, "time": 0.162, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 25, "time": 0.24, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 24, "time": 0.174, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 25, "time": 0.125, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 22, "time": 0.178, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 22, "time": 0.212, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 23, "time": 0.162, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 22, "time": 0.155, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 89, "n": 3, "success": true, "steps": 31, "time": 0.246, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 90, "n": 2, "success": true, "steps": 29, "time": 0.173, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 24, "time": 0.233, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 24, "time": 0.223, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 27, "time": 0.151, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 22, "time": 0.116, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 22, "time": 0.205, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 25, "time": 0.303, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 27, "time": 0.202, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 24, "time": 0.171, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 27, "time": 0.211, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_final_latest.txt b/stats_final_latest.txt
deleted file mode 100644
index 5e4837f..0000000
--- a/stats_final_latest.txt
+++ /dev/null
@@ -1,11 +0,0 @@
    1        -{'seed': 0, 'n': 3, 'success': True, 'steps': 28, 'time': 0.196, 'bad': [0, 0, 0], 'ops': [3, 3, 2, 2, 2]}
    2        -{'seed': 10, 'n': 3, 'success': True, 'steps': 22, 'time': 0.194, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    3        -{'seed': 20, 'n': 3, 'success': True, 'steps': 27, 'time': 0.266, 'bad': [0, 0, 0], 'ops': [4, 3, 2, 2, 2]}
    4        -{'seed': 30, 'n': 1, 'success': True, 'steps': 34, 'time': 0.24, 'bad': [0, 0, 4], 'ops': [1, 1, 6, 2, 2]}
    5        -{'seed': 40, 'n': 2, 'success': True, 'steps': 25, 'time': 0.201, 'bad': [0, 0, 0], 'ops': [3, 3, 4, 2, 2]}
    6        -{'seed': 50, 'n': 3, 'success': True, 'steps': 24, 'time': 0.233, 'bad': [0, 0, 0], 'ops': [3, 3, 3, 2, 2]}
    7        -{'seed': 60, 'n': 1, 'success': True, 'steps': 22, 'time': 0.138, 'bad': [0, 0, 0], 'ops': [1, 1, 2, 2, 2]}
    8        -{'seed': 70, 'n': 2, 'success': True, 'steps': 22, 'time': 0.135, 'bad': [0, 1, 0], 'ops': [3, 2, 3, 2, 2]}
    9        -{'seed': 80, 'n': 3, 'success': True, 'steps': 23, 'time': 0.173, 'bad': [0, 1, 0], 'ops': [4, 3, 2, 2, 2]}
   10        -{'seed': 90, 'n': 2, 'success': True, 'steps': 29, 'time': 0.173, 'bad': [0, 0, 0], 'ops': [4, 4, 2, 2, 2]}
   11        -SUMMARY 100 100 mean 23.83 max_time 0.303
diff --git a/stats_final_latest4.json b/stats_final_latest4.json
deleted file mode 100644
index 34ef00b..0000000
--- a/stats_final_latest4.json
+++ /dev/null
@@ -1 +0,0 @@
    1        -[{"seed": 1200, "n": 4, "success": true, "steps": 26, "time": 0.164, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1201, "n": 4, "success": true, "steps": 26, "time": 0.268, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1202, "n": 4, "success": true, "steps": 29, "time": 0.253, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1203, "n": 4, "success": true, "steps": 27, "time": 0.204, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1204, "n": 4, "success": true, "steps": 26, "time": 0.272, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1205, "n": 4, "success": true, "steps": 32, "time": 0.278, "bad": [0, 1, 0], "ops": [6, 5, 4, 2, 2]}, {"seed": 1206, "n": 4, "success": true, "steps": 25, "time": 0.235, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1207, "n": 4, "success": true, "steps": 22, "time": 0.208, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1208, "n": 4, "success": true, "steps": 30, "time": 0.321, "bad": [0, 1, 1], "ops": [5, 4, 3, 2, 2]}, {"seed": 1209, "n": 4, "success": true, "steps": 24, "time": 0.237, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1210, "n": 4, "success": true, "steps": 24, "time": 0.253, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1211, "n": 4, "success": true, "steps": 24, "time": 0.269, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1212, "n": 4, "success": true, "steps": 37, "time": 0.317, "bad": [0, 0, 13], "ops": [4, 4, 16, 2, 2]}, {"seed": 1213, "n": 4, "success": true, "steps": 27, "time": 0.197, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1214, "n": 4, "success": true, "steps": 26, "time": 0.237, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1215, "n": 4, "success": true, "steps": 24, "time": 0.25, "bad": [0, 1, 0], "ops": [5, 4, 2, 2, 2]}, {"seed": 1216, "n": 4, "success": true, "steps": 24, "time": 0.229, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1217, "n": 4, "success": true, "steps": 28, "time": 0.259, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1218, "n": 4, "success": true, "steps": 26, "time": 0.258, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1219, "n": 4, "success": true, "steps": 29, "time": 0.273, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1220, "n": 4, "success": true, "steps": 23, "time": 0.201, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1221, "n": 4, "success": true, "steps": 30, "time": 0.292, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1222, "n": 4, "success": true, "steps": 29, "time": 0.252, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1223, "n": 4, "success": true, "steps": 29, "time": 0.262, "bad": [0, 0, 0], "ops": [5, 5, 5, 2, 2]}, {"seed": 1224, "n": 4, "success": true, "steps": 24, "time": 0.249, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1225, "n": 4, "success": true, "steps": 24, "time": 0.228, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1226, "n": 4, "success": true, "steps": 29, "time": 0.239, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1227, "n": 4, "success": true, "steps": 24, "time": 0.189, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1228, "n": 4, "success": true, "steps": 25, "time": 0.169, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1229, "n": 4, "success": true, "steps": 30, "time": 0.309, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1230, "n": 4, "success": true, "steps": 29, "time": 0.261, "bad": [0, 1, 0], "ops": [5, 4, 4, 2, 2]}, {"seed": 1231, "n": 4, "success": true, "steps": 45, "time": 0.412, "bad": [0, 0, 12], "ops": [5, 5, 17, 2, 2]}, {"seed": 1232, "n": 4, "success": true, "steps": 26, "time": 0.303, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1233, "n": 4, "success": true, "steps": 27, "time": 0.246, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1234, "n": 4, "success": true, "steps": 27, "time": 0.187, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1235, "n": 4, "success": true, "steps": 25, "time": 0.238, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1236, "n": 4, "success": true, "steps": 26, "time": 0.284, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1237, "n": 4, "success": true, "steps": 28, "time": 0.272, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1238, "n": 4, "success": true, "steps": 31, "time": 0.286, "bad": [0, 0, 0], "ops": [6, 6, 5, 2, 2]}, {"seed": 1239, "n": 4, "success": true, "steps": 25, "time": 0.255, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1240, "n": 4, "success": true, "steps": 26, "time": 0.245, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1241, "n": 4, "success": true, "steps": 28, "time": 0.235, "bad": [0, 0, 2], "ops": [6, 6, 6, 2, 2]}, {"seed": 1242, "n": 4, "success": true, "steps": 25, "time": 0.238, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1243, "n": 4, "success": true, "steps": 27, "time": 0.303, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1244, "n": 4, "success": true, "steps": 25, "time": 0.201, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1245, "n": 4, "success": true, "steps": 25, "time": 0.249, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1246, "n": 4, "success": true, "steps": 27, "time": 0.25, "bad": [0, 1, 0], "ops": [7, 6, 3, 2, 2]}, {"seed": 1247, "n": 4, "success": true, "steps": 25, "time": 0.258, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1248, "n": 4, "success": true, "steps": 27, "time": 0.318, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1249, "n": 4, "success": true, "steps": 30, "time": 0.249, "bad": [0, 0, 5], "ops": [5, 5, 8, 2, 2]}, {"seed": 1250, "n": 4, "success": true, "steps": 24, "time": 0.243, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1251, "n": 4, "success": true, "steps": 31, "time": 0.337, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1252, "n": 4, "success": true, "steps": 26, "time": 0.237, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1253, "n": 4, "success": true, "steps": 24, "time": 0.252, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1254, "n": 4, "success": true, "steps": 25, "time": 0.166, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1255, "n": 4, "success": true, "steps": 28, "time": 0.272, "bad": [0, 0, 1], "ops": [5, 4, 3, 2, 2]}, {"seed": 1256, "n": 4, "success": true, "steps": 31, "time": 0.305, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1257, "n": 4, "success": true, "steps": 28, "time": 0.24, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1258, "n": 4, "success": true, "steps": 24, "time": 0.164, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1259, "n": 4, "success": true, "steps": 29, "time": 0.251, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 1260, "n": 4, "success": true, "steps": 28, "time": 0.206, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1261, "n": 4, "success": true, "steps": 26, "time": 0.254, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1262, "n": 4, "success": true, "steps": 29, "time": 0.297, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 1263, "n": 4, "success": true, "steps": 24, "time": 0.214, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1264, "n": 4, "success": true, "steps": 30, "time": 0.283, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1265, "n": 4, "success": true, "steps": 26, "time": 0.287, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1266, "n": 4, "success": true, "steps": 31, "time": 0.271, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1267, "n": 4, "success": true, "steps": 25, "time": 0.284, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1268, "n": 4, "success": true, "steps": 24, "time": 0.165, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1269, "n": 4, "success": true, "steps": 25, "time": 0.257, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1270, "n": 4, "success": true, "steps": 28, "time": 0.176, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1271, "n": 4, "success": true, "steps": 24, "time": 0.231, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1272, "n": 4, "success": true, "steps": 26, "time": 0.256, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1273, "n": 4, "success": true, "steps": 25, "time": 0.255, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1274, "n": 4, "success": true, "steps": 28, "time": 0.263, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1275, "n": 4, "success": true, "steps": 28, "time": 0.27, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1276, "n": 4, "success": true, "steps": 25, "time": 0.26, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1277, "n": 4, "success": true, "steps": 25, "time": 0.247, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1278, "n": 4, "success": true, "steps": 29, "time": 0.18, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1279, "n": 4, "success": true, "steps": 24, "time": 0.208, "bad": [0, 1, 0], "ops": [5, 4, 5, 2, 2]}, {"seed": 1280, "n": 4, "success": true, "steps": 24, "time": 0.178, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1281, "n": 4, "success": true, "steps": 24, "time": 0.224, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1282, "n": 4, "success": true, "steps": 25, "time": 0.244, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1283, "n": 4, "success": true, "steps": 24, "time": 0.211, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1284, "n": 4, "success": true, "steps": 28, "time": 0.234, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1285, "n": 4, "success": true, "steps": 25, "time": 0.179, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1286, "n": 4, "success": true, "steps": 28, "time": 0.206, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1287, "n": 4, "success": true, "steps": 24, "time": 0.175, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1288, "n": 4, "success": true, "steps": 24, "time": 0.227, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1289, "n": 4, "success": true, "steps": 29, "time": 0.189, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1290, "n": 4, "success": true, "steps": 26, "time": 0.185, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 1291, "n": 4, "success": true, "steps": 26, "time": 0.169, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 1292, "n": 4, "success": true, "steps": 24, "time": 0.207, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1293, "n": 4, "success": true, "steps": 26, "time": 0.228, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1294, "n": 4, "success": true, "steps": 24, "time": 0.124, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1295, "n": 4, "success": true, "steps": 29, "time": 0.214, "bad": [0, 0, 2], "ops": [5, 5, 6, 2, 2]}, {"seed": 1296, "n": 4, "success": true, "steps": 26, "time": 0.239, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1297, "n": 4, "success": true, "steps": 26, "time": 0.214, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1298, "n": 4, "success": true, "steps": 24, "time": 0.194, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1299, "n": 4, "success": true, "steps": 30, "time": 0.144, "bad": [0, 0, 0], "ops": [7, 7, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_final_latest4.txt b/stats_final_latest4.txt
deleted file mode 100644
index ba4bd7c..0000000
--- a/stats_final_latest4.txt
+++ /dev/null
@@ -1,11 +0,0 @@
    1        -{'seed': 1200, 'n': 4, 'success': True, 'steps': 26, 'time': 0.164, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
    2        -{'seed': 1210, 'n': 4, 'success': True, 'steps': 24, 'time': 0.253, 'bad': [0, 0, 0], 'ops': [5, 5, 4, 2, 2]}
    3        -{'seed': 1220, 'n': 4, 'success': True, 'steps': 23, 'time': 0.201, 'bad': [0, 0, 0], 'ops': [5, 5, 3, 2, 2]}
    4        -{'seed': 1230, 'n': 4, 'success': True, 'steps': 29, 'time': 0.261, 'bad': [0, 1, 0], 'ops': [5, 4, 4, 2, 2]}
    5        -{'seed': 1240, 'n': 4, 'success': True, 'steps': 26, 'time': 0.245, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
    6        -{'seed': 1250, 'n': 4, 'success': True, 'steps': 24, 'time': 0.243, 'bad': [0, 0, 0], 'ops': [4, 4, 4, 2, 2]}
    7        -{'seed': 1260, 'n': 4, 'success': True, 'steps': 28, 'time': 0.206, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
    8        -{'seed': 1270, 'n': 4, 'success': True, 'steps': 28, 'time': 0.176, 'bad': [0, 0, 0], 'ops': [4, 4, 3, 2, 2]}
    9        -{'seed': 1280, 'n': 4, 'success': True, 'steps': 24, 'time': 0.178, 'bad': [0, 0, 0], 'ops': [4, 4, 4, 2, 2]}
   10        -{'seed': 1290, 'n': 4, 'success': True, 'steps': 26, 'time': 0.185, 'bad': [0, 1, 0], 'ops': [5, 4, 3, 2, 2]}
   11        -SUMMARY 100 100 mean 26.73 max_time 0.412
diff --git a/stats_release.json b/stats_release.json
new file mode 100644
index 0000000..8483610
--- /dev/null
+++ b/stats_release.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "n": 3, "success": true, "steps": 28, "time": 0.188, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 1, "n": 2, "success": true, "steps": 21, "time": 0.19, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 2, "n": 3, "success": true, "steps": 21, "time": 0.147, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 3, "n": 3, "success": true, "steps": 24, "time": 0.159, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 4, "n": 3, "success": true, "steps": 23, "time": 0.211, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 5, "n": 3, "success": true, "steps": 25, "time": 0.262, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 6, "n": 2, "success": true, "steps": 21, "time": 0.161, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 7, "n": 3, "success": true, "steps": 24, "time": 0.154, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 8, "n": 3, "success": true, "steps": 26, "time": 0.195, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 9, "n": 2, "success": true, "steps": 24, "time": 0.214, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 10, "n": 3, "success": true, "steps": 22, "time": 0.127, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 11, "n": 1, "success": true, "steps": 20, "time": 0.072, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 12, "n": 2, "success": true, "steps": 24, "time": 0.243, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 13, "n": 3, "success": true, "steps": 28, "time": 0.25, "bad": [0, 1, 0], "ops": [4, 3, 3, 2, 2]}, {"seed": 14, "n": 1, "success": true, "steps": 31, "time": 0.235, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 15, "n": 3, "success": true, "steps": 27, "time": 0.288, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 16, "n": 2, "success": true, "steps": 23, "time": 0.232, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 17, "n": 3, "success": true, "steps": 26, "time": 0.214, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 18, "n": 3, "success": true, "steps": 24, "time": 0.225, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 19, "n": 2, "success": true, "steps": 31, "time": 0.29, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 20, "n": 3, "success": true, "steps": 27, "time": 0.141, "bad": [0, 0, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 21, "n": 1, "success": true, "steps": 23, "time": 0.173, "bad": [0, 0, 7], "ops": [1, 1, 8, 2, 2]}, {"seed": 22, "n": 3, "success": true, "steps": 24, "time": 0.218, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 23, "n": 1, "success": true, "steps": 18, "time": 0.147, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 24, "n": 2, "success": true, "steps": 20, "time": 0.153, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 25, "n": 2, "success": true, "steps": 20, "time": 0.19, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 26, "n": 3, "success": true, "steps": 26, "time": 0.219, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 27, "n": 1, "success": true, "steps": 22, "time": 0.143, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 28, "n": 2, "success": true, "steps": 24, "time": 0.116, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 29, "n": 3, "success": true, "steps": 23, "time": 0.239, "bad": [0, 0, 0], "ops": [3, 3, 2, 2, 2]}, {"seed": 30, "n": 1, "success": true, "steps": 24, "time": 0.176, "bad": [0, 0, 4], "ops": [1, 1, 6, 2, 2]}, {"seed": 31, "n": 2, "success": true, "steps": 27, "time": 0.267, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 32, "n": 3, "success": true, "steps": 21, "time": 0.148, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 33, "n": 3, "success": true, "steps": 27, "time": 0.247, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 34, "n": 1, "success": true, "steps": 20, "time": 0.151, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 35, "n": 1, "success": true, "steps": 20, "time": 0.161, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 36, "n": 2, "success": true, "steps": 21, "time": 0.175, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 37, "n": 1, "success": true, "steps": 20, "time": 0.14, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 38, "n": 1, "success": true, "steps": 21, "time": 0.17, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 39, "n": 3, "success": true, "steps": 25, "time": 0.271, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 40, "n": 2, "success": true, "steps": 25, "time": 0.197, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 41, "n": 2, "success": true, "steps": 21, "time": 0.167, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 42, "n": 1, "success": true, "steps": 23, "time": 0.179, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 43, "n": 2, "success": true, "steps": 27, "time": 0.176, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 44, "n": 3, "success": true, "steps": 23, "time": 0.19, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 45, "n": 3, "success": true, "steps": 24, "time": 0.176, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 46, "n": 2, "success": true, "steps": 21, "time": 0.196, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 47, "n": 1, "success": true, "steps": 25, "time": 0.16, "bad": [0, 0, 6], "ops": [1, 1, 7, 2, 2]}, {"seed": 48, "n": 1, "success": true, "steps": 20, "time": 0.15, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 49, "n": 1, "success": true, "steps": 22, "time": 0.178, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 50, "n": 3, "success": true, "steps": 24, "time": 0.249, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 51, "n": 2, "success": true, "steps": 22, "time": 0.207, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 52, "n": 3, "success": true, "steps": 23, "time": 0.202, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 53, "n": 3, "success": true, "steps": 30, "time": 0.268, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 54, "n": 1, "success": true, "steps": 21, "time": 0.164, "bad": [0, 0, 5], "ops": [1, 1, 7, 2, 2]}, {"seed": 55, "n": 3, "success": true, "steps": 27, "time": 0.198, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 56, "n": 2, "success": true, "steps": 25, "time": 0.194, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 57, "n": 1, "success": true, "steps": 18, "time": 0.155, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 58, "n": 2, "success": true, "steps": 26, "time": 0.219, "bad": [0, 0, 2], "ops": [2, 2, 4, 2, 2]}, {"seed": 59, "n": 3, "success": true, "steps": 23, "time": 0.212, "bad": [0, 0, 0], "ops": [3, 3, 5, 2, 2]}, {"seed": 60, "n": 1, "success": true, "steps": 22, "time": 0.193, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 61, "n": 2, "success": true, "steps": 21, "time": 0.202, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 62, "n": 2, "success": true, "steps": 25, "time": 0.188, "bad": [0, 0, 5], "ops": [2, 2, 7, 2, 2]}, {"seed": 63, "n": 2, "success": true, "steps": 26, "time": 0.191, "bad": [0, 0, 4], "ops": [2, 2, 7, 2, 2]}, {"seed": 64, "n": 2, "success": true, "steps": 23, "time": 0.221, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 65, "n": 1, "success": true, "steps": 19, "time": 0.149, "bad": [0, 0, 2], "ops": [1, 1, 5, 2, 2]}, {"seed": 66, "n": 3, "success": true, "steps": 23, "time": 0.25, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 67, "n": 3, "success": true, "steps": 24, "time": 0.219, "bad": [0, 2, 0], "ops": [5, 3, 4, 2, 2]}, {"seed": 68, "n": 2, "success": true, "steps": 22, "time": 0.156, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 69, "n": 1, "success": true, "steps": 23, "time": 0.159, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 70, "n": 2, "success": true, "steps": 22, "time": 0.164, "bad": [0, 1, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 71, "n": 3, "success": true, "steps": 23, "time": 0.199, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 72, "n": 3, "success": true, "steps": 23, "time": 0.187, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 73, "n": 3, "success": true, "steps": 26, "time": 0.25, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 74, "n": 1, "success": true, "steps": 24, "time": 0.085, "bad": [0, 0, 7], "ops": [1, 1, 10, 2, 2]}, {"seed": 75, "n": 2, "success": true, "steps": 19, "time": 0.159, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 76, "n": 2, "success": true, "steps": 24, "time": 0.167, "bad": [0, 0, 6], "ops": [2, 2, 9, 2, 2]}, {"seed": 77, "n": 1, "success": true, "steps": 20, "time": 0.113, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 78, "n": 3, "success": true, "steps": 26, "time": 0.259, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 79, "n": 1, "success": true, "steps": 24, "time": 0.165, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 80, "n": 3, "success": true, "steps": 23, "time": 0.221, "bad": [0, 1, 0], "ops": [4, 3, 2, 2, 2]}, {"seed": 81, "n": 1, "success": true, "steps": 20, "time": 0.17, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 82, "n": 3, "success": true, "steps": 25, "time": 0.241, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 83, "n": 3, "success": true, "steps": 24, "time": 0.239, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 84, "n": 2, "success": true, "steps": 25, "time": 0.208, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 85, "n": 3, "success": true, "steps": 22, "time": 0.241, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 86, "n": 3, "success": true, "steps": 22, "time": 0.279, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 87, "n": 2, "success": true, "steps": 23, "time": 0.216, "bad": [0, 0, 0], "ops": [3, 2, 3, 2, 2]}, {"seed": 88, "n": 2, "success": true, "steps": 22, "time": 0.205, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 89, "n": 3, "success": true, "steps": 31, "time": 0.276, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 90, "n": 2, "success": true, "steps": 29, "time": 0.15, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 91, "n": 3, "success": true, "steps": 24, "time": 0.168, "bad": [0, 0, 0], "ops": [3, 3, 4, 2, 2]}, {"seed": 92, "n": 2, "success": true, "steps": 24, "time": 0.221, "bad": [0, 0, 0], "ops": [2, 2, 3, 2, 2]}, {"seed": 93, "n": 3, "success": true, "steps": 27, "time": 0.205, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 94, "n": 1, "success": true, "steps": 22, "time": 0.143, "bad": [0, 0, 0], "ops": [1, 1, 2, 2, 2]}, {"seed": 95, "n": 2, "success": true, "steps": 22, "time": 0.223, "bad": [0, 0, 0], "ops": [2, 2, 4, 2, 2]}, {"seed": 96, "n": 3, "success": true, "steps": 25, "time": 0.185, "bad": [0, 0, 0], "ops": [3, 3, 3, 2, 2]}, {"seed": 97, "n": 1, "success": true, "steps": 27, "time": 0.192, "bad": [0, 0, 0], "ops": [1, 1, 3, 2, 2]}, {"seed": 98, "n": 2, "success": true, "steps": 24, "time": 0.229, "bad": [0, 0, 0], "ops": [2, 2, 2, 2, 2]}, {"seed": 99, "n": 3, "success": true, "steps": 27, "time": 0.24, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}]
\ No newline at end of file
diff --git a/stats_release4.json b/stats_release4.json
new file mode 100644
index 0000000..cb5ea78
--- /dev/null
+++ b/stats_release4.json
@@ -0,0 +1 @@
           1 +[{"seed": 1200, "n": 4, "success": true, "steps": 26, "time": 0.183, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1201, "n": 4, "success": true, "steps": 26, "time": 0.274, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1202, "n": 4, "success": true, "steps": 29, "time": 0.197, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1203, "n": 4, "success": true, "steps": 27, "time": 0.275, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1204, "n": 4, "success": true, "steps": 26, "time": 0.289, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1205, "n": 4, "success": true, "steps": 32, "time": 0.277, "bad": [0, 1, 0], "ops": [6, 5, 4, 2, 2]}, {"seed": 1206, "n": 4, "success": true, "steps": 25, "time": 0.25, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1207, "n": 4, "success": true, "steps": 22, "time": 0.252, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1208, "n": 4, "success": true, "steps": 30, "time": 0.205, "bad": [0, 1, 1], "ops": [5, 4, 3, 2, 2]}, {"seed": 1209, "n": 4, "success": true, "steps": 24, "time": 0.192, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1210, "n": 4, "success": true, "steps": 24, "time": 0.198, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1211, "n": 4, "success": true, "steps": 24, "time": 0.245, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1212, "n": 4, "success": true, "steps": 42, "time": 0.366, "bad": [0, 0, 18], "ops": [4, 4, 21, 2, 2]}, {"seed": 1213, "n": 4, "success": true, "steps": 27, "time": 0.254, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1214, "n": 4, "success": true, "steps": 26, "time": 0.269, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1215, "n": 4, "success": true, "steps": 24, "time": 0.241, "bad": [0, 1, 0], "ops": [5, 4, 2, 2, 2]}, {"seed": 1216, "n": 4, "success": true, "steps": 24, "time": 0.185, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1217, "n": 4, "success": true, "steps": 28, "time": 0.268, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1218, "n": 4, "success": true, "steps": 26, "time": 0.18, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1219, "n": 4, "success": true, "steps": 29, "time": 0.256, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1220, "n": 4, "success": true, "steps": 23, "time": 0.222, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1221, "n": 4, "success": true, "steps": 30, "time": 0.263, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1222, "n": 4, "success": true, "steps": 29, "time": 0.239, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1223, "n": 4, "success": true, "steps": 29, "time": 0.274, "bad": [0, 0, 0], "ops": [5, 5, 5, 2, 2]}, {"seed": 1224, "n": 4, "success": true, "steps": 24, "time": 0.194, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1225, "n": 4, "success": true, "steps": 24, "time": 0.245, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1226, "n": 4, "success": true, "steps": 29, "time": 0.238, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1227, "n": 4, "success": true, "steps": 24, "time": 0.191, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1228, "n": 4, "success": true, "steps": 25, "time": 0.211, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1229, "n": 4, "success": true, "steps": 30, "time": 0.267, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1230, "n": 4, "success": true, "steps": 29, "time": 0.263, "bad": [0, 1, 0], "ops": [5, 4, 4, 2, 2]}, {"seed": 1231, "n": 4, "success": true, "steps": 29, "time": 0.277, "bad": [0, 0, 0], "ops": [5, 5, 5, 2, 2]}, {"seed": 1232, "n": 4, "success": true, "steps": 26, "time": 0.246, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1233, "n": 4, "success": true, "steps": 27, "time": 0.271, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1234, "n": 4, "success": true, "steps": 27, "time": 0.23, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1235, "n": 4, "success": true, "steps": 25, "time": 0.224, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1236, "n": 4, "success": true, "steps": 26, "time": 0.258, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1237, "n": 4, "success": true, "steps": 28, "time": 0.264, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1238, "n": 4, "success": true, "steps": 31, "time": 0.296, "bad": [0, 0, 0], "ops": [6, 6, 5, 2, 2]}, {"seed": 1239, "n": 4, "success": true, "steps": 25, "time": 0.275, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1240, "n": 4, "success": true, "steps": 26, "time": 0.212, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1241, "n": 4, "success": true, "steps": 28, "time": 0.258, "bad": [0, 0, 2], "ops": [6, 6, 6, 2, 2]}, {"seed": 1242, "n": 4, "success": true, "steps": 25, "time": 0.228, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1243, "n": 4, "success": true, "steps": 27, "time": 0.266, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1244, "n": 4, "success": true, "steps": 25, "time": 0.237, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1245, "n": 4, "success": true, "steps": 25, "time": 0.241, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1246, "n": 4, "success": true, "steps": 27, "time": 0.266, "bad": [0, 1, 0], "ops": [7, 6, 3, 2, 2]}, {"seed": 1247, "n": 4, "success": true, "steps": 25, "time": 0.254, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1248, "n": 4, "success": true, "steps": 27, "time": 0.29, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1249, "n": 4, "success": true, "steps": 30, "time": 0.294, "bad": [0, 0, 5], "ops": [5, 5, 8, 2, 2]}, {"seed": 1250, "n": 4, "success": true, "steps": 24, "time": 0.298, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1251, "n": 4, "success": true, "steps": 31, "time": 0.328, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1252, "n": 4, "success": true, "steps": 26, "time": 0.218, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1253, "n": 4, "success": true, "steps": 24, "time": 0.218, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1254, "n": 4, "success": true, "steps": 25, "time": 0.241, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1255, "n": 4, "success": true, "steps": 28, "time": 0.253, "bad": [0, 0, 1], "ops": [5, 4, 3, 2, 2]}, {"seed": 1256, "n": 4, "success": true, "steps": 31, "time": 0.3, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1257, "n": 4, "success": true, "steps": 28, "time": 0.263, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1258, "n": 4, "success": true, "steps": 24, "time": 0.24, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1259, "n": 4, "success": true, "steps": 29, "time": 0.255, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 1260, "n": 4, "success": true, "steps": 28, "time": 0.218, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1261, "n": 4, "success": true, "steps": 26, "time": 0.284, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1262, "n": 4, "success": true, "steps": 29, "time": 0.227, "bad": [0, 0, 0], "ops": [6, 6, 4, 2, 2]}, {"seed": 1263, "n": 4, "success": true, "steps": 24, "time": 0.26, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1264, "n": 4, "success": true, "steps": 30, "time": 0.337, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1265, "n": 4, "success": true, "steps": 26, "time": 0.281, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1266, "n": 4, "success": true, "steps": 31, "time": 0.248, "bad": [0, 0, 0], "ops": [5, 5, 4, 2, 2]}, {"seed": 1267, "n": 4, "success": true, "steps": 25, "time": 0.245, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1268, "n": 4, "success": true, "steps": 24, "time": 0.22, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1269, "n": 4, "success": true, "steps": 25, "time": 0.236, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1270, "n": 4, "success": true, "steps": 28, "time": 0.275, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1271, "n": 4, "success": true, "steps": 24, "time": 0.245, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1272, "n": 4, "success": true, "steps": 26, "time": 0.267, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1273, "n": 4, "success": true, "steps": 25, "time": 0.246, "bad": [0, 0, 0], "ops": [4, 4, 5, 2, 2]}, {"seed": 1274, "n": 4, "success": true, "steps": 28, "time": 0.259, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1275, "n": 4, "success": true, "steps": 28, "time": 0.215, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1276, "n": 4, "success": true, "steps": 25, "time": 0.249, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1277, "n": 4, "success": true, "steps": 25, "time": 0.221, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1278, "n": 4, "success": true, "steps": 29, "time": 0.262, "bad": [0, 0, 0], "ops": [6, 6, 3, 2, 2]}, {"seed": 1279, "n": 4, "success": true, "steps": 24, "time": 0.264, "bad": [0, 1, 0], "ops": [5, 4, 5, 2, 2]}, {"seed": 1280, "n": 4, "success": true, "steps": 24, "time": 0.245, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1281, "n": 4, "success": true, "steps": 24, "time": 0.219, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1282, "n": 4, "success": true, "steps": 25, "time": 0.249, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1283, "n": 4, "success": true, "steps": 24, "time": 0.242, "bad": [0, 0, 0], "ops": [4, 4, 4, 2, 2]}, {"seed": 1284, "n": 4, "success": true, "steps": 28, "time": 0.257, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1285, "n": 4, "success": true, "steps": 25, "time": 0.178, "bad": [0, 0, 0], "ops": [5, 5, 2, 2, 2]}, {"seed": 1286, "n": 4, "success": true, "steps": 28, "time": 0.229, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1287, "n": 4, "success": true, "steps": 24, "time": 0.218, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1288, "n": 4, "success": true, "steps": 24, "time": 0.169, "bad": [0, 0, 0], "ops": [4, 4, 2, 2, 2]}, {"seed": 1289, "n": 4, "success": true, "steps": 29, "time": 0.201, "bad": [0, 0, 0], "ops": [5, 5, 3, 2, 2]}, {"seed": 1290, "n": 4, "success": true, "steps": 26, "time": 0.145, "bad": [0, 1, 0], "ops": [5, 4, 3, 2, 2]}, {"seed": 1291, "n": 4, "success": true, "steps": 26, "time": 0.131, "bad": [0, 1, 0], "ops": [6, 5, 3, 2, 2]}, {"seed": 1292, "n": 4, "success": true, "steps": 24, "time": 0.133, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1293, "n": 4, "success": true, "steps": 26, "time": 0.185, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1294, "n": 4, "success": true, "steps": 24, "time": 0.184, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1295, "n": 4, "success": true, "steps": 29, "time": 0.165, "bad": [0, 0, 2], "ops": [5, 5, 6, 2, 2]}, {"seed": 1296, "n": 4, "success": true, "steps": 26, "time": 0.229, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1297, "n": 4, "success": true, "steps": 26, "time": 0.214, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1298, "n": 4, "success": true, "steps": 24, "time": 0.206, "bad": [0, 0, 0], "ops": [4, 4, 3, 2, 2]}, {"seed": 1299, "n": 4, "success": true, "steps": 30, "time": 0.204, "bad": [0, 0, 0], "ops": [7, 7, 3, 2, 2]}]
\ No newline at end of file
````

</details>

