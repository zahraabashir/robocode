# Rovers · gpt-6-astra · replicate 24: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `9afebcc` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `761887d` | Add initial observation probe | inspect_env.py | [E0007](01_timeline.md#E0007) |
| [C003](#C003) · `9c8f0e9` | Add initial geometry observation probe | probe_geometry.py | No matched commit command/output |
| [C004](#C004) · `9bac1cd` | Probe motion scale and static wall collision | probe_geometry.py | No matched commit command/output |
| [C005](#C005) · `95c9e62` | Add camera visibility probes across candidate viewpoints | probe_camera.py | No matched commit command/output |
| [C006](#C006) · `2777b78` | Map center wall extent with independent crossing probes | probe_camera.log, probe_geometry.py | No matched commit command/output |
| [C007](#C007) · `f17dd4f` | Implement geometric navigation with concurrent sampling imaging and radio tasks | approach.py, probe_camera.log, probe_camera_results.json | [E0015](01_timeline.md#E0015) |
| [C008](#C008) · `51f7d9e` | Measure wall opening and arena margin on independent seed | probe_geometry.py | No matched commit command/output |
| [C009](#C009) · `a6557ef` | Separate full center driving wall from camera occlusion and add episode tests | test_approach.py | [E0028](01_timeline.md#E0028) |
| [C010](#C010) · `b86fb77` | Correct wall driving extent and omit it from visibility checks | approach.py, test_results.jsonl | [E0019](01_timeline.md#E0019) |
| [C011](#C011) · `5800789` | Probe rover radius, pillar corners, and lander footprint | probe_geometry.py | No matched commit command/output |
| [C012](#C012) · `aceb14a` | Add concise trajectory debugger | debug_run.py, test_results.jsonl | [E0025](01_timeline.md#E0025) |
| [C013](#C013) · `3c4c4b9` | Refine collision margins near lander and pillars | probe_geometry.py | No matched commit command/output |
| [C014](#C014) · `8ba0f2b` | Probe image transmission across middle wall at known ranges | current_results.jsonl, probe_radio.py, test_results.jsonl | No matched commit command/output |
| [C015](#C015) · `e438150` | Measure exact lander clearance and possible confounding pillars | current_results.jsonl, probe_lander.py, visual_validation_20_29.jsonl | No matched commit command/output |
| [C016](#C016) · `c747817` | Learn failed radio and camera viewpoints and refine rover collision radius | approach.py, current_results.jsonl | [E0039](01_timeline.md#E0039) |
| [C017](#C017) · `f3158c2` | Add independent seeds20-29 validation with stalled-state detection | visual_validate.py | No matched commit command/output |
| [C018](#C018) · `e73f450` | Add broad seed and variable-object-count regression checks | current_results.jsonl, revised_results.jsonl, stress_test.py, visual_validation_20_29.jsonl | [E0057](01_timeline.md#E0057) |
| [C019](#C019) · `44c1aee` | Compare radio LOS and range across nearby transmission poses | probe_radio_details.py, stress_default.jsonl, stress_eight.jsonl, stress_four.jsonl | No matched commit command/output |
| [C020](#C020) · `831e060` | Photograph opportunistically during travel and cache static visibility maps | approach.py, stress_default.jsonl, stress_four.jsonl | [E0059](01_timeline.md#E0059) |
| [C021](#C021) · `63b51c6` | Refine effective transmission radius below four meters | opportunistic.jsonl | No matched commit command/output |
| [C022](#C022) · `1b5aab2` | Measure exact radio cutoff and occluder padding with fine-grained poses | opportunistic.jsonl, probe_radio_details.py | No matched commit command/output |
| [C023](#C023) · `3645140` | Test exact 3.9 meter radio radius and padded pillar threshold | probe_radio_details.py, radio_details.log | No matched commit command/output |
| [C024](#C024) · `e8d6a4c` | Locate radio cutoff and compare equivalent-distance poses | probe_radio_details.py, radio_details.log | No matched commit command/output |
| [C025](#C025) · `9425eee` | Radio while returning home and prepare the camera during otherwise idle travel | approach.py, radio_details.log | [E0071](01_timeline.md#E0071) |
| [C026](#C026) · `744f3f6` | Prototype joint rover task selection minimizing concurrent route cost | assignment_baseline.py, build_assignment.py, candidate_assignment.py, test_assignment.py | No matched commit command/output |
| [C027](#C027) · `730d4d1` | Use total immediate task distance for joint rover matching | candidate_assignment.py | No matched commit command/output |
| [C028](#C028) · `b429738` | Refine radio visibility from measured occlusion and continue useful travel while transmitting | approach.py, assignment_minimax_results.jsonl, assignment_results.jsonl, larger_stress.jsonl, travel_ops.jsonl | [E0083](01_timeline.md#E0083) |
| [C029](#C029) · `ec4e79b` | Compare balanced joint task distance without optional rover idling | candidate_balanced.py, test_balanced.py | No matched commit command/output |
| [C030](#C030) · `2f9bf86` | Probe sample selector priority and repeated collection semantics | assignment_results.jsonl, balanced_results.jsonl, larger_stress.jsonl, probe_samples.py, refined_radio.jsonl, stress_500.jsonl | No matched commit command/output |
| [C031](#C031) · `6b263fc` | Avoid repeatedly collecting the wrong material near overlapping sample sites | approach.py, assignment_results.jsonl, balanced_results.jsonl, refined_radio.jsonl, stress_500.jsonl | [E0085](01_timeline.md#E0085) |
| [C032](#C032) · `fd291b6` | Add a sample-first scheduling candidate for comparative evaluation | sample_priority.py, test_priority.py | [E0092](01_timeline.md#E0092) |
| [C033](#C033) · `c1d186e` | Evaluate navigation edges matching full per-step motion bounds | assignment_results.jsonl, navigation_candidate.py, sample_priority_results.jsonl, stress_500.jsonl, test_navigation.py | [E0100](01_timeline.md#E0100) |
| [C034](#C034) · `34dc5d6` | Preserve comparison data and add sample scheduling trace | debug_priority.py, navigation_results.jsonl, sample_priority_results.jsonl, stress_500.jsonl | [E0107](01_timeline.md#E0107) |
| [C035](#C035) · `5e42672` | Use full-motion navigation and favor collecting samples along outbound routes | approach.py, stress_500.jsonl | [E0113](01_timeline.md#E0113) |
| [C036](#C036) · `c7180a4` | Compare balanced task ownership from small abstract route optimization | combined_results.jsonl, test_tour.py, tour_candidate.py | [E0122](01_timeline.md#E0122) |
| [C037](#C037) · `e57842e` | Treat refused calibration as evidence against every predicted image at that viewpoint | approach.py, failure_15_None.json, tour_candidate.py, tour_results.jsonl, validation_combined.jsonl | [E0130](01_timeline.md#E0130) |
| [C038](#C038) · `1a3f4c1` | Compare following the task order from the compact routing model | ordered_candidate.py, test_ordered.py, tour_fixed.jsonl, validation_combined.jsonl | [E0139](01_timeline.md#E0139) |
| [C039](#C039) · `2e4955b` | Document the validated controller and preserve comparison results | approach.py, final_four_check.jsonl, final_mixed_check.jsonl, ordered_results.jsonl | [E0144](01_timeline.md#E0144) |
| [C040](#C040) · `7cc4641` | Record final 200-episode validation with all goals completed | final_four_check.jsonl, final_mixed_check.jsonl, validation_summary.json | [E0158](01_timeline.md#E0158) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `9afebcc4567cde1b8b54326e22dfcb1cbd708457`; parents: none (initial snapshot). Recorded author date: 2026-09-20T03:46:11+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_9afebcc.diff)

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
index 0000000..563f88b
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1 @@
           1 +{"host": "127.0.0.1", "port": 18081, "token": "3d4623701a2ddf2ae2896fe93fd7bf2d", "observation_space": {"type": "ObjectCentric", "types": [{"name": "lander", "parent": null, "features": ["x", "y", "z"]}, {"name": "objective", "parent": null, "features": ["x", "y", "z", "have_image_rover0", "have_image_rover1", "received_image"]}, {"name": "obstacle", "parent": null, "features": ["x", "y", "z", "half_x", "half_y", "half_z"]}, {"name": "rover", "parent": null, "features": ["x", "y", "theta", "store_full", "calibrated", "at_home"]}, {"name": "sample", "parent": null, "features": ["x", "y", "z", "is_soil", "analyzed_rover0", "analyzed_rover1", "received_analysis"]}]}, "action_space": {"type": "Box", "shape": [8], "low": [-0.20000000298023224, -0.20000000298023224, -0.4000000059604645, -1.0, -0.20000000298023224, -0.20000000298023224, -0.4000000059604645, -1.0], "high": [0.20000000298023224, 0.20000000298023224, 0.4000000059604645, 1.0, 0.20000000298023224, 0.20000000298023224, 0.4000000059604645, 1.0], "dtype": "float32"}, "max_steps": 1000, "primitives": [], "strict": true}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Add initial observation probe

Commit `761887dbff1e2942ebe943d7ae74be9c61af0e1e`; parents: 9afebcc4567cde1b8b54326e22dfcb1cbd708457. Recorded author date: 2026-09-20T03:46:40+02:00.

File roles (automatic): diagnostic/test.

- [E0007](01_timeline.md#E0007): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C002_761887d.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/inspect_env.py b/inspect_env.py
new file mode 100644
index 0000000..9dbc53b
--- /dev/null
+++ b/inspect_env.py
@@ -0,0 +1,8 @@
           1 +from env_client import make_env
           2 +E=make_env(); s,info=E.reset(seed=0)
           3 +print('INFO',info,'max',E.max_steps)
           4 +for t in E.observation_space.types:
           5 + print('TYPE',t)
           6 + for o in s.get_objects(t):
           7 +  print(str(o),[(f,s.get(o,f)) for f in E.observation_space.type_features[t]])
           8 +E.close()
```

</details>

<a id="C003"></a>
### C003 · Add initial geometry observation probe

Commit `9c8f0e94ede4353666f40be4487d702223d14905`; parents: 761887dbff1e2942ebe943d7ae74be9c61af0e1e. Recorded author date: 2026-09-20T03:46:59+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C003_9c8f0e9.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_geometry.py b/probe_geometry.py
new file mode 100644
index 0000000..073b9fa
--- /dev/null
+++ b/probe_geometry.py
@@ -0,0 +1,10 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +e=make_env();s,i=e.reset(seed=0)
           5 +print('info',i,'max_steps',e.max_steps)
           6 +print('types',e.observation_space.type_features)
           7 +for n in s.get_object_names():
           8 + o=s.get_object_from_name(n)
           9 + print(n,[(f,s.get(o,f)) for f in e.observation_space.type_features[o.type]])
          10 +e.close()
```

</details>

<a id="C004"></a>
### C004 · Probe motion scale and static wall collision

Commit `9bac1cd2df09557f5209075b1add81601c502b98`; parents: 9c8f0e94ede4353666f40be4487d702223d14905. Recorded author date: 2026-09-20T03:47:17+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C004_9bac1cd.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_geometry.py b/probe_geometry.py
index 073b9fa..35f88b2 100644
--- a/probe_geometry.py
+++ b/probe_geometry.py
@@ -2,9 +2,17 @@ from env_client import make_env
    2      2  import numpy as np
    3      3  
    4      4  e=make_env();s,i=e.reset(seed=0)
    5        -print('info',i,'max_steps',e.max_steps)
    6        -print('types',e.observation_space.type_features)
    7        -for n in s.get_object_names():
    8        - o=s.get_object_from_name(n)
    9        - print(n,[(f,s.get(o,f)) for f in e.observation_space.type_features[o.type]])
           5 +print('action',e.action_space.low,e.action_space.high)
           6 +def pos(j=0):
           7 + o=s.get_object_from_name('rover'+str(j));return tuple(round(float(s.get(o,f)),4) for f in ('x','y','theta','calibrated','at_home'))
           8 +def act(dx=0,dy=0,op=0,j=0,dt=0):
           9 + global s
          10 + a=np.zeros(8,dtype=np.float32);a[4*j:4*j+4]=[dx,dy,dt,op]
          11 + s,r,t,tr,i=e.step(a);return pos(j)
          12 +print('start',pos())
          13 +print('x input .2',act(.2))
          14 +print('x input 1',act(1))
          15 +print('north',*[act(dy=1) for _ in range(13)])
          16 +print('west',*[act(dx=-1) for _ in range(10)])
          17 +print('north2',*[act(dy=1,op=-.5) for _ in range(8)])
   10     18  e.close()
```

</details>

<a id="C005"></a>
### C005 · Add camera visibility probes across candidate viewpoints

Commit `95c9e620f775847d4e6ba5415d01e7fd2e26e589`; parents: 9bac1cd2df09557f5209075b1add81601c502b98. Recorded author date: 2026-09-20T03:47:30+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C005_95c9e62.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_camera.py b/probe_camera.py
new file mode 100644
index 0000000..666a03d
--- /dev/null
+++ b/probe_camera.py
@@ -0,0 +1,33 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +import json
           4 +
           5 +def run(seed, x, y):
           6 + e=make_env();s,_=e.reset(seed=seed)
           7 + rovers=[s.get_object_from_name('rover'+str(i)) for i in range(2)]
           8 + objs=list(s.get_objects(e.observation_space.get_type('objective')))
           9 + targets=[(abs(x),y),(-abs(x),y)]
          10 + for axis in [0,1]:
          11 +  for k in range(25):
          12 +   a=np.zeros(8)
          13 +   done=True
          14 +   for i,r in enumerate(rovers):
          15 +    diff=targets[i][axis]-s.get(r,['x','y'][axis]);a[4*i+axis]=np.clip(diff,-.2,.2)
          16 +    if abs(diff)>.001:done=False
          17 +   if done:break
          18 +   s,*_=e.step(a)
          19 + a=np.zeros(8);a[[3,7]]=-.5
          20 + s,*_=e.step(a)
          21 + cal=[s.get(r,'calibrated') for r in rovers]
          22 + a[[3,7]]=-1/6
          23 + s,*_=e.step(a)
          24 + images=[[o.name for o in objs if s.get(o,'have_image_rover'+str(i))] for i in range(2)]
          25 + result={'seed':seed,'wanted':[x,y],'xy':[[s.get(r,'x'),s.get(r,'y')] for r in rovers], 'cal':cal,'images':images,'objectives':[[o.name,s.get(o,'x'),s.get(o,'y')] for o in objs]}
          26 + e.close();return result
          27 +if __name__=='__main__':
          28 + out=[]
          29 + for seed in [0,1,2]:
          30 +  for x in [.4,1.,1.6,2.1]:
          31 +   for y in [.3,.8,1.3]:
          32 +    r=run(seed,x,y);out.append(r);print(json.dumps(r),flush=True)
          33 + with open('probe_camera_results.json','w') as f:json.dump(out,f)
```

</details>

<a id="C006"></a>
### C006 · Map center wall extent with independent crossing probes

Commit `2777b78986fb3c3fa0e38dd17aede602a6da6f68`; parents: 95c9e620f775847d4e6ba5415d01e7fd2e26e589. Recorded author date: 2026-09-20T03:47:43+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C006_2777b78.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_camera.log b/probe_camera.log
new file mode 100644
index 0000000..7325be5
--- /dev/null
+++ b/probe_camera.log
@@ -0,0 +1,25 @@
           1 +{"seed": 0, "wanted": [0.4, 0.3], "xy": [[0.4000000059604645, 0.30000001192092896], [-0.4000000059604645, 0.30000001192092896]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective0"]], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
           2 +{"seed": 0, "wanted": [0.4, 0.8], "xy": [[0.4000000059604645, 0.800000011920929], [-0.4000000059604645, 0.800000011920929]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective0"]], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
           3 +{"seed": 0, "wanted": [0.4, 1.3], "xy": [[0.4000000059604645, 0.8500000238418579], [-0.4000000059604645, 1.2999999523162842]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective0"]], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
           4 +{"seed": 0, "wanted": [1.0, 0.3], "xy": [[1.0, 0.30000001192092896], [-1.0, -0.15000000596046448]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
           5 +{"seed": 0, "wanted": [1.0, 0.8], "xy": [[1.0, 0.800000011920929], [-1.0, -0.15000000596046448]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
           6 +{"seed": 0, "wanted": [1.0, 1.3], "xy": [[1.0, 1.2999999523162842], [-1.0, -0.15000000596046448]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
           7 +{"seed": 0, "wanted": [1.6, 0.3], "xy": [[1.5999999046325684, 0.30000001192092896], [-1.2000000476837158, 0.30000001192092896]], "cal": [1.0, 1.0], "images": [["objective1"], ["objective2"]], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
           8 +{"seed": 0, "wanted": [1.6, 0.8], "xy": [[1.5999999046325684, 0.800000011920929], [-1.2000000476837158, 0.25]], "cal": [1.0, 0.0], "images": [["objective1"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
           9 +{"seed": 0, "wanted": [1.6, 1.3], "xy": [[1.5999999046325684, 1.2999999523162842], [-1.2000000476837158, 0.25]], "cal": [1.0, 0.0], "images": [["objective1"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
          10 +{"seed": 0, "wanted": [2.1, 0.3], "xy": [[2.0999999046325684, 0.30000001192092896], [-1.2000000476837158, 0.30000001192092896]], "cal": [1.0, 1.0], "images": [["objective1"], ["objective2"]], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
          11 +{"seed": 0, "wanted": [2.1, 0.8], "xy": [[2.0999999046325684, 0.800000011920929], [-1.2000000476837158, 0.25]], "cal": [1.0, 0.0], "images": [["objective1"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
          12 +{"seed": 0, "wanted": [2.1, 1.3], "xy": [[2.0999999046325684, 1.2999999523162842], [-1.2000000476837158, 0.25]], "cal": [1.0, 0.0], "images": [["objective1"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}
          13 +{"seed": 1, "wanted": [0.4, 0.3], "xy": [[0.4000000059604645, -1.350000023841858], [-0.4000000059604645, -0.75]], "cal": [0.0, 0.0], "images": [[], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          14 +{"seed": 1, "wanted": [0.4, 0.8], "xy": [[0.4000000059604645, -1.350000023841858], [-0.4000000059604645, -0.75]], "cal": [0.0, 0.0], "images": [[], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          15 +{"seed": 1, "wanted": [0.4, 1.3], "xy": [[0.4000000059604645, -1.350000023841858], [-0.4000000059604645, -0.75]], "cal": [0.0, 0.0], "images": [[], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          16 +{"seed": 1, "wanted": [1.0, 0.3], "xy": [[1.0, 0.30000001192092896], [-1.0, 0.05000000074505806]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          17 +{"seed": 1, "wanted": [1.0, 0.8], "xy": [[1.0, 0.800000011920929], [-1.0, 0.05000000074505806]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          18 +{"seed": 1, "wanted": [1.0, 1.3], "xy": [[1.0, 1.2999999523162842], [-1.0, 0.05000000074505806]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          19 +{"seed": 1, "wanted": [1.6, 0.3], "xy": [[1.5999999046325684, 0.30000001192092896], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          20 +{"seed": 1, "wanted": [1.6, 0.8], "xy": [[1.5999999046325684, 0.800000011920929], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          21 +{"seed": 1, "wanted": [1.6, 1.3], "xy": [[1.5999999046325684, 1.2999999523162842], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          22 +{"seed": 1, "wanted": [2.1, 0.3], "xy": [[2.0999999046325684, 0.30000001192092896], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          23 +{"seed": 1, "wanted": [2.1, 0.8], "xy": [[2.0999999046325684, 0.800000011920929], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          24 +{"seed": 1, "wanted": [2.1, 1.3], "xy": [[2.0999999046325684, 1.2999999523162842], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
          25 +{"seed": 2, "wanted": [0.4, 0.3], "xy": [[0.4000000059604645, 0.30000001192092896], [-0.4000000059604645, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
diff --git a/probe_geometry.py b/probe_geometry.py
index 35f88b2..7deb0ef 100644
--- a/probe_geometry.py
+++ b/probe_geometry.py
@@ -1,18 +1,16 @@
    1      1  from env_client import make_env
    2      2  import numpy as np
    3      3  
    4        -e=make_env();s,i=e.reset(seed=0)
    5        -print('action',e.action_space.low,e.action_space.high)
    6        -def pos(j=0):
    7        - o=s.get_object_from_name('rover'+str(j));return tuple(round(float(s.get(o,f)),4) for f in ('x','y','theta','calibrated','at_home'))
    8        -def act(dx=0,dy=0,op=0,j=0,dt=0):
    9        - global s
   10        - a=np.zeros(8,dtype=np.float32);a[4*j:4*j+4]=[dx,dy,dt,op]
   11        - s,r,t,tr,i=e.step(a);return pos(j)
   12        -print('start',pos())
   13        -print('x input .2',act(.2))
   14        -print('x input 1',act(1))
   15        -print('north',*[act(dy=1) for _ in range(13)])
   16        -print('west',*[act(dx=-1) for _ in range(10)])
   17        -print('north2',*[act(dy=1,op=-.5) for _ in range(8)])
   18        -e.close()
           4 +def trial(y):
           5 + e=make_env();s,_=e.reset(seed=0);o=s.get_object_from_name('rover0')
           6 + def p():return np.array([s.get(o,'x'),s.get(o,'y')])
           7 + def go(target):
           8 +  nonlocal s
           9 +  for k in range(40):
          10 +   q=p();d=np.clip(np.array(target)-q,-.2,.2)
          11 +   if max(abs(d))<1e-5:return
          12 +   a=np.zeros(8);a[:2]=d;s,*_=e.step(a)
          13 +   if np.linalg.norm(p()-q)<1e-7:return
          14 + go((1.0,y));start=p();go((-.5,y));print('cross',y,'start',start,'end',p())
          15 + e.close()
          16 +for y in [-2.4,-1.75,-1.5,-1.3,-1.2,-1.0,0,1,1.3,1.5,1.65]:trial(y)
```

</details>

<a id="C007"></a>
### C007 · Implement geometric navigation with concurrent sampling imaging and radio tasks

Commit `f17dd4f3a77f0d141c2b0b5489f9c47344c4ad20`; parents: 2777b78986fb3c3fa0e38dd17aede602a6da6f68. Recorded author date: 2026-09-20T03:48:02+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0015](01_timeline.md#E0015): commit hash in recorded output.
[Controller after this commit](evidence/versions/C007_f17dd4f_approach.py) · [Exact all-file diff](evidence/diffs/C007_f17dd4f.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..1b84da8
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,127 @@
           1 +import numpy as np
           2 +from scipy.sparse import csr_matrix
           3 +from scipy.sparse.csgraph import dijkstra
           4 +
           5 +class GeneratedApproach:
           6 +    def __init__(self, action_space, observation_space, primitives):
           7 +        self.space = observation_space
           8 +    def objects(self, s, t):
           9 +        return s.get_objects(self.space.get_type(t))
          10 +    def xy(self,s,o):
          11 +        return np.array([s.get(o,'x'),s.get(o,'y')])
          12 +    def reset(self,state,info):
          13 +        self.rovers=[state.get_object_from_name('rover'+str(i)) for i in range(2)]
          14 +        self.homes=[self.xy(state,r) for r in self.rovers]
          15 +        self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
          16 +        self.lander=self.xy(state,self.objects(state,'lander')[0])
          17 +        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,1.5]])
          18 +        self.axis=np.arange(-2.3,2.301,0.1)
          19 +        self.n=len(self.axis)
          20 +        self.points=np.array([(x,y) for x in self.axis for y in self.axis])
          21 +        self.valid=self.free(self.points)
          22 +        self.bad=np.zeros((2,len(self.points),len(self.objs)),dtype=bool)
          23 +        self.prev=None; self.step=0
          24 +        self.make_graph()
          25 +    def free(self,p):
          26 +        p=np.atleast_2d(p)
          27 +        d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
          28 +        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.19**2,axis=1)
          29 +        ok &= np.linalg.norm(p-self.lander,axis=1)>.55
          30 +        return ok
          31 +    def make_graph(self):
          32 +        rows=[]; cols=[]
          33 +        for i in np.flatnonzero(self.valid):
          34 +            x,y=divmod(i,self.n)
          35 +            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
          36 +                xx,yy=x+dx,y+dy
          37 +                if 0<=xx<self.n and 0<=yy<self.n:
          38 +                    j=xx*self.n+yy
          39 +                    if self.valid[j]: rows.append(i);cols.append(j)
          40 +        self.graph=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(self.points),len(self.points)))
          41 +    def visible(self,p,target,limit):
          42 +        p=np.atleast_2d(p); target=np.asarray(target)
          43 +        ok=np.linalg.norm(p-target,axis=1)<limit-.025
          44 +        # Low mounds do not occlude the camera, but pillars and wall do.
          45 +        boxes=self.boxes[(self.boxes[:,2]<.2)]
          46 +        delta=target-p
          47 +        for b in boxes:
          48 +            lo=b[:2]-b[2:];hi=b[:2]+b[2:]
          49 +            with np.errstate(divide='ignore',invalid='ignore'):
          50 +                t1=(lo-p)/delta;t2=(hi-p)/delta
          51 +            near=np.maximum(np.min(np.stack([t1,t2]),axis=0).max(axis=1),.001)
          52 +            far=np.minimum(np.max(np.stack([t1,t2]),axis=0).min(axis=1),.999)
          53 +            ok &= near>far
          54 +        return ok
          55 +    def nearest(self,p):
          56 +        ds=np.sum((self.points-p)**2,axis=1);ds[~self.valid]=np.inf
          57 +        return int(np.argmin(ds))
          58 +    def get_action(self,s):
          59 +        self.step+=1
          60 +        pos=[self.xy(s,r) for r in self.rovers]
          61 +        if self.prev is not None:
          62 +            for i in range(2):
          63 +                old,move,op,idx=self.prev[i]
          64 +                if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
          65 +                    q=old+move
          66 +                    ids=np.linalg.norm(self.points-q,axis=1)<.085
          67 +                    self.valid[ids]=False
          68 +                    self.make_graph()
          69 +                if op in [-.5,-1/6] and idx is not None:
          70 +                    if op==-.5 and not s.get(self.rovers[i],'calibrated'):
          71 +                        self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
          72 +        action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
          73 +        received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
          74 +        acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
          75 +        for i,r in enumerate(self.rovers):
          76 +            p=pos[i]; start=self.nearest(p)
          77 +            dist,pred=dijkstra(self.graph,indices=start,return_predecessors=True)
          78 +            candidates=[]
          79 +            for k in [0,1]:
          80 +                if not acquired[k] and k not in kinds and not s.get(r,'store_full'):
          81 +                    for o in self.samples:
          82 +                        if int(s.get(o,'is_soil'))==k:
          83 +                            mask=np.linalg.norm(self.points-self.xy(s,o),axis=1)<.24
          84 +                            candidates.append((mask,'sample',o,k))
          85 +            for j,o in enumerate(self.objs):
          86 +                if not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]) and j not in assigned:
          87 +                    mask=self.visible(self.points,self.xy(s,o),2)&~self.bad[i,:,j]
          88 +                    candidates.append((mask,'image',o,j))
          89 +            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
          90 +            if pending: candidates.append((self.visible(self.points,self.lander,4),'send',None,None))
          91 +            best=None; score=np.inf
          92 +            for mask,task,o,j in candidates:
          93 +                dd=dist.copy();dd[~mask]=np.inf
          94 +                target=int(np.argmin(dd)); cost=dd[target]
          95 +                if task=='send': cost+=5 if any(c[1]!='send' for c in candidates) else 0
          96 +                if cost<score: score=cost;best=(target,task,o,j)
          97 +            if best is None: best=(self.nearest(self.homes[i]),'home',None,None)
          98 +            target,task,o,j=best
          99 +            if task=='sample': kinds.add(j)
         100 +            if task=='image': assigned.add(j)
         101 +            targetpos=self.points[target]
         102 +            if task=='home': targetpos=self.homes[i]
         103 +            path=[target];cur=target
         104 +            for _ in range(len(self.points)):
         105 +                if cur==start:break
         106 +                cur=int(pred[cur])
         107 +                if cur<0:break
         108 +                path.append(cur)
         109 +            path=path[::-1]
         110 +            goal=targetpos
         111 +            for node in path:
         112 +                q=self.points[node]
         113 +                if np.max(np.abs(q-p))<=.20001: goal=q
         114 +                else: break
         115 +            if np.max(np.abs(targetpos-p))<=.2:goal=targetpos
         116 +            move=np.clip(goal-p,-.2,.2)
         117 +            if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
         118 +            q=p+move; op=0.;idx=None
         119 +            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249:op=-5/6
         120 +            elif task=='image' and self.visible(q,self.xy(s,o),2)[0]:
         121 +                op=-1/6 if s.get(r,'calibrated') else -.5;idx=j
         122 +            elif pending and self.visible(q,self.lander,4)[0]:op=.5
         123 +            elif s.get(r,'store_full'):op=5/6
         124 +            action[4*i:4*i+2]=move;action[4*i+3]=op
         125 +            records.append((p,move,op,idx))
         126 +        self.prev=records
         127 +        return action
diff --git a/probe_camera.log b/probe_camera.log
index 7325be5..713a2e5 100644
--- a/probe_camera.log
+++ b/probe_camera.log
@@ -23,3 +23,14 @@
   23     23  {"seed": 1, "wanted": [2.1, 0.8], "xy": [[2.0999999046325684, 0.800000011920929], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
   24     24  {"seed": 1, "wanted": [2.1, 1.3], "xy": [[2.0999999046325684, 1.2999999523162842], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}
   25     25  {"seed": 2, "wanted": [0.4, 0.3], "xy": [[0.4000000059604645, 0.30000001192092896], [-0.4000000059604645, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          26 +{"seed": 2, "wanted": [0.4, 0.8], "xy": [[0.4000000059604645, 0.800000011920929], [-0.4000000059604645, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          27 +{"seed": 2, "wanted": [0.4, 1.3], "xy": [[0.4000000059604645, 1.2999999523162842], [-0.4000000059604645, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          28 +{"seed": 2, "wanted": [1.0, 0.3], "xy": [[1.0, 0.30000001192092896], [-1.0, 0.30000001192092896]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          29 +{"seed": 2, "wanted": [1.0, 0.8], "xy": [[1.0, 0.800000011920929], [-1.0, 0.800000011920929]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          30 +{"seed": 2, "wanted": [1.0, 1.3], "xy": [[1.0, 1.2999999523162842], [-1.0, 0.8500000238418579]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          31 +{"seed": 2, "wanted": [1.6, 0.3], "xy": [[1.5999999046325684, -0.949999988079071], [-1.2000000476837158, 0.30000001192092896]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          32 +{"seed": 2, "wanted": [1.6, 0.8], "xy": [[1.5999999046325684, -0.949999988079071], [-1.2000000476837158, 0.800000011920929]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          33 +{"seed": 2, "wanted": [1.6, 1.3], "xy": [[1.5999999046325684, -0.949999988079071], [-1.2000000476837158, 1.2999999523162842]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          34 +{"seed": 2, "wanted": [2.1, 0.3], "xy": [[2.0999999046325684, -1.350000023841858], [-1.2000000476837158, 0.30000001192092896]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          35 +{"seed": 2, "wanted": [2.1, 0.8], "xy": [[2.0999999046325684, -1.350000023841858], [-1.2000000476837158, 0.800000011920929]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
          36 +{"seed": 2, "wanted": [2.1, 1.3], "xy": [[2.0999999046325684, -1.350000023841858], [-1.2000000476837158, 1.2999999523162842]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}
diff --git a/probe_camera_results.json b/probe_camera_results.json
new file mode 100644
index 0000000..e73b74c
--- /dev/null
+++ b/probe_camera_results.json
@@ -0,0 +1 @@
           1 +[{"seed": 0, "wanted": [0.4, 0.3], "xy": [[0.4000000059604645, 0.30000001192092896], [-0.4000000059604645, 0.30000001192092896]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective0"]], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [0.4, 0.8], "xy": [[0.4000000059604645, 0.800000011920929], [-0.4000000059604645, 0.800000011920929]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective0"]], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [0.4, 1.3], "xy": [[0.4000000059604645, 0.8500000238418579], [-0.4000000059604645, 1.2999999523162842]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective0"]], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [1.0, 0.3], "xy": [[1.0, 0.30000001192092896], [-1.0, -0.15000000596046448]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [1.0, 0.8], "xy": [[1.0, 0.800000011920929], [-1.0, -0.15000000596046448]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [1.0, 1.3], "xy": [[1.0, 1.2999999523162842], [-1.0, -0.15000000596046448]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [1.6, 0.3], "xy": [[1.5999999046325684, 0.30000001192092896], [-1.2000000476837158, 0.30000001192092896]], "cal": [1.0, 1.0], "images": [["objective1"], ["objective2"]], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [1.6, 0.8], "xy": [[1.5999999046325684, 0.800000011920929], [-1.2000000476837158, 0.25]], "cal": [1.0, 0.0], "images": [["objective1"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [1.6, 1.3], "xy": [[1.5999999046325684, 1.2999999523162842], [-1.2000000476837158, 0.25]], "cal": [1.0, 0.0], "images": [["objective1"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [2.1, 0.3], "xy": [[2.0999999046325684, 0.30000001192092896], [-1.2000000476837158, 0.30000001192092896]], "cal": [1.0, 1.0], "images": [["objective1"], ["objective2"]], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [2.1, 0.8], "xy": [[2.0999999046325684, 0.800000011920929], [-1.2000000476837158, 0.25]], "cal": [1.0, 0.0], "images": [["objective1"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 0, "wanted": [2.1, 1.3], "xy": [[2.0999999046325684, 1.2999999523162842], [-1.2000000476837158, 0.25]], "cal": [1.0, 0.0], "images": [["objective1"], []], "objectives": [["objective0", 0.6602243185043335, 1.9191694259643555], ["objective1", 1.9636701345443726, 2.109961986541748], ["objective2", -1.8657476902008057, 2.1903953552246094]]}, {"seed": 1, "wanted": [0.4, 0.3], "xy": [[0.4000000059604645, -1.350000023841858], [-0.4000000059604645, -0.75]], "cal": [0.0, 0.0], "images": [[], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [0.4, 0.8], "xy": [[0.4000000059604645, -1.350000023841858], [-0.4000000059604645, -0.75]], "cal": [0.0, 0.0], "images": [[], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [0.4, 1.3], "xy": [[0.4000000059604645, -1.350000023841858], [-0.4000000059604645, -0.75]], "cal": [0.0, 0.0], "images": [[], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [1.0, 0.3], "xy": [[1.0, 0.30000001192092896], [-1.0, 0.05000000074505806]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [1.0, 0.8], "xy": [[1.0, 0.800000011920929], [-1.0, 0.05000000074505806]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [1.0, 1.3], "xy": [[1.0, 1.2999999523162842], [-1.0, 0.05000000074505806]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [1.6, 0.3], "xy": [[1.5999999046325684, 0.30000001192092896], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [1.6, 0.8], "xy": [[1.5999999046325684, 0.800000011920929], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [1.6, 1.3], "xy": [[1.5999999046325684, 1.2999999523162842], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [2.1, 0.3], "xy": [[2.0999999046325684, 0.30000001192092896], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [2.1, 0.8], "xy": [[2.0999999046325684, 0.800000011920929], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 1, "wanted": [2.1, 1.3], "xy": [[2.0999999046325684, 1.2999999523162842], [-1.2000000476837158, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 2.117588520050049, 1.9229792356491089], ["objective1", -2.114065170288086, 2.0957462787628174]]}, {"seed": 2, "wanted": [0.4, 0.3], "xy": [[0.4000000059604645, 0.30000001192092896], [-0.4000000059604645, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [0.4, 0.8], "xy": [[0.4000000059604645, 0.800000011920929], [-0.4000000059604645, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [0.4, 1.3], "xy": [[0.4000000059604645, 1.2999999523162842], [-0.4000000059604645, -0.949999988079071]], "cal": [1.0, 0.0], "images": [["objective0"], []], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [1.0, 0.3], "xy": [[1.0, 0.30000001192092896], [-1.0, 0.30000001192092896]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [1.0, 0.8], "xy": [[1.0, 0.800000011920929], [-1.0, 0.800000011920929]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [1.0, 1.3], "xy": [[1.0, 1.2999999523162842], [-1.0, 0.8500000238418579]], "cal": [1.0, 1.0], "images": [["objective0"], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [1.6, 0.3], "xy": [[1.5999999046325684, -0.949999988079071], [-1.2000000476837158, 0.30000001192092896]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [1.6, 0.8], "xy": [[1.5999999046325684, -0.949999988079071], [-1.2000000476837158, 0.800000011920929]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [1.6, 1.3], "xy": [[1.5999999046325684, -0.949999988079071], [-1.2000000476837158, 1.2999999523162842]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [2.1, 0.3], "xy": [[2.0999999046325684, -1.350000023841858], [-1.2000000476837158, 0.30000001192092896]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [2.1, 0.8], "xy": [[2.0999999046325684, -1.350000023841858], [-1.2000000476837158, 0.800000011920929]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}, {"seed": 2, "wanted": [2.1, 1.3], "xy": [[2.0999999046325684, -1.350000023841858], [-1.2000000476837158, 1.2999999523162842]], "cal": [0.0, 1.0], "images": [[], ["objective2"]], "objectives": [["objective0", 0.4399506747722626, 1.8454203605651855], ["objective1", -2.1755123138427734, 1.8365923166275024], ["objective2", -0.4921627342700958, 1.8822369575500488]]}]
\ No newline at end of file
```

</details>

<a id="C008"></a>
### C008 · Measure wall opening and arena margin on independent seed

Commit `51f7d9e85b87966a9ad21f8df4c8dd1605d9b2c9`; parents: f17dd4f3a77f0d141c2b0b5489f9c47344c4ad20. Recorded author date: 2026-09-20T03:48:19+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C008_51f7d9e.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_geometry.py b/probe_geometry.py
index 7deb0ef..f8a61f9 100644
--- a/probe_geometry.py
+++ b/probe_geometry.py
@@ -1,16 +1,14 @@
    1      1  from env_client import make_env
    2      2  import numpy as np
    3        -
    4        -def trial(y):
    5        - e=make_env();s,_=e.reset(seed=0);o=s.get_object_from_name('rover0')
           3 +for target in [(0.2,-2.15),(0.2,-2.2),(0.2,-2.24),(.2,-2.25),(.2,-2.1),(.2,1.45),(.2,.5),(.2,-.5)]:
           4 + e=make_env();s,_=e.reset(seed=2);o=s.get_object_from_name('rover0')
    6      5   def p():return np.array([s.get(o,'x'),s.get(o,'y')])
    7        - def go(target):
    8        -  nonlocal s
           6 + def go(t):
           7 +  global s
    9      8    for k in range(40):
   10        -   q=p();d=np.clip(np.array(target)-q,-.2,.2)
           9 +   q=p();d=np.clip(np.array(t)-q,-.2,.2)
   11     10     if max(abs(d))<1e-5:return
   12     11     a=np.zeros(8);a[:2]=d;s,*_=e.step(a)
   13     12     if np.linalg.norm(p()-q)<1e-7:return
   14        - go((1.0,y));start=p();go((-.5,y));print('cross',y,'start',start,'end',p())
          13 + go((1.,target[1]));q=p();go(target);print(target,'pre',q,'end',p())
   15     14   e.close()
   16        -for y in [-2.4,-1.75,-1.5,-1.3,-1.2,-1.0,0,1,1.3,1.5,1.65]:trial(y)
```

</details>

<a id="C009"></a>
### C009 · Separate full center driving wall from camera occlusion and add episode tests

Commit `a6557ef1139e8e0132a844f77d27fc4e518b5c94`; parents: 51f7d9e85b87966a9ad21f8df4c8dd1605d9b2c9. Recorded author date: 2026-09-20T03:48:30+02:00.

File roles (automatic): diagnostic/test.

- [E0028](01_timeline.md#E0028): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C009_a6557ef.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..5614344
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import time,sys,json
           4 +seeds=[int(x) for x in sys.argv[1:]] or list(range(10))
           5 +for seed in seeds:
           6 + e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{})
           7 + start=time.time();p.reset(s,info); trace=[]
           8 + for step in range(1000):
           9 +  a=p.get_action(s);s,r,term,trunc,inf=e.step(a)
          10 +  if step%50==0:trace.append((step,[[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers],[[s.get(ob,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for ob in p.objs],a.tolist()))
          11 +  if term or trunc:break
          12 + print(json.dumps({'seed':seed,'n':info.get('object_count'),'steps':step+1,'success':term,'seconds':round(time.time()-start,2),'trace':trace if not term else []}),flush=True)
          13 + e.close()
```

</details>

<a id="C010"></a>
### C010 · Correct wall driving extent and omit it from visibility checks

Commit `b86fb776c02056e39dd886b7de1ac31ed8fe9289`; parents: a6557ef1139e8e0132a844f77d27fc4e518b5c94. Recorded author date: 2026-09-20T03:48:41+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0019](01_timeline.md#E0019): commit hash in recorded output.
[Controller after this commit](evidence/versions/C010_b86fb77_approach.py) · [Exact all-file diff](evidence/diffs/C010_b86fb77.diff)

[Previous saved controller snapshot](evidence/versions/C007_f17dd4f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1b84da8..ed46c43 100644
--- a/approach.py
+++ b/approach.py
@@ -14,7 +14,7 @@ class GeneratedApproach:
   14     14          self.homes=[self.xy(state,r) for r in self.rovers]
   15     15          self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
   16     16          self.lander=self.xy(state,self.objects(state,'lander')[0])
   17        -        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,1.5]])
          17 +        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,2.5]])
   18     18          self.axis=np.arange(-2.3,2.301,0.1)
   19     19          self.n=len(self.axis)
   20     20          self.points=np.array([(x,y) for x in self.axis for y in self.axis])
@@ -42,7 +42,7 @@ class GeneratedApproach:
   42     42          p=np.atleast_2d(p); target=np.asarray(target)
   43     43          ok=np.linalg.norm(p-target,axis=1)<limit-.025
   44     44          # Low mounds do not occlude the camera, but pillars and wall do.
   45        -        boxes=self.boxes[(self.boxes[:,2]<.2)]
          45 +        boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
   46     46          delta=target-p
   47     47          for b in boxes:
   48     48              lo=b[:2]-b[2:];hi=b[:2]+b[2:]
diff --git a/test_results.jsonl b/test_results.jsonl
new file mode 100644
index 0000000..e69de29
```

</details>

<a id="C011"></a>
### C011 · Probe rover radius, pillar corners, and lander footprint

Commit `58007891f65c5bef3d4658599af00479b10bc43a`; parents: b86fb776c02056e39dd886b7de1ac31ed8fe9289. Recorded author date: 2026-09-20T03:48:51+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C011_5800789.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_geometry.py b/probe_geometry.py
index f8a61f9..f714254 100644
--- a/probe_geometry.py
+++ b/probe_geometry.py
@@ -1,14 +1,18 @@
    1      1  from env_client import make_env
    2      2  import numpy as np
    3        -for target in [(0.2,-2.15),(0.2,-2.2),(0.2,-2.24),(.2,-2.25),(.2,-2.1),(.2,1.45),(.2,.5),(.2,-.5)]:
    4        - e=make_env();s,_=e.reset(seed=2);o=s.get_object_from_name('rover0')
           3 +
           4 +def run(seed,j,targets):
           5 + e=make_env();s,_=e.reset(seed=seed);o=s.get_object_from_name('rover'+str(j))
    5      6   def p():return np.array([s.get(o,'x'),s.get(o,'y')])
    6        - def go(t):
    7        -  global s
           7 + for t in targets:
    8      8    for k in range(40):
    9      9     q=p();d=np.clip(np.array(t)-q,-.2,.2)
   10        -   if max(abs(d))<1e-5:return
   11        -   a=np.zeros(8);a[:2]=d;s,*_=e.step(a)
   12        -   if np.linalg.norm(p()-q)<1e-7:return
   13        - go((1.,target[1]));q=p();go(target);print(target,'pre',q,'end',p())
          10 +   if max(abs(d))<1e-5:break
          11 +   a=np.zeros(8);a[4*j:4*j+2]=d;s,*_=e.step(a)
          12 +   if np.linalg.norm(p()-q)<1e-7:break
          13 +  print(seed,j,t,'actual',p())
   14     14   e.close()
          15 +run(0,0,[(1.1,.0713),(.9243,.0713),(.9143,.0613),(.9043,.0513)])
          16 +run(2,1,[(-1.0,-1.75),(-1.2,-1.75),(-1.4,-1.75),(-1.5,-1.75),(-1.6,-1.75)])
          17 +run(2,1,[(-1.,-1.1),(-1.9,-1.1),(-1.9,-1.2),(-1.9,-1.3),(-1.9,-1.4),(-1.9,-1.5)])
          18 +run(2,0,[(2.25,-1.75),(2.26,-1.75),(2.3,-1.75)])
```

</details>

<a id="C012"></a>
### C012 · Add concise trajectory debugger

Commit `aceb14a04746748e8beb615a7e6f2868ceafbc4c`; parents: 58007891f65c5bef3d4658599af00479b10bc43a. Recorded author date: 2026-09-20T03:49:05+02:00.

File roles (automatic): diagnostic/test.

- [E0025](01_timeline.md#E0025): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C012_aceb14a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/debug_run.py b/debug_run.py
new file mode 100644
index 0000000..2e8f120
--- /dev/null
+++ b/debug_run.py
@@ -0,0 +1,9 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import sys
           4 +E=make_env();s,info=E.reset(seed=int(sys.argv[1]) if len(sys.argv)>1 else 0);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info)
           5 +for t in range(120):
           6 + a=p.get_action(s);s,r,done,trunc,inf=E.step(a)
           7 + if t%5==0 or done:print(t,[[round(s.get(ro,k),3) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers],[[s.get(o,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for o in p.objs],a.round(2),flush=True)
           8 + if done:break
           9 +E.close()
diff --git a/test_results.jsonl b/test_results.jsonl
index e69de29..d429d3f 100644
--- a/test_results.jsonl
+++ b/test_results.jsonl
@@ -0,0 +1,2 @@
           1 +{"seed": 0, "n": 3, "steps": 1000, "success": false, "seconds": 23.86, "trace": [[0, [[0.8999999761581421, -1.899999976158142, 0.0, 0.0, 1.0], [-1.2000000476837158, -1.600000023841858, 0.0, 0.0, 0.0]], [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], [-0.10000000149011612, -0.15000000596046448, 0.0, 0.0, -0.20000000298023224, 0.15000000596046448, 0.0, 0.0]], [50, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [100, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [150, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [200, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [250, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [300, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [350, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [400, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [450, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [500, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [550, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [600, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [650, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [700, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [750, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [800, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [850, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [900, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [950, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]]]}
           2 +{"seed": 1, "n": 2, "steps": 29, "success": true, "seconds": 0.59, "trace": []}
```

</details>

<a id="C013"></a>
### C013 · Refine collision margins near lander and pillars

Commit `3c4c4b945a9dbffdc248df340818b197350805b1`; parents: aceb14a04746748e8beb615a7e6f2868ceafbc4c. Recorded author date: 2026-09-20T03:49:06+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C013_3c4c4b9.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_geometry.py b/probe_geometry.py
index f714254..6f9e20f 100644
--- a/probe_geometry.py
+++ b/probe_geometry.py
@@ -16,3 +16,7 @@ run(0,0,[(1.1,.0713),(.9243,.0713),(.9143,.0613),(.9043,.0513)])
   16     16  run(2,1,[(-1.0,-1.75),(-1.2,-1.75),(-1.4,-1.75),(-1.5,-1.75),(-1.6,-1.75)])
   17     17  run(2,1,[(-1.,-1.1),(-1.9,-1.1),(-1.9,-1.2),(-1.9,-1.3),(-1.9,-1.4),(-1.9,-1.5)])
   18     18  run(2,0,[(2.25,-1.75),(2.26,-1.75),(2.3,-1.75)])
          19 +run(2,0,[(2.27,-1.75),(2.28,-1.75),(2.29,-1.75)])
          20 +run(2,1,[(-1.25,-1.75),(-1.27,-1.75),(-1.28,-1.75),(-1.29,-1.75)])
          21 +run(2,1,[(-1.,-1.1),(-1.9,-1.1),(-1.9,-1.42),(-1.9,-1.44),(-1.9,-1.46),(-1.9,-1.48)])
          22 +run(0,0,[(1.1,.0213),(.8743,.0213),(.8643,.0113),(.8543,.0013),(.8443,-.0087)])
```

</details>

<a id="C014"></a>
### C014 · Probe image transmission across middle wall at known ranges

Commit `8ba0f2b4914b524b1ff86a54c92a230dddb4b32a`; parents: 3c4c4b945a9dbffdc248df340818b197350805b1. Recorded author date: 2026-09-20T03:49:43+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C014_8ba0f2b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/current_results.jsonl b/current_results.jsonl
new file mode 100644
index 0000000..df543bf
--- /dev/null
+++ b/current_results.jsonl
@@ -0,0 +1,2 @@
           1 +{"seed": 0, "n": 3, "steps": 37, "success": true, "seconds": 0.63, "trace": []}
           2 +{"seed": 1, "n": 2, "steps": 29, "success": true, "seconds": 0.6, "trace": []}
diff --git a/probe_radio.py b/probe_radio.py
new file mode 100644
index 0000000..2951e5b
--- /dev/null
+++ b/probe_radio.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +e=make_env();s,_=e.reset(seed=0);o=s.get_object_from_name('rover0')
           4 +def step(dx=0,dy=0,op=0):
           5 + global s
           6 + a=np.zeros(8);a[:4]=dx,dy,0,op;s,*_=e.step(a)
           7 +def p():return np.array([s.get(o,'x'),s.get(o,'y')])
           8 +def go(t):
           9 + for k in range(30):
          10 +  q=p();d=np.clip(np.array(t)-q,-.2,.2)
          11 +  if max(abs(d))<1e-5:break
          12 +  step(*d)
          13 +  if np.linalg.norm(p()-q)<1e-7:break
          14 +
          15 +def flags():return [(ob.name,s.get(ob,'have_image_rover0'),s.get(ob,'received_image')) for ob in s.get_objects(e.observation_space.get_type('objective'))]
          16 +go((1,.9));step(op=-.5);step(op=-1/6);print('camera',p(),flags())
          17 +for y in [.7,.5,.3,.1,-.1,-.3,-.5,-.7,-.9,-1.1,-1.3,-1.5,-1.75]:
          18 + go((1,y));step(op=.5);print('send',p(),flags())
          19 +e.close()
diff --git a/test_results.jsonl b/test_results.jsonl
index d429d3f..a8918dd 100644
--- a/test_results.jsonl
+++ b/test_results.jsonl
@@ -1,2 +1,4 @@
    1      1  {"seed": 0, "n": 3, "steps": 1000, "success": false, "seconds": 23.86, "trace": [[0, [[0.8999999761581421, -1.899999976158142, 0.0, 0.0, 1.0], [-1.2000000476837158, -1.600000023841858, 0.0, 0.0, 0.0]], [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], [-0.10000000149011612, -0.15000000596046448, 0.0, 0.0, -0.20000000298023224, 0.15000000596046448, 0.0, 0.0]], [50, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [100, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [150, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [200, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [250, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [300, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [350, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [400, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [450, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [500, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [550, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [600, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [650, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [700, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [750, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [800, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [850, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [900, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [950, [[1.7000000476837158, -1.100000023841858, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [7.152557657263969e-08, 2.3841860041784457e-08, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]]]}
    2      2  {"seed": 1, "n": 2, "steps": 29, "success": true, "seconds": 0.59, "trace": []}
           3 +{"seed": 2, "n": 3, "steps": 1000, "success": false, "seconds": 18.51, "trace": [[0, [[0.800000011920929, -1.600000023841858, 0.0, 0.0, 0.0], [-1.2000000476837158, -1.600000023841858, 0.0, 0.0, 0.0]], [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], [-0.20000000298023224, 0.15000000596046448, 0.0, 0.0, -0.20000000298023224, 0.15000000596046448, 0.0, 0.0]], [50, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [100, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [150, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [200, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [250, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [300, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [350, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [400, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [450, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [500, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [550, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [600, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [650, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [700, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [750, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [800, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [850, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [900, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [950, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]]]}
           4 +{"seed": 3, "n": 3, "steps": 26, "success": true, "seconds": 0.65, "trace": []}
```

</details>

<a id="C015"></a>
### C015 · Measure exact lander clearance and possible confounding pillars

Commit `e438150f25dceecf80da4a8e0b3b2c3123c0c8af`; parents: 8ba0f2b4914b524b1ff86a54c92a230dddb4b32a. Recorded author date: 2026-09-20T03:50:06+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C015_e438150.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/current_results.jsonl b/current_results.jsonl
index df543bf..4586d39 100644
--- a/current_results.jsonl
+++ b/current_results.jsonl
@@ -1,2 +1,3 @@
    1      1  {"seed": 0, "n": 3, "steps": 37, "success": true, "seconds": 0.63, "trace": []}
    2      2  {"seed": 1, "n": 2, "steps": 29, "success": true, "seconds": 0.6, "trace": []}
           3 +{"seed": 2, "n": 3, "steps": 1000, "success": false, "seconds": 22.86, "trace": [[0, [[0.800000011920929, -1.600000023841858, 0.0, 0.0, 0.0], [-1.2000000476837158, -1.600000023841858, 0.0, 0.0, 0.0]], [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], [-0.20000000298023224, 0.15000000596046448, 0.0, 0.0, -0.20000000298023224, 0.15000000596046448, 0.0, 0.0]], [50, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [100, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [150, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [200, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [250, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [300, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [350, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [400, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [450, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [500, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [550, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [600, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [650, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [700, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [750, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [800, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [850, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [900, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [950, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]]]}
diff --git a/probe_lander.py b/probe_lander.py
new file mode 100644
index 0000000..e9ff18b
--- /dev/null
+++ b/probe_lander.py
@@ -0,0 +1,17 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +e=make_env();s,_=e.reset(seed=2);o=s.get_object_from_name('rover1')
           4 +for ob in s.get_objects(e.observation_space.get_type('obstacle')):
           5 + x,y=s.get(ob,'x'),s.get(ob,'y')
           6 + if x<0 and y<-1: print('near',ob.name,x,y)
           7 +def go(t):
           8 + global s
           9 + for k in range(30):
          10 +  p=np.array([s.get(o,'x'),s.get(o,'y')]);d=np.clip(np.array(t)-p,-.2,.2)
          11 +  if max(abs(d))<1e-6:break
          12 +  a=np.zeros(8);a[4:6]=d;s,*_=e.step(a)
          13 +  q=np.array([s.get(o,'x'),s.get(o,'y')])
          14 +  if np.linalg.norm(q-p)<1e-7:break
          15 + print(t,s.get(o,'x'),s.get(o,'y'))
          16 +for t in [(-1.,-1.1),(-1.9,-1.1),(-1.9,-1.49),(-1.9,-1.495),(-1.9,-1.499),(-1.9,-1.5)]:go(t)
          17 +e.close()
diff --git a/visual_validation_20_29.jsonl b/visual_validation_20_29.jsonl
new file mode 100644
index 0000000..e69de29
```

</details>

<a id="C016"></a>
### C016 · Learn failed radio and camera viewpoints and refine rover collision radius

Commit `c7478172801f008c8ff0ed3cc284a44514b2c16f`; parents: e438150f25dceecf80da4a8e0b3b2c3123c0c8af. Recorded author date: 2026-09-20T03:50:17+02:00.

File roles (automatic): policy, setup/other.

- [E0039](01_timeline.md#E0039): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_c747817_approach.py) · [Exact all-file diff](evidence/diffs/C016_c747817.diff)

[Previous saved controller snapshot](evidence/versions/C010_b86fb77_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ed46c43..8ae1622 100644
--- a/approach.py
+++ b/approach.py
@@ -20,13 +20,15 @@ class GeneratedApproach:
   20     20          self.points=np.array([(x,y) for x in self.axis for y in self.axis])
   21     21          self.valid=self.free(self.points)
   22     22          self.bad=np.zeros((2,len(self.points),len(self.objs)),dtype=bool)
          23 +        self.send_bad=np.zeros((2,len(self.points)),dtype=bool)
   23     24          self.prev=None; self.step=0
   24     25          self.make_graph()
   25     26      def free(self,p):
   26     27          p=np.atleast_2d(p)
   27     28          d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
   28        -        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.19**2,axis=1)
          29 +        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.228**2,axis=1)
   29     30          ok &= np.linalg.norm(p-self.lander,axis=1)>.55
          31 +        ok &= np.max(np.abs(p),axis=1)<2.271
   30     32          return ok
   31     33      def make_graph(self):
   32     34          rows=[]; cols=[]
@@ -55,19 +57,23 @@ class GeneratedApproach:
   55     57      def nearest(self,p):
   56     58          ds=np.sum((self.points-p)**2,axis=1);ds[~self.valid]=np.inf
   57     59          return int(np.argmin(ds))
          60 +    def pending_count(self,s,i):
          61 +        return sum(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs)+sum(s.get(o,'analyzed_rover'+str(i)) and not s.get(o,'received_analysis') for o in self.samples)
   58     62      def get_action(self,s):
   59     63          self.step+=1
   60     64          pos=[self.xy(s,r) for r in self.rovers]
   61     65          if self.prev is not None:
   62     66              for i in range(2):
   63        -                old,move,op,idx=self.prev[i]
          67 +                old,move,op,idx,had=self.prev[i]
   64     68                  if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
   65     69                      q=old+move
   66     70                      ids=np.linalg.norm(self.points-q,axis=1)<.085
   67     71                      self.valid[ids]=False
   68     72                      self.make_graph()
          73 +                if op==.5 and self.pending_count(s,i)>=had:
          74 +                    self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
   69     75                  if op in [-.5,-1/6] and idx is not None:
   70        -                    if op==-.5 and not s.get(self.rovers[i],'calibrated'):
          76 +                    if (op==-.5 and not s.get(self.rovers[i],'calibrated')) or (op==-1/6 and not s.get(self.objs[idx],'have_image_rover'+str(i))):
   71     77                          self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
   72     78          action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
   73     79          received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
@@ -87,7 +93,7 @@ class GeneratedApproach:
   87     93                      mask=self.visible(self.points,self.xy(s,o),2)&~self.bad[i,:,j]
   88     94                      candidates.append((mask,'image',o,j))
   89     95              pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
   90        -            if pending: candidates.append((self.visible(self.points,self.lander,4),'send',None,None))
          96 +            if pending: candidates.append((self.visible(self.points,self.lander,4)&~self.send_bad[i],'send',None,None))
   91     97              best=None; score=np.inf
   92     98              for mask,task,o,j in candidates:
   93     99                  dd=dist.copy();dd[~mask]=np.inf
@@ -119,9 +125,9 @@ class GeneratedApproach:
  119    125              if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249:op=-5/6
  120    126              elif task=='image' and self.visible(q,self.xy(s,o),2)[0]:
  121    127                  op=-1/6 if s.get(r,'calibrated') else -.5;idx=j
  122        -            elif pending and self.visible(q,self.lander,4)[0]:op=.5
         128 +            elif pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
  123    129              elif s.get(r,'store_full'):op=5/6
  124    130              action[4*i:4*i+2]=move;action[4*i+3]=op
  125        -            records.append((p,move,op,idx))
         131 +            records.append((p,move,op,idx,self.pending_count(s,i)))
  126    132          self.prev=records
  127    133          return action
diff --git a/current_results.jsonl b/current_results.jsonl
index 4586d39..c9f16a9 100644
--- a/current_results.jsonl
+++ b/current_results.jsonl
@@ -1,3 +1,7 @@
    1      1  {"seed": 0, "n": 3, "steps": 37, "success": true, "seconds": 0.63, "trace": []}
    2      2  {"seed": 1, "n": 2, "steps": 29, "success": true, "seconds": 0.6, "trace": []}
    3      3  {"seed": 2, "n": 3, "steps": 1000, "success": false, "seconds": 22.86, "trace": [[0, [[0.800000011920929, -1.600000023841858, 0.0, 0.0, 0.0], [-1.2000000476837158, -1.600000023841858, 0.0, 0.0, 0.0]], [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], [-0.20000000298023224, 0.15000000596046448, 0.0, 0.0, -0.20000000298023224, 0.15000000596046448, 0.0, 0.0]], [50, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [100, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [150, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [200, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [250, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [300, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [350, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [400, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [450, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [500, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [550, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [600, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [650, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [700, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [750, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [800, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [850, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [900, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]], [950, [[1.0, -1.75, 0.0, 0.0, 1.0], [-2.200000047683716, 2.220446049250313e-15, 0.0, 0.0, 0.0]], [[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 1.0, 0.0]], [0.0, 0.0, 0.0, 0.0, -1.9073486612342094e-07, 0.0, 0.0, 0.5]]]}
           4 +{"seed": 3, "n": 3, "steps": 1000, "success": false, "seconds": 22.13, "trace": [[0, [[1.2000000476837158, -1.600000023841858, 0.0, 0.0, 0.0], [-1.2000000476837158, -1.600000023841858, 0.0, 0.0, 0.0]], [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], [0.20000000298023224, 0.15000000596046448, 0.0, 0.0, -0.20000000298023224, 0.15000000596046448, 0.0, 0.0]], [50, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [100, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [150, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [200, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [250, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [300, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [350, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [400, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [450, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [500, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [550, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [600, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [650, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [700, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [750, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [800, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [850, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [900, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]], [950, [[1.399999976158142, 0.20000000298023224, 0.0, 0.0, 0.0], [-1.0, -1.75, 0.0, 0.0, 1.0]], [[0.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [2.3841861818141297e-08, -2.980229840687798e-09, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0]]]}
           5 +{"seed": 4, "n": 3, "steps": 26, "success": true, "seconds": 0.67, "trace": []}
           6 +{"seed": 5, "n": 3, "steps": 35, "success": true, "seconds": 0.63, "trace": []}
           7 +{"seed": 6, "n": 2, "steps": 23, "success": true, "seconds": 0.64, "trace": []}
```

</details>

<a id="C017"></a>
### C017 · Add independent seeds20-29 validation with stalled-state detection

Commit `f3158c285e6569ef44ad3bf419587fc119ab1420`; parents: c7478172801f008c8ff0ed3cc284a44514b2c16f. Recorded author date: 2026-09-20T03:50:48+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C017_f3158c2.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/visual_validate.py b/visual_validate.py
new file mode 100644
index 0000000..e8fae60
--- /dev/null
+++ b/visual_validate.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import time,json
           4 +for seed in range(20,30):
           5 + e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{})
           6 + start=time.time();p.reset(s,info);trace=[];same=0;old=None
           7 + for step in range(300):
           8 +  a=p.get_action(s);s,r,term,trunc,inf=e.step(a)
           9 +  sig=repr([[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers])+repr([[s.get(ob,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for ob in p.objs])
          10 +  same=same+1 if sig==old else 0;old=sig
          11 +  if step%10==0 or same>15:trace.append((step,[[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers],[[s.get(ob,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for ob in p.objs],a.tolist()))
          12 +  if term or trunc or same>15:break
          13 + print(json.dumps({'seed':seed,'n':info.get('object_count'),'steps':step+1,'success':term,'seconds':round(time.time()-start,2),'trace':trace if not term else []}),flush=True)
          14 + e.close()
```

</details>

<a id="C018"></a>
### C018 · Add broad seed and variable-object-count regression checks

Commit `e73f4506ec4518871be3666dda4572d7d91b6343`; parents: f3158c285e6569ef44ad3bf419587fc119ab1420. Recorded author date: 2026-09-20T03:51:15+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0057](01_timeline.md#E0057): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C018_e73f450.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/current_results.jsonl b/current_results.jsonl
index c9f16a9..d269e69 100644
--- a/current_results.jsonl
+++ b/current_results.jsonl
@@ -5,3 +5,6 @@
    5      5  {"seed": 4, "n": 3, "steps": 26, "success": true, "seconds": 0.67, "trace": []}
    6      6  {"seed": 5, "n": 3, "steps": 35, "success": true, "seconds": 0.63, "trace": []}
    7      7  {"seed": 6, "n": 2, "steps": 23, "success": true, "seconds": 0.64, "trace": []}
           8 +{"seed": 7, "n": 3, "steps": 1000, "success": false, "seconds": 34.9, "trace": [[0, [[1.100000023841858, -1.600000023841858, 0.0, 0.0, 1.0], [-0.8999999761581421, -1.600000023841858, 0.0, 0.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], [0.10000000149011612, 0.15000000596046448, 0.0, 0.0, 0.10000000149011612, 0.15000000596046448, 0.0, 0.0]], [50, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [100, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [150, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [200, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [250, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [300, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [350, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [400, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [450, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [500, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [550, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [600, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [650, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [700, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [750, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [800, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [850, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [900, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]], [950, [[1.399999976158142, 0.29999998211860657, 0.0, 1.0, 0.0], [-1.0, -1.75, 0.0, 1.0, 1.0]], [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]], [-9.536742595628311e-08, -1.192092646817855e-08, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]]]}
           9 +{"seed": 8, "n": 3, "steps": 29, "success": true, "seconds": 0.77, "trace": []}
          10 +{"seed": 9, "n": 2, "steps": 27, "success": true, "seconds": 0.85, "trace": []}
diff --git a/revised_results.jsonl b/revised_results.jsonl
new file mode 100644
index 0000000..6d44a23
--- /dev/null
+++ b/revised_results.jsonl
@@ -0,0 +1,10 @@
           1 +{"seed": 0, "n": 3, "steps": 37, "success": true, "seconds": 1.36, "trace": []}
           2 +{"seed": 1, "n": 2, "steps": 23, "success": true, "seconds": 0.96, "trace": []}
           3 +{"seed": 2, "n": 3, "steps": 23, "success": true, "seconds": 0.86, "trace": []}
           4 +{"seed": 3, "n": 3, "steps": 28, "success": true, "seconds": 1.13, "trace": []}
           5 +{"seed": 4, "n": 3, "steps": 26, "success": true, "seconds": 0.94, "trace": []}
           6 +{"seed": 5, "n": 3, "steps": 31, "success": true, "seconds": 1.59, "trace": []}
           7 +{"seed": 6, "n": 2, "steps": 22, "success": true, "seconds": 0.8, "trace": []}
           8 +{"seed": 7, "n": 3, "steps": 33, "success": true, "seconds": 1.18, "trace": []}
           9 +{"seed": 8, "n": 3, "steps": 29, "success": true, "seconds": 0.86, "trace": []}
          10 +{"seed": 9, "n": 2, "steps": 26, "success": true, "seconds": 0.82, "trace": []}
diff --git a/stress_test.py b/stress_test.py
new file mode 100644
index 0000000..f498186
--- /dev/null
+++ b/stress_test.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import time,sys,json
           4 +start_seed=int(sys.argv[1]);end_seed=int(sys.argv[2]);count=int(sys.argv[3]) if len(sys.argv)>3 else None
           5 +for seed in range(start_seed,end_seed):
           6 + e=make_env();s,info=e.reset(seed=seed,options={'object_count':count} if count else None);p=GeneratedApproach(e.action_space,e.observation_space,{})
           7 + start=time.time();p.reset(s,info);hist=[]
           8 + for t in range(200):
           9 +  a=p.get_action(s);s,r,done,trunc,inf=e.step(a)
          10 +  hist.append({'t':t,'rover':[[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers], 'images':[[s.get(o,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for o in p.objs], 'samples':[[s.get(o,k) for k in ['received_analysis','analyzed_rover0','analyzed_rover1']] for o in p.samples], 'action':a.tolist()})
          11 +  if done or trunc:break
          12 + result={'seed':seed,'n':len(p.objs),'steps':t+1,'success':done,'sec':round(time.time()-start,3)}
          13 + if not done:
          14 +  with open('failure_%s_%s.json'%(seed,count),'w') as f:json.dump(hist,f)
          15 + print(json.dumps(result),flush=True);e.close()
diff --git a/visual_validation_20_29.jsonl b/visual_validation_20_29.jsonl
index e69de29..adb6c03 100644
--- a/visual_validation_20_29.jsonl
+++ b/visual_validation_20_29.jsonl
@@ -0,0 +1,10 @@
           1 +{"seed": 20, "n": 3, "steps": 39, "success": true, "seconds": 0.74, "trace": []}
           2 +{"seed": 21, "n": 1, "steps": 31, "success": true, "seconds": 0.54, "trace": []}
           3 +{"seed": 22, "n": 3, "steps": 26, "success": true, "seconds": 0.55, "trace": []}
           4 +{"seed": 23, "n": 1, "steps": 20, "success": true, "seconds": 0.32, "trace": []}
           5 +{"seed": 24, "n": 2, "steps": 27, "success": true, "seconds": 0.51, "trace": []}
           6 +{"seed": 25, "n": 2, "steps": 22, "success": true, "seconds": 0.43, "trace": []}
           7 +{"seed": 26, "n": 3, "steps": 26, "success": true, "seconds": 0.58, "trace": []}
           8 +{"seed": 27, "n": 1, "steps": 26, "success": true, "seconds": 0.45, "trace": []}
           9 +{"seed": 28, "n": 2, "steps": 27, "success": true, "seconds": 0.49, "trace": []}
          10 +{"seed": 29, "n": 3, "steps": 37, "success": true, "seconds": 0.58, "trace": []}
```

</details>

<a id="C019"></a>
### C019 · Compare radio LOS and range across nearby transmission poses

Commit `44c1aeee5071e45dff8597e866f42c771891ae84`; parents: e73f4506ec4518871be3666dda4572d7d91b6343. Recorded author date: 2026-09-20T03:51:28+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C019_44c1aee.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_radio_details.py b/probe_radio_details.py
new file mode 100644
index 0000000..9fe49de
--- /dev/null
+++ b/probe_radio_details.py
@@ -0,0 +1,41 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +from scipy.sparse.csgraph import dijkstra
           4 +import numpy as np
           5 +
           6 +def trial(seed,j,target):
           7 + e=make_env();s,_=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,{})
           8 + r=p.rovers[j]
           9 + def xy():return p.xy(s,r)
          10 + def step(move,op):
          11 +  nonlocal s
          12 +  a=np.zeros(8);a[4*j:4*j+2]=move;a[4*j+3]=op;s,*_=e.step(a)
          13 + def go(t,im=False):
          14 +  end=p.nearest(np.array(t))
          15 +  for k in range(120):
          16 +   q=xy();start=p.nearest(q)
          17 +   if np.linalg.norm(q-p.points[end])<.02:break
          18 +   dist,pred=dijkstra(p.graph,indices=start,return_predecessors=True)
          19 +   path=[end]
          20 +   while path[-1]!=start:
          21 +    z=int(pred[path[-1]])
          22 +    if z<0:return False
          23 +    path.append(z)
          24 +   dest=p.points[path[-2] if len(path)>1 else end]
          25 +   move=np.clip(dest-q,-.2,.2)
          26 +   op=(-1/6 if s.get(r,'calibrated') else -.5) if im else 0
          27 +   step(move,op)
          28 +   if np.linalg.norm(xy()-q)<1e-6:return False
          29 +  return True
          30 + go((1 if j==0 else -1.8,.9),True)
          31 + for k in range(2):step([0,0],-1/6 if s.get(r,'calibrated') else -.5)
          32 + have=sum(s.get(o,'have_image_rover'+str(j)) for o in p.objs)
          33 + ok=go(target)
          34 + step([0,0],.5)
          35 + rec=sum(s.get(o,'received_image') for o in p.objs)
          36 + print(seed,j,target,'actual',xy(),'have',have,'received',rec,'go',ok,flush=True)
          37 + if seed==2 and target==(-2.2,0):
          38 +  print('obs',p.boxes.tolist(),flush=True)
          39 + e.close()
          40 +for t in [(-2.2,0),(-2.,0),(-1.8,0),(-2.2,-.2),(-2.2,-.4),(-2.2,.2),(-2.,.2),(-1.8,.2)]:trial(2,1,t)
          41 +for t in [(1,.6),(1,.7),(.9,.7),(1.1,.6),(1.2,.5)]:trial(0,0,t)
diff --git a/stress_default.jsonl b/stress_default.jsonl
new file mode 100644
index 0000000..a8c888b
--- /dev/null
+++ b/stress_default.jsonl
@@ -0,0 +1,11 @@
           1 +{"seed": 30, "n": 1, "steps": 30, "success": true, "sec": 0.444}
           2 +{"seed": 31, "n": 2, "steps": 30, "success": true, "sec": 0.544}
           3 +{"seed": 32, "n": 3, "steps": 25, "success": true, "sec": 0.549}
           4 +{"seed": 33, "n": 3, "steps": 34, "success": true, "sec": 0.685}
           5 +{"seed": 34, "n": 1, "steps": 22, "success": true, "sec": 0.361}
           6 +{"seed": 35, "n": 1, "steps": 21, "success": true, "sec": 0.347}
           7 +{"seed": 36, "n": 2, "steps": 34, "success": true, "sec": 0.373}
           8 +{"seed": 37, "n": 1, "steps": 23, "success": true, "sec": 0.353}
           9 +{"seed": 38, "n": 1, "steps": 23, "success": true, "sec": 0.817}
          10 +{"seed": 39, "n": 3, "steps": 25, "success": true, "sec": 1.287}
          11 +{"seed": 40, "n": 2, "steps": 25, "success": true, "sec": 1.107}
diff --git a/stress_eight.jsonl b/stress_eight.jsonl
new file mode 100644
index 0000000..e69de29
diff --git a/stress_four.jsonl b/stress_four.jsonl
new file mode 100644
index 0000000..fb74f2e
--- /dev/null
+++ b/stress_four.jsonl
@@ -0,0 +1,2 @@
           1 +{"seed": 0, "n": 4, "steps": 29, "success": true, "sec": 1.062}
           2 +{"seed": 1, "n": 4, "steps": 35, "success": true, "sec": 1.504}
```

</details>

<a id="C020"></a>
### C020 · Photograph opportunistically during travel and cache static visibility maps

Commit `831e0608b1a9e2a882b8eb72d2b3776ad3bf295c`; parents: 44c1aeee5071e45dff8597e866f42c771891ae84. Recorded author date: 2026-09-20T03:52:39+02:00.

File roles (automatic): policy, setup/other.

- [E0059](01_timeline.md#E0059): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_831e060_approach.py) · [Exact all-file diff](evidence/diffs/C020_831e060.diff)

[Previous saved controller snapshot](evidence/versions/C016_c747817_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8ae1622..697f75c 100644
--- a/approach.py
+++ b/approach.py
@@ -23,6 +23,10 @@ class GeneratedApproach:
   23     23          self.send_bad=np.zeros((2,len(self.points)),dtype=bool)
   24     24          self.prev=None; self.step=0
   25     25          self.make_graph()
          26 +        self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
          27 +        self.sample_masks=[np.linalg.norm(self.points-self.xy(state,o),axis=1)<.245 for o in self.samples]
          28 +        self.radio_mask=self.visible(self.points,self.lander,4)
          29 +        self.home_dist=[dijkstra(self.graph,indices=self.nearest(h)) for h in self.homes]
   26     30      def free(self,p):
   27     31          p=np.atleast_2d(p)
   28     32          d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
@@ -84,19 +88,19 @@ class GeneratedApproach:
   84     88              candidates=[]
   85     89              for k in [0,1]:
   86     90                  if not acquired[k] and k not in kinds and not s.get(r,'store_full'):
   87        -                    for o in self.samples:
          91 +                    for oi,o in enumerate(self.samples):
   88     92                          if int(s.get(o,'is_soil'))==k:
   89        -                            mask=np.linalg.norm(self.points-self.xy(s,o),axis=1)<.24
          93 +                            mask=self.sample_masks[oi]
   90     94                              candidates.append((mask,'sample',o,k))
   91     95              for j,o in enumerate(self.objs):
   92     96                  if not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]) and j not in assigned:
   93        -                    mask=self.visible(self.points,self.xy(s,o),2)&~self.bad[i,:,j]
          97 +                    mask=self.image_masks[j]&~self.bad[i,:,j]
   94     98                      candidates.append((mask,'image',o,j))
   95     99              pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
   96        -            if pending: candidates.append((self.visible(self.points,self.lander,4)&~self.send_bad[i],'send',None,None))
         100 +            if pending: candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
   97    101              best=None; score=np.inf
   98    102              for mask,task,o,j in candidates:
   99        -                dd=dist.copy();dd[~mask]=np.inf
         103 +                dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
  100    104                  target=int(np.argmin(dd)); cost=dd[target]
  101    105                  if task=='send': cost+=5 if any(c[1]!='send' for c in candidates) else 0
  102    106                  if cost<score: score=cost;best=(target,task,o,j)
@@ -123,10 +127,13 @@ class GeneratedApproach:
  123    127              if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
  124    128              q=p+move; op=0.;idx=None
  125    129              if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249:op=-5/6
  126        -            elif task=='image' and self.visible(q,self.xy(s,o),2)[0]:
  127        -                op=-1/6 if s.get(r,'calibrated') else -.5;idx=j
  128        -            elif pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
  129        -            elif s.get(r,'store_full'):op=5/6
         130 +            else:
         131 +                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
         132 +                if useful:
         133 +                    idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
         134 +                    op=-1/6 if s.get(r,'calibrated') else -.5
         135 +            if op==0 and pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
         136 +            elif op==0 and s.get(r,'store_full'):op=5/6
  130    137              action[4*i:4*i+2]=move;action[4*i+3]=op
  131    138              records.append((p,move,op,idx,self.pending_count(s,i)))
  132    139          self.prev=records
diff --git a/stress_default.jsonl b/stress_default.jsonl
index a8c888b..30fec34 100644
--- a/stress_default.jsonl
+++ b/stress_default.jsonl
@@ -9,3 +9,42 @@
    9      9  {"seed": 38, "n": 1, "steps": 23, "success": true, "sec": 0.817}
   10     10  {"seed": 39, "n": 3, "steps": 25, "success": true, "sec": 1.287}
   11     11  {"seed": 40, "n": 2, "steps": 25, "success": true, "sec": 1.107}
          12 +{"seed": 41, "n": 2, "steps": 21, "success": true, "sec": 1.193}
          13 +{"seed": 42, "n": 1, "steps": 33, "success": true, "sec": 1.779}
          14 +{"seed": 43, "n": 2, "steps": 33, "success": true, "sec": 1.447}
          15 +{"seed": 44, "n": 3, "steps": 29, "success": true, "sec": 1.143}
          16 +{"seed": 45, "n": 3, "steps": 32, "success": true, "sec": 2.087}
          17 +{"seed": 46, "n": 2, "steps": 24, "success": true, "sec": 1.693}
          18 +{"seed": 47, "n": 1, "steps": 26, "success": true, "sec": 1.765}
          19 +{"seed": 48, "n": 1, "steps": 22, "success": true, "sec": 1.379}
          20 +{"seed": 49, "n": 1, "steps": 23, "success": true, "sec": 1.139}
          21 +{"seed": 50, "n": 3, "steps": 32, "success": true, "sec": 2.393}
          22 +{"seed": 51, "n": 2, "steps": 24, "success": true, "sec": 1.367}
          23 +{"seed": 52, "n": 3, "steps": 27, "success": true, "sec": 1.297}
          24 +{"seed": 53, "n": 3, "steps": 30, "success": true, "sec": 0.81}
          25 +{"seed": 54, "n": 1, "steps": 23, "success": true, "sec": 0.907}
          26 +{"seed": 55, "n": 3, "steps": 30, "success": true, "sec": 1.286}
          27 +{"seed": 56, "n": 2, "steps": 29, "success": true, "sec": 1.243}
          28 +{"seed": 57, "n": 1, "steps": 20, "success": true, "sec": 0.611}
          29 +{"seed": 58, "n": 2, "steps": 36, "success": true, "sec": 1.384}
          30 +{"seed": 59, "n": 3, "steps": 27, "success": true, "sec": 1.322}
          31 +{"seed": 60, "n": 1, "steps": 32, "success": true, "sec": 1.351}
          32 +{"seed": 61, "n": 2, "steps": 28, "success": true, "sec": 1.138}
          33 +{"seed": 62, "n": 2, "steps": 28, "success": true, "sec": 0.736}
          34 +{"seed": 63, "n": 2, "steps": 30, "success": true, "sec": 0.901}
          35 +{"seed": 64, "n": 2, "steps": 28, "success": true, "sec": 0.986}
          36 +{"seed": 65, "n": 1, "steps": 21, "success": true, "sec": 1.007}
          37 +{"seed": 66, "n": 3, "steps": 26, "success": true, "sec": 0.743}
          38 +{"seed": 67, "n": 3, "steps": 28, "success": true, "sec": 1.346}
          39 +{"seed": 68, "n": 2, "steps": 24, "success": true, "sec": 1.198}
          40 +{"seed": 69, "n": 1, "steps": 25, "success": true, "sec": 0.645}
          41 +{"seed": 70, "n": 2, "steps": 24, "success": true, "sec": 0.482}
          42 +{"seed": 71, "n": 3, "steps": 25, "success": true, "sec": 0.559}
          43 +{"seed": 72, "n": 3, "steps": 32, "success": true, "sec": 0.729}
          44 +{"seed": 73, "n": 3, "steps": 31, "success": true, "sec": 0.665}
          45 +{"seed": 74, "n": 1, "steps": 24, "success": true, "sec": 0.359}
          46 +{"seed": 75, "n": 2, "steps": 27, "success": true, "sec": 0.527}
          47 +{"seed": 76, "n": 2, "steps": 25, "success": true, "sec": 0.415}
          48 +{"seed": 77, "n": 1, "steps": 25, "success": true, "sec": 0.417}
          49 +{"seed": 78, "n": 3, "steps": 28, "success": true, "sec": 0.612}
          50 +{"seed": 79, "n": 1, "steps": 29, "success": true, "sec": 0.479}
diff --git a/stress_four.jsonl b/stress_four.jsonl
index fb74f2e..2bcd274 100644
--- a/stress_four.jsonl
+++ b/stress_four.jsonl
@@ -1,2 +1,25 @@
    1      1  {"seed": 0, "n": 4, "steps": 29, "success": true, "sec": 1.062}
    2      2  {"seed": 1, "n": 4, "steps": 35, "success": true, "sec": 1.504}
           3 +{"seed": 2, "n": 4, "steps": 32, "success": true, "sec": 1.865}
           4 +{"seed": 3, "n": 4, "steps": 34, "success": true, "sec": 2.204}
           5 +{"seed": 4, "n": 4, "steps": 32, "success": true, "sec": 1.912}
           6 +{"seed": 5, "n": 4, "steps": 37, "success": true, "sec": 1.784}
           7 +{"seed": 6, "n": 4, "steps": 29, "success": true, "sec": 1.867}
           8 +{"seed": 7, "n": 4, "steps": 33, "success": true, "sec": 2.001}
           9 +{"seed": 8, "n": 4, "steps": 31, "success": true, "sec": 2.028}
          10 +{"seed": 9, "n": 4, "steps": 33, "success": true, "sec": 2.627}
          11 +{"seed": 10, "n": 4, "steps": 28, "success": true, "sec": 1.788}
          12 +{"seed": 11, "n": 4, "steps": 32, "success": true, "sec": 1.704}
          13 +{"seed": 12, "n": 4, "steps": 37, "success": true, "sec": 1.876}
          14 +{"seed": 13, "n": 4, "steps": 32, "success": true, "sec": 0.982}
          15 +{"seed": 14, "n": 4, "steps": 35, "success": true, "sec": 1.471}
          16 +{"seed": 15, "n": 4, "steps": 32, "success": true, "sec": 1.925}
          17 +{"seed": 16, "n": 4, "steps": 25, "success": true, "sec": 1.0}
          18 +{"seed": 17, "n": 4, "steps": 38, "success": true, "sec": 1.564}
          19 +{"seed": 18, "n": 4, "steps": 32, "success": true, "sec": 1.297}
          20 +{"seed": 19, "n": 4, "steps": 38, "success": true, "sec": 1.513}
          21 +{"seed": 20, "n": 4, "steps": 36, "success": true, "sec": 1.683}
          22 +{"seed": 21, "n": 4, "steps": 35, "success": true, "sec": 1.383}
          23 +{"seed": 22, "n": 4, "steps": 36, "success": true, "sec": 1.592}
          24 +{"seed": 23, "n": 4, "steps": 33, "success": true, "sec": 1.546}
          25 +{"seed": 24, "n": 4, "steps": 33, "success": true, "sec": 2.163}
```

</details>

<a id="C021"></a>
### C021 · Refine effective transmission radius below four meters

Commit `63b51c6878fd969b84292fb7c7185616c1d17d9d`; parents: 831e0608b1a9e2a882b8eb72d2b3776ad3bf295c. Recorded author date: 2026-09-20T03:52:47+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C021_63b51c6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/opportunistic.jsonl b/opportunistic.jsonl
new file mode 100644
index 0000000..57dccbf
--- /dev/null
+++ b/opportunistic.jsonl
@@ -0,0 +1,10 @@
           1 +{"seed": 0, "n": 3, "steps": 37, "success": true, "sec": 0.322}
           2 +{"seed": 1, "n": 2, "steps": 23, "success": true, "sec": 0.21}
           3 +{"seed": 2, "n": 3, "steps": 23, "success": true, "sec": 0.344}
           4 +{"seed": 3, "n": 3, "steps": 28, "success": true, "sec": 0.401}
           5 +{"seed": 4, "n": 3, "steps": 26, "success": true, "sec": 0.431}
           6 +{"seed": 5, "n": 3, "steps": 31, "success": true, "sec": 0.369}
           7 +{"seed": 6, "n": 2, "steps": 24, "success": true, "sec": 0.302}
           8 +{"seed": 7, "n": 3, "steps": 32, "success": true, "sec": 0.47}
           9 +{"seed": 8, "n": 3, "steps": 26, "success": true, "sec": 0.378}
          10 +{"seed": 9, "n": 2, "steps": 26, "success": true, "sec": 0.348}
```

</details>

<a id="C022"></a>
### C022 · Measure exact radio cutoff and occluder padding with fine-grained poses

Commit `1b5aab21049aa95ea6e05a41d71ed1e20c3a8d26`; parents: 63b51c6878fd969b84292fb7c7185616c1d17d9d. Recorded author date: 2026-09-20T03:53:12+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C022_1b5aab2.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/opportunistic.jsonl b/opportunistic.jsonl
index 57dccbf..3b0f7f9 100644
--- a/opportunistic.jsonl
+++ b/opportunistic.jsonl
@@ -8,3 +8,23 @@
    8      8  {"seed": 7, "n": 3, "steps": 32, "success": true, "sec": 0.47}
    9      9  {"seed": 8, "n": 3, "steps": 26, "success": true, "sec": 0.378}
   10     10  {"seed": 9, "n": 2, "steps": 26, "success": true, "sec": 0.348}
          11 +{"seed": 10, "n": 3, "steps": 28, "success": true, "sec": 0.765}
          12 +{"seed": 11, "n": 1, "steps": 29, "success": true, "sec": 0.492}
          13 +{"seed": 12, "n": 2, "steps": 28, "success": true, "sec": 0.973}
          14 +{"seed": 13, "n": 3, "steps": 35, "success": true, "sec": 1.146}
          15 +{"seed": 14, "n": 1, "steps": 37, "success": true, "sec": 0.911}
          16 +{"seed": 15, "n": 3, "steps": 46, "success": true, "sec": 1.617}
          17 +{"seed": 16, "n": 2, "steps": 28, "success": true, "sec": 0.805}
          18 +{"seed": 17, "n": 3, "steps": 33, "success": true, "sec": 0.965}
          19 +{"seed": 18, "n": 3, "steps": 27, "success": true, "sec": 0.953}
          20 +{"seed": 19, "n": 2, "steps": 31, "success": true, "sec": 0.525}
          21 +{"seed": 20, "n": 3, "steps": 32, "success": true, "sec": 0.518}
          22 +{"seed": 21, "n": 1, "steps": 31, "success": true, "sec": 0.423}
          23 +{"seed": 22, "n": 3, "steps": 26, "success": true, "sec": 0.41}
          24 +{"seed": 23, "n": 1, "steps": 20, "success": true, "sec": 0.262}
          25 +{"seed": 24, "n": 2, "steps": 27, "success": true, "sec": 0.349}
          26 +{"seed": 25, "n": 2, "steps": 22, "success": true, "sec": 0.303}
          27 +{"seed": 26, "n": 3, "steps": 26, "success": true, "sec": 0.412}
          28 +{"seed": 27, "n": 1, "steps": 26, "success": true, "sec": 0.353}
          29 +{"seed": 28, "n": 2, "steps": 26, "success": true, "sec": 0.397}
          30 +{"seed": 29, "n": 3, "steps": 37, "success": true, "sec": 0.629}
diff --git a/probe_radio_details.py b/probe_radio_details.py
index 9fe49de..ab96497 100644
--- a/probe_radio_details.py
+++ b/probe_radio_details.py
@@ -31,11 +31,12 @@ def trial(seed,j,target):
   31     31   for k in range(2):step([0,0],-1/6 if s.get(r,'calibrated') else -.5)
   32     32   have=sum(s.get(o,'have_image_rover'+str(j)) for o in p.objs)
   33     33   ok=go(target)
          34 + step(np.clip(np.array(target)-xy(),-.2,.2),0)
   34     35   step([0,0],.5)
   35     36   rec=sum(s.get(o,'received_image') for o in p.objs)
   36     37   print(seed,j,target,'actual',xy(),'have',have,'received',rec,'go',ok,flush=True)
   37     38   if seed==2 and target==(-2.2,0):
   38     39    print('obs',p.boxes.tolist(),flush=True)
   39     40   e.close()
   40        -for t in [(-2.2,0),(-2.,0),(-1.8,0),(-2.2,-.2),(-2.2,-.4),(-2.2,.2),(-2.,.2),(-1.8,.2)]:trial(2,1,t)
   41        -for t in [(1,.6),(1,.7),(.9,.7),(1.1,.6),(1.2,.5)]:trial(0,0,t)
          41 +for t in [(1,.65),(1,.66),(1,.67),(1,.68),(1,.69)]:trial(0,0,t)
          42 +for x in [-2.25,-2.20,-2.175,-2.15,-2.125,-2.1,-2.05]:trial(2,1,(x,0))
```

</details>

<a id="C023"></a>
### C023 · Test exact 3.9 meter radio radius and padded pillar threshold

Commit `36451407f00ea9fa74fef53897dba3972bdf7bab`; parents: 1b5aab21049aa95ea6e05a41d71ed1e20c3a8d26. Recorded author date: 2026-09-20T03:53:43+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C023_3645140.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_radio_details.py b/probe_radio_details.py
index ab96497..50841ce 100644
--- a/probe_radio_details.py
+++ b/probe_radio_details.py
@@ -38,5 +38,5 @@ def trial(seed,j,target):
   38     38   if seed==2 and target==(-2.2,0):
   39     39    print('obs',p.boxes.tolist(),flush=True)
   40     40   e.close()
   41        -for t in [(1,.65),(1,.66),(1,.67),(1,.68),(1,.69)]:trial(0,0,t)
   42        -for x in [-2.25,-2.20,-2.175,-2.15,-2.125,-2.1,-2.05]:trial(2,1,(x,0))
          41 +for t in [(1,.60),(1,.605),(1,.61),(1,.615)]:trial(0,0,t)
          42 +for x in [-2.19,-2.185,-2.18,-2.175]:trial(2,1,(x,0))
diff --git a/radio_details.log b/radio_details.log
new file mode 100644
index 0000000..64bfda4
--- /dev/null
+++ b/radio_details.log
@@ -0,0 +1,13 @@
           1 +0 0 (1, 0.65) actual [1.         0.64999998] have 2.0 received 0.0 go True
           2 +0 0 (1, 0.66) actual [1.         0.66000003] have 2.0 received 0.0 go True
           3 +0 0 (1, 0.67) actual [1.         0.67000002] have 2.0 received 0.0 go True
           4 +0 0 (1, 0.68) actual [1.         0.68000001] have 2.0 received 0.0 go True
           5 +0 0 (1, 0.69) actual [1.   0.69] have 2.0 received 0.0 go True
           6 +2 1 (-2.25, 0) actual [-2.25  0.  ] have 2.0 received 0.0 go True
           7 +2 1 (-2.2, 0) actual [-2.20000005  0.        ] have 2.0 received 0.0 go True
           8 +obs [[2.0, 2.0, 0.25, 0.25], [-2.0, 2.0, 0.25, 0.25], [-0.21526943147182465, -0.5559921264648438, 0.05000000074505806, 0.05000000074505806], [0.7348376512527466, 0.4442424476146698, 0.05000000074505806, 0.05000000074505806], [0.5, 2.0, 0.25, 0.25], [-0.5, 2.0, 0.25, 0.25], [2.1178300380706787, -0.9612797498703003, 0.05000000074505806, 0.05000000074505806], [-1.7171909809112549, 0.9063087105751038, 0.05000000074505806, 0.05000000074505806], [1.639979600906372, 0.7337386012077332, 0.05000000074505806, 0.05000000074505806], [1.7862882614135742, -0.5400499105453491, 0.05000000074505806, 0.05000000074505806], [-0.9069060683250427, 1.2679052352905273, 0.05000000074505806, 0.05000000074505806], [-2.1559410095214844, -1.0042955875396729, 0.05000000074505806, 0.05000000074505806], [0.0, 0.0, 0.05, 2.5]]
           9 +2 1 (-2.175, 0) actual [-2.17499995  0.        ] have 2.0 received 2.0 go True
          10 +2 1 (-2.15, 0) actual [-2.14999986  0.        ] have 2.0 received 2.0 go True
          11 +2 1 (-2.125, 0) actual [-2.125  0.   ] have 2.0 received 2.0 go True
          12 +2 1 (-2.1, 0) actual [-2.10000014  0.        ] have 2.0 received 2.0 go True
          13 +2 1 (-2.05, 0) actual [-2.05000019  0.        ] have 2.0 received 2.0 go True
```

</details>

<a id="C024"></a>
### C024 · Locate radio cutoff and compare equivalent-distance poses

Commit `e8d6a4cd4bb01aa61e6d6cc2aa4fce643b02e2e7`; parents: 36451407f00ea9fa74fef53897dba3972bdf7bab. Recorded author date: 2026-09-20T03:54:00+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C024_e8d6a4c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_radio_details.py b/probe_radio_details.py
index 50841ce..19ebd42 100644
--- a/probe_radio_details.py
+++ b/probe_radio_details.py
@@ -38,5 +38,4 @@ def trial(seed,j,target):
   38     38   if seed==2 and target==(-2.2,0):
   39     39    print('obs',p.boxes.tolist(),flush=True)
   40     40   e.close()
   41        -for t in [(1,.60),(1,.605),(1,.61),(1,.615)]:trial(0,0,t)
   42        -for x in [-2.19,-2.185,-2.18,-2.175]:trial(2,1,(x,0))
          41 +for t in [(1,.62),(1,.625),(1,.63),(1,.635),(1,.64),(.9,.74),(1.1,.505)]:trial(0,0,t)
diff --git a/radio_details.log b/radio_details.log
index 64bfda4..630b28d 100644
--- a/radio_details.log
+++ b/radio_details.log
@@ -1,13 +1,8 @@
    1        -0 0 (1, 0.65) actual [1.         0.64999998] have 2.0 received 0.0 go True
    2        -0 0 (1, 0.66) actual [1.         0.66000003] have 2.0 received 0.0 go True
    3        -0 0 (1, 0.67) actual [1.         0.67000002] have 2.0 received 0.0 go True
    4        -0 0 (1, 0.68) actual [1.         0.68000001] have 2.0 received 0.0 go True
    5        -0 0 (1, 0.69) actual [1.   0.69] have 2.0 received 0.0 go True
    6        -2 1 (-2.25, 0) actual [-2.25  0.  ] have 2.0 received 0.0 go True
    7        -2 1 (-2.2, 0) actual [-2.20000005  0.        ] have 2.0 received 0.0 go True
    8        -obs [[2.0, 2.0, 0.25, 0.25], [-2.0, 2.0, 0.25, 0.25], [-0.21526943147182465, -0.5559921264648438, 0.05000000074505806, 0.05000000074505806], [0.7348376512527466, 0.4442424476146698, 0.05000000074505806, 0.05000000074505806], [0.5, 2.0, 0.25, 0.25], [-0.5, 2.0, 0.25, 0.25], [2.1178300380706787, -0.9612797498703003, 0.05000000074505806, 0.05000000074505806], [-1.7171909809112549, 0.9063087105751038, 0.05000000074505806, 0.05000000074505806], [1.639979600906372, 0.7337386012077332, 0.05000000074505806, 0.05000000074505806], [1.7862882614135742, -0.5400499105453491, 0.05000000074505806, 0.05000000074505806], [-0.9069060683250427, 1.2679052352905273, 0.05000000074505806, 0.05000000074505806], [-2.1559410095214844, -1.0042955875396729, 0.05000000074505806, 0.05000000074505806], [0.0, 0.0, 0.05, 2.5]]
           1 +0 0 (1, 0.6) actual [1.         0.59999996] have 2.0 received 2.0 go True
           2 +0 0 (1, 0.605) actual [1.         0.60499996] have 2.0 received 2.0 go True
           3 +0 0 (1, 0.61) actual [1.         0.61000001] have 2.0 received 2.0 go True
           4 +0 0 (1, 0.615) actual [1.         0.61500001] have 2.0 received 2.0 go True
           5 +2 1 (-2.19, 0) actual [-2.19000006  0.        ] have 2.0 received 0.0 go True
           6 +2 1 (-2.185, 0) actual [-2.18499994  0.        ] have 2.0 received 0.0 go True
           7 +2 1 (-2.18, 0) actual [-2.17999983  0.        ] have 2.0 received 2.0 go True
    9      8  2 1 (-2.175, 0) actual [-2.17499995  0.        ] have 2.0 received 2.0 go True
   10        -2 1 (-2.15, 0) actual [-2.14999986  0.        ] have 2.0 received 2.0 go True
   11        -2 1 (-2.125, 0) actual [-2.125  0.   ] have 2.0 received 2.0 go True
   12        -2 1 (-2.1, 0) actual [-2.10000014  0.        ] have 2.0 received 2.0 go True
   13        -2 1 (-2.05, 0) actual [-2.05000019  0.        ] have 2.0 received 2.0 go True
```

</details>

<a id="C025"></a>
### C025 · Radio while returning home and prepare the camera during otherwise idle travel

Commit `9425eeef7e42d43842e32244c7663f2d701a0963`; parents: e8d6a4cd4bb01aa61e6d6cc2aa4fce643b02e2e7. Recorded author date: 2026-09-20T03:54:14+02:00.

File roles (automatic): policy, setup/other.

- [E0071](01_timeline.md#E0071): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C025_9425eee_approach.py) · [Exact all-file diff](evidence/diffs/C025_9425eee.diff)

[Previous saved controller snapshot](evidence/versions/C020_831e060_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 697f75c..91d9276 100644
--- a/approach.py
+++ b/approach.py
@@ -31,7 +31,8 @@ class GeneratedApproach:
   31     31          p=np.atleast_2d(p)
   32     32          d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
   33     33          ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.228**2,axis=1)
   34        -        ok &= np.linalg.norm(p-self.lander,axis=1)>.55
          34 +        ld=np.maximum(np.abs(p-self.lander)-np.array([.45,.30]),0)
          35 +        ok &= np.sum(ld**2,axis=1)>.228**2
   35     36          ok &= np.max(np.abs(p),axis=1)<2.271
   36     37          return ok
   37     38      def make_graph(self):
@@ -106,6 +107,8 @@ class GeneratedApproach:
  106    107                  if cost<score: score=cost;best=(target,task,o,j)
  107    108              if best is None: best=(self.nearest(self.homes[i]),'home',None,None)
  108    109              target,task,o,j=best
         110 +            if task=='send' and self.visible(p,self.lander,4)[0] and not self.send_bad[i,start]:
         111 +                target=self.nearest(self.homes[i]);task='home'
  109    112              if task=='sample': kinds.add(j)
  110    113              if task=='image': assigned.add(j)
  111    114              targetpos=self.points[target]
@@ -134,6 +137,7 @@ class GeneratedApproach:
  134    137                      op=-1/6 if s.get(r,'calibrated') else -.5
  135    138              if op==0 and pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
  136    139              elif op==0 and s.get(r,'store_full'):op=5/6
         140 +            elif op==0 and not s.get(r,'calibrated') and any(not s.get(oo,'received_image') for oo in self.objs) and any(self.visible(q,self.xy(s,oo),2)[0] for oo in self.objs):op=-.5
  137    141              action[4*i:4*i+2]=move;action[4*i+3]=op
  138    142              records.append((p,move,op,idx,self.pending_count(s,i)))
  139    143          self.prev=records
diff --git a/radio_details.log b/radio_details.log
index 630b28d..710db39 100644
--- a/radio_details.log
+++ b/radio_details.log
@@ -1,8 +1,7 @@
    1        -0 0 (1, 0.6) actual [1.         0.59999996] have 2.0 received 2.0 go True
    2        -0 0 (1, 0.605) actual [1.         0.60499996] have 2.0 received 2.0 go True
    3        -0 0 (1, 0.61) actual [1.         0.61000001] have 2.0 received 2.0 go True
    4        -0 0 (1, 0.615) actual [1.         0.61500001] have 2.0 received 2.0 go True
    5        -2 1 (-2.19, 0) actual [-2.19000006  0.        ] have 2.0 received 0.0 go True
    6        -2 1 (-2.185, 0) actual [-2.18499994  0.        ] have 2.0 received 0.0 go True
    7        -2 1 (-2.18, 0) actual [-2.17999983  0.        ] have 2.0 received 2.0 go True
    8        -2 1 (-2.175, 0) actual [-2.17499995  0.        ] have 2.0 received 2.0 go True
           1 +0 0 (1, 0.62) actual [1.   0.62] have 2.0 received 2.0 go True
           2 +0 0 (1, 0.625) actual [1.    0.625] have 2.0 received 2.0 go True
           3 +0 0 (1, 0.63) actual [1.   0.63] have 2.0 received 2.0 go True
           4 +0 0 (1, 0.635) actual [1.         0.63499999] have 2.0 received 0.0 go True
           5 +0 0 (1, 0.64) actual [1.         0.63999999] have 2.0 received 0.0 go True
           6 +0 0 (0.9, 0.74) actual [0.89999998 0.74000001] have 2.0 received 2.0 go True
           7 +0 0 (1.1, 0.505) actual [1.10000002 0.505     ] have 2.0 received 0.0 go True
```

</details>

<a id="C026"></a>
### C026 · Prototype joint rover task selection minimizing concurrent route cost

Commit `744f3f611e5bfac5fb9a5460c344205be923b500`; parents: 9425eeef7e42d43842e32244c7663f2d701a0963. Recorded author date: 2026-09-20T03:54:28+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

[Exact all-file diff](evidence/diffs/C026_744f3f6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/assignment_baseline.py b/assignment_baseline.py
new file mode 100644
index 0000000..91d9276
--- /dev/null
+++ b/assignment_baseline.py
@@ -0,0 +1,144 @@
           1 +import numpy as np
           2 +from scipy.sparse import csr_matrix
           3 +from scipy.sparse.csgraph import dijkstra
           4 +
           5 +class GeneratedApproach:
           6 +    def __init__(self, action_space, observation_space, primitives):
           7 +        self.space = observation_space
           8 +    def objects(self, s, t):
           9 +        return s.get_objects(self.space.get_type(t))
          10 +    def xy(self,s,o):
          11 +        return np.array([s.get(o,'x'),s.get(o,'y')])
          12 +    def reset(self,state,info):
          13 +        self.rovers=[state.get_object_from_name('rover'+str(i)) for i in range(2)]
          14 +        self.homes=[self.xy(state,r) for r in self.rovers]
          15 +        self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
          16 +        self.lander=self.xy(state,self.objects(state,'lander')[0])
          17 +        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,2.5]])
          18 +        self.axis=np.arange(-2.3,2.301,0.1)
          19 +        self.n=len(self.axis)
          20 +        self.points=np.array([(x,y) for x in self.axis for y in self.axis])
          21 +        self.valid=self.free(self.points)
          22 +        self.bad=np.zeros((2,len(self.points),len(self.objs)),dtype=bool)
          23 +        self.send_bad=np.zeros((2,len(self.points)),dtype=bool)
          24 +        self.prev=None; self.step=0
          25 +        self.make_graph()
          26 +        self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
          27 +        self.sample_masks=[np.linalg.norm(self.points-self.xy(state,o),axis=1)<.245 for o in self.samples]
          28 +        self.radio_mask=self.visible(self.points,self.lander,4)
          29 +        self.home_dist=[dijkstra(self.graph,indices=self.nearest(h)) for h in self.homes]
          30 +    def free(self,p):
          31 +        p=np.atleast_2d(p)
          32 +        d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
          33 +        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.228**2,axis=1)
          34 +        ld=np.maximum(np.abs(p-self.lander)-np.array([.45,.30]),0)
          35 +        ok &= np.sum(ld**2,axis=1)>.228**2
          36 +        ok &= np.max(np.abs(p),axis=1)<2.271
          37 +        return ok
          38 +    def make_graph(self):
          39 +        rows=[]; cols=[]
          40 +        for i in np.flatnonzero(self.valid):
          41 +            x,y=divmod(i,self.n)
          42 +            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
          43 +                xx,yy=x+dx,y+dy
          44 +                if 0<=xx<self.n and 0<=yy<self.n:
          45 +                    j=xx*self.n+yy
          46 +                    if self.valid[j]: rows.append(i);cols.append(j)
          47 +        self.graph=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(self.points),len(self.points)))
          48 +    def visible(self,p,target,limit):
          49 +        p=np.atleast_2d(p); target=np.asarray(target)
          50 +        ok=np.linalg.norm(p-target,axis=1)<limit-.025
          51 +        # Low mounds do not occlude the camera, but pillars and wall do.
          52 +        boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
          53 +        delta=target-p
          54 +        for b in boxes:
          55 +            lo=b[:2]-b[2:];hi=b[:2]+b[2:]
          56 +            with np.errstate(divide='ignore',invalid='ignore'):
          57 +                t1=(lo-p)/delta;t2=(hi-p)/delta
          58 +            near=np.maximum(np.min(np.stack([t1,t2]),axis=0).max(axis=1),.001)
          59 +            far=np.minimum(np.max(np.stack([t1,t2]),axis=0).min(axis=1),.999)
          60 +            ok &= near>far
          61 +        return ok
          62 +    def nearest(self,p):
          63 +        ds=np.sum((self.points-p)**2,axis=1);ds[~self.valid]=np.inf
          64 +        return int(np.argmin(ds))
          65 +    def pending_count(self,s,i):
          66 +        return sum(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs)+sum(s.get(o,'analyzed_rover'+str(i)) and not s.get(o,'received_analysis') for o in self.samples)
          67 +    def get_action(self,s):
          68 +        self.step+=1
          69 +        pos=[self.xy(s,r) for r in self.rovers]
          70 +        if self.prev is not None:
          71 +            for i in range(2):
          72 +                old,move,op,idx,had=self.prev[i]
          73 +                if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
          74 +                    q=old+move
          75 +                    ids=np.linalg.norm(self.points-q,axis=1)<.085
          76 +                    self.valid[ids]=False
          77 +                    self.make_graph()
          78 +                if op==.5 and self.pending_count(s,i)>=had:
          79 +                    self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
          80 +                if op in [-.5,-1/6] and idx is not None:
          81 +                    if (op==-.5 and not s.get(self.rovers[i],'calibrated')) or (op==-1/6 and not s.get(self.objs[idx],'have_image_rover'+str(i))):
          82 +                        self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
          83 +        action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
          84 +        received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
          85 +        acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
          86 +        for i,r in enumerate(self.rovers):
          87 +            p=pos[i]; start=self.nearest(p)
          88 +            dist,pred=dijkstra(self.graph,indices=start,return_predecessors=True)
          89 +            candidates=[]
          90 +            for k in [0,1]:
          91 +                if not acquired[k] and k not in kinds and not s.get(r,'store_full'):
          92 +                    for oi,o in enumerate(self.samples):
          93 +                        if int(s.get(o,'is_soil'))==k:
          94 +                            mask=self.sample_masks[oi]
          95 +                            candidates.append((mask,'sample',o,k))
          96 +            for j,o in enumerate(self.objs):
          97 +                if not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]) and j not in assigned:
          98 +                    mask=self.image_masks[j]&~self.bad[i,:,j]
          99 +                    candidates.append((mask,'image',o,j))
         100 +            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
         101 +            if pending: candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
         102 +            best=None; score=np.inf
         103 +            for mask,task,o,j in candidates:
         104 +                dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         105 +                target=int(np.argmin(dd)); cost=dd[target]
         106 +                if task=='send': cost+=5 if any(c[1]!='send' for c in candidates) else 0
         107 +                if cost<score: score=cost;best=(target,task,o,j)
         108 +            if best is None: best=(self.nearest(self.homes[i]),'home',None,None)
         109 +            target,task,o,j=best
         110 +            if task=='send' and self.visible(p,self.lander,4)[0] and not self.send_bad[i,start]:
         111 +                target=self.nearest(self.homes[i]);task='home'
         112 +            if task=='sample': kinds.add(j)
         113 +            if task=='image': assigned.add(j)
         114 +            targetpos=self.points[target]
         115 +            if task=='home': targetpos=self.homes[i]
         116 +            path=[target];cur=target
         117 +            for _ in range(len(self.points)):
         118 +                if cur==start:break
         119 +                cur=int(pred[cur])
         120 +                if cur<0:break
         121 +                path.append(cur)
         122 +            path=path[::-1]
         123 +            goal=targetpos
         124 +            for node in path:
         125 +                q=self.points[node]
         126 +                if np.max(np.abs(q-p))<=.20001: goal=q
         127 +                else: break
         128 +            if np.max(np.abs(targetpos-p))<=.2:goal=targetpos
         129 +            move=np.clip(goal-p,-.2,.2)
         130 +            if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
         131 +            q=p+move; op=0.;idx=None
         132 +            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249:op=-5/6
         133 +            else:
         134 +                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
         135 +                if useful:
         136 +                    idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
         137 +                    op=-1/6 if s.get(r,'calibrated') else -.5
         138 +            if op==0 and pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
         139 +            elif op==0 and s.get(r,'store_full'):op=5/6
         140 +            elif op==0 and not s.get(r,'calibrated') and any(not s.get(oo,'received_image') for oo in self.objs) and any(self.visible(q,self.xy(s,oo),2)[0] for oo in self.objs):op=-.5
         141 +            action[4*i:4*i+2]=move;action[4*i+3]=op
         142 +            records.append((p,move,op,idx,self.pending_count(s,i)))
         143 +        self.prev=records
         144 +        return action
diff --git a/build_assignment.py b/build_assignment.py
new file mode 100644
index 0000000..9cd4ae1
--- /dev/null
+++ b/build_assignment.py
@@ -0,0 +1,45 @@
           1 +p='candidate_assignment.py'
           2 +s=open(p).read()
           3 +start=s.index('        for i,r in enumerate(self.rovers):\n            p=pos[i]; start=self.nearest(p)')
           4 +end=s.index('            target,task,o,j=best',start)
           5 +s=s[:start]+'''        routes=[dijkstra(self.graph,indices=self.nearest(pos[i]),return_predecessors=True) for i in range(2)]
           6 +        options=[[],[]]
           7 +        for i,r in enumerate(self.rovers):
           8 +            dist=routes[i][0]
           9 +            candidates=[]
          10 +            for k in [0,1]:
          11 +                if not acquired[k] and not s.get(r,'store_full'):
          12 +                    for oi,o in enumerate(self.samples):
          13 +                        if int(s.get(o,'is_soil'))==k:
          14 +                            candidates.append((self.sample_masks[oi],'sample',o,k))
          15 +            for j,o in enumerate(self.objs):
          16 +                if not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]):
          17 +                    candidates.append((self.image_masks[j]&~self.bad[i,:,j],'image',o,j))
          18 +            if self.pending_count(s,i):
          19 +                candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
          20 +            for mask,task,o,j in candidates:
          21 +                dd=dist+.05*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
          22 +                target=int(np.argmin(dd));cost=dd[target]
          23 +                if not np.isfinite(cost):continue
          24 +                cost+= .15*self.home_dist[i][target]
          25 +                if task=='send':cost+=5 if any(c[1]!='send' for c in candidates) else 0
          26 +                if hasattr(self,'last_tasks') and self.last_tasks[i]==(task,j):cost-=1.5
          27 +                options[i].append((cost,(target,task,o,j)))
          28 +            h=self.nearest(self.homes[i])
          29 +            options[i].append((12+.2*dist[h],(h,'home',None,None)))
          30 +        best_pair=None;best_score=np.inf
          31 +        anywork=any(len(o)>1 for o in options)
          32 +        for c0,b0 in options[0]:
          33 +            for c1,b1 in options[1]:
          34 +                if b0[1]==b1[1] and b0[1] in ['sample','image'] and b0[3]==b1[3]:continue
          35 +                if anywork and b0[1]==b1[1]=='home':continue
          36 +                score=max(c0,c1)+.3*(c0+c1)
          37 +                if score<best_score:best_score=score;best_pair=(b0,b1)
          38 +        if best_pair is None:best_pair=(options[0][-1][1],options[1][-1][1])
          39 +        self.last_tasks=[(b[1],b[3]) for b in best_pair]
          40 +        for i,r in enumerate(self.rovers):
          41 +            p=pos[i];start=self.nearest(p);dist,pred=routes[i]
          42 +            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
          43 +            best=best_pair[i]
          44 +''' + s[end:]
          45 +open(p,'w').write(s)
diff --git a/candidate_assignment.py b/candidate_assignment.py
new file mode 100644
index 0000000..960b8fb
--- /dev/null
+++ b/candidate_assignment.py
@@ -0,0 +1,160 @@
           1 +import numpy as np
           2 +from scipy.sparse import csr_matrix
           3 +from scipy.sparse.csgraph import dijkstra
           4 +
           5 +class GeneratedApproach:
           6 +    def __init__(self, action_space, observation_space, primitives):
           7 +        self.space = observation_space
           8 +    def objects(self, s, t):
           9 +        return s.get_objects(self.space.get_type(t))
          10 +    def xy(self,s,o):
          11 +        return np.array([s.get(o,'x'),s.get(o,'y')])
          12 +    def reset(self,state,info):
          13 +        self.rovers=[state.get_object_from_name('rover'+str(i)) for i in range(2)]
          14 +        self.homes=[self.xy(state,r) for r in self.rovers]
          15 +        self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
          16 +        self.lander=self.xy(state,self.objects(state,'lander')[0])
          17 +        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,2.5]])
          18 +        self.axis=np.arange(-2.3,2.301,0.1)
          19 +        self.n=len(self.axis)
          20 +        self.points=np.array([(x,y) for x in self.axis for y in self.axis])
          21 +        self.valid=self.free(self.points)
          22 +        self.bad=np.zeros((2,len(self.points),len(self.objs)),dtype=bool)
          23 +        self.send_bad=np.zeros((2,len(self.points)),dtype=bool)
          24 +        self.prev=None; self.step=0
          25 +        self.make_graph()
          26 +        self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
          27 +        self.sample_masks=[np.linalg.norm(self.points-self.xy(state,o),axis=1)<.245 for o in self.samples]
          28 +        self.radio_mask=self.visible(self.points,self.lander,4)
          29 +        self.home_dist=[dijkstra(self.graph,indices=self.nearest(h)) for h in self.homes]
          30 +    def free(self,p):
          31 +        p=np.atleast_2d(p)
          32 +        d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
          33 +        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.228**2,axis=1)
          34 +        ld=np.maximum(np.abs(p-self.lander)-np.array([.45,.30]),0)
          35 +        ok &= np.sum(ld**2,axis=1)>.228**2
          36 +        ok &= np.max(np.abs(p),axis=1)<2.271
          37 +        return ok
          38 +    def make_graph(self):
          39 +        rows=[]; cols=[]
          40 +        for i in np.flatnonzero(self.valid):
          41 +            x,y=divmod(i,self.n)
          42 +            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
          43 +                xx,yy=x+dx,y+dy
          44 +                if 0<=xx<self.n and 0<=yy<self.n:
          45 +                    j=xx*self.n+yy
          46 +                    if self.valid[j]: rows.append(i);cols.append(j)
          47 +        self.graph=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(self.points),len(self.points)))
          48 +    def visible(self,p,target,limit):
          49 +        p=np.atleast_2d(p); target=np.asarray(target)
          50 +        ok=np.linalg.norm(p-target,axis=1)<limit-.025
          51 +        # Low mounds do not occlude the camera, but pillars and wall do.
          52 +        boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
          53 +        delta=target-p
          54 +        for b in boxes:
          55 +            lo=b[:2]-b[2:];hi=b[:2]+b[2:]
          56 +            with np.errstate(divide='ignore',invalid='ignore'):
          57 +                t1=(lo-p)/delta;t2=(hi-p)/delta
          58 +            near=np.maximum(np.min(np.stack([t1,t2]),axis=0).max(axis=1),.001)
          59 +            far=np.minimum(np.max(np.stack([t1,t2]),axis=0).min(axis=1),.999)
          60 +            ok &= near>far
          61 +        return ok
          62 +    def nearest(self,p):
          63 +        ds=np.sum((self.points-p)**2,axis=1);ds[~self.valid]=np.inf
          64 +        return int(np.argmin(ds))
          65 +    def pending_count(self,s,i):
          66 +        return sum(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs)+sum(s.get(o,'analyzed_rover'+str(i)) and not s.get(o,'received_analysis') for o in self.samples)
          67 +    def get_action(self,s):
          68 +        self.step+=1
          69 +        pos=[self.xy(s,r) for r in self.rovers]
          70 +        if self.prev is not None:
          71 +            for i in range(2):
          72 +                old,move,op,idx,had=self.prev[i]
          73 +                if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
          74 +                    q=old+move
          75 +                    ids=np.linalg.norm(self.points-q,axis=1)<.085
          76 +                    self.valid[ids]=False
          77 +                    self.make_graph()
          78 +                if op==.5 and self.pending_count(s,i)>=had:
          79 +                    self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
          80 +                if op in [-.5,-1/6] and idx is not None:
          81 +                    if (op==-.5 and not s.get(self.rovers[i],'calibrated')) or (op==-1/6 and not s.get(self.objs[idx],'have_image_rover'+str(i))):
          82 +                        self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
          83 +        action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
          84 +        received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
          85 +        acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
          86 +        routes=[dijkstra(self.graph,indices=self.nearest(pos[i]),return_predecessors=True) for i in range(2)]
          87 +        options=[[],[]]
          88 +        for i,r in enumerate(self.rovers):
          89 +            dist=routes[i][0]
          90 +            candidates=[]
          91 +            for k in [0,1]:
          92 +                if not acquired[k] and not s.get(r,'store_full'):
          93 +                    for oi,o in enumerate(self.samples):
          94 +                        if int(s.get(o,'is_soil'))==k:
          95 +                            candidates.append((self.sample_masks[oi],'sample',o,k))
          96 +            for j,o in enumerate(self.objs):
          97 +                if not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]):
          98 +                    candidates.append((self.image_masks[j]&~self.bad[i,:,j],'image',o,j))
          99 +            if self.pending_count(s,i):
         100 +                candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
         101 +            for mask,task,o,j in candidates:
         102 +                dd=dist+.05*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         103 +                target=int(np.argmin(dd));cost=dd[target]
         104 +                if not np.isfinite(cost):continue
         105 +                cost+= .15*self.home_dist[i][target]
         106 +                if task=='send':cost+=5 if any(c[1]!='send' for c in candidates) else 0
         107 +                if hasattr(self,'last_tasks') and self.last_tasks[i]==(task,j):cost-=1.5
         108 +                options[i].append((cost,(target,task,o,j)))
         109 +            h=self.nearest(self.homes[i])
         110 +            options[i].append((12+.2*dist[h],(h,'home',None,None)))
         111 +        best_pair=None;best_score=np.inf
         112 +        anywork=any(len(o)>1 for o in options)
         113 +        for c0,b0 in options[0]:
         114 +            for c1,b1 in options[1]:
         115 +                if b0[1]==b1[1] and b0[1] in ['sample','image'] and b0[3]==b1[3]:continue
         116 +                if anywork and b0[1]==b1[1]=='home':continue
         117 +                score=max(c0,c1)+.3*(c0+c1)
         118 +                if score<best_score:best_score=score;best_pair=(b0,b1)
         119 +        if best_pair is None:best_pair=(options[0][-1][1],options[1][-1][1])
         120 +        self.last_tasks=[(b[1],b[3]) for b in best_pair]
         121 +        for i,r in enumerate(self.rovers):
         122 +            p=pos[i];start=self.nearest(p);dist,pred=routes[i]
         123 +            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
         124 +            best=best_pair[i]
         125 +            target,task,o,j=best
         126 +            if task=='send' and self.visible(p,self.lander,4)[0] and not self.send_bad[i,start]:
         127 +                target=self.nearest(self.homes[i]);task='home'
         128 +            if task=='sample': kinds.add(j)
         129 +            if task=='image': assigned.add(j)
         130 +            targetpos=self.points[target]
         131 +            if task=='home': targetpos=self.homes[i]
         132 +            path=[target];cur=target
         133 +            for _ in range(len(self.points)):
         134 +                if cur==start:break
         135 +                cur=int(pred[cur])
         136 +                if cur<0:break
         137 +                path.append(cur)
         138 +            path=path[::-1]
         139 +            goal=targetpos
         140 +            for node in path:
         141 +                q=self.points[node]
         142 +                if np.max(np.abs(q-p))<=.20001: goal=q
         143 +                else: break
         144 +            if np.max(np.abs(targetpos-p))<=.2:goal=targetpos
         145 +            move=np.clip(goal-p,-.2,.2)
         146 +            if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
         147 +            q=p+move; op=0.;idx=None
         148 +            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249:op=-5/6
         149 +            else:
         150 +                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
         151 +                if useful:
         152 +                    idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
         153 +                    op=-1/6 if s.get(r,'calibrated') else -.5
         154 +            if op==0 and pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
         155 +            elif op==0 and s.get(r,'store_full'):op=5/6
         156 +            elif op==0 and not s.get(r,'calibrated') and any(not s.get(oo,'received_image') for oo in self.objs) and any(self.visible(q,self.xy(s,oo),2)[0] for oo in self.objs):op=-.5
         157 +            action[4*i:4*i+2]=move;action[4*i+3]=op
         158 +            records.append((p,move,op,idx,self.pending_count(s,i)))
         159 +        self.prev=records
         160 +        return action
diff --git a/test_assignment.py b/test_assignment.py
new file mode 100644
index 0000000..ac268c0
--- /dev/null
+++ b/test_assignment.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +from candidate_assignment import GeneratedApproach as Candidate
           3 +from assignment_baseline import GeneratedApproach as Baseline
           4 +import json,time
           5 +for seed in range(30):
           6 + record={'seed':seed}
           7 + for label,cls in [('base',Baseline),('candidate',Candidate)]:
           8 +  e=make_env();s,info=e.reset(seed=seed);p=cls(e.action_space,e.observation_space,{})
           9 +  start=time.time();p.reset(s,info)
          10 +  for step in range(160):
          11 +   s,r,term,trunc,inf=e.step(p.get_action(s))
          12 +   if term or trunc:break
          13 +  record[label]={'steps':step+1,'success':term,'seconds':round(time.time()-start,3)}
          14 +  e.close()
          15 + print(json.dumps(record),flush=True)
```

</details>

<a id="C027"></a>
### C027 · Use total immediate task distance for joint rover matching

Commit `730d4d131cad228ad52b5f6964457a6bb6a66486`; parents: 744f3f611e5bfac5fb9a5460c344205be923b500. Recorded author date: 2026-09-20T03:55:20+02:00.

File roles (automatic): support code (role needs review).

[Exact all-file diff](evidence/diffs/C027_730d4d1.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/candidate_assignment.py b/candidate_assignment.py
index 960b8fb..2e24a9c 100644
--- a/candidate_assignment.py
+++ b/candidate_assignment.py
@@ -99,22 +99,21 @@ class GeneratedApproach:
   99     99              if self.pending_count(s,i):
  100    100                  candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
  101    101              for mask,task,o,j in candidates:
  102        -                dd=dist+.05*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         102 +                dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
  103    103                  target=int(np.argmin(dd));cost=dd[target]
  104    104                  if not np.isfinite(cost):continue
  105        -                cost+= .15*self.home_dist[i][target]
  106    105                  if task=='send':cost+=5 if any(c[1]!='send' for c in candidates) else 0
  107        -                if hasattr(self,'last_tasks') and self.last_tasks[i]==(task,j):cost-=1.5
         106 +                if hasattr(self,'last_tasks') and self.last_tasks[i]==(task,j):cost-=.1
  108    107                  options[i].append((cost,(target,task,o,j)))
  109    108              h=self.nearest(self.homes[i])
  110        -            options[i].append((12+.2*dist[h],(h,'home',None,None)))
         109 +            options[i].append((10000.,(h,'home',None,None)))
  111    110          best_pair=None;best_score=np.inf
  112    111          anywork=any(len(o)>1 for o in options)
  113    112          for c0,b0 in options[0]:
  114    113              for c1,b1 in options[1]:
  115    114                  if b0[1]==b1[1] and b0[1] in ['sample','image'] and b0[3]==b1[3]:continue
  116    115                  if anywork and b0[1]==b1[1]=='home':continue
  117        -                score=max(c0,c1)+.3*(c0+c1)
         116 +                score=c0+c1
  118    117                  if score<best_score:best_score=score;best_pair=(b0,b1)
  119    118          if best_pair is None:best_pair=(options[0][-1][1],options[1][-1][1])
  120    119          self.last_tasks=[(b[1],b[3]) for b in best_pair]
```

</details>

<a id="C028"></a>
### C028 · Refine radio visibility from measured occlusion and continue useful travel while transmitting

Commit `b429738699a38464886aabfb7bbe867cd69b77cc`; parents: 730d4d131cad228ad52b5f6964457a6bb6a66486. Recorded author date: 2026-09-20T03:55:28+02:00.

File roles (automatic): policy, setup/other.

- [E0083](01_timeline.md#E0083): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C028_b429738_approach.py) · [Exact all-file diff](evidence/diffs/C028_b429738.diff)

[Previous saved controller snapshot](evidence/versions/C025_9425eee_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 91d9276..9557a1c 100644
--- a/approach.py
+++ b/approach.py
@@ -47,12 +47,13 @@ class GeneratedApproach:
   47     47          self.graph=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(self.points),len(self.points)))
   48     48      def visible(self,p,target,limit):
   49     49          p=np.atleast_2d(p); target=np.asarray(target)
   50        -        ok=np.linalg.norm(p-target,axis=1)<limit-.025
          50 +        ok=np.linalg.norm(p-target,axis=1)<(3.91 if limit>3 else limit-.025)
   51     51          # Low mounds do not occlude the camera, but pillars and wall do.
   52     52          boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
   53     53          delta=target-p
   54     54          for b in boxes:
   55        -            lo=b[:2]-b[2:];hi=b[:2]+b[2:]
          55 +            padding=.05 if limit>3 else 0.
          56 +            lo=b[:2]-b[2:]-padding;hi=b[:2]+b[2:]+padding
   56     57              with np.errstate(divide='ignore',invalid='ignore'):
   57     58                  t1=(lo-p)/delta;t2=(hi-p)/delta
   58     59              near=np.maximum(np.min(np.stack([t1,t2]),axis=0).max(axis=1),.001)
@@ -108,7 +109,14 @@ class GeneratedApproach:
  108    109              if best is None: best=(self.nearest(self.homes[i]),'home',None,None)
  109    110              target,task,o,j=best
  110    111              if task=='send' and self.visible(p,self.lander,4)[0] and not self.send_bad[i,start]:
  111        -                target=self.nearest(self.homes[i]);task='home'
         112 +                navbest=None;navcost=np.inf
         113 +                for mask,nt,no,nj in candidates:
         114 +                    if nt=='send':continue
         115 +                    dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         116 +                    ni=int(np.argmin(dd))
         117 +                    if dd[ni]<navcost:navcost=dd[ni];navbest=(ni,nt,no,nj)
         118 +                if navbest is not None:target,task,o,j=navbest
         119 +                else:target=self.nearest(self.homes[i]);task='home'
  112    120              if task=='sample': kinds.add(j)
  113    121              if task=='image': assigned.add(j)
  114    122              targetpos=self.points[target]
diff --git a/assignment_minimax_results.jsonl b/assignment_minimax_results.jsonl
new file mode 100644
index 0000000..d2b4547
--- /dev/null
+++ b/assignment_minimax_results.jsonl
@@ -0,0 +1,11 @@
           1 +{"seed": 0, "base": {"steps": 39, "success": true, "seconds": 2.385}, "candidate": {"steps": 52, "success": true, "seconds": 3.705}}
           2 +{"seed": 1, "base": {"steps": 23, "success": true, "seconds": 1.557}, "candidate": {"steps": 34, "success": true, "seconds": 2.298}}
           3 +{"seed": 2, "base": {"steps": 23, "success": true, "seconds": 1.563}, "candidate": {"steps": 37, "success": true, "seconds": 2.418}}
           4 +{"seed": 3, "base": {"steps": 28, "success": true, "seconds": 1.684}, "candidate": {"steps": 44, "success": true, "seconds": 3.115}}
           5 +{"seed": 4, "base": {"steps": 26, "success": true, "seconds": 1.956}, "candidate": {"steps": 36, "success": true, "seconds": 2.538}}
           6 +{"seed": 5, "base": {"steps": 30, "success": true, "seconds": 1.931}, "candidate": {"steps": 43, "success": true, "seconds": 2.382}}
           7 +{"seed": 6, "base": {"steps": 20, "success": true, "seconds": 0.653}, "candidate": {"steps": 32, "success": true, "seconds": 1.212}}
           8 +{"seed": 7, "base": {"steps": 32, "success": true, "seconds": 1.352}, "candidate": {"steps": 39, "success": true, "seconds": 1.586}}
           9 +{"seed": 8, "base": {"steps": 25, "success": true, "seconds": 1.038}, "candidate": {"steps": 54, "success": true, "seconds": 2.49}}
          10 +{"seed": 9, "base": {"steps": 28, "success": true, "seconds": 0.715}, "candidate": {"steps": 37, "success": true, "seconds": 1.326}}
          11 +{"seed": 10, "base": {"steps": 30, "success": true, "seconds": 1.215}, "candidate": {"steps": 36, "success": true, "seconds": 1.946}}
diff --git a/assignment_results.jsonl b/assignment_results.jsonl
new file mode 100644
index 0000000..9444fb2
--- /dev/null
+++ b/assignment_results.jsonl
@@ -0,0 +1,2 @@
           1 +{"seed": 0, "base": {"steps": 39, "success": true, "seconds": 1.39}, "candidate": {"steps": 33, "success": true, "seconds": 1.286}}
           2 +{"seed": 1, "base": {"steps": 23, "success": true, "seconds": 0.623}, "candidate": {"steps": 23, "success": true, "seconds": 1.093}}
diff --git a/larger_stress.jsonl b/larger_stress.jsonl
new file mode 100644
index 0000000..d757283
--- /dev/null
+++ b/larger_stress.jsonl
@@ -0,0 +1,31 @@
           1 +{"seed": 100, "n": 4, "steps": 33, "success": true, "sec": 1.022}
           2 +{"seed": 101, "n": 4, "steps": 27, "success": true, "sec": 1.146}
           3 +{"seed": 102, "n": 4, "steps": 31, "success": true, "sec": 1.22}
           4 +{"seed": 103, "n": 4, "steps": 31, "success": true, "sec": 1.694}
           5 +{"seed": 104, "n": 4, "steps": 28, "success": true, "sec": 1.517}
           6 +{"seed": 105, "n": 4, "steps": 29, "success": true, "sec": 2.117}
           7 +{"seed": 106, "n": 4, "steps": 28, "success": true, "sec": 1.968}
           8 +{"seed": 107, "n": 4, "steps": 30, "success": true, "sec": 1.784}
           9 +{"seed": 108, "n": 4, "steps": 28, "success": true, "sec": 1.762}
          10 +{"seed": 109, "n": 4, "steps": 27, "success": true, "sec": 1.478}
          11 +{"seed": 110, "n": 4, "steps": 48, "success": true, "sec": 2.766}
          12 +{"seed": 111, "n": 4, "steps": 33, "success": true, "sec": 2.03}
          13 +{"seed": 112, "n": 4, "steps": 31, "success": true, "sec": 1.518}
          14 +{"seed": 113, "n": 4, "steps": 26, "success": true, "sec": 1.8}
          15 +{"seed": 114, "n": 4, "steps": 28, "success": true, "sec": 1.886}
          16 +{"seed": 115, "n": 4, "steps": 29, "success": true, "sec": 1.199}
          17 +{"seed": 116, "n": 4, "steps": 26, "success": true, "sec": 1.156}
          18 +{"seed": 117, "n": 4, "steps": 24, "success": true, "sec": 0.626}
          19 +{"seed": 118, "n": 4, "steps": 25, "success": true, "sec": 0.836}
          20 +{"seed": 119, "n": 4, "steps": 30, "success": true, "sec": 1.16}
          21 +{"seed": 120, "n": 4, "steps": 31, "success": true, "sec": 1.189}
          22 +{"seed": 121, "n": 4, "steps": 30, "success": true, "sec": 0.984}
          23 +{"seed": 122, "n": 4, "steps": 25, "success": true, "sec": 0.674}
          24 +{"seed": 123, "n": 4, "steps": 32, "success": true, "sec": 1.295}
          25 +{"seed": 124, "n": 4, "steps": 32, "success": true, "sec": 1.165}
          26 +{"seed": 125, "n": 4, "steps": 31, "success": true, "sec": 1.085}
          27 +{"seed": 126, "n": 4, "steps": 26, "success": true, "sec": 0.715}
          28 +{"seed": 127, "n": 4, "steps": 31, "success": true, "sec": 1.589}
          29 +{"seed": 128, "n": 4, "steps": 31, "success": true, "sec": 1.13}
          30 +{"seed": 129, "n": 4, "steps": 32, "success": true, "sec": 1.784}
          31 +{"seed": 130, "n": 4, "steps": 32, "success": true, "sec": 1.103}
diff --git a/travel_ops.jsonl b/travel_ops.jsonl
new file mode 100644
index 0000000..1b955ae
--- /dev/null
+++ b/travel_ops.jsonl
@@ -0,0 +1,30 @@
           1 +{"seed": 0, "n": 3, "steps": 39, "success": true, "sec": 0.424}
           2 +{"seed": 1, "n": 2, "steps": 23, "success": true, "sec": 0.362}
           3 +{"seed": 2, "n": 3, "steps": 23, "success": true, "sec": 0.248}
           4 +{"seed": 3, "n": 3, "steps": 28, "success": true, "sec": 0.427}
           5 +{"seed": 4, "n": 3, "steps": 26, "success": true, "sec": 0.455}
           6 +{"seed": 5, "n": 3, "steps": 30, "success": true, "sec": 0.579}
           7 +{"seed": 6, "n": 2, "steps": 20, "success": true, "sec": 0.276}
           8 +{"seed": 7, "n": 3, "steps": 32, "success": true, "sec": 0.491}
           9 +{"seed": 8, "n": 3, "steps": 25, "success": true, "sec": 0.398}
          10 +{"seed": 9, "n": 2, "steps": 28, "success": true, "sec": 0.424}
          11 +{"seed": 10, "n": 3, "steps": 30, "success": true, "sec": 0.51}
          12 +{"seed": 11, "n": 1, "steps": 29, "success": true, "sec": 0.282}
          13 +{"seed": 12, "n": 2, "steps": 26, "success": true, "sec": 0.845}
          14 +{"seed": 13, "n": 3, "steps": 34, "success": true, "sec": 1.37}
          15 +{"seed": 14, "n": 1, "steps": 37, "success": true, "sec": 1.168}
          16 +{"seed": 15, "n": 3, "steps": 35, "success": true, "sec": 1.528}
          17 +{"seed": 16, "n": 2, "steps": 26, "success": true, "sec": 1.498}
          18 +{"seed": 17, "n": 3, "steps": 31, "success": true, "sec": 2.575}
          19 +{"seed": 18, "n": 3, "steps": 26, "success": true, "sec": 1.964}
          20 +{"seed": 19, "n": 2, "steps": 32, "success": true, "sec": 1.972}
          21 +{"seed": 20, "n": 3, "steps": 32, "success": true, "sec": 1.788}
          22 +{"seed": 21, "n": 1, "steps": 31, "success": true, "sec": 1.817}
          23 +{"seed": 22, "n": 3, "steps": 25, "success": true, "sec": 1.727}
          24 +{"seed": 23, "n": 1, "steps": 20, "success": true, "sec": 0.697}
          25 +{"seed": 24, "n": 2, "steps": 25, "success": true, "sec": 1.693}
          26 +{"seed": 25, "n": 2, "steps": 23, "success": true, "sec": 1.638}
          27 +{"seed": 26, "n": 3, "steps": 26, "success": true, "sec": 1.334}
          28 +{"seed": 27, "n": 1, "steps": 24, "success": true, "sec": 1.523}
          29 +{"seed": 28, "n": 2, "steps": 25, "success": true, "sec": 1.308}
          30 +{"seed": 29, "n": 3, "steps": 28, "success": true, "sec": 1.983}
```

</details>

<a id="C029"></a>
### C029 · Compare balanced joint task distance without optional rover idling

Commit `ec4e79b4c244fce769b9ddd3b6f0c138ae7c90e2`; parents: b429738699a38464886aabfb7bbe867cd69b77cc. Recorded author date: 2026-09-20T03:56:03+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

[Exact all-file diff](evidence/diffs/C029_ec4e79b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/candidate_balanced.py b/candidate_balanced.py
new file mode 100644
index 0000000..987d5ae
--- /dev/null
+++ b/candidate_balanced.py
@@ -0,0 +1,159 @@
           1 +import numpy as np
           2 +from scipy.sparse import csr_matrix
           3 +from scipy.sparse.csgraph import dijkstra
           4 +
           5 +class GeneratedApproach:
           6 +    def __init__(self, action_space, observation_space, primitives):
           7 +        self.space = observation_space
           8 +    def objects(self, s, t):
           9 +        return s.get_objects(self.space.get_type(t))
          10 +    def xy(self,s,o):
          11 +        return np.array([s.get(o,'x'),s.get(o,'y')])
          12 +    def reset(self,state,info):
          13 +        self.rovers=[state.get_object_from_name('rover'+str(i)) for i in range(2)]
          14 +        self.homes=[self.xy(state,r) for r in self.rovers]
          15 +        self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
          16 +        self.lander=self.xy(state,self.objects(state,'lander')[0])
          17 +        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,2.5]])
          18 +        self.axis=np.arange(-2.3,2.301,0.1)
          19 +        self.n=len(self.axis)
          20 +        self.points=np.array([(x,y) for x in self.axis for y in self.axis])
          21 +        self.valid=self.free(self.points)
          22 +        self.bad=np.zeros((2,len(self.points),len(self.objs)),dtype=bool)
          23 +        self.send_bad=np.zeros((2,len(self.points)),dtype=bool)
          24 +        self.prev=None; self.step=0
          25 +        self.make_graph()
          26 +        self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
          27 +        self.sample_masks=[np.linalg.norm(self.points-self.xy(state,o),axis=1)<.245 for o in self.samples]
          28 +        self.radio_mask=self.visible(self.points,self.lander,4)
          29 +        self.home_dist=[dijkstra(self.graph,indices=self.nearest(h)) for h in self.homes]
          30 +    def free(self,p):
          31 +        p=np.atleast_2d(p)
          32 +        d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
          33 +        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.228**2,axis=1)
          34 +        ld=np.maximum(np.abs(p-self.lander)-np.array([.45,.30]),0)
          35 +        ok &= np.sum(ld**2,axis=1)>.228**2
          36 +        ok &= np.max(np.abs(p),axis=1)<2.271
          37 +        return ok
          38 +    def make_graph(self):
          39 +        rows=[]; cols=[]
          40 +        for i in np.flatnonzero(self.valid):
          41 +            x,y=divmod(i,self.n)
          42 +            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
          43 +                xx,yy=x+dx,y+dy
          44 +                if 0<=xx<self.n and 0<=yy<self.n:
          45 +                    j=xx*self.n+yy
          46 +                    if self.valid[j]: rows.append(i);cols.append(j)
          47 +        self.graph=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(self.points),len(self.points)))
          48 +    def visible(self,p,target,limit):
          49 +        p=np.atleast_2d(p); target=np.asarray(target)
          50 +        ok=np.linalg.norm(p-target,axis=1)<limit-.025
          51 +        # Low mounds do not occlude the camera, but pillars and wall do.
          52 +        boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
          53 +        delta=target-p
          54 +        for b in boxes:
          55 +            lo=b[:2]-b[2:];hi=b[:2]+b[2:]
          56 +            with np.errstate(divide='ignore',invalid='ignore'):
          57 +                t1=(lo-p)/delta;t2=(hi-p)/delta
          58 +            near=np.maximum(np.min(np.stack([t1,t2]),axis=0).max(axis=1),.001)
          59 +            far=np.minimum(np.max(np.stack([t1,t2]),axis=0).min(axis=1),.999)
          60 +            ok &= near>far
          61 +        return ok
          62 +    def nearest(self,p):
          63 +        ds=np.sum((self.points-p)**2,axis=1);ds[~self.valid]=np.inf
          64 +        return int(np.argmin(ds))
          65 +    def pending_count(self,s,i):
          66 +        return sum(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs)+sum(s.get(o,'analyzed_rover'+str(i)) and not s.get(o,'received_analysis') for o in self.samples)
          67 +    def get_action(self,s):
          68 +        self.step+=1
          69 +        pos=[self.xy(s,r) for r in self.rovers]
          70 +        if self.prev is not None:
          71 +            for i in range(2):
          72 +                old,move,op,idx,had=self.prev[i]
          73 +                if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
          74 +                    q=old+move
          75 +                    ids=np.linalg.norm(self.points-q,axis=1)<.085
          76 +                    self.valid[ids]=False
          77 +                    self.make_graph()
          78 +                if op==.5 and self.pending_count(s,i)>=had:
          79 +                    self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
          80 +                if op in [-.5,-1/6] and idx is not None:
          81 +                    if (op==-.5 and not s.get(self.rovers[i],'calibrated')) or (op==-1/6 and not s.get(self.objs[idx],'have_image_rover'+str(i))):
          82 +                        self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
          83 +        action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
          84 +        received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
          85 +        acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
          86 +        routes=[dijkstra(self.graph,indices=self.nearest(pos[i]),return_predecessors=True) for i in range(2)]
          87 +        options=[[],[]]
          88 +        for i,r in enumerate(self.rovers):
          89 +            dist=routes[i][0]
          90 +            candidates=[]
          91 +            for k in [0,1]:
          92 +                if not acquired[k] and not s.get(r,'store_full'):
          93 +                    for oi,o in enumerate(self.samples):
          94 +                        if int(s.get(o,'is_soil'))==k:
          95 +                            candidates.append((self.sample_masks[oi],'sample',o,k))
          96 +            for j,o in enumerate(self.objs):
          97 +                if not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]):
          98 +                    candidates.append((self.image_masks[j]&~self.bad[i,:,j],'image',o,j))
          99 +            if self.pending_count(s,i):
         100 +                candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
         101 +            for mask,task,o,j in candidates:
         102 +                dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         103 +                target=int(np.argmin(dd));cost=dd[target]
         104 +                if not np.isfinite(cost):continue
         105 +                if task=='send':cost+=5 if any(c[1]!='send' for c in candidates) else 0
         106 +                if hasattr(self,'last_tasks') and self.last_tasks[i]==(task,j):cost-=.1
         107 +                options[i].append((cost,(target,task,o,j)))
         108 +            h=self.nearest(self.homes[i])
         109 +            options[i].append((10000.,(h,'home',None,None)))
         110 +        best_pair=None;best_score=np.inf
         111 +        anywork=any(len(o)>1 for o in options)
         112 +        for c0,b0 in options[0]:
         113 +            for c1,b1 in options[1]:
         114 +                if b0[1]==b1[1] and b0[1] in ['sample','image'] and b0[3]==b1[3]:continue
         115 +                if anywork and b0[1]==b1[1]=='home':continue
         116 +                score=max(c0,c1)+.3*(c0+c1)
         117 +                if score<best_score:best_score=score;best_pair=(b0,b1)
         118 +        if best_pair is None:best_pair=(options[0][-1][1],options[1][-1][1])
         119 +        self.last_tasks=[(b[1],b[3]) for b in best_pair]
         120 +        for i,r in enumerate(self.rovers):
         121 +            p=pos[i];start=self.nearest(p);dist,pred=routes[i]
         122 +            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
         123 +            best=best_pair[i]
         124 +            target,task,o,j=best
         125 +            if task=='send' and self.visible(p,self.lander,4)[0] and not self.send_bad[i,start]:
         126 +                target=self.nearest(self.homes[i]);task='home'
         127 +            if task=='sample': kinds.add(j)
         128 +            if task=='image': assigned.add(j)
         129 +            targetpos=self.points[target]
         130 +            if task=='home': targetpos=self.homes[i]
         131 +            path=[target];cur=target
         132 +            for _ in range(len(self.points)):
         133 +                if cur==start:break
         134 +                cur=int(pred[cur])
         135 +                if cur<0:break
         136 +                path.append(cur)
         137 +            path=path[::-1]
         138 +            goal=targetpos
         139 +            for node in path:
         140 +                q=self.points[node]
         141 +                if np.max(np.abs(q-p))<=.20001: goal=q
         142 +                else: break
         143 +            if np.max(np.abs(targetpos-p))<=.2:goal=targetpos
         144 +            move=np.clip(goal-p,-.2,.2)
         145 +            if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
         146 +            q=p+move; op=0.;idx=None
         147 +            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249:op=-5/6
         148 +            else:
         149 +                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
         150 +                if useful:
         151 +                    idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
         152 +                    op=-1/6 if s.get(r,'calibrated') else -.5
         153 +            if op==0 and pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
         154 +            elif op==0 and s.get(r,'store_full'):op=5/6
         155 +            elif op==0 and not s.get(r,'calibrated') and any(not s.get(oo,'received_image') for oo in self.objs) and any(self.visible(q,self.xy(s,oo),2)[0] for oo in self.objs):op=-.5
         156 +            action[4*i:4*i+2]=move;action[4*i+3]=op
         157 +            records.append((p,move,op,idx,self.pending_count(s,i)))
         158 +        self.prev=records
         159 +        return action
diff --git a/test_balanced.py b/test_balanced.py
new file mode 100644
index 0000000..3ff979f
--- /dev/null
+++ b/test_balanced.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +from candidate_balanced import GeneratedApproach as Candidate
           3 +from assignment_baseline import GeneratedApproach as Baseline
           4 +import json,time
           5 +for seed in range(10):
           6 + record={'seed':seed}
           7 + for label,cls in [('candidate',Candidate)]:
           8 +  e=make_env();s,info=e.reset(seed=seed);p=cls(e.action_space,e.observation_space,{})
           9 +  start=time.time();p.reset(s,info)
          10 +  for step in range(160):
          11 +   s,r,term,trunc,inf=e.step(p.get_action(s))
          12 +   if term or trunc:break
          13 +  record[label]={'steps':step+1,'success':term,'seconds':round(time.time()-start,3)}
          14 +  e.close()
          15 + print(json.dumps(record),flush=True)
```

</details>

<a id="C030"></a>
### C030 · Probe sample selector priority and repeated collection semantics

Commit `2f9bf86e9bf4aea1d33a960b1a396787412c946b`; parents: ec4e79b4c244fce769b9ddd3b6f0c138ae7c90e2. Recorded author date: 2026-09-20T03:56:28+02:00.

File roles (automatic): diagnostic/test, setup/other.

[Exact all-file diff](evidence/diffs/C030_2f9bf86.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/assignment_results.jsonl b/assignment_results.jsonl
index 9444fb2..ba50b2e 100644
--- a/assignment_results.jsonl
+++ b/assignment_results.jsonl
@@ -1,2 +1,15 @@
    1      1  {"seed": 0, "base": {"steps": 39, "success": true, "seconds": 1.39}, "candidate": {"steps": 33, "success": true, "seconds": 1.286}}
    2      2  {"seed": 1, "base": {"steps": 23, "success": true, "seconds": 0.623}, "candidate": {"steps": 23, "success": true, "seconds": 1.093}}
           3 +{"seed": 2, "base": {"steps": 23, "success": true, "seconds": 0.996}, "candidate": {"steps": 25, "success": true, "seconds": 1.294}}
           4 +{"seed": 3, "base": {"steps": 28, "success": true, "seconds": 1.237}, "candidate": {"steps": 32, "success": true, "seconds": 1.245}}
           5 +{"seed": 4, "base": {"steps": 26, "success": true, "seconds": 1.65}, "candidate": {"steps": 26, "success": true, "seconds": 1.467}}
           6 +{"seed": 5, "base": {"steps": 30, "success": true, "seconds": 1.617}, "candidate": {"steps": 31, "success": true, "seconds": 2.128}}
           7 +{"seed": 6, "base": {"steps": 20, "success": true, "seconds": 0.988}, "candidate": {"steps": 20, "success": true, "seconds": 1.269}}
           8 +{"seed": 7, "base": {"steps": 32, "success": true, "seconds": 1.946}, "candidate": {"steps": 27, "success": true, "seconds": 1.338}}
           9 +{"seed": 8, "base": {"steps": 25, "success": true, "seconds": 1.625}, "candidate": {"steps": 25, "success": true, "seconds": 1.816}}
          10 +{"seed": 9, "base": {"steps": 28, "success": true, "seconds": 1.779}, "candidate": {"steps": 28, "success": true, "seconds": 1.495}}
          11 +{"seed": 10, "base": {"steps": 30, "success": true, "seconds": 1.578}, "candidate": {"steps": 30, "success": true, "seconds": 1.317}}
          12 +{"seed": 11, "base": {"steps": 29, "success": true, "seconds": 1.651}, "candidate": {"steps": 21, "success": true, "seconds": 2.005}}
          13 +{"seed": 12, "base": {"steps": 26, "success": true, "seconds": 2.068}, "candidate": {"steps": 26, "success": true, "seconds": 2.206}}
          14 +{"seed": 13, "base": {"steps": 34, "success": true, "seconds": 2.591}, "candidate": {"steps": 33, "success": true, "seconds": 1.74}}
          15 +{"seed": 14, "base": {"steps": 37, "success": true, "seconds": 2.23}, "candidate": {"steps": 35, "success": true, "seconds": 1.481}}
diff --git a/balanced_results.jsonl b/balanced_results.jsonl
new file mode 100644
index 0000000..3f6fd9f
--- /dev/null
+++ b/balanced_results.jsonl
@@ -0,0 +1,9 @@
           1 +{"seed": 0, "candidate": {"steps": 33, "success": true, "seconds": 2.594}}
           2 +{"seed": 1, "candidate": {"steps": 23, "success": true, "seconds": 2.078}}
           3 +{"seed": 2, "candidate": {"steps": 25, "success": true, "seconds": 1.9}}
           4 +{"seed": 3, "candidate": {"steps": 32, "success": true, "seconds": 2.653}}
           5 +{"seed": 4, "candidate": {"steps": 26, "success": true, "seconds": 2.207}}
           6 +{"seed": 5, "candidate": {"steps": 31, "success": true, "seconds": 1.873}}
           7 +{"seed": 6, "candidate": {"steps": 20, "success": true, "seconds": 1.284}}
           8 +{"seed": 7, "candidate": {"steps": 31, "success": true, "seconds": 1.728}}
           9 +{"seed": 8, "candidate": {"steps": 25, "success": true, "seconds": 1.844}}
diff --git a/larger_stress.jsonl b/larger_stress.jsonl
index d757283..cd2f639 100644
--- a/larger_stress.jsonl
+++ b/larger_stress.jsonl
@@ -29,3 +29,22 @@
   29     29  {"seed": 128, "n": 4, "steps": 31, "success": true, "sec": 1.13}
   30     30  {"seed": 129, "n": 4, "steps": 32, "success": true, "sec": 1.784}
   31     31  {"seed": 130, "n": 4, "steps": 32, "success": true, "sec": 1.103}
          32 +{"seed": 131, "n": 4, "steps": 29, "success": true, "sec": 0.894}
          33 +{"seed": 132, "n": 4, "steps": 33, "success": true, "sec": 1.477}
          34 +{"seed": 133, "n": 4, "steps": 30, "success": true, "sec": 1.641}
          35 +{"seed": 134, "n": 4, "steps": 30, "success": true, "sec": 1.543}
          36 +{"seed": 135, "n": 4, "steps": 34, "success": true, "sec": 1.771}
          37 +{"seed": 136, "n": 4, "steps": 33, "success": true, "sec": 1.904}
          38 +{"seed": 137, "n": 4, "steps": 34, "success": true, "sec": 2.601}
          39 +{"seed": 138, "n": 4, "steps": 34, "success": true, "sec": 1.854}
          40 +{"seed": 139, "n": 4, "steps": 31, "success": true, "sec": 2.073}
          41 +{"seed": 140, "n": 4, "steps": 30, "success": true, "sec": 1.819}
          42 +{"seed": 141, "n": 4, "steps": 33, "success": true, "sec": 2.196}
          43 +{"seed": 142, "n": 4, "steps": 29, "success": true, "sec": 1.809}
          44 +{"seed": 143, "n": 4, "steps": 27, "success": true, "sec": 1.45}
          45 +{"seed": 144, "n": 4, "steps": 31, "success": true, "sec": 1.638}
          46 +{"seed": 145, "n": 4, "steps": 28, "success": true, "sec": 1.681}
          47 +{"seed": 146, "n": 4, "steps": 28, "success": true, "sec": 3.2}
          48 +{"seed": 147, "n": 4, "steps": 35, "success": true, "sec": 2.84}
          49 +{"seed": 148, "n": 4, "steps": 27, "success": true, "sec": 2.301}
          50 +{"seed": 149, "n": 4, "steps": 34, "success": true, "sec": 2.68}
diff --git a/probe_samples.py b/probe_samples.py
new file mode 100644
index 0000000..e43253b
--- /dev/null
+++ b/probe_samples.py
@@ -0,0 +1,42 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +from scipy.sparse.csgraph import dijkstra
           4 +import numpy as np
           5 +for seed in range(200):
           6 + e=make_env();s,_=e.reset(seed=seed)
           7 + samples=sorted(s.get_objects(e.observation_space.get_type('sample')),key=lambda o:o.name)
           8 + coords=np.array([[s.get(o,'x'),s.get(o,'y')] for o in samples])
           9 + pairs=[(i,j) for i in range(3) for j in range(3,6) if np.linalg.norm(coords[i]-coords[j])<.44]
          10 + if not pairs:e.close();continue
          11 + p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,{})
          12 + found=False
          13 + for stone,soil in pairs:
          14 +  d1=np.linalg.norm(p.points-coords[stone],axis=1);d2=np.linalg.norm(p.points-coords[soil],axis=1)
          15 +  ids=np.flatnonzero(p.valid&(d1<.245)&(d2<d1-.025))
          16 +  for end in ids:
          17 +   j=0 if p.points[end,0]>0 else 1;r=p.rovers[j]
          18 +   dist,pred=dijkstra(p.graph,indices=p.nearest(p.homes[j]),return_predecessors=True)
          19 +   if np.isfinite(dist[end]):found=True;break
          20 +  if found:break
          21 + if not found:e.close();continue
          22 + print('seed',seed,'pair',stone,soil,'coords',coords.tolist(),'target',p.points[end].tolist(),'dist',d1[end],d2[end],flush=True)
          23 + def step(move,op):
          24 +  global s
          25 +  a=np.zeros(8);a[4*j:4*j+2]=move;a[4*j+3]=op;s,*_=e.step(a)
          26 + for k in range(130):
          27 +  q=p.xy(s,r);start=p.nearest(q)
          28 +  if np.linalg.norm(q-p.points[end])<.01:break
          29 +  dist,pred=dijkstra(p.graph,indices=start,return_predecessors=True);path=[end]
          30 +  while path[-1]!=start:
          31 +   z=int(pred[path[-1]])
          32 +   if z<0:break
          33 +   path.append(z)
          34 +  dest=p.points[path[-2] if len(path)>1 else end];step(np.clip(dest-q,-.2,.2),0)
          35 +  if np.linalg.norm(p.xy(s,r)-q)<1e-7:break
          36 + print('arrived',p.xy(s,r).tolist(),flush=True)
          37 + for rep in range(3):
          38 +  step([0,0],-5/6)
          39 +  print('sample',rep,'full',s.get(r,'store_full'),'analyzed',[o.name for o in samples if s.get(o,'analyzed_rover'+str(j))],flush=True)
          40 +  step([0,0],5/6)
          41 + e.close()
          42 + break
diff --git a/refined_radio.jsonl b/refined_radio.jsonl
new file mode 100644
index 0000000..8745e54
--- /dev/null
+++ b/refined_radio.jsonl
@@ -0,0 +1,24 @@
           1 +{"seed": 0, "n": 3, "steps": 34, "success": true, "sec": 1.438}
           2 +{"seed": 1, "n": 2, "steps": 21, "success": true, "sec": 1.155}
           3 +{"seed": 2, "n": 3, "steps": 22, "success": true, "sec": 1.506}
           4 +{"seed": 3, "n": 3, "steps": 26, "success": true, "sec": 1.324}
           5 +{"seed": 4, "n": 3, "steps": 24, "success": true, "sec": 1.065}
           6 +{"seed": 5, "n": 3, "steps": 30, "success": true, "sec": 1.745}
           7 +{"seed": 6, "n": 2, "steps": 22, "success": true, "sec": 1.869}
           8 +{"seed": 7, "n": 3, "steps": 33, "success": true, "sec": 2.481}
           9 +{"seed": 8, "n": 3, "steps": 26, "success": true, "sec": 1.577}
          10 +{"seed": 9, "n": 2, "steps": 25, "success": true, "sec": 1.07}
          11 +{"seed": 10, "n": 3, "steps": 26, "success": true, "sec": 1.658}
          12 +{"seed": 11, "n": 1, "steps": 28, "success": true, "sec": 1.83}
          13 +{"seed": 12, "n": 2, "steps": 26, "success": true, "sec": 1.848}
          14 +{"seed": 13, "n": 3, "steps": 33, "success": true, "sec": 1.928}
          15 +{"seed": 14, "n": 1, "steps": 37, "success": true, "sec": 2.017}
          16 +{"seed": 15, "n": 3, "steps": 47, "success": true, "sec": 4.129}
          17 +{"seed": 16, "n": 2, "steps": 26, "success": true, "sec": 2.773}
          18 +{"seed": 17, "n": 3, "steps": 31, "success": true, "sec": 2.73}
          19 +{"seed": 18, "n": 3, "steps": 32, "success": true, "sec": 2.573}
          20 +{"seed": 19, "n": 2, "steps": 30, "success": true, "sec": 1.661}
          21 +{"seed": 20, "n": 3, "steps": 36, "success": true, "sec": 2.147}
          22 +{"seed": 21, "n": 1, "steps": 33, "success": true, "sec": 1.885}
          23 +{"seed": 22, "n": 3, "steps": 25, "success": true, "sec": 1.234}
          24 +{"seed": 23, "n": 1, "steps": 18, "success": true, "sec": 1.467}
diff --git a/stress_500.jsonl b/stress_500.jsonl
new file mode 100644
index 0000000..e69de29
```

</details>

<a id="C031"></a>
### C031 · Avoid repeatedly collecting the wrong material near overlapping sample sites

Commit `6b263fc3e3c730a37ee698d3f8199d75c74f5ef3`; parents: 2f9bf86e9bf4aea1d33a960b1a396787412c946b. Recorded author date: 2026-09-20T03:57:10+02:00.

File roles (automatic): policy, setup/other.

- [E0085](01_timeline.md#E0085): commit hash in recorded output.
[Controller after this commit](evidence/versions/C031_6b263fc_approach.py) · [Exact all-file diff](evidence/diffs/C031_6b263fc.diff)

[Previous saved controller snapshot](evidence/versions/C028_b429738_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9557a1c..a8afb6b 100644
--- a/approach.py
+++ b/approach.py
@@ -24,7 +24,8 @@ class GeneratedApproach:
   24     24          self.prev=None; self.step=0
   25     25          self.make_graph()
   26     26          self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
   27        -        self.sample_masks=[np.linalg.norm(self.points-self.xy(state,o),axis=1)<.245 for o in self.samples]
          27 +        sample_dist=np.array([np.linalg.norm(self.points-self.xy(state,o),axis=1) for o in self.samples])
          28 +        self.sample_masks=[(dd<.245)&(dd<=sample_dist.min(axis=0)+1e-8) for dd in sample_dist]
   28     29          self.radio_mask=self.visible(self.points,self.lander,4)
   29     30          self.home_dist=[dijkstra(self.graph,indices=self.nearest(h)) for h in self.homes]
   30     31      def free(self,p):
@@ -48,7 +49,7 @@ class GeneratedApproach:
   48     49      def visible(self,p,target,limit):
   49     50          p=np.atleast_2d(p); target=np.asarray(target)
   50     51          ok=np.linalg.norm(p-target,axis=1)<(3.91 if limit>3 else limit-.025)
   51        -        # Low mounds do not occlude the camera, but pillars and wall do.
          52 +        # Low mounds and the central driving wall do not obstruct the camera.
   52     53          boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
   53     54          delta=target-p
   54     55          for b in boxes:
@@ -137,7 +138,8 @@ class GeneratedApproach:
  137    138              move=np.clip(goal-p,-.2,.2)
  138    139              if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
  139    140              q=p+move; op=0.;idx=None
  140        -            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249:op=-5/6
         141 +            nearest_sample=min(self.samples,key=lambda oo:np.linalg.norm(q-self.xy(s,oo)))
         142 +            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249 and s.get(nearest_sample,'is_soil')==j:op=-5/6
  141    143              else:
  142    144                  useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
  143    145                  if useful:
diff --git a/assignment_results.jsonl b/assignment_results.jsonl
index ba50b2e..aff0cf0 100644
--- a/assignment_results.jsonl
+++ b/assignment_results.jsonl
@@ -13,3 +13,15 @@
   13     13  {"seed": 12, "base": {"steps": 26, "success": true, "seconds": 2.068}, "candidate": {"steps": 26, "success": true, "seconds": 2.206}}
   14     14  {"seed": 13, "base": {"steps": 34, "success": true, "seconds": 2.591}, "candidate": {"steps": 33, "success": true, "seconds": 1.74}}
   15     15  {"seed": 14, "base": {"steps": 37, "success": true, "seconds": 2.23}, "candidate": {"steps": 35, "success": true, "seconds": 1.481}}
          16 +{"seed": 15, "base": {"steps": 35, "success": true, "seconds": 3.37}, "candidate": {"steps": 32, "success": true, "seconds": 3.801}}
          17 +{"seed": 16, "base": {"steps": 26, "success": true, "seconds": 1.645}, "candidate": {"steps": 26, "success": true, "seconds": 2.065}}
          18 +{"seed": 17, "base": {"steps": 31, "success": true, "seconds": 2.344}, "candidate": {"steps": 31, "success": true, "seconds": 1.393}}
          19 +{"seed": 18, "base": {"steps": 26, "success": true, "seconds": 1.14}, "candidate": {"steps": 26, "success": true, "seconds": 1.131}}
          20 +{"seed": 19, "base": {"steps": 32, "success": true, "seconds": 1.219}, "candidate": {"steps": 32, "success": true, "seconds": 1.051}}
          21 +{"seed": 20, "base": {"steps": 32, "success": true, "seconds": 1.201}, "candidate": {"steps": 34, "success": true, "seconds": 1.2}}
          22 +{"seed": 21, "base": {"steps": 31, "success": true, "seconds": 1.138}, "candidate": {"steps": 31, "success": true, "seconds": 1.225}}
          23 +{"seed": 22, "base": {"steps": 25, "success": true, "seconds": 0.654}, "candidate": {"steps": 25, "success": true, "seconds": 0.92}}
          24 +{"seed": 23, "base": {"steps": 20, "success": true, "seconds": 0.434}, "candidate": {"steps": 20, "success": true, "seconds": 0.694}}
          25 +{"seed": 24, "base": {"steps": 25, "success": true, "seconds": 0.982}, "candidate": {"steps": 25, "success": true, "seconds": 0.629}}
          26 +{"seed": 25, "base": {"steps": 23, "success": true, "seconds": 0.605}, "candidate": {"steps": 23, "success": true, "seconds": 0.904}}
          27 +{"seed": 26, "base": {"steps": 26, "success": true, "seconds": 1.111}, "candidate": {"steps": 30, "success": true, "seconds": 1.081}}
diff --git a/balanced_results.jsonl b/balanced_results.jsonl
index 3f6fd9f..6eb1fae 100644
--- a/balanced_results.jsonl
+++ b/balanced_results.jsonl
@@ -7,3 +7,4 @@
    7      7  {"seed": 6, "candidate": {"steps": 20, "success": true, "seconds": 1.284}}
    8      8  {"seed": 7, "candidate": {"steps": 31, "success": true, "seconds": 1.728}}
    9      9  {"seed": 8, "candidate": {"steps": 25, "success": true, "seconds": 1.844}}
          10 +{"seed": 9, "candidate": {"steps": 28, "success": true, "seconds": 4.705}}
diff --git a/refined_radio.jsonl b/refined_radio.jsonl
index 8745e54..63476b3 100644
--- a/refined_radio.jsonl
+++ b/refined_radio.jsonl
@@ -22,3 +22,9 @@
   22     22  {"seed": 21, "n": 1, "steps": 33, "success": true, "sec": 1.885}
   23     23  {"seed": 22, "n": 3, "steps": 25, "success": true, "sec": 1.234}
   24     24  {"seed": 23, "n": 1, "steps": 18, "success": true, "sec": 1.467}
          25 +{"seed": 24, "n": 2, "steps": 25, "success": true, "sec": 3.552}
          26 +{"seed": 25, "n": 2, "steps": 22, "success": true, "sec": 1.795}
          27 +{"seed": 26, "n": 3, "steps": 25, "success": true, "sec": 1.436}
          28 +{"seed": 27, "n": 1, "steps": 24, "success": true, "sec": 1.507}
          29 +{"seed": 28, "n": 2, "steps": 26, "success": true, "sec": 1.341}
          30 +{"seed": 29, "n": 3, "steps": 26, "success": true, "sec": 1.441}
diff --git a/stress_500.jsonl b/stress_500.jsonl
index e69de29..e963dfe 100644
--- a/stress_500.jsonl
+++ b/stress_500.jsonl
@@ -0,0 +1,21 @@
           1 +{"seed": 500, "n": 4, "steps": 28, "success": true, "sec": 3.293}
           2 +{"seed": 501, "n": 4, "steps": 31, "success": true, "sec": 3.05}
           3 +{"seed": 502, "n": 4, "steps": 37, "success": true, "sec": 2.451}
           4 +{"seed": 503, "n": 4, "steps": 34, "success": true, "sec": 1.941}
           5 +{"seed": 504, "n": 4, "steps": 29, "success": true, "sec": 1.503}
           6 +{"seed": 505, "n": 4, "steps": 30, "success": true, "sec": 1.017}
           7 +{"seed": 506, "n": 4, "steps": 28, "success": true, "sec": 0.995}
           8 +{"seed": 507, "n": 4, "steps": 29, "success": true, "sec": 1.313}
           9 +{"seed": 508, "n": 4, "steps": 26, "success": true, "sec": 0.935}
          10 +{"seed": 509, "n": 4, "steps": 22, "success": true, "sec": 0.851}
          11 +{"seed": 510, "n": 4, "steps": 29, "success": true, "sec": 1.109}
          12 +{"seed": 511, "n": 4, "steps": 25, "success": true, "sec": 1.147}
          13 +{"seed": 512, "n": 4, "steps": 34, "success": true, "sec": 1.391}
          14 +{"seed": 513, "n": 4, "steps": 34, "success": true, "sec": 1.453}
          15 +{"seed": 514, "n": 4, "steps": 33, "success": true, "sec": 1.65}
          16 +{"seed": 515, "n": 4, "steps": 34, "success": true, "sec": 1.286}
          17 +{"seed": 516, "n": 4, "steps": 28, "success": true, "sec": 1.058}
          18 +{"seed": 517, "n": 4, "steps": 30, "success": true, "sec": 1.633}
          19 +{"seed": 518, "n": 4, "steps": 32, "success": true, "sec": 1.024}
          20 +{"seed": 519, "n": 4, "steps": 28, "success": true, "sec": 0.996}
          21 +{"seed": 520, "n": 4, "steps": 29, "success": true, "sec": 1.133}
```

</details>

<a id="C032"></a>
### C032 · Add a sample-first scheduling candidate for comparative evaluation

Commit `fd291b629a9a63642dd93948bc5e8133ee3f62e9`; parents: 6b263fc3e3c730a37ee698d3f8199d75c74f5ef3. Recorded author date: 2026-09-20T03:57:10+02:00.

File roles (automatic): diagnostic/test, support code (role needs review).

- [E0092](01_timeline.md#E0092): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C032_fd291b6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/sample_priority.py b/sample_priority.py
new file mode 100644
index 0000000..2355d08
--- /dev/null
+++ b/sample_priority.py
@@ -0,0 +1,155 @@
           1 +import numpy as np
           2 +from scipy.sparse import csr_matrix
           3 +from scipy.sparse.csgraph import dijkstra
           4 +
           5 +class GeneratedApproach:
           6 +    def __init__(self, action_space, observation_space, primitives):
           7 +        self.space = observation_space
           8 +    def objects(self, s, t):
           9 +        return s.get_objects(self.space.get_type(t))
          10 +    def xy(self,s,o):
          11 +        return np.array([s.get(o,'x'),s.get(o,'y')])
          12 +    def reset(self,state,info):
          13 +        self.rovers=[state.get_object_from_name('rover'+str(i)) for i in range(2)]
          14 +        self.homes=[self.xy(state,r) for r in self.rovers]
          15 +        self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
          16 +        self.lander=self.xy(state,self.objects(state,'lander')[0])
          17 +        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,2.5]])
          18 +        self.axis=np.arange(-2.3,2.301,0.1)
          19 +        self.n=len(self.axis)
          20 +        self.points=np.array([(x,y) for x in self.axis for y in self.axis])
          21 +        self.valid=self.free(self.points)
          22 +        self.bad=np.zeros((2,len(self.points),len(self.objs)),dtype=bool)
          23 +        self.send_bad=np.zeros((2,len(self.points)),dtype=bool)
          24 +        self.prev=None; self.step=0
          25 +        self.make_graph()
          26 +        self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
          27 +        sample_dist=np.array([np.linalg.norm(self.points-self.xy(state,o),axis=1) for o in self.samples])
          28 +        self.sample_masks=[(dd<.245)&(dd<=sample_dist.min(axis=0)+1e-8) for dd in sample_dist]
          29 +        self.radio_mask=self.visible(self.points,self.lander,4)
          30 +        self.home_dist=[dijkstra(self.graph,indices=self.nearest(h)) for h in self.homes]
          31 +    def free(self,p):
          32 +        p=np.atleast_2d(p)
          33 +        d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
          34 +        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.228**2,axis=1)
          35 +        ld=np.maximum(np.abs(p-self.lander)-np.array([.45,.30]),0)
          36 +        ok &= np.sum(ld**2,axis=1)>.228**2
          37 +        ok &= np.max(np.abs(p),axis=1)<2.271
          38 +        return ok
          39 +    def make_graph(self):
          40 +        rows=[]; cols=[]
          41 +        for i in np.flatnonzero(self.valid):
          42 +            x,y=divmod(i,self.n)
          43 +            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
          44 +                xx,yy=x+dx,y+dy
          45 +                if 0<=xx<self.n and 0<=yy<self.n:
          46 +                    j=xx*self.n+yy
          47 +                    if self.valid[j]: rows.append(i);cols.append(j)
          48 +        self.graph=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(self.points),len(self.points)))
          49 +    def visible(self,p,target,limit):
          50 +        p=np.atleast_2d(p); target=np.asarray(target)
          51 +        ok=np.linalg.norm(p-target,axis=1)<(3.91 if limit>3 else limit-.025)
          52 +        # Low mounds and the central driving wall do not obstruct the camera.
          53 +        boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
          54 +        delta=target-p
          55 +        for b in boxes:
          56 +            padding=.05 if limit>3 else 0.
          57 +            lo=b[:2]-b[2:]-padding;hi=b[:2]+b[2:]+padding
          58 +            with np.errstate(divide='ignore',invalid='ignore'):
          59 +                t1=(lo-p)/delta;t2=(hi-p)/delta
          60 +            near=np.maximum(np.min(np.stack([t1,t2]),axis=0).max(axis=1),.001)
          61 +            far=np.minimum(np.max(np.stack([t1,t2]),axis=0).min(axis=1),.999)
          62 +            ok &= near>far
          63 +        return ok
          64 +    def nearest(self,p):
          65 +        ds=np.sum((self.points-p)**2,axis=1);ds[~self.valid]=np.inf
          66 +        return int(np.argmin(ds))
          67 +    def pending_count(self,s,i):
          68 +        return sum(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs)+sum(s.get(o,'analyzed_rover'+str(i)) and not s.get(o,'received_analysis') for o in self.samples)
          69 +    def get_action(self,s):
          70 +        self.step+=1
          71 +        pos=[self.xy(s,r) for r in self.rovers]
          72 +        if self.prev is not None:
          73 +            for i in range(2):
          74 +                old,move,op,idx,had=self.prev[i]
          75 +                if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
          76 +                    q=old+move
          77 +                    ids=np.linalg.norm(self.points-q,axis=1)<.085
          78 +                    self.valid[ids]=False
          79 +                    self.make_graph()
          80 +                if op==.5 and self.pending_count(s,i)>=had:
          81 +                    self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
          82 +                if op in [-.5,-1/6] and idx is not None:
          83 +                    if (op==-.5 and not s.get(self.rovers[i],'calibrated')) or (op==-1/6 and not s.get(self.objs[idx],'have_image_rover'+str(i))):
          84 +                        self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
          85 +        action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
          86 +        received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
          87 +        acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
          88 +        for i,r in enumerate(self.rovers):
          89 +            p=pos[i]; start=self.nearest(p)
          90 +            dist,pred=dijkstra(self.graph,indices=start,return_predecessors=True)
          91 +            candidates=[]
          92 +            for k in [0,1]:
          93 +                if not acquired[k] and k not in kinds and not s.get(r,'store_full'):
          94 +                    for oi,o in enumerate(self.samples):
          95 +                        if int(s.get(o,'is_soil'))==k:
          96 +                            mask=self.sample_masks[oi]
          97 +                            candidates.append((mask,'sample',o,k))
          98 +            for j,o in enumerate(self.objs):
          99 +                if not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]) and j not in assigned:
         100 +                    mask=self.image_masks[j]&~self.bad[i,:,j]
         101 +                    candidates.append((mask,'image',o,j))
         102 +            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
         103 +            if pending: candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
         104 +            best=None; score=np.inf
         105 +            for mask,task,o,j in candidates:
         106 +                dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         107 +                target=int(np.argmin(dd)); cost=dd[target]
         108 +                if task=='sample': cost-=6
         109 +                if task=='send': cost+=5 if any(c[1]!='send' for c in candidates) else 0
         110 +                if cost<score: score=cost;best=(target,task,o,j)
         111 +            if best is None: best=(self.nearest(self.homes[i]),'home',None,None)
         112 +            target,task,o,j=best
         113 +            if task=='send' and self.visible(p,self.lander,4)[0] and not self.send_bad[i,start]:
         114 +                navbest=None;navcost=np.inf
         115 +                for mask,nt,no,nj in candidates:
         116 +                    if nt=='send':continue
         117 +                    dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         118 +                    ni=int(np.argmin(dd))
         119 +                    if dd[ni]<navcost:navcost=dd[ni];navbest=(ni,nt,no,nj)
         120 +                if navbest is not None:target,task,o,j=navbest
         121 +                else:target=self.nearest(self.homes[i]);task='home'
         122 +            if task=='sample': kinds.add(j)
         123 +            if task=='image': assigned.add(j)
         124 +            targetpos=self.points[target]
         125 +            if task=='home': targetpos=self.homes[i]
         126 +            path=[target];cur=target
         127 +            for _ in range(len(self.points)):
         128 +                if cur==start:break
         129 +                cur=int(pred[cur])
         130 +                if cur<0:break
         131 +                path.append(cur)
         132 +            path=path[::-1]
         133 +            goal=targetpos
         134 +            for node in path:
         135 +                q=self.points[node]
         136 +                if np.max(np.abs(q-p))<=.20001: goal=q
         137 +                else: break
         138 +            if np.max(np.abs(targetpos-p))<=.2:goal=targetpos
         139 +            move=np.clip(goal-p,-.2,.2)
         140 +            if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
         141 +            q=p+move; op=0.;idx=None
         142 +            nearest_sample=min(self.samples,key=lambda oo:np.linalg.norm(q-self.xy(s,oo)))
         143 +            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249 and s.get(nearest_sample,'is_soil')==j:op=-5/6
         144 +            else:
         145 +                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
         146 +                if useful:
         147 +                    idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
         148 +                    op=-1/6 if s.get(r,'calibrated') else -.5
         149 +            if op==0 and pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
         150 +            elif op==0 and s.get(r,'store_full'):op=5/6
         151 +            elif op==0 and not s.get(r,'calibrated') and any(not s.get(oo,'received_image') for oo in self.objs) and any(self.visible(q,self.xy(s,oo),2)[0] for oo in self.objs):op=-.5
         152 +            action[4*i:4*i+2]=move;action[4*i+3]=op
         153 +            records.append((p,move,op,idx,self.pending_count(s,i)))
         154 +        self.prev=records
         155 +        return action
diff --git a/test_priority.py b/test_priority.py
new file mode 100644
index 0000000..90337c8
--- /dev/null
+++ b/test_priority.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +from sample_priority import GeneratedApproach
           3 +import time,sys,json
           4 +start_seed=int(sys.argv[1]);end_seed=int(sys.argv[2]);count=int(sys.argv[3]) if len(sys.argv)>3 else None
           5 +for seed in range(start_seed,end_seed):
           6 + e=make_env();s,info=e.reset(seed=seed,options={'object_count':count} if count else None);p=GeneratedApproach(e.action_space,e.observation_space,{})
           7 + start=time.time();p.reset(s,info);hist=[]
           8 + for t in range(200):
           9 +  a=p.get_action(s);s,r,done,trunc,inf=e.step(a)
          10 +  hist.append({'t':t,'rover':[[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers], 'images':[[s.get(o,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for o in p.objs], 'samples':[[s.get(o,k) for k in ['received_analysis','analyzed_rover0','analyzed_rover1']] for o in p.samples], 'action':a.tolist()})
          11 +  if done or trunc:break
          12 + result={'seed':seed,'n':len(p.objs),'steps':t+1,'success':done,'sec':round(time.time()-start,3)}
          13 + if not done:
          14 +  with open('failure_%s_%s.json'%(seed,count),'w') as f:json.dump(hist,f)
          15 + print(json.dumps(result),flush=True);e.close()
```

</details>

<a id="C033"></a>
### C033 · Evaluate navigation edges matching full per-step motion bounds

Commit `c1d186ed0008fabdf31c2d0e5dc09f570c603253`; parents: fd291b629a9a63642dd93948bc5e8133ee3f62e9. Recorded author date: 2026-09-20T03:57:54+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0100](01_timeline.md#E0100): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C033_c1d186e.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/assignment_results.jsonl b/assignment_results.jsonl
index aff0cf0..e291894 100644
--- a/assignment_results.jsonl
+++ b/assignment_results.jsonl
@@ -25,3 +25,6 @@
   25     25  {"seed": 24, "base": {"steps": 25, "success": true, "seconds": 0.982}, "candidate": {"steps": 25, "success": true, "seconds": 0.629}}
   26     26  {"seed": 25, "base": {"steps": 23, "success": true, "seconds": 0.605}, "candidate": {"steps": 23, "success": true, "seconds": 0.904}}
   27     27  {"seed": 26, "base": {"steps": 26, "success": true, "seconds": 1.111}, "candidate": {"steps": 30, "success": true, "seconds": 1.081}}
          28 +{"seed": 27, "base": {"steps": 24, "success": true, "seconds": 0.888}, "candidate": {"steps": 24, "success": true, "seconds": 1.261}}
          29 +{"seed": 28, "base": {"steps": 25, "success": true, "seconds": 1.349}, "candidate": {"steps": 28, "success": true, "seconds": 1.943}}
          30 +{"seed": 29, "base": {"steps": 28, "success": true, "seconds": 1.729}, "candidate": {"steps": 31, "success": true, "seconds": 1.754}}
diff --git a/navigation_candidate.py b/navigation_candidate.py
new file mode 100644
index 0000000..9fc85c0
--- /dev/null
+++ b/navigation_candidate.py
@@ -0,0 +1,154 @@
           1 +import numpy as np
           2 +from scipy.sparse import csr_matrix
           3 +from scipy.sparse.csgraph import dijkstra
           4 +
           5 +class GeneratedApproach:
           6 +    def __init__(self, action_space, observation_space, primitives):
           7 +        self.space = observation_space
           8 +    def objects(self, s, t):
           9 +        return s.get_objects(self.space.get_type(t))
          10 +    def xy(self,s,o):
          11 +        return np.array([s.get(o,'x'),s.get(o,'y')])
          12 +    def reset(self,state,info):
          13 +        self.rovers=[state.get_object_from_name('rover'+str(i)) for i in range(2)]
          14 +        self.homes=[self.xy(state,r) for r in self.rovers]
          15 +        self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
          16 +        self.lander=self.xy(state,self.objects(state,'lander')[0])
          17 +        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,2.5]])
          18 +        self.axis=np.arange(-2.3,2.301,0.1)
          19 +        self.n=len(self.axis)
          20 +        self.points=np.array([(x,y) for x in self.axis for y in self.axis])
          21 +        self.valid=self.free(self.points)
          22 +        self.bad=np.zeros((2,len(self.points),len(self.objs)),dtype=bool)
          23 +        self.send_bad=np.zeros((2,len(self.points)),dtype=bool)
          24 +        self.prev=None; self.step=0
          25 +        self.make_graph()
          26 +        self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
          27 +        sample_dist=np.array([np.linalg.norm(self.points-self.xy(state,o),axis=1) for o in self.samples])
          28 +        self.sample_masks=[(dd<.245)&(dd<=sample_dist.min(axis=0)+1e-8) for dd in sample_dist]
          29 +        self.radio_mask=self.visible(self.points,self.lander,4)
          30 +        self.home_dist=[dijkstra(self.graph,indices=self.nearest(h)) for h in self.homes]
          31 +    def free(self,p):
          32 +        p=np.atleast_2d(p)
          33 +        d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
          34 +        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.228**2,axis=1)
          35 +        ld=np.maximum(np.abs(p-self.lander)-np.array([.45,.30]),0)
          36 +        ok &= np.sum(ld**2,axis=1)>.228**2
          37 +        ok &= np.max(np.abs(p),axis=1)<2.271
          38 +        return ok
          39 +    def make_graph(self):
          40 +        rows=[]; cols=[]
          41 +        for i in np.flatnonzero(self.valid):
          42 +            x,y=divmod(i,self.n)
          43 +            for dx,dy in [(dx,dy) for dx in range(-2,3) for dy in range(-2,3) if dx or dy]:
          44 +                xx,yy=x+dx,y+dy
          45 +                if 0<=xx<self.n and 0<=yy<self.n:
          46 +                    j=xx*self.n+yy
          47 +                    if self.valid[j]: rows.append(i);cols.append(j)
          48 +        self.graph=csr_matrix((np.full(len(rows),2.),(rows,cols)),shape=(len(self.points),len(self.points)))
          49 +    def visible(self,p,target,limit):
          50 +        p=np.atleast_2d(p); target=np.asarray(target)
          51 +        ok=np.linalg.norm(p-target,axis=1)<(3.91 if limit>3 else limit-.025)
          52 +        # Low mounds and the central driving wall do not obstruct the camera.
          53 +        boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
          54 +        delta=target-p
          55 +        for b in boxes:
          56 +            padding=.05 if limit>3 else 0.
          57 +            lo=b[:2]-b[2:]-padding;hi=b[:2]+b[2:]+padding
          58 +            with np.errstate(divide='ignore',invalid='ignore'):
          59 +                t1=(lo-p)/delta;t2=(hi-p)/delta
          60 +            near=np.maximum(np.min(np.stack([t1,t2]),axis=0).max(axis=1),.001)
          61 +            far=np.minimum(np.max(np.stack([t1,t2]),axis=0).min(axis=1),.999)
          62 +            ok &= near>far
          63 +        return ok
          64 +    def nearest(self,p):
          65 +        ds=np.sum((self.points-p)**2,axis=1);ds[~self.valid]=np.inf
          66 +        return int(np.argmin(ds))
          67 +    def pending_count(self,s,i):
          68 +        return sum(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs)+sum(s.get(o,'analyzed_rover'+str(i)) and not s.get(o,'received_analysis') for o in self.samples)
          69 +    def get_action(self,s):
          70 +        self.step+=1
          71 +        pos=[self.xy(s,r) for r in self.rovers]
          72 +        if self.prev is not None:
          73 +            for i in range(2):
          74 +                old,move,op,idx,had=self.prev[i]
          75 +                if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
          76 +                    q=old+move
          77 +                    ids=np.linalg.norm(self.points-q,axis=1)<.085
          78 +                    self.valid[ids]=False
          79 +                    self.make_graph()
          80 +                if op==.5 and self.pending_count(s,i)>=had:
          81 +                    self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
          82 +                if op in [-.5,-1/6] and idx is not None:
          83 +                    if (op==-.5 and not s.get(self.rovers[i],'calibrated')) or (op==-1/6 and not s.get(self.objs[idx],'have_image_rover'+str(i))):
          84 +                        self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
          85 +        action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
          86 +        received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
          87 +        acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
          88 +        for i,r in enumerate(self.rovers):
          89 +            p=pos[i]; start=self.nearest(p)
          90 +            dist,pred=dijkstra(self.graph,indices=start,return_predecessors=True)
          91 +            candidates=[]
          92 +            for k in [0,1]:
          93 +                if not acquired[k] and k not in kinds and not s.get(r,'store_full'):
          94 +                    for oi,o in enumerate(self.samples):
          95 +                        if int(s.get(o,'is_soil'))==k:
          96 +                            mask=self.sample_masks[oi]
          97 +                            candidates.append((mask,'sample',o,k))
          98 +            for j,o in enumerate(self.objs):
          99 +                if not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]) and j not in assigned:
         100 +                    mask=self.image_masks[j]&~self.bad[i,:,j]
         101 +                    candidates.append((mask,'image',o,j))
         102 +            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
         103 +            if pending: candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
         104 +            best=None; score=np.inf
         105 +            for mask,task,o,j in candidates:
         106 +                dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         107 +                target=int(np.argmin(dd)); cost=dd[target]
         108 +                if task=='send': cost+=5 if any(c[1]!='send' for c in candidates) else 0
         109 +                if cost<score: score=cost;best=(target,task,o,j)
         110 +            if best is None: best=(self.nearest(self.homes[i]),'home',None,None)
         111 +            target,task,o,j=best
         112 +            if task=='send' and self.visible(p,self.lander,4)[0] and not self.send_bad[i,start]:
         113 +                navbest=None;navcost=np.inf
         114 +                for mask,nt,no,nj in candidates:
         115 +                    if nt=='send':continue
         116 +                    dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         117 +                    ni=int(np.argmin(dd))
         118 +                    if dd[ni]<navcost:navcost=dd[ni];navbest=(ni,nt,no,nj)
         119 +                if navbest is not None:target,task,o,j=navbest
         120 +                else:target=self.nearest(self.homes[i]);task='home'
         121 +            if task=='sample': kinds.add(j)
         122 +            if task=='image': assigned.add(j)
         123 +            targetpos=self.points[target]
         124 +            if task=='home': targetpos=self.homes[i]
         125 +            path=[target];cur=target
         126 +            for _ in range(len(self.points)):
         127 +                if cur==start:break
         128 +                cur=int(pred[cur])
         129 +                if cur<0:break
         130 +                path.append(cur)
         131 +            path=path[::-1]
         132 +            goal=targetpos
         133 +            for node in path:
         134 +                q=self.points[node]
         135 +                if np.max(np.abs(q-p))<=.20001: goal=q
         136 +                else: break
         137 +            if np.max(np.abs(targetpos-p))<=.2:goal=targetpos
         138 +            move=np.clip(goal-p,-.2,.2)
         139 +            if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
         140 +            q=p+move; op=0.;idx=None
         141 +            nearest_sample=min(self.samples,key=lambda oo:np.linalg.norm(q-self.xy(s,oo)))
         142 +            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249 and s.get(nearest_sample,'is_soil')==j:op=-5/6
         143 +            else:
         144 +                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
         145 +                if useful:
         146 +                    idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
         147 +                    op=-1/6 if s.get(r,'calibrated') else -.5
         148 +            if op==0 and pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
         149 +            elif op==0 and s.get(r,'store_full'):op=5/6
         150 +            elif op==0 and not s.get(r,'calibrated') and any(not s.get(oo,'received_image') for oo in self.objs) and any(self.visible(q,self.xy(s,oo),2)[0] for oo in self.objs):op=-.5
         151 +            action[4*i:4*i+2]=move;action[4*i+3]=op
         152 +            records.append((p,move,op,idx,self.pending_count(s,i)))
         153 +        self.prev=records
         154 +        return action
diff --git a/sample_priority_results.jsonl b/sample_priority_results.jsonl
new file mode 100644
index 0000000..11a4423
--- /dev/null
+++ b/sample_priority_results.jsonl
@@ -0,0 +1,26 @@
           1 +{"seed": 0, "n": 3, "steps": 34, "success": true, "sec": 1.928}
           2 +{"seed": 1, "n": 2, "steps": 21, "success": true, "sec": 0.686}
           3 +{"seed": 2, "n": 3, "steps": 22, "success": true, "sec": 1.249}
           4 +{"seed": 3, "n": 3, "steps": 26, "success": true, "sec": 1.658}
           5 +{"seed": 4, "n": 3, "steps": 24, "success": true, "sec": 1.473}
           6 +{"seed": 5, "n": 3, "steps": 30, "success": true, "sec": 1.28}
           7 +{"seed": 6, "n": 2, "steps": 22, "success": true, "sec": 0.61}
           8 +{"seed": 7, "n": 3, "steps": 26, "success": true, "sec": 1.099}
           9 +{"seed": 8, "n": 3, "steps": 26, "success": true, "sec": 0.644}
          10 +{"seed": 9, "n": 2, "steps": 25, "success": true, "sec": 0.689}
          11 +{"seed": 10, "n": 3, "steps": 26, "success": true, "sec": 0.679}
          12 +{"seed": 11, "n": 1, "steps": 28, "success": true, "sec": 1.085}
          13 +{"seed": 12, "n": 2, "steps": 26, "success": true, "sec": 1.083}
          14 +{"seed": 13, "n": 3, "steps": 33, "success": true, "sec": 1.714}
          15 +{"seed": 14, "n": 1, "steps": 37, "success": true, "sec": 1.244}
          16 +{"seed": 15, "n": 3, "steps": 47, "success": true, "sec": 1.605}
          17 +{"seed": 16, "n": 2, "steps": 26, "success": true, "sec": 1.179}
          18 +{"seed": 17, "n": 3, "steps": 31, "success": true, "sec": 1.144}
          19 +{"seed": 18, "n": 3, "steps": 24, "success": true, "sec": 1.122}
          20 +{"seed": 19, "n": 2, "steps": 31, "success": true, "sec": 1.262}
          21 +{"seed": 20, "n": 3, "steps": 34, "success": true, "sec": 1.355}
          22 +{"seed": 21, "n": 1, "steps": 25, "success": true, "sec": 0.616}
          23 +{"seed": 22, "n": 3, "steps": 25, "success": true, "sec": 0.687}
          24 +{"seed": 23, "n": 1, "steps": 18, "success": true, "sec": 0.872}
          25 +{"seed": 24, "n": 2, "steps": 25, "success": true, "sec": 0.999}
          26 +{"seed": 25, "n": 2, "steps": 22, "success": true, "sec": 0.504}
diff --git a/stress_500.jsonl b/stress_500.jsonl
index e963dfe..43f346b 100644
--- a/stress_500.jsonl
+++ b/stress_500.jsonl
@@ -19,3 +19,26 @@
   19     19  {"seed": 518, "n": 4, "steps": 32, "success": true, "sec": 1.024}
   20     20  {"seed": 519, "n": 4, "steps": 28, "success": true, "sec": 0.996}
   21     21  {"seed": 520, "n": 4, "steps": 29, "success": true, "sec": 1.133}
          22 +{"seed": 521, "n": 4, "steps": 30, "success": true, "sec": 1.558}
          23 +{"seed": 522, "n": 4, "steps": 34, "success": true, "sec": 2.955}
          24 +{"seed": 523, "n": 4, "steps": 26, "success": true, "sec": 1.544}
          25 +{"seed": 524, "n": 4, "steps": 29, "success": true, "sec": 1.55}
          26 +{"seed": 525, "n": 4, "steps": 33, "success": true, "sec": 1.157}
          27 +{"seed": 526, "n": 4, "steps": 46, "success": true, "sec": 2.016}
          28 +{"seed": 527, "n": 4, "steps": 30, "success": true, "sec": 1.04}
          29 +{"seed": 528, "n": 4, "steps": 26, "success": true, "sec": 1.112}
          30 +{"seed": 529, "n": 4, "steps": 27, "success": true, "sec": 1.06}
          31 +{"seed": 530, "n": 4, "steps": 31, "success": true, "sec": 1.29}
          32 +{"seed": 531, "n": 4, "steps": 27, "success": true, "sec": 0.838}
          33 +{"seed": 532, "n": 4, "steps": 26, "success": true, "sec": 0.708}
          34 +{"seed": 533, "n": 4, "steps": 29, "success": true, "sec": 1.039}
          35 +{"seed": 534, "n": 4, "steps": 28, "success": true, "sec": 1.096}
          36 +{"seed": 535, "n": 4, "steps": 31, "success": true, "sec": 1.287}
          37 +{"seed": 536, "n": 4, "steps": 28, "success": true, "sec": 1.095}
          38 +{"seed": 537, "n": 4, "steps": 28, "success": true, "sec": 1.087}
          39 +{"seed": 538, "n": 4, "steps": 29, "success": true, "sec": 1.213}
          40 +{"seed": 539, "n": 4, "steps": 32, "success": true, "sec": 1.137}
          41 +{"seed": 540, "n": 4, "steps": 27, "success": true, "sec": 1.166}
          42 +{"seed": 541, "n": 4, "steps": 33, "success": true, "sec": 1.421}
          43 +{"seed": 542, "n": 4, "steps": 32, "success": true, "sec": 1.335}
          44 +{"seed": 543, "n": 4, "steps": 27, "success": true, "sec": 1.149}
diff --git a/test_navigation.py b/test_navigation.py
new file mode 100644
index 0000000..11401d3
--- /dev/null
+++ b/test_navigation.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +from navigation_candidate import GeneratedApproach
           3 +import time,sys,json
           4 +start_seed=int(sys.argv[1]);end_seed=int(sys.argv[2]);count=int(sys.argv[3]) if len(sys.argv)>3 else None
           5 +for seed in range(start_seed,end_seed):
           6 + e=make_env();s,info=e.reset(seed=seed,options={'object_count':count} if count else None);p=GeneratedApproach(e.action_space,e.observation_space,{})
           7 + start=time.time();p.reset(s,info);hist=[]
           8 + for t in range(200):
           9 +  a=p.get_action(s);s,r,done,trunc,inf=e.step(a)
          10 +  hist.append({'t':t,'rover':[[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers], 'images':[[s.get(o,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for o in p.objs], 'samples':[[s.get(o,k) for k in ['received_analysis','analyzed_rover0','analyzed_rover1']] for o in p.samples], 'action':a.tolist()})
          11 +  if done or trunc:break
          12 + result={'seed':seed,'n':len(p.objs),'steps':t+1,'success':done,'sec':round(time.time()-start,3)}
          13 + if not done:
          14 +  with open('failure_%s_%s.json'%(seed,count),'w') as f:json.dump(hist,f)
          15 + print(json.dumps(result),flush=True);e.close()
```

</details>

<a id="C034"></a>
### C034 · Preserve comparison data and add sample scheduling trace

Commit `34dc5d60085bcc5a3e4e7479c46636c7e692014f`; parents: c1d186ed0008fabdf31c2d0e5dc09f570c603253. Recorded author date: 2026-09-20T03:59:10+02:00.

File roles (automatic): diagnostic/test, setup/other.

- [E0107](01_timeline.md#E0107): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C034_34dc5d6.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/debug_priority.py b/debug_priority.py
new file mode 100644
index 0000000..303baae
--- /dev/null
+++ b/debug_priority.py
@@ -0,0 +1,9 @@
           1 +from env_client import make_env
           2 +from sample_priority import GeneratedApproach
           3 +import sys
           4 +E=make_env();s,info=E.reset(seed=int(sys.argv[1]) if len(sys.argv)>1 else 0);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info)
           5 +for t in range(120):
           6 + a=p.get_action(s);s,r,done,trunc,inf=E.step(a)
           7 + if t%5==0 or done:print(t,[[round(s.get(ro,k),3) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers],[[s.get(o,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for o in p.objs],a.round(2),flush=True)
           8 + if done:break
           9 +E.close()
diff --git a/navigation_results.jsonl b/navigation_results.jsonl
new file mode 100644
index 0000000..c79a415
--- /dev/null
+++ b/navigation_results.jsonl
@@ -0,0 +1,30 @@
           1 +{"seed": 0, "n": 3, "steps": 34, "success": true, "sec": 2.362}
           2 +{"seed": 1, "n": 2, "steps": 21, "success": true, "sec": 1.373}
           3 +{"seed": 2, "n": 3, "steps": 22, "success": true, "sec": 1.325}
           4 +{"seed": 3, "n": 3, "steps": 23, "success": true, "sec": 0.455}
           5 +{"seed": 4, "n": 3, "steps": 25, "success": true, "sec": 1.106}
           6 +{"seed": 5, "n": 3, "steps": 29, "success": true, "sec": 0.947}
           7 +{"seed": 6, "n": 2, "steps": 22, "success": true, "sec": 0.541}
           8 +{"seed": 7, "n": 3, "steps": 26, "success": true, "sec": 1.201}
           9 +{"seed": 8, "n": 3, "steps": 28, "success": true, "sec": 1.209}
          10 +{"seed": 9, "n": 2, "steps": 24, "success": true, "sec": 1.028}
          11 +{"seed": 10, "n": 3, "steps": 28, "success": true, "sec": 1.157}
          12 +{"seed": 11, "n": 1, "steps": 29, "success": true, "sec": 1.246}
          13 +{"seed": 12, "n": 2, "steps": 25, "success": true, "sec": 0.67}
          14 +{"seed": 13, "n": 3, "steps": 32, "success": true, "sec": 1.293}
          15 +{"seed": 14, "n": 1, "steps": 37, "success": true, "sec": 1.28}
          16 +{"seed": 15, "n": 3, "steps": 43, "success": true, "sec": 1.554}
          17 +{"seed": 16, "n": 2, "steps": 26, "success": true, "sec": 1.169}
          18 +{"seed": 17, "n": 3, "steps": 30, "success": true, "sec": 1.385}
          19 +{"seed": 18, "n": 3, "steps": 24, "success": true, "sec": 1.149}
          20 +{"seed": 19, "n": 2, "steps": 30, "success": true, "sec": 1.651}
          21 +{"seed": 20, "n": 3, "steps": 34, "success": true, "sec": 1.038}
          22 +{"seed": 21, "n": 1, "steps": 33, "success": true, "sec": 1.18}
          23 +{"seed": 22, "n": 3, "steps": 24, "success": true, "sec": 1.085}
          24 +{"seed": 23, "n": 1, "steps": 18, "success": true, "sec": 0.419}
          25 +{"seed": 24, "n": 2, "steps": 25, "success": true, "sec": 1.167}
          26 +{"seed": 25, "n": 2, "steps": 22, "success": true, "sec": 1.03}
          27 +{"seed": 26, "n": 3, "steps": 24, "success": true, "sec": 1.003}
          28 +{"seed": 27, "n": 1, "steps": 23, "success": true, "sec": 0.391}
          29 +{"seed": 28, "n": 2, "steps": 27, "success": true, "sec": 1.027}
          30 +{"seed": 29, "n": 3, "steps": 25, "success": true, "sec": 1.164}
diff --git a/sample_priority_results.jsonl b/sample_priority_results.jsonl
index 11a4423..42a2f1f 100644
--- a/sample_priority_results.jsonl
+++ b/sample_priority_results.jsonl
@@ -24,3 +24,7 @@
   24     24  {"seed": 23, "n": 1, "steps": 18, "success": true, "sec": 0.872}
   25     25  {"seed": 24, "n": 2, "steps": 25, "success": true, "sec": 0.999}
   26     26  {"seed": 25, "n": 2, "steps": 22, "success": true, "sec": 0.504}
          27 +{"seed": 26, "n": 3, "steps": 25, "success": true, "sec": 0.794}
          28 +{"seed": 27, "n": 1, "steps": 24, "success": true, "sec": 1.301}
          29 +{"seed": 28, "n": 2, "steps": 26, "success": true, "sec": 1.687}
          30 +{"seed": 29, "n": 3, "steps": 25, "success": true, "sec": 1.068}
diff --git a/stress_500.jsonl b/stress_500.jsonl
index 43f346b..63a14b9 100644
--- a/stress_500.jsonl
+++ b/stress_500.jsonl
@@ -42,3 +42,58 @@
   42     42  {"seed": 541, "n": 4, "steps": 33, "success": true, "sec": 1.421}
   43     43  {"seed": 542, "n": 4, "steps": 32, "success": true, "sec": 1.335}
   44     44  {"seed": 543, "n": 4, "steps": 27, "success": true, "sec": 1.149}
          45 +{"seed": 544, "n": 4, "steps": 32, "success": true, "sec": 1.516}
          46 +{"seed": 545, "n": 4, "steps": 26, "success": true, "sec": 1.893}
          47 +{"seed": 546, "n": 4, "steps": 28, "success": true, "sec": 1.547}
          48 +{"seed": 547, "n": 4, "steps": 38, "success": true, "sec": 1.4}
          49 +{"seed": 548, "n": 4, "steps": 29, "success": true, "sec": 0.918}
          50 +{"seed": 549, "n": 4, "steps": 45, "success": true, "sec": 1.903}
          51 +{"seed": 550, "n": 4, "steps": 29, "success": true, "sec": 1.028}
          52 +{"seed": 551, "n": 4, "steps": 30, "success": true, "sec": 1.263}
          53 +{"seed": 552, "n": 4, "steps": 28, "success": true, "sec": 0.967}
          54 +{"seed": 553, "n": 4, "steps": 26, "success": true, "sec": 1.275}
          55 +{"seed": 554, "n": 4, "steps": 33, "success": true, "sec": 1.33}
          56 +{"seed": 555, "n": 4, "steps": 30, "success": true, "sec": 0.831}
          57 +{"seed": 556, "n": 4, "steps": 27, "success": true, "sec": 1.101}
          58 +{"seed": 557, "n": 4, "steps": 33, "success": true, "sec": 1.129}
          59 +{"seed": 558, "n": 4, "steps": 27, "success": true, "sec": 1.087}
          60 +{"seed": 559, "n": 4, "steps": 29, "success": true, "sec": 0.999}
          61 +{"seed": 560, "n": 4, "steps": 32, "success": true, "sec": 1.055}
          62 +{"seed": 561, "n": 4, "steps": 30, "success": true, "sec": 1.58}
          63 +{"seed": 562, "n": 4, "steps": 31, "success": true, "sec": 1.277}
          64 +{"seed": 563, "n": 4, "steps": 27, "success": true, "sec": 1.077}
          65 +{"seed": 564, "n": 4, "steps": 27, "success": true, "sec": 0.944}
          66 +{"seed": 565, "n": 4, "steps": 31, "success": true, "sec": 1.75}
          67 +{"seed": 566, "n": 4, "steps": 30, "success": true, "sec": 1.139}
          68 +{"seed": 567, "n": 4, "steps": 28, "success": true, "sec": 0.957}
          69 +{"seed": 568, "n": 4, "steps": 30, "success": true, "sec": 1.67}
          70 +{"seed": 569, "n": 4, "steps": 27, "success": true, "sec": 0.998}
          71 +{"seed": 570, "n": 4, "steps": 29, "success": true, "sec": 0.869}
          72 +{"seed": 571, "n": 4, "steps": 33, "success": true, "sec": 0.506}
          73 +{"seed": 572, "n": 4, "steps": 27, "success": true, "sec": 0.473}
          74 +{"seed": 573, "n": 4, "steps": 38, "success": true, "sec": 0.6}
          75 +{"seed": 574, "n": 4, "steps": 24, "success": true, "sec": 0.41}
          76 +{"seed": 575, "n": 4, "steps": 29, "success": true, "sec": 0.476}
          77 +{"seed": 576, "n": 4, "steps": 33, "success": true, "sec": 0.564}
          78 +{"seed": 577, "n": 4, "steps": 29, "success": true, "sec": 0.521}
          79 +{"seed": 578, "n": 4, "steps": 26, "success": true, "sec": 0.429}
          80 +{"seed": 579, "n": 4, "steps": 33, "success": true, "sec": 0.539}
          81 +{"seed": 580, "n": 4, "steps": 27, "success": true, "sec": 0.445}
          82 +{"seed": 581, "n": 4, "steps": 30, "success": true, "sec": 0.475}
          83 +{"seed": 582, "n": 4, "steps": 28, "success": true, "sec": 0.483}
          84 +{"seed": 583, "n": 4, "steps": 31, "success": true, "sec": 0.514}
          85 +{"seed": 584, "n": 4, "steps": 36, "success": true, "sec": 0.644}
          86 +{"seed": 585, "n": 4, "steps": 25, "success": true, "sec": 0.421}
          87 +{"seed": 586, "n": 4, "steps": 35, "success": true, "sec": 0.63}
          88 +{"seed": 587, "n": 4, "steps": 29, "success": true, "sec": 0.589}
          89 +{"seed": 588, "n": 4, "steps": 26, "success": true, "sec": 0.422}
          90 +{"seed": 589, "n": 4, "steps": 34, "success": true, "sec": 0.59}
          91 +{"seed": 590, "n": 4, "steps": 27, "success": true, "sec": 0.48}
          92 +{"seed": 591, "n": 4, "steps": 26, "success": true, "sec": 0.428}
          93 +{"seed": 592, "n": 4, "steps": 27, "success": true, "sec": 0.462}
          94 +{"seed": 593, "n": 4, "steps": 25, "success": true, "sec": 0.422}
          95 +{"seed": 594, "n": 4, "steps": 36, "success": true, "sec": 0.57}
          96 +{"seed": 595, "n": 4, "steps": 34, "success": true, "sec": 0.584}
          97 +{"seed": 596, "n": 4, "steps": 25, "success": true, "sec": 0.413}
          98 +{"seed": 597, "n": 4, "steps": 25, "success": true, "sec": 0.43}
          99 +{"seed": 598, "n": 4, "steps": 30, "success": true, "sec": 0.367}
```

</details>

<a id="C035"></a>
### C035 · Use full-motion navigation and favor collecting samples along outbound routes

Commit `5e426722e51e711e45a92d76cef3bf520c3e4cbd`; parents: 34dc5d60085bcc5a3e4e7479c46636c7e692014f. Recorded author date: 2026-09-20T04:00:04+02:00.

File roles (automatic): policy, setup/other.

- [E0113](01_timeline.md#E0113): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C035_5e42672_approach.py) · [Exact all-file diff](evidence/diffs/C035_5e42672.diff)

[Previous saved controller snapshot](evidence/versions/C031_6b263fc_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a8afb6b..0078060 100644
--- a/approach.py
+++ b/approach.py
@@ -40,12 +40,12 @@ class GeneratedApproach:
   40     40          rows=[]; cols=[]
   41     41          for i in np.flatnonzero(self.valid):
   42     42              x,y=divmod(i,self.n)
   43        -            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
          43 +            for dx,dy in [(dx,dy) for dx in range(-2,3) for dy in range(-2,3) if dx or dy]:
   44     44                  xx,yy=x+dx,y+dy
   45     45                  if 0<=xx<self.n and 0<=yy<self.n:
   46     46                      j=xx*self.n+yy
   47     47                      if self.valid[j]: rows.append(i);cols.append(j)
   48        -        self.graph=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(self.points),len(self.points)))
          48 +        self.graph=csr_matrix((np.full(len(rows),2.),(rows,cols)),shape=(len(self.points),len(self.points)))
   49     49      def visible(self,p,target,limit):
   50     50          p=np.atleast_2d(p); target=np.asarray(target)
   51     51          ok=np.linalg.norm(p-target,axis=1)<(3.91 if limit>3 else limit-.025)
@@ -105,6 +105,7 @@ class GeneratedApproach:
  105    105              for mask,task,o,j in candidates:
  106    106                  dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
  107    107                  target=int(np.argmin(dd)); cost=dd[target]
         108 +                if task=='sample': cost-=6
  108    109                  if task=='send': cost+=5 if any(c[1]!='send' for c in candidates) else 0
  109    110                  if cost<score: score=cost;best=(target,task,o,j)
  110    111              if best is None: best=(self.nearest(self.homes[i]),'home',None,None)
diff --git a/stress_500.jsonl b/stress_500.jsonl
index 63a14b9..58f50d5 100644
--- a/stress_500.jsonl
+++ b/stress_500.jsonl
@@ -97,3 +97,4 @@
   97     97  {"seed": 596, "n": 4, "steps": 25, "success": true, "sec": 0.413}
   98     98  {"seed": 597, "n": 4, "steps": 25, "success": true, "sec": 0.43}
   99     99  {"seed": 598, "n": 4, "steps": 30, "success": true, "sec": 0.367}
         100 +{"seed": 599, "n": 4, "steps": 30, "success": true, "sec": 0.73}
```

</details>

<a id="C036"></a>
### C036 · Compare balanced task ownership from small abstract route optimization

Commit `c7180a498e0c4a5dbe22b4d3f4d2c22f36ba6e59`; parents: 5e426722e51e711e45a92d76cef3bf520c3e4cbd. Recorded author date: 2026-09-20T04:01:04+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0122](01_timeline.md#E0122): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C036_c7180a4.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/combined_results.jsonl b/combined_results.jsonl
new file mode 100644
index 0000000..1a5abfb
--- /dev/null
+++ b/combined_results.jsonl
@@ -0,0 +1,30 @@
           1 +{"seed": 0, "n": 3, "steps": 34, "success": true, "sec": 0.364}
           2 +{"seed": 1, "n": 2, "steps": 21, "success": true, "sec": 0.342}
           3 +{"seed": 2, "n": 3, "steps": 22, "success": true, "sec": 0.37}
           4 +{"seed": 3, "n": 3, "steps": 23, "success": true, "sec": 0.403}
           5 +{"seed": 4, "n": 3, "steps": 25, "success": true, "sec": 0.419}
           6 +{"seed": 5, "n": 3, "steps": 29, "success": true, "sec": 0.541}
           7 +{"seed": 6, "n": 2, "steps": 22, "success": true, "sec": 0.342}
           8 +{"seed": 7, "n": 3, "steps": 26, "success": true, "sec": 0.447}
           9 +{"seed": 8, "n": 3, "steps": 28, "success": true, "sec": 0.388}
          10 +{"seed": 9, "n": 2, "steps": 24, "success": true, "sec": 0.394}
          11 +{"seed": 10, "n": 3, "steps": 28, "success": true, "sec": 0.478}
          12 +{"seed": 11, "n": 1, "steps": 29, "success": true, "sec": 0.398}
          13 +{"seed": 12, "n": 2, "steps": 25, "success": true, "sec": 0.414}
          14 +{"seed": 13, "n": 3, "steps": 32, "success": true, "sec": 0.579}
          15 +{"seed": 14, "n": 1, "steps": 35, "success": true, "sec": 0.522}
          16 +{"seed": 15, "n": 3, "steps": 41, "success": true, "sec": 0.875}
          17 +{"seed": 16, "n": 2, "steps": 26, "success": true, "sec": 0.457}
          18 +{"seed": 17, "n": 3, "steps": 30, "success": true, "sec": 0.538}
          19 +{"seed": 18, "n": 3, "steps": 24, "success": true, "sec": 0.416}
          20 +{"seed": 19, "n": 2, "steps": 30, "success": true, "sec": 0.46}
          21 +{"seed": 20, "n": 3, "steps": 32, "success": true, "sec": 0.509}
          22 +{"seed": 21, "n": 1, "steps": 24, "success": true, "sec": 0.349}
          23 +{"seed": 22, "n": 3, "steps": 24, "success": true, "sec": 0.373}
          24 +{"seed": 23, "n": 1, "steps": 18, "success": true, "sec": 0.273}
          25 +{"seed": 24, "n": 2, "steps": 25, "success": true, "sec": 0.413}
          26 +{"seed": 25, "n": 2, "steps": 22, "success": true, "sec": 0.224}
          27 +{"seed": 26, "n": 3, "steps": 24, "success": true, "sec": 0.387}
          28 +{"seed": 27, "n": 1, "steps": 23, "success": true, "sec": 0.361}
          29 +{"seed": 28, "n": 2, "steps": 27, "success": true, "sec": 0.423}
          30 +{"seed": 29, "n": 3, "steps": 25, "success": true, "sec": 0.423}
diff --git a/test_tour.py b/test_tour.py
new file mode 100644
index 0000000..6bed0f1
--- /dev/null
+++ b/test_tour.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +from tour_candidate import GeneratedApproach
           3 +import time,sys,json
           4 +start_seed=int(sys.argv[1]);end_seed=int(sys.argv[2]);count=int(sys.argv[3]) if len(sys.argv)>3 else None
           5 +for seed in range(start_seed,end_seed):
           6 + e=make_env();s,info=e.reset(seed=seed,options={'object_count':count} if count else None);p=GeneratedApproach(e.action_space,e.observation_space,{})
           7 + start=time.time();p.reset(s,info);hist=[]
           8 + for t in range(200):
           9 +  a=p.get_action(s);s,r,done,trunc,inf=e.step(a)
          10 +  hist.append({'t':t,'rover':[[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers], 'images':[[s.get(o,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for o in p.objs], 'samples':[[s.get(o,k) for k in ['received_analysis','analyzed_rover0','analyzed_rover1']] for o in p.samples], 'action':a.tolist()})
          11 +  if done or trunc:break
          12 + result={'seed':seed,'n':len(p.objs),'steps':t+1,'success':done,'sec':round(time.time()-start,3)}
          13 + if not done:
          14 +  with open('failure_%s_%s.json'%(seed,count),'w') as f:json.dump(hist,f)
          15 + print(json.dumps(result),flush=True);e.close()
diff --git a/tour_candidate.py b/tour_candidate.py
new file mode 100644
index 0000000..3f2bf90
--- /dev/null
+++ b/tour_candidate.py
@@ -0,0 +1,197 @@
           1 +import numpy as np
           2 +from scipy.sparse import csr_matrix
           3 +from scipy.sparse.csgraph import dijkstra
           4 +
           5 +class GeneratedApproach:
           6 +    def __init__(self, action_space, observation_space, primitives):
           7 +        self.space = observation_space
           8 +    def objects(self, s, t):
           9 +        return s.get_objects(self.space.get_type(t))
          10 +    def xy(self,s,o):
          11 +        return np.array([s.get(o,'x'),s.get(o,'y')])
          12 +    def reset(self,state,info):
          13 +        self.rovers=[state.get_object_from_name('rover'+str(i)) for i in range(2)]
          14 +        self.homes=[self.xy(state,r) for r in self.rovers]
          15 +        self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
          16 +        self.lander=self.xy(state,self.objects(state,'lander')[0])
          17 +        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,2.5]])
          18 +        self.axis=np.arange(-2.3,2.301,0.1)
          19 +        self.n=len(self.axis)
          20 +        self.points=np.array([(x,y) for x in self.axis for y in self.axis])
          21 +        self.valid=self.free(self.points)
          22 +        self.bad=np.zeros((2,len(self.points),len(self.objs)),dtype=bool)
          23 +        self.send_bad=np.zeros((2,len(self.points)),dtype=bool)
          24 +        self.prev=None; self.step=0
          25 +        self.make_graph()
          26 +        self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
          27 +        sample_dist=np.array([np.linalg.norm(self.points-self.xy(state,o),axis=1) for o in self.samples])
          28 +        self.sample_masks=[(dd<.245)&(dd<=sample_dist.min(axis=0)+1e-8) for dd in sample_dist]
          29 +        self.radio_mask=self.visible(self.points,self.lander,4)
          30 +        self.home_dist=[dijkstra(self.graph,indices=self.nearest(h)) for h in self.homes]
          31 +        self.allocate(state)
          32 +    def allocate(self,s):
          33 +        num=len(self.objs); size=1<<(num+2); allbits=size-1
          34 +        masks=self.sample_masks+self.image_masks
          35 +        costs=[]
          36 +        for r in range(2):
          37 +            hd=self.home_dist[r]; nodes={self.nearest(self.homes[r])}
          38 +            for mask in self.sample_masks:
          39 +                dd=np.where(mask,hd,np.inf);idx=int(dd.argmin())
          40 +                if np.isfinite(dd[idx]):nodes.add(idx)
          41 +            for subset in range(1,1<<num):
          42 +                mask=self.valid.copy()
          43 +                for j in range(num):
          44 +                    if subset>>j&1:mask &= self.image_masks[j]
          45 +                dd=np.where(mask,hd,np.inf);idx=int(dd.argmin())
          46 +                if np.isfinite(dd[idx]):nodes.add(idx)
          47 +            nodes=list(nodes); D=dijkstra(self.graph,indices=nodes)[:,nodes]
          48 +            cover=[]
          49 +            for node in nodes:
          50 +                bits=0
          51 +                for j,m in enumerate(self.sample_masks):
          52 +                    if m[node]:bits|=1<<int(s.get(self.samples[j],'is_soil'))
          53 +                for j,m in enumerate(self.image_masks):
          54 +                    if m[node]:bits|=1<<(j+2)
          55 +                cover.append(bits)
          56 +            dp=np.full((size,len(nodes)),np.inf)
          57 +            home=nodes.index(self.nearest(self.homes[r]));dp[0,home]=0
          58 +            for mask in range(size):
          59 +                if not np.isfinite(dp[mask]).any():continue
          60 +                arrivals=np.min(dp[mask,:,None]+D,axis=0)
          61 +                for j,bits in enumerate(cover):
          62 +                    gain=bits&~mask
          63 +                    if not gain:continue
          64 +                    extra=2*((gain&3).bit_count())+4*((gain>>2).bit_count())
          65 +                    new=mask|bits;dp[new,j]=min(dp[new,j],arrivals[j]+extra)
          66 +            val=np.min(dp+D[:,home],axis=1)
          67 +            for mask in range(size-1,-1,-1):
          68 +                for j in range(num+2):
          69 +                    if not mask>>j&1:val[mask]=min(val[mask],val[mask|(1<<j)])
          70 +            costs.append(val)
          71 +        best=min(range(size),key=lambda m:max(costs[0][m],costs[1][allbits^m])+.05*(costs[0][m]+costs[1][allbits^m]))
          72 +        self.owner=[0 if best>>j&1 else 1 for j in range(num+2)]
          73 +    def free(self,p):
          74 +        p=np.atleast_2d(p)
          75 +        d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
          76 +        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.228**2,axis=1)
          77 +        ld=np.maximum(np.abs(p-self.lander)-np.array([.45,.30]),0)
          78 +        ok &= np.sum(ld**2,axis=1)>.228**2
          79 +        ok &= np.max(np.abs(p),axis=1)<2.271
          80 +        return ok
          81 +    def make_graph(self):
          82 +        rows=[]; cols=[]
          83 +        for i in np.flatnonzero(self.valid):
          84 +            x,y=divmod(i,self.n)
          85 +            for dx,dy in [(dx,dy) for dx in range(-2,3) for dy in range(-2,3) if dx or dy]:
          86 +                xx,yy=x+dx,y+dy
          87 +                if 0<=xx<self.n and 0<=yy<self.n:
          88 +                    j=xx*self.n+yy
          89 +                    if self.valid[j]: rows.append(i);cols.append(j)
          90 +        self.graph=csr_matrix((np.full(len(rows),2.),(rows,cols)),shape=(len(self.points),len(self.points)))
          91 +    def visible(self,p,target,limit):
          92 +        p=np.atleast_2d(p); target=np.asarray(target)
          93 +        ok=np.linalg.norm(p-target,axis=1)<(3.91 if limit>3 else limit-.025)
          94 +        # Low mounds and the central driving wall do not obstruct the camera.
          95 +        boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
          96 +        delta=target-p
          97 +        for b in boxes:
          98 +            padding=.05 if limit>3 else 0.
          99 +            lo=b[:2]-b[2:]-padding;hi=b[:2]+b[2:]+padding
         100 +            with np.errstate(divide='ignore',invalid='ignore'):
         101 +                t1=(lo-p)/delta;t2=(hi-p)/delta
         102 +            near=np.maximum(np.min(np.stack([t1,t2]),axis=0).max(axis=1),.001)
         103 +            far=np.minimum(np.max(np.stack([t1,t2]),axis=0).min(axis=1),.999)
         104 +            ok &= near>far
         105 +        return ok
         106 +    def nearest(self,p):
         107 +        ds=np.sum((self.points-p)**2,axis=1);ds[~self.valid]=np.inf
         108 +        return int(np.argmin(ds))
         109 +    def pending_count(self,s,i):
         110 +        return sum(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs)+sum(s.get(o,'analyzed_rover'+str(i)) and not s.get(o,'received_analysis') for o in self.samples)
         111 +    def get_action(self,s):
         112 +        self.step+=1
         113 +        pos=[self.xy(s,r) for r in self.rovers]
         114 +        if self.prev is not None:
         115 +            for i in range(2):
         116 +                old,move,op,idx,had=self.prev[i]
         117 +                if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
         118 +                    q=old+move
         119 +                    ids=np.linalg.norm(self.points-q,axis=1)<.085
         120 +                    self.valid[ids]=False
         121 +                    self.make_graph()
         122 +                if op==.5 and self.pending_count(s,i)>=had:
         123 +                    self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
         124 +                if op in [-.5,-1/6] and idx is not None:
         125 +                    if (op==-.5 and not s.get(self.rovers[i],'calibrated')) or (op==-1/6 and not s.get(self.objs[idx],'have_image_rover'+str(i))):
         126 +                        self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
         127 +        action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
         128 +        received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
         129 +        acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
         130 +        for i,r in enumerate(self.rovers):
         131 +            p=pos[i]; start=self.nearest(p)
         132 +            dist,pred=dijkstra(self.graph,indices=start,return_predecessors=True)
         133 +            candidates=[]
         134 +            for k in [0,1]:
         135 +                if self.owner[k]==i and not acquired[k] and k not in kinds and not s.get(r,'store_full'):
         136 +                    for oi,o in enumerate(self.samples):
         137 +                        if int(s.get(o,'is_soil'))==k:
         138 +                            mask=self.sample_masks[oi]
         139 +                            candidates.append((mask,'sample',o,k))
         140 +            for j,o in enumerate(self.objs):
         141 +                if self.owner[j+2]==i and not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]) and j not in assigned:
         142 +                    mask=self.image_masks[j]&~self.bad[i,:,j]
         143 +                    candidates.append((mask,'image',o,j))
         144 +            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
         145 +            if pending: candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
         146 +            best=None; score=np.inf
         147 +            for mask,task,o,j in candidates:
         148 +                dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         149 +                target=int(np.argmin(dd)); cost=dd[target]
         150 +                if task=='sample': cost-=6
         151 +                if task=='send': cost+=5 if any(c[1]!='send' for c in candidates) else 0
         152 +                if cost<score: score=cost;best=(target,task,o,j)
         153 +            if best is None: best=(self.nearest(self.homes[i]),'home',None,None)
         154 +            target,task,o,j=best
         155 +            if task=='send' and self.visible(p,self.lander,4)[0] and not self.send_bad[i,start]:
         156 +                navbest=None;navcost=np.inf
         157 +                for mask,nt,no,nj in candidates:
         158 +                    if nt=='send':continue
         159 +                    dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         160 +                    ni=int(np.argmin(dd))
         161 +                    if dd[ni]<navcost:navcost=dd[ni];navbest=(ni,nt,no,nj)
         162 +                if navbest is not None:target,task,o,j=navbest
         163 +                else:target=self.nearest(self.homes[i]);task='home'
         164 +            if task=='sample': kinds.add(j)
         165 +            if task=='image': assigned.add(j)
         166 +            targetpos=self.points[target]
         167 +            if task=='home': targetpos=self.homes[i]
         168 +            path=[target];cur=target
         169 +            for _ in range(len(self.points)):
         170 +                if cur==start:break
         171 +                cur=int(pred[cur])
         172 +                if cur<0:break
         173 +                path.append(cur)
         174 +            path=path[::-1]
         175 +            goal=targetpos
         176 +            for node in path:
         177 +                q=self.points[node]
         178 +                if np.max(np.abs(q-p))<=.20001: goal=q
         179 +                else: break
         180 +            if np.max(np.abs(targetpos-p))<=.2:goal=targetpos
         181 +            move=np.clip(goal-p,-.2,.2)
         182 +            if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
         183 +            q=p+move; op=0.;idx=None
         184 +            nearest_sample=min(self.samples,key=lambda oo:np.linalg.norm(q-self.xy(s,oo)))
         185 +            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249 and s.get(nearest_sample,'is_soil')==j:op=-5/6
         186 +            else:
         187 +                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
         188 +                if useful:
         189 +                    idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
         190 +                    op=-1/6 if s.get(r,'calibrated') else -.5
         191 +            if op==0 and pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
         192 +            elif op==0 and s.get(r,'store_full'):op=5/6
         193 +            elif op==0 and not s.get(r,'calibrated') and any(not s.get(oo,'received_image') for oo in self.objs) and any(self.visible(q,self.xy(s,oo),2)[0] for oo in self.objs):op=-.5
         194 +            action[4*i:4*i+2]=move;action[4*i+3]=op
         195 +            records.append((p,move,op,idx,self.pending_count(s,i)))
         196 +        self.prev=records
         197 +        return action
```

</details>

<a id="C037"></a>
### C037 · Treat refused calibration as evidence against every predicted image at that viewpoint

Commit `e57842e3d05f9fd7cd6cd9d29f51e75f8fbb68dd`; parents: c7180a498e0c4a5dbe22b4d3f4d2c22f36ba6e59. Recorded author date: 2026-09-20T04:02:20+02:00.

File roles (automatic): policy, setup/other, support code (role needs review).

- [E0130](01_timeline.md#E0130): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C037_e57842e_approach.py) · [Exact all-file diff](evidence/diffs/C037_e57842e.diff)

[Previous saved controller snapshot](evidence/versions/C035_5e42672_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0078060..de9f329 100644
--- a/approach.py
+++ b/approach.py
@@ -71,7 +71,7 @@ class GeneratedApproach:
   71     71          pos=[self.xy(s,r) for r in self.rovers]
   72     72          if self.prev is not None:
   73     73              for i in range(2):
   74        -                old,move,op,idx,had=self.prev[i]
          74 +                old,move,op,idx,had,old_images=self.prev[i]
   75     75                  if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
   76     76                      q=old+move
   77     77                      ids=np.linalg.norm(self.points-q,axis=1)<.085
@@ -79,9 +79,10 @@ class GeneratedApproach:
   79     79                      self.make_graph()
   80     80                  if op==.5 and self.pending_count(s,i)>=had:
   81     81                      self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
   82        -                if op in [-.5,-1/6] and idx is not None:
   83        -                    if (op==-.5 and not s.get(self.rovers[i],'calibrated')) or (op==-1/6 and not s.get(self.objs[idx],'have_image_rover'+str(i))):
   84        -                        self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
          82 +                if op==-.5 and not s.get(self.rovers[i],'calibrated'):
          83 +                    self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.12,:]=True
          84 +                if op==-1/6 and idx is not None and sum(s.get(oo,'have_image_rover'+str(i)) for oo in self.objs)<=old_images:
          85 +                    self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.12,idx]=True
   85     86          action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
   86     87          received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
   87     88          acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
@@ -142,7 +143,7 @@ class GeneratedApproach:
  142    143              nearest_sample=min(self.samples,key=lambda oo:np.linalg.norm(q-self.xy(s,oo)))
  143    144              if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249 and s.get(nearest_sample,'is_soil')==j:op=-5/6
  144    145              else:
  145        -                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
         146 +                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and not self.bad[i,self.nearest(q),jj] and self.visible(q,self.xy(s,oo),2)[0]]
  146    147                  if useful:
  147    148                      idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
  148    149                      op=-1/6 if s.get(r,'calibrated') else -.5
@@ -150,6 +151,6 @@ class GeneratedApproach:
  150    151              elif op==0 and s.get(r,'store_full'):op=5/6
  151    152              elif op==0 and not s.get(r,'calibrated') and any(not s.get(oo,'received_image') for oo in self.objs) and any(self.visible(q,self.xy(s,oo),2)[0] for oo in self.objs):op=-.5
  152    153              action[4*i:4*i+2]=move;action[4*i+3]=op
  153        -            records.append((p,move,op,idx,self.pending_count(s,i)))
         154 +            records.append((p,move,op,idx,self.pending_count(s,i),sum(s.get(oo,'have_image_rover'+str(i)) for oo in self.objs)))
  154    155          self.prev=records
  155    156          return action
diff --git a/failure_15_None.json b/failure_15_None.json
new file mode 100644
index 0000000..f0621e3
--- /dev/null
+++ b/failure_15_None.json
@@ -0,0 +1 @@
           1 +[{"t": 0, "rover": [[0.800000011920929, -1.600000023841858, 0.0, 0.0, 0.0], [-0.800000011920929, -1.600000023841858, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, 0.15000000596046448, 0.0, 0.0, 0.20000000298023224, 0.15000000596046448, 0.0, 0.0]}, {"t": 1, "rover": [[0.6000000238418579, -1.399999976158142, 1.0, 0.0, 0.0], [-0.699999988079071, -1.399999976158142, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, 0.20000000298023224, 0.0, -0.8333333134651184, 0.10000000894069672, 0.20000000298023224, 0.0, 0.0]}, {"t": 2, "rover": [[0.7999999523162842, -1.2000000476837158, 1.0, 0.0, 0.0], [-0.5, -1.2000000476837158, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.19999997317790985, 0.19999997317790985, 0.0, 0.5, 0.19999998807907104, 0.19999997317790985, 0.0, 0.0]}, {"t": 3, "rover": [[1.0, -1.0, 0.0, 0.0, 0.0], [-0.699999988079071, -1.0, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.20000000298023224, 0.20000000298023224, 0.0, 0.8333333134651184, -0.20000000298023224, 0.20000000298023224, 0.0, 0.0]}, {"t": 4, "rover": [[1.1999999284744263, -1.100000023841858, 0.0, 0.0, 0.0], [-0.5, -0.800000011920929, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.20000000298023224, -0.10000000149011612, 0.0, 0.0, 0.19999998807907104, 0.20000000298023224, 0.0, 0.0]}, {"t": 5, "rover": [[1.399999976158142, -1.2999999523162842, 0.0, 0.0, 0.0], [-0.699999988079071, -0.6000000238418579, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.20000000298023224, -0.19999997317790985, 0.0, 0.0, -0.20000000298023224, 0.20000000298023224, 0.0, 0.0]}, {"t": 6, "rover": [[1.600000023841858, -1.5, 0.0, 0.0, 0.0], [-0.5, -0.40000003576278687, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.20000000298023224, -0.20000000298023224, 0.0, 0.0, 0.19999998807907104, 0.20000000298023224, 0.0, 0.0]}, {"t": 7, "rover": [[1.7999999523162842, -1.600000023841858, 0.0, 0.0, 0.0], [-0.30000001192092896, -0.20000001788139343, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.19999997317790985, -0.10000000149011612, 0.0, 0.0, 0.20000000298023224, 0.20000000298023224, 0.0, 0.0]}, {"t": 8, "rover": [[2.0, -1.600000023841858, 0.0, 0.0, 0.0], [-0.30000001192092896, -2.086162531611535e-08, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.20000000298023224, 2.3841858265427618e-08, 0.0, 0.0, 1.1920930909070648e-08, 0.20000000298023224, 0.0, -0.5]}, {"t": 9, "rover": [[2.0999999046325684, -1.7999999523162842, 1.0, 0.0, 0.0], [-0.4000000059604645, 0.19999997317790985, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.10000000149011612, -0.19999997317790985, 0.0, -0.8333333134651184, -0.09999998658895493, 0.20000000298023224, 0.0, -0.5]}, {"t": 10, "rover": [[1.9000000953674316, -2.0, 1.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.19999989867210388, -0.20000000298023224, 0.0, 0.5, 5.960466342713744e-09, 2.6822092991096724e-08, 0.0, -0.5]}, {"t": 11, "rover": [[1.7000000476837158, -1.7999999523162842, 0.0, 0.0, 0.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, 0.20000000298023224, 0.0, 0.8333333134651184, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 12, "rover": [[1.899999976158142, -1.600000023841858, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.19999995827674866, 0.19999995827674866, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 13, "rover": [[2.0, -1.399999976158142, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.10000002384185791, 0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 14, "rover": [[1.8000000715255737, -1.2000000476837158, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, 0.19999997317790985, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 15, "rover": [[1.600000023841858, -1.0, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, 0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 16, "rover": [[1.7999999523162842, -0.800000011920929, 0.0, 0.0, 0.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.19999997317790985, 0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 17, "rover": [[2.0, -0.6000000238418579, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.20000000298023224, 0.20000000298023224, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 18, "rover": [[1.7999999523162842, -0.4000000059604645, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, 0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 19, "rover": [[1.600000023841858, -0.20000001788139343, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.19999995827674866, 0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 20, "rover": [[1.7000000476837158, -1.4901161193847656e-08, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.09999997913837433, 0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 21, "rover": [[1.5, 0.19999998807907104, 0.0, 1.0, 0.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, 0.20000000298023224, 0.0, -0.5, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 22, "rover": [[1.5, 0.20000000298023224, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [3.552713678800501e-15, 1.1920931797249068e-08, 0.0, -0.1666666716337204, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 23, "rover": [[1.3000000715255737, -2.9802291745539833e-09, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, -0.20000000298023224, 0.0, 0.5, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 24, "rover": [[1.100000023841858, -0.20000000298023224, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, -0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 25, "rover": [[1.2999999523162842, -0.4000000059604645, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.19999997317790985, -0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 26, "rover": [[1.5, -0.5999999642372131, 0.0, 0.0, 0.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.20000000298023224, -0.19999998807907104, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 27, "rover": [[1.2999999523162842, -0.800000011920929, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, -0.20000000298023224, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 28, "rover": [[1.5, -1.0, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.20000000298023224, -0.19999998807907104, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 29, "rover": [[1.2999999523162842, -1.1999999284744263, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, -0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 30, "rover": [[1.100000023841858, -1.399999976158142, 0.0, 0.0, 0.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.19999995827674866, -0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 31, "rover": [[0.9000000357627869, -1.600000023841858, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [-0.20000000298023224, -0.20000000298023224, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 32, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.09999996423721313, -0.1499999761581421, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 33, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 34, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 35, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 36, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 37, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 38, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 39, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 40, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 41, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 42, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 43, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 44, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 45, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 46, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 47, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 48, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 49, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 50, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 51, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 52, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 53, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 54, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 55, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 56, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 57, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 58, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 59, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 60, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 61, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 62, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 63, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 64, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 65, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 66, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 67, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 68, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 69, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 70, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 71, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 72, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 73, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 74, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 75, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 76, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 77, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 78, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 79, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 80, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 81, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 82, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 83, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 84, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 85, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 86, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 87, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 88, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 89, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 90, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 91, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 92, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 93, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 94, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 95, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 96, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 97, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 98, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 99, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 100, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 101, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 102, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 103, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 104, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 105, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 106, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 107, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 108, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 109, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 110, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 111, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 112, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 113, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 114, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 115, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 116, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 117, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 118, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 119, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 120, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 121, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 122, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 123, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 124, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 125, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 126, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 127, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 128, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 129, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 130, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 131, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 132, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 133, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 134, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 135, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 136, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 137, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 138, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 139, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 140, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 141, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 142, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 143, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 144, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 145, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 146, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 147, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 148, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 149, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 150, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 151, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 152, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 153, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 154, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 155, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 156, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 157, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 158, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 159, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 160, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 161, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 162, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 163, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 164, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 165, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 166, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 167, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 168, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 169, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 170, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 171, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 172, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 173, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 174, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 175, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 176, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 177, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 178, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 179, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 180, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 181, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 182, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 183, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 184, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 185, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 186, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 187, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 188, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 189, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 190, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 191, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 192, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 193, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 194, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 195, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, 1.1920931797249068e-08, 0.0, -0.5]}, {"t": 196, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.3999999761581421, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 197, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, -2.384185648907078e-08, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 198, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.20000000298023224, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}, {"t": 199, "rover": [[1.0, -1.75, 0.0, 0.0, 1.0], [-0.4000000059604645, 0.19999998807907104, 0.0, 0.0, 0.0]], "images": [[0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0]], "samples": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], "action": [0.0, 0.0, 0.0, 0.0, 5.960466342713744e-09, -2.980229840687798e-09, 0.0, -0.5]}]
\ No newline at end of file
diff --git a/tour_candidate.py b/tour_candidate.py
index 3f2bf90..401240f 100644
--- a/tour_candidate.py
+++ b/tour_candidate.py
@@ -113,7 +113,7 @@ class GeneratedApproach:
  113    113          pos=[self.xy(s,r) for r in self.rovers]
  114    114          if self.prev is not None:
  115    115              for i in range(2):
  116        -                old,move,op,idx,had=self.prev[i]
         116 +                old,move,op,idx,had,old_images=self.prev[i]
  117    117                  if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
  118    118                      q=old+move
  119    119                      ids=np.linalg.norm(self.points-q,axis=1)<.085
@@ -121,9 +121,10 @@ class GeneratedApproach:
  121    121                      self.make_graph()
  122    122                  if op==.5 and self.pending_count(s,i)>=had:
  123    123                      self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
  124        -                if op in [-.5,-1/6] and idx is not None:
  125        -                    if (op==-.5 and not s.get(self.rovers[i],'calibrated')) or (op==-1/6 and not s.get(self.objs[idx],'have_image_rover'+str(i))):
  126        -                        self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
         124 +                if op==-.5 and not s.get(self.rovers[i],'calibrated'):
         125 +                    self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.12,:]=True
         126 +                if op==-1/6 and idx is not None and sum(s.get(oo,'have_image_rover'+str(i)) for oo in self.objs)<=old_images:
         127 +                    self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.12,idx]=True
  127    128          action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
  128    129          received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
  129    130          acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
@@ -184,7 +185,7 @@ class GeneratedApproach:
  184    185              nearest_sample=min(self.samples,key=lambda oo:np.linalg.norm(q-self.xy(s,oo)))
  185    186              if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249 and s.get(nearest_sample,'is_soil')==j:op=-5/6
  186    187              else:
  187        -                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
         188 +                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and not self.bad[i,self.nearest(q),jj] and self.visible(q,self.xy(s,oo),2)[0]]
  188    189                  if useful:
  189    190                      idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
  190    191                      op=-1/6 if s.get(r,'calibrated') else -.5
@@ -192,6 +193,6 @@ class GeneratedApproach:
  192    193              elif op==0 and s.get(r,'store_full'):op=5/6
  193    194              elif op==0 and not s.get(r,'calibrated') and any(not s.get(oo,'received_image') for oo in self.objs) and any(self.visible(q,self.xy(s,oo),2)[0] for oo in self.objs):op=-.5
  194    195              action[4*i:4*i+2]=move;action[4*i+3]=op
  195        -            records.append((p,move,op,idx,self.pending_count(s,i)))
         196 +            records.append((p,move,op,idx,self.pending_count(s,i),sum(s.get(oo,'have_image_rover'+str(i)) for oo in self.objs)))
  196    197          self.prev=records
  197    198          return action
diff --git a/tour_results.jsonl b/tour_results.jsonl
new file mode 100644
index 0000000..a031bd2
--- /dev/null
+++ b/tour_results.jsonl
@@ -0,0 +1,30 @@
           1 +{"seed": 0, "n": 3, "steps": 31, "success": true, "sec": 0.322}
           2 +{"seed": 1, "n": 2, "steps": 21, "success": true, "sec": 0.207}
           3 +{"seed": 2, "n": 3, "steps": 22, "success": true, "sec": 0.346}
           4 +{"seed": 3, "n": 3, "steps": 32, "success": true, "sec": 0.562}
           5 +{"seed": 4, "n": 3, "steps": 24, "success": true, "sec": 0.4}
           6 +{"seed": 5, "n": 3, "steps": 28, "success": true, "sec": 0.446}
           7 +{"seed": 6, "n": 2, "steps": 20, "success": true, "sec": 0.239}
           8 +{"seed": 7, "n": 3, "steps": 26, "success": true, "sec": 0.398}
           9 +{"seed": 8, "n": 3, "steps": 26, "success": true, "sec": 0.418}
          10 +{"seed": 9, "n": 2, "steps": 24, "success": true, "sec": 0.385}
          11 +{"seed": 10, "n": 3, "steps": 25, "success": true, "sec": 0.423}
          12 +{"seed": 11, "n": 1, "steps": 21, "success": true, "sec": 0.279}
          13 +{"seed": 12, "n": 2, "steps": 24, "success": true, "sec": 0.353}
          14 +{"seed": 13, "n": 3, "steps": 32, "success": true, "sec": 0.524}
          15 +{"seed": 14, "n": 1, "steps": 35, "success": true, "sec": 1.281}
          16 +{"seed": 15, "n": 3, "steps": 200, "success": false, "sec": 8.55}
          17 +{"seed": 16, "n": 2, "steps": 26, "success": true, "sec": 0.894}
          18 +{"seed": 17, "n": 3, "steps": 31, "success": true, "sec": 1.319}
          19 +{"seed": 18, "n": 3, "steps": 24, "success": true, "sec": 0.894}
          20 +{"seed": 19, "n": 2, "steps": 30, "success": true, "sec": 1.174}
          21 +{"seed": 20, "n": 3, "steps": 32, "success": true, "sec": 1.288}
          22 +{"seed": 21, "n": 1, "steps": 24, "success": true, "sec": 0.866}
          23 +{"seed": 22, "n": 3, "steps": 24, "success": true, "sec": 0.653}
          24 +{"seed": 23, "n": 1, "steps": 18, "success": true, "sec": 0.882}
          25 +{"seed": 24, "n": 2, "steps": 33, "success": true, "sec": 1.131}
          26 +{"seed": 25, "n": 2, "steps": 22, "success": true, "sec": 0.813}
          27 +{"seed": 26, "n": 3, "steps": 30, "success": true, "sec": 1.221}
          28 +{"seed": 27, "n": 1, "steps": 23, "success": true, "sec": 0.558}
          29 +{"seed": 28, "n": 2, "steps": 29, "success": true, "sec": 0.823}
          30 +{"seed": 29, "n": 3, "steps": 25, "success": true, "sec": 0.894}
diff --git a/validation_combined.jsonl b/validation_combined.jsonl
new file mode 100644
index 0000000..31f4a8a
--- /dev/null
+++ b/validation_combined.jsonl
@@ -0,0 +1,63 @@
           1 +{"seed": 1000, "n": 1, "steps": 25, "success": true, "sec": 0.539}
           2 +{"seed": 1001, "n": 3, "steps": 32, "success": true, "sec": 1.158}
           3 +{"seed": 1002, "n": 2, "steps": 22, "success": true, "sec": 0.618}
           4 +{"seed": 1003, "n": 1, "steps": 26, "success": true, "sec": 0.671}
           5 +{"seed": 1004, "n": 3, "steps": 25, "success": true, "sec": 0.56}
           6 +{"seed": 1005, "n": 2, "steps": 24, "success": true, "sec": 0.68}
           7 +{"seed": 1006, "n": 2, "steps": 27, "success": true, "sec": 0.692}
           8 +{"seed": 1007, "n": 1, "steps": 22, "success": true, "sec": 0.58}
           9 +{"seed": 1008, "n": 2, "steps": 26, "success": true, "sec": 0.587}
          10 +{"seed": 1009, "n": 3, "steps": 22, "success": true, "sec": 1.02}
          11 +{"seed": 1010, "n": 3, "steps": 25, "success": true, "sec": 0.901}
          12 +{"seed": 1011, "n": 1, "steps": 33, "success": true, "sec": 1.038}
          13 +{"seed": 1012, "n": 3, "steps": 29, "success": true, "sec": 1.245}
          14 +{"seed": 1013, "n": 1, "steps": 27, "success": true, "sec": 0.922}
          15 +{"seed": 1014, "n": 2, "steps": 30, "success": true, "sec": 1.244}
          16 +{"seed": 1015, "n": 2, "steps": 41, "success": true, "sec": 1.627}
          17 +{"seed": 1016, "n": 2, "steps": 25, "success": true, "sec": 1.182}
          18 +{"seed": 1017, "n": 3, "steps": 33, "success": true, "sec": 1.329}
          19 +{"seed": 1018, "n": 3, "steps": 29, "success": true, "sec": 1.01}
          20 +{"seed": 1019, "n": 2, "steps": 30, "success": true, "sec": 1.828}
          21 +{"seed": 1020, "n": 3, "steps": 24, "success": true, "sec": 0.758}
          22 +{"seed": 1021, "n": 1, "steps": 22, "success": true, "sec": 0.472}
          23 +{"seed": 1022, "n": 3, "steps": 23, "success": true, "sec": 0.405}
          24 +{"seed": 1023, "n": 1, "steps": 33, "success": true, "sec": 0.396}
          25 +{"seed": 1024, "n": 2, "steps": 29, "success": true, "sec": 0.473}
          26 +{"seed": 1025, "n": 3, "steps": 26, "success": true, "sec": 0.422}
          27 +{"seed": 1026, "n": 2, "steps": 21, "success": true, "sec": 0.327}
          28 +{"seed": 1027, "n": 2, "steps": 21, "success": true, "sec": 0.342}
          29 +{"seed": 1028, "n": 2, "steps": 27, "success": true, "sec": 0.431}
          30 +{"seed": 1029, "n": 2, "steps": 23, "success": true, "sec": 0.343}
          31 +{"seed": 1030, "n": 2, "steps": 32, "success": true, "sec": 0.504}
          32 +{"seed": 1031, "n": 3, "steps": 25, "success": true, "sec": 0.433}
          33 +{"seed": 1032, "n": 2, "steps": 29, "success": true, "sec": 0.449}
          34 +{"seed": 1033, "n": 2, "steps": 21, "success": true, "sec": 0.336}
          35 +{"seed": 1034, "n": 2, "steps": 26, "success": true, "sec": 0.46}
          36 +{"seed": 1035, "n": 1, "steps": 20, "success": true, "sec": 0.304}
          37 +{"seed": 1036, "n": 2, "steps": 25, "success": true, "sec": 0.4}
          38 +{"seed": 1037, "n": 2, "steps": 21, "success": true, "sec": 0.332}
          39 +{"seed": 1038, "n": 2, "steps": 28, "success": true, "sec": 0.457}
          40 +{"seed": 1039, "n": 2, "steps": 27, "success": true, "sec": 0.396}
          41 +{"seed": 1040, "n": 1, "steps": 24, "success": true, "sec": 0.362}
          42 +{"seed": 1041, "n": 3, "steps": 27, "success": true, "sec": 0.477}
          43 +{"seed": 1042, "n": 3, "steps": 29, "success": true, "sec": 0.474}
          44 +{"seed": 1043, "n": 3, "steps": 25, "success": true, "sec": 0.404}
          45 +{"seed": 1044, "n": 1, "steps": 24, "success": true, "sec": 0.268}
          46 +{"seed": 1045, "n": 3, "steps": 25, "success": true, "sec": 0.414}
          47 +{"seed": 1046, "n": 1, "steps": 21, "success": true, "sec": 0.303}
          48 +{"seed": 1047, "n": 1, "steps": 31, "success": true, "sec": 0.453}
          49 +{"seed": 1048, "n": 3, "steps": 26, "success": true, "sec": 0.443}
          50 +{"seed": 1049, "n": 3, "steps": 29, "success": true, "sec": 0.463}
          51 +{"seed": 1050, "n": 2, "steps": 30, "success": true, "sec": 0.21}
          52 +{"seed": 1051, "n": 1, "steps": 18, "success": true, "sec": 0.222}
          53 +{"seed": 1052, "n": 2, "steps": 32, "success": true, "sec": 0.482}
          54 +{"seed": 1053, "n": 1, "steps": 20, "success": true, "sec": 0.296}
          55 +{"seed": 1054, "n": 1, "steps": 25, "success": true, "sec": 0.375}
          56 +{"seed": 1055, "n": 2, "steps": 25, "success": true, "sec": 0.31}
          57 +{"seed": 1056, "n": 3, "steps": 28, "success": true, "sec": 0.445}
          58 +{"seed": 1057, "n": 3, "steps": 33, "success": true, "sec": 0.348}
          59 +{"seed": 1058, "n": 3, "steps": 30, "success": true, "sec": 0.491}
          60 +{"seed": 1059, "n": 2, "steps": 25, "success": true, "sec": 0.402}
          61 +{"seed": 1060, "n": 1, "steps": 21, "success": true, "sec": 0.277}
          62 +{"seed": 1061, "n": 3, "steps": 31, "success": true, "sec": 0.328}
          63 +{"seed": 1062, "n": 3, "steps": 24, "success": true, "sec": 0.392}
```

</details>

<a id="C038"></a>
### C038 · Compare following the task order from the compact routing model

Commit `1a3f4c1e66e1ec0a7436fcdd2f49cc7e30ce0cf5`; parents: e57842e3d05f9fd7cd6cd9d29f51e75f8fbb68dd. Recorded author date: 2026-09-20T04:04:06+02:00.

File roles (automatic): diagnostic/test, setup/other, support code (role needs review).

- [E0139](01_timeline.md#E0139): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C038_1a3f4c1.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/ordered_candidate.py b/ordered_candidate.py
new file mode 100644
index 0000000..29f1af4
--- /dev/null
+++ b/ordered_candidate.py
@@ -0,0 +1,219 @@
           1 +import numpy as np
           2 +from scipy.sparse import csr_matrix
           3 +from scipy.sparse.csgraph import dijkstra
           4 +
           5 +class GeneratedApproach:
           6 +    def __init__(self, action_space, observation_space, primitives):
           7 +        self.space = observation_space
           8 +    def objects(self, s, t):
           9 +        return s.get_objects(self.space.get_type(t))
          10 +    def xy(self,s,o):
          11 +        return np.array([s.get(o,'x'),s.get(o,'y')])
          12 +    def reset(self,state,info):
          13 +        self.rovers=[state.get_object_from_name('rover'+str(i)) for i in range(2)]
          14 +        self.homes=[self.xy(state,r) for r in self.rovers]
          15 +        self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
          16 +        self.lander=self.xy(state,self.objects(state,'lander')[0])
          17 +        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,2.5]])
          18 +        self.axis=np.arange(-2.3,2.301,0.1)
          19 +        self.n=len(self.axis)
          20 +        self.points=np.array([(x,y) for x in self.axis for y in self.axis])
          21 +        self.valid=self.free(self.points)
          22 +        self.bad=np.zeros((2,len(self.points),len(self.objs)),dtype=bool)
          23 +        self.send_bad=np.zeros((2,len(self.points)),dtype=bool)
          24 +        self.prev=None; self.step=0
          25 +        self.make_graph()
          26 +        self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
          27 +        sample_dist=np.array([np.linalg.norm(self.points-self.xy(state,o),axis=1) for o in self.samples])
          28 +        self.sample_masks=[(dd<.245)&(dd<=sample_dist.min(axis=0)+1e-8) for dd in sample_dist]
          29 +        self.radio_mask=self.visible(self.points,self.lander,4)
          30 +        self.home_dist=[dijkstra(self.graph,indices=self.nearest(h)) for h in self.homes]
          31 +        self.allocate(state)
          32 +    def allocate(self,s):
          33 +        num=len(self.objs); size=1<<(num+2); allbits=size-1
          34 +        masks=self.sample_masks+self.image_masks
          35 +        costs=[]; traces=[]
          36 +        for r in range(2):
          37 +            hd=self.home_dist[r]; nodes={self.nearest(self.homes[r])}
          38 +            for mask in self.sample_masks:
          39 +                dd=np.where(mask,hd,np.inf);idx=int(dd.argmin())
          40 +                if np.isfinite(dd[idx]):nodes.add(idx)
          41 +            for subset in range(1,1<<num):
          42 +                mask=self.valid.copy()
          43 +                for j in range(num):
          44 +                    if subset>>j&1:mask &= self.image_masks[j]
          45 +                dd=np.where(mask,hd,np.inf);idx=int(dd.argmin())
          46 +                if np.isfinite(dd[idx]):nodes.add(idx)
          47 +            nodes=list(nodes); D=dijkstra(self.graph,indices=nodes)[:,nodes]
          48 +            cover=[]
          49 +            for node in nodes:
          50 +                bits=0
          51 +                for j,m in enumerate(self.sample_masks):
          52 +                    if m[node]:bits|=1<<int(s.get(self.samples[j],'is_soil'))
          53 +                for j,m in enumerate(self.image_masks):
          54 +                    if m[node]:bits|=1<<(j+2)
          55 +                cover.append(bits)
          56 +            dp=np.full((size,len(nodes)),np.inf)
          57 +            parents=np.full((size,len(nodes),2),-1,dtype=int)
          58 +            home=nodes.index(self.nearest(self.homes[r]));dp[0,home]=0
          59 +            for mask in range(size):
          60 +                if not np.isfinite(dp[mask]).any():continue
          61 +                arrivals=np.min(dp[mask,:,None]+D,axis=0)
          62 +                for j,bits in enumerate(cover):
          63 +                    gain=bits&~mask
          64 +                    if not gain:continue
          65 +                    extra=2*((gain&3).bit_count())+4*((gain>>2).bit_count())
          66 +                    new=mask|bits
          67 +                    if arrivals[j]+extra<dp[new,j]:
          68 +                        dp[new,j]=arrivals[j]+extra
          69 +                        parents[new,j]=[mask,int(np.argmin(dp[mask]+D[:,j]))]
          70 +            val=np.min(dp+D[:,home],axis=1)
          71 +            bestmask=np.arange(size)
          72 +            for mask in range(size-1,-1,-1):
          73 +                for j in range(num+2):
          74 +                    if not mask>>j&1 and val[mask|(1<<j)]<val[mask]:
          75 +                        val[mask]=val[mask|(1<<j)];bestmask[mask]=bestmask[mask|(1<<j)]
          76 +            costs.append(val)
          77 +            traces.append((dp,D[:,home],parents,bestmask,nodes))
          78 +        best=min(range(size),key=lambda m:max(costs[0][m],costs[1][allbits^m])+.05*(costs[0][m]+costs[1][allbits^m]))
          79 +        self.owner=[0 if best>>j&1 else 1 for j in range(num+2)]
          80 +        self.stages=[]
          81 +        for r,need in enumerate([best,allbits^best]):
          82 +            dp,back,parents,bestmask,nodes=traces[r]
          83 +            mask=int(bestmask[need]);node=int(np.argmin(dp[mask]+back));stages=[]
          84 +            while mask:
          85 +                previous,prevnode=parents[mask,node]
          86 +                if previous<0:break
          87 +                stages.append(int(mask^previous));mask=int(previous);node=int(prevnode)
          88 +            self.stages.append(stages[::-1])
          89 +    def free(self,p):
          90 +        p=np.atleast_2d(p)
          91 +        d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
          92 +        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.228**2,axis=1)
          93 +        ld=np.maximum(np.abs(p-self.lander)-np.array([.45,.30]),0)
          94 +        ok &= np.sum(ld**2,axis=1)>.228**2
          95 +        ok &= np.max(np.abs(p),axis=1)<2.271
          96 +        return ok
          97 +    def make_graph(self):
          98 +        rows=[]; cols=[]
          99 +        for i in np.flatnonzero(self.valid):
         100 +            x,y=divmod(i,self.n)
         101 +            for dx,dy in [(dx,dy) for dx in range(-2,3) for dy in range(-2,3) if dx or dy]:
         102 +                xx,yy=x+dx,y+dy
         103 +                if 0<=xx<self.n and 0<=yy<self.n:
         104 +                    j=xx*self.n+yy
         105 +                    if self.valid[j]: rows.append(i);cols.append(j)
         106 +        self.graph=csr_matrix((np.full(len(rows),2.),(rows,cols)),shape=(len(self.points),len(self.points)))
         107 +    def visible(self,p,target,limit):
         108 +        p=np.atleast_2d(p); target=np.asarray(target)
         109 +        ok=np.linalg.norm(p-target,axis=1)<(3.91 if limit>3 else limit-.025)
         110 +        # Low mounds and the central driving wall do not obstruct the camera.
         111 +        boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
         112 +        delta=target-p
         113 +        for b in boxes:
         114 +            padding=.05 if limit>3 else 0.
         115 +            lo=b[:2]-b[2:]-padding;hi=b[:2]+b[2:]+padding
         116 +            with np.errstate(divide='ignore',invalid='ignore'):
         117 +                t1=(lo-p)/delta;t2=(hi-p)/delta
         118 +            near=np.maximum(np.min(np.stack([t1,t2]),axis=0).max(axis=1),.001)
         119 +            far=np.minimum(np.max(np.stack([t1,t2]),axis=0).min(axis=1),.999)
         120 +            ok &= near>far
         121 +        return ok
         122 +    def nearest(self,p):
         123 +        ds=np.sum((self.points-p)**2,axis=1);ds[~self.valid]=np.inf
         124 +        return int(np.argmin(ds))
         125 +    def pending_count(self,s,i):
         126 +        return sum(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs)+sum(s.get(o,'analyzed_rover'+str(i)) and not s.get(o,'received_analysis') for o in self.samples)
         127 +    def get_action(self,s):
         128 +        self.step+=1
         129 +        pos=[self.xy(s,r) for r in self.rovers]
         130 +        if self.prev is not None:
         131 +            for i in range(2):
         132 +                old,move,op,idx,had,old_images=self.prev[i]
         133 +                if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
         134 +                    q=old+move
         135 +                    ids=np.linalg.norm(self.points-q,axis=1)<.085
         136 +                    self.valid[ids]=False
         137 +                    self.make_graph()
         138 +                if op==.5 and self.pending_count(s,i)>=had:
         139 +                    self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
         140 +                if op==-.5 and not s.get(self.rovers[i],'calibrated'):
         141 +                    self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.12,:]=True
         142 +                if op==-1/6 and idx is not None and sum(s.get(oo,'have_image_rover'+str(i)) for oo in self.objs)<=old_images:
         143 +                    self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.12,idx]=True
         144 +        action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
         145 +        received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
         146 +        acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
         147 +        complete=int(acquired[0])+2*int(acquired[1])
         148 +        for j,o in enumerate(self.objs):
         149 +            if s.get(o,'received_image') or any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]):complete |=1<<(j+2)
         150 +        for i,r in enumerate(self.rovers):
         151 +            while self.stages[i] and not self.stages[i][0]&~complete:self.stages[i].pop(0)
         152 +            stage=self.stages[i][0] if self.stages[i] else 0
         153 +            p=pos[i]; start=self.nearest(p)
         154 +            dist,pred=dijkstra(self.graph,indices=start,return_predecessors=True)
         155 +            candidates=[]
         156 +            for k in [0,1]:
         157 +                if stage>>k&1 and not acquired[k] and k not in kinds and not s.get(r,'store_full'):
         158 +                    for oi,o in enumerate(self.samples):
         159 +                        if int(s.get(o,'is_soil'))==k:
         160 +                            mask=self.sample_masks[oi]
         161 +                            candidates.append((mask,'sample',o,k))
         162 +            for j,o in enumerate(self.objs):
         163 +                if stage>>(j+2)&1 and not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]) and j not in assigned:
         164 +                    mask=self.image_masks[j]&~self.bad[i,:,j]
         165 +                    candidates.append((mask,'image',o,j))
         166 +            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
         167 +            if pending: candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
         168 +            best=None; score=np.inf
         169 +            for mask,task,o,j in candidates:
         170 +                dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         171 +                target=int(np.argmin(dd)); cost=dd[target]
         172 +                if task=='sample': cost-=6
         173 +                if task=='send': cost+=5 if any(c[1]!='send' for c in candidates) else 0
         174 +                if cost<score: score=cost;best=(target,task,o,j)
         175 +            if best is None: best=(self.nearest(self.homes[i]),'home',None,None)
         176 +            target,task,o,j=best
         177 +            if task=='send' and self.visible(p,self.lander,4)[0] and not self.send_bad[i,start]:
         178 +                navbest=None;navcost=np.inf
         179 +                for mask,nt,no,nj in candidates:
         180 +                    if nt=='send':continue
         181 +                    dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
         182 +                    ni=int(np.argmin(dd))
         183 +                    if dd[ni]<navcost:navcost=dd[ni];navbest=(ni,nt,no,nj)
         184 +                if navbest is not None:target,task,o,j=navbest
         185 +                else:target=self.nearest(self.homes[i]);task='home'
         186 +            if task=='sample': kinds.add(j)
         187 +            if task=='image': assigned.add(j)
         188 +            targetpos=self.points[target]
         189 +            if task=='home': targetpos=self.homes[i]
         190 +            path=[target];cur=target
         191 +            for _ in range(len(self.points)):
         192 +                if cur==start:break
         193 +                cur=int(pred[cur])
         194 +                if cur<0:break
         195 +                path.append(cur)
         196 +            path=path[::-1]
         197 +            goal=targetpos
         198 +            for node in path:
         199 +                q=self.points[node]
         200 +                if np.max(np.abs(q-p))<=.20001: goal=q
         201 +                else: break
         202 +            if np.max(np.abs(targetpos-p))<=.2:goal=targetpos
         203 +            move=np.clip(goal-p,-.2,.2)
         204 +            if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
         205 +            q=p+move; op=0.;idx=None
         206 +            nearest_sample=min(self.samples,key=lambda oo:np.linalg.norm(q-self.xy(s,oo)))
         207 +            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249 and s.get(nearest_sample,'is_soil')==j:op=-5/6
         208 +            else:
         209 +                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and not self.bad[i,self.nearest(q),jj] and self.visible(q,self.xy(s,oo),2)[0]]
         210 +                if useful:
         211 +                    idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
         212 +                    op=-1/6 if s.get(r,'calibrated') else -.5
         213 +            if op==0 and pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
         214 +            elif op==0 and s.get(r,'store_full'):op=5/6
         215 +            elif op==0 and not s.get(r,'calibrated') and any(not s.get(oo,'received_image') for oo in self.objs) and any(self.visible(q,self.xy(s,oo),2)[0] for oo in self.objs):op=-.5
         216 +            action[4*i:4*i+2]=move;action[4*i+3]=op
         217 +            records.append((p,move,op,idx,self.pending_count(s,i),sum(s.get(oo,'have_image_rover'+str(i)) for oo in self.objs)))
         218 +        self.prev=records
         219 +        return action
diff --git a/test_ordered.py b/test_ordered.py
new file mode 100644
index 0000000..53c75cb
--- /dev/null
+++ b/test_ordered.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +from ordered_candidate import GeneratedApproach
           3 +import time,sys,json
           4 +start_seed=int(sys.argv[1]);end_seed=int(sys.argv[2]);count=int(sys.argv[3]) if len(sys.argv)>3 else None
           5 +for seed in range(start_seed,end_seed):
           6 + e=make_env();s,info=e.reset(seed=seed,options={'object_count':count} if count else None);p=GeneratedApproach(e.action_space,e.observation_space,{})
           7 + start=time.time();p.reset(s,info);hist=[]
           8 + for t in range(200):
           9 +  a=p.get_action(s);s,r,done,trunc,inf=e.step(a)
          10 +  hist.append({'t':t,'rover':[[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers], 'images':[[s.get(o,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for o in p.objs], 'samples':[[s.get(o,k) for k in ['received_analysis','analyzed_rover0','analyzed_rover1']] for o in p.samples], 'action':a.tolist()})
          11 +  if done or trunc:break
          12 + result={'seed':seed,'n':len(p.objs),'steps':t+1,'success':done,'sec':round(time.time()-start,3)}
          13 + if not done:
          14 +  with open('failure_%s_%s.json'%(seed,count),'w') as f:json.dump(hist,f)
          15 + print(json.dumps(result),flush=True);e.close()
diff --git a/tour_fixed.jsonl b/tour_fixed.jsonl
new file mode 100644
index 0000000..4140ab8
--- /dev/null
+++ b/tour_fixed.jsonl
@@ -0,0 +1,30 @@
           1 +{"seed": 0, "n": 3, "steps": 31, "success": true, "sec": 0.608}
           2 +{"seed": 1, "n": 2, "steps": 21, "success": true, "sec": 0.886}
           3 +{"seed": 2, "n": 3, "steps": 22, "success": true, "sec": 0.858}
           4 +{"seed": 3, "n": 3, "steps": 31, "success": true, "sec": 1.379}
           5 +{"seed": 4, "n": 3, "steps": 24, "success": true, "sec": 1.172}
           6 +{"seed": 5, "n": 3, "steps": 28, "success": true, "sec": 1.205}
           7 +{"seed": 6, "n": 2, "steps": 20, "success": true, "sec": 0.859}
           8 +{"seed": 7, "n": 3, "steps": 26, "success": true, "sec": 0.968}
           9 +{"seed": 8, "n": 3, "steps": 26, "success": true, "sec": 0.877}
          10 +{"seed": 9, "n": 2, "steps": 24, "success": true, "sec": 1.076}
          11 +{"seed": 10, "n": 3, "steps": 25, "success": true, "sec": 1.088}
          12 +{"seed": 11, "n": 1, "steps": 21, "success": true, "sec": 0.653}
          13 +{"seed": 12, "n": 2, "steps": 24, "success": true, "sec": 1.077}
          14 +{"seed": 13, "n": 3, "steps": 32, "success": true, "sec": 1.091}
          15 +{"seed": 14, "n": 1, "steps": 35, "success": true, "sec": 1.099}
          16 +{"seed": 15, "n": 3, "steps": 32, "success": true, "sec": 1.394}
          17 +{"seed": 16, "n": 2, "steps": 26, "success": true, "sec": 1.155}
          18 +{"seed": 17, "n": 3, "steps": 31, "success": true, "sec": 1.01}
          19 +{"seed": 18, "n": 3, "steps": 24, "success": true, "sec": 1.094}
          20 +{"seed": 19, "n": 2, "steps": 30, "success": true, "sec": 1.219}
          21 +{"seed": 20, "n": 3, "steps": 32, "success": true, "sec": 1.594}
          22 +{"seed": 21, "n": 1, "steps": 24, "success": true, "sec": 0.596}
          23 +{"seed": 22, "n": 3, "steps": 24, "success": true, "sec": 1.032}
          24 +{"seed": 23, "n": 1, "steps": 18, "success": true, "sec": 0.57}
          25 +{"seed": 24, "n": 2, "steps": 33, "success": true, "sec": 1.871}
          26 +{"seed": 25, "n": 2, "steps": 22, "success": true, "sec": 1.051}
          27 +{"seed": 26, "n": 3, "steps": 31, "success": true, "sec": 1.06}
          28 +{"seed": 27, "n": 1, "steps": 23, "success": true, "sec": 0.874}
          29 +{"seed": 28, "n": 2, "steps": 29, "success": true, "sec": 1.098}
          30 +{"seed": 29, "n": 3, "steps": 25, "success": true, "sec": 0.834}
diff --git a/validation_combined.jsonl b/validation_combined.jsonl
index 31f4a8a..1cbaa2a 100644
--- a/validation_combined.jsonl
+++ b/validation_combined.jsonl
@@ -61,3 +61,40 @@
   61     61  {"seed": 1060, "n": 1, "steps": 21, "success": true, "sec": 0.277}
   62     62  {"seed": 1061, "n": 3, "steps": 31, "success": true, "sec": 0.328}
   63     63  {"seed": 1062, "n": 3, "steps": 24, "success": true, "sec": 0.392}
          64 +{"seed": 1063, "n": 2, "steps": 22, "success": true, "sec": 0.317}
          65 +{"seed": 1064, "n": 3, "steps": 36, "success": true, "sec": 1.288}
          66 +{"seed": 1065, "n": 3, "steps": 26, "success": true, "sec": 1.003}
          67 +{"seed": 1066, "n": 3, "steps": 28, "success": true, "sec": 1.057}
          68 +{"seed": 1067, "n": 1, "steps": 31, "success": true, "sec": 0.941}
          69 +{"seed": 1068, "n": 1, "steps": 23, "success": true, "sec": 0.843}
          70 +{"seed": 1069, "n": 2, "steps": 30, "success": true, "sec": 1.238}
          71 +{"seed": 1070, "n": 1, "steps": 27, "success": true, "sec": 0.737}
          72 +{"seed": 1071, "n": 3, "steps": 24, "success": true, "sec": 0.891}
          73 +{"seed": 1072, "n": 3, "steps": 25, "success": true, "sec": 1.131}
          74 +{"seed": 1073, "n": 2, "steps": 26, "success": true, "sec": 0.782}
          75 +{"seed": 1074, "n": 2, "steps": 23, "success": true, "sec": 1.088}
          76 +{"seed": 1075, "n": 3, "steps": 23, "success": true, "sec": 0.971}
          77 +{"seed": 1076, "n": 2, "steps": 23, "success": true, "sec": 0.816}
          78 +{"seed": 1077, "n": 3, "steps": 32, "success": true, "sec": 1.314}
          79 +{"seed": 1078, "n": 3, "steps": 27, "success": true, "sec": 1.078}
          80 +{"seed": 1079, "n": 1, "steps": 31, "success": true, "sec": 0.747}
          81 +{"seed": 1080, "n": 2, "steps": 20, "success": true, "sec": 0.65}
          82 +{"seed": 1081, "n": 2, "steps": 18, "success": true, "sec": 0.715}
          83 +{"seed": 1082, "n": 2, "steps": 23, "success": true, "sec": 0.636}
          84 +{"seed": 1083, "n": 2, "steps": 27, "success": true, "sec": 1.173}
          85 +{"seed": 1084, "n": 1, "steps": 25, "success": true, "sec": 0.626}
          86 +{"seed": 1085, "n": 2, "steps": 25, "success": true, "sec": 0.671}
          87 +{"seed": 1086, "n": 3, "steps": 29, "success": true, "sec": 1.442}
          88 +{"seed": 1087, "n": 2, "steps": 23, "success": true, "sec": 0.868}
          89 +{"seed": 1088, "n": 1, "steps": 28, "success": true, "sec": 1.044}
          90 +{"seed": 1089, "n": 1, "steps": 22, "success": true, "sec": 0.57}
          91 +{"seed": 1090, "n": 1, "steps": 24, "success": true, "sec": 1.04}
          92 +{"seed": 1091, "n": 2, "steps": 23, "success": true, "sec": 0.719}
          93 +{"seed": 1092, "n": 3, "steps": 29, "success": true, "sec": 1.166}
          94 +{"seed": 1093, "n": 3, "steps": 26, "success": true, "sec": 1.113}
          95 +{"seed": 1094, "n": 3, "steps": 34, "success": true, "sec": 1.3}
          96 +{"seed": 1095, "n": 1, "steps": 20, "success": true, "sec": 0.327}
          97 +{"seed": 1096, "n": 2, "steps": 25, "success": true, "sec": 0.394}
          98 +{"seed": 1097, "n": 1, "steps": 27, "success": true, "sec": 0.401}
          99 +{"seed": 1098, "n": 2, "steps": 31, "success": true, "sec": 0.446}
         100 +{"seed": 1099, "n": 1, "steps": 37, "success": true, "sec": 0.577}
```

</details>

<a id="C039"></a>
### C039 · Document the validated controller and preserve comparison results

Commit `2e4955bb60ad4b90a3b00dc94140ead360d1e995`; parents: 1a3f4c1e66e1ec0a7436fcdd2f49cc7e30ce0cf5. Recorded author date: 2026-09-20T04:05:16+02:00.

File roles (automatic): policy, setup/other.

- [E0144](01_timeline.md#E0144): commit hash in recorded output.
[Controller after this commit](evidence/versions/C039_2e4955b_approach.py) · [Exact all-file diff](evidence/diffs/C039_2e4955b.diff)

[Previous saved controller snapshot](evidence/versions/C037_e57842e_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index de9f329..f3f5054 100644
--- a/approach.py
+++ b/approach.py
@@ -3,6 +3,12 @@ from scipy.sparse import csr_matrix
    3      3  from scipy.sparse.csgraph import dijkstra
    4      4  
    5      5  class GeneratedApproach:
           6 +    """Concurrent rover control with short grid paths and learned visibility failures.
           7 +
           8 +    The grid encodes driving geometry, while separate masks encode camera and
           9 +    radio visibility. Operators run during travel whenever their preconditions
          10 +    are predicted to hold. Failed operations refine these masks online.
          11 +    """
    6     12      def __init__(self, action_space, observation_space, primitives):
    7     13          self.space = observation_space
    8     14      def objects(self, s, t):
@@ -14,6 +20,7 @@ class GeneratedApproach:
   14     20          self.homes=[self.xy(state,r) for r in self.rovers]
   15     21          self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
   16     22          self.lander=self.xy(state,self.objects(state,'lander')[0])
          23 +        # The central wall is fixed but is not included in the observation.
   17     24          self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,2.5]])
   18     25          self.axis=np.arange(-2.3,2.301,0.1)
   19     26          self.n=len(self.axis)
@@ -24,6 +31,7 @@ class GeneratedApproach:
   24     31          self.prev=None; self.step=0
   25     32          self.make_graph()
   26     33          self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
          34 +        # Sampling selects the closest sample, including analyzed samples.
   27     35          sample_dist=np.array([np.linalg.norm(self.points-self.xy(state,o),axis=1) for o in self.samples])
   28     36          self.sample_masks=[(dd<.245)&(dd<=sample_dist.min(axis=0)+1e-8) for dd in sample_dist]
   29     37          self.radio_mask=self.visible(self.points,self.lander,4)
@@ -37,6 +45,7 @@ class GeneratedApproach:
   37     45          ok &= np.max(np.abs(p),axis=1)<2.271
   38     46          return ok
   39     47      def make_graph(self):
          48 +        # A graph edge is one action, including diagonal and partial moves.
   40     49          rows=[]; cols=[]
   41     50          for i in np.flatnonzero(self.valid):
   42     51              x,y=divmod(i,self.n)
@@ -69,6 +78,7 @@ class GeneratedApproach:
   69     78      def get_action(self,s):
   70     79          self.step+=1
   71     80          pos=[self.xy(s,r) for r in self.rovers]
          81 +        # Silent refusals provide local collision and visibility evidence.
   72     82          if self.prev is not None:
   73     83              for i in range(2):
   74     84                  old,move,op,idx,had,old_images=self.prev[i]
diff --git a/final_four_check.jsonl b/final_four_check.jsonl
new file mode 100644
index 0000000..14a2d73
--- /dev/null
+++ b/final_four_check.jsonl
@@ -0,0 +1,48 @@
           1 +{"seed": 2000, "n": 4, "steps": 31, "success": true, "sec": 0.863}
           2 +{"seed": 2001, "n": 4, "steps": 31, "success": true, "sec": 1.651}
           3 +{"seed": 2002, "n": 4, "steps": 27, "success": true, "sec": 1.01}
           4 +{"seed": 2003, "n": 4, "steps": 30, "success": true, "sec": 1.195}
           5 +{"seed": 2004, "n": 4, "steps": 27, "success": true, "sec": 0.952}
           6 +{"seed": 2005, "n": 4, "steps": 33, "success": true, "sec": 1.252}
           7 +{"seed": 2006, "n": 4, "steps": 32, "success": true, "sec": 1.192}
           8 +{"seed": 2007, "n": 4, "steps": 24, "success": true, "sec": 1.094}
           9 +{"seed": 2008, "n": 4, "steps": 29, "success": true, "sec": 1.297}
          10 +{"seed": 2009, "n": 4, "steps": 28, "success": true, "sec": 1.003}
          11 +{"seed": 2010, "n": 4, "steps": 27, "success": true, "sec": 1.142}
          12 +{"seed": 2011, "n": 4, "steps": 31, "success": true, "sec": 1.155}
          13 +{"seed": 2012, "n": 4, "steps": 23, "success": true, "sec": 0.874}
          14 +{"seed": 2013, "n": 4, "steps": 27, "success": true, "sec": 0.645}
          15 +{"seed": 2014, "n": 4, "steps": 26, "success": true, "sec": 0.468}
          16 +{"seed": 2015, "n": 4, "steps": 24, "success": true, "sec": 0.375}
          17 +{"seed": 2016, "n": 4, "steps": 28, "success": true, "sec": 0.504}
          18 +{"seed": 2017, "n": 4, "steps": 33, "success": true, "sec": 0.628}
          19 +{"seed": 2018, "n": 4, "steps": 30, "success": true, "sec": 0.536}
          20 +{"seed": 2019, "n": 4, "steps": 24, "success": true, "sec": 0.421}
          21 +{"seed": 2020, "n": 4, "steps": 29, "success": true, "sec": 0.507}
          22 +{"seed": 2021, "n": 4, "steps": 27, "success": true, "sec": 0.471}
          23 +{"seed": 2022, "n": 4, "steps": 31, "success": true, "sec": 0.547}
          24 +{"seed": 2023, "n": 4, "steps": 32, "success": true, "sec": 0.585}
          25 +{"seed": 2024, "n": 4, "steps": 38, "success": true, "sec": 0.643}
          26 +{"seed": 2025, "n": 4, "steps": 25, "success": true, "sec": 0.463}
          27 +{"seed": 2026, "n": 4, "steps": 24, "success": true, "sec": 0.402}
          28 +{"seed": 2027, "n": 4, "steps": 33, "success": true, "sec": 0.617}
          29 +{"seed": 2028, "n": 4, "steps": 35, "success": true, "sec": 0.596}
          30 +{"seed": 2029, "n": 4, "steps": 24, "success": true, "sec": 0.426}
          31 +{"seed": 2030, "n": 4, "steps": 24, "success": true, "sec": 0.318}
          32 +{"seed": 2031, "n": 4, "steps": 27, "success": true, "sec": 0.465}
          33 +{"seed": 2032, "n": 4, "steps": 29, "success": true, "sec": 0.56}
          34 +{"seed": 2033, "n": 4, "steps": 26, "success": true, "sec": 0.457}
          35 +{"seed": 2034, "n": 4, "steps": 28, "success": true, "sec": 0.554}
          36 +{"seed": 2035, "n": 4, "steps": 39, "success": true, "sec": 0.643}
          37 +{"seed": 2036, "n": 4, "steps": 32, "success": true, "sec": 0.576}
          38 +{"seed": 2037, "n": 4, "steps": 29, "success": true, "sec": 0.5}
          39 +{"seed": 2038, "n": 4, "steps": 30, "success": true, "sec": 0.555}
          40 +{"seed": 2039, "n": 4, "steps": 28, "success": true, "sec": 0.424}
          41 +{"seed": 2040, "n": 4, "steps": 25, "success": true, "sec": 0.384}
          42 +{"seed": 2041, "n": 4, "steps": 25, "success": true, "sec": 0.447}
          43 +{"seed": 2042, "n": 4, "steps": 30, "success": true, "sec": 0.531}
          44 +{"seed": 2043, "n": 4, "steps": 29, "success": true, "sec": 0.416}
          45 +{"seed": 2044, "n": 4, "steps": 29, "success": true, "sec": 0.458}
          46 +{"seed": 2045, "n": 4, "steps": 27, "success": true, "sec": 0.471}
          47 +{"seed": 2046, "n": 4, "steps": 35, "success": true, "sec": 0.69}
          48 +{"seed": 2047, "n": 4, "steps": 30, "success": true, "sec": 1.084}
diff --git a/final_mixed_check.jsonl b/final_mixed_check.jsonl
new file mode 100644
index 0000000..e69de29
diff --git a/ordered_results.jsonl b/ordered_results.jsonl
new file mode 100644
index 0000000..3d1a9d9
--- /dev/null
+++ b/ordered_results.jsonl
@@ -0,0 +1,30 @@
           1 +{"seed": 0, "n": 3, "steps": 31, "success": true, "sec": 0.315}
           2 +{"seed": 1, "n": 2, "steps": 21, "success": true, "sec": 0.246}
           3 +{"seed": 2, "n": 3, "steps": 22, "success": true, "sec": 0.362}
           4 +{"seed": 3, "n": 3, "steps": 31, "success": true, "sec": 0.489}
           5 +{"seed": 4, "n": 3, "steps": 24, "success": true, "sec": 0.367}
           6 +{"seed": 5, "n": 3, "steps": 28, "success": true, "sec": 0.47}
           7 +{"seed": 6, "n": 2, "steps": 20, "success": true, "sec": 0.268}
           8 +{"seed": 7, "n": 3, "steps": 28, "success": true, "sec": 0.368}
           9 +{"seed": 8, "n": 3, "steps": 26, "success": true, "sec": 0.445}
          10 +{"seed": 9, "n": 2, "steps": 24, "success": true, "sec": 0.376}
          11 +{"seed": 10, "n": 3, "steps": 24, "success": true, "sec": 0.418}
          12 +{"seed": 11, "n": 1, "steps": 20, "success": true, "sec": 0.298}
          13 +{"seed": 12, "n": 2, "steps": 24, "success": true, "sec": 0.393}
          14 +{"seed": 13, "n": 3, "steps": 34, "success": true, "sec": 0.569}
          15 +{"seed": 14, "n": 1, "steps": 35, "success": true, "sec": 0.375}
          16 +{"seed": 15, "n": 3, "steps": 43, "success": true, "sec": 1.772}
          17 +{"seed": 16, "n": 2, "steps": 26, "success": true, "sec": 0.64}
          18 +{"seed": 17, "n": 3, "steps": 23, "success": true, "sec": 1.01}
          19 +{"seed": 18, "n": 3, "steps": 28, "success": true, "sec": 1.241}
          20 +{"seed": 19, "n": 2, "steps": 30, "success": true, "sec": 1.264}
          21 +{"seed": 20, "n": 3, "steps": 32, "success": true, "sec": 1.291}
          22 +{"seed": 21, "n": 1, "steps": 23, "success": true, "sec": 1.0}
          23 +{"seed": 22, "n": 3, "steps": 24, "success": true, "sec": 0.598}
          24 +{"seed": 23, "n": 1, "steps": 21, "success": true, "sec": 0.917}
          25 +{"seed": 24, "n": 2, "steps": 33, "success": true, "sec": 1.391}
          26 +{"seed": 25, "n": 2, "steps": 22, "success": true, "sec": 1.078}
          27 +{"seed": 26, "n": 3, "steps": 31, "success": true, "sec": 1.303}
          28 +{"seed": 27, "n": 1, "steps": 23, "success": true, "sec": 0.821}
          29 +{"seed": 28, "n": 2, "steps": 29, "success": true, "sec": 1.273}
          30 +{"seed": 29, "n": 3, "steps": 25, "success": true, "sec": 1.208}
```

</details>

<a id="C040"></a>
### C040 · Record final 200-episode validation with all goals completed

Commit `7cc4641efbbaea1a1018677648148bb1c5023d7b`; parents: 2e4955bb60ad4b90a3b00dc94140ead360d1e995. Recorded author date: 2026-09-20T04:07:38+02:00.

File roles (automatic): setup/other.

- [E0158](01_timeline.md#E0158): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C040_7cc4641.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/final_four_check.jsonl b/final_four_check.jsonl
index 14a2d73..607c2d1 100644
--- a/final_four_check.jsonl
+++ b/final_four_check.jsonl
@@ -46,3 +46,55 @@
   46     46  {"seed": 2045, "n": 4, "steps": 27, "success": true, "sec": 0.471}
   47     47  {"seed": 2046, "n": 4, "steps": 35, "success": true, "sec": 0.69}
   48     48  {"seed": 2047, "n": 4, "steps": 30, "success": true, "sec": 1.084}
          49 +{"seed": 2048, "n": 4, "steps": 29, "success": true, "sec": 1.491}
          50 +{"seed": 2049, "n": 4, "steps": 23, "success": true, "sec": 1.037}
          51 +{"seed": 2050, "n": 4, "steps": 29, "success": true, "sec": 1.206}
          52 +{"seed": 2051, "n": 4, "steps": 30, "success": true, "sec": 1.052}
          53 +{"seed": 2052, "n": 4, "steps": 31, "success": true, "sec": 1.329}
          54 +{"seed": 2053, "n": 4, "steps": 24, "success": true, "sec": 1.146}
          55 +{"seed": 2054, "n": 4, "steps": 29, "success": true, "sec": 1.142}
          56 +{"seed": 2055, "n": 4, "steps": 27, "success": true, "sec": 1.249}
          57 +{"seed": 2056, "n": 4, "steps": 33, "success": true, "sec": 1.463}
          58 +{"seed": 2057, "n": 4, "steps": 27, "success": true, "sec": 1.212}
          59 +{"seed": 2058, "n": 4, "steps": 28, "success": true, "sec": 1.186}
          60 +{"seed": 2059, "n": 4, "steps": 32, "success": true, "sec": 1.42}
          61 +{"seed": 2060, "n": 4, "steps": 28, "success": true, "sec": 0.937}
          62 +{"seed": 2061, "n": 4, "steps": 23, "success": true, "sec": 0.805}
          63 +{"seed": 2062, "n": 4, "steps": 25, "success": true, "sec": 1.179}
          64 +{"seed": 2063, "n": 4, "steps": 32, "success": true, "sec": 1.274}
          65 +{"seed": 2064, "n": 4, "steps": 33, "success": true, "sec": 1.691}
          66 +{"seed": 2065, "n": 4, "steps": 30, "success": true, "sec": 1.27}
          67 +{"seed": 2066, "n": 4, "steps": 34, "success": true, "sec": 1.373}
          68 +{"seed": 2067, "n": 4, "steps": 24, "success": true, "sec": 1.673}
          69 +{"seed": 2068, "n": 4, "steps": 31, "success": true, "sec": 1.188}
          70 +{"seed": 2069, "n": 4, "steps": 28, "success": true, "sec": 1.594}
          71 +{"seed": 2070, "n": 4, "steps": 24, "success": true, "sec": 0.985}
          72 +{"seed": 2071, "n": 4, "steps": 36, "success": true, "sec": 1.426}
          73 +{"seed": 2072, "n": 4, "steps": 28, "success": true, "sec": 1.028}
          74 +{"seed": 2073, "n": 4, "steps": 27, "success": true, "sec": 1.029}
          75 +{"seed": 2074, "n": 4, "steps": 26, "success": true, "sec": 0.919}
          76 +{"seed": 2075, "n": 4, "steps": 28, "success": true, "sec": 1.054}
          77 +{"seed": 2076, "n": 4, "steps": 33, "success": true, "sec": 1.65}
          78 +{"seed": 2077, "n": 4, "steps": 27, "success": true, "sec": 1.076}
          79 +{"seed": 2078, "n": 4, "steps": 25, "success": true, "sec": 0.892}
          80 +{"seed": 2079, "n": 4, "steps": 31, "success": true, "sec": 1.128}
          81 +{"seed": 2080, "n": 4, "steps": 27, "success": true, "sec": 1.077}
          82 +{"seed": 2081, "n": 4, "steps": 24, "success": true, "sec": 1.107}
          83 +{"seed": 2082, "n": 4, "steps": 30, "success": true, "sec": 1.024}
          84 +{"seed": 2083, "n": 4, "steps": 26, "success": true, "sec": 0.943}
          85 +{"seed": 2084, "n": 4, "steps": 27, "success": true, "sec": 0.81}
          86 +{"seed": 2085, "n": 4, "steps": 31, "success": true, "sec": 1.507}
          87 +{"seed": 2086, "n": 4, "steps": 26, "success": true, "sec": 0.829}
          88 +{"seed": 2087, "n": 4, "steps": 27, "success": true, "sec": 1.266}
          89 +{"seed": 2088, "n": 4, "steps": 31, "success": true, "sec": 1.384}
          90 +{"seed": 2089, "n": 4, "steps": 30, "success": true, "sec": 0.921}
          91 +{"seed": 2090, "n": 4, "steps": 24, "success": true, "sec": 1.058}
          92 +{"seed": 2091, "n": 4, "steps": 27, "success": true, "sec": 0.968}
          93 +{"seed": 2092, "n": 4, "steps": 25, "success": true, "sec": 1.003}
          94 +{"seed": 2093, "n": 4, "steps": 37, "success": true, "sec": 1.814}
          95 +{"seed": 2094, "n": 4, "steps": 25, "success": true, "sec": 1.054}
          96 +{"seed": 2095, "n": 4, "steps": 28, "success": true, "sec": 1.27}
          97 +{"seed": 2096, "n": 4, "steps": 32, "success": true, "sec": 1.524}
          98 +{"seed": 2097, "n": 4, "steps": 27, "success": true, "sec": 0.82}
          99 +{"seed": 2098, "n": 4, "steps": 37, "success": true, "sec": 1.362}
         100 +{"seed": 2099, "n": 4, "steps": 29, "success": true, "sec": 1.513}
diff --git a/final_mixed_check.jsonl b/final_mixed_check.jsonl
index e69de29..4a2e679 100644
--- a/final_mixed_check.jsonl
+++ b/final_mixed_check.jsonl
@@ -0,0 +1,100 @@
           1 +{"seed": 5000, "n": 2, "steps": 20, "success": true, "sec": 0.885}
           2 +{"seed": 5001, "n": 1, "steps": 21, "success": true, "sec": 0.584}
           3 +{"seed": 5002, "n": 3, "steps": 25, "success": true, "sec": 1.107}
           4 +{"seed": 5003, "n": 1, "steps": 29, "success": true, "sec": 1.053}
           5 +{"seed": 5004, "n": 1, "steps": 29, "success": true, "sec": 1.206}
           6 +{"seed": 5005, "n": 3, "steps": 24, "success": true, "sec": 1.082}
           7 +{"seed": 5006, "n": 1, "steps": 27, "success": true, "sec": 1.126}
           8 +{"seed": 5007, "n": 2, "steps": 35, "success": true, "sec": 1.294}
           9 +{"seed": 5008, "n": 3, "steps": 32, "success": true, "sec": 1.235}
          10 +{"seed": 5009, "n": 2, "steps": 32, "success": true, "sec": 1.467}
          11 +{"seed": 5010, "n": 1, "steps": 20, "success": true, "sec": 0.542}
          12 +{"seed": 5011, "n": 1, "steps": 21, "success": true, "sec": 0.932}
          13 +{"seed": 5012, "n": 1, "steps": 29, "success": true, "sec": 1.205}
          14 +{"seed": 5013, "n": 1, "steps": 23, "success": true, "sec": 1.027}
          15 +{"seed": 5014, "n": 2, "steps": 24, "success": true, "sec": 0.933}
          16 +{"seed": 5015, "n": 3, "steps": 24, "success": true, "sec": 1.261}
          17 +{"seed": 5016, "n": 3, "steps": 25, "success": true, "sec": 1.149}
          18 +{"seed": 5017, "n": 1, "steps": 25, "success": true, "sec": 1.083}
          19 +{"seed": 5018, "n": 2, "steps": 36, "success": true, "sec": 1.392}
          20 +{"seed": 5019, "n": 1, "steps": 21, "success": true, "sec": 0.51}
          21 +{"seed": 5020, "n": 2, "steps": 22, "success": true, "sec": 1.031}
          22 +{"seed": 5021, "n": 2, "steps": 29, "success": true, "sec": 1.35}
          23 +{"seed": 5022, "n": 1, "steps": 18, "success": true, "sec": 0.93}
          24 +{"seed": 5023, "n": 1, "steps": 22, "success": true, "sec": 0.533}
          25 +{"seed": 5024, "n": 1, "steps": 20, "success": true, "sec": 0.933}
          26 +{"seed": 5025, "n": 3, "steps": 23, "success": true, "sec": 1.124}
          27 +{"seed": 5026, "n": 1, "steps": 20, "success": true, "sec": 0.407}
          28 +{"seed": 5027, "n": 2, "steps": 30, "success": true, "sec": 1.324}
          29 +{"seed": 5028, "n": 3, "steps": 26, "success": true, "sec": 1.246}
          30 +{"seed": 5029, "n": 2, "steps": 23, "success": true, "sec": 1.184}
          31 +{"seed": 5030, "n": 3, "steps": 24, "success": true, "sec": 1.082}
          32 +{"seed": 5031, "n": 3, "steps": 29, "success": true, "sec": 1.247}
          33 +{"seed": 5032, "n": 3, "steps": 28, "success": true, "sec": 1.138}
          34 +{"seed": 5033, "n": 3, "steps": 29, "success": true, "sec": 1.175}
          35 +{"seed": 5034, "n": 1, "steps": 25, "success": true, "sec": 0.622}
          36 +{"seed": 5035, "n": 3, "steps": 23, "success": true, "sec": 1.067}
          37 +{"seed": 5036, "n": 1, "steps": 26, "success": true, "sec": 0.937}
          38 +{"seed": 5037, "n": 2, "steps": 25, "success": true, "sec": 0.969}
          39 +{"seed": 5038, "n": 1, "steps": 21, "success": true, "sec": 0.966}
          40 +{"seed": 5039, "n": 3, "steps": 30, "success": true, "sec": 1.262}
          41 +{"seed": 5040, "n": 2, "steps": 29, "success": true, "sec": 1.062}
          42 +{"seed": 5041, "n": 3, "steps": 23, "success": true, "sec": 0.573}
          43 +{"seed": 5042, "n": 1, "steps": 29, "success": true, "sec": 1.074}
          44 +{"seed": 5043, "n": 2, "steps": 22, "success": true, "sec": 1.022}
          45 +{"seed": 5044, "n": 1, "steps": 32, "success": true, "sec": 0.829}
          46 +{"seed": 5045, "n": 1, "steps": 23, "success": true, "sec": 0.586}
          47 +{"seed": 5046, "n": 2, "steps": 25, "success": true, "sec": 1.027}
          48 +{"seed": 5047, "n": 1, "steps": 18, "success": true, "sec": 0.95}
          49 +{"seed": 5048, "n": 2, "steps": 29, "success": true, "sec": 1.228}
          50 +{"seed": 5049, "n": 3, "steps": 25, "success": true, "sec": 1.032}
          51 +{"seed": 5050, "n": 2, "steps": 23, "success": true, "sec": 1.116}
          52 +{"seed": 5051, "n": 1, "steps": 31, "success": true, "sec": 1.055}
          53 +{"seed": 5052, "n": 3, "steps": 23, "success": true, "sec": 0.904}
          54 +{"seed": 5053, "n": 1, "steps": 24, "success": true, "sec": 0.618}
          55 +{"seed": 5054, "n": 2, "steps": 21, "success": true, "sec": 0.982}
          56 +{"seed": 5055, "n": 2, "steps": 24, "success": true, "sec": 1.16}
          57 +{"seed": 5056, "n": 2, "steps": 22, "success": true, "sec": 1.019}
          58 +{"seed": 5057, "n": 1, "steps": 26, "success": true, "sec": 0.649}
          59 +{"seed": 5058, "n": 3, "steps": 23, "success": true, "sec": 0.942}
          60 +{"seed": 5059, "n": 3, "steps": 32, "success": true, "sec": 1.049}
          61 +{"seed": 5060, "n": 1, "steps": 20, "success": true, "sec": 0.96}
          62 +{"seed": 5061, "n": 1, "steps": 26, "success": true, "sec": 0.477}
          63 +{"seed": 5062, "n": 3, "steps": 22, "success": true, "sec": 0.42}
          64 +{"seed": 5063, "n": 3, "steps": 30, "success": true, "sec": 0.542}
          65 +{"seed": 5064, "n": 2, "steps": 22, "success": true, "sec": 0.342}
          66 +{"seed": 5065, "n": 2, "steps": 31, "success": true, "sec": 0.53}
          67 +{"seed": 5066, "n": 2, "steps": 24, "success": true, "sec": 0.286}
          68 +{"seed": 5067, "n": 2, "steps": 28, "success": true, "sec": 0.422}
          69 +{"seed": 5068, "n": 1, "steps": 24, "success": true, "sec": 0.277}
          70 +{"seed": 5069, "n": 3, "steps": 26, "success": true, "sec": 0.432}
          71 +{"seed": 5070, "n": 3, "steps": 25, "success": true, "sec": 0.419}
          72 +{"seed": 5071, "n": 1, "steps": 36, "success": true, "sec": 0.583}
          73 +{"seed": 5072, "n": 2, "steps": 23, "success": true, "sec": 0.356}
          74 +{"seed": 5073, "n": 2, "steps": 29, "success": true, "sec": 0.503}
          75 +{"seed": 5074, "n": 1, "steps": 26, "success": true, "sec": 0.44}
          76 +{"seed": 5075, "n": 2, "steps": 22, "success": true, "sec": 0.353}
          77 +{"seed": 5076, "n": 2, "steps": 28, "success": true, "sec": 0.461}
          78 +{"seed": 5077, "n": 1, "steps": 22, "success": true, "sec": 0.322}
          79 +{"seed": 5078, "n": 1, "steps": 24, "success": true, "sec": 0.37}
          80 +{"seed": 5079, "n": 2, "steps": 22, "success": true, "sec": 0.355}
          81 +{"seed": 5080, "n": 2, "steps": 26, "success": true, "sec": 0.303}
          82 +{"seed": 5081, "n": 3, "steps": 22, "success": true, "sec": 0.381}
          83 +{"seed": 5082, "n": 3, "steps": 24, "success": true, "sec": 0.421}
          84 +{"seed": 5083, "n": 1, "steps": 26, "success": true, "sec": 0.382}
          85 +{"seed": 5084, "n": 2, "steps": 26, "success": true, "sec": 0.427}
          86 +{"seed": 5085, "n": 3, "steps": 24, "success": true, "sec": 0.419}
          87 +{"seed": 5086, "n": 1, "steps": 19, "success": true, "sec": 0.222}
          88 +{"seed": 5087, "n": 1, "steps": 24, "success": true, "sec": 0.366}
          89 +{"seed": 5088, "n": 3, "steps": 21, "success": true, "sec": 0.386}
          90 +{"seed": 5089, "n": 1, "steps": 37, "success": true, "sec": 0.434}
          91 +{"seed": 5090, "n": 2, "steps": 28, "success": true, "sec": 0.463}
          92 +{"seed": 5091, "n": 1, "steps": 22, "success": true, "sec": 0.315}
          93 +{"seed": 5092, "n": 1, "steps": 18, "success": true, "sec": 0.289}
          94 +{"seed": 5093, "n": 1, "steps": 26, "success": true, "sec": 0.22}
          95 +{"seed": 5094, "n": 3, "steps": 25, "success": true, "sec": 0.407}
          96 +{"seed": 5095, "n": 1, "steps": 27, "success": true, "sec": 0.397}
          97 +{"seed": 5096, "n": 3, "steps": 27, "success": true, "sec": 0.479}
          98 +{"seed": 5097, "n": 2, "steps": 26, "success": true, "sec": 0.409}
          99 +{"seed": 5098, "n": 3, "steps": 31, "success": true, "sec": 0.477}
         100 +{"seed": 5099, "n": 2, "steps": 24, "success": true, "sec": 0.241}
diff --git a/validation_summary.json b/validation_summary.json
new file mode 100644
index 0000000..c2486fd
--- /dev/null
+++ b/validation_summary.json
@@ -0,0 +1,12 @@
           1 +{
           2 +  "episodes": 200,
           3 +  "successes": 200,
           4 +  "mean_steps": 27.01,
           5 +  "min_steps": 18,
           6 +  "max_steps": 39,
           7 +  "max_wall_seconds": 1.814,
           8 +  "result_files": [
           9 +    "final_four_check.jsonl",
          10 +    "final_mixed_check.jsonl"
          11 +  ]
          12 +}
```

</details>

