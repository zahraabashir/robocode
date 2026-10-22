# Rovers · gpt-5.6-sol · replicate 424: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `39b704b` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `749e49b` | Add geometry probe for planner design | probe_planner_design.py | No matched commit command/output |
| [C003](#C003) · `43ce01c` | Fix probe to use environment observation space | probe_planner_design.py | No matched commit command/output |
| [C004](#C004) · `bb12723` | Add black-box arena geometry probe | probe_geometry.py | No matched commit command/output |
| [C005](#C005) · `fddd393` | add focused black-box operator probe | probe_ops.py | No matched commit command/output |
| [C006](#C006) · `36258b2` | Fix object type feature lookup in geometry probe | probe_geometry.py | No matched commit command/output |
| [C007](#C007) · `56169bb` | Add rover collision and motion probe | probe_motion_design.py | No matched commit command/output |
| [C008](#C008) · `3c52b1b` | extend operator probe with stateful sample and image scenario | probe_ops.py | No matched commit command/output |
| [C009](#C009) · `ce9d483` | Add targeted wall and visibility semantics probes | probe_semantics.py | No matched commit command/output |
| [C010](#C010) · `c8b9c70` | Probe lower wall crossing clearance | probe_motion_design.py | No matched commit command/output |
| [C011](#C011) · `dbe015e` | probe home tolerance and simultaneous rover collision handling | probe_ops.py | No matched commit command/output |
| [C012](#C012) · `0f846f8` | Add initial geometry-based rover policy and test harness | approach.py, inspect_env.py, test_approach.py | [E0016](01_timeline.md#E0016) |
| [C013](#C013) · `a030225` | Increase collision clearance and radio opportunistically | approach.py, probe_ops.py | [E0027](01_timeline.md#E0027) |
| [C014](#C014) · `0ba4818` | Probe sample and radio visibility from right arena | probe_ops_design.py | No matched commit command/output |
| [C015](#C015) · `c9a3e23` | Probe lower-gap radio point | probe_ops_design.py | No matched commit command/output |
| [C016](#C016) · `fd428f8` | Probe image visibility and calibration semantics | probe_image_design.py | No matched commit command/output |
| [C017](#C017) · `738181b` | Respect central wall and split imaging across rovers | approach.py, trace_run.py | [E0035](01_timeline.md#E0035) |
| [C018](#C018) · `71d3423` | Allocate sample types to reachable arena sides | approach.py | [E0039](01_timeline.md#E0039) |
| [C019](#C019) · `2af3414` | Enable left rover to image left-side objectives | approach.py | [E0043](01_timeline.md#E0043) |
| [C020](#C020) · `03b6e5b` | Add measured rover clearance around obstacles | approach.py | [E0049](01_timeline.md#E0049) |
| [C021](#C021) · `6a2200f` | Follow planned segments without componentwise deviation | approach.py | [E0053](01_timeline.md#E0053) |
| [C022](#C022) · `d0e92ec` | Clamp sample stances inside rover arena boundary | approach.py, trace_run.py | [E0060](01_timeline.md#E0060) |
| [C023](#C023) · `07d9f61` | Use measured clearance to preserve narrow navigable gaps | approach.py | [E0068](01_timeline.md#E0068) |
| [C024](#C024) · `b89302c` | Refine planning grid for tight pillar passages | approach.py | [E0078](01_timeline.md#E0078) |
| [C025](#C025) · `2f8f2a2` | Keep planned paths inside physical boundary with safe clearance | approach.py | [E0084](01_timeline.md#E0084) |
| [C026](#C026) · `bc97ce1` | Retry narrow routes at measured clearance only when needed | approach.py | [E0091](01_timeline.md#E0091) |
| [C027](#C027) · `2493a4e` | Add robust camera standoff rings and safer primary routes | approach.py | [E0099](01_timeline.md#E0099) |
| [C028](#C028) · `a914a91` | Support both required sample types on the same rover side | approach.py | [E0105](01_timeline.md#E0105) |
| [C029](#C029) · `b98dc7b` | Choose reachable sample stances near boundaries and lander | approach.py | [E0109](01_timeline.md#E0109) |
| [C030](#C030) · `46c4b3a` | Route around lander and avoid samples trapped beside it | approach.py | [E0115](01_timeline.md#E0115) |
| [C031](#C031) · `89fd168` | Exclude lander-overlapping samples from assignment | approach.py | [E0119](01_timeline.md#E0119) |
| [C032](#C032) · `9ca15aa` | Model full lander footprint and inset corner stances | approach.py | [E0129](01_timeline.md#E0129) |
| [C033](#C033) · `9904610` | Avoid unreachable samples in rounded arena corners | approach.py | [E0139](01_timeline.md#E0139) |
| [C034](#C034) · `a732c2a` | Penalize sample assignments obstructed by the lander | approach.py | [E0145](01_timeline.md#E0145) |
| [C035](#C035) · `85d529c` | Add bounded adversarial seed search harness | search_failures.py | [E0157](01_timeline.md#E0157) |
| [C036](#C036) · `83e4d78` | Use conservative sampling distance away from forced edge stances | approach.py | [E0172](01_timeline.md#E0172) |
| [C037](#C037) · `4a7e3f9` | Increase modeled vertical lander collision clearance | approach.py | [E0184](01_timeline.md#E0184) |
| [C038](#C038) · `af51a50` | Recover when overlapping samples are analyzed out of queue order | approach.py | [E0208](01_timeline.md#E0208) |
| [C039](#C039) · `1648752` | Choose sample stances that disambiguate overlapping samples | approach.py | [E0218](01_timeline.md#E0218) |
| [C040](#C040) · `21f9614` | Add variable-object-count validation harness | test_counts.py | [E0236](01_timeline.md#E0236) |
| [C041](#C041) · `4e995ed` | Optimize diagonal routes and sample on arrival | approach.py | [E0254](01_timeline.md#E0254) |
| [C042](#C042) · `0d4421d` | Restore shorter geometric paths after rollout regression | approach.py | [E0258](01_timeline.md#E0258) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `39b704bd4c673badf283a944dbdf9834714c2ad6`; parents: none (initial snapshot). Recorded author date: 2026-09-11T11:44:13+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_39b704b.diff)

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
index 0000000..3c66053
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1,98 @@
           1 +{
           2 +  "host": "127.0.0.1",
           3 +  "port": 36669,
           4 +  "token": "24492d07fb3fd2b0bb56bfb4bf497d7c",
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
### C002 · Add geometry probe for planner design

Commit `749e49bf2fdf785b57ab36eb024c5299cc4d70de`; parents: 39b704bd4c673badf283a944dbdf9834714c2ad6. Recorded author date: 2026-09-11T11:44:57+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C002_749e49b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_planner_design.py b/probe_planner_design.py
new file mode 100644
index 0000000..1d6895c
--- /dev/null
+++ b/probe_planner_design.py
@@ -0,0 +1,18 @@
           1 +from env_client import make_env
           2 +
           3 +
           4 +def objects(obs, typ):
           5 +    t = next(t for t in obs.space.types if t.name == typ)
           6 +    out = []
           7 +    for o in obs.get_objects(t):
           8 +        out.append((o.name, {f: float(obs.get(o, f)) for f in obs.space.type_features[t]}))
           9 +    return out
          10 +
          11 +
          12 +for seed in range(5):
          13 +    env = make_env()
          14 +    obs, info = env.reset(seed=seed)
          15 +    print("SEED", seed, "max", env.max_steps, "info", info)
          16 +    for typ in ("rover", "lander", "objective", "sample", "obstacle"):
          17 +        print(typ, objects(obs, typ))
          18 +    env.close()
```

</details>

<a id="C003"></a>
### C003 · Fix probe to use environment observation space

Commit `43ce01c901d24823e5a13d954a6027a430250be8`; parents: 749e49bf2fdf785b57ab36eb024c5299cc4d70de. Recorded author date: 2026-09-11T11:45:04+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C003_43ce01c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_planner_design.py b/probe_planner_design.py
index 1d6895c..d034cab 100644
--- a/probe_planner_design.py
+++ b/probe_planner_design.py
@@ -1,11 +1,11 @@
    1      1  from env_client import make_env
    2      2  
    3      3  
    4        -def objects(obs, typ):
    5        -    t = next(t for t in obs.space.types if t.name == typ)
           4 +def objects(obs, space, typ):
           5 +    t = next(t for t in space.types if t.name == typ)
    6      6      out = []
    7      7      for o in obs.get_objects(t):
    8        -        out.append((o.name, {f: float(obs.get(o, f)) for f in obs.space.type_features[t]}))
           8 +        out.append((o.name, {f: float(obs.get(o, f)) for f in space.type_features[t]}))
    9      9      return out
   10     10  
   11     11  
@@ -14,5 +14,5 @@ for seed in range(5):
   14     14      obs, info = env.reset(seed=seed)
   15     15      print("SEED", seed, "max", env.max_steps, "info", info)
   16     16      for typ in ("rover", "lander", "objective", "sample", "obstacle"):
   17        -        print(typ, objects(obs, typ))
          17 +        print(typ, objects(obs, env.observation_space, typ))
   18     18      env.close()
```

</details>

<a id="C004"></a>
### C004 · Add black-box arena geometry probe

Commit `bb12723a0162eb68971644c3d83d32db722f6e0a`; parents: 43ce01c901d24823e5a13d954a6027a430250be8. Recorded author date: 2026-09-11T11:45:07+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C004_bb12723.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_geometry.py b/probe_geometry.py
new file mode 100644
index 0000000..e0421d0
--- /dev/null
+++ b/probe_geometry.py
@@ -0,0 +1,47 @@
           1 +"""Small black-box probes for rover state geometry and action semantics."""
           2 +from env_client import make_env
           3 +import numpy as np
           4 +
           5 +
           6 +def snapshot(state, env):
           7 +    out = {}
           8 +    for typ in env.observation_space.types:
           9 +        vals = []
          10 +        for obj in state.get_objects(typ):
          11 +            fs = env.observation_space.type_features[typ.name]
          12 +            vals.append((obj.name, {f: float(state.get(obj, f)) for f in fs}))
          13 +        out[typ.name] = vals
          14 +    return out
          15 +
          16 +
          17 +def main():
          18 +    for seed in range(8):
          19 +        env = make_env()
          20 +        s, info = env.reset(seed=seed)
          21 +        d = snapshot(s, env)
          22 +        print("SEED", seed, "max", env.max_steps)
          23 +        for typ in ("rover", "lander", "objective", "sample", "obstacle"):
          24 +            print(typ, d[typ])
          25 +        env.close()
          26 +
          27 +    # Raw action scaling and heading behavior from a fresh seed.
          28 +    env = make_env()
          29 +    s, _ = env.reset(seed=0)
          30 +    rt = env.observation_space.get_type("rover")
          31 +    rs = list(s.get_objects(rt))
          32 +    print("MOTION INITIAL", [(o.name, float(s.get(o,"x")), float(s.get(o,"y")), float(s.get(o,"theta"))) for o in rs])
          33 +    tests = [
          34 +        np.array([1,0,0,0, 0,0,0,0], np.float32),
          35 +        np.array([0,1,0,0, 0,0,0,0], np.float32),
          36 +        np.array([0,0,1,0, 0,0,0,0], np.float32),
          37 +        np.array([1,1,1,0, 0,0,0,0], np.float32),
          38 +        np.array([-1,-1,-1,0, 0,0,0,0], np.float32),
          39 +    ]
          40 +    for a in tests:
          41 +        s, r, term, trunc, info = env.step(a)
          42 +        print("ACT", a.tolist(), [(o.name, float(s.get(o,"x")), float(s.get(o,"y")), float(s.get(o,"theta"))) for o in rs], r, term, trunc)
          43 +    env.close()
          44 +
          45 +
          46 +if __name__ == "__main__":
          47 +    main()
```

</details>

<a id="C005"></a>
### C005 · add focused black-box operator probe

Commit `fddd393297b4388c0bb002950eb148fc0a37f7f4`; parents: bb12723a0162eb68971644c3d83d32db722f6e0a. Recorded author date: 2026-09-11T11:45:20+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C005_fddd393.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_ops.py b/probe_ops.py
new file mode 100644
index 0000000..a988884
--- /dev/null
+++ b/probe_ops.py
@@ -0,0 +1,98 @@
           1 +"""Small black-box probes for the Rovers environment (never imported by approach.py)."""
           2 +
           3 +import argparse
           4 +import math
           5 +
           6 +import numpy as np
           7 +
           8 +from env_client import make_env
           9 +
          10 +
          11 +CENTERS = [-5 / 6, -1 / 2, -1 / 6, 1 / 6, 1 / 2, 5 / 6]
          12 +
          13 +
          14 +def objects(state, env, type_name):
          15 +    return state.get_objects(env.observation_space.get_type(type_name))
          16 +
          17 +
          18 +def row(state, obj):
          19 +    return obj.name, tuple(round(float(x), 3) for x in state.data[obj])
          20 +
          21 +
          22 +def changed(before, after):
          23 +    out = []
          24 +    for name in sorted(before.get_object_names()):
          25 +        a = before.get_object_from_name(name)
          26 +        b = after.get_object_from_name(name)
          27 +        if not np.array_equal(before.data[a], after.data[b]):
          28 +            out.append((name, row(before, a)[1], row(after, b)[1]))
          29 +    return out
          30 +
          31 +
          32 +def action(r0=(0, 0, 0, 0), r1=(0, 0, 0, 0)):
          33 +    return np.asarray((*r0, *r1), dtype=np.float32)
          34 +
          35 +
          36 +def dump(seed):
          37 +    env = make_env()
          38 +    state, info = env.reset(seed=seed)
          39 +    print("seed", seed, "info", info, "max_steps", env.max_steps)
          40 +    for typ in ("rover", "lander", "objective", "sample", "obstacle"):
          41 +        print(typ, *[row(state, o) for o in objects(state, env, typ)], sep="\n  ")
          42 +    env.close()
          43 +
          44 +
          45 +def selector(seed):
          46 +    for value in CENTERS:
          47 +        env = make_env()
          48 +        state, _ = env.reset(seed=seed)
          49 +        nxt, rew, term, trunc, info = env.step(action((0, 0, 0, value)))
          50 +        print(value, "reward", rew, "done", term, trunc, "changed", changed(state, nxt), "info", info)
          51 +        env.close()
          52 +
          53 +
          54 +def drive_and_operate(seed, rover_index, target_name, op_value, stop=0.12):
          55 +    """Greedily drive one rover directly to an object, then apply an operator."""
          56 +    env = make_env()
          57 +    state, _ = env.reset(seed=seed)
          58 +    rover_name = f"rover{rover_index}"
          59 +    steps = 0
          60 +    while steps < 100:
          61 +        r = state.get_object_from_name(rover_name)
          62 +        t = state.get_object_from_name(target_name)
          63 +        dx = state.get(t, "x") - state.get(r, "x")
          64 +        dy = state.get(t, "y") - state.get(r, "y")
          65 +        dist = math.hypot(dx, dy)
          66 +        if dist <= stop:
          67 +            break
          68 +        scale = min(1.0, max(0.0, (dist - stop) / max(abs(dx), abs(dy), 1e-9)))
          69 +        cmd = (max(-.2, min(.2, dx * scale)), max(-.2, min(.2, dy * scale)), 0, CENTERS[3])
          70 +        a = action(cmd, (0, 0, 0, CENTERS[3])) if rover_index == 0 else action((0, 0, 0, CENTERS[3]), cmd)
          71 +        nxt, _, term, trunc, _ = env.step(a)
          72 +        if not changed(state, nxt):
          73 +            print("stuck", rover_name, "at", row(state, r), "toward", row(state, t), "dist", dist)
          74 +            break
          75 +        state = nxt
          76 +        steps += 1
          77 +    before = state
          78 +    cmd = (0, 0, 0, op_value)
          79 +    a = action(cmd, (0, 0, 0, CENTERS[3])) if rover_index == 0 else action((0, 0, 0, CENTERS[3]), cmd)
          80 +    state, rew, term, trunc, info = env.step(a)
          81 +    print("steps", steps, "operator", op_value, "changed", changed(before, state), "done", term, trunc, "info", info)
          82 +    env.close()
          83 +
          84 +
          85 +if __name__ == "__main__":
          86 +    p = argparse.ArgumentParser()
          87 +    p.add_argument("mode", choices=["dump", "selector", "operate"])
          88 +    p.add_argument("--seed", type=int, default=0)
          89 +    p.add_argument("--rover", type=int, default=0)
          90 +    p.add_argument("--target", default="sample0")
          91 +    p.add_argument("--op", type=float, default=CENTERS[0])
          92 +    args = p.parse_args()
          93 +    if args.mode == "dump":
          94 +        dump(args.seed)
          95 +    elif args.mode == "selector":
          96 +        selector(args.seed)
          97 +    else:
          98 +        drive_and_operate(args.seed, args.rover, args.target, args.op)
```

</details>

<a id="C006"></a>
### C006 · Fix object type feature lookup in geometry probe

Commit `36258b277abd0c8b283651fe7d1c296535d03a25`; parents: fddd393297b4388c0bb002950eb148fc0a37f7f4. Recorded author date: 2026-09-11T11:45:21+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C006_36258b2.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_geometry.py b/probe_geometry.py
index e0421d0..51daa3e 100644
--- a/probe_geometry.py
+++ b/probe_geometry.py
@@ -8,7 +8,7 @@ def snapshot(state, env):
    8      8      for typ in env.observation_space.types:
    9      9          vals = []
   10     10          for obj in state.get_objects(typ):
   11        -            fs = env.observation_space.type_features[typ.name]
          11 +            fs = env.observation_space.type_features[typ]
   12     12              vals.append((obj.name, {f: float(state.get(obj, f)) for f in fs}))
   13     13          out[typ.name] = vals
   14     14      return out
```

</details>

<a id="C007"></a>
### C007 · Add rover collision and motion probe

Commit `56169bb2934fb8f3639bcc0918d2bc7d83c22b6c`; parents: 36258b277abd0c8b283651fe7d1c296535d03a25. Recorded author date: 2026-09-11T11:45:24+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C007_56169bb.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_motion_design.py b/probe_motion_design.py
new file mode 100644
index 0000000..8b830a9
--- /dev/null
+++ b/probe_motion_design.py
@@ -0,0 +1,30 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +
           4 +
           5 +def rover_xy(obs, env, i=0):
           6 +    typ = next(t for t in env.observation_space.types if t.name == "rover")
           7 +    rover = sorted(obs.get_objects(typ), key=lambda o: o.name)[i]
           8 +    return tuple(float(obs.get(rover, f)) for f in ("x", "y", "theta"))
           9 +
          10 +
          11 +def run(seed, commands):
          12 +    env = make_env()
          13 +    obs, _ = env.reset(seed=seed)
          14 +    print("start", rover_xy(obs, env))
          15 +    for label, delta, n in commands:
          16 +        for k in range(n):
          17 +            act = np.zeros(8, dtype=np.float32)
          18 +            act[0:2] = delta
          19 +            old = rover_xy(obs, env)
          20 +            obs, _, term, trunc, _ = env.step(act)
          21 +            new = rover_xy(obs, env)
          22 +            if new[:2] == old[:2] or k == n - 1:
          23 +                print(label, k + 1, old, "->", new, "reject", new[:2] == old[:2])
          24 +            if term or trunc:
          25 +                break
          26 +    env.close()
          27 +
          28 +
          29 +run(0, [("north", (0, .2), 22), ("west", (-.2, 0), 18), ("south", (0, -.2), 22)])
          30 +run(1, [("west", (-.2, 0), 18), ("north", (0, .2), 22), ("east", (.2, 0), 22)])
```

</details>

<a id="C008"></a>
### C008 · extend operator probe with stateful sample and image scenario

Commit `3c52b1b29e896e1de7335805722a15167da06d1c`; parents: 56169bb2934fb8f3639bcc0918d2bc7d83c22b6c. Recorded author date: 2026-09-11T11:46:08+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C008_3c52b1b.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_ops.py b/probe_ops.py
index a988884..f3d4c79 100644
--- a/probe_ops.py
+++ b/probe_ops.py
@@ -82,9 +82,59 @@ def drive_and_operate(seed, rover_index, target_name, op_value, stop=0.12):
   82     82      env.close()
   83     83  
   84     84  
          85 +def move(env, state, rover_index, tx, ty, stop=0.12, limit=100):
          86 +    rover_name = f"rover{rover_index}"
          87 +    for n in range(limit):
          88 +        r = state.get_object_from_name(rover_name)
          89 +        dx, dy = tx - state.get(r, "x"), ty - state.get(r, "y")
          90 +        dist = math.hypot(dx, dy)
          91 +        if dist <= stop:
          92 +            return state, n, False
          93 +        scale = min(1.0, max(0.0, (dist - stop) / max(abs(dx), abs(dy), 1e-9)))
          94 +        cmd = (max(-.2, min(.2, dx * scale)), max(-.2, min(.2, dy * scale)), 0, CENTERS[3])
          95 +        a = action(cmd, (0, 0, 0, CENTERS[3])) if rover_index == 0 else action((0, 0, 0, CENTERS[3]), cmd)
          96 +        nxt, _, _, _, _ = env.step(a)
          97 +        oldr, newr = state.get_object_from_name(rover_name), nxt.get_object_from_name(rover_name)
          98 +        stuck = (state.get(oldr, "x") == nxt.get(newr, "x") and state.get(oldr, "y") == nxt.get(newr, "y"))
          99 +        state = nxt
         100 +        if stuck:
         101 +            return state, n + 1, True
         102 +    return state, limit, True
         103 +
         104 +
         105 +def op(env, state, rover_index, op_index, motion=(0, 0, 0)):
         106 +    cmd = (*motion, CENTERS[op_index])
         107 +    a = action(cmd, (0, 0, 0, CENTERS[3])) if rover_index == 0 else action((0, 0, 0, CENTERS[3]), cmd)
         108 +    nxt, rew, term, trunc, info = env.step(a)
         109 +    print("op", op_index, "r", rover_index, "motion", motion, "changed", changed(state, nxt), "done", term, trunc)
         110 +    return nxt
         111 +
         112 +
         113 +def scenario(seed):
         114 +    env = make_env()
         115 +    state, _ = env.reset(seed=seed)
         116 +    # Seed 0 has a conveniently accessible soil sample near rover1.
         117 +    sample = state.get_object_from_name("sample4")
         118 +    state, n, stuck = move(env, state, 1, state.get(sample, "x"), state.get(sample, "y"))
         119 +    print("move to sample", n, stuck)
         120 +    state = op(env, state, 1, 0)
         121 +    state = op(env, state, 1, 4)
         122 +    state = op(env, state, 1, 5)
         123 +    # Approach an objective until its mound rejects further motion.
         124 +    objective = state.get_object_from_name("objective2")
         125 +    state, n, stuck = move(env, state, 1, state.get(objective, "x"), state.get(objective, "y"))
         126 +    print("move to objective", n, stuck)
         127 +    state = op(env, state, 1, 2)  # image without calibration: refused
         128 +    state = op(env, state, 1, 1)
         129 +    state = op(env, state, 1, 2)
         130 +    state = op(env, state, 1, 2)  # calibration was spent: refused
         131 +    state = op(env, state, 1, 4)  # expected out of lander range / occluded
         132 +    env.close()
         133 +
         134 +
   85    135  if __name__ == "__main__":
   86    136      p = argparse.ArgumentParser()
   87        -    p.add_argument("mode", choices=["dump", "selector", "operate"])
         137 +    p.add_argument("mode", choices=["dump", "selector", "operate", "scenario"])
   88    138      p.add_argument("--seed", type=int, default=0)
   89    139      p.add_argument("--rover", type=int, default=0)
   90    140      p.add_argument("--target", default="sample0")
@@ -94,5 +144,7 @@ if __name__ == "__main__":
   94    144          dump(args.seed)
   95    145      elif args.mode == "selector":
   96    146          selector(args.seed)
   97        -    else:
         147 +    elif args.mode == "operate":
   98    148          drive_and_operate(args.seed, args.rover, args.target, args.op)
         149 +    else:
         150 +        scenario(args.seed)
```

</details>

<a id="C009"></a>
### C009 · Add targeted wall and visibility semantics probes

Commit `ce9d483fd7a86f004d313bd98e0e820c09145a31`; parents: 3c52b1b29e896e1de7335805722a15167da06d1c. Recorded author date: 2026-09-11T11:46:09+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C009_ce9d483.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_semantics.py b/probe_semantics.py
new file mode 100644
index 0000000..5dcaf8a
--- /dev/null
+++ b/probe_semantics.py
@@ -0,0 +1,71 @@
           1 +"""Targeted probes for hidden wall, collision radius, home and camera semantics."""
           2 +from env_client import make_env
           3 +import numpy as np
           4 +
           5 +
           6 +def rover_data(s, e, idx=0):
           7 +    t = e.observation_space.get_type("rover")
           8 +    o = sorted(s.get_objects(t), key=lambda q: q.name)[idx]
           9 +    return o, tuple(float(s.get(o, f)) for f in ("x", "y", "theta", "store_full", "calibrated", "at_home"))
          10 +
          11 +
          12 +def act(e, a0=(0, 0, 0, 0), a1=(0, 0, 0, 0)):
          13 +    a = np.asarray(a0 + a1, dtype=np.float32)
          14 +    return e.step(a)[0]
          15 +
          16 +
          17 +def move_axis(e, s, idx, axis, target, maxn=100):
          18 +    for _ in range(maxn):
          19 +        _, d = rover_data(s, e, idx)
          20 +        cur = d[axis]
          21 +        delta = max(-0.2, min(0.2, target-cur))
          22 +        if abs(delta) < 1e-5:
          23 +            break
          24 +        aa = [0., 0., 0., 0.]
          25 +        aa[axis] = delta
          26 +        s2 = act(e, tuple(aa), (0,0,0,0)) if idx == 0 else act(e, (0,0,0,0), tuple(aa))
          27 +        _, d2 = rover_data(s2, e, idx)
          28 +        s = s2
          29 +        if abs(d2[axis]-cur) < 1e-6:
          30 +            break
          31 +    return s
          32 +
          33 +
          34 +def wall_probe(seed, y):
          35 +    e = make_env(); s,_=e.reset(seed=seed)
          36 +    s=move_axis(e,s,0,1,y)
          37 +    s=move_axis(e,s,0,0,-1.0)
          38 +    print("WALL",seed,y,rover_data(s,e,0)[1])
          39 +    e.close()
          40 +
          41 +
          42 +def main():
          43 +    for y in (-2.3,-1.75,-1.0,0.0,1.0,1.5,1.8,2.3):
          44 +        wall_probe(20,y)
          45 +
          46 +    # Boundary: choose mostly clear bottom/right edges.
          47 +    e=make_env(); s,_=e.reset(seed=30)
          48 +    s=move_axis(e,s,0,0,3.0); print("BOUND X",rover_data(s,e,0)[1])
          49 +    e.close()
          50 +
          51 +    # Home status along x and y offsets.
          52 +    for dx,dy in ((.05,0),(.1,0),(.15,0),(.2,0),(0,.05),(0,.1),(0,.15),(0,.2)):
          53 +        e=make_env(); s,_=e.reset(seed=31)
          54 +        s=act(e,(dx,dy,0,0)); print("HOME",dx,dy,rover_data(s,e,0)[1]); e.close()
          55 +
          56 +    # Camera at a clear standoff below seed 0's right-center mound/objective.
          57 +    # Route on right half, theta remains pi and objective lies roughly north.
          58 +    for heading_delta in (0.0, -1.57, 1.57, 3.14):
          59 +        e=make_env(); s,_=e.reset(seed=0)
          60 +        s=move_axis(e,s,0,0,1.0); s=move_axis(e,s,0,1,1.15)
          61 +        # Apply requested heading change in <=.4 increments.
          62 +        remain=heading_delta
          63 +        while abs(remain)>1e-4:
          64 +            q=max(-.4,min(.4,remain)); s=act(e,(0,0,q,0)); remain-=q
          65 +        s=act(e,(0,0,0,-.5))
          66 +        print("CAL",heading_delta,rover_data(s,e,0)[1])
          67 +        e.close()
          68 +
          69 +
          70 +if __name__ == "__main__":
          71 +    main()
```

</details>

<a id="C010"></a>
### C010 · Probe lower wall crossing clearance

Commit `c8b9c70a77e9184d51b7e81e8ad1a98df6000996`; parents: ce9d483fd7a86f004d313bd98e0e820c09145a31. Recorded author date: 2026-09-11T11:46:22+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C010_c8b9c70.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_motion_design.py b/probe_motion_design.py
index 8b830a9..e24e373 100644
--- a/probe_motion_design.py
+++ b/probe_motion_design.py
@@ -28,3 +28,5 @@ def run(seed, commands):
   28     28  
   29     29  run(0, [("north", (0, .2), 22), ("west", (-.2, 0), 18), ("south", (0, -.2), 22)])
   30     30  run(1, [("west", (-.2, 0), 18), ("north", (0, .2), 22), ("east", (.2, 0), 22)])
          31 +for south_steps in range(0, 4):
          32 +    run(20 + south_steps, [("south-gap", (0, -.2), south_steps), ("cross-west", (-.2, 0), 7)])
```

</details>

<a id="C011"></a>
### C011 · probe home tolerance and simultaneous rover collision handling

Commit `dbe015e7076c61ad5b3b52060d4e5a4026f084f8`; parents: c8b9c70a77e9184d51b7e81e8ad1a98df6000996. Recorded author date: 2026-09-11T11:46:45+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C011_dbe015e.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_ops.py b/probe_ops.py
index f3d4c79..3355fef 100644
--- a/probe_ops.py
+++ b/probe_ops.py
@@ -132,9 +132,33 @@ def scenario(seed):
  132    132      env.close()
  133    133  
  134    134  
         135 +def home_probe(seed):
         136 +    env = make_env()
         137 +    state, _ = env.reset(seed=seed)
         138 +    # Walk rover0 away in 0.1m increments, then back, displaying at_home.
         139 +    for dx in (0.1, 0.1, 0.1, -0.1, -0.1, -0.1):
         140 +        before = state
         141 +        state, _, term, trunc, _ = env.step(action((dx, 0, 0, CENTERS[3]), (0, 0, 0, CENTERS[3])))
         142 +        r = state.get_object_from_name("rover0")
         143 +        print("dx", dx, "xy", state.get(r, "x"), state.get(r, "y"), "home", state.get(r, "at_home"), "done", term, trunc,
         144 +              "delta", changed(before, state))
         145 +    env.close()
         146 +
         147 +
         148 +def simultaneous_probe(seed):
         149 +    env = make_env()
         150 +    state, _ = env.reset(seed=seed)
         151 +    # Initial rovers are two metres apart. Drive both toward x=0 concurrently.
         152 +    for n in range(6):
         153 +        before = state
         154 +        state, _, _, _, _ = env.step(action((-.2, 0, 0, CENTERS[3]), (.2, 0, 0, CENTERS[3])))
         155 +        print("step", n, changed(before, state))
         156 +    env.close()
         157 +
         158 +
  135    159  if __name__ == "__main__":
  136    160      p = argparse.ArgumentParser()
  137        -    p.add_argument("mode", choices=["dump", "selector", "operate", "scenario"])
         161 +    p.add_argument("mode", choices=["dump", "selector", "operate", "scenario", "home", "simultaneous"])
  138    162      p.add_argument("--seed", type=int, default=0)
  139    163      p.add_argument("--rover", type=int, default=0)
  140    164      p.add_argument("--target", default="sample0")
@@ -146,5 +170,9 @@ if __name__ == "__main__":
  146    170          selector(args.seed)
  147    171      elif args.mode == "operate":
  148    172          drive_and_operate(args.seed, args.rover, args.target, args.op)
  149        -    else:
         173 +    elif args.mode == "scenario":
  150    174          scenario(args.seed)
         175 +    elif args.mode == "home":
         176 +        home_probe(args.seed)
         177 +    else:
         178 +        simultaneous_probe(args.seed)
```

</details>

<a id="C012"></a>
### C012 · Add initial geometry-based rover policy and test harness

Commit `0f846f82c995a3f3cfb8bea319322d69e7504afa`; parents: dbe015e7076c61ad5b3b52060d4e5a4026f084f8. Recorded author date: 2026-09-11T11:46:48+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0016](01_timeline.md#E0016): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C012_0f846f8_approach.py) · [Exact all-file diff](evidence/diffs/C012_0f846f8.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..71cda63
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,287 @@
           1 +"""Fast geometry-based controller for the object-centric Rovers task."""
           2 +
           3 +import heapq
           4 +import math
           5 +import numpy as np
           6 +
           7 +
           8 +SAMPLE = -5.0 / 6.0
           9 +CALIBRATE = -0.5
          10 +IMAGE = -1.0 / 6.0
          11 +NOOP = 1.0 / 6.0
          12 +SEND = 0.5
          13 +DROP = 5.0 / 6.0
          14 +
          15 +
          16 +class GeneratedApproach:
          17 +    def __init__(self, action_space, observation_space, primitives):
          18 +        self.action_space = action_space
          19 +        self.space = observation_space
          20 +        self.types = {t.name: t for t in observation_space.types}
          21 +
          22 +    def _objs(self, state, kind):
          23 +        return list(state.get_objects(self.types[kind]))
          24 +
          25 +    @staticmethod
          26 +    def _name(obj):
          27 +        return obj.name
          28 +
          29 +    def _v(self, state, obj, feat):
          30 +        return float(state.get(obj, feat))
          31 +
          32 +    def _xy(self, state, obj):
          33 +        return (self._v(state, obj, "x"), self._v(state, obj, "y"))
          34 +
          35 +    def reset(self, state, info):
          36 +        self.homes = {}
          37 +        rovers = sorted(self._objs(state, "rover"), key=self._name)
          38 +        for i, rover in enumerate(rovers):
          39 +            self.homes[i] = self._xy(state, rover)
          40 +        self.obstacles = []
          41 +        for ob in self._objs(state, "obstacle"):
          42 +            x, y = self._xy(state, ob)
          43 +            hx = self._v(state, ob, "half_x")
          44 +            hy = self._v(state, ob, "half_y")
          45 +            self.obstacles.append((x, y, hx, hy))
          46 +        samples = self._objs(state, "sample")
          47 +        stones = [s for s in samples if self._v(state, s, "is_soil") < 0.5]
          48 +        soils = [s for s in samples if self._v(state, s, "is_soil") > 0.5]
          49 +        self.sample_names = {
          50 +            0: self._closest_name(state, stones, self.homes[0]),
          51 +            1: self._closest_name(state, soils, self.homes[1]),
          52 +        }
          53 +        self.phase = ["sample", "sample"]
          54 +        self.targets = [None, None]
          55 +        self.paths = [[], []]
          56 +        self.last_pos = [self.homes[0], self.homes[1]]
          57 +        self.stuck = [0, 0]
          58 +        self.image_site_index = 0
          59 +        self.image_attempts = 0
          60 +        self.send_attempts = [0, 0]
          61 +
          62 +    def _closest_name(self, state, objs, point):
          63 +        if not objs:
          64 +            return None
          65 +        return min(objs, key=lambda o: self._dist(self._xy(state, o), point)).name
          66 +
          67 +    @staticmethod
          68 +    def _dist(a, b):
          69 +        return math.hypot(a[0] - b[0], a[1] - b[1])
          70 +
          71 +    def _blocked(self, p, extra=None, margin=0.17):
          72 +        x, y = p
          73 +        if x < -2.38 or x > 2.38 or y < -2.38 or y > 2.38:
          74 +            return True
          75 +        for ox, oy, hx, hy in self.obstacles:
          76 +            if abs(x - ox) <= hx + margin and abs(y - oy) <= hy + margin:
          77 +                return True
          78 +        if extra is not None and self._dist(p, extra) < 0.28:
          79 +            return True
          80 +        return False
          81 +
          82 +    def _line_free(self, a, b, extra=None):
          83 +        d = self._dist(a, b)
          84 +        n = max(1, int(d / 0.08))
          85 +        for i in range(1, n + 1):
          86 +            q = (a[0] + (b[0] - a[0]) * i / n,
          87 +                 a[1] + (b[1] - a[1]) * i / n)
          88 +            if self._blocked(q, extra):
          89 +                return False
          90 +        return True
          91 +
          92 +    def _plan(self, start, goal, extra=None):
          93 +        # A compact 0.1 m grid A*. Endpoints are connected separately so exact
          94 +        # sample and home coordinates remain attainable.
          95 +        res = 0.1
          96 +        lo = -2.4
          97 +        conv = lambda p: (int(round((p[0] - lo) / res)),
          98 +                          int(round((p[1] - lo) / res)))
          99 +        pos = lambda n: (lo + n[0] * res, lo + n[1] * res)
         100 +        s, g = conv(start), conv(goal)
         101 +        if self._line_free(start, goal, extra):
         102 +            return [goal]
         103 +        frontier = [(0.0, s)]
         104 +        came = {s: None}
         105 +        cost = {s: 0.0}
         106 +        moves = ((1, 0), (-1, 0), (0, 1), (0, -1),
         107 +                 (1, 1), (1, -1), (-1, 1), (-1, -1))
         108 +        found = None
         109 +        while frontier:
         110 +            _, cur = heapq.heappop(frontier)
         111 +            if cur == g or self._dist(pos(cur), goal) < 0.16:
         112 +                found = cur
         113 +                break
         114 +            for dx, dy in moves:
         115 +                nb = (cur[0] + dx, cur[1] + dy)
         116 +                q = pos(nb)
         117 +                if self._blocked(q, extra):
         118 +                    continue
         119 +                nc = cost[cur] + (1.414 if dx and dy else 1.0)
         120 +                if nc < cost.get(nb, 1e30):
         121 +                    cost[nb] = nc
         122 +                    came[nb] = cur
         123 +                    h = math.hypot(nb[0] - g[0], nb[1] - g[1])
         124 +                    heapq.heappush(frontier, (nc + h, nb))
         125 +        if found is None:
         126 +            return [goal]
         127 +        rev = []
         128 +        cur = found
         129 +        while cur != s:
         130 +            rev.append(pos(cur))
         131 +            cur = came[cur]
         132 +        rev.reverse()
         133 +        rev.append(goal)
         134 +        # String-pull the grid route to reduce action count.
         135 +        route = []
         136 +        anchor = start
         137 +        i = 0
         138 +        while i < len(rev):
         139 +            j = len(rev) - 1
         140 +            while j > i and not self._line_free(anchor, rev[j], extra):
         141 +                j -= 1
         142 +            route.append(rev[j])
         143 +            anchor = rev[j]
         144 +            i = j + 1
         145 +        return route
         146 +
         147 +    def _move(self, idx, pos, goal, other):
         148 +        if self.targets[idx] != goal or not self.paths[idx] or self.stuck[idx] >= 2:
         149 +            self.targets[idx] = goal
         150 +            self.paths[idx] = self._plan(pos, goal, other)
         151 +            self.stuck[idx] = 0
         152 +        while self.paths[idx] and self._dist(pos, self.paths[idx][0]) < 0.075:
         153 +            self.paths[idx].pop(0)
         154 +        waypoint = self.paths[idx][0] if self.paths[idx] else goal
         155 +        dx = max(-0.2, min(0.2, waypoint[0] - pos[0]))
         156 +        dy = max(-0.2, min(0.2, waypoint[1] - pos[1]))
         157 +        return dx, dy
         158 +
         159 +    def _objective_sites(self, state):
         160 +        objs = sorted(self._objs(state, "objective"), key=self._name)
         161 +        sites = []
         162 +        # South is normally shortest and clear of the mound row; alternate
         163 +        # directions handle pillars that happen to occlude a particular view.
         164 +        directions = ((0, -1), (1, 0), (-1, 0), (0, 1),
         165 +                      (0.707, -0.707), (-0.707, -0.707))
         166 +        for ob in objs:
         167 +            x, y = self._xy(state, ob)
         168 +            for ux, uy in directions:
         169 +                q = (x + 0.62 * ux, y + 0.62 * uy)
         170 +                if not self._blocked(q):
         171 +                    sites.append(q)
         172 +        return sites
         173 +
         174 +    def _all_images_taken(self, state):
         175 +        return all(self._v(state, o, "have_image_rover0") > 0.5
         176 +                   for o in self._objs(state, "objective"))
         177 +
         178 +    def _all_images_received(self, state):
         179 +        return all(self._v(state, o, "received_image") > 0.5
         180 +                   for o in self._objs(state, "objective"))
         181 +
         182 +    def _sample_obj(self, state, idx):
         183 +        name = self.sample_names[idx]
         184 +        if name is None:
         185 +            return None
         186 +        return state.get_object_from_name(name)
         187 +
         188 +    def _received_own_sample(self, state, idx):
         189 +        ob = self._sample_obj(state, idx)
         190 +        return ob is None or self._v(state, ob, "received_analysis") > 0.5
         191 +
         192 +    def _set_op(self, action, idx, value):
         193 +        action[4 * idx + 3] = value
         194 +
         195 +    def get_action(self, state):
         196 +        action = np.zeros(8, dtype=np.float32)
         197 +        action[3] = NOOP
         198 +        action[7] = NOOP
         199 +        rovers = sorted(self._objs(state, "rover"), key=self._name)
         200 +        positions = [self._xy(state, r) for r in rovers]
         201 +
         202 +        for i in range(2):
         203 +            moved = self._dist(positions[i], self.last_pos[i])
         204 +            self.stuck[i] = self.stuck[i] + 1 if moved < 0.015 else 0
         205 +            self.last_pos[i] = positions[i]
         206 +            r = rovers[i]
         207 +            full = self._v(state, r, "store_full") > 0.5
         208 +            calibrated = self._v(state, r, "calibrated") > 0.5
         209 +
         210 +            if self.phase[i] == "sample":
         211 +                sob = self._sample_obj(state, i)
         212 +                analyzed = sob is None or self._v(state, sob, "analyzed_rover%d" % i) > 0.5
         213 +                if analyzed:
         214 +                    self.phase[i] = "images" if i == 0 else "send"
         215 +                    self.targets[i] = None
         216 +                elif self._dist(positions[i], self._xy(state, sob)) <= 0.235:
         217 +                    self._set_op(action, i, SAMPLE)
         218 +                    continue
         219 +                else:
         220 +                    dx, dy = self._move(i, positions[i], self._xy(state, sob), positions[1-i])
         221 +                    action[4*i] = dx
         222 +                    action[4*i+1] = dy
         223 +                    continue
         224 +
         225 +            if self.phase[i] == "images":
         226 +                if self._all_images_taken(state):
         227 +                    self.phase[i] = "send"
         228 +                    self.targets[i] = None
         229 +                else:
         230 +                    sites = self._objective_sites(state)
         231 +                    if not sites:
         232 +                        sites = [(0.0, 1.25)]
         233 +                    site = sites[self.image_site_index % len(sites)]
         234 +                    if self._dist(positions[i], site) > 0.12:
         235 +                        dx, dy = self._move(i, positions[i], site, positions[1-i])
         236 +                        action[4*i] = dx
         237 +                        action[4*i+1] = dy
         238 +                        continue
         239 +                    if calibrated:
         240 +                        self._set_op(action, i, IMAGE)
         241 +                    else:
         242 +                        self._set_op(action, i, CALIBRATE)
         243 +                    self.image_attempts += 1
         244 +                    if self.image_attempts >= 3:
         245 +                        self.image_attempts = 0
         246 +                        self.image_site_index += 1
         247 +                        self.targets[i] = None
         248 +                    continue
         249 +
         250 +            if self.phase[i] == "send":
         251 +                need = (not self._received_own_sample(state, i) or
         252 +                        (i == 0 and not self._all_images_received(state)))
         253 +                if not need:
         254 +                    self.phase[i] = "drop"
         255 +                else:
         256 +                    lander = self._xy(state, self._objs(state, "lander")[0])
         257 +                    # Close, unobstructed points around the lander.
         258 +                    send_sites = [(lander[0] + 0.48, lander[1] + 0.15),
         259 +                                  (lander[0] + 0.15, lander[1] + 0.48),
         260 +                                  (lander[0] - 0.35, lander[1] + 0.25)]
         261 +                    site = send_sites[(self.send_attempts[i] // 2) % len(send_sites)]
         262 +                    if self._dist(positions[i], site) > 0.13:
         263 +                        dx, dy = self._move(i, positions[i], site, positions[1-i])
         264 +                        action[4*i] = dx
         265 +                        action[4*i+1] = dy
         266 +                    else:
         267 +                        self._set_op(action, i, SEND)
         268 +                        self.send_attempts[i] += 1
         269 +                        if self.send_attempts[i] % 2 == 0:
         270 +                            self.targets[i] = None
         271 +                    continue
         272 +
         273 +            if self.phase[i] == "drop":
         274 +                if full:
         275 +                    self._set_op(action, i, DROP)
         276 +                    continue
         277 +                self.phase[i] = "home"
         278 +                self.targets[i] = None
         279 +
         280 +            if self.phase[i] == "home":
         281 +                if self._v(state, r, "at_home") < 0.5:
         282 +                    dx, dy = self._move(i, positions[i], self.homes[i], positions[1-i])
         283 +                    action[4*i] = dx
         284 +                    action[4*i+1] = dy
         285 +                continue
         286 +
         287 +        return action
diff --git a/inspect_env.py b/inspect_env.py
new file mode 100644
index 0000000..f164f96
--- /dev/null
+++ b/inspect_env.py
@@ -0,0 +1,13 @@
           1 +from env_client import make_env
           2 +
           3 +env = make_env()
           4 +for seed in range(2):
           5 +    obs, info = env.reset(seed=seed)
           6 +    print("SEED", seed, "info", info, "max", env.max_steps)
           7 +    print("types", env.observation_space.types)
           8 +    for name in obs.get_object_names():
           9 +        obj = obs.get_object_from_name(name)
          10 +        typ = obj.type.name if hasattr(obj.type, "name") else str(obj.type)
          11 +        feats = env.observation_space.type_features[obj.type]
          12 +        print(name, typ, {f: float(obs.get(obj, f)) for f in feats})
          13 +env.close()
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..22a97c4
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,32 @@
           1 +import sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +
           5 +
           6 +def run(seed, verbose=False):
           7 +    env = make_env()
           8 +    obs, info = env.reset(seed=seed)
           9 +    app = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
          10 +    app.reset(obs, info)
          11 +    total = 0
          12 +    term = trunc = False
          13 +    for step in range(env.max_steps):
          14 +        obs, rew, term, trunc, info = env.step(app.get_action(obs))
          15 +        total += rew
          16 +        if term or trunc:
          17 +            break
          18 +    if verbose or not term:
          19 +        print(seed, term, trunc, step + 1, total, info, app.phase)
          20 +        if not term:
          21 +            for typ in ("rover", "objective", "sample"):
          22 +                for ob in obs.get_objects(app.types[typ]):
          23 +                    feats = app.space.type_features[ob.type]
          24 +                    print(ob.name, {f: float(obs.get(ob, f)) for f in feats})
          25 +    env.close()
          26 +    return term, step + 1
          27 +
          28 +
          29 +if __name__ == "__main__":
          30 +    seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
          31 +    out = [run(s) for s in seeds]
          32 +    print("SUMMARY", sum(x[0] for x in out), "/", len(out), out)
```

</details>

<a id="C013"></a>
### C013 · Increase collision clearance and radio opportunistically

Commit `a0302251f8192894c5434bc31e835ade9dc33526`; parents: 0f846f82c995a3f3cfb8bea319322d69e7504afa. Recorded author date: 2026-09-11T11:47:11+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0027](01_timeline.md#E0027): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C013_a030225_approach.py) · [Exact all-file diff](evidence/diffs/C013_a030225.diff)

[Previous saved controller snapshot](evidence/versions/C012_0f846f8_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 71cda63..f740435 100644
--- a/approach.py
+++ b/approach.py
@@ -68,7 +68,7 @@ class GeneratedApproach:
   68     68      def _dist(a, b):
   69     69          return math.hypot(a[0] - b[0], a[1] - b[1])
   70     70  
   71        -    def _blocked(self, p, extra=None, margin=0.17):
          71 +    def _blocked(self, p, extra=None, margin=0.27):
   72     72          x, y = p
   73     73          if x < -2.38 or x > 2.38 or y < -2.38 or y > 2.38:
   74     74              return True
@@ -263,6 +263,9 @@ class GeneratedApproach:
  263    263                          dx, dy = self._move(i, positions[i], site, positions[1-i])
  264    264                          action[4*i] = dx
  265    265                          action[4*i+1] = dy
         266 +                        # Sending is cheap and may already be possible anywhere
         267 +                        # along the route (range is 4m), avoiding needless travel.
         268 +                        self._set_op(action, i, SEND)
  266    269                      else:
  267    270                          self._set_op(action, i, SEND)
  268    271                          self.send_attempts[i] += 1
diff --git a/probe_ops.py b/probe_ops.py
index 3355fef..d402dbd 100644
--- a/probe_ops.py
+++ b/probe_ops.py
@@ -156,9 +156,17 @@ def simultaneous_probe(seed):
  156    156      env.close()
  157    157  
  158    158  
         159 +def count_probe(start, count):
         160 +    for seed in range(start, start + count):
         161 +        env = make_env()
         162 +        _, info = env.reset(seed=seed)
         163 +        print(seed, info.get("object_count"))
         164 +        env.close()
         165 +
         166 +
  159    167  if __name__ == "__main__":
  160    168      p = argparse.ArgumentParser()
  161        -    p.add_argument("mode", choices=["dump", "selector", "operate", "scenario", "home", "simultaneous"])
         169 +    p.add_argument("mode", choices=["dump", "selector", "operate", "scenario", "home", "simultaneous", "counts"])
  162    170      p.add_argument("--seed", type=int, default=0)
  163    171      p.add_argument("--rover", type=int, default=0)
  164    172      p.add_argument("--target", default="sample0")
@@ -174,5 +182,7 @@ if __name__ == "__main__":
  174    182          scenario(args.seed)
  175    183      elif args.mode == "home":
  176    184          home_probe(args.seed)
  177        -    else:
         185 +    elif args.mode == "simultaneous":
  178    186          simultaneous_probe(args.seed)
         187 +    else:
         188 +        count_probe(args.seed, 20)
```

</details>

<a id="C014"></a>
### C014 · Probe sample and radio visibility from right arena

Commit `0ba4818f7975931aa294dffa1c41a3751e7f56a8`; parents: a0302251f8192894c5434bc31e835ade9dc33526. Recorded author date: 2026-09-11T11:47:26+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C014_0ba4818.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_ops_design.py b/probe_ops_design.py
new file mode 100644
index 0000000..5123dbe
--- /dev/null
+++ b/probe_ops_design.py
@@ -0,0 +1,37 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +
           4 +
           5 +SAMPLE = -5 / 6
           6 +SEND = 1 / 2
           7 +
           8 +
           9 +env = make_env()
          10 +obs, _ = env.reset(seed=1)
          11 +st = next(t for t in env.observation_space.types if t.name == "sample")
          12 +rv = next(t for t in env.observation_space.types if t.name == "rover")
          13 +r0 = sorted(obs.get_objects(rv), key=lambda o: o.name)[0]
          14 +s3 = sorted(obs.get_objects(st), key=lambda o: o.name)[3]
          15 +
          16 +
          17 +def status(label):
          18 +    print(label, "rover", [float(obs.get(r0, f)) for f in ("x", "y", "store_full")],
          19 +          "sample", [float(obs.get(s3, f)) for f in ("analyzed_rover0", "received_analysis")])
          20 +
          21 +
          22 +status("start")
          23 +for k in range(2):
          24 +    a = np.zeros(8, np.float32)
          25 +    a[:2] = (-.2, .2)
          26 +    if k == 1:
          27 +        a[3] = SAMPLE
          28 +    obs, *_ = env.step(a)
          29 +    status("move/sample")
          30 +for pos_label, delta in (("send-here", (0, 0)), ("south", (0, -.2)), ("south", (0, -.2)),
          31 +                         ("west", (-.2, 0)), ("west", (-.2, 0))):
          32 +    a = np.zeros(8, np.float32)
          33 +    a[:2] = delta
          34 +    a[3] = SEND
          35 +    obs, *_ = env.step(a)
          36 +    status(pos_label)
          37 +env.close()
```

</details>

<a id="C015"></a>
### C015 · Probe lower-gap radio point

Commit `c9a3e23fdd4fded13ee9f3827e92eda40f34bdd3`; parents: 0ba4818f7975931aa294dffa1c41a3751e7f56a8. Recorded author date: 2026-09-11T11:47:35+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C015_c9a3e23.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_ops_design.py b/probe_ops_design.py
index 5123dbe..77c1a5f 100644
--- a/probe_ops_design.py
+++ b/probe_ops_design.py
@@ -34,4 +34,10 @@ for pos_label, delta in (("send-here", (0, 0)), ("south", (0, -.2)), ("south", (
   34     34      a[3] = SEND
   35     35      obs, *_ = env.step(a)
   36     36      status(pos_label)
          37 +for k in range(3):
          38 +    a = np.zeros(8, np.float32)
          39 +    a[1] = -.2
          40 +    a[3] = SEND
          41 +    obs, *_ = env.step(a)
          42 +    status("gap-send")
   37     43  env.close()
```

</details>

<a id="C016"></a>
### C016 · Probe image visibility and calibration semantics

Commit `fd428f80bb7f87173472455850c2c01371479739`; parents: c9a3e23fdd4fded13ee9f3827e92eda40f34bdd3. Recorded author date: 2026-09-11T11:47:50+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C016_fd428f8.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_image_design.py b/probe_image_design.py
new file mode 100644
index 0000000..e80253b
--- /dev/null
+++ b/probe_image_design.py
@@ -0,0 +1,33 @@
           1 +import numpy as np
           2 +from env_client import make_env
           3 +
           4 +CALIBRATE = -1 / 2
           5 +IMAGE = -1 / 6
           6 +env = make_env()
           7 +obs, _ = env.reset(seed=1)
           8 +space = env.observation_space
           9 +rt = next(t for t in space.types if t.name == "rover")
          10 +ot = next(t for t in space.types if t.name == "objective")
          11 +r0 = sorted(obs.get_objects(rt), key=lambda o: o.name)[0]
          12 +objs = sorted(obs.get_objects(ot), key=lambda o: o.name)
          13 +
          14 +
          15 +def show(label):
          16 +    print(label, [round(float(obs.get(r0, f)), 2) for f in ("x", "y", "calibrated")],
          17 +          [[int(obs.get(o, f)) for f in ("have_image_rover0", "received_image")] for o in objs])
          18 +
          19 +
          20 +for k in range(13):
          21 +    a = np.zeros(8, np.float32)
          22 +    if k < 2:
          23 +        a[:2] = (.2, .2)
          24 +    else:
          25 +        a[1] = .2
          26 +    obs, *_ = env.step(a)
          27 +show("vantage")
          28 +for op in (CALIBRATE, IMAGE, CALIBRATE, IMAGE):
          29 +    a = np.zeros(8, np.float32)
          30 +    a[3] = op
          31 +    obs, *_ = env.step(a)
          32 +    show("op")
          33 +env.close()
```

</details>

<a id="C017"></a>
### C017 · Respect central wall and split imaging across rovers

Commit `738181b2caac73262a5d59e56fae8c5f2c0692a6`; parents: fd428f80bb7f87173472455850c2c01371479739. Recorded author date: 2026-09-11T11:50:10+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0035](01_timeline.md#E0035): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C017_738181b_approach.py) · [Exact all-file diff](evidence/diffs/C017_738181b.diff)

[Previous saved controller snapshot](evidence/versions/C013_a030225_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index f740435..9f65e6d 100644
--- a/approach.py
+++ b/approach.py
@@ -43,20 +43,26 @@ class GeneratedApproach:
   43     43              hx = self._v(state, ob, "half_x")
   44     44              hy = self._v(state, ob, "half_y")
   45     45              self.obstacles.append((x, y, hx, hy))
          46 +        # The fixed separating wall is part of the arena but omitted from the
          47 +        # object list.  Treat it as a full-height divider: all useful tasks have
          48 +        # a reachable stance on their own side.
          49 +        self.obstacles.append((0.0, 0.0, 0.18, 2.6))
   46     50          samples = self._objs(state, "sample")
   47     51          stones = [s for s in samples if self._v(state, s, "is_soil") < 0.5]
   48     52          soils = [s for s in samples if self._v(state, s, "is_soil") > 0.5]
          53 +        right_stones = [s for s in stones if self._v(state, s, "x") >= -0.05]
          54 +        left_soils = [s for s in soils if self._v(state, s, "x") <= 0.05]
   49     55          self.sample_names = {
   50        -            0: self._closest_name(state, stones, self.homes[0]),
   51        -            1: self._closest_name(state, soils, self.homes[1]),
          56 +            0: self._closest_name(state, right_stones or stones, self.homes[0]),
          57 +            1: self._closest_name(state, left_soils or soils, self.homes[1]),
   52     58          }
   53     59          self.phase = ["sample", "sample"]
   54     60          self.targets = [None, None]
   55     61          self.paths = [[], []]
   56     62          self.last_pos = [self.homes[0], self.homes[1]]
   57     63          self.stuck = [0, 0]
   58        -        self.image_site_index = 0
   59        -        self.image_attempts = 0
          64 +        self.image_site_index = [0, 0]
          65 +        self.image_attempts = [0, 0]
   60     66          self.send_attempts = [0, 0]
   61     67  
   62     68      def _closest_name(self, state, objs, point):
@@ -68,7 +74,7 @@ class GeneratedApproach:
   68     74      def _dist(a, b):
   69     75          return math.hypot(a[0] - b[0], a[1] - b[1])
   70     76  
   71        -    def _blocked(self, p, extra=None, margin=0.27):
          77 +    def _blocked(self, p, extra=None, margin=0.18):
   72     78          x, y = p
   73     79          if x < -2.38 or x > 2.38 or y < -2.38 or y > 2.38:
   74     80              return True
@@ -156,8 +162,10 @@ class GeneratedApproach:
  156    162          dy = max(-0.2, min(0.2, waypoint[1] - pos[1]))
  157    163          return dx, dy
  158    164  
  159        -    def _objective_sites(self, state):
         165 +    def _objective_sites(self, state, idx):
  160    166          objs = sorted(self._objs(state, "objective"), key=self._name)
         167 +        objs = [o for o in objs if not self._image_done(state, o) and
         168 +                ((self._v(state, o, "x") >= 0) == (idx == 0))]
  161    169          sites = []
  162    170          # South is normally shortest and clear of the mound row; alternate
  163    171          # directions handle pillars that happen to occlude a particular view.
@@ -167,12 +175,24 @@ class GeneratedApproach:
  167    175              x, y = self._xy(state, ob)
  168    176              for ux, uy in directions:
  169    177                  q = (x + 0.62 * ux, y + 0.62 * uy)
  170        -                if not self._blocked(q):
         178 +                if not self._blocked(q) and ((q[0] > 0) == (idx == 0)):
  171    179                      sites.append(q)
  172    180          return sites
  173    181  
  174        -    def _all_images_taken(self, state):
  175        -        return all(self._v(state, o, "have_image_rover0") > 0.5
         182 +    def _image_done(self, state, ob):
         183 +        return (self._v(state, ob, "received_image") > 0.5 or
         184 +                self._v(state, ob, "have_image_rover0") > 0.5 or
         185 +                self._v(state, ob, "have_image_rover1") > 0.5)
         186 +
         187 +    def _side_images_done(self, state, idx):
         188 +        side = [o for o in self._objs(state, "objective")
         189 +                if ((self._v(state, o, "x") >= 0) == (idx == 0))]
         190 +        return all(self._image_done(state, o) for o in side)
         191 +
         192 +    def _own_images_received(self, state, idx):
         193 +        own = "have_image_rover%d" % idx
         194 +        return all(self._v(state, o, own) < 0.5 or
         195 +                   self._v(state, o, "received_image") > 0.5
  176    196                     for o in self._objs(state, "objective"))
  177    197  
  178    198      def _all_images_received(self, state):
@@ -185,6 +205,15 @@ class GeneratedApproach:
  185    205              return None
  186    206          return state.get_object_from_name(name)
  187    207  
         208 +    @staticmethod
         209 +    def _same_side_goal(point, idx):
         210 +        x, y = point
         211 +        if idx == 0 and x < 0.43:
         212 +            x = 0.43
         213 +        if idx == 1 and x > -0.43:
         214 +            x = -0.43
         215 +        return (x, y)
         216 +
  188    217      def _received_own_sample(self, state, idx):
  189    218          ob = self._sample_obj(state, idx)
  190    219          return ob is None or self._v(state, ob, "received_analysis") > 0.5
@@ -217,20 +246,21 @@ class GeneratedApproach:
  217    246                      self._set_op(action, i, SAMPLE)
  218    247                      continue
  219    248                  else:
  220        -                    dx, dy = self._move(i, positions[i], self._xy(state, sob), positions[1-i])
         249 +                    goal = self._same_side_goal(self._xy(state, sob), i)
         250 +                    dx, dy = self._move(i, positions[i], goal, positions[1-i])
  221    251                      action[4*i] = dx
  222    252                      action[4*i+1] = dy
  223    253                      continue
  224    254  
  225    255              if self.phase[i] == "images":
  226        -                if self._all_images_taken(state):
         256 +                if self._side_images_done(state, i):
  227    257                      self.phase[i] = "send"
  228    258                      self.targets[i] = None
  229    259                  else:
  230        -                    sites = self._objective_sites(state)
         260 +                    sites = self._objective_sites(state, i)
  231    261                      if not sites:
  232    262                          sites = [(0.0, 1.25)]
  233        -                    site = sites[self.image_site_index % len(sites)]
         263 +                    site = sites[self.image_site_index[i] % len(sites)]
  234    264                      if self._dist(positions[i], site) > 0.12:
  235    265                          dx, dy = self._move(i, positions[i], site, positions[1-i])
  236    266                          action[4*i] = dx
@@ -240,24 +270,25 @@ class GeneratedApproach:
  240    270                          self._set_op(action, i, IMAGE)
  241    271                      else:
  242    272                          self._set_op(action, i, CALIBRATE)
  243        -                    self.image_attempts += 1
  244        -                    if self.image_attempts >= 3:
  245        -                        self.image_attempts = 0
  246        -                        self.image_site_index += 1
         273 +                    self.image_attempts[i] += 1
         274 +                    if self.image_attempts[i] >= 3:
         275 +                        self.image_attempts[i] = 0
         276 +                        self.image_site_index[i] += 1
  247    277                          self.targets[i] = None
  248    278                      continue
  249    279  
  250    280              if self.phase[i] == "send":
  251    281                  need = (not self._received_own_sample(state, i) or
  252        -                        (i == 0 and not self._all_images_received(state)))
         282 +                        not self._own_images_received(state, i))
  253    283                  if not need:
  254    284                      self.phase[i] = "drop"
  255    285                  else:
  256    286                      lander = self._xy(state, self._objs(state, "lander")[0])
  257    287                      # Close, unobstructed points around the lander.
  258        -                    send_sites = [(lander[0] + 0.48, lander[1] + 0.15),
  259        -                                  (lander[0] + 0.15, lander[1] + 0.48),
  260        -                                  (lander[0] - 0.35, lander[1] + 0.25)]
         288 +                    if i == 0:
         289 +                        send_sites = [(0.43, -1.95), (0.43, -2.15)]
         290 +                    else:
         291 +                        send_sites = [(-1.2, -1.8), (-1.45, -1.65)]
  261    292                      site = send_sites[(self.send_attempts[i] // 2) % len(send_sites)]
  262    293                      if self._dist(positions[i], site) > 0.13:
  263    294                          dx, dy = self._move(i, positions[i], site, positions[1-i])
diff --git a/trace_run.py b/trace_run.py
new file mode 100644
index 0000000..b18825f
--- /dev/null
+++ b/trace_run.py
@@ -0,0 +1,18 @@
           1 +from env_client import make_env
           2 +from approach import GeneratedApproach
           3 +
           4 +env = make_env(); s, info = env.reset(seed=0)
           5 +a = GeneratedApproach(env.action_space, env.observation_space, {})
           6 +a.reset(s, info)
           7 +last = None
           8 +for k in range(250):
           9 +    act = a.get_action(s)
          10 +    s, r, term, trunc, info = env.step(act)
          11 +    rovers = sorted(a._objs(s, "rover"), key=a._name)
          12 +    snap = (tuple(a.phase), tuple((round(a._v(s, x, "x"), 2), round(a._v(s, x, "y"), 2)) for x in rovers))
          13 +    if k % 10 == 0 or tuple(a.phase) != (last[0] if last else None):
          14 +        print(k + 1, snap, [round(float(x), 2) for x in act], [a.stuck[i] for i in range(2)])
          15 +    last = snap
          16 +    if term or trunc:
          17 +        print("END", k + 1, term, trunc); break
          18 +env.close()
```

</details>

<a id="C018"></a>
### C018 · Allocate sample types to reachable arena sides

Commit `71d3423e0dd9d28422bed029015d7d9bae82fcc8`; parents: 738181b2caac73262a5d59e56fae8c5f2c0692a6. Recorded author date: 2026-09-11T11:50:38+02:00.

File roles (automatic): policy.

- [E0039](01_timeline.md#E0039): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C018_71d3423_approach.py) · [Exact all-file diff](evidence/diffs/C018_71d3423.diff)

[Previous saved controller snapshot](evidence/versions/C017_738181b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 9f65e6d..d6fc49a 100644
--- a/approach.py
+++ b/approach.py
@@ -50,12 +50,27 @@ class GeneratedApproach:
   50     50          samples = self._objs(state, "sample")
   51     51          stones = [s for s in samples if self._v(state, s, "is_soil") < 0.5]
   52     52          soils = [s for s in samples if self._v(state, s, "is_soil") > 0.5]
   53        -        right_stones = [s for s in stones if self._v(state, s, "x") >= -0.05]
   54        -        left_soils = [s for s in soils if self._v(state, s, "x") <= 0.05]
   55        -        self.sample_names = {
   56        -            0: self._closest_name(state, right_stones or stones, self.homes[0]),
   57        -            1: self._closest_name(state, left_soils or soils, self.homes[1]),
   58        -        }
          53 +        def feasible(items, idx):
          54 +            # A sample near the wall can be reached from a stance at x=+/-0.43.
          55 +            return [s for s in items if
          56 +                    (self._v(state, s, "x") >= 0.18 if idx == 0
          57 +                     else self._v(state, s, "x") <= -0.18)]
          58 +        choices = []
          59 +        for kinds in ((stones, soils), (soils, stones)):
          60 +            pair = [feasible(kinds[i], i) for i in range(2)]
          61 +            if pair[0] and pair[1]:
          62 +                picked = [min(pair[i], key=lambda s: self._dist(
          63 +                    self._xy(state, s), self.homes[i])) for i in range(2)]
          64 +                score = sum(self._dist(self._xy(state, picked[i]), self.homes[i])
          65 +                            for i in range(2))
          66 +                choices.append((score, picked))
          67 +        if choices:
          68 +            picked = min(choices, key=lambda x: x[0])[1]
          69 +        else:
          70 +            # Defensive fallback for unusual generated layouts.
          71 +            picked = [min(stones, key=lambda s: self._dist(self._xy(state, s), self.homes[0])),
          72 +                      min(soils, key=lambda s: self._dist(self._xy(state, s), self.homes[1]))]
          73 +        self.sample_names = {i: picked[i].name for i in range(2)}
   59     74          self.phase = ["sample", "sample"]
   60     75          self.targets = [None, None]
   61     76          self.paths = [[], []]
@@ -242,7 +257,7 @@ class GeneratedApproach:
  242    257                  if analyzed:
  243    258                      self.phase[i] = "images" if i == 0 else "send"
  244    259                      self.targets[i] = None
  245        -                elif self._dist(positions[i], self._xy(state, sob)) <= 0.235:
         260 +                elif self._dist(positions[i], self._xy(state, sob)) <= 0.2495:
  246    261                      self._set_op(action, i, SAMPLE)
  247    262                      continue
  248    263                  else:
```

</details>

<a id="C019"></a>
### C019 · Enable left rover to image left-side objectives

Commit `2af34144897078d862cb54111e5d4838c0d8151d`; parents: 71d3423e0dd9d28422bed029015d7d9bae82fcc8. Recorded author date: 2026-09-11T11:50:49+02:00.

File roles (automatic): policy.

- [E0043](01_timeline.md#E0043): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_2af3414_approach.py) · [Exact all-file diff](evidence/diffs/C019_2af3414.diff)

[Previous saved controller snapshot](evidence/versions/C018_71d3423_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d6fc49a..387fec2 100644
--- a/approach.py
+++ b/approach.py
@@ -255,7 +255,7 @@ class GeneratedApproach:
  255    255                  sob = self._sample_obj(state, i)
  256    256                  analyzed = sob is None or self._v(state, sob, "analyzed_rover%d" % i) > 0.5
  257    257                  if analyzed:
  258        -                    self.phase[i] = "images" if i == 0 else "send"
         258 +                    self.phase[i] = "images"
  259    259                      self.targets[i] = None
  260    260                  elif self._dist(positions[i], self._xy(state, sob)) <= 0.2495:
  261    261                      self._set_op(action, i, SAMPLE)
```

</details>

<a id="C020"></a>
### C020 · Add measured rover clearance around obstacles

Commit `03b6e5b1831d1c9cf61b9ccebeec4ce64d4c81fd`; parents: 2af34144897078d862cb54111e5d4838c0d8151d. Recorded author date: 2026-09-11T11:51:37+02:00.

File roles (automatic): policy.

- [E0049](01_timeline.md#E0049): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_03b6e5b_approach.py) · [Exact all-file diff](evidence/diffs/C020_03b6e5b.diff)

[Previous saved controller snapshot](evidence/versions/C019_2af3414_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 387fec2..3e4e36d 100644
--- a/approach.py
+++ b/approach.py
@@ -89,7 +89,7 @@ class GeneratedApproach:
   89     89      def _dist(a, b):
   90     90          return math.hypot(a[0] - b[0], a[1] - b[1])
   91     91  
   92        -    def _blocked(self, p, extra=None, margin=0.18):
          92 +    def _blocked(self, p, extra=None, margin=0.22):
   93     93          x, y = p
   94     94          if x < -2.38 or x > 2.38 or y < -2.38 or y > 2.38:
   95     95              return True
```

</details>

<a id="C021"></a>
### C021 · Follow planned segments without componentwise deviation

Commit `6a2200f6db647e8823ffdd7b42168ed1bdbe9b1f`; parents: 03b6e5b1831d1c9cf61b9ccebeec4ce64d4c81fd. Recorded author date: 2026-09-11T11:52:03+02:00.

File roles (automatic): policy.

- [E0053](01_timeline.md#E0053): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C021_6a2200f_approach.py) · [Exact all-file diff](evidence/diffs/C021_6a2200f.diff)

[Previous saved controller snapshot](evidence/versions/C020_03b6e5b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 3e4e36d..352ef5a 100644
--- a/approach.py
+++ b/approach.py
@@ -173,8 +173,11 @@ class GeneratedApproach:
  173    173          while self.paths[idx] and self._dist(pos, self.paths[idx][0]) < 0.075:
  174    174              self.paths[idx].pop(0)
  175    175          waypoint = self.paths[idx][0] if self.paths[idx] else goal
  176        -        dx = max(-0.2, min(0.2, waypoint[0] - pos[0]))
  177        -        dy = max(-0.2, min(0.2, waypoint[1] - pos[1]))
         176 +        vx = waypoint[0] - pos[0]
         177 +        vy = waypoint[1] - pos[1]
         178 +        scale = min(1.0, 0.2 / max(abs(vx), abs(vy), 1e-9))
         179 +        dx = vx * scale
         180 +        dy = vy * scale
  178    181          return dx, dy
  179    182  
  180    183      def _objective_sites(self, state, idx):
```

</details>

<a id="C022"></a>
### C022 · Clamp sample stances inside rover arena boundary

Commit `d0e92ecfcaaa15872d707d8855e222943f78ec7d`; parents: 6a2200f6db647e8823ffdd7b42168ed1bdbe9b1f. Recorded author date: 2026-09-11T11:52:55+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0060](01_timeline.md#E0060): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C022_d0e92ec_approach.py) · [Exact all-file diff](evidence/diffs/C022_d0e92ec.diff)

[Previous saved controller snapshot](evidence/versions/C021_6a2200f_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 352ef5a..dc0aba0 100644
--- a/approach.py
+++ b/approach.py
@@ -230,6 +230,8 @@ class GeneratedApproach:
  230    230              x = 0.43
  231    231          if idx == 1 and x > -0.43:
  232    232              x = -0.43
         233 +        x = max(-2.25, min(2.25, x))
         234 +        y = max(-2.25, min(2.25, y))
  233    235          return (x, y)
  234    236  
  235    237      def _received_own_sample(self, state, idx):
diff --git a/trace_run.py b/trace_run.py
index b18825f..e8780b6 100644
--- a/trace_run.py
+++ b/trace_run.py
@@ -1,7 +1,9 @@
           1 +import sys
    1      2  from env_client import make_env
    2      3  from approach import GeneratedApproach
    3      4  
    4        -env = make_env(); s, info = env.reset(seed=0)
           5 +seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
           6 +env = make_env(); s, info = env.reset(seed=seed)
    5      7  a = GeneratedApproach(env.action_space, env.observation_space, {})
    6      8  a.reset(s, info)
    7      9  last = None
@@ -11,7 +13,7 @@ for k in range(250):
   11     13      rovers = sorted(a._objs(s, "rover"), key=a._name)
   12     14      snap = (tuple(a.phase), tuple((round(a._v(s, x, "x"), 2), round(a._v(s, x, "y"), 2)) for x in rovers))
   13     15      if k % 10 == 0 or tuple(a.phase) != (last[0] if last else None):
   14        -        print(k + 1, snap, [round(float(x), 2) for x in act], [a.stuck[i] for i in range(2)])
          16 +        print(k + 1, snap, [round(float(x), 2) for x in act], [a.stuck[i] for i in range(2)], a.targets)
   15     17      last = snap
   16     18      if term or trunc:
   17     19          print("END", k + 1, term, trunc); break
```

</details>

<a id="C023"></a>
### C023 · Use measured clearance to preserve narrow navigable gaps

Commit `07d9f616c47661d22905a0cbdd52dfd3d8367b85`; parents: d0e92ecfcaaa15872d707d8855e222943f78ec7d. Recorded author date: 2026-09-11T11:53:35+02:00.

File roles (automatic): policy.

- [E0068](01_timeline.md#E0068): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C023_07d9f61_approach.py) · [Exact all-file diff](evidence/diffs/C023_07d9f61.diff)

[Previous saved controller snapshot](evidence/versions/C022_d0e92ec_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index dc0aba0..d792798 100644
--- a/approach.py
+++ b/approach.py
@@ -89,7 +89,7 @@ class GeneratedApproach:
   89     89      def _dist(a, b):
   90     90          return math.hypot(a[0] - b[0], a[1] - b[1])
   91     91  
   92        -    def _blocked(self, p, extra=None, margin=0.22):
          92 +    def _blocked(self, p, extra=None, margin=0.19):
   93     93          x, y = p
   94     94          if x < -2.38 or x > 2.38 or y < -2.38 or y > 2.38:
   95     95              return True
```

</details>

<a id="C024"></a>
### C024 · Refine planning grid for tight pillar passages

Commit `b89302c3a49bddaf005583842196c02392d890ef`; parents: 07d9f616c47661d22905a0cbdd52dfd3d8367b85. Recorded author date: 2026-09-11T11:54:29+02:00.

File roles (automatic): policy.

- [E0078](01_timeline.md#E0078): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C024_b89302c_approach.py) · [Exact all-file diff](evidence/diffs/C024_b89302c.diff)

[Previous saved controller snapshot](evidence/versions/C023_07d9f61_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index d792798..74d3052 100644
--- a/approach.py
+++ b/approach.py
@@ -89,7 +89,7 @@ class GeneratedApproach:
   89     89      def _dist(a, b):
   90     90          return math.hypot(a[0] - b[0], a[1] - b[1])
   91     91  
   92        -    def _blocked(self, p, extra=None, margin=0.19):
          92 +    def _blocked(self, p, extra=None, margin=0.185):
   93     93          x, y = p
   94     94          if x < -2.38 or x > 2.38 or y < -2.38 or y > 2.38:
   95     95              return True
@@ -113,7 +113,7 @@ class GeneratedApproach:
  113    113      def _plan(self, start, goal, extra=None):
  114    114          # A compact 0.1 m grid A*. Endpoints are connected separately so exact
  115    115          # sample and home coordinates remain attainable.
  116        -        res = 0.1
         116 +        res = 0.05
  117    117          lo = -2.4
  118    118          conv = lambda p: (int(round((p[0] - lo) / res)),
  119    119                            int(round((p[1] - lo) / res)))
```

</details>

<a id="C025"></a>
### C025 · Keep planned paths inside physical boundary with safe clearance

Commit `2f8f2a2c38038e41b22227355a18885ce4287c75`; parents: b89302c3a49bddaf005583842196c02392d890ef. Recorded author date: 2026-09-11T11:55:06+02:00.

File roles (automatic): policy.

- [E0084](01_timeline.md#E0084): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C025_2f8f2a2_approach.py) · [Exact all-file diff](evidence/diffs/C025_2f8f2a2.diff)

[Previous saved controller snapshot](evidence/versions/C024_b89302c_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 74d3052..85429ab 100644
--- a/approach.py
+++ b/approach.py
@@ -89,9 +89,9 @@ class GeneratedApproach:
   89     89      def _dist(a, b):
   90     90          return math.hypot(a[0] - b[0], a[1] - b[1])
   91     91  
   92        -    def _blocked(self, p, extra=None, margin=0.185):
          92 +    def _blocked(self, p, extra=None, margin=0.20):
   93     93          x, y = p
   94        -        if x < -2.38 or x > 2.38 or y < -2.38 or y > 2.38:
          94 +        if x < -2.25 or x > 2.25 or y < -2.25 or y > 2.25:
   95     95              return True
   96     96          for ox, oy, hx, hy in self.obstacles:
   97     97              if abs(x - ox) <= hx + margin and abs(y - oy) <= hy + margin:
```

</details>

<a id="C026"></a>
### C026 · Retry narrow routes at measured clearance only when needed

Commit `bc97ce11ef9874ce72993b41681c554824f6542f`; parents: 2f8f2a2c38038e41b22227355a18885ce4287c75. Recorded author date: 2026-09-11T11:56:08+02:00.

File roles (automatic): policy.

- [E0091](01_timeline.md#E0091): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C026_bc97ce1_approach.py) · [Exact all-file diff](evidence/diffs/C026_bc97ce1.diff)

[Previous saved controller snapshot](evidence/versions/C025_2f8f2a2_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 85429ab..b691b77 100644
--- a/approach.py
+++ b/approach.py
@@ -100,17 +100,23 @@ class GeneratedApproach:
  100    100              return True
  101    101          return False
  102    102  
  103        -    def _line_free(self, a, b, extra=None):
         103 +    def _line_free(self, a, b, extra=None, margin=0.20):
  104    104          d = self._dist(a, b)
  105    105          n = max(1, int(d / 0.08))
  106    106          for i in range(1, n + 1):
  107    107              q = (a[0] + (b[0] - a[0]) * i / n,
  108    108                   a[1] + (b[1] - a[1]) * i / n)
  109        -            if self._blocked(q, extra):
         109 +            if self._blocked(q, extra, margin):
  110    110                  return False
  111    111          return True
  112    112  
  113    113      def _plan(self, start, goal, extra=None):
         114 +        route = self._plan_with_margin(start, goal, extra, 0.20)
         115 +        if route is None:
         116 +            route = self._plan_with_margin(start, goal, extra, 0.185)
         117 +        return route if route is not None else [goal]
         118 +
         119 +    def _plan_with_margin(self, start, goal, extra, margin):
  114    120          # A compact 0.1 m grid A*. Endpoints are connected separately so exact
  115    121          # sample and home coordinates remain attainable.
  116    122          res = 0.05
@@ -119,7 +125,7 @@ class GeneratedApproach:
  119    125                            int(round((p[1] - lo) / res)))
  120    126          pos = lambda n: (lo + n[0] * res, lo + n[1] * res)
  121    127          s, g = conv(start), conv(goal)
  122        -        if self._line_free(start, goal, extra):
         128 +        if self._line_free(start, goal, extra, margin):
  123    129              return [goal]
  124    130          frontier = [(0.0, s)]
  125    131          came = {s: None}
@@ -135,7 +141,7 @@ class GeneratedApproach:
  135    141              for dx, dy in moves:
  136    142                  nb = (cur[0] + dx, cur[1] + dy)
  137    143                  q = pos(nb)
  138        -                if self._blocked(q, extra):
         144 +                if self._blocked(q, extra, margin):
  139    145                      continue
  140    146                  nc = cost[cur] + (1.414 if dx and dy else 1.0)
  141    147                  if nc < cost.get(nb, 1e30):
@@ -144,7 +150,7 @@ class GeneratedApproach:
  144    150                      h = math.hypot(nb[0] - g[0], nb[1] - g[1])
  145    151                      heapq.heappush(frontier, (nc + h, nb))
  146    152          if found is None:
  147        -            return [goal]
         153 +            return None
  148    154          rev = []
  149    155          cur = found
  150    156          while cur != s:
@@ -158,7 +164,7 @@ class GeneratedApproach:
  158    164          i = 0
  159    165          while i < len(rev):
  160    166              j = len(rev) - 1
  161        -            while j > i and not self._line_free(anchor, rev[j], extra):
         167 +            while j > i and not self._line_free(anchor, rev[j], extra, margin):
  162    168                  j -= 1
  163    169              route.append(rev[j])
  164    170              anchor = rev[j]
```

</details>

<a id="C027"></a>
### C027 · Add robust camera standoff rings and safer primary routes

Commit `2493a4e36af5a79fb4b0dd51799f2d6aafeb0696`; parents: bc97ce11ef9874ce72993b41681c554824f6542f. Recorded author date: 2026-09-11T11:57:06+02:00.

File roles (automatic): policy.

- [E0099](01_timeline.md#E0099): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C027_2493a4e_approach.py) · [Exact all-file diff](evidence/diffs/C027_2493a4e.diff)

[Previous saved controller snapshot](evidence/versions/C026_bc97ce1_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b691b77..e92dc1c 100644
--- a/approach.py
+++ b/approach.py
@@ -111,9 +111,9 @@ class GeneratedApproach:
  111    111          return True
  112    112  
  113    113      def _plan(self, start, goal, extra=None):
  114        -        route = self._plan_with_margin(start, goal, extra, 0.20)
         114 +        route = self._plan_with_margin(start, goal, extra, 0.21)
  115    115          if route is None:
  116        -            route = self._plan_with_margin(start, goal, extra, 0.185)
         116 +            route = self._plan_with_margin(start, goal, extra, 0.195)
  117    117          return route if route is not None else [goal]
  118    118  
  119    119      def _plan_with_margin(self, start, goal, extra, margin):
@@ -197,10 +197,11 @@ class GeneratedApproach:
  197    197                        (0.707, -0.707), (-0.707, -0.707))
  198    198          for ob in objs:
  199    199              x, y = self._xy(state, ob)
  200        -            for ux, uy in directions:
  201        -                q = (x + 0.62 * ux, y + 0.62 * uy)
  202        -                if not self._blocked(q) and ((q[0] > 0) == (idx == 0)):
  203        -                    sites.append(q)
         200 +            for radius in (0.75, 1.0, 1.3):
         201 +                for ux, uy in directions:
         202 +                    q = (x + radius * ux, y + radius * uy)
         203 +                    if not self._blocked(q) and ((q[0] > 0) == (idx == 0)):
         204 +                        sites.append(q)
  204    205          return sites
  205    206  
  206    207      def _image_done(self, state, ob):
```

</details>

<a id="C028"></a>
### C028 · Support both required sample types on the same rover side

Commit `a914a91f14f1e11973ce740a2ddcf6befb02fa77`; parents: 2493a4e36af5a79fb4b0dd51799f2d6aafeb0696. Recorded author date: 2026-09-11T11:58:17+02:00.

File roles (automatic): policy.

- [E0105](01_timeline.md#E0105): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C028_a914a91_approach.py) · [Exact all-file diff](evidence/diffs/C028_a914a91.diff)

[Previous saved controller snapshot](evidence/versions/C027_2493a4e_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index e92dc1c..7f79f25 100644
--- a/approach.py
+++ b/approach.py
@@ -55,22 +55,21 @@ class GeneratedApproach:
   55     55              return [s for s in items if
   56     56                      (self._v(state, s, "x") >= 0.18 if idx == 0
   57     57                       else self._v(state, s, "x") <= -0.18)]
   58        -        choices = []
   59        -        for kinds in ((stones, soils), (soils, stones)):
   60        -            pair = [feasible(kinds[i], i) for i in range(2)]
   61        -            if pair[0] and pair[1]:
   62        -                picked = [min(pair[i], key=lambda s: self._dist(
   63        -                    self._xy(state, s), self.homes[i])) for i in range(2)]
   64        -                score = sum(self._dist(self._xy(state, picked[i]), self.homes[i])
   65        -                            for i in range(2))
   66        -                choices.append((score, picked))
   67        -        if choices:
   68        -            picked = min(choices, key=lambda x: x[0])[1]
   69        -        else:
   70        -            # Defensive fallback for unusual generated layouts.
   71        -            picked = [min(stones, key=lambda s: self._dist(self._xy(state, s), self.homes[0])),
   72        -                      min(soils, key=lambda s: self._dist(self._xy(state, s), self.homes[1]))]
   73        -        self.sample_names = {i: picked[i].name for i in range(2)}
          58 +        self.sample_queues = [[], []]
          59 +        # Assign each required type independently. Some layouts put both types
          60 +        # on one side, in which case one rover collects two samples sequentially.
          61 +        for items in (stones, soils):
          62 +            options = []
          63 +            for i in range(2):
          64 +                reachable = feasible(items, i)
          65 +                if reachable:
          66 +                    ob = min(reachable, key=lambda s: self._dist(
          67 +                        self._xy(state, s), self.homes[i]))
          68 +                    options.append((self._dist(self._xy(state, ob), self.homes[i]), i, ob))
          69 +            if options:
          70 +                _, owner, ob = min(options, key=lambda x: x[0])
          71 +                self.sample_queues[owner].append(ob.name)
          72 +        self.sample_index = [0, 0]
   74     73          self.phase = ["sample", "sample"]
   75     74          self.targets = [None, None]
   76     75          self.paths = [[], []]
@@ -225,9 +224,9 @@ class GeneratedApproach:
  225    224                     for o in self._objs(state, "objective"))
  226    225  
  227    226      def _sample_obj(self, state, idx):
  228        -        name = self.sample_names[idx]
  229        -        if name is None:
         227 +        if self.sample_index[idx] >= len(self.sample_queues[idx]):
  230    228              return None
         229 +        name = self.sample_queues[idx][self.sample_index[idx]]
  231    230          return state.get_object_from_name(name)
  232    231  
  233    232      @staticmethod
@@ -242,8 +241,9 @@ class GeneratedApproach:
  242    241          return (x, y)
  243    242  
  244    243      def _received_own_sample(self, state, idx):
  245        -        ob = self._sample_obj(state, idx)
  246        -        return ob is None or self._v(state, ob, "received_analysis") > 0.5
         244 +        return all(self._v(state, state.get_object_from_name(name),
         245 +                           "received_analysis") > 0.5
         246 +                   for name in self.sample_queues[idx])
  247    247  
  248    248      def _set_op(self, action, idx, value):
  249    249          action[4 * idx + 3] = value
@@ -267,8 +267,15 @@ class GeneratedApproach:
  267    267                  sob = self._sample_obj(state, i)
  268    268                  analyzed = sob is None or self._v(state, sob, "analyzed_rover%d" % i) > 0.5
  269    269                  if analyzed:
  270        -                    self.phase[i] = "images"
  271        -                    self.targets[i] = None
         270 +                    if full:
         271 +                        self._set_op(action, i, DROP)
         272 +                        continue
         273 +                    if sob is not None:
         274 +                        self.sample_index[i] += 1
         275 +                        self.targets[i] = None
         276 +                    if self._sample_obj(state, i) is None:
         277 +                        self.phase[i] = "images"
         278 +                        self.targets[i] = None
  272    279                  elif self._dist(positions[i], self._xy(state, sob)) <= 0.2495:
  273    280                      self._set_op(action, i, SAMPLE)
  274    281                      continue
```

</details>

<a id="C029"></a>
### C029 · Choose reachable sample stances near boundaries and lander

Commit `b98dc7b4b36ca662b82c6b69f89f65619f90ebc3`; parents: a914a91f14f1e11973ce740a2ddcf6befb02fa77. Recorded author date: 2026-09-11T11:59:00+02:00.

File roles (automatic): policy.

- [E0109](01_timeline.md#E0109): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C029_b98dc7b_approach.py) · [Exact all-file diff](evidence/diffs/C029_b98dc7b.diff)

[Previous saved controller snapshot](evidence/versions/C028_a914a91_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7f79f25..5b31b09 100644
--- a/approach.py
+++ b/approach.py
@@ -47,6 +47,7 @@ class GeneratedApproach:
   47     47          # object list.  Treat it as a full-height divider: all useful tasks have
   48     48          # a reachable stance on their own side.
   49     49          self.obstacles.append((0.0, 0.0, 0.18, 2.6))
          50 +        self.lander_xy = self._xy(state, self._objs(state, "lander")[0])
   50     51          samples = self._objs(state, "sample")
   51     52          stones = [s for s in samples if self._v(state, s, "is_soil") < 0.5]
   52     53          soils = [s for s in samples if self._v(state, s, "is_soil") > 0.5]
@@ -240,6 +241,24 @@ class GeneratedApproach:
  240    241          y = max(-2.25, min(2.25, y))
  241    242          return (x, y)
  242    243  
         244 +    def _sample_goal(self, state, sample, idx, rover_pos):
         245 +        sx, sy = self._xy(state, sample)
         246 +        candidates = []
         247 +        for radius in (0.0, 0.20, 0.24):
         248 +            count = 1 if radius == 0 else 16
         249 +            for k in range(count):
         250 +                angle = 2.0 * math.pi * k / count
         251 +                q = (sx + radius * math.cos(angle),
         252 +                     sy + radius * math.sin(angle))
         253 +                q = self._same_side_goal(q, idx)
         254 +                if self._dist(q, (sx, sy)) <= 0.245 and not self._blocked(q):
         255 +                    # Strongly prefer a stance away from the collidable lander.
         256 +                    lander_penalty = max(0.0, 0.55 - self._dist(q, self.lander_xy)) * 20.0
         257 +                    candidates.append((self._dist(q, rover_pos) + lander_penalty, q))
         258 +        if candidates:
         259 +            return min(candidates, key=lambda x: x[0])[1]
         260 +        return self._same_side_goal((sx, sy), idx)
         261 +
  243    262      def _received_own_sample(self, state, idx):
  244    263          return all(self._v(state, state.get_object_from_name(name),
  245    264                             "received_analysis") > 0.5
@@ -280,7 +299,7 @@ class GeneratedApproach:
  280    299                      self._set_op(action, i, SAMPLE)
  281    300                      continue
  282    301                  else:
  283        -                    goal = self._same_side_goal(self._xy(state, sob), i)
         302 +                    goal = self._sample_goal(state, sob, i, positions[i])
  284    303                      dx, dy = self._move(i, positions[i], goal, positions[1-i])
  285    304                      action[4*i] = dx
  286    305                      action[4*i+1] = dy
```

</details>

<a id="C030"></a>
### C030 · Route around lander and avoid samples trapped beside it

Commit `46c4b3a011a01614675f4d672f7dcc367eeab746`; parents: b98dc7b4b36ca662b82c6b69f89f65619f90ebc3. Recorded author date: 2026-09-11T11:59:30+02:00.

File roles (automatic): policy.

- [E0115](01_timeline.md#E0115): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C030_46c4b3a_approach.py) · [Exact all-file diff](evidence/diffs/C030_46c4b3a.diff)

[Previous saved controller snapshot](evidence/versions/C029_b98dc7b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5b31b09..88884f2 100644
--- a/approach.py
+++ b/approach.py
@@ -48,14 +48,18 @@ class GeneratedApproach:
   48     48          # a reachable stance on their own side.
   49     49          self.obstacles.append((0.0, 0.0, 0.18, 2.6))
   50     50          self.lander_xy = self._xy(state, self._objs(state, "lander")[0])
          51 +        self.obstacles.append((self.lander_xy[0], self.lander_xy[1], 0.30, 0.22))
   51     52          samples = self._objs(state, "sample")
   52     53          stones = [s for s in samples if self._v(state, s, "is_soil") < 0.5]
   53     54          soils = [s for s in samples if self._v(state, s, "is_soil") > 0.5]
   54     55          def feasible(items, idx):
   55     56              # A sample near the wall can be reached from a stance at x=+/-0.43.
   56        -            return [s for s in items if
   57        -                    (self._v(state, s, "x") >= 0.18 if idx == 0
   58        -                     else self._v(state, s, "x") <= -0.18)]
          57 +            result = [s for s in items if
          58 +                      (self._v(state, s, "x") >= 0.18 if idx == 0
          59 +                       else self._v(state, s, "x") <= -0.18)]
          60 +            away = [s for s in result if self._dist(
          61 +                self._xy(state, s), self.lander_xy) > 0.62]
          62 +            return away or result
   59     63          self.sample_queues = [[], []]
   60     64          # Assign each required type independently. Some layouts put both types
   61     65          # on one side, in which case one rover collects two samples sequentially.
```

</details>

<a id="C031"></a>
### C031 · Exclude lander-overlapping samples from assignment

Commit `89fd168ba7553392a2fae44ecdc20ddaa753e3f8`; parents: 46c4b3a011a01614675f4d672f7dcc367eeab746. Recorded author date: 2026-09-11T11:59:43+02:00.

File roles (automatic): policy.

- [E0119](01_timeline.md#E0119): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C031_89fd168_approach.py) · [Exact all-file diff](evidence/diffs/C031_89fd168.diff)

[Previous saved controller snapshot](evidence/versions/C030_46c4b3a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 88884f2..75f15d1 100644
--- a/approach.py
+++ b/approach.py
@@ -59,7 +59,7 @@ class GeneratedApproach:
   59     59                         else self._v(state, s, "x") <= -0.18)]
   60     60              away = [s for s in result if self._dist(
   61     61                  self._xy(state, s), self.lander_xy) > 0.62]
   62        -            return away or result
          62 +            return away
   63     63          self.sample_queues = [[], []]
   64     64          # Assign each required type independently. Some layouts put both types
   65     65          # on one side, in which case one rover collects two samples sequentially.
```

</details>

<a id="C032"></a>
### C032 · Model full lander footprint and inset corner stances

Commit `9ca15aa90f6a6aa64c0120a6f4a662cd23f6e3c6`; parents: 89fd168ba7553392a2fae44ecdc20ddaa753e3f8. Recorded author date: 2026-09-11T12:00:59+02:00.

File roles (automatic): policy.

- [E0129](01_timeline.md#E0129): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C032_9ca15aa_approach.py) · [Exact all-file diff](evidence/diffs/C032_9ca15aa.diff)

[Previous saved controller snapshot](evidence/versions/C031_89fd168_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 75f15d1..6257cf4 100644
--- a/approach.py
+++ b/approach.py
@@ -48,7 +48,7 @@ class GeneratedApproach:
   48     48          # a reachable stance on their own side.
   49     49          self.obstacles.append((0.0, 0.0, 0.18, 2.6))
   50     50          self.lander_xy = self._xy(state, self._objs(state, "lander")[0])
   51        -        self.obstacles.append((self.lander_xy[0], self.lander_xy[1], 0.30, 0.22))
          51 +        self.obstacles.append((self.lander_xy[0], self.lander_xy[1], 0.42, 0.30))
   52     52          samples = self._objs(state, "sample")
   53     53          stones = [s for s in samples if self._v(state, s, "is_soil") < 0.5]
   54     54          soils = [s for s in samples if self._v(state, s, "is_soil") > 0.5]
@@ -95,7 +95,7 @@ class GeneratedApproach:
   95     95  
   96     96      def _blocked(self, p, extra=None, margin=0.20):
   97     97          x, y = p
   98        -        if x < -2.25 or x > 2.25 or y < -2.25 or y > 2.25:
          98 +        if x < -2.22 or x > 2.22 or y < -2.22 or y > 2.22:
   99     99              return True
  100    100          for ox, oy, hx, hy in self.obstacles:
  101    101              if abs(x - ox) <= hx + margin and abs(y - oy) <= hy + margin:
@@ -241,8 +241,8 @@ class GeneratedApproach:
  241    241              x = 0.43
  242    242          if idx == 1 and x > -0.43:
  243    243              x = -0.43
  244        -        x = max(-2.25, min(2.25, x))
  245        -        y = max(-2.25, min(2.25, y))
         244 +        x = max(-2.22, min(2.22, x))
         245 +        y = max(-2.22, min(2.22, y))
  246    246          return (x, y)
  247    247  
  248    248      def _sample_goal(self, state, sample, idx, rover_pos):
```

</details>

<a id="C033"></a>
### C033 · Avoid unreachable samples in rounded arena corners

Commit `99046102fbbd4189667cd3446db32918856db38d`; parents: 9ca15aa90f6a6aa64c0120a6f4a662cd23f6e3c6. Recorded author date: 2026-09-11T12:01:49+02:00.

File roles (automatic): policy.

- [E0139](01_timeline.md#E0139): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C033_9904610_approach.py) · [Exact all-file diff](evidence/diffs/C033_9904610.diff)

[Previous saved controller snapshot](evidence/versions/C032_9ca15aa_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6257cf4..47f00df 100644
--- a/approach.py
+++ b/approach.py
@@ -59,7 +59,13 @@ class GeneratedApproach:
   59     59                         else self._v(state, s, "x") <= -0.18)]
   60     60              away = [s for s in result if self._dist(
   61     61                  self._xy(state, s), self.lander_xy) > 0.62]
   62        -            return away
          62 +            result = away or result
          63 +            # The tray's rounded corners can make extreme corner samples
          64 +            # unreachable even though their coordinates lie inside the square.
          65 +            noncorner = [s for s in result if not (
          66 +                abs(self._v(state, s, "x")) > 1.9 and
          67 +                abs(self._v(state, s, "y")) > 1.9)]
          68 +            return noncorner or result
   63     69          self.sample_queues = [[], []]
   64     70          # Assign each required type independently. Some layouts put both types
   65     71          # on one side, in which case one rover collects two samples sequentially.
```

</details>

<a id="C034"></a>
### C034 · Penalize sample assignments obstructed by the lander

Commit `a732c2ac277125c06315ab9575081404a90846fc`; parents: 99046102fbbd4189667cd3446db32918856db38d. Recorded author date: 2026-09-11T12:02:40+02:00.

File roles (automatic): policy.

- [E0145](01_timeline.md#E0145): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C034_a732c2a_approach.py) · [Exact all-file diff](evidence/diffs/C034_a732c2a.diff)

[Previous saved controller snapshot](evidence/versions/C033_9904610_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 47f00df..c2627c9 100644
--- a/approach.py
+++ b/approach.py
@@ -74,9 +74,13 @@ class GeneratedApproach:
   74     74              for i in range(2):
   75     75                  reachable = feasible(items, i)
   76     76                  if reachable:
   77        -                    ob = min(reachable, key=lambda s: self._dist(
   78        -                        self._xy(state, s), self.homes[i]))
   79        -                    options.append((self._dist(self._xy(state, ob), self.homes[i]), i, ob))
          77 +                    def sample_cost(s):
          78 +                        travel = self._dist(self._xy(state, s), self.homes[i])
          79 +                        near_lander = max(0.0, 0.70 - self._dist(
          80 +                            self._xy(state, s), self.lander_xy)) * 20.0
          81 +                        return travel + near_lander
          82 +                    ob = min(reachable, key=sample_cost)
          83 +                    options.append((sample_cost(ob), i, ob))
   80     84              if options:
   81     85                  _, owner, ob = min(options, key=lambda x: x[0])
   82     86                  self.sample_queues[owner].append(ob.name)
```

</details>

<a id="C035"></a>
### C035 · Add bounded adversarial seed search harness

Commit `85d529c1265dda8a2d0388a642e3a0044710da64`; parents: a732c2ac277125c06315ab9575081404a90846fc. Recorded author date: 2026-09-11T12:03:27+02:00.

File roles (automatic): support code (role needs review).

- [E0157](01_timeline.md#E0157): commit hash in recorded output.
[Exact all-file diff](evidence/diffs/C035_85d529c.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/search_failures.py b/search_failures.py
new file mode 100644
index 0000000..baef26c
--- /dev/null
+++ b/search_failures.py
@@ -0,0 +1,21 @@
           1 +import sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +
           5 +start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
           6 +stop = int(sys.argv[2]) if len(sys.argv) > 2 else start + 50
           7 +fail = []
           8 +for seed in range(start, stop):
           9 +    env = make_env(); state, info = env.reset(seed=seed)
          10 +    app = GeneratedApproach(env.action_space, env.observation_space, {})
          11 +    app.reset(state, info)
          12 +    done = False
          13 +    for step in range(180):
          14 +        state, _, done, trunc, _ = env.step(app.get_action(state))
          15 +        if done or trunc:
          16 +            break
          17 +    env.close()
          18 +    if not done:
          19 +        fail.append((seed, app.phase, step + 1))
          20 +        print("FAIL", fail[-1], flush=True)
          21 +print("RESULT", start, stop, "failures", fail, flush=True)
```

</details>

<a id="C036"></a>
### C036 · Use conservative sampling distance away from forced edge stances

Commit `83e4d78886a50cd1b4438ef6780667fbbd7c8d1b`; parents: 85d529c1265dda8a2d0388a642e3a0044710da64. Recorded author date: 2026-09-11T12:04:50+02:00.

File roles (automatic): policy.

- [E0172](01_timeline.md#E0172): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C036_83e4d78_approach.py) · [Exact all-file diff](evidence/diffs/C036_83e4d78.diff)

[Previous saved controller snapshot](evidence/versions/C034_a732c2a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c2627c9..ceefa4a 100644
--- a/approach.py
+++ b/approach.py
@@ -258,7 +258,10 @@ class GeneratedApproach:
  258    258      def _sample_goal(self, state, sample, idx, rover_pos):
  259    259          sx, sy = self._xy(state, sample)
  260    260          candidates = []
  261        -        for radius in (0.0, 0.20, 0.24):
         261 +        edge_needed = (abs(sx) < 0.43 or abs(sx) > 2.22 or
         262 +                       abs(sy) > 2.22 or self._blocked((sx, sy)))
         263 +        radii = (0.0, 0.18, 0.24) if edge_needed else (0.0, 0.18)
         264 +        for radius in radii:
  262    265              count = 1 if radius == 0 else 16
  263    266              for k in range(count):
  264    267                  angle = 2.0 * math.pi * k / count
```

</details>

<a id="C037"></a>
### C037 · Increase modeled vertical lander collision clearance

Commit `4a7e3f9a3afcc929b91f4ecadba26226c9f8bd67`; parents: 83e4d78886a50cd1b4438ef6780667fbbd7c8d1b. Recorded author date: 2026-09-11T12:05:45+02:00.

File roles (automatic): policy.

- [E0184](01_timeline.md#E0184): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C037_4a7e3f9_approach.py) · [Exact all-file diff](evidence/diffs/C037_4a7e3f9.diff)

[Previous saved controller snapshot](evidence/versions/C036_83e4d78_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ceefa4a..0009fb0 100644
--- a/approach.py
+++ b/approach.py
@@ -48,7 +48,7 @@ class GeneratedApproach:
   48     48          # a reachable stance on their own side.
   49     49          self.obstacles.append((0.0, 0.0, 0.18, 2.6))
   50     50          self.lander_xy = self._xy(state, self._objs(state, "lander")[0])
   51        -        self.obstacles.append((self.lander_xy[0], self.lander_xy[1], 0.42, 0.30))
          51 +        self.obstacles.append((self.lander_xy[0], self.lander_xy[1], 0.42, 0.36))
   52     52          samples = self._objs(state, "sample")
   53     53          stones = [s for s in samples if self._v(state, s, "is_soil") < 0.5]
   54     54          soils = [s for s in samples if self._v(state, s, "is_soil") > 0.5]
```

</details>

<a id="C038"></a>
### C038 · Recover when overlapping samples are analyzed out of queue order

Commit `af51a502752fe0ffa536654fee0f02fe0ab7c251`; parents: 4a7e3f9a3afcc929b91f4ecadba26226c9f8bd67. Recorded author date: 2026-09-11T12:07:54+02:00.

File roles (automatic): policy.

- [E0208](01_timeline.md#E0208): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C038_af51a50_approach.py) · [Exact all-file diff](evidence/diffs/C038_af51a50.diff)

[Previous saved controller snapshot](evidence/versions/C037_4a7e3f9_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 0009fb0..b5aa980 100644
--- a/approach.py
+++ b/approach.py
@@ -301,11 +301,13 @@ class GeneratedApproach:
  301    301  
  302    302              if self.phase[i] == "sample":
  303    303                  sob = self._sample_obj(state, i)
         304 +                # Sampling selects a nearby sample internally. If two samples
         305 +                # overlap, it may validly analyze the other queued type first.
         306 +                if full:
         307 +                    self._set_op(action, i, DROP)
         308 +                    continue
  304    309                  analyzed = sob is None or self._v(state, sob, "analyzed_rover%d" % i) > 0.5
  305    310                  if analyzed:
  306        -                    if full:
  307        -                        self._set_op(action, i, DROP)
  308        -                        continue
  309    311                      if sob is not None:
  310    312                          self.sample_index[i] += 1
  311    313                          self.targets[i] = None
```

</details>

<a id="C039"></a>
### C039 · Choose sample stances that disambiguate overlapping samples

Commit `16487520898b534efd5c39bbfb970516a3e36ce0`; parents: af51a502752fe0ffa536654fee0f02fe0ab7c251. Recorded author date: 2026-09-11T12:08:36+02:00.

File roles (automatic): policy.

- [E0218](01_timeline.md#E0218): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C039_1648752_approach.py) · [Exact all-file diff](evidence/diffs/C039_1648752.diff)

[Previous saved controller snapshot](evidence/versions/C038_af51a50_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index b5aa980..4b79729 100644
--- a/approach.py
+++ b/approach.py
@@ -271,7 +271,15 @@ class GeneratedApproach:
  271    271                  if self._dist(q, (sx, sy)) <= 0.245 and not self._blocked(q):
  272    272                      # Strongly prefer a stance away from the collidable lander.
  273    273                      lander_penalty = max(0.0, 0.55 - self._dist(q, self.lander_xy)) * 20.0
  274        -                    candidates.append((self._dist(q, rover_pos) + lander_penalty, q))
         274 +                    target_d = self._dist(q, (sx, sy))
         275 +                    conflict = 0.0
         276 +                    for other in self._objs(state, "sample"):
         277 +                        if other.name != sample.name:
         278 +                            od = self._dist(q, self._xy(state, other))
         279 +                            if od < 0.27 or od <= target_d + 0.02:
         280 +                                conflict += 10.0
         281 +                    candidates.append((self._dist(q, rover_pos) +
         282 +                                       lander_penalty + conflict, q))
  275    283          if candidates:
  276    284              return min(candidates, key=lambda x: x[0])[1]
  277    285          return self._same_side_goal((sx, sy), idx)
```

</details>

<a id="C040"></a>
### C040 · Add variable-object-count validation harness

Commit `21f9614b103025f26fe6f5df1fffec27797a8867`; parents: 16487520898b534efd5c39bbfb970516a3e36ce0. Recorded author date: 2026-09-11T12:10:03+02:00.

File roles (automatic): diagnostic/test.

- [E0236](01_timeline.md#E0236): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C040_21f9614.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_counts.py b/test_counts.py
new file mode 100644
index 0000000..8983a66
--- /dev/null
+++ b/test_counts.py
@@ -0,0 +1,22 @@
           1 +import sys
           2 +from env_client import make_env
           3 +from approach import GeneratedApproach
           4 +
           5 +start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
           6 +stop = int(sys.argv[2]) if len(sys.argv) > 2 else 5
           7 +for count in (1, 2, 3, 4):
           8 +    for seed in range(start, stop):
           9 +        env = make_env()
          10 +        try:
          11 +            state, info = env.reset(seed=seed, options={"object_count": count})
          12 +        except TypeError as exc:
          13 +            print("options unsupported", exc); env.close(); raise SystemExit
          14 +        app = GeneratedApproach(env.action_space, env.observation_space, {})
          15 +        app.reset(state, info)
          16 +        done = False
          17 +        for step in range(180):
          18 +            state, _, done, trunc, _ = env.step(app.get_action(state))
          19 +            if done or trunc:
          20 +                break
          21 +        print(count, seed, done, step + 1, app.phase, flush=True)
          22 +        env.close()
```

</details>

<a id="C041"></a>
### C041 · Optimize diagonal routes and sample on arrival

Commit `4e995ed7e8337a6d511e0baf46be7e87b888af8a`; parents: 21f9614b103025f26fe6f5df1fffec27797a8867. Recorded author date: 2026-09-11T12:12:22+02:00.

File roles (automatic): policy.

- [E0254](01_timeline.md#E0254): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C041_4e995ed_approach.py) · [Exact all-file diff](evidence/diffs/C041_4e995ed.diff)

[Previous saved controller snapshot](evidence/versions/C039_1648752_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 4b79729..8ac05b7 100644
--- a/approach.py
+++ b/approach.py
@@ -157,11 +157,12 @@ class GeneratedApproach:
  157    157                  q = pos(nb)
  158    158                  if self._blocked(q, extra, margin):
  159    159                      continue
  160        -                nc = cost[cur] + (1.414 if dx and dy else 1.0)
         160 +                # Diagonal and axial commands both consume one environment step.
         161 +                nc = cost[cur] + 1.0
  161    162                  if nc < cost.get(nb, 1e30):
  162    163                      cost[nb] = nc
  163    164                      came[nb] = cur
  164        -                    h = math.hypot(nb[0] - g[0], nb[1] - g[1])
         165 +                    h = max(abs(nb[0] - g[0]), abs(nb[1] - g[1]))
  165    166                      heapq.heappush(frontier, (nc + h, nb))
  166    167          if found is None:
  167    168              return None
@@ -330,6 +331,9 @@ class GeneratedApproach:
  330    331                      dx, dy = self._move(i, positions[i], goal, positions[1-i])
  331    332                      action[4*i] = dx
  332    333                      action[4*i+1] = dy
         334 +                    if self._dist((positions[i][0] + dx, positions[i][1] + dy),
         335 +                                  self._xy(state, sob)) <= 0.22:
         336 +                        self._set_op(action, i, SAMPLE)
  333    337                      continue
  334    338  
  335    339              if self.phase[i] == "images":
```

</details>

<a id="C042"></a>
### C042 · Restore shorter geometric paths after rollout regression

Commit `0d4421dafd8406cfbcb682dd9280daac0b4233b8`; parents: 4e995ed7e8337a6d511e0baf46be7e87b888af8a. Recorded author date: 2026-09-11T12:12:42+02:00.

File roles (automatic): policy.

- [E0258](01_timeline.md#E0258): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C042_0d4421d_approach.py) · [Exact all-file diff](evidence/diffs/C042_0d4421d.diff)

[Previous saved controller snapshot](evidence/versions/C041_4e995ed_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8ac05b7..693aebc 100644
--- a/approach.py
+++ b/approach.py
@@ -157,12 +157,11 @@ class GeneratedApproach:
  157    157                  q = pos(nb)
  158    158                  if self._blocked(q, extra, margin):
  159    159                      continue
  160        -                # Diagonal and axial commands both consume one environment step.
  161        -                nc = cost[cur] + 1.0
         160 +                nc = cost[cur] + (1.414 if dx and dy else 1.0)
  162    161                  if nc < cost.get(nb, 1e30):
  163    162                      cost[nb] = nc
  164    163                      came[nb] = cur
  165        -                    h = max(abs(nb[0] - g[0]), abs(nb[1] - g[1]))
         164 +                    h = math.hypot(nb[0] - g[0], nb[1] - g[1])
  166    165                      heapq.heappush(frontier, (nc + h, nb))
  167    166          if found is None:
  168    167              return None
```

</details>

