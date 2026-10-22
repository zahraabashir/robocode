# Obstruction2D · gpt-6-astra · replicate 24: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `5eb2325` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `7553b0a` | Add initial object-centric policy scaffold for grasp experiments | approach.py, probe_dynamics.py, probe_layouts.py | [E0014](01_timeline.md#E0014) |
| [C003](#C003) · `a695a4f` | Implement top-grasp transport and clear destination obstructions into free space | approach.py, probe_dynamics.py, probe_edges.py, probe_limits.py, probe_release.py, test_approach.py | [E0025](01_timeline.md#E0025) |
| [C004](#C004) · `327ced2` | Detect early vacuum attachment and keep transport base within workspace | approach.py | [E0027](01_timeline.md#E0027), [E0032](01_timeline.md#E0032) |
| [C005](#C005) · `ab62469` | Plan grasp offsets and clearing tasks with gripper and base collision clearance | approach.py, probe_failure239.py, probe_validation_60_259.jsonl, results.jsonl, rewrite_policy.py, test_counts_scene.jsonl, test_counts_scene.log, test_counts_scene.py | [E0050](01_timeline.md#E0050) |
| [C006](#C006) · `41ec7aa` | Reserve target pickup clearance when parking removed obstructions | approach.py, probe_validation_239_260_459.jsonl, results_geometry.jsonl, test_counts_scene.jsonl, test_counts_scene.log, test_counts_scene.py, test_counts_scene_v2.jsonl, test_cou… | [E0052](01_timeline.md#E0052) |
| [C007](#C007) · `56e8c6c` | Reduce transport height from observed obstacle clearance and combine safe approach motion | approach.py, probe_failure319.log, probe_failure319.py, probe_validation_239_260_459.jsonl, test_counts_scene_v2.jsonl, test_counts_scene_v2.log | [E0056](01_timeline.md#E0056) |
| [C008](#C008) · `2c8ccf9` | Keep vacuum grasp proximity clear to prevent attaching two neighboring blocks | approach.py, probe_recheck319.jsonl, probe_validation_239_260_459.jsonl, results_fast.jsonl | [E0055](01_timeline.md#E0055) |
| [C009](#C009) · `4942e85` | Distinguish existing close-packed pickup geometry from placement clearance | approach.py, probe319_fix.py, results_fast.jsonl | [E0059](01_timeline.md#E0059) |
| [C010](#C010) · `ca0e8ec` | Add reproducible count-controlled validation with policy runtime measurement | probe_final_0_499.jsonl, test_counts_scene.py, test_counts_scene_v3.jsonl, test_counts_scene_v3.log, validate.py | [E0077](01_timeline.md#E0077) |
| [C011](#C011) · `4ef204b` | Add stress probe for fixed-grasp workspace reachability | probe_final_0_499.jsonl, probe_reachability.py, test_counts_scene_v3.jsonl, test_counts_scene_v3.log, validate_count3.jsonl | [E0086](01_timeline.md#E0086) |
| [C012](#C012) · `e8ce3b8` | Clear neighboring grasp dependencies even when the obstructing block is shorter | approach.py, probe_final_0_499.jsonl, reachability.jsonl, test_counts_scene_v3.jsonl, test_counts_scene_v3.log, validate_count3.jsonl | [E0081](01_timeline.md#E0081) |
| [C013](#C013) · `ffca88e` | Protect the full target lift column and clear overhead grasp obstructions | approach.py, probe_final_0_499.jsonl, probe_grasp_offsets.py, probe_grasp_offsets_fine.py, probe_reach_edges.json, probe_reach_edges.py, reachability.jsonl, test_counts_scene_v3.j… | [E0091](01_timeline.md#E0091) |
| [C014](#C014) · `04cf477` | Use empirically verified edge grasps with one millimeter gripper overlap | approach.py, final_count3.jsonl, final_count4.jsonl, final_count4.log, final_defaults.jsonl, probe_reach_edges.json, test_counts_scene_v3.jsonl, test_counts_scene_v3.log, validate… | [E0119](01_timeline.md#E0119) |
| [C015](#C015) · `64aee98` | Use extreme edge grasps only when ordinary grasp offsets cannot reach | approach.py, final_count4.jsonl, final_defaults.jsonl | [E0121](01_timeline.md#E0121) |
| [C016](#C016) · `29518eb` | Record final regression evidence and add extreme workspace-edge search | final_count4.jsonl, final_edge_regression.jsonl, probe_count3_edges.json, probe_count3_edges.py, scan_edge_cases.py | [E0128](01_timeline.md#E0128) |
| [C017](#C017) · `71ac235` | Add tested tilted-gripper recovery for unreachable wall-side grasp configurations | approach.py, probe_angled_grasp.py, probe_angled_grasp_heights.py, scan_edge_cases.jsonl | [E0130](01_timeline.md#E0130) |
| [C018](#C018) · `93f861c` | Add reproducible forced edge-recovery regression tests | final_smoke_count3.jsonl, final_smoke_count4.jsonl, final_smoke_defaults.jsonl, test_edge_recovery.py | [E0146](01_timeline.md#E0146) |
| [C019](#C019) · `3b02891` | Document validation evidence and preserve the final tested policy | VALIDATION.md, final_forced_edges.jsonl, validation_summary.json | [E0148](01_timeline.md#E0148) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `5eb2325b23296eedbfdb58ffaeb5f963c08b5f48`; parents: none (initial snapshot). Recorded author date: 2026-09-21T13:17:17-04:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_5eb2325.diff)

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
index 0000000..865edef
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1,168 @@
           1 +{
           2 +  "host": "host.docker.internal",
           3 +  "port": 46157,
           4 +  "token": "a50e0badc8591d0e51237469ee29a874",
           5 +  "observation_space": {
           6 +    "type": "ObjectCentric",
           7 +    "types": [
           8 +      {
           9 +        "name": "crv_robot",
          10 +        "parent": null,
          11 +        "features": [
          12 +          "x",
          13 +          "y",
          14 +          "theta",
          15 +          "base_radius",
          16 +          "arm_joint",
          17 +          "arm_length",
          18 +          "vacuum",
          19 +          "gripper_height",
          20 +          "gripper_width"
          21 +        ]
          22 +      },
          23 +      {
          24 +        "name": "kinematic2d",
          25 +        "parent": null,
          26 +        "features": [
          27 +          "x",
          28 +          "y",
          29 +          "theta",
          30 +          "static",
          31 +          "color_r",
          32 +          "color_g",
          33 +          "color_b",
          34 +          "z_order"
          35 +        ]
          36 +      },
          37 +      {
          38 +        "name": "circle",
          39 +        "parent": "kinematic2d",
          40 +        "features": [
          41 +          "x",
          42 +          "y",
          43 +          "theta",
          44 +          "static",
          45 +          "color_r",
          46 +          "color_g",
          47 +          "color_b",
          48 +          "z_order",
          49 +          "radius"
          50 +        ]
          51 +      },
          52 +      {
          53 +        "name": "double_rectangle",
          54 +        "parent": "kinematic2d",
          55 +        "features": [
          56 +          "x",
          57 +          "y",
          58 +          "theta",
          59 +          "static",
          60 +          "color_r",
          61 +          "color_g",
          62 +          "color_b",
          63 +          "z_order",
          64 +          "width",
          65 +          "height",
          66 +          "x1",
          67 +          "y1",
          68 +          "theta1",
          69 +          "width1",
          70 +          "height1",
          71 +          "z_order1",
          72 +          "color_r1",
          73 +          "color_g1",
          74 +          "color_b1"
          75 +        ]
          76 +      },
          77 +      {
          78 +        "name": "lobject",
          79 +        "parent": "kinematic2d",
          80 +        "features": [
          81 +          "x",
          82 +          "y",
          83 +          "theta",
          84 +          "static",
          85 +          "color_r",
          86 +          "color_g",
          87 +          "color_b",
          88 +          "z_order",
          89 +          "width",
          90 +          "length_side1",
          91 +          "length_side2"
          92 +        ]
          93 +      },
          94 +      {
          95 +        "name": "rectangle",
          96 +        "parent": "kinematic2d",
          97 +        "features": [
          98 +          "x",
          99 +          "y",
         100 +          "theta",
         101 +          "static",
         102 +          "color_r",
         103 +          "color_g",
         104 +          "color_b",
         105 +          "z_order",
         106 +          "width",
         107 +          "height"
         108 +        ]
         109 +      },
         110 +      {
         111 +        "name": "target_block",
         112 +        "parent": "rectangle",
         113 +        "features": [
         114 +          "x",
         115 +          "y",
         116 +          "theta",
         117 +          "static",
         118 +          "color_r",
         119 +          "color_g",
         120 +          "color_b",
         121 +          "z_order",
         122 +          "width",
         123 +          "height"
         124 +        ]
         125 +      },
         126 +      {
         127 +        "name": "target_surface",
         128 +        "parent": "rectangle",
         129 +        "features": [
         130 +          "x",
         131 +          "y",
         132 +          "theta",
         133 +          "static",
         134 +          "color_r",
         135 +          "color_g",
         136 +          "color_b",
         137 +          "z_order",
         138 +          "width",
         139 +          "height"
         140 +        ]
         141 +      }
         142 +    ]
         143 +  },
         144 +  "action_space": {
         145 +    "type": "Box",
         146 +    "shape": [
         147 +      5
         148 +    ],
         149 +    "low": [
         150 +      -0.05000000074505806,
         151 +      -0.05000000074505806,
         152 +      -0.19634954631328583,
         153 +      -0.10000000149011612,
         154 +      0.0
         155 +    ],
         156 +    "high": [
         157 +      0.05000000074505806,
         158 +      0.05000000074505806,
         159 +      0.19634954631328583,
         160 +      0.10000000149011612,
         161 +      1.0
         162 +    ],
         163 +    "dtype": "float32"
         164 +  },
         165 +  "max_steps": 1000,
         166 +  "primitives": [],
         167 +  "strict": true
         168 +}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Add initial object-centric policy scaffold for grasp experiments

Commit `7553b0a83cdd8b3c2910f304522fcd648dd60faa`; parents: 5eb2325b23296eedbfdb58ffaeb5f963c08b5f48. Recorded author date: 2026-09-21T17:18:10Z.

File roles (automatic): diagnostic/test, policy.

- [E0014](01_timeline.md#E0014): commit hash in recorded output.
[Controller after this commit](evidence/versions/C002_7553b0a_approach.py) · [Exact all-file diff](evidence/diffs/C002_7553b0a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..c61ba1e
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,17 @@
           1 +import math
           2 +import numpy as np
           3 +
           4 +class GeneratedApproach:
           5 +    def __init__(self, action_space, observation_space, primitives):
           6 +        self.action_space = action_space
           7 +        self.types = {t.name: t for t in observation_space.types}
           8 +    def reset(self, state, info):
           9 +        self.phase = 0
          10 +        self.obj = None
          11 +    def get_action(self, state):
          12 +        r = next(iter(state.get_objects(self.types['crv_robot'])))
          13 +        b = next(iter(state.get_objects(self.types['target_block'])))
          14 +        x, y = state.get(r,'x'), state.get(r,'y')
          15 +        tx = state.get(b,'x') + state.get(b,'width') / 2
          16 +        ty = state.get(b,'y') + state.get(b,'height') + .3
          17 +        return np.array([np.clip(tx-x,-.05,.05),np.clip(ty-y,-.05,.05),0,0,1],dtype=np.float32)
diff --git a/probe_dynamics.py b/probe_dynamics.py
new file mode 100644
index 0000000..f22728b
--- /dev/null
+++ b/probe_dynamics.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def dump(s,e):
           5 + for name in sorted(s.get_object_names()):
           6 +  o=s.get_object_from_name(name)
           7 +  fs=e.observation_space.type_features[o.type]
           8 +  print(name, {f:round(s.get(o,f),4) for f in fs if not f.startswith('color')})
           9 +e=make_env();s,i=e.reset(seed=0); print('MAX',e.max_steps,'INFO',i);dump(s,e)
          10 +for a in [[0,0,0,0,0],[0,0,0,.1,0],[.05,0,0,0,0],[0,.05,0,0,0],[0,0,.196,0,0]]:
          11 + s,r,t,tr,i=e.step(np.array(a));print('ACTION',a,r,t,tr,i);dump(s,e)
          12 +e.close()
diff --git a/probe_layouts.py b/probe_layouts.py
new file mode 100644
index 0000000..a50427d
--- /dev/null
+++ b/probe_layouts.py
@@ -0,0 +1,9 @@
           1 +from env_client import make_env
           2 +for seed in range(6):
           3 + env=make_env(); s,_=env.reset(seed=seed)
           4 + print('SEED',seed)
           5 + for name in s.get_object_names():
           6 +  o=s.get_object_from_name(name)
           7 +  fields=['x','y','theta']+(['base_radius','arm_joint','arm_length','gripper_width','gripper_height'] if o.type.name=='crv_robot' else ['width','height','static'])
           8 +  print(name,o.type.name,{f:round(float(s.get(o,f)),4) for f in fields})
           9 + env.close()
```

</details>

<a id="C003"></a>
### C003 · Implement top-grasp transport and clear destination obstructions into free space

Commit `a695a4f577789019891b6d4b97757662a1219bf5`; parents: 7553b0a83cdd8b3c2910f304522fcd648dd60faa. Recorded author date: 2026-09-21T17:20:35Z.

File roles (automatic): diagnostic/test, policy.

- [E0025](01_timeline.md#E0025): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_a695a4f_approach.py) · [Exact all-file diff](evidence/diffs/C003_a695a4f.diff)

[Previous saved controller snapshot](evidence/versions/C002_7553b0a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c61ba1e..c2c33a1 100644
--- a/approach.py
+++ b/approach.py
@@ -5,13 +5,107 @@ class GeneratedApproach:
    5      5      def __init__(self, action_space, observation_space, primitives):
    6      6          self.action_space = action_space
    7      7          self.types = {t.name: t for t in observation_space.types}
           8 +
    8      9      def reset(self, state, info):
    9        -        self.phase = 0
   10        -        self.obj = None
   11        -    def get_action(self, state):
   12        -        r = next(iter(state.get_objects(self.types['crv_robot'])))
   13        -        b = next(iter(state.get_objects(self.types['target_block'])))
   14        -        x, y = state.get(r,'x'), state.get(r,'y')
   15        -        tx = state.get(b,'x') + state.get(b,'width') / 2
   16        -        ty = state.get(b,'y') + state.get(b,'height') + .3
   17        -        return np.array([np.clip(tx-x,-.05,.05),np.clip(ty-y,-.05,.05),0,0,1],dtype=np.float32)
          10 +        self.robot = next(iter(state.get_objects(self.types['crv_robot'])))
          11 +        self.block = next(iter(state.get_objects(self.types['target_block'])))
          12 +        self.surface = next(iter(state.get_objects(self.types['target_surface'])))
          13 +        self.phase = 'choose'
          14 +        self.task = None
          15 +        self.steps = 0
          16 +        self.stuck = 0
          17 +        self.last = None
          18 +
          19 +    def rect(self, s, o):
          20 +        return [float(s.get(o,f)) for f in ('x','y','width','height')]
          21 +
          22 +    def obstacles(self,s):
          23 +        return [o for o in s.get_objects(self.types['rectangle']) if o != self.surface and o != self.block and not s.get(o,'static')]
          24 +
          25 +    def select(self,s):
          26 +        bx,by,bw,bh=self.rect(s,self.block)
          27 +        sx,sy,sw,sh=self.rect(s,self.surface)
          28 +        obs=self.obstacles(s)
          29 +        lo,hi=sx+.002,sx+sw-bw-.002
          30 +        candidates=[lo,hi,(lo+hi)/2]
          31 +        for o in obs:
          32 +            x,y,w,h=self.rect(s,o)
          33 +            candidates += [max(lo,min(hi,x-bw-.006)),max(lo,min(hi,x+w+.006))]
          34 +        def blockers(x):
          35 +            return [o for o in obs if self.rect(s,o)[0]<x+bw+.004 and self.rect(s,o)[0]+self.rect(s,o)[2]>x-.004 and self.rect(s,o)[1]<sy+sh+bh+.01]
          36 +        gx=min(candidates,key=lambda x:(len(blockers(x)),abs(x-bx)))
          37 +        self.goal=(gx,sy+sh+.005)
          38 +        blocking=blockers(gx)
          39 +        if blocking:
          40 +            o=max(blocking,key=lambda o:self.rect(s,o)[1]+self.rect(s,o)[3])
          41 +            x,y,w,h=self.rect(s,o)
          42 +            occupied=[self.rect(s,p) for p in obs+[self.block] if p!=o]
          43 +            occupied.append([gx,sy+sh,bw,bh])
          44 +            places=[]
          45 +            for px in np.linspace(.012,1.606-w,90):
          46 +                py=.105
          47 +                for qx,qy,qw,qh in occupied:
          48 +                    if px<qx+qw+.018 and px+w>qx-.018:
          49 +                        py=max(py,qy+qh+.02)
          50 +                if py+h<.48 and not (px<gx+bw+.12 and px+w>gx-.12):
          51 +                    places.append((py*8+abs(px-x),float(px),py))
          52 +            if not places:
          53 +                for px in np.linspace(.012,1.606-w,90):
          54 +                    if px<gx+bw+.04 and px+w>gx-.04: continue
          55 +                    py=max([.105]+[qy+qh+.02 for qx,qy,qw,qh in occupied if px<qx+qw+.01 and px+w>qx-.01])
          56 +                    places.append((py*8+abs(px-x),float(px),py))
          57 +            if places:
          58 +                _,px,py=min(places)
          59 +                self.dest=(px,py)
          60 +            else:self.dest=(max(.01,gx-w-.05),.35)
          61 +        else:
          62 +            o=self.block
          63 +            self.dest=self.goal
          64 +        self.task=o
          65 +        x,y,w,h=self.rect(s,o)
          66 +        self.pickx=max(.105,min(1.513,x+w/2))
          67 +        self.offsetx=self.pickx-x
          68 +        self.picktop=y+h
          69 +        self.phase='above'
          70 +        self.stuck=0
          71 +
          72 +    def get_action(self, s):
          73 +        self.steps+=1
          74 +        r=self.robot
          75 +        rx,ry=float(s.get(r,'x')),float(s.get(r,'y'))
          76 +        theta=float(s.get(r,'theta'))
          77 +        arm=float(s.get(r,'arm_joint'))
          78 +        if self.phase=='choose':self.select(s)
          79 +        x,y,w,h=self.rect(s,self.task)
          80 +        vac=0.
          81 +        tx,ty=rx,ry
          82 +        if self.phase=='above':
          83 +            ty=.86
          84 +            if abs(ry-ty)<.002:
          85 +                tx=self.pickx
          86 +                if abs(rx-tx)<.002:self.phase='down'
          87 +        if self.phase=='down':
          88 +            tx=self.pickx;ty=self.picktop+.215;vac=1.
          89 +            if abs(rx-tx)<.002 and abs(ry-ty)<.002:
          90 +                self.phase='lift';self.before_y=y
          91 +        elif self.phase=='lift':
          92 +            vac=1.;ty=.86
          93 +            if y>self.before_y+.025:
          94 +                self.offsetx=rx-x;self.offsety=ry-y
          95 +            if abs(ry-ty)<.002:
          96 +                if y<self.before_y+.025:
          97 +                    self.phase='down';self.picktop-=.005
          98 +                else:self.phase='carry'
          99 +        elif self.phase=='carry':
         100 +            vac=1.;ty=.86;tx=self.dest[0]+self.offsetx
         101 +            if abs(rx-tx)<.002:self.phase='place'
         102 +        elif self.phase=='place':
         103 +            vac=1.;tx=self.dest[0]+self.offsetx;ty=self.dest[1]+self.offsety
         104 +            if abs(rx-tx)<.002 and abs(ry-ty)<.002:self.phase='release'
         105 +        elif self.phase=='release':
         106 +            vac=0.;self.phase='retreat'
         107 +        elif self.phase=='retreat':
         108 +            ty=.86
         109 +            if abs(ry-ty)<.002:self.phase='choose'
         110 +        delta=np.array([tx-rx,ty-ry,(-math.pi/2-theta+math.pi)%(2*math.pi)-math.pi,.2-arm,vac])
         111 +        return np.clip(delta,self.action_space.low,self.action_space.high).astype(np.float32)
diff --git a/probe_dynamics.py b/probe_dynamics.py
index f22728b..c1630d8 100644
--- a/probe_dynamics.py
+++ b/probe_dynamics.py
@@ -1,12 +1,22 @@
    1      1  from env_client import make_env
    2      2  import numpy as np
    3      3  
    4        -def dump(s,e):
    5        - for name in sorted(s.get_object_names()):
    6        -  o=s.get_object_from_name(name)
    7        -  fs=e.observation_space.type_features[o.type]
    8        -  print(name, {f:round(s.get(o,f),4) for f in fs if not f.startswith('color')})
    9        -e=make_env();s,i=e.reset(seed=0); print('MAX',e.max_steps,'INFO',i);dump(s,e)
   10        -for a in [[0,0,0,0,0],[0,0,0,.1,0],[.05,0,0,0,0],[0,.05,0,0,0],[0,0,.196,0,0]]:
   11        - s,r,t,tr,i=e.step(np.array(a));print('ACTION',a,r,t,tr,i);dump(s,e)
   12        -e.close()
           4 +def experiment(joint,epsilon,release=False):
           5 + e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           6 + def step(a):
           7 +  nonlocal s
           8 +  s,re,t,tr,i=e.step(np.array(a,dtype=np.float32));return t
           9 + x=s.get(b,'x')+s.get(b,'width')/2;top=s.get(b,'y')+s.get(b,'height'); y=top+joint+epsilon
          10 + for k in range(30):
          11 +  step([np.clip(x-s.get(r,'x'),-.05,.05),np.clip(y-s.get(r,'y'),-.05,.05),0,np.clip(joint-s.get(r,'arm_joint'),-.1,.1),1])
          12 + by=s.get(b,'y');ry=s.get(r,'y');step([0,.05,0,0,1]);dy=s.get(b,'y')-by
          13 + print('joint eps',joint,epsilon,'base_y',round(ry,5),'offset',round(ry-top,5),'grasp',round(dy,5))
          14 + if release:
          15 +  for k in range(5):step([0,.05,0,0,1])
          16 +  print('lift',s.get(b,'y'));step([0,0,0,0,0]);print('release',s.get(b,'y'))
          17 +  for k in range(5):step([0,0,0,0,0])
          18 +  print('after5',s.get(b,'y'))
          19 + e.close()
          20 +for joint in [.1,.2]:
          21 + for epsilon in [0,.005,.009,.01,.011,.015,.02,.03]:experiment(joint,epsilon)
          22 +experiment(.2,.01,True)
diff --git a/probe_edges.py b/probe_edges.py
new file mode 100644
index 0000000..f264a00
--- /dev/null
+++ b/probe_edges.py
@@ -0,0 +1,18 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +ext=[]
           4 +for seed in range(60):
           5 + e=make_env();s,i=e.reset(seed=seed)
           6 + for typ in ['rectangle','target_block']:
           7 +  for o in s.get_objects(e.observation_space.get_type(typ)):
           8 +   x=s.get(o,'x');w=s.get(o,'width')
           9 +   if x+w/2<.1 or x+w/2>1.518:ext.append((seed,o.name,x,w,s.get(o,'y'),s.get(o,'height')))
          10 + e.close()
          11 +print('extreme',ext[:15], 'count',len(ext))
          12 +for seed,name,x,w,y,h in ext[:8]:
          13 + e=make_env();s,i=e.reset(seed=seed);r=s.get_object_from_name('robot');b=s.get_object_from_name(name)
          14 + bx=np.clip(x+w/2,.1001,1.5179);by=y+h+.22
          15 + for j in range(40):s,*_=e.step(np.array([np.clip(bx-s.get(r,'x'),-.05,.05),np.clip(by-s.get(r,'y'),-.05,.05),0,.1,1],dtype=np.float32))
          16 + orig=s.get(b,'y');s,*_=e.step(np.array([0,.05,0,0,1],dtype=np.float32))
          17 + print(seed,name,'objx',x,'w',w,'bx',bx,'basex',s.get(r,'x'),'delta_y',s.get(b,'y')-orig)
          18 + e.close()
diff --git a/probe_limits.py b/probe_limits.py
new file mode 100644
index 0000000..8ae0999
--- /dev/null
+++ b/probe_limits.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +for feature,index,d in [('x',0,-.05),('x',0,.05),('y',1,.05)]:
           4 + e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot')
           5 + for delta in [d,d/10,d/100,d/1000]:
           6 +  for j in range(40):
           7 +   a=np.zeros(5,dtype=np.float32);a[index]=delta;s,*_=e.step(a)
           8 + print('base bound',feature,d,s.get(r,feature));e.close()
           9 +for dy in [-.05,-.01]:
          10 + e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
          11 + x=s.get(b,'x')+s.get(b,'width')/2
          12 + for j in range(10):s,*_=e.step(np.array([np.clip(x-s.get(r,'x'),-.05,.05),0,0,.1,0],dtype=np.float32))
          13 + for j in range(100):s,*_=e.step(np.array([0,dy,0,0,1],dtype=np.float32))
          14 + by=s.get(b,'y');ry=s.get(r,'y');s,*_=e.step(np.array([0,.05,0,0,1],dtype=np.float32))
          15 + print('descend',dy,'stopped',ry,'target_top',by+s.get(b,'height'),'grasp_dy',s.get(b,'y')-by);e.close()
diff --git a/probe_release.py b/probe_release.py
new file mode 100644
index 0000000..d47e87b
--- /dev/null
+++ b/probe_release.py
@@ -0,0 +1,30 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +def run(release):
           5 + e=make_env();s,_=e.reset(seed=0);r=s.get_object_from_name('robot');o=s.get_object_from_name('obstruction1')
           6 + def step(a):
           7 +  nonlocal s
           8 +  s,_,_,_,_=e.step(np.array(a,dtype=np.float32))
           9 + def pos(): return [round(s.get(z,f),4) for z in [r,o] for f in ['x','y']]
          10 + def move(x,y,v=1):
          11 +  for _ in range(100):
          12 +   dx=x-s.get(r,'x');dy=y-s.get(r,'y')
          13 +   if max(abs(dx),abs(dy))<1e-5:break
          14 +   old=pos();step([np.clip(dx,-.05,.05),np.clip(dy,-.05,.05),0,0,v])
          15 +   if pos()==old:break
          16 + x=s.get(o,'x')+s.get(o,'width')/2
          17 + step([0,0,0,.1,0])
          18 + move(x,s.get(r,'y'),0)
          19 + move(x,s.get(o,'y')+s.get(o,'height')+.205)
          20 + print('CONTACT',pos(),'arm',s.get(r,'arm_joint'))
          21 + move(x,s.get(r,'y')+.2)
          22 + print('LIFT',pos())
          23 + if release:
          24 +  step([0,0,0,0,0]); print('RELEASE',pos())
          25 +  for i in range(4):step([-.05,0,0,0,0]);print('AFTER',i,pos())
          26 + else:
          27 +  move(.85,s.get(r,'y')); move(.85,.4963); print('LOWER_ON_OBSTACLE',pos()); move(.85,.6963); move(1.8,s.get(r,'y'));print('RIGHT_BOUND',pos())
          28 +  for i in range(5):step([.05,0,0,0,1]);print('RIGHT_MORE',pos())
          29 + e.close()
          30 +run(True);run(False)
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..29f99e0
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import sys,time,json
           4 +seeds=[int(x) for x in sys.argv[1:]] or list(range(20))
           5 +for seed in seeds:
           6 + e=make_env();s,i=e.reset(seed=seed);a=GeneratedApproach(e.action_space,e.observation_space,{ });a.reset(s,i);start=time.time()
           7 + last=None;stuck=0
           8 + for n in range(e.max_steps):
           9 +  act=a.get_action(s);s,r,t,tr,info=e.step(act)
          10 +  sig=(a.phase,tuple(s.get(a.robot,f) for f in ('x','y')),tuple(s.get(a.task,f) for f in ('x','y')))
          11 +  stuck=stuck+1 if sig==last else 0;last=sig
          12 +  if t or tr or stuck>35:break
          13 + print(json.dumps({'seed':seed,'success':t,'steps':n+1,'seconds':round(time.time()-start,2),'phase':a.phase,'task':a.task.name,'robot':[s.get(a.robot,f) for f in ('x','y')],'taskxy':[s.get(a.task,f) for f in ('x','y')],'dest':a.dest}),flush=True)
          14 + e.close()
```

</details>

<a id="C004"></a>
### C004 · Detect early vacuum attachment and keep transport base within workspace

Commit `327ced2e64eb5bc6485e9474c9c502c7c4b3a7f4`; parents: a695a4f577789019891b6d4b97757662a1219bf5. Recorded author date: 2026-09-21T17:21:32Z.

File roles (automatic): policy.

- [E0027](01_timeline.md#E0027): commit title in command; output may not confirm creation.
- [E0032](01_timeline.md#E0032): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_327ced2_approach.py) · [Exact all-file diff](evidence/diffs/C004_327ced2.diff)

[Previous saved controller snapshot](evidence/versions/C003_a695a4f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c2c33a1..2a2bc7b 100644
--- a/approach.py
+++ b/approach.py
@@ -42,7 +42,7 @@ class GeneratedApproach:
   42     42              occupied=[self.rect(s,p) for p in obs+[self.block] if p!=o]
   43     43              occupied.append([gx,sy+sh,bw,bh])
   44     44              places=[]
   45        -            for px in np.linspace(.012,1.606-w,90):
          45 +            for px in np.linspace(.11,1.50-w,90):
   46     46                  py=.105
   47     47                  for qx,qy,qw,qh in occupied:
   48     48                      if px<qx+qw+.018 and px+w>qx-.018:
@@ -50,7 +50,7 @@ class GeneratedApproach:
   50     50                  if py+h<.48 and not (px<gx+bw+.12 and px+w>gx-.12):
   51     51                      places.append((py*8+abs(px-x),float(px),py))
   52     52              if not places:
   53        -                for px in np.linspace(.012,1.606-w,90):
          53 +                for px in np.linspace(.11,1.50-w,90):
   54     54                      if px<gx+bw+.04 and px+w>gx-.04: continue
   55     55                      py=max([.105]+[qy+qh+.02 for qx,qy,qw,qh in occupied if px<qx+qw+.01 and px+w>qx-.01])
   56     56                      places.append((py*8+abs(px-x),float(px),py))
@@ -63,7 +63,10 @@ class GeneratedApproach:
   63     63              self.dest=self.goal
   64     64          self.task=o
   65     65          x,y,w,h=self.rect(s,o)
   66        -        self.pickx=max(.105,min(1.513,x+w/2))
          66 +        lower=max(.1002-x,.1002-self.dest[0],-.025)
          67 +        upper=min(1.5178-x,1.5178-self.dest[0],w+.025)
          68 +        offset=max(lower,min(upper,w/2))
          69 +        self.pickx=max(.1002,min(1.5178,x+offset))
   67     70          self.offsetx=self.pickx-x
   68     71          self.picktop=y+h
   69     72          self.phase='above'
@@ -75,6 +78,10 @@ class GeneratedApproach:
   75     78          rx,ry=float(s.get(r,'x')),float(s.get(r,'y'))
   76     79          theta=float(s.get(r,'theta'))
   77     80          arm=float(s.get(r,'arm_joint'))
          81 +        pose=(rx,ry)
          82 +        oldphase=self.phase
          83 +        self.stuck=self.stuck+1 if self.last==(pose,oldphase) else 0
          84 +        self.last=(pose,oldphase)
   78     85          if self.phase=='choose':self.select(s)
   79     86          x,y,w,h=self.rect(s,self.task)
   80     87          vac=0.
@@ -86,7 +93,7 @@ class GeneratedApproach:
   86     93                  if abs(rx-tx)<.002:self.phase='down'
   87     94          if self.phase=='down':
   88     95              tx=self.pickx;ty=self.picktop+.215;vac=1.
   89        -            if abs(rx-tx)<.002 and abs(ry-ty)<.002:
          96 +            if (abs(rx-tx)<.002 and abs(ry-ty)<.002) or self.stuck>=2:
   90     97                  self.phase='lift';self.before_y=y
   91     98          elif self.phase=='lift':
   92     99              vac=1.;ty=.86
```

</details>

<a id="C005"></a>
### C005 · Plan grasp offsets and clearing tasks with gripper and base collision clearance

Commit `ab62469ecce03eeee0f7ececba4deeb569f06baf`; parents: 327ced2e64eb5bc6485e9474c9c502c7c4b3a7f4. Recorded author date: 2026-09-21T17:24:59Z.

File roles (automatic): diagnostic/test, policy, setup/other, support code (role needs review).

- [E0050](01_timeline.md#E0050): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C005_ab62469_approach.py) · [Exact all-file diff](evidence/diffs/C005_ab62469.diff)

[Previous saved controller snapshot](evidence/versions/C004_327ced2_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 2a2bc7b..71860bb 100644
--- a/approach.py
+++ b/approach.py
@@ -22,6 +22,30 @@ class GeneratedApproach:
   22     22      def obstacles(self,s):
   23     23          return [o for o in s.get_objects(self.types['rectangle']) if o != self.surface and o != self.block and not s.get(o,'static')]
   24     24  
          25 +    @staticmethod
          26 +    def overlap(a,b,margin=.003):
          27 +        return a[0]<b[0]+b[2]+margin and a[0]+a[2]>b[0]-margin and a[1]<b[1]+b[3]+margin and a[1]+a[3]>b[1]-margin
          28 +
          29 +    def conflicts(self,s,obj,x,y,offset,others):
          30 +        _,_,w,h=self.rect(s,obj)
          31 +        rx=x+offset;ry=y+h+.215
          32 +        gripper=(rx-.035,ry-.21,.07,.01)
          33 +        arm=(rx-.008,ry-.2,.016,.2)
          34 +        bad=[]
          35 +        for o in others:
          36 +            q=self.rect(s,o)
          37 +            dx=max(q[0]-rx,0,rx-q[0]-q[2])
          38 +            dy=max(q[1]-ry,0,ry-q[1]-q[3])
          39 +            if self.overlap((x,y,w,h),q) or self.overlap(gripper,q) or self.overlap(arm,q) or dx*dx+dy*dy<.103**2:
          40 +                bad.append(o)
          41 +        return bad
          42 +
          43 +    def offsets(self,x,px,w):
          44 +        low=max(.1002-x,.1002-px,-.022)
          45 +        high=min(1.5178-x,1.5178-px,w+.022)
          46 +        if low>high:return []
          47 +        return sorted(set([max(low,min(high,w/2))]+[float(z) for z in np.linspace(low,high,7)]),key=lambda z:abs(z-w/2))
          48 +
   25     49      def select(self,s):
   26     50          bx,by,bw,bh=self.rect(s,self.block)
   27     51          sx,sy,sw,sh=self.rect(s,self.surface)
@@ -30,42 +54,62 @@ class GeneratedApproach:
   30     54          candidates=[lo,hi,(lo+hi)/2]
   31     55          for o in obs:
   32     56              x,y,w,h=self.rect(s,o)
   33        -            candidates += [max(lo,min(hi,x-bw-.006)),max(lo,min(hi,x+w+.006))]
   34        -        def blockers(x):
   35        -            return [o for o in obs if self.rect(s,o)[0]<x+bw+.004 and self.rect(s,o)[0]+self.rect(s,o)[2]>x-.004 and self.rect(s,o)[1]<sy+sh+bh+.01]
   36        -        gx=min(candidates,key=lambda x:(len(blockers(x)),abs(x-bx)))
          57 +            candidates += [max(lo,min(hi,x-bw-.007)),max(lo,min(hi,x+w+.007))]
          58 +        plans=[]
          59 +        for gx in candidates:
          60 +            for offset in self.offsets(bx,gx,bw):
          61 +                bad=set(self.conflicts(s,self.block,gx,sy+sh+.005,offset,obs)+self.conflicts(s,self.block,bx,by,offset,obs))
          62 +                plans.append(((len(bad),abs(offset-bw/2)*.2+abs(gx-bx)*.01),gx,offset,bad))
          63 +        if not plans:
          64 +            gx=(lo+hi)/2;offset=max(.1002-bx,min(1.5178-gx,bw/2))
          65 +            plans=[((len(obs),0),gx,offset,set(obs))]
          66 +        _,gx,offset,bad=min(plans,key=lambda p:p[0])
   37     67          self.goal=(gx,sy+sh+.005)
   38        -        blocking=blockers(gx)
   39        -        if blocking:
   40        -            o=max(blocking,key=lambda o:self.rect(s,o)[1]+self.rect(s,o)[3])
          68 +        if not bad:
          69 +            o=self.block;self.dest=self.goal
          70 +        else:
          71 +            o=max(bad,key=lambda p:self.rect(s,p)[1]+self.rect(s,p)[3])
          72 +            # A taller neighbour may block the selected object's top grasp.
          73 +            for _ in range(len(obs)+1):
          74 +                x,y,w,h=self.rect(s,o)
          75 +                others=[p for p in obs+[self.block] if p!=o]
          76 +                grasps=[]
          77 +                for off in self.offsets(x,x,w):
          78 +                    blocking=self.conflicts(s,o,x,y,off,others)
          79 +                    grasps.append((len(blocking),abs(off-w/2),off,blocking))
          80 +                best=min(grasps,key=lambda z:z[:2])
          81 +                if not best[0]:break
          82 +                taller=[p for p in best[3] if self.rect(s,p)[1]+self.rect(s,p)[3]>y+h+.001 and p!=self.block]
          83 +                if not taller:break
          84 +                o=max(taller,key=lambda p:self.rect(s,p)[1]+self.rect(s,p)[3])
   41     85              x,y,w,h=self.rect(s,o)
   42        -            occupied=[self.rect(s,p) for p in obs+[self.block] if p!=o]
   43        -            occupied.append([gx,sy+sh,bw,bh])
          86 +            others=[p for p in obs+[self.block] if p!=o]
          87 +            occupied=[self.rect(s,p) for p in others]
   44     88              places=[]
   45        -            for px in np.linspace(.11,1.50-w,90):
   46        -                py=.105
   47        -                for qx,qy,qw,qh in occupied:
   48        -                    if px<qx+qw+.018 and px+w>qx-.018:
   49        -                        py=max(py,qy+qh+.02)
   50        -                if py+h<.48 and not (px<gx+bw+.12 and px+w>gx-.12):
   51        -                    places.append((py*8+abs(px-x),float(px),py))
   52        -            if not places:
   53        -                for px in np.linspace(.11,1.50-w,90):
   54        -                    if px<gx+bw+.04 and px+w>gx-.04: continue
   55        -                    py=max([.105]+[qy+qh+.02 for qx,qy,qw,qh in occupied if px<qx+qw+.01 and px+w>qx-.01])
   56        -                    places.append((py*8+abs(px-x),float(px),py))
          89 +            for px in np.linspace(.105,1.513-w,75):
          90 +                if px<gx+bw+.13 and px+w>gx-.13:continue
          91 +                py=max([.105]+[qy+qh+.022 for qx,qy,qw,qh in occupied if px<qx+qw+.025 and px+w>qx-.025])
          92 +                if py+h>.43:continue
          93 +                for off in self.offsets(x,px,w):
          94 +                    blockers=self.conflicts(s,o,x,y,off,others)+self.conflicts(s,o,px,py,off,others)
          95 +                    if not blockers:
          96 +                        places.append((py*8+abs(px-x)+abs(off-w/2)*.2,float(px),py,off))
   57     97              if places:
   58        -                _,px,py=min(places)
          98 +                _,px,py,offset=min(places)
          99 +                self.dest=(px,py)
         100 +            else:
         101 +                # If floor space is scarce, park above the lowest nearby stack.
         102 +                fallback=[]
         103 +                for px in np.linspace(.105,1.513-w,75):
         104 +                    if px<gx+bw+.07 and px+w>gx-.07:continue
         105 +                    py=max([.105]+[qy+qh+.025 for qx,qy,qw,qh in occupied if px<qx+qw+.04 and px+w>qx-.04])
         106 +                    for off in self.offsets(x,px,w):
         107 +                        blockers=self.conflicts(s,o,x,y,off,others)+self.conflicts(s,o,px,py,off,others)
         108 +                        fallback.append((len(blockers),py*8+abs(px-x),float(px),py,off))
         109 +                _,_,px,py,offset=min(fallback)
   59    110                  self.dest=(px,py)
   60        -            else:self.dest=(max(.01,gx-w-.05),.35)
   61        -        else:
   62        -            o=self.block
   63        -            self.dest=self.goal
   64    111          self.task=o
   65    112          x,y,w,h=self.rect(s,o)
   66        -        lower=max(.1002-x,.1002-self.dest[0],-.025)
   67        -        upper=min(1.5178-x,1.5178-self.dest[0],w+.025)
   68        -        offset=max(lower,min(upper,w/2))
   69    113          self.pickx=max(.1002,min(1.5178,x+offset))
   70    114          self.offsetx=self.pickx-x
   71    115          self.picktop=y+h
@@ -92,9 +136,9 @@ class GeneratedApproach:
   92    136                  tx=self.pickx
   93    137                  if abs(rx-tx)<.002:self.phase='down'
   94    138          if self.phase=='down':
   95        -            tx=self.pickx;ty=self.picktop+.215;vac=1.
         139 +            tx=self.pickx;ty=self.picktop+.215;vac=0.
   96    140              if (abs(rx-tx)<.002 and abs(ry-ty)<.002) or self.stuck>=2:
   97        -                self.phase='lift';self.before_y=y
         141 +                self.phase='lift';self.before_y=y;vac=1.
   98    142          elif self.phase=='lift':
   99    143              vac=1.;ty=.86
  100    144              if y>self.before_y+.025:
diff --git a/probe_failure239.py b/probe_failure239.py
new file mode 100644
index 0000000..9a7892b
--- /dev/null
+++ b/probe_failure239.py
@@ -0,0 +1,16 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import json
           4 +E=make_env();s,i=E.reset(seed=239);a=GeneratedApproach(E.action_space,E.observation_space,{});a.reset(s,i)
           5 +def dump(s):
           6 + for n in sorted(s.get_object_names()):
           7 +  o=s.get_object_from_name(n)
           8 +  fs=['x','y','theta'] if n=='robot' else ['x','y','width','height']
           9 +  print(n,[round(s.get(o,f),6) for f in fs])
          10 +print('INITIAL',i);dump(s);prev=None
          11 +for step in range(250):
          12 + act=a.get_action(s);s,r,t,tr,_=E.step(act)
          13 + sig=(a.phase,a.task.name,a.dest)
          14 + if sig!=prev:print(step,sig,'robot',[round(s.get(a.robot,f),6) for f in ['x','y']],'task',[round(s.get(a.task,f),6) for f in ['x','y']]);prev=sig
          15 + if t:print('SUCCESS',step);break
          16 +print('FINAL');dump(s);E.close()
diff --git a/probe_validation_60_259.jsonl b/probe_validation_60_259.jsonl
new file mode 100644
index 0000000..2b0516d
--- /dev/null
+++ b/probe_validation_60_259.jsonl
@@ -0,0 +1,200 @@
           1 +{"seed": 60, "success": true, "steps": 44, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.6079647541046143, 0.38666898012161255], "taskxy": [0.5506206154823303, 0.10499999672174454], "dest": [0.5506205822825432, 0.10500000149011612]}
           2 +{"seed": 61, "success": true, "steps": 109, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.5086811184883118, 0.5149990320205688], "taskxy": [0.4088241457939148, 0.10500001907348633], "dest": [0.4088242094516754, 0.10500000149011612]}
           3 +{"seed": 62, "success": true, "steps": 109, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [1.3378403186798096, 0.5099999904632568], "taskxy": [1.2743176221847534, 0.11390747129917145], "dest": [1.2743177671432495, 0.10500000149011612]}
           4 +{"seed": 63, "success": true, "steps": 90, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [0.7719019651412964, 0.41499897837638855], "taskxy": [0.7193304300308228, 0.10499998182058334], "dest": [0.719330501139164, 0.10500000149011612]}
           5 +{"seed": 64, "success": true, "steps": 49, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.4470421075820923, 0.4649990200996399], "taskxy": [0.3481397032737732, 0.10500004142522812], "dest": [0.34813969242572784, 0.10500000149011612]}
           6 +{"seed": 65, "success": true, "steps": 43, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.3692214787006378, 0.37646761536598206], "taskxy": [0.32330766320228577, 0.10499998927116394], "dest": [0.3233076523542404, 0.10500000149011612]}
           7 +{"seed": 66, "success": true, "steps": 105, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [1.208558440208435, 0.4599999785423279], "taskxy": [1.123029351234436, 0.10559123754501343], "dest": [1.1230293552875519, 0.10500000149011612]}
           8 +{"seed": 67, "success": true, "steps": 100, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.2920019328594208, 0.42329514026641846], "taskxy": [0.24387985467910767, 0.10500002652406693], "dest": [0.2438798885345459, 0.10500000149011612]}
           9 +{"seed": 68, "success": true, "steps": 103, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [0.46296456456184387, 0.3822042942047119], "taskxy": [0.39746949076652527, 0.10499998182058334], "dest": [0.3974694867134094, 0.10500000149011612]}
          10 +{"seed": 69, "success": true, "steps": 57, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [0.21700942516326904, 0.43561235070228577], "taskxy": [0.15116183459758759, 0.10499999672174454], "dest": [0.15116179394721985, 0.10500000149011612]}
          11 +{"seed": 70, "success": true, "steps": 110, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [1.2810150384902954, 0.3704374134540558], "taskxy": [1.2404485940933228, 0.10499993711709976], "dest": [1.2404485832452774, 0.10500000149011612]}
          12 +{"seed": 71, "success": true, "steps": 99, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [1.0334404706954956, 0.4099999666213989], "taskxy": [0.9692030549049377, 0.11478820443153381], "dest": [0.969202939748764, 0.10500000149011612]}
          13 +{"seed": 72, "success": true, "steps": 144, "seconds": 0.43, "phase": "place", "task": "target_block", "robot": [0.2402489185333252, 0.4099999964237213], "taskxy": [0.19537505507469177, 0.11010850965976715], "dest": [0.1953750963807106, 0.10500000149011612]}
          14 +{"seed": 73, "success": true, "steps": 101, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [1.1164096593856812, 0.4099999964237213], "taskxy": [1.034185528755188, 0.12183128297328949], "dest": [1.034185673713684, 0.10500000149011612]}
          15 +{"seed": 74, "success": true, "steps": 43, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [1.5013699531555176, 0.48225638270378113], "taskxy": [1.4760719537734985, 0.10500004142522812], "dest": [1.4760720987319946, 0.10500000149011612]}
          16 +{"seed": 75, "success": true, "steps": 117, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [1.4256354570388794, 0.5149989724159241], "taskxy": [1.3311207294464111, 0.10500001162290573], "dest": [1.3311206359863281, 0.10500000149011612]}
          17 +{"seed": 76, "success": true, "steps": 41, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.5033426880836487, 0.515011727809906], "taskxy": [0.43621283769607544, 0.10500000417232513], "dest": [0.4362128417491913, 0.10500000149011612]}
          18 +{"seed": 77, "success": true, "steps": 48, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.7169095873832703, 0.3836202621459961], "taskxy": [0.6318119764328003, 0.10500001907348633], "dest": [0.6318120617866516, 0.10500000149011612]}
          19 +{"seed": 78, "success": true, "steps": 164, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [0.6102669835090637, 0.4099999666213989], "taskxy": [0.5429974794387817, 0.10633157193660736], "dest": [0.5429975051879883, 0.10500000149011612]}
          20 +{"seed": 79, "success": true, "steps": 58, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [0.3093271553516388, 0.4262493848800659], "taskxy": [0.24849961698055267, 0.10499997437000275], "dest": [0.24849958312511444, 0.10500000149011612]}
          21 +{"seed": 80, "success": true, "steps": 109, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.38471463322639465, 0.43649914860725403], "taskxy": [0.30512362718582153, 0.10499994456768036], "dest": [0.30512363463640213, 0.10500000149011612]}
          22 +{"seed": 81, "success": true, "steps": 50, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [0.5939594507217407, 0.3846059739589691], "taskxy": [0.5340566039085388, 0.10500001907348633], "dest": [0.5340565558075905, 0.10500000149011612]}
          23 +{"seed": 82, "success": true, "steps": 51, "seconds": 0.17, "phase": "place", "task": "target_block", "robot": [1.2749502658843994, 0.4599999785423279], "taskxy": [1.2143901586532593, 0.12408500909805298], "dest": [1.2143901762962341, 0.10500000149011612]}
          24 +{"seed": 83, "success": true, "steps": 170, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [0.25152280926704407, 0.5099999904632568], "taskxy": [0.16700731217861176, 0.1118953749537468], "dest": [0.1670072864294052, 0.10500000149011612]}
          25 +{"seed": 84, "success": true, "steps": 118, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [0.6042965054512024, 0.41499897837638855], "taskxy": [0.5306368470191956, 0.10499996691942215], "dest": [0.530636821269989, 0.10500000149011612]}
          26 +{"seed": 85, "success": true, "steps": 101, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.9010718464851379, 0.3812885582447052], "taskxy": [0.8189694881439209, 0.10499999672174454], "dest": [0.8189695138931274, 0.10500000149011612]}
          27 +{"seed": 86, "success": true, "steps": 90, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.7719181180000305, 0.3897438645362854], "taskxy": [0.6749577522277832, 0.10500001907348633], "dest": [0.6749577779769897, 0.10500000149011612]}
          28 +{"seed": 87, "success": true, "steps": 107, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [1.203840970993042, 0.46000000834465027], "taskxy": [1.1384081840515137, 0.11968253552913666], "dest": [1.1384080905914307, 0.10500000149011612]}
          29 +{"seed": 88, "success": true, "steps": 112, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [0.4685811400413513, 0.41715937852859497], "taskxy": [0.43061888217926025, 0.10500001162290573], "dest": [0.43061895328760147, 0.10500000149011612]}
          30 +{"seed": 89, "success": true, "steps": 104, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.6049009561538696, 0.46915969252586365], "taskxy": [0.5215333700180054, 0.10499998927116394], "dest": [0.5215333361625671, 0.10500000149011612]}
          31 +{"seed": 90, "success": true, "steps": 109, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.23972979187965393, 0.5099999904632568], "taskxy": [0.18388605117797852, 0.11477714031934738], "dest": [0.18388607013225555, 0.10500000149011612]}
          32 +{"seed": 91, "success": true, "steps": 90, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [0.924026608467102, 0.46000000834465027], "taskxy": [0.8921022415161133, 0.11228382587432861], "dest": [0.8921022232174873, 0.10500000149011612]}
          33 +{"seed": 92, "success": true, "steps": 107, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [1.0326489210128784, 0.370410293340683], "taskxy": [1.00502347946167, 0.10499997437000275], "dest": [1.0050235052108765, 0.10500000149011612]}
          34 +{"seed": 93, "success": true, "steps": 157, "seconds": 0.49, "phase": "place", "task": "target_block", "robot": [1.0940170288085938, 0.41499894857406616], "taskxy": [1.0277327299118042, 0.10499995946884155], "dest": [1.0277326364517212, 0.10500000149011612]}
          35 +{"seed": 94, "success": true, "steps": 40, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [0.6026238799095154, 0.5099999904632568], "taskxy": [0.5353033542633057, 0.11197803169488907], "dest": [0.5353033800125122, 0.10500000149011612]}
          36 +{"seed": 95, "success": true, "steps": 102, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [1.2636786699295044, 0.48673880100250244], "taskxy": [1.2265461683273315, 0.10500001162290573], "dest": [1.226546194076538, 0.10500000149011612]}
          37 +{"seed": 96, "success": true, "steps": 45, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [1.429643154144287, 0.5149989128112793], "taskxy": [1.3976911306381226, 0.10499996691942215], "dest": [1.3976912078857422, 0.10500000149011612]}
          38 +{"seed": 97, "success": true, "steps": 62, "seconds": 0.17, "phase": "place", "task": "target_block", "robot": [0.6469579935073853, 0.37733790278434753], "taskxy": [0.6194591522216797, 0.10499994456768036], "dest": [0.6194591637253761, 0.10500000149011612]}
          39 +{"seed": 98, "success": true, "steps": 103, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [0.23062244057655334, 0.4179598391056061], "taskxy": [0.14807526767253876, 0.10499995201826096], "dest": [0.1480752568244934, 0.10500000149011612]}
          40 +{"seed": 99, "success": true, "steps": 62, "seconds": 0.19, "phase": "place", "task": "target_block", "robot": [1.2927566766738892, 0.4704902768135071], "taskxy": [1.2396767139434814, 0.10500004887580872], "dest": [1.239676739692688, 0.10500000149011612]}
          41 +{"seed": 100, "success": true, "steps": 172, "seconds": 0.59, "phase": "place", "task": "target_block", "robot": [1.1768378019332886, 0.4099999964237213], "taskxy": [1.1082637310028076, 0.11725763976573944], "dest": [1.1082637567520142, 0.10500000149011612]}
          42 +{"seed": 101, "success": true, "steps": 39, "seconds": 0.22, "phase": "place", "task": "target_block", "robot": [0.9191758036613464, 0.422054260969162], "taskxy": [0.8452778458595276, 0.10499999672174454], "dest": [0.8452778350114822, 0.10500000149011612]}
          43 +{"seed": 102, "success": true, "steps": 115, "seconds": 0.93, "phase": "place", "task": "target_block", "robot": [0.5098951458930969, 0.4099999964237213], "taskxy": [0.4805404543876648, 0.12043117731809616], "dest": [0.48054044353961944, 0.10500000149011612]}
          44 +{"seed": 103, "success": true, "steps": 49, "seconds": 0.53, "phase": "place", "task": "target_block", "robot": [1.1813424825668335, 0.46923577785491943], "taskxy": [1.1346606016159058, 0.10499999672174454], "dest": [1.1346606950759888, 0.10500000149011612]}
          45 +{"seed": 104, "success": true, "steps": 159, "seconds": 1.94, "phase": "place", "task": "target_block", "robot": [0.4151942729949951, 0.4712737798690796], "taskxy": [0.340412974357605, 0.10500003397464752], "dest": [0.34041296350955963, 0.10500000149011612]}
          46 +{"seed": 105, "success": true, "steps": 35, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [1.061379313468933, 0.46000000834465027], "taskxy": [0.9701266288757324, 0.11392758786678314], "dest": [0.9701267142295837, 0.10500000149011612]}
          47 +{"seed": 106, "success": true, "steps": 118, "seconds": 1.21, "phase": "place", "task": "target_block", "robot": [0.6255789995193481, 0.4099999666213989], "taskxy": [0.5761586427688599, 0.11624380946159363], "dest": [0.5761585648655891, 0.10500000149011612]}
          48 +{"seed": 107, "success": true, "steps": 45, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [0.41790473461151123, 0.5184365510940552], "taskxy": [0.3617343306541443, 0.10499999672174454], "dest": [0.3617343943119049, 0.10500000149011612]}
          49 +{"seed": 108, "success": true, "steps": 44, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.7884620428085327, 0.5099999904632568], "taskxy": [0.7277265787124634, 0.1109299510717392], "dest": [0.7277265448570251, 0.10500000149011612]}
          50 +{"seed": 109, "success": true, "steps": 99, "seconds": 0.83, "phase": "place", "task": "target_block", "robot": [0.9078325629234314, 0.46000000834465027], "taskxy": [0.8714743852615356, 0.11941707879304886], "dest": [0.8714744110107422, 0.10500000149011612]}
          51 +{"seed": 110, "success": true, "steps": 112, "seconds": 1.08, "phase": "place", "task": "target_block", "robot": [0.2949291169643402, 0.4753939211368561], "taskxy": [0.264769047498703, 0.10500000417232513], "dest": [0.26476904782652855, 0.10500000149011612]}
          52 +{"seed": 111, "success": true, "steps": 53, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [0.5557337403297424, 0.5153118371963501], "taskxy": [0.47091394662857056, 0.10499998182058334], "dest": [0.4709138125181198, 0.10500000149011612]}
          53 +{"seed": 112, "success": true, "steps": 44, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [0.6327254176139832, 0.4100000262260437], "taskxy": [0.5456929802894592, 0.10571519285440445], "dest": [0.5456930060386658, 0.10500000149011612]}
          54 +{"seed": 113, "success": true, "steps": 66, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [0.2628070116043091, 0.4099999964237213], "taskxy": [0.2005523145198822, 0.11943120509386063], "dest": [0.20055228877067566, 0.10500000149011612]}
          55 +{"seed": 114, "success": true, "steps": 37, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [1.4253013134002686, 0.4599999785423279], "taskxy": [1.3676819801330566, 0.11798892915248871], "dest": [1.3676820058822632, 0.10500000149011612]}
          56 +{"seed": 115, "success": true, "steps": 122, "seconds": 1.26, "phase": "place", "task": "target_block", "robot": [0.5034860968589783, 0.4314608573913574], "taskxy": [0.4315631091594696, 0.10500006377696991], "dest": [0.43156305360794067, 0.10500000149011612]}
          57 +{"seed": 116, "success": true, "steps": 71, "seconds": 0.52, "phase": "place", "task": "target_block", "robot": [0.6146400570869446, 0.46000000834465027], "taskxy": [0.5671278834342957, 0.11293917149305344], "dest": [0.5671278949379921, 0.10500000149011612]}
          58 +{"seed": 117, "success": true, "steps": 50, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.46189069747924805, 0.4287354052066803], "taskxy": [0.38455235958099365, 0.10500001907348633], "dest": [0.3845523040294647, 0.10500000149011612]}
          59 +{"seed": 118, "success": true, "steps": 105, "seconds": 0.87, "phase": "place", "task": "target_block", "robot": [0.7981575131416321, 0.5100000500679016], "taskxy": [0.722709059715271, 0.10578078031539917], "dest": [0.7227090854644775, 0.10500000149011612]}
          60 +{"seed": 119, "success": true, "steps": 108, "seconds": 0.99, "phase": "place", "task": "target_block", "robot": [0.9632325768470764, 0.37250176072120667], "taskxy": [0.8959778547286987, 0.10499999672174454], "dest": [0.8959778804779053, 0.10500000149011612]}
          61 +{"seed": 120, "success": true, "steps": 35, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.35513538122177124, 0.5099999904632568], "taskxy": [0.3210921287536621, 0.1138542890548706], "dest": [0.32109214025735855, 0.10500000149011612]}
          62 +{"seed": 121, "success": true, "steps": 42, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [0.5002689361572266, 0.42802488803863525], "taskxy": [0.4419304132461548, 0.10500000417232513], "dest": [0.44193040984869003, 0.10500000149011612]}
          63 +{"seed": 122, "success": true, "steps": 124, "seconds": 1.47, "phase": "place", "task": "target_block", "robot": [1.0388150215148926, 0.4099999964237213], "taskxy": [1.0035731792449951, 0.11781293898820877], "dest": [1.0035731149315834, 0.10500000149011612]}
          64 +{"seed": 123, "success": true, "steps": 66, "seconds": 0.57, "phase": "place", "task": "target_block", "robot": [1.358690619468689, 0.41499897837638855], "taskxy": [1.2644398212432861, 0.10499997437000275], "dest": [1.2644398469924927, 0.10500000149011612]}
          65 +{"seed": 124, "success": true, "steps": 119, "seconds": 1.34, "phase": "place", "task": "target_block", "robot": [0.7890815734863281, 0.46000000834465027], "taskxy": [0.7506853938102722, 0.10670293867588043], "dest": [0.7506853233575821, 0.10500000149011612]}
          66 +{"seed": 125, "success": true, "steps": 121, "seconds": 0.98, "phase": "place", "task": "target_block", "robot": [1.280517578125, 0.37442073225975037], "taskxy": [1.2240878343582153, 0.10500001907348633], "dest": [1.2240878601074219, 0.10500000149011612]}
          67 +{"seed": 126, "success": true, "steps": 37, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.6344805359840393, 0.4762766659259796], "taskxy": [0.5738680362701416, 0.10500001907348633], "dest": [0.5738680024147034, 0.10500000149011612]}
          68 +{"seed": 127, "success": true, "steps": 123, "seconds": 1.14, "phase": "place", "task": "target_block", "robot": [0.6004003286361694, 0.5099999904632568], "taskxy": [0.5034160614013672, 0.12286374717950821], "dest": [0.5034160505533218, 0.10500000149011612]}
          69 +{"seed": 128, "success": true, "steps": 173, "seconds": 2.05, "phase": "place", "task": "target_block", "robot": [0.23824124038219452, 0.48470622301101685], "taskxy": [0.14383257925510406, 0.10499995201826096], "dest": [0.14383253860473633, 0.10500000149011612]}
          70 +{"seed": 129, "success": true, "steps": 56, "seconds": 0.73, "phase": "place", "task": "target_block", "robot": [0.2833930253982544, 0.48651087284088135], "taskxy": [0.19691209495067596, 0.10500003397464752], "dest": [0.1969121288061142, 0.10500000149011612]}
          71 +{"seed": 130, "success": true, "steps": 106, "seconds": 1.16, "phase": "place", "task": "target_block", "robot": [1.141689419746399, 0.46000000834465027], "taskxy": [1.1159781217575073, 0.11898896098136902], "dest": [1.1159781475067139, 0.10500000149011612]}
          72 +{"seed": 131, "success": true, "steps": 57, "seconds": 0.49, "phase": "place", "task": "target_block", "robot": [1.1254593133926392, 0.46000000834465027], "taskxy": [1.033521294593811, 0.10836672782897949], "dest": [1.033521327137947, 0.10500000149011612]}
          73 +{"seed": 132, "success": true, "steps": 157, "seconds": 1.82, "phase": "place", "task": "target_block", "robot": [1.424458384513855, 0.4194662570953369], "taskxy": [1.3488508462905884, 0.10500001907348633], "dest": [1.348850872039795, 0.10500000149011612]}
          74 +{"seed": 133, "success": true, "steps": 99, "seconds": 1.06, "phase": "place", "task": "target_block", "robot": [0.4228183925151825, 0.4812164604663849], "taskxy": [0.35348230600357056, 0.10500001162290573], "dest": [0.3534823100566864, 0.10500000149011612]}
          75 +{"seed": 134, "success": true, "steps": 45, "seconds": 0.49, "phase": "place", "task": "target_block", "robot": [0.9702278971672058, 0.37834659218788147], "taskxy": [0.9396535754203796, 0.10500005632638931], "dest": [0.9396535415649414, 0.10500000149011612]}
          76 +{"seed": 135, "success": true, "steps": 37, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.8588243126869202, 0.46903303265571594], "taskxy": [0.7696531414985657, 0.10500001907348633], "dest": [0.769653226852417, 0.10500000149011612]}
          77 +{"seed": 136, "success": true, "steps": 104, "seconds": 1.13, "phase": "place", "task": "target_block", "robot": [0.46690863370895386, 0.4099999964237213], "taskxy": [0.3709888756275177, 0.11291814595460892], "dest": [0.37098889458179474, 0.10500000149011612]}
          78 +{"seed": 137, "success": true, "steps": 126, "seconds": 1.08, "phase": "place", "task": "target_block", "robot": [0.30551716685295105, 0.4218129813671112], "taskxy": [0.23787200450897217, 0.10500001162290573], "dest": [0.23787191915512085, 0.10500000149011612]}
          79 +{"seed": 138, "success": true, "steps": 139, "seconds": 0.76, "phase": "place", "task": "target_block", "robot": [0.31431150436401367, 0.4099999964237213], "taskxy": [0.24058590829372406, 0.11966364085674286], "dest": [0.2405859123468399, 0.10500000149011612]}
          80 +{"seed": 139, "success": true, "steps": 127, "seconds": 0.94, "phase": "place", "task": "target_block", "robot": [1.418540358543396, 0.4099999964237213], "taskxy": [1.3357714414596558, 0.11049259454011917], "dest": [1.3357714672088623, 0.10500000149011612]}
          81 +{"seed": 140, "success": true, "steps": 46, "seconds": 0.36, "phase": "place", "task": "target_block", "robot": [0.4379059672355652, 0.4100000262260437], "taskxy": [0.3777534067630768, 0.11213250458240509], "dest": [0.3777534108161926, 0.10500000149011612]}
          82 +{"seed": 141, "success": true, "steps": 96, "seconds": 0.55, "phase": "place", "task": "target_block", "robot": [0.9136666655540466, 0.41499900817871094], "taskxy": [0.8598531484603882, 0.10500001162290573], "dest": [0.85985311460495, 0.10500000149011612]}
          83 +{"seed": 142, "success": true, "steps": 78, "seconds": 0.36, "phase": "place", "task": "target_block", "robot": [0.6798703074455261, 0.4099999666213989], "taskxy": [0.637774646282196, 0.10692957043647766], "dest": [0.6377746652364731, 0.10500000149011612]}
          84 +{"seed": 143, "success": true, "steps": 102, "seconds": 0.8, "phase": "place", "task": "target_block", "robot": [0.818950891494751, 0.3874554932117462], "taskxy": [0.7649366855621338, 0.10499998927116394], "dest": [0.7649366828203201, 0.10500000149011612]}
          85 +{"seed": 144, "success": true, "steps": 58, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [0.9016543030738831, 0.5099999904632568], "taskxy": [0.8060433268547058, 0.1213487908244133], "dest": [0.8060432929992676, 0.10500000149011612]}
          86 +{"seed": 145, "success": true, "steps": 87, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [0.5213470458984375, 0.4855923652648926], "taskxy": [0.4759812653064728, 0.10499997437000275], "dest": [0.47598123145103455, 0.10500000149011612]}
          87 +{"seed": 146, "success": true, "steps": 107, "seconds": 0.77, "phase": "place", "task": "target_block", "robot": [0.9525736570358276, 0.46000000834465027], "taskxy": [0.9010354280471802, 0.11600760370492935], "dest": [0.9010354537963867, 0.10500000149011612]}
          88 +{"seed": 147, "success": true, "steps": 44, "seconds": 0.36, "phase": "place", "task": "target_block", "robot": [0.7222214937210083, 0.4742678105831146], "taskxy": [0.6897183060646057, 0.10500005632638931], "dest": [0.6897182728648186, 0.10500000149011612]}
          89 +{"seed": 148, "success": true, "steps": 37, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [1.106476902961731, 0.4099999666213989], "taskxy": [1.0169843435287476, 0.11207161098718643], "dest": [1.016984243273735, 0.10500000149011612]}
          90 +{"seed": 149, "success": true, "steps": 46, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [1.1682243347167969, 0.5188928842544556], "taskxy": [1.106494665145874, 0.10500003397464752], "dest": [1.1064947064518929, 0.10500000149011612]}
          91 +{"seed": 150, "success": true, "steps": 49, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [0.6279230117797852, 0.5099999904632568], "taskxy": [0.5899595618247986, 0.12473844736814499], "dest": [0.5899595875740051, 0.10500000149011612]}
          92 +{"seed": 151, "success": true, "steps": 41, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [0.7792736887931824, 0.5099999904632568], "taskxy": [0.75375896692276, 0.10933399945497513], "dest": [0.7537589232027531, 0.10500000149011612]}
          93 +{"seed": 152, "success": true, "steps": 96, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [0.8721857666969299, 0.46635934710502625], "taskxy": [0.8440008759498596, 0.10500001162290573], "dest": [0.8440008464753628, 0.10500000149011612]}
          94 +{"seed": 153, "success": true, "steps": 156, "seconds": 1.05, "phase": "place", "task": "target_block", "robot": [0.837716281414032, 0.42963817715644836], "taskxy": [0.7561463117599487, 0.10499999672174454], "dest": [0.7561462779045105, 0.10500000149011612]}
          95 +{"seed": 154, "success": true, "steps": 57, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [1.4377177953720093, 0.5099999904632568], "taskxy": [1.3732746839523315, 0.11366841197013855], "dest": [1.373274709701538, 0.10500000149011612]}
          96 +{"seed": 155, "success": true, "steps": 46, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [0.6788397431373596, 0.5100000500679016], "taskxy": [0.6380122900009155, 0.11521480977535248], "dest": [0.638012226998806, 0.10500000149011612]}
          97 +{"seed": 156, "success": true, "steps": 138, "seconds": 0.84, "phase": "place", "task": "target_block", "robot": [0.5066274404525757, 0.48027175664901733], "taskxy": [0.4116956293582916, 0.10499998927116394], "dest": [0.41169568490982056, 0.10500000149011612]}
          98 +{"seed": 157, "success": true, "steps": 49, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [1.349788784980774, 0.4778461158275604], "taskxy": [1.322613000869751, 0.10500001907348633], "dest": [1.3226130266189575, 0.10500000149011612]}
          99 +{"seed": 158, "success": true, "steps": 125, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [0.37651997804641724, 0.5184415578842163], "taskxy": [0.32549503445625305, 0.10500003397464752], "dest": [0.3254949938058853, 0.10500000149011612]}
         100 +{"seed": 159, "success": true, "steps": 100, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [0.9177734851837158, 0.4706752598285675], "taskxy": [0.8794414401054382, 0.10500000417232513], "dest": [0.8794415248036385, 0.10500000149011612]}
         101 +{"seed": 160, "success": true, "steps": 42, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.8499254584312439, 0.37141042947769165], "taskxy": [0.7984732985496521, 0.10500004142522812], "dest": [0.7984733324050903, 0.10500000149011612]}
         102 +{"seed": 161, "success": true, "steps": 106, "seconds": 0.66, "phase": "place", "task": "target_block", "robot": [1.1081222295761108, 0.4100000262260437], "taskxy": [1.068873405456543, 0.11547641456127167], "dest": [1.0688733573555946, 0.10500000149011612]}
         103 +{"seed": 162, "success": true, "steps": 103, "seconds": 0.56, "phase": "place", "task": "target_block", "robot": [1.0537642240524292, 0.4099999964237213], "taskxy": [1.01065194606781, 0.11313172429800034], "dest": [1.0106520469784737, 0.10500000149011612]}
         104 +{"seed": 163, "success": true, "steps": 98, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [0.9177964925765991, 0.3824598491191864], "taskxy": [0.8651366233825684, 0.10499998927116394], "dest": [0.8651366572380066, 0.10500000149011612]}
         105 +{"seed": 164, "success": true, "steps": 100, "seconds": 0.53, "phase": "place", "task": "target_block", "robot": [1.2256959676742554, 0.5099999904632568], "taskxy": [1.1723312139511108, 0.10562071949243546], "dest": [1.1723312403559685, 0.10500000149011612]}
         106 +{"seed": 165, "success": true, "steps": 122, "seconds": 0.68, "phase": "place", "task": "target_block", "robot": [0.2682191729545593, 0.4599999785423279], "taskxy": [0.1840570718050003, 0.11902344971895218], "dest": [0.18405709075927734, 0.10500000149011612]}
         107 +{"seed": 166, "success": true, "steps": 101, "seconds": 0.66, "phase": "place", "task": "target_block", "robot": [0.6377274990081787, 0.4099999666213989], "taskxy": [0.5801003575325012, 0.12264285981655121], "dest": [0.580100323677063, 0.10500000149011612]}
         108 +{"seed": 167, "success": true, "steps": 112, "seconds": 0.72, "phase": "place", "task": "target_block", "robot": [0.34188753366470337, 0.4285704791545868], "taskxy": [0.26078566908836365, 0.10499998927116394], "dest": [0.2607856433391571, 0.10500000149011612]}
         109 +{"seed": 168, "success": true, "steps": 67, "seconds": 0.4, "phase": "place", "task": "target_block", "robot": [0.319296270608902, 0.46000000834465027], "taskxy": [0.2873324155807495, 0.12115897983312607], "dest": [0.28733244198560715, 0.10500000149011612]}
         110 +{"seed": 169, "success": true, "steps": 128, "seconds": 0.76, "phase": "place", "task": "target_block", "robot": [1.1847256422042847, 0.4099999964237213], "taskxy": [1.1273775100708008, 0.11878211051225662], "dest": [1.1273774979114533, 0.10500000149011612]}
         111 +{"seed": 170, "success": true, "steps": 99, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [1.1065208911895752, 0.3782927989959717], "taskxy": [1.0794156789779663, 0.10500000417232513], "dest": [1.0794156532287598, 0.10500000149011612]}
         112 +{"seed": 171, "success": true, "steps": 110, "seconds": 0.67, "phase": "place", "task": "target_block", "robot": [0.8218992352485657, 0.41499900817871094], "taskxy": [0.7442371249198914, 0.10499999672174454], "dest": [0.7442371127605438, 0.10500000149011612]}
         113 +{"seed": 172, "success": true, "steps": 92, "seconds": 0.52, "phase": "place", "task": "target_block", "robot": [0.4154045879840851, 0.46000000834465027], "taskxy": [0.3587934970855713, 0.11072710901498795], "dest": [0.35879347878694534, 0.10500000149011612]}
         114 +{"seed": 173, "success": true, "steps": 121, "seconds": 0.74, "phase": "place", "task": "target_block", "robot": [1.0729845762252808, 0.4149989187717438], "taskxy": [1.0037026405334473, 0.10499995201826096], "dest": [1.0037026730775833, 0.10500000149011612]}
         115 +{"seed": 174, "success": true, "steps": 101, "seconds": 0.58, "phase": "place", "task": "target_block", "robot": [1.3998658657073975, 0.5099999904632568], "taskxy": [1.3021860122680664, 0.11062567681074142], "dest": [1.302186038017273, 0.10500000149011612]}
         116 +{"seed": 175, "success": true, "steps": 102, "seconds": 0.85, "phase": "place", "task": "target_block", "robot": [0.5429722666740417, 0.4099999964237213], "taskxy": [0.4575830399990082, 0.11101280897855759], "dest": [0.45758303594589234, 0.10500000149011612]}
         117 +{"seed": 176, "success": true, "steps": 52, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.5253434181213379, 0.4100000262260437], "taskxy": [0.438852995634079, 0.11774450540542603], "dest": [0.43885291028022766, 0.10500000149011612]}
         118 +{"seed": 177, "success": true, "steps": 107, "seconds": 0.71, "phase": "place", "task": "target_block", "robot": [0.4299778938293457, 0.5099999904632568], "taskxy": [0.3458276093006134, 0.10889900475740433], "dest": [0.34582762825489044, 0.10500000149011612]}
         119 +{"seed": 178, "success": true, "steps": 128, "seconds": 0.94, "phase": "place", "task": "target_block", "robot": [0.4065884053707123, 0.4810401201248169], "taskxy": [0.32131674885749817, 0.10499997437000275], "dest": [0.32131667840480804, 0.10500000149011612]}
         120 +{"seed": 179, "success": true, "steps": 129, "seconds": 0.77, "phase": "place", "task": "target_block", "robot": [0.7077009677886963, 0.5099999904632568], "taskxy": [0.6586494445800781, 0.11325297504663467], "dest": [0.6586494703292847, 0.10500000149011612]}
         121 +{"seed": 180, "success": true, "steps": 54, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [1.3683747053146362, 0.5149990320205688], "taskxy": [1.3210786581039429, 0.10499999672174454], "dest": [1.3210786838531494, 0.10500000149011612]}
         122 +{"seed": 181, "success": true, "steps": 110, "seconds": 0.95, "phase": "place", "task": "target_block", "robot": [0.7293605208396912, 0.4387282431125641], "taskxy": [0.6468708515167236, 0.10499995201826096], "dest": [0.6468708636760712, 0.10500000149011612]}
         123 +{"seed": 182, "success": true, "steps": 180, "seconds": 1.18, "phase": "place", "task": "target_block", "robot": [1.2127326726913452, 0.46000000834465027], "taskxy": [1.1303985118865967, 0.12315625697374344], "dest": [1.1303985376358032, 0.10500000149011612]}
         124 +{"seed": 183, "success": true, "steps": 110, "seconds": 0.99, "phase": "place", "task": "target_block", "robot": [0.7095969319343567, 0.42436733841896057], "taskxy": [0.6201819777488708, 0.10500000417232513], "dest": [0.6201819506883621, 0.10500000149011612]}
         125 +{"seed": 184, "success": true, "steps": 120, "seconds": 0.6, "phase": "place", "task": "target_block", "robot": [0.5227537751197815, 0.42881375551223755], "taskxy": [0.46838968992233276, 0.10500004142522812], "dest": [0.4683896716237068, 0.10500000149011612]}
         126 +{"seed": 185, "success": true, "steps": 47, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [1.129578709602356, 0.4156990647315979], "taskxy": [1.1027228832244873, 0.10499995946884155], "dest": [1.1027229089736938, 0.10500000149011612]}
         127 +{"seed": 186, "success": true, "steps": 43, "seconds": 0.22, "phase": "place", "task": "target_block", "robot": [0.8565796613693237, 0.4599999785423279], "taskxy": [0.8123355507850647, 0.11864811182022095], "dest": [0.812335472881794, 0.10500000149011612]}
         128 +{"seed": 187, "success": true, "steps": 104, "seconds": 0.72, "phase": "place", "task": "target_block", "robot": [0.8796343803405762, 0.4099999964237213], "taskxy": [0.8033652305603027, 0.12227272987365723], "dest": [0.8033652563095093, 0.10500000149011612]}
         129 +{"seed": 188, "success": true, "steps": 36, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [1.1417644023895264, 0.5100000500679016], "taskxy": [1.083407998085022, 0.1167507916688919], "dest": [1.0834080238342285, 0.10500000149011612]}
         130 +{"seed": 189, "success": true, "steps": 61, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [0.5203484296798706, 0.3785127103328705], "taskxy": [0.48104849457740784, 0.10500001162290573], "dest": [0.4810485135316849, 0.10500000149011612]}
         131 +{"seed": 190, "success": true, "steps": 42, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [1.229278326034546, 0.38788771629333496], "taskxy": [1.1581885814666748, 0.10500001907348633], "dest": [1.1581884880065918, 0.10500000149011612]}
         132 +{"seed": 191, "success": true, "steps": 51, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [0.3704800605773926, 0.48505374789237976], "taskxy": [0.3236472010612488, 0.10499995201826096], "dest": [0.3236472647190094, 0.10500000149011612]}
         133 +{"seed": 192, "success": true, "steps": 99, "seconds": 0.6, "phase": "place", "task": "target_block", "robot": [0.8002225160598755, 0.4599999785423279], "taskxy": [0.7718510627746582, 0.11986493319272995], "dest": [0.77185102891922, 0.10500000149011612]}
         134 +{"seed": 193, "success": true, "steps": 112, "seconds": 0.8, "phase": "place", "task": "target_block", "robot": [0.9963451027870178, 0.46000000834465027], "taskxy": [0.9350860714912415, 0.12250472605228424], "dest": [0.9350860376358032, 0.10500000149011612]}
         135 +{"seed": 194, "success": true, "steps": 156, "seconds": 1.05, "phase": "place", "task": "target_block", "robot": [0.7642730474472046, 0.437491774559021], "taskxy": [0.678351879119873, 0.10499999672174454], "dest": [0.6783518452644348, 0.10500000149011612]}
         136 +{"seed": 195, "success": true, "steps": 45, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.9645843505859375, 0.46732091903686523], "taskxy": [0.9271239638328552, 0.10500000417232513], "dest": [0.927123929977417, 0.10500000149011612]}
         137 +{"seed": 196, "success": true, "steps": 56, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [0.3127783238887787, 0.4252198040485382], "taskxy": [0.28194281458854675, 0.10499998927116394], "dest": [0.2819427962899208, 0.10500000149011612]}
         138 +{"seed": 197, "success": true, "steps": 185, "seconds": 1.44, "phase": "place", "task": "target_block", "robot": [0.2304581254720688, 0.3733106851577759], "taskxy": [0.13174697756767273, 0.10500003397464752], "dest": [0.13174698907136917, 0.10500000149011612]}
         139 +{"seed": 198, "success": true, "steps": 114, "seconds": 0.84, "phase": "place", "task": "target_block", "robot": [0.5582054257392883, 0.4099999964237213], "taskxy": [0.4988063871860504, 0.11794696748256683], "dest": [0.49880640614032745, 0.10500000149011612]}
         140 +{"seed": 199, "success": true, "steps": 90, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [0.648369312286377, 0.38046732544898987], "taskxy": [0.6041066646575928, 0.10499998182058334], "dest": [0.6041066308021545, 0.10500000149011612]}
         141 +{"seed": 200, "success": true, "steps": 46, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.2759738862514496, 0.42613640427589417], "taskxy": [0.2114548236131668, 0.10499999672174454], "dest": [0.21145481276512146, 0.10500000149011612]}
         142 +{"seed": 201, "success": true, "steps": 50, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [1.3988491296768188, 0.46000000834465027], "taskxy": [1.3624950647354126, 0.11358065903186798], "dest": [1.3624950904846191, 0.10500000149011612]}
         143 +{"seed": 202, "success": true, "steps": 51, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.5097998380661011, 0.5099999904632568], "taskxy": [0.44253653287887573, 0.1194891631603241], "dest": [0.4425364326238632, 0.10500000149011612]}
         144 +{"seed": 203, "success": true, "steps": 60, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [1.186576008796692, 0.43590208888053894], "taskxy": [1.115207314491272, 0.10499997437000275], "dest": [1.1152073402404785, 0.10500000149011612]}
         145 +{"seed": 204, "success": true, "steps": 109, "seconds": 1.01, "phase": "place", "task": "target_block", "robot": [1.039375901222229, 0.4599999785423279], "taskxy": [0.9875588417053223, 0.10804903507232666], "dest": [0.9875588830113411, 0.10500000149011612]}
         146 +{"seed": 205, "success": true, "steps": 60, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [0.7076284885406494, 0.38412514328956604], "taskxy": [0.6479342579841614, 0.10500000417232513], "dest": [0.6479342241287231, 0.10500000149011612]}
         147 +{"seed": 206, "success": true, "steps": 106, "seconds": 0.62, "phase": "place", "task": "target_block", "robot": [1.0803149938583374, 0.5099999904632568], "taskxy": [0.9917110204696655, 0.11592815071344376], "dest": [0.9917109866142273, 0.10500000149011612]}
         148 +{"seed": 207, "success": true, "steps": 47, "seconds": 0.2, "phase": "place", "task": "target_block", "robot": [1.129778504371643, 0.4149989187717438], "taskxy": [1.0416414737701416, 0.10499995946884155], "dest": [1.0416414995193481, 0.10500000149011612]}
         149 +{"seed": 208, "success": true, "steps": 45, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [0.5994526147842407, 0.5149989724159241], "taskxy": [0.5107808709144592, 0.10499997437000275], "dest": [0.5107808383703232, 0.10500000149011612]}
         150 +{"seed": 209, "success": true, "steps": 88, "seconds": 0.76, "phase": "place", "task": "target_block", "robot": [0.3402767777442932, 0.4764922559261322], "taskxy": [0.2583696246147156, 0.10499999672174454], "dest": [0.25836959075927735, 0.10500000149011612]}
         151 +{"seed": 210, "success": true, "steps": 39, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [1.3060803413391113, 0.4392000138759613], "taskxy": [1.2502148151397705, 0.10499995201826096], "dest": [1.2502147216796875, 0.10500000149011612]}
         152 +{"seed": 211, "success": true, "steps": 53, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.36744755506515503, 0.46000000834465027], "taskxy": [0.2727294862270355, 0.11035006493330002], "dest": [0.2727294306755066, 0.10500000149011612]}
         153 +{"seed": 212, "success": true, "steps": 52, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.585322916507721, 0.46521446108818054], "taskxy": [0.4856983423233032, 0.10499999672174454], "dest": [0.48569840598106384, 0.10500000149011612]}
         154 +{"seed": 213, "success": true, "steps": 43, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.6057042479515076, 0.3828946650028229], "taskxy": [0.5172274708747864, 0.10499999672174454], "dest": [0.5172275047302246, 0.10500000149011612]}
         155 +{"seed": 214, "success": true, "steps": 72, "seconds": 0.46, "phase": "place", "task": "target_block", "robot": [0.8655529022216797, 0.37298282980918884], "taskxy": [0.7683004140853882, 0.10499995201826096], "dest": [0.7683004032373428, 0.10500000149011612]}
         156 +{"seed": 215, "success": true, "steps": 118, "seconds": 0.85, "phase": "place", "task": "target_block", "robot": [1.320755124092102, 0.4599999785423279], "taskxy": [1.2284895181655884, 0.11447552591562271], "dest": [1.228489543914795, 0.10500000149011612]}
         157 +{"seed": 216, "success": true, "steps": 104, "seconds": 0.87, "phase": "place", "task": "target_block", "robot": [1.205291986465454, 0.4838959276676178], "taskxy": [1.176392912864685, 0.10500001162290573], "dest": [1.1763929386138916, 0.10500000149011612]}
         158 +{"seed": 217, "success": true, "steps": 95, "seconds": 0.8, "phase": "place", "task": "target_block", "robot": [1.175728440284729, 0.4811908006668091], "taskxy": [1.1115593910217285, 0.10500001162290573], "dest": [1.111559416770935, 0.10500000149011612]}
         159 +{"seed": 218, "success": true, "steps": 93, "seconds": 0.73, "phase": "place", "task": "target_block", "robot": [1.176265001296997, 0.38821133971214294], "taskxy": [1.1356467008590698, 0.10500002652406693], "dest": [1.1356467266082764, 0.10500000149011612]}
         160 +{"seed": 219, "success": true, "steps": 50, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [1.1573489904403687, 0.4099999666213989], "taskxy": [1.139815092086792, 0.1192697212100029], "dest": [1.1398151296675205, 0.10500000149011612]}
         161 +{"seed": 220, "success": true, "steps": 102, "seconds": 0.85, "phase": "place", "task": "target_block", "robot": [1.09867262840271, 0.4099999964237213], "taskxy": [1.0730983018875122, 0.10505354404449463], "dest": [1.0730983276367188, 0.10500000149011612]}
         162 +{"seed": 221, "success": true, "steps": 120, "seconds": 0.81, "phase": "place", "task": "target_block", "robot": [0.33584752678871155, 0.4099999964237213], "taskxy": [0.2883746922016144, 0.1149783506989479], "dest": [0.28837466645240784, 0.10500000149011612]}
         163 +{"seed": 222, "success": true, "steps": 102, "seconds": 0.72, "phase": "place", "task": "target_block", "robot": [0.9746833443641663, 0.46000000834465027], "taskxy": [0.9080283045768738, 0.11519318073987961], "dest": [0.908028338432312, 0.10500000149011612]}
         164 +{"seed": 223, "success": true, "steps": 50, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.7633123993873596, 0.5099999904632568], "taskxy": [0.7206600308418274, 0.10502651333808899], "dest": [0.7206600565910339, 0.10500000149011612]}
         165 +{"seed": 224, "success": true, "steps": 94, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [0.6675875782966614, 0.5099999904632568], "taskxy": [0.6234042048454285, 0.10592404007911682], "dest": [0.6234041852355003, 0.10500000149011612]}
         166 +{"seed": 225, "success": true, "steps": 162, "seconds": 1.28, "phase": "place", "task": "target_block", "robot": [1.384186029434204, 0.5099999904632568], "taskxy": [1.3023366928100586, 0.11537095159292221], "dest": [1.3023365993499756, 0.10500000149011612]}
         167 +{"seed": 226, "success": true, "steps": 160, "seconds": 1.16, "phase": "place", "task": "target_block", "robot": [1.177959680557251, 0.4367905855178833], "taskxy": [1.0982797145843506, 0.10500006377696991], "dest": [1.0982797403335571, 0.10500000149011612]}
         168 +{"seed": 227, "success": true, "steps": 99, "seconds": 0.64, "phase": "place", "task": "target_block", "robot": [0.3517327308654785, 0.5155988931655884], "taskxy": [0.32258114218711853, 0.10499999672174454], "dest": [0.3225811462402344, 0.10500000149011612]}
         169 +{"seed": 228, "success": true, "steps": 105, "seconds": 0.71, "phase": "place", "task": "target_block", "robot": [0.3378911018371582, 0.5149990320205688], "taskxy": [0.28288230299949646, 0.10500002652406693], "dest": [0.2828822921514511, 0.10500000149011612]}
         170 +{"seed": 229, "success": true, "steps": 49, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.7486321926116943, 0.4222504794597626], "taskxy": [0.6714966297149658, 0.10499998182058334], "dest": [0.6714965958595276, 0.10500000149011612]}
         171 +{"seed": 230, "success": true, "steps": 95, "seconds": 0.62, "phase": "place", "task": "target_block", "robot": [0.5077855587005615, 0.4311956465244293], "taskxy": [0.4547581970691681, 0.10499999672174454], "dest": [0.45475822281837464, 0.10500000149011612]}
         172 +{"seed": 231, "success": true, "steps": 51, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [1.4847581386566162, 0.4100000262260437], "taskxy": [1.4124529361724854, 0.12465054541826248], "dest": [1.412452961921692, 0.10500000149011612]}
         173 +{"seed": 232, "success": true, "steps": 47, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [0.8916046023368835, 0.4254990518093109], "taskxy": [0.8406209945678711, 0.10499999672174454], "dest": [0.8406209607124329, 0.10500000149011612]}
         174 +{"seed": 233, "success": true, "steps": 48, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.46690353751182556, 0.42640039324760437], "taskxy": [0.4409103989601135, 0.10500002652406693], "dest": [0.44091043654084205, 0.10500000149011612]}
         175 +{"seed": 234, "success": true, "steps": 101, "seconds": 0.66, "phase": "place", "task": "target_block", "robot": [0.8331328630447388, 0.4100000262260437], "taskxy": [0.7439514994621277, 0.11869783699512482], "dest": [0.7439514656066895, 0.10500000149011612]}
         176 +{"seed": 235, "success": true, "steps": 127, "seconds": 1.03, "phase": "place", "task": "target_block", "robot": [1.0686664581298828, 0.4238031804561615], "taskxy": [0.9809160232543945, 0.10500001162290573], "dest": [0.9809161086082459, 0.10500000149011612]}
         177 +{"seed": 236, "success": true, "steps": 132, "seconds": 0.81, "phase": "place", "task": "target_block", "robot": [0.43392854928970337, 0.4599999785423279], "taskxy": [0.40065380930900574, 0.10696648806333542], "dest": [0.4006537910103798, 0.10500000149011612]}
         178 +{"seed": 237, "success": true, "steps": 192, "seconds": 1.47, "phase": "place", "task": "target_block", "robot": [1.158176064491272, 0.41499900817871094], "taskxy": [1.0837353467941284, 0.10499999672174454], "dest": [1.0837352533340454, 0.10500000149011612]}
         179 +{"seed": 238, "success": true, "steps": 31, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [1.1040300130844116, 0.5099999904632568], "taskxy": [1.028597354888916, 0.11172892898321152], "dest": [1.028597284436226, 0.10500000149011612]}
         180 +{"seed": 239, "success": false, "steps": 150, "seconds": 1.15, "phase": "place", "task": "target_block", "robot": [0.18424083292484283, 0.4599999785423279], "taskxy": [0.15699279308319092, 0.18406200408935547], "dest": [0.15699279779195785, 0.10500000149011612]}
         181 +{"seed": 240, "success": true, "steps": 159, "seconds": 1.12, "phase": "place", "task": "target_block", "robot": [0.6126667261123657, 0.48277005553245544], "taskxy": [0.5492324233055115, 0.10499998182058334], "dest": [0.5492323379516602, 0.10500000149011612]}
         182 +{"seed": 241, "success": true, "steps": 38, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.7412592172622681, 0.4599999785423279], "taskxy": [0.7108486294746399, 0.12396121770143509], "dest": [0.7108485956192017, 0.10500000149011612]}
         183 +{"seed": 242, "success": true, "steps": 116, "seconds": 0.85, "phase": "place", "task": "target_block", "robot": [1.1531999111175537, 0.4656291604042053], "taskxy": [1.100527286529541, 0.10500005632638931], "dest": [1.1005273122787476, 0.10500000149011612]}
         184 +{"seed": 243, "success": true, "steps": 56, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [0.8676689863204956, 0.46000000834465027], "taskxy": [0.8228185772895813, 0.11275994032621384], "dest": [0.8228185447454452, 0.10500000149011612]}
         185 +{"seed": 244, "success": true, "steps": 88, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [0.4911010265350342, 0.4373009502887726], "taskxy": [0.4545808434486389, 0.10499994456768036], "dest": [0.45458084005117416, 0.10500000149011612]}
         186 +{"seed": 245, "success": true, "steps": 59, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [1.4415509700775146, 0.47763052582740784], "taskxy": [1.3971720933914185, 0.10500001162290573], "dest": [1.3971720598638058, 0.10500000149011612]}
         187 +{"seed": 246, "success": true, "steps": 151, "seconds": 1.15, "phase": "place", "task": "target_block", "robot": [0.7642503380775452, 0.5099999904632568], "taskxy": [0.6990669369697571, 0.12411757558584213], "dest": [0.6990669627189636, 0.10500000149011612]}
         188 +{"seed": 247, "success": true, "steps": 48, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.20380054414272308, 0.4834861755371094], "taskxy": [0.14033645391464233, 0.10500001907348633], "dest": [0.14033650267124176, 0.10500000149011612]}
         189 +{"seed": 248, "success": true, "steps": 108, "seconds": 0.66, "phase": "place", "task": "target_block", "robot": [0.8608198761940002, 0.46000000834465027], "taskxy": [0.7712673544883728, 0.10803037881851196], "dest": [0.7712672244310379, 0.10500000149011612]}
         190 +{"seed": 249, "success": true, "steps": 104, "seconds": 0.78, "phase": "place", "task": "target_block", "robot": [0.8829272985458374, 0.4100000262260437], "taskxy": [0.8378003835678101, 0.11952757835388184], "dest": [0.8378004093170166, 0.10500000149011612]}
         191 +{"seed": 250, "success": true, "steps": 124, "seconds": 0.86, "phase": "place", "task": "target_block", "robot": [1.3038841485977173, 0.4599999785423279], "taskxy": [1.2672724723815918, 0.11488290131092072], "dest": [1.2672724981307983, 0.10500000149011612]}
         192 +{"seed": 251, "success": true, "steps": 41, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.7847656011581421, 0.4099999964237213], "taskxy": [0.7452534437179565, 0.12352477759122849], "dest": [0.7452534098625183, 0.10500000149011612]}
         193 +{"seed": 252, "success": true, "steps": 163, "seconds": 1.21, "phase": "place", "task": "target_block", "robot": [0.31486761569976807, 0.4099999964237213], "taskxy": [0.23266513645648956, 0.1120409145951271], "dest": [0.23266509580612182, 0.10500000149011612]}
         194 +{"seed": 253, "success": true, "steps": 99, "seconds": 0.64, "phase": "place", "task": "target_block", "robot": [0.4712182879447937, 0.4166892170906067], "taskxy": [0.3968850076198578, 0.10499998182058334], "dest": [0.39688499677181244, 0.10500000149011612]}
         195 +{"seed": 254, "success": true, "steps": 49, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [1.1631126403808594, 0.4831763207912445], "taskxy": [1.0712007284164429, 0.10499999672174454], "dest": [1.0712006349563599, 0.10500000149011612]}
         196 +{"seed": 255, "success": true, "steps": 43, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [0.47499650716781616, 0.5149990320205688], "taskxy": [0.4397558271884918, 0.10500001162290573], "dest": [0.4397557939887047, 0.10500000149011612]}
         197 +{"seed": 256, "success": true, "steps": 97, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [0.187763512134552, 0.3770383298397064], "taskxy": [0.15264758467674255, 0.10499998927116394], "dest": [0.1526476110816002, 0.10500000149011612]}
         198 +{"seed": 257, "success": true, "steps": 99, "seconds": 0.78, "phase": "place", "task": "target_block", "robot": [0.7609816193580627, 0.4099999964237213], "taskxy": [0.7189556360244751, 0.11185920238494873], "dest": [0.7189555432200432, 0.10500000149011612]}
         199 +{"seed": 258, "success": true, "steps": 107, "seconds": 0.69, "phase": "place", "task": "target_block", "robot": [0.7062091827392578, 0.4599999785423279], "taskxy": [0.6362115144729614, 0.1153079941868782], "dest": [0.6362114806175232, 0.10500000149011612]}
         200 +{"seed": 259, "success": true, "steps": 34, "seconds": 0.19, "phase": "place", "task": "target_block", "robot": [0.9312154650688171, 0.4692976474761963], "taskxy": [0.897455096244812, 0.10500001162290573], "dest": [0.8974550630450249, 0.10500000149011612]}
diff --git a/results.jsonl b/results.jsonl
new file mode 100644
index 0000000..d392baf
--- /dev/null
+++ b/results.jsonl
@@ -0,0 +1,60 @@
           1 +{"seed": 0, "success": true, "steps": 161, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [0.7908052802085876, 0.4099999964237213], "taskxy": [0.7405965328216553, 0.1224580705165863], "dest": [0.740596498966217, 0.10500000149011612]}
           2 +{"seed": 1, "success": true, "steps": 115, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.9666023254394531, 0.47871848940849304], "taskxy": [0.8694780468940735, 0.10499997437000275], "dest": [0.86947807264328, 0.10500000149011612]}
           3 +{"seed": 2, "success": true, "steps": 152, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [0.9954461455345154, 0.5160518288612366], "taskxy": [0.9415640234947205, 0.10499998927116394], "dest": [0.941564049243927, 0.10500000149011612]}
           4 +{"seed": 3, "success": true, "steps": 91, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [1.2916558980941772, 0.46499893069267273], "taskxy": [1.216448187828064, 0.10499992966651917], "dest": [1.2164482135772705, 0.10500000149011612]}
           5 +{"seed": 4, "success": true, "steps": 79, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [1.4231511354446411, 0.4099999666213989], "taskxy": [1.3380085229873657, 0.11882080882787704], "dest": [1.3380084295272827, 0.10500000149011612]}
           6 +{"seed": 5, "success": true, "steps": 179, "seconds": 0.53, "phase": "place", "task": "target_block", "robot": [0.24981096386909485, 0.3767913281917572], "taskxy": [0.19417543709278107, 0.10500004887580872], "dest": [0.19417539644241333, 0.10500000149011612]}
           7 +{"seed": 6, "success": true, "steps": 99, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [1.1417207717895508, 0.41949447989463806], "taskxy": [1.0661463737487793, 0.10499998927116394], "dest": [1.0661463994979858, 0.10500000149011612]}
           8 +{"seed": 7, "success": true, "steps": 186, "seconds": 0.56, "phase": "place", "task": "target_block", "robot": [0.20300805568695068, 0.4099999964237213], "taskxy": [0.14074257016181946, 0.10787273198366165], "dest": [0.14074252951145172, 0.10500000149011612]}
           9 +{"seed": 8, "success": true, "steps": 157, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [0.29301247000694275, 0.4649989604949951], "taskxy": [0.2498759627342224, 0.10499998927116394], "dest": [0.24987597423791885, 0.10500000149011612]}
          10 +{"seed": 9, "success": true, "steps": 136, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [1.5061836242675781, 0.3817973732948303], "taskxy": [1.4225263595581055, 0.10500002652406693], "dest": [1.422526385307312, 0.10500000149011612]}
          11 +{"seed": 10, "success": true, "steps": 56, "seconds": 0.16, "phase": "place", "task": "target_block", "robot": [0.3620208501815796, 0.4366528391838074], "taskxy": [0.31965428590774536, 0.10500001162290573], "dest": [0.31965430825948715, 0.10500000149011612]}
          12 +{"seed": 11, "success": true, "steps": 64, "seconds": 0.19, "phase": "place", "task": "target_block", "robot": [1.4770435094833374, 0.3894660770893097], "taskxy": [1.446761965751648, 0.10500000417232513], "dest": [1.4467619915008545, 0.10500000149011612]}
          13 +{"seed": 12, "success": true, "steps": 140, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [1.4482805728912354, 0.38726189732551575], "taskxy": [1.3729971647262573, 0.10499999672174454], "dest": [1.3729971904754639, 0.10500000149011612]}
          14 +{"seed": 13, "success": true, "steps": 108, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [1.0467785596847534, 0.4355349540710449], "taskxy": [0.9504138231277466, 0.10500002652406693], "dest": [0.9504137960672379, 0.10500000149011612]}
          15 +{"seed": 14, "success": true, "steps": 42, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.8645417094230652, 0.47744718194007874], "taskxy": [0.7823681831359863, 0.10500001907348633], "dest": [0.7823681126832962, 0.10500000149011612]}
          16 +{"seed": 15, "success": true, "steps": 42, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.7696993947029114, 0.4099999964237213], "taskxy": [0.6985525488853455, 0.1074572429060936], "dest": [0.698552561044693, 0.10500000149011612]}
          17 +{"seed": 16, "success": true, "steps": 40, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.29229098558425903, 0.5099999904632568], "taskxy": [0.2016935646533966, 0.11689253896474838], "dest": [0.20169359850883484, 0.10500000149011612]}
          18 +{"seed": 17, "success": true, "steps": 101, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [1.2152363061904907, 0.4649989902973175], "taskxy": [1.1581239700317383, 0.10499999672174454], "dest": [1.1581239951252937, 0.10500000149011612]}
          19 +{"seed": 18, "success": true, "steps": 113, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [0.9564871191978455, 0.38076379895210266], "taskxy": [0.8622570037841797, 0.10500000417232513], "dest": [0.8622569333314896, 0.10500000149011612]}
          20 +{"seed": 19, "success": true, "steps": 97, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.6275245547294617, 0.46000000834465027], "taskxy": [0.5439521670341492, 0.11419502645730972], "dest": [0.5439521331787109, 0.10500000149011612]}
          21 +{"seed": 20, "success": true, "steps": 115, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.2820524573326111, 0.4599999785423279], "taskxy": [0.23252736032009125, 0.10872434824705124], "dest": [0.23252737927436828, 0.10500000149011612]}
          22 +{"seed": 21, "success": true, "steps": 77, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [1.5176098346710205, 0.3868604898452759], "taskxy": [1.460854411125183, 0.10500001907348633], "dest": [1.4608544368743897, 0.10500000149011612]}
          23 +{"seed": 22, "success": true, "steps": 161, "seconds": 0.48, "phase": "place", "task": "target_block", "robot": [0.2813137173652649, 0.5099999904632568], "taskxy": [0.19244615733623505, 0.11945580691099167], "dest": [0.1924461613893509, 0.10500000149011612]}
          24 +{"seed": 23, "success": true, "steps": 67, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [1.1582746505737305, 0.4099999964237213], "taskxy": [1.1181412935256958, 0.1122971922159195], "dest": [1.1181413192749023, 0.10500000149011612]}
          25 +{"seed": 24, "success": true, "steps": 119, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [1.245413899421692, 0.3829645812511444], "taskxy": [1.1548551321029663, 0.10500002652406693], "dest": [1.1548551578521729, 0.10500000149011612]}
          26 +{"seed": 25, "success": true, "steps": 90, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.4168006181716919, 0.48804014921188354], "taskxy": [0.3174859881401062, 0.10500001907348633], "dest": [0.3174859176874161, 0.10500000149011612]}
          27 +{"seed": 26, "success": true, "steps": 87, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [1.0472371578216553, 0.5194762349128723], "taskxy": [0.9775223135948181, 0.10499997437000275], "dest": [0.9775223393440247, 0.10500000149011612]}
          28 +{"seed": 27, "success": true, "steps": 45, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [0.5648511052131653, 0.4099999964237213], "taskxy": [0.5390996932983398, 0.1151600182056427], "dest": [0.5390996899008751, 0.10500000149011612]}
          29 +{"seed": 28, "success": true, "steps": 64, "seconds": 0.17, "phase": "place", "task": "target_block", "robot": [0.9479617476463318, 0.5149989724159241], "taskxy": [0.8572614789009094, 0.10499999672174454], "dest": [0.8572614450454712, 0.10500000149011612]}
          30 +{"seed": 29, "success": true, "steps": 92, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.33369460701942444, 0.4099999666213989], "taskxy": [0.2974048852920532, 0.12160825729370117], "dest": [0.297404851436615, 0.10500000149011612]}
          31 +{"seed": 30, "success": true, "steps": 51, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.752332866191864, 0.3864370286464691], "taskxy": [0.7028486728668213, 0.10499998927116394], "dest": [0.7028486992716789, 0.10500000149011612]}
          32 +{"seed": 31, "success": true, "steps": 62, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [1.517799973487854, 0.4099999666213989], "taskxy": [1.5210670232772827, 0.11852043122053146], "dest": [1.52106707072258, 0.10500000149011612]}
          33 +{"seed": 32, "success": true, "steps": 157, "seconds": 0.46, "phase": "place", "task": "target_block", "robot": [1.1594833135604858, 0.5175359845161438], "taskxy": [1.0761679410934448, 0.10499998927116394], "dest": [1.0761679668426514, 0.10500000149011612]}
          34 +{"seed": 33, "success": true, "steps": 153, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [0.3969971835613251, 0.5099999904632568], "taskxy": [0.30219539999961853, 0.1197897344827652], "dest": [0.302195374250412, 0.10500000149011612]}
          35 +{"seed": 34, "success": true, "steps": 51, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [0.9681728482246399, 0.5100000500679016], "taskxy": [0.8771185874938965, 0.11004173755645752], "dest": [0.8771186213493347, 0.10500000149011612]}
          36 +{"seed": 35, "success": true, "steps": 50, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [1.3312757015228271, 0.5099999904632568], "taskxy": [1.272279143333435, 0.1087510883808136], "dest": [1.2722791026830673, 0.10500000149011612]}
          37 +{"seed": 36, "success": true, "steps": 84, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [0.5443218350410461, 0.5099999904632568], "taskxy": [0.47916486859321594, 0.1136968731880188], "dest": [0.4791648726463318, 0.10500000149011612]}
          38 +{"seed": 37, "success": true, "steps": 50, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [0.4979923367500305, 0.3796648383140564], "taskxy": [0.3994463086128235, 0.10500000417232513], "dest": [0.39944628286361694, 0.10500000149011612]}
          39 +{"seed": 38, "success": true, "steps": 42, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [0.8291527628898621, 0.4599999785423279], "taskxy": [0.7415209412574768, 0.12051041424274445], "dest": [0.7415208410024643, 0.10500000149011612]}
          40 +{"seed": 39, "success": true, "steps": 116, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [0.5169748663902283, 0.4242390990257263], "taskxy": [0.4464716911315918, 0.10499998927116394], "dest": [0.4464717181921005, 0.10500000149011612]}
          41 +{"seed": 40, "success": true, "steps": 113, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [1.0161665678024292, 0.42075860500335693], "taskxy": [0.9554902911186218, 0.10499999672174454], "dest": [0.9554902572631836, 0.10500000149011612]}
          42 +{"seed": 41, "success": true, "steps": 47, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [0.6770239472389221, 0.4649990200996399], "taskxy": [0.6136682629585266, 0.10500001907348633], "dest": [0.6136682900190353, 0.10500000149011612]}
          43 +{"seed": 42, "success": true, "steps": 45, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.40955793857574463, 0.4879096746444702], "taskxy": [0.32747235894203186, 0.10500001907348633], "dest": [0.32747245240211487, 0.10500000149011612]}
          44 +{"seed": 43, "success": true, "steps": 52, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [0.8216844201087952, 0.4099999964237213], "taskxy": [0.7403000593185425, 0.10544615238904953], "dest": [0.7402999888658524, 0.10500000149011612]}
          45 +{"seed": 44, "success": true, "steps": 112, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [1.128604531288147, 0.4206942617893219], "taskxy": [1.0913760662078857, 0.10499999672174454], "dest": [1.091375988304615, 0.10500000149011612]}
          46 +{"seed": 45, "success": true, "steps": 167, "seconds": 0.53, "phase": "place", "task": "target_block", "robot": [0.8072885870933533, 0.46000000834465027], "taskxy": [0.722580075263977, 0.1057867482304573], "dest": [0.7225800346136093, 0.10500000149011612]}
          47 +{"seed": 46, "success": true, "steps": 54, "seconds": 0.16, "phase": "place", "task": "target_block", "robot": [0.9167006611824036, 0.46000000834465027], "taskxy": [0.8438284993171692, 0.12318698316812515], "dest": [0.8438284816741943, 0.10500000149011612]}
          48 +{"seed": 47, "success": true, "steps": 57, "seconds": 0.16, "phase": "place", "task": "target_block", "robot": [0.8696834444999695, 0.5100000500679016], "taskxy": [0.829658567905426, 0.1163361445069313], "dest": [0.8296585936546326, 0.10500000149011612]}
          49 +{"seed": 48, "success": true, "steps": 43, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [1.2655638456344604, 0.46000000834465027], "taskxy": [1.1963255405426025, 0.11580398678779602], "dest": [1.1963254470825195, 0.10500000149011612]}
          50 +{"seed": 49, "success": true, "steps": 37, "seconds": 0.11, "phase": "place", "task": "target_block", "robot": [0.9421949982643127, 0.5193631649017334], "taskxy": [0.8589698076248169, 0.10499998927116394], "dest": [0.8589697371721268, 0.10500000149011612]}
          51 +{"seed": 50, "success": true, "steps": 121, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [0.7234074473381042, 0.4599999785423279], "taskxy": [0.6935305595397949, 0.1116633340716362], "dest": [0.6935305269956589, 0.10500000149011612]}
          52 +{"seed": 51, "success": true, "steps": 53, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [0.7855204343795776, 0.47989875078201294], "taskxy": [0.7000908851623535, 0.10500003397464752], "dest": [0.7000909109115601, 0.10500000149011612]}
          53 +{"seed": 52, "success": true, "steps": 155, "seconds": 0.49, "phase": "place", "task": "target_block", "robot": [0.5762956738471985, 0.4599999785423279], "taskxy": [0.49785351753234863, 0.12045298516750336], "dest": [0.4978534768819809, 0.10500000149011612]}
          54 +{"seed": 53, "success": true, "steps": 172, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [0.7180459499359131, 0.37796008586883545], "taskxy": [0.6186805963516235, 0.10500001162290573], "dest": [0.6186806153059006, 0.10500000149011612]}
          55 +{"seed": 54, "success": true, "steps": 56, "seconds": 0.17, "phase": "place", "task": "target_block", "robot": [1.49070143699646, 0.38928577303886414], "taskxy": [1.4156248569488525, 0.10500000417232513], "dest": [1.415624882698059, 0.10500000149011612]}
          56 +{"seed": 55, "success": true, "steps": 38, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.6290306448936462, 0.4394878149032593], "taskxy": [0.5789648294448853, 0.10500001907348633], "dest": [0.5789648108184338, 0.10500000149011612]}
          57 +{"seed": 56, "success": true, "steps": 111, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [1.455591082572937, 0.3702753484249115], "taskxy": [1.4038506746292114, 0.10500003397464752], "dest": [1.403850700378418, 0.10500000149011612]}
          58 +{"seed": 57, "success": true, "steps": 38, "seconds": 0.11, "phase": "place", "task": "target_block", "robot": [0.6021356582641602, 0.4789509177207947], "taskxy": [0.5449443459510803, 0.10500002652406693], "dest": [0.5449443425536156, 0.10500000149011612]}
          59 +{"seed": 58, "success": true, "steps": 113, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [0.896597146987915, 0.4099999964237213], "taskxy": [0.8486972451210022, 0.12422782927751541], "dest": [0.848697211265564, 0.10500000149011612]}
          60 +{"seed": 59, "success": true, "steps": 108, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [1.2168526649475098, 0.46000000834465027], "taskxy": [1.1603264808654785, 0.11593063175678253], "dest": [1.160326506614685, 0.10500000149011612]}
diff --git a/rewrite_policy.py b/rewrite_policy.py
new file mode 100644
index 0000000..f7cb6cb
--- /dev/null
+++ b/rewrite_policy.py
@@ -0,0 +1,102 @@
           1 +p='approach.py'
           2 +s=open(p).read()
           3 +a=s.index('    def select(self,s):');b=s.index('    def get_action(self, s):')
           4 +s=s[:a]+'''    @staticmethod
           5 +    def overlap(a,b,margin=.003):
           6 +        return a[0]<b[0]+b[2]+margin and a[0]+a[2]>b[0]-margin and a[1]<b[1]+b[3]+margin and a[1]+a[3]>b[1]-margin
           7 +
           8 +    def conflicts(self,s,obj,x,y,offset,others):
           9 +        _,_,w,h=self.rect(s,obj)
          10 +        rx=x+offset;ry=y+h+.215
          11 +        gripper=(rx-.035,ry-.21,.07,.01)
          12 +        arm=(rx-.008,ry-.2,.016,.2)
          13 +        bad=[]
          14 +        for o in others:
          15 +            q=self.rect(s,o)
          16 +            dx=max(q[0]-rx,0,rx-q[0]-q[2])
          17 +            dy=max(q[1]-ry,0,ry-q[1]-q[3])
          18 +            if self.overlap((x,y,w,h),q) or self.overlap(gripper,q) or self.overlap(arm,q) or dx*dx+dy*dy<.103**2:
          19 +                bad.append(o)
          20 +        return bad
          21 +
          22 +    def offsets(self,x,px,w):
          23 +        low=max(.1002-x,.1002-px,-.022)
          24 +        high=min(1.5178-x,1.5178-px,w+.022)
          25 +        if low>high:return []
          26 +        return sorted(set([max(low,min(high,w/2))]+[float(z) for z in np.linspace(low,high,7)]),key=lambda z:abs(z-w/2))
          27 +
          28 +    def select(self,s):
          29 +        bx,by,bw,bh=self.rect(s,self.block)
          30 +        sx,sy,sw,sh=self.rect(s,self.surface)
          31 +        obs=self.obstacles(s)
          32 +        lo,hi=sx+.002,sx+sw-bw-.002
          33 +        candidates=[lo,hi,(lo+hi)/2]
          34 +        for o in obs:
          35 +            x,y,w,h=self.rect(s,o)
          36 +            candidates += [max(lo,min(hi,x-bw-.007)),max(lo,min(hi,x+w+.007))]
          37 +        plans=[]
          38 +        for gx in candidates:
          39 +            for offset in self.offsets(bx,gx,bw):
          40 +                bad=set(self.conflicts(s,self.block,gx,sy+sh+.005,offset,obs)+self.conflicts(s,self.block,bx,by,offset,obs))
          41 +                plans.append(((len(bad),abs(offset-bw/2)*.2+abs(gx-bx)*.01),gx,offset,bad))
          42 +        if not plans:
          43 +            gx=(lo+hi)/2;offset=max(.1002-bx,min(1.5178-gx,bw/2))
          44 +            plans=[((len(obs),0),gx,offset,set(obs))]
          45 +        _,gx,offset,bad=min(plans,key=lambda p:p[0])
          46 +        self.goal=(gx,sy+sh+.005)
          47 +        if not bad:
          48 +            o=self.block;self.dest=self.goal
          49 +        else:
          50 +            o=max(bad,key=lambda p:self.rect(s,p)[1]+self.rect(s,p)[3])
          51 +            # A taller neighbour may block the selected object's top grasp.
          52 +            for _ in range(len(obs)+1):
          53 +                x,y,w,h=self.rect(s,o)
          54 +                others=[p for p in obs+[self.block] if p!=o]
          55 +                grasps=[]
          56 +                for off in self.offsets(x,x,w):
          57 +                    blocking=self.conflicts(s,o,x,y,off,others)
          58 +                    grasps.append((len(blocking),abs(off-w/2),off,blocking))
          59 +                best=min(grasps,key=lambda z:z[:2])
          60 +                if not best[0]:break
          61 +                taller=[p for p in best[3] if self.rect(s,p)[1]+self.rect(s,p)[3]>y+h+.001 and p!=self.block]
          62 +                if not taller:break
          63 +                o=max(taller,key=lambda p:self.rect(s,p)[1]+self.rect(s,p)[3])
          64 +            x,y,w,h=self.rect(s,o)
          65 +            others=[p for p in obs+[self.block] if p!=o]
          66 +            occupied=[self.rect(s,p) for p in others]
          67 +            places=[]
          68 +            for px in np.linspace(.105,1.513-w,75):
          69 +                if px<gx+bw+.13 and px+w>gx-.13:continue
          70 +                py=max([.105]+[qy+qh+.022 for qx,qy,qw,qh in occupied if px<qx+qw+.025 and px+w>qx-.025])
          71 +                if py+h>.43:continue
          72 +                for off in self.offsets(x,px,w):
          73 +                    blockers=self.conflicts(s,o,x,y,off,others)+self.conflicts(s,o,px,py,off,others)
          74 +                    if not blockers:
          75 +                        places.append((py*8+abs(px-x)+abs(off-w/2)*.2,float(px),py,off))
          76 +            if places:
          77 +                _,px,py,offset=min(places)
          78 +                self.dest=(px,py)
          79 +            else:
          80 +                # If floor space is scarce, park above the lowest nearby stack.
          81 +                fallback=[]
          82 +                for px in np.linspace(.105,1.513-w,75):
          83 +                    if px<gx+bw+.07 and px+w>gx-.07:continue
          84 +                    py=max([.105]+[qy+qh+.025 for qx,qy,qw,qh in occupied if px<qx+qw+.04 and px+w>qx-.04])
          85 +                    for off in self.offsets(x,px,w):
          86 +                        blockers=self.conflicts(s,o,x,y,off,others)+self.conflicts(s,o,px,py,off,others)
          87 +                        fallback.append((len(blockers),py*8+abs(px-x),float(px),py,off))
          88 +                _,_,px,py,offset=min(fallback)
          89 +                self.dest=(px,py)
          90 +        self.task=o
          91 +        x,y,w,h=self.rect(s,o)
          92 +        self.pickx=max(.1002,min(1.5178,x+offset))
          93 +        self.offsetx=self.pickx-x
          94 +        self.picktop=y+h
          95 +        self.phase='above'
          96 +        self.stuck=0
          97 +
          98 +'''+s[b:]
          99 +# Delay vacuum until final descent, avoiding early grasp and floor collision.
         100 +s=s.replace("tx=self.pickx;ty=self.picktop+.215;vac=1.","tx=self.pickx;ty=self.picktop+.215;vac=0.")
         101 +s=s.replace("self.phase='lift';self.before_y=y","self.phase='lift';self.before_y=y;vac=1.")
         102 +open(p,'w').write(s)
diff --git a/test_counts_scene.jsonl b/test_counts_scene.jsonl
new file mode 100644
index 0000000..f65eec9
--- /dev/null
+++ b/test_counts_scene.jsonl
@@ -0,0 +1,34 @@
           1 +{"count": 3, "seed": 0, "steps": 39, "success": true, "seconds": 1.05}
           2 +{"count": 3, "seed": 1, "steps": 169, "success": true, "seconds": 2.68}
           3 +{"count": 3, "seed": 2, "steps": 181, "success": true, "seconds": 3.13}
           4 +{"count": 3, "seed": 3, "steps": 119, "success": true, "seconds": 1.83}
           5 +{"count": 3, "seed": 4, "steps": 117, "success": true, "seconds": 1.85}
           6 +{"count": 3, "seed": 5, "steps": 41, "success": true, "seconds": 0.95}
           7 +{"count": 3, "seed": 6, "steps": 150, "success": true, "seconds": 2.38}
           8 +{"count": 3, "seed": 7, "steps": 167, "success": true, "seconds": 2.69}
           9 +{"count": 3, "seed": 8, "steps": 157, "success": true, "seconds": 2.27}
          10 +{"count": 3, "seed": 9, "steps": 164, "success": true, "seconds": 2.4}
          11 +{"count": 3, "seed": 10, "steps": 130, "success": true, "seconds": 2.01}
          12 +{"count": 3, "seed": 11, "steps": 102, "success": true, "seconds": 1.58}
          13 +{"count": 3, "seed": 12, "steps": 181, "success": true, "seconds": 3.08}
          14 +{"count": 3, "seed": 13, "steps": 147, "success": true, "seconds": 2.26}
          15 +{"count": 3, "seed": 14, "steps": 169, "success": true, "seconds": 2.66}
          16 +{"count": 4, "seed": 0, "steps": 157, "success": true, "seconds": 2.68}
          17 +{"count": 4, "seed": 1, "steps": 212, "success": true, "seconds": 3.09}
          18 +{"count": 4, "seed": 2, "steps": 89, "success": true, "seconds": 2.51}
          19 +{"count": 4, "seed": 3, "steps": 1000, "success": false, "seconds": 9.06, "phase": "place", "task": "target_block", "dest": [1.3095843521356583, 0.10500000149011612], "robot": [1.3366822004318237, 0.5099999904632568], "init": {"obstruction0": [1.152086615562439, 0.10000099986791611, 0.1514977365732193, 0.15962274372577667], "obstruction1": [1.3116801977157593, 0.10000099986791611, 0.08749981224536896, 0.19032169878482819], "obstruction2": [0.43964964151382446, 0.10000099986791611, 0.1306634545326233, 0.1996031254529953], "obstruction3": [0.7467350363731384, 0.10000099986791611, 0.1965513676404953, 0.15759406983852386], "target_block": [0.19977444410324097, 0.10000099986791611, 0.05419572442770004, 0.07431439310312271], "target_surface": [1.2884182929992676, 0.0, 0.08759234845638275, 0.10000000149011612]}, "final": {"obstruction0": [1.152086615562439, 0.10000099986791611, 0.1514977365732193, 0.15962274372577667], "obstruction1": [1.0319945812225342, 0.10499999672174454, 0.08749981224536896, 0.19032169878482819], "obstruction2": [0.43964964151382446, 0.10000099986791611, 0.1306634545326233, 0.1996031254529953], "obstruction3": [0.7467350363731384, 0.10000099986791611, 0.1965513676404953, 0.15759406983852386], "target_block": [1.309584379196167, 0.22068558633327484, 0.05419572442770004, 0.07431439310312271], "target_surface": [1.2884182929992676, 0.0, 0.08759234845638275, 0.10000000149011612]}}
          20 +{"count": 4, "seed": 4, "steps": 1000, "success": false, "seconds": 8.63, "phase": "down", "task": "obstruction2", "dest": [1.0537458757486906, 0.105], "robot": [1.3541035652160645, 0.7099999785423279], "init": {"obstruction0": [1.4178024530410767, 0.10000099986791611, 0.06802277266979218, 0.05388985574245453], "obstruction1": [1.4920032024383545, 0.10000099986791611, 0.07113966345787048, 0.12770894169807434], "obstruction2": [1.3257176876068115, 0.10000099986791611, 0.05677169933915138, 0.05042976886034012], "obstruction3": [1.2369496822357178, 0.10000099986791611, 0.08748079836368561, 0.16814841330051422], "target_block": [0.27295616269111633, 0.10000099986791611, 0.14293360710144043, 0.1114027351140976], "target_surface": [1.3184852600097656, 0.0, 0.18072666227817535, 0.10000000149011612]}, "final": {"obstruction0": [1.1349036693572998, 0.10500004887580872, 0.06802277266979218, 0.05388985574245453], "obstruction1": [1.4920032024383545, 0.10000099986791611, 0.07113966345787048, 0.12770894169807434], "obstruction2": [1.3257176876068115, 0.10000099986791611, 0.05677169933915138, 0.05042976886034012], "obstruction3": [1.2369496822357178, 0.10000099986791611, 0.08748079836368561, 0.16814841330051422], "target_block": [0.27295616269111633, 0.10000099986791611, 0.14293360710144043, 0.1114027351140976], "target_surface": [1.3184852600097656, 0.0, 0.18072666227817535, 0.10000000149011612]}}
          21 +{"count": 4, "seed": 5, "steps": 130, "success": true, "seconds": 1.94}
          22 +{"count": 4, "seed": 6, "steps": 172, "success": true, "seconds": 2.63}
          23 +{"count": 4, "seed": 7, "steps": 132, "success": true, "seconds": 2.21}
          24 +{"count": 4, "seed": 8, "steps": 157, "success": true, "seconds": 2.38}
          25 +{"count": 4, "seed": 9, "steps": 143, "success": true, "seconds": 3.72}
          26 +{"count": 4, "seed": 10, "steps": 157, "success": true, "seconds": 2.28}
          27 +{"count": 4, "seed": 11, "steps": 101, "success": true, "seconds": 1.87}
          28 +{"count": 4, "seed": 12, "steps": 167, "success": true, "seconds": 3.04}
          29 +{"count": 4, "seed": 13, "steps": 139, "success": true, "seconds": 2.9}
          30 +{"count": 4, "seed": 14, "steps": 103, "success": true, "seconds": 4.06}
          31 +{"count": 6, "seed": 0, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
          32 +{"count": 6, "seed": 1, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
          33 +{"count": 6, "seed": 2, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
          34 +{"count": 6, "seed": 3, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
diff --git a/test_counts_scene.log b/test_counts_scene.log
new file mode 100644
index 0000000..f65eec9
--- /dev/null
+++ b/test_counts_scene.log
@@ -0,0 +1,34 @@
           1 +{"count": 3, "seed": 0, "steps": 39, "success": true, "seconds": 1.05}
           2 +{"count": 3, "seed": 1, "steps": 169, "success": true, "seconds": 2.68}
           3 +{"count": 3, "seed": 2, "steps": 181, "success": true, "seconds": 3.13}
           4 +{"count": 3, "seed": 3, "steps": 119, "success": true, "seconds": 1.83}
           5 +{"count": 3, "seed": 4, "steps": 117, "success": true, "seconds": 1.85}
           6 +{"count": 3, "seed": 5, "steps": 41, "success": true, "seconds": 0.95}
           7 +{"count": 3, "seed": 6, "steps": 150, "success": true, "seconds": 2.38}
           8 +{"count": 3, "seed": 7, "steps": 167, "success": true, "seconds": 2.69}
           9 +{"count": 3, "seed": 8, "steps": 157, "success": true, "seconds": 2.27}
          10 +{"count": 3, "seed": 9, "steps": 164, "success": true, "seconds": 2.4}
          11 +{"count": 3, "seed": 10, "steps": 130, "success": true, "seconds": 2.01}
          12 +{"count": 3, "seed": 11, "steps": 102, "success": true, "seconds": 1.58}
          13 +{"count": 3, "seed": 12, "steps": 181, "success": true, "seconds": 3.08}
          14 +{"count": 3, "seed": 13, "steps": 147, "success": true, "seconds": 2.26}
          15 +{"count": 3, "seed": 14, "steps": 169, "success": true, "seconds": 2.66}
          16 +{"count": 4, "seed": 0, "steps": 157, "success": true, "seconds": 2.68}
          17 +{"count": 4, "seed": 1, "steps": 212, "success": true, "seconds": 3.09}
          18 +{"count": 4, "seed": 2, "steps": 89, "success": true, "seconds": 2.51}
          19 +{"count": 4, "seed": 3, "steps": 1000, "success": false, "seconds": 9.06, "phase": "place", "task": "target_block", "dest": [1.3095843521356583, 0.10500000149011612], "robot": [1.3366822004318237, 0.5099999904632568], "init": {"obstruction0": [1.152086615562439, 0.10000099986791611, 0.1514977365732193, 0.15962274372577667], "obstruction1": [1.3116801977157593, 0.10000099986791611, 0.08749981224536896, 0.19032169878482819], "obstruction2": [0.43964964151382446, 0.10000099986791611, 0.1306634545326233, 0.1996031254529953], "obstruction3": [0.7467350363731384, 0.10000099986791611, 0.1965513676404953, 0.15759406983852386], "target_block": [0.19977444410324097, 0.10000099986791611, 0.05419572442770004, 0.07431439310312271], "target_surface": [1.2884182929992676, 0.0, 0.08759234845638275, 0.10000000149011612]}, "final": {"obstruction0": [1.152086615562439, 0.10000099986791611, 0.1514977365732193, 0.15962274372577667], "obstruction1": [1.0319945812225342, 0.10499999672174454, 0.08749981224536896, 0.19032169878482819], "obstruction2": [0.43964964151382446, 0.10000099986791611, 0.1306634545326233, 0.1996031254529953], "obstruction3": [0.7467350363731384, 0.10000099986791611, 0.1965513676404953, 0.15759406983852386], "target_block": [1.309584379196167, 0.22068558633327484, 0.05419572442770004, 0.07431439310312271], "target_surface": [1.2884182929992676, 0.0, 0.08759234845638275, 0.10000000149011612]}}
          20 +{"count": 4, "seed": 4, "steps": 1000, "success": false, "seconds": 8.63, "phase": "down", "task": "obstruction2", "dest": [1.0537458757486906, 0.105], "robot": [1.3541035652160645, 0.7099999785423279], "init": {"obstruction0": [1.4178024530410767, 0.10000099986791611, 0.06802277266979218, 0.05388985574245453], "obstruction1": [1.4920032024383545, 0.10000099986791611, 0.07113966345787048, 0.12770894169807434], "obstruction2": [1.3257176876068115, 0.10000099986791611, 0.05677169933915138, 0.05042976886034012], "obstruction3": [1.2369496822357178, 0.10000099986791611, 0.08748079836368561, 0.16814841330051422], "target_block": [0.27295616269111633, 0.10000099986791611, 0.14293360710144043, 0.1114027351140976], "target_surface": [1.3184852600097656, 0.0, 0.18072666227817535, 0.10000000149011612]}, "final": {"obstruction0": [1.1349036693572998, 0.10500004887580872, 0.06802277266979218, 0.05388985574245453], "obstruction1": [1.4920032024383545, 0.10000099986791611, 0.07113966345787048, 0.12770894169807434], "obstruction2": [1.3257176876068115, 0.10000099986791611, 0.05677169933915138, 0.05042976886034012], "obstruction3": [1.2369496822357178, 0.10000099986791611, 0.08748079836368561, 0.16814841330051422], "target_block": [0.27295616269111633, 0.10000099986791611, 0.14293360710144043, 0.1114027351140976], "target_surface": [1.3184852600097656, 0.0, 0.18072666227817535, 0.10000000149011612]}}
          21 +{"count": 4, "seed": 5, "steps": 130, "success": true, "seconds": 1.94}
          22 +{"count": 4, "seed": 6, "steps": 172, "success": true, "seconds": 2.63}
          23 +{"count": 4, "seed": 7, "steps": 132, "success": true, "seconds": 2.21}
          24 +{"count": 4, "seed": 8, "steps": 157, "success": true, "seconds": 2.38}
          25 +{"count": 4, "seed": 9, "steps": 143, "success": true, "seconds": 3.72}
          26 +{"count": 4, "seed": 10, "steps": 157, "success": true, "seconds": 2.28}
          27 +{"count": 4, "seed": 11, "steps": 101, "success": true, "seconds": 1.87}
          28 +{"count": 4, "seed": 12, "steps": 167, "success": true, "seconds": 3.04}
          29 +{"count": 4, "seed": 13, "steps": 139, "success": true, "seconds": 2.9}
          30 +{"count": 4, "seed": 14, "steps": 103, "success": true, "seconds": 4.06}
          31 +{"count": 6, "seed": 0, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
          32 +{"count": 6, "seed": 1, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
          33 +{"count": 6, "seed": 2, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
          34 +{"count": 6, "seed": 3, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
diff --git a/test_counts_scene.py b/test_counts_scene.py
new file mode 100644
index 0000000..5c5ece3
--- /dev/null
+++ b/test_counts_scene.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import json,time
           4 +f=open('test_counts_scene.jsonl','w')
           5 +for count in [3,4,6,8]:
           6 + for seed in range(15):
           7 +  e=make_env();start=time.time()
           8 +  try:
           9 +   s,i=e.reset(seed=seed,options={'object_count':count});a=GeneratedApproach(e.action_space,e.observation_space,{})
          10 +   a.reset(s,i);init={str(o.name):a.rect(s,o) for o in s.get_objects(a.types['rectangle'])}
          11 +   term=False
          12 +   for k in range(e.max_steps):
          13 +    s,r,term,trunc,i=e.step(a.get_action(s))
          14 +    if term or trunc:break
          15 +   row={'count':count,'seed':seed,'steps':k+1,'success':term,'seconds':round(time.time()-start,2)}
          16 +   if not term:row.update(phase=a.phase,task=str(a.task.name),dest=a.dest,robot=[s.get(a.robot,z) for z in ['x','y']],init=init,final={str(o.name):a.rect(s,o) for o in s.get_objects(a.types['rectangle'])})
          17 +  except Exception as exc: row={'count':count,'seed':seed,'error':str(exc)}
          18 +  finally:e.close()
          19 +  f.write(json.dumps(row)+'\n');f.flush();print(json.dumps(row),flush=True)
```

</details>

<a id="C006"></a>
### C006 · Reserve target pickup clearance when parking removed obstructions

Commit `41ec7aaba58f7c4e90a7656565f0ab9ccf715908`; parents: ab62469ecce03eeee0f7ececba4deeb569f06baf. Recorded author date: 2026-09-21T17:27:01Z.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0052](01_timeline.md#E0052): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_41ec7aa_approach.py) · [Exact all-file diff](evidence/diffs/C006_41ec7aa.diff)

[Previous saved controller snapshot](evidence/versions/C005_ab62469_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 71860bb..6ad96db 100644
--- a/approach.py
+++ b/approach.py
@@ -26,19 +26,18 @@ class GeneratedApproach:
   26     26      def overlap(a,b,margin=.003):
   27     27          return a[0]<b[0]+b[2]+margin and a[0]+a[2]>b[0]-margin and a[1]<b[1]+b[3]+margin and a[1]+a[3]>b[1]-margin
   28     28  
          29 +    def hits_configuration(self,q,x,y,w,h,offset):
          30 +        rx=x+offset;ry=y+h+.215
          31 +        dx=max(q[0]-rx,0,rx-q[0]-q[2])
          32 +        dy=max(q[1]-ry,0,ry-q[1]-q[3])
          33 +        return (self.overlap((x,y,w,h),q)
          34 +                or self.overlap((rx-.035,ry-.21,.07,.01),q)
          35 +                or self.overlap((rx-.008,ry-.2,.016,.2),q)
          36 +                or dx*dx+dy*dy<.103**2)
          37 +
   29     38      def conflicts(self,s,obj,x,y,offset,others):
   30     39          _,_,w,h=self.rect(s,obj)
   31        -        rx=x+offset;ry=y+h+.215
   32        -        gripper=(rx-.035,ry-.21,.07,.01)
   33        -        arm=(rx-.008,ry-.2,.016,.2)
   34        -        bad=[]
   35        -        for o in others:
   36        -            q=self.rect(s,o)
   37        -            dx=max(q[0]-rx,0,rx-q[0]-q[2])
   38        -            dy=max(q[1]-ry,0,ry-q[1]-q[3])
   39        -            if self.overlap((x,y,w,h),q) or self.overlap(gripper,q) or self.overlap(arm,q) or dx*dx+dy*dy<.103**2:
   40        -                bad.append(o)
   41        -        return bad
          40 +        return [o for o in others if self.hits_configuration(self.rect(s,o),x,y,w,h,offset)]
   42     41  
   43     42      def offsets(self,x,px,w):
   44     43          low=max(.1002-x,.1002-px,-.022)
@@ -65,6 +64,8 @@ class GeneratedApproach:
   65     64              plans=[((len(obs),0),gx,offset,set(obs))]
   66     65          _,gx,offset,bad=min(plans,key=lambda p:p[0])
   67     66          self.goal=(gx,sy+sh+.005)
          67 +        keep_pick=(bx,by,bw,bh,offset)
          68 +        keep_place=(gx,sy+sh+.005,bw,bh,offset)
   68     69          if not bad:
   69     70              o=self.block;self.dest=self.goal
   70     71          else:
@@ -90,6 +91,7 @@ class GeneratedApproach:
   90     91                  if px<gx+bw+.13 and px+w>gx-.13:continue
   91     92                  py=max([.105]+[qy+qh+.022 for qx,qy,qw,qh in occupied if px<qx+qw+.025 and px+w>qx-.025])
   92     93                  if py+h>.43:continue
          94 +                if self.hits_configuration((px,py,w,h),*keep_pick) or self.hits_configuration((px,py,w,h),*keep_place):continue
   93     95                  for off in self.offsets(x,px,w):
   94     96                      blockers=self.conflicts(s,o,x,y,off,others)+self.conflicts(s,o,px,py,off,others)
   95     97                      if not blockers:
@@ -103,6 +105,7 @@ class GeneratedApproach:
  103    105                  for px in np.linspace(.105,1.513-w,75):
  104    106                      if px<gx+bw+.07 and px+w>gx-.07:continue
  105    107                      py=max([.105]+[qy+qh+.025 for qx,qy,qw,qh in occupied if px<qx+qw+.04 and px+w>qx-.04])
         108 +                    if self.hits_configuration((px,py,w,h),*keep_pick) or self.hits_configuration((px,py,w,h),*keep_place):continue
  106    109                      for off in self.offsets(x,px,w):
  107    110                          blockers=self.conflicts(s,o,x,y,off,others)+self.conflicts(s,o,px,py,off,others)
  108    111                          fallback.append((len(blockers),py*8+abs(px-x),float(px),py,off))
diff --git a/probe_validation_239_260_459.jsonl b/probe_validation_239_260_459.jsonl
new file mode 100644
index 0000000..5df5736
--- /dev/null
+++ b/probe_validation_239_260_459.jsonl
@@ -0,0 +1,120 @@
           1 +{"seed": 239, "success": true, "steps": 115, "seconds": 1.47, "phase": "place", "task": "target_block", "robot": [0.1668248027563095, 0.38093802332878113], "taskxy": [0.15599282085895538, 0.10500002652406693], "dest": [0.15599279779195785, 0.10500000149011612]}
           2 +{"seed": 260, "success": true, "steps": 96, "seconds": 1.39, "phase": "place", "task": "target_block", "robot": [0.20646949112415314, 0.46000003814697266], "taskxy": [0.14486879110336304, 0.10866768658161163], "dest": [0.1448687504529953, 0.10500000149011612]}
           3 +{"seed": 261, "success": true, "steps": 125, "seconds": 1.39, "phase": "place", "task": "target_block", "robot": [1.3919466733932495, 0.4769737422466278], "taskxy": [1.3416986465454102, 0.10499998927116394], "dest": [1.3416986722946167, 0.10500000149011612]}
           4 +{"seed": 262, "success": true, "steps": 114, "seconds": 1.49, "phase": "place", "task": "target_block", "robot": [0.7046521902084351, 0.4099999964237213], "taskxy": [0.6676232218742371, 0.11769488453865051], "dest": [0.6676231317520142, 0.10500000149011612]}
           5 +{"seed": 263, "success": true, "steps": 96, "seconds": 1.47, "phase": "place", "task": "target_block", "robot": [0.9665014743804932, 0.42356497049331665], "taskxy": [0.8788727521896362, 0.10500001907348633], "dest": [0.878872718334198, 0.10500000149011612]}
           6 +{"seed": 264, "success": true, "steps": 61, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [1.4424644708633423, 0.5099999904632568], "taskxy": [1.372986912727356, 0.10877612978219986], "dest": [1.3729869384765625, 0.10500000149011612]}
           7 +{"seed": 265, "success": true, "steps": 154, "seconds": 1.81, "phase": "place", "task": "target_block", "robot": [0.9962602257728577, 0.4609554708003998], "taskxy": [0.9276090264320374, 0.10499995201826096], "dest": [0.9276089925765991, 0.10500000149011612]}
           8 +{"seed": 266, "success": true, "steps": 101, "seconds": 1.55, "phase": "place", "task": "target_block", "robot": [0.7869789004325867, 0.5099999904632568], "taskxy": [0.7370191812515259, 0.11924762278795242], "dest": [0.7370191473960876, 0.10500000149011612]}
           9 +{"seed": 267, "success": true, "steps": 96, "seconds": 1.46, "phase": "place", "task": "target_block", "robot": [0.5722533464431763, 0.5099999904632568], "taskxy": [0.506056010723114, 0.10555486381053925], "dest": [0.5060559768676758, 0.10500000149011612]}
          10 +{"seed": 268, "success": true, "steps": 175, "seconds": 2.44, "phase": "place", "task": "target_block", "robot": [0.38274726271629333, 0.5191410779953003], "taskxy": [0.30395936965942383, 0.10500001907348633], "dest": [0.3039593439102173, 0.10500000149011612]}
          11 +{"seed": 269, "success": true, "steps": 110, "seconds": 0.98, "phase": "place", "task": "target_block", "robot": [0.8137311339378357, 0.3704873025417328], "taskxy": [0.7295321226119995, 0.10499995201826096], "dest": [0.7295321713685989, 0.10500000149011612]}
          12 +{"seed": 270, "success": true, "steps": 99, "seconds": 0.73, "phase": "place", "task": "target_block", "robot": [0.34268081188201904, 0.4154650866985321], "taskxy": [0.26159849762916565, 0.10499999672174454], "dest": [0.2615984867811203, 0.10500000149011612]}
          13 +{"seed": 271, "success": true, "steps": 107, "seconds": 1.05, "phase": "place", "task": "target_block", "robot": [0.2940387427806854, 0.41176778078079224], "taskxy": [0.24563854932785034, 0.10500001162290573], "dest": [0.24563857573270798, 0.10500000149011612]}
          14 +{"seed": 272, "success": true, "steps": 35, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [1.150151014328003, 0.5176444053649902], "taskxy": [1.0988149642944336, 0.10499995946884155], "dest": [1.0988151092529297, 0.10500000149011612]}
          15 +{"seed": 273, "success": true, "steps": 54, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [1.4732701778411865, 0.43444886803627014], "taskxy": [1.3840725421905518, 0.10499999672174454], "dest": [1.3840724487304688, 0.10500000149011612]}
          16 +{"seed": 274, "success": true, "steps": 54, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [0.24332614243030548, 0.477049320936203], "taskxy": [0.2147076427936554, 0.10499995201826096], "dest": [0.21470768305659294, 0.10500000149011612]}
          17 +{"seed": 275, "success": true, "steps": 60, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [0.3664751648902893, 0.41051146388053894], "taskxy": [0.3079841732978821, 0.10500001907348633], "dest": [0.30798413944244385, 0.10500000149011612]}
          18 +{"seed": 276, "success": true, "steps": 37, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.9892939925193787, 0.5130295753479004], "taskxy": [0.93091881275177, 0.10499998927116394], "dest": [0.9309187077283859, 0.10500000149011612]}
          19 +{"seed": 277, "success": true, "steps": 59, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.8304593563079834, 0.4099999964237213], "taskxy": [0.795076310634613, 0.12204722315073013], "dest": [0.7950763363838196, 0.10500000149011612]}
          20 +{"seed": 278, "success": true, "steps": 37, "seconds": 0.36, "phase": "place", "task": "target_block", "robot": [1.4918053150177002, 0.5132402181625366], "taskxy": [1.4112334251403809, 0.10500001907348633], "dest": [1.4112335003614425, 0.10500000149011612]}
          21 +{"seed": 279, "success": true, "steps": 99, "seconds": 0.82, "phase": "place", "task": "target_block", "robot": [0.420990914106369, 0.46458151936531067], "taskxy": [0.35212716460227966, 0.10499997437000275], "dest": [0.3521271686553955, 0.10500000149011612]}
          22 +{"seed": 280, "success": true, "steps": 49, "seconds": 0.49, "phase": "place", "task": "target_block", "robot": [1.1088048219680786, 0.4784339368343353], "taskxy": [1.0706390142440796, 0.10499993711709976], "dest": [1.0706390298604964, 0.10500000149011612]}
          23 +{"seed": 281, "success": true, "steps": 110, "seconds": 1.01, "phase": "place", "task": "target_block", "robot": [0.492141991853714, 0.37818920612335205], "taskxy": [0.403380811214447, 0.10499998182058334], "dest": [0.4033807854652405, 0.10500000149011612]}
          24 +{"seed": 282, "success": true, "steps": 90, "seconds": 0.92, "phase": "place", "task": "target_block", "robot": [0.38454127311706543, 0.486489474773407], "taskxy": [0.3537065386772156, 0.10500003397464752], "dest": [0.3537065576314926, 0.10500000149011612]}
          25 +{"seed": 283, "success": true, "steps": 75, "seconds": 0.49, "phase": "place", "task": "target_block", "robot": [1.3864120244979858, 0.4255913197994232], "taskxy": [1.2941601276397705, 0.10499998182058334], "dest": [1.294160153388977, 0.10500000149011612]}
          26 +{"seed": 284, "success": true, "steps": 50, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [0.6078687310218811, 0.4099999964237213], "taskxy": [0.5217065215110779, 0.11462900042533875], "dest": [0.5217065472602844, 0.10500000149011612]}
          27 +{"seed": 285, "success": true, "steps": 125, "seconds": 1.06, "phase": "place", "task": "target_block", "robot": [1.009474515914917, 0.4882239103317261], "taskxy": [0.9658775925636292, 0.10499999672174454], "dest": [0.9658775891661644, 0.10500000149011612]}
          28 +{"seed": 286, "success": true, "steps": 50, "seconds": 0.59, "phase": "place", "task": "target_block", "robot": [1.2314084768295288, 0.4099999964237213], "taskxy": [1.1772443056106567, 0.10617012530565262], "dest": [1.1772443313598633, 0.10500000149011612]}
          29 +{"seed": 287, "success": true, "steps": 137, "seconds": 1.65, "phase": "place", "task": "target_block", "robot": [0.18717947602272034, 0.4621281921863556], "taskxy": [0.13079257309436798, 0.10499998182058334], "dest": [0.1307925321161747, 0.10500000149011612]}
          30 +{"seed": 288, "success": true, "steps": 44, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [1.0804330110549927, 0.41304251551628113], "taskxy": [1.0270190238952637, 0.10500000417232513], "dest": [1.0270189608931541, 0.10500000149011612]}
          31 +{"seed": 289, "success": true, "steps": 54, "seconds": 0.58, "phase": "place", "task": "target_block", "robot": [0.3689393699169159, 0.37934720516204834], "taskxy": [0.333075612783432, 0.10500004142522812], "dest": [0.33307558703422546, 0.10500000149011612]}
          32 +{"seed": 290, "success": true, "steps": 61, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [1.3682904243469238, 0.4099999964237213], "taskxy": [1.3338006734848022, 0.11689493805170059], "dest": [1.3338005800247192, 0.10500000149011612]}
          33 +{"seed": 291, "success": true, "steps": 54, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [0.9961521029472351, 0.3819141089916229], "taskxy": [0.9554237127304077, 0.10499996691942215], "dest": [0.9554236788749695, 0.10500000149011612]}
          34 +{"seed": 292, "success": true, "steps": 135, "seconds": 1.18, "phase": "place", "task": "target_block", "robot": [1.3690439462661743, 0.4107983708381653], "taskxy": [1.3160985708236694, 0.10500001907348633], "dest": [1.316098596572876, 0.10500000149011612]}
          35 +{"seed": 293, "success": true, "steps": 56, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [1.0617640018463135, 0.42949041724205017], "taskxy": [1.0247303247451782, 0.10499998927116394], "dest": [1.0247303504943848, 0.10500000149011612]}
          36 +{"seed": 294, "success": true, "steps": 53, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [1.3249820470809937, 0.4201604723930359], "taskxy": [1.242795467376709, 0.10500001907348633], "dest": [1.2427954931259155, 0.10500000149011612]}
          37 +{"seed": 295, "success": true, "steps": 71, "seconds": 0.52, "phase": "place", "task": "target_block", "robot": [0.517683744430542, 0.48791879415512085], "taskxy": [0.4601781368255615, 0.10500001162290573], "dest": [0.4601781185269356, 0.10500000149011612]}
          38 +{"seed": 296, "success": true, "steps": 48, "seconds": 0.54, "phase": "place", "task": "target_block", "robot": [0.5613390207290649, 0.46164003014564514], "taskxy": [0.4785318970680237, 0.10499998182058334], "dest": [0.4785319526195526, 0.10500000149011612]}
          39 +{"seed": 297, "success": true, "steps": 57, "seconds": 0.52, "phase": "place", "task": "target_block", "robot": [1.4843109846115112, 0.4599999785423279], "taskxy": [1.3920979499816895, 0.11964461207389832], "dest": [1.3920978565216064, 0.10500000149011612]}
          40 +{"seed": 298, "success": true, "steps": 103, "seconds": 0.91, "phase": "place", "task": "target_block", "robot": [1.0350075960159302, 0.4171169400215149], "taskxy": [1.0057158470153809, 0.10499999672174454], "dest": [1.0057158398926258, 0.10500000149011612]}
          41 +{"seed": 299, "success": true, "steps": 114, "seconds": 1.13, "phase": "place", "task": "target_block", "robot": [0.35475966334342957, 0.48631390929222107], "taskxy": [0.2669532299041748, 0.10499995946884155], "dest": [0.26695320415496826, 0.10500000149011612]}
          42 +{"seed": 300, "success": true, "steps": 47, "seconds": 0.43, "phase": "place", "task": "target_block", "robot": [0.8936876058578491, 0.4742531478404999], "taskxy": [0.8328515887260437, 0.10499997437000275], "dest": [0.8328514952659607, 0.10500000149011612]}
          43 +{"seed": 301, "success": true, "steps": 76, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [0.18627993762493134, 0.3761947453022003], "taskxy": [0.1538957953453064, 0.10499996691942215], "dest": [0.15389579194784164, 0.10500000149011612]}
          44 +{"seed": 302, "success": true, "steps": 107, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [0.7731902003288269, 0.41276904940605164], "taskxy": [0.7437592148780823, 0.10499997437000275], "dest": [0.7437592003047466, 0.10500000149011612]}
          45 +{"seed": 303, "success": true, "steps": 121, "seconds": 0.62, "phase": "place", "task": "target_block", "robot": [0.38469311594963074, 0.4599999785423279], "taskxy": [0.3498140871524811, 0.1218726858496666], "dest": [0.3498141061067581, 0.10500000149011612]}
          46 +{"seed": 304, "success": true, "steps": 93, "seconds": 0.75, "phase": "place", "task": "target_block", "robot": [1.1474123001098633, 0.5099999904632568], "taskxy": [1.0517457723617554, 0.11395873129367828], "dest": [1.051745798110962, 0.10500000149011612]}
          47 +{"seed": 305, "success": true, "steps": 46, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.35821810364723206, 0.4599999785423279], "taskxy": [0.2632489502429962, 0.11747202277183533], "dest": [0.26324899899959564, 0.10500000149011612]}
          48 +{"seed": 306, "success": true, "steps": 96, "seconds": 0.71, "phase": "place", "task": "target_block", "robot": [1.3522207736968994, 0.511391282081604], "taskxy": [1.3064438104629517, 0.10500000417232513], "dest": [1.306443796277046, 0.10500000149011612]}
          49 +{"seed": 307, "success": true, "steps": 114, "seconds": 0.76, "phase": "place", "task": "target_block", "robot": [0.5665631890296936, 0.5099999904632568], "taskxy": [0.49748751521110535, 0.1196226179599762], "dest": [0.49748757886886597, 0.10500000149011612]}
          50 +{"seed": 308, "success": true, "steps": 106, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [1.290595531463623, 0.48604506254196167], "taskxy": [1.1991163492202759, 0.10499998927116394], "dest": [1.1991163749694824, 0.10500000149011612]}
          51 +{"seed": 309, "success": true, "steps": 125, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [1.3671461343765259, 0.5099999904632568], "taskxy": [1.2690550088882446, 0.11256975680589676], "dest": [1.2690550346374512, 0.10500000149011612]}
          52 +{"seed": 310, "success": true, "steps": 41, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [0.793923020362854, 0.47272157669067383], "taskxy": [0.7359315752983093, 0.10499999672174454], "dest": [0.735931489944458, 0.10500000149011612]}
          53 +{"seed": 311, "success": true, "steps": 112, "seconds": 0.87, "phase": "place", "task": "target_block", "robot": [0.5073915123939514, 0.3823091685771942], "taskxy": [0.4081820249557495, 0.10499995946884155], "dest": [0.40818208861351013, 0.10500000149011612]}
          54 +{"seed": 312, "success": true, "steps": 72, "seconds": 0.43, "phase": "place", "task": "target_block", "robot": [1.4693986177444458, 0.46117880940437317], "taskxy": [1.4436348676681519, 0.10499999672174454], "dest": [1.4436348934173584, 0.10500000149011612]}
          55 +{"seed": 313, "success": true, "steps": 45, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [0.18323567509651184, 0.4730072319507599], "taskxy": [0.15031012892723083, 0.10500001162290573], "dest": [0.15031013298034668, 0.10500000149011612]}
          56 +{"seed": 314, "success": true, "steps": 64, "seconds": 0.46, "phase": "place", "task": "target_block", "robot": [0.600214421749115, 0.38512155413627625], "taskxy": [0.5405755043029785, 0.10499998927116394], "dest": [0.5405755300521851, 0.10500000149011612]}
          57 +{"seed": 315, "success": true, "steps": 38, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [0.7293165922164917, 0.4823475778102875], "taskxy": [0.6978800296783447, 0.10499997437000275], "dest": [0.6978800039291382, 0.10500000149011612]}
          58 +{"seed": 316, "success": true, "steps": 46, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.6356379389762878, 0.5099999904632568], "taskxy": [0.5817077159881592, 0.11186989396810532], "dest": [0.5817077498435974, 0.10500000149011612]}
          59 +{"seed": 317, "success": true, "steps": 37, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [1.394159197807312, 0.4158160984516144], "taskxy": [1.3610461950302124, 0.10499996691942215], "dest": [1.361046220779419, 0.10500000149011612]}
          60 +{"seed": 318, "success": true, "steps": 71, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [1.209058165550232, 0.4599999785423279], "taskxy": [1.111480474472046, 0.12144854664802551], "dest": [1.1114805002212524, 0.10500000149011612]}
          61 +{"seed": 319, "success": false, "steps": 1000, "seconds": 7.68, "phase": "retreat", "task": "obstruction1", "robot": [0.7737568020820618, 0.6079561710357666], "taskxy": [0.7957567572593689, 0.10499999672174454], "dest": [0.7957568021207242, 0.105]}
          62 +{"seed": 320, "success": true, "steps": 35, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.8800582885742188, 0.5099999904632568], "taskxy": [0.8098044395446777, 0.12333826720714569], "dest": [0.8098045330047607, 0.10500000149011612]}
          63 +{"seed": 321, "success": true, "steps": 114, "seconds": 0.78, "phase": "place", "task": "target_block", "robot": [0.7267362475395203, 0.4100000262260437], "taskxy": [0.6505126953125, 0.11680873483419418], "dest": [0.6505127440690994, 0.10500000149011612]}
          64 +{"seed": 322, "success": true, "steps": 43, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [1.0728050470352173, 0.4599999785423279], "taskxy": [1.0314122438430786, 0.12197653949260712], "dest": [1.0314122695922852, 0.10500000149011612]}
          65 +{"seed": 323, "success": true, "steps": 58, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.34236881136894226, 0.5132068991661072], "taskxy": [0.2718922197818756, 0.10500001162290573], "dest": [0.2718922983407974, 0.10500000149011612]}
          66 +{"seed": 324, "success": true, "steps": 130, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [1.5161855220794678, 0.4898565411567688], "taskxy": [1.4886822700500488, 0.10500000417232513], "dest": [1.4886822957992554, 0.10500000149011612]}
          67 +{"seed": 325, "success": true, "steps": 45, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.7079545855522156, 0.42777302861213684], "taskxy": [0.6459164619445801, 0.10499998927116394], "dest": [0.6459165107011795, 0.10500000149011612]}
          68 +{"seed": 326, "success": true, "steps": 73, "seconds": 0.43, "phase": "place", "task": "target_block", "robot": [0.679954469203949, 0.46000000834465027], "taskxy": [0.6208028197288513, 0.1100674718618393], "dest": [0.6208028237819672, 0.10500000149011612]}
          69 +{"seed": 327, "success": true, "steps": 52, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.9083618521690369, 0.47017601132392883], "taskxy": [0.8197245001792908, 0.10499994456768036], "dest": [0.8197245259284973, 0.10500000149011612]}
          70 +{"seed": 328, "success": true, "steps": 38, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [0.924819827079773, 0.5099999904632568], "taskxy": [0.865313708782196, 0.10891865193843842], "dest": [0.8653137351870537, 0.10500000149011612]}
          71 +{"seed": 329, "success": true, "steps": 102, "seconds": 0.78, "phase": "place", "task": "target_block", "robot": [0.44284236431121826, 0.5171633362770081], "taskxy": [0.36773356795310974, 0.10500000417232513], "dest": [0.3677335374355316, 0.10500000149011612]}
          72 +{"seed": 330, "success": true, "steps": 115, "seconds": 0.73, "phase": "place", "task": "target_block", "robot": [0.24568285048007965, 0.4099999666213989], "taskxy": [0.20743131637573242, 0.12213821709156036], "dest": [0.20743132042884826, 0.10500000149011612]}
          73 +{"seed": 331, "success": true, "steps": 35, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [0.3515565097332001, 0.478592187166214], "taskxy": [0.2664846181869507, 0.10499995201826096], "dest": [0.2664846520423889, 0.10500000149011612]}
          74 +{"seed": 332, "success": true, "steps": 97, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [1.1005173921585083, 0.4881539046764374], "taskxy": [1.0080639123916626, 0.10500000417232513], "dest": [1.0080640058517456, 0.10500000149011612]}
          75 +{"seed": 333, "success": true, "steps": 33, "seconds": 0.16, "phase": "place", "task": "target_block", "robot": [1.3470020294189453, 0.46000000834465027], "taskxy": [1.2630146741867065, 0.10780331492424011], "dest": [1.263014699935913, 0.10500000149011612]}
          76 +{"seed": 334, "success": true, "steps": 35, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [0.26984304189682007, 0.519265353679657], "taskxy": [0.2011958509683609, 0.10499999672174454], "dest": [0.20119589495658874, 0.10500000149011612]}
          77 +{"seed": 335, "success": true, "steps": 42, "seconds": 0.22, "phase": "place", "task": "target_block", "robot": [0.3087906539440155, 0.432595819234848], "taskxy": [0.2595124840736389, 0.10499998927116394], "dest": [0.25951251047849655, 0.10500000149011612]}
          78 +{"seed": 336, "success": true, "steps": 111, "seconds": 0.72, "phase": "place", "task": "target_block", "robot": [0.5934719443321228, 0.37605854868888855], "taskxy": [0.5204938650131226, 0.10499994456768036], "dest": [0.5204938311576843, 0.10500000149011612]}
          79 +{"seed": 337, "success": true, "steps": 77, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.3567902743816376, 0.5099999904632568], "taskxy": [0.2657935321331024, 0.11249882727861404], "dest": [0.26579353618621826, 0.10500000149011612]}
          80 +{"seed": 338, "success": true, "steps": 40, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [1.1712125539779663, 0.3796985149383545], "taskxy": [1.0815515518188477, 0.10500004887580872], "dest": [1.0815515775680542, 0.10500000149011612]}
          81 +{"seed": 339, "success": true, "steps": 58, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.8108394145965576, 0.46000000834465027], "taskxy": [0.7675414085388184, 0.113197922706604], "dest": [0.767541434943676, 0.10500000149011612]}
          82 +{"seed": 340, "success": true, "steps": 39, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [1.0653237104415894, 0.37675711512565613], "taskxy": [0.9754631519317627, 0.10500003397464752], "dest": [0.9754631857872009, 0.10500000149011612]}
          83 +{"seed": 341, "success": true, "steps": 96, "seconds": 0.83, "phase": "place", "task": "target_block", "robot": [0.3389563262462616, 0.423636257648468], "taskxy": [0.2740456759929657, 0.10499997437000275], "dest": [0.27404568004608154, 0.10500000149011612]}
          84 +{"seed": 342, "success": true, "steps": 184, "seconds": 1.32, "phase": "place", "task": "target_block", "robot": [0.23260344564914703, 0.46000000834465027], "taskxy": [0.17010419070720673, 0.11850132793188095], "dest": [0.17010415750741958, 0.10500000149011612]}
          85 +{"seed": 343, "success": true, "steps": 54, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [0.21994648873806, 0.4100000262260437], "taskxy": [0.1751694679260254, 0.11989148706197739], "dest": [0.17516949433088302, 0.10500000149011612]}
          86 +{"seed": 344, "success": true, "steps": 55, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [1.3018485307693481, 0.4100000262260437], "taskxy": [1.2444264888763428, 0.11345072835683823], "dest": [1.2444265146255493, 0.10500000149011612]}
          87 +{"seed": 345, "success": true, "steps": 54, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [1.0308574438095093, 0.47729843854904175], "taskxy": [1.0037689208984375, 0.10500003397464752], "dest": [1.003768946647644, 0.10500000149011612]}
          88 +{"seed": 346, "success": true, "steps": 132, "seconds": 0.8, "phase": "place", "task": "target_block", "robot": [1.3004465103149414, 0.5110181570053101], "taskxy": [1.227562427520752, 0.10499998182058334], "dest": [1.2275624532699585, 0.10500000149011612]}
          89 +{"seed": 347, "success": true, "steps": 93, "seconds": 0.71, "phase": "place", "task": "target_block", "robot": [0.5847686529159546, 0.4099999964237213], "taskxy": [0.5332255959510803, 0.12362729012966156], "dest": [0.5332256217002869, 0.10500000149011612]}
          90 +{"seed": 348, "success": true, "steps": 49, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.6970056891441345, 0.5099999904632568], "taskxy": [0.6259430050849915, 0.11906317621469498], "dest": [0.6259429346323013, 0.10500000149011612]}
          91 +{"seed": 349, "success": true, "steps": 59, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [0.4264829754829407, 0.42374247312545776], "taskxy": [0.3346993923187256, 0.10499998182058334], "dest": [0.33469941806793213, 0.10500000149011612]}
          92 +{"seed": 350, "success": true, "steps": 95, "seconds": 0.68, "phase": "place", "task": "target_block", "robot": [1.2051740884780884, 0.37077680230140686], "taskxy": [1.1500871181488037, 0.10500005632638931], "dest": [1.1500871438980103, 0.10500000149011612]}
          93 +{"seed": 351, "success": true, "steps": 119, "seconds": 0.74, "phase": "place", "task": "target_block", "robot": [0.2357281744480133, 0.48420560359954834], "taskxy": [0.19747114181518555, 0.10500001907348633], "dest": [0.19747116822004318, 0.10500000149011612]}
          94 +{"seed": 352, "success": true, "steps": 58, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.29718780517578125, 0.4676550626754761], "taskxy": [0.20680363476276398, 0.10499997437000275], "dest": [0.2068036686182022, 0.10500000149011612]}
          95 +{"seed": 353, "success": true, "steps": 43, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [0.4751858115196228, 0.5099999904632568], "taskxy": [0.44934824109077454, 0.10712219774723053], "dest": [0.449348252594471, 0.10500000149011612]}
          96 +{"seed": 354, "success": true, "steps": 172, "seconds": 1.38, "phase": "place", "task": "target_block", "robot": [1.2424331903457642, 0.4684006869792938], "taskxy": [1.1681216955184937, 0.10499998927116394], "dest": [1.1681217212677002, 0.10500000149011612]}
          97 +{"seed": 355, "success": true, "steps": 55, "seconds": 0.41, "phase": "place", "task": "target_block", "robot": [1.3716999292373657, 0.3794129192829132], "taskxy": [1.3339169025421143, 0.10499994456768036], "dest": [1.3339169282913208, 0.10500000149011612]}
          98 +{"seed": 356, "success": true, "steps": 50, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [1.2542973756790161, 0.38310542702674866], "taskxy": [1.1752009391784668, 0.10499995946884155], "dest": [1.1752009649276733, 0.10500000149011612]}
          99 +{"seed": 357, "success": true, "steps": 120, "seconds": 0.67, "phase": "place", "task": "target_block", "robot": [0.3316482901573181, 0.4099999964237213], "taskxy": [0.3289629817008972, 0.11692105978727341], "dest": [0.32896299320459366, 0.10500000149011612]}
         100 +{"seed": 358, "success": true, "steps": 90, "seconds": 0.75, "phase": "place", "task": "target_block", "robot": [1.389143705368042, 0.486097127199173], "taskxy": [1.3612420558929443, 0.10500000417232513], "dest": [1.3612419624328613, 0.10500000149011612]}
         101 +{"seed": 359, "success": true, "steps": 105, "seconds": 0.78, "phase": "place", "task": "target_block", "robot": [1.308441162109375, 0.43355727195739746], "taskxy": [1.2634875774383545, 0.10499998182058334], "dest": [1.2634876112937927, 0.10500000149011612]}
         102 +{"seed": 360, "success": true, "steps": 106, "seconds": 0.68, "phase": "place", "task": "target_block", "robot": [0.3861427307128906, 0.43217071890830994], "taskxy": [0.34029051661491394, 0.10499999672174454], "dest": [0.3402904786467552, 0.10500000149011612]}
         103 +{"seed": 361, "success": true, "steps": 156, "seconds": 1.14, "phase": "place", "task": "target_block", "robot": [0.758104145526886, 0.4106521010398865], "taskxy": [0.7003186941146851, 0.10500006377696991], "dest": [0.7003187198638916, 0.10500000149011612]}
         104 +{"seed": 362, "success": true, "steps": 162, "seconds": 1.23, "phase": "place", "task": "target_block", "robot": [0.871920645236969, 0.3759083151817322], "taskxy": [0.787159264087677, 0.10500004887580872], "dest": [0.7871591489315033, 0.10500000149011612]}
         105 +{"seed": 363, "success": true, "steps": 62, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [1.1427361965179443, 0.5140930414199829], "taskxy": [1.0492112636566162, 0.10500001907348633], "dest": [1.0492112894058228, 0.10500000149011612]}
         106 +{"seed": 364, "success": true, "steps": 50, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.9731898903846741, 0.4099999666213989], "taskxy": [0.9161137938499451, 0.1114002913236618], "dest": [0.9161137796640396, 0.10500000149011612]}
         107 +{"seed": 365, "success": true, "steps": 69, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [1.4279255867004395, 0.3862181603908539], "taskxy": [1.3494309186935425, 0.10499998927116394], "dest": [1.349430944442749, 0.10500000149011612]}
         108 +{"seed": 366, "success": true, "steps": 41, "seconds": 0.22, "phase": "place", "task": "target_block", "robot": [0.75588458776474, 0.5099999904632568], "taskxy": [0.6691274642944336, 0.10906171053647995], "dest": [0.669127438545227, 0.10500000149011612]}
         109 +{"seed": 367, "success": true, "steps": 192, "seconds": 1.28, "phase": "place", "task": "target_block", "robot": [1.3824125528335571, 0.4351896047592163], "taskxy": [1.2946926355361938, 0.10500001907348633], "dest": [1.2946926612854004, 0.10500000149011612]}
         110 +{"seed": 368, "success": true, "steps": 148, "seconds": 0.78, "phase": "place", "task": "target_block", "robot": [1.184515357017517, 0.5165359973907471], "taskxy": [1.1053075790405273, 0.10500000417232513], "dest": [1.1053074855804443, 0.10500000149011612]}
         111 +{"seed": 369, "success": true, "steps": 178, "seconds": 1.25, "phase": "place", "task": "target_block", "robot": [1.1377695798873901, 0.5099999904632568], "taskxy": [1.0438092947006226, 0.1124066486954689], "dest": [1.043809320449829, 0.10500000149011612]}
         112 +{"seed": 370, "success": true, "steps": 110, "seconds": 0.53, "phase": "place", "task": "target_block", "robot": [1.3422964811325073, 0.48133257031440735], "taskxy": [1.2666141986846924, 0.10499994456768036], "dest": [1.266614224433899, 0.10500000149011612]}
         113 +{"seed": 371, "success": true, "steps": 35, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.7827033400535583, 0.4345360994338989], "taskxy": [0.7195940017700195, 0.10499999672174454], "dest": [0.7195939909219742, 0.10500000149011612]}
         114 +{"seed": 372, "success": true, "steps": 135, "seconds": 0.89, "phase": "place", "task": "target_block", "robot": [1.4600592851638794, 0.38346046209335327], "taskxy": [1.40603768825531, 0.10499998927116394], "dest": [1.4060377140045166, 0.10500000149011612]}
         115 +{"seed": 373, "success": true, "steps": 113, "seconds": 0.68, "phase": "place", "task": "target_block", "robot": [0.580845832824707, 0.48446857929229736], "taskxy": [0.5003811717033386, 0.10500000417232513], "dest": [0.5003811676502228, 0.10500000149011612]}
         116 +{"seed": 374, "success": true, "steps": 93, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [0.4415781795978546, 0.4616100788116455], "taskxy": [0.34783172607421875, 0.10499997437000275], "dest": [0.347831685423851, 0.10500000149011612]}
         117 +{"seed": 375, "success": true, "steps": 47, "seconds": 0.22, "phase": "place", "task": "target_block", "robot": [0.6132703423500061, 0.5169161558151245], "taskxy": [0.5731595754623413, 0.10499999672174454], "dest": [0.5731595416069031, 0.10500000149011612]}
         118 +{"seed": 376, "success": true, "steps": 113, "seconds": 0.79, "phase": "place", "task": "target_block", "robot": [0.962884247303009, 0.3838501572608948], "taskxy": [0.9230465292930603, 0.10499998927116394], "dest": [0.9230465550422668, 0.10500000149011612]}
         119 +{"seed": 377, "success": true, "steps": 125, "seconds": 0.74, "phase": "place", "task": "target_block", "robot": [0.7124477624893188, 0.4322310984134674], "taskxy": [0.6667981147766113, 0.10499997437000275], "dest": [0.6667979996204376, 0.10500000149011612]}
         120 +{"seed": 378, "success": true, "steps": 139, "seconds": 0.88, "phase": "place", "task": "target_block", "robot": [1.320676565170288, 0.4099999666213989], "taskxy": [1.2750359773635864, 0.10723832994699478], "dest": [1.275036003112793, 0.10500000149011612]}
diff --git a/results_geometry.jsonl b/results_geometry.jsonl
new file mode 100644
index 0000000..1e3d911
--- /dev/null
+++ b/results_geometry.jsonl
@@ -0,0 +1,60 @@
           1 +{"seed": 0, "success": true, "steps": 164, "seconds": 1.18, "phase": "place", "task": "target_block", "robot": [0.7908052802085876, 0.4099999666213989], "taskxy": [0.7405964732170105, 0.12245805561542511], "dest": [0.740596498966217, 0.10500000149011612]}
           2 +{"seed": 1, "success": true, "steps": 115, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [0.9666023254394531, 0.47871848940849304], "taskxy": [0.8694781064987183, 0.10499997437000275], "dest": [0.86947807264328, 0.10500000149011612]}
           3 +{"seed": 2, "success": true, "steps": 152, "seconds": 1.15, "phase": "place", "task": "target_block", "robot": [0.9954461455345154, 0.5160517692565918], "taskxy": [0.9415640234947205, 0.10499998182058334], "dest": [0.941564049243927, 0.10500000149011612]}
           4 +{"seed": 3, "success": true, "steps": 91, "seconds": 0.66, "phase": "place", "task": "target_block", "robot": [1.2916558980941772, 0.4622512459754944], "taskxy": [1.216448187828064, 0.10499998182058334], "dest": [1.2164482135772705, 0.10500000149011612]}
           5 +{"seed": 4, "success": true, "steps": 79, "seconds": 0.62, "phase": "place", "task": "target_block", "robot": [1.4231510162353516, 0.4099999666213989], "taskxy": [1.3380084037780762, 0.11882078647613525], "dest": [1.3380084295272827, 0.10500000149011612]}
           6 +{"seed": 5, "success": true, "steps": 181, "seconds": 1.3, "phase": "place", "task": "target_block", "robot": [0.24981091916561127, 0.3767913579940796], "taskxy": [0.19417540729045868, 0.10500004887580872], "dest": [0.19417539644241333, 0.10500000149011612]}
           7 +{"seed": 6, "success": true, "steps": 99, "seconds": 0.66, "phase": "place", "task": "target_block", "robot": [1.1417207717895508, 0.41949447989463806], "taskxy": [1.0661464929580688, 0.10499996691942215], "dest": [1.0661463994979858, 0.10500000149011612]}
           8 +{"seed": 7, "success": true, "steps": 187, "seconds": 1.37, "phase": "place", "task": "target_block", "robot": [0.2030080407857895, 0.4099999666213989], "taskxy": [0.14074254035949707, 0.10787275433540344], "dest": [0.14074252951145172, 0.10500000149011612]}
           9 +{"seed": 8, "success": true, "steps": 155, "seconds": 1.15, "phase": "place", "task": "target_block", "robot": [0.29301247000694275, 0.46457356214523315], "taskxy": [0.2498759627342224, 0.10499998927116394], "dest": [0.24987597423791885, 0.10500000149011612]}
          10 +{"seed": 9, "success": true, "steps": 136, "seconds": 0.86, "phase": "place", "task": "target_block", "robot": [1.5061836242675781, 0.38179731369018555], "taskxy": [1.4225263595581055, 0.10499996691942215], "dest": [1.422526385307312, 0.10500000149011612]}
          11 +{"seed": 10, "success": true, "steps": 56, "seconds": 0.45, "phase": "place", "task": "target_block", "robot": [0.3620208203792572, 0.4366528391838074], "taskxy": [0.31965428590774536, 0.10500001162290573], "dest": [0.31965430825948715, 0.10500000149011612]}
          12 +{"seed": 11, "success": true, "steps": 64, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [1.4770435094833374, 0.38946613669395447], "taskxy": [1.446761965751648, 0.10500003397464752], "dest": [1.4467619915008545, 0.10500000149011612]}
          13 +{"seed": 12, "success": true, "steps": 140, "seconds": 0.93, "phase": "place", "task": "target_block", "robot": [1.4482805728912354, 0.38726189732551575], "taskxy": [1.3729971647262573, 0.10500000417232513], "dest": [1.3729971904754639, 0.10500000149011612]}
          14 +{"seed": 13, "success": true, "steps": 109, "seconds": 0.81, "phase": "place", "task": "target_block", "robot": [1.0472872257232666, 0.43553492426872253], "taskxy": [0.9509224891662598, 0.10499998927116394], "dest": [0.9509224817156792, 0.10500000149011612]}
          15 +{"seed": 14, "success": true, "steps": 42, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.8645417094230652, 0.47744715213775635], "taskxy": [0.7823681831359863, 0.10500000417232513], "dest": [0.7823681126832962, 0.10500000149011612]}
          16 +{"seed": 15, "success": true, "steps": 42, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [0.7686994075775146, 0.4099999964237213], "taskxy": [0.6975525617599487, 0.1074572280049324], "dest": [0.697552561044693, 0.10500000149011612]}
          17 +{"seed": 16, "success": true, "steps": 40, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.2922910451889038, 0.5099999904632568], "taskxy": [0.2016936093568802, 0.11689255386590958], "dest": [0.20169359850883484, 0.10500000149011612]}
          18 +{"seed": 17, "success": true, "steps": 110, "seconds": 0.85, "phase": "place", "task": "target_block", "robot": [1.2162363529205322, 0.4617014527320862], "taskxy": [1.1591240167617798, 0.10499998927116394], "dest": [1.1591239951252936, 0.10500000149011612]}
          19 +{"seed": 18, "success": true, "steps": 113, "seconds": 0.88, "phase": "place", "task": "target_block", "robot": [0.9564869999885559, 0.38076379895210266], "taskxy": [0.8622569441795349, 0.10500001907348633], "dest": [0.8622569333314896, 0.10500000149011612]}
          20 +{"seed": 19, "success": true, "steps": 97, "seconds": 0.67, "phase": "place", "task": "target_block", "robot": [0.6275244951248169, 0.46000000834465027], "taskxy": [0.5439521074295044, 0.11419503390789032], "dest": [0.5439521331787109, 0.10500000149011612]}
          21 +{"seed": 20, "success": true, "steps": 115, "seconds": 0.8, "phase": "place", "task": "target_block", "robot": [0.2820524573326111, 0.4599999785423279], "taskxy": [0.23252736032009125, 0.10872436314821243], "dest": [0.23252737927436828, 0.10500000149011612]}
          22 +{"seed": 21, "success": true, "steps": 77, "seconds": 0.4, "phase": "place", "task": "target_block", "robot": [1.5176098346710205, 0.3868604898452759], "taskxy": [1.460854411125183, 0.10500003397464752], "dest": [1.4608544368743897, 0.10500000149011612]}
          23 +{"seed": 22, "success": true, "steps": 161, "seconds": 1.34, "phase": "place", "task": "target_block", "robot": [0.2813136875629425, 0.5099999904632568], "taskxy": [0.19244618713855743, 0.11945578455924988], "dest": [0.1924461613893509, 0.10500000149011612]}
          24 +{"seed": 23, "success": true, "steps": 67, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [1.15827476978302, 0.4099999964237213], "taskxy": [1.1181412935256958, 0.11229719966650009], "dest": [1.1181413192749023, 0.10500000149011612]}
          25 +{"seed": 24, "success": true, "steps": 120, "seconds": 0.78, "phase": "place", "task": "target_block", "robot": [1.2454140186309814, 0.382964551448822], "taskxy": [1.1548552513122559, 0.10499998182058334], "dest": [1.1548551578521729, 0.10500000149011612]}
          26 +{"seed": 25, "success": true, "steps": 90, "seconds": 0.6, "phase": "place", "task": "target_block", "robot": [0.4168006181716919, 0.48804014921188354], "taskxy": [0.3174859583377838, 0.10500000417232513], "dest": [0.3174859176874161, 0.10500000149011612]}
          27 +{"seed": 26, "success": false, "steps": 1000, "seconds": 12.62, "phase": "lift", "task": "obstruction1", "robot": [0.9065601825714111, 0.85999995470047], "taskxy": [0.928560197353363, 0.10000099986791611], "dest": [0.6336692657502921, 0.105]}
          28 +{"seed": 27, "success": true, "steps": 45, "seconds": 0.59, "phase": "place", "task": "target_block", "robot": [0.5648511648178101, 0.4099999964237213], "taskxy": [0.5390996932983398, 0.1151600182056427], "dest": [0.5390996899008751, 0.10500000149011612]}
          29 +{"seed": 28, "success": true, "steps": 64, "seconds": 1.02, "phase": "place", "task": "target_block", "robot": [0.9479617476463318, 0.512631893157959], "taskxy": [0.8572614789009094, 0.10499998182058334], "dest": [0.8572614450454712, 0.10500000149011612]}
          30 +{"seed": 29, "success": true, "steps": 92, "seconds": 1.44, "phase": "place", "task": "target_block", "robot": [0.3336946368217468, 0.4099999666213989], "taskxy": [0.2974048852920532, 0.12160825729370117], "dest": [0.297404851436615, 0.10500000149011612]}
          31 +{"seed": 30, "success": true, "steps": 51, "seconds": 0.55, "phase": "place", "task": "target_block", "robot": [0.752332866191864, 0.3864370882511139], "taskxy": [0.7028487324714661, 0.10500002652406693], "dest": [0.7028486992716789, 0.10500000149011612]}
          32 +{"seed": 31, "success": true, "steps": 62, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [1.517799973487854, 0.4099999666213989], "taskxy": [1.5220670700073242, 0.11852043867111206], "dest": [1.5220670707225799, 0.10500000149011612]}
          33 +{"seed": 32, "success": true, "steps": 157, "seconds": 1.69, "phase": "place", "task": "target_block", "robot": [1.1594833135604858, 0.5175359845161438], "taskxy": [1.0761679410934448, 0.10500000417232513], "dest": [1.0761679668426514, 0.10500000149011612]}
          34 +{"seed": 33, "success": true, "steps": 97, "seconds": 0.88, "phase": "place", "task": "target_block", "robot": [0.3969971537590027, 0.5099999904632568], "taskxy": [0.30219534039497375, 0.11978977918624878], "dest": [0.302195374250412, 0.10500000149011612]}
          35 +{"seed": 34, "success": true, "steps": 51, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [0.9681728482246399, 0.5100000500679016], "taskxy": [0.8771185874938965, 0.11004174500703812], "dest": [0.8771186213493347, 0.10500000149011612]}
          36 +{"seed": 35, "success": true, "steps": 50, "seconds": 0.41, "phase": "place", "task": "target_block", "robot": [1.3312757015228271, 0.5099999904632568], "taskxy": [1.272279143333435, 0.1087510958313942], "dest": [1.2722791026830673, 0.10500000149011612]}
          37 +{"seed": 36, "success": true, "steps": 84, "seconds": 0.88, "phase": "place", "task": "target_block", "robot": [0.5443218350410461, 0.5099999904632568], "taskxy": [0.47916486859321594, 0.1136968582868576], "dest": [0.4791648726463318, 0.10500000149011612]}
          38 +{"seed": 37, "success": true, "steps": 50, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [0.49799245595932007, 0.3796647787094116], "taskxy": [0.39944636821746826, 0.10499995946884155], "dest": [0.39944628286361694, 0.10500000149011612]}
          39 +{"seed": 38, "success": true, "steps": 42, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.8291526436805725, 0.4599999785423279], "taskxy": [0.741520881652832, 0.12051041424274445], "dest": [0.7415208410024643, 0.10500000149011612]}
          40 +{"seed": 39, "success": true, "steps": 116, "seconds": 1.26, "phase": "place", "task": "target_block", "robot": [0.5159749388694763, 0.4242390990257263], "taskxy": [0.44547176361083984, 0.10499999672174454], "dest": [0.4454717181921005, 0.10500000149011612]}
          41 +{"seed": 40, "success": true, "steps": 112, "seconds": 0.91, "phase": "place", "task": "target_block", "robot": [1.0161664485931396, 0.42075857520103455], "taskxy": [0.9554901719093323, 0.10499995946884155], "dest": [0.9554902572631836, 0.10500000149011612]}
          42 +{"seed": 41, "success": true, "steps": 47, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.6760239601135254, 0.4603749215602875], "taskxy": [0.6126682758331299, 0.10499994456768036], "dest": [0.6126682900190353, 0.10500000149011612]}
          43 +{"seed": 42, "success": true, "steps": 45, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.4095580577850342, 0.48790961503982544], "taskxy": [0.3274724781513214, 0.10499999672174454], "dest": [0.32747245240211487, 0.10500000149011612]}
          44 +{"seed": 43, "success": true, "steps": 52, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.8216844201087952, 0.4099999964237213], "taskxy": [0.7403000593185425, 0.10544615983963013], "dest": [0.7402999888658524, 0.10500000149011612]}
          45 +{"seed": 44, "success": true, "steps": 111, "seconds": 1.14, "phase": "place", "task": "target_block", "robot": [1.1286042928695679, 0.4206942915916443], "taskxy": [1.0913759469985962, 0.10499998927116394], "dest": [1.091375988304615, 0.10500000149011612]}
          46 +{"seed": 45, "success": true, "steps": 167, "seconds": 1.72, "phase": "place", "task": "target_block", "robot": [0.8072885870933533, 0.46000000834465027], "taskxy": [0.722580075263977, 0.10578674077987671], "dest": [0.7225800346136093, 0.10500000149011612]}
          47 +{"seed": 46, "success": true, "steps": 55, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [0.9157004952430725, 0.4599999785423279], "taskxy": [0.8428284525871277, 0.12318695336580276], "dest": [0.8428284816741943, 0.10500000149011612]}
          48 +{"seed": 47, "success": true, "steps": 57, "seconds": 0.6, "phase": "place", "task": "target_block", "robot": [0.8696834444999695, 0.5100000500679016], "taskxy": [0.829658567905426, 0.1163361594080925], "dest": [0.8296585936546326, 0.10500000149011612]}
          49 +{"seed": 48, "success": true, "steps": 43, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [1.2655638456344604, 0.46000000834465027], "taskxy": [1.1963255405426025, 0.11580400913953781], "dest": [1.1963254470825195, 0.10500000149011612]}
          50 +{"seed": 49, "success": true, "steps": 37, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [0.942194938659668, 0.5193631649017334], "taskxy": [0.8589698076248169, 0.10499998927116394], "dest": [0.8589697371721268, 0.10500000149011612]}
          51 +{"seed": 50, "success": true, "steps": 121, "seconds": 1.13, "phase": "place", "task": "target_block", "robot": [0.7224075198173523, 0.4599999785423279], "taskxy": [0.6925305724143982, 0.1116633266210556], "dest": [0.6925305269956589, 0.10500000149011612]}
          52 +{"seed": 51, "success": true, "steps": 53, "seconds": 0.57, "phase": "place", "task": "target_block", "robot": [0.7855204343795776, 0.47989872097969055], "taskxy": [0.7000909447669983, 0.10500000417232513], "dest": [0.7000909109115601, 0.10500000149011612]}
          53 +{"seed": 52, "success": true, "steps": 157, "seconds": 1.65, "phase": "place", "task": "target_block", "robot": [0.5762956738471985, 0.4599999785423279], "taskxy": [0.49785345792770386, 0.12045300006866455], "dest": [0.4978534768819809, 0.10500000149011612]}
          54 +{"seed": 53, "success": true, "steps": 172, "seconds": 1.71, "phase": "place", "task": "target_block", "robot": [0.7180458903312683, 0.37796008586883545], "taskxy": [0.6186805367469788, 0.10500000417232513], "dest": [0.6186806153059006, 0.10500000149011612]}
          55 +{"seed": 54, "success": true, "steps": 56, "seconds": 0.55, "phase": "place", "task": "target_block", "robot": [1.49070143699646, 0.38928577303886414], "taskxy": [1.415624976158142, 0.10500001907348633], "dest": [1.415624882698059, 0.10500000149011612]}
          56 +{"seed": 55, "success": true, "steps": 38, "seconds": 0.46, "phase": "place", "task": "target_block", "robot": [0.6290306448936462, 0.4394877552986145], "taskxy": [0.5789648294448853, 0.10499997437000275], "dest": [0.5789648108184338, 0.10500000149011612]}
          57 +{"seed": 56, "success": true, "steps": 111, "seconds": 0.96, "phase": "place", "task": "target_block", "robot": [1.455591082572937, 0.3702752888202667], "taskxy": [1.4038506746292114, 0.10499998927116394], "dest": [1.403850700378418, 0.10500000149011612]}
          58 +{"seed": 57, "success": true, "steps": 38, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.6021356582641602, 0.4789509177207947], "taskxy": [0.5449443459510803, 0.10500002652406693], "dest": [0.5449443425536156, 0.10500000149011612]}
          59 +{"seed": 58, "success": true, "steps": 114, "seconds": 0.77, "phase": "place", "task": "target_block", "robot": [0.896597146987915, 0.4100000262260437], "taskxy": [0.8486971855163574, 0.1242278441786766], "dest": [0.848697211265564, 0.10500000149011612]}
          60 +{"seed": 59, "success": true, "steps": 108, "seconds": 1.45, "phase": "place", "task": "target_block", "robot": [1.2168526649475098, 0.46000000834465027], "taskxy": [1.1603264808654785, 0.11593062430620193], "dest": [1.160326506614685, 0.10500000149011612]}
diff --git a/test_counts_scene.jsonl b/test_counts_scene.jsonl
index f65eec9..5744013 100644
--- a/test_counts_scene.jsonl
+++ b/test_counts_scene.jsonl
@@ -32,3 +32,4 @@
   32     32  {"count": 6, "seed": 1, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
   33     33  {"count": 6, "seed": 2, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
   34     34  {"count": 6, "seed": 3, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
          35 +{"count": 6, "seed": 4, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
diff --git a/test_counts_scene.log b/test_counts_scene.log
index f65eec9..5744013 100644
--- a/test_counts_scene.log
+++ b/test_counts_scene.log
@@ -32,3 +32,4 @@
   32     32  {"count": 6, "seed": 1, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
   33     33  {"count": 6, "seed": 2, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
   34     34  {"count": 6, "seed": 3, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
          35 +{"count": 6, "seed": 4, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=6; it likely exceeds the family's feasible object count. Lower the configured counts."}
diff --git a/test_counts_scene.py b/test_counts_scene.py
index 5c5ece3..e4feca4 100644
--- a/test_counts_scene.py
+++ b/test_counts_scene.py
@@ -1,9 +1,9 @@
    1      1  from env_client import make_env
    2      2  from approach import GeneratedApproach
    3      3  import json,time
    4        -f=open('test_counts_scene.jsonl','w')
    5        -for count in [3,4,6,8]:
    6        - for seed in range(15):
           4 +f=open('test_counts_scene_v2.jsonl','w')
           5 +for count in [4,5]:
           6 + for seed in range(31 if count==4 else 11):
    7      7    e=make_env();start=time.time()
    8      8    try:
    9      9     s,i=e.reset(seed=seed,options={'object_count':count});a=GeneratedApproach(e.action_space,e.observation_space,{})
diff --git a/test_counts_scene_v2.jsonl b/test_counts_scene_v2.jsonl
new file mode 100644
index 0000000..f6ec3d5
--- /dev/null
+++ b/test_counts_scene_v2.jsonl
@@ -0,0 +1,29 @@
           1 +{"count": 4, "seed": 0, "steps": 159, "success": true, "seconds": 5.41}
           2 +{"count": 4, "seed": 1, "steps": 174, "success": true, "seconds": 5.16}
           3 +{"count": 4, "seed": 2, "steps": 1000, "success": false, "seconds": 18.9, "phase": "retreat", "task": "obstruction1", "dest": [1.2973547558011234, 0.18411265698075294], "robot": [1.388616919517517, 0.8600000143051147], "init": {"obstruction0": [0.41724511981010437, 0.10000099986791611, 0.16559429466724396, 0.19393038749694824], "obstruction1": [1.0809205770492554, 0.10000099986791611, 0.18252427875995636, 0.16370268166065216], "obstruction2": [0.6930773258209229, 0.10000099986791611, 0.19260691106319427, 0.13893510401248932], "obstruction3": [0.9658926725387573, 0.10000099986791611, 0.06577402353286743, 0.09953121095895767], "target_block": [1.5010786056518555, 0.10000099986791611, 0.0980890691280365, 0.06211165711283684], "target_surface": [1.0282063484191895, 0.0, 0.1298033446073532, 0.10000000149011612]}, "final": {"obstruction0": [0.41724511981010437, 0.10000099986791611, 0.16559429466724396, 0.19393038749694824], "obstruction1": [1.297354817390442, 0.18411266803741455, 0.18252427875995636, 0.16370268166065216], "obstruction2": [0.6930773258209229, 0.10000099986791611, 0.19260691106319427, 0.13893510401248932], "obstruction3": [0.9658926725387573, 0.10000099986791611, 0.06577402353286743, 0.09953121095895767], "target_block": [1.5010786056518555, 0.10000099986791611, 0.0980890691280365, 0.06211165711283684], "target_surface": [1.0282063484191895, 0.0, 0.1298033446073532, 0.10000000149011612]}}
           4 +{"count": 4, "seed": 3, "steps": 118, "success": true, "seconds": 2.83}
           5 +{"count": 4, "seed": 4, "steps": 247, "success": true, "seconds": 4.65}
           6 +{"count": 4, "seed": 5, "steps": 131, "success": true, "seconds": 3.62}
           7 +{"count": 4, "seed": 6, "steps": 182, "success": true, "seconds": 2.88}
           8 +{"count": 4, "seed": 7, "steps": 133, "success": true, "seconds": 2.44}
           9 +{"count": 4, "seed": 8, "steps": 157, "success": true, "seconds": 2.22}
          10 +{"count": 4, "seed": 9, "steps": 139, "success": true, "seconds": 3.85}
          11 +{"count": 4, "seed": 10, "steps": 158, "success": true, "seconds": 2.41}
          12 +{"count": 4, "seed": 11, "steps": 102, "success": true, "seconds": 1.96}
          13 +{"count": 4, "seed": 12, "steps": 167, "success": true, "seconds": 2.79}
          14 +{"count": 4, "seed": 13, "steps": 156, "success": true, "seconds": 3.16}
          15 +{"count": 4, "seed": 14, "steps": 103, "success": true, "seconds": 1.92}
          16 +{"count": 4, "seed": 15, "steps": 154, "success": true, "seconds": 2.5}
          17 +{"count": 4, "seed": 16, "steps": 136, "success": true, "seconds": 2.55}
          18 +{"count": 4, "seed": 17, "steps": 119, "success": true, "seconds": 2.84}
          19 +{"count": 4, "seed": 18, "steps": 57, "success": true, "seconds": 1.57}
          20 +{"count": 4, "seed": 19, "steps": 108, "success": true, "seconds": 2.06}
          21 +{"count": 4, "seed": 20, "steps": 75, "success": true, "seconds": 1.96}
          22 +{"count": 4, "seed": 21, "steps": 87, "success": true, "seconds": 3.35}
          23 +{"count": 4, "seed": 22, "steps": 105, "success": true, "seconds": 2.55}
          24 +{"count": 4, "seed": 23, "steps": 100, "success": true, "seconds": 1.63}
          25 +{"count": 4, "seed": 24, "steps": 226, "success": true, "seconds": 2.83}
          26 +{"count": 4, "seed": 25, "steps": 230, "success": true, "seconds": 2.31}
          27 +{"count": 4, "seed": 26, "steps": 165, "success": true, "seconds": 2.18}
          28 +{"count": 4, "seed": 27, "steps": 169, "success": true, "seconds": 2.28}
          29 +{"count": 4, "seed": 28, "steps": 174, "success": true, "seconds": 2.47}
diff --git a/test_counts_scene_v2.log b/test_counts_scene_v2.log
new file mode 100644
index 0000000..f6ec3d5
--- /dev/null
+++ b/test_counts_scene_v2.log
@@ -0,0 +1,29 @@
           1 +{"count": 4, "seed": 0, "steps": 159, "success": true, "seconds": 5.41}
           2 +{"count": 4, "seed": 1, "steps": 174, "success": true, "seconds": 5.16}
           3 +{"count": 4, "seed": 2, "steps": 1000, "success": false, "seconds": 18.9, "phase": "retreat", "task": "obstruction1", "dest": [1.2973547558011234, 0.18411265698075294], "robot": [1.388616919517517, 0.8600000143051147], "init": {"obstruction0": [0.41724511981010437, 0.10000099986791611, 0.16559429466724396, 0.19393038749694824], "obstruction1": [1.0809205770492554, 0.10000099986791611, 0.18252427875995636, 0.16370268166065216], "obstruction2": [0.6930773258209229, 0.10000099986791611, 0.19260691106319427, 0.13893510401248932], "obstruction3": [0.9658926725387573, 0.10000099986791611, 0.06577402353286743, 0.09953121095895767], "target_block": [1.5010786056518555, 0.10000099986791611, 0.0980890691280365, 0.06211165711283684], "target_surface": [1.0282063484191895, 0.0, 0.1298033446073532, 0.10000000149011612]}, "final": {"obstruction0": [0.41724511981010437, 0.10000099986791611, 0.16559429466724396, 0.19393038749694824], "obstruction1": [1.297354817390442, 0.18411266803741455, 0.18252427875995636, 0.16370268166065216], "obstruction2": [0.6930773258209229, 0.10000099986791611, 0.19260691106319427, 0.13893510401248932], "obstruction3": [0.9658926725387573, 0.10000099986791611, 0.06577402353286743, 0.09953121095895767], "target_block": [1.5010786056518555, 0.10000099986791611, 0.0980890691280365, 0.06211165711283684], "target_surface": [1.0282063484191895, 0.0, 0.1298033446073532, 0.10000000149011612]}}
           4 +{"count": 4, "seed": 3, "steps": 118, "success": true, "seconds": 2.83}
           5 +{"count": 4, "seed": 4, "steps": 247, "success": true, "seconds": 4.65}
           6 +{"count": 4, "seed": 5, "steps": 131, "success": true, "seconds": 3.62}
           7 +{"count": 4, "seed": 6, "steps": 182, "success": true, "seconds": 2.88}
           8 +{"count": 4, "seed": 7, "steps": 133, "success": true, "seconds": 2.44}
           9 +{"count": 4, "seed": 8, "steps": 157, "success": true, "seconds": 2.22}
          10 +{"count": 4, "seed": 9, "steps": 139, "success": true, "seconds": 3.85}
          11 +{"count": 4, "seed": 10, "steps": 158, "success": true, "seconds": 2.41}
          12 +{"count": 4, "seed": 11, "steps": 102, "success": true, "seconds": 1.96}
          13 +{"count": 4, "seed": 12, "steps": 167, "success": true, "seconds": 2.79}
          14 +{"count": 4, "seed": 13, "steps": 156, "success": true, "seconds": 3.16}
          15 +{"count": 4, "seed": 14, "steps": 103, "success": true, "seconds": 1.92}
          16 +{"count": 4, "seed": 15, "steps": 154, "success": true, "seconds": 2.5}
          17 +{"count": 4, "seed": 16, "steps": 136, "success": true, "seconds": 2.55}
          18 +{"count": 4, "seed": 17, "steps": 119, "success": true, "seconds": 2.84}
          19 +{"count": 4, "seed": 18, "steps": 57, "success": true, "seconds": 1.57}
          20 +{"count": 4, "seed": 19, "steps": 108, "success": true, "seconds": 2.06}
          21 +{"count": 4, "seed": 20, "steps": 75, "success": true, "seconds": 1.96}
          22 +{"count": 4, "seed": 21, "steps": 87, "success": true, "seconds": 3.35}
          23 +{"count": 4, "seed": 22, "steps": 105, "success": true, "seconds": 2.55}
          24 +{"count": 4, "seed": 23, "steps": 100, "success": true, "seconds": 1.63}
          25 +{"count": 4, "seed": 24, "steps": 226, "success": true, "seconds": 2.83}
          26 +{"count": 4, "seed": 25, "steps": 230, "success": true, "seconds": 2.31}
          27 +{"count": 4, "seed": 26, "steps": 165, "success": true, "seconds": 2.18}
          28 +{"count": 4, "seed": 27, "steps": 169, "success": true, "seconds": 2.28}
          29 +{"count": 4, "seed": 28, "steps": 174, "success": true, "seconds": 2.47}
```

</details>

<a id="C007"></a>
### C007 · Reduce transport height from observed obstacle clearance and combine safe approach motion

Commit `56e8c6c08294a6ecee4669861d506320de347c66`; parents: 41ec7aaba58f7c4e90a7656565f0ab9ccf715908. Recorded author date: 2026-09-21T17:27:41Z.

File roles (automatic): diagnostic/test, policy.

- [E0056](01_timeline.md#E0056): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_56e8c6c_approach.py) · [Exact all-file diff](evidence/diffs/C007_56e8c6c.diff)

[Previous saved controller snapshot](evidence/versions/C006_41ec7aa_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6ad96db..1701ba4 100644
--- a/approach.py
+++ b/approach.py
@@ -116,6 +116,10 @@ class GeneratedApproach:
  116    116          self.pickx=max(.1002,min(1.5178,x+offset))
  117    117          self.offsetx=self.pickx-x
  118    118          self.picktop=y+h
         119 +        rx=float(s.get(self.robot,'x'))
         120 +        self.empty_cruise=max([.34]+[qy+qh+.235 for p in obs+[self.block] for qx,qy,qw,qh in [self.rect(s,p)] if qx<max(rx,self.pickx)+.11 and qx+qw>min(rx,self.pickx)-.11])
         121 +        self.empty_cruise=min(.86,self.empty_cruise)
         122 +        self.carry_cruise=.86
  119    123          self.phase='above'
  120    124          self.stuck=0
  121    125  
@@ -134,16 +138,20 @@ class GeneratedApproach:
  134    138          vac=0.
  135    139          tx,ty=rx,ry
  136    140          if self.phase=='above':
  137        -            ty=.86
  138        -            if abs(ry-ty)<.002:
         141 +            ty=self.empty_cruise
         142 +            if ry>=ty-.002:
  139    143                  tx=self.pickx
  140    144                  if abs(rx-tx)<.002:self.phase='down'
  141    145          if self.phase=='down':
  142    146              tx=self.pickx;ty=self.picktop+.215;vac=0.
  143    147              if (abs(rx-tx)<.002 and abs(ry-ty)<.002) or self.stuck>=2:
  144    148                  self.phase='lift';self.before_y=y;vac=1.
         149 +                self.offsety=ry-y;self.offsetx=rx-x
         150 +                left=min(x,self.dest[0])-.11;right=max(x+w,self.dest[0]+w)+.11
         151 +                tops=[qy+qh for p in self.obstacles(s)+[self.block] if p!=self.task for qx,qy,qw,qh in [self.rect(s,p)] if qx<right and qx+qw>left]
         152 +                self.carry_cruise=min(.88,max([y+.06]+tops)+self.offsety+.026)
  145    153          elif self.phase=='lift':
  146        -            vac=1.;ty=.86
         154 +            vac=1.;ty=self.carry_cruise
  147    155              if y>self.before_y+.025:
  148    156                  self.offsetx=rx-x;self.offsety=ry-y
  149    157              if abs(ry-ty)<.002:
@@ -151,13 +159,13 @@ class GeneratedApproach:
  151    159                      self.phase='down';self.picktop-=.005
  152    160                  else:self.phase='carry'
  153    161          elif self.phase=='carry':
  154        -            vac=1.;ty=.86;tx=self.dest[0]+self.offsetx
         162 +            vac=1.;ty=self.carry_cruise;tx=self.dest[0]+self.offsetx
  155    163              if abs(rx-tx)<.002:self.phase='place'
  156    164          elif self.phase=='place':
  157    165              vac=1.;tx=self.dest[0]+self.offsetx;ty=self.dest[1]+self.offsety
  158    166              if abs(rx-tx)<.002 and abs(ry-ty)<.002:self.phase='release'
  159    167          elif self.phase=='release':
  160        -            vac=0.;self.phase='retreat'
         168 +            vac=0.;self.phase='choose'
  161    169          elif self.phase=='retreat':
  162    170              ty=.86
  163    171              if abs(ry-ty)<.002:self.phase='choose'
diff --git a/probe_failure319.log b/probe_failure319.log
new file mode 100644
index 0000000..5c36910
--- /dev/null
+++ b/probe_failure319.log
@@ -0,0 +1,187 @@
           1 +INITIAL {'object_count': 2}
           2 +obstruction0 [1.210984, 0.100001, 0.161419, 0.115854]
           3 +obstruction1 [0.486631, 0.100001, 0.190952, 0.187956]
           4 +robot [1.185983, 0.892465, -1.570796]
           5 +target_block [0.308954, 0.100001, 0.176284, 0.189023]
           6 +target_surface [1.248493, 0.0, 0.21702, 0.1]
           7 +0 ('above', 'obstruction1', (0.5326113536937817, 0.105)) robot [1.185983, 0.86] task [0.486631, 0.100001]
           8 +16 ('down', 'obstruction1', (0.5326113536937817, 0.105)) robot [0.464631, 0.81] task [0.486631, 0.100001]
           9 +24 ('lift', 'obstruction1', (0.5326113536937817, 0.105)) robot [0.464631, 0.502957] task [0.486631, 0.100001]
          10 +33 ('carry', 'obstruction1', (0.5326113536937817, 0.105)) robot [0.464631, 0.86] task [0.486631, 0.457044]
          11 +35 ('place', 'obstruction1', (0.5326113536937817, 0.105)) robot [0.510611, 0.86] task [0.532611, 0.457044]
          12 +44 ('release', 'obstruction1', (0.5326113536937817, 0.105)) robot [0.510611, 0.507956] task [0.532611, 0.105]
          13 +45 ('retreat', 'obstruction1', (0.5326113536937817, 0.105)) robot [0.510611, 0.507956] task [0.532611, 0.105]
          14 +54 ('choose', 'obstruction1', (0.5326113536937817, 0.105)) robot [0.510611, 0.86] task [0.532611, 0.105]
          15 +55 ('down', 'obstruction1', (0.5819511252738334, 0.105)) robot [0.510611, 0.81] task [0.532611, 0.105]
          16 +63 ('lift', 'obstruction1', (0.5819511252738334, 0.105)) robot [0.510611, 0.507956] task [0.532611, 0.105]
          17 +72 ('carry', 'obstruction1', (0.5819511252738334, 0.105)) robot [0.510611, 0.86] task [0.532611, 0.457044]
          18 +74 ('place', 'obstruction1', (0.5819511252738334, 0.105)) robot [0.559951, 0.86] task [0.581951, 0.457044]
          19 +83 ('release', 'obstruction1', (0.5819511252738334, 0.105)) robot [0.559951, 0.507956] task [0.581951, 0.105]
          20 +84 ('retreat', 'obstruction1', (0.5819511252738334, 0.105)) robot [0.559951, 0.507956] task [0.581951, 0.105]
          21 +93 ('choose', 'obstruction1', (0.5819511252738334, 0.105)) robot [0.559951, 0.86] task [0.581951, 0.105]
          22 +94 ('down', 'obstruction1', (0.6312908968538851, 0.105)) robot [0.559951, 0.81] task [0.581951, 0.105]
          23 +102 ('lift', 'obstruction1', (0.6312908968538851, 0.105)) robot [0.559951, 0.507956] task [0.581951, 0.105]
          24 +111 ('carry', 'obstruction1', (0.6312908968538851, 0.105)) robot [0.559951, 0.86] task [0.581951, 0.457044]
          25 +113 ('place', 'obstruction1', (0.6312908968538851, 0.105)) robot [0.609291, 0.86] task [0.631291, 0.457044]
          26 +122 ('release', 'obstruction1', (0.6312908968538851, 0.105)) robot [0.609291, 0.507956] task [0.631291, 0.105]
          27 +123 ('retreat', 'obstruction1', (0.6312908968538851, 0.105)) robot [0.609291, 0.507956] task [0.631291, 0.105]
          28 +132 ('choose', 'obstruction1', (0.6312908968538851, 0.105)) robot [0.609291, 0.86] task [0.631291, 0.105]
          29 +133 ('down', 'obstruction1', (0.6806306684339368, 0.105)) robot [0.609291, 0.81] task [0.631291, 0.105]
          30 +141 ('lift', 'obstruction1', (0.6806306684339368, 0.105)) robot [0.609291, 0.507956] task [0.631291, 0.105]
          31 +150 ('carry', 'obstruction1', (0.6806306684339368, 0.105)) robot [0.609291, 0.86] task [0.631291, 0.457044]
          32 +152 ('place', 'obstruction1', (0.6806306684339368, 0.105)) robot [0.658631, 0.86] task [0.680631, 0.457044]
          33 +161 ('release', 'obstruction1', (0.6806306684339368, 0.105)) robot [0.658631, 0.507956] task [0.680631, 0.105]
          34 +162 ('retreat', 'obstruction1', (0.6806306684339368, 0.105)) robot [0.658631, 0.507956] task [0.680631, 0.105]
          35 +171 ('choose', 'obstruction1', (0.6806306684339368, 0.105)) robot [0.658631, 0.86] task [0.680631, 0.105]
          36 +172 ('down', 'obstruction1', (0.7299704400139885, 0.105)) robot [0.658631, 0.81] task [0.680631, 0.105]
          37 +180 ('lift', 'obstruction1', (0.7299704400139885, 0.105)) robot [0.658631, 0.507956] task [0.680631, 0.105]
          38 +189 ('carry', 'obstruction1', (0.7299704400139885, 0.105)) robot [0.658631, 0.86] task [0.680631, 0.457044]
          39 +191 ('place', 'obstruction1', (0.7299704400139885, 0.105)) robot [0.70797, 0.86] task [0.72997, 0.457044]
          40 +200 ('release', 'obstruction1', (0.7299704400139885, 0.105)) robot [0.70797, 0.507956] task [0.72997, 0.105]
          41 +201 ('retreat', 'obstruction1', (0.7299704400139885, 0.105)) robot [0.70797, 0.507956] task [0.72997, 0.105]
          42 +210 ('choose', 'obstruction1', (0.7299704400139885, 0.105)) robot [0.70797, 0.86] task [0.72997, 0.105]
          43 +211 ('down', 'obstruction1', (0.7793102115940402, 0.105)) robot [0.70797, 0.81] task [0.72997, 0.105]
          44 +219 ('lift', 'obstruction1', (0.7793102115940402, 0.105)) robot [0.70797, 0.507956] task [0.72997, 0.105]
          45 +228 ('carry', 'obstruction1', (0.7793102115940402, 0.105)) robot [0.70797, 0.86] task [0.72997, 0.457044]
          46 +230 ('place', 'obstruction1', (0.7793102115940402, 0.105)) robot [0.75731, 0.86] task [0.77931, 0.457044]
          47 +239 ('release', 'obstruction1', (0.7793102115940402, 0.105)) robot [0.75731, 0.507956] task [0.77931, 0.105]
          48 +240 ('retreat', 'obstruction1', (0.7793102115940402, 0.105)) robot [0.75731, 0.507956] task [0.77931, 0.105]
          49 +249 ('choose', 'obstruction1', (0.7793102115940402, 0.105)) robot [0.75731, 0.86] task [0.77931, 0.105]
          50 +250 ('down', 'obstruction1', (0.828649983174092, 0.105)) robot [0.75731, 0.81] task [0.77931, 0.105]
          51 +258 ('lift', 'obstruction1', (0.828649983174092, 0.105)) robot [0.75731, 0.507956] task [0.77931, 0.105]
          52 +267 ('carry', 'obstruction1', (0.828649983174092, 0.105)) robot [0.75731, 0.86] task [0.77931, 0.457044]
          53 +269 ('place', 'obstruction1', (0.828649983174092, 0.105)) robot [0.80665, 0.86] task [0.82865, 0.457044]
          54 +278 ('release', 'obstruction1', (0.828649983174092, 0.105)) robot [0.80665, 0.507956] task [0.82865, 0.105]
          55 +279 ('retreat', 'obstruction1', (0.828649983174092, 0.105)) robot [0.80665, 0.507956] task [0.82865, 0.105]
          56 +288 ('choose', 'obstruction1', (0.828649983174092, 0.105)) robot [0.80665, 0.86] task [0.82865, 0.105]
          57 +289 ('down', 'obstruction1', (0.8779897547541436, 0.105)) robot [0.80665, 0.81] task [0.82865, 0.105]
          58 +297 ('lift', 'obstruction1', (0.8779897547541436, 0.105)) robot [0.80665, 0.507956] task [0.82865, 0.105]
          59 +306 ('carry', 'obstruction1', (0.8779897547541436, 0.105)) robot [0.80665, 0.86] task [0.82865, 0.457044]
          60 +308 ('place', 'obstruction1', (0.8779897547541436, 0.105)) robot [0.85599, 0.86] task [0.87799, 0.457044]
          61 +317 ('release', 'obstruction1', (0.8779897547541436, 0.105)) robot [0.85599, 0.507956] task [0.87799, 0.105]
          62 +318 ('retreat', 'obstruction1', (0.8779897547541436, 0.105)) robot [0.85599, 0.507956] task [0.87799, 0.105]
          63 +327 ('choose', 'obstruction1', (0.8779897547541436, 0.105)) robot [0.85599, 0.86] task [0.87799, 0.105]
          64 +328 ('down', 'obstruction1', (0.9273295263341954, 0.105)) robot [0.85599, 0.81] task [0.87799, 0.105]
          65 +336 ('lift', 'obstruction1', (0.9273295263341954, 0.105)) robot [0.85599, 0.507956] task [0.87799, 0.105]
          66 +345 ('carry', 'obstruction1', (0.9273295263341954, 0.105)) robot [0.85599, 0.86] task [0.87799, 0.457044]
          67 +347 ('place', 'obstruction1', (0.9273295263341954, 0.105)) robot [0.90533, 0.86] task [0.92733, 0.457044]
          68 +356 ('release', 'obstruction1', (0.9273295263341954, 0.105)) robot [0.90533, 0.507956] task [0.92733, 0.105]
          69 +357 ('retreat', 'obstruction1', (0.9273295263341954, 0.105)) robot [0.90533, 0.507956] task [0.92733, 0.105]
          70 +366 ('choose', 'obstruction1', (0.9273295263341954, 0.105)) robot [0.90533, 0.86] task [0.92733, 0.105]
          71 +367 ('down', 'obstruction1', (0.9766692979142472, 0.105)) robot [0.90533, 0.81] task [0.92733, 0.105]
          72 +375 ('lift', 'obstruction1', (0.9766692979142472, 0.105)) robot [0.90533, 0.507956] task [0.92733, 0.105]
          73 +384 ('carry', 'obstruction1', (0.9766692979142472, 0.105)) robot [0.90533, 0.86] task [0.92733, 0.457044]
          74 +386 ('place', 'obstruction1', (0.9766692979142472, 0.105)) robot [0.954669, 0.86] task [0.976669, 0.457044]
          75 +395 ('release', 'obstruction1', (0.9766692979142472, 0.105)) robot [0.954669, 0.507956] task [0.976669, 0.105]
          76 +396 ('retreat', 'obstruction1', (0.9766692979142472, 0.105)) robot [0.954669, 0.507956] task [0.976669, 0.105]
          77 +405 ('choose', 'obstruction1', (0.9766692979142472, 0.105)) robot [0.954669, 0.86] task [0.976669, 0.105]
          78 +406 ('down', 'obstruction1', (0.5655045347471495, 0.105)) robot [0.954669, 0.81] task [0.976669, 0.105]
          79 +414 ('lift', 'obstruction1', (0.5655045347471495, 0.105)) robot [0.954669, 0.507956] task [0.976669, 0.105]
          80 +423 ('carry', 'obstruction1', (0.5655045347471495, 0.105)) robot [0.954669, 0.86] task [0.976669, 0.457044]
          81 +433 ('place', 'obstruction1', (0.5655045347471495, 0.105)) robot [0.543504, 0.86] task [0.565504, 0.457044]
          82 +442 ('release', 'obstruction1', (0.5655045347471495, 0.105)) robot [0.543505, 0.507956] task [0.565504, 0.105]
          83 +443 ('retreat', 'obstruction1', (0.5655045347471495, 0.105)) robot [0.543505, 0.507956] task [0.565504, 0.105]
          84 +452 ('choose', 'obstruction1', (0.5655045347471495, 0.105)) robot [0.543505, 0.86] task [0.565504, 0.105]
          85 +453 ('down', 'obstruction1', (0.6148443063272011, 0.105)) robot [0.543504, 0.81] task [0.565504, 0.105]
          86 +461 ('lift', 'obstruction1', (0.6148443063272011, 0.105)) robot [0.543504, 0.507956] task [0.565504, 0.105]
          87 +470 ('carry', 'obstruction1', (0.6148443063272011, 0.105)) robot [0.543504, 0.86] task [0.565504, 0.457044]
          88 +472 ('place', 'obstruction1', (0.6148443063272011, 0.105)) robot [0.592844, 0.86] task [0.614844, 0.457044]
          89 +481 ('release', 'obstruction1', (0.6148443063272011, 0.105)) robot [0.592844, 0.507956] task [0.614844, 0.105]
          90 +482 ('retreat', 'obstruction1', (0.6148443063272011, 0.105)) robot [0.592844, 0.507956] task [0.614844, 0.105]
          91 +491 ('choose', 'obstruction1', (0.6148443063272011, 0.105)) robot [0.592844, 0.86] task [0.614844, 0.105]
          92 +492 ('down', 'obstruction1', (0.6641840779072529, 0.105)) robot [0.592844, 0.81] task [0.614844, 0.105]
          93 +500 ('lift', 'obstruction1', (0.6641840779072529, 0.105)) robot [0.592844, 0.507956] task [0.614844, 0.105]
          94 +509 ('carry', 'obstruction1', (0.6641840779072529, 0.105)) robot [0.592844, 0.86] task [0.614844, 0.457044]
          95 +511 ('place', 'obstruction1', (0.6641840779072529, 0.105)) robot [0.642184, 0.86] task [0.664184, 0.457044]
          96 +520 ('release', 'obstruction1', (0.6641840779072529, 0.105)) robot [0.642184, 0.507956] task [0.664184, 0.105]
          97 +521 ('retreat', 'obstruction1', (0.6641840779072529, 0.105)) robot [0.642184, 0.507956] task [0.664184, 0.105]
          98 +530 ('choose', 'obstruction1', (0.6641840779072529, 0.105)) robot [0.642184, 0.86] task [0.664184, 0.105]
          99 +531 ('down', 'obstruction1', (0.7135238494873046, 0.105)) robot [0.642184, 0.81] task [0.664184, 0.105]
         100 +539 ('lift', 'obstruction1', (0.7135238494873046, 0.105)) robot [0.642184, 0.507956] task [0.664184, 0.105]
         101 +548 ('carry', 'obstruction1', (0.7135238494873046, 0.105)) robot [0.642184, 0.86] task [0.664184, 0.457044]
         102 +550 ('place', 'obstruction1', (0.7135238494873046, 0.105)) robot [0.691524, 0.86] task [0.713524, 0.457044]
         103 +559 ('release', 'obstruction1', (0.7135238494873046, 0.105)) robot [0.691524, 0.507956] task [0.713524, 0.105]
         104 +560 ('retreat', 'obstruction1', (0.7135238494873046, 0.105)) robot [0.691524, 0.507956] task [0.713524, 0.105]
         105 +569 ('choose', 'obstruction1', (0.7135238494873046, 0.105)) robot [0.691524, 0.86] task [0.713524, 0.105]
         106 +570 ('down', 'obstruction1', (0.7628636210673563, 0.105)) robot [0.691524, 0.81] task [0.713524, 0.105]
         107 +578 ('lift', 'obstruction1', (0.7628636210673563, 0.105)) robot [0.691524, 0.507956] task [0.713524, 0.105]
         108 +587 ('carry', 'obstruction1', (0.7628636210673563, 0.105)) robot [0.691524, 0.86] task [0.713524, 0.457044]
         109 +589 ('place', 'obstruction1', (0.7628636210673563, 0.105)) robot [0.740864, 0.86] task [0.762864, 0.457044]
         110 +598 ('release', 'obstruction1', (0.7628636210673563, 0.105)) robot [0.740864, 0.507956] task [0.762864, 0.105]
         111 +599 ('retreat', 'obstruction1', (0.7628636210673563, 0.105)) robot [0.740864, 0.507956] task [0.762864, 0.105]
         112 +608 ('choose', 'obstruction1', (0.7628636210673563, 0.105)) robot [0.740864, 0.86] task [0.762864, 0.105]
         113 +609 ('down', 'obstruction1', (0.812203392647408, 0.105)) robot [0.740864, 0.81] task [0.762864, 0.105]
         114 +617 ('lift', 'obstruction1', (0.812203392647408, 0.105)) robot [0.740864, 0.507956] task [0.762864, 0.105]
         115 +626 ('carry', 'obstruction1', (0.812203392647408, 0.105)) robot [0.740864, 0.86] task [0.762864, 0.457044]
         116 +628 ('place', 'obstruction1', (0.812203392647408, 0.105)) robot [0.790203, 0.86] task [0.812203, 0.457044]
         117 +637 ('release', 'obstruction1', (0.812203392647408, 0.105)) robot [0.790203, 0.507956] task [0.812203, 0.105]
         118 +638 ('retreat', 'obstruction1', (0.812203392647408, 0.105)) robot [0.790203, 0.507956] task [0.812203, 0.105]
         119 +647 ('choose', 'obstruction1', (0.812203392647408, 0.105)) robot [0.790203, 0.86] task [0.812203, 0.105]
         120 +648 ('down', 'obstruction1', (0.8615431642274598, 0.105)) robot [0.790203, 0.81] task [0.812203, 0.105]
         121 +656 ('lift', 'obstruction1', (0.8615431642274598, 0.105)) robot [0.790203, 0.507956] task [0.812203, 0.105]
         122 +665 ('carry', 'obstruction1', (0.8615431642274598, 0.105)) robot [0.790203, 0.86] task [0.812203, 0.457044]
         123 +667 ('place', 'obstruction1', (0.8615431642274598, 0.105)) robot [0.839543, 0.86] task [0.861543, 0.457044]
         124 +676 ('release', 'obstruction1', (0.8615431642274598, 0.105)) robot [0.839543, 0.507956] task [0.861543, 0.105]
         125 +677 ('retreat', 'obstruction1', (0.8615431642274598, 0.105)) robot [0.839543, 0.507956] task [0.861543, 0.105]
         126 +686 ('choose', 'obstruction1', (0.8615431642274598, 0.105)) robot [0.839543, 0.86] task [0.861543, 0.105]
         127 +687 ('down', 'obstruction1', (0.9108829358075116, 0.105)) robot [0.839543, 0.81] task [0.861543, 0.105]
         128 +695 ('lift', 'obstruction1', (0.9108829358075116, 0.105)) robot [0.839543, 0.507956] task [0.861543, 0.105]
         129 +704 ('carry', 'obstruction1', (0.9108829358075116, 0.105)) robot [0.839543, 0.86] task [0.861543, 0.457044]
         130 +706 ('place', 'obstruction1', (0.9108829358075116, 0.105)) robot [0.888883, 0.86] task [0.910883, 0.457044]
         131 +715 ('release', 'obstruction1', (0.9108829358075116, 0.105)) robot [0.888883, 0.507956] task [0.910883, 0.105]
         132 +716 ('retreat', 'obstruction1', (0.9108829358075116, 0.105)) robot [0.888883, 0.507956] task [0.910883, 0.105]
         133 +725 ('choose', 'obstruction1', (0.9108829358075116, 0.105)) robot [0.888883, 0.86] task [0.910883, 0.105]
         134 +726 ('down', 'obstruction1', (0.9602227073875632, 0.105)) robot [0.888883, 0.81] task [0.910883, 0.105]
         135 +734 ('lift', 'obstruction1', (0.9602227073875632, 0.105)) robot [0.888883, 0.507956] task [0.910883, 0.105]
         136 +743 ('carry', 'obstruction1', (0.9602227073875632, 0.105)) robot [0.888883, 0.86] task [0.910883, 0.457044]
         137 +745 ('place', 'obstruction1', (0.9602227073875632, 0.105)) robot [0.938223, 0.86] task [0.960223, 0.457044]
         138 +754 ('release', 'obstruction1', (0.9602227073875632, 0.105)) robot [0.938223, 0.507956] task [0.960223, 0.105]
         139 +755 ('retreat', 'obstruction1', (0.9602227073875632, 0.105)) robot [0.938223, 0.507956] task [0.960223, 0.105]
         140 +764 ('choose', 'obstruction1', (0.9602227073875632, 0.105)) robot [0.938223, 0.86] task [0.960223, 0.105]
         141 +765 ('down', 'obstruction1', (0.5490579442204655, 0.105)) robot [0.938223, 0.81] task [0.960223, 0.105]
         142 +773 ('lift', 'obstruction1', (0.5490579442204655, 0.105)) robot [0.938223, 0.507956] task [0.960223, 0.105]
         143 +782 ('carry', 'obstruction1', (0.5490579442204655, 0.105)) robot [0.938223, 0.86] task [0.960223, 0.457044]
         144 +792 ('place', 'obstruction1', (0.5490579442204655, 0.105)) robot [0.527058, 0.86] task [0.549058, 0.457044]
         145 +801 ('release', 'obstruction1', (0.5490579442204655, 0.105)) robot [0.527058, 0.507956] task [0.549058, 0.105]
         146 +802 ('retreat', 'obstruction1', (0.5490579442204655, 0.105)) robot [0.527058, 0.507956] task [0.549058, 0.105]
         147 +811 ('choose', 'obstruction1', (0.5490579442204655, 0.105)) robot [0.527058, 0.86] task [0.549058, 0.105]
         148 +812 ('down', 'obstruction1', (0.5983977158005173, 0.105)) robot [0.527058, 0.81] task [0.549058, 0.105]
         149 +820 ('lift', 'obstruction1', (0.5983977158005173, 0.105)) robot [0.527058, 0.507956] task [0.549058, 0.105]
         150 +829 ('carry', 'obstruction1', (0.5983977158005173, 0.105)) robot [0.527058, 0.86] task [0.549058, 0.457044]
         151 +831 ('place', 'obstruction1', (0.5983977158005173, 0.105)) robot [0.576398, 0.86] task [0.598398, 0.457044]
         152 +840 ('release', 'obstruction1', (0.5983977158005173, 0.105)) robot [0.576398, 0.507956] task [0.598398, 0.105]
         153 +841 ('retreat', 'obstruction1', (0.5983977158005173, 0.105)) robot [0.576398, 0.507956] task [0.598398, 0.105]
         154 +850 ('choose', 'obstruction1', (0.5983977158005173, 0.105)) robot [0.576398, 0.86] task [0.598398, 0.105]
         155 +851 ('down', 'obstruction1', (0.647737487380569, 0.105)) robot [0.576398, 0.81] task [0.598398, 0.105]
         156 +859 ('lift', 'obstruction1', (0.647737487380569, 0.105)) robot [0.576398, 0.507956] task [0.598398, 0.105]
         157 +868 ('carry', 'obstruction1', (0.647737487380569, 0.105)) robot [0.576398, 0.86] task [0.598398, 0.457044]
         158 +870 ('place', 'obstruction1', (0.647737487380569, 0.105)) robot [0.625737, 0.86] task [0.647738, 0.457044]
         159 +879 ('release', 'obstruction1', (0.647737487380569, 0.105)) robot [0.625737, 0.507956] task [0.647737, 0.105]
         160 +880 ('retreat', 'obstruction1', (0.647737487380569, 0.105)) robot [0.625737, 0.507956] task [0.647737, 0.105]
         161 +889 ('choose', 'obstruction1', (0.647737487380569, 0.105)) robot [0.625737, 0.86] task [0.647737, 0.105]
         162 +890 ('down', 'obstruction1', (0.6970772589606207, 0.105)) robot [0.625737, 0.81] task [0.647737, 0.105]
         163 +898 ('lift', 'obstruction1', (0.6970772589606207, 0.105)) robot [0.625737, 0.507956] task [0.647737, 0.105]
         164 +907 ('carry', 'obstruction1', (0.6970772589606207, 0.105)) robot [0.625737, 0.86] task [0.647737, 0.457044]
         165 +909 ('place', 'obstruction1', (0.6970772589606207, 0.105)) robot [0.675077, 0.86] task [0.697077, 0.457044]
         166 +918 ('release', 'obstruction1', (0.6970772589606207, 0.105)) robot [0.675077, 0.507956] task [0.697077, 0.105]
         167 +919 ('retreat', 'obstruction1', (0.6970772589606207, 0.105)) robot [0.675077, 0.507956] task [0.697077, 0.105]
         168 +928 ('choose', 'obstruction1', (0.6970772589606207, 0.105)) robot [0.675077, 0.86] task [0.697077, 0.105]
         169 +929 ('down', 'obstruction1', (0.7464170305406724, 0.105)) robot [0.675077, 0.81] task [0.697077, 0.105]
         170 +937 ('lift', 'obstruction1', (0.7464170305406724, 0.105)) robot [0.675077, 0.507956] task [0.697077, 0.105]
         171 +946 ('carry', 'obstruction1', (0.7464170305406724, 0.105)) robot [0.675077, 0.86] task [0.697077, 0.457044]
         172 +948 ('place', 'obstruction1', (0.7464170305406724, 0.105)) robot [0.724417, 0.86] task [0.746417, 0.457044]
         173 +957 ('release', 'obstruction1', (0.7464170305406724, 0.105)) robot [0.724417, 0.507956] task [0.746417, 0.105]
         174 +958 ('retreat', 'obstruction1', (0.7464170305406724, 0.105)) robot [0.724417, 0.507956] task [0.746417, 0.105]
         175 +967 ('choose', 'obstruction1', (0.7464170305406724, 0.105)) robot [0.724417, 0.86] task [0.746417, 0.105]
         176 +968 ('down', 'obstruction1', (0.7957568021207242, 0.105)) robot [0.724417, 0.81] task [0.746417, 0.105]
         177 +976 ('lift', 'obstruction1', (0.7957568021207242, 0.105)) robot [0.724417, 0.507956] task [0.746417, 0.105]
         178 +985 ('carry', 'obstruction1', (0.7957568021207242, 0.105)) robot [0.724417, 0.86] task [0.746417, 0.457044]
         179 +987 ('place', 'obstruction1', (0.7957568021207242, 0.105)) robot [0.773757, 0.86] task [0.795757, 0.457044]
         180 +996 ('release', 'obstruction1', (0.7957568021207242, 0.105)) robot [0.773757, 0.507956] task [0.795757, 0.105]
         181 +997 ('retreat', 'obstruction1', (0.7957568021207242, 0.105)) robot [0.773757, 0.507956] task [0.795757, 0.105]
         182 +FINAL
         183 +obstruction0 [1.210984, 0.100001, 0.161419, 0.115854]
         184 +obstruction1 [0.795757, 0.105, 0.190952, 0.187956]
         185 +robot [0.773757, 0.607956, -1.570796]
         186 +target_block [0.61808, 0.105, 0.176284, 0.189023]
         187 +target_surface [1.248493, 0.0, 0.21702, 0.1]
diff --git a/probe_failure319.py b/probe_failure319.py
new file mode 100644
index 0000000..4bcc365
--- /dev/null
+++ b/probe_failure319.py
@@ -0,0 +1,16 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import json
           4 +E=make_env();s,i=E.reset(seed=319);a=GeneratedApproach(E.action_space,E.observation_space,{});a.reset(s,i)
           5 +def dump(s):
           6 + for n in sorted(s.get_object_names()):
           7 +  o=s.get_object_from_name(n)
           8 +  fs=['x','y','theta'] if n=='robot' else ['x','y','width','height']
           9 +  print(n,[round(s.get(o,f),6) for f in fs])
          10 +print('INITIAL',i);dump(s);prev=None
          11 +for step in range(1000):
          12 + act=a.get_action(s);s,r,t,tr,_=E.step(act)
          13 + sig=(a.phase,a.task.name,a.dest)
          14 + if sig!=prev:print(step,sig,'robot',[round(s.get(a.robot,f),6) for f in ['x','y']],'task',[round(s.get(a.task,f),6) for f in ['x','y']]);prev=sig
          15 + if t:print('SUCCESS',step);break
          16 +print('FINAL');dump(s);E.close()
diff --git a/probe_validation_239_260_459.jsonl b/probe_validation_239_260_459.jsonl
index 5df5736..4fdac47 100644
--- a/probe_validation_239_260_459.jsonl
+++ b/probe_validation_239_260_459.jsonl
@@ -118,3 +118,61 @@
  118    118  {"seed": 376, "success": true, "steps": 113, "seconds": 0.79, "phase": "place", "task": "target_block", "robot": [0.962884247303009, 0.3838501572608948], "taskxy": [0.9230465292930603, 0.10499998927116394], "dest": [0.9230465550422668, 0.10500000149011612]}
  119    119  {"seed": 377, "success": true, "steps": 125, "seconds": 0.74, "phase": "place", "task": "target_block", "robot": [0.7124477624893188, 0.4322310984134674], "taskxy": [0.6667981147766113, 0.10499997437000275], "dest": [0.6667979996204376, 0.10500000149011612]}
  120    120  {"seed": 378, "success": true, "steps": 139, "seconds": 0.88, "phase": "place", "task": "target_block", "robot": [1.320676565170288, 0.4099999666213989], "taskxy": [1.2750359773635864, 0.10723832994699478], "dest": [1.275036003112793, 0.10500000149011612]}
         121 +{"seed": 379, "success": true, "steps": 100, "seconds": 1.35, "phase": "place", "task": "target_block", "robot": [0.5351549386978149, 0.4626084268093109], "taskxy": [0.44198378920555115, 0.10499998927116394], "dest": [0.4419838480949402, 0.10500000149011612]}
         122 +{"seed": 380, "success": true, "steps": 117, "seconds": 1.44, "phase": "place", "task": "target_block", "robot": [1.1052097082138062, 0.3802589476108551], "taskxy": [1.0409190654754639, 0.10500001907348633], "dest": [1.040919084429741, 0.10500000149011612]}
         123 +{"seed": 381, "success": true, "steps": 128, "seconds": 1.73, "phase": "place", "task": "target_block", "robot": [0.21044324338436127, 0.4099999666213989], "taskxy": [0.1830083727836609, 0.12117896974086761], "dest": [0.18300830605626106, 0.10500000149011612]}
         124 +{"seed": 382, "success": true, "steps": 64, "seconds": 0.83, "phase": "place", "task": "target_block", "robot": [0.3416171073913574, 0.5099999904632568], "taskxy": [0.3064669668674469, 0.10809426009654999], "dest": [0.30646691131591797, 0.10500000149011612]}
         125 +{"seed": 383, "success": true, "steps": 60, "seconds": 0.75, "phase": "place", "task": "target_block", "robot": [0.9091927409172058, 0.4223421514034271], "taskxy": [0.8700603246688843, 0.10499999672174454], "dest": [0.8700603659749031, 0.10500000149011612]}
         126 +{"seed": 384, "success": true, "steps": 61, "seconds": 0.79, "phase": "place", "task": "target_block", "robot": [0.40793582797050476, 0.46000000834465027], "taskxy": [0.381402850151062, 0.12396419048309326], "dest": [0.38140282067656517, 0.10500000149011612]}
         127 +{"seed": 385, "success": true, "steps": 138, "seconds": 2.06, "phase": "place", "task": "target_block", "robot": [0.298006147146225, 0.48279163241386414], "taskxy": [0.24873580038547516, 0.10499998182058334], "dest": [0.24873575228452682, 0.10500000149011612]}
         128 +{"seed": 386, "success": true, "steps": 98, "seconds": 1.57, "phase": "place", "task": "target_block", "robot": [0.8682867884635925, 0.42778250575065613], "taskxy": [0.7869170308113098, 0.10499998182058334], "dest": [0.7869169901609421, 0.10500000149011612]}
         129 +{"seed": 387, "success": true, "steps": 107, "seconds": 1.38, "phase": "place", "task": "target_block", "robot": [0.7617767453193665, 0.4269392192363739], "taskxy": [0.6695501208305359, 0.10500000417232513], "dest": [0.6695501546859741, 0.10500000149011612]}
         130 +{"seed": 388, "success": true, "steps": 102, "seconds": 1.22, "phase": "place", "task": "target_block", "robot": [0.6219067573547363, 0.37798935174942017], "taskxy": [0.5424970984458923, 0.10499996691942215], "dest": [0.5424971241950989, 0.10500000149011612]}
         131 +{"seed": 389, "success": true, "steps": 51, "seconds": 0.64, "phase": "place", "task": "target_block", "robot": [0.9091194868087769, 0.48607856035232544], "taskxy": [0.8831784725189209, 0.10499998927116394], "dest": [0.8831784951984882, 0.10500000149011612]}
         132 +{"seed": 390, "success": true, "steps": 118, "seconds": 1.4, "phase": "place", "task": "target_block", "robot": [0.29385292530059814, 0.4261748790740967], "taskxy": [0.2044985592365265, 0.10499998182058334], "dest": [0.20449851858615875, 0.10500000149011612]}
         133 +{"seed": 391, "success": true, "steps": 63, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.8823308944702148, 0.46000000834465027], "taskxy": [0.8134672045707703, 0.11873778700828552], "dest": [0.8134671639204025, 0.10500000149011612]}
         134 +{"seed": 392, "success": true, "steps": 43, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [0.3959086239337921, 0.4099999964237213], "taskxy": [0.3851921558380127, 0.1116122305393219], "dest": [0.3851922113895416, 0.10500000149011612]}
         135 +{"seed": 393, "success": true, "steps": 42, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [0.8473110198974609, 0.4641478955745697], "taskxy": [0.7964699268341064, 0.10499999672174454], "dest": [0.7964699234366417, 0.10500000149011612]}
         136 +{"seed": 394, "success": true, "steps": 40, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [1.2903193235397339, 0.3718622922897339], "taskxy": [1.2496579885482788, 0.10500004887580872], "dest": [1.2496580142974854, 0.10500000149011612]}
         137 +{"seed": 395, "success": true, "steps": 71, "seconds": 0.48, "phase": "place", "task": "target_block", "robot": [1.0701254606246948, 0.3849175274372101], "taskxy": [1.0085678100585938, 0.10499999672174454], "dest": [1.0085678358078003, 0.10500000149011612]}
         138 +{"seed": 396, "success": true, "steps": 131, "seconds": 0.95, "phase": "place", "task": "target_block", "robot": [1.4435029029846191, 0.4239347279071808], "taskxy": [1.3997095823287964, 0.10499995201826096], "dest": [1.3997094888687134, 0.10500000149011612]}
         139 +{"seed": 397, "success": true, "steps": 99, "seconds": 0.84, "phase": "place", "task": "target_block", "robot": [0.8939307332038879, 0.5099999904632568], "taskxy": [0.8469716310501099, 0.107193224132061], "dest": [0.8469716567993164, 0.10500000149011612]}
         140 +{"seed": 398, "success": true, "steps": 116, "seconds": 1.07, "phase": "place", "task": "target_block", "robot": [1.1266947984695435, 0.43454593420028687], "taskxy": [1.0583785772323608, 0.10500001162290573], "dest": [1.058378685593605, 0.10500000149011612]}
         141 +{"seed": 399, "success": true, "steps": 160, "seconds": 1.31, "phase": "place", "task": "target_block", "robot": [1.074883222579956, 0.46000000834465027], "taskxy": [1.0180078744888306, 0.12211591005325317], "dest": [1.0180077810287476, 0.10500000149011612]}
         142 +{"seed": 400, "success": true, "steps": 122, "seconds": 1.03, "phase": "place", "task": "target_block", "robot": [1.3494116067886353, 0.42408624291419983], "taskxy": [1.2923473119735718, 0.10500000417232513], "dest": [1.2923473377227783, 0.10500000149011612]}
         143 +{"seed": 401, "success": true, "steps": 96, "seconds": 0.6, "phase": "place", "task": "target_block", "robot": [0.9968143105506897, 0.5099999904632568], "taskxy": [0.9094895124435425, 0.1196649968624115], "dest": [0.9094894866943359, 0.10500000149011612]}
         144 +{"seed": 402, "success": true, "steps": 173, "seconds": 1.37, "phase": "place", "task": "target_block", "robot": [0.25376230478286743, 0.4841252267360687], "taskxy": [0.18817047774791718, 0.10499993711709976], "dest": [0.18817048180103302, 0.10500000149011612]}
         145 +{"seed": 403, "success": true, "steps": 49, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [1.2087756395339966, 0.48637619614601135], "taskxy": [1.1544865369796753, 0.10500000417232513], "dest": [1.1544865627288818, 0.10500000149011612]}
         146 +{"seed": 404, "success": true, "steps": 110, "seconds": 0.88, "phase": "place", "task": "target_block", "robot": [1.2266795635223389, 0.4599999785423279], "taskxy": [1.183605432510376, 0.11132096499204636], "dest": [1.183605339050293, 0.10500000149011612]}
         147 +{"seed": 405, "success": true, "steps": 53, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [0.30883678793907166, 0.46000000834465027], "taskxy": [0.2701936960220337, 0.11215289682149887], "dest": [0.27019365060329437, 0.10500000149011612]}
         148 +{"seed": 406, "success": true, "steps": 114, "seconds": 0.88, "phase": "place", "task": "target_block", "robot": [1.0068823099136353, 0.3726465702056885], "taskxy": [0.9335246682167053, 0.10500000417232513], "dest": [0.9335246343612671, 0.10500000149011612]}
         149 +{"seed": 407, "success": true, "steps": 46, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.49152159690856934, 0.5099999904632568], "taskxy": [0.4177647829055786, 0.11976788192987442], "dest": [0.41776478695869446, 0.10500000149011612]}
         150 +{"seed": 408, "success": true, "steps": 42, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [1.4128938913345337, 0.38593870401382446], "taskxy": [1.343496561050415, 0.10499999672174454], "dest": [1.3434965867996216, 0.10500000149011612]}
         151 +{"seed": 409, "success": true, "steps": 51, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.9631754755973816, 0.5181084275245667], "taskxy": [0.9129404425621033, 0.10500003397464752], "dest": [0.9129405658245087, 0.10500000149011612]}
         152 +{"seed": 410, "success": true, "steps": 110, "seconds": 0.76, "phase": "place", "task": "target_block", "robot": [1.2863388061523438, 0.43366649746894836], "taskxy": [1.199735403060913, 0.10499995946884155], "dest": [1.19973530960083, 0.10500000149011612]}
         153 +{"seed": 411, "success": true, "steps": 46, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [1.237841010093689, 0.5195780396461487], "taskxy": [1.154388427734375, 0.10500001907348633], "dest": [1.1543883870840073, 0.10500000149011612]}
         154 +{"seed": 412, "success": true, "steps": 104, "seconds": 0.55, "phase": "place", "task": "target_block", "robot": [0.40534552931785583, 0.5183286666870117], "taskxy": [0.34775203466415405, 0.10500004887580872], "dest": [0.3477520861029625, 0.10500000149011612]}
         155 +{"seed": 413, "success": true, "steps": 44, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [0.6949586272239685, 0.4099999666213989], "taskxy": [0.6593862771987915, 0.11419090628623962], "dest": [0.6593862433433533, 0.10500000149011612]}
         156 +{"seed": 414, "success": true, "steps": 114, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [0.78714519739151, 0.4100000262260437], "taskxy": [0.7129248976707458, 0.1066809669137001], "dest": [0.7129248719215393, 0.10500000149011612]}
         157 +{"seed": 415, "success": true, "steps": 114, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [1.3313018083572388, 0.5099999904632568], "taskxy": [1.254622220993042, 0.10837230086326599], "dest": [1.254622127532959, 0.10500000149011612]}
         158 +{"seed": 416, "success": true, "steps": 99, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.5655575394630432, 0.48688700795173645], "taskxy": [0.506436288356781, 0.10499997437000275], "dest": [0.5064363222122192, 0.10500000149011612]}
         159 +{"seed": 417, "success": true, "steps": 48, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [0.4717937409877777, 0.4889780282974243], "taskxy": [0.37312066555023193, 0.10500001907348633], "dest": [0.3731206547021866, 0.10500000149011612]}
         160 +{"seed": 418, "success": true, "steps": 34, "seconds": 0.11, "phase": "place", "task": "target_block", "robot": [0.30147528648376465, 0.5110160112380981], "taskxy": [0.22236646711826324, 0.10499999672174454], "dest": [0.2223664562702179, 0.10500000149011612]}
         161 +{"seed": 419, "success": true, "steps": 42, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.5558983683586121, 0.47383809089660645], "taskxy": [0.5161226391792297, 0.10500001907348633], "dest": [0.5161226310133934, 0.10500000149011612]}
         162 +{"seed": 420, "success": true, "steps": 92, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [1.0016852617263794, 0.46000000834465027], "taskxy": [0.9752458333969116, 0.12035991251468658], "dest": [0.9752458591461182, 0.10500000149011612]}
         163 +{"seed": 421, "success": true, "steps": 61, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [0.7292649149894714, 0.5099999904632568], "taskxy": [0.6377012133598328, 0.10799118876457214], "dest": [0.6377012621164322, 0.10500000149011612]}
         164 +{"seed": 422, "success": true, "steps": 53, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [1.217798113822937, 0.4862258732318878], "taskxy": [1.1851561069488525, 0.10500000417232513], "dest": [1.185156132698059, 0.10500000149011612]}
         165 +{"seed": 423, "success": true, "steps": 53, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.2538324296474457, 0.5099999904632568], "taskxy": [0.20377209782600403, 0.1060633733868599], "dest": [0.20377211645245552, 0.10500000149011612]}
         166 +{"seed": 424, "success": true, "steps": 46, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [0.8263397216796875, 0.4099999964237213], "taskxy": [0.7333964705467224, 0.12397715449333191], "dest": [0.733396534204483, 0.10500000149011612]}
         167 +{"seed": 425, "success": true, "steps": 51, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [1.0872663259506226, 0.4733668565750122], "taskxy": [1.0078121423721313, 0.10499993711709976], "dest": [1.0078121017217636, 0.10500000149011612]}
         168 +{"seed": 426, "success": true, "steps": 41, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [1.1259393692016602, 0.48864486813545227], "taskxy": [1.058435082435608, 0.10499997437000275], "dest": [1.058434988975525, 0.10500000149011612]}
         169 +{"seed": 427, "success": true, "steps": 94, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [1.1728700399398804, 0.43867042660713196], "taskxy": [1.1356995105743408, 0.10499995946884155], "dest": [1.1356995363235474, 0.10500000149011612]}
         170 +{"seed": 428, "success": true, "steps": 51, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [1.1063966751098633, 0.38594019412994385], "taskxy": [1.0149590969085693, 0.10499999672174454], "dest": [1.0149590034484863, 0.10500000149011612]}
         171 +{"seed": 429, "success": true, "steps": 60, "seconds": 0.16, "phase": "place", "task": "target_block", "robot": [0.8236263394355774, 0.37104350328445435], "taskxy": [0.7275202870368958, 0.10499998182058334], "dest": [0.727520246386528, 0.10500000149011612]}
         172 +{"seed": 430, "success": true, "steps": 44, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.514426052570343, 0.5099999904632568], "taskxy": [0.47870147228240967, 0.12264573574066162], "dest": [0.47870141673088074, 0.10500000149011612]}
         173 +{"seed": 431, "success": true, "steps": 106, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.36169353127479553, 0.5099999904632568], "taskxy": [0.29767850041389465, 0.12272898107767105], "dest": [0.2976784698963165, 0.10500000149011612]}
         174 +{"seed": 432, "success": true, "steps": 38, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.886044442653656, 0.4739563465118408], "taskxy": [0.846439778804779, 0.10500000417232513], "dest": [0.8464398227930069, 0.10500000149011612]}
         175 +{"seed": 433, "success": true, "steps": 53, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [0.7844719290733337, 0.46000000834465027], "taskxy": [0.7369139194488525, 0.11384446173906326], "dest": [0.7369138638973236, 0.10500000149011612]}
         176 +{"seed": 434, "success": true, "steps": 47, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [1.186089038848877, 0.43385952711105347], "taskxy": [1.14407217502594, 0.10499998927116394], "dest": [1.1440721384882926, 0.10500000149011612]}
         177 +{"seed": 435, "success": true, "steps": 103, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.7736154198646545, 0.46176329255104065], "taskxy": [0.6938204765319824, 0.10499998182058334], "dest": [0.6938204507827759, 0.10500000149011612]}
         178 +{"seed": 436, "success": true, "steps": 140, "seconds": 0.43, "phase": "place", "task": "target_block", "robot": [0.5325717329978943, 0.5100000500679016], "taskxy": [0.45083412528038025, 0.1119426041841507], "dest": [0.4508340995311737, 0.10500000149011612]}
diff --git a/test_counts_scene_v2.jsonl b/test_counts_scene_v2.jsonl
index f6ec3d5..d8fcd13 100644
--- a/test_counts_scene_v2.jsonl
+++ b/test_counts_scene_v2.jsonl
@@ -27,3 +27,5 @@
   27     27  {"count": 4, "seed": 26, "steps": 165, "success": true, "seconds": 2.18}
   28     28  {"count": 4, "seed": 27, "steps": 169, "success": true, "seconds": 2.28}
   29     29  {"count": 4, "seed": 28, "steps": 174, "success": true, "seconds": 2.47}
          30 +{"count": 4, "seed": 29, "steps": 105, "success": true, "seconds": 3.38}
          31 +{"count": 4, "seed": 30, "steps": 168, "success": true, "seconds": 5.26}
diff --git a/test_counts_scene_v2.log b/test_counts_scene_v2.log
index f6ec3d5..d8fcd13 100644
--- a/test_counts_scene_v2.log
+++ b/test_counts_scene_v2.log
@@ -27,3 +27,5 @@
   27     27  {"count": 4, "seed": 26, "steps": 165, "success": true, "seconds": 2.18}
   28     28  {"count": 4, "seed": 27, "steps": 169, "success": true, "seconds": 2.28}
   29     29  {"count": 4, "seed": 28, "steps": 174, "success": true, "seconds": 2.47}
          30 +{"count": 4, "seed": 29, "steps": 105, "success": true, "seconds": 3.38}
          31 +{"count": 4, "seed": 30, "steps": 168, "success": true, "seconds": 5.26}
```

</details>

<a id="C008"></a>
### C008 · Keep vacuum grasp proximity clear to prevent attaching two neighboring blocks

Commit `2c8ccf93c784b3875bf5bc5d75e02b55e5cc28a0`; parents: 56e8c6c08294a6ecee4669861d506320de347c66. Recorded author date: 2026-09-21T17:28:10Z.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0055](01_timeline.md#E0055): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_2c8ccf9_approach.py) · [Exact all-file diff](evidence/diffs/C008_2c8ccf9.diff)

[Previous saved controller snapshot](evidence/versions/C007_56e8c6c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1701ba4..fb5cdee 100644
--- a/approach.py
+++ b/approach.py
@@ -31,7 +31,7 @@ class GeneratedApproach:
   31     31          dx=max(q[0]-rx,0,rx-q[0]-q[2])
   32     32          dy=max(q[1]-ry,0,ry-q[1]-q[3])
   33     33          return (self.overlap((x,y,w,h),q)
   34        -                or self.overlap((rx-.035,ry-.21,.07,.01),q)
          34 +                or self.overlap((rx-.035,ry-.21,.07,.01),q,margin=.014)
   35     35                  or self.overlap((rx-.008,ry-.2,.016,.2),q)
   36     36                  or dx*dx+dy*dy<.103**2)
   37     37  
diff --git a/probe_recheck319.jsonl b/probe_recheck319.jsonl
new file mode 100644
index 0000000..6061f81
--- /dev/null
+++ b/probe_recheck319.jsonl
@@ -0,0 +1 @@
           1 +{"seed": 319, "success": false, "steps": 1000, "seconds": 10.72, "phase": "carry", "task": "obstruction1", "robot": [0.7737568020820618, 0.7229787707328796], "taskxy": [0.7957567572593689, 0.3200226128101349], "dest": [0.7957568021207242, 0.105]}
diff --git a/probe_validation_239_260_459.jsonl b/probe_validation_239_260_459.jsonl
index 4fdac47..0469080 100644
--- a/probe_validation_239_260_459.jsonl
+++ b/probe_validation_239_260_459.jsonl
@@ -176,3 +176,12 @@
  176    176  {"seed": 434, "success": true, "steps": 47, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [1.186089038848877, 0.43385952711105347], "taskxy": [1.14407217502594, 0.10499998927116394], "dest": [1.1440721384882926, 0.10500000149011612]}
  177    177  {"seed": 435, "success": true, "steps": 103, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.7736154198646545, 0.46176329255104065], "taskxy": [0.6938204765319824, 0.10499998182058334], "dest": [0.6938204507827759, 0.10500000149011612]}
  178    178  {"seed": 436, "success": true, "steps": 140, "seconds": 0.43, "phase": "place", "task": "target_block", "robot": [0.5325717329978943, 0.5100000500679016], "taskxy": [0.45083412528038025, 0.1119426041841507], "dest": [0.4508340995311737, 0.10500000149011612]}
         179 +{"seed": 437, "success": true, "steps": 112, "seconds": 0.49, "phase": "place", "task": "target_block", "robot": [0.6703659296035767, 0.42911556363105774], "taskxy": [0.5936304330825806, 0.10499993711709976], "dest": [0.5936303924322128, 0.10500000149011612]}
         180 +{"seed": 438, "success": true, "steps": 91, "seconds": 1.07, "phase": "place", "task": "target_block", "robot": [0.6167632341384888, 0.4099999964237213], "taskxy": [0.5296130180358887, 0.11335067451000214], "dest": [0.5296130518913269, 0.10500000149011612]}
         181 +{"seed": 439, "success": true, "steps": 53, "seconds": 0.54, "phase": "place", "task": "target_block", "robot": [0.2713389992713928, 0.4646719992160797], "taskxy": [0.22512543201446533, 0.10500000417232513], "dest": [0.22512545096874237, 0.10500000149011612]}
         182 +{"seed": 440, "success": true, "steps": 40, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.9498897194862366, 0.48621055483818054], "taskxy": [0.9097335338592529, 0.10500002652406693], "dest": [0.9097336124181747, 0.10500000149011612]}
         183 +{"seed": 441, "success": true, "steps": 121, "seconds": 1.11, "phase": "place", "task": "target_block", "robot": [0.6751702427864075, 0.3700801134109497], "taskxy": [0.5988636016845703, 0.10499995946884155], "dest": [0.598863516330719, 0.10500000149011612]}
         184 +{"seed": 442, "success": true, "steps": 31, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.7107297778129578, 0.5182258486747742], "taskxy": [0.6200562119483948, 0.10499998927116394], "dest": [0.6200561780929565, 0.10500000149011612]}
         185 +{"seed": 443, "success": true, "steps": 57, "seconds": 0.52, "phase": "place", "task": "target_block", "robot": [0.9791145920753479, 0.5099999904632568], "taskxy": [0.920532763004303, 0.12427860498428345], "dest": [0.9205327521562576, 0.10500000149011612]}
         186 +{"seed": 444, "success": true, "steps": 104, "seconds": 1.19, "phase": "place", "task": "target_block", "robot": [1.193660020828247, 0.5099999904632568], "taskxy": [1.1656880378723145, 0.1185615286231041], "dest": [1.1656879444122314, 0.10500000149011612]}
         187 +{"seed": 445, "success": true, "steps": 42, "seconds": 0.4, "phase": "place", "task": "target_block", "robot": [0.25367891788482666, 0.5099999904632568], "taskxy": [0.1572979837656021, 0.12112739682197571], "dest": [0.15729798036813736, 0.10500000149011612]}
diff --git a/results_fast.jsonl b/results_fast.jsonl
new file mode 100644
index 0000000..9f04e50
--- /dev/null
+++ b/results_fast.jsonl
@@ -0,0 +1,83 @@
           1 +{"seed": 0, "success": true, "steps": 92, "seconds": 0.87, "phase": "place", "task": "target_block", "robot": [0.7908053398132324, 0.39254191517829895], "taskxy": [0.7405965328216553, 0.10499999672174454], "dest": [0.740596498966217, 0.10500000149011612]}
           2 +{"seed": 1, "success": true, "steps": 64, "seconds": 0.64, "phase": "place", "task": "target_block", "robot": [0.9666023254394531, 0.47871848940849304], "taskxy": [0.8694780468940735, 0.10499999672174454], "dest": [0.86947807264328, 0.10500000149011612]}
           3 +{"seed": 2, "success": true, "steps": 82, "seconds": 1.02, "phase": "place", "task": "target_block", "robot": [0.9954461455345154, 0.5192327499389648], "taskxy": [0.9415640234947205, 0.10818088054656982], "dest": [0.941564049243927, 0.10500000149011612]}
           4 +{"seed": 3, "success": true, "steps": 58, "seconds": 0.64, "phase": "place", "task": "target_block", "robot": [1.2916557788848877, 0.463218092918396], "taskxy": [1.2164483070373535, 0.10596683621406555], "dest": [1.2164482135772705, 0.10500000149011612]}
           5 +{"seed": 4, "success": true, "steps": 60, "seconds": 0.84, "phase": "place", "task": "target_block", "robot": [1.4231510162353516, 0.3961791694164276], "taskxy": [1.3380084037780762, 0.10500002652406693], "dest": [1.3380084295272827, 0.10500000149011612]}
           6 +{"seed": 5, "success": true, "steps": 118, "seconds": 1.31, "phase": "place", "task": "target_block", "robot": [0.24981090426445007, 0.3767912685871124], "taskxy": [0.19417539238929749, 0.10499998182058334], "dest": [0.19417539644241333, 0.10500000149011612]}
           7 +{"seed": 6, "success": true, "steps": 55, "seconds": 0.69, "phase": "place", "task": "target_block", "robot": [1.1417206525802612, 0.41949453949928284], "taskxy": [1.0661463737487793, 0.10500002652406693], "dest": [1.0661463994979858, 0.10500000149011612]}
           8 +{"seed": 7, "success": true, "steps": 121, "seconds": 0.99, "phase": "place", "task": "target_block", "robot": [0.2030080407857895, 0.4101998209953308], "taskxy": [0.14074254035949707, 0.10807256400585175], "dest": [0.14074252951145172, 0.10500000149011612]}
           9 +{"seed": 8, "success": true, "steps": 76, "seconds": 0.52, "phase": "place", "task": "target_block", "robot": [0.29301244020462036, 0.46457359194755554], "taskxy": [0.2498759925365448, 0.10500001162290573], "dest": [0.24987597423791885, 0.10500000149011612]}
          10 +{"seed": 9, "success": true, "steps": 86, "seconds": 0.54, "phase": "place", "task": "target_block", "robot": [1.5061836242675781, 0.3970007002353668], "taskxy": [1.4225263595581055, 0.12020336836576462], "dest": [1.422526385307312, 0.10500000149011612]}
          11 +{"seed": 10, "success": true, "steps": 38, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [0.3620208501815796, 0.436652809381485], "taskxy": [0.31965431571006775, 0.10499998927116394], "dest": [0.31965430825948715, 0.10500000149011612]}
          12 +{"seed": 11, "success": true, "steps": 44, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [1.4770435094833374, 0.3894661068916321], "taskxy": [1.4467620849609375, 0.10499999672174454], "dest": [1.4467619915008545, 0.10500000149011612]}
          13 +{"seed": 12, "success": true, "steps": 82, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [1.448280692100525, 0.40195518732070923], "taskxy": [1.3729972839355469, 0.11969327926635742], "dest": [1.3729971904754639, 0.10500000149011612]}
          14 +{"seed": 13, "success": true, "steps": 68, "seconds": 0.48, "phase": "place", "task": "target_block", "robot": [1.047287106513977, 0.43553492426872253], "taskxy": [0.950922429561615, 0.10500000417232513], "dest": [0.9509224817156792, 0.10500000149011612]}
          15 +{"seed": 14, "success": true, "steps": 26, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.8645416498184204, 0.47744715213775635], "taskxy": [0.7823680639266968, 0.10499998927116394], "dest": [0.7823681126832962, 0.10500000149011612]}
          16 +{"seed": 15, "success": true, "steps": 25, "seconds": 0.08, "phase": "place", "task": "target_block", "robot": [0.7686994075775146, 0.42260345816612244], "taskxy": [0.6975526213645935, 0.12006070464849472], "dest": [0.697552561044693, 0.10500000149011612]}
          17 +{"seed": 16, "success": true, "steps": 22, "seconds": 0.06, "phase": "place", "task": "target_block", "robot": [0.2922910451889038, 0.4981074333190918], "taskxy": [0.201693594455719, 0.10499999672174454], "dest": [0.20169359850883484, 0.10500000149011612]}
          18 +{"seed": 17, "success": true, "steps": 74, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [1.2162362337112427, 0.46170151233673096], "taskxy": [1.1591240167617798, 0.10500002652406693], "dest": [1.1591239951252936, 0.10500000149011612]}
          19 +{"seed": 18, "success": true, "steps": 57, "seconds": 0.17, "phase": "place", "task": "target_block", "robot": [0.9564871191978455, 0.3807637691497803], "taskxy": [0.8622569441795349, 0.10499997437000275], "dest": [0.8622569333314896, 0.10500000149011612]}
          20 +{"seed": 19, "success": true, "steps": 53, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [0.6275244951248169, 0.45080500841140747], "taskxy": [0.5439521074295044, 0.10500002652406693], "dest": [0.5439521331787109, 0.10500000149011612]}
          21 +{"seed": 20, "success": true, "steps": 68, "seconds": 0.2, "phase": "place", "task": "target_block", "robot": [0.28205248713493347, 0.45627561211586], "taskxy": [0.23252740502357483, 0.10500000417232513], "dest": [0.23252737927436828, 0.10500000149011612]}
          22 +{"seed": 21, "success": true, "steps": 52, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [1.5176098346710205, 0.3868604898452759], "taskxy": [1.460854411125183, 0.10500002652406693], "dest": [1.4608544368743897, 0.10500000149011612]}
          23 +{"seed": 22, "success": true, "steps": 101, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [0.28131383657455444, 0.5087708830833435], "taskxy": [0.1924462765455246, 0.11822669208049774], "dest": [0.1924461613893509, 0.10500000149011612]}
          24 +{"seed": 23, "success": true, "steps": 42, "seconds": 0.11, "phase": "place", "task": "target_block", "robot": [1.1582746505737305, 0.40270280838012695], "taskxy": [1.1181412935256958, 0.10500001162290573], "dest": [1.1181413192749023, 0.10500000149011612]}
          25 +{"seed": 24, "success": true, "steps": 59, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [1.2454140186309814, 0.3829645812511444], "taskxy": [1.1548552513122559, 0.10500001162290573], "dest": [1.1548551578521729, 0.10500000149011612]}
          26 +{"seed": 25, "success": true, "steps": 54, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [0.41680049896240234, 0.48804011940956116], "taskxy": [0.31748586893081665, 0.10499998927116394], "dest": [0.3174859176874161, 0.10500000149011612]}
          27 +{"seed": 26, "success": false, "steps": 1000, "seconds": 2.47, "phase": "lift", "task": "obstruction1", "robot": [0.9065601825714111, 0.5442469120025635], "taskxy": [0.928560197353363, 0.10000099986791611], "dest": [0.6336692657502921, 0.105]}
          28 +{"seed": 27, "success": true, "steps": 20, "seconds": 0.05, "phase": "place", "task": "target_block", "robot": [0.5648511052131653, 0.39983999729156494], "taskxy": [0.5390996932983398, 0.10500002652406693], "dest": [0.5390996899008751, 0.10500000149011612]}
          29 +{"seed": 28, "success": true, "steps": 45, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [0.9479617476463318, 0.5126319527626038], "taskxy": [0.8572614789009094, 0.10500000417232513], "dest": [0.8572614450454712, 0.10500000149011612]}
          30 +{"seed": 29, "success": true, "steps": 40, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.33369460701942444, 0.3933916985988617], "taskxy": [0.29740485548973083, 0.10499998182058334], "dest": [0.297404851436615, 0.10500000149011612]}
          31 +{"seed": 30, "success": true, "steps": 25, "seconds": 0.06, "phase": "place", "task": "target_block", "robot": [0.7523328065872192, 0.3864370584487915], "taskxy": [0.7028486728668213, 0.10499998182058334], "dest": [0.7028486992716789, 0.10500000149011612]}
          32 +{"seed": 31, "success": true, "steps": 37, "seconds": 0.11, "phase": "place", "task": "target_block", "robot": [1.5178000926971436, 0.3989855945110321], "taskxy": [1.5220670700073242, 0.10750607401132584], "dest": [1.5220670707225799, 0.10500000149011612]}
          33 +{"seed": 32, "success": true, "steps": 91, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [1.1594833135604858, 0.5175359845161438], "taskxy": [1.0761679410934448, 0.10499995201826096], "dest": [1.0761679668426514, 0.10500000149011612]}
          34 +{"seed": 33, "success": true, "steps": 61, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.39699721336364746, 0.5100560188293457], "taskxy": [0.3021954298019409, 0.11984580010175705], "dest": [0.302195374250412, 0.10500000149011612]}
          35 +{"seed": 34, "success": true, "steps": 32, "seconds": 0.07, "phase": "place", "task": "target_block", "robot": [0.9681728482246399, 0.5049582719802856], "taskxy": [0.8771185278892517, 0.10499998182058334], "dest": [0.8771186213493347, 0.10500000149011612]}
          36 +{"seed": 35, "success": true, "steps": 31, "seconds": 0.08, "phase": "place", "task": "target_block", "robot": [1.3312755823135376, 0.506248950958252], "taskxy": [1.272279143333435, 0.10500004142522812], "dest": [1.2722791026830673, 0.10500000149011612]}
          37 +{"seed": 36, "success": true, "steps": 43, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.5443218946456909, 0.5013031363487244], "taskxy": [0.47916486859321594, 0.10499997437000275], "dest": [0.4791648726463318, 0.10500000149011612]}
          38 +{"seed": 37, "success": true, "steps": 31, "seconds": 0.09, "phase": "place", "task": "target_block", "robot": [0.49799245595932007, 0.3796648383140564], "taskxy": [0.39944636821746826, 0.10499998927116394], "dest": [0.39944628286361694, 0.10500000149011612]}
          39 +{"seed": 38, "success": true, "steps": 21, "seconds": 0.06, "phase": "place", "task": "target_block", "robot": [0.8291525840759277, 0.4444895386695862], "taskxy": [0.7415208220481873, 0.10499999672174454], "dest": [0.7415208410024643, 0.10500000149011612]}
          40 +{"seed": 39, "success": true, "steps": 62, "seconds": 0.17, "phase": "place", "task": "target_block", "robot": [0.515974760055542, 0.4242390990257263], "taskxy": [0.4454716742038727, 0.10500001162290573], "dest": [0.4454717181921005, 0.10500000149011612]}
          41 +{"seed": 40, "success": true, "steps": 60, "seconds": 0.17, "phase": "place", "task": "target_block", "robot": [1.0161664485931396, 0.4207586348056793], "taskxy": [0.955490231513977, 0.10500002652406693], "dest": [0.9554902572631836, 0.10500000149011612]}
          42 +{"seed": 41, "success": true, "steps": 32, "seconds": 0.09, "phase": "place", "task": "target_block", "robot": [0.6760239601135254, 0.46037498116493225], "taskxy": [0.6126683354377747, 0.10499999672174454], "dest": [0.6126682900190353, 0.10500000149011612]}
          43 +{"seed": 42, "success": true, "steps": 31, "seconds": 0.09, "phase": "place", "task": "target_block", "robot": [0.4095580577850342, 0.48790961503982544], "taskxy": [0.3274724781513214, 0.10499996691942215], "dest": [0.32747245240211487, 0.10500000149011612]}
          44 +{"seed": 43, "success": true, "steps": 27, "seconds": 0.08, "phase": "place", "task": "target_block", "robot": [0.8216844201087952, 0.4223349690437317], "taskxy": [0.7403000593185425, 0.1177811399102211], "dest": [0.7402999888658524, 0.10500000149011612]}
          45 +{"seed": 44, "success": true, "steps": 66, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [1.1286044120788574, 0.43070754408836365], "taskxy": [1.0913759469985962, 0.11501327157020569], "dest": [1.091375988304615, 0.10500000149011612]}
          46 +{"seed": 45, "success": true, "steps": 94, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.8072885870933533, 0.46456602215766907], "taskxy": [0.722580075263977, 0.1103527769446373], "dest": [0.7225800346136093, 0.10500000149011612]}
          47 +{"seed": 46, "success": true, "steps": 39, "seconds": 0.11, "phase": "place", "task": "target_block", "robot": [0.9157004952430725, 0.44781431555747986], "taskxy": [0.8428284525871277, 0.11100126802921295], "dest": [0.8428284816741943, 0.10500000149011612]}
          48 +{"seed": 47, "success": true, "steps": 38, "seconds": 0.09, "phase": "place", "task": "target_block", "robot": [0.8696834444999695, 0.49866390228271484], "taskxy": [0.829658567905426, 0.10500001907348633], "dest": [0.8296585936546326, 0.10500000149011612]}
          49 +{"seed": 48, "success": true, "steps": 22, "seconds": 0.06, "phase": "place", "task": "target_block", "robot": [1.2655636072158813, 0.4491959512233734], "taskxy": [1.196325421333313, 0.10499995946884155], "dest": [1.1963254470825195, 0.10500000149011612]}
          50 +{"seed": 49, "success": true, "steps": 21, "seconds": 0.06, "phase": "place", "task": "target_block", "robot": [0.942194938659668, 0.5193631649017334], "taskxy": [0.8589697480201721, 0.10500001162290573], "dest": [0.8589697371721268, 0.10500000149011612]}
          51 +{"seed": 50, "success": true, "steps": 70, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.722407341003418, 0.4533366560935974], "taskxy": [0.6925303936004639, 0.10500000417232513], "dest": [0.6925305269956589, 0.10500000149011612]}
          52 +{"seed": 51, "success": true, "steps": 37, "seconds": 0.09, "phase": "place", "task": "target_block", "robot": [0.7855203747749329, 0.47989869117736816], "taskxy": [0.7000908255577087, 0.10499997437000275], "dest": [0.7000909109115601, 0.10500000149011612]}
          53 +{"seed": 52, "success": true, "steps": 81, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [0.5762956738471985, 0.44454696774482727], "taskxy": [0.49785348773002625, 0.10499999672174454], "dest": [0.4978534768819809, 0.10500000149011612]}
          54 +{"seed": 53, "success": true, "steps": 92, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.7180459499359131, 0.38794079422950745], "taskxy": [0.6186805963516235, 0.11498072743415833], "dest": [0.6186806153059006, 0.10500000149011612]}
          55 +{"seed": 54, "success": true, "steps": 30, "seconds": 0.08, "phase": "place", "task": "target_block", "robot": [1.49070143699646, 0.38928577303886414], "taskxy": [1.4156248569488525, 0.10500001162290573], "dest": [1.415624882698059, 0.10500000149011612]}
          56 +{"seed": 55, "success": true, "steps": 25, "seconds": 0.08, "phase": "place", "task": "target_block", "robot": [0.6290305852890015, 0.4394877851009369], "taskxy": [0.5789647698402405, 0.10499998927116394], "dest": [0.5789648108184338, 0.10500000149011612]}
          57 +{"seed": 56, "success": true, "steps": 64, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [1.4555909633636475, 0.3702752888202667], "taskxy": [1.4038506746292114, 0.10499998182058334], "dest": [1.403850700378418, 0.10500000149011612]}
          58 +{"seed": 57, "success": true, "steps": 18, "seconds": 0.04, "phase": "place", "task": "target_block", "robot": [0.6021356582641602, 0.4789508879184723], "taskxy": [0.5449443459510803, 0.10499997437000275], "dest": [0.5449443425536156, 0.10500000149011612]}
          59 +{"seed": 58, "success": true, "steps": 60, "seconds": 0.16, "phase": "place", "task": "target_block", "robot": [0.896597146987915, 0.3907721936702728], "taskxy": [0.8486972451210022, 0.10500001162290573], "dest": [0.848697211265564, 0.10500000149011612]}
          60 +{"seed": 59, "success": true, "steps": 63, "seconds": 0.2, "phase": "place", "task": "target_block", "robot": [1.2168527841567993, 0.44906941056251526], "taskxy": [1.1603264808654785, 0.10500000417232513], "dest": [1.160326506614685, 0.10500000149011612]}
          61 +{"seed": 60, "success": true, "steps": 25, "seconds": 0.07, "phase": "place", "task": "target_block", "robot": [0.6079646348953247, 0.38666898012161255], "taskxy": [0.5506205558776855, 0.10499999672174454], "dest": [0.5506205822825432, 0.10500000149011612]}
          62 +{"seed": 61, "success": true, "steps": 68, "seconds": 0.19, "phase": "place", "task": "target_block", "robot": [0.508681058883667, 0.5121599435806274], "taskxy": [0.40882420539855957, 0.10499997437000275], "dest": [0.4088242094516754, 0.10500000149011612]}
          63 +{"seed": 62, "success": true, "steps": 63, "seconds": 0.19, "phase": "place", "task": "target_block", "robot": [1.3378404378890991, 0.5010924935340881], "taskxy": [1.274317741394043, 0.10500004142522812], "dest": [1.2743177671432495, 0.10500000149011612]}
          64 +{"seed": 63, "success": true, "steps": 43, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.7719020247459412, 0.4131719172000885], "taskxy": [0.7193305492401123, 0.10499999672174454], "dest": [0.719330501139164, 0.10500000149011612]}
          65 +{"seed": 64, "success": true, "steps": 29, "seconds": 0.08, "phase": "place", "task": "target_block", "robot": [0.4470420479774475, 0.46380719542503357], "taskxy": [0.34813961386680603, 0.10499999672174454], "dest": [0.34813969242572784, 0.10500000149011612]}
          66 +{"seed": 65, "success": true, "steps": 19, "seconds": 0.05, "phase": "place", "task": "target_block", "robot": [0.3692214787006378, 0.37646761536598206], "taskxy": [0.32330766320228577, 0.10499999672174454], "dest": [0.3233076523542404, 0.10500000149011612]}
          67 +{"seed": 66, "success": true, "steps": 60, "seconds": 0.17, "phase": "place", "task": "target_block", "robot": [1.208558440208435, 0.4594087302684784], "taskxy": [1.123029351234436, 0.10499998927116394], "dest": [1.1230293552875519, 0.10500000149011612]}
          68 +{"seed": 67, "success": true, "steps": 51, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [0.29200199246406555, 0.4232950806617737], "taskxy": [0.24387986958026886, 0.10499999672174454], "dest": [0.2438798885345459, 0.10500000149011612]}
          69 +{"seed": 68, "success": true, "steps": 47, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.4629645347595215, 0.3822043240070343], "taskxy": [0.39746949076652527, 0.10500001162290573], "dest": [0.3974694867134094, 0.10500000149011612]}
          70 +{"seed": 69, "success": true, "steps": 36, "seconds": 0.1, "phase": "place", "task": "target_block", "robot": [0.2170093059539795, 0.43561235070228577], "taskxy": [0.15116170048713684, 0.10499999672174454], "dest": [0.15116179394721985, 0.10500000149011612]}
          71 +{"seed": 70, "success": true, "steps": 49, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [1.2810150384902954, 0.37043750286102295], "taskxy": [1.2404487133026123, 0.10500001162290573], "dest": [1.2404485832452774, 0.10500000149011612]}
          72 +{"seed": 71, "success": true, "steps": 42, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [1.0334404706954956, 0.40021178126335144], "taskxy": [0.969202995300293, 0.10500002652406693], "dest": [0.969202939748764, 0.10500000149011612]}
          73 +{"seed": 72, "success": true, "steps": 97, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.24024903774261475, 0.4113594591617584], "taskxy": [0.19537508487701416, 0.11146795749664307], "dest": [0.1953750963807106, 0.10500000149011612]}
          74 +{"seed": 73, "success": true, "steps": 59, "seconds": 0.19, "phase": "place", "task": "target_block", "robot": [1.1164097785949707, 0.4124401807785034], "taskxy": [1.0341856479644775, 0.12427147477865219], "dest": [1.034185673713684, 0.10500000149011612]}
          75 +{"seed": 74, "success": true, "steps": 24, "seconds": 0.07, "phase": "place", "task": "target_block", "robot": [1.5013700723648071, 0.48225638270378113], "taskxy": [1.476072072982788, 0.10500003397464752], "dest": [1.4760720987319946, 0.10500000149011612]}
          76 +{"seed": 75, "success": true, "steps": 73, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [1.4256352186203003, 0.5120925307273865], "taskxy": [1.331120491027832, 0.10499999672174454], "dest": [1.3311206359863281, 0.10500000149011612]}
          77 +{"seed": 76, "success": true, "steps": 30, "seconds": 0.09, "phase": "place", "task": "target_block", "robot": [0.5033426880836487, 0.5277675986289978], "taskxy": [0.43621283769607544, 0.11775586009025574], "dest": [0.4362128417491913, 0.10500000149011612]}
          78 +{"seed": 77, "success": true, "steps": 22, "seconds": 0.05, "phase": "place", "task": "target_block", "robot": [0.716909646987915, 0.3836202323436737], "taskxy": [0.6318120360374451, 0.10499999672174454], "dest": [0.6318120617866516, 0.10500000149011612]}
          79 +{"seed": 78, "success": true, "steps": 99, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.6102669835090637, 0.4086683690547943], "taskxy": [0.5429975390434265, 0.10499998927116394], "dest": [0.5429975051879883, 0.10500000149011612]}
          80 +{"seed": 79, "success": true, "steps": 34, "seconds": 0.08, "phase": "place", "task": "target_block", "robot": [0.309327095746994, 0.4262494444847107], "taskxy": [0.2484995722770691, 0.10500003397464752], "dest": [0.24849958312511444, 0.10500000149011612]}
          81 +{"seed": 80, "success": true, "steps": 68, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.38471460342407227, 0.4364992380142212], "taskxy": [0.30512362718582153, 0.10500005632638931], "dest": [0.30512363463640213, 0.10500000149011612]}
          82 +{"seed": 81, "success": true, "steps": 25, "seconds": 0.07, "phase": "place", "task": "target_block", "robot": [0.593959391117096, 0.3846059739589691], "taskxy": [0.534056544303894, 0.10499999672174454], "dest": [0.5340565558075905, 0.10500000149011612]}
          83 +{"seed": 82, "success": true, "steps": 37, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [1.2759501934051514, 0.45464026927948], "taskxy": [1.2153900861740112, 0.11872528493404388], "dest": [1.215390176296234, 0.10500000149011612]}
```

</details>

<a id="C009"></a>
### C009 · Distinguish existing close-packed pickup geometry from placement clearance

Commit `4942e85ec3e5c6faa35a66cd13cd62b220ff5373`; parents: 2c8ccf93c784b3875bf5bc5d75e02b55e5cc28a0. Recorded author date: 2026-09-21T17:28:39Z.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0059](01_timeline.md#E0059): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C009_4942e85_approach.py) · [Exact all-file diff](evidence/diffs/C009_4942e85.diff)

[Previous saved controller snapshot](evidence/versions/C008_2c8ccf9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index fb5cdee..bedf44b 100644
--- a/approach.py
+++ b/approach.py
@@ -26,18 +26,18 @@ class GeneratedApproach:
   26     26      def overlap(a,b,margin=.003):
   27     27          return a[0]<b[0]+b[2]+margin and a[0]+a[2]>b[0]-margin and a[1]<b[1]+b[3]+margin and a[1]+a[3]>b[1]-margin
   28     28  
   29        -    def hits_configuration(self,q,x,y,w,h,offset):
          29 +    def hits_configuration(self,q,x,y,w,h,offset,body_margin=.003):
   30     30          rx=x+offset;ry=y+h+.215
   31     31          dx=max(q[0]-rx,0,rx-q[0]-q[2])
   32     32          dy=max(q[1]-ry,0,ry-q[1]-q[3])
   33        -        return (self.overlap((x,y,w,h),q)
          33 +        return (self.overlap((x,y,w,h),q,margin=body_margin)
   34     34                  or self.overlap((rx-.035,ry-.21,.07,.01),q,margin=.014)
   35     35                  or self.overlap((rx-.008,ry-.2,.016,.2),q)
   36     36                  or dx*dx+dy*dy<.103**2)
   37     37  
   38        -    def conflicts(self,s,obj,x,y,offset,others):
          38 +    def conflicts(self,s,obj,x,y,offset,others,pickup=False):
   39     39          _,_,w,h=self.rect(s,obj)
   40        -        return [o for o in others if self.hits_configuration(self.rect(s,o),x,y,w,h,offset)]
          40 +        return [o for o in others if self.hits_configuration(self.rect(s,o),x,y,w,h,offset,body_margin=.00001 if pickup else .003)]
   41     41  
   42     42      def offsets(self,x,px,w):
   43     43          low=max(.1002-x,.1002-px,-.022)
@@ -57,7 +57,7 @@ class GeneratedApproach:
   57     57          plans=[]
   58     58          for gx in candidates:
   59     59              for offset in self.offsets(bx,gx,bw):
   60        -                bad=set(self.conflicts(s,self.block,gx,sy+sh+.005,offset,obs)+self.conflicts(s,self.block,bx,by,offset,obs))
          60 +                bad=set(self.conflicts(s,self.block,gx,sy+sh+.005,offset,obs)+self.conflicts(s,self.block,bx,by,offset,obs,True))
   61     61                  plans.append(((len(bad),abs(offset-bw/2)*.2+abs(gx-bx)*.01),gx,offset,bad))
   62     62          if not plans:
   63     63              gx=(lo+hi)/2;offset=max(.1002-bx,min(1.5178-gx,bw/2))
@@ -76,7 +76,7 @@ class GeneratedApproach:
   76     76                  others=[p for p in obs+[self.block] if p!=o]
   77     77                  grasps=[]
   78     78                  for off in self.offsets(x,x,w):
   79        -                    blocking=self.conflicts(s,o,x,y,off,others)
          79 +                    blocking=self.conflicts(s,o,x,y,off,others,True)
   80     80                      grasps.append((len(blocking),abs(off-w/2),off,blocking))
   81     81                  best=min(grasps,key=lambda z:z[:2])
   82     82                  if not best[0]:break
@@ -93,7 +93,7 @@ class GeneratedApproach:
   93     93                  if py+h>.43:continue
   94     94                  if self.hits_configuration((px,py,w,h),*keep_pick) or self.hits_configuration((px,py,w,h),*keep_place):continue
   95     95                  for off in self.offsets(x,px,w):
   96        -                    blockers=self.conflicts(s,o,x,y,off,others)+self.conflicts(s,o,px,py,off,others)
          96 +                    blockers=self.conflicts(s,o,x,y,off,others,True)+self.conflicts(s,o,px,py,off,others)
   97     97                      if not blockers:
   98     98                          places.append((py*8+abs(px-x)+abs(off-w/2)*.2,float(px),py,off))
   99     99              if places:
@@ -107,7 +107,7 @@ class GeneratedApproach:
  107    107                      py=max([.105]+[qy+qh+.025 for qx,qy,qw,qh in occupied if px<qx+qw+.04 and px+w>qx-.04])
  108    108                      if self.hits_configuration((px,py,w,h),*keep_pick) or self.hits_configuration((px,py,w,h),*keep_place):continue
  109    109                      for off in self.offsets(x,px,w):
  110        -                        blockers=self.conflicts(s,o,x,y,off,others)+self.conflicts(s,o,px,py,off,others)
         110 +                        blockers=self.conflicts(s,o,x,y,off,others,True)+self.conflicts(s,o,px,py,off,others)
  111    111                          fallback.append((len(blockers),py*8+abs(px-x),float(px),py,off))
  112    112                  _,_,px,py,offset=min(fallback)
  113    113                  self.dest=(px,py)
diff --git a/probe319_fix.py b/probe319_fix.py
new file mode 100644
index 0000000..0e62886
--- /dev/null
+++ b/probe319_fix.py
@@ -0,0 +1,15 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +class Probe(GeneratedApproach):
           4 + def conflicts(self,s,obj,x,y,offset,others):
           5 +  _,_,w,h=self.rect(s,obj);rx=x+offset;ry=y+h+.215
           6 +  gripper=(rx-.035,ry-.21,.07,.01);arm=(rx-.008,ry-.2,.016,.2);bad=[]
           7 +  for o in others:
           8 +   q=self.rect(s,o);dx=max(q[0]-rx,0,rx-q[0]-q[2]);dy=max(q[1]-ry,0,ry-q[1]-q[3])
           9 +   if self.overlap((x,y,w,h),q,.0002) or self.overlap(gripper,q,.014) or self.overlap(arm,q) or dx*dx+dy*dy<.103**2:bad.append(o)
          10 +  return bad
          11 +E=make_env();s,i=E.reset(seed=319);a=Probe(E.action_space,E.observation_space,{});a.reset(s,i)
          12 +for n in range(1000):
          13 + act=a.get_action(s);s,r,t,tr,_=E.step(act)
          14 + if t:break
          15 +print('success',t,'steps',n+1,'phase',a.phase);E.close()
diff --git a/results_fast.jsonl b/results_fast.jsonl
index 9f04e50..382befd 100644
--- a/results_fast.jsonl
+++ b/results_fast.jsonl
@@ -81,3 +81,22 @@
   81     81  {"seed": 80, "success": true, "steps": 68, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.38471460342407227, 0.4364992380142212], "taskxy": [0.30512362718582153, 0.10500005632638931], "dest": [0.30512363463640213, 0.10500000149011612]}
   82     82  {"seed": 81, "success": true, "steps": 25, "seconds": 0.07, "phase": "place", "task": "target_block", "robot": [0.593959391117096, 0.3846059739589691], "taskxy": [0.534056544303894, 0.10499999672174454], "dest": [0.5340565558075905, 0.10500000149011612]}
   83     83  {"seed": 82, "success": true, "steps": 37, "seconds": 0.12, "phase": "place", "task": "target_block", "robot": [1.2759501934051514, 0.45464026927948], "taskxy": [1.2153900861740112, 0.11872528493404388], "dest": [1.215390176296234, 0.10500000149011612]}
          84 +{"seed": 83, "success": true, "steps": 111, "seconds": 0.65, "phase": "place", "task": "target_block", "robot": [0.25152280926704407, 0.5031046271324158], "taskxy": [0.16700725257396698, 0.10500004887580872], "dest": [0.1670072864294052, 0.10500000149011612]}
          85 +{"seed": 84, "success": true, "steps": 64, "seconds": 0.41, "phase": "place", "task": "target_block", "robot": [0.6042964458465576, 0.4124278724193573], "taskxy": [0.5306367874145508, 0.10500001907348633], "dest": [0.530636821269989, 0.10500000149011612]}
          86 +{"seed": 85, "success": true, "steps": 59, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [0.9010717868804932, 0.3812885880470276], "taskxy": [0.8189694881439209, 0.10500001162290573], "dest": [0.8189695138931274, 0.10500000149011612]}
          87 +{"seed": 86, "success": true, "steps": 45, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.7719181180000305, 0.3897438645362854], "taskxy": [0.6749577522277832, 0.10500000417232513], "dest": [0.6749577779769897, 0.10500000149011612]}
          88 +{"seed": 87, "success": true, "steps": 53, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [1.203840970993042, 0.44531750679016113], "taskxy": [1.1384081840515137, 0.10500002652406693], "dest": [1.1384080905914307, 0.10500000149011612]}
          89 +{"seed": 88, "success": true, "steps": 63, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.4685811400413513, 0.41715937852859497], "taskxy": [0.43061888217926025, 0.10500002652406693], "dest": [0.43061895328760147, 0.10500000149011612]}
          90 +{"seed": 89, "success": true, "steps": 61, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [0.6049009561538696, 0.477839857339859], "taskxy": [0.5215333104133606, 0.1136801466345787], "dest": [0.5215333361625671, 0.10500000149011612]}
          91 +{"seed": 90, "success": true, "steps": 77, "seconds": 0.46, "phase": "place", "task": "target_block", "robot": [0.23972977697849274, 0.5201032757759094], "taskxy": [0.1838860809803009, 0.12488047778606415], "dest": [0.18388607013225555, 0.10500000149011612]}
          92 +{"seed": 91, "success": true, "steps": 43, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.924026608467102, 0.452716201543808], "taskxy": [0.8921021819114685, 0.10500000417232513], "dest": [0.8921022232174873, 0.10500000149011612]}
          93 +{"seed": 92, "success": true, "steps": 54, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [1.0326489210128784, 0.37041032314300537], "taskxy": [1.00502347946167, 0.10500000417232513], "dest": [1.0050235052108765, 0.10500000149011612]}
          94 +{"seed": 93, "success": true, "steps": 76, "seconds": 0.56, "phase": "place", "task": "target_block", "robot": [1.0940169095993042, 0.41185927391052246], "taskxy": [1.0277326107025146, 0.10499999672174454], "dest": [1.0277326364517212, 0.10500000149011612]}
          95 +{"seed": 94, "success": true, "steps": 23, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.6026239395141602, 0.5030219554901123], "taskxy": [0.5353034138679504, 0.10499999672174454], "dest": [0.5353033800125122, 0.10500000149011612]}
          96 +{"seed": 95, "success": true, "steps": 60, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [1.2636786699295044, 0.48673880100250244], "taskxy": [1.2265461683273315, 0.10500001907348633], "dest": [1.226546194076538, 0.10500000149011612]}
          97 +{"seed": 96, "success": true, "steps": 32, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [1.4306432008743286, 0.5141889452934265], "taskxy": [1.398691177368164, 0.10500001907348633], "dest": [1.398691207885742, 0.10500000149011612]}
          98 +{"seed": 97, "success": true, "steps": 36, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.6469581127166748, 0.3773379623889923], "taskxy": [0.6194592118263245, 0.10500001907348633], "dest": [0.6194591637253761, 0.10500000149011612]}
          99 +{"seed": 98, "success": true, "steps": 57, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [0.23062244057655334, 0.41795989871025085], "taskxy": [0.14807526767253876, 0.10500001907348633], "dest": [0.1480752568244934, 0.10500000149011612]}
         100 +{"seed": 99, "success": true, "steps": 46, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [1.2927566766738892, 0.4704902172088623], "taskxy": [1.2396767139434814, 0.10499997437000275], "dest": [1.239676739692688, 0.10500000149011612]}
         101 +{"seed": 239, "success": true, "steps": 65, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [0.16682486236095428, 0.38093799352645874], "taskxy": [0.15599285066127777, 0.10500001907348633], "dest": [0.15599279779195785, 0.10500000149011612]}
         102 +{"seed": 319, "success": false, "steps": 1000, "seconds": 5.8, "phase": "carry", "task": "obstruction1", "robot": [0.7737568020820618, 0.7229787707328796], "taskxy": [0.7957567572593689, 0.3200226128101349], "dest": [0.7957568021207242, 0.105]}
```

</details>

<a id="C010"></a>
### C010 · Add reproducible count-controlled validation with policy runtime measurement

Commit `ca0e8ec24a2bdf8ac40eb8d6f3d0e75bb6fde39d`; parents: 4942e85ec3e5c6faa35a66cd13cd62b220ff5373. Recorded author date: 2026-09-21T17:29:27Z.

File roles (automatic): diagnostic/test.

- [E0077](01_timeline.md#E0077): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C010_ca0e8ec.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_final_0_499.jsonl b/probe_final_0_499.jsonl
new file mode 100644
index 0000000..90bd59a
--- /dev/null
+++ b/probe_final_0_499.jsonl
@@ -0,0 +1,36 @@
           1 +{"seed": 0, "success": true, "steps": 92, "seconds": 0.81, "phase": "place", "task": "target_block", "robot": [0.7908053398132324, 0.39254191517829895], "taskxy": [0.7405965328216553, 0.10499999672174454], "dest": [0.740596498966217, 0.10500000149011612]}
           2 +{"seed": 1, "success": true, "steps": 64, "seconds": 0.4, "phase": "place", "task": "target_block", "robot": [0.9666023254394531, 0.47871848940849304], "taskxy": [0.8694780468940735, 0.10499999672174454], "dest": [0.86947807264328, 0.10500000149011612]}
           3 +{"seed": 2, "success": true, "steps": 82, "seconds": 0.81, "phase": "place", "task": "target_block", "robot": [0.9954461455345154, 0.5192327499389648], "taskxy": [0.9415640234947205, 0.10818088054656982], "dest": [0.941564049243927, 0.10500000149011612]}
           4 +{"seed": 3, "success": true, "steps": 58, "seconds": 0.41, "phase": "place", "task": "target_block", "robot": [1.2916557788848877, 0.463218092918396], "taskxy": [1.2164483070373535, 0.10596683621406555], "dest": [1.2164482135772705, 0.10500000149011612]}
           5 +{"seed": 4, "success": true, "steps": 60, "seconds": 0.4, "phase": "place", "task": "target_block", "robot": [1.4231510162353516, 0.3961791694164276], "taskxy": [1.3380084037780762, 0.10500002652406693], "dest": [1.3380084295272827, 0.10500000149011612]}
           6 +{"seed": 5, "success": true, "steps": 118, "seconds": 1.17, "phase": "place", "task": "target_block", "robot": [0.24981090426445007, 0.3767912685871124], "taskxy": [0.19417539238929749, 0.10499998182058334], "dest": [0.19417539644241333, 0.10500000149011612]}
           7 +{"seed": 6, "success": true, "steps": 55, "seconds": 0.46, "phase": "place", "task": "target_block", "robot": [1.1417206525802612, 0.41949453949928284], "taskxy": [1.0661463737487793, 0.10500002652406693], "dest": [1.0661463994979858, 0.10500000149011612]}
           8 +{"seed": 7, "success": true, "steps": 121, "seconds": 1.11, "phase": "place", "task": "target_block", "robot": [0.2030080407857895, 0.4101998209953308], "taskxy": [0.14074254035949707, 0.10807256400585175], "dest": [0.14074252951145172, 0.10500000149011612]}
           9 +{"seed": 8, "success": true, "steps": 81, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [0.29301249980926514, 0.46457359194755554], "taskxy": [0.2498759776353836, 0.10500002652406693], "dest": [0.24987597423791885, 0.10500000149011612]}
          10 +{"seed": 9, "success": true, "steps": 86, "seconds": 0.69, "phase": "place", "task": "target_block", "robot": [1.5061836242675781, 0.3970007002353668], "taskxy": [1.4225263595581055, 0.12020336836576462], "dest": [1.422526385307312, 0.10500000149011612]}
          11 +{"seed": 10, "success": true, "steps": 38, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.3638133704662323, 0.436652809381485], "taskxy": [0.32144686579704285, 0.10499998927116394], "dest": [0.3214468665122986, 0.10500000149011612]}
          12 +{"seed": 11, "success": true, "steps": 44, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [1.4770435094833374, 0.3894661068916321], "taskxy": [1.4467620849609375, 0.10499999672174454], "dest": [1.4467619915008545, 0.10500000149011612]}
          13 +{"seed": 12, "success": true, "steps": 82, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [1.448280692100525, 0.40195518732070923], "taskxy": [1.3729972839355469, 0.11969327926635742], "dest": [1.3729971904754639, 0.10500000149011612]}
          14 +{"seed": 13, "success": true, "steps": 68, "seconds": 0.46, "phase": "place", "task": "target_block", "robot": [1.047287106513977, 0.43553492426872253], "taskxy": [0.950922429561615, 0.10500000417232513], "dest": [0.9509224817156792, 0.10500000149011612]}
          15 +{"seed": 14, "success": true, "steps": 26, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.8645416498184204, 0.47744715213775635], "taskxy": [0.7823680639266968, 0.10499998927116394], "dest": [0.7823681126832962, 0.10500000149011612]}
          16 +{"seed": 15, "success": true, "steps": 25, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [0.7686994075775146, 0.42260345816612244], "taskxy": [0.6975526213645935, 0.12006070464849472], "dest": [0.697552561044693, 0.10500000149011612]}
          17 +{"seed": 16, "success": true, "steps": 22, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [0.2922910451889038, 0.4981074333190918], "taskxy": [0.201693594455719, 0.10499999672174454], "dest": [0.20169359850883484, 0.10500000149011612]}
          18 +{"seed": 17, "success": true, "steps": 74, "seconds": 0.65, "phase": "place", "task": "target_block", "robot": [1.2162362337112427, 0.46170151233673096], "taskxy": [1.1591240167617798, 0.10500002652406693], "dest": [1.1591239951252936, 0.10500000149011612]}
          19 +{"seed": 18, "success": true, "steps": 57, "seconds": 0.49, "phase": "place", "task": "target_block", "robot": [0.9564871191978455, 0.3807637691497803], "taskxy": [0.8622569441795349, 0.10499997437000275], "dest": [0.8622569333314896, 0.10500000149011612]}
          20 +{"seed": 19, "success": true, "steps": 53, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [0.6275244951248169, 0.45080500841140747], "taskxy": [0.5439521074295044, 0.10500002652406693], "dest": [0.5439521331787109, 0.10500000149011612]}
          21 +{"seed": 20, "success": true, "steps": 68, "seconds": 0.52, "phase": "place", "task": "target_block", "robot": [0.28205248713493347, 0.45627561211586], "taskxy": [0.23252740502357483, 0.10500000417232513], "dest": [0.23252737927436828, 0.10500000149011612]}
          22 +{"seed": 21, "success": true, "steps": 52, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [1.5176098346710205, 0.3868604898452759], "taskxy": [1.460854411125183, 0.10500002652406693], "dest": [1.4608544368743897, 0.10500000149011612]}
          23 +{"seed": 22, "success": true, "steps": 101, "seconds": 0.92, "phase": "place", "task": "target_block", "robot": [0.28131383657455444, 0.5087708830833435], "taskxy": [0.1924462765455246, 0.11822669208049774], "dest": [0.1924461613893509, 0.10500000149011612]}
          24 +{"seed": 23, "success": true, "steps": 42, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [1.1582746505737305, 0.40270280838012695], "taskxy": [1.1181412935256958, 0.10500001162290573], "dest": [1.1181413192749023, 0.10500000149011612]}
          25 +{"seed": 24, "success": true, "steps": 59, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [1.2454140186309814, 0.3829645812511444], "taskxy": [1.1548552513122559, 0.10500001162290573], "dest": [1.1548551578521729, 0.10500000149011612]}
          26 +{"seed": 25, "success": true, "steps": 54, "seconds": 0.43, "phase": "place", "task": "target_block", "robot": [0.41680049896240234, 0.48804011940956116], "taskxy": [0.31748586893081665, 0.10499998927116394], "dest": [0.3174859176874161, 0.10500000149011612]}
          27 +{"seed": 26, "success": true, "steps": 56, "seconds": 0.55, "phase": "place", "task": "target_block", "robot": [1.0472371578216553, 0.5194762945175171], "taskxy": [0.9775223731994629, 0.10500001162290573], "dest": [0.9775223393440247, 0.10500000149011612]}
          28 +{"seed": 27, "success": true, "steps": 20, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [0.5648511052131653, 0.39983999729156494], "taskxy": [0.5390996932983398, 0.10500002652406693], "dest": [0.5390996899008751, 0.10500000149011612]}
          29 +{"seed": 28, "success": true, "steps": 45, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [0.9479617476463318, 0.5126319527626038], "taskxy": [0.8572614789009094, 0.10500000417232513], "dest": [0.8572614450454712, 0.10500000149011612]}
          30 +{"seed": 29, "success": true, "steps": 40, "seconds": 0.41, "phase": "place", "task": "target_block", "robot": [0.33369460701942444, 0.3933916985988617], "taskxy": [0.29740485548973083, 0.10499998182058334], "dest": [0.297404851436615, 0.10500000149011612]}
          31 +{"seed": 30, "success": true, "steps": 25, "seconds": 0.16, "phase": "place", "task": "target_block", "robot": [0.7523328065872192, 0.3864370584487915], "taskxy": [0.7028486728668213, 0.10499998182058334], "dest": [0.7028486992716789, 0.10500000149011612]}
          32 +{"seed": 31, "success": true, "steps": 57, "seconds": 0.53, "phase": "place", "task": "target_block", "robot": [1.517799973487854, 0.40398457646369934], "taskxy": [1.4897868633270264, 0.11250504851341248], "dest": [1.489786889076233, 0.10500000149011612]}
          33 +{"seed": 32, "success": true, "steps": 91, "seconds": 0.87, "phase": "place", "task": "target_block", "robot": [1.1594833135604858, 0.5175359845161438], "taskxy": [1.0761679410934448, 0.10499995201826096], "dest": [1.0761679668426514, 0.10500000149011612]}
          34 +{"seed": 33, "success": true, "steps": 61, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [0.39699721336364746, 0.5100560188293457], "taskxy": [0.3021954298019409, 0.11984580010175705], "dest": [0.302195374250412, 0.10500000149011612]}
          35 +{"seed": 34, "success": true, "steps": 32, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.9681728482246399, 0.5049582719802856], "taskxy": [0.8771185278892517, 0.10499998182058334], "dest": [0.8771186213493347, 0.10500000149011612]}
          36 +{"seed": 35, "success": true, "steps": 31, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [1.3312755823135376, 0.506248950958252], "taskxy": [1.272279143333435, 0.10500004142522812], "dest": [1.2722791026830673, 0.10500000149011612]}
diff --git a/test_counts_scene.py b/test_counts_scene.py
index e4feca4..440e6bc 100644
--- a/test_counts_scene.py
+++ b/test_counts_scene.py
@@ -1,9 +1,9 @@
    1      1  from env_client import make_env
    2      2  from approach import GeneratedApproach
    3      3  import json,time
    4        -f=open('test_counts_scene_v2.jsonl','w')
           4 +f=open('test_counts_scene_v3.jsonl','w')
    5      5  for count in [4,5]:
    6        - for seed in range(31 if count==4 else 11):
           6 + for seed in range(100 if count==4 else 2):
    7      7    e=make_env();start=time.time()
    8      8    try:
    9      9     s,i=e.reset(seed=seed,options={'object_count':count});a=GeneratedApproach(e.action_space,e.observation_space,{})
diff --git a/test_counts_scene_v3.jsonl b/test_counts_scene_v3.jsonl
new file mode 100644
index 0000000..5d99a38
--- /dev/null
+++ b/test_counts_scene_v3.jsonl
@@ -0,0 +1,14 @@
           1 +{"count": 4, "seed": 0, "steps": 89, "success": true, "seconds": 1.02}
           2 +{"count": 4, "seed": 1, "steps": 117, "success": true, "seconds": 1.05}
           3 +{"count": 4, "seed": 2, "steps": 105, "success": true, "seconds": 1.41}
           4 +{"count": 4, "seed": 3, "steps": 84, "success": true, "seconds": 1.35}
           5 +{"count": 4, "seed": 4, "steps": 127, "success": true, "seconds": 0.95}
           6 +{"count": 4, "seed": 5, "steps": 88, "success": true, "seconds": 0.85}
           7 +{"count": 4, "seed": 6, "steps": 123, "success": true, "seconds": 0.89}
           8 +{"count": 4, "seed": 7, "steps": 85, "success": true, "seconds": 1.66}
           9 +{"count": 4, "seed": 8, "steps": 105, "success": true, "seconds": 1.95}
          10 +{"count": 4, "seed": 9, "steps": 79, "success": true, "seconds": 3.46}
          11 +{"count": 4, "seed": 10, "steps": 89, "success": true, "seconds": 1.95}
          12 +{"count": 4, "seed": 11, "steps": 64, "success": true, "seconds": 1.62}
          13 +{"count": 4, "seed": 12, "steps": 105, "success": true, "seconds": 2.76}
          14 +{"count": 4, "seed": 13, "steps": 98, "success": true, "seconds": 2.59}
diff --git a/test_counts_scene_v3.log b/test_counts_scene_v3.log
new file mode 100644
index 0000000..5d99a38
--- /dev/null
+++ b/test_counts_scene_v3.log
@@ -0,0 +1,14 @@
           1 +{"count": 4, "seed": 0, "steps": 89, "success": true, "seconds": 1.02}
           2 +{"count": 4, "seed": 1, "steps": 117, "success": true, "seconds": 1.05}
           3 +{"count": 4, "seed": 2, "steps": 105, "success": true, "seconds": 1.41}
           4 +{"count": 4, "seed": 3, "steps": 84, "success": true, "seconds": 1.35}
           5 +{"count": 4, "seed": 4, "steps": 127, "success": true, "seconds": 0.95}
           6 +{"count": 4, "seed": 5, "steps": 88, "success": true, "seconds": 0.85}
           7 +{"count": 4, "seed": 6, "steps": 123, "success": true, "seconds": 0.89}
           8 +{"count": 4, "seed": 7, "steps": 85, "success": true, "seconds": 1.66}
           9 +{"count": 4, "seed": 8, "steps": 105, "success": true, "seconds": 1.95}
          10 +{"count": 4, "seed": 9, "steps": 79, "success": true, "seconds": 3.46}
          11 +{"count": 4, "seed": 10, "steps": 89, "success": true, "seconds": 1.95}
          12 +{"count": 4, "seed": 11, "steps": 64, "success": true, "seconds": 1.62}
          13 +{"count": 4, "seed": 12, "steps": 105, "success": true, "seconds": 2.76}
          14 +{"count": 4, "seed": 13, "steps": 98, "success": true, "seconds": 2.59}
diff --git a/validate.py b/validate.py
new file mode 100644
index 0000000..4e42bfb
--- /dev/null
+++ b/validate.py
@@ -0,0 +1,32 @@
           1 +"""Black-box validation; this module is not imported by the submitted policy."""
           2 +import argparse
           3 +import json
           4 +import time
           5 +from env_client import make_env
           6 +from approach import GeneratedApproach
           7 +
           8 +p=argparse.ArgumentParser()
           9 +p.add_argument('--start',type=int,default=0)
          10 +p.add_argument('--stop',type=int,default=100)
          11 +p.add_argument('--count',type=int)
          12 +p.add_argument('--out',default='validation.jsonl')
          13 +args=p.parse_args()
          14 +with open(args.out,'w') as out:
          15 + for seed in range(args.start,args.stop):
          16 +  e=make_env()
          17 +  try:
          18 +   s,info=e.reset(seed=seed,options={'object_count':args.count} if args.count is not None else None)
          19 +   a=GeneratedApproach(e.action_space,e.observation_space,{})
          20 +   start=time.perf_counter();a.reset(s,info);compute=time.perf_counter()-start
          21 +   initial={o.name:a.rect(s,o) for o in s.get_objects(a.types['rectangle'])}
          22 +   for n in range(e.max_steps):
          23 +    now=time.perf_counter();action=a.get_action(s);compute+=time.perf_counter()-now
          24 +    s,reward,term,trunc,info=e.step(action)
          25 +    if term or trunc:break
          26 +   row={'seed':seed,'count':args.count,'success':term,'steps':n+1,'policy_seconds':round(compute,4),'elapsed':round(time.perf_counter()-start,3)}
          27 +   if not term:row.update(phase=a.phase,task=a.task.name,dest=a.dest,robot=[s.get(a.robot,f) for f in ('x','y')],initial=initial,final={o.name:a.rect(s,o) for o in s.get_objects(a.types['rectangle'])})
          28 +  except Exception as error:
          29 +   row={'seed':seed,'count':args.count,'error':str(error)}
          30 +  finally:e.close()
          31 +  out.write(json.dumps(row)+'\n');out.flush()
          32 +  if not row.get('success',False):print(json.dumps(row),flush=True)
```

</details>

<a id="C011"></a>
### C011 · Add stress probe for fixed-grasp workspace reachability

Commit `4ef204b1169e79429247b7774e33bece8740190e`; parents: ca0e8ec24a2bdf8ac40eb8d6f3d0e75bb6fde39d. Recorded author date: 2026-09-21T17:30:52Z.

File roles (automatic): diagnostic/test.

- [E0086](01_timeline.md#E0086): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C011_4ef204b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_final_0_499.jsonl b/probe_final_0_499.jsonl
index 90bd59a..54945fd 100644
--- a/probe_final_0_499.jsonl
+++ b/probe_final_0_499.jsonl
@@ -34,3 +34,122 @@
   34     34  {"seed": 33, "success": true, "steps": 61, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [0.39699721336364746, 0.5100560188293457], "taskxy": [0.3021954298019409, 0.11984580010175705], "dest": [0.302195374250412, 0.10500000149011612]}
   35     35  {"seed": 34, "success": true, "steps": 32, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.9681728482246399, 0.5049582719802856], "taskxy": [0.8771185278892517, 0.10499998182058334], "dest": [0.8771186213493347, 0.10500000149011612]}
   36     36  {"seed": 35, "success": true, "steps": 31, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [1.3312755823135376, 0.506248950958252], "taskxy": [1.272279143333435, 0.10500004142522812], "dest": [1.2722791026830673, 0.10500000149011612]}
          37 +{"seed": 36, "success": true, "steps": 43, "seconds": 0.59, "phase": "place", "task": "target_block", "robot": [0.5443218946456909, 0.5013031363487244], "taskxy": [0.47916486859321594, 0.10499997437000275], "dest": [0.4791648726463318, 0.10500000149011612]}
          38 +{"seed": 37, "success": true, "steps": 31, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [0.49799245595932007, 0.3796648383140564], "taskxy": [0.39944636821746826, 0.10499998927116394], "dest": [0.39944628286361694, 0.10500000149011612]}
          39 +{"seed": 38, "success": true, "steps": 21, "seconds": 0.2, "phase": "place", "task": "target_block", "robot": [0.8291525840759277, 0.4444895386695862], "taskxy": [0.7415208220481873, 0.10499999672174454], "dest": [0.7415208410024643, 0.10500000149011612]}
          40 +{"seed": 39, "success": true, "steps": 62, "seconds": 0.93, "phase": "place", "task": "target_block", "robot": [0.515974760055542, 0.4242390990257263], "taskxy": [0.4454716742038727, 0.10500001162290573], "dest": [0.4454717181921005, 0.10500000149011612]}
          41 +{"seed": 40, "success": true, "steps": 60, "seconds": 0.58, "phase": "place", "task": "target_block", "robot": [1.0161664485931396, 0.4207586348056793], "taskxy": [0.955490231513977, 0.10500002652406693], "dest": [0.9554902572631836, 0.10500000149011612]}
          42 +{"seed": 41, "success": true, "steps": 32, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [0.6760239601135254, 0.46037498116493225], "taskxy": [0.6126683354377747, 0.10499999672174454], "dest": [0.6126682900190353, 0.10500000149011612]}
          43 +{"seed": 42, "success": true, "steps": 31, "seconds": 0.36, "phase": "place", "task": "target_block", "robot": [0.4095580577850342, 0.48790961503982544], "taskxy": [0.3274724781513214, 0.10499996691942215], "dest": [0.32747245240211487, 0.10500000149011612]}
          44 +{"seed": 43, "success": true, "steps": 27, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [0.8216844201087952, 0.4223349690437317], "taskxy": [0.7403000593185425, 0.1177811399102211], "dest": [0.7402999888658524, 0.10500000149011612]}
          45 +{"seed": 44, "success": true, "steps": 66, "seconds": 0.87, "phase": "place", "task": "target_block", "robot": [1.1286044120788574, 0.43070754408836365], "taskxy": [1.0913759469985962, 0.11501327157020569], "dest": [1.091375988304615, 0.10500000149011612]}
          46 +{"seed": 45, "success": true, "steps": 94, "seconds": 1.28, "phase": "place", "task": "target_block", "robot": [0.8072885870933533, 0.46456602215766907], "taskxy": [0.722580075263977, 0.1103527769446373], "dest": [0.7225800346136093, 0.10500000149011612]}
          47 +{"seed": 46, "success": true, "steps": 39, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [0.9157004952430725, 0.44781431555747986], "taskxy": [0.8428284525871277, 0.11100126802921295], "dest": [0.8428284816741943, 0.10500000149011612]}
          48 +{"seed": 47, "success": true, "steps": 38, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [0.8696834444999695, 0.49866390228271484], "taskxy": [0.829658567905426, 0.10500001907348633], "dest": [0.8296585936546326, 0.10500000149011612]}
          49 +{"seed": 48, "success": true, "steps": 22, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [1.2655636072158813, 0.4491959512233734], "taskxy": [1.196325421333313, 0.10499995946884155], "dest": [1.1963254470825195, 0.10500000149011612]}
          50 +{"seed": 49, "success": true, "steps": 21, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [0.942194938659668, 0.5193631649017334], "taskxy": [0.8589697480201721, 0.10500001162290573], "dest": [0.8589697371721268, 0.10500000149011612]}
          51 +{"seed": 50, "success": true, "steps": 70, "seconds": 1.12, "phase": "place", "task": "target_block", "robot": [0.722407341003418, 0.4533366560935974], "taskxy": [0.6925303936004639, 0.10500000417232513], "dest": [0.6925305269956589, 0.10500000149011612]}
          52 +{"seed": 51, "success": true, "steps": 37, "seconds": 0.43, "phase": "place", "task": "target_block", "robot": [0.7855203747749329, 0.47989869117736816], "taskxy": [0.7000908255577087, 0.10499997437000275], "dest": [0.7000909109115601, 0.10500000149011612]}
          53 +{"seed": 52, "success": true, "steps": 81, "seconds": 1.21, "phase": "place", "task": "target_block", "robot": [0.5762956738471985, 0.44454696774482727], "taskxy": [0.49785348773002625, 0.10499999672174454], "dest": [0.4978534768819809, 0.10500000149011612]}
          54 +{"seed": 53, "success": true, "steps": 92, "seconds": 1.3, "phase": "place", "task": "target_block", "robot": [0.7180459499359131, 0.38794079422950745], "taskxy": [0.6186805963516235, 0.11498072743415833], "dest": [0.6186806153059006, 0.10500000149011612]}
          55 +{"seed": 54, "success": true, "steps": 30, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [1.49070143699646, 0.38928577303886414], "taskxy": [1.4156248569488525, 0.10500001162290573], "dest": [1.415624882698059, 0.10500000149011612]}
          56 +{"seed": 55, "success": true, "steps": 25, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [0.6290305852890015, 0.4394877851009369], "taskxy": [0.5789647698402405, 0.10499998927116394], "dest": [0.5789648108184338, 0.10500000149011612]}
          57 +{"seed": 56, "success": true, "steps": 64, "seconds": 0.65, "phase": "place", "task": "target_block", "robot": [1.4555909633636475, 0.3702752888202667], "taskxy": [1.4038506746292114, 0.10499998182058334], "dest": [1.403850700378418, 0.10500000149011612]}
          58 +{"seed": 57, "success": true, "steps": 18, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.6021356582641602, 0.4789508879184723], "taskxy": [0.5449443459510803, 0.10499997437000275], "dest": [0.5449443425536156, 0.10500000149011612]}
          59 +{"seed": 58, "success": true, "steps": 60, "seconds": 0.73, "phase": "place", "task": "target_block", "robot": [0.896597146987915, 0.3907721936702728], "taskxy": [0.8486972451210022, 0.10500001162290573], "dest": [0.848697211265564, 0.10500000149011612]}
          60 +{"seed": 59, "success": true, "steps": 63, "seconds": 0.9, "phase": "place", "task": "target_block", "robot": [1.2168527841567993, 0.44906941056251526], "taskxy": [1.1603264808654785, 0.10500000417232513], "dest": [1.160326506614685, 0.10500000149011612]}
          61 +{"seed": 60, "success": true, "steps": 25, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [0.6079646348953247, 0.38666898012161255], "taskxy": [0.5506205558776855, 0.10499999672174454], "dest": [0.5506205822825432, 0.10500000149011612]}
          62 +{"seed": 61, "success": true, "steps": 68, "seconds": 0.73, "phase": "place", "task": "target_block", "robot": [0.508681058883667, 0.5121599435806274], "taskxy": [0.40882420539855957, 0.10499997437000275], "dest": [0.4088242094516754, 0.10500000149011612]}
          63 +{"seed": 62, "success": true, "steps": 63, "seconds": 0.8, "phase": "place", "task": "target_block", "robot": [1.3378404378890991, 0.5010924935340881], "taskxy": [1.274317741394043, 0.10500004142522812], "dest": [1.2743177671432495, 0.10500000149011612]}
          64 +{"seed": 63, "success": true, "steps": 43, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [0.7719020247459412, 0.4131719172000885], "taskxy": [0.7193305492401123, 0.10499999672174454], "dest": [0.719330501139164, 0.10500000149011612]}
          65 +{"seed": 64, "success": true, "steps": 29, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.4470420479774475, 0.46380719542503357], "taskxy": [0.34813961386680603, 0.10499999672174454], "dest": [0.34813969242572784, 0.10500000149011612]}
          66 +{"seed": 65, "success": true, "steps": 19, "seconds": 0.19, "phase": "place", "task": "target_block", "robot": [0.3692214787006378, 0.37646761536598206], "taskxy": [0.32330766320228577, 0.10499999672174454], "dest": [0.3233076523542404, 0.10500000149011612]}
          67 +{"seed": 66, "success": true, "steps": 61, "seconds": 0.8, "phase": "place", "task": "target_block", "robot": [1.208558440208435, 0.4594087302684784], "taskxy": [1.123029351234436, 0.10499998182058334], "dest": [1.1230293552875519, 0.10500000149011612]}
          68 +{"seed": 67, "success": true, "steps": 51, "seconds": 0.53, "phase": "place", "task": "target_block", "robot": [0.29200199246406555, 0.4232950806617737], "taskxy": [0.24387986958026886, 0.10499999672174454], "dest": [0.2438798885345459, 0.10500000149011612]}
          69 +{"seed": 68, "success": true, "steps": 47, "seconds": 0.65, "phase": "place", "task": "target_block", "robot": [0.4629645347595215, 0.3822043240070343], "taskxy": [0.39746949076652527, 0.10500001162290573], "dest": [0.3974694867134094, 0.10500000149011612]}
          70 +{"seed": 69, "success": true, "steps": 36, "seconds": 0.36, "phase": "place", "task": "target_block", "robot": [0.2170093059539795, 0.43561235070228577], "taskxy": [0.15116170048713684, 0.10499999672174454], "dest": [0.15116179394721985, 0.10500000149011612]}
          71 +{"seed": 70, "success": true, "steps": 49, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [1.2810150384902954, 0.37043750286102295], "taskxy": [1.2404487133026123, 0.10500001162290573], "dest": [1.2404485832452774, 0.10500000149011612]}
          72 +{"seed": 71, "success": true, "steps": 42, "seconds": 0.57, "phase": "place", "task": "target_block", "robot": [1.0334404706954956, 0.40021178126335144], "taskxy": [0.969202995300293, 0.10500002652406693], "dest": [0.969202939748764, 0.10500000149011612]}
          73 +{"seed": 72, "success": true, "steps": 97, "seconds": 1.4, "phase": "place", "task": "target_block", "robot": [0.24024903774261475, 0.4113594591617584], "taskxy": [0.19537508487701416, 0.11146795749664307], "dest": [0.1953750963807106, 0.10500000149011612]}
          74 +{"seed": 73, "success": true, "steps": 59, "seconds": 0.9, "phase": "place", "task": "target_block", "robot": [1.1164097785949707, 0.4124401807785034], "taskxy": [1.0341856479644775, 0.12427147477865219], "dest": [1.034185673713684, 0.10500000149011612]}
          75 +{"seed": 74, "success": true, "steps": 24, "seconds": 0.2, "phase": "place", "task": "target_block", "robot": [1.5013700723648071, 0.48225638270378113], "taskxy": [1.476072072982788, 0.10500003397464752], "dest": [1.4760720987319946, 0.10500000149011612]}
          76 +{"seed": 75, "success": true, "steps": 73, "seconds": 0.85, "phase": "place", "task": "target_block", "robot": [1.4256352186203003, 0.5120925307273865], "taskxy": [1.331120491027832, 0.10499999672174454], "dest": [1.3311206359863281, 0.10500000149011612]}
          77 +{"seed": 76, "success": true, "steps": 30, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.5033426880836487, 0.5277675986289978], "taskxy": [0.43621283769607544, 0.11775586009025574], "dest": [0.4362128417491913, 0.10500000149011612]}
          78 +{"seed": 77, "success": true, "steps": 22, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.716909646987915, 0.3836202323436737], "taskxy": [0.6318120360374451, 0.10499999672174454], "dest": [0.6318120617866516, 0.10500000149011612]}
          79 +{"seed": 78, "success": true, "steps": 99, "seconds": 1.33, "phase": "place", "task": "target_block", "robot": [0.6102669835090637, 0.4086683690547943], "taskxy": [0.5429975390434265, 0.10499998927116394], "dest": [0.5429975051879883, 0.10500000149011612]}
          80 +{"seed": 79, "success": true, "steps": 34, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.309327095746994, 0.4262494444847107], "taskxy": [0.2484995722770691, 0.10500003397464752], "dest": [0.24849958312511444, 0.10500000149011612]}
          81 +{"seed": 80, "success": true, "steps": 68, "seconds": 0.98, "phase": "place", "task": "target_block", "robot": [0.38471460342407227, 0.4364992380142212], "taskxy": [0.30512362718582153, 0.10500005632638931], "dest": [0.30512363463640213, 0.10500000149011612]}
          82 +{"seed": 81, "success": true, "steps": 25, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.593959391117096, 0.3846059739589691], "taskxy": [0.534056544303894, 0.10499999672174454], "dest": [0.5340565558075905, 0.10500000149011612]}
          83 +{"seed": 82, "success": true, "steps": 37, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [1.2759501934051514, 0.45464026927948], "taskxy": [1.2153900861740112, 0.11872528493404388], "dest": [1.215390176296234, 0.10500000149011612]}
          84 +{"seed": 83, "success": true, "steps": 111, "seconds": 1.7, "phase": "place", "task": "target_block", "robot": [0.25152280926704407, 0.5031046271324158], "taskxy": [0.16700725257396698, 0.10500004887580872], "dest": [0.1670072864294052, 0.10500000149011612]}
          85 +{"seed": 84, "success": true, "steps": 64, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [0.6042964458465576, 0.4124278724193573], "taskxy": [0.5306367874145508, 0.10500001907348633], "dest": [0.530636821269989, 0.10500000149011612]}
          86 +{"seed": 85, "success": true, "steps": 59, "seconds": 0.87, "phase": "place", "task": "target_block", "robot": [0.9010717868804932, 0.3812885880470276], "taskxy": [0.8189694881439209, 0.10500001162290573], "dest": [0.8189695138931274, 0.10500000149011612]}
          87 +{"seed": 86, "success": true, "steps": 45, "seconds": 0.66, "phase": "place", "task": "target_block", "robot": [0.7719181180000305, 0.3897438645362854], "taskxy": [0.6749577522277832, 0.10500000417232513], "dest": [0.6749577779769897, 0.10500000149011612]}
          88 +{"seed": 87, "success": true, "steps": 53, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [1.203840970993042, 0.44531750679016113], "taskxy": [1.1384081840515137, 0.10500002652406693], "dest": [1.1384080905914307, 0.10500000149011612]}
          89 +{"seed": 88, "success": true, "steps": 63, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [0.4685811400413513, 0.41715937852859497], "taskxy": [0.43061888217926025, 0.10500002652406693], "dest": [0.43061895328760147, 0.10500000149011612]}
          90 +{"seed": 89, "success": true, "steps": 61, "seconds": 0.64, "phase": "place", "task": "target_block", "robot": [0.6049009561538696, 0.477839857339859], "taskxy": [0.5215333104133606, 0.1136801466345787], "dest": [0.5215333361625671, 0.10500000149011612]}
          91 +{"seed": 90, "success": true, "steps": 77, "seconds": 1.0, "phase": "place", "task": "target_block", "robot": [0.23972977697849274, 0.5201032757759094], "taskxy": [0.1838860809803009, 0.12488047778606415], "dest": [0.18388607013225555, 0.10500000149011612]}
          92 +{"seed": 91, "success": true, "steps": 43, "seconds": 0.52, "phase": "place", "task": "target_block", "robot": [0.924026608467102, 0.452716201543808], "taskxy": [0.8921021819114685, 0.10500000417232513], "dest": [0.8921022232174873, 0.10500000149011612]}
          93 +{"seed": 92, "success": true, "steps": 54, "seconds": 0.48, "phase": "place", "task": "target_block", "robot": [1.0326489210128784, 0.37041032314300537], "taskxy": [1.00502347946167, 0.10500000417232513], "dest": [1.0050235052108765, 0.10500000149011612]}
          94 +{"seed": 93, "success": true, "steps": 76, "seconds": 0.71, "phase": "place", "task": "target_block", "robot": [1.0940169095993042, 0.41185927391052246], "taskxy": [1.0277326107025146, 0.10499999672174454], "dest": [1.0277326364517212, 0.10500000149011612]}
          95 +{"seed": 94, "success": true, "steps": 23, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.6026239395141602, 0.5030219554901123], "taskxy": [0.5353034138679504, 0.10499999672174454], "dest": [0.5353033800125122, 0.10500000149011612]}
          96 +{"seed": 95, "success": true, "steps": 60, "seconds": 0.55, "phase": "place", "task": "target_block", "robot": [1.2636786699295044, 0.48673880100250244], "taskxy": [1.2265461683273315, 0.10500001907348633], "dest": [1.226546194076538, 0.10500000149011612]}
          97 +{"seed": 96, "success": true, "steps": 32, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [1.4306432008743286, 0.5141889452934265], "taskxy": [1.398691177368164, 0.10500001907348633], "dest": [1.398691207885742, 0.10500000149011612]}
          98 +{"seed": 97, "success": true, "steps": 36, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.6469581127166748, 0.3773379623889923], "taskxy": [0.6194592118263245, 0.10500001907348633], "dest": [0.6194591637253761, 0.10500000149011612]}
          99 +{"seed": 98, "success": true, "steps": 57, "seconds": 0.57, "phase": "place", "task": "target_block", "robot": [0.23062244057655334, 0.41795989871025085], "taskxy": [0.14807526767253876, 0.10500001907348633], "dest": [0.1480752568244934, 0.10500000149011612]}
         100 +{"seed": 99, "success": true, "steps": 46, "seconds": 0.4, "phase": "place", "task": "target_block", "robot": [1.2927566766738892, 0.4704902172088623], "taskxy": [1.2396767139434814, 0.10499997437000275], "dest": [1.239676739692688, 0.10500000149011612]}
         101 +{"seed": 100, "success": true, "steps": 97, "seconds": 1.19, "phase": "place", "task": "target_block", "robot": [1.1768378019332886, 0.39897847175598145], "taskxy": [1.1082637310028076, 0.10623612254858017], "dest": [1.1082637567520142, 0.10500000149011612]}
         102 +{"seed": 101, "success": true, "steps": 17, "seconds": 0.17, "phase": "place", "task": "target_block", "robot": [0.9191758632659912, 0.422054260969162], "taskxy": [0.8452779054641724, 0.10499999672174454], "dest": [0.8452778350114822, 0.10500000149011612]}
         103 +{"seed": 102, "success": true, "steps": 64, "seconds": 0.8, "phase": "place", "task": "target_block", "robot": [0.5098951458930969, 0.3945688009262085], "taskxy": [0.4805404841899872, 0.10499999672174454], "dest": [0.48054044353961944, 0.10500000149011612]}
         104 +{"seed": 103, "success": true, "steps": 35, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [1.1813424825668335, 0.48421770334243774], "taskxy": [1.1346606016159058, 0.11998195946216583], "dest": [1.1346606950759888, 0.10500000149011612]}
         105 +{"seed": 104, "success": true, "steps": 103, "seconds": 1.02, "phase": "place", "task": "target_block", "robot": [0.4151942729949951, 0.4712737798690796], "taskxy": [0.3404129445552826, 0.10500001907348633], "dest": [0.34041296350955963, 0.10500000149011612]}
         106 +{"seed": 105, "success": true, "steps": 20, "seconds": 0.13, "phase": "place", "task": "target_block", "robot": [1.0613794326782227, 0.45107242465019226], "taskxy": [0.970126748085022, 0.10500000417232513], "dest": [0.9701267142295837, 0.10500000149011612]}
         107 +{"seed": 106, "success": true, "steps": 26, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.6255789995193481, 0.39875614643096924], "taskxy": [0.5761585831642151, 0.10499998927116394], "dest": [0.5761585648655891, 0.10500000149011612]}
         108 +{"seed": 107, "success": true, "steps": 30, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.4179047644138336, 0.5184366106987], "taskxy": [0.3617344796657562, 0.10500004142522812], "dest": [0.3617343943119049, 0.10500000149011612]}
         109 +{"seed": 108, "success": true, "steps": 25, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.7884621024131775, 0.5040700435638428], "taskxy": [0.7277265787124634, 0.10500001907348633], "dest": [0.7277265448570251, 0.10500000149011612]}
         110 +{"seed": 109, "success": true, "steps": 51, "seconds": 0.54, "phase": "place", "task": "target_block", "robot": [0.907832682132721, 0.44558295607566833], "taskxy": [0.8714744448661804, 0.10500001907348633], "dest": [0.8714744110107422, 0.10500000149011612]}
         111 +{"seed": 110, "success": true, "steps": 68, "seconds": 0.58, "phase": "place", "task": "target_block", "robot": [0.2949291169643402, 0.4753938913345337], "taskxy": [0.264769047498703, 0.10499995946884155], "dest": [0.26476904782652855, 0.10500000149011612]}
         112 +{"seed": 111, "success": true, "steps": 38, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.5557335019111633, 0.5153118968009949], "taskxy": [0.4709137976169586, 0.10500001162290573], "dest": [0.4709138125181198, 0.10500000149011612]}
         113 +{"seed": 112, "success": true, "steps": 26, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.6327254176139832, 0.4092848300933838], "taskxy": [0.545693039894104, 0.10500001162290573], "dest": [0.5456930060386658, 0.10500000149011612]}
         114 +{"seed": 113, "success": true, "steps": 41, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [0.2628070116043091, 0.3955687880516052], "taskxy": [0.2005523145198822, 0.10499996691942215], "dest": [0.20055228877067566, 0.10500000149011612]}
         115 +{"seed": 114, "success": true, "steps": 21, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [1.4253013134002686, 0.4470110535621643], "taskxy": [1.3676819801330566, 0.10499999672174454], "dest": [1.3676820058822632, 0.10500000149011612]}
         116 +{"seed": 115, "success": true, "steps": 66, "seconds": 0.6, "phase": "place", "task": "target_block", "robot": [0.503485918045044, 0.43146076798439026], "taskxy": [0.43156304955482483, 0.10499999672174454], "dest": [0.43156305360794067, 0.10500000149011612]}
         117 +{"seed": 116, "success": true, "steps": 49, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [0.6146401762962341, 0.4520607888698578], "taskxy": [0.5671280026435852, 0.10500000417232513], "dest": [0.5671278949379921, 0.10500000149011612]}
         118 +{"seed": 117, "success": true, "steps": 27, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [0.46189069747924805, 0.4287354052066803], "taskxy": [0.38455232977867126, 0.10500000417232513], "dest": [0.3845523040294647, 0.10500000149011612]}
         119 +{"seed": 118, "success": true, "steps": 56, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [0.7981575131416321, 0.5092192888259888], "taskxy": [0.722709059715271, 0.10500001162290573], "dest": [0.7227090854644775, 0.10500000149011612]}
         120 +{"seed": 119, "success": true, "steps": 60, "seconds": 0.67, "phase": "place", "task": "target_block", "robot": [0.9632326364517212, 0.37250176072120667], "taskxy": [0.8959778547286987, 0.10500001162290573], "dest": [0.8959778804779053, 0.10500000149011612]}
         121 +{"seed": 120, "success": true, "steps": 20, "seconds": 0.18, "phase": "place", "task": "target_block", "robot": [0.35513538122177124, 0.5011457204818726], "taskxy": [0.3210921585559845, 0.10500004887580872], "dest": [0.32109214025735855, 0.10500000149011612]}
         122 +{"seed": 121, "success": true, "steps": 26, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [0.5002688765525818, 0.42802485823631287], "taskxy": [0.4419303834438324, 0.10499998182058334], "dest": [0.44193040984869003, 0.10500000149011612]}
         123 +{"seed": 122, "success": true, "steps": 77, "seconds": 0.84, "phase": "place", "task": "target_block", "robot": [1.0588955879211426, 0.3971870541572571], "taskxy": [1.004573106765747, 0.10500001162290573], "dest": [1.0045731149315833, 0.10500000149011612]}
         124 +{"seed": 123, "success": true, "steps": 40, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [1.358690619468689, 0.4114861488342285], "taskxy": [1.2644398212432861, 0.10499999672174454], "dest": [1.2644398469924927, 0.10500000149011612]}
         125 +{"seed": 124, "success": true, "steps": 67, "seconds": 0.79, "phase": "place", "task": "target_block", "robot": [0.7890814542770386, 0.45829707384109497], "taskxy": [0.7506852746009827, 0.10500000417232513], "dest": [0.7506853233575821, 0.10500000149011612]}
         126 +{"seed": 125, "success": true, "steps": 75, "seconds": 0.89, "phase": "place", "task": "target_block", "robot": [1.280517578125, 0.37442073225975037], "taskxy": [1.2240878343582153, 0.10500002652406693], "dest": [1.2240878601074219, 0.10500000149011612]}
         127 +{"seed": 126, "success": true, "steps": 17, "seconds": 0.16, "phase": "place", "task": "target_block", "robot": [0.6344804763793945, 0.4762766361236572], "taskxy": [0.5738679766654968, 0.10500002652406693], "dest": [0.5738680024147034, 0.10500000149011612]}
         128 +{"seed": 127, "success": true, "steps": 75, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [0.6004003286361694, 0.4921362102031708], "taskxy": [0.5034160017967224, 0.10500000417232513], "dest": [0.5034160505533218, 0.10500000149011612]}
         129 +{"seed": 128, "success": true, "steps": 103, "seconds": 1.42, "phase": "place", "task": "target_block", "robot": [0.23824124038219452, 0.49311575293540955], "taskxy": [0.14383253455162048, 0.11340951919555664], "dest": [0.14383253860473633, 0.10500000149011612]}
         130 +{"seed": 129, "success": true, "steps": 38, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.2833929657936096, 0.48651084303855896], "taskxy": [0.19691210985183716, 0.10499998182058334], "dest": [0.1969121288061142, 0.10500000149011612]}
         131 +{"seed": 130, "success": true, "steps": 58, "seconds": 0.8, "phase": "place", "task": "target_block", "robot": [1.1416895389556885, 0.4460110664367676], "taskxy": [1.1159781217575073, 0.10499998182058334], "dest": [1.1159781475067139, 0.10500000149011612]}
         132 +{"seed": 131, "success": true, "steps": 36, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [1.1264592409133911, 0.4566332995891571], "taskxy": [1.034521222114563, 0.10499998927116394], "dest": [1.034521327137947, 0.10500000149011612]}
         133 +{"seed": 132, "success": true, "steps": 97, "seconds": 1.33, "phase": "place", "task": "target_block", "robot": [1.424458384513855, 0.4283716082572937], "taskxy": [1.348850965499878, 0.1139054000377655], "dest": [1.348850872039795, 0.10500000149011612]}
         134 +{"seed": 133, "success": true, "steps": 65, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [0.42281824350357056, 0.4812164902687073], "taskxy": [0.3534822165966034, 0.10500004887580872], "dest": [0.3534823100566864, 0.10500000149011612]}
         135 +{"seed": 134, "success": true, "steps": 26, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [0.9702277779579163, 0.3841283917427063], "taskxy": [0.9396535158157349, 0.11078184098005295], "dest": [0.9396535415649414, 0.10500000149011612]}
         136 +{"seed": 135, "success": true, "steps": 18, "seconds": 0.19, "phase": "place", "task": "target_block", "robot": [0.8588243722915649, 0.46903297305107117], "taskxy": [0.7696532011032104, 0.10499998182058334], "dest": [0.769653226852417, 0.10500000149011612]}
         137 +{"seed": 136, "success": true, "steps": 52, "seconds": 0.86, "phase": "place", "task": "target_block", "robot": [0.4669085741043091, 0.40208184719085693], "taskxy": [0.3709888458251953, 0.10499998927116394], "dest": [0.37098889458179474, 0.10500000149011612]}
         138 +{"seed": 137, "success": true, "steps": 75, "seconds": 0.75, "phase": "place", "task": "target_block", "robot": [0.3055169880390167, 0.42432138323783875], "taskxy": [0.2378719002008438, 0.10750839114189148], "dest": [0.23787191915512085, 0.10500000149011612]}
         139 +{"seed": 138, "success": true, "steps": 85, "seconds": 0.76, "phase": "place", "task": "target_block", "robot": [0.3143114745616913, 0.3953363299369812], "taskxy": [0.24058590829372406, 0.10499999672174454], "dest": [0.2405859123468399, 0.10500000149011612]}
         140 +{"seed": 139, "success": true, "steps": 86, "seconds": 0.85, "phase": "place", "task": "target_block", "robot": [1.4185402393341064, 0.4045073986053467], "taskxy": [1.3357714414596558, 0.10499998182058334], "dest": [1.3357714672088623, 0.10500000149011612]}
         141 +{"seed": 140, "success": true, "steps": 23, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [0.4379059672355652, 0.40286746621131897], "taskxy": [0.3777534067630768, 0.10499995946884155], "dest": [0.3777534108161926, 0.10500000149011612]}
         142 +{"seed": 141, "success": true, "steps": 55, "seconds": 0.59, "phase": "place", "task": "target_block", "robot": [0.9136666655540466, 0.41413864493370056], "taskxy": [0.8598531484603882, 0.10499999672174454], "dest": [0.85985311460495, 0.10500000149011612]}
         143 +{"seed": 142, "success": true, "steps": 53, "seconds": 0.4, "phase": "place", "task": "target_block", "robot": [0.6798704862594604, 0.4080703854560852], "taskxy": [0.6377748250961304, 0.10499997437000275], "dest": [0.6377746652364731, 0.10500000149011612]}
         144 +{"seed": 143, "success": true, "steps": 61, "seconds": 0.66, "phase": "place", "task": "target_block", "robot": [0.8179507851600647, 0.3874554932117462], "taskxy": [0.7639366388320923, 0.10499996691942215], "dest": [0.7639366828203201, 0.10500000149011612]}
         145 +{"seed": 144, "success": true, "steps": 38, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.9016542434692383, 0.4936511814594269], "taskxy": [0.806043267250061, 0.10500001907348633], "dest": [0.8060432929992676, 0.10500000149011612]}
         146 +{"seed": 145, "success": true, "steps": 46, "seconds": 0.57, "phase": "place", "task": "target_block", "robot": [0.5213470458984375, 0.48559242486953735], "taskxy": [0.475981205701828, 0.10500002652406693], "dest": [0.47598123145103455, 0.10500000149011612]}
         147 +{"seed": 146, "success": true, "steps": 55, "seconds": 0.64, "phase": "place", "task": "target_block", "robot": [0.9525736570358276, 0.44899240136146545], "taskxy": [0.901035487651825, 0.10499999672174454], "dest": [0.9010354537963867, 0.10500000149011612]}
         148 +{"seed": 147, "success": true, "steps": 24, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [0.7222214341163635, 0.4742678105831146], "taskxy": [0.6897182464599609, 0.10500004142522812], "dest": [0.6897182728648186, 0.10500000149011612]}
         149 +{"seed": 148, "success": true, "steps": 18, "seconds": 0.11, "phase": "place", "task": "target_block", "robot": [1.1064766645431519, 0.4029283821582794], "taskxy": [1.0169841051101685, 0.10500000417232513], "dest": [1.016984243273735, 0.10500000149011612]}
         150 +{"seed": 149, "success": true, "steps": 29, "seconds": 0.22, "phase": "place", "task": "target_block", "robot": [1.1682244539260864, 0.5188928842544556], "taskxy": [1.1064947843551636, 0.10499998927116394], "dest": [1.1064947064518929, 0.10500000149011612]}
         151 +{"seed": 150, "success": true, "steps": 35, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [0.6279230713844299, 0.4909636676311493], "taskxy": [0.5899596214294434, 0.10570214688777924], "dest": [0.5899595875740051, 0.10500000149011612]}
         152 +{"seed": 151, "success": true, "steps": 28, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.8112809062004089, 0.5056660175323486], "taskxy": [0.7540895938873291, 0.10499999672174454], "dest": [0.7540896281301975, 0.10500000149011612]}
         153 +{"seed": 152, "success": true, "steps": 47, "seconds": 0.57, "phase": "place", "task": "target_block", "robot": [0.8721857666969299, 0.46635934710502625], "taskxy": [0.8440008163452148, 0.10500002652406693], "dest": [0.8440008464753628, 0.10500000149011612]}
         154 +{"seed": 153, "success": true, "steps": 77, "seconds": 1.04, "phase": "place", "task": "target_block", "robot": [0.837716281414032, 0.4352205991744995], "taskxy": [0.7561463117599487, 0.11058241128921509], "dest": [0.7561462779045105, 0.10500000149011612]}
         155 +{"seed": 154, "success": true, "steps": 38, "seconds": 0.36, "phase": "place", "task": "target_block", "robot": [1.4377179145812988, 0.5013315677642822], "taskxy": [1.373274803161621, 0.10499999672174454], "dest": [1.373274709701538, 0.10500000149011612]}
diff --git a/probe_reachability.py b/probe_reachability.py
new file mode 100644
index 0000000..daedf40
--- /dev/null
+++ b/probe_reachability.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +import json
           3 +cases=[]
           4 +for seed in range(1000,2500):
           5 + e=make_env();s,i=e.reset(seed=seed);b=next(iter(s.get_objects(e.observation_space.get_type('target_block'))));g=next(iter(s.get_objects(e.observation_space.get_type('target_surface'))))
           6 + x,w=s.get(b,'x'),s.get(b,'width');gx,gw=s.get(g,'x'),s.get(g,'width')
           7 + possible=False
           8 + for dest in (gx+.002,gx+gw-w-.002):
           9 +  low=max(.1002-x,.1002-dest,-.022);high=min(1.5178-x,1.5178-dest,w+.022)
          10 +  possible |= low<=high
          11 + if not possible:
          12 +  row={'seed':seed,'block':[x,w],'surface':[gx,gw]};cases.append(row);print(json.dumps(row),flush=True)
          13 + e.close()
          14 +print('FOUND',len(cases),flush=True)
diff --git a/test_counts_scene_v3.jsonl b/test_counts_scene_v3.jsonl
index 5d99a38..19506c0 100644
--- a/test_counts_scene_v3.jsonl
+++ b/test_counts_scene_v3.jsonl
@@ -12,3 +12,26 @@
   12     12  {"count": 4, "seed": 11, "steps": 64, "success": true, "seconds": 1.62}
   13     13  {"count": 4, "seed": 12, "steps": 105, "success": true, "seconds": 2.76}
   14     14  {"count": 4, "seed": 13, "steps": 98, "success": true, "seconds": 2.59}
          15 +{"count": 4, "seed": 14, "steps": 55, "success": true, "seconds": 6.1}
          16 +{"count": 4, "seed": 15, "steps": 89, "success": true, "seconds": 5.12}
          17 +{"count": 4, "seed": 16, "steps": 80, "success": true, "seconds": 3.27}
          18 +{"count": 4, "seed": 17, "steps": 86, "success": true, "seconds": 6.66}
          19 +{"count": 4, "seed": 18, "steps": 36, "success": true, "seconds": 2.63}
          20 +{"count": 4, "seed": 19, "steps": 70, "success": true, "seconds": 5.06}
          21 +{"count": 4, "seed": 20, "steps": 60, "success": true, "seconds": 2.33}
          22 +{"count": 4, "seed": 21, "steps": 56, "success": true, "seconds": 3.42}
          23 +{"count": 4, "seed": 22, "steps": 55, "success": true, "seconds": 5.84}
          24 +{"count": 4, "seed": 23, "steps": 59, "success": true, "seconds": 2.31}
          25 +{"count": 4, "seed": 24, "steps": 117, "success": true, "seconds": 4.0}
          26 +{"count": 4, "seed": 25, "steps": 100, "success": true, "seconds": 3.06}
          27 +{"count": 4, "seed": 26, "steps": 88, "success": true, "seconds": 4.53}
          28 +{"count": 4, "seed": 27, "steps": 93, "success": true, "seconds": 4.14}
          29 +{"count": 4, "seed": 28, "steps": 112, "success": true, "seconds": 3.86}
          30 +{"count": 4, "seed": 29, "steps": 63, "success": true, "seconds": 2.69}
          31 +{"count": 4, "seed": 30, "steps": 113, "success": true, "seconds": 3.69}
          32 +{"count": 4, "seed": 31, "steps": 48, "success": true, "seconds": 2.32}
          33 +{"count": 4, "seed": 32, "steps": 40, "success": true, "seconds": 2.14}
          34 +{"count": 4, "seed": 33, "steps": 68, "success": true, "seconds": 3.73}
          35 +{"count": 4, "seed": 34, "steps": 101, "success": true, "seconds": 3.93}
          36 +{"count": 4, "seed": 35, "steps": 50, "success": true, "seconds": 3.79}
          37 +{"count": 4, "seed": 36, "steps": 164, "success": true, "seconds": 3.88}
diff --git a/test_counts_scene_v3.log b/test_counts_scene_v3.log
index 5d99a38..19506c0 100644
--- a/test_counts_scene_v3.log
+++ b/test_counts_scene_v3.log
@@ -12,3 +12,26 @@
   12     12  {"count": 4, "seed": 11, "steps": 64, "success": true, "seconds": 1.62}
   13     13  {"count": 4, "seed": 12, "steps": 105, "success": true, "seconds": 2.76}
   14     14  {"count": 4, "seed": 13, "steps": 98, "success": true, "seconds": 2.59}
          15 +{"count": 4, "seed": 14, "steps": 55, "success": true, "seconds": 6.1}
          16 +{"count": 4, "seed": 15, "steps": 89, "success": true, "seconds": 5.12}
          17 +{"count": 4, "seed": 16, "steps": 80, "success": true, "seconds": 3.27}
          18 +{"count": 4, "seed": 17, "steps": 86, "success": true, "seconds": 6.66}
          19 +{"count": 4, "seed": 18, "steps": 36, "success": true, "seconds": 2.63}
          20 +{"count": 4, "seed": 19, "steps": 70, "success": true, "seconds": 5.06}
          21 +{"count": 4, "seed": 20, "steps": 60, "success": true, "seconds": 2.33}
          22 +{"count": 4, "seed": 21, "steps": 56, "success": true, "seconds": 3.42}
          23 +{"count": 4, "seed": 22, "steps": 55, "success": true, "seconds": 5.84}
          24 +{"count": 4, "seed": 23, "steps": 59, "success": true, "seconds": 2.31}
          25 +{"count": 4, "seed": 24, "steps": 117, "success": true, "seconds": 4.0}
          26 +{"count": 4, "seed": 25, "steps": 100, "success": true, "seconds": 3.06}
          27 +{"count": 4, "seed": 26, "steps": 88, "success": true, "seconds": 4.53}
          28 +{"count": 4, "seed": 27, "steps": 93, "success": true, "seconds": 4.14}
          29 +{"count": 4, "seed": 28, "steps": 112, "success": true, "seconds": 3.86}
          30 +{"count": 4, "seed": 29, "steps": 63, "success": true, "seconds": 2.69}
          31 +{"count": 4, "seed": 30, "steps": 113, "success": true, "seconds": 3.69}
          32 +{"count": 4, "seed": 31, "steps": 48, "success": true, "seconds": 2.32}
          33 +{"count": 4, "seed": 32, "steps": 40, "success": true, "seconds": 2.14}
          34 +{"count": 4, "seed": 33, "steps": 68, "success": true, "seconds": 3.73}
          35 +{"count": 4, "seed": 34, "steps": 101, "success": true, "seconds": 3.93}
          36 +{"count": 4, "seed": 35, "steps": 50, "success": true, "seconds": 3.79}
          37 +{"count": 4, "seed": 36, "steps": 164, "success": true, "seconds": 3.88}
diff --git a/validate_count3.jsonl b/validate_count3.jsonl
new file mode 100644
index 0000000..e8f7b10
--- /dev/null
+++ b/validate_count3.jsonl
@@ -0,0 +1,50 @@
           1 +{"seed": 100, "count": 3, "success": true, "steps": 84, "policy_seconds": 0.0118, "elapsed": 1.459}
           2 +{"seed": 101, "count": 3, "success": true, "steps": 80, "policy_seconds": 0.0169, "elapsed": 1.439}
           3 +{"seed": 102, "count": 3, "success": true, "steps": 51, "policy_seconds": 0.0186, "elapsed": 0.776}
           4 +{"seed": 103, "count": 3, "success": true, "steps": 68, "policy_seconds": 0.0114, "elapsed": 1.058}
           5 +{"seed": 104, "count": 3, "success": true, "steps": 106, "policy_seconds": 0.0224, "elapsed": 1.554}
           6 +{"seed": 105, "count": 3, "success": true, "steps": 72, "policy_seconds": 0.0147, "elapsed": 1.058}
           7 +{"seed": 106, "count": 3, "success": true, "steps": 64, "policy_seconds": 0.013, "elapsed": 0.977}
           8 +{"seed": 107, "count": 3, "success": true, "steps": 69, "policy_seconds": 0.0186, "elapsed": 1.054}
           9 +{"seed": 108, "count": 3, "success": true, "steps": 88, "policy_seconds": 0.0272, "elapsed": 1.416}
          10 +{"seed": 109, "count": 3, "success": true, "steps": 77, "policy_seconds": 0.0134, "elapsed": 1.226}
          11 +{"seed": 110, "count": 3, "success": true, "steps": 55, "policy_seconds": 0.0156, "elapsed": 0.9}
          12 +{"seed": 111, "count": 3, "success": true, "steps": 127, "policy_seconds": 0.0343, "elapsed": 2.276}
          13 +{"seed": 112, "count": 3, "success": true, "steps": 65, "policy_seconds": 0.0141, "elapsed": 0.957}
          14 +{"seed": 113, "count": 3, "success": true, "steps": 104, "policy_seconds": 0.0292, "elapsed": 1.515}
          15 +{"seed": 114, "count": 3, "success": true, "steps": 134, "policy_seconds": 0.0235, "elapsed": 1.878}
          16 +{"seed": 115, "count": 3, "success": true, "steps": 120, "policy_seconds": 0.0302, "elapsed": 1.775}
          17 +{"seed": 116, "count": 3, "success": true, "steps": 49, "policy_seconds": 0.0151, "elapsed": 0.729}
          18 +{"seed": 117, "count": 3, "success": true, "steps": 83, "policy_seconds": 0.0246, "elapsed": 1.366}
          19 +{"seed": 118, "count": 3, "success": true, "steps": 83, "policy_seconds": 0.0128, "elapsed": 1.366}
          20 +{"seed": 119, "count": 3, "success": true, "steps": 106, "policy_seconds": 0.0265, "elapsed": 1.579}
          21 +{"seed": 120, "count": 3, "success": true, "steps": 87, "policy_seconds": 0.0129, "elapsed": 1.228}
          22 +{"seed": 121, "count": 3, "success": true, "steps": 90, "policy_seconds": 0.0252, "elapsed": 1.324}
          23 +{"seed": 122, "count": 3, "success": true, "steps": 88, "policy_seconds": 0.0221, "elapsed": 1.33}
          24 +{"seed": 123, "count": 3, "success": true, "steps": 87, "policy_seconds": 0.017, "elapsed": 0.991}
          25 +{"seed": 124, "count": 3, "success": true, "steps": 82, "policy_seconds": 0.0153, "elapsed": 1.105}
          26 +{"seed": 125, "count": 3, "success": true, "steps": 102, "policy_seconds": 0.0174, "elapsed": 1.314}
          27 +{"seed": 126, "count": 3, "success": true, "steps": 51, "policy_seconds": 0.0116, "elapsed": 0.788}
          28 +{"seed": 127, "count": 3, "success": true, "steps": 112, "policy_seconds": 0.0165, "elapsed": 1.735}
          29 +{"seed": 128, "count": 3, "success": true, "steps": 138, "policy_seconds": 0.0335, "elapsed": 1.917}
          30 +{"seed": 129, "count": 3, "success": true, "steps": 123, "policy_seconds": 0.0106, "elapsed": 1.373}
          31 +{"seed": 130, "count": 3, "success": true, "steps": 95, "policy_seconds": 0.0153, "elapsed": 1.495}
          32 +{"seed": 131, "count": 3, "success": true, "steps": 72, "policy_seconds": 0.0238, "elapsed": 0.953}
          33 +{"seed": 132, "count": 3, "success": true, "steps": 131, "policy_seconds": 0.0203, "elapsed": 1.995}
          34 +{"seed": 133, "count": 3, "success": true, "steps": 112, "policy_seconds": 0.0179, "elapsed": 1.734}
          35 +{"seed": 134, "count": 3, "success": true, "steps": 112, "policy_seconds": 0.0146, "elapsed": 1.363}
          36 +{"seed": 135, "count": 3, "success": true, "steps": 62, "policy_seconds": 0.0128, "elapsed": 0.87}
          37 +{"seed": 136, "count": 3, "success": true, "steps": 76, "policy_seconds": 0.0214, "elapsed": 1.141}
          38 +{"seed": 137, "count": 3, "success": true, "steps": 89, "policy_seconds": 0.0125, "elapsed": 1.165}
          39 +{"seed": 138, "count": 3, "success": true, "steps": 105, "policy_seconds": 0.0221, "elapsed": 1.393}
          40 +{"seed": 139, "count": 3, "success": true, "steps": 59, "policy_seconds": 0.0116, "elapsed": 0.853}
          41 +{"seed": 140, "count": 3, "success": true, "steps": 60, "policy_seconds": 0.0092, "elapsed": 0.729}
          42 +{"seed": 141, "count": 3, "success": true, "steps": 54, "policy_seconds": 0.0138, "elapsed": 0.957}
          43 +{"seed": 142, "count": 3, "success": true, "steps": 89, "policy_seconds": 0.0246, "elapsed": 1.292}
          44 +{"seed": 143, "count": 3, "success": true, "steps": 86, "policy_seconds": 0.0275, "elapsed": 0.914}
          45 +{"seed": 144, "count": 3, "success": true, "steps": 53, "policy_seconds": 0.0147, "elapsed": 0.896}
          46 +{"seed": 145, "count": 3, "success": true, "steps": 98, "policy_seconds": 0.0174, "elapsed": 1.614}
          47 +{"seed": 146, "count": 3, "success": true, "steps": 60, "policy_seconds": 0.0105, "elapsed": 0.695}
          48 +{"seed": 147, "count": 3, "success": true, "steps": 61, "policy_seconds": 0.0131, "elapsed": 0.828}
          49 +{"seed": 148, "count": 3, "success": true, "steps": 102, "policy_seconds": 0.0154, "elapsed": 1.313}
          50 +{"seed": 149, "count": 3, "success": true, "steps": 56, "policy_seconds": 0.0111, "elapsed": 0.786}
```

</details>

<a id="C012"></a>
### C012 · Clear neighboring grasp dependencies even when the obstructing block is shorter

Commit `e8ce3b889ab7f28c968f9f5f00117b5b19934db1`; parents: 4ef204b1169e79429247b7774e33bece8740190e. Recorded author date: 2026-09-21T17:33:17Z.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0081](01_timeline.md#E0081): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_e8ce3b8_approach.py) · [Exact all-file diff](evidence/diffs/C012_e8ce3b8.diff)

[Previous saved controller snapshot](evidence/versions/C009_4942e85_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index bedf44b..f735e39 100644
--- a/approach.py
+++ b/approach.py
@@ -70,8 +70,11 @@ class GeneratedApproach:
   70     70              o=self.block;self.dest=self.goal
   71     71          else:
   72     72              o=max(bad,key=lambda p:self.rect(s,p)[1]+self.rect(s,p)[3])
   73        -            # A taller neighbour may block the selected object's top grasp.
   74        -            for _ in range(len(obs)+1):
          73 +            # Clear dependencies of an exclusive vacuum grasp, including shorter
          74 +            # neighbours. Track visited tasks to avoid dependency cycles.
          75 +            visited=set()
          76 +            for _ in range(len(obs)+2):
          77 +                visited.add(o)
   75     78                  x,y,w,h=self.rect(s,o)
   76     79                  others=[p for p in obs+[self.block] if p!=o]
   77     80                  grasps=[]
@@ -80,9 +83,14 @@ class GeneratedApproach:
   80     83                      grasps.append((len(blocking),abs(off-w/2),off,blocking))
   81     84                  best=min(grasps,key=lambda z:z[:2])
   82     85                  if not best[0]:break
   83        -                taller=[p for p in best[3] if self.rect(s,p)[1]+self.rect(s,p)[3]>y+h+.001 and p!=self.block]
   84        -                if not taller:break
   85        -                o=max(taller,key=lambda p:self.rect(s,p)[1]+self.rect(s,p)[3])
          86 +                dependencies=set(p for grasp in grasps for p in grasp[3] if p not in visited)
          87 +                if not dependencies:break
          88 +                def access_cost(p):
          89 +                    qx,qy,qw,qh=self.rect(s,p)
          90 +                    rest=[q for q in obs+[self.block] if q!=p]
          91 +                    scores=[len(self.conflicts(s,p,qx,qy,z,rest,True)) for z in self.offsets(qx,qx,qw)]
          92 +                    return (min(scores) if scores else 999,p==self.block,-qy-qh)
          93 +                o=min(dependencies,key=access_cost)
   86     94              x,y,w,h=self.rect(s,o)
   87     95              others=[p for p in obs+[self.block] if p!=o]
   88     96              occupied=[self.rect(s,p) for p in others]
diff --git a/probe_final_0_499.jsonl b/probe_final_0_499.jsonl
index 54945fd..a1f7574 100644
--- a/probe_final_0_499.jsonl
+++ b/probe_final_0_499.jsonl
@@ -153,3 +153,119 @@
  153    153  {"seed": 152, "success": true, "steps": 47, "seconds": 0.57, "phase": "place", "task": "target_block", "robot": [0.8721857666969299, 0.46635934710502625], "taskxy": [0.8440008163452148, 0.10500002652406693], "dest": [0.8440008464753628, 0.10500000149011612]}
  154    154  {"seed": 153, "success": true, "steps": 77, "seconds": 1.04, "phase": "place", "task": "target_block", "robot": [0.837716281414032, 0.4352205991744995], "taskxy": [0.7561463117599487, 0.11058241128921509], "dest": [0.7561462779045105, 0.10500000149011612]}
  155    155  {"seed": 154, "success": true, "steps": 38, "seconds": 0.36, "phase": "place", "task": "target_block", "robot": [1.4377179145812988, 0.5013315677642822], "taskxy": [1.373274803161621, 0.10499999672174454], "dest": [1.373274709701538, 0.10500000149011612]}
         156 +{"seed": 155, "success": true, "steps": 27, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.6788395643234253, 0.4997852146625519], "taskxy": [0.638012170791626, 0.10500000417232513], "dest": [0.638012226998806, 0.10500000149011612]}
         157 +{"seed": 156, "success": true, "steps": 75, "seconds": 1.76, "phase": "place", "task": "target_block", "robot": [0.5066274404525757, 0.48027175664901733], "taskxy": [0.4116956293582916, 0.10499999672174454], "dest": [0.41169568490982056, 0.10500000149011612]}
         158 +{"seed": 157, "success": true, "steps": 35, "seconds": 0.59, "phase": "place", "task": "target_block", "robot": [1.3497886657714844, 0.47784608602523804], "taskxy": [1.322613000869751, 0.10500001907348633], "dest": [1.3226130266189575, 0.10500000149011612]}
         159 +{"seed": 158, "success": true, "steps": 79, "seconds": 1.42, "phase": "place", "task": "target_block", "robot": [0.37651991844177246, 0.5184414982795715], "taskxy": [0.3254949450492859, 0.10499996691942215], "dest": [0.3254949938058853, 0.10500000149011612]}
         160 +{"seed": 159, "success": true, "steps": 57, "seconds": 1.24, "phase": "place", "task": "target_block", "robot": [0.9187734723091125, 0.48148277401924133], "taskxy": [0.8804414868354797, 0.11580751091241837], "dest": [0.8804415248036385, 0.10500000149011612]}
         161 +{"seed": 160, "success": true, "steps": 22, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [0.8499256372451782, 0.3714103698730469], "taskxy": [0.7984733581542969, 0.10500001162290573], "dest": [0.7984733324050903, 0.10500000149011612]}
         162 +{"seed": 161, "success": true, "steps": 55, "seconds": 1.19, "phase": "place", "task": "target_block", "robot": [1.1081222295761108, 0.39952361583709717], "taskxy": [1.068873405456543, 0.10500001907348633], "dest": [1.0688733573555946, 0.10500000149011612]}
         163 +{"seed": 162, "success": true, "steps": 57, "seconds": 1.2, "phase": "place", "task": "target_block", "robot": [1.0537642240524292, 0.40186822414398193], "taskxy": [1.0106520652770996, 0.10499997437000275], "dest": [1.0106520469784737, 0.10500000149011612]}
         164 +{"seed": 163, "success": true, "steps": 54, "seconds": 0.88, "phase": "place", "task": "target_block", "robot": [0.9177966713905334, 0.3824598789215088], "taskxy": [0.8651367425918579, 0.10500003397464752], "dest": [0.8651366572380066, 0.10500000149011612]}
         165 +{"seed": 164, "success": true, "steps": 57, "seconds": 1.08, "phase": "place", "task": "target_block", "robot": [1.2256959676742554, 0.5093793272972107], "taskxy": [1.1723312139511108, 0.10500004887580872], "dest": [1.1723312403559685, 0.10500000149011612]}
         166 +{"seed": 165, "success": true, "steps": 67, "seconds": 1.1, "phase": "place", "task": "target_block", "robot": [0.2682192027568817, 0.4459765553474426], "taskxy": [0.1840570867061615, 0.10500002652406693], "dest": [0.18405709075927734, 0.10500000149011612]}
         167 +{"seed": 166, "success": true, "steps": 49, "seconds": 1.01, "phase": "place", "task": "target_block", "robot": [0.6377275586128235, 0.39235711097717285], "taskxy": [0.5801003575325012, 0.10500000417232513], "dest": [0.580100323677063, 0.10500000149011612]}
         168 +{"seed": 167, "success": true, "steps": 73, "seconds": 1.66, "phase": "place", "task": "target_block", "robot": [0.34188753366470337, 0.4285704493522644], "taskxy": [0.2607855796813965, 0.10499997437000275], "dest": [0.2607856433391571, 0.10500000149011612]}
         169 +{"seed": 168, "success": true, "steps": 44, "seconds": 0.68, "phase": "place", "task": "target_block", "robot": [0.319296270608902, 0.44384098052978516], "taskxy": [0.2873324155807495, 0.10499998182058334], "dest": [0.28733244198560715, 0.10500000149011612]}
         170 +{"seed": 169, "success": true, "steps": 76, "seconds": 1.48, "phase": "place", "task": "target_block", "robot": [1.1820814609527588, 0.39930057525634766], "taskxy": [1.124733328819275, 0.10808269679546356], "dest": [1.1247333250939846, 0.10500000149011612]}
         171 +{"seed": 170, "success": true, "steps": 57, "seconds": 1.24, "phase": "place", "task": "target_block", "robot": [1.1065210103988647, 0.3782927691936493], "taskxy": [1.0794156789779663, 0.10500001907348633], "dest": [1.0794156532287598, 0.10500000149011612]}
         172 +{"seed": 171, "success": true, "steps": 70, "seconds": 1.67, "phase": "place", "task": "target_block", "robot": [0.8228991627693176, 0.41371044516563416], "taskxy": [0.7452370524406433, 0.10500001162290573], "dest": [0.7452371127605438, 0.10500000149011612]}
         173 +{"seed": 172, "success": true, "steps": 53, "seconds": 1.11, "phase": "place", "task": "target_block", "robot": [0.41540467739105225, 0.45427289605140686], "taskxy": [0.3587935268878937, 0.10500001907348633], "dest": [0.35879347878694534, 0.10500000149011612]}
         174 +{"seed": 173, "success": true, "steps": 82, "seconds": 1.68, "phase": "place", "task": "target_block", "robot": [1.0739846229553223, 0.427572637796402], "taskxy": [1.0047025680541992, 0.11802444607019424], "dest": [1.0047026730775832, 0.10500000149011612]}
         175 +{"seed": 174, "success": true, "steps": 60, "seconds": 1.18, "phase": "place", "task": "target_block", "robot": [1.3998658657073975, 0.5096529126167297], "taskxy": [1.3021860122680664, 0.11027856171131134], "dest": [1.302186038017273, 0.10500000149011612]}
         176 +{"seed": 175, "success": true, "steps": 54, "seconds": 0.98, "phase": "place", "task": "target_block", "robot": [0.5429722666740417, 0.40398716926574707], "taskxy": [0.4575830399990082, 0.10499999672174454], "dest": [0.45758303594589234, 0.10500000149011612]}
         177 +{"seed": 176, "success": true, "steps": 34, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [0.5253431797027588, 0.3972555100917816], "taskxy": [0.43885281682014465, 0.10499997437000275], "dest": [0.43885291028022766, 0.10500000149011612]}
         178 +{"seed": 177, "success": true, "steps": 66, "seconds": 1.31, "phase": "place", "task": "target_block", "robot": [0.4299778640270233, 0.5061010718345642], "taskxy": [0.3458276093006134, 0.10500006377696991], "dest": [0.34582762825489044, 0.10500000149011612]}
         179 +{"seed": 178, "success": true, "steps": 83, "seconds": 1.57, "phase": "place", "task": "target_block", "robot": [0.4065881669521332, 0.48104023933410645], "taskxy": [0.3213166296482086, 0.10500004887580872], "dest": [0.32131667840480804, 0.10500000149011612]}
         180 +{"seed": 179, "success": true, "steps": 80, "seconds": 1.64, "phase": "place", "task": "target_block", "robot": [0.7077009677886963, 0.5017470717430115], "taskxy": [0.6586494445800781, 0.10500005632638931], "dest": [0.6586494703292847, 0.10500000149011612]}
         181 +{"seed": 180, "success": true, "steps": 37, "seconds": 0.62, "phase": "place", "task": "target_block", "robot": [1.3683747053146362, 0.5143249034881592], "taskxy": [1.3210786581039429, 0.10500001907348633], "dest": [1.3210786838531494, 0.10500000149011612]}
         182 +{"seed": 181, "success": true, "steps": 64, "seconds": 1.25, "phase": "place", "task": "target_block", "robot": [0.7283605337142944, 0.4436970055103302], "taskxy": [0.6458709239959717, 0.10996868461370468], "dest": [0.6458708636760712, 0.10500000149011612]}
         183 +{"seed": 182, "success": true, "steps": 123, "seconds": 2.59, "phase": "place", "task": "target_block", "robot": [1.2127327919006348, 0.4545983672142029], "taskxy": [1.1303986310958862, 0.11775460094213486], "dest": [1.1303985376358032, 0.10500000149011612]}
         184 +{"seed": 183, "success": true, "steps": 68, "seconds": 1.27, "phase": "place", "task": "target_block", "robot": [0.7105968594551086, 0.43518194556236267], "taskxy": [0.6211819052696228, 0.11581460386514664], "dest": [0.6211819506883621, 0.10500000149011612]}
         185 +{"seed": 184, "success": true, "steps": 56, "seconds": 1.09, "phase": "place", "task": "target_block", "robot": [0.5227537751197815, 0.4349152147769928], "taskxy": [0.46838974952697754, 0.11110152304172516], "dest": [0.4683896716237068, 0.10500000149011612]}
         186 +{"seed": 185, "success": true, "steps": 26, "seconds": 0.48, "phase": "place", "task": "target_block", "robot": [1.1295785903930664, 0.4156990945339203], "taskxy": [1.1027228832244873, 0.10500001162290573], "dest": [1.1027229089736938, 0.10500000149011612]}
         187 +{"seed": 186, "success": true, "steps": 23, "seconds": 0.45, "phase": "place", "task": "target_block", "robot": [0.8565794825553894, 0.44635188579559326], "taskxy": [0.8123353719711304, 0.10499999672174454], "dest": [0.812335472881794, 0.10500000149011612]}
         188 +{"seed": 187, "success": true, "steps": 55, "seconds": 0.72, "phase": "place", "task": "target_block", "robot": [0.879634439945221, 0.3927272856235504], "taskxy": [0.8033652305603027, 0.10500000417232513], "dest": [0.8033652563095093, 0.10500000149011612]}
         189 +{"seed": 188, "success": true, "steps": 25, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [1.1417644023895264, 0.5073009133338928], "taskxy": [1.083407998085022, 0.1140517070889473], "dest": [1.0834080238342285, 0.10500000149011612]}
         190 +{"seed": 189, "success": true, "steps": 37, "seconds": 0.58, "phase": "place", "task": "target_block", "robot": [0.5203484892845154, 0.3785127103328705], "taskxy": [0.4810485541820526, 0.10500001162290573], "dest": [0.4810485135316849, 0.10500000149011612]}
         191 +{"seed": 190, "success": true, "steps": 19, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [1.2292784452438354, 0.38788771629333496], "taskxy": [1.1581885814666748, 0.10500000417232513], "dest": [1.1581884880065918, 0.10500000149011612]}
         192 +{"seed": 191, "success": true, "steps": 31, "seconds": 0.45, "phase": "place", "task": "target_block", "robot": [0.3704800605773926, 0.48505374789237976], "taskxy": [0.32364729046821594, 0.10499995201826096], "dest": [0.3236472647190094, 0.10500000149011612]}
         193 +{"seed": 192, "success": true, "steps": 51, "seconds": 0.96, "phase": "place", "task": "target_block", "robot": [0.8002225756645203, 0.45102423429489136], "taskxy": [0.7718510627746582, 0.11088915169239044], "dest": [0.77185102891922, 0.10500000149011612]}
         194 +{"seed": 193, "success": true, "steps": 61, "seconds": 1.14, "phase": "place", "task": "target_block", "robot": [0.9963451027870178, 0.44249528646469116], "taskxy": [0.9350860714912415, 0.10499998927116394], "dest": [0.9350860376358032, 0.10500000149011612]}
         195 +{"seed": 194, "success": true, "steps": 80, "seconds": 1.54, "phase": "place", "task": "target_block", "robot": [0.7642729878425598, 0.44943496584892273], "taskxy": [0.6783518195152283, 0.11694321036338806], "dest": [0.6783518452644348, 0.10500000149011612]}
         196 +{"seed": 195, "success": true, "steps": 25, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [0.964584469795227, 0.4673209488391876], "taskxy": [0.9271239638328552, 0.10499999672174454], "dest": [0.927123929977417, 0.10500000149011612]}
         197 +{"seed": 196, "success": true, "steps": 39, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [0.31277817487716675, 0.4252198338508606], "taskxy": [0.28194278478622437, 0.10499998182058334], "dest": [0.2819427962899208, 0.10500000149011612]}
         198 +{"seed": 197, "success": true, "steps": 105, "seconds": 1.88, "phase": "place", "task": "target_block", "robot": [0.23045824468135834, 0.3804325461387634], "taskxy": [0.1317470520734787, 0.11212193220853806], "dest": [0.13174698907136917, 0.10500000149011612]}
         199 +{"seed": 198, "success": true, "steps": 64, "seconds": 1.18, "phase": "place", "task": "target_block", "robot": [0.5582054257392883, 0.3970530331134796], "taskxy": [0.4988064169883728, 0.10499998182058334], "dest": [0.49880640614032745, 0.10500000149011612]}
         200 +{"seed": 199, "success": true, "steps": 55, "seconds": 1.0, "phase": "place", "task": "target_block", "robot": [0.648369312286377, 0.38046735525131226], "taskxy": [0.6041066646575928, 0.10499998927116394], "dest": [0.6041066308021545, 0.10500000149011612]}
         201 +{"seed": 200, "success": true, "steps": 23, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [0.2759738564491272, 0.42613643407821655], "taskxy": [0.211454838514328, 0.10500000417232513], "dest": [0.21145481276512146, 0.10500000149011612]}
         202 +{"seed": 201, "success": true, "steps": 28, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [1.3988492488861084, 0.45141932368278503], "taskxy": [1.3624951839447021, 0.10500000417232513], "dest": [1.3624950904846191, 0.10500000149011612]}
         203 +{"seed": 202, "success": true, "steps": 32, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [0.5097997784614563, 0.4955108165740967], "taskxy": [0.44253644347190857, 0.10500001162290573], "dest": [0.4425364326238632, 0.10500000149011612]}
         204 +{"seed": 203, "success": true, "steps": 37, "seconds": 0.67, "phase": "place", "task": "target_block", "robot": [1.186576008796692, 0.43590211868286133], "taskxy": [1.115207314491272, 0.10499999672174454], "dest": [1.1152073402404785, 0.10500000149011612]}
         205 +{"seed": 204, "success": true, "steps": 62, "seconds": 1.27, "phase": "place", "task": "target_block", "robot": [1.0393760204315186, 0.4598790407180786], "taskxy": [0.987558901309967, 0.1079280897974968], "dest": [0.9875588830113411, 0.10500000149011612]}
         206 +{"seed": 205, "success": true, "steps": 41, "seconds": 0.87, "phase": "place", "task": "target_block", "robot": [0.7076284885406494, 0.38412514328956604], "taskxy": [0.6479341983795166, 0.10499999672174454], "dest": [0.6479342241287231, 0.10500000149011612]}
         207 +{"seed": 206, "success": true, "steps": 60, "seconds": 0.87, "phase": "place", "task": "target_block", "robot": [1.0803148746490479, 0.4990718364715576], "taskxy": [0.991710901260376, 0.10500001162290573], "dest": [0.9917109866142273, 0.10500000149011612]}
         208 +{"seed": 207, "success": true, "steps": 22, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [1.1297786235809326, 0.4129013419151306], "taskxy": [1.0416415929794312, 0.10499998927116394], "dest": [1.0416414995193481, 0.10500000149011612]}
         209 +{"seed": 208, "success": true, "steps": 29, "seconds": 0.62, "phase": "place", "task": "target_block", "robot": [0.5984526872634888, 0.5258283615112305], "taskxy": [0.5097808837890625, 0.1189642995595932], "dest": [0.5097808383703232, 0.10500000149011612]}
         210 +{"seed": 209, "success": true, "steps": 47, "seconds": 1.15, "phase": "place", "task": "target_block", "robot": [0.3402767777442932, 0.4764922559261322], "taskxy": [0.2583696246147156, 0.10499997437000275], "dest": [0.25836959075927735, 0.10500000149011612]}
         211 +{"seed": 210, "success": true, "steps": 22, "seconds": 0.43, "phase": "place", "task": "target_block", "robot": [1.3060802221298218, 0.4392000734806061], "taskxy": [1.250214695930481, 0.10500001907348633], "dest": [1.2502147216796875, 0.10500000149011612]}
         212 +{"seed": 211, "success": true, "steps": 31, "seconds": 0.45, "phase": "place", "task": "target_block", "robot": [0.3674474060535431, 0.4546499252319336], "taskxy": [0.27272942662239075, 0.10499999672174454], "dest": [0.2727294306755066, 0.10500000149011612]}
         213 +{"seed": 212, "success": true, "steps": 32, "seconds": 0.56, "phase": "place", "task": "target_block", "robot": [0.585322916507721, 0.46521443128585815], "taskxy": [0.4856983423233032, 0.10499997437000275], "dest": [0.48569840598106384, 0.10500000149011612]}
         214 +{"seed": 213, "success": true, "steps": 20, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [0.6057043075561523, 0.38289469480514526], "taskxy": [0.5172275304794312, 0.10500000417232513], "dest": [0.5172275047302246, 0.10500000149011612]}
         215 +{"seed": 214, "success": true, "steps": 46, "seconds": 0.91, "phase": "place", "task": "target_block", "robot": [0.8655529022216797, 0.3729828894138336], "taskxy": [0.7683003544807434, 0.10499998927116394], "dest": [0.7683004032373428, 0.10500000149011612]}
         216 +{"seed": 215, "success": true, "steps": 77, "seconds": 1.83, "phase": "place", "task": "target_block", "robot": [1.320755124092102, 0.4673813581466675], "taskxy": [1.2284895181655884, 0.1218569427728653], "dest": [1.228489543914795, 0.10500000149011612]}
         217 +{"seed": 216, "success": true, "steps": 34, "seconds": 0.64, "phase": "place", "task": "target_block", "robot": [1.2239514589309692, 0.4838959276676178], "taskxy": [1.1950523853302002, 0.10500002652406693], "dest": [1.1950523372292519, 0.10500000149011612]}
         218 +{"seed": 217, "success": true, "steps": 54, "seconds": 1.34, "phase": "place", "task": "target_block", "robot": [1.175728440284729, 0.4819212853908539], "taskxy": [1.1115593910217285, 0.10573051124811172], "dest": [1.111559416770935, 0.10500000149011612]}
         219 +{"seed": 218, "success": true, "steps": 44, "seconds": 0.78, "phase": "place", "task": "target_block", "robot": [1.176265001296997, 0.38821133971214294], "taskxy": [1.1356468200683594, 0.10500000417232513], "dest": [1.1356467266082764, 0.10500000149011612]}
         220 +{"seed": 219, "success": true, "steps": 25, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [1.157348871231079, 0.39573025703430176], "taskxy": [1.1398152112960815, 0.10499999672174454], "dest": [1.1398151296675205, 0.10500000149011612]}
         221 +{"seed": 220, "success": true, "steps": 52, "seconds": 1.37, "phase": "place", "task": "target_block", "robot": [1.0986727476119995, 0.4213770925998688], "taskxy": [1.0730984210968018, 0.11643066257238388], "dest": [1.0730983276367188, 0.10500000149011612]}
         222 +{"seed": 221, "success": true, "steps": 61, "seconds": 1.17, "phase": "place", "task": "target_block", "robot": [0.3358476459980011, 0.4090851843357086], "taskxy": [0.28837478160858154, 0.11406353116035461], "dest": [0.28837466645240784, 0.10500000149011612]}
         223 +{"seed": 222, "success": true, "steps": 50, "seconds": 0.79, "phase": "place", "task": "target_block", "robot": [0.9746835231781006, 0.4498068690299988], "taskxy": [0.9080284237861633, 0.10500002652406693], "dest": [0.908028338432312, 0.10500000149011612]}
         224 +{"seed": 223, "success": true, "steps": 32, "seconds": 0.67, "phase": "place", "task": "target_block", "robot": [0.7633123993873596, 0.509973406791687], "taskxy": [0.7206600308418274, 0.10499997437000275], "dest": [0.7206600565910339, 0.10500000149011612]}
         225 +{"seed": 224, "success": true, "steps": 58, "seconds": 1.31, "phase": "place", "task": "target_block", "robot": [0.6685876250267029, 0.5090759992599487], "taskxy": [0.62440425157547, 0.10500002652406693], "dest": [0.6244041852355003, 0.10500000149011612]}
         226 +{"seed": 225, "success": true, "steps": 104, "seconds": 2.16, "phase": "place", "task": "target_block", "robot": [1.384185791015625, 0.49962905049324036], "taskxy": [1.302336573600769, 0.10499996691942215], "dest": [1.3023365993499756, 0.10500000149011612]}
         227 +{"seed": 226, "success": true, "steps": 96, "seconds": 2.37, "phase": "place", "task": "target_block", "robot": [1.1779597997665405, 0.43679046630859375], "taskxy": [1.0982797145843506, 0.10499999672174454], "dest": [1.0982797403335571, 0.10500000149011612]}
         228 +{"seed": 227, "success": true, "steps": 63, "seconds": 1.41, "phase": "place", "task": "target_block", "robot": [0.3517328202724457, 0.5155989527702332], "taskxy": [0.3225812017917633, 0.10500003397464752], "dest": [0.3225811462402344, 0.10500000149011612]}
         229 +{"seed": 228, "success": true, "steps": 65, "seconds": 1.12, "phase": "place", "task": "target_block", "robot": [0.3378910720348358, 0.5143822431564331], "taskxy": [0.28288230299949646, 0.10500001162290573], "dest": [0.2828822921514511, 0.10500000149011612]}
         230 +{"seed": 229, "success": true, "steps": 26, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [0.7486321926116943, 0.4222504794597626], "taskxy": [0.671496570110321, 0.10499998182058334], "dest": [0.6714965958595276, 0.10500000149011612]}
         231 +{"seed": 230, "success": true, "steps": 45, "seconds": 0.75, "phase": "place", "task": "target_block", "robot": [0.5077856183052063, 0.4311956465244293], "taskxy": [0.45475825667381287, 0.10500001907348633], "dest": [0.45475822281837464, 0.10500000149011612]}
         232 +{"seed": 231, "success": true, "steps": 32, "seconds": 0.48, "phase": "place", "task": "target_block", "robot": [1.4847581386566162, 0.39034947752952576], "taskxy": [1.412453055381775, 0.10500000417232513], "dest": [1.412452961921692, 0.10500000149011612]}
         233 +{"seed": 232, "success": true, "steps": 28, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [0.8916046619415283, 0.4392629563808441], "taskxy": [0.8406209945678711, 0.11876391619443893], "dest": [0.8406209607124329, 0.10500000149011612]}
         234 +{"seed": 233, "success": true, "steps": 25, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.46690359711647034, 0.426400363445282], "taskxy": [0.4409104585647583, 0.10499998927116394], "dest": [0.44091043654084205, 0.10500000149011612]}
         235 +{"seed": 234, "success": true, "steps": 48, "seconds": 0.97, "phase": "place", "task": "target_block", "robot": [0.8331327438354492, 0.39630216360092163], "taskxy": [0.7439514398574829, 0.10499998927116394], "dest": [0.7439514656066895, 0.10500000149011612]}
         236 +{"seed": 235, "success": true, "steps": 70, "seconds": 1.37, "phase": "place", "task": "target_block", "robot": [1.0686665773391724, 0.4238032102584839], "taskxy": [0.9809161424636841, 0.10500001907348633], "dest": [0.9809161086082459, 0.10500000149011612]}
         237 +{"seed": 236, "success": true, "steps": 78, "seconds": 1.41, "phase": "place", "task": "target_block", "robot": [0.43392857909202576, 0.4580334722995758], "taskxy": [0.4006537199020386, 0.10500000417232513], "dest": [0.4006537910103798, 0.10500000149011612]}
         238 +{"seed": 237, "success": true, "steps": 130, "seconds": 2.82, "phase": "place", "task": "target_block", "robot": [1.1581759452819824, 0.4202324151992798], "taskxy": [1.0837352275848389, 0.11442454159259796], "dest": [1.0837352533340454, 0.10500000149011612]}
         239 +{"seed": 238, "success": true, "steps": 17, "seconds": 0.27, "phase": "place", "task": "target_block", "robot": [1.1040297746658325, 0.5032710433006287], "taskxy": [1.0285972356796265, 0.10499997437000275], "dest": [1.028597284436226, 0.10500000149011612]}
         240 +{"seed": 239, "success": true, "steps": 66, "seconds": 1.48, "phase": "place", "task": "target_block", "robot": [0.16682486236095428, 0.38093796372413635], "taskxy": [0.15599282085895538, 0.10499998927116394], "dest": [0.15599279779195785, 0.10500000149011612]}
         241 +{"seed": 240, "success": true, "steps": 88, "seconds": 2.15, "phase": "place", "task": "target_block", "robot": [0.612666666507721, 0.48277008533477783], "taskxy": [0.5492323637008667, 0.10499998182058334], "dest": [0.5492323379516602, 0.10500000149011612]}
         242 +{"seed": 241, "success": true, "steps": 16, "seconds": 0.45, "phase": "place", "task": "target_block", "robot": [0.7412592172622681, 0.4410387873649597], "taskxy": [0.7108486294746399, 0.10500002652406693], "dest": [0.7108485956192017, 0.10500000149011612]}
         243 +{"seed": 242, "success": true, "steps": 74, "seconds": 1.57, "phase": "place", "task": "target_block", "robot": [1.1532000303268433, 0.4735446274280548], "taskxy": [1.1005274057388306, 0.11291550099849701], "dest": [1.1005273122787476, 0.10500000149011612]}
         244 +{"seed": 243, "success": true, "steps": 36, "seconds": 0.94, "phase": "place", "task": "target_block", "robot": [0.8666688799858093, 0.4522400498390198], "taskxy": [0.8218184113502502, 0.10499998927116394], "dest": [0.8218185447454452, 0.10500000149011612]}
         245 +{"seed": 244, "success": true, "steps": 56, "seconds": 1.21, "phase": "place", "task": "target_block", "robot": [0.4911010265350342, 0.45117995142936707], "taskxy": [0.4545808434486389, 0.11887894570827484], "dest": [0.45458084005117416, 0.10500000149011612]}
         246 +{"seed": 245, "success": true, "steps": 44, "seconds": 0.76, "phase": "place", "task": "target_block", "robot": [1.4415509700775146, 0.49445393681526184], "taskxy": [1.3971720933914185, 0.12182342261075974], "dest": [1.3971720598638058, 0.10500000149011612]}
         247 +{"seed": 246, "success": true, "steps": 85, "seconds": 1.73, "phase": "place", "task": "target_block", "robot": [0.7642503976821899, 0.49088242650032043], "taskxy": [0.6990669965744019, 0.10500001162290573], "dest": [0.6990669627189636, 0.10500000149011612]}
         248 +{"seed": 247, "success": true, "steps": 31, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [0.20380060374736786, 0.4834861755371094], "taskxy": [0.1403365582227707, 0.10500002652406693], "dest": [0.14033650267124176, 0.10500000149011612]}
         249 +{"seed": 248, "success": true, "steps": 58, "seconds": 1.06, "phase": "place", "task": "target_block", "robot": [0.8608196973800659, 0.45696964859962463], "taskxy": [0.7712672352790833, 0.10499998182058334], "dest": [0.7712672244310379, 0.10500000149011612]}
         250 +{"seed": 249, "success": true, "steps": 59, "seconds": 1.4, "phase": "place", "task": "target_block", "robot": [0.8829273581504822, 0.3954724371433258], "taskxy": [0.8378003835678101, 0.10500002652406693], "dest": [0.8378004093170166, 0.10500000149011612]}
         251 +{"seed": 250, "success": true, "steps": 76, "seconds": 1.37, "phase": "place", "task": "target_block", "robot": [1.3038842678070068, 0.46708062291145325], "taskxy": [1.2672725915908813, 0.12196354568004608], "dest": [1.2672724981307983, 0.10500000149011612]}
         252 +{"seed": 251, "success": true, "steps": 21, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [0.7847655415534973, 0.39147523045539856], "taskxy": [0.7452533841133118, 0.10500001162290573], "dest": [0.7452534098625183, 0.10500000149011612]}
         253 +{"seed": 252, "success": true, "steps": 105, "seconds": 2.42, "phase": "place", "task": "target_block", "robot": [0.3148675560951233, 0.41874825954437256], "taskxy": [0.2326650470495224, 0.12078919261693954], "dest": [0.23266509580612182, 0.10500000149011612]}
         254 +{"seed": 253, "success": true, "steps": 59, "seconds": 1.22, "phase": "place", "task": "target_block", "robot": [0.47121843695640564, 0.4166892170906067], "taskxy": [0.39688506722450256, 0.10499998927116394], "dest": [0.39688499677181244, 0.10500000149011612]}
         255 +{"seed": 254, "success": true, "steps": 30, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [1.1631126403808594, 0.4831763207912445], "taskxy": [1.0712007284164429, 0.10500000417232513], "dest": [1.0712006349563599, 0.10500000149011612]}
         256 +{"seed": 255, "success": true, "steps": 24, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [0.4749964475631714, 0.5114946365356445], "taskxy": [0.43975576758384705, 0.10500001162290573], "dest": [0.4397557939887047, 0.10500000149011612]}
         257 +{"seed": 256, "success": true, "steps": 41, "seconds": 0.74, "phase": "place", "task": "target_block", "robot": [0.18776346743106842, 0.3770383596420288], "taskxy": [0.15264756977558136, 0.10500002652406693], "dest": [0.1526476110816002, 0.10500000149011612]}
         258 +{"seed": 257, "success": true, "steps": 42, "seconds": 0.99, "phase": "place", "task": "target_block", "robot": [0.7609815001487732, 0.4031407833099365], "taskxy": [0.7189555168151855, 0.10500001162290573], "dest": [0.7189555432200432, 0.10500000149011612]}
         259 +{"seed": 258, "success": true, "steps": 59, "seconds": 0.97, "phase": "place", "task": "target_block", "robot": [0.7062091827392578, 0.4496920108795166], "taskxy": [0.6362114548683167, 0.10500001162290573], "dest": [0.6362114806175232, 0.10500000149011612]}
         260 +{"seed": 259, "success": true, "steps": 18, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.9312155246734619, 0.46929770708084106], "taskxy": [0.8974550366401672, 0.10500004142522812], "dest": [0.8974550630450249, 0.10500000149011612]}
         261 +{"seed": 260, "success": true, "steps": 48, "seconds": 0.79, "phase": "place", "task": "target_block", "robot": [0.20646943151950836, 0.45633232593536377], "taskxy": [0.14486873149871826, 0.10499999672174454], "dest": [0.1448687504529953, 0.10500000149011612]}
         262 +{"seed": 261, "success": true, "steps": 84, "seconds": 1.21, "phase": "place", "task": "target_block", "robot": [1.3919466733932495, 0.4903557598590851], "taskxy": [1.3416986465454102, 0.11838201433420181], "dest": [1.3416986722946167, 0.10500000149011612]}
         263 +{"seed": 262, "success": true, "steps": 68, "seconds": 1.41, "phase": "place", "task": "target_block", "robot": [0.6816429495811462, 0.4072231948375702], "taskxy": [0.644614040851593, 0.11491809040307999], "dest": [0.6446140069961548, 0.10500000149011612]}
         264 +{"seed": 263, "success": true, "steps": 58, "seconds": 1.04, "phase": "place", "task": "target_block", "robot": [0.9665015339851379, 0.42489609122276306], "taskxy": [0.8788727521896362, 0.10633112490177155], "dest": [0.878872718334198, 0.10500000149011612]}
         265 +{"seed": 264, "success": true, "steps": 42, "seconds": 0.52, "phase": "place", "task": "target_block", "robot": [1.4424645900726318, 0.5062238574028015], "taskxy": [1.3729870319366455, 0.10499998927116394], "dest": [1.3729869384765625, 0.10500000149011612]}
         266 +{"seed": 265, "success": true, "steps": 76, "seconds": 1.24, "phase": "place", "task": "target_block", "robot": [0.9962603449821472, 0.46669816970825195], "taskxy": [0.9276090264320374, 0.11074265092611313], "dest": [0.9276089925765991, 0.10500000149011612]}
         267 +{"seed": 266, "success": true, "steps": 57, "seconds": 0.75, "phase": "place", "task": "target_block", "robot": [0.7869787812232971, 0.49575239419937134], "taskxy": [0.7370191216468811, 0.10500004887580872], "dest": [0.7370191473960876, 0.10500000149011612]}
         268 +{"seed": 267, "success": true, "steps": 52, "seconds": 0.71, "phase": "place", "task": "target_block", "robot": [0.5722533464431763, 0.5094451308250427], "taskxy": [0.506056010723114, 0.10499999672174454], "dest": [0.5060559768676758, 0.10500000149011612]}
         269 +{"seed": 268, "success": true, "steps": 119, "seconds": 2.02, "phase": "place", "task": "target_block", "robot": [0.3827471435070038, 0.5371249914169312], "taskxy": [0.30395928025245667, 0.12298395484685898], "dest": [0.3039593439102173, 0.10500000149011612]}
         270 +{"seed": 269, "success": true, "steps": 69, "seconds": 1.35, "phase": "place", "task": "target_block", "robot": [0.8137312531471252, 0.373912513256073], "taskxy": [0.7295321822166443, 0.10842517018318176], "dest": [0.7295321713685989, 0.10500000149011612]}
         271 +{"seed": 270, "success": true, "steps": 47, "seconds": 0.79, "phase": "place", "task": "target_block", "robot": [0.34268084168434143, 0.41687682271003723], "taskxy": [0.26159849762916565, 0.10641171038150787], "dest": [0.2615984867811203, 0.10500000149011612]}
diff --git a/reachability.jsonl b/reachability.jsonl
new file mode 100644
index 0000000..e69de29
diff --git a/test_counts_scene_v3.jsonl b/test_counts_scene_v3.jsonl
index 19506c0..8c570c1 100644
--- a/test_counts_scene_v3.jsonl
+++ b/test_counts_scene_v3.jsonl
@@ -35,3 +35,23 @@
   35     35  {"count": 4, "seed": 34, "steps": 101, "success": true, "seconds": 3.93}
   36     36  {"count": 4, "seed": 35, "steps": 50, "success": true, "seconds": 3.79}
   37     37  {"count": 4, "seed": 36, "steps": 164, "success": true, "seconds": 3.88}
          38 +{"count": 4, "seed": 37, "steps": 125, "success": true, "seconds": 8.42}
          39 +{"count": 4, "seed": 38, "steps": 78, "success": true, "seconds": 5.62}
          40 +{"count": 4, "seed": 39, "steps": 115, "success": true, "seconds": 9.62}
          41 +{"count": 4, "seed": 40, "steps": 1000, "success": false, "seconds": 28.52, "phase": "lift", "task": "obstruction0", "dest": [1.0216619691292983, 0.105], "robot": [1.1846210956573486, 0.5024091005325317], "init": {"obstruction0": [1.2066210508346558, 0.10000099986791611, 0.05134028568863869, 0.0626128688454628], "obstruction1": [1.1243525743484497, 0.10000099986791611, 0.05510848015546799, 0.08476104587316513], "obstruction2": [1.2656339406967163, 0.10000099986791611, 0.0683768093585968, 0.06045512482523918], "obstruction3": [1.373109221458435, 0.10000099986791611, 0.15054073929786682, 0.09669425338506699], "target_block": [0.5387240052223206, 0.10000099986791611, 0.16028523445129395, 0.06994911283254623], "target_surface": [1.1792722940444946, 0.0, 0.19835792481899261, 0.10000000149011612]}, "final": {"obstruction0": [1.2066210508346558, 0.10000099986791611, 0.05134028568863869, 0.0626128688454628], "obstruction1": [1.1243525743484497, 0.10000099986791611, 0.05510848015546799, 0.08476104587316513], "obstruction2": [1.2656339406967163, 0.10000099986791611, 0.0683768093585968, 0.06045512482523918], "obstruction3": [1.373109221458435, 0.10000099986791611, 0.15054073929786682, 0.09669425338506699], "target_block": [0.5387240052223206, 0.10000099986791611, 0.16028523445129395, 0.06994911283254623], "target_surface": [1.1792722940444946, 0.0, 0.19835792481899261, 0.10000000149011612]}}
          42 +{"count": 4, "seed": 41, "steps": 100, "success": true, "seconds": 5.03}
          43 +{"count": 4, "seed": 42, "steps": 63, "success": true, "seconds": 4.4}
          44 +{"count": 4, "seed": 43, "steps": 82, "success": true, "seconds": 5.74}
          45 +{"count": 4, "seed": 44, "steps": 85, "success": true, "seconds": 4.03}
          46 +{"count": 4, "seed": 45, "steps": 67, "success": true, "seconds": 5.09}
          47 +{"count": 4, "seed": 46, "steps": 112, "success": true, "seconds": 6.21}
          48 +{"count": 4, "seed": 47, "steps": 84, "success": true, "seconds": 5.49}
          49 +{"count": 4, "seed": 48, "steps": 118, "success": true, "seconds": 7.17}
          50 +{"count": 4, "seed": 49, "steps": 71, "success": true, "seconds": 4.98}
          51 +{"count": 4, "seed": 50, "steps": 78, "success": true, "seconds": 6.33}
          52 +{"count": 4, "seed": 51, "steps": 81, "success": true, "seconds": 7.94}
          53 +{"count": 4, "seed": 52, "steps": 72, "success": true, "seconds": 7.5}
          54 +{"count": 4, "seed": 53, "steps": 87, "success": true, "seconds": 7.5}
          55 +{"count": 4, "seed": 54, "steps": 63, "success": true, "seconds": 5.81}
          56 +{"count": 4, "seed": 55, "steps": 106, "success": true, "seconds": 5.02}
          57 +{"count": 4, "seed": 56, "steps": 88, "success": true, "seconds": 3.38}
diff --git a/test_counts_scene_v3.log b/test_counts_scene_v3.log
index 19506c0..8c570c1 100644
--- a/test_counts_scene_v3.log
+++ b/test_counts_scene_v3.log
@@ -35,3 +35,23 @@
   35     35  {"count": 4, "seed": 34, "steps": 101, "success": true, "seconds": 3.93}
   36     36  {"count": 4, "seed": 35, "steps": 50, "success": true, "seconds": 3.79}
   37     37  {"count": 4, "seed": 36, "steps": 164, "success": true, "seconds": 3.88}
          38 +{"count": 4, "seed": 37, "steps": 125, "success": true, "seconds": 8.42}
          39 +{"count": 4, "seed": 38, "steps": 78, "success": true, "seconds": 5.62}
          40 +{"count": 4, "seed": 39, "steps": 115, "success": true, "seconds": 9.62}
          41 +{"count": 4, "seed": 40, "steps": 1000, "success": false, "seconds": 28.52, "phase": "lift", "task": "obstruction0", "dest": [1.0216619691292983, 0.105], "robot": [1.1846210956573486, 0.5024091005325317], "init": {"obstruction0": [1.2066210508346558, 0.10000099986791611, 0.05134028568863869, 0.0626128688454628], "obstruction1": [1.1243525743484497, 0.10000099986791611, 0.05510848015546799, 0.08476104587316513], "obstruction2": [1.2656339406967163, 0.10000099986791611, 0.0683768093585968, 0.06045512482523918], "obstruction3": [1.373109221458435, 0.10000099986791611, 0.15054073929786682, 0.09669425338506699], "target_block": [0.5387240052223206, 0.10000099986791611, 0.16028523445129395, 0.06994911283254623], "target_surface": [1.1792722940444946, 0.0, 0.19835792481899261, 0.10000000149011612]}, "final": {"obstruction0": [1.2066210508346558, 0.10000099986791611, 0.05134028568863869, 0.0626128688454628], "obstruction1": [1.1243525743484497, 0.10000099986791611, 0.05510848015546799, 0.08476104587316513], "obstruction2": [1.2656339406967163, 0.10000099986791611, 0.0683768093585968, 0.06045512482523918], "obstruction3": [1.373109221458435, 0.10000099986791611, 0.15054073929786682, 0.09669425338506699], "target_block": [0.5387240052223206, 0.10000099986791611, 0.16028523445129395, 0.06994911283254623], "target_surface": [1.1792722940444946, 0.0, 0.19835792481899261, 0.10000000149011612]}}
          42 +{"count": 4, "seed": 41, "steps": 100, "success": true, "seconds": 5.03}
          43 +{"count": 4, "seed": 42, "steps": 63, "success": true, "seconds": 4.4}
          44 +{"count": 4, "seed": 43, "steps": 82, "success": true, "seconds": 5.74}
          45 +{"count": 4, "seed": 44, "steps": 85, "success": true, "seconds": 4.03}
          46 +{"count": 4, "seed": 45, "steps": 67, "success": true, "seconds": 5.09}
          47 +{"count": 4, "seed": 46, "steps": 112, "success": true, "seconds": 6.21}
          48 +{"count": 4, "seed": 47, "steps": 84, "success": true, "seconds": 5.49}
          49 +{"count": 4, "seed": 48, "steps": 118, "success": true, "seconds": 7.17}
          50 +{"count": 4, "seed": 49, "steps": 71, "success": true, "seconds": 4.98}
          51 +{"count": 4, "seed": 50, "steps": 78, "success": true, "seconds": 6.33}
          52 +{"count": 4, "seed": 51, "steps": 81, "success": true, "seconds": 7.94}
          53 +{"count": 4, "seed": 52, "steps": 72, "success": true, "seconds": 7.5}
          54 +{"count": 4, "seed": 53, "steps": 87, "success": true, "seconds": 7.5}
          55 +{"count": 4, "seed": 54, "steps": 63, "success": true, "seconds": 5.81}
          56 +{"count": 4, "seed": 55, "steps": 106, "success": true, "seconds": 5.02}
          57 +{"count": 4, "seed": 56, "steps": 88, "success": true, "seconds": 3.38}
diff --git a/validate_count3.jsonl b/validate_count3.jsonl
index e8f7b10..d0dc937 100644
--- a/validate_count3.jsonl
+++ b/validate_count3.jsonl
@@ -48,3 +48,53 @@
   48     48  {"seed": 147, "count": 3, "success": true, "steps": 61, "policy_seconds": 0.0131, "elapsed": 0.828}
   49     49  {"seed": 148, "count": 3, "success": true, "steps": 102, "policy_seconds": 0.0154, "elapsed": 1.313}
   50     50  {"seed": 149, "count": 3, "success": true, "steps": 56, "policy_seconds": 0.0111, "elapsed": 0.786}
          51 +{"seed": 150, "count": 3, "success": true, "steps": 101, "policy_seconds": 0.0247, "elapsed": 1.753}
          52 +{"seed": 151, "count": 3, "success": true, "steps": 65, "policy_seconds": 0.0126, "elapsed": 1.701}
          53 +{"seed": 152, "count": 3, "success": true, "steps": 85, "policy_seconds": 0.0155, "elapsed": 1.867}
          54 +{"seed": 153, "count": 3, "success": true, "steps": 110, "policy_seconds": 0.0282, "elapsed": 2.715}
          55 +{"seed": 154, "count": 3, "success": true, "steps": 73, "policy_seconds": 0.014, "elapsed": 1.691}
          56 +{"seed": 155, "count": 3, "success": true, "steps": 98, "policy_seconds": 0.0167, "elapsed": 2.265}
          57 +{"seed": 156, "count": 3, "success": true, "steps": 71, "policy_seconds": 0.0124, "elapsed": 1.669}
          58 +{"seed": 157, "count": 3, "success": true, "steps": 62, "policy_seconds": 0.0125, "elapsed": 1.307}
          59 +{"seed": 158, "count": 3, "success": true, "steps": 64, "policy_seconds": 0.0136, "elapsed": 1.446}
          60 +{"seed": 159, "count": 3, "success": true, "steps": 61, "policy_seconds": 0.0143, "elapsed": 1.384}
          61 +{"seed": 160, "count": 3, "success": true, "steps": 80, "policy_seconds": 0.0125, "elapsed": 2.052}
          62 +{"seed": 161, "count": 3, "success": true, "steps": 60, "policy_seconds": 0.0148, "elapsed": 1.349}
          63 +{"seed": 162, "count": 3, "success": true, "steps": 22, "policy_seconds": 0.003, "elapsed": 0.47}
          64 +{"seed": 163, "count": 3, "success": true, "steps": 61, "policy_seconds": 0.0196, "elapsed": 1.584}
          65 +{"seed": 164, "count": 3, "success": true, "steps": 121, "policy_seconds": 0.0338, "elapsed": 3.087}
          66 +{"seed": 165, "count": 3, "success": true, "steps": 97, "policy_seconds": 0.0217, "elapsed": 2.266}
          67 +{"seed": 166, "count": 3, "success": true, "steps": 93, "policy_seconds": 0.0224, "elapsed": 2.03}
          68 +{"seed": 167, "count": 3, "success": true, "steps": 65, "policy_seconds": 0.0128, "elapsed": 1.467}
          69 +{"seed": 168, "count": 3, "success": true, "steps": 70, "policy_seconds": 0.0135, "elapsed": 1.541}
          70 +{"seed": 169, "count": 3, "success": true, "steps": 44, "policy_seconds": 0.014, "elapsed": 1.02}
          71 +{"seed": 170, "count": 3, "success": true, "steps": 74, "policy_seconds": 0.0121, "elapsed": 1.62}
          72 +{"seed": 171, "count": 3, "success": true, "steps": 64, "policy_seconds": 0.0124, "elapsed": 1.493}
          73 +{"seed": 172, "count": 3, "success": true, "steps": 74, "policy_seconds": 0.0134, "elapsed": 1.6}
          74 +{"seed": 173, "count": 3, "success": true, "steps": 101, "policy_seconds": 0.0242, "elapsed": 2.402}
          75 +{"seed": 174, "count": 3, "success": true, "steps": 57, "policy_seconds": 0.0125, "elapsed": 1.415}
          76 +{"seed": 175, "count": 3, "success": true, "steps": 75, "policy_seconds": 0.0173, "elapsed": 1.819}
          77 +{"seed": 176, "count": 3, "success": true, "steps": 68, "policy_seconds": 0.0094, "elapsed": 1.467}
          78 +{"seed": 177, "count": 3, "success": true, "steps": 54, "policy_seconds": 0.0131, "elapsed": 1.232}
          79 +{"seed": 178, "count": 3, "success": true, "steps": 93, "policy_seconds": 0.0155, "elapsed": 2.149}
          80 +{"seed": 179, "count": 3, "success": true, "steps": 61, "policy_seconds": 0.0099, "elapsed": 1.38}
          81 +{"seed": 180, "count": 3, "success": true, "steps": 76, "policy_seconds": 0.0263, "elapsed": 1.88}
          82 +{"seed": 181, "count": 3, "success": true, "steps": 71, "policy_seconds": 0.0138, "elapsed": 1.809}
          83 +{"seed": 182, "count": 3, "success": true, "steps": 93, "policy_seconds": 0.0142, "elapsed": 2.196}
          84 +{"seed": 183, "count": 3, "success": true, "steps": 88, "policy_seconds": 0.0096, "elapsed": 2.394}
          85 +{"seed": 184, "count": 3, "success": true, "steps": 110, "policy_seconds": 0.0277, "elapsed": 2.755}
          86 +{"seed": 185, "count": 3, "success": true, "steps": 93, "policy_seconds": 0.0209, "elapsed": 2.409}
          87 +{"seed": 186, "count": 3, "success": true, "steps": 63, "policy_seconds": 0.01, "elapsed": 1.773}
          88 +{"seed": 187, "count": 3, "success": true, "steps": 90, "policy_seconds": 0.0184, "elapsed": 2.279}
          89 +{"seed": 188, "count": 3, "success": true, "steps": 90, "policy_seconds": 0.0144, "elapsed": 1.952}
          90 +{"seed": 189, "count": 3, "success": true, "steps": 101, "policy_seconds": 0.0229, "elapsed": 2.766}
          91 +{"seed": 190, "count": 3, "success": true, "steps": 79, "policy_seconds": 0.0172, "elapsed": 2.111}
          92 +{"seed": 191, "count": 3, "success": true, "steps": 106, "policy_seconds": 0.0326, "elapsed": 2.566}
          93 +{"seed": 192, "count": 3, "success": true, "steps": 69, "policy_seconds": 0.0139, "elapsed": 1.61}
          94 +{"seed": 193, "count": 3, "success": true, "steps": 124, "policy_seconds": 0.0147, "elapsed": 3.349}
          95 +{"seed": 194, "count": 3, "success": true, "steps": 117, "policy_seconds": 0.0292, "elapsed": 2.851}
          96 +{"seed": 195, "count": 3, "success": true, "steps": 57, "policy_seconds": 0.0133, "elapsed": 1.606}
          97 +{"seed": 196, "count": 3, "success": true, "steps": 57, "policy_seconds": 0.0144, "elapsed": 1.559}
          98 +{"seed": 197, "count": 3, "success": true, "steps": 139, "policy_seconds": 0.037, "elapsed": 3.739}
          99 +{"seed": 198, "count": 3, "success": true, "steps": 75, "policy_seconds": 0.0149, "elapsed": 2.177}
         100 +{"seed": 199, "count": 3, "success": true, "steps": 82, "policy_seconds": 0.0165, "elapsed": 1.865}
```

</details>

<a id="C013"></a>
### C013 · Protect the full target lift column and clear overhead grasp obstructions

Commit `ffca88e4b374cf20096b79c277d3c5907a3cab00`; parents: e8ce3b889ab7f28c968f9f5f00117b5b19934db1. Recorded author date: 2026-09-21T17:37:19Z.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0091](01_timeline.md#E0091): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_ffca88e_approach.py) · [Exact all-file diff](evidence/diffs/C013_ffca88e.diff)

[Previous saved controller snapshot](evidence/versions/C012_e8ce3b8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f735e39..1bc7e68 100644
--- a/approach.py
+++ b/approach.py
@@ -37,7 +37,13 @@ class GeneratedApproach:
   37     37  
   38     38      def conflicts(self,s,obj,x,y,offset,others,pickup=False):
   39     39          _,_,w,h=self.rect(s,obj)
   40        -        return [o for o in others if self.hits_configuration(self.rect(s,o),x,y,w,h,offset,body_margin=.00001 if pickup else .003)]
          40 +        bad=[]
          41 +        for o in others:
          42 +            q=self.rect(s,o)
          43 +            overhead=pickup and q[1]>=y+h-.001 and q[0]<x+w+.001 and q[0]+q[2]>x-.001
          44 +            if overhead or self.hits_configuration(q,x,y,w,h,offset,body_margin=.00001 if pickup else .003):
          45 +                bad.append(o)
          46 +        return bad
   41     47  
   42     48      def offsets(self,x,px,w):
   43     49          low=max(.1002-x,.1002-px,-.022)
@@ -97,6 +103,7 @@ class GeneratedApproach:
   97    103              places=[]
   98    104              for px in np.linspace(.105,1.513-w,75):
   99    105                  if px<gx+bw+.13 and px+w>gx-.13:continue
         106 +                if px<bx+bw+.008 and px+w>bx-.008:continue
  100    107                  py=max([.105]+[qy+qh+.022 for qx,qy,qw,qh in occupied if px<qx+qw+.025 and px+w>qx-.025])
  101    108                  if py+h>.43:continue
  102    109                  if self.hits_configuration((px,py,w,h),*keep_pick) or self.hits_configuration((px,py,w,h),*keep_place):continue
@@ -112,6 +119,7 @@ class GeneratedApproach:
  112    119                  fallback=[]
  113    120                  for px in np.linspace(.105,1.513-w,75):
  114    121                      if px<gx+bw+.07 and px+w>gx-.07:continue
         122 +                    if px<bx+bw+.008 and px+w>bx-.008:continue
  115    123                      py=max([.105]+[qy+qh+.025 for qx,qy,qw,qh in occupied if px<qx+qw+.04 and px+w>qx-.04])
  116    124                      if self.hits_configuration((px,py,w,h),*keep_pick) or self.hits_configuration((px,py,w,h),*keep_place):continue
  117    125                      for off in self.offsets(x,px,w):
diff --git a/probe_final_0_499.jsonl b/probe_final_0_499.jsonl
index a1f7574..fc35185 100644
--- a/probe_final_0_499.jsonl
+++ b/probe_final_0_499.jsonl
@@ -269,3 +269,232 @@
  269    269  {"seed": 268, "success": true, "steps": 119, "seconds": 2.02, "phase": "place", "task": "target_block", "robot": [0.3827471435070038, 0.5371249914169312], "taskxy": [0.30395928025245667, 0.12298395484685898], "dest": [0.3039593439102173, 0.10500000149011612]}
  270    270  {"seed": 269, "success": true, "steps": 69, "seconds": 1.35, "phase": "place", "task": "target_block", "robot": [0.8137312531471252, 0.373912513256073], "taskxy": [0.7295321822166443, 0.10842517018318176], "dest": [0.7295321713685989, 0.10500000149011612]}
  271    271  {"seed": 270, "success": true, "steps": 47, "seconds": 0.79, "phase": "place", "task": "target_block", "robot": [0.34268084168434143, 0.41687682271003723], "taskxy": [0.26159849762916565, 0.10641171038150787], "dest": [0.2615984867811203, 0.10500000149011612]}
         272 +{"seed": 271, "success": true, "steps": 62, "seconds": 1.26, "phase": "place", "task": "target_block", "robot": [0.2940387725830078, 0.41176772117614746], "taskxy": [0.24563856422901154, 0.10499996691942215], "dest": [0.24563857573270798, 0.10500000149011612]}
         273 +{"seed": 272, "success": true, "steps": 18, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [1.1501511335372925, 0.517644464969635], "taskxy": [1.0988150835037231, 0.10500000417232513], "dest": [1.0988151092529297, 0.10500000149011612]}
         274 +{"seed": 273, "success": true, "steps": 31, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [1.4732701778411865, 0.43444886803627014], "taskxy": [1.3840725421905518, 0.10499998182058334], "dest": [1.3840724487304688, 0.10500000149011612]}
         275 +{"seed": 274, "success": true, "steps": 41, "seconds": 0.77, "phase": "place", "task": "target_block", "robot": [0.22645337879657745, 0.4770493507385254], "taskxy": [0.2147076278924942, 0.10499999672174454], "dest": [0.21470768305659294, 0.10500000149011612]}
         276 +{"seed": 275, "success": true, "steps": 35, "seconds": 0.54, "phase": "place", "task": "target_block", "robot": [0.36647510528564453, 0.41051149368286133], "taskxy": [0.3079841136932373, 0.10500001907348633], "dest": [0.30798413944244385, 0.10500000149011612]}
         277 +{"seed": 276, "success": true, "steps": 25, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [0.9892939329147339, 0.5130296349525452], "taskxy": [0.9309187531471252, 0.10500001907348633], "dest": [0.9309187077283859, 0.10500000149011612]}
         278 +{"seed": 277, "success": true, "steps": 34, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [0.8304592967033386, 0.3929527997970581], "taskxy": [0.795076310634613, 0.10499998182058334], "dest": [0.7950763363838196, 0.10500000149011612]}
         279 +{"seed": 278, "success": true, "steps": 27, "seconds": 0.54, "phase": "place", "task": "target_block", "robot": [1.4918051958084106, 0.5132402181625366], "taskxy": [1.4112334251403809, 0.10499998927116394], "dest": [1.4112335003614425, 0.10500000149011612]}
         280 +{"seed": 279, "success": true, "steps": 59, "seconds": 1.16, "phase": "place", "task": "target_block", "robot": [0.420990914106369, 0.46458157896995544], "taskxy": [0.3521271347999573, 0.10500001907348633], "dest": [0.3521271686553955, 0.10500000149011612]}
         281 +{"seed": 280, "success": true, "steps": 32, "seconds": 0.78, "phase": "place", "task": "target_block", "robot": [1.1088048219680786, 0.48295891284942627], "taskxy": [1.07063889503479, 0.1095249354839325], "dest": [1.0706390298604964, 0.10500000149011612]}
         282 +{"seed": 281, "success": true, "steps": 59, "seconds": 0.88, "phase": "place", "task": "target_block", "robot": [0.4921419322490692, 0.37818923592567444], "taskxy": [0.40338075160980225, 0.10500001162290573], "dest": [0.4033807854652405, 0.10500000149011612]}
         283 +{"seed": 282, "success": true, "steps": 60, "seconds": 1.35, "phase": "place", "task": "target_block", "robot": [0.3845413625240326, 0.4864894151687622], "taskxy": [0.35370656847953796, 0.10499998927116394], "dest": [0.3537065576314926, 0.10500000149011612]}
         284 +{"seed": 283, "success": true, "steps": 52, "seconds": 0.85, "phase": "place", "task": "target_block", "robot": [1.3864120244979858, 0.4255913496017456], "taskxy": [1.2941601276397705, 0.10499999672174454], "dest": [1.294160153388977, 0.10500000149011612]}
         285 +{"seed": 284, "success": true, "steps": 25, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [0.6078687310218811, 0.4003709852695465], "taskxy": [0.5217065215110779, 0.10500000417232513], "dest": [0.5217065472602844, 0.10500000149011612]}
         286 +{"seed": 285, "success": true, "steps": 82, "seconds": 1.54, "phase": "place", "task": "target_block", "robot": [1.009474515914917, 0.4882239103317261], "taskxy": [0.9658775925636292, 0.10499998182058334], "dest": [0.9658775891661644, 0.10500000149011612]}
         287 +{"seed": 286, "success": true, "steps": 31, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [1.2314084768295288, 0.40882986783981323], "taskxy": [1.1772443056106567, 0.10499998927116394], "dest": [1.1772443313598633, 0.10500000149011612]}
         288 +{"seed": 287, "success": true, "steps": 93, "seconds": 1.68, "phase": "place", "task": "target_block", "robot": [0.18717947602272034, 0.4621281921863556], "taskxy": [0.1307925581932068, 0.10500000417232513], "dest": [0.1307925321161747, 0.10500000149011612]}
         289 +{"seed": 288, "success": true, "steps": 23, "seconds": 0.41, "phase": "place", "task": "target_block", "robot": [1.0804330110549927, 0.4130425453186035], "taskxy": [1.0270189046859741, 0.10500001907348633], "dest": [1.0270189608931541, 0.10500000149011612]}
         290 +{"seed": 289, "success": true, "steps": 31, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [0.3689393103122711, 0.37934714555740356], "taskxy": [0.3330755829811096, 0.10499999672174454], "dest": [0.33307558703422546, 0.10500000149011612]}
         291 +{"seed": 290, "success": true, "steps": 37, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [1.3682904243469238, 0.39810508489608765], "taskxy": [1.3338005542755127, 0.10499999672174454], "dest": [1.3338005800247192, 0.10500000149011612]}
         292 +{"seed": 291, "success": true, "steps": 33, "seconds": 0.54, "phase": "place", "task": "target_block", "robot": [0.9961521029472351, 0.3819141387939453], "taskxy": [0.9554236531257629, 0.10500001162290573], "dest": [0.9554236788749695, 0.10500000149011612]}
         293 +{"seed": 292, "success": true, "steps": 95, "seconds": 2.08, "phase": "place", "task": "target_block", "robot": [1.3690439462661743, 0.4288320243358612], "taskxy": [1.3160985708236694, 0.12303368747234344], "dest": [1.316098596572876, 0.10500000149011612]}
         294 +{"seed": 293, "success": true, "steps": 33, "seconds": 0.62, "phase": "place", "task": "target_block", "robot": [1.0617640018463135, 0.42949044704437256], "taskxy": [1.0247303247451782, 0.10499998182058334], "dest": [1.0247303504943848, 0.10500000149011612]}
         295 +{"seed": 294, "success": true, "steps": 30, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [1.3249820470809937, 0.4201604127883911], "taskxy": [1.242795467376709, 0.10499999672174454], "dest": [1.2427954931259155, 0.10500000149011612]}
         296 +{"seed": 295, "success": true, "steps": 50, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [0.5176838636398315, 0.48791879415512085], "taskxy": [0.4601781964302063, 0.10500000417232513], "dest": [0.4601781185269356, 0.10500000149011612]}
         297 +{"seed": 296, "success": true, "steps": 26, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [0.5613390207290649, 0.46164003014564514], "taskxy": [0.47853192687034607, 0.10499997437000275], "dest": [0.4785319526195526, 0.10500000149011612]}
         298 +{"seed": 297, "success": true, "steps": 35, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [1.4843109846115112, 0.4453553557395935], "taskxy": [1.3920978307724, 0.10499998927116394], "dest": [1.3920978565216064, 0.10500000149011612]}
         299 +{"seed": 298, "success": true, "steps": 54, "seconds": 0.94, "phase": "place", "task": "target_block", "robot": [1.0350075960159302, 0.4171168804168701], "taskxy": [1.0057158470153809, 0.10499997437000275], "dest": [1.0057158398926258, 0.10500000149011612]}
         300 +{"seed": 299, "success": true, "steps": 72, "seconds": 1.38, "phase": "place", "task": "target_block", "robot": [0.3547597825527191, 0.48631396889686584], "taskxy": [0.26695334911346436, 0.10500001162290573], "dest": [0.26695320415496826, 0.10500000149011612]}
         301 +{"seed": 300, "success": true, "steps": 27, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [0.8936875462532043, 0.4742531478404999], "taskxy": [0.8328515291213989, 0.10499998927116394], "dest": [0.8328514952659607, 0.10500000149011612]}
         302 +{"seed": 301, "success": true, "steps": 50, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [0.18627995252609253, 0.3761948049068451], "taskxy": [0.15389588475227356, 0.10500001907348633], "dest": [0.15389579194784164, 0.10500000149011612]}
         303 +{"seed": 302, "success": true, "steps": 60, "seconds": 0.91, "phase": "place", "task": "target_block", "robot": [0.7731902003288269, 0.412769079208374], "taskxy": [0.743759274482727, 0.10499998182058334], "dest": [0.7437592003047466, 0.10500000149011612]}
         304 +{"seed": 303, "success": true, "steps": 73, "seconds": 1.04, "phase": "place", "task": "target_block", "robot": [0.3846931457519531, 0.4578608572483063], "taskxy": [0.3498140573501587, 0.11973357945680618], "dest": [0.3498141061067581, 0.10500000149011612]}
         305 +{"seed": 304, "success": true, "steps": 57, "seconds": 1.02, "phase": "place", "task": "target_block", "robot": [1.1474121809005737, 0.5010412335395813], "taskxy": [1.0517457723617554, 0.10500001162290573], "dest": [1.051745798110962, 0.10500000149011612]}
         306 +{"seed": 305, "success": true, "steps": 29, "seconds": 0.41, "phase": "place", "task": "target_block", "robot": [0.35821813344955444, 0.4475279748439789], "taskxy": [0.263249009847641, 0.10500002652406693], "dest": [0.26324899899959564, 0.10500000149011612]}
         307 +{"seed": 306, "success": true, "steps": 57, "seconds": 1.0, "phase": "place", "task": "target_block", "robot": [1.3522206544876099, 0.5113912224769592], "taskxy": [1.3064438104629517, 0.10499998182058334], "dest": [1.306443796277046, 0.10500000149011612]}
         308 +{"seed": 307, "success": true, "steps": 64, "seconds": 1.16, "phase": "place", "task": "target_block", "robot": [0.5665632486343384, 0.4953773617744446], "taskxy": [0.4974875748157501, 0.10499998927116394], "dest": [0.49748757886886597, 0.10500000149011612]}
         309 +{"seed": 308, "success": true, "steps": 63, "seconds": 0.89, "phase": "place", "task": "target_block", "robot": [1.2905954122543335, 0.48604512214660645], "taskxy": [1.1991163492202759, 0.10500004887580872], "dest": [1.1991163749694824, 0.10500000149011612]}
         310 +{"seed": 309, "success": true, "steps": 76, "seconds": 0.84, "phase": "place", "task": "target_block", "robot": [1.3671461343765259, 0.50931316614151], "taskxy": [1.2690550088882446, 0.11188290268182755], "dest": [1.2690550346374512, 0.10500000149011612]}
         311 +{"seed": 310, "success": true, "steps": 23, "seconds": 0.17, "phase": "place", "task": "target_block", "robot": [0.7939228415489197, 0.47272157669067383], "taskxy": [0.735931396484375, 0.10499998927116394], "dest": [0.735931489944458, 0.10500000149011612]}
         312 +{"seed": 311, "success": true, "steps": 55, "seconds": 0.8, "phase": "place", "task": "target_block", "robot": [0.5073915123939514, 0.382309228181839], "taskxy": [0.4081820547580719, 0.10499998927116394], "dest": [0.40818208861351013, 0.10500000149011612]}
         313 +{"seed": 312, "success": true, "steps": 50, "seconds": 0.56, "phase": "place", "task": "target_block", "robot": [1.4693986177444458, 0.46117880940437317], "taskxy": [1.4436348676681519, 0.10499999672174454], "dest": [1.4436348934173584, 0.10500000149011612]}
         314 +{"seed": 313, "success": true, "steps": 26, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.18323567509651184, 0.4730072617530823], "taskxy": [0.15031011402606964, 0.10500001162290573], "dest": [0.15031013298034668, 0.10500000149011612]}
         315 +{"seed": 314, "success": true, "steps": 39, "seconds": 0.48, "phase": "place", "task": "target_block", "robot": [0.6002144813537598, 0.38512155413627625], "taskxy": [0.5405755639076233, 0.10499999672174454], "dest": [0.5405755300521851, 0.10500000149011612]}
         316 +{"seed": 315, "success": true, "steps": 26, "seconds": 0.37, "phase": "place", "task": "target_block", "robot": [0.7293165326118469, 0.4898226857185364], "taskxy": [0.6978799700737, 0.11247511953115463], "dest": [0.6978800039291382, 0.10500000149011612]}
         317 +{"seed": 316, "success": true, "steps": 26, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [0.6356378793716431, 0.5031300783157349], "taskxy": [0.5817077159881592, 0.10500002652406693], "dest": [0.5817077498435974, 0.10500000149011612]}
         318 +{"seed": 317, "success": true, "steps": 19, "seconds": 0.22, "phase": "place", "task": "target_block", "robot": [1.3941590785980225, 0.4158160984516144], "taskxy": [1.3610461950302124, 0.10499997437000275], "dest": [1.361046220779419, 0.10500000149011612]}
         319 +{"seed": 318, "success": true, "steps": 49, "seconds": 0.62, "phase": "place", "task": "target_block", "robot": [1.209058165550232, 0.4435513913631439], "taskxy": [1.111480474472046, 0.10499997437000275], "dest": [1.1114805002212524, 0.10500000149011612]}
         320 +{"seed": 319, "success": true, "steps": 72, "seconds": 1.3, "phase": "place", "task": "target_block", "robot": [1.3386346101760864, 0.5179796814918518], "taskxy": [1.2504926919937134, 0.11395709961652756], "dest": [1.2504925985336304, 0.10500000149011612]}
         321 +{"seed": 320, "success": true, "steps": 19, "seconds": 0.25, "phase": "place", "task": "target_block", "robot": [0.8800584077835083, 0.4916617274284363], "taskxy": [0.8098044991493225, 0.10499997437000275], "dest": [0.8098045330047607, 0.10500000149011612]}
         322 +{"seed": 321, "success": true, "steps": 64, "seconds": 1.02, "phase": "place", "task": "target_block", "robot": [0.726736307144165, 0.39819130301475525], "taskxy": [0.6505128145217896, 0.10500001162290573], "dest": [0.6505127440690994, 0.10500000149011612]}
         323 +{"seed": 322, "success": true, "steps": 28, "seconds": 0.48, "phase": "place", "task": "target_block", "robot": [1.0728050470352173, 0.4430234432220459], "taskxy": [1.0314122438430786, 0.10500001162290573], "dest": [1.0314122695922852, 0.10500000149011612]}
         324 +{"seed": 323, "success": true, "steps": 44, "seconds": 0.72, "phase": "place", "task": "target_block", "robot": [0.34236907958984375, 0.5141783356666565], "taskxy": [0.2718924283981323, 0.10597153753042221], "dest": [0.2718922983407974, 0.10500000149011612]}
         325 +{"seed": 324, "success": true, "steps": 85, "seconds": 1.35, "phase": "place", "task": "target_block", "robot": [1.5161854028701782, 0.4976927936077118], "taskxy": [1.4886822700500488, 0.11283627152442932], "dest": [1.4886822957992554, 0.10500000149011612]}
         326 +{"seed": 325, "success": true, "steps": 24, "seconds": 0.59, "phase": "place", "task": "target_block", "robot": [0.7079544067382812, 0.4277730882167816], "taskxy": [0.6459163427352905, 0.10500003397464752], "dest": [0.6459165107011795, 0.10500000149011612]}
         327 +{"seed": 326, "success": true, "steps": 51, "seconds": 0.89, "phase": "place", "task": "target_block", "robot": [0.679954469203949, 0.4549325704574585], "taskxy": [0.6208027601242065, 0.10500005632638931], "dest": [0.6208028237819672, 0.10500000149011612]}
         328 +{"seed": 327, "success": true, "steps": 37, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [0.9083619117736816, 0.4701760709285736], "taskxy": [0.8197245001792908, 0.10500001162290573], "dest": [0.8197245259284973, 0.10500000149011612]}
         329 +{"seed": 328, "success": true, "steps": 19, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [0.9248197674751282, 0.5060813426971436], "taskxy": [0.8653136491775513, 0.10499997437000275], "dest": [0.8653137351870537, 0.10500000149011612]}
         330 +{"seed": 329, "success": true, "steps": 60, "seconds": 1.08, "phase": "place", "task": "target_block", "robot": [0.4428423047065735, 0.5171633362770081], "taskxy": [0.36773353815078735, 0.10499998182058334], "dest": [0.3677335374355316, 0.10500000149011612]}
         331 +{"seed": 330, "success": true, "steps": 63, "seconds": 0.98, "phase": "place", "task": "target_block", "robot": [0.24568280577659607, 0.39871105551719666], "taskxy": [0.20743128657341003, 0.1108492836356163], "dest": [0.20743132042884826, 0.10500000149011612]}
         332 +{"seed": 331, "success": true, "steps": 21, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [0.3515564501285553, 0.4785922169685364], "taskxy": [0.2664845883846283, 0.10499999672174454], "dest": [0.2664846520423889, 0.10500000149011612]}
         333 +{"seed": 332, "success": true, "steps": 51, "seconds": 0.93, "phase": "place", "task": "target_block", "robot": [1.1005175113677979, 0.48815393447875977], "taskxy": [1.0080640316009521, 0.10500002652406693], "dest": [1.0080640058517456, 0.10500000149011612]}
         334 +{"seed": 333, "success": true, "steps": 17, "seconds": 0.24, "phase": "place", "task": "target_block", "robot": [1.3470020294189453, 0.4571966528892517], "taskxy": [1.2630146741867065, 0.10499996691942215], "dest": [1.263014699935913, 0.10500000149011612]}
         335 +{"seed": 334, "success": true, "steps": 25, "seconds": 0.43, "phase": "place", "task": "target_block", "robot": [0.2698429822921753, 0.5192652940750122], "taskxy": [0.2011958360671997, 0.10499993711709976], "dest": [0.20119589495658874, 0.10500000149011612]}
         336 +{"seed": 335, "success": true, "steps": 24, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [0.3087906539440155, 0.4325958490371704], "taskxy": [0.25951245427131653, 0.10500000417232513], "dest": [0.25951251047849655, 0.10500000149011612]}
         337 +{"seed": 336, "success": true, "steps": 60, "seconds": 1.14, "phase": "place", "task": "target_block", "robot": [0.593471884727478, 0.3760586380958557], "taskxy": [0.5204938054084778, 0.10500002652406693], "dest": [0.5204938311576843, 0.10500000149011612]}
         338 +{"seed": 337, "success": true, "steps": 58, "seconds": 1.13, "phase": "place", "task": "target_block", "robot": [0.3567903935909271, 0.5025011301040649], "taskxy": [0.2657935619354248, 0.10499998182058334], "dest": [0.26579353618621826, 0.10500000149011612]}
         339 +{"seed": 338, "success": true, "steps": 23, "seconds": 0.46, "phase": "place", "task": "target_block", "robot": [1.1712126731872559, 0.37969842553138733], "taskxy": [1.0815516710281372, 0.10499995946884155], "dest": [1.0815515775680542, 0.10500000149011612]}
         340 +{"seed": 339, "success": true, "steps": 36, "seconds": 0.7, "phase": "place", "task": "target_block", "robot": [0.8108395338058472, 0.45180201530456543], "taskxy": [0.7675414681434631, 0.10499997437000275], "dest": [0.767541434943676, 0.10500000149011612]}
         341 +{"seed": 340, "success": true, "steps": 19, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [1.0653239488601685, 0.37675711512565613], "taskxy": [0.9754632115364075, 0.10499999672174454], "dest": [0.9754631857872009, 0.10500000149011612]}
         342 +{"seed": 341, "success": true, "steps": 64, "seconds": 1.57, "phase": "place", "task": "target_block", "robot": [0.33895638585090637, 0.4424559473991394], "taskxy": [0.2740457355976105, 0.12381965667009354], "dest": [0.27404568004608154, 0.10500000149011612]}
         343 +{"seed": 342, "success": true, "steps": 102, "seconds": 1.88, "phase": "place", "task": "target_block", "robot": [0.23260343074798584, 0.44649866223335266], "taskxy": [0.17010417580604553, 0.10499996691942215], "dest": [0.17010415750741958, 0.10500000149011612]}
         344 +{"seed": 343, "success": true, "steps": 29, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [0.21994648873806, 0.39510855078697205], "taskxy": [0.17516948282718658, 0.10499999672174454], "dest": [0.17516949433088302, 0.10500000149011612]}
         345 +{"seed": 344, "success": true, "steps": 30, "seconds": 0.46, "phase": "place", "task": "target_block", "robot": [1.3018486499786377, 0.4015492796897888], "taskxy": [1.2444266080856323, 0.10500002652406693], "dest": [1.2444265146255493, 0.10500000149011612]}
         346 +{"seed": 345, "success": true, "steps": 34, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [1.0308574438095093, 0.47729840874671936], "taskxy": [1.0037689208984375, 0.10499998182058334], "dest": [1.003768946647644, 0.10500000149011612]}
         347 +{"seed": 346, "success": true, "steps": 84, "seconds": 1.42, "phase": "place", "task": "target_block", "robot": [1.3004465103149414, 0.5165852904319763], "taskxy": [1.227562427520752, 0.1105671152472496], "dest": [1.2275624532699585, 0.10500000149011612]}
         348 +{"seed": 347, "success": true, "steps": 47, "seconds": 0.85, "phase": "place", "task": "target_block", "robot": [0.5847686529159546, 0.3913727104663849], "taskxy": [0.5332256555557251, 0.10500001162290573], "dest": [0.5332256217002869, 0.10500000149011612]}
         349 +{"seed": 348, "success": true, "steps": 30, "seconds": 0.41, "phase": "place", "task": "target_block", "robot": [0.6970056295394897, 0.495936781167984], "taskxy": [0.6259429454803467, 0.10499998927116394], "dest": [0.6259429346323013, 0.10500000149011612]}
         350 +{"seed": 349, "success": true, "steps": 42, "seconds": 0.88, "phase": "place", "task": "target_block", "robot": [0.4264829754829407, 0.4354375898838043], "taskxy": [0.33469945192337036, 0.1166950985789299], "dest": [0.33469941806793213, 0.10500000149011612]}
         351 +{"seed": 350, "success": true, "steps": 41, "seconds": 0.65, "phase": "place", "task": "target_block", "robot": [1.2051740884780884, 0.3707767724990845], "taskxy": [1.1500869989395142, 0.10499998927116394], "dest": [1.1500871438980103, 0.10500000149011612]}
         352 +{"seed": 351, "success": true, "steps": 69, "seconds": 1.16, "phase": "place", "task": "target_block", "robot": [0.2357281744480133, 0.5022150874137878], "taskxy": [0.19747120141983032, 0.12300948798656464], "dest": [0.19747116822004318, 0.10500000149011612]}
         353 +{"seed": 352, "success": true, "steps": 38, "seconds": 0.55, "phase": "place", "task": "target_block", "robot": [0.29718780517578125, 0.46765515208244324], "taskxy": [0.20680366456508636, 0.10500004887580872], "dest": [0.2068036686182022, 0.10500000149011612]}
         354 +{"seed": 353, "success": true, "steps": 28, "seconds": 0.41, "phase": "place", "task": "target_block", "robot": [0.4751857817173004, 0.507877767086029], "taskxy": [0.4493483006954193, 0.10500001907348633], "dest": [0.449348252594471, 0.10500000149011612]}
         355 +{"seed": 354, "success": true, "steps": 110, "seconds": 2.17, "phase": "place", "task": "target_block", "robot": [1.2424330711364746, 0.46840062737464905], "taskxy": [1.1681216955184937, 0.10499995946884155], "dest": [1.1681217212677002, 0.10500000149011612]}
         356 +{"seed": 355, "success": true, "steps": 32, "seconds": 0.49, "phase": "place", "task": "target_block", "robot": [1.3716999292373657, 0.379412978887558], "taskxy": [1.3339169025421143, 0.10500000417232513], "dest": [1.3339169282913208, 0.10500000149011612]}
         357 +{"seed": 356, "success": true, "steps": 31, "seconds": 0.48, "phase": "place", "task": "target_block", "robot": [1.2542973756790161, 0.38310545682907104], "taskxy": [1.1752009391784668, 0.10499998927116394], "dest": [1.1752009649276733, 0.10500000149011612]}
         358 +{"seed": 357, "success": true, "steps": 78, "seconds": 1.39, "phase": "place", "task": "target_block", "robot": [0.33164840936660767, 0.39807894825935364], "taskxy": [0.3289630115032196, 0.10499999672174454], "dest": [0.32896299320459366, 0.10500000149011612]}
         359 +{"seed": 358, "success": true, "steps": 55, "seconds": 1.24, "phase": "place", "task": "target_block", "robot": [1.4205483198165894, 0.4915751814842224], "taskxy": [1.3926466703414917, 0.11047805100679398], "dest": [1.3926466561555861, 0.10500000149011612]}
         360 +{"seed": 359, "success": true, "steps": 48, "seconds": 0.89, "phase": "place", "task": "target_block", "robot": [1.3084410429000854, 0.43355727195739746], "taskxy": [1.2634875774383545, 0.10500001907348633], "dest": [1.2634876112937927, 0.10500000149011612]}
         361 +{"seed": 360, "success": true, "steps": 67, "seconds": 1.46, "phase": "place", "task": "target_block", "robot": [0.38614264130592346, 0.4415320158004761], "taskxy": [0.3402904272079468, 0.11436126381158829], "dest": [0.3402904786467552, 0.10500000149011612]}
         362 +{"seed": 361, "success": true, "steps": 83, "seconds": 1.51, "phase": "place", "task": "target_block", "robot": [0.758104145526886, 0.4106520116329193], "taskxy": [0.7003187537193298, 0.10499998927116394], "dest": [0.7003187198638916, 0.10500000149011612]}
         363 +{"seed": 362, "success": true, "steps": 88, "seconds": 1.62, "phase": "place", "task": "target_block", "robot": [0.871920645236969, 0.3759082853794098], "taskxy": [0.7871592044830322, 0.10500001907348633], "dest": [0.7871591489315033, 0.10500000149011612]}
         364 +{"seed": 363, "success": true, "steps": 45, "seconds": 0.74, "phase": "place", "task": "target_block", "robot": [1.1427360773086548, 0.5140930414199829], "taskxy": [1.0492112636566162, 0.10500000417232513], "dest": [1.0492112894058228, 0.10500000149011612]}
         365 +{"seed": 364, "success": true, "steps": 33, "seconds": 0.73, "phase": "place", "task": "target_block", "robot": [0.9731898903846741, 0.40359964966773987], "taskxy": [0.9161137938499451, 0.10499998182058334], "dest": [0.9161137796640396, 0.10500000149011612]}
         366 +{"seed": 365, "success": true, "steps": 43, "seconds": 0.84, "phase": "place", "task": "target_block", "robot": [1.427925705909729, 0.3862181603908539], "taskxy": [1.3494309186935425, 0.10499999672174454], "dest": [1.349430944442749, 0.10500000149011612]}
         367 +{"seed": 366, "success": true, "steps": 23, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [0.75588458776474, 0.5059382915496826], "taskxy": [0.6691274642944336, 0.10500000417232513], "dest": [0.669127438545227, 0.10500000149011612]}
         368 +{"seed": 367, "success": true, "steps": 109, "seconds": 2.26, "phase": "place", "task": "target_block", "robot": [1.3824125528335571, 0.43518954515457153], "taskxy": [1.2946926355361938, 0.10499998182058334], "dest": [1.2946926612854004, 0.10500000149011612]}
         369 +{"seed": 368, "success": true, "steps": 89, "seconds": 2.05, "phase": "place", "task": "target_block", "robot": [1.184515357017517, 0.5208714604377747], "taskxy": [1.1053075790405273, 0.10933549702167511], "dest": [1.1053074855804443, 0.10500000149011612]}
         370 +{"seed": 369, "success": true, "steps": 127, "seconds": 2.29, "phase": "place", "task": "target_block", "robot": [1.1377696990966797, 0.5025933980941772], "taskxy": [1.0438092947006226, 0.10500003397464752], "dest": [1.043809320449829, 0.10500000149011612]}
         371 +{"seed": 370, "success": true, "steps": 63, "seconds": 1.16, "phase": "place", "task": "target_block", "robot": [1.3422964811325073, 0.4813326597213745], "taskxy": [1.2666141986846924, 0.10500004142522812], "dest": [1.266614224433899, 0.10500000149011612]}
         372 +{"seed": 371, "success": true, "steps": 22, "seconds": 0.58, "phase": "place", "task": "target_block", "robot": [0.7827033400535583, 0.45050060749053955], "taskxy": [0.7195940017700195, 0.12096451222896576], "dest": [0.7195939909219742, 0.10500000149011612]}
         373 +{"seed": 372, "success": true, "steps": 82, "seconds": 1.72, "phase": "place", "task": "target_block", "robot": [1.460059404373169, 0.38847801089286804], "taskxy": [1.40603768825531, 0.11001753807067871], "dest": [1.4060377140045166, 0.10500000149011612]}
         374 +{"seed": 373, "success": true, "steps": 60, "seconds": 1.02, "phase": "place", "task": "target_block", "robot": [0.5808458924293518, 0.48446857929229736], "taskxy": [0.5003811717033386, 0.10500000417232513], "dest": [0.5003811676502228, 0.10500000149011612]}
         375 +{"seed": 374, "success": true, "steps": 53, "seconds": 1.01, "phase": "place", "task": "target_block", "robot": [0.4415781497955322, 0.4806370437145233], "taskxy": [0.34783169627189636, 0.12402693182229996], "dest": [0.347831685423851, 0.10500000149011612]}
         376 +{"seed": 375, "success": true, "steps": 30, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [0.6132702827453613, 0.5169162154197693], "taskxy": [0.5731595158576965, 0.10500000417232513], "dest": [0.5731595416069031, 0.10500000149011612]}
         377 +{"seed": 376, "success": true, "steps": 64, "seconds": 1.0, "phase": "place", "task": "target_block", "robot": [0.9628843069076538, 0.38385018706321716], "taskxy": [0.9230465888977051, 0.10500001907348633], "dest": [0.9230465550422668, 0.10500000149011612]}
         378 +{"seed": 377, "success": true, "steps": 75, "seconds": 1.16, "phase": "place", "task": "target_block", "robot": [0.7124477624893188, 0.4406503736972809], "taskxy": [0.6667979955673218, 0.11341925710439682], "dest": [0.6667979996204376, 0.10500000149011612]}
         379 +{"seed": 378, "success": true, "steps": 84, "seconds": 1.55, "phase": "place", "task": "target_block", "robot": [1.3206766843795776, 0.40776166319847107], "taskxy": [1.275036096572876, 0.10500001907348633], "dest": [1.275036003112793, 0.10500000149011612]}
         380 +{"seed": 379, "success": true, "steps": 54, "seconds": 1.0, "phase": "place", "task": "target_block", "robot": [0.5351548194885254, 0.47113144397735596], "taskxy": [0.44198372960090637, 0.11352303624153137], "dest": [0.4419838480949402, 0.10500000149011612]}
         381 +{"seed": 380, "success": true, "steps": 60, "seconds": 1.21, "phase": "place", "task": "target_block", "robot": [1.1052097082138062, 0.3802589476108551], "taskxy": [1.0409190654754639, 0.10500001907348633], "dest": [1.040919084429741, 0.10500000149011612]}
         382 +{"seed": 381, "success": true, "steps": 85, "seconds": 1.8, "phase": "place", "task": "target_block", "robot": [0.2104431390762329, 0.4087058901786804], "taskxy": [0.1830083131790161, 0.11988488584756851], "dest": [0.18300830605626106, 0.10500000149011612]}
         383 +{"seed": 382, "success": true, "steps": 45, "seconds": 0.85, "phase": "place", "task": "target_block", "robot": [0.3416171967983246, 0.5069057941436768], "taskxy": [0.3064669668674469, 0.10500006377696991], "dest": [0.30646691131591797, 0.10500000149011612]}
         384 +{"seed": 383, "success": true, "steps": 37, "seconds": 0.62, "phase": "place", "task": "target_block", "robot": [0.9091926217079163, 0.4223421812057495], "taskxy": [0.8700602650642395, 0.10500001907348633], "dest": [0.8700603659749031, 0.10500000149011612]}
         385 +{"seed": 384, "success": true, "steps": 39, "seconds": 0.58, "phase": "place", "task": "target_block", "robot": [0.40793582797050476, 0.44103580713272095], "taskxy": [0.381402850151062, 0.10499998927116394], "dest": [0.38140282067656517, 0.10500000149011612]}
         386 +{"seed": 385, "success": true, "steps": 91, "seconds": 1.81, "phase": "place", "task": "target_block", "robot": [0.2980060279369354, 0.4906361997127533], "taskxy": [0.24873575568199158, 0.11284453421831131], "dest": [0.24873575228452682, 0.10500000149011612]}
         387 +{"seed": 386, "success": true, "steps": 54, "seconds": 0.93, "phase": "place", "task": "target_block", "robot": [0.8682867288589478, 0.4277825355529785], "taskxy": [0.786916971206665, 0.10500002652406693], "dest": [0.7869169901609421, 0.10500000149011612]}
         388 +{"seed": 387, "success": true, "steps": 63, "seconds": 1.22, "phase": "place", "task": "target_block", "robot": [0.7617766261100769, 0.4269392192363739], "taskxy": [0.6695500612258911, 0.10499999672174454], "dest": [0.6695501546859741, 0.10500000149011612]}
         389 +{"seed": 388, "success": true, "steps": 44, "seconds": 0.79, "phase": "place", "task": "target_block", "robot": [0.6219068169593811, 0.37798938155174255], "taskxy": [0.5424971580505371, 0.10500000417232513], "dest": [0.5424971241950989, 0.10500000149011612]}
         390 +{"seed": 389, "success": true, "steps": 31, "seconds": 0.55, "phase": "place", "task": "target_block", "robot": [0.9091193675994873, 0.4860785901546478], "taskxy": [0.8831784129142761, 0.10500003397464752], "dest": [0.8831784951984882, 0.10500000149011612]}
         391 +{"seed": 390, "success": true, "steps": 67, "seconds": 1.24, "phase": "place", "task": "target_block", "robot": [0.29385292530059814, 0.42617490887641907], "taskxy": [0.20449846982955933, 0.10500002652406693], "dest": [0.20449851858615875, 0.10500000149011612]}
         392 +{"seed": 391, "success": true, "steps": 41, "seconds": 0.65, "phase": "place", "task": "target_block", "robot": [0.8823307752609253, 0.44626227021217346], "taskxy": [0.8134671449661255, 0.10500001162290573], "dest": [0.8134671639204025, 0.10500000149011612]}
         393 +{"seed": 392, "success": true, "steps": 29, "seconds": 0.36, "phase": "place", "task": "target_block", "robot": [0.37955033779144287, 0.40338778495788574], "taskxy": [0.3851921558380127, 0.10500001907348633], "dest": [0.3851922113895416, 0.10500000149011612]}
         394 +{"seed": 393, "success": true, "steps": 22, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.8473110198974609, 0.4641478955745697], "taskxy": [0.7964699268341064, 0.10499998927116394], "dest": [0.7964699234366417, 0.10500000149011612]}
         395 +{"seed": 394, "success": true, "steps": 19, "seconds": 0.16, "phase": "place", "task": "target_block", "robot": [1.2903192043304443, 0.3718622028827667], "taskxy": [1.2496579885482788, 0.10500000417232513], "dest": [1.2496580142974854, 0.10500000149011612]}
         396 +{"seed": 395, "success": true, "steps": 46, "seconds": 0.55, "phase": "place", "task": "target_block", "robot": [1.0701255798339844, 0.3965071737766266], "taskxy": [1.0085679292678833, 0.11658960580825806], "dest": [1.0085678358078003, 0.10500000149011612]}
         397 +{"seed": 396, "success": true, "steps": 83, "seconds": 0.81, "phase": "place", "task": "target_block", "robot": [1.44350266456604, 0.44291046261787415], "taskxy": [1.3997094631195068, 0.12397567927837372], "dest": [1.3997094888687134, 0.10500000149011612]}
         398 +{"seed": 397, "success": true, "steps": 62, "seconds": 0.69, "phase": "place", "task": "target_block", "robot": [0.8939307332038879, 0.5264719724655151], "taskxy": [0.8469716310501099, 0.12366519123315811], "dest": [0.8469716567993164, 0.10500000149011612]}
         399 +{"seed": 398, "success": true, "steps": 70, "seconds": 0.98, "phase": "place", "task": "target_block", "robot": [1.1266947984695435, 0.4345459043979645], "taskxy": [1.0583786964416504, 0.10499999672174454], "dest": [1.058378685593605, 0.10500000149011612]}
         400 +{"seed": 399, "success": true, "steps": 89, "seconds": 1.02, "phase": "place", "task": "target_block", "robot": [1.0748831033706665, 0.45899903774261475], "taskxy": [1.018007755279541, 0.12111495435237885], "dest": [1.0180077810287476, 0.10500000149011612]}
         401 +{"seed": 400, "success": true, "steps": 80, "seconds": 1.17, "phase": "place", "task": "target_block", "robot": [1.3494116067886353, 0.4367658793926239], "taskxy": [1.2923473119735718, 0.11767960339784622], "dest": [1.2923473377227783, 0.10500000149011612]}
         402 +{"seed": 401, "success": true, "steps": 54, "seconds": 0.53, "phase": "place", "task": "target_block", "robot": [0.9968143701553345, 0.4953349828720093], "taskxy": [0.9094895720481873, 0.10500001162290573], "dest": [0.9094894866943359, 0.10500000149011612]}
         403 +{"seed": 402, "success": true, "steps": 106, "seconds": 1.33, "phase": "place", "task": "target_block", "robot": [0.253762423992157, 0.4841252863407135], "taskxy": [0.18817053735256195, 0.10500003397464752], "dest": [0.18817048180103302, 0.10500000149011612]}
         404 +{"seed": 403, "success": true, "steps": 32, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [1.2087756395339966, 0.500328540802002], "taskxy": [1.1544866561889648, 0.11895236372947693], "dest": [1.1544865627288818, 0.10500000149011612]}
         405 +{"seed": 404, "success": true, "steps": 59, "seconds": 0.64, "phase": "place", "task": "target_block", "robot": [1.2266795635223389, 0.45367899537086487], "taskxy": [1.1836053133010864, 0.10499997437000275], "dest": [1.183605339050293, 0.10500000149011612]}
         406 +{"seed": 405, "success": true, "steps": 39, "seconds": 0.49, "phase": "place", "task": "target_block", "robot": [0.30883678793907166, 0.4528471529483795], "taskxy": [0.2701936960220337, 0.10500004887580872], "dest": [0.27019365060329437, 0.10500000149011612]}
         407 +{"seed": 406, "success": true, "steps": 64, "seconds": 0.83, "phase": "place", "task": "target_block", "robot": [1.0068821907043457, 0.3727278709411621], "taskxy": [0.9335246086120605, 0.10508127510547638], "dest": [0.9335246343612671, 0.10500000149011612]}
         408 +{"seed": 407, "success": true, "steps": 27, "seconds": 0.22, "phase": "place", "task": "target_block", "robot": [0.49152159690856934, 0.49523210525512695], "taskxy": [0.4177647531032562, 0.10499998927116394], "dest": [0.41776478695869446, 0.10500000149011612]}
         409 +{"seed": 408, "success": true, "steps": 23, "seconds": 0.2, "phase": "place", "task": "target_block", "robot": [1.4128938913345337, 0.38593870401382446], "taskxy": [1.343496561050415, 0.10500001907348633], "dest": [1.3434965867996216, 0.10500000149011612]}
         410 +{"seed": 409, "success": true, "steps": 34, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [0.9631755948066711, 0.5181084275245667], "taskxy": [0.9129406213760376, 0.10500001907348633], "dest": [0.9129405658245087, 0.10500000149011612]}
         411 +{"seed": 410, "success": true, "steps": 56, "seconds": 0.53, "phase": "place", "task": "target_block", "robot": [1.2863386869430542, 0.43366652727127075], "taskxy": [1.1997352838516235, 0.10500000417232513], "dest": [1.19973530960083, 0.10500000149011612]}
         412 +{"seed": 411, "success": true, "steps": 29, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [1.237841010093689, 0.5195780396461487], "taskxy": [1.1543883085250854, 0.10499998927116394], "dest": [1.1543883870840073, 0.10500000149011612]}
         413 +{"seed": 412, "success": true, "steps": 69, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [0.4053456783294678, 0.5344061851501465], "taskxy": [0.3477521538734436, 0.12107758224010468], "dest": [0.3477520861029625, 0.10500000149011612]}
         414 +{"seed": 413, "success": true, "steps": 26, "seconds": 0.19, "phase": "place", "task": "target_block", "robot": [0.6949586868286133, 0.40080904960632324], "taskxy": [0.6593862175941467, 0.10500000417232513], "dest": [0.6593862433433533, 0.10500000149011612]}
         415 +{"seed": 414, "success": true, "steps": 59, "seconds": 0.54, "phase": "place", "task": "target_block", "robot": [0.7871450781822205, 0.4083190858364105], "taskxy": [0.7129248380661011, 0.10500001907348633], "dest": [0.7129248719215393, 0.10500000149011612]}
         416 +{"seed": 415, "success": true, "steps": 67, "seconds": 0.54, "phase": "place", "task": "target_block", "robot": [1.3313018083572388, 0.5228032469749451], "taskxy": [1.2546221017837524, 0.12117548286914825], "dest": [1.254622127532959, 0.10500000149011612]}
         417 +{"seed": 416, "success": true, "steps": 51, "seconds": 0.47, "phase": "place", "task": "target_block", "robot": [0.5655575394630432, 0.4945884644985199], "taskxy": [0.506436288356781, 0.1127014309167862], "dest": [0.5064363222122192, 0.10500000149011612]}
         418 +{"seed": 417, "success": true, "steps": 28, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [0.4717937409877777, 0.4889780580997467], "taskxy": [0.37312066555023193, 0.10500003397464752], "dest": [0.3731206547021866, 0.10500000149011612]}
         419 +{"seed": 418, "success": true, "steps": 21, "seconds": 0.14, "phase": "place", "task": "target_block", "robot": [0.3014752268791199, 0.5110159516334534], "taskxy": [0.22236640751361847, 0.10499999672174454], "dest": [0.2223664562702179, 0.10500000149011612]}
         420 +{"seed": 419, "success": true, "steps": 28, "seconds": 0.22, "phase": "place", "task": "target_block", "robot": [0.5558981895446777, 0.48906293511390686], "taskxy": [0.516122579574585, 0.12022484838962555], "dest": [0.5161226310133934, 0.10500000149011612]}
         421 +{"seed": 420, "success": true, "steps": 48, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [1.001685380935669, 0.4446401000022888], "taskxy": [0.9752458930015564, 0.10499998927116394], "dest": [0.9752458591461182, 0.10500000149011612]}
         422 +{"seed": 421, "success": true, "steps": 42, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.7292650938034058, 0.5070088505744934], "taskxy": [0.6377013325691223, 0.10499999672174454], "dest": [0.6377012621164322, 0.10500000149011612]}
         423 +{"seed": 422, "success": true, "steps": 33, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [1.217798113822937, 0.4862259030342102], "taskxy": [1.185156226158142, 0.10500003397464752], "dest": [1.185156132698059, 0.10500000149011612]}
         424 +{"seed": 423, "success": true, "steps": 34, "seconds": 0.28, "phase": "place", "task": "target_block", "robot": [0.25383251905441284, 0.5234514474868774], "taskxy": [0.2037721574306488, 0.11951478570699692], "dest": [0.20377211645245552, 0.10500000149011612]}
         425 +{"seed": 424, "success": true, "steps": 21, "seconds": 0.15, "phase": "place", "task": "target_block", "robot": [0.8263399004936218, 0.39102283120155334], "taskxy": [0.733396589756012, 0.10500001907348633], "dest": [0.733396534204483, 0.10500000149011612]}
         426 +{"seed": 425, "success": true, "steps": 31, "seconds": 0.23, "phase": "place", "task": "target_block", "robot": [1.087266445159912, 0.473366916179657], "taskxy": [1.0078121423721313, 0.10499998927116394], "dest": [1.0078121017217636, 0.10500000149011612]}
         427 +{"seed": 426, "success": true, "steps": 23, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [1.1259394884109497, 0.48864489793777466], "taskxy": [1.058435082435608, 0.10499996691942215], "dest": [1.058434988975525, 0.10500000149011612]}
         428 +{"seed": 427, "success": true, "steps": 52, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [1.17287015914917, 0.4519144296646118], "taskxy": [1.1356996297836304, 0.11824394762516022], "dest": [1.1356995363235474, 0.10500000149011612]}
         429 +{"seed": 428, "success": true, "steps": 27, "seconds": 0.21, "phase": "place", "task": "target_block", "robot": [1.1063965559005737, 0.38594019412994385], "taskxy": [1.0149589776992798, 0.10500001162290573], "dest": [1.0149590034484863, 0.10500000149011612]}
         430 +{"seed": 429, "success": true, "steps": 33, "seconds": 0.22, "phase": "place", "task": "target_block", "robot": [0.8236263394355774, 0.37104350328445435], "taskxy": [0.7275203466415405, 0.10499999672174454], "dest": [0.727520246386528, 0.10500000149011612]}
         431 +{"seed": 430, "success": true, "steps": 30, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [0.5144259333610535, 0.49235424399375916], "taskxy": [0.4787014424800873, 0.10500003397464752], "dest": [0.47870141673088074, 0.10500000149011612]}
         432 +{"seed": 431, "success": true, "steps": 64, "seconds": 0.82, "phase": "place", "task": "target_block", "robot": [0.3616935610771179, 0.49227097630500793], "taskxy": [0.29767850041389465, 0.10499997437000275], "dest": [0.2976784698963165, 0.10500000149011612]}
         433 +{"seed": 432, "success": true, "steps": 27, "seconds": 0.26, "phase": "place", "task": "target_block", "robot": [0.8821484446525574, 0.47395628690719604], "taskxy": [0.8425437211990356, 0.10499996691942215], "dest": [0.8425436873435974, 0.10500000149011612]}
         434 +{"seed": 433, "success": true, "steps": 32, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [0.7844719290733337, 0.45115551352500916], "taskxy": [0.736913800239563, 0.10499999672174454], "dest": [0.7369138638973236, 0.10500000149011612]}
         435 +{"seed": 434, "success": true, "steps": 28, "seconds": 0.3, "phase": "place", "task": "target_block", "robot": [1.186089038848877, 0.43385955691337585], "taskxy": [1.1440720558166504, 0.10500002652406693], "dest": [1.1440721384882926, 0.10500000149011612]}
         436 +{"seed": 435, "success": true, "steps": 52, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [0.7736154198646545, 0.46176329255104065], "taskxy": [0.6938204765319824, 0.10499995946884155], "dest": [0.6938204507827759, 0.10500000149011612]}
         437 +{"seed": 436, "success": true, "steps": 80, "seconds": 0.92, "phase": "place", "task": "target_block", "robot": [0.5325717329978943, 0.5030574202537537], "taskxy": [0.45083415508270264, 0.10499998927116394], "dest": [0.4508340995311737, 0.10500000149011612]}
         438 +{"seed": 437, "success": true, "steps": 61, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [0.6703659892082214, 0.4291155934333801], "taskxy": [0.5936304926872253, 0.10499997437000275], "dest": [0.5936303924322128, 0.10500000149011612]}
         439 +{"seed": 438, "success": true, "steps": 49, "seconds": 0.63, "phase": "place", "task": "target_block", "robot": [0.6167633533477783, 0.41034695506095886], "taskxy": [0.5296130776405334, 0.11369764804840088], "dest": [0.5296130518913269, 0.10500000149011612]}
         440 +{"seed": 439, "success": true, "steps": 35, "seconds": 0.33, "phase": "place", "task": "target_block", "robot": [0.27133920788764954, 0.4646720290184021], "taskxy": [0.2251255214214325, 0.10500003397464752], "dest": [0.22512545096874237, 0.10500000149011612]}
         441 +{"seed": 440, "success": true, "steps": 21, "seconds": 0.2, "phase": "place", "task": "target_block", "robot": [0.9498898386955261, 0.48621052503585815], "taskxy": [0.9097335338592529, 0.10499999672174454], "dest": [0.9097336124181747, 0.10500000149011612]}
         442 +{"seed": 441, "success": true, "steps": 72, "seconds": 1.31, "phase": "place", "task": "target_block", "robot": [0.6751701831817627, 0.3700801432132721], "taskxy": [0.5988635420799255, 0.10500001162290573], "dest": [0.598863516330719, 0.10500000149011612]}
         443 +{"seed": 442, "success": true, "steps": 20, "seconds": 0.42, "phase": "place", "task": "target_block", "robot": [0.7107297778129578, 0.5182258486747742], "taskxy": [0.6200562119483948, 0.10499998927116394], "dest": [0.6200561780929565, 0.10500000149011612]}
         444 +{"seed": 443, "success": true, "steps": 38, "seconds": 0.67, "phase": "place", "task": "target_block", "robot": [0.9791145920753479, 0.49072137475013733], "taskxy": [0.920532763004303, 0.10499998182058334], "dest": [0.9205327521562576, 0.10500000149011612]}
         445 +{"seed": 444, "success": true, "steps": 57, "seconds": 0.79, "phase": "place", "task": "target_block", "robot": [1.193660020828247, 0.49643847346305847], "taskxy": [1.165687918663025, 0.10500003397464752], "dest": [1.1656879444122314, 0.10500000149011612]}
         446 +{"seed": 445, "success": true, "steps": 27, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.2536788880825043, 0.49387258291244507], "taskxy": [0.15729795396327972, 0.10499999672174454], "dest": [0.15729798036813736, 0.10500000149011612]}
         447 +{"seed": 446, "success": true, "steps": 50, "seconds": 0.71, "phase": "place", "task": "target_block", "robot": [1.4527028799057007, 0.3832665681838989], "taskxy": [1.391485571861267, 0.10499998182058334], "dest": [1.3914855976104736, 0.10500000149011612]}
         448 +{"seed": 447, "success": true, "steps": 57, "seconds": 1.03, "phase": "place", "task": "target_block", "robot": [0.5465806126594543, 0.5314117074012756], "taskxy": [0.45502421259880066, 0.11707635223865509], "dest": [0.4550241570472717, 0.10500000149011612]}
         449 +{"seed": 448, "success": true, "steps": 60, "seconds": 1.05, "phase": "place", "task": "target_block", "robot": [0.6048207879066467, 0.5303805470466614], "taskxy": [0.5620731115341187, 0.12405738234519958], "dest": [0.562073104083538, 0.10500000149011612]}
         450 +{"seed": 449, "success": true, "steps": 71, "seconds": 1.48, "phase": "place", "task": "target_block", "robot": [1.0442818403244019, 0.45916974544525146], "taskxy": [1.0044156312942505, 0.12462929636240005], "dest": [1.004415612667799, 0.10500000149011612]}
         451 +{"seed": 450, "success": true, "steps": 29, "seconds": 0.5, "phase": "place", "task": "target_block", "robot": [0.9787688255310059, 0.4080934524536133], "taskxy": [0.8863322138786316, 0.10500001907348633], "dest": [0.8863321800231934, 0.10500000149011612]}
         452 +{"seed": 451, "success": true, "steps": 19, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [0.5027430653572083, 0.43735384941101074], "taskxy": [0.4087274372577667, 0.10499996691942215], "dest": [0.40872748601436615, 0.10500000149011612]}
         453 +{"seed": 452, "success": true, "steps": 37, "seconds": 0.81, "phase": "place", "task": "target_block", "robot": [0.21862415969371796, 0.41991791129112244], "taskxy": [0.17620809376239777, 0.10500002652406693], "dest": [0.176208130300045, 0.10500000149011612]}
         454 +{"seed": 453, "success": true, "steps": 92, "seconds": 1.63, "phase": "place", "task": "target_block", "robot": [1.1940276622772217, 0.45344531536102295], "taskxy": [1.1342824697494507, 0.10500002652406693], "dest": [1.1342824954986572, 0.10500000149011612]}
         455 +{"seed": 454, "success": true, "steps": 40, "seconds": 0.58, "phase": "place", "task": "target_block", "robot": [0.14672353863716125, 0.5158683657646179], "taskxy": [0.1035240963101387, 0.10499998927116394], "dest": [0.10352412539720535, 0.10500000149011612]}
         456 +{"seed": 455, "success": true, "steps": 71, "seconds": 1.65, "phase": "place", "task": "target_block", "robot": [0.5873875021934509, 0.3734879493713379], "taskxy": [0.4961259663105011, 0.10499996691942215], "dest": [0.4961258660554886, 0.10500000149011612]}
         457 +{"seed": 456, "success": true, "steps": 58, "seconds": 1.11, "phase": "place", "task": "target_block", "robot": [0.7513043880462646, 0.4894079267978668], "taskxy": [0.7034813165664673, 0.10500000417232513], "dest": [0.703481231212616, 0.10500000149011612]}
         458 +{"seed": 457, "success": true, "steps": 28, "seconds": 0.35, "phase": "place", "task": "target_block", "robot": [1.2092502117156982, 0.47740495204925537], "taskxy": [1.143894076347351, 0.10500001907348633], "dest": [1.1438941020965576, 0.10500000149011612]}
         459 +{"seed": 458, "success": true, "steps": 42, "seconds": 0.87, "phase": "place", "task": "target_block", "robot": [1.3543760776519775, 0.4380762577056885], "taskxy": [1.258226990699768, 0.10500000417232513], "dest": [1.2582270164489746, 0.10500000149011612]}
         460 +{"seed": 459, "success": true, "steps": 51, "seconds": 0.77, "phase": "place", "task": "target_block", "robot": [0.8949966430664062, 0.4358721673488617], "taskxy": [0.8042349815368652, 0.10499998927116394], "dest": [0.8042350072860718, 0.10500000149011612]}
         461 +{"seed": 460, "success": true, "steps": 31, "seconds": 0.53, "phase": "place", "task": "target_block", "robot": [0.4915502369403839, 0.39837050437927246], "taskxy": [0.45702847838401794, 0.10499999672174454], "dest": [0.4570284526348114, 0.10500000149011612]}
         462 +{"seed": 461, "success": true, "steps": 36, "seconds": 0.52, "phase": "place", "task": "target_block", "robot": [0.7984176278114319, 0.4007566571235657], "taskxy": [0.7274772524833679, 0.10924255847930908], "dest": [0.7274772416353226, 0.10500000149011612]}
         463 +{"seed": 462, "success": true, "steps": 75, "seconds": 1.33, "phase": "place", "task": "target_block", "robot": [1.119032859802246, 0.4206627309322357], "taskxy": [1.0743098258972168, 0.11028961837291718], "dest": [1.0743098516464233, 0.10500000149011612]}
         464 +{"seed": 463, "success": true, "steps": 76, "seconds": 1.4, "phase": "place", "task": "target_block", "robot": [0.5828627347946167, 0.3752358853816986], "taskxy": [0.48847901821136475, 0.10999319702386856], "dest": [0.4884790222644806, 0.10500000149011612]}
         465 +{"seed": 464, "success": true, "steps": 24, "seconds": 0.32, "phase": "place", "task": "target_block", "robot": [0.5552369356155396, 0.4998384118080139], "taskxy": [0.4698141813278198, 0.10500002652406693], "dest": [0.46981420707702637, 0.10500000149011612]}
         466 +{"seed": 465, "success": true, "steps": 31, "seconds": 0.61, "phase": "place", "task": "target_block", "robot": [0.29272717237472534, 0.41059741377830505], "taskxy": [0.22420108318328857, 0.10500001162290573], "dest": [0.22420102763175964, 0.10500000149011612]}
         467 +{"seed": 466, "success": true, "steps": 76, "seconds": 1.2, "phase": "place", "task": "target_block", "robot": [0.3964116871356964, 0.37440282106399536], "taskxy": [0.33807942271232605, 0.10500002652406693], "dest": [0.33807950127124786, 0.10500000149011612]}
         468 +{"seed": 467, "success": true, "steps": 25, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [0.30594131350517273, 0.435766339302063], "taskxy": [0.22357070446014404, 0.10499996691942215], "dest": [0.2235706936120987, 0.10500000149011612]}
         469 +{"seed": 468, "success": true, "steps": 54, "seconds": 1.12, "phase": "place", "task": "target_block", "robot": [1.4502806663513184, 0.5148032903671265], "taskxy": [1.4242255687713623, 0.10500004887580872], "dest": [1.4242255945205688, 0.10500000149011612]}
         470 +{"seed": 469, "success": true, "steps": 18, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [0.4815669655799866, 0.4449140727519989], "taskxy": [0.3874962329864502, 0.10500003397464752], "dest": [0.38749623703956604, 0.10500000149011612]}
         471 +{"seed": 470, "success": true, "steps": 61, "seconds": 1.02, "phase": "place", "task": "target_block", "robot": [0.9526808857917786, 0.4618937373161316], "taskxy": [0.9055215716362, 0.10500003397464752], "dest": [0.9055215973854065, 0.10500000149011612]}
         472 +{"seed": 471, "success": true, "steps": 32, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [1.1565824747085571, 0.49484726786613464], "taskxy": [1.0802152156829834, 0.10500001162290573], "dest": [1.080215279340744, 0.10500000149011612]}
         473 +{"seed": 472, "success": true, "steps": 35, "seconds": 0.69, "phase": "place", "task": "target_block", "robot": [0.8498849272727966, 0.5100600123405457], "taskxy": [0.8023722767829895, 0.10499998182058334], "dest": [0.8023722429275513, 0.10500000149011612]}
         474 +{"seed": 473, "success": true, "steps": 23, "seconds": 0.34, "phase": "place", "task": "target_block", "robot": [0.5496442914009094, 0.39851030707359314], "taskxy": [0.5143927335739136, 0.10499999672174454], "dest": [0.5143926997184753, 0.10500000149011612]}
         475 +{"seed": 474, "success": true, "steps": 24, "seconds": 0.39, "phase": "place", "task": "target_block", "robot": [0.9430978298187256, 0.5055946707725525], "taskxy": [0.8805963397026062, 0.10500000417232513], "dest": [0.8805963654518127, 0.10500000149011612]}
         476 +{"seed": 475, "success": true, "steps": 78, "seconds": 1.43, "phase": "place", "task": "target_block", "robot": [0.34146833419799805, 0.46245819330215454], "taskxy": [0.2883759140968323, 0.1127057671546936], "dest": [0.2883759554028511, 0.10500000149011612]}
         477 +{"seed": 476, "success": true, "steps": 93, "seconds": 1.64, "phase": "place", "task": "target_block", "robot": [0.951252281665802, 0.39542269706726074], "taskxy": [0.8631830811500549, 0.10500001907348633], "dest": [0.8631830472946167, 0.10500000149011612]}
         478 +{"seed": 477, "success": true, "steps": 63, "seconds": 0.94, "phase": "place", "task": "target_block", "robot": [0.5486372709274292, 0.394290030002594], "taskxy": [0.5080342888832092, 0.10500003397464752], "dest": [0.5080342556834221, 0.10500000149011612]}
         479 +{"seed": 478, "success": true, "steps": 15, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [0.44697853922843933, 0.49700209498405457], "taskxy": [0.3698624074459076, 0.10500003397464752], "dest": [0.36986242640018463, 0.10500000149011612]}
         480 +{"seed": 479, "success": true, "steps": 55, "seconds": 1.1, "phase": "place", "task": "target_block", "robot": [0.5823673009872437, 0.43667325377464294], "taskxy": [0.5469830632209778, 0.11490549892187119], "dest": [0.5469831641316414, 0.10500000149011612]}
         481 +{"seed": 480, "success": true, "steps": 102, "seconds": 2.1, "phase": "place", "task": "target_block", "robot": [1.1354312896728516, 0.49741870164871216], "taskxy": [1.054786205291748, 0.10524564981460571], "dest": [1.054786111831665, 0.10500000149011612]}
         482 +{"seed": 481, "success": true, "steps": 25, "seconds": 0.38, "phase": "place", "task": "target_block", "robot": [1.0390381813049316, 0.45583683252334595], "taskxy": [0.9964914321899414, 0.11204298585653305], "dest": [0.9964915629029274, 0.10500000149011612]}
         483 +{"seed": 482, "success": true, "steps": 22, "seconds": 0.41, "phase": "place", "task": "target_block", "robot": [1.033591389656067, 0.4458504617214203], "taskxy": [0.9904835820198059, 0.10500001907348633], "dest": [0.9904836382269859, 0.10500000149011612]}
         484 +{"seed": 483, "success": true, "steps": 24, "seconds": 0.31, "phase": "place", "task": "target_block", "robot": [0.9906456470489502, 0.3742591440677643], "taskxy": [0.8974855542182922, 0.10499998927116394], "dest": [0.8974855799674988, 0.10500000149011612]}
         485 +{"seed": 484, "success": true, "steps": 88, "seconds": 1.77, "phase": "place", "task": "target_block", "robot": [0.8115697503089905, 0.3781345784664154], "taskxy": [0.7165996432304382, 0.10500000417232513], "dest": [0.716599609375, 0.10500000149011612]}
         486 +{"seed": 485, "success": true, "steps": 40, "seconds": 0.91, "phase": "place", "task": "target_block", "robot": [0.23464356362819672, 0.4472915232181549], "taskxy": [0.20712390542030334, 0.10500001907348633], "dest": [0.2071239162683487, 0.10500000149011612]}
         487 +{"seed": 486, "success": true, "steps": 27, "seconds": 0.29, "phase": "place", "task": "target_block", "robot": [1.0622328519821167, 0.4451289772987366], "taskxy": [0.9689070582389832, 0.1202172264456749], "dest": [0.9689070324897766, 0.10500000149011612]}
         488 +{"seed": 487, "success": true, "steps": 27, "seconds": 0.51, "phase": "place", "task": "target_block", "robot": [0.23724062740802765, 0.48993369936943054], "taskxy": [0.1688162088394165, 0.10500003397464752], "dest": [0.16881622779369354, 0.10500000149011612]}
         489 +{"seed": 488, "success": true, "steps": 135, "seconds": 2.56, "phase": "place", "task": "target_block", "robot": [1.3292651176452637, 0.43845924735069275], "taskxy": [1.233031988143921, 0.10500003397464752], "dest": [1.2330320138931274, 0.10500000149011612]}
         490 +{"seed": 489, "success": true, "steps": 80, "seconds": 1.78, "phase": "place", "task": "target_block", "robot": [0.5909014344215393, 0.40329286456108093], "taskxy": [0.5415055155754089, 0.12436433136463165], "dest": [0.5415054823756218, 0.10500000149011612]}
         491 +{"seed": 490, "success": true, "steps": 70, "seconds": 1.44, "phase": "place", "task": "target_block", "robot": [0.18347446620464325, 0.42899784445762634], "taskxy": [0.12703530490398407, 0.11337000876665115], "dest": [0.12703530150651932, 0.10500000149011612]}
         492 +{"seed": 491, "success": true, "steps": 58, "seconds": 1.13, "phase": "place", "task": "target_block", "robot": [0.8065091967582703, 0.4914292097091675], "taskxy": [0.766475260257721, 0.10499994456768036], "dest": [0.7664752264022827, 0.10500000149011612]}
         493 +{"seed": 492, "success": true, "steps": 77, "seconds": 1.76, "phase": "place", "task": "target_block", "robot": [0.27742788195610046, 0.47477662563323975], "taskxy": [0.22761890292167664, 0.10982654243707657], "dest": [0.22761890697479248, 0.10500000149011612]}
         494 +{"seed": 493, "success": true, "steps": 64, "seconds": 1.42, "phase": "place", "task": "target_block", "robot": [0.927149772644043, 0.47880470752716064], "taskxy": [0.8694081902503967, 0.10499997437000275], "dest": [0.8694080899953842, 0.10500000149011612]}
         495 +{"seed": 494, "success": true, "steps": 51, "seconds": 1.1, "phase": "place", "task": "target_block", "robot": [1.4770275354385376, 0.44332262873649597], "taskxy": [1.384963870048523, 0.10499998927116394], "dest": [1.3849638957977295, 0.10500000149011612]}
         496 +{"seed": 495, "success": true, "steps": 26, "seconds": 0.44, "phase": "place", "task": "target_block", "robot": [0.4699491858482361, 0.44213712215423584], "taskxy": [0.4443826675415039, 0.10500001162290573], "dest": [0.44438272002339363, 0.10500000149011612]}
         497 +{"seed": 496, "success": true, "steps": 31, "seconds": 0.56, "phase": "place", "task": "target_block", "robot": [0.47455039620399475, 0.49521511793136597], "taskxy": [0.4396788775920868, 0.10499997437000275], "dest": [0.4396789263486862, 0.10500000149011612]}
         498 +{"seed": 497, "success": true, "steps": 21, "seconds": 0.4, "phase": "place", "task": "target_block", "robot": [1.2507071495056152, 0.5195919275283813], "taskxy": [1.2033272981643677, 0.10500002652406693], "dest": [1.2033273239135742, 0.10500000149011612]}
         499 +{"seed": 498, "success": true, "steps": 59, "seconds": 1.06, "phase": "place", "task": "target_block", "robot": [1.3294920921325684, 0.48880669474601746], "taskxy": [1.2877061367034912, 0.10500001162290573], "dest": [1.2877061624526978, 0.10500000149011612]}
         500 +{"seed": 499, "success": true, "steps": 111, "seconds": 2.12, "phase": "place", "task": "target_block", "robot": [0.32589974999427795, 0.5357880592346191], "taskxy": [0.24360260367393494, 0.12125337868928909], "dest": [0.2436025630235672, 0.10500000149011612]}
diff --git a/probe_grasp_offsets.py b/probe_grasp_offsets.py
new file mode 100644
index 0000000..44321c3
--- /dev/null
+++ b/probe_grasp_offsets.py
@@ -0,0 +1,17 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +for off in [-.022,-.03,-.035,-.04,-.043,-.045]:
           4 + e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           5 + def step(a):
           6 +  global s
           7 +  s,*_=e.step(np.array(a,dtype=np.float32))
           8 + def move(x,y,v=0):
           9 +  for _ in range(30):
          10 +   rx,ry=s.get(r,'x'),s.get(r,'y')
          11 +   if abs(rx-x)<1e-5 and abs(ry-y)<1e-5:break
          12 +   step([np.clip(x-rx,-.05,.05),np.clip(y-ry,-.05,.05),0,.1,v])
          13 + x,y,w,h=[s.get(b,f) for f in ['x','y','width','height']]
          14 + move(x+w/2,.8);move(x+w/2,y+h+.215);step([0,0,0,0,1]);move(x+w/2,.65,1);step([0,0,0,0,0])
          15 + x,y,w,h=[s.get(b,f) for f in ['x','y','width','height']]
          16 + move(x+w/2,.85);move(x+off,.85);move(x+off,y+h+.215);step([0,0,0,0,1]);old=s.get(b,'y');step([0,.05,0,0,1]);dy=s.get(b,'y')-old
          17 + print('offset',off,'grasp_delta_y',round(dy,6),'robot_x_error',round(s.get(r,'x')-x-off,6),flush=True);e.close()
diff --git a/probe_grasp_offsets_fine.py b/probe_grasp_offsets_fine.py
new file mode 100644
index 0000000..b6027e1
--- /dev/null
+++ b/probe_grasp_offsets_fine.py
@@ -0,0 +1,17 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +for off in [-.032,-.034,-.0349]:
           4 + e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           5 + def step(a):
           6 +  global s
           7 +  s,*_=e.step(np.array(a,dtype=np.float32))
           8 + def move(x,y,v=0):
           9 +  for _ in range(30):
          10 +   rx,ry=s.get(r,'x'),s.get(r,'y')
          11 +   if abs(rx-x)<1e-5 and abs(ry-y)<1e-5:break
          12 +   step([np.clip(x-rx,-.05,.05),np.clip(y-ry,-.05,.05),0,.1,v])
          13 + x,y,w,h=[s.get(b,f) for f in ['x','y','width','height']]
          14 + move(x+w/2,.8);move(x+w/2,y+h+.215);step([0,0,0,0,1]);move(x+w/2,.65,1);step([0,0,0,0,0])
          15 + x,y,w,h=[s.get(b,f) for f in ['x','y','width','height']]
          16 + move(x+w/2,.85);move(x+off,.85);move(x+off,y+h+.215);step([0,0,0,0,1]);old=s.get(b,'y');step([0,.05,0,0,1]);dy=s.get(b,'y')-old
          17 + print('offset',off,'grasp_delta_y',round(dy,6),'robot_x_error',round(s.get(r,'x')-x-off,6),flush=True);e.close()
diff --git a/probe_reach_edges.json b/probe_reach_edges.json
new file mode 100644
index 0000000..e69de29
diff --git a/probe_reach_edges.py b/probe_reach_edges.py
new file mode 100644
index 0000000..43559a9
--- /dev/null
+++ b/probe_reach_edges.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +import json
           4 +edge=[];inaccessible=[]
           5 +for seed in range(500,1000):
           6 + e=make_env();s,i=e.reset(seed=seed);a=GeneratedApproach(e.action_space,e.observation_space,{});a.reset(s,i)
           7 + for o in a.obstacles(s)+[a.block]:
           8 +  x,y,w,h=a.rect(s,o)
           9 +  if x>1.52 or x+w<.10:edge.append((seed,o.name,x,w))
          10 +  if not a.offsets(x,x,w):inaccessible.append((seed,o.name,x,y,w,h))
          11 + e.close()
          12 +print(json.dumps({'inaccessible':inaccessible,'edges':edge}));
diff --git a/reachability.jsonl b/reachability.jsonl
index e69de29..23424d6 100644
--- a/reachability.jsonl
+++ b/reachability.jsonl
@@ -0,0 +1 @@
           1 +FOUND 0
diff --git a/test_counts_scene_v3.jsonl b/test_counts_scene_v3.jsonl
index 8c570c1..d7cd708 100644
--- a/test_counts_scene_v3.jsonl
+++ b/test_counts_scene_v3.jsonl
@@ -55,3 +55,45 @@
   55     55  {"count": 4, "seed": 54, "steps": 63, "success": true, "seconds": 5.81}
   56     56  {"count": 4, "seed": 55, "steps": 106, "success": true, "seconds": 5.02}
   57     57  {"count": 4, "seed": 56, "steps": 88, "success": true, "seconds": 3.38}
          58 +{"count": 4, "seed": 57, "steps": 102, "success": true, "seconds": 7.76}
          59 +{"count": 4, "seed": 58, "steps": 69, "success": true, "seconds": 8.19}
          60 +{"count": 4, "seed": 59, "steps": 55, "success": true, "seconds": 4.8}
          61 +{"count": 4, "seed": 60, "steps": 93, "success": true, "seconds": 7.57}
          62 +{"count": 4, "seed": 61, "steps": 64, "success": true, "seconds": 3.96}
          63 +{"count": 4, "seed": 62, "steps": 103, "success": true, "seconds": 3.44}
          64 +{"count": 4, "seed": 63, "steps": 115, "success": true, "seconds": 4.77}
          65 +{"count": 4, "seed": 64, "steps": 109, "success": true, "seconds": 3.31}
          66 +{"count": 4, "seed": 65, "steps": 104, "success": true, "seconds": 3.73}
          67 +{"count": 4, "seed": 66, "steps": 95, "success": true, "seconds": 6.46}
          68 +{"count": 4, "seed": 67, "steps": 100, "success": true, "seconds": 5.42}
          69 +{"count": 4, "seed": 68, "steps": 77, "success": true, "seconds": 4.93}
          70 +{"count": 4, "seed": 69, "steps": 74, "success": true, "seconds": 4.93}
          71 +{"count": 4, "seed": 70, "steps": 91, "success": true, "seconds": 4.55}
          72 +{"count": 4, "seed": 71, "steps": 110, "success": true, "seconds": 5.96}
          73 +{"count": 4, "seed": 72, "steps": 64, "success": true, "seconds": 3.83}
          74 +{"count": 4, "seed": 73, "steps": 65, "success": true, "seconds": 4.44}
          75 +{"count": 4, "seed": 74, "steps": 81, "success": true, "seconds": 6.23}
          76 +{"count": 4, "seed": 75, "steps": 118, "success": true, "seconds": 8.08}
          77 +{"count": 4, "seed": 76, "steps": 110, "success": true, "seconds": 5.02}
          78 +{"count": 4, "seed": 77, "steps": 36, "success": true, "seconds": 2.8}
          79 +{"count": 4, "seed": 78, "steps": 82, "success": true, "seconds": 5.6}
          80 +{"count": 4, "seed": 79, "steps": 63, "success": true, "seconds": 3.48}
          81 +{"count": 4, "seed": 80, "steps": 153, "success": true, "seconds": 9.41}
          82 +{"count": 4, "seed": 81, "steps": 78, "success": true, "seconds": 5.97}
          83 +{"count": 4, "seed": 82, "steps": 69, "success": true, "seconds": 2.84}
          84 +{"count": 4, "seed": 83, "steps": 1000, "success": false, "seconds": 19.45, "phase": "lift", "task": "target_block", "dest": [0.19771828162670135, 0.10500000149011612], "robot": [0.6942889094352722, 0.3742868900299072], "init": {"obstruction0": [0.11350048333406448, 0.10000099986791611, 0.13890758156776428, 0.10552427172660828], "obstruction1": [0.9244295358657837, 0.10000099986791611, 0.17725242674350739, 0.1894860714673996], "obstruction2": [0.32857516407966614, 0.10000099986791611, 0.13157790899276733, 0.16201446950435638], "obstruction3": [1.2943108081817627, 0.10000099986791611, 0.05907825380563736, 0.07893645018339157], "target_block": [0.6104315519332886, 0.10000099986791611, 0.16771472990512848, 0.05928588658571243], "target_surface": [0.1578989028930664, 0.0, 0.20953410863876343, 0.10000000149011612]}, "final": {"obstruction0": [0.49944761395454407, 0.18128690123558044, 0.13890758156776428, 0.10552427172660828], "obstruction1": [0.9244295358657837, 0.10000099986791611, 0.17725242674350739, 0.1894860714673996], "obstruction2": [1.3814220428466797, 0.10499998182058334, 0.13157790899276733, 0.16201446950435638], "obstruction3": [1.2943108081817627, 0.10000099986791611, 0.05907825380563736, 0.07893645018339157], "target_block": [0.6104315519332886, 0.10000099986791611, 0.16771472990512848, 0.05928588658571243], "target_surface": [0.1578989028930664, 0.0, 0.20953410863876343, 0.10000000149011612]}}
          85 +{"count": 4, "seed": 84, "steps": 65, "success": true, "seconds": 4.93}
          86 +{"count": 4, "seed": 85, "steps": 126, "success": true, "seconds": 5.51}
          87 +{"count": 4, "seed": 86, "steps": 86, "success": true, "seconds": 4.77}
          88 +{"count": 4, "seed": 87, "steps": 98, "success": true, "seconds": 6.15}
          89 +{"count": 4, "seed": 88, "steps": 110, "success": true, "seconds": 8.28}
          90 +{"count": 4, "seed": 89, "steps": 98, "success": true, "seconds": 4.78}
          91 +{"count": 4, "seed": 90, "steps": 57, "success": true, "seconds": 6.2}
          92 +{"count": 4, "seed": 91, "steps": 102, "success": true, "seconds": 5.37}
          93 +{"count": 4, "seed": 92, "steps": 82, "success": true, "seconds": 6.18}
          94 +{"count": 4, "seed": 93, "steps": 100, "success": true, "seconds": 7.39}
          95 +{"count": 4, "seed": 94, "steps": 68, "success": true, "seconds": 5.19}
          96 +{"count": 4, "seed": 95, "steps": 87, "success": true, "seconds": 4.31}
          97 +{"count": 4, "seed": 96, "steps": 59, "success": true, "seconds": 3.98}
          98 +{"count": 4, "seed": 97, "steps": 147, "success": true, "seconds": 6.48}
          99 +{"count": 4, "seed": 98, "steps": 105, "success": true, "seconds": 6.08}
diff --git a/test_counts_scene_v3.log b/test_counts_scene_v3.log
index 8c570c1..d7cd708 100644
--- a/test_counts_scene_v3.log
+++ b/test_counts_scene_v3.log
@@ -55,3 +55,45 @@
   55     55  {"count": 4, "seed": 54, "steps": 63, "success": true, "seconds": 5.81}
   56     56  {"count": 4, "seed": 55, "steps": 106, "success": true, "seconds": 5.02}
   57     57  {"count": 4, "seed": 56, "steps": 88, "success": true, "seconds": 3.38}
          58 +{"count": 4, "seed": 57, "steps": 102, "success": true, "seconds": 7.76}
          59 +{"count": 4, "seed": 58, "steps": 69, "success": true, "seconds": 8.19}
          60 +{"count": 4, "seed": 59, "steps": 55, "success": true, "seconds": 4.8}
          61 +{"count": 4, "seed": 60, "steps": 93, "success": true, "seconds": 7.57}
          62 +{"count": 4, "seed": 61, "steps": 64, "success": true, "seconds": 3.96}
          63 +{"count": 4, "seed": 62, "steps": 103, "success": true, "seconds": 3.44}
          64 +{"count": 4, "seed": 63, "steps": 115, "success": true, "seconds": 4.77}
          65 +{"count": 4, "seed": 64, "steps": 109, "success": true, "seconds": 3.31}
          66 +{"count": 4, "seed": 65, "steps": 104, "success": true, "seconds": 3.73}
          67 +{"count": 4, "seed": 66, "steps": 95, "success": true, "seconds": 6.46}
          68 +{"count": 4, "seed": 67, "steps": 100, "success": true, "seconds": 5.42}
          69 +{"count": 4, "seed": 68, "steps": 77, "success": true, "seconds": 4.93}
          70 +{"count": 4, "seed": 69, "steps": 74, "success": true, "seconds": 4.93}
          71 +{"count": 4, "seed": 70, "steps": 91, "success": true, "seconds": 4.55}
          72 +{"count": 4, "seed": 71, "steps": 110, "success": true, "seconds": 5.96}
          73 +{"count": 4, "seed": 72, "steps": 64, "success": true, "seconds": 3.83}
          74 +{"count": 4, "seed": 73, "steps": 65, "success": true, "seconds": 4.44}
          75 +{"count": 4, "seed": 74, "steps": 81, "success": true, "seconds": 6.23}
          76 +{"count": 4, "seed": 75, "steps": 118, "success": true, "seconds": 8.08}
          77 +{"count": 4, "seed": 76, "steps": 110, "success": true, "seconds": 5.02}
          78 +{"count": 4, "seed": 77, "steps": 36, "success": true, "seconds": 2.8}
          79 +{"count": 4, "seed": 78, "steps": 82, "success": true, "seconds": 5.6}
          80 +{"count": 4, "seed": 79, "steps": 63, "success": true, "seconds": 3.48}
          81 +{"count": 4, "seed": 80, "steps": 153, "success": true, "seconds": 9.41}
          82 +{"count": 4, "seed": 81, "steps": 78, "success": true, "seconds": 5.97}
          83 +{"count": 4, "seed": 82, "steps": 69, "success": true, "seconds": 2.84}
          84 +{"count": 4, "seed": 83, "steps": 1000, "success": false, "seconds": 19.45, "phase": "lift", "task": "target_block", "dest": [0.19771828162670135, 0.10500000149011612], "robot": [0.6942889094352722, 0.3742868900299072], "init": {"obstruction0": [0.11350048333406448, 0.10000099986791611, 0.13890758156776428, 0.10552427172660828], "obstruction1": [0.9244295358657837, 0.10000099986791611, 0.17725242674350739, 0.1894860714673996], "obstruction2": [0.32857516407966614, 0.10000099986791611, 0.13157790899276733, 0.16201446950435638], "obstruction3": [1.2943108081817627, 0.10000099986791611, 0.05907825380563736, 0.07893645018339157], "target_block": [0.6104315519332886, 0.10000099986791611, 0.16771472990512848, 0.05928588658571243], "target_surface": [0.1578989028930664, 0.0, 0.20953410863876343, 0.10000000149011612]}, "final": {"obstruction0": [0.49944761395454407, 0.18128690123558044, 0.13890758156776428, 0.10552427172660828], "obstruction1": [0.9244295358657837, 0.10000099986791611, 0.17725242674350739, 0.1894860714673996], "obstruction2": [1.3814220428466797, 0.10499998182058334, 0.13157790899276733, 0.16201446950435638], "obstruction3": [1.2943108081817627, 0.10000099986791611, 0.05907825380563736, 0.07893645018339157], "target_block": [0.6104315519332886, 0.10000099986791611, 0.16771472990512848, 0.05928588658571243], "target_surface": [0.1578989028930664, 0.0, 0.20953410863876343, 0.10000000149011612]}}
          85 +{"count": 4, "seed": 84, "steps": 65, "success": true, "seconds": 4.93}
          86 +{"count": 4, "seed": 85, "steps": 126, "success": true, "seconds": 5.51}
          87 +{"count": 4, "seed": 86, "steps": 86, "success": true, "seconds": 4.77}
          88 +{"count": 4, "seed": 87, "steps": 98, "success": true, "seconds": 6.15}
          89 +{"count": 4, "seed": 88, "steps": 110, "success": true, "seconds": 8.28}
          90 +{"count": 4, "seed": 89, "steps": 98, "success": true, "seconds": 4.78}
          91 +{"count": 4, "seed": 90, "steps": 57, "success": true, "seconds": 6.2}
          92 +{"count": 4, "seed": 91, "steps": 102, "success": true, "seconds": 5.37}
          93 +{"count": 4, "seed": 92, "steps": 82, "success": true, "seconds": 6.18}
          94 +{"count": 4, "seed": 93, "steps": 100, "success": true, "seconds": 7.39}
          95 +{"count": 4, "seed": 94, "steps": 68, "success": true, "seconds": 5.19}
          96 +{"count": 4, "seed": 95, "steps": 87, "success": true, "seconds": 4.31}
          97 +{"count": 4, "seed": 96, "steps": 59, "success": true, "seconds": 3.98}
          98 +{"count": 4, "seed": 97, "steps": 147, "success": true, "seconds": 6.48}
          99 +{"count": 4, "seed": 98, "steps": 105, "success": true, "seconds": 6.08}
diff --git a/validate_count4_later.jsonl b/validate_count4_later.jsonl
new file mode 100644
index 0000000..9166a17
--- /dev/null
+++ b/validate_count4_later.jsonl
@@ -0,0 +1,35 @@
           1 +{"seed": 100, "count": 4, "success": true, "steps": 98, "policy_seconds": 0.0285, "elapsed": 2.512}
           2 +{"seed": 101, "count": 4, "success": true, "steps": 111, "policy_seconds": 0.0274, "elapsed": 2.778}
           3 +{"seed": 102, "count": 4, "success": true, "steps": 95, "policy_seconds": 0.0267, "elapsed": 2.755}
           4 +{"seed": 103, "count": 4, "success": true, "steps": 85, "policy_seconds": 0.0292, "elapsed": 1.792}
           5 +{"seed": 104, "count": 4, "success": true, "steps": 122, "policy_seconds": 0.0249, "elapsed": 3.215}
           6 +{"seed": 105, "count": 4, "success": true, "steps": 95, "policy_seconds": 0.0181, "elapsed": 2.678}
           7 +{"seed": 106, "count": 4, "success": true, "steps": 93, "policy_seconds": 0.0309, "elapsed": 2.717}
           8 +{"seed": 107, "count": 4, "success": true, "steps": 65, "policy_seconds": 0.0134, "elapsed": 1.689}
           9 +{"seed": 108, "count": 4, "success": true, "steps": 68, "policy_seconds": 0.0297, "elapsed": 1.83}
          10 +{"seed": 109, "count": 4, "success": true, "steps": 53, "policy_seconds": 0.0165, "elapsed": 1.356}
          11 +{"seed": 110, "count": 4, "success": true, "steps": 75, "policy_seconds": 0.0156, "elapsed": 2.122}
          12 +{"seed": 111, "count": 4, "success": true, "steps": 60, "policy_seconds": 0.0129, "elapsed": 1.768}
          13 +{"seed": 112, "count": 4, "success": true, "steps": 102, "policy_seconds": 0.0313, "elapsed": 2.904}
          14 +{"seed": 113, "count": 4, "success": true, "steps": 89, "policy_seconds": 0.0258, "elapsed": 1.82}
          15 +{"seed": 114, "count": 4, "success": true, "steps": 77, "policy_seconds": 0.0157, "elapsed": 1.115}
          16 +{"seed": 115, "count": 4, "success": true, "steps": 92, "policy_seconds": 0.0297, "elapsed": 1.387}
          17 +{"seed": 116, "count": 4, "success": true, "steps": 61, "policy_seconds": 0.0143, "elapsed": 0.841}
          18 +{"seed": 117, "count": 4, "success": true, "steps": 126, "policy_seconds": 0.0316, "elapsed": 1.673}
          19 +{"seed": 118, "count": 4, "success": true, "steps": 97, "policy_seconds": 0.0226, "elapsed": 1.342}
          20 +{"seed": 119, "count": 4, "success": true, "steps": 80, "policy_seconds": 0.0264, "elapsed": 1.184}
          21 +{"seed": 120, "count": 4, "success": true, "steps": 110, "policy_seconds": 0.0287, "elapsed": 1.818}
          22 +{"seed": 121, "count": 4, "success": true, "steps": 72, "policy_seconds": 0.018, "elapsed": 1.458}
          23 +{"seed": 122, "count": 4, "success": true, "steps": 89, "policy_seconds": 0.0282, "elapsed": 2.262}
          24 +{"seed": 123, "count": 4, "success": true, "steps": 79, "policy_seconds": 0.0118, "elapsed": 2.118}
          25 +{"seed": 124, "count": 4, "success": true, "steps": 109, "policy_seconds": 0.0305, "elapsed": 2.804}
          26 +{"seed": 125, "count": 4, "success": true, "steps": 41, "policy_seconds": 0.0048, "elapsed": 1.284}
          27 +{"seed": 126, "count": 4, "success": true, "steps": 108, "policy_seconds": 0.027, "elapsed": 2.683}
          28 +{"seed": 127, "count": 4, "success": true, "steps": 122, "policy_seconds": 0.0232, "elapsed": 3.1}
          29 +{"seed": 128, "count": 4, "success": true, "steps": 96, "policy_seconds": 0.0236, "elapsed": 2.431}
          30 +{"seed": 129, "count": 4, "success": true, "steps": 102, "policy_seconds": 0.0341, "elapsed": 2.451}
          31 +{"seed": 130, "count": 4, "success": true, "steps": 106, "policy_seconds": 0.024, "elapsed": 2.864}
          32 +{"seed": 131, "count": 4, "success": true, "steps": 55, "policy_seconds": 0.0138, "elapsed": 1.458}
          33 +{"seed": 132, "count": 4, "success": true, "steps": 102, "policy_seconds": 0.0266, "elapsed": 2.654}
          34 +{"seed": 133, "count": 4, "success": true, "steps": 124, "policy_seconds": 0.0294, "elapsed": 2.605}
          35 +{"seed": 134, "count": 4, "success": true, "steps": 87, "policy_seconds": 0.0153, "elapsed": 2.037}
```

</details>

<a id="C014"></a>
### C014 · Use empirically verified edge grasps with one millimeter gripper overlap

Commit `04cf477a35413b414056a4e756cd7a9b029a1df1`; parents: ffca88e4b374cf20096b79c277d3c5907a3cab00. Recorded author date: 2026-09-21T17:42:52Z.

File roles (automatic): diagnostic/test, policy, setup/other.

- [E0119](01_timeline.md#E0119): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_04cf477_approach.py) · [Exact all-file diff](evidence/diffs/C014_04cf477.diff)

[Previous saved controller snapshot](evidence/versions/C013_ffca88e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1bc7e68..5449220 100644
--- a/approach.py
+++ b/approach.py
@@ -46,8 +46,8 @@ class GeneratedApproach:
   46     46          return bad
   47     47  
   48     48      def offsets(self,x,px,w):
   49        -        low=max(.1002-x,.1002-px,-.022)
   50        -        high=min(1.5178-x,1.5178-px,w+.022)
          49 +        low=max(.1002-x,.1002-px,-.034)
          50 +        high=min(1.5178-x,1.5178-px,w+.034)
   51     51          if low>high:return []
   52     52          return sorted(set([max(low,min(high,w/2))]+[float(z) for z in np.linspace(low,high,7)]),key=lambda z:abs(z-w/2))
   53     53  
diff --git a/final_count3.jsonl b/final_count3.jsonl
new file mode 100644
index 0000000..85e664c
--- /dev/null
+++ b/final_count3.jsonl
@@ -0,0 +1,100 @@
           1 +{"seed": 300, "count": 3, "success": true, "steps": 102, "policy_seconds": 0.0223, "elapsed": 1.716}
           2 +{"seed": 301, "count": 3, "success": true, "steps": 78, "policy_seconds": 0.0118, "elapsed": 1.299}
           3 +{"seed": 302, "count": 3, "success": true, "steps": 89, "policy_seconds": 0.013, "elapsed": 1.234}
           4 +{"seed": 303, "count": 3, "success": true, "steps": 113, "policy_seconds": 0.0265, "elapsed": 1.603}
           5 +{"seed": 304, "count": 3, "success": true, "steps": 71, "policy_seconds": 0.0105, "elapsed": 0.811}
           6 +{"seed": 305, "count": 3, "success": true, "steps": 48, "policy_seconds": 0.0131, "elapsed": 0.656}
           7 +{"seed": 306, "count": 3, "success": true, "steps": 92, "policy_seconds": 0.0216, "elapsed": 1.442}
           8 +{"seed": 307, "count": 3, "success": true, "steps": 69, "policy_seconds": 0.0123, "elapsed": 0.691}
           9 +{"seed": 308, "count": 3, "success": true, "steps": 72, "policy_seconds": 0.0129, "elapsed": 0.919}
          10 +{"seed": 309, "count": 3, "success": true, "steps": 106, "policy_seconds": 0.0261, "elapsed": 1.407}
          11 +{"seed": 310, "count": 3, "success": true, "steps": 65, "policy_seconds": 0.0104, "elapsed": 1.085}
          12 +{"seed": 311, "count": 3, "success": true, "steps": 114, "policy_seconds": 0.0224, "elapsed": 1.363}
          13 +{"seed": 312, "count": 3, "success": true, "steps": 107, "policy_seconds": 0.0156, "elapsed": 1.575}
          14 +{"seed": 313, "count": 3, "success": true, "steps": 58, "policy_seconds": 0.01, "elapsed": 0.648}
          15 +{"seed": 314, "count": 3, "success": true, "steps": 81, "policy_seconds": 0.0121, "elapsed": 1.144}
          16 +{"seed": 315, "count": 3, "success": true, "steps": 29, "policy_seconds": 0.0028, "elapsed": 0.48}
          17 +{"seed": 316, "count": 3, "success": true, "steps": 73, "policy_seconds": 0.0149, "elapsed": 0.99}
          18 +{"seed": 317, "count": 3, "success": true, "steps": 70, "policy_seconds": 0.0118, "elapsed": 0.846}
          19 +{"seed": 318, "count": 3, "success": true, "steps": 94, "policy_seconds": 0.0252, "elapsed": 1.384}
          20 +{"seed": 319, "count": 3, "success": true, "steps": 104, "policy_seconds": 0.0209, "elapsed": 1.37}
          21 +{"seed": 320, "count": 3, "success": true, "steps": 51, "policy_seconds": 0.0117, "elapsed": 0.57}
          22 +{"seed": 321, "count": 3, "success": true, "steps": 54, "policy_seconds": 0.0105, "elapsed": 0.791}
          23 +{"seed": 322, "count": 3, "success": true, "steps": 75, "policy_seconds": 0.0108, "elapsed": 1.177}
          24 +{"seed": 323, "count": 3, "success": true, "steps": 70, "policy_seconds": 0.0105, "elapsed": 0.935}
          25 +{"seed": 324, "count": 3, "success": true, "steps": 75, "policy_seconds": 0.0122, "elapsed": 1.158}
          26 +{"seed": 325, "count": 3, "success": true, "steps": 90, "policy_seconds": 0.0169, "elapsed": 1.386}
          27 +{"seed": 326, "count": 3, "success": true, "steps": 102, "policy_seconds": 0.0214, "elapsed": 1.54}
          28 +{"seed": 327, "count": 3, "success": true, "steps": 69, "policy_seconds": 0.0168, "elapsed": 0.888}
          29 +{"seed": 328, "count": 3, "success": true, "steps": 107, "policy_seconds": 0.0249, "elapsed": 1.593}
          30 +{"seed": 329, "count": 3, "success": true, "steps": 108, "policy_seconds": 0.0252, "elapsed": 1.562}
          31 +{"seed": 330, "count": 3, "success": true, "steps": 95, "policy_seconds": 0.0206, "elapsed": 0.956}
          32 +{"seed": 331, "count": 3, "success": true, "steps": 115, "policy_seconds": 0.0209, "elapsed": 1.464}
          33 +{"seed": 332, "count": 3, "success": true, "steps": 96, "policy_seconds": 0.0227, "elapsed": 1.069}
          34 +{"seed": 333, "count": 3, "success": true, "steps": 31, "policy_seconds": 0.0023, "elapsed": 0.367}
          35 +{"seed": 334, "count": 3, "success": true, "steps": 84, "policy_seconds": 0.0194, "elapsed": 0.786}
          36 +{"seed": 335, "count": 3, "success": true, "steps": 95, "policy_seconds": 0.0171, "elapsed": 1.411}
          37 +{"seed": 336, "count": 3, "success": true, "steps": 91, "policy_seconds": 0.0114, "elapsed": 1.144}
          38 +{"seed": 337, "count": 3, "success": true, "steps": 110, "policy_seconds": 0.0215, "elapsed": 1.375}
          39 +{"seed": 338, "count": 3, "success": true, "steps": 155, "policy_seconds": 0.0206, "elapsed": 1.928}
          40 +{"seed": 339, "count": 3, "success": true, "steps": 85, "policy_seconds": 0.0162, "elapsed": 1.017}
          41 +{"seed": 340, "count": 3, "success": true, "steps": 99, "policy_seconds": 0.0124, "elapsed": 1.019}
          42 +{"seed": 341, "count": 3, "success": true, "steps": 50, "policy_seconds": 0.0111, "elapsed": 0.513}
          43 +{"seed": 342, "count": 3, "success": true, "steps": 77, "policy_seconds": 0.0261, "elapsed": 0.933}
          44 +{"seed": 343, "count": 3, "success": true, "steps": 49, "policy_seconds": 0.0029, "elapsed": 0.679}
          45 +{"seed": 344, "count": 3, "success": true, "steps": 78, "policy_seconds": 0.0122, "elapsed": 1.148}
          46 +{"seed": 345, "count": 3, "success": true, "steps": 98, "policy_seconds": 0.019, "elapsed": 1.252}
          47 +{"seed": 346, "count": 3, "success": true, "steps": 43, "policy_seconds": 0.0025, "elapsed": 0.379}
          48 +{"seed": 347, "count": 3, "success": true, "steps": 94, "policy_seconds": 0.0213, "elapsed": 1.333}
          49 +{"seed": 348, "count": 3, "success": true, "steps": 55, "policy_seconds": 0.0066, "elapsed": 0.711}
          50 +{"seed": 349, "count": 3, "success": true, "steps": 132, "policy_seconds": 0.0296, "elapsed": 1.692}
          51 +{"seed": 350, "count": 3, "success": true, "steps": 102, "policy_seconds": 0.0181, "elapsed": 1.518}
          52 +{"seed": 351, "count": 3, "success": true, "steps": 81, "policy_seconds": 0.0093, "elapsed": 0.721}
          53 +{"seed": 352, "count": 3, "success": true, "steps": 116, "policy_seconds": 0.0137, "elapsed": 1.371}
          54 +{"seed": 353, "count": 3, "success": true, "steps": 77, "policy_seconds": 0.0087, "elapsed": 0.911}
          55 +{"seed": 354, "count": 3, "success": true, "steps": 63, "policy_seconds": 0.0119, "elapsed": 0.601}
          56 +{"seed": 355, "count": 3, "success": true, "steps": 91, "policy_seconds": 0.0204, "elapsed": 1.052}
          57 +{"seed": 356, "count": 3, "success": true, "steps": 114, "policy_seconds": 0.0179, "elapsed": 1.519}
          58 +{"seed": 357, "count": 3, "success": true, "steps": 87, "policy_seconds": 0.0184, "elapsed": 1.367}
          59 +{"seed": 358, "count": 3, "success": true, "steps": 74, "policy_seconds": 0.0108, "elapsed": 0.947}
          60 +{"seed": 359, "count": 3, "success": true, "steps": 109, "policy_seconds": 0.0238, "elapsed": 1.309}
          61 +{"seed": 360, "count": 3, "success": true, "steps": 54, "policy_seconds": 0.0122, "elapsed": 0.565}
          62 +{"seed": 361, "count": 3, "success": true, "steps": 73, "policy_seconds": 0.0136, "elapsed": 1.073}
          63 +{"seed": 362, "count": 3, "success": true, "steps": 98, "policy_seconds": 0.0123, "elapsed": 1.207}
          64 +{"seed": 363, "count": 3, "success": true, "steps": 61, "policy_seconds": 0.0117, "elapsed": 0.756}
          65 +{"seed": 364, "count": 3, "success": true, "steps": 71, "policy_seconds": 0.0146, "elapsed": 0.977}
          66 +{"seed": 365, "count": 3, "success": true, "steps": 73, "policy_seconds": 0.0108, "elapsed": 0.784}
          67 +{"seed": 366, "count": 3, "success": true, "steps": 86, "policy_seconds": 0.0127, "elapsed": 1.211}
          68 +{"seed": 367, "count": 3, "success": true, "steps": 100, "policy_seconds": 0.0147, "elapsed": 1.018}
          69 +{"seed": 368, "count": 3, "success": true, "steps": 97, "policy_seconds": 0.0198, "elapsed": 0.953}
          70 +{"seed": 369, "count": 3, "success": true, "steps": 94, "policy_seconds": 0.0156, "elapsed": 1.222}
          71 +{"seed": 370, "count": 3, "success": true, "steps": 75, "policy_seconds": 0.0162, "elapsed": 0.839}
          72 +{"seed": 371, "count": 3, "success": true, "steps": 64, "policy_seconds": 0.0098, "elapsed": 0.915}
          73 +{"seed": 372, "count": 3, "success": true, "steps": 52, "policy_seconds": 0.0116, "elapsed": 0.717}
          74 +{"seed": 373, "count": 3, "success": true, "steps": 74, "policy_seconds": 0.0189, "elapsed": 1.029}
          75 +{"seed": 374, "count": 3, "success": true, "steps": 56, "policy_seconds": 0.0103, "elapsed": 0.722}
          76 +{"seed": 375, "count": 3, "success": true, "steps": 48, "policy_seconds": 0.0139, "elapsed": 0.74}
          77 +{"seed": 376, "count": 3, "success": true, "steps": 79, "policy_seconds": 0.0155, "elapsed": 1.033}
          78 +{"seed": 377, "count": 3, "success": true, "steps": 101, "policy_seconds": 0.0276, "elapsed": 1.247}
          79 +{"seed": 378, "count": 3, "success": true, "steps": 64, "policy_seconds": 0.0076, "elapsed": 0.684}
          80 +{"seed": 379, "count": 3, "success": true, "steps": 62, "policy_seconds": 0.007, "elapsed": 0.771}
          81 +{"seed": 380, "count": 3, "success": true, "steps": 88, "policy_seconds": 0.0177, "elapsed": 0.963}
          82 +{"seed": 381, "count": 3, "success": true, "steps": 100, "policy_seconds": 0.0184, "elapsed": 1.272}
          83 +{"seed": 382, "count": 3, "success": true, "steps": 71, "policy_seconds": 0.011, "elapsed": 0.922}
          84 +{"seed": 383, "count": 3, "success": true, "steps": 59, "policy_seconds": 0.0124, "elapsed": 0.621}
          85 +{"seed": 384, "count": 3, "success": true, "steps": 112, "policy_seconds": 0.0224, "elapsed": 1.655}
          86 +{"seed": 385, "count": 3, "success": true, "steps": 66, "policy_seconds": 0.0075, "elapsed": 0.874}
          87 +{"seed": 386, "count": 3, "error": "min() arg is an empty sequence"}
          88 +{"seed": 387, "count": 3, "success": true, "steps": 80, "policy_seconds": 0.0213, "elapsed": 1.182}
          89 +{"seed": 388, "count": 3, "success": true, "steps": 35, "policy_seconds": 0.0024, "elapsed": 0.48}
          90 +{"seed": 389, "count": 3, "success": true, "steps": 76, "policy_seconds": 0.0158, "elapsed": 1.258}
          91 +{"seed": 390, "count": 3, "success": true, "steps": 50, "policy_seconds": 0.0131, "elapsed": 0.781}
          92 +{"seed": 391, "count": 3, "success": true, "steps": 70, "policy_seconds": 0.0265, "elapsed": 1.122}
          93 +{"seed": 392, "count": 3, "success": true, "steps": 26, "policy_seconds": 0.0022, "elapsed": 0.248}
          94 +{"seed": 393, "count": 3, "success": true, "steps": 69, "policy_seconds": 0.0138, "elapsed": 0.678}
          95 +{"seed": 394, "count": 3, "success": true, "steps": 47, "policy_seconds": 0.0026, "elapsed": 0.61}
          96 +{"seed": 395, "count": 3, "success": true, "steps": 135, "policy_seconds": 0.0309, "elapsed": 1.361}
          97 +{"seed": 396, "count": 3, "success": true, "steps": 61, "policy_seconds": 0.0118, "elapsed": 0.791}
          98 +{"seed": 397, "count": 3, "success": true, "steps": 54, "policy_seconds": 0.0109, "elapsed": 0.693}
          99 +{"seed": 398, "count": 3, "success": true, "steps": 64, "policy_seconds": 0.0087, "elapsed": 0.636}
         100 +{"seed": 399, "count": 3, "success": true, "steps": 97, "policy_seconds": 0.0152, "elapsed": 1.516}
diff --git a/final_count4.jsonl b/final_count4.jsonl
new file mode 100644
index 0000000..c9193db
--- /dev/null
+++ b/final_count4.jsonl
@@ -0,0 +1,82 @@
           1 +{"seed": 0, "count": 4, "success": true, "steps": 89, "policy_seconds": 0.0212, "elapsed": 1.199}
           2 +{"seed": 1, "count": 4, "success": true, "steps": 117, "policy_seconds": 0.0224, "elapsed": 1.773}
           3 +{"seed": 2, "count": 4, "success": true, "steps": 105, "policy_seconds": 0.0238, "elapsed": 1.34}
           4 +{"seed": 3, "count": 4, "success": true, "steps": 84, "policy_seconds": 0.0105, "elapsed": 1.17}
           5 +{"seed": 4, "count": 4, "success": true, "steps": 127, "policy_seconds": 0.0304, "elapsed": 1.793}
           6 +{"seed": 5, "count": 4, "success": true, "steps": 88, "policy_seconds": 0.016, "elapsed": 1.39}
           7 +{"seed": 6, "count": 4, "success": true, "steps": 123, "policy_seconds": 0.0308, "elapsed": 1.877}
           8 +{"seed": 7, "count": 4, "success": true, "steps": 85, "policy_seconds": 0.0155, "elapsed": 1.133}
           9 +{"seed": 8, "count": 4, "success": true, "steps": 105, "policy_seconds": 0.0182, "elapsed": 1.508}
          10 +{"seed": 9, "count": 4, "success": true, "steps": 79, "policy_seconds": 0.0213, "elapsed": 1.44}
          11 +{"seed": 10, "count": 4, "success": true, "steps": 89, "policy_seconds": 0.024, "elapsed": 2.186}
          12 +{"seed": 11, "count": 4, "success": true, "steps": 64, "policy_seconds": 0.0112, "elapsed": 0.983}
          13 +{"seed": 12, "count": 4, "success": true, "steps": 105, "policy_seconds": 0.0193, "elapsed": 1.528}
          14 +{"seed": 13, "count": 4, "success": true, "steps": 98, "policy_seconds": 0.0226, "elapsed": 1.291}
          15 +{"seed": 14, "count": 4, "success": true, "steps": 55, "policy_seconds": 0.0117, "elapsed": 0.697}
          16 +{"seed": 15, "count": 4, "success": true, "steps": 89, "policy_seconds": 0.0305, "elapsed": 1.104}
          17 +{"seed": 16, "count": 4, "success": true, "steps": 80, "policy_seconds": 0.0236, "elapsed": 1.38}
          18 +{"seed": 17, "count": 4, "success": true, "steps": 86, "policy_seconds": 0.0139, "elapsed": 1.407}
          19 +{"seed": 18, "count": 4, "success": true, "steps": 36, "policy_seconds": 0.0034, "elapsed": 0.489}
          20 +{"seed": 19, "count": 4, "success": true, "steps": 70, "policy_seconds": 0.0154, "elapsed": 0.979}
          21 +{"seed": 20, "count": 4, "success": true, "steps": 60, "policy_seconds": 0.0042, "elapsed": 0.874}
          22 +{"seed": 21, "count": 4, "success": true, "steps": 56, "policy_seconds": 0.0112, "elapsed": 0.747}
          23 +{"seed": 22, "count": 4, "success": true, "steps": 55, "policy_seconds": 0.0164, "elapsed": 0.84}
          24 +{"seed": 23, "count": 4, "success": true, "steps": 59, "policy_seconds": 0.0129, "elapsed": 0.961}
          25 +{"seed": 24, "count": 4, "success": true, "steps": 117, "policy_seconds": 0.0284, "elapsed": 1.723}
          26 +{"seed": 25, "count": 4, "success": true, "steps": 100, "policy_seconds": 0.0293, "elapsed": 1.56}
          27 +{"seed": 26, "count": 4, "success": true, "steps": 88, "policy_seconds": 0.0301, "elapsed": 1.455}
          28 +{"seed": 27, "count": 4, "success": true, "steps": 93, "policy_seconds": 0.0203, "elapsed": 1.065}
          29 +{"seed": 28, "count": 4, "success": true, "steps": 112, "policy_seconds": 0.0209, "elapsed": 1.56}
          30 +{"seed": 29, "count": 4, "success": true, "steps": 63, "policy_seconds": 0.0191, "elapsed": 0.907}
          31 +{"seed": 30, "count": 4, "success": true, "steps": 113, "policy_seconds": 0.0163, "elapsed": 1.485}
          32 +{"seed": 31, "count": 4, "success": true, "steps": 48, "policy_seconds": 0.0084, "elapsed": 0.623}
          33 +{"seed": 32, "count": 4, "success": true, "steps": 40, "policy_seconds": 0.0032, "elapsed": 0.632}
          34 +{"seed": 33, "count": 4, "success": true, "steps": 68, "policy_seconds": 0.0125, "elapsed": 0.947}
          35 +{"seed": 34, "count": 4, "success": true, "steps": 101, "policy_seconds": 0.0258, "elapsed": 1.507}
          36 +{"seed": 35, "count": 4, "success": true, "steps": 50, "policy_seconds": 0.0129, "elapsed": 0.66}
          37 +{"seed": 36, "count": 4, "success": true, "steps": 164, "policy_seconds": 0.0416, "elapsed": 2.535}
          38 +{"seed": 37, "count": 4, "success": true, "steps": 125, "policy_seconds": 0.0214, "elapsed": 1.69}
          39 +{"seed": 38, "count": 4, "success": true, "steps": 78, "policy_seconds": 0.0126, "elapsed": 1.12}
          40 +{"seed": 39, "count": 4, "success": true, "steps": 115, "policy_seconds": 0.0286, "elapsed": 1.768}
          41 +{"seed": 40, "count": 4, "success": true, "steps": 104, "policy_seconds": 0.0415, "elapsed": 1.622}
          42 +{"seed": 41, "count": 4, "success": true, "steps": 100, "policy_seconds": 0.0173, "elapsed": 1.403}
          43 +{"seed": 42, "count": 4, "success": true, "steps": 63, "policy_seconds": 0.0163, "elapsed": 0.905}
          44 +{"seed": 43, "count": 4, "success": true, "steps": 82, "policy_seconds": 0.0203, "elapsed": 1.043}
          45 +{"seed": 44, "count": 4, "success": true, "steps": 85, "policy_seconds": 0.0253, "elapsed": 1.088}
          46 +{"seed": 45, "count": 4, "success": true, "steps": 67, "policy_seconds": 0.0137, "elapsed": 0.863}
          47 +{"seed": 46, "count": 4, "success": true, "steps": 112, "policy_seconds": 0.0217, "elapsed": 1.524}
          48 +{"seed": 47, "count": 4, "success": true, "steps": 84, "policy_seconds": 0.0456, "elapsed": 1.53}
          49 +{"seed": 48, "count": 4, "success": true, "steps": 118, "policy_seconds": 0.0299, "elapsed": 1.673}
          50 +{"seed": 49, "count": 4, "success": true, "steps": 71, "policy_seconds": 0.0116, "elapsed": 1.114}
          51 +{"seed": 50, "count": 4, "success": true, "steps": 78, "policy_seconds": 0.0149, "elapsed": 1.081}
          52 +{"seed": 51, "count": 4, "success": true, "steps": 81, "policy_seconds": 0.0212, "elapsed": 0.81}
          53 +{"seed": 52, "count": 4, "success": true, "steps": 72, "policy_seconds": 0.0141, "elapsed": 0.546}
          54 +{"seed": 53, "count": 4, "success": true, "steps": 87, "policy_seconds": 0.0156, "elapsed": 0.689}
          55 +{"seed": 54, "count": 4, "success": true, "steps": 63, "policy_seconds": 0.0129, "elapsed": 0.545}
          56 +{"seed": 55, "count": 4, "success": true, "steps": 106, "policy_seconds": 0.024, "elapsed": 1.068}
          57 +{"seed": 56, "count": 4, "success": true, "steps": 88, "policy_seconds": 0.0279, "elapsed": 0.818}
          58 +{"seed": 57, "count": 4, "success": true, "steps": 102, "policy_seconds": 0.0241, "elapsed": 0.786}
          59 +{"seed": 58, "count": 4, "success": true, "steps": 69, "policy_seconds": 0.0119, "elapsed": 0.584}
          60 +{"seed": 59, "count": 4, "success": true, "steps": 55, "policy_seconds": 0.0142, "elapsed": 0.383}
          61 +{"seed": 60, "count": 4, "success": true, "steps": 93, "policy_seconds": 0.0239, "elapsed": 0.732}
          62 +{"seed": 61, "count": 4, "success": true, "steps": 64, "policy_seconds": 0.0133, "elapsed": 0.538}
          63 +{"seed": 62, "count": 4, "success": true, "steps": 103, "policy_seconds": 0.0235, "elapsed": 0.929}
          64 +{"seed": 63, "count": 4, "success": true, "steps": 115, "policy_seconds": 0.028, "elapsed": 0.879}
          65 +{"seed": 64, "count": 4, "success": true, "steps": 109, "policy_seconds": 0.0179, "elapsed": 0.92}
          66 +{"seed": 65, "count": 4, "success": true, "steps": 104, "policy_seconds": 0.0215, "elapsed": 0.776}
          67 +{"seed": 66, "count": 4, "success": true, "steps": 95, "policy_seconds": 0.0233, "elapsed": 0.943}
          68 +{"seed": 67, "count": 4, "success": true, "steps": 100, "policy_seconds": 0.0099, "elapsed": 0.726}
          69 +{"seed": 68, "count": 4, "success": true, "steps": 77, "policy_seconds": 0.0138, "elapsed": 0.7}
          70 +{"seed": 69, "count": 4, "success": true, "steps": 74, "policy_seconds": 0.0122, "elapsed": 0.558}
          71 +{"seed": 70, "count": 4, "success": true, "steps": 91, "policy_seconds": 0.0275, "elapsed": 0.651}
          72 +{"seed": 71, "count": 4, "success": true, "steps": 110, "policy_seconds": 0.0268, "elapsed": 0.813}
          73 +{"seed": 72, "count": 4, "success": true, "steps": 64, "policy_seconds": 0.014, "elapsed": 0.593}
          74 +{"seed": 73, "count": 4, "success": true, "steps": 65, "policy_seconds": 0.0147, "elapsed": 0.515}
          75 +{"seed": 74, "count": 4, "success": true, "steps": 81, "policy_seconds": 0.0119, "elapsed": 0.684}
          76 +{"seed": 75, "count": 4, "success": true, "steps": 118, "policy_seconds": 0.0192, "elapsed": 0.847}
          77 +{"seed": 76, "count": 4, "success": true, "steps": 110, "policy_seconds": 0.0187, "elapsed": 0.824}
          78 +{"seed": 77, "count": 4, "success": true, "steps": 36, "policy_seconds": 0.0028, "elapsed": 0.313}
          79 +{"seed": 78, "count": 4, "success": true, "steps": 82, "policy_seconds": 0.0137, "elapsed": 0.658}
          80 +{"seed": 79, "count": 4, "success": true, "steps": 63, "policy_seconds": 0.0114, "elapsed": 0.494}
          81 +{"seed": 80, "count": 4, "success": true, "steps": 153, "policy_seconds": 0.0427, "elapsed": 1.427}
          82 +{"seed": 81, "count": 4, "success": true, "steps": 78, "policy_seconds": 0.0131, "elapsed": 0.56}
diff --git a/final_count4.log b/final_count4.log
new file mode 100644
index 0000000..e69de29
diff --git a/final_defaults.jsonl b/final_defaults.jsonl
new file mode 100644
index 0000000..54b1323
--- /dev/null
+++ b/final_defaults.jsonl
@@ -0,0 +1,436 @@
           1 +{"seed": 0, "count": null, "success": true, "steps": 92, "policy_seconds": 0.0177, "elapsed": 0.723}
           2 +{"seed": 1, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0081, "elapsed": 0.322}
           3 +{"seed": 2, "count": null, "success": true, "steps": 82, "policy_seconds": 0.0192, "elapsed": 0.615}
           4 +{"seed": 3, "count": null, "success": true, "steps": 58, "policy_seconds": 0.0091, "elapsed": 0.413}
           5 +{"seed": 4, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0024, "elapsed": 0.342}
           6 +{"seed": 5, "count": null, "success": true, "steps": 118, "policy_seconds": 0.0207, "elapsed": 1.382}
           7 +{"seed": 6, "count": null, "success": true, "steps": 55, "policy_seconds": 0.0059, "elapsed": 0.431}
           8 +{"seed": 7, "count": null, "success": true, "steps": 121, "policy_seconds": 0.026, "elapsed": 1.244}
           9 +{"seed": 8, "count": null, "success": true, "steps": 81, "policy_seconds": 0.0174, "elapsed": 1.127}
          10 +{"seed": 9, "count": null, "success": true, "steps": 86, "policy_seconds": 0.0073, "elapsed": 0.725}
          11 +{"seed": 10, "count": null, "success": true, "steps": 38, "policy_seconds": 0.0024, "elapsed": 0.373}
          12 +{"seed": 11, "count": null, "success": true, "steps": 44, "policy_seconds": 0.0016, "elapsed": 0.44}
          13 +{"seed": 12, "count": null, "success": true, "steps": 82, "policy_seconds": 0.0081, "elapsed": 0.792}
          14 +{"seed": 13, "count": null, "success": true, "steps": 68, "policy_seconds": 0.006, "elapsed": 0.718}
          15 +{"seed": 14, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0009, "elapsed": 0.221}
          16 +{"seed": 15, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0018, "elapsed": 0.273}
          17 +{"seed": 16, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0012, "elapsed": 0.164}
          18 +{"seed": 17, "count": null, "success": true, "steps": 74, "policy_seconds": 0.0113, "elapsed": 1.055}
          19 +{"seed": 18, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0081, "elapsed": 0.736}
          20 +{"seed": 19, "count": null, "success": true, "steps": 53, "policy_seconds": 0.0059, "elapsed": 0.419}
          21 +{"seed": 20, "count": null, "success": true, "steps": 68, "policy_seconds": 0.0106, "elapsed": 0.572}
          22 +{"seed": 21, "count": null, "success": true, "steps": 52, "policy_seconds": 0.0017, "elapsed": 0.494}
          23 +{"seed": 22, "count": null, "success": true, "steps": 101, "policy_seconds": 0.016, "elapsed": 1.258}
          24 +{"seed": 23, "count": null, "success": true, "steps": 42, "policy_seconds": 0.0014, "elapsed": 0.261}
          25 +{"seed": 24, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0052, "elapsed": 0.512}
          26 +{"seed": 25, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0058, "elapsed": 0.633}
          27 +{"seed": 26, "count": null, "success": true, "steps": 56, "policy_seconds": 0.0091, "elapsed": 0.736}
          28 +{"seed": 27, "count": null, "success": true, "steps": 20, "policy_seconds": 0.0008, "elapsed": 0.19}
          29 +{"seed": 28, "count": null, "success": true, "steps": 45, "policy_seconds": 0.0017, "elapsed": 0.342}
          30 +{"seed": 29, "count": null, "success": true, "steps": 40, "policy_seconds": 0.0104, "elapsed": 0.487}
          31 +{"seed": 30, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0009, "elapsed": 0.138}
          32 +{"seed": 31, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0088, "elapsed": 0.527}
          33 +{"seed": 32, "count": null, "success": true, "steps": 91, "policy_seconds": 0.013, "elapsed": 1.034}
          34 +{"seed": 33, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0073, "elapsed": 0.662}
          35 +{"seed": 34, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0011, "elapsed": 0.234}
          36 +{"seed": 35, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0011, "elapsed": 0.265}
          37 +{"seed": 36, "count": null, "success": true, "steps": 43, "policy_seconds": 0.0064, "elapsed": 0.352}
          38 +{"seed": 37, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0011, "elapsed": 0.249}
          39 +{"seed": 38, "count": null, "success": true, "steps": 21, "policy_seconds": 0.0008, "elapsed": 0.183}
          40 +{"seed": 39, "count": null, "success": true, "steps": 62, "policy_seconds": 0.0065, "elapsed": 0.627}
          41 +{"seed": 40, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0056, "elapsed": 0.469}
          42 +{"seed": 41, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0018, "elapsed": 0.28}
          43 +{"seed": 42, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0012, "elapsed": 0.334}
          44 +{"seed": 43, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0013, "elapsed": 0.258}
          45 +{"seed": 44, "count": null, "success": true, "steps": 66, "policy_seconds": 0.0102, "elapsed": 0.75}
          46 +{"seed": 45, "count": null, "success": true, "steps": 94, "policy_seconds": 0.0134, "elapsed": 1.016}
          47 +{"seed": 46, "count": null, "success": true, "steps": 39, "policy_seconds": 0.0016, "elapsed": 0.298}
          48 +{"seed": 47, "count": null, "success": true, "steps": 38, "policy_seconds": 0.0015, "elapsed": 0.402}
          49 +{"seed": 48, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0009, "elapsed": 0.159}
          50 +{"seed": 49, "count": null, "success": true, "steps": 21, "policy_seconds": 0.0008, "elapsed": 0.187}
          51 +{"seed": 50, "count": null, "success": true, "steps": 70, "policy_seconds": 0.0109, "elapsed": 0.838}
          52 +{"seed": 51, "count": null, "success": true, "steps": 37, "policy_seconds": 0.0016, "elapsed": 0.322}
          53 +{"seed": 52, "count": null, "success": true, "steps": 81, "policy_seconds": 0.0146, "elapsed": 0.832}
          54 +{"seed": 53, "count": null, "success": true, "steps": 92, "policy_seconds": 0.0161, "elapsed": 1.074}
          55 +{"seed": 54, "count": null, "success": true, "steps": 30, "policy_seconds": 0.0012, "elapsed": 0.265}
          56 +{"seed": 55, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0019, "elapsed": 0.293}
          57 +{"seed": 56, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0095, "elapsed": 0.652}
          58 +{"seed": 57, "count": null, "success": true, "steps": 18, "policy_seconds": 0.0007, "elapsed": 0.114}
          59 +{"seed": 58, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0046, "elapsed": 0.483}
          60 +{"seed": 59, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0091, "elapsed": 0.613}
          61 +{"seed": 60, "count": null, "success": true, "steps": 25, "policy_seconds": 0.001, "elapsed": 0.214}
          62 +{"seed": 61, "count": null, "success": true, "steps": 68, "policy_seconds": 0.0051, "elapsed": 0.98}
          63 +{"seed": 62, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0067, "elapsed": 0.874}
          64 +{"seed": 63, "count": null, "success": true, "steps": 43, "policy_seconds": 0.0078, "elapsed": 0.584}
          65 +{"seed": 64, "count": null, "success": true, "steps": 29, "policy_seconds": 0.0017, "elapsed": 0.389}
          66 +{"seed": 65, "count": null, "success": true, "steps": 19, "policy_seconds": 0.0008, "elapsed": 0.206}
          67 +{"seed": 66, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0086, "elapsed": 0.946}
          68 +{"seed": 67, "count": null, "success": true, "steps": 51, "policy_seconds": 0.0107, "elapsed": 0.695}
          69 +{"seed": 68, "count": null, "success": true, "steps": 47, "policy_seconds": 0.0059, "elapsed": 0.448}
          70 +{"seed": 69, "count": null, "success": true, "steps": 36, "policy_seconds": 0.0013, "elapsed": 0.272}
          71 +{"seed": 70, "count": null, "success": true, "steps": 49, "policy_seconds": 0.0102, "elapsed": 0.497}
          72 +{"seed": 71, "count": null, "success": true, "steps": 42, "policy_seconds": 0.0104, "elapsed": 0.464}
          73 +{"seed": 72, "count": null, "success": true, "steps": 97, "policy_seconds": 0.0106, "elapsed": 0.928}
          74 +{"seed": 73, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0072, "elapsed": 0.68}
          75 +{"seed": 74, "count": null, "success": true, "steps": 24, "policy_seconds": 0.0012, "elapsed": 0.277}
          76 +{"seed": 75, "count": null, "success": true, "steps": 73, "policy_seconds": 0.0079, "elapsed": 0.684}
          77 +{"seed": 76, "count": null, "success": true, "steps": 30, "policy_seconds": 0.0013, "elapsed": 0.218}
          78 +{"seed": 77, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0007, "elapsed": 0.125}
          79 +{"seed": 78, "count": null, "success": true, "steps": 99, "policy_seconds": 0.0184, "elapsed": 1.0}
          80 +{"seed": 79, "count": null, "success": true, "steps": 34, "policy_seconds": 0.0012, "elapsed": 0.315}
          81 +{"seed": 80, "count": null, "success": true, "steps": 68, "policy_seconds": 0.0071, "elapsed": 0.689}
          82 +{"seed": 81, "count": null, "success": true, "steps": 25, "policy_seconds": 0.001, "elapsed": 0.338}
          83 +{"seed": 82, "count": null, "success": true, "steps": 37, "policy_seconds": 0.0021, "elapsed": 0.395}
          84 +{"seed": 83, "count": null, "success": true, "steps": 111, "policy_seconds": 0.0185, "elapsed": 1.226}
          85 +{"seed": 84, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0062, "elapsed": 0.595}
          86 +{"seed": 85, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0066, "elapsed": 0.631}
          87 +{"seed": 86, "count": null, "success": true, "steps": 45, "policy_seconds": 0.0097, "elapsed": 0.327}
          88 +{"seed": 87, "count": null, "success": true, "steps": 53, "policy_seconds": 0.0065, "elapsed": 0.586}
          89 +{"seed": 88, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0058, "elapsed": 0.58}
          90 +{"seed": 89, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0103, "elapsed": 0.712}
          91 +{"seed": 90, "count": null, "success": true, "steps": 77, "policy_seconds": 0.0068, "elapsed": 0.801}
          92 +{"seed": 91, "count": null, "success": true, "steps": 43, "policy_seconds": 0.0098, "elapsed": 0.511}
          93 +{"seed": 92, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0058, "elapsed": 0.484}
          94 +{"seed": 93, "count": null, "success": true, "steps": 76, "policy_seconds": 0.0116, "elapsed": 1.0}
          95 +{"seed": 94, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0011, "elapsed": 0.29}
          96 +{"seed": 95, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0082, "elapsed": 0.516}
          97 +{"seed": 96, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0021, "elapsed": 0.277}
          98 +{"seed": 97, "count": null, "success": true, "steps": 36, "policy_seconds": 0.0011, "elapsed": 0.344}
          99 +{"seed": 98, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0067, "elapsed": 0.383}
         100 +{"seed": 99, "count": null, "success": true, "steps": 46, "policy_seconds": 0.0027, "elapsed": 0.673}
         101 +{"seed": 100, "count": null, "success": true, "steps": 97, "policy_seconds": 0.0155, "elapsed": 1.161}
         102 +{"seed": 101, "count": null, "success": true, "steps": 17, "policy_seconds": 0.0007, "elapsed": 0.123}
         103 +{"seed": 102, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0085, "elapsed": 0.504}
         104 +{"seed": 103, "count": null, "success": true, "steps": 35, "policy_seconds": 0.0016, "elapsed": 0.34}
         105 +{"seed": 104, "count": null, "success": true, "steps": 103, "policy_seconds": 0.0156, "elapsed": 1.214}
         106 +{"seed": 105, "count": null, "success": true, "steps": 20, "policy_seconds": 0.0007, "elapsed": 0.148}
         107 +{"seed": 106, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0015, "elapsed": 0.245}
         108 +{"seed": 107, "count": null, "success": true, "steps": 30, "policy_seconds": 0.0012, "elapsed": 0.306}
         109 +{"seed": 108, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0009, "elapsed": 0.239}
         110 +{"seed": 109, "count": null, "success": true, "steps": 51, "policy_seconds": 0.006, "elapsed": 0.486}
         111 +{"seed": 110, "count": null, "success": true, "steps": 68, "policy_seconds": 0.008, "elapsed": 0.559}
         112 +{"seed": 111, "count": null, "success": true, "steps": 38, "policy_seconds": 0.0016, "elapsed": 0.303}
         113 +{"seed": 112, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0013, "elapsed": 0.288}
         114 +{"seed": 113, "count": null, "success": true, "steps": 41, "policy_seconds": 0.0016, "elapsed": 0.331}
         115 +{"seed": 114, "count": null, "success": true, "steps": 21, "policy_seconds": 0.0009, "elapsed": 0.148}
         116 +{"seed": 115, "count": null, "success": true, "steps": 66, "policy_seconds": 0.0068, "elapsed": 0.594}
         117 +{"seed": 116, "count": null, "success": true, "steps": 49, "policy_seconds": 0.0015, "elapsed": 0.32}
         118 +{"seed": 117, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0009, "elapsed": 0.14}
         119 +{"seed": 118, "count": null, "success": true, "steps": 56, "policy_seconds": 0.0057, "elapsed": 0.483}
         120 +{"seed": 119, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0063, "elapsed": 0.658}
         121 +{"seed": 120, "count": null, "success": true, "steps": 20, "policy_seconds": 0.0009, "elapsed": 0.18}
         122 +{"seed": 121, "count": null, "success": true, "steps": 26, "policy_seconds": 0.001, "elapsed": 0.185}
         123 +{"seed": 122, "count": null, "success": true, "steps": 77, "policy_seconds": 0.0089, "elapsed": 0.966}
         124 +{"seed": 123, "count": null, "success": true, "steps": 40, "policy_seconds": 0.0012, "elapsed": 0.227}
         125 +{"seed": 124, "count": null, "success": true, "steps": 67, "policy_seconds": 0.0088, "elapsed": 0.749}
         126 +{"seed": 125, "count": null, "success": true, "steps": 75, "policy_seconds": 0.0062, "elapsed": 0.667}
         127 +{"seed": 126, "count": null, "success": true, "steps": 17, "policy_seconds": 0.0007, "elapsed": 0.119}
         128 +{"seed": 127, "count": null, "success": true, "steps": 75, "policy_seconds": 0.0058, "elapsed": 0.796}
         129 +{"seed": 128, "count": null, "success": true, "steps": 103, "policy_seconds": 0.0184, "elapsed": 1.222}
         130 +{"seed": 129, "count": null, "success": true, "steps": 38, "policy_seconds": 0.0015, "elapsed": 0.387}
         131 +{"seed": 130, "count": null, "success": true, "steps": 58, "policy_seconds": 0.0072, "elapsed": 0.493}
         132 +{"seed": 131, "count": null, "success": true, "steps": 36, "policy_seconds": 0.0019, "elapsed": 0.365}
         133 +{"seed": 132, "count": null, "success": true, "steps": 97, "policy_seconds": 0.0185, "elapsed": 1.096}
         134 +{"seed": 133, "count": null, "success": true, "steps": 65, "policy_seconds": 0.0047, "elapsed": 0.507}
         135 +{"seed": 134, "count": null, "success": true, "steps": 26, "policy_seconds": 0.002, "elapsed": 0.185}
         136 +{"seed": 135, "count": null, "success": true, "steps": 18, "policy_seconds": 0.001, "elapsed": 0.078}
         137 +{"seed": 136, "count": null, "success": true, "steps": 52, "policy_seconds": 0.0087, "elapsed": 0.643}
         138 +{"seed": 137, "count": null, "success": true, "steps": 75, "policy_seconds": 0.0055, "elapsed": 0.744}
         139 +{"seed": 138, "count": null, "success": true, "steps": 85, "policy_seconds": 0.0075, "elapsed": 0.554}
         140 +{"seed": 139, "count": null, "success": true, "steps": 86, "policy_seconds": 0.007, "elapsed": 0.731}
         141 +{"seed": 140, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0011, "elapsed": 0.155}
         142 +{"seed": 141, "count": null, "success": true, "steps": 55, "policy_seconds": 0.0058, "elapsed": 0.492}
         143 +{"seed": 142, "count": null, "success": true, "steps": 53, "policy_seconds": 0.0015, "elapsed": 0.411}
         144 +{"seed": 143, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0086, "elapsed": 0.43}
         145 +{"seed": 144, "count": null, "success": true, "steps": 38, "policy_seconds": 0.0011, "elapsed": 0.319}
         146 +{"seed": 145, "count": null, "success": true, "steps": 46, "policy_seconds": 0.0067, "elapsed": 0.416}
         147 +{"seed": 146, "count": null, "success": true, "steps": 55, "policy_seconds": 0.0068, "elapsed": 0.558}
         148 +{"seed": 147, "count": null, "success": true, "steps": 24, "policy_seconds": 0.0008, "elapsed": 0.149}
         149 +{"seed": 148, "count": null, "success": true, "steps": 18, "policy_seconds": 0.0007, "elapsed": 0.236}
         150 +{"seed": 149, "count": null, "success": true, "steps": 29, "policy_seconds": 0.0009, "elapsed": 0.202}
         151 +{"seed": 150, "count": null, "success": true, "steps": 35, "policy_seconds": 0.0013, "elapsed": 0.269}
         152 +{"seed": 151, "count": null, "success": true, "steps": 28, "policy_seconds": 0.0017, "elapsed": 0.271}
         153 +{"seed": 152, "count": null, "success": true, "steps": 47, "policy_seconds": 0.0109, "elapsed": 0.363}
         154 +{"seed": 153, "count": null, "success": true, "steps": 77, "policy_seconds": 0.0157, "elapsed": 0.928}
         155 +{"seed": 154, "count": null, "success": true, "steps": 38, "policy_seconds": 0.0011, "elapsed": 0.19}
         156 +{"seed": 155, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0009, "elapsed": 0.222}
         157 +{"seed": 156, "count": null, "success": true, "steps": 75, "policy_seconds": 0.0164, "elapsed": 0.884}
         158 +{"seed": 157, "count": null, "success": true, "steps": 35, "policy_seconds": 0.0011, "elapsed": 0.336}
         159 +{"seed": 158, "count": null, "success": true, "steps": 79, "policy_seconds": 0.0062, "elapsed": 0.642}
         160 +{"seed": 159, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0083, "elapsed": 0.444}
         161 +{"seed": 160, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0009, "elapsed": 0.15}
         162 +{"seed": 161, "count": null, "success": true, "steps": 55, "policy_seconds": 0.0086, "elapsed": 0.769}
         163 +{"seed": 162, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0066, "elapsed": 0.517}
         164 +{"seed": 163, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0055, "elapsed": 0.51}
         165 +{"seed": 164, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0066, "elapsed": 0.511}
         166 +{"seed": 165, "count": null, "success": true, "steps": 67, "policy_seconds": 0.0057, "elapsed": 0.512}
         167 +{"seed": 166, "count": null, "success": true, "steps": 49, "policy_seconds": 0.008, "elapsed": 0.501}
         168 +{"seed": 167, "count": null, "success": true, "steps": 73, "policy_seconds": 0.0081, "elapsed": 0.964}
         169 +{"seed": 168, "count": null, "success": true, "steps": 44, "policy_seconds": 0.0017, "elapsed": 0.393}
         170 +{"seed": 169, "count": null, "success": true, "steps": 76, "policy_seconds": 0.0076, "elapsed": 0.73}
         171 +{"seed": 170, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0098, "elapsed": 0.702}
         172 +{"seed": 171, "count": null, "success": true, "steps": 70, "policy_seconds": 0.0067, "elapsed": 0.903}
         173 +{"seed": 172, "count": null, "success": true, "steps": 53, "policy_seconds": 0.0058, "elapsed": 0.443}
         174 +{"seed": 173, "count": null, "success": true, "steps": 82, "policy_seconds": 0.0081, "elapsed": 0.844}
         175 +{"seed": 174, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0061, "elapsed": 0.467}
         176 +{"seed": 175, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0064, "elapsed": 0.656}
         177 +{"seed": 176, "count": null, "success": true, "steps": 34, "policy_seconds": 0.001, "elapsed": 0.293}
         178 +{"seed": 177, "count": null, "success": true, "steps": 66, "policy_seconds": 0.006, "elapsed": 0.476}
         179 +{"seed": 178, "count": null, "success": true, "steps": 83, "policy_seconds": 0.0064, "elapsed": 0.621}
         180 +{"seed": 179, "count": null, "success": true, "steps": 80, "policy_seconds": 0.0075, "elapsed": 0.79}
         181 +{"seed": 180, "count": null, "success": true, "steps": 37, "policy_seconds": 0.0011, "elapsed": 0.427}
         182 +{"seed": 181, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0081, "elapsed": 0.634}
         183 +{"seed": 182, "count": null, "success": true, "steps": 123, "policy_seconds": 0.0113, "elapsed": 1.269}
         184 +{"seed": 183, "count": null, "success": true, "steps": 68, "policy_seconds": 0.0066, "elapsed": 0.676}
         185 +{"seed": 184, "count": null, "success": true, "steps": 56, "policy_seconds": 0.0067, "elapsed": 0.594}
         186 +{"seed": 185, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0008, "elapsed": 0.186}
         187 +{"seed": 186, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0008, "elapsed": 0.146}
         188 +{"seed": 187, "count": null, "success": true, "steps": 55, "policy_seconds": 0.0043, "elapsed": 0.343}
         189 +{"seed": 188, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0013, "elapsed": 0.206}
         190 +{"seed": 189, "count": null, "success": true, "steps": 37, "policy_seconds": 0.0015, "elapsed": 0.359}
         191 +{"seed": 190, "count": null, "success": true, "steps": 19, "policy_seconds": 0.0007, "elapsed": 0.13}
         192 +{"seed": 191, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0009, "elapsed": 0.23}
         193 +{"seed": 192, "count": null, "success": true, "steps": 51, "policy_seconds": 0.0093, "elapsed": 0.532}
         194 +{"seed": 193, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0058, "elapsed": 0.591}
         195 +{"seed": 194, "count": null, "success": true, "steps": 80, "policy_seconds": 0.012, "elapsed": 0.966}
         196 +{"seed": 195, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0008, "elapsed": 0.138}
         197 +{"seed": 196, "count": null, "success": true, "steps": 39, "policy_seconds": 0.0012, "elapsed": 0.261}
         198 +{"seed": 197, "count": null, "success": true, "steps": 105, "policy_seconds": 0.0154, "elapsed": 0.883}
         199 +{"seed": 198, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0051, "elapsed": 0.584}
         200 +{"seed": 199, "count": null, "success": true, "steps": 55, "policy_seconds": 0.006, "elapsed": 0.4}
         201 +{"seed": 200, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0007, "elapsed": 0.168}
         202 +{"seed": 201, "count": null, "success": true, "steps": 28, "policy_seconds": 0.001, "elapsed": 0.224}
         203 +{"seed": 202, "count": null, "success": true, "steps": 32, "policy_seconds": 0.001, "elapsed": 0.192}
         204 +{"seed": 203, "count": null, "success": true, "steps": 37, "policy_seconds": 0.0011, "elapsed": 0.196}
         205 +{"seed": 204, "count": null, "success": true, "steps": 62, "policy_seconds": 0.0079, "elapsed": 0.815}
         206 +{"seed": 205, "count": null, "success": true, "steps": 41, "policy_seconds": 0.0015, "elapsed": 0.344}
         207 +{"seed": 206, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0052, "elapsed": 0.583}
         208 +{"seed": 207, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0007, "elapsed": 0.155}
         209 +{"seed": 208, "count": null, "success": true, "steps": 29, "policy_seconds": 0.0018, "elapsed": 0.223}
         210 +{"seed": 209, "count": null, "success": true, "steps": 47, "policy_seconds": 0.0104, "elapsed": 0.588}
         211 +{"seed": 210, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0008, "elapsed": 0.133}
         212 +{"seed": 211, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0011, "elapsed": 0.246}
         213 +{"seed": 212, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0011, "elapsed": 0.361}
         214 +{"seed": 213, "count": null, "success": true, "steps": 20, "policy_seconds": 0.0007, "elapsed": 0.202}
         215 +{"seed": 214, "count": null, "success": true, "steps": 46, "policy_seconds": 0.0012, "elapsed": 0.343}
         216 +{"seed": 215, "count": null, "success": true, "steps": 77, "policy_seconds": 0.0081, "elapsed": 0.838}
         217 +{"seed": 216, "count": null, "success": true, "steps": 34, "policy_seconds": 0.0017, "elapsed": 0.242}
         218 +{"seed": 217, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0073, "elapsed": 0.536}
         219 +{"seed": 218, "count": null, "success": true, "steps": 44, "policy_seconds": 0.0066, "elapsed": 0.328}
         220 +{"seed": 219, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0008, "elapsed": 0.219}
         221 +{"seed": 220, "count": null, "success": true, "steps": 52, "policy_seconds": 0.0076, "elapsed": 0.58}
         222 +{"seed": 221, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0061, "elapsed": 0.413}
         223 +{"seed": 222, "count": null, "success": true, "steps": 50, "policy_seconds": 0.0056, "elapsed": 0.517}
         224 +{"seed": 223, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0013, "elapsed": 0.211}
         225 +{"seed": 224, "count": null, "success": true, "steps": 58, "policy_seconds": 0.0079, "elapsed": 0.846}
         226 +{"seed": 225, "count": null, "success": true, "steps": 104, "policy_seconds": 0.0159, "elapsed": 1.019}
         227 +{"seed": 226, "count": null, "success": true, "steps": 96, "policy_seconds": 0.0143, "elapsed": 1.165}
         228 +{"seed": 227, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0062, "elapsed": 0.552}
         229 +{"seed": 228, "count": null, "success": true, "steps": 65, "policy_seconds": 0.0065, "elapsed": 0.552}
         230 +{"seed": 229, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0011, "elapsed": 0.171}
         231 +{"seed": 230, "count": null, "success": true, "steps": 45, "policy_seconds": 0.0066, "elapsed": 0.45}
         232 +{"seed": 231, "count": null, "success": true, "steps": 32, "policy_seconds": 0.001, "elapsed": 0.264}
         233 +{"seed": 232, "count": null, "success": true, "steps": 28, "policy_seconds": 0.0012, "elapsed": 0.226}
         234 +{"seed": 233, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0009, "elapsed": 0.223}
         235 +{"seed": 234, "count": null, "success": true, "steps": 48, "policy_seconds": 0.0059, "elapsed": 0.304}
         236 +{"seed": 235, "count": null, "success": true, "steps": 70, "policy_seconds": 0.0055, "elapsed": 0.823}
         237 +{"seed": 236, "count": null, "success": true, "steps": 78, "policy_seconds": 0.0067, "elapsed": 0.633}
         238 +{"seed": 237, "count": null, "success": true, "steps": 130, "policy_seconds": 0.0109, "elapsed": 1.428}
         239 +{"seed": 238, "count": null, "success": true, "steps": 17, "policy_seconds": 0.0009, "elapsed": 0.128}
         240 +{"seed": 239, "count": null, "success": true, "steps": 66, "policy_seconds": 0.0104, "elapsed": 0.775}
         241 +{"seed": 240, "count": null, "success": true, "steps": 88, "policy_seconds": 0.0178, "elapsed": 0.856}
         242 +{"seed": 241, "count": null, "success": true, "steps": 16, "policy_seconds": 0.001, "elapsed": 0.267}
         243 +{"seed": 242, "count": null, "success": true, "steps": 74, "policy_seconds": 0.007, "elapsed": 0.767}
         244 +{"seed": 243, "count": null, "success": true, "steps": 36, "policy_seconds": 0.0019, "elapsed": 0.363}
         245 +{"seed": 244, "count": null, "success": true, "steps": 56, "policy_seconds": 0.0082, "elapsed": 0.358}
         246 +{"seed": 245, "count": null, "success": true, "steps": 44, "policy_seconds": 0.0025, "elapsed": 0.469}
         247 +{"seed": 246, "count": null, "success": true, "steps": 85, "policy_seconds": 0.0164, "elapsed": 0.862}
         248 +{"seed": 247, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0009, "elapsed": 0.216}
         249 +{"seed": 248, "count": null, "success": true, "steps": 58, "policy_seconds": 0.0055, "elapsed": 0.466}
         250 +{"seed": 249, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0095, "elapsed": 0.564}
         251 +{"seed": 250, "count": null, "success": true, "steps": 76, "policy_seconds": 0.007, "elapsed": 0.646}
         252 +{"seed": 251, "count": null, "success": true, "steps": 21, "policy_seconds": 0.0007, "elapsed": 0.115}
         253 +{"seed": 252, "count": null, "success": true, "steps": 105, "policy_seconds": 0.0114, "elapsed": 1.149}
         254 +{"seed": 253, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0043, "elapsed": 0.532}
         255 +{"seed": 254, "count": null, "success": true, "steps": 30, "policy_seconds": 0.001, "elapsed": 0.3}
         256 +{"seed": 255, "count": null, "success": true, "steps": 24, "policy_seconds": 0.001, "elapsed": 0.155}
         257 +{"seed": 256, "count": null, "success": true, "steps": 41, "policy_seconds": 0.0093, "elapsed": 0.555}
         258 +{"seed": 257, "count": null, "success": true, "steps": 42, "policy_seconds": 0.0161, "elapsed": 0.635}
         259 +{"seed": 258, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0073, "elapsed": 0.817}
         260 +{"seed": 259, "count": null, "success": true, "steps": 18, "policy_seconds": 0.0014, "elapsed": 0.164}
         261 +{"seed": 260, "count": null, "success": true, "steps": 48, "policy_seconds": 0.0122, "elapsed": 0.643}
         262 +{"seed": 261, "count": null, "success": true, "steps": 84, "policy_seconds": 0.0092, "elapsed": 0.983}
         263 +{"seed": 262, "count": null, "success": true, "steps": 68, "policy_seconds": 0.0073, "elapsed": 0.655}
         264 +{"seed": 263, "count": null, "success": true, "steps": 58, "policy_seconds": 0.0055, "elapsed": 0.527}
         265 +{"seed": 264, "count": null, "success": true, "steps": 42, "policy_seconds": 0.0012, "elapsed": 0.392}
         266 +{"seed": 265, "count": null, "success": true, "steps": 76, "policy_seconds": 0.0173, "elapsed": 0.872}
         267 +{"seed": 266, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0049, "elapsed": 0.386}
         268 +{"seed": 267, "count": null, "success": true, "steps": 52, "policy_seconds": 0.0051, "elapsed": 0.447}
         269 +{"seed": 268, "count": null, "success": true, "steps": 119, "policy_seconds": 0.0121, "elapsed": 1.357}
         270 +{"seed": 269, "count": null, "success": true, "steps": 69, "policy_seconds": 0.0068, "elapsed": 0.812}
         271 +{"seed": 270, "count": null, "success": true, "steps": 47, "policy_seconds": 0.0062, "elapsed": 0.405}
         272 +{"seed": 271, "count": null, "success": true, "steps": 62, "policy_seconds": 0.0097, "elapsed": 0.546}
         273 +{"seed": 272, "count": null, "success": true, "steps": 18, "policy_seconds": 0.0007, "elapsed": 0.166}
         274 +{"seed": 273, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0009, "elapsed": 0.222}
         275 +{"seed": 274, "count": null, "success": true, "steps": 41, "policy_seconds": 0.0016, "elapsed": 0.296}
         276 +{"seed": 275, "count": null, "success": true, "steps": 35, "policy_seconds": 0.0009, "elapsed": 0.133}
         277 +{"seed": 276, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0011, "elapsed": 0.13}
         278 +{"seed": 277, "count": null, "success": true, "steps": 34, "policy_seconds": 0.0009, "elapsed": 0.156}
         279 +{"seed": 278, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0015, "elapsed": 0.141}
         280 +{"seed": 279, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0048, "elapsed": 0.384}
         281 +{"seed": 280, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0013, "elapsed": 0.203}
         282 +{"seed": 281, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0049, "elapsed": 0.347}
         283 +{"seed": 282, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0067, "elapsed": 0.417}
         284 +{"seed": 283, "count": null, "success": true, "steps": 52, "policy_seconds": 0.0015, "elapsed": 0.312}
         285 +{"seed": 284, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0008, "elapsed": 0.141}
         286 +{"seed": 285, "count": null, "success": true, "steps": 82, "policy_seconds": 0.0094, "elapsed": 0.49}
         287 +{"seed": 286, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0009, "elapsed": 0.165}
         288 +{"seed": 287, "count": null, "success": true, "steps": 93, "policy_seconds": 0.0096, "elapsed": 0.72}
         289 +{"seed": 288, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0007, "elapsed": 0.103}
         290 +{"seed": 289, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0013, "elapsed": 0.17}
         291 +{"seed": 290, "count": null, "success": true, "steps": 37, "policy_seconds": 0.0011, "elapsed": 0.194}
         292 +{"seed": 291, "count": null, "success": true, "steps": 33, "policy_seconds": 0.001, "elapsed": 0.195}
         293 +{"seed": 292, "count": null, "success": true, "steps": 95, "policy_seconds": 0.009, "elapsed": 0.727}
         294 +{"seed": 293, "count": null, "success": true, "steps": 33, "policy_seconds": 0.0009, "elapsed": 0.138}
         295 +{"seed": 294, "count": null, "success": true, "steps": 30, "policy_seconds": 0.0008, "elapsed": 0.123}
         296 +{"seed": 295, "count": null, "success": true, "steps": 50, "policy_seconds": 0.0012, "elapsed": 0.199}
         297 +{"seed": 296, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0008, "elapsed": 0.121}
         298 +{"seed": 297, "count": null, "success": true, "steps": 35, "policy_seconds": 0.0009, "elapsed": 0.202}
         299 +{"seed": 298, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0057, "elapsed": 0.335}
         300 +{"seed": 299, "count": null, "success": true, "steps": 72, "policy_seconds": 0.0061, "elapsed": 0.459}
         301 +{"seed": 300, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0009, "elapsed": 0.105}
         302 +{"seed": 301, "count": null, "success": true, "steps": 50, "policy_seconds": 0.0013, "elapsed": 0.219}
         303 +{"seed": 302, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0076, "elapsed": 0.469}
         304 +{"seed": 303, "count": null, "success": true, "steps": 73, "policy_seconds": 0.0055, "elapsed": 0.456}
         305 +{"seed": 304, "count": null, "success": true, "steps": 57, "policy_seconds": 0.007, "elapsed": 0.45}
         306 +{"seed": 305, "count": null, "success": true, "steps": 29, "policy_seconds": 0.0008, "elapsed": 0.166}
         307 +{"seed": 306, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0098, "elapsed": 0.314}
         308 +{"seed": 307, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0086, "elapsed": 0.335}
         309 +{"seed": 308, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0064, "elapsed": 0.412}
         310 +{"seed": 309, "count": null, "success": true, "steps": 76, "policy_seconds": 0.0073, "elapsed": 0.497}
         311 +{"seed": 310, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0007, "elapsed": 0.119}
         312 +{"seed": 311, "count": null, "success": true, "steps": 55, "policy_seconds": 0.0051, "elapsed": 0.414}
         313 +{"seed": 312, "count": null, "success": true, "steps": 50, "policy_seconds": 0.0015, "elapsed": 0.282}
         314 +{"seed": 313, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0008, "elapsed": 0.102}
         315 +{"seed": 314, "count": null, "success": true, "steps": 39, "policy_seconds": 0.0016, "elapsed": 0.177}
         316 +{"seed": 315, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0012, "elapsed": 0.147}
         317 +{"seed": 316, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0008, "elapsed": 0.142}
         318 +{"seed": 317, "count": null, "success": true, "steps": 19, "policy_seconds": 0.0007, "elapsed": 0.103}
         319 +{"seed": 318, "count": null, "success": true, "steps": 49, "policy_seconds": 0.0013, "elapsed": 0.265}
         320 +{"seed": 319, "count": null, "success": true, "steps": 72, "policy_seconds": 0.0074, "elapsed": 0.462}
         321 +{"seed": 320, "count": null, "success": true, "steps": 19, "policy_seconds": 0.0006, "elapsed": 0.106}
         322 +{"seed": 321, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0042, "elapsed": 0.371}
         323 +{"seed": 322, "count": null, "success": true, "steps": 28, "policy_seconds": 0.0008, "elapsed": 0.143}
         324 +{"seed": 323, "count": null, "success": true, "steps": 44, "policy_seconds": 0.002, "elapsed": 0.372}
         325 +{"seed": 324, "count": null, "success": true, "steps": 85, "policy_seconds": 0.0065, "elapsed": 0.388}
         326 +{"seed": 325, "count": null, "success": true, "steps": 24, "policy_seconds": 0.0007, "elapsed": 0.111}
         327 +{"seed": 326, "count": null, "success": true, "steps": 51, "policy_seconds": 0.0013, "elapsed": 0.255}
         328 +{"seed": 327, "count": null, "success": true, "steps": 37, "policy_seconds": 0.0014, "elapsed": 0.263}
         329 +{"seed": 328, "count": null, "success": true, "steps": 19, "policy_seconds": 0.0006, "elapsed": 0.09}
         330 +{"seed": 329, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0084, "elapsed": 0.379}
         331 +{"seed": 330, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0064, "elapsed": 0.289}
         332 +{"seed": 331, "count": null, "success": true, "steps": 21, "policy_seconds": 0.0008, "elapsed": 0.138}
         333 +{"seed": 332, "count": null, "success": true, "steps": 51, "policy_seconds": 0.0054, "elapsed": 0.321}
         334 +{"seed": 333, "count": null, "success": true, "steps": 17, "policy_seconds": 0.0006, "elapsed": 0.095}
         335 +{"seed": 334, "count": null, "success": true, "steps": 25, "policy_seconds": 0.001, "elapsed": 0.184}
         336 +{"seed": 335, "count": null, "success": true, "steps": 24, "policy_seconds": 0.0008, "elapsed": 0.129}
         337 +{"seed": 336, "count": null, "success": true, "steps": 60, "policy_seconds": 0.005, "elapsed": 0.297}
         338 +{"seed": 337, "count": null, "success": true, "steps": 58, "policy_seconds": 0.0014, "elapsed": 0.233}
         339 +{"seed": 338, "count": null, "success": true, "steps": 23, "policy_seconds": 0.001, "elapsed": 0.081}
         340 +{"seed": 339, "count": null, "success": true, "steps": 36, "policy_seconds": 0.001, "elapsed": 0.162}
         341 +{"seed": 340, "count": null, "success": true, "steps": 19, "policy_seconds": 0.0007, "elapsed": 0.109}
         342 +{"seed": 341, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0066, "elapsed": 0.495}
         343 +{"seed": 342, "count": null, "success": true, "steps": 102, "policy_seconds": 0.0164, "elapsed": 0.804}
         344 +{"seed": 343, "count": null, "success": true, "steps": 29, "policy_seconds": 0.0009, "elapsed": 0.145}
         345 +{"seed": 344, "count": null, "success": true, "steps": 30, "policy_seconds": 0.0009, "elapsed": 0.153}
         346 +{"seed": 345, "count": null, "success": true, "steps": 34, "policy_seconds": 0.0009, "elapsed": 0.182}
         347 +{"seed": 346, "count": null, "success": true, "steps": 84, "policy_seconds": 0.0054, "elapsed": 0.462}
         348 +{"seed": 347, "count": null, "success": true, "steps": 47, "policy_seconds": 0.0064, "elapsed": 0.233}
         349 +{"seed": 348, "count": null, "success": true, "steps": 30, "policy_seconds": 0.0009, "elapsed": 0.14}
         350 +{"seed": 349, "count": null, "success": true, "steps": 42, "policy_seconds": 0.0019, "elapsed": 0.277}
         351 +{"seed": 350, "count": null, "success": true, "steps": 41, "policy_seconds": 0.0062, "elapsed": 0.256}
         352 +{"seed": 351, "count": null, "success": true, "steps": 69, "policy_seconds": 0.0075, "elapsed": 0.45}
         353 +{"seed": 352, "count": null, "success": true, "steps": 38, "policy_seconds": 0.001, "elapsed": 0.182}
         354 +{"seed": 353, "count": null, "success": true, "steps": 28, "policy_seconds": 0.0008, "elapsed": 0.144}
         355 +{"seed": 354, "count": null, "success": true, "steps": 110, "policy_seconds": 0.0132, "elapsed": 0.832}
         356 +{"seed": 355, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0012, "elapsed": 0.172}
         357 +{"seed": 356, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0008, "elapsed": 0.117}
         358 +{"seed": 357, "count": null, "success": true, "steps": 78, "policy_seconds": 0.0078, "elapsed": 0.463}
         359 +{"seed": 358, "count": null, "success": true, "steps": 55, "policy_seconds": 0.0093, "elapsed": 0.419}
         360 +{"seed": 359, "count": null, "success": true, "steps": 48, "policy_seconds": 0.0069, "elapsed": 0.259}
         361 +{"seed": 360, "count": null, "success": true, "steps": 67, "policy_seconds": 0.0081, "elapsed": 0.343}
         362 +{"seed": 361, "count": null, "success": true, "steps": 83, "policy_seconds": 0.0155, "elapsed": 0.64}
         363 +{"seed": 362, "count": null, "success": true, "steps": 88, "policy_seconds": 0.0239, "elapsed": 0.682}
         364 +{"seed": 363, "count": null, "success": true, "steps": 45, "policy_seconds": 0.0014, "elapsed": 0.158}
         365 +{"seed": 364, "count": null, "success": true, "steps": 33, "policy_seconds": 0.0013, "elapsed": 0.158}
         366 +{"seed": 365, "count": null, "success": true, "steps": 43, "policy_seconds": 0.0012, "elapsed": 0.188}
         367 +{"seed": 366, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0007, "elapsed": 0.085}
         368 +{"seed": 367, "count": null, "success": true, "steps": 109, "policy_seconds": 0.016, "elapsed": 0.945}
         369 +{"seed": 368, "count": null, "success": true, "steps": 89, "policy_seconds": 0.0151, "elapsed": 0.505}
         370 +{"seed": 369, "count": null, "success": true, "steps": 127, "policy_seconds": 0.0115, "elapsed": 0.943}
         371 +{"seed": 370, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0061, "elapsed": 0.299}
         372 +{"seed": 371, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0017, "elapsed": 0.186}
         373 +{"seed": 372, "count": null, "success": true, "steps": 82, "policy_seconds": 0.0071, "elapsed": 0.593}
         374 +{"seed": 373, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0052, "elapsed": 0.268}
         375 +{"seed": 374, "count": null, "success": true, "steps": 53, "policy_seconds": 0.0076, "elapsed": 0.433}
         376 +{"seed": 375, "count": null, "success": true, "steps": 30, "policy_seconds": 0.0009, "elapsed": 0.15}
         377 +{"seed": 376, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0059, "elapsed": 0.351}
         378 +{"seed": 377, "count": null, "success": true, "steps": 75, "policy_seconds": 0.0089, "elapsed": 0.382}
         379 +{"seed": 378, "count": null, "success": true, "steps": 84, "policy_seconds": 0.0077, "elapsed": 0.514}
         380 +{"seed": 379, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0075, "elapsed": 0.357}
         381 +{"seed": 380, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0056, "elapsed": 0.251}
         382 +{"seed": 381, "count": null, "success": true, "steps": 85, "policy_seconds": 0.0095, "elapsed": 0.621}
         383 +{"seed": 382, "count": null, "success": true, "steps": 45, "policy_seconds": 0.0012, "elapsed": 0.235}
         384 +{"seed": 383, "count": null, "success": true, "steps": 37, "policy_seconds": 0.0011, "elapsed": 0.114}
         385 +{"seed": 384, "count": null, "success": true, "steps": 39, "policy_seconds": 0.001, "elapsed": 0.168}
         386 +{"seed": 385, "count": null, "success": true, "steps": 91, "policy_seconds": 0.009, "elapsed": 0.661}
         387 +{"seed": 386, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0047, "elapsed": 0.253}
         388 +{"seed": 387, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0053, "elapsed": 0.453}
         389 +{"seed": 388, "count": null, "success": true, "steps": 44, "policy_seconds": 0.0063, "elapsed": 0.397}
         390 +{"seed": 389, "count": null, "success": true, "steps": 31, "policy_seconds": 0.001, "elapsed": 0.318}
         391 +{"seed": 390, "count": null, "success": true, "steps": 67, "policy_seconds": 0.0061, "elapsed": 0.433}
         392 +{"seed": 391, "count": null, "success": true, "steps": 41, "policy_seconds": 0.0012, "elapsed": 0.249}
         393 +{"seed": 392, "count": null, "success": true, "steps": 29, "policy_seconds": 0.0016, "elapsed": 0.16}
         394 +{"seed": 393, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0014, "elapsed": 0.122}
         395 +{"seed": 394, "count": null, "success": true, "steps": 19, "policy_seconds": 0.0006, "elapsed": 0.077}
         396 +{"seed": 395, "count": null, "success": true, "steps": 46, "policy_seconds": 0.0017, "elapsed": 0.299}
         397 +{"seed": 396, "count": null, "success": true, "steps": 83, "policy_seconds": 0.0063, "elapsed": 0.498}
         398 +{"seed": 397, "count": null, "success": true, "steps": 62, "policy_seconds": 0.0082, "elapsed": 0.47}
         399 +{"seed": 398, "count": null, "success": true, "steps": 70, "policy_seconds": 0.0066, "elapsed": 0.527}
         400 +{"seed": 399, "count": null, "success": true, "steps": 89, "policy_seconds": 0.0109, "elapsed": 0.607}
         401 +{"seed": 400, "count": null, "success": true, "steps": 80, "policy_seconds": 0.0103, "elapsed": 0.435}
         402 +{"seed": 401, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0054, "elapsed": 0.387}
         403 +{"seed": 402, "count": null, "success": true, "steps": 106, "policy_seconds": 0.0141, "elapsed": 0.605}
         404 +{"seed": 403, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0012, "elapsed": 0.146}
         405 +{"seed": 404, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0091, "elapsed": 0.515}
         406 +{"seed": 405, "count": null, "success": true, "steps": 39, "policy_seconds": 0.0016, "elapsed": 0.353}
         407 +{"seed": 406, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0078, "elapsed": 0.53}
         408 +{"seed": 407, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0008, "elapsed": 0.109}
         409 +{"seed": 408, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0011, "elapsed": 0.135}
         410 +{"seed": 409, "count": null, "success": true, "steps": 34, "policy_seconds": 0.001, "elapsed": 0.182}
         411 +{"seed": 410, "count": null, "success": true, "steps": 56, "policy_seconds": 0.0057, "elapsed": 0.404}
         412 +{"seed": 411, "count": null, "success": true, "steps": 29, "policy_seconds": 0.0009, "elapsed": 0.099}
         413 +{"seed": 412, "count": null, "success": true, "steps": 69, "policy_seconds": 0.0074, "elapsed": 0.362}
         414 +{"seed": 413, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0009, "elapsed": 0.167}
         415 +{"seed": 414, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0083, "elapsed": 0.487}
         416 +{"seed": 415, "count": null, "success": true, "steps": 67, "policy_seconds": 0.0098, "elapsed": 0.312}
         417 +{"seed": 416, "count": null, "success": true, "steps": 51, "policy_seconds": 0.0058, "elapsed": 0.375}
         418 +{"seed": 417, "count": null, "success": true, "steps": 28, "policy_seconds": 0.0008, "elapsed": 0.195}
         419 +{"seed": 418, "count": null, "success": true, "steps": 21, "policy_seconds": 0.001, "elapsed": 0.178}
         420 +{"seed": 419, "count": null, "success": true, "steps": 28, "policy_seconds": 0.0018, "elapsed": 0.23}
         421 +{"seed": 420, "count": null, "success": true, "steps": 48, "policy_seconds": 0.0058, "elapsed": 0.199}
         422 +{"seed": 421, "count": null, "success": true, "steps": 42, "policy_seconds": 0.0012, "elapsed": 0.156}
         423 +{"seed": 422, "count": null, "success": true, "steps": 33, "policy_seconds": 0.0009, "elapsed": 0.166}
         424 +{"seed": 423, "count": null, "success": true, "steps": 34, "policy_seconds": 0.0012, "elapsed": 0.17}
         425 +{"seed": 424, "count": null, "success": true, "steps": 21, "policy_seconds": 0.0009, "elapsed": 0.069}
         426 +{"seed": 425, "count": null, "success": true, "steps": 31, "policy_seconds": 0.001, "elapsed": 0.133}
         427 +{"seed": 426, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0007, "elapsed": 0.162}
         428 +{"seed": 427, "count": null, "success": true, "steps": 52, "policy_seconds": 0.0067, "elapsed": 0.391}
         429 +{"seed": 428, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0009, "elapsed": 0.147}
         430 +{"seed": 429, "count": null, "success": true, "steps": 33, "policy_seconds": 0.001, "elapsed": 0.194}
         431 +{"seed": 430, "count": null, "success": true, "steps": 30, "policy_seconds": 0.0009, "elapsed": 0.158}
         432 +{"seed": 431, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0083, "elapsed": 0.499}
         433 +{"seed": 432, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0017, "elapsed": 0.229}
         434 +{"seed": 433, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0008, "elapsed": 0.138}
         435 +{"seed": 434, "count": null, "success": true, "steps": 28, "policy_seconds": 0.0018, "elapsed": 0.165}
         436 +{"seed": 435, "count": null, "success": true, "steps": 52, "policy_seconds": 0.0055, "elapsed": 0.31}
diff --git a/probe_reach_edges.json b/probe_reach_edges.json
index e69de29..cb070a1 100644
--- a/probe_reach_edges.json
+++ b/probe_reach_edges.json
@@ -0,0 +1 @@
           1 +{"inaccessible": [], "edges": []}
diff --git a/test_counts_scene_v3.jsonl b/test_counts_scene_v3.jsonl
index d7cd708..128a448 100644
--- a/test_counts_scene_v3.jsonl
+++ b/test_counts_scene_v3.jsonl
@@ -97,3 +97,5 @@
   97     97  {"count": 4, "seed": 96, "steps": 59, "success": true, "seconds": 3.98}
   98     98  {"count": 4, "seed": 97, "steps": 147, "success": true, "seconds": 6.48}
   99     99  {"count": 4, "seed": 98, "steps": 105, "success": true, "seconds": 6.08}
         100 +{"count": 4, "seed": 99, "steps": 100, "success": true, "seconds": 11.44}
         101 +{"count": 5, "seed": 0, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=5; it likely exceeds the family's feasible object count. Lower the configured counts."}
diff --git a/test_counts_scene_v3.log b/test_counts_scene_v3.log
index d7cd708..128a448 100644
--- a/test_counts_scene_v3.log
+++ b/test_counts_scene_v3.log
@@ -97,3 +97,5 @@
   97     97  {"count": 4, "seed": 96, "steps": 59, "success": true, "seconds": 3.98}
   98     98  {"count": 4, "seed": 97, "steps": 147, "success": true, "seconds": 6.48}
   99     99  {"count": 4, "seed": 98, "steps": 105, "success": true, "seconds": 6.08}
         100 +{"count": 4, "seed": 99, "steps": 100, "success": true, "seconds": 11.44}
         101 +{"count": 5, "seed": 0, "error": "Environment server error: ValueError: Obstruction2DEnv could not build an instance with num_obstructions=5; it likely exceeds the family's feasible object count. Lower the configured counts."}
diff --git a/validate_count4_later.jsonl b/validate_count4_later.jsonl
index 9166a17..5cc8711 100644
--- a/validate_count4_later.jsonl
+++ b/validate_count4_later.jsonl
@@ -33,3 +33,68 @@
   33     33  {"seed": 132, "count": 4, "success": true, "steps": 102, "policy_seconds": 0.0266, "elapsed": 2.654}
   34     34  {"seed": 133, "count": 4, "success": true, "steps": 124, "policy_seconds": 0.0294, "elapsed": 2.605}
   35     35  {"seed": 134, "count": 4, "success": true, "steps": 87, "policy_seconds": 0.0153, "elapsed": 2.037}
          36 +{"seed": 135, "count": 4, "success": true, "steps": 141, "policy_seconds": 0.0265, "elapsed": 4.411}
          37 +{"seed": 136, "count": 4, "success": true, "steps": 98, "policy_seconds": 0.0227, "elapsed": 1.533}
          38 +{"seed": 137, "count": 4, "success": true, "steps": 98, "policy_seconds": 0.0262, "elapsed": 1.637}
          39 +{"seed": 138, "count": 4, "success": true, "steps": 111, "policy_seconds": 0.0281, "elapsed": 1.028}
          40 +{"seed": 139, "count": 4, "success": true, "steps": 77, "policy_seconds": 0.0136, "elapsed": 0.677}
          41 +{"seed": 140, "count": 4, "success": true, "steps": 110, "policy_seconds": 0.0145, "elapsed": 0.97}
          42 +{"seed": 141, "count": 4, "success": true, "steps": 88, "policy_seconds": 0.0191, "elapsed": 0.738}
          43 +{"seed": 142, "count": 4, "success": true, "steps": 65, "policy_seconds": 0.0158, "elapsed": 0.552}
          44 +{"seed": 143, "count": 4, "success": true, "steps": 113, "policy_seconds": 0.0251, "elapsed": 0.997}
          45 +{"seed": 144, "count": 4, "success": true, "steps": 76, "policy_seconds": 0.0137, "elapsed": 0.653}
          46 +{"seed": 145, "count": 4, "success": true, "steps": 60, "policy_seconds": 0.013, "elapsed": 0.525}
          47 +{"seed": 146, "count": 4, "success": true, "steps": 71, "policy_seconds": 0.0163, "elapsed": 0.636}
          48 +{"seed": 147, "count": 4, "success": true, "steps": 88, "policy_seconds": 0.0337, "elapsed": 0.813}
          49 +{"seed": 148, "count": 4, "success": true, "steps": 54, "policy_seconds": 0.0137, "elapsed": 0.48}
          50 +{"seed": 149, "count": 4, "success": true, "steps": 142, "policy_seconds": 0.0334, "elapsed": 1.228}
          51 +{"seed": 150, "count": 4, "success": true, "steps": 93, "policy_seconds": 0.0179, "elapsed": 0.806}
          52 +{"seed": 151, "count": 4, "success": true, "steps": 93, "policy_seconds": 0.0147, "elapsed": 0.786}
          53 +{"seed": 152, "count": 4, "success": true, "steps": 133, "policy_seconds": 0.0348, "elapsed": 1.139}
          54 +{"seed": 153, "count": 4, "success": true, "steps": 73, "policy_seconds": 0.0145, "elapsed": 0.649}
          55 +{"seed": 154, "count": 4, "success": true, "steps": 74, "policy_seconds": 0.0161, "elapsed": 0.602}
          56 +{"seed": 155, "count": 4, "success": true, "steps": 134, "policy_seconds": 0.0308, "elapsed": 1.173}
          57 +{"seed": 156, "count": 4, "success": true, "steps": 95, "policy_seconds": 0.0304, "elapsed": 0.835}
          58 +{"seed": 157, "count": 4, "success": true, "steps": 92, "policy_seconds": 0.0134, "elapsed": 0.755}
          59 +{"seed": 158, "count": 4, "success": true, "steps": 50, "policy_seconds": 0.0114, "elapsed": 0.421}
          60 +{"seed": 159, "count": 4, "success": true, "steps": 65, "policy_seconds": 0.0156, "elapsed": 0.57}
          61 +{"seed": 160, "count": 4, "success": true, "steps": 92, "policy_seconds": 0.0171, "elapsed": 0.802}
          62 +{"seed": 161, "count": 4, "success": true, "steps": 112, "policy_seconds": 0.0342, "elapsed": 1.048}
          63 +{"seed": 162, "count": 4, "success": true, "steps": 90, "policy_seconds": 0.0333, "elapsed": 0.773}
          64 +{"seed": 163, "count": 4, "success": true, "steps": 92, "policy_seconds": 0.0324, "elapsed": 0.778}
          65 +{"seed": 164, "count": 4, "success": true, "steps": 84, "policy_seconds": 0.0259, "elapsed": 0.287}
          66 +{"seed": 165, "count": 4, "success": true, "steps": 123, "policy_seconds": 0.018, "elapsed": 0.388}
          67 +{"seed": 166, "count": 4, "success": true, "steps": 74, "policy_seconds": 0.0139, "elapsed": 0.22}
          68 +{"seed": 167, "count": 4, "success": true, "steps": 79, "policy_seconds": 0.0178, "elapsed": 0.263}
          69 +{"seed": 168, "count": 4, "success": true, "steps": 110, "policy_seconds": 0.0185, "elapsed": 0.357}
          70 +{"seed": 169, "count": 4, "success": true, "steps": 86, "policy_seconds": 0.01, "elapsed": 0.28}
          71 +{"seed": 170, "count": 4, "success": true, "steps": 90, "policy_seconds": 0.0208, "elapsed": 0.289}
          72 +{"seed": 171, "count": 4, "success": true, "steps": 140, "policy_seconds": 0.0377, "elapsed": 0.471}
          73 +{"seed": 172, "count": 4, "success": true, "steps": 106, "policy_seconds": 0.0186, "elapsed": 0.331}
          74 +{"seed": 173, "count": 4, "success": true, "steps": 77, "policy_seconds": 0.0173, "elapsed": 0.242}
          75 +{"seed": 174, "count": 4, "success": true, "steps": 71, "policy_seconds": 0.0225, "elapsed": 0.229}
          76 +{"seed": 175, "count": 4, "success": true, "steps": 76, "policy_seconds": 0.0123, "elapsed": 0.226}
          77 +{"seed": 176, "count": 4, "success": true, "steps": 82, "policy_seconds": 0.014, "elapsed": 0.253}
          78 +{"seed": 177, "count": 4, "success": true, "steps": 91, "policy_seconds": 0.0151, "elapsed": 0.279}
          79 +{"seed": 178, "count": 4, "success": true, "steps": 72, "policy_seconds": 0.0147, "elapsed": 0.223}
          80 +{"seed": 179, "count": 4, "success": true, "steps": 65, "policy_seconds": 0.012, "elapsed": 0.209}
          81 +{"seed": 180, "count": 4, "success": true, "steps": 62, "policy_seconds": 0.0101, "elapsed": 0.204}
          82 +{"seed": 181, "count": 4, "success": true, "steps": 73, "policy_seconds": 0.0163, "elapsed": 0.243}
          83 +{"seed": 182, "count": 4, "success": true, "steps": 90, "policy_seconds": 0.0249, "elapsed": 0.309}
          84 +{"seed": 183, "count": 4, "success": true, "steps": 62, "policy_seconds": 0.0112, "elapsed": 0.209}
          85 +{"seed": 184, "count": 4, "success": true, "steps": 110, "policy_seconds": 0.0295, "elapsed": 0.518}
          86 +{"seed": 185, "count": 4, "success": true, "steps": 59, "policy_seconds": 0.0153, "elapsed": 0.469}
          87 +{"seed": 186, "count": 4, "success": true, "steps": 78, "policy_seconds": 0.0143, "elapsed": 0.612}
          88 +{"seed": 187, "count": 4, "success": true, "steps": 115, "policy_seconds": 0.0242, "elapsed": 1.734}
          89 +{"seed": 188, "count": 4, "success": true, "steps": 119, "policy_seconds": 0.0366, "elapsed": 1.837}
          90 +{"seed": 189, "count": 4, "success": true, "steps": 52, "policy_seconds": 0.0117, "elapsed": 0.745}
          91 +{"seed": 190, "count": 4, "success": true, "steps": 109, "policy_seconds": 0.0252, "elapsed": 1.584}
          92 +{"seed": 191, "count": 4, "success": true, "steps": 76, "policy_seconds": 0.0311, "elapsed": 1.213}
          93 +{"seed": 192, "count": 4, "success": true, "steps": 95, "policy_seconds": 0.0265, "elapsed": 1.492}
          94 +{"seed": 193, "count": 4, "success": true, "steps": 68, "policy_seconds": 0.0089, "elapsed": 1.176}
          95 +{"seed": 194, "count": 4, "success": true, "steps": 61, "policy_seconds": 0.0148, "elapsed": 0.935}
          96 +{"seed": 195, "count": 4, "success": true, "steps": 133, "policy_seconds": 0.0225, "elapsed": 2.063}
          97 +{"seed": 196, "count": 4, "success": true, "steps": 56, "policy_seconds": 0.0113, "elapsed": 0.855}
          98 +{"seed": 197, "count": 4, "success": true, "steps": 118, "policy_seconds": 0.0265, "elapsed": 1.834}
          99 +{"seed": 198, "count": 4, "success": true, "steps": 98, "policy_seconds": 0.0263, "elapsed": 2.104}
         100 +{"seed": 199, "count": 4, "success": true, "steps": 34, "policy_seconds": 0.0032, "elapsed": 0.747}
```

</details>

<a id="C015"></a>
### C015 · Use extreme edge grasps only when ordinary grasp offsets cannot reach

Commit `64aee982b0d765fcdfeca16866ce03112f61e524`; parents: 04cf477a35413b414056a4e756cd7a9b029a1df1. Recorded author date: 2026-09-21T17:43:28Z.

File roles (automatic): policy, setup/other.

- [E0121](01_timeline.md#E0121): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C015_64aee98_approach.py) · [Exact all-file diff](evidence/diffs/C015_64aee98.diff)

[Previous saved controller snapshot](evidence/versions/C014_04cf477_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5449220..26c3893 100644
--- a/approach.py
+++ b/approach.py
@@ -46,8 +46,12 @@ class GeneratedApproach:
   46     46          return bad
   47     47  
   48     48      def offsets(self,x,px,w):
   49        -        low=max(.1002-x,.1002-px,-.034)
   50        -        high=min(1.5178-x,1.5178-px,w+.034)
          49 +        low=max(.1002-x,.1002-px,-.022)
          50 +        high=min(1.5178-x,1.5178-px,w+.022)
          51 +        if low>high:
          52 +            # Near a wall, retain at least 1 mm of gripper overlap.
          53 +            low=max(.1002-x,.1002-px,-.034)
          54 +            high=min(1.5178-x,1.5178-px,w+.034)
   51     55          if low>high:return []
   52     56          return sorted(set([max(low,min(high,w/2))]+[float(z) for z in np.linspace(low,high,7)]),key=lambda z:abs(z-w/2))
   53     57  
diff --git a/final_count4.jsonl b/final_count4.jsonl
index c9193db..381692a 100644
--- a/final_count4.jsonl
+++ b/final_count4.jsonl
@@ -80,3 +80,20 @@
   80     80  {"seed": 79, "count": 4, "success": true, "steps": 63, "policy_seconds": 0.0114, "elapsed": 0.494}
   81     81  {"seed": 80, "count": 4, "success": true, "steps": 153, "policy_seconds": 0.0427, "elapsed": 1.427}
   82     82  {"seed": 81, "count": 4, "success": true, "steps": 78, "policy_seconds": 0.0131, "elapsed": 0.56}
          83 +{"seed": 82, "count": 4, "success": true, "steps": 69, "policy_seconds": 0.0101, "elapsed": 0.79}
          84 +{"seed": 83, "count": 4, "success": true, "steps": 140, "policy_seconds": 0.0218, "elapsed": 2.074}
          85 +{"seed": 84, "count": 4, "success": true, "steps": 65, "policy_seconds": 0.0149, "elapsed": 0.808}
          86 +{"seed": 85, "count": 4, "success": true, "steps": 126, "policy_seconds": 0.0252, "elapsed": 1.396}
          87 +{"seed": 86, "count": 4, "success": true, "steps": 86, "policy_seconds": 0.0217, "elapsed": 0.718}
          88 +{"seed": 87, "count": 4, "success": true, "steps": 98, "policy_seconds": 0.0204, "elapsed": 0.843}
          89 +{"seed": 88, "count": 4, "success": true, "steps": 110, "policy_seconds": 0.0206, "elapsed": 0.766}
          90 +{"seed": 89, "count": 4, "success": true, "steps": 98, "policy_seconds": 0.0204, "elapsed": 0.777}
          91 +{"seed": 90, "count": 4, "success": true, "steps": 57, "policy_seconds": 0.0144, "elapsed": 0.415}
          92 +{"seed": 91, "count": 4, "success": true, "steps": 102, "policy_seconds": 0.0185, "elapsed": 0.758}
          93 +{"seed": 92, "count": 4, "success": true, "steps": 82, "policy_seconds": 0.0159, "elapsed": 0.516}
          94 +{"seed": 93, "count": 4, "success": true, "steps": 100, "policy_seconds": 0.0146, "elapsed": 0.318}
          95 +{"seed": 94, "count": 4, "success": true, "steps": 68, "policy_seconds": 0.014, "elapsed": 0.208}
          96 +{"seed": 95, "count": 4, "success": true, "steps": 87, "policy_seconds": 0.029, "elapsed": 0.301}
          97 +{"seed": 96, "count": 4, "success": true, "steps": 59, "policy_seconds": 0.011, "elapsed": 0.183}
          98 +{"seed": 97, "count": 4, "success": true, "steps": 147, "policy_seconds": 0.0273, "elapsed": 0.44}
          99 +{"seed": 98, "count": 4, "success": true, "steps": 105, "policy_seconds": 0.0226, "elapsed": 0.328}
diff --git a/final_defaults.jsonl b/final_defaults.jsonl
index 54b1323..d48fcd2 100644
--- a/final_defaults.jsonl
+++ b/final_defaults.jsonl
@@ -434,3 +434,67 @@
  434    434  {"seed": 433, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0008, "elapsed": 0.138}
  435    435  {"seed": 434, "count": null, "success": true, "steps": 28, "policy_seconds": 0.0018, "elapsed": 0.165}
  436    436  {"seed": 435, "count": null, "success": true, "steps": 52, "policy_seconds": 0.0055, "elapsed": 0.31}
         437 +{"seed": 436, "count": null, "success": true, "steps": 80, "policy_seconds": 0.0187, "elapsed": 0.867}
         438 +{"seed": 437, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0051, "elapsed": 0.4}
         439 +{"seed": 438, "count": null, "success": true, "steps": 49, "policy_seconds": 0.0099, "elapsed": 0.554}
         440 +{"seed": 439, "count": null, "success": true, "steps": 35, "policy_seconds": 0.0014, "elapsed": 0.355}
         441 +{"seed": 440, "count": null, "success": true, "steps": 21, "policy_seconds": 0.0007, "elapsed": 0.171}
         442 +{"seed": 441, "count": null, "success": true, "steps": 72, "policy_seconds": 0.0057, "elapsed": 0.739}
         443 +{"seed": 442, "count": null, "success": true, "steps": 20, "policy_seconds": 0.001, "elapsed": 0.164}
         444 +{"seed": 443, "count": null, "success": true, "steps": 38, "policy_seconds": 0.001, "elapsed": 0.206}
         445 +{"seed": 444, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0071, "elapsed": 0.671}
         446 +{"seed": 445, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0008, "elapsed": 0.155}
         447 +{"seed": 446, "count": null, "success": true, "steps": 50, "policy_seconds": 0.0013, "elapsed": 0.418}
         448 +{"seed": 447, "count": null, "success": true, "steps": 57, "policy_seconds": 0.004, "elapsed": 0.415}
         449 +{"seed": 448, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0083, "elapsed": 0.513}
         450 +{"seed": 449, "count": null, "success": true, "steps": 71, "policy_seconds": 0.0081, "elapsed": 0.605}
         451 +{"seed": 450, "count": null, "success": true, "steps": 29, "policy_seconds": 0.001, "elapsed": 0.27}
         452 +{"seed": 451, "count": null, "success": true, "steps": 19, "policy_seconds": 0.0014, "elapsed": 0.205}
         453 +{"seed": 452, "count": null, "success": true, "steps": 37, "policy_seconds": 0.0014, "elapsed": 0.272}
         454 +{"seed": 453, "count": null, "success": true, "steps": 92, "policy_seconds": 0.0133, "elapsed": 0.937}
         455 +{"seed": 454, "count": null, "success": true, "steps": 40, "policy_seconds": 0.0015, "elapsed": 0.316}
         456 +{"seed": 455, "count": null, "success": true, "steps": 71, "policy_seconds": 0.0074, "elapsed": 0.809}
         457 +{"seed": 456, "count": null, "success": true, "steps": 58, "policy_seconds": 0.005, "elapsed": 0.422}
         458 +{"seed": 457, "count": null, "success": true, "steps": 28, "policy_seconds": 0.0009, "elapsed": 0.188}
         459 +{"seed": 458, "count": null, "success": true, "steps": 42, "policy_seconds": 0.0011, "elapsed": 0.28}
         460 +{"seed": 459, "count": null, "success": true, "steps": 51, "policy_seconds": 0.0052, "elapsed": 0.423}
         461 +{"seed": 460, "count": null, "success": true, "steps": 31, "policy_seconds": 0.001, "elapsed": 0.236}
         462 +{"seed": 461, "count": null, "success": true, "steps": 36, "policy_seconds": 0.0019, "elapsed": 0.31}
         463 +{"seed": 462, "count": null, "success": true, "steps": 75, "policy_seconds": 0.0054, "elapsed": 0.509}
         464 +{"seed": 463, "count": null, "success": true, "steps": 76, "policy_seconds": 0.0107, "elapsed": 0.583}
         465 +{"seed": 464, "count": null, "success": true, "steps": 24, "policy_seconds": 0.0007, "elapsed": 0.112}
         466 +{"seed": 465, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0009, "elapsed": 0.154}
         467 +{"seed": 466, "count": null, "success": true, "steps": 76, "policy_seconds": 0.0062, "elapsed": 0.357}
         468 +{"seed": 467, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0007, "elapsed": 0.104}
         469 +{"seed": 468, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0014, "elapsed": 0.308}
         470 +{"seed": 469, "count": null, "success": true, "steps": 18, "policy_seconds": 0.0006, "elapsed": 0.099}
         471 +{"seed": 470, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0069, "elapsed": 0.527}
         472 +{"seed": 471, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0009, "elapsed": 0.162}
         473 +{"seed": 472, "count": null, "success": true, "steps": 35, "policy_seconds": 0.0011, "elapsed": 0.194}
         474 +{"seed": 473, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0007, "elapsed": 0.08}
         475 +{"seed": 474, "count": null, "success": true, "steps": 24, "policy_seconds": 0.0007, "elapsed": 0.097}
         476 +{"seed": 475, "count": null, "success": true, "steps": 78, "policy_seconds": 0.0075, "elapsed": 0.4}
         477 +{"seed": 476, "count": null, "success": true, "steps": 93, "policy_seconds": 0.0125, "elapsed": 0.781}
         478 +{"seed": 477, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0053, "elapsed": 0.409}
         479 +{"seed": 478, "count": null, "success": true, "steps": 15, "policy_seconds": 0.0005, "elapsed": 0.063}
         480 +{"seed": 479, "count": null, "success": true, "steps": 55, "policy_seconds": 0.0022, "elapsed": 0.283}
         481 +{"seed": 480, "count": null, "success": true, "steps": 102, "policy_seconds": 0.0116, "elapsed": 0.681}
         482 +{"seed": 481, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0011, "elapsed": 0.153}
         483 +{"seed": 482, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0007, "elapsed": 0.11}
         484 +{"seed": 483, "count": null, "success": true, "steps": 24, "policy_seconds": 0.0007, "elapsed": 0.098}
         485 +{"seed": 484, "count": null, "success": true, "steps": 88, "policy_seconds": 0.0152, "elapsed": 0.65}
         486 +{"seed": 485, "count": null, "success": true, "steps": 40, "policy_seconds": 0.0109, "elapsed": 0.212}
         487 +{"seed": 486, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0011, "elapsed": 0.159}
         488 +{"seed": 487, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0012, "elapsed": 0.153}
         489 +{"seed": 488, "count": null, "success": true, "steps": 135, "policy_seconds": 0.014, "elapsed": 1.047}
         490 +{"seed": 489, "count": null, "success": true, "steps": 80, "policy_seconds": 0.0164, "elapsed": 0.511}
         491 +{"seed": 490, "count": null, "success": true, "steps": 70, "policy_seconds": 0.0061, "elapsed": 0.433}
         492 +{"seed": 491, "count": null, "success": true, "steps": 58, "policy_seconds": 0.0053, "elapsed": 0.393}
         493 +{"seed": 492, "count": null, "success": true, "steps": 77, "policy_seconds": 0.008, "elapsed": 0.472}
         494 +{"seed": 493, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0092, "elapsed": 0.365}
         495 +{"seed": 494, "count": null, "success": true, "steps": 51, "policy_seconds": 0.0066, "elapsed": 0.386}
         496 +{"seed": 495, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0007, "elapsed": 0.124}
         497 +{"seed": 496, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0009, "elapsed": 0.167}
         498 +{"seed": 497, "count": null, "success": true, "steps": 21, "policy_seconds": 0.0007, "elapsed": 0.099}
         499 +{"seed": 498, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0061, "elapsed": 0.372}
         500 +{"seed": 499, "count": null, "success": true, "steps": 111, "policy_seconds": 0.0132, "elapsed": 0.72}
```

</details>

<a id="C016"></a>
### C016 · Record final regression evidence and add extreme workspace-edge search

Commit `29518eb3545b9c0f7b352d23c86da968224cd617`; parents: 64aee982b0d765fcdfeca16866ce03112f61e524. Recorded author date: 2026-09-21T17:45:49Z.

File roles (automatic): diagnostic/test, setup/other.

- [E0128](01_timeline.md#E0128): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C016_29518eb.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/final_count4.jsonl b/final_count4.jsonl
index 381692a..babaa40 100644
--- a/final_count4.jsonl
+++ b/final_count4.jsonl
@@ -97,3 +97,4 @@
   97     97  {"seed": 96, "count": 4, "success": true, "steps": 59, "policy_seconds": 0.011, "elapsed": 0.183}
   98     98  {"seed": 97, "count": 4, "success": true, "steps": 147, "policy_seconds": 0.0273, "elapsed": 0.44}
   99     99  {"seed": 98, "count": 4, "success": true, "steps": 105, "policy_seconds": 0.0226, "elapsed": 0.328}
         100 +{"seed": 99, "count": 4, "success": true, "steps": 100, "policy_seconds": 0.017, "elapsed": 0.721}
diff --git a/final_edge_regression.jsonl b/final_edge_regression.jsonl
new file mode 100644
index 0000000..65541fa
--- /dev/null
+++ b/final_edge_regression.jsonl
@@ -0,0 +1,20 @@
           1 +{"seed": 380, "count": 3, "success": true, "steps": 88, "policy_seconds": 0.0204, "elapsed": 0.731}
           2 +{"seed": 381, "count": 3, "success": true, "steps": 100, "policy_seconds": 0.0165, "elapsed": 0.6}
           3 +{"seed": 382, "count": 3, "success": true, "steps": 71, "policy_seconds": 0.0103, "elapsed": 0.206}
           4 +{"seed": 383, "count": 3, "success": true, "steps": 59, "policy_seconds": 0.011, "elapsed": 0.183}
           5 +{"seed": 384, "count": 3, "success": true, "steps": 112, "policy_seconds": 0.0209, "elapsed": 0.341}
           6 +{"seed": 385, "count": 3, "success": true, "steps": 66, "policy_seconds": 0.008, "elapsed": 0.205}
           7 +{"seed": 386, "count": 3, "success": true, "steps": 84, "policy_seconds": 0.0117, "elapsed": 0.236}
           8 +{"seed": 387, "count": 3, "success": true, "steps": 80, "policy_seconds": 0.0218, "elapsed": 0.242}
           9 +{"seed": 388, "count": 3, "success": true, "steps": 35, "policy_seconds": 0.0023, "elapsed": 0.091}
          10 +{"seed": 389, "count": 3, "success": true, "steps": 76, "policy_seconds": 0.0119, "elapsed": 0.243}
          11 +{"seed": 390, "count": 3, "success": true, "steps": 50, "policy_seconds": 0.0094, "elapsed": 0.157}
          12 +{"seed": 391, "count": 3, "success": true, "steps": 70, "policy_seconds": 0.0205, "elapsed": 0.217}
          13 +{"seed": 392, "count": 3, "success": true, "steps": 26, "policy_seconds": 0.0022, "elapsed": 0.082}
          14 +{"seed": 393, "count": 3, "success": true, "steps": 69, "policy_seconds": 0.012, "elapsed": 0.214}
          15 +{"seed": 394, "count": 3, "success": true, "steps": 47, "policy_seconds": 0.0025, "elapsed": 0.13}
          16 +{"seed": 395, "count": 3, "success": true, "steps": 135, "policy_seconds": 0.0289, "elapsed": 0.398}
          17 +{"seed": 396, "count": 3, "success": true, "steps": 61, "policy_seconds": 0.0101, "elapsed": 0.182}
          18 +{"seed": 397, "count": 3, "success": true, "steps": 54, "policy_seconds": 0.0106, "elapsed": 0.16}
          19 +{"seed": 398, "count": 3, "success": true, "steps": 64, "policy_seconds": 0.0088, "elapsed": 0.194}
          20 +{"seed": 399, "count": 3, "success": true, "steps": 97, "policy_seconds": 0.0149, "elapsed": 0.298}
diff --git a/probe_count3_edges.json b/probe_count3_edges.json
new file mode 100644
index 0000000..f886bd6
--- /dev/null
+++ b/probe_count3_edges.json
@@ -0,0 +1 @@
           1 +{"far": [], "edges": []}
diff --git a/probe_count3_edges.py b/probe_count3_edges.py
new file mode 100644
index 0000000..0ec772a
--- /dev/null
+++ b/probe_count3_edges.py
@@ -0,0 +1,12 @@
           1 +from env_client import make_env
           2 +import json
           3 +edge=[];far=[]
           4 +for seed in range(400,600):
           5 + e=make_env();s,i=e.reset(seed=seed,options={'object_count':3})
           6 + for o in s.get_objects(e.observation_space.get_type('rectangle')):
           7 +  if s.get(o,'static'):continue
           8 +  x,y,w,h=[s.get(o,f) for f in ['x','y','width','height']]
           9 +  if x>1.5398:edge.append((seed,o.name,x,y,w,h))
          10 +  if x>1.5518:far.append((seed,o.name,x,y,w,h))
          11 + e.close()
          12 +print(json.dumps({'far':far,'edges':edge}),flush=True)
diff --git a/scan_edge_cases.py b/scan_edge_cases.py
new file mode 100644
index 0000000..e542fc9
--- /dev/null
+++ b/scan_edge_cases.py
@@ -0,0 +1,8 @@
           1 +from env_client import make_env
           2 +import json
           3 +for seed in range(600,1100):
           4 + e=make_env();s,i=e.reset(seed=seed,options={'object_count':3})
           5 + edge=[(o.name,s.get(o,'x'),s.get(o,'width')) for o in s.get_objects(e.observation_space.get_type('rectangle')) if o.type.name!='target_surface' and (s.get(o,'x')>1.5518 or s.get(o,'x')+s.get(o,'width')<.0662)]
           6 + if edge:print(json.dumps({'seed':seed,'edge':edge}),flush=True)
           7 + e.close()
           8 +print('completed',flush=True)
```

</details>

<a id="C017"></a>
### C017 · Add tested tilted-gripper recovery for unreachable wall-side grasp configurations

Commit `71ac23558ec105e23f8d9346938d625af3325b3b`; parents: 29518eb3545b9c0f7b352d23c86da968224cd617. Recorded author date: 2026-09-21T17:47:46Z.

File roles (automatic): diagnostic/test, policy.

- [E0130](01_timeline.md#E0130): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_71ac235_approach.py) · [Exact all-file diff](evidence/diffs/C017_71ac235.diff)

[Previous saved controller snapshot](evidence/versions/C015_64aee98_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 26c3893..7081b4e 100644
--- a/approach.py
+++ b/approach.py
@@ -55,7 +55,34 @@ class GeneratedApproach:
   55     55          if low>high:return []
   56     56          return sorted(set([max(low,min(high,w/2))]+[float(z) for z in np.linspace(low,high,7)]),key=lambda z:abs(z-w/2))
   57     57  
          58 +    def edge_task(self,s,o):
          59 +        # A tilted gripper reaches wall-adjacent objects without rotating them.
          60 +        x,y,w,h=self.rect(s,o)
          61 +        bx,by,bw,bh=self.rect(s,self.block)
          62 +        sx,sy,sw,sh=self.rect(s,self.surface)
          63 +        direction=1 if x>0.8 else -1
          64 +        self.task_theta=-math.pi/2+direction*.22
          65 +        self.grasp_height=.210
          66 +        self.pickx=max(.1002,min(1.5178,x-.045 if direction>0 else x+w+.045))
          67 +        offset=self.pickx-x
          68 +        others=[self.rect(s,p) for p in self.obstacles(s)+[self.block] if p!=o]
          69 +        places=[]
          70 +        for px in np.linspace(.19,1.42-w,100):
          71 +            if px<sx+sw+.13 and px+w>sx-.13:continue
          72 +            if px<bx+bw+.13 and px+w>bx-.13:continue
          73 +            py=max([.105]+[qy+qh+.03 for qx,qy,qw,qh in others if px<qx+qw+.16 and px+w>qx-.16])
          74 +            places.append((py*8+abs(px-x),float(px),py))
          75 +        if not places:
          76 +            places=[(0,.3,.36)]
          77 +        _,px,py=min(places)
          78 +        self.task=o;self.dest=(px,py)
          79 +        self.offsetx=offset;self.picktop=y+h
          80 +        self.empty_cruise=.86;self.carry_cruise=.86
          81 +        self.phase='above';self.stuck=0
          82 +
   58     83      def select(self,s):
          84 +        self.task_theta=-math.pi/2
          85 +        self.grasp_height=.215
   59     86          bx,by,bw,bh=self.rect(s,self.block)
   60     87          sx,sy,sw,sh=self.rect(s,self.surface)
   61     88          obs=self.obstacles(s)
@@ -70,8 +97,8 @@ class GeneratedApproach:
   70     97                  bad=set(self.conflicts(s,self.block,gx,sy+sh+.005,offset,obs)+self.conflicts(s,self.block,bx,by,offset,obs,True))
   71     98                  plans.append(((len(bad),abs(offset-bw/2)*.2+abs(gx-bx)*.01),gx,offset,bad))
   72     99          if not plans:
   73        -            gx=(lo+hi)/2;offset=max(.1002-bx,min(1.5178-gx,bw/2))
   74        -            plans=[((len(obs),0),gx,offset,set(obs))]
         100 +            self.edge_task(s,self.block)
         101 +            return
   75    102          _,gx,offset,bad=min(plans,key=lambda p:p[0])
   76    103          self.goal=(gx,sy+sh+.005)
   77    104          keep_pick=(bx,by,bw,bh,offset)
@@ -91,6 +118,9 @@ class GeneratedApproach:
   91    118                  for off in self.offsets(x,x,w):
   92    119                      blocking=self.conflicts(s,o,x,y,off,others,True)
   93    120                      grasps.append((len(blocking),abs(off-w/2),off,blocking))
         121 +                if not grasps:
         122 +                    self.edge_task(s,o)
         123 +                    return
   94    124                  best=min(grasps,key=lambda z:z[:2])
   95    125                  if not best[0]:break
   96    126                  dependencies=set(p for grasp in grasps for p in grasp[3] if p not in visited)
@@ -129,6 +159,9 @@ class GeneratedApproach:
  129    159                      for off in self.offsets(x,px,w):
  130    160                          blockers=self.conflicts(s,o,x,y,off,others,True)+self.conflicts(s,o,px,py,off,others)
  131    161                          fallback.append((len(blockers),py*8+abs(px-x),float(px),py,off))
         162 +                if not fallback:
         163 +                    self.edge_task(s,o)
         164 +                    return
  132    165                  _,_,px,py,offset=min(fallback)
  133    166                  self.dest=(px,py)
  134    167          self.task=o
@@ -163,7 +196,7 @@ class GeneratedApproach:
  163    196                  tx=self.pickx
  164    197                  if abs(rx-tx)<.002:self.phase='down'
  165    198          if self.phase=='down':
  166        -            tx=self.pickx;ty=self.picktop+.215;vac=0.
         199 +            tx=self.pickx;ty=self.picktop+self.grasp_height;vac=0.
  167    200              if (abs(rx-tx)<.002 and abs(ry-ty)<.002) or self.stuck>=2:
  168    201                  self.phase='lift';self.before_y=y;vac=1.
  169    202                  self.offsety=ry-y;self.offsetx=rx-x
@@ -189,5 +222,5 @@ class GeneratedApproach:
  189    222          elif self.phase=='retreat':
  190    223              ty=.86
  191    224              if abs(ry-ty)<.002:self.phase='choose'
  192        -        delta=np.array([tx-rx,ty-ry,(-math.pi/2-theta+math.pi)%(2*math.pi)-math.pi,.2-arm,vac])
         225 +        delta=np.array([tx-rx,ty-ry,(self.task_theta-theta+math.pi)%(2*math.pi)-math.pi,.2-arm,vac])
  193    226          return np.clip(delta,self.action_space.low,self.action_space.high).astype(np.float32)
diff --git a/probe_angled_grasp.py b/probe_angled_grasp.py
new file mode 100644
index 0000000..22619df
--- /dev/null
+++ b/probe_angled_grasp.py
@@ -0,0 +1,20 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +import math
           4 +for sign in [1,-1]:
           5 + e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           6 + theta=-math.pi/2+sign*.22
           7 + def step(a):
           8 +  global s
           9 +  s,*_=e.step(np.array(a,dtype=np.float32))
          10 + def move(x,y,v=0):
          11 +  for _ in range(40):
          12 +   rx,ry,rt=[s.get(r,f) for f in ['x','y','theta']]
          13 +   if abs(rx-x)<1e-5 and abs(ry-y)<1e-5 and abs(rt-theta)<1e-5:break
          14 +   step([np.clip(x-rx,-.05,.05),np.clip(y-ry,-.05,.05),np.clip(theta-rt,-.196,.196),np.clip(.2-s.get(r,'arm_joint'),-.1,.1),v])
          15 + x,y,w,h=[s.get(b,f) for f in ['x','y','width','height']]
          16 + gx=x-.045 if sign==1 else x+w+.045; gy=y+h+.21857
          17 + move(gx,.8);move(gx,gy);step([0,0,0,0,1]);before=[s.get(b,f) for f in ['x','y','theta']];robotbefore=[s.get(r,f) for f in ['x','y','theta']]
          18 + step([0,.05,0,0,1]);after=[s.get(b,f) for f in ['x','y','theta']]
          19 + step([.05,0,0,0,1]);horizontal=[s.get(b,f) for f in ['x','y','theta']]
          20 + print({'sign':sign,'requested_base':[gx,gy,theta],'actual_base':robotbefore,'before':before,'lifted':after,'translated':horizontal},flush=True);e.close()
diff --git a/probe_angled_grasp_heights.py b/probe_angled_grasp_heights.py
new file mode 100644
index 0000000..9a781e6
--- /dev/null
+++ b/probe_angled_grasp_heights.py
@@ -0,0 +1,20 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +import math
           4 +for sign,heightoff in [(1,.216),(1,.213),(1,.210),(1,.207),(1,.204),(-1,.213),(-1,.207)]:
           5 + e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
           6 + theta=-math.pi/2+sign*.22
           7 + def step(a):
           8 +  global s
           9 +  s,*_=e.step(np.array(a,dtype=np.float32))
          10 + def move(x,y,v=0):
          11 +  for _ in range(40):
          12 +   rx,ry,rt=[s.get(r,f) for f in ['x','y','theta']]
          13 +   if abs(rx-x)<1e-5 and abs(ry-y)<1e-5 and abs(rt-theta)<1e-5:break
          14 +   step([np.clip(x-rx,-.05,.05),np.clip(y-ry,-.05,.05),np.clip(theta-rt,-.196,.196),np.clip(.2-s.get(r,'arm_joint'),-.1,.1),v])
          15 + x,y,w,h=[s.get(b,f) for f in ['x','y','width','height']]
          16 + gx=x-.045 if sign==1 else x+w+.045; gy=y+h+heightoff
          17 + move(gx,.8);move(gx,gy);step([0,0,0,0,1]);before=[s.get(b,f) for f in ['x','y','theta']];robotbefore=[s.get(r,f) for f in ['x','y','theta']]
          18 + step([0,.05,0,0,1]);after=[s.get(b,f) for f in ['x','y','theta']]
          19 + step([.05,0,0,0,1]);horizontal=[s.get(b,f) for f in ['x','y','theta']]
          20 + print({'sign':sign,'requested_base':[gx,gy,theta],'actual_base':robotbefore,'before':before,'lifted':after,'translated':horizontal},flush=True);e.close()
diff --git a/scan_edge_cases.jsonl b/scan_edge_cases.jsonl
new file mode 100644
index 0000000..6ab9fed
--- /dev/null
+++ b/scan_edge_cases.jsonl
@@ -0,0 +1 @@
           1 +completed
```

</details>

<a id="C018"></a>
### C018 · Add reproducible forced edge-recovery regression tests

Commit `93f861c63ca0004f84e50cf03b352c7bd077c2d1`; parents: 71ac23558ec105e23f8d9346938d625af3325b3b. Recorded author date: 2026-09-21T17:49:45Z.

File roles (automatic): diagnostic/test, setup/other.

- [E0146](01_timeline.md#E0146): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C018_93f861c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/final_smoke_count3.jsonl b/final_smoke_count3.jsonl
new file mode 100644
index 0000000..3eaf0f3
--- /dev/null
+++ b/final_smoke_count3.jsonl
@@ -0,0 +1,20 @@
           1 +{"seed": 380, "count": 3, "success": true, "steps": 88, "policy_seconds": 0.0182, "elapsed": 1.116}
           2 +{"seed": 381, "count": 3, "success": true, "steps": 100, "policy_seconds": 0.0216, "elapsed": 1.098}
           3 +{"seed": 382, "count": 3, "success": true, "steps": 71, "policy_seconds": 0.0109, "elapsed": 0.789}
           4 +{"seed": 383, "count": 3, "success": true, "steps": 59, "policy_seconds": 0.013, "elapsed": 0.719}
           5 +{"seed": 384, "count": 3, "success": true, "steps": 112, "policy_seconds": 0.0224, "elapsed": 1.474}
           6 +{"seed": 385, "count": 3, "success": true, "steps": 66, "policy_seconds": 0.0118, "elapsed": 0.722}
           7 +{"seed": 386, "count": 3, "success": true, "steps": 84, "policy_seconds": 0.014, "elapsed": 1.003}
           8 +{"seed": 387, "count": 3, "success": true, "steps": 80, "policy_seconds": 0.0251, "elapsed": 0.935}
           9 +{"seed": 388, "count": 3, "success": true, "steps": 35, "policy_seconds": 0.0025, "elapsed": 0.548}
          10 +{"seed": 389, "count": 3, "success": true, "steps": 76, "policy_seconds": 0.0126, "elapsed": 1.038}
          11 +{"seed": 390, "count": 3, "success": true, "steps": 50, "policy_seconds": 0.0133, "elapsed": 0.682}
          12 +{"seed": 391, "count": 3, "success": true, "steps": 70, "policy_seconds": 0.0296, "elapsed": 0.952}
          13 +{"seed": 392, "count": 3, "success": true, "steps": 26, "policy_seconds": 0.0023, "elapsed": 0.249}
          14 +{"seed": 393, "count": 3, "success": true, "steps": 69, "policy_seconds": 0.0126, "elapsed": 0.724}
          15 +{"seed": 394, "count": 3, "success": true, "steps": 47, "policy_seconds": 0.0027, "elapsed": 0.672}
          16 +{"seed": 395, "count": 3, "success": true, "steps": 135, "policy_seconds": 0.0348, "elapsed": 1.783}
          17 +{"seed": 396, "count": 3, "success": true, "steps": 61, "policy_seconds": 0.0123, "elapsed": 0.934}
          18 +{"seed": 397, "count": 3, "success": true, "steps": 54, "policy_seconds": 0.0156, "elapsed": 0.748}
          19 +{"seed": 398, "count": 3, "success": true, "steps": 64, "policy_seconds": 0.009, "elapsed": 0.811}
          20 +{"seed": 399, "count": 3, "success": true, "steps": 97, "policy_seconds": 0.0158, "elapsed": 1.328}
diff --git a/final_smoke_count4.jsonl b/final_smoke_count4.jsonl
new file mode 100644
index 0000000..b910adf
--- /dev/null
+++ b/final_smoke_count4.jsonl
@@ -0,0 +1,20 @@
           1 +{"seed": 80, "count": 4, "success": true, "steps": 153, "policy_seconds": 0.0475, "elapsed": 2.105}
           2 +{"seed": 81, "count": 4, "success": true, "steps": 78, "policy_seconds": 0.0142, "elapsed": 1.117}
           3 +{"seed": 82, "count": 4, "success": true, "steps": 69, "policy_seconds": 0.0117, "elapsed": 1.091}
           4 +{"seed": 83, "count": 4, "success": true, "steps": 140, "policy_seconds": 0.0212, "elapsed": 2.172}
           5 +{"seed": 84, "count": 4, "success": true, "steps": 65, "policy_seconds": 0.0157, "elapsed": 0.932}
           6 +{"seed": 85, "count": 4, "success": true, "steps": 126, "policy_seconds": 0.0249, "elapsed": 1.705}
           7 +{"seed": 86, "count": 4, "success": true, "steps": 86, "policy_seconds": 0.0243, "elapsed": 0.752}
           8 +{"seed": 87, "count": 4, "success": true, "steps": 98, "policy_seconds": 0.0228, "elapsed": 0.811}
           9 +{"seed": 88, "count": 4, "success": true, "steps": 110, "policy_seconds": 0.0227, "elapsed": 0.991}
          10 +{"seed": 89, "count": 4, "success": true, "steps": 98, "policy_seconds": 0.021, "elapsed": 0.706}
          11 +{"seed": 90, "count": 4, "success": true, "steps": 57, "policy_seconds": 0.018, "elapsed": 0.423}
          12 +{"seed": 91, "count": 4, "success": true, "steps": 102, "policy_seconds": 0.0194, "elapsed": 0.887}
          13 +{"seed": 92, "count": 4, "success": true, "steps": 82, "policy_seconds": 0.0161, "elapsed": 0.708}
          14 +{"seed": 93, "count": 4, "success": true, "steps": 100, "policy_seconds": 0.0176, "elapsed": 1.333}
          15 +{"seed": 94, "count": 4, "success": true, "steps": 68, "policy_seconds": 0.0203, "elapsed": 0.489}
          16 +{"seed": 95, "count": 4, "success": true, "steps": 87, "policy_seconds": 0.0318, "elapsed": 0.707}
          17 +{"seed": 96, "count": 4, "success": true, "steps": 59, "policy_seconds": 0.0106, "elapsed": 0.421}
          18 +{"seed": 97, "count": 4, "success": true, "steps": 147, "policy_seconds": 0.0263, "elapsed": 1.213}
          19 +{"seed": 98, "count": 4, "success": true, "steps": 105, "policy_seconds": 0.0228, "elapsed": 0.329}
          20 +{"seed": 99, "count": 4, "success": true, "steps": 100, "policy_seconds": 0.0163, "elapsed": 0.317}
diff --git a/final_smoke_defaults.jsonl b/final_smoke_defaults.jsonl
new file mode 100644
index 0000000..d3826d6
--- /dev/null
+++ b/final_smoke_defaults.jsonl
@@ -0,0 +1,100 @@
           1 +{"seed": 0, "count": null, "success": true, "steps": 92, "policy_seconds": 0.0171, "elapsed": 1.296}
           2 +{"seed": 1, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0051, "elapsed": 0.591}
           3 +{"seed": 2, "count": null, "success": true, "steps": 82, "policy_seconds": 0.0187, "elapsed": 0.741}
           4 +{"seed": 3, "count": null, "success": true, "steps": 58, "policy_seconds": 0.0078, "elapsed": 0.634}
           5 +{"seed": 4, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0027, "elapsed": 0.736}
           6 +{"seed": 5, "count": null, "success": true, "steps": 118, "policy_seconds": 0.0188, "elapsed": 1.414}
           7 +{"seed": 6, "count": null, "success": true, "steps": 55, "policy_seconds": 0.0056, "elapsed": 0.442}
           8 +{"seed": 7, "count": null, "success": true, "steps": 121, "policy_seconds": 0.0232, "elapsed": 1.406}
           9 +{"seed": 8, "count": null, "success": true, "steps": 81, "policy_seconds": 0.0155, "elapsed": 0.775}
          10 +{"seed": 9, "count": null, "success": true, "steps": 86, "policy_seconds": 0.0079, "elapsed": 0.765}
          11 +{"seed": 10, "count": null, "success": true, "steps": 38, "policy_seconds": 0.0019, "elapsed": 0.437}
          12 +{"seed": 11, "count": null, "success": true, "steps": 44, "policy_seconds": 0.0013, "elapsed": 0.326}
          13 +{"seed": 12, "count": null, "success": true, "steps": 82, "policy_seconds": 0.0073, "elapsed": 0.755}
          14 +{"seed": 13, "count": null, "success": true, "steps": 68, "policy_seconds": 0.0055, "elapsed": 0.708}
          15 +{"seed": 14, "count": null, "success": true, "steps": 26, "policy_seconds": 0.0008, "elapsed": 0.209}
          16 +{"seed": 15, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0018, "elapsed": 0.219}
          17 +{"seed": 16, "count": null, "success": true, "steps": 22, "policy_seconds": 0.001, "elapsed": 0.299}
          18 +{"seed": 17, "count": null, "success": true, "steps": 74, "policy_seconds": 0.0095, "elapsed": 0.764}
          19 +{"seed": 18, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0087, "elapsed": 0.653}
          20 +{"seed": 19, "count": null, "success": true, "steps": 53, "policy_seconds": 0.0051, "elapsed": 0.389}
          21 +{"seed": 20, "count": null, "success": true, "steps": 68, "policy_seconds": 0.0093, "elapsed": 0.63}
          22 +{"seed": 21, "count": null, "success": true, "steps": 52, "policy_seconds": 0.0014, "elapsed": 0.391}
          23 +{"seed": 22, "count": null, "success": true, "steps": 101, "policy_seconds": 0.0154, "elapsed": 1.203}
          24 +{"seed": 23, "count": null, "success": true, "steps": 42, "policy_seconds": 0.0012, "elapsed": 0.357}
          25 +{"seed": 24, "count": null, "success": true, "steps": 59, "policy_seconds": 0.005, "elapsed": 0.325}
          26 +{"seed": 25, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0055, "elapsed": 0.751}
          27 +{"seed": 26, "count": null, "success": true, "steps": 56, "policy_seconds": 0.0114, "elapsed": 0.778}
          28 +{"seed": 27, "count": null, "success": true, "steps": 20, "policy_seconds": 0.0008, "elapsed": 0.189}
          29 +{"seed": 28, "count": null, "success": true, "steps": 45, "policy_seconds": 0.0016, "elapsed": 0.329}
          30 +{"seed": 29, "count": null, "success": true, "steps": 40, "policy_seconds": 0.0104, "elapsed": 0.433}
          31 +{"seed": 30, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0009, "elapsed": 0.139}
          32 +{"seed": 31, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0069, "elapsed": 0.599}
          33 +{"seed": 32, "count": null, "success": true, "steps": 91, "policy_seconds": 0.0131, "elapsed": 1.043}
          34 +{"seed": 33, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0081, "elapsed": 0.568}
          35 +{"seed": 34, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0012, "elapsed": 0.137}
          36 +{"seed": 35, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0009, "elapsed": 0.131}
          37 +{"seed": 36, "count": null, "success": true, "steps": 43, "policy_seconds": 0.0053, "elapsed": 0.289}
          38 +{"seed": 37, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0008, "elapsed": 0.165}
          39 +{"seed": 38, "count": null, "success": true, "steps": 21, "policy_seconds": 0.0007, "elapsed": 0.107}
          40 +{"seed": 39, "count": null, "success": true, "steps": 62, "policy_seconds": 0.0065, "elapsed": 0.499}
          41 +{"seed": 40, "count": null, "success": true, "steps": 60, "policy_seconds": 0.005, "elapsed": 0.398}
          42 +{"seed": 41, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0012, "elapsed": 0.211}
          43 +{"seed": 42, "count": null, "success": true, "steps": 31, "policy_seconds": 0.0009, "elapsed": 0.211}
          44 +{"seed": 43, "count": null, "success": true, "steps": 27, "policy_seconds": 0.0012, "elapsed": 0.122}
          45 +{"seed": 44, "count": null, "success": true, "steps": 66, "policy_seconds": 0.01, "elapsed": 0.383}
          46 +{"seed": 45, "count": null, "success": true, "steps": 94, "policy_seconds": 0.013, "elapsed": 0.73}
          47 +{"seed": 46, "count": null, "success": true, "steps": 39, "policy_seconds": 0.0015, "elapsed": 0.298}
          48 +{"seed": 47, "count": null, "success": true, "steps": 38, "policy_seconds": 0.0011, "elapsed": 0.228}
          49 +{"seed": 48, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0007, "elapsed": 0.093}
          50 +{"seed": 49, "count": null, "success": true, "steps": 21, "policy_seconds": 0.0007, "elapsed": 0.083}
          51 +{"seed": 50, "count": null, "success": true, "steps": 70, "policy_seconds": 0.011, "elapsed": 0.353}
          52 +{"seed": 51, "count": null, "success": true, "steps": 37, "policy_seconds": 0.0016, "elapsed": 0.349}
          53 +{"seed": 52, "count": null, "success": true, "steps": 81, "policy_seconds": 0.015, "elapsed": 0.59}
          54 +{"seed": 53, "count": null, "success": true, "steps": 92, "policy_seconds": 0.0152, "elapsed": 0.665}
          55 +{"seed": 54, "count": null, "success": true, "steps": 30, "policy_seconds": 0.0009, "elapsed": 0.155}
          56 +{"seed": 55, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0017, "elapsed": 0.232}
          57 +{"seed": 56, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0074, "elapsed": 0.426}
          58 +{"seed": 57, "count": null, "success": true, "steps": 18, "policy_seconds": 0.0008, "elapsed": 0.111}
          59 +{"seed": 58, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0049, "elapsed": 0.343}
          60 +{"seed": 59, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0073, "elapsed": 0.456}
          61 +{"seed": 60, "count": null, "success": true, "steps": 25, "policy_seconds": 0.001, "elapsed": 0.164}
          62 +{"seed": 61, "count": null, "success": true, "steps": 68, "policy_seconds": 0.0043, "elapsed": 0.504}
          63 +{"seed": 62, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0061, "elapsed": 0.326}
          64 +{"seed": 63, "count": null, "success": true, "steps": 43, "policy_seconds": 0.0075, "elapsed": 0.209}
          65 +{"seed": 64, "count": null, "success": true, "steps": 29, "policy_seconds": 0.0013, "elapsed": 0.176}
          66 +{"seed": 65, "count": null, "success": true, "steps": 19, "policy_seconds": 0.0008, "elapsed": 0.096}
          67 +{"seed": 66, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0076, "elapsed": 0.531}
          68 +{"seed": 67, "count": null, "success": true, "steps": 51, "policy_seconds": 0.0093, "elapsed": 0.437}
          69 +{"seed": 68, "count": null, "success": true, "steps": 47, "policy_seconds": 0.0057, "elapsed": 0.234}
          70 +{"seed": 69, "count": null, "success": true, "steps": 36, "policy_seconds": 0.0011, "elapsed": 0.173}
          71 +{"seed": 70, "count": null, "success": true, "steps": 49, "policy_seconds": 0.012, "elapsed": 0.521}
          72 +{"seed": 71, "count": null, "success": true, "steps": 42, "policy_seconds": 0.0096, "elapsed": 0.391}
          73 +{"seed": 72, "count": null, "success": true, "steps": 97, "policy_seconds": 0.0093, "elapsed": 1.109}
          74 +{"seed": 73, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0067, "elapsed": 0.579}
          75 +{"seed": 74, "count": null, "success": true, "steps": 24, "policy_seconds": 0.0008, "elapsed": 0.214}
          76 +{"seed": 75, "count": null, "success": true, "steps": 73, "policy_seconds": 0.0082, "elapsed": 0.57}
          77 +{"seed": 76, "count": null, "success": true, "steps": 30, "policy_seconds": 0.0012, "elapsed": 0.193}
          78 +{"seed": 77, "count": null, "success": true, "steps": 22, "policy_seconds": 0.0009, "elapsed": 0.231}
          79 +{"seed": 78, "count": null, "success": true, "steps": 99, "policy_seconds": 0.0222, "elapsed": 0.82}
          80 +{"seed": 79, "count": null, "success": true, "steps": 34, "policy_seconds": 0.001, "elapsed": 0.19}
          81 +{"seed": 80, "count": null, "success": true, "steps": 68, "policy_seconds": 0.0063, "elapsed": 0.578}
          82 +{"seed": 81, "count": null, "success": true, "steps": 25, "policy_seconds": 0.0007, "elapsed": 0.123}
          83 +{"seed": 82, "count": null, "success": true, "steps": 37, "policy_seconds": 0.002, "elapsed": 0.249}
          84 +{"seed": 83, "count": null, "success": true, "steps": 111, "policy_seconds": 0.0178, "elapsed": 0.814}
          85 +{"seed": 84, "count": null, "success": true, "steps": 64, "policy_seconds": 0.0058, "elapsed": 0.375}
          86 +{"seed": 85, "count": null, "success": true, "steps": 59, "policy_seconds": 0.0088, "elapsed": 0.357}
          87 +{"seed": 86, "count": null, "success": true, "steps": 45, "policy_seconds": 0.0094, "elapsed": 0.359}
          88 +{"seed": 87, "count": null, "success": true, "steps": 53, "policy_seconds": 0.0062, "elapsed": 0.381}
          89 +{"seed": 88, "count": null, "success": true, "steps": 63, "policy_seconds": 0.0054, "elapsed": 0.319}
          90 +{"seed": 89, "count": null, "success": true, "steps": 61, "policy_seconds": 0.0077, "elapsed": 0.499}
          91 +{"seed": 90, "count": null, "success": true, "steps": 77, "policy_seconds": 0.0056, "elapsed": 0.421}
          92 +{"seed": 91, "count": null, "success": true, "steps": 43, "policy_seconds": 0.0089, "elapsed": 0.366}
          93 +{"seed": 92, "count": null, "success": true, "steps": 54, "policy_seconds": 0.0056, "elapsed": 0.315}
          94 +{"seed": 93, "count": null, "success": true, "steps": 76, "policy_seconds": 0.0106, "elapsed": 0.44}
          95 +{"seed": 94, "count": null, "success": true, "steps": 23, "policy_seconds": 0.0008, "elapsed": 0.116}
          96 +{"seed": 95, "count": null, "success": true, "steps": 60, "policy_seconds": 0.0062, "elapsed": 0.275}
          97 +{"seed": 96, "count": null, "success": true, "steps": 32, "policy_seconds": 0.0016, "elapsed": 0.264}
          98 +{"seed": 97, "count": null, "success": true, "steps": 36, "policy_seconds": 0.001, "elapsed": 0.229}
          99 +{"seed": 98, "count": null, "success": true, "steps": 57, "policy_seconds": 0.0058, "elapsed": 0.381}
         100 +{"seed": 99, "count": null, "success": true, "steps": 46, "policy_seconds": 0.0023, "elapsed": 0.461}
diff --git a/test_edge_recovery.py b/test_edge_recovery.py
new file mode 100644
index 0000000..419d0fa
--- /dev/null
+++ b/test_edge_recovery.py
@@ -0,0 +1,22 @@
           1 +"""Exercise the tilted-gripper recovery even on ordinary reachable blocks."""
           2 +import json
           3 +import math
           4 +from env_client import make_env
           5 +from approach import GeneratedApproach
           6 +
           7 +for seed, offset in [(0,None),(1,None),(2,None),(7,None),(0,-.05),(0,-.055),(0,-.06)]:
           8 +    env=make_env()
           9 +    state,info=env.reset(seed=seed)
          10 +    policy=GeneratedApproach(env.action_space,env.observation_space,{})
          11 +    policy.reset(state,info)
          12 +    policy.edge_task(state,policy.block)
          13 +    if offset is not None:
          14 +        policy.pickx=state.get(policy.block,'x')+offset
          15 +        policy.task_theta=-math.pi/2+.22
          16 +    for step in range(env.max_steps):
          17 +        state,reward,terminated,truncated,info=env.step(policy.get_action(state))
          18 +        if terminated or truncated:
          19 +            break
          20 +    print(json.dumps({'seed':seed,'offset':offset,'success':terminated,'steps':step+1}),flush=True)
          21 +    env.close()
          22 +    assert terminated
```

</details>

<a id="C019"></a>
### C019 · Document validation evidence and preserve the final tested policy

Commit `3b0289191de493678a1a4daa43dfa65bc0784e45`; parents: 93f861c63ca0004f84e50cf03b352c7bd077c2d1. Recorded author date: 2026-09-21T17:50:20Z.

File roles (automatic): setup/other.

- [E0148](01_timeline.md#E0148): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C019_3b02891.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/VALIDATION.md b/VALIDATION.md
new file mode 100644
index 0000000..ed93b9e
--- /dev/null
+++ b/VALIDATION.md
@@ -0,0 +1,10 @@
           1 +The policy enumerates typed objects, chooses a collision-free target placement and grasp offset, clears obstructing grasp dependencies, and transports blocks above the observed obstacles. Parking preserves the target pickup column. A tilted-gripper recovery handles objects at the workspace edges.
           2 +
           3 +Validation results:
           4 +
           5 +- Core policy: 500/500 default seeds and 100/100 four-obstruction scenes.
           6 +- Three-obstruction sweep: one wall-edge failure among 100 scenes; fixed and checked with 20/20 passing regressions.
           7 +- Final implementation: 140/140 regression episodes and 7/7 forced tilted-gripper recovery episodes.
           8 +- Maximum measured final policy computation: 0.0475 seconds per episode.
           9 +
          10 +Run `/opt/robocode-strict/bin/python validate.py --count 4 --start 0 --stop 100 --out validation.jsonl` or `/opt/robocode-strict/bin/python test_edge_recovery.py` to reproduce tests. See `validation_summary.json` and the referenced JSONL files for detailed results.
diff --git a/final_forced_edges.jsonl b/final_forced_edges.jsonl
new file mode 100644
index 0000000..34bb98d
--- /dev/null
+++ b/final_forced_edges.jsonl
@@ -0,0 +1,7 @@
           1 +{"seed": 0, "offset": null, "success": true, "steps": 127}
           2 +{"seed": 1, "offset": null, "success": true, "steps": 116}
           3 +{"seed": 2, "offset": null, "success": true, "steps": 113}
           4 +{"seed": 7, "offset": null, "success": true, "steps": 174}
           5 +{"seed": 0, "offset": -0.05, "success": true, "steps": 127}
           6 +{"seed": 0, "offset": -0.055, "success": true, "steps": 127}
           7 +{"seed": 0, "offset": -0.06, "success": true, "steps": 127}
diff --git a/validation_summary.json b/validation_summary.json
new file mode 100644
index 0000000..e73f8ef
--- /dev/null
+++ b/validation_summary.json
@@ -0,0 +1,50 @@
           1 +{
           2 +  "approach_sha256": "c7c9db30a99eb3764bb063ed6b03030573cfa8e0d5623c189cac5c65e31afb38",
           3 +  "suites": {
           4 +    "final_defaults.jsonl": {
           5 +      "episodes": 500,
           6 +      "passed": 500,
           7 +      "max_policy_seconds": 0.026
           8 +    },
           9 +    "final_count4.jsonl": {
          10 +      "episodes": 100,
          11 +      "passed": 100,
          12 +      "max_policy_seconds": 0.0456
          13 +    },
          14 +    "final_count3.jsonl": {
          15 +      "episodes": 100,
          16 +      "passed": 99,
          17 +      "max_policy_seconds": 0.0309
          18 +    },
          19 +    "final_edge_regression.jsonl": {
          20 +      "episodes": 20,
          21 +      "passed": 20,
          22 +      "max_policy_seconds": 0.0289
          23 +    },
          24 +    "final_smoke_defaults.jsonl": {
          25 +      "episodes": 100,
          26 +      "passed": 100,
          27 +      "max_policy_seconds": 0.0232
          28 +    },
          29 +    "final_smoke_count3.jsonl": {
          30 +      "episodes": 20,
          31 +      "passed": 20,
          32 +      "max_policy_seconds": 0.0348
          33 +    },
          34 +    "final_smoke_count4.jsonl": {
          35 +      "episodes": 20,
          36 +      "passed": 20,
          37 +      "max_policy_seconds": 0.0475
          38 +    },
          39 +    "final_forced_edges.jsonl": {
          40 +      "episodes": 7,
          41 +      "passed": 7,
          42 +      "max_policy_seconds": 0
          43 +    }
          44 +  },
          45 +  "notes": [
          46 +    "The broad default and count4 sweeps tested ffca88e before the isolated edge-recovery extension.",
          47 +    "The original count3 sweep failed seed386; expanded wall-edge grasp bounds fixed it, and all20 edge regression cases passed.",
          48 +    "The final implementation passed100 default,20 count3,20 count4 and7 forced tilted-gripper regressions."
          49 +  ]
          50 +}
```

</details>

