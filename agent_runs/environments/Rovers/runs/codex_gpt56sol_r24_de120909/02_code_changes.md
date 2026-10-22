# Rovers · gpt-5.6-sol · replicate 24: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `79958ef` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `9388a13` | add geometry-aware dual rover planning baseline | approach.py, inspect_env.py, probe_layouts.out, probe_layouts.py, probe_ops.py, probe_summary.py | [E0012](01_timeline.md#E0012) |
| [C003](#C003) · `68b0db9` | drop transmitted samples and add rollout test harness | approach.py, probe_summary.py, test_approach.py | [E0020](01_timeline.md#E0020) |
| [C004](#C004) · `faa36e0` | fix waypoint delta coordinate calculation | approach.py | [E0027](01_timeline.md#E0027) |
| [C005](#C005) · `a633607` | add compact rollout diagnostics | debug_rollout.py | [E0033](01_timeline.md#E0033) |
| [C006](#C006) · `bd89862` | model hidden central wall and stop after required sample type | approach.py | [E0043](01_timeline.md#E0043) |
| [C007](#C007) · `2646aca` | correct wall geometry and allocate work by reachable side | approach.py, probe_ops.py, probe_side_stats.py | [E0050](01_timeline.md#E0050) |
| [C008](#C008) · `d7128c0` | use validated radio poses and relax lattice goal tolerance | approach.py | [E0058](01_timeline.md#E0058) |
| [C009](#C009) · `1ab6891` | show per-rover image flags in rollout diagnostics | debug_rollout.py | [E0062](01_timeline.md#E0062) |
| [C010](#C010) · `10f9a6c` | advance after sent images and navigate samples to true pickup radius | approach.py | [E0066](01_timeline.md#E0066) |
| [C011](#C011) · `1fafd85` | parameterize rollout debugger by seed | debug_rollout.py | [E0070](01_timeline.md#E0070) |
| [C012](#C012) · `5ceb580` | adapt radio poses around random occluding pillars | approach.py | [E0075](01_timeline.md#E0075) |
| [C013](#C013) · `b38c5e0` | densify collision-free fallback radio viewpoints | approach.py | [E0081](01_timeline.md#E0081) |
| [C014](#C014) · `7d3acca` | match measured rover clearance and compact lander footprint | approach.py | [E0089](01_timeline.md#E0089) |
| [C015](#C015) · `b756d22` | add targeted lander-corner accessibility probe | probe_corner.py | [E0097](01_timeline.md#E0097) |
| [C016](#C016) · `62a9024` | avoid trapped lander-corner samples and enforce side-local pickups | approach.py | [E0101](01_timeline.md#E0101) |
| [C017](#C017) · `c936cf5` | honor selected sample and approach objectives with robust margin | approach.py | [E0109](01_timeline.md#E0109) |
| [C018](#C018) · `84d91db` | learn rejected collision segments and target pickup disks | approach.py | [E0118](01_timeline.md#E0118) |
| [C019](#C019) · `846bb14` | avoid edge samples and distinguish tiny successful moves from collisions | approach.py | [E0125](01_timeline.md#E0125) |
| [C020](#C020) · `50ee284` | keep image viewpoints inside conservative visibility radius | approach.py | [E0129](01_timeline.md#E0129) |
| [C021](#C021) · `cacac5e` | nudge and sample at tight divider-side pickup poses | approach.py | [E0135](01_timeline.md#E0135) |
| [C022](#C022) · `b3062a5` | sample from safely inside acquisition cutoff | approach.py | [E0143](01_timeline.md#E0143) |
| [C023](#C023) · `6285fa6` | prefer unpinched samples and bound learned collision map | approach.py | [E0149](01_timeline.md#E0149) |
| [C024](#C024) · `dd4d929` | keep learned collision cells local enough to route around | approach.py | [E0155](01_timeline.md#E0155) |
| [C025](#C025) · `b648b65` | sidestep after rejected navigation motion | approach.py | [E0159](01_timeline.md#E0159) |
| [C026](#C026) · `27f3d97` | increase early rollout diagnostic resolution | debug_rollout.py | [E0165](01_timeline.md#E0165) |
| [C027](#C027) · `2d32ae7` | preserve stall signal through replanning for escape move | approach.py | [E0169](01_timeline.md#E0169) |
| [C028](#C028) · `fa6490b` | make collision escape continue around obstacle flank | approach.py | [E0175](01_timeline.md#E0175) |
| [C029](#C029) · `6af5f87` | use camera-ray clearance around pillar silhouettes | approach.py | [E0183](01_timeline.md#E0183) |
| [C030](#C030) · `d3aad59` | detect pinched samples from typed pillar dimensions | approach.py | [E0191](01_timeline.md#E0191) |
| [C031](#C031) · `b6baaea` | rank lander-trapped samples below merely edge-adjacent ones | approach.py | [E0200](01_timeline.md#E0200) |
| [C032](#C032) · `70cf2a1` | escape north around lander east-side collision boundary | approach.py | [E0208](01_timeline.md#E0208) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `79958ef92f9217e28907411987d00e67fe9cb759`; parents: none (initial snapshot). Recorded author date: 2026-09-11T11:32:33+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_79958ef.diff)

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
index 0000000..6923c9f
--- /dev/null
+++ b/env_client.py
@@ -0,0 +1,735 @@
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
          86 +        return f"Type({self.name})"
          87 +
          88 +
          89 +class _Object:
          90 +    """A local mirror of relational_structs.Object (name + type)."""
          91 +
          92 +    def __init__(self, name: str, typ: _Type) -> None:
          93 +        self.name = name
          94 +        self.type = typ
          95 +
          96 +    def is_instance(self, typ: _Type) -> bool:
          97 +        """True if this object's type is *typ* or a descendant of it."""
          98 +        return typ in self.type.get_ancestors()
          99 +
         100 +    def __eq__(self, other: Any) -> bool:
         101 +        return isinstance(other, _Object) and other.name == self.name
         102 +
         103 +    def __hash__(self) -> int:
         104 +        return hash(self.name)
         105 +
         106 +    def __repr__(self) -> str:
         107 +        return f"{self.name}:{self.type.name}"
         108 +
         109 +
         110 +class _ObjectCentricState:
         111 +    """A local mirror of relational_structs.ObjectCentricState.
         112 +
         113 +    Holds ``{Object: feature ndarray}`` as ``data`` plus ``{Type: [feature names]}`` as
         114 +    ``type_features`` (both public, matching the real state) and exposes the read/write
         115 +    API a program uses. Iteration yields the objects, sorted by name for determinism.
         116 +    """
         117 +
         118 +    def __init__(
         119 +        self,
         120 +        data: dict[_Object, np.ndarray],
         121 +        type_features: dict[_Type, list[str]],
         122 +    ) -> None:
         123 +        self.data = data
         124 +        self.type_features = type_features
         125 +
         126 +    def __iter__(self) -> Any:
         127 +        return iter(sorted(self.data, key=lambda o: o.name))
         128 +
         129 +    def get_object_names(self) -> set[str]:
         130 +        """The set of object names in this state."""
         131 +        return {o.name for o in self.data}
         132 +
         133 +    def get_object_from_name(self, name: str) -> _Object:
         134 +        """The object with the given name."""
         135 +        for obj in self.data:
         136 +            if obj.name == name:
         137 +                return obj
         138 +        raise ValueError(f"No object named {name!r}")
         139 +
         140 +    def get_objects(self, typ: _Type) -> list[_Object]:
         141 +        """Objects that are instances of *typ* (its subtypes included), by name."""
         142 +        return sorted(
         143 +            (o for o in self.data if o.is_instance(typ)), key=lambda o: o.name
         144 +        )
         145 +
         146 +    def _feature_index(self, obj: _Object, feature: str) -> int:
         147 +        return self.type_features[obj.type].index(feature)
         148 +
         149 +    def get(self, obj: _Object, feature: str) -> float:
         150 +        """Read a named feature of an object."""
         151 +        return float(self.data[obj][self._feature_index(obj, feature)])
         152 +
         153 +    def set(self, obj: _Object, feature: str, value: float) -> None:
         154 +        """Write a named feature of an object in place."""
         155 +        self.data[obj][self._feature_index(obj, feature)] = value
         156 +
         157 +    def vec(self, objects: Any) -> np.ndarray:
         158 +        """Concatenate the feature vectors of the given objects."""
         159 +        return (
         160 +            np.concatenate([self.data[o] for o in objects]) if objects else np.array([])
         161 +        )
         162 +
         163 +    def copy(self) -> "_ObjectCentricState":
         164 +        """A deep copy of this state."""
         165 +        return _ObjectCentricState(
         166 +            {o: arr.copy() for o, arr in self.data.items()},
         167 +            {t: list(f) for t, f in self.type_features.items()},
         168 +        )
         169 +
         170 +    def allclose(self, other: "_ObjectCentricState") -> bool:
         171 +        """True if *other* has the same objects with numerically-close features."""
         172 +        if self.get_object_names() != other.get_object_names():
         173 +            return False
         174 +        return all(
         175 +            np.allclose(self.data[o], other.data[other.get_object_from_name(o.name)])
         176 +            for o in self.data
         177 +        )
         178 +
         179 +
         180 +def _build_local_types(
         181 +    types_payload: list[dict[str, Any]],
         182 +) -> tuple[dict[str, _Type], dict[_Type, list[str]]]:
         183 +    """Rebuild local {name: _Type} and {_Type: [features]} (parents-first payload)."""
         184 +    type_by_name: dict[str, _Type] = {}
         185 +    type_features: dict[_Type, list[str]] = {}
         186 +    for entry in types_payload:
         187 +        parent = type_by_name[entry["parent"]] if entry["parent"] is not None else None
         188 +        typ = _Type(entry["name"], parent)
         189 +        type_by_name[entry["name"]] = typ
         190 +        type_features[typ] = list(entry["features"])
         191 +    return type_by_name, type_features
         192 +
         193 +
         194 +def _ocs_from_payload(payload: dict[str, Any]) -> _ObjectCentricState:
         195 +    """Reconstruct a local ObjectCentricState from a self-contained codec payload."""
         196 +    type_by_name, type_features = _build_local_types(payload["types"])
         197 +    data: dict[_Object, np.ndarray] = {}
         198 +    for entry in payload["objects"]:
         199 +        obj = _Object(entry["name"], type_by_name[entry["type"]])
         200 +        data[obj] = np.array(entry["features"], dtype=np.float32)
         201 +    return _ObjectCentricState(data, type_features)
         202 +
         203 +
         204 +def _ocs_to_payload(state: _ObjectCentricState) -> dict[str, Any]:
         205 +    """Encode a local ObjectCentricState back to the self-contained codec payload."""
         206 +
         207 +    def depth(t: _Type) -> int:
         208 +        n, p = 0, t.parent
         209 +        while p is not None:
         210 +            n, p = n + 1, p.parent
         211 +        return n
         212 +
         213 +    types = sorted(state.type_features, key=lambda t: (depth(t), t.name))
         214 +    return {
         215 +        "types": [
         216 +            {
         217 +                "name": t.name,
         218 +                "parent": t.parent.name if t.parent is not None else None,
         219 +                "features": list(state.type_features[t]),
         220 +            }
         221 +            for t in types
         222 +        ],
         223 +        "objects": [
         224 +            {
         225 +                "name": o.name,
         226 +                "type": o.type.name,
         227 +                "features": [float(v) for v in state.data[o]],
         228 +            }
         229 +            for o in sorted(state.data, key=lambda o: o.name)
         230 +        ],
         231 +    }
         232 +
         233 +
         234 +def _encode(obj: Any) -> Any:
         235 +    """Encode values as tagged JSON (mirrors robocode.utils.env_server)."""
         236 +    if isinstance(obj, _ObjectCentricState):
         237 +        return {_OCS_TAG: _ocs_to_payload(obj)}
         238 +    if isinstance(obj, np.generic):
         239 +        return obj.item()
         240 +    if isinstance(obj, np.ndarray):
         241 +        return {_NDARRAY_TAG: obj.tolist(), "dtype": str(obj.dtype)}
         242 +    if isinstance(obj, dict):
         243 +        return {key: _encode(value) for key, value in obj.items()}
         244 +    if isinstance(obj, (list, tuple)):
         245 +        return [_encode(value) for value in obj]
         246 +    return obj
         247 +
         248 +
         249 +def _decode(obj: Any) -> Any:
         250 +    """Decode tagged JSON (mirrors robocode.utils.env_server)."""
         251 +    if isinstance(obj, dict):
         252 +        if _OCS_TAG in obj:
         253 +            return _ocs_from_payload(obj[_OCS_TAG])
         254 +        if _NDARRAY_TAG in obj:
         255 +            return np.array(obj[_NDARRAY_TAG], dtype=np.dtype(obj["dtype"]))
         256 +        return {key: _decode(value) for key, value in obj.items()}
         257 +    if isinstance(obj, list):
         258 +        return [_decode(value) for value in obj]
         259 +    return obj
         260 +
         261 +
         262 +def _encode_ref(obj: Any) -> Any:
         263 +    """Encode args/targets for the remote-object proxy commands.
         264 +
         265 +    Same as ``_encode`` but ``_RemoteHandle`` objects serialize to their
         266 +    ``{"__handle__": id}`` token so the host resolves them from its registry.
         267 +    Used only by devectorize/vectorize/getattr/call requests.
         268 +    """
         269 +    if isinstance(obj, _RemoteHandle):
         270 +        return {_HANDLE_TAG: obj._handle_id}  # pylint: disable=protected-access
         271 +    if isinstance(obj, _ObjectCentricState):
         272 +        return {_OCS_TAG: _ocs_to_payload(obj)}
         273 +    if isinstance(obj, np.generic):
         274 +        return obj.item()
         275 +    if isinstance(obj, np.ndarray):
         276 +        return {_NDARRAY_TAG: obj.tolist(), "dtype": str(obj.dtype)}
         277 +    if isinstance(obj, dict):
         278 +        return {key: _encode_ref(value) for key, value in obj.items()}
         279 +    if isinstance(obj, (list, tuple)):
         280 +        return [_encode_ref(value) for value in obj]
         281 +    if isinstance(obj, (set, frozenset)):
         282 +        return {_SET_TAG: [_encode_ref(value) for value in obj]}
         283 +    return obj
         284 +
         285 +
         286 +class SpaceInfo:
         287 +    """Metadata for a Box space: shape, low, high, dtype, and sample()."""
         288 +
         289 +    def __init__(self, spec: dict[str, Any]) -> None:
         290 +        if spec["type"] != "Box":
         291 +            raise TypeError(
         292 +                f"Unsupported space type {spec['type']!r}; extend SpaceInfo "
         293 +                "alongside the server's serialize_space"
         294 +            )
         295 +        self.shape: tuple[int, ...] = tuple(spec["shape"])
         296 +        self.dtype: np.dtype[Any] = np.dtype(spec["dtype"])
         297 +        self.low: np.ndarray = np.array(spec["low"], dtype=self.dtype)
         298 +        self.high: np.ndarray = np.array(spec["high"], dtype=self.dtype)
         299 +
         300 +    def sample(self, rng: np.random.Generator | None = None) -> np.ndarray:
         301 +        """Sample uniformly between low and high."""
         302 +        if rng is None:
         303 +            rng = np.random.default_rng()
         304 +        return rng.uniform(self.low, self.high).astype(self.dtype)
         305 +
         306 +
         307 +class _RemoteHandle:
         308 +    """A reference to a host-side object, used over the env server.
         309 +
         310 +    Attribute access and calls are proxied to the host: ``handle.method(...)``
         311 +    issues a ``getattr`` (returning another handle for the bound method) then a
         312 +    ``call``. Returned values are decoded the same way as any response, so a
         313 +    scalar/ndarray comes back inline and another object comes back as a nested
         314 +    ``_RemoteHandle``. Private/dunder attributes are refused client-side, both
         315 +    to avoid surprise round-trips and to mirror the host security guard.
         316 +    """
         317 +
         318 +    def __init__(self, client: "BlackboxEnv", handle_id: str) -> None:
         319 +        # Use object.__setattr__-free plain assignment; __getattr__ only fires
         320 +        # for names not found normally, and these two are set here.
         321 +        self._client = client
         322 +        self._handle_id = handle_id
         323 +
         324 +    def __getattr__(self, name: str) -> Any:
         325 +        if name.startswith("_"):
         326 +            raise AttributeError(
         327 +                f"refusing private/dunder attribute access on remote handle: "
         328 +                f"{name!r}"
         329 +            )
         330 +        response = self._client._request(  # pylint: disable=protected-access
         331 +            {
         332 +                "cmd": "getattr",
         333 +                "target": {_HANDLE_TAG: self._handle_id},
         334 +                "name": name,
         335 +            }
         336 +        )
         337 +        return self._client._decode_ref(  # pylint: disable=protected-access
         338 +            response["result"]
         339 +        )
         340 +
         341 +    def __call__(self, *args: Any, **kwargs: Any) -> Any:
         342 +        response = self._client._request(  # pylint: disable=protected-access
         343 +            {
         344 +                "cmd": "call",
         345 +                "target": {_HANDLE_TAG: self._handle_id},
         346 +                "args": _encode_ref(list(args)),
         347 +                "kwargs": _encode_ref(kwargs),
         348 +            }
         349 +        )
         350 +        return self._client._decode_ref(  # pylint: disable=protected-access
         351 +            response["result"]
         352 +        )
         353 +
         354 +
         355 +class _RemoteModule:
         356 +    """A reference to a whitelisted host module (e.g. crv_motion_planning).
         357 +
         358 +    Attribute access proxies a ``getattr`` against the ``{"__module__": name}``
         359 +    target, so ``module.plan_crv_actions`` returns a callable handle the agent
         360 +    can invoke. Mirrors how a remote-module primitive is used at eval time,
         361 +    where ``primitives['crv_motion_planning']`` is the real module.
         362 +    """
         363 +
         364 +    def __init__(self, client: "BlackboxEnv", short_name: str) -> None:
         365 +        self._client = client
         366 +        self._short_name = short_name
         367 +
         368 +    def __getattr__(self, name: str) -> Any:
         369 +        if name.startswith("_"):
         370 +            raise AttributeError(
         371 +                f"refusing private/dunder attribute access on remote module: "
         372 +                f"{name!r}"
         373 +            )
         374 +        response = self._client._request(  # pylint: disable=protected-access
         375 +            {
         376 +                "cmd": "getattr",
         377 +                "target": {_MODULE_TAG: self._short_name},
         378 +                "name": name,
         379 +            }
         380 +        )
         381 +        return self._client._decode_ref(  # pylint: disable=protected-access
         382 +            response["result"]
         383 +        )
         384 +
         385 +
         386 +class _BlackboxObservationSpace(SpaceInfo):
         387 +    """Box-space metadata plus client-backed devectorize/vectorize.
         388 +
         389 +    Stands in for the eval-time ``ObjectCentricBoxSpace``: it keeps the
         390 +    shape/low/high/dtype/sample() of a plain ``SpaceInfo`` and adds
         391 +    ``devectorize(obs)`` / ``vectorize(ocs)`` that proxy to the host. The agent
         392 +    writes ``observation_space.devectorize(obs)`` exactly as it would at eval.
         393 +    """
         394 +
         395 +    def __init__(self, spec: dict[str, Any], client: "BlackboxEnv") -> None:
         396 +        super().__init__(spec)
         397 +        self._client = client
         398 +
         399 +    def devectorize(self, obs: Any) -> Any:
         400 +        """Return an object-centric view of *obs* as a remote handle."""
         401 +        return self._client.devectorize(obs)
         402 +
         403 +    def vectorize(self, state: Any) -> np.ndarray:
         404 +        """Return the flat observation vector for an object-centric state."""
         405 +        return self._client.vectorize(state)
         406 +
         407 +
         408 +class _ObjectCentricObservationSpace:
         409 +    """Client-side view of a variable-count env's ObjectCentricStateSpace.
         410 +
         411 +    The observation is already an object-centric state (reconstructed locally from the
         412 +    wire), so this space has no fixed shape/vector: it exposes the domain ``types`` and
         413 +    ``type_features`` the program needs to enumerate objects, matching the eval-time
         414 +    ``observation_space.types``. There is no ``devectorize`` -- the state is not a
         415 +    vector.
         416 +    """
         417 +
         418 +    def __init__(self, spec: dict[str, Any]) -> None:
         419 +        self._type_by_name, self._type_features = _build_local_types(spec["types"])
         420 +
         421 +    @property
         422 +    def types(self) -> set[_Type]:
         423 +        """The domain object types (matches the eval-time observation_space.types)."""
         424 +        return set(self._type_features)
         425 +
         426 +    @property
         427 +    def type_features(self) -> dict[_Type, list[str]]:
         428 +        """Feature names for each type."""
         429 +        return {t: list(f) for t, f in self._type_features.items()}
         430 +
         431 +    def get_type(self, name: str) -> _Type:
         432 +        """The domain type with the given name (e.g. ``"rectangle"``)."""
         433 +        return self._type_by_name[name]
         434 +
         435 +
         436 +class BlackboxEnv:
         437 +    """A live environment instance, accessed over the wire."""
         438 +
         439 +    def __init__(self, meta: dict[str, Any], sandbox_root: Any = None) -> None:
         440 +        obs_spec = meta["observation_space"]
         441 +        self._strict = bool(meta.get("strict", False))
         442 +        # A variable-count env sends object-centric states, reconstructed locally; a
         443 +        # fixed-count env sends Box vectors as before.
         444 +        self._object_centric = obs_spec.get("type") == "ObjectCentric"
         445 +        if self._object_centric:
         446 +            self.observation_space: Any = _ObjectCentricObservationSpace(obs_spec)
         447 +        elif self._strict:
         448 +            # Strict blackbox exposes only generic array metadata. In particular,
         449 +            # do not attach the host-backed devectorize/vectorize helpers that make
         450 +            # the legacy blackbox convenient but confound the isolation ablation.
         451 +            self.observation_space = SpaceInfo(obs_spec)
         452 +        else:
         453 +            self.observation_space = _BlackboxObservationSpace(obs_spec, self)
         454 +        self.action_space = SpaceInfo(meta["action_space"])
         455 +        self.max_steps: int | None = meta["max_steps"]
         456 +        # How make_primitives rebuilds the eval-time primitives dict (see
         457 +        # robocode.primitives.blackbox_primitive_manifest). Empty when the
         458 +        # run configures no primitives.
         459 +        self._primitive_manifest: list[dict[str, Any]] = meta.get("primitives", [])
         460 +        # Where render_policy looks for approach.py and make_primitives imports
         461 +        # generic primitive sources; the sandbox dir in real runs (set by
         462 +        # make_env), the current dir for ad-hoc construction.
         463 +        self._sandbox_root = (
         464 +            Path(sandbox_root) if sandbox_root is not None else Path.cwd()
         465 +        )
         466 +        self._token: str = meta["token"]
         467 +        self._sock = socket.create_connection((meta["host"], meta["port"]))
         468 +        self._file = self._sock.makefile("rwb")
         469 +
         470 +    def _request(self, payload: dict[str, Any]) -> dict[str, Any]:
         471 +        payload["token"] = self._token
         472 +        self._file.write(json.dumps(payload).encode("utf-8") + b"\n")
         473 +        self._file.flush()
         474 +        line = self._file.readline()
         475 +        if not line:
         476 +            raise RuntimeError("Connection to the environment server was closed")
         477 +        response = json.loads(line)
         478 +        if "error" in response:
         479 +            raise RuntimeError(f"Environment server error: {response['error']}")
         480 +        return _decode(response)
         481 +
         482 +    def _decode_ref(self, obj: Any) -> Any:
         483 +        """Decode a remote-command result, mapping handles to _RemoteHandle.
         484 +
         485 +        ``_request`` already ran ``_decode`` over the response (so ndarrays are
         486 +        arrays), but it leaves ``{"__handle__": id}`` dicts intact since it does
         487 +        not know the handle tag. Here we turn those into ``_RemoteHandle``
         488 +        objects and recurse through the remaining containers.
         489 +        """
         490 +        if isinstance(obj, dict):
         491 +            if _HANDLE_TAG in obj:
         492 +                return _RemoteHandle(self, obj[_HANDLE_TAG])
         493 +            if _SET_TAG in obj:
         494 +                return {self._decode_ref(value) for value in obj[_SET_TAG]}
         495 +            return {key: self._decode_ref(value) for key, value in obj.items()}
         496 +        if isinstance(obj, list):
         497 +            return [self._decode_ref(value) for value in obj]
         498 +        return obj
         499 +
         500 +    def devectorize(self, obs: Any) -> _RemoteHandle:
         501 +        """Return an object-centric view of *obs* (a remote ObjectCentricState).
         502 +
         503 +        Proxies ``observation_space.devectorize`` to the host. The returned
         504 +        handle exposes the public ObjectCentricState API (``get_object_names``,
         505 +        ``get_object_from_name``, ``get_objects``, ``get``, ``set``, ``copy``,
         506 +        ...) over the wire. Pass it straight to the CRV planners from
         507 +        ``make_primitives``.
         508 +        """
         509 +        response = self._request(
         510 +            {"cmd": "devectorize", "obs": _encode(np.asarray(obs))}
         511 +        )
         512 +        return self._decode_ref(response["result"])
         513 +
         514 +    def vectorize(self, state: Any) -> np.ndarray:
         515 +        """Return the flat observation vector for an object-centric state handle."""
         516 +        response = self._request({"cmd": "vectorize", "state": _encode_ref(state)})
         517 +        return self._decode_ref(response["result"])
         518 +
         519 +    def reset(
         520 +        self, seed: int | None = None, options: dict[str, Any] | None = None
         521 +    ) -> tuple[np.ndarray, dict[str, Any]]:
         522 +        """Reset the environment; returns (obs, info)."""
         523 +        response = self._request({"cmd": "reset", "seed": seed, "options": options})
         524 +        return response["obs"], response["info"]
         525 +
         526 +    def step(self, action: Any) -> tuple[np.ndarray, float, bool, bool, dict[str, Any]]:
         527 +        """Step the environment; returns (obs, reward, terminated, truncated, info)."""
         528 +        action = np.asarray(action, dtype=self.action_space.dtype)
         529 +        response = self._request({"cmd": "step", "action": _encode(action)})
         530 +        return (
         531 +            response["obs"],
         532 +            response["reward"],
         533 +            response["terminated"],
         534 +            response["truncated"],
         535 +            response["info"],
         536 +        )
         537 +
         538 +    def get_state(self) -> Any:
         539 +        """Return a snapshot of the full environment state.
         540 +
         541 +        A Box vector for a fixed-count env; a local ObjectCentricState for a
         542 +        variable-count env (reconstructed by ``_decode``).
         543 +        """
         544 +        return self._request({"cmd": "get_state"})["state"]
         545 +
         546 +    def _encode_state(self, state: Any) -> Any:
         547 +        """Encode a state for the wire: an object-centric state or a Box vector."""
         548 +        if isinstance(state, _ObjectCentricState):
         549 +            return _encode(state)
         550 +        return _encode(np.asarray(state))
         551 +
         552 +    def render_state(
         553 +        self,
         554 +        seed: int = 42,
         555 +        state: Any = None,
         556 +        label: str = "",
         557 +        object_count: int | None = None,
         558 +    ) -> str:
         559 +        """Render a state on the host; returns a PNG path inside the sandbox.
         560 +
         561 +        Either pass ``seed`` to render the initial state after a reset (with
         562 +        ``object_count`` to pin a variable-count env's object count), or ``state`` (a
         563 +        flat list of floats, as from ``get_state().tolist()``) to render an arbitrary
         564 +        state. The path is relative to the sandbox dir.
         565 +        """
         566 +        if isinstance(state, _ObjectCentricState):
         567 +            state = _encode(state)  # tagged object-centric payload, decoded host-side
         568 +        elif isinstance(state, np.ndarray):
         569 +            state = state.tolist()
         570 +        return self._request(
         571 +            {
         572 +                "cmd": "render_state",
         573 +                "seed": seed,
         574 +                "state": state,
         575 +                "label": label,
         576 +                "object_count": object_count,
         577 +            }
         578 +        )["path"]
         579 +
         580 +    def render_policy(
         581 +        self,
         582 +        seed: int = 42,
         583 +        max_steps: int = 1000,
         584 +        max_frames: int = 100,
         585 +        approach_path: Any = None,
         586 +        object_count: int | None = None,
         587 +    ) -> list[str]:
         588 +        """Run an episode of approach.py here and render the visited states.
         589 +
         590 +        The policy runs in this process: only ``get_action`` (which needs the
         591 +        observation alone) executes locally, while each visited state is
         592 +        rendered on the host via ``render_state``. No approach code runs on the
         593 +        host, so a black-box agent cannot reach the env source through rendering.
         594 +        ``object_count`` pins a variable-count env's object count on the rollout reset.
         595 +        Returns the PNG paths (relative to the sandbox dir).
         596 +        """
         597 +        path = (
         598 +            Path(approach_path)
         599 +            if approach_path is not None
         600 +            else self._sandbox_root / "approach.py"
         601 +        )
         602 +        approach = _load_generated_approach(
         603 +            path, self.action_space, self.observation_space, self.make_primitives()
         604 +        )
         605 +        options = {"object_count": object_count} if object_count is not None else None
         606 +        obs, info = self.reset(seed=seed, options=options)
         607 +        approach.reset(obs, info)
         608 +        # Strict mode deliberately withholds raw state snapshots. Its observations
         609 +        # are nevertheless renderable, so use them to visualize a policy without
         610 +        # opening the get_state channel to agent scripts.
         611 +        states = [obs if self._strict else self.get_state()]
         612 +        for _ in range(max_steps):
         613 +            obs, reward, terminated, truncated, info = self.step(
         614 +                approach.get_action(obs)
         615 +            )
         616 +            if hasattr(approach, "update"):
         617 +                approach.update(obs, reward, terminated or truncated, info)
         618 +            states.append(obs if self._strict else self.get_state())
         619 +            if terminated or truncated:
         620 +                break
         621 +        return [
         622 +            self.render_state(state=state, label=f"policy_seed{seed}_{i:04d}")
         623 +            for i, state in enumerate(states[:max_frames])
         624 +        ]
         625 +
         626 +    def set_state(self, state: Any) -> None:
         627 +        """Restore a state snapshot previously returned by get_state()."""
         628 +        self._request({"cmd": "set_state", "state": self._encode_state(state)})
         629 +
         630 +    def check_action_collision(self, state: Any, action: Any) -> bool:
         631 +        """Return True if taking *action* in *state* causes a collision.
         632 +
         633 +        Runs the env-dependent collision primitive on the host (the sandbox
         634 +        lacks the env source), against this connection's env. Mirrors the
         635 +        eval-time ``primitives['check_action_collision']`` callable, so test
         636 +        scripts that get it from ``make_primitives`` call it the same way.
         637 +        """
         638 +        response = self._request(
         639 +            {
         640 +                "cmd": "check_action_collision",
         641 +                "state": self._encode_state(state),
         642 +                "action": _encode(np.asarray(action, dtype=self.action_space.dtype)),
         643 +            }
         644 +        )
         645 +        return response["collision"]
         646 +
         647 +    def make_primitives(self) -> dict[str, Any]:
         648 +        """Build the eval-time primitives dict for this black-box env.
         649 +
         650 +        Black-box counterpart of ``robocode.primitives.build_primitives``:
         651 +        env-dependent primitives proxy to the host, while generic ones are
         652 +        imported from their copies under ``primitives/`` in the sandbox. Use
         653 +        it in test scripts so they exercise exactly the primitives the harness
         654 +        passes to ``GeneratedApproach`` at evaluation time::
         655 +
         656 +            from env_client import make_env
         657 +
         658 +            env = make_env()
         659 +            primitives = env.make_primitives()
         660 +        """
         661 +        sandbox_dir = str(self._sandbox_root.resolve())
         662 +        if sandbox_dir not in sys.path:
         663 +            sys.path.insert(0, sandbox_dir)
         664 +        primitives: dict[str, Any] = {}
         665 +        for spec in self._primitive_manifest:
         666 +            if spec["kind"] == "host_proxy":
         667 +                primitives[spec["name"]] = getattr(self, spec["name"])
         668 +            elif spec["kind"] == "remote_module":
         669 +                # The module source is withheld from the sandbox; reach it on
         670 +                # the host via a remote-module proxy (e.g. crv_motion_planning).
         671 +                primitives[spec["name"]] = _RemoteModule(self, spec["module"])
         672 +            else:
         673 +                module = importlib.import_module(f"primitives.{spec['module']}")
         674 +                primitives[spec["name"]] = (
         675 +                    module if spec["attr"] is None else getattr(module, spec["attr"])
         676 +                )
         677 +        return primitives
         678 +
         679 +    def close(self) -> None:
         680 +        """Close the connection (and the server-side environment)."""
         681 +        try:
         682 +            self._file.write(
         683 +                json.dumps({"cmd": "close", "token": self._token}).encode("utf-8")
         684 +                + b"\n"
         685 +            )
         686 +            self._file.flush()
         687 +        finally:
         688 +            # makefile() wraps a dup of the socket; close it too so the buffered
         689 +            # file object does not leak (ResourceWarning) when close() runs.
         690 +            self._file.close()
         691 +            self._sock.close()
         692 +
         693 +    def __enter__(self) -> "BlackboxEnv":
         694 +        return self
         695 +
         696 +    def __exit__(self, *exc_info: Any) -> None:
         697 +        self.close()
         698 +
         699 +
         700 +def _load_generated_approach(
         701 +    path: Path, action_space: Any, observation_space: Any, primitives: dict[str, Any]
         702 +) -> Any:
         703 +    """Exec ``approach.py`` and instantiate its ``GeneratedApproach``.
         704 +
         705 +    Mirrors ``robocode.utils.episode.load_generated_approach``; duplicated here
         706 +    (like the codec above) because this module must stay importable with only
         707 +    the standard library and numpy, since it is copied standalone into the
         708 +    sandbox. Used only by ``render_policy`` for visual debugging.
         709 +    """
         710 +    sandbox_dir = str(path.resolve().parent)
         711 +    added = sandbox_dir not in sys.path
         712 +    if added:
         713 +        sys.path.insert(0, sandbox_dir)
         714 +    try:
         715 +        namespace: dict[str, Any] = {"__file__": str(path)}
         716 +        exec(  # pylint: disable=exec-used
         717 +            compile(path.read_text(encoding="utf-8"), str(path), "exec"), namespace
         718 +        )
         719 +    finally:
         720 +        if added:
         721 +            sys.path.remove(sandbox_dir)
         722 +    return namespace["GeneratedApproach"](
         723 +        action_space, observation_space, primitives=primitives
         724 +    )
         725 +
         726 +
         727 +def make_env(metadata_path: Any = None) -> BlackboxEnv:
         728 +    """Connect to the environment server; returns a fresh env instance.
         729 +
         730 +    *metadata_path* defaults to ``env_spaces.json`` next to this module
         731 +    (the agent's sandbox copy); the MCP server passes an explicit path.
         732 +    """
         733 +    path = Path(metadata_path) if metadata_path is not None else _METADATA_PATH
         734 +    meta = json.loads(path.read_text(encoding="utf-8"))
         735 +    return BlackboxEnv(meta, sandbox_root=path.parent)
diff --git a/env_spaces.json b/env_spaces.json
new file mode 100644
index 0000000..9a71400
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1,98 @@
           1 +{
           2 +  "host": "127.0.0.1",
           3 +  "port": 46737,
           4 +  "token": "39fffb3ad582258cc6754e143d3fd913",
           5 +  "observation_space": {
           6 +    "type": "ObjectCentric",
           7 +    "types": [
           8 +      {
           9 +        "name": "lander",
          10 +        "parent": null,
          11 +        "features": [
          12 +          "x",
          13 +          "y",
          14 +          "z"
          15 +        ]
          16 +      },
          17 +      {
          18 +        "name": "objective",
          19 +        "parent": null,
          20 +        "features": [
          21 +          "x",
          22 +          "y",
          23 +          "z",
          24 +          "have_image_rover0",
          25 +          "have_image_rover1",
          26 +          "received_image"
          27 +        ]
          28 +      },
          29 +      {
          30 +        "name": "obstacle",
          31 +        "parent": null,
          32 +        "features": [
          33 +          "x",
          34 +          "y",
          35 +          "z",
          36 +          "half_x",
          37 +          "half_y",
          38 +          "half_z"
          39 +        ]
          40 +      },
          41 +      {
          42 +        "name": "rover",
          43 +        "parent": null,
          44 +        "features": [
          45 +          "x",
          46 +          "y",
          47 +          "theta",
          48 +          "store_full",
          49 +          "calibrated",
          50 +          "at_home"
          51 +        ]
          52 +      },
          53 +      {
          54 +        "name": "sample",
          55 +        "parent": null,
          56 +        "features": [
          57 +          "x",
          58 +          "y",
          59 +          "z",
          60 +          "is_soil",
          61 +          "analyzed_rover0",
          62 +          "analyzed_rover1",
          63 +          "received_analysis"
          64 +        ]
          65 +      }
          66 +    ]
          67 +  },
          68 +  "action_space": {
          69 +    "type": "Box",
          70 +    "shape": [
          71 +      8
          72 +    ],
          73 +    "low": [
          74 +      -0.20000000298023224,
          75 +      -0.20000000298023224,
          76 +      -0.4000000059604645,
          77 +      -1.0,
          78 +      -0.20000000298023224,
          79 +      -0.20000000298023224,
          80 +      -0.4000000059604645,
          81 +      -1.0
          82 +    ],
          83 +    "high": [
          84 +      0.20000000298023224,
          85 +      0.20000000298023224,
          86 +      0.4000000059604645,
          87 +      1.0,
          88 +      0.20000000298023224,
          89 +      0.20000000298023224,
          90 +      0.4000000059604645,
          91 +      1.0
          92 +    ],
          93 +    "dtype": "float32"
          94 +  },
          95 +  "max_steps": 1000,
          96 +  "primitives": [],
          97 +  "strict": true
          98 +}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · add geometry-aware dual rover planning baseline

Commit `9388a139d79dbc412ac5812c56064bc5735ec322`; parents: 79958ef92f9217e28907411987d00e67fe9cb759. Recorded author date: 2026-09-11T11:34:12+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0012](01_timeline.md#E0012): commit hash in recorded output.
[Controller after this commit](evidence/versions/C002_9388a13_approach.py) · [Exact all-file diff](evidence/diffs/C002_9388a13.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..ce70d8d
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,190 @@
           1 +"""Geometry-aware policy for the black-box Rovers environment."""
           2 +import math
           3 +import heapq
           4 +import numpy as np
           5 +
           6 +
           7 +class GeneratedApproach:
           8 +    # Centres of sample, calibrate, image, noop, send, drop selector bands.
           9 +    OPS = {"sample": -5/6, "calibrate": -1/2, "image": -1/6,
          10 +           "noop": 1/6, "send": 1/2, "drop": 5/6}
          11 +
          12 +    def __init__(self, action_space, observation_space, primitives):
          13 +        self.action_space = action_space
          14 +        self.space = observation_space
          15 +        self.types = {t.name: t for t in observation_space.types}
          16 +
          17 +    def _get(self, s, typ):
          18 +        return s.get_objects(self.types[typ])
          19 +
          20 +    def reset(self, state, info):
          21 +        self.names = [[o.name for o in self._get(state, "rover")][i] for i in range(2)]
          22 +        self.home = []
          23 +        for n in self.names:
          24 +            r = state.get_object_from_name(n)
          25 +            self.home.append((state.get(r, "x"), state.get(r, "y")))
          26 +        self.phase = ["work", "work"]
          27 +        self.paths = [[], []]
          28 +        self.targets = [None, None]
          29 +        self.stalls = [0, 0]
          30 +        self.lastpos = list(self.home)
          31 +
          32 +    def _rects(self, s):
          33 +        ans = []
          34 +        for o in self._get(s, "obstacle"):
          35 +            ans.append((s.get(o,"x"), s.get(o,"y"), s.get(o,"half_x"), s.get(o,"half_y")))
          36 +        # Lander is a physical obstacle; use a conservative footprint.
          37 +        for o in self._get(s, "lander"):
          38 +            ans.append((s.get(o,"x"), s.get(o,"y"), .32, .32))
          39 +        return ans
          40 +
          41 +    @staticmethod
          42 +    def _seg_rect(a, b, rect, pad=0.0):
          43 +        # Slab intersection, including boundaries.
          44 +        x, y, hx, hy = rect
          45 +        lo, hi = 0.0, 1.0
          46 +        for p, q, mn, mx in ((a[0], b[0], x-hx-pad, x+hx+pad),
          47 +                             (a[1], b[1], y-hy-pad, y+hy+pad)):
          48 +            d = q-p
          49 +            if abs(d) < 1e-9:
          50 +                if p < mn or p > mx: return False
          51 +            else:
          52 +                u, v = (mn-p)/d, (mx-p)/d
          53 +                if u > v: u, v = v, u
          54 +                lo, hi = max(lo,u), min(hi,v)
          55 +                if lo > hi: return False
          56 +        return True
          57 +
          58 +    def _free(self, p, rects, pad=.24):
          59 +        if p[0] < -2.30 or p[0] > 2.30 or p[1] < -2.30 or p[1] > 2.30:
          60 +            return False
          61 +        return not any(abs(p[0]-x) <= hx+pad and abs(p[1]-y) <= hy+pad
          62 +                       for x,y,hx,hy in rects)
          63 +
          64 +    def _los(self, p, q, rects):
          65 +        # Ignore an obstacle containing the target (objective's own mound).
          66 +        for rect in rects:
          67 +            x,y,hx,hy = rect
          68 +            if abs(q[0]-x) <= hx+1e-5 and abs(q[1]-y) <= hy+1e-5:
          69 +                continue
          70 +            if self._seg_rect(p, q, rect, .01): return False
          71 +        return True
          72 +
          73 +    def _astar(self, start, goals, rects):
          74 +        if not goals: return []
          75 +        step = .20
          76 +        # Lattice anchored at current location, keeping actions exactly feasible.
          77 +        def pos(k): return (start[0]+k[0]*step, start[1]+k[1]*step)
          78 +        goal = min(goals, key=lambda g: (g[0]-start[0])**2+(g[1]-start[1])**2)
          79 +        def h(k):
          80 +            p=pos(k); return max(abs(p[0]-goal[0]),abs(p[1]-goal[1]))/step
          81 +        openq=[(h((0,0)),0,(0,0))]; parent={}; cost={(0,0):0}
          82 +        end=None
          83 +        for _ in range(12000):
          84 +            if not openq: break
          85 +            _,g,k=heapq.heappop(openq)
          86 +            if g != cost.get(k): continue
          87 +            p=pos(k)
          88 +            if any((p[0]-q[0])**2+(p[1]-q[1])**2 <= .10**2 for q in goals):
          89 +                end=k; break
          90 +            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
          91 +                nk=(k[0]+dx,k[1]+dy); np_=pos(nk)
          92 +                if not self._free(np_,rects): continue
          93 +                # Endpoint checking suffices for convex inflated rectangles at this resolution,
          94 +                # except diagonal corner cutting.
          95 +                if not self._free((p[0]+dx*step,p[1]),rects) and dx and dy: continue
          96 +                if not self._free((p[0],p[1]+dy*step),rects) and dx and dy: continue
          97 +                ng=g+1
          98 +                if ng < cost.get(nk,10**9):
          99 +                    cost[nk]=ng; parent[nk]=k; heapq.heappush(openq,(ng+h(nk),ng,nk))
         100 +        if end is None: return []
         101 +        ks=[]
         102 +        while end != (0,0): ks.append(end); end=parent[end]
         103 +        ks.reverse()
         104 +        return [pos(k) for k in ks]
         105 +
         106 +    def _candidates(self, s, q, radius, require_los=True):
         107 +        rects=self._rects(s); out=[]
         108 +        # Fine angular rings give plenty of robust visibility choices.
         109 +        for rad in (min(radius*.72,1.55), min(radius*.88,1.82), radius*.55):
         110 +            for j in range(32):
         111 +                a=2*math.pi*j/32
         112 +                p=(q[0]+rad*math.cos(a),q[1]+rad*math.sin(a))
         113 +                if self._free(p,rects) and (not require_los or self._los(p,q,rects)):
         114 +                    out.append(p)
         115 +        return out
         116 +
         117 +    def _choose_task(self, s, i, pos):
         118 +        r=s.get_object_from_name(self.names[i])
         119 +        rects=self._rects(s)
         120 +        # Finish any held sample result, then empty store.
         121 +        if s.get(r,"store_full") > .5:
         122 +            land=self._get(s,"lander")[0]; q=(s.get(land,"x"),s.get(land,"y"))
         123 +            if math.dist(pos,q) <= 3.85 and self._los(pos,q,rects): return ("send",pos)
         124 +            cs=self._candidates(s,q,3.8,True); return ("nav_send", min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
         125 +        # Split objectives deterministically between the rovers.
         126 +        need=[]
         127 +        for j,o in enumerate(self._get(s,"objective")):
         128 +            if j%2==i and s.get(o,"received_image") < .5:
         129 +                q=(s.get(o,"x"),s.get(o,"y")); need.append((o,q))
         130 +        if need:
         131 +            # If we have an unsent image and can see lander, send opportunistically.
         132 +            land=self._get(s,"lander")[0]; lq=(s.get(land,"x"),s.get(land,"y"))
         133 +            if any(s.get(o,"have_image_rover%d"%i)>.5 for o in self._get(s,"objective")):
         134 +                if math.dist(pos,lq)<=3.85 and self._los(pos,lq,rects): return ("send",pos)
         135 +            best=None
         136 +            for o,q in need:
         137 +                # Already photographed by this rover: only needs sending.
         138 +                if s.get(o,"have_image_rover%d"%i)>.5: continue
         139 +                if math.dist(pos,q)<=1.90 and self._los(pos,q,rects):
         140 +                    return (("image" if s.get(r,"calibrated")>.5 else "calibrate"),pos)
         141 +                cs=self._candidates(s,q,1.9,True)
         142 +                if cs:
         143 +                    p=min(cs,key=lambda x:math.dist(pos,x)); val=math.dist(pos,p)
         144 +                    if best is None or val<best[0]: best=(val,p)
         145 +            if best: return ("nav_image",best[1])
         146 +            # All local images taken: go radio.
         147 +            cs=self._candidates(s,lq,3.8,True); return ("nav_send",min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
         148 +        # One rover takes stone, the other soil, choosing nearest unreceived sample.
         149 +        soil=bool(i)
         150 +        samples=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==soil and s.get(o,"received_analysis")<.5]
         151 +        if samples:
         152 +            candidates=[]
         153 +            for o in samples:
         154 +                q=(s.get(o,"x"),s.get(o,"y"))
         155 +                if s.get(o,"analyzed_rover%d"%i)>.5:
         156 +                    land=self._get(s,"lander")[0]; lq=(s.get(land,"x"),s.get(land,"y"))
         157 +                    if math.dist(pos,lq)<=3.85 and self._los(pos,lq,rects): return ("send",pos)
         158 +                    cs=self._candidates(s,lq,3.8,True)
         159 +                    return ("nav_send",min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
         160 +                q=(s.get(o,"x"),s.get(o,"y"))
         161 +                candidates.append((math.dist(pos,q),q))
         162 +            q=min(candidates)[1]
         163 +            if math.dist(pos,q)<=.24: return ("sample",pos)
         164 +            return ("nav_sample",q)
         165 +        # No pending work of our nominal class: help with anything globally missing.
         166 +        return ("home",self.home[i])
         167 +
         168 +    def get_action(self, state):
         169 +        a=np.zeros(8,dtype=np.float32)
         170 +        rects=self._rects(state)
         171 +        for i in range(2):
         172 +            r=state.get_object_from_name(self.names[i]); pos=(state.get(r,"x"),state.get(r,"y"))
         173 +            task,target=self._choose_task(state,i,pos)
         174 +            op=task if task in self.OPS else "noop"
         175 +            if task.startswith("nav") or task=="home":
         176 +                key=(task,round(target[0],2),round(target[1],2))
         177 +                if self.targets[i]!=key or not self.paths[i] or self.stalls[i]>=2:
         178 +                    radius=.24 if task=="nav_sample" else .12
         179 +                    goals=[target] if radius<.2 else self._candidates(state,target,radius,False)+[target]
         180 +                    self.paths[i]=self._astar(pos,goals,rects)
         181 +                    self.targets[i]=key; self.stalls[i]=0
         182 +                while self.paths[i] and math.dist(pos,self.paths[i][0])<.05: self.paths[i].pop(0)
         183 +                if self.paths[i]:
         184 +                    wp=self.paths[i][0]
         185 +                    a[4*i]=max(-.2,min(.2,wp[0]-pos)); a[4*i+1]=max(-.2,min(.2,wp[1]-pos))
         186 +            a[4*i+3]=self.OPS[op]
         187 +            moved=math.dist(pos,self.lastpos[i])>.03
         188 +            self.stalls[i]=0 if moved or (abs(a[4*i])+abs(a[4*i+1])<.01) else self.stalls[i]+1
         189 +            self.lastpos[i]=pos
         190 +        return a
diff --git a/inspect_env.py b/inspect_env.py
new file mode 100644
index 0000000..52e8152
--- /dev/null
+++ b/inspect_env.py
@@ -0,0 +1,11 @@
           1 +from env_client import make_env
           2 +
           3 +for seed in range(4):
           4 +    env = make_env()
           5 +    s, info = env.reset(seed=seed)
           6 +    print("SEED", seed, "max", env.max_steps, "info", info)
           7 +    for name in sorted(s.get_object_names()):
           8 +        o = s.get_object_from_name(name)
           9 +        fs = s.type_features[o.type]
          10 +        print(name, dict(zip(fs, [s.get(o, f) for f in fs])))
          11 +    env.close()
diff --git a/probe_layouts.out b/probe_layouts.out
new file mode 100644
index 0000000..be055d5
--- /dev/null
+++ b/probe_layouts.out
@@ -0,0 +1,367 @@
           1 +SEED 0 max_steps 1000 info {'object_count': 3}
           2 +names 24 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'objective2', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
           3 + TYPE lander n 1
           4 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
           5 + TYPE objective n 3
           6 +   objective0 {'x': 0.6602243185043335, 'y': 1.9191694259643555, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
           7 +   objective1 {'x': 1.9636701345443726, 'y': 2.109961986541748, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
           8 +   objective2 {'x': -1.8657476902008057, 'y': 2.1903953552246094, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
           9 + TYPE sample n 6
          10 +   sample0 {'x': -1.6931731700897217, 'y': 0.9708871245384216, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          11 +   sample1 {'x': -1.192281723022461, 'y': 2.3732709884643555, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          12 +   sample2 {'x': 0.19003422558307648, 'y': 1.4868561029434204, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          13 +   sample3 {'x': -1.386987328529358, 'y': 0.15173353254795074, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          14 +   sample4 {'x': -0.27064311504364014, 'y': -2.040459394454956, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          15 +   sample5 {'x': -0.9967090487480164, 'y': 0.7318636775016785, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          16 + TYPE rover n 2
          17 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
          18 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
          19 + TYPE obstacle n 12
          20 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          21 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          22 +   obstacle10 {'x': -1.808438777923584, 'y': -1.5490243434906006, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          23 +   obstacle11 {'x': -2.3528029918670654, 'y': -0.02079753205180168, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          24 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          25 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          26 +   obstacle4 {'x': 0.2724447250366211, 'y': 1.2091444730758667, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          27 +   obstacle5 {'x': -0.8076643943786621, 'y': 0.1918671876192093, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          28 +   obstacle6 {'x': -0.13526616990566254, 'y': -0.6399457454681396, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          29 +   obstacle7 {'x': -1.3539739847183228, 'y': 0.5535165071487427, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          30 +   obstacle8 {'x': 1.3540021181106567, 'y': 2.2589950561523438, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          31 +   obstacle9 {'x': 0.6542917490005493, 'y': -0.19871839880943298, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          32 +SEED 1 max_steps 1000 info {'object_count': 2}
          33 +names 23 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
          34 + TYPE lander n 1
          35 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
          36 + TYPE objective n 2
          37 +   objective0 {'x': 2.117588520050049, 'y': 1.9229792356491089, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
          38 +   objective1 {'x': -2.114065170288086, 'y': 2.0957462787628174, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
          39 + TYPE sample n 6
          40 +   sample0 {'x': -2.1286683082580566, 'y': 0.17148301005363464, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          41 +   sample1 {'x': -1.4853466749191284, 'y': -1.3669425249099731, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          42 +   sample2 {'x': -2.213594436645508, 'y': 0.5535051226615906, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          43 +   sample3 {'x': 0.5465056300163269, 'y': -1.348296880722046, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          44 +   sample4 {'x': 2.296544075012207, 'y': 1.3868496417999268, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          45 +   sample5 {'x': -1.403843641281128, 'y': 1.7180376052856445, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          46 + TYPE rover n 2
          47 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
          48 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
          49 + TYPE obstacle n 12
          50 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          51 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          52 +   obstacle10 {'x': 0.31049302220344543, 'y': 0.5678908228874207, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          53 +   obstacle11 {'x': 0.23704051971435547, 'y': -0.1867079883813858, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          54 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          55 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          56 +   obstacle4 {'x': 0.33527684211730957, 'y': -1.010396122932434, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          57 +   obstacle5 {'x': -1.3300279378890991, 'y': -0.6791890859603882, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          58 +   obstacle6 {'x': -0.4819117486476898, 'y': -0.3552263081073761, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          59 +   obstacle7 {'x': 0.2668764293193817, 'y': 0.9906727075576782, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          60 +   obstacle8 {'x': -1.002398133277893, 'y': 0.43533992767333984, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          61 +   obstacle9 {'x': 2.192112684249878, 'y': -2.2338356971740723, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          62 +SEED 2 max_steps 1000 info {'object_count': 3}
          63 +names 24 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'objective2', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
          64 + TYPE lander n 1
          65 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
          66 + TYPE objective n 3
          67 +   objective0 {'x': 0.4399506747722626, 'y': 1.8454203605651855, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
          68 +   objective1 {'x': -2.1755123138427734, 'y': 1.8365923166275024, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
          69 +   objective2 {'x': -0.4921627342700958, 'y': 1.8822369575500488, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
          70 + TYPE sample n 6
          71 +   sample0 {'x': -1.260940432548523, 'y': 1.4199334383010864, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          72 +   sample1 {'x': -2.227665662765503, 'y': -0.20427893102169037, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          73 +   sample2 {'x': -1.6537846326828003, 'y': 2.02565598487854, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          74 +   sample3 {'x': 0.3442700207233429, 'y': -1.0490632057189941, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          75 +   sample4 {'x': -1.795253872871399, 'y': -0.9030962586402893, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          76 +   sample5 {'x': 0.27009862661361694, 'y': -0.1309989094734192, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
          77 + TYPE rover n 2
          78 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
          79 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
          80 + TYPE obstacle n 12
          81 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          82 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          83 +   obstacle10 {'x': -0.21526943147182465, 'y': -0.5559921264648438, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          84 +   obstacle11 {'x': 0.7348376512527466, 'y': 0.4442424476146698, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          85 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          86 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
          87 +   obstacle4 {'x': 2.1178300380706787, 'y': -0.9612797498703003, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          88 +   obstacle5 {'x': -1.7171909809112549, 'y': 0.9063087105751038, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          89 +   obstacle6 {'x': 1.639979600906372, 'y': 0.7337386012077332, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          90 +   obstacle7 {'x': 1.7862882614135742, 'y': -0.5400499105453491, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          91 +   obstacle8 {'x': -0.9069060683250427, 'y': 1.2679052352905273, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          92 +   obstacle9 {'x': -2.1559410095214844, 'y': -1.0042955875396729, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
          93 +SEED 3 max_steps 1000 info {'object_count': 3}
          94 +names 24 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'objective2', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
          95 + TYPE lander n 1
          96 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
          97 + TYPE objective n 3
          98 +   objective0 {'x': 1.9244773387908936, 'y': 2.0533640384674072, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
          99 +   objective1 {'x': 0.5048069953918457, 'y': 2.0269014835357666, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         100 +   objective2 {'x': -2.0648295879364014, 'y': 2.040855884552002, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         101 + TYPE sample n 6
         102 +   sample0 {'x': 1.8120503425598145, 'y': 0.7380498647689819, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         103 +   sample1 {'x': 1.7172051668167114, 'y': 0.06407832354307175, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         104 +   sample2 {'x': 2.3241500854492188, 'y': 0.9441180229187012, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         105 +   sample3 {'x': 1.8121854066848755, 'y': -1.1380623579025269, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         106 +   sample4 {'x': -0.9907154440879822, 'y': 2.1148152351379395, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         107 +   sample5 {'x': -2.379605531692505, 'y': -0.9457017779350281, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         108 + TYPE rover n 2
         109 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         110 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         111 + TYPE obstacle n 12
         112 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         113 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         114 +   obstacle10 {'x': 1.4495865106582642, 'y': 0.6304627656936646, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         115 +   obstacle11 {'x': 0.8851555585861206, 'y': 1.204131007194519, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         116 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         117 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         118 +   obstacle4 {'x': -1.5387417078018188, 'y': -0.8219141960144043, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         119 +   obstacle5 {'x': 0.44155824184417725, 'y': -0.022902123630046844, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         120 +   obstacle6 {'x': 0.2903352677822113, 'y': -0.2776281535625458, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         121 +   obstacle7 {'x': 1.9210973978042603, 'y': 2.3438620567321777, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         122 +   obstacle8 {'x': -2.040555715560913, 'y': 0.3285779356956482, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         123 +   obstacle9 {'x': -1.6183394193649292, 'y': -1.390781283378601, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         124 +SEED 4 max_steps 1000 info {'object_count': 3}
         125 +names 24 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'objective2', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
         126 + TYPE lander n 1
         127 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
         128 + TYPE objective n 3
         129 +   objective0 {'x': 0.6825451254844666, 'y': 1.8741904497146606, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         130 +   objective1 {'x': 1.8373348712921143, 'y': 2.1531083583831787, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         131 +   objective2 {'x': -1.8025481700897217, 'y': 1.9246771335601807, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         132 + TYPE sample n 6
         133 +   sample0 {'x': -0.2556298077106476, 'y': 1.2273503541946411, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         134 +   sample1 {'x': -1.5983179807662964, 'y': -0.9514265656471252, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         135 +   sample2 {'x': 1.543015718460083, 'y': 1.4166061878204346, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         136 +   sample3 {'x': -0.8331830501556396, 'y': 2.272369623184204, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         137 +   sample4 {'x': 1.5832135677337646, 'y': -0.7248134016990662, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         138 +   sample5 {'x': -1.7574530839920044, 'y': -0.4015559256076813, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         139 + TYPE rover n 2
         140 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         141 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         142 + TYPE obstacle n 12
         143 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         144 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         145 +   obstacle10 {'x': 1.7166746854782104, 'y': 1.215036153793335, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         146 +   obstacle11 {'x': 1.355916976928711, 'y': -0.639632523059845, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         147 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         148 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         149 +   obstacle4 {'x': -1.8589937686920166, 'y': 0.44547125697135925, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         150 +   obstacle5 {'x': -1.3587859869003296, 'y': 1.0556634664535522, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         151 +   obstacle6 {'x': -0.9720496535301208, 'y': 1.3049595355987549, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         152 +   obstacle7 {'x': 1.249559760093689, 'y': 2.3779003620147705, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         153 +   obstacle8 {'x': 0.1178240180015564, 'y': 0.3486069142818451, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         154 +   obstacle9 {'x': -1.9206608533859253, 'y': 1.2813137769699097, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         155 +SEED 5 max_steps 1000 info {'object_count': 3}
         156 +names 24 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'objective2', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
         157 + TYPE lander n 1
         158 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
         159 + TYPE objective n 3
         160 +   objective0 {'x': 1.9212899208068848, 'y': 1.8827879428863525, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         161 +   objective1 {'x': -0.411826491355896, 'y': 1.9438259601593018, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         162 +   objective2 {'x': -1.9596754312515259, 'y': 2.1125600337982178, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         163 + TYPE sample n 6
         164 +   sample0 {'x': 2.1506261825561523, 'y': -2.236929178237915, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         165 +   sample1 {'x': -1.0157957077026367, 'y': 1.8226312398910522, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         166 +   sample2 {'x': 1.209559679031372, 'y': 2.0007026195526123, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         167 +   sample3 {'x': 2.0523154735565186, 'y': -1.8467820882797241, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         168 +   sample4 {'x': 1.1003532409667969, 'y': -0.8151493072509766, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         169 +   sample5 {'x': -0.17822851240634918, 'y': -2.1917858123779297, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         170 + TYPE rover n 2
         171 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         172 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         173 + TYPE obstacle n 12
         174 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         175 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         176 +   obstacle10 {'x': 0.861774206161499, 'y': -0.2673511505126953, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         177 +   obstacle11 {'x': -1.7443859577178955, 'y': -1.3858054876327515, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         178 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         179 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         180 +   obstacle4 {'x': 0.698523998260498, 'y': 0.18819178640842438, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         181 +   obstacle5 {'x': -0.8571684956550598, 'y': 0.2665146589279175, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         182 +   obstacle6 {'x': 0.7266861200332642, 'y': -0.41026800870895386, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         183 +   obstacle7 {'x': 1.1491450071334839, 'y': -1.1285814046859741, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         184 +   obstacle8 {'x': 2.29902720451355, 'y': -1.7032335996627808, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         185 +   obstacle9 {'x': -1.9301033020019531, 'y': -0.27923136949539185, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         186 +SEED 6 max_steps 1000 info {'object_count': 2}
         187 +names 23 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
         188 + TYPE lander n 1
         189 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
         190 + TYPE objective n 2
         191 +   objective0 {'x': 0.6754189729690552, 'y': 1.9155398607254028, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         192 +   objective1 {'x': -0.616466224193573, 'y': 1.9193686246871948, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         193 + TYPE sample n 6
         194 +   sample0 {'x': 0.9487950801849365, 'y': 1.8743493556976318, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         195 +   sample1 {'x': 1.3928444385528564, 'y': -0.5552215576171875, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         196 +   sample2 {'x': -0.46584615111351013, 'y': -1.2343082427978516, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         197 +   sample3 {'x': -1.4402183294296265, 'y': 0.5656703114509583, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         198 +   sample4 {'x': -2.2347750663757324, 'y': -0.7940686941146851, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         199 +   sample5 {'x': -1.618239164352417, 'y': 2.2083945274353027, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         200 + TYPE rover n 2
         201 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         202 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         203 + TYPE obstacle n 12
         204 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         205 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         206 +   obstacle10 {'x': -0.2593466341495514, 'y': -2.247386932373047, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         207 +   obstacle11 {'x': -1.003123164176941, 'y': 0.9469658136367798, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         208 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         209 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         210 +   obstacle4 {'x': -2.3479177951812744, 'y': 2.1812400817871094, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         211 +   obstacle5 {'x': -1.5802319049835205, 'y': -0.3195483982563019, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         212 +   obstacle6 {'x': 1.0960665941238403, 'y': 0.6989491581916809, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         213 +   obstacle7 {'x': 1.2770472764968872, 'y': 1.2630878686904907, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         214 +   obstacle8 {'x': 1.7658292055130005, 'y': 1.4306260347366333, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         215 +   obstacle9 {'x': 1.532206416130066, 'y': -0.3089228868484497, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         216 +SEED 7 max_steps 1000 info {'object_count': 3}
         217 +names 24 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'objective2', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
         218 + TYPE lander n 1
         219 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
         220 + TYPE objective n 3
         221 +   objective0 {'x': 0.34952637553215027, 'y': 1.9588342905044556, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         222 +   objective1 {'x': 1.829329490661621, 'y': 1.8274201154708862, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         223 +   objective2 {'x': -0.5388090014457703, 'y': 1.8302867412567139, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         224 + TYPE sample n 6
         225 +   sample0 {'x': 2.1423048973083496, 'y': -0.26697438955307007, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         226 +   sample1 {'x': 1.7090951204299927, 'y': 0.04669347032904625, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         227 +   sample2 {'x': 2.3548946380615234, 'y': 2.2761428356170654, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         228 +   sample3 {'x': 0.6676969528198242, 'y': 1.0815653800964355, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         229 +   sample4 {'x': -1.8840984106063843, 'y': 0.37141507863998413, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         230 +   sample5 {'x': 1.0145654678344727, 'y': 1.2299681901931763, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         231 + TYPE rover n 2
         232 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         233 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         234 + TYPE obstacle n 12
         235 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         236 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         237 +   obstacle10 {'x': 1.234261393547058, 'y': 0.04434873163700104, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         238 +   obstacle11 {'x': -0.6932554841041565, 'y': 1.0566117763519287, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         239 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         240 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         241 +   obstacle4 {'x': -0.4931207001209259, 'y': -0.6309523582458496, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         242 +   obstacle5 {'x': 0.7972133159637451, 'y': 1.0064725875854492, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         243 +   obstacle6 {'x': -0.3712671995162964, 'y': 0.7869153022766113, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         244 +   obstacle7 {'x': -0.8229485750198364, 'y': 0.3480057120323181, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         245 +   obstacle8 {'x': -1.828883409500122, 'y': 1.1798979043960571, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         246 +   obstacle9 {'x': 1.5414416790008545, 'y': -1.132764220237732, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         247 +SEED 8 max_steps 1000 info {'object_count': 3}
         248 +names 24 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'objective2', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
         249 + TYPE lander n 1
         250 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
         251 + TYPE objective n 3
         252 +   objective0 {'x': -0.3965030312538147, 'y': 2.1256392002105713, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         253 +   objective1 {'x': 1.857717514038086, 'y': 2.1887311935424805, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         254 +   objective2 {'x': -1.8016111850738525, 'y': 1.8543975353240967, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         255 + TYPE sample n 6
         256 +   sample0 {'x': 1.4873863458633423, 'y': -0.12068790197372437, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         257 +   sample1 {'x': -2.15095853805542, 'y': 0.2470843642950058, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         258 +   sample2 {'x': -2.3156490325927734, 'y': 0.596152663230896, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         259 +   sample3 {'x': 2.1039977073669434, 'y': 0.1862383335828781, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         260 +   sample4 {'x': -0.874420166015625, 'y': 0.12193363159894943, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         261 +   sample5 {'x': -2.1206912994384766, 'y': 1.319748044013977, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         262 + TYPE rover n 2
         263 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         264 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         265 + TYPE obstacle n 12
         266 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         267 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         268 +   obstacle10 {'x': -1.9354742765426636, 'y': 0.3947531282901764, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         269 +   obstacle11 {'x': 0.599370539188385, 'y': 1.2821154594421387, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         270 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         271 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         272 +   obstacle4 {'x': -0.9911293387413025, 'y': 0.8287094831466675, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         273 +   obstacle5 {'x': 1.1889575719833374, 'y': 2.0945098400115967, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         274 +   obstacle6 {'x': 2.3602755069732666, 'y': -1.5905033349990845, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         275 +   obstacle7 {'x': -1.051819920539856, 'y': 1.2043700218200684, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         276 +   obstacle8 {'x': -0.16158358752727509, 'y': -0.08824300765991211, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         277 +   obstacle9 {'x': 1.259828805923462, 'y': 0.6431530117988586, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         278 +SEED 9 max_steps 1000 info {'object_count': 2}
         279 +names 23 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
         280 + TYPE lander n 1
         281 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
         282 + TYPE objective n 2
         283 +   objective0 {'x': -2.1803736686706543, 'y': 2.1017825603485107, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         284 +   objective1 {'x': -0.5382619500160217, 'y': 2.0994715690612793, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         285 + TYPE sample n 6
         286 +   sample0 {'x': 0.7171162962913513, 'y': -0.8487573266029358, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         287 +   sample1 {'x': 1.3344111442565918, 'y': -0.4573226273059845, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         288 +   sample2 {'x': -1.533219575881958, 'y': -0.18037037551403046, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         289 +   sample3 {'x': -1.5739545822143555, 'y': 2.245443820953369, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         290 +   sample4 {'x': -0.2904849946498871, 'y': -1.6218717098236084, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         291 +   sample5 {'x': 1.0769057273864746, 'y': 2.1338231563568115, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         292 + TYPE rover n 2
         293 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         294 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         295 + TYPE obstacle n 12
         296 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         297 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         298 +   obstacle10 {'x': 0.9782406091690063, 'y': 1.2767870426177979, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         299 +   obstacle11 {'x': 1.5264748334884644, 'y': 2.130880832672119, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         300 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         301 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         302 +   obstacle4 {'x': -2.118025302886963, 'y': 0.49105244874954224, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         303 +   obstacle5 {'x': -0.7618707418441772, 'y': -1.1441105604171753, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         304 +   obstacle6 {'x': -0.3413566052913666, 'y': 0.20937201380729675, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         305 +   obstacle7 {'x': 1.4674433469772339, 'y': 0.32685938477516174, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         306 +   obstacle8 {'x': -1.4525147676467896, 'y': -1.2227517366409302, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         307 +   obstacle9 {'x': -1.432167649269104, 'y': -0.13217264413833618, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         308 +SEED 10 max_steps 1000 info {'object_count': 3}
         309 +names 24 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'objective2', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'objective1', 'sample4'}
         310 + TYPE lander n 1
         311 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
         312 + TYPE objective n 3
         313 +   objective0 {'x': -0.3925993740558624, 'y': 1.9287258386611938, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         314 +   objective1 {'x': 0.468386709690094, 'y': 1.815531849861145, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         315 +   objective2 {'x': 1.9908298254013062, 'y': 1.94472336769104, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         316 + TYPE sample n 6
         317 +   sample0 {'x': -1.2423176765441895, 'y': -2.304168701171875, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         318 +   sample1 {'x': 1.1733624935150146, 'y': 1.3862577676773071, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         319 +   sample2 {'x': 1.5047764778137207, 'y': 1.2253191471099854, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         320 +   sample3 {'x': 0.4079228341579437, 'y': -0.5915204882621765, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         321 +   sample4 {'x': -2.029278516769409, 'y': -1.5321757793426514, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         322 +   sample5 {'x': 0.7326945662498474, 'y': 1.4535070657730103, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         323 + TYPE rover n 2
         324 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         325 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         326 + TYPE obstacle n 12
         327 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         328 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         329 +   obstacle10 {'x': 0.38144704699516296, 'y': -1.6358813047409058, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         330 +   obstacle11 {'x': -0.28399938344955444, 'y': -0.7855584621429443, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         331 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         332 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         333 +   obstacle4 {'x': -0.9373608231544495, 'y': 0.39532485604286194, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         334 +   obstacle5 {'x': -1.2283709049224854, 'y': 0.45192721486091614, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         335 +   obstacle6 {'x': 2.3068339824676514, 'y': 0.23645123839378357, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         336 +   obstacle7 {'x': -1.9426652193069458, 'y': 0.20236629247665405, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         337 +   obstacle8 {'x': -0.9029765725135803, 'y': 1.0501313209533691, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         338 +   obstacle9 {'x': -1.1456115245819092, 'y': -0.7056430578231812, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         339 +SEED 11 max_steps 1000 info {'object_count': 1}
         340 +names 22 {'sample1', 'obstacle1', 'obstacle11', 'obstacle8', 'obstacle0', 'rover1', 'obstacle7', 'objective0', 'obstacle10', 'obstacle2', 'sample5', 'obstacle6', 'obstacle3', 'obstacle9', 'sample2', 'obstacle4', 'sample3', 'obstacle5', 'rover0', 'lander', 'sample0', 'sample4'}
         341 + TYPE lander n 1
         342 +   lander {'x': -1.899999976158142, 'y': -2.0, 'z': 0.0030000784900039434}
         343 + TYPE objective n 1
         344 +   objective0 {'x': -2.0966074466705322, 'y': 2.0041697025299072, 'z': 0.20100000500679016, 'have_image_rover0': 0.0, 'have_image_rover1': 0.0, 'received_image': 0.0}
         345 + TYPE sample n 6
         346 +   sample0 {'x': -1.9329649209976196, 'y': 0.16039203107357025, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         347 +   sample1 {'x': 2.0293328762054443, 'y': 0.24305954575538635, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         348 +   sample2 {'x': 1.6306571960449219, 'y': 1.2362234592437744, 'z': 0.006000000052154064, 'is_soil': 0.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         349 +   sample3 {'x': 0.6768538951873779, 'y': -0.917472243309021, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         350 +   sample4 {'x': -1.949135184288025, 'y': 2.3489339351654053, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         351 +   sample5 {'x': -2.3791942596435547, 'y': 1.0255407094955444, 'z': 0.0035000001080334187, 'is_soil': 1.0, 'analyzed_rover0': 0.0, 'analyzed_rover1': 0.0, 'received_analysis': 0.0}
         352 + TYPE rover n 2
         353 +   rover0 {'x': 1.0, 'y': -1.75, 'theta': 3.1415927410125732, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         354 +   rover1 {'x': -1.0, 'y': -1.75, 'theta': 0.0, 'store_full': 0.0, 'calibrated': 0.0, 'at_home': 1.0}
         355 + TYPE obstacle n 12
         356 +   obstacle0 {'x': 2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         357 +   obstacle1 {'x': -2.0, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         358 +   obstacle10 {'x': -1.311220407485962, 'y': 1.8670309782028198, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         359 +   obstacle11 {'x': -0.7415972352027893, 'y': -0.7925357222557068, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         360 +   obstacle2 {'x': 0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         361 +   obstacle3 {'x': -0.5, 'y': 2.0, 'z': 0.05000000074505806, 'half_x': 0.25, 'half_y': 0.25, 'half_z': 0.05000000074505806}
         362 +   obstacle4 {'x': 1.2984998226165771, 'y': 1.0159571170806885, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         363 +   obstacle5 {'x': -0.8423476815223694, 'y': 2.1227071285247803, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         364 +   obstacle6 {'x': 1.8918756246566772, 'y': -0.46649399399757385, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         365 +   obstacle7 {'x': 0.5674732327461243, 'y': 0.9071117043495178, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         366 +   obstacle8 {'x': 1.440147042274475, 'y': -0.19332359731197357, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
         367 +   obstacle9 {'x': 0.48372581601142883, 'y': -2.1444954872131348, 'z': 0.20100000500679016, 'half_x': 0.05000000074505806, 'half_y': 0.05000000074505806, 'half_z': 0.20000000298023224}
diff --git a/probe_layouts.py b/probe_layouts.py
new file mode 100644
index 0000000..1b25142
--- /dev/null
+++ b/probe_layouts.py
@@ -0,0 +1,19 @@
           1 +from env_client import make_env
           2 +
           3 +
           4 +def f(state, obj, name):
           5 +    return float(state.get(obj, name))
           6 +
           7 +
           8 +for seed in range(12):
           9 +    env = make_env()
          10 +    state, info = env.reset(seed=seed)
          11 +    print("SEED", seed, "max_steps", env.max_steps, "info", info)
          12 +    print("names", len(state.get_object_names()), state.get_object_names())
          13 +    for typ in env.observation_space.types:
          14 +        objs = state.get_objects(typ)
          15 +        print(" TYPE", typ.name if hasattr(typ, "name") else typ, "n", len(objs))
          16 +        for o in objs:
          17 +            vals = {x: f(state, o, x) for x in env.observation_space.type_features[typ]}
          18 +            print("  ", o.name if hasattr(o, "name") else o, vals)
          19 +    env.close()
diff --git a/probe_ops.py b/probe_ops.py
new file mode 100644
index 0000000..5424503
--- /dev/null
+++ b/probe_ops.py
@@ -0,0 +1,91 @@
           1 +from env_client import make_env
           2 +import numpy as np
           3 +
           4 +
           5 +def snap(state):
           6 +    out = {}
           7 +    for name in state.get_object_names():
           8 +        obj = state.get_object_from_name(name)
           9 +        feats = {}
          10 +        # Public type metadata is awkward to recover from obj, so query known fields.
          11 +        for f in ("x", "y", "z", "theta", "store_full", "calibrated", "at_home",
          12 +                  "is_soil", "analyzed_rover0", "analyzed_rover1", "received_analysis",
          13 +                  "have_image_rover0", "have_image_rover1", "received_image",
          14 +                  "half_x", "half_y", "half_z"):
          15 +            try:
          16 +                feats[f] = float(state.get(obj, f))
          17 +            except Exception:
          18 +                pass
          19 +        out[name] = feats
          20 +    return out
          21 +
          22 +
          23 +def main():
          24 +    env = make_env()
          25 +    s, info = env.reset(seed=0)
          26 +    print("max_steps", env.max_steps, "action", env.action_space.shape,
          27 +          env.action_space.low.tolist(), env.action_space.high.tolist(), env.action_space.dtype)
          28 +    print("types", env.observation_space.types)
          29 +    print("features", env.observation_space.type_features)
          30 +    print("names", s.get_object_names())
          31 +    for k, v in snap(s).items():
          32 +        print(k, v)
          33 +    print("info", info)
          34 +    env.close()
          35 +
          36 +
          37 +def rover_values(s, i=0):
          38 +    r = s.get_object_from_name("rover%d" % i)
          39 +    return tuple(float(s.get(r, f)) for f in
          40 +                 ("x", "y", "theta", "store_full", "calibrated", "at_home"))
          41 +
          42 +
          43 +def move_to(env, s, xy, rover=0, selector=0.0):
          44 +    for _ in range(100):
          45 +        vals = rover_values(s, rover)
          46 +        dx = max(-0.2, min(0.2, xy[0] - vals[0]))
          47 +        dy = max(-0.2, min(0.2, xy[1] - vals[1]))
          48 +        if abs(dx) < 1e-5 and abs(dy) < 1e-5:
          49 +            return s
          50 +        a = np.zeros(8, dtype=np.float32)
          51 +        off = rover * 4
          52 +        a[off:off + 4] = (dx, dy, 0.0, selector)
          53 +        s, _, term, trunc, _ = env.step(a)
          54 +        if term or trunc:
          55 +            return s
          56 +    return s
          57 +
          58 +
          59 +def sample_trial(selector, pre_offset=0.20, motion=0.0):
          60 +    env = make_env()
          61 +    s, _ = env.reset(seed=0)
          62 +    sample = s.get_object_from_name("sample4")
          63 +    sx, sy = float(s.get(sample, "x")), float(s.get(sample, "y"))
          64 +    # Approach from east through clear southern region.
          65 +    s = move_to(env, s, (sx + pre_offset, sy))
          66 +    before = rover_values(s)
          67 +    a = np.zeros(8, np.float32)
          68 +    a[:4] = (-motion, 0, 0, selector)
          69 +    s, rew, term, trunc, _ = env.step(a)
          70 +    after = rover_values(s)
          71 +    analyzed = float(s.get(sample, "analyzed_rover0"))
          72 +    env.close()
          73 +    return before, after, analyzed, rew, term, trunc
          74 +
          75 +
          76 +def trials():
          77 +    print("SAMPLE SELECTORS")
          78 +    for sel in (-1.0, -0.999, -2/3 - 1e-4, -2/3, -2/3 + 1e-4,
          79 +                -0.5, -1/3, 0.0, 1/3, 2/3, 1.0):
          80 +        print(sel, sample_trial(sel))
          81 +    print("SAMPLE DISTANCE / MOTION ORDER")
          82 +    for off, motion in ((0.249, 0), (0.251, 0), (0.26, .02), (.24, -.02)):
          83 +        print(off, motion, sample_trial(-5/6, off, motion))
          84 +
          85 +
          86 +if __name__ == "__main__":
          87 +    import sys
          88 +    if len(sys.argv) > 1:
          89 +        trials()
          90 +    else:
          91 +        main()
diff --git a/probe_summary.py b/probe_summary.py
new file mode 100644
index 0000000..3d0eace
--- /dev/null
+++ b/probe_summary.py
@@ -0,0 +1,33 @@
           1 +from collections import Counter
           2 +from env_client import make_env
           3 +
           4 +counts = Counter()
           5 +ranges = {}
           6 +assignments = Counter()
           7 +for seed in range(100):
           8 +    env = make_env()
           9 +    s, info = env.reset(seed=seed)
          10 +    counts[info["object_count"]] += 1
          11 +    ots = {str(t): t for t in env.observation_space.types}
          12 +    # Some implementations stringify types as their bare names.
          13 +    for typ in env.observation_space.types:
          14 +        name = getattr(typ, "name", str(typ))
          15 +        for o in s.get_objects(typ):
          16 +            for feat in env.observation_space.type_features[typ]:
          17 +                v = float(s.get(o, feat))
          18 +                key = (name, feat)
          19 +                if key not in ranges:
          20 +                    ranges[key] = [v, v]
          21 +                else:
          22 +                    ranges[key][0] = min(ranges[key][0], v)
          23 +                    ranges[key][1] = max(ranges[key][1], v)
          24 +            if name == "objective":
          25 +                x, y = float(s.get(o, "x")), float(s.get(o, "y"))
          26 +                center = min(((2,2),(-2,2),(.5,2),(-.5,2)), key=lambda p:(x-p[0])**2+(y-p[1])**2)
          27 +                assignments[center] += 1
          28 +    env.close()
          29 +print("counts", counts)
          30 +print("objective mound assignments", assignments)
          31 +for k in sorted(ranges):
          32 +    if k[1] in ("x", "y", "z", "half_x", "half_y", "half_z", "theta"):
          33 +        print(k, tuple(round(v,4) for v in ranges[k]))
```

</details>

<a id="C003"></a>
### C003 · drop transmitted samples and add rollout test harness

Commit `68b0db975447ba7b5c05df3c4dc804423002dd73`; parents: 9388a139d79dbc412ac5812c56064bc5735ec322. Recorded author date: 2026-09-11T11:34:49+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0020](01_timeline.md#E0020): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C003_68b0db9_approach.py) · [Exact all-file diff](evidence/diffs/C003_68b0db9.diff)

[Previous saved controller snapshot](evidence/versions/C002_9388a13_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ce70d8d..9f53796 100644
--- a/approach.py
+++ b/approach.py
@@ -119,6 +119,11 @@ class GeneratedApproach:
  119    119          rects=self._rects(s)
  120    120          # Finish any held sample result, then empty store.
  121    121          if s.get(r,"store_full") > .5:
         122 +            pending_analysis = any(s.get(o,"analyzed_rover%d"%i)>.5 and
         123 +                                   s.get(o,"received_analysis")<.5
         124 +                                   for o in self._get(s,"sample"))
         125 +            if not pending_analysis:
         126 +                return ("drop",pos)
  122    127              land=self._get(s,"lander")[0]; q=(s.get(land,"x"),s.get(land,"y"))
  123    128              if math.dist(pos,q) <= 3.85 and self._los(pos,q,rects): return ("send",pos)
  124    129              cs=self._candidates(s,q,3.8,True); return ("nav_send", min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
diff --git a/probe_summary.py b/probe_summary.py
index 3d0eace..27b043f 100644
--- a/probe_summary.py
+++ b/probe_summary.py
@@ -4,7 +4,7 @@ from env_client import make_env
    4      4  counts = Counter()
    5      5  ranges = {}
    6      6  assignments = Counter()
    7        -for seed in range(100):
           7 +for seed in range(40):
    8      8      env = make_env()
    9      9      s, info = env.reset(seed=seed)
   10     10      counts[info["object_count"]] += 1
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..bc2967f
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,24 @@
           1 +import sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +
           5 +seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
           6 +for seed in seeds:
           7 +    env=make_env(); s,info=env.reset(seed=seed)
           8 +    ap=GeneratedApproach(env.action_space,env.observation_space,env.make_primitives())
           9 +    ap.reset(s,info)
          10 +    term=trunc=False
          11 +    for step in range(env.max_steps):
          12 +        s,r,term,trunc,inf=env.step(ap.get_action(s))
          13 +        if term or trunc: break
          14 +    rovers=[]
          15 +    rt=env.observation_space.get_type("rover")
          16 +    for o in s.get_objects(rt):
          17 +        rovers.append((o.name,round(s.get(o,"x"),2),round(s.get(o,"y"),2),
          18 +                       int(s.get(o,"store_full")),int(s.get(o,"at_home"))))
          19 +    ot=env.observation_space.get_type("objective")
          20 +    st=env.observation_space.get_type("sample")
          21 +    print(seed,info.get("object_count"),step+1,term,trunc,
          22 +          "img",[int(s.get(o,"received_image")) for o in s.get_objects(ot)],
          23 +          "samp",[int(s.get(o,"received_analysis")) for o in s.get_objects(st)],rovers)
          24 +    env.close()
```

</details>

<a id="C004"></a>
### C004 · fix waypoint delta coordinate calculation

Commit `faa36e08cdc133f2200b218ed26323b0eb0b1c30`; parents: 68b0db975447ba7b5c05df3c4dc804423002dd73. Recorded author date: 2026-09-11T11:34:56+02:00.

File roles (automatic): policy.

- [E0027](01_timeline.md#E0027): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_faa36e0_approach.py) · [Exact all-file diff](evidence/diffs/C004_faa36e0.diff)

[Previous saved controller snapshot](evidence/versions/C003_68b0db9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9f53796..8068d7e 100644
--- a/approach.py
+++ b/approach.py
@@ -187,7 +187,7 @@ class GeneratedApproach:
  187    187                  while self.paths[i] and math.dist(pos,self.paths[i][0])<.05: self.paths[i].pop(0)
  188    188                  if self.paths[i]:
  189    189                      wp=self.paths[i][0]
  190        -                    a[4*i]=max(-.2,min(.2,wp[0]-pos)); a[4*i+1]=max(-.2,min(.2,wp[1]-pos))
         190 +                    a[4*i]=max(-.2,min(.2,wp[0]-pos[0])); a[4*i+1]=max(-.2,min(.2,wp[1]-pos[1]))
  191    191              a[4*i+3]=self.OPS[op]
  192    192              moved=math.dist(pos,self.lastpos[i])>.03
  193    193              self.stalls[i]=0 if moved or (abs(a[4*i])+abs(a[4*i+1])<.01) else self.stalls[i]+1
```

</details>

<a id="C005"></a>
### C005 · add compact rollout diagnostics

Commit `a633607d24ae59938b5ffe334cda0a155f5923ed`; parents: faa36e08cdc133f2200b218ed26323b0eb0b1c30. Recorded author date: 2026-09-11T11:36:10+02:00.

File roles (automatic): diagnostic/test.

- [E0033](01_timeline.md#E0033): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C005_a633607.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/debug_rollout.py b/debug_rollout.py
new file mode 100644
index 0000000..c836f8e
--- /dev/null
+++ b/debug_rollout.py
@@ -0,0 +1,14 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +env=make_env(); s,info=env.reset(seed=0)
           4 +ap=GeneratedApproach(env.action_space,env.observation_space,env.make_primitives()); ap.reset(s,info)
           5 +for step in range(160):
           6 +    if step%10==0:
           7 +        vals=[]
           8 +        for i,n in enumerate(ap.names):
           9 +            r=s.get_object_from_name(n); p=(s.get(r,"x"),s.get(r,"y"))
          10 +            vals.append((i,tuple(round(x,2) for x in p),ap._choose_task(s,i,p),len(ap.paths[i]),ap.stalls[i]))
          11 +        print(step,vals)
          12 +    s,r,t,tr,inf=env.step(ap.get_action(s))
          13 +    if t or tr: print("END",step+1,t,tr);break
          14 +env.close()
```

</details>

<a id="C006"></a>
### C006 · model hidden central wall and stop after required sample type

Commit `bd8986244795716076dcb7f20399110d4425db31`; parents: a633607d24ae59938b5ffe334cda0a155f5923ed. Recorded author date: 2026-09-11T11:37:00+02:00.

File roles (automatic): policy.

- [E0043](01_timeline.md#E0043): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C006_bd89862_approach.py) · [Exact all-file diff](evidence/diffs/C006_bd89862.diff)

[Previous saved controller snapshot](evidence/versions/C004_faa36e0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8068d7e..cc6e81f 100644
--- a/approach.py
+++ b/approach.py
@@ -30,7 +30,10 @@ class GeneratedApproach:
   30     30          self.lastpos = list(self.home)
   31     31  
   32     32      def _rects(self, s):
   33        -        ans = []
          33 +        # The central wall is a fixed part of the arena but is intentionally not
          34 +        # listed among observation objects.  Its narrow ends leave routes around
          35 +        # it at the north and south edges.
          36 +        ans = [(0.0, 0.0, .20, 1.50)]
   34     37          for o in self._get(s, "obstacle"):
   35     38              ans.append((s.get(o,"x"), s.get(o,"y"), s.get(o,"half_x"), s.get(o,"half_y")))
   36     39          # Lander is a physical obstacle; use a conservative footprint.
@@ -85,7 +88,7 @@ class GeneratedApproach:
   85     88              _,g,k=heapq.heappop(openq)
   86     89              if g != cost.get(k): continue
   87     90              p=pos(k)
   88        -            if any((p[0]-q[0])**2+(p[1]-q[1])**2 <= .10**2 for q in goals):
          91 +            if any((p[0]-q[0])**2+(p[1]-q[1])**2 <= .15**2 for q in goals):
   89     92                  end=k; break
   90     93              for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
   91     94                  nk=(k[0]+dx,k[1]+dy); np_=pos(nk)
@@ -152,7 +155,10 @@ class GeneratedApproach:
  152    155              cs=self._candidates(s,lq,3.8,True); return ("nav_send",min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
  153    156          # One rover takes stone, the other soil, choosing nearest unreceived sample.
  154    157          soil=bool(i)
  155        -        samples=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==soil and s.get(o,"received_analysis")<.5]
         158 +        matching=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==soil]
         159 +        if any(s.get(o,"received_analysis")>.5 for o in matching):
         160 +            return ("home",self.home[i])
         161 +        samples=[o for o in matching if s.get(o,"received_analysis")<.5]
  156    162          if samples:
  157    163              candidates=[]
  158    164              for o in samples:
```

</details>

<a id="C007"></a>
### C007 · correct wall geometry and allocate work by reachable side

Commit `2646aca54ef40932e46b9cde041b90feaaa6e326`; parents: bd8986244795716076dcb7f20399110d4425db31. Recorded author date: 2026-09-11T11:39:13+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0050](01_timeline.md#E0050): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C007_2646aca_approach.py) · [Exact all-file diff](evidence/diffs/C007_2646aca.diff)

[Previous saved controller snapshot](evidence/versions/C006_bd89862_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index cc6e81f..477f198 100644
--- a/approach.py
+++ b/approach.py
@@ -28,12 +28,25 @@ class GeneratedApproach:
   28     28          self.targets = [None, None]
   29     29          self.stalls = [0, 0]
   30     30          self.lastpos = list(self.home)
          31 +        # Pick one concrete sample of each required kind and give it to the rover
          32 +        # already on that side of the wall.
          33 +        self.sample_jobs = [set(), set()]
          34 +        for soil in (False, True):
          35 +            choices=[]
          36 +            for o in self._get(state,"sample"):
          37 +                if bool(state.get(o,"is_soil")>.5) != soil: continue
          38 +                x,y=state.get(o,"x"),state.get(o,"y")
          39 +                owner=0 if x>=0 else 1
          40 +                choices.append((math.dist(self.home[owner],(x,y)),owner,o.name))
          41 +            if choices:
          42 +                _,owner,name=min(choices)
          43 +                self.sample_jobs[owner].add(soil)
   31     44  
   32     45      def _rects(self, s):
   33     46          # The central wall is a fixed part of the arena but is intentionally not
   34     47          # listed among observation objects.  Its narrow ends leave routes around
   35     48          # it at the north and south edges.
   36        -        ans = [(0.0, 0.0, .20, 1.50)]
          49 +        ans = [(0.0, -1.75, .03, .75)]
   37     50          for o in self._get(s, "obstacle"):
   38     51              ans.append((s.get(o,"x"), s.get(o,"y"), s.get(o,"half_x"), s.get(o,"half_y")))
   39     52          # Lander is a physical obstacle; use a conservative footprint.
@@ -130,10 +143,11 @@ class GeneratedApproach:
  130    143              land=self._get(s,"lander")[0]; q=(s.get(land,"x"),s.get(land,"y"))
  131    144              if math.dist(pos,q) <= 3.85 and self._los(pos,q,rects): return ("send",pos)
  132    145              cs=self._candidates(s,q,3.8,True); return ("nav_send", min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
  133        -        # Split objectives deterministically between the rovers.
         146 +        # Each rover handles objectives on its own side of the short south wall.
  134    147          need=[]
  135    148          for j,o in enumerate(self._get(s,"objective")):
  136        -            if j%2==i and s.get(o,"received_image") < .5:
         149 +            owner=0 if s.get(o,"x")>=0 else 1
         150 +            if owner==i and s.get(o,"received_image") < .5:
  137    151                  q=(s.get(o,"x"),s.get(o,"y")); need.append((o,q))
  138    152          if need:
  139    153              # If we have an unsent image and can see lander, send opportunistically.
@@ -153,11 +167,14 @@ class GeneratedApproach:
  153    167              if best: return ("nav_image",best[1])
  154    168              # All local images taken: go radio.
  155    169              cs=self._candidates(s,lq,3.8,True); return ("nav_send",min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
  156        -        # One rover takes stone, the other soil, choosing nearest unreceived sample.
  157        -        soil=bool(i)
         170 +        # Execute the preassigned one-stone/one-soil jobs (possibly both on one rover).
         171 +        soil=None
         172 +        for kind in sorted(self.sample_jobs[i]):
         173 +            matching=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==kind]
         174 +            if not any(s.get(o,"received_analysis")>.5 for o in matching):
         175 +                soil=kind; break
         176 +        if soil is None: return ("home",self.home[i])
  158    177          matching=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==soil]
  159        -        if any(s.get(o,"received_analysis")>.5 for o in matching):
  160        -            return ("home",self.home[i])
  161    178          samples=[o for o in matching if s.get(o,"received_analysis")<.5]
  162    179          if samples:
  163    180              candidates=[]
diff --git a/probe_ops.py b/probe_ops.py
index 5424503..4a60598 100644
--- a/probe_ops.py
+++ b/probe_ops.py
@@ -56,19 +56,20 @@ def move_to(env, s, xy, rover=0, selector=0.0):
   56     56      return s
   57     57  
   58     58  
   59        -def sample_trial(selector, pre_offset=0.20, motion=0.0):
          59 +def sample_trial(selector, pre_offset=0.20, motion=0.0, rover=1, side=-1):
   60     60      env = make_env()
   61     61      s, _ = env.reset(seed=0)
   62     62      sample = s.get_object_from_name("sample4")
   63     63      sx, sy = float(s.get(sample, "x")), float(s.get(sample, "y"))
   64     64      # Approach from east through clear southern region.
   65        -    s = move_to(env, s, (sx + pre_offset, sy))
   66        -    before = rover_values(s)
          65 +    s = move_to(env, s, (sx + side * pre_offset, sy), rover=rover)
          66 +    before = rover_values(s, rover)
   67     67      a = np.zeros(8, np.float32)
   68        -    a[:4] = (-motion, 0, 0, selector)
          68 +    off = rover * 4
          69 +    a[off:off + 4] = (-side * motion, 0, 0, selector)
   69     70      s, rew, term, trunc, _ = env.step(a)
   70        -    after = rover_values(s)
   71        -    analyzed = float(s.get(sample, "analyzed_rover0"))
          71 +    after = rover_values(s, rover)
          72 +    analyzed = float(s.get(sample, "analyzed_rover%d" % rover))
   72     73      env.close()
   73     74      return before, after, analyzed, rew, term, trunc
   74     75  
diff --git a/probe_side_stats.py b/probe_side_stats.py
new file mode 100644
index 0000000..35a3bcc
--- /dev/null
+++ b/probe_side_stats.py
@@ -0,0 +1,17 @@
           1 +from collections import Counter
           2 +from env_client import make_env
           3 +
           4 +c=Counter(); minabs=9
           5 +for seed in range(40):
           6 + e=make_env(); s,_=e.reset(seed=seed)
           7 + typ=next(t for t in e.observation_space.types if getattr(t,"name",str(t))=="sample")
           8 + nums=[]
           9 + for soil in (0,1):
          10 +  sides=[]
          11 +  for o in s.get_objects(typ):
          12 +   if round(float(s.get(o,"is_soil")))==soil:
          13 +    x=float(s.get(o,"x")); sides.append(x>0); minabs=min(minabs,abs(x))
          14 +  nums.append(sum(sides))
          15 + c[tuple(nums)]+=1
          16 + e.close()
          17 +print(c, "min_abs_x", minabs)
```

</details>

<a id="C008"></a>
### C008 · use validated radio poses and relax lattice goal tolerance

Commit `d7128c0cb7a3fc747f8bf119cafbccea15da5022`; parents: 2646aca54ef40932e46b9cde041b90feaaa6e326. Recorded author date: 2026-09-11T11:40:24+02:00.

File roles (automatic): policy.

- [E0058](01_timeline.md#E0058): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C008_d7128c0_approach.py) · [Exact all-file diff](evidence/diffs/C008_d7128c0.diff)

[Previous saved controller snapshot](evidence/versions/C007_2646aca_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 477f198..c19bb42 100644
--- a/approach.py
+++ b/approach.py
@@ -28,6 +28,9 @@ class GeneratedApproach:
   28     28          self.targets = [None, None]
   29     29          self.stalls = [0, 0]
   30     30          self.lastpos = list(self.home)
          31 +        # Known-clear robust communication poses.  The right rover must stand
          32 +        # above the north tip of the wall for line of sight to the lander.
          33 +        self.radio = [(1.0, .45), self.home[1]]
   31     34          # Pick one concrete sample of each required kind and give it to the rover
   32     35          # already on that side of the wall.
   33     36          self.sample_jobs = [set(), set()]
@@ -101,7 +104,7 @@ class GeneratedApproach:
  101    104              _,g,k=heapq.heappop(openq)
  102    105              if g != cost.get(k): continue
  103    106              p=pos(k)
  104        -            if any((p[0]-q[0])**2+(p[1]-q[1])**2 <= .15**2 for q in goals):
         107 +            if any((p[0]-q[0])**2+(p[1]-q[1])**2 <= .19**2 for q in goals):
  105    108                  end=k; break
  106    109              for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
  107    110                  nk=(k[0]+dx,k[1]+dy); np_=pos(nk)
@@ -140,9 +143,8 @@ class GeneratedApproach:
  140    143                                     for o in self._get(s,"sample"))
  141    144              if not pending_analysis:
  142    145                  return ("drop",pos)
  143        -            land=self._get(s,"lander")[0]; q=(s.get(land,"x"),s.get(land,"y"))
  144        -            if math.dist(pos,q) <= 3.85 and self._los(pos,q,rects): return ("send",pos)
  145        -            cs=self._candidates(s,q,3.8,True); return ("nav_send", min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
         146 +            q=self.radio[i]
         147 +            return ("send",pos) if math.dist(pos,q)<.16 else ("nav_send",q)
  146    148          # Each rover handles objectives on its own side of the short south wall.
  147    149          need=[]
  148    150          for j,o in enumerate(self._get(s,"objective")):
@@ -151,9 +153,9 @@ class GeneratedApproach:
  151    153                  q=(s.get(o,"x"),s.get(o,"y")); need.append((o,q))
  152    154          if need:
  153    155              # If we have an unsent image and can see lander, send opportunistically.
  154        -            land=self._get(s,"lander")[0]; lq=(s.get(land,"x"),s.get(land,"y"))
  155    156              if any(s.get(o,"have_image_rover%d"%i)>.5 for o in self._get(s,"objective")):
  156        -                if math.dist(pos,lq)<=3.85 and self._los(pos,lq,rects): return ("send",pos)
         157 +                q=self.radio[i]
         158 +                return ("send",pos) if math.dist(pos,q)<.16 else ("nav_send",q)
  157    159              best=None
  158    160              for o,q in need:
  159    161                  # Already photographed by this rover: only needs sending.
@@ -166,7 +168,7 @@ class GeneratedApproach:
  166    168                      if best is None or val<best[0]: best=(val,p)
  167    169              if best: return ("nav_image",best[1])
  168    170              # All local images taken: go radio.
  169        -            cs=self._candidates(s,lq,3.8,True); return ("nav_send",min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
         171 +            return ("nav_send",self.radio[i])
  170    172          # Execute the preassigned one-stone/one-soil jobs (possibly both on one rover).
  171    173          soil=None
  172    174          for kind in sorted(self.sample_jobs[i]):
@@ -181,10 +183,8 @@ class GeneratedApproach:
  181    183              for o in samples:
  182    184                  q=(s.get(o,"x"),s.get(o,"y"))
  183    185                  if s.get(o,"analyzed_rover%d"%i)>.5:
  184        -                    land=self._get(s,"lander")[0]; lq=(s.get(land,"x"),s.get(land,"y"))
  185        -                    if math.dist(pos,lq)<=3.85 and self._los(pos,lq,rects): return ("send",pos)
  186        -                    cs=self._candidates(s,lq,3.8,True)
  187        -                    return ("nav_send",min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
         186 +                    q=self.radio[i]
         187 +                    return ("send",pos) if math.dist(pos,q)<.16 else ("nav_send",q)
  188    188                  q=(s.get(o,"x"),s.get(o,"y"))
  189    189                  candidates.append((math.dist(pos,q),q))
  190    190              q=min(candidates)[1]
```

</details>

<a id="C009"></a>
### C009 · show per-rover image flags in rollout diagnostics

Commit `1ab68910e7ad0f0b096fdcc8dc95833c2a93f722`; parents: d7128c0cb7a3fc747f8bf119cafbccea15da5022. Recorded author date: 2026-09-11T11:41:06+02:00.

File roles (automatic): diagnostic/test.

- [E0062](01_timeline.md#E0062): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C009_1ab6891.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/debug_rollout.py b/debug_rollout.py
index c836f8e..6aab3b3 100644
--- a/debug_rollout.py
+++ b/debug_rollout.py
@@ -8,7 +8,9 @@ for step in range(160):
    8      8          for i,n in enumerate(ap.names):
    9      9              r=s.get_object_from_name(n); p=(s.get(r,"x"),s.get(r,"y"))
   10     10              vals.append((i,tuple(round(x,2) for x in p),ap._choose_task(s,i,p),len(ap.paths[i]),ap.stalls[i]))
   11        -        print(step,vals)
          11 +        ots=env.observation_space.get_type("objective")
          12 +        imgs=[(o.name,int(s.get(o,"have_image_rover0")),int(s.get(o,"have_image_rover1")),int(s.get(o,"received_image"))) for o in s.get_objects(ots)]
          13 +        print(step,vals,imgs)
   12     14      s,r,t,tr,inf=env.step(ap.get_action(s))
   13     15      if t or tr: print("END",step+1,t,tr);break
   14     16  env.close()
```

</details>

<a id="C010"></a>
### C010 · advance after sent images and navigate samples to true pickup radius

Commit `10f9a6c93908cb4efc17711a41e8cc9954583d55`; parents: 1ab68910e7ad0f0b096fdcc8dc95833c2a93f722. Recorded author date: 2026-09-11T11:41:28+02:00.

File roles (automatic): policy.

- [E0066](01_timeline.md#E0066): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C010_10f9a6c_approach.py) · [Exact all-file diff](evidence/diffs/C010_10f9a6c.diff)

[Previous saved controller snapshot](evidence/versions/C008_d7128c0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c19bb42..eb63c00 100644
--- a/approach.py
+++ b/approach.py
@@ -49,7 +49,7 @@ class GeneratedApproach:
   49     49          # The central wall is a fixed part of the arena but is intentionally not
   50     50          # listed among observation objects.  Its narrow ends leave routes around
   51     51          # it at the north and south edges.
   52        -        ans = [(0.0, -1.75, .03, .75)]
          52 +        ans = [(0.0, 0.0, .03, 2.50)]
   53     53          for o in self._get(s, "obstacle"):
   54     54              ans.append((s.get(o,"x"), s.get(o,"y"), s.get(o,"half_x"), s.get(o,"half_y")))
   55     55          # Lander is a physical obstacle; use a conservative footprint.
@@ -89,7 +89,7 @@ class GeneratedApproach:
   89     89              if self._seg_rect(p, q, rect, .01): return False
   90     90          return True
   91     91  
   92        -    def _astar(self, start, goals, rects):
          92 +    def _astar(self, start, goals, rects, tolerance=.18):
   93     93          if not goals: return []
   94     94          step = .20
   95     95          # Lattice anchored at current location, keeping actions exactly feasible.
@@ -104,7 +104,7 @@ class GeneratedApproach:
  104    104              _,g,k=heapq.heappop(openq)
  105    105              if g != cost.get(k): continue
  106    106              p=pos(k)
  107        -            if any((p[0]-q[0])**2+(p[1]-q[1])**2 <= .19**2 for q in goals):
         107 +            if any((p[0]-q[0])**2+(p[1]-q[1])**2 <= tolerance**2 for q in goals):
  108    108                  end=k; break
  109    109              for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
  110    110                  nk=(k[0]+dx,k[1]+dy); np_=pos(nk)
@@ -153,7 +153,8 @@ class GeneratedApproach:
  153    153                  q=(s.get(o,"x"),s.get(o,"y")); need.append((o,q))
  154    154          if need:
  155    155              # If we have an unsent image and can see lander, send opportunistically.
  156        -            if any(s.get(o,"have_image_rover%d"%i)>.5 for o in self._get(s,"objective")):
         156 +            if any(s.get(o,"have_image_rover%d"%i)>.5 and s.get(o,"received_image")<.5
         157 +                   for o in self._get(s,"objective")):
  157    158                  q=self.radio[i]
  158    159                  return ("send",pos) if math.dist(pos,q)<.16 else ("nav_send",q)
  159    160              best=None
@@ -203,9 +204,11 @@ class GeneratedApproach:
  203    204              if task.startswith("nav") or task=="home":
  204    205                  key=(task,round(target[0],2),round(target[1],2))
  205    206                  if self.targets[i]!=key or not self.paths[i] or self.stalls[i]>=2:
  206        -                    radius=.24 if task=="nav_sample" else .12
  207        -                    goals=[target] if radius<.2 else self._candidates(state,target,radius,False)+[target]
  208        -                    self.paths[i]=self._astar(pos,goals,rects)
         207 +                    if task=="nav_sample":
         208 +                        goals=[target]; tolerance=.24
         209 +                    else:
         210 +                        goals=[target]; tolerance=.15
         211 +                    self.paths[i]=self._astar(pos,goals,rects,tolerance)
  209    212                      self.targets[i]=key; self.stalls[i]=0
  210    213                  while self.paths[i] and math.dist(pos,self.paths[i][0])<.05: self.paths[i].pop(0)
  211    214                  if self.paths[i]:
```

</details>

<a id="C011"></a>
### C011 · parameterize rollout debugger by seed

Commit `1fafd856b7856bab8c3358717b17fe9c4cdce31f`; parents: 10f9a6c93908cb4efc17711a41e8cc9954583d55. Recorded author date: 2026-09-11T11:42:10+02:00.

File roles (automatic): diagnostic/test.

- [E0070](01_timeline.md#E0070): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C011_1fafd85.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/debug_rollout.py b/debug_rollout.py
index 6aab3b3..0adb950 100644
--- a/debug_rollout.py
+++ b/debug_rollout.py
@@ -1,6 +1,7 @@
           1 +import sys
    1      2  from env_client import make_env
    2      3  from approach import GeneratedApproach
    3        -env=make_env(); s,info=env.reset(seed=0)
           4 +env=make_env(); s,info=env.reset(seed=int(sys.argv[1]) if len(sys.argv)>1 else 0)
    4      5  ap=GeneratedApproach(env.action_space,env.observation_space,env.make_primitives()); ap.reset(s,info)
    5      6  for step in range(160):
    6      7      if step%10==0:
```

</details>

<a id="C012"></a>
### C012 · adapt radio poses around random occluding pillars

Commit `5ceb580fd258b3f0833f2e56189c6efb70db6e61`; parents: 1fafd856b7856bab8c3358717b17fe9c4cdce31f. Recorded author date: 2026-09-11T11:42:49+02:00.

File roles (automatic): policy.

- [E0075](01_timeline.md#E0075): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_5ceb580_approach.py) · [Exact all-file diff](evidence/diffs/C012_5ceb580.diff)

[Previous saved controller snapshot](evidence/versions/C010_10f9a6c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index eb63c00..9e2e916 100644
--- a/approach.py
+++ b/approach.py
@@ -28,9 +28,9 @@ class GeneratedApproach:
   28     28          self.targets = [None, None]
   29     29          self.stalls = [0, 0]
   30     30          self.lastpos = list(self.home)
   31        -        # Known-clear robust communication poses.  The right rover must stand
   32        -        # above the north tip of the wall for line of sight to the lander.
   33        -        self.radio = [(1.0, .45), self.home[1]]
          31 +        self.radio_choices=[self._radio_points(state,i) for i in range(2)]
          32 +        self.radio_idx=[0,0]
          33 +        self.last_ops=["noop","noop"]
   34     34          # Pick one concrete sample of each required kind and give it to the rover
   35     35          # already on that side of the wall.
   36     36          self.sample_jobs = [set(), set()]
@@ -45,6 +45,23 @@ class GeneratedApproach:
   45     45                  _,owner,name=min(choices)
   46     46                  self.sample_jobs[owner].add(soil)
   47     47  
          48 +    def _radio_points(self,s,i):
          49 +        land=self._get(s,"lander")[0]; q=(s.get(land,"x"),s.get(land,"y"))
          50 +        if i==0:
          51 +            raw=[(x,y) for y in (.35,.55,.75,.95) for x in (1.0,.8,.6,.4)]
          52 +        else:
          53 +            raw=[(-1.0,-1.75),(-1.0,-1.45),(-1.3,-1.6),(-1.5,-1.4),(-1.7,-1.2)]
          54 +        rects=self._rects(s)[1:] # wall is low enough to radio over from right poses
          55 +        good=[]
          56 +        for p in raw:
          57 +            if math.dist(p,q)>=3.9 or not self._free(p,self._rects(s)): continue
          58 +            if not any(self._seg_rect(p,q,r,.07) for r in rects): good.append(p)
          59 +        return good or raw
          60 +
          61 +    def _radio(self,i):
          62 +        pts=self.radio_choices[i]
          63 +        return pts[self.radio_idx[i] % len(pts)]
          64 +
   48     65      def _rects(self, s):
   49     66          # The central wall is a fixed part of the arena but is intentionally not
   50     67          # listed among observation objects.  Its narrow ends leave routes around
@@ -143,7 +160,7 @@ class GeneratedApproach:
  143    160                                     for o in self._get(s,"sample"))
  144    161              if not pending_analysis:
  145    162                  return ("drop",pos)
  146        -            q=self.radio[i]
         163 +            q=self._radio(i)
  147    164              return ("send",pos) if math.dist(pos,q)<.16 else ("nav_send",q)
  148    165          # Each rover handles objectives on its own side of the short south wall.
  149    166          need=[]
@@ -155,7 +172,7 @@ class GeneratedApproach:
  155    172              # If we have an unsent image and can see lander, send opportunistically.
  156    173              if any(s.get(o,"have_image_rover%d"%i)>.5 and s.get(o,"received_image")<.5
  157    174                     for o in self._get(s,"objective")):
  158        -                q=self.radio[i]
         175 +                q=self._radio(i)
  159    176                  return ("send",pos) if math.dist(pos,q)<.16 else ("nav_send",q)
  160    177              best=None
  161    178              for o,q in need:
@@ -169,7 +186,7 @@ class GeneratedApproach:
  169    186                      if best is None or val<best[0]: best=(val,p)
  170    187              if best: return ("nav_image",best[1])
  171    188              # All local images taken: go radio.
  172        -            return ("nav_send",self.radio[i])
         189 +            return ("nav_send",self._radio(i))
  173    190          # Execute the preassigned one-stone/one-soil jobs (possibly both on one rover).
  174    191          soil=None
  175    192          for kind in sorted(self.sample_jobs[i]):
@@ -184,7 +201,7 @@ class GeneratedApproach:
  184    201              for o in samples:
  185    202                  q=(s.get(o,"x"),s.get(o,"y"))
  186    203                  if s.get(o,"analyzed_rover%d"%i)>.5:
  187        -                    q=self.radio[i]
         204 +                    q=self._radio(i)
  188    205                      return ("send",pos) if math.dist(pos,q)<.16 else ("nav_send",q)
  189    206                  q=(s.get(o,"x"),s.get(o,"y"))
  190    207                  candidates.append((math.dist(pos,q),q))
@@ -199,6 +216,13 @@ class GeneratedApproach:
  199    216          rects=self._rects(state)
  200    217          for i in range(2):
  201    218              r=state.get_object_from_name(self.names[i]); pos=(state.get(r,"x"),state.get(r,"y"))
         219 +            if self.last_ops[i]=="send":
         220 +                pending_img=any(state.get(o,"have_image_rover%d"%i)>.5 and state.get(o,"received_image")<.5
         221 +                                for o in self._get(state,"objective"))
         222 +                pending_ana=any(state.get(o,"analyzed_rover%d"%i)>.5 and state.get(o,"received_analysis")<.5
         223 +                                for o in self._get(state,"sample"))
         224 +                if pending_img or pending_ana:
         225 +                    self.radio_idx[i]+=1; self.paths[i]=[]; self.targets[i]=None
  202    226              task,target=self._choose_task(state,i,pos)
  203    227              op=task if task in self.OPS else "noop"
  204    228              if task.startswith("nav") or task=="home":
@@ -218,4 +242,5 @@ class GeneratedApproach:
  218    242              moved=math.dist(pos,self.lastpos[i])>.03
  219    243              self.stalls[i]=0 if moved or (abs(a[4*i])+abs(a[4*i+1])<.01) else self.stalls[i]+1
  220    244              self.lastpos[i]=pos
         245 +            self.last_ops[i]=op
  221    246          return a
```

</details>

<a id="C013"></a>
### C013 · densify collision-free fallback radio viewpoints

Commit `b38c5e0df261a1f0126d3e71f13402fc2854f680`; parents: 5ceb580fd258b3f0833f2e56189c6efb70db6e61. Recorded author date: 2026-09-11T11:44:37+02:00.

File roles (automatic): policy.

- [E0081](01_timeline.md#E0081): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_b38c5e0_approach.py) · [Exact all-file diff](evidence/diffs/C013_b38c5e0.diff)

[Previous saved controller snapshot](evidence/versions/C012_5ceb580_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9e2e916..9179de7 100644
--- a/approach.py
+++ b/approach.py
@@ -48,15 +48,19 @@ class GeneratedApproach:
   48     48      def _radio_points(self,s,i):
   49     49          land=self._get(s,"lander")[0]; q=(s.get(land,"x"),s.get(land,"y"))
   50     50          if i==0:
   51        -            raw=[(x,y) for y in (.35,.55,.75,.95) for x in (1.0,.8,.6,.4)]
          51 +            raw=[(x,y) for y in (.25,.45,.65,.85)
          52 +                 for x in (.35,.55,.75,.95,1.15,1.35)]
   52     53          else:
   53     54              raw=[(-1.0,-1.75),(-1.0,-1.45),(-1.3,-1.6),(-1.5,-1.4),(-1.7,-1.2)]
   54     55          rects=self._rects(s)[1:] # wall is low enough to radio over from right poses
   55        -        good=[]
          56 +        free=[]; good=[]
   56     57          for p in raw:
   57     58              if math.dist(p,q)>=3.9 or not self._free(p,self._rects(s)): continue
          59 +            free.append(p)
   58     60              if not any(self._seg_rect(p,q,r,.07) for r in rects): good.append(p)
   59        -        return good or raw
          61 +        # Try predicted-clear rays first, but retain every collision-free pose so
          62 +        # silent failures can be escaped even when the crude 2-D LOS model is wrong.
          63 +        return good+[p for p in free if p not in good]
   60     64  
   61     65      def _radio(self,i):
   62     66          pts=self.radio_choices[i]
```

</details>

<a id="C014"></a>
### C014 · match measured rover clearance and compact lander footprint

Commit `7d3acca366e5a3a5f76d1868eb6c4d203bb0f40e`; parents: b38c5e0df261a1f0126d3e71f13402fc2854f680. Recorded author date: 2026-09-11T11:45:57+02:00.

File roles (automatic): policy.

- [E0089](01_timeline.md#E0089): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_7d3acca_approach.py) · [Exact all-file diff](evidence/diffs/C014_7d3acca.diff)

[Previous saved controller snapshot](evidence/versions/C013_b38c5e0_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9179de7..66958e5 100644
--- a/approach.py
+++ b/approach.py
@@ -75,7 +75,8 @@ class GeneratedApproach:
   75     75              ans.append((s.get(o,"x"), s.get(o,"y"), s.get(o,"half_x"), s.get(o,"half_y")))
   76     76          # Lander is a physical obstacle; use a conservative footprint.
   77     77          for o in self._get(s, "lander"):
   78        -            ans.append((s.get(o,"x"), s.get(o,"y"), .32, .32))
          78 +            # Its collision body is compact (rover1 starts only .25 m north of it).
          79 +            ans.append((s.get(o,"x"), s.get(o,"y"), .04, .04))
   79     80          return ans
   80     81  
   81     82      @staticmethod
@@ -95,8 +96,8 @@ class GeneratedApproach:
   95     96                  if lo > hi: return False
   96     97          return True
   97     98  
   98        -    def _free(self, p, rects, pad=.24):
   99        -        if p[0] < -2.30 or p[0] > 2.30 or p[1] < -2.30 or p[1] > 2.30:
          99 +    def _free(self, p, rects, pad=.20):
         100 +        if p[0] < -2.27 or p[0] > 2.27 or p[1] < -2.27 or p[1] > 2.27:
  100    101              return False
  101    102          return not any(abs(p[0]-x) <= hx+pad and abs(p[1]-y) <= hy+pad
  102    103                         for x,y,hx,hy in rects)
```

</details>

<a id="C015"></a>
### C015 · add targeted lander-corner accessibility probe

Commit `b756d22a713a8ec2951ef37f9c114badf245be3e`; parents: 7d3acca366e5a3a5f76d1868eb6c4d203bb0f40e. Recorded author date: 2026-09-11T11:47:59+02:00.

File roles (automatic): diagnostic/test.

- [E0097](01_timeline.md#E0097): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C015_b756d22.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_corner.py b/probe_corner.py
new file mode 100644
index 0000000..11025eb
--- /dev/null
+++ b/probe_corner.py
@@ -0,0 +1,17 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +e=make_env();s,_=e.reset(seed=13)
           4 +def go(x,y):
           5 + global s
           6 + for _ in range(30):
           7 +  r=s.get_object_from_name('rover1'); px,py=s.get(r,'x'),s.get(r,'y')
           8 +  a=np.zeros(8,np.float32);a[4]=max(-.2,min(.2,x-px));a[5]=max(-.2,min(.2,y-py))
           9 +  old=(px,py);s,*_=e.step(a)
          10 +  r=s.get_object_from_name('rover1');new=(s.get(r,'x'),s.get(r,'y'))
          11 +  print('go',x,y,'old',old,'new',new)
          12 +  if abs(new[0]-x)<.03 and abs(new[1]-y)<.03:return
          13 +  if new==old:return
          14 +go(-1,-1.4);go(-2.25,-1.4);go(-2.25,-2.05)
          15 +a=np.zeros(8,np.float32);a[7]=-5/6;s,*_=e.step(a)
          16 +r=s.get_object_from_name('rover1');print('FINAL',s.get(r,'x'),s.get(r,'y'),s.get(r,'store_full'))
          17 +e.close()
```

</details>

<a id="C016"></a>
### C016 · avoid trapped lander-corner samples and enforce side-local pickups

Commit `62a9024e29a81652adc3ee174730655539bbd2c0`; parents: b756d22a713a8ec2951ef37f9c114badf245be3e. Recorded author date: 2026-09-11T11:48:20+02:00.

File roles (automatic): policy.

- [E0101](01_timeline.md#E0101): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C016_62a9024_approach.py) · [Exact all-file diff](evidence/diffs/C016_62a9024.diff)

[Previous saved controller snapshot](evidence/versions/C014_7d3acca_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 66958e5..4cdd5d7 100644
--- a/approach.py
+++ b/approach.py
@@ -36,13 +36,18 @@ class GeneratedApproach:
   36     36          self.sample_jobs = [set(), set()]
   37     37          for soil in (False, True):
   38     38              choices=[]
          39 +            land=self._get(state,"lander")[0]
          40 +            lq=(state.get(land,"x"),state.get(land,"y"))
   39     41              for o in self._get(state,"sample"):
   40     42                  if bool(state.get(o,"is_soil")>.5) != soil: continue
   41     43                  x,y=state.get(o,"x"),state.get(o,"y")
   42     44                  owner=0 if x>=0 else 1
   43        -                choices.append((math.dist(self.home[owner],(x,y)),owner,o.name))
          45 +                # Samples squeezed between the large lander and southwest arena
          46 +                # corner are not drive-reachable; prefer either of the other two.
          47 +                trapped = owner==1 and math.dist((x,y),lq)<.60 and y<lq[1]+.05
          48 +                choices.append((int(trapped),math.dist(self.home[owner],(x,y)),owner,o.name))
   44     49              if choices:
   45        -                _,owner,name=min(choices)
          50 +                _,_,owner,name=min(choices)
   46     51                  self.sample_jobs[owner].add(soil)
   47     52  
   48     53      def _radio_points(self,s,i):
@@ -200,7 +205,8 @@ class GeneratedApproach:
  200    205                  soil=kind; break
  201    206          if soil is None: return ("home",self.home[i])
  202    207          matching=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==soil]
  203        -        samples=[o for o in matching if s.get(o,"received_analysis")<.5]
         208 +        samples=[o for o in matching if s.get(o,"received_analysis")<.5 and
         209 +                 ((s.get(o,"x")>=0) == (i==0))]
  204    210          if samples:
  205    211              candidates=[]
  206    212              for o in samples:
```

</details>

<a id="C017"></a>
### C017 · honor selected sample and approach objectives with robust margin

Commit `c936cf5994f9ac1ac584e2baa7094b5559dec920`; parents: 62a9024e29a81652adc3ee174730655539bbd2c0. Recorded author date: 2026-09-11T11:50:04+02:00.

File roles (automatic): policy.

- [E0109](01_timeline.md#E0109): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_c936cf5_approach.py) · [Exact all-file diff](evidence/diffs/C017_c936cf5.diff)

[Previous saved controller snapshot](evidence/versions/C016_62a9024_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4cdd5d7..08aa295 100644
--- a/approach.py
+++ b/approach.py
@@ -33,7 +33,7 @@ class GeneratedApproach:
   33     33          self.last_ops=["noop","noop"]
   34     34          # Pick one concrete sample of each required kind and give it to the rover
   35     35          # already on that side of the wall.
   36        -        self.sample_jobs = [set(), set()]
          36 +        self.sample_jobs = [{}, {}]
   37     37          for soil in (False, True):
   38     38              choices=[]
   39     39              land=self._get(state,"lander")[0]
@@ -48,7 +48,7 @@ class GeneratedApproach:
   48     48                  choices.append((int(trapped),math.dist(self.home[owner],(x,y)),owner,o.name))
   49     49              if choices:
   50     50                  _,_,owner,name=min(choices)
   51        -                self.sample_jobs[owner].add(soil)
          51 +                self.sample_jobs[owner][soil]=name
   52     52  
   53     53      def _radio_points(self,s,i):
   54     54          land=self._get(s,"lander")[0]; q=(s.get(land,"x"),s.get(land,"y"))
@@ -188,7 +188,7 @@ class GeneratedApproach:
  188    188              for o,q in need:
  189    189                  # Already photographed by this rover: only needs sending.
  190    190                  if s.get(o,"have_image_rover%d"%i)>.5: continue
  191        -                if math.dist(pos,q)<=1.90 and self._los(pos,q,rects):
         191 +                if math.dist(pos,q)<=1.72 and self._los(pos,q,rects):
  192    192                      return (("image" if s.get(r,"calibrated")>.5 else "calibrate"),pos)
  193    193                  cs=self._candidates(s,q,1.9,True)
  194    194                  if cs:
@@ -199,14 +199,14 @@ class GeneratedApproach:
  199    199              return ("nav_send",self._radio(i))
  200    200          # Execute the preassigned one-stone/one-soil jobs (possibly both on one rover).
  201    201          soil=None
  202        -        for kind in sorted(self.sample_jobs[i]):
         202 +        chosen_name=None
         203 +        for kind,name in sorted(self.sample_jobs[i].items()):
  203    204              matching=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==kind]
  204    205              if not any(s.get(o,"received_analysis")>.5 for o in matching):
  205        -                soil=kind; break
         206 +                soil=kind; chosen_name=name; break
  206    207          if soil is None: return ("home",self.home[i])
  207    208          matching=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==soil]
  208        -        samples=[o for o in matching if s.get(o,"received_analysis")<.5 and
  209        -                 ((s.get(o,"x")>=0) == (i==0))]
         209 +        samples=[s.get_object_from_name(chosen_name)]
  210    210          if samples:
  211    211              candidates=[]
  212    212              for o in samples:
@@ -245,6 +245,8 @@ class GeneratedApproach:
  245    245                          goals=[target]; tolerance=.15
  246    246                      self.paths[i]=self._astar(pos,goals,rects,tolerance)
  247    247                      self.targets[i]=key; self.stalls[i]=0
         248 +                    if not self.paths[i] and task!="nav_sample" and self._free(target,rects):
         249 +                        self.paths[i]=[target]
  248    250                  while self.paths[i] and math.dist(pos,self.paths[i][0])<.05: self.paths[i].pop(0)
  249    251                  if self.paths[i]:
  250    252                      wp=self.paths[i][0]
```

</details>

<a id="C018"></a>
### C018 · learn rejected collision segments and target pickup disks

Commit `84d91db688d9348b2a984de3bdc5fb2e1dd6c523`; parents: c936cf5994f9ac1ac584e2baa7094b5559dec920. Recorded author date: 2026-09-11T11:51:52+02:00.

File roles (automatic): policy.

- [E0118](01_timeline.md#E0118): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_84d91db_approach.py) · [Exact all-file diff](evidence/diffs/C018_84d91db.diff)

[Previous saved controller snapshot](evidence/versions/C017_c936cf5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 08aa295..6532ad2 100644
--- a/approach.py
+++ b/approach.py
@@ -28,6 +28,8 @@ class GeneratedApproach:
   28     28          self.targets = [None, None]
   29     29          self.stalls = [0, 0]
   30     30          self.lastpos = list(self.home)
          31 +        self.extra_rects=[[],[]]
          32 +        self.last_motion=[None,None]
   31     33          self.radio_choices=[self._radio_points(state,i) for i in range(2)]
   32     34          self.radio_idx=[0,0]
   33     35          self.last_ops=["noop","noop"]
@@ -44,7 +46,7 @@ class GeneratedApproach:
   44     46                  owner=0 if x>=0 else 1
   45     47                  # Samples squeezed between the large lander and southwest arena
   46     48                  # corner are not drive-reachable; prefer either of the other two.
   47        -                trapped = owner==1 and math.dist((x,y),lq)<.60 and y<lq[1]+.05
          49 +                trapped = owner==1 and math.dist((x,y),lq)<.60
   48     50                  choices.append((int(trapped),math.dist(self.home[owner],(x,y)),owner,o.name))
   49     51              if choices:
   50     52                  _,_,owner,name=min(choices)
@@ -144,10 +146,15 @@ class GeneratedApproach:
  144    146                  if ng < cost.get(nk,10**9):
  145    147                      cost[nk]=ng; parent[nk]=k; heapq.heappush(openq,(ng+h(nk),ng,nk))
  146    148          if end is None: return []
         149 +        endpos=pos(end)
  147    150          ks=[]
  148    151          while end != (0,0): ks.append(end); end=parent[end]
  149    152          ks.reverse()
  150        -        return [pos(k) for k in ks]
         153 +        path=[pos(k) for k in ks]
         154 +        final=min(goals,key=lambda q:math.dist(endpos,q))
         155 +        if self._free(final,rects) and math.dist(endpos,final)>.025:
         156 +            path.append(final)
         157 +        return path
  151    158  
  152    159      def _candidates(self, s, q, radius, require_los=True):
  153    160          rects=self._rects(s); out=[]
@@ -224,9 +231,14 @@ class GeneratedApproach:
  224    231  
  225    232      def get_action(self, state):
  226    233          a=np.zeros(8,dtype=np.float32)
  227        -        rects=self._rects(state)
         234 +        base_rects=self._rects(state)
  228    235          for i in range(2):
  229    236              r=state.get_object_from_name(self.names[i]); pos=(state.get(r,"x"),state.get(r,"y"))
         237 +            if self.last_motion[i] is not None and math.dist(pos,self.lastpos[i])<.02:
         238 +                bx,by=self.last_motion[i]
         239 +                self.extra_rects[i].append((bx,by,.07,.07))
         240 +                self.paths[i]=[]; self.targets[i]=None
         241 +            rects=base_rects+self.extra_rects[i]
  230    242              if self.last_ops[i]=="send":
  231    243                  pending_img=any(state.get(o,"have_image_rover%d"%i)>.5 and state.get(o,"received_image")<.5
  232    244                                  for o in self._get(state,"objective"))
@@ -240,7 +252,7 @@ class GeneratedApproach:
  240    252                  key=(task,round(target[0],2),round(target[1],2))
  241    253                  if self.targets[i]!=key or not self.paths[i] or self.stalls[i]>=2:
  242    254                      if task=="nav_sample":
  243        -                        goals=[target]; tolerance=.24
         255 +                        goals=self._candidates(state,target,.24,False)+[target]; tolerance=.09
  244    256                      else:
  245    257                          goals=[target]; tolerance=.15
  246    258                      self.paths[i]=self._astar(pos,goals,rects,tolerance)
@@ -256,4 +268,5 @@ class GeneratedApproach:
  256    268              self.stalls[i]=0 if moved or (abs(a[4*i])+abs(a[4*i+1])<.01) else self.stalls[i]+1
  257    269              self.lastpos[i]=pos
  258    270              self.last_ops[i]=op
         271 +            self.last_motion[i]=(pos[0]+float(a[4*i]),pos[1]+float(a[4*i+1])) if abs(a[4*i])+abs(a[4*i+1])>.01 else None
  259    272          return a
```

</details>

<a id="C019"></a>
### C019 · avoid edge samples and distinguish tiny successful moves from collisions

Commit `846bb142ab5b27c304d4f4a725177dbb3fb308d5`; parents: 84d91db688d9348b2a984de3bdc5fb2e1dd6c523. Recorded author date: 2026-09-11T11:53:24+02:00.

File roles (automatic): policy.

- [E0125](01_timeline.md#E0125): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_846bb14_approach.py) · [Exact all-file diff](evidence/diffs/C019_846bb14.diff)

[Previous saved controller snapshot](evidence/versions/C018_84d91db_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6532ad2..b3d2885 100644
--- a/approach.py
+++ b/approach.py
@@ -47,7 +47,8 @@ class GeneratedApproach:
   47     47                  # Samples squeezed between the large lander and southwest arena
   48     48                  # corner are not drive-reachable; prefer either of the other two.
   49     49                  trapped = owner==1 and math.dist((x,y),lq)<.60
   50        -                choices.append((int(trapped),math.dist(self.home[owner],(x,y)),owner,o.name))
          50 +                edge = abs(x)>2.20 or abs(y)>2.20
          51 +                choices.append((int(trapped or edge),math.dist(self.home[owner],(x,y)),owner,o.name))
   51     52              if choices:
   52     53                  _,_,owner,name=min(choices)
   53     54                  self.sample_jobs[owner][soil]=name
@@ -159,7 +160,8 @@ class GeneratedApproach:
  159    160      def _candidates(self, s, q, radius, require_los=True):
  160    161          rects=self._rects(s); out=[]
  161    162          # Fine angular rings give plenty of robust visibility choices.
  162        -        for rad in (min(radius*.72,1.55), min(radius*.88,1.82), radius*.55):
         163 +        for rad in (min(radius*.72,1.55), min(radius*.88,1.82),
         164 +                    min(radius*.98,1.88), radius*.55):
  163    165              for j in range(32):
  164    166                  a=2*math.pi*j/32
  165    167                  p=(q[0]+rad*math.cos(a),q[1]+rad*math.sin(a))
@@ -224,7 +226,7 @@ class GeneratedApproach:
  224    226                  q=(s.get(o,"x"),s.get(o,"y"))
  225    227                  candidates.append((math.dist(pos,q),q))
  226    228              q=min(candidates)[1]
  227        -            if math.dist(pos,q)<=.24: return ("sample",pos)
         229 +            if math.dist(pos,q)<=.249: return ("sample",pos)
  228    230              return ("nav_sample",q)
  229    231          # No pending work of our nominal class: help with anything globally missing.
  230    232          return ("home",self.home[i])
@@ -234,7 +236,7 @@ class GeneratedApproach:
  234    236          base_rects=self._rects(state)
  235    237          for i in range(2):
  236    238              r=state.get_object_from_name(self.names[i]); pos=(state.get(r,"x"),state.get(r,"y"))
  237        -            if self.last_motion[i] is not None and math.dist(pos,self.lastpos[i])<.02:
         239 +            if self.last_motion[i] is not None and math.dist(pos,self.lastpos[i])<.0005:
  238    240                  bx,by=self.last_motion[i]
  239    241                  self.extra_rects[i].append((bx,by,.07,.07))
  240    242                  self.paths[i]=[]; self.targets[i]=None
```

</details>

<a id="C020"></a>
### C020 · keep image viewpoints inside conservative visibility radius

Commit `50ee2849db52d753ff7da60fdf38ad4e353c4350`; parents: 846bb142ab5b27c304d4f4a725177dbb3fb308d5. Recorded author date: 2026-09-11T11:55:22+02:00.

File roles (automatic): policy.

- [E0129](01_timeline.md#E0129): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_50ee284_approach.py) · [Exact all-file diff](evidence/diffs/C020_50ee284.diff)

[Previous saved controller snapshot](evidence/versions/C019_846bb14_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b3d2885..8b86c74 100644
--- a/approach.py
+++ b/approach.py
@@ -160,8 +160,9 @@ class GeneratedApproach:
  160    160      def _candidates(self, s, q, radius, require_los=True):
  161    161          rects=self._rects(s); out=[]
  162    162          # Fine angular rings give plenty of robust visibility choices.
  163        -        for rad in (min(radius*.72,1.55), min(radius*.88,1.82),
  164        -                    min(radius*.98,1.88), radius*.55):
         163 +        rings=[min(radius*.72,1.55), min(radius*.88,1.68), radius*.55]
         164 +        if radius<.5: rings.insert(0,radius*.98)
         165 +        for rad in rings:
  165    166              for j in range(32):
  166    167                  a=2*math.pi*j/32
  167    168                  p=(q[0]+rad*math.cos(a),q[1]+rad*math.sin(a))
```

</details>

<a id="C021"></a>
### C021 · nudge and sample at tight divider-side pickup poses

Commit `cacac5e029d97b14d226f26cd599a44e79bae18b`; parents: 50ee2849db52d753ff7da60fdf38ad4e353c4350. Recorded author date: 2026-09-11T11:56:19+02:00.

File roles (automatic): policy.

- [E0135](01_timeline.md#E0135): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C021_cacac5e_approach.py) · [Exact all-file diff](evidence/diffs/C021_cacac5e.diff)

[Previous saved controller snapshot](evidence/versions/C020_50ee284_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8b86c74..538aa64 100644
--- a/approach.py
+++ b/approach.py
@@ -251,6 +251,13 @@ class GeneratedApproach:
  251    251                      self.radio_idx[i]+=1; self.paths[i]=[]; self.targets[i]=None
  252    252              task,target=self._choose_task(state,i,pos)
  253    253              op=task if task in self.OPS else "noop"
         254 +            if task=="nav_sample" and math.dist(pos,target)<.34:
         255 +                # Nudge into the exact pickup disk while attempting the operator;
         256 +                # this is especially important for samples beside the divider.
         257 +                op="sample"
         258 +                a[4*i]=max(-.04,min(.04,target[0]-pos[0]))
         259 +                a[4*i+1]=max(-.04,min(.04,target[1]-pos[1]))
         260 +                task="near_sample"
  254    261              if task.startswith("nav") or task=="home":
  255    262                  key=(task,round(target[0],2),round(target[1],2))
  256    263                  if self.targets[i]!=key or not self.paths[i] or self.stalls[i]>=2:
```

</details>

<a id="C022"></a>
### C022 · sample from safely inside acquisition cutoff

Commit `b3062a58ec872fbdf610e592de076b1183c31b47`; parents: cacac5e029d97b14d226f26cd599a44e79bae18b. Recorded author date: 2026-09-11T11:59:43+02:00.

File roles (automatic): policy.

- [E0143](01_timeline.md#E0143): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C022_b3062a5_approach.py) · [Exact all-file diff](evidence/diffs/C022_b3062a5.diff)

[Previous saved controller snapshot](evidence/versions/C021_cacac5e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 538aa64..3b30b1b 100644
--- a/approach.py
+++ b/approach.py
@@ -227,7 +227,9 @@ class GeneratedApproach:
  227    227                  q=(s.get(o,"x"),s.get(o,"y"))
  228    228                  candidates.append((math.dist(pos,q),q))
  229    229              q=min(candidates)[1]
  230        -            if math.dist(pos,q)<=.249: return ("sample",pos)
         230 +            # Aim well inside the inclusive .25 m server cutoff; stopping near its
         231 +            # floating-point boundary proved brittle on diagonals.
         232 +            if math.dist(pos,q)<=.18: return ("sample",pos)
  231    233              return ("nav_sample",q)
  232    234          # No pending work of our nominal class: help with anything globally missing.
  233    235          return ("home",self.home[i])
```

</details>

<a id="C023"></a>
### C023 · prefer unpinched samples and bound learned collision map

Commit `6285fa693df3dd5b9eaa2ba2a598c8ac6c4f13b3`; parents: b3062a58ec872fbdf610e592de076b1183c31b47. Recorded author date: 2026-09-11T12:02:24+02:00.

File roles (automatic): policy.

- [E0149](01_timeline.md#E0149): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C023_6285fa6_approach.py) · [Exact all-file diff](evidence/diffs/C023_6285fa6.diff)

[Previous saved controller snapshot](evidence/versions/C022_b3062a5_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3b30b1b..6d48354 100644
--- a/approach.py
+++ b/approach.py
@@ -48,7 +48,9 @@ class GeneratedApproach:
   48     48                  # corner are not drive-reachable; prefer either of the other two.
   49     49                  trapped = owner==1 and math.dist((x,y),lq)<.60
   50     50                  edge = abs(x)>2.20 or abs(y)>2.20
   51        -                choices.append((int(trapped or edge),math.dist(self.home[owner],(x,y)),owner,o.name))
          51 +                pillars=self._rects(state)[5:]  # skip wall, four mounds
          52 +                pinched=any(math.dist((x,y),(r[0],r[1]))<.34 for r in pillars)
          53 +                choices.append((int(trapped or edge or pinched),math.dist(self.home[owner],(x,y)),owner,o.name))
   52     54              if choices:
   53     55                  _,_,owner,name=min(choices)
   54     56                  self.sample_jobs[owner][soil]=name
@@ -241,7 +243,9 @@ class GeneratedApproach:
  241    243              r=state.get_object_from_name(self.names[i]); pos=(state.get(r,"x"),state.get(r,"y"))
  242    244              if self.last_motion[i] is not None and math.dist(pos,self.lastpos[i])<.0005:
  243    245                  bx,by=self.last_motion[i]
  244        -                self.extra_rects[i].append((bx,by,.07,.07))
         246 +                if not any(math.dist((bx,by),(r[0],r[1]))<.08 for r in self.extra_rects[i]):
         247 +                    self.extra_rects[i].append((bx,by,.07,.07))
         248 +                    self.extra_rects[i]=self.extra_rects[i][-12:]
  245    249                  self.paths[i]=[]; self.targets[i]=None
  246    250              rects=base_rects+self.extra_rects[i]
  247    251              if self.last_ops[i]=="send":
```

</details>

<a id="C024"></a>
### C024 · keep learned collision cells local enough to route around

Commit `dd4d9297c3235ab413a64ce09838c17a3a171b04`; parents: 6285fa693df3dd5b9eaa2ba2a598c8ac6c4f13b3. Recorded author date: 2026-09-11T12:03:10+02:00.

File roles (automatic): policy.

- [E0155](01_timeline.md#E0155): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C024_dd4d929_approach.py) · [Exact all-file diff](evidence/diffs/C024_dd4d929.diff)

[Previous saved controller snapshot](evidence/versions/C023_6285fa6_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6d48354..ec2e470 100644
--- a/approach.py
+++ b/approach.py
@@ -244,7 +244,9 @@ class GeneratedApproach:
  244    244              if self.last_motion[i] is not None and math.dist(pos,self.lastpos[i])<.0005:
  245    245                  bx,by=self.last_motion[i]
  246    246                  if not any(math.dist((bx,by),(r[0],r[1]))<.08 for r in self.extra_rects[i]):
  247        -                    self.extra_rects[i].append((bx,by,.07,.07))
         247 +                    # _free adds the rover-radius pad, so a negative raw half-size
         248 +                    # represents a small learned blocked cell rather than a pillar.
         249 +                    self.extra_rects[i].append((bx,by,-.14,-.14))
  248    250                      self.extra_rects[i]=self.extra_rects[i][-12:]
  249    251                  self.paths[i]=[]; self.targets[i]=None
  250    252              rects=base_rects+self.extra_rects[i]
```

</details>

<a id="C025"></a>
### C025 · sidestep after rejected navigation motion

Commit `b648b659c5150d3b26b5c6824518fd74004f61f0`; parents: dd4d9297c3235ab413a64ce09838c17a3a171b04. Recorded author date: 2026-09-11T12:04:38+02:00.

File roles (automatic): policy.

- [E0159](01_timeline.md#E0159): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C025_b648b65_approach.py) · [Exact all-file diff](evidence/diffs/C025_b648b65.diff)

[Previous saved controller snapshot](evidence/versions/C024_dd4d929_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ec2e470..6fd51cb 100644
--- a/approach.py
+++ b/approach.py
@@ -281,6 +281,12 @@ class GeneratedApproach:
  281    281                  if self.paths[i]:
  282    282                      wp=self.paths[i][0]
  283    283                      a[4*i]=max(-.2,min(.2,wp[0]-pos[0])); a[4*i+1]=max(-.2,min(.2,wp[1]-pos[1]))
         284 +                if self.stalls[i]>=1:
         285 +                    # One-step lateral escape from an unmodelled/underestimated
         286 +                    # collision boundary, then the route is rebuilt next state.
         287 +                    outward = (i==0 and pos[0]<1.5) or (i==1 and pos[0]>-1.5)
         288 +                    a[4*i]=.2 if (i==0)==outward else -.2
         289 +                    a[4*i+1]=0.0
  284    290              a[4*i+3]=self.OPS[op]
  285    291              moved=math.dist(pos,self.lastpos[i])>.03
  286    292              self.stalls[i]=0 if moved or (abs(a[4*i])+abs(a[4*i+1])<.01) else self.stalls[i]+1
```

</details>

<a id="C026"></a>
### C026 · increase early rollout diagnostic resolution

Commit `27f3d97ed69adeee5ef579264ee9eaf469215af5`; parents: b648b659c5150d3b26b5c6824518fd74004f61f0. Recorded author date: 2026-09-11T12:06:18+02:00.

File roles (automatic): diagnostic/test.

- [E0165](01_timeline.md#E0165): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C026_27f3d97.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/debug_rollout.py b/debug_rollout.py
index 0adb950..de314cd 100644
--- a/debug_rollout.py
+++ b/debug_rollout.py
@@ -4,7 +4,7 @@ from approach import GeneratedApproach
    4      4  env=make_env(); s,info=env.reset(seed=int(sys.argv[1]) if len(sys.argv)>1 else 0)
    5      5  ap=GeneratedApproach(env.action_space,env.observation_space,env.make_primitives()); ap.reset(s,info)
    6      6  for step in range(160):
    7        -    if step%10==0:
           7 +    if step < 25 or step%10==0:
    8      8          vals=[]
    9      9          for i,n in enumerate(ap.names):
   10     10              r=s.get_object_from_name(n); p=(s.get(r,"x"),s.get(r,"y"))
```

</details>

<a id="C027"></a>
### C027 · preserve stall signal through replanning for escape move

Commit `2d32ae7ed810357c05b0522ca7927f820d3e66e1`; parents: 27f3d97ed69adeee5ef579264ee9eaf469215af5. Recorded author date: 2026-09-11T12:06:32+02:00.

File roles (automatic): policy.

- [E0169](01_timeline.md#E0169): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C027_2d32ae7_approach.py) · [Exact all-file diff](evidence/diffs/C027_2d32ae7.diff)

[Previous saved controller snapshot](evidence/versions/C025_b648b65_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6fd51cb..525214d 100644
--- a/approach.py
+++ b/approach.py
@@ -274,7 +274,7 @@ class GeneratedApproach:
  274    274                      else:
  275    275                          goals=[target]; tolerance=.15
  276    276                      self.paths[i]=self._astar(pos,goals,rects,tolerance)
  277        -                    self.targets[i]=key; self.stalls[i]=0
         277 +                    self.targets[i]=key
  278    278                      if not self.paths[i] and task!="nav_sample" and self._free(target,rects):
  279    279                          self.paths[i]=[target]
  280    280                  while self.paths[i] and math.dist(pos,self.paths[i][0])<.05: self.paths[i].pop(0)
```

</details>

<a id="C028"></a>
### C028 · make collision escape continue around obstacle flank

Commit `fa6490b6f6605cc2f0f63fbbf70fcf902eb24cba`; parents: 2d32ae7ed810357c05b0522ca7927f820d3e66e1. Recorded author date: 2026-09-11T12:07:32+02:00.

File roles (automatic): policy.

- [E0175](01_timeline.md#E0175): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C028_fa6490b_approach.py) · [Exact all-file diff](evidence/diffs/C028_fa6490b.diff)

[Previous saved controller snapshot](evidence/versions/C027_2d32ae7_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 525214d..56e95c6 100644
--- a/approach.py
+++ b/approach.py
@@ -284,9 +284,11 @@ class GeneratedApproach:
  284    284                  if self.stalls[i]>=1:
  285    285                      # One-step lateral escape from an unmodelled/underestimated
  286    286                      # collision boundary, then the route is rebuilt next state.
  287        -                    outward = (i==0 and pos[0]<1.5) or (i==1 and pos[0]>-1.5)
  288        -                    a[4*i]=.2 if (i==0)==outward else -.2
  289        -                    a[4*i+1]=0.0
         287 +                    direction=1.0 if i==0 else -1.0
         288 +                    if (i==0 and pos[0]<2.0) or (i==1 and pos[0]>-2.0):
         289 +                        a[4*i]=.2*direction; a[4*i+1]=0.0
         290 +                    else:
         291 +                        a[4*i]=0.0; a[4*i+1]=.2
  290    292              a[4*i+3]=self.OPS[op]
  291    293              moved=math.dist(pos,self.lastpos[i])>.03
  292    294              self.stalls[i]=0 if moved or (abs(a[4*i])+abs(a[4*i+1])<.01) else self.stalls[i]+1
```

</details>

<a id="C029"></a>
### C029 · use camera-ray clearance around pillar silhouettes

Commit `6af5f874cd2cf1bd02e1101e6b46732f665f7660`; parents: fa6490b6f6605cc2f0f63fbbf70fcf902eb24cba. Recorded author date: 2026-09-11T12:08:10+02:00.

File roles (automatic): policy.

- [E0183](01_timeline.md#E0183): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C029_6af5f87_approach.py) · [Exact all-file diff](evidence/diffs/C029_6af5f87.diff)

[Previous saved controller snapshot](evidence/versions/C028_fa6490b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 56e95c6..bf0301b 100644
--- a/approach.py
+++ b/approach.py
@@ -118,7 +118,7 @@ class GeneratedApproach:
  118    118              x,y,hx,hy = rect
  119    119              if abs(q[0]-x) <= hx+1e-5 and abs(q[1]-y) <= hy+1e-5:
  120    120                  continue
  121        -            if self._seg_rect(p, q, rect, .01): return False
         121 +            if self._seg_rect(p, q, rect, .10): return False
  122    122          return True
  123    123  
  124    124      def _astar(self, start, goals, rects, tolerance=.18):
```

</details>

<a id="C030"></a>
### C030 · detect pinched samples from typed pillar dimensions

Commit `d3aad59cbfbc586f6827a8b2b48975df4af8a5c5`; parents: 6af5f874cd2cf1bd02e1101e6b46732f665f7660. Recorded author date: 2026-09-11T12:08:50+02:00.

File roles (automatic): policy.

- [E0191](01_timeline.md#E0191): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C030_d3aad59_approach.py) · [Exact all-file diff](evidence/diffs/C030_d3aad59.diff)

[Previous saved controller snapshot](evidence/versions/C029_6af5f87_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index bf0301b..7fc2b5e 100644
--- a/approach.py
+++ b/approach.py
@@ -48,8 +48,10 @@ class GeneratedApproach:
   48     48                  # corner are not drive-reachable; prefer either of the other two.
   49     49                  trapped = owner==1 and math.dist((x,y),lq)<.60
   50     50                  edge = abs(x)>2.20 or abs(y)>2.20
   51        -                pillars=self._rects(state)[5:]  # skip wall, four mounds
   52        -                pinched=any(math.dist((x,y),(r[0],r[1]))<.34 for r in pillars)
          51 +                pillars=[p for p in self._get(state,"obstacle")
          52 +                         if state.get(p,"half_x")<.10]
          53 +                pinched=any(math.dist((x,y),(state.get(p,"x"),state.get(p,"y")))<.34
          54 +                            for p in pillars)
   53     55                  choices.append((int(trapped or edge or pinched),math.dist(self.home[owner],(x,y)),owner,o.name))
   54     56              if choices:
   55     57                  _,_,owner,name=min(choices)
```

</details>

<a id="C031"></a>
### C031 · rank lander-trapped samples below merely edge-adjacent ones

Commit `b6baaea5775476aa010ac0f05b9ed98e4aaca63c`; parents: d3aad59cbfbc586f6827a8b2b48975df4af8a5c5. Recorded author date: 2026-09-11T12:11:31+02:00.

File roles (automatic): policy.

- [E0200](01_timeline.md#E0200): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C031_b6baaea_approach.py) · [Exact all-file diff](evidence/diffs/C031_b6baaea.diff)

[Previous saved controller snapshot](evidence/versions/C030_d3aad59_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7fc2b5e..ea59546 100644
--- a/approach.py
+++ b/approach.py
@@ -52,7 +52,8 @@ class GeneratedApproach:
   52     52                           if state.get(p,"half_x")<.10]
   53     53                  pinched=any(math.dist((x,y),(state.get(p,"x"),state.get(p,"y")))<.34
   54     54                              for p in pillars)
   55        -                choices.append((int(trapped or edge or pinched),math.dist(self.home[owner],(x,y)),owner,o.name))
          55 +                risk=2 if trapped else (1 if edge or pinched else 0)
          56 +                choices.append((risk,math.dist(self.home[owner],(x,y)),owner,o.name))
   56     57              if choices:
   57     58                  _,_,owner,name=min(choices)
   58     59                  self.sample_jobs[owner][soil]=name
```

</details>

<a id="C032"></a>
### C032 · escape north around lander east-side collision boundary

Commit `70cf2a1c81dac8b8191277b61dae7702dda2ef95`; parents: b6baaea5775476aa010ac0f05b9ed98e4aaca63c. Recorded author date: 2026-09-11T12:12:20+02:00.

File roles (automatic): policy.

- [E0208](01_timeline.md#E0208): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C032_70cf2a1_approach.py) · [Exact all-file diff](evidence/diffs/C032_70cf2a1.diff)

[Previous saved controller snapshot](evidence/versions/C031_b6baaea_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ea59546..cbc94f9 100644
--- a/approach.py
+++ b/approach.py
@@ -288,7 +288,10 @@ class GeneratedApproach:
  288    288                      # One-step lateral escape from an unmodelled/underestimated
  289    289                      # collision boundary, then the route is rebuilt next state.
  290    290                      direction=1.0 if i==0 else -1.0
  291        -                    if (i==0 and pos[0]<2.0) or (i==1 and pos[0]>-2.0):
         291 +                    if i==1 and pos[1]<-1.4 and pos[0]>-1.5:
         292 +                        # Move north around the lander's long east side.
         293 +                        a[4*i]=0.0; a[4*i+1]=.2
         294 +                    elif (i==0 and pos[0]<2.0) or (i==1 and pos[0]>-2.0):
  292    295                          a[4*i]=.2*direction; a[4*i+1]=0.0
  293    296                      else:
  294    297                          a[4*i]=0.0; a[4*i+1]=.2
```

</details>

