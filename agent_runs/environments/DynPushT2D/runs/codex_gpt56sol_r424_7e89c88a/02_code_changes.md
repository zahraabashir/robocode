# DynPushT2D · gpt-5.6-sol · replicate 424: commits and changed lines

[Timeline](01_timeline.md) · [Findings and your notes](03_findings.md) · [Final controller](evidence/final/approach.py)

Every saved commit in HEAD ancestry is included, including setup, test changes and reverts. C identifiers count all commits; older R aliases count Obstruction2D policy revisions only. Commit order is Git ancestry order; concurrent tool activity must be read in the timeline.

Titles are the agent’s original commit messages unless an explicitly marked prior analyst description is supplied. A commit title can overstate what changed. Exact all-file diffs follow below with OLD/NEW line numbers. These are saved commit differences, not a promise that every intermediate uncommitted edit is recoverable.

| Commit | Original title | Files/roles | Linked events |
| --- | --- | --- | --- | --- |
| [C001](#C001) · `21d9203` | initial sandbox setup | .gitignore, AGENTS.md, env_client.py, env_spaces.json | No matched commit command/output |
| [C002](#C002) · `2a27e4a` | Add valid reactive pushing baseline and test harness | approach.py, test_approach.py | [E0009](01_timeline.md#E0009) |
| [C003](#C003) · `36fdbe5` | add isolated rotation dynamics probe | probe_rotation_agent.py | No matched commit command/output |
| [C004](#C004) · `edd2c7d` | Keep actions strictly inside server bounds | approach.py | [E0023](01_timeline.md#E0023) |
| [C005](#C005) · `96b4b43` | Add numerical seed survey for policy failures | seed_survey.py | No matched commit command/output |
| [C006](#C006) · `f836fb9` | Add isolated black-box geometry probe | probe_geometry.py | No matched commit command/output |
| [C007](#C007) · `ad9d002` | probe T-block contact offsets and induced rotation | probe_rotation_agent.py | No matched commit command/output |
| [C008](#C008) · `ed75869` | use action-space dtype in rotation probe | probe_rotation_agent.py | No matched commit command/output |
| [C009](#C009) · `dde97e4` | stay within strict action bounds in probe | probe_rotation_agent.py | No matched commit command/output |
| [C010](#C010) · `f0d4d6a` | Probe uncontaminated radial contacts from reset poses | probe_geometry.py | No matched commit command/output |
| [C011](#C011) · `a766629` | measure short offset pushes for controlled rotation | probe_rotation_agent.py | No matched commit command/output |
| [C012](#C012) · `359ffb7` | Add capped flushed rollouts for efficient policy iteration | test_approach.py | [E0034](01_timeline.md#E0034) |
| [C013](#C013) · `0968980` | validate rotation contacts in arbitrary block frames | probe_rotation_agent.py | No matched commit command/output |
| [C014](#C014) · `40a0345` | Drive through block center to ensure contact and translation | approach.py | [E0038](01_timeline.md#E0038) |
| [C015](#C015) · `9e1edf7` | test paired torque pushes for translation cancellation | probe_rotation_agent.py | No matched commit command/output |
| [C016](#C016) · `ab58679` | Measure sustained push response after clean contact | approach.py, probe_geometry.py | No matched commit command/output |
| [C017](#C017) · `b17244a` | verify mirrored low-translation rotation pair | probe_rotation_agent.py | No matched commit command/output |
| [C018](#C018) · `2fc7f82` | Implement geometry-aware rotation and centerline translation planner | approach.py | [E0049](01_timeline.md#E0049) |
| [C019](#C019) · `cc1fc8a` | Use accessible center-of-mass rays for faster direct translation | approach.py | [E0059](01_timeline.md#E0059) |
| [C020](#C020) · `0b98261` | Accelerate manipulation and handle angle branch-cut termination | approach.py | [E0065](01_timeline.md#E0065) |
| [C021](#C021) · `cf6854b` | Use diagonal routing and defer orientation cleanup during translation | approach.py | [E0071](01_timeline.md#E0071) |
| [C022](#C022) · `7d6d4ed` | Recover navigation from wall-limited waypoints | approach.py | [E0081](01_timeline.md#E0081) |
| [C023](#C023) · `a3e7cd5` | Preposition long blocks for wall-safe rotation | approach.py | [E0086](01_timeline.md#E0086) |
| [C024](#C024) · `9633667` | Allow small final orientation corrections at valid goal poses | approach.py | [E0092](01_timeline.md#E0092) |

## Change details

<a id="C001"></a>
### C001 · initial sandbox setup

Commit `21d9203d61e751ee157ffd4c7c8d169d3f27dd15`; parents: none (initial snapshot). Recorded author date: 2026-09-09T08:24:02+02:00.

File roles (automatic): setup/other.

[Exact all-file diff](evidence/diffs/C001_21d9203.diff)

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
index 0000000..b034ec3
--- /dev/null
+++ b/AGENTS.md
@@ -0,0 +1,13 @@
           1 +You are an expert at writing policies for gymnasium environments. The environment is a black box: its source code is not available, so you will discover the dynamics, reward structure, and termination conditions empirically by interacting with a live environment instance, and write an optimal approach class. Your program must generalize to any instance of this environment (any env.reset()). At evaluation time your program is given 60 seconds of wall-clock per instance; if it exceeds this budget it is stopped and the instance is scored as a failure, so it must select actions efficiently rather than rely on exhaustive search or slow planners. IMPORTANT: You MUST write ALL files (approach.py, test scripts, etc.) to the current working directory using RELATIVE paths only. Never use absolute paths when writing files. IMPORTANT: Write code often to approach.py as you iterate. You may be interrupted at any time, so you should make sure that approach.py is your best current attempt at all times. VERSION CONTROL: This directory is a git repo. After each meaningful change to approach.py or supporting modules, run `git add -A && git commit -m '<describe what you changed and why>'`. Commit often, do not batch everything into one final commit. You should commit the approach every time before you test it in the environment. Use subagents to run exploration experiments in parallel, e.g. spawn subagents to probe action effects, reward structure, and termination conditions simultaneously rather than sequentially; each test script gets its own fresh environment instance. IMPORTANT: You have visual debugging tools (render_state, render_policy). You can render initial states by seed and existing observations by passing obs.tolist() to render_state's `state` parameter. Raw state snapshots, devectorize/vectorize, and named feature metadata are unavailable. CRITICAL: MCP tools are only available to YOU directly, they CANNOT be called from inside subagents. Always call MCP tools yourself, then delegate image reading to a subagent.
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
index 0000000..cf3b299
--- /dev/null
+++ b/env_spaces.json
@@ -0,0 +1,124 @@
           1 +{
           2 +  "host": "127.0.0.1",
           3 +  "port": 40119,
           4 +  "token": "627591feddf0f977489546f317828753",
           5 +  "observation_space": {
           6 +    "type": "Box",
           7 +    "shape": [
           8 +      45
           9 +    ],
          10 +    "low": [
          11 +      -Infinity,
          12 +      -Infinity,
          13 +      -Infinity,
          14 +      -Infinity,
          15 +      -Infinity,
          16 +      -Infinity,
          17 +      -Infinity,
          18 +      -Infinity,
          19 +      -Infinity,
          20 +      -Infinity,
          21 +      -Infinity,
          22 +      -Infinity,
          23 +      -Infinity,
          24 +      -Infinity,
          25 +      -Infinity,
          26 +      -Infinity,
          27 +      -Infinity,
          28 +      -Infinity,
          29 +      -Infinity,
          30 +      -Infinity,
          31 +      -Infinity,
          32 +      -Infinity,
          33 +      -Infinity,
          34 +      -Infinity,
          35 +      -Infinity,
          36 +      -Infinity,
          37 +      -Infinity,
          38 +      -Infinity,
          39 +      -Infinity,
          40 +      -Infinity,
          41 +      -Infinity,
          42 +      -Infinity,
          43 +      -Infinity,
          44 +      -Infinity,
          45 +      -Infinity,
          46 +      -Infinity,
          47 +      -Infinity,
          48 +      -Infinity,
          49 +      -Infinity,
          50 +      -Infinity,
          51 +      -Infinity,
          52 +      -Infinity,
          53 +      -Infinity,
          54 +      -Infinity,
          55 +      -Infinity
          56 +    ],
          57 +    "high": [
          58 +      Infinity,
          59 +      Infinity,
          60 +      Infinity,
          61 +      Infinity,
          62 +      Infinity,
          63 +      Infinity,
          64 +      Infinity,
          65 +      Infinity,
          66 +      Infinity,
          67 +      Infinity,
          68 +      Infinity,
          69 +      Infinity,
          70 +      Infinity,
          71 +      Infinity,
          72 +      Infinity,
          73 +      Infinity,
          74 +      Infinity,
          75 +      Infinity,
          76 +      Infinity,
          77 +      Infinity,
          78 +      Infinity,
          79 +      Infinity,
          80 +      Infinity,
          81 +      Infinity,
          82 +      Infinity,
          83 +      Infinity,
          84 +      Infinity,
          85 +      Infinity,
          86 +      Infinity,
          87 +      Infinity,
          88 +      Infinity,
          89 +      Infinity,
          90 +      Infinity,
          91 +      Infinity,
          92 +      Infinity,
          93 +      Infinity,
          94 +      Infinity,
          95 +      Infinity,
          96 +      Infinity,
          97 +      Infinity,
          98 +      Infinity,
          99 +      Infinity,
         100 +      Infinity,
         101 +      Infinity,
         102 +      Infinity
         103 +    ],
         104 +    "dtype": "float64"
         105 +  },
         106 +  "action_space": {
         107 +    "type": "Box",
         108 +    "shape": [
         109 +      2
         110 +    ],
         111 +    "low": [
         112 +      -0.05,
         113 +      -0.05
         114 +    ],
         115 +    "high": [
         116 +      0.05,
         117 +      0.05
         118 +    ],
         119 +    "dtype": "float64"
         120 +  },
         121 +  "max_steps": 1000,
         122 +  "primitives": [],
         123 +  "strict": true
         124 +}
\ No newline at end of file
```

</details>

<a id="C002"></a>
### C002 · Add valid reactive pushing baseline and test harness

Commit `2a27e4afcf52ffe998c168533d677badf0a11666`; parents: 21d9203d61e751ee157ffd4c7c8d169d3f27dd15. Recorded author date: 2026-09-09T08:24:56+02:00.

File roles (automatic): diagnostic/test, policy.

- [E0009](01_timeline.md#E0009): commit hash in recorded output.
[Controller after this commit](evidence/versions/C002_2a27e4a_approach.py) · [Exact all-file diff](evidence/diffs/C002_2a27e4a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
new file mode 100644
index 0000000..7b387f0
--- /dev/null
+++ b/approach.py
@@ -0,0 +1,32 @@
           1 +import math
           2 +import numpy as np
           3 +
           4 +
           5 +class GeneratedApproach:
           6 +    """Fast reactive baseline: get behind the block and push its centre to goal."""
           7 +
           8 +    def __init__(self, action_space, observation_space, primitives):
           9 +        self.low = np.asarray(action_space.low, dtype=float)
          10 +        self.high = np.asarray(action_space.high, dtype=float)
          11 +        self.step = 0
          12 +
          13 +    def reset(self, state, info):
          14 +        self.step = 0
          15 +
          16 +    def get_action(self, state):
          17 +        s = np.asarray(state, dtype=float)
          18 +        block = s[0:2]
          19 +        robot = s[16:18]
          20 +        goal = s[29:31]
          21 +        delta = goal - block
          22 +        distance = float(np.linalg.norm(delta))
          23 +        if distance < 1e-9:
          24 +            direction = np.array([1.0, 0.0])
          25 +        else:
          26 +            direction = delta / distance
          27 +        # Conservative clearance for the initial positioning phase.
          28 +        staging = block - direction * 0.13
          29 +        target = staging if np.linalg.norm(robot - staging) > 0.035 else block + direction * 0.08
          30 +        move = np.clip(target - robot, self.low, self.high)
          31 +        self.step += 1
          32 +        return move.astype(float)
diff --git a/test_approach.py b/test_approach.py
new file mode 100644
index 0000000..d107f07
--- /dev/null
+++ b/test_approach.py
@@ -0,0 +1,32 @@
           1 +import argparse
           2 +import numpy as np
           3 +from env_client import make_env
           4 +from approach import GeneratedApproach
           5 +
           6 +
           7 +def run(seed, verbose=False):
           8 +    env = make_env()
           9 +    obs, info = env.reset(seed=seed)
          10 +    policy = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
          11 +    policy.reset(obs, info)
          12 +    initial = obs.copy()
          13 +    terminated = truncated = False
          14 +    steps = 0
          15 +    while not (terminated or truncated):
          16 +        obs, reward, terminated, truncated, info = env.step(policy.get_action(obs))
          17 +        steps += 1
          18 +    poserr = float(np.linalg.norm(obs[:2] - obs[29:31]))
          19 +    angerr = abs(float((obs[2] - obs[31] + np.pi) % (2*np.pi) - np.pi))
          20 +    env.close()
          21 +    if verbose:
          22 +        print(seed, terminated, steps, "init", np.round(initial[[0,1,2,16,17,29,30,31]],3),
          23 +              "finalerr", round(poserr,3), round(angerr,3))
          24 +    return terminated, steps, poserr, angerr
          25 +
          26 +
          27 +if __name__ == "__main__":
          28 +    ap = argparse.ArgumentParser()
          29 +    ap.add_argument("seeds", nargs="*", type=int, default=list(range(10)))
          30 +    args = ap.parse_args()
          31 +    results = [run(seed, True) for seed in args.seeds]
          32 +    print("success", sum(x[0] for x in results), "/", len(results))
```

</details>

<a id="C003"></a>
### C003 · add isolated rotation dynamics probe

Commit `36fdbe55fbf17af71106da9d5c3f0b59b9262fad`; parents: 2a27e4afcf52ffe998c168533d677badf0a11666. Recorded author date: 2026-09-09T08:25:35+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C003_36fdbe5.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_rotation_agent.py b/probe_rotation_agent.py
new file mode 100644
index 0000000..989dd88
--- /dev/null
+++ b/probe_rotation_agent.py
@@ -0,0 +1,30 @@
           1 +"""Independent black-box rotation probes for DynPushT2D (not policy code)."""
           2 +import math
           3 +import numpy as np
           4 +
           5 +from env_client import make_env
           6 +
           7 +
           8 +def wrap(x):
           9 +    return (x + math.pi) % (2 * math.pi) - math.pi
          10 +
          11 +
          12 +def summarize(seed):
          13 +    env = make_env()
          14 +    s, _ = env.reset(seed=seed)
          15 +    print("RESET", seed,
          16 +          "block", np.round(s[[0, 1, 2]], 4),
          17 +          "robot", np.round(s[[16, 17]], 4),
          18 +          "goal", np.round(s[[29, 30, 31]], 4),
          19 +          "dims", np.round(s[[12, 13, 14, 28]], 4),
          20 +          "err", round(wrap(float(s[31] - s[2])), 4))
          21 +    env.close()
          22 +
          23 +
          24 +def main():
          25 +    for seed in range(12):
          26 +        summarize(seed)
          27 +
          28 +
          29 +if __name__ == "__main__":
          30 +    main()
```

</details>

<a id="C004"></a>
### C004 · Keep actions strictly inside server bounds

Commit `edd2c7d44029e4a07bb664fa166bf2c0ace128f9`; parents: 36fdbe55fbf17af71106da9d5c3f0b59b9262fad. Recorded author date: 2026-09-09T08:25:51+02:00.

File roles (automatic): policy.

- [E0023](01_timeline.md#E0023): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C004_edd2c7d_approach.py) · [Exact all-file diff](evidence/diffs/C004_edd2c7d.diff)

[Previous saved controller snapshot](evidence/versions/C002_2a27e4a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 7b387f0..8e52236 100644
--- a/approach.py
+++ b/approach.py
@@ -27,6 +27,7 @@ class GeneratedApproach:
   27     27          # Conservative clearance for the initial positioning phase.
   28     28          staging = block - direction * 0.13
   29     29          target = staging if np.linalg.norm(robot - staging) > 0.035 else block + direction * 0.08
   30        -        move = np.clip(target - robot, self.low, self.high)
          30 +        # The server checks the open interval despite the advertised Box bounds.
          31 +        move = np.clip(target - robot, self.low + 1e-6, self.high - 1e-6)
   31     32          self.step += 1
   32     33          return move.astype(float)
```

</details>

<a id="C005"></a>
### C005 · Add numerical seed survey for policy failures

Commit `96b4b4393638dee6042cc1bc0b099b363965ef1c`; parents: edd2c7d44029e4a07bb664fa166bf2c0ace128f9. Recorded author date: 2026-09-09T08:26:23+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C005_96b4b43.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/seed_survey.py b/seed_survey.py
new file mode 100644
index 0000000..82634b7
--- /dev/null
+++ b/seed_survey.py
@@ -0,0 +1,100 @@
           1 +"""Numerical seed survey for the current approach (kept separate from evaluation)."""
           2 +
           3 +import argparse
           4 +import math
           5 +
           6 +import numpy as np
           7 +
           8 +from approach import GeneratedApproach
           9 +from env_client import make_env
          10 +
          11 +
          12 +def angle_error(a, b):
          13 +    return abs((a - b + math.pi) % (2 * math.pi) - math.pi)
          14 +
          15 +
          16 +def run_seed(seed, cap=None):
          17 +    env = make_env()
          18 +    obs, info = env.reset(seed=seed)
          19 +    policy = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
          20 +    policy.reset(obs, info)
          21 +    initial = obs.copy()
          22 +    max_steps = min(env.max_steps, cap) if cap else env.max_steps
          23 +    min_pos = float("inf")
          24 +    min_ang = float("inf")
          25 +    min_joint = float("inf")
          26 +    max_displacement = 0.0
          27 +    max_rotation = 0.0
          28 +    first_motion = None
          29 +    block0 = initial[:2].copy()
          30 +    theta0 = float(initial[2])
          31 +    terminated = truncated = False
          32 +    for step in range(1, max_steps + 1):
          33 +        action = policy.get_action(obs)
          34 +        obs, reward, terminated, truncated, info = env.step(action)
          35 +        pe = float(np.linalg.norm(obs[:2] - obs[29:31]))
          36 +        ae = angle_error(float(obs[2]), float(obs[31]))
          37 +        min_pos = min(min_pos, pe)
          38 +        min_ang = min(min_ang, ae)
          39 +        # Unitless score where <1 in all termination dimensions approximately succeeds.
          40 +        joint = max(abs(float(obs[0] - obs[29])) / 0.03,
          41 +                    abs(float(obs[1] - obs[30])) / 0.03,
          42 +                    ae / math.radians(8))
          43 +        min_joint = min(min_joint, joint)
          44 +        displacement = float(np.linalg.norm(obs[:2] - block0))
          45 +        rotation = angle_error(float(obs[2]), theta0)
          46 +        max_displacement = max(max_displacement, displacement)
          47 +        max_rotation = max(max_rotation, rotation)
          48 +        if first_motion is None and (displacement > 0.002 or rotation > math.radians(1)):
          49 +            first_motion = step
          50 +        if terminated or truncated:
          51 +            break
          52 +    env.close()
          53 +    return {
          54 +        "seed": seed,
          55 +        "ok": bool(terminated),
          56 +        "steps": step,
          57 +        "init_b": initial[:3],
          58 +        "init_r": initial[16:18],
          59 +        "goal": initial[29:32],
          60 +        "final_b": obs[:3],
          61 +        "final_r": obs[16:18],
          62 +        "pos": float(np.linalg.norm(obs[:2] - obs[29:31])),
          63 +        "ang_deg": math.degrees(angle_error(float(obs[2]), float(obs[31]))),
          64 +        "min_pos": min_pos,
          65 +        "min_ang_deg": math.degrees(min_ang),
          66 +        "min_joint": min_joint,
          67 +        "max_disp": max_displacement,
          68 +        "max_rot_deg": math.degrees(max_rotation),
          69 +        "first_motion": first_motion,
          70 +    }
          71 +
          72 +
          73 +def main():
          74 +    parser = argparse.ArgumentParser()
          75 +    parser.add_argument("--seeds", default="0-11")
          76 +    parser.add_argument("--cap", type=int)
          77 +    args = parser.parse_args()
          78 +    if "-" in args.seeds:
          79 +        lo, hi = map(int, args.seeds.split("-"))
          80 +        seeds = range(lo, hi + 1)
          81 +    else:
          82 +        seeds = [int(x) for x in args.seeds.split(",")]
          83 +    rows = [run_seed(seed, args.cap) for seed in seeds]
          84 +    for r in rows:
          85 +        print(
          86 +            f"seed={r['seed']:3d} ok={int(r['ok'])} n={r['steps']:4d} "
          87 +            f"initB=({r['init_b'][0]:.3f},{r['init_b'][1]:.3f},{math.degrees(r['init_b'][2]):6.1f}) "
          88 +            f"R=({r['init_r'][0]:.3f},{r['init_r'][1]:.3f}) "
          89 +            f"G=({r['goal'][0]:.3f},{r['goal'][1]:.3f},{math.degrees(r['goal'][2]):6.1f}) "
          90 +            f"finalerr=({r['pos']:.3f},{r['ang_deg']:5.1f}deg) "
          91 +            f"min=({r['min_pos']:.3f},{r['min_ang_deg']:5.1f}deg,J={r['min_joint']:.2f}) "
          92 +            f"motion@={r['first_motion']} disp={r['max_disp']:.3f} rot={r['max_rot_deg']:.1f}"
          93 +        )
          94 +    successes = [r for r in rows if r["ok"]]
          95 +    print(f"SUMMARY success={len(successes)}/{len(rows)} mean_steps_success=" +
          96 +          (f"{np.mean([r['steps'] for r in successes]):.1f}" if successes else "NA"))
          97 +
          98 +
          99 +if __name__ == "__main__":
         100 +    main()
```

</details>

<a id="C006"></a>
### C006 · Add isolated black-box geometry probe

Commit `f836fb9ae6c07389b10f8d57e7882de3f770d909`; parents: 96b4b4393638dee6042cc1bc0b099b363965ef1c. Recorded author date: 2026-09-09T08:26:23+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C006_f836fb9.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_geometry.py b/probe_geometry.py
new file mode 100644
index 0000000..a8e06dc
--- /dev/null
+++ b/probe_geometry.py
@@ -0,0 +1,106 @@
           1 +"""Small black-box probes for DynPushT2D.  Not used by the submitted policy."""
           2 +import argparse
           3 +import math
           4 +import numpy as np
           5 +
           6 +from env_client import make_env
           7 +
           8 +
           9 +def brief(seed):
          10 +    env = make_env()
          11 +    obs, _ = env.reset(seed=seed)
          12 +    print(seed, "max", env.max_steps,
          13 +          "block", np.round(obs[[0, 1, 2]], 5),
          14 +          "robot", np.round(obs[[16, 17]], 5),
          15 +          "goal", np.round(obs[[29, 30, 31]], 5),
          16 +          "dims", np.round(obs[[12, 13, 14, 15, 28]], 5))
          17 +    env.close()
          18 +
          19 +
          20 +def go(env, obs, target, speed=0.05, max_steps=100):
          21 +    """Move toward a point and return state plus trajectory samples."""
          22 +    out = []
          23 +    for _ in range(max_steps):
          24 +        delta = np.asarray(target, float) - obs[16:18]
          25 +        if np.linalg.norm(delta) < 1e-4:
          26 +            break
          27 +        act = np.clip(delta, -speed, speed)
          28 +        before = obs.copy()
          29 +        obs, _, term, trunc, _ = env.step(act)
          30 +        out.append((before, act.copy(), obs.copy()))
          31 +        if term or trunc:
          32 +            break
          33 +    return obs, out
          34 +
          35 +
          36 +def free_motion(seed, action, n=30):
          37 +    env = make_env()
          38 +    obs, _ = env.reset(seed=seed)
          39 +    initial = obs.copy()
          40 +    print("initial block/robot", initial[:3], initial[16:18])
          41 +    for i in range(n):
          42 +        prev = obs.copy()
          43 +        obs, _, term, trunc, _ = env.step(np.asarray(action, float))
          44 +        if i < 5 or i == n - 1:
          45 +            print(i + 1, "r", np.round(obs[16:22], 5), "b", np.round(obs[:6], 5),
          46 +                  "dr", np.round(obs[16:18] - prev[16:18], 5))
          47 +        if term or trunc:
          48 +            break
          49 +    env.close()
          50 +
          51 +
          52 +def ray(seed, angle, start_dist=0.45, end_dist=-0.05, speed=0.005):
          53 +    """Approach block center along world-space radial ray; report first response."""
          54 +    env = make_env()
          55 +    obs, _ = env.reset(seed=seed)
          56 +    c0 = obs[:2].copy()
          57 +    theta = obs[2]
          58 +    d = np.array([math.cos(angle), math.sin(angle)])
          59 +    start = c0 + d * start_dist
          60 +    # First place robot.  Record contamination from accidental collisions.
          61 +    obs, placement = go(env, obs, start, speed=0.025, max_steps=100)
          62 +    contaminated = np.linalg.norm(obs[:2] - c0) > 1e-5 or abs(obs[2] - theta) > 1e-5
          63 +    first = None
          64 +    samples = []
          65 +    target = c0 + d * end_dist
          66 +    for k in range(160):
          67 +        prev = obs.copy()
          68 +        obs, _, term, trunc, _ = env.step(np.clip(target - obs[16:18], -speed, speed))
          69 +        change = np.linalg.norm(obs[:2] - prev[:2]) + abs(obs[2] - prev[2])
          70 +        if change > 1e-7 and first is None:
          71 +            first = (k, prev.copy(), obs.copy())
          72 +        if first is not None and len(samples) < 4:
          73 +            samples.append(obs.copy())
          74 +        if np.linalg.norm(obs[16:18] - target) < 1e-4 or term or trunc:
          75 +            break
          76 +    label = f"seed={seed} worldang={angle:.3f} localang={(angle-theta):.3f} contam={contaminated}"
          77 +    if first is None:
          78 +        print(label, "NO CONTACT", "final r", np.round(obs[16:18], 4))
          79 +    else:
          80 +        k, before, after = first
          81 +        rel = before[16:18] - before[:2]
          82 +        local = np.array([[math.cos(-before[2]), -math.sin(-before[2])],
          83 +                          [math.sin(-before[2]), math.cos(-before[2])]]) @ rel
          84 +        print(label, "contactstep", k,
          85 +              "world_rel", np.round(rel, 5), "local_rel", np.round(local, 5),
          86 +              "center_dist", round(float(np.linalg.norm(rel)), 5),
          87 +              "block_delta", np.round(after[:3] - before[:3], 6))
          88 +        if samples:
          89 +            print("  after", [(np.round(x[:3], 4).tolist(), np.round(x[16:18], 4).tolist()) for x in samples])
          90 +    env.close()
          91 +
          92 +
          93 +if __name__ == "__main__":
          94 +    ap = argparse.ArgumentParser()
          95 +    ap.add_argument("mode", choices=["brief", "free", "rays"])
          96 +    ap.add_argument("--seed", type=int, default=0)
          97 +    args = ap.parse_args()
          98 +    if args.mode == "brief":
          99 +        for s in range(12):
         100 +            brief(s)
         101 +    elif args.mode == "free":
         102 +        free_motion(args.seed, [0.05, 0.0])
         103 +    else:
         104 +        env = make_env(); o, _ = env.reset(seed=args.seed); th = float(o[2]); env.close()
         105 +        for local_angle in np.linspace(0, 2 * math.pi, 12, endpoint=False):
         106 +            ray(args.seed, th + local_angle)
```

</details>

<a id="C007"></a>
### C007 · probe T-block contact offsets and induced rotation

Commit `ad9d002bb23b7e1bfcbcf287ccc7583b8d6fd539`; parents: f836fb9ae6c07389b10f8d57e7882de3f770d909. Recorded author date: 2026-09-09T08:26:34+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C007_ad9d002.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_rotation_agent.py b/probe_rotation_agent.py
index 989dd88..37aec50 100644
--- a/probe_rotation_agent.py
+++ b/probe_rotation_agent.py
@@ -21,9 +21,59 @@ def summarize(seed):
   21     21      env.close()
   22     22  
   23     23  
          24 +def move_to(env, s, target, nmax=200):
          25 +    for _ in range(nmax):
          26 +        d = np.asarray(target) - s[[16, 17]]
          27 +        if np.linalg.norm(d) < 0.012:
          28 +            break
          29 +        a = np.clip(d, -0.05, 0.05)
          30 +        s, _, done, trunc, _ = env.step(a)
          31 +        if done or trunc:
          32 +            break
          33 +    return s
          34 +
          35 +
          36 +def horizontal_scan(seed, yoff):
          37 +    env = make_env(); s, _ = env.reset(seed=seed)
          38 +    p0 = s[:3].copy(); bx, by = s[:2]
          39 +    # Route underneath/above the object before approaching from the left.
          40 +    safe_y = by + yoff
          41 +    s = move_to(env, s, [bx - 1.2, s[17]])
          42 +    s = move_to(env, s, [bx - 1.2, safe_y])
          43 +    first = None
          44 +    for k in range(38):
          45 +        s, _, done, trunc, _ = env.step(np.array([0.05, 0.0]))
          46 +        delta = np.linalg.norm(s[:2] - p0[:2])
          47 +        if first is None and (delta > 1e-4 or abs(wrap(float(s[2]-p0[2]))) > 1e-4):
          48 +            first = (k, float(s[16]), float(s[17]))
          49 +        if done or trunc: break
          50 +    print("HSCAN", yoff, "first", first, "dxy", np.round(s[:2]-p0[:2],4),
          51 +          "dth", round(wrap(float(s[2]-p0[2])),4), "robot", np.round(s[[16,17]],3))
          52 +    env.close()
          53 +
          54 +
          55 +def vertical_scan(seed, xoff):
          56 +    env = make_env(); s, _ = env.reset(seed=seed)
          57 +    p0 = s[:3].copy(); bx, by = s[:2]
          58 +    s = move_to(env, s, [s[16], by - 1.2])
          59 +    s = move_to(env, s, [bx + xoff, by - 1.2])
          60 +    first = None
          61 +    for k in range(38):
          62 +        s, _, done, trunc, _ = env.step(np.array([0.0, 0.05]))
          63 +        delta = np.linalg.norm(s[:2] - p0[:2])
          64 +        if first is None and (delta > 1e-4 or abs(wrap(float(s[2]-p0[2]))) > 1e-4):
          65 +            first = (k, float(s[16]), float(s[17]))
          66 +        if done or trunc: break
          67 +    print("VSCAN", xoff, "first", first, "dxy", np.round(s[:2]-p0[:2],4),
          68 +          "dth", round(wrap(float(s[2]-p0[2])),4), "robot", np.round(s[[16,17]],3))
          69 +    env.close()
          70 +
          71 +
   24     72  def main():
   25        -    for seed in range(12):
   26        -        summarize(seed)
          73 +    for off in [-0.7, -0.5, -0.3, -0.1, 0.1, 0.3, 0.5, 0.7]:
          74 +        horizontal_scan(11, off)
          75 +    for off in [-0.7, -0.5, -0.3, -0.1, 0.1, 0.3, 0.5, 0.7]:
          76 +        vertical_scan(11, off)
   27     77  
   28     78  
   29     79  if __name__ == "__main__":
```

</details>

<a id="C008"></a>
### C008 · use action-space dtype in rotation probe

Commit `ed758690595e0893c878768fe86d3bd163321df2`; parents: ad9d002bb23b7e1bfcbcf287ccc7583b8d6fd539. Recorded author date: 2026-09-09T08:26:55+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C008_ed75869.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_rotation_agent.py b/probe_rotation_agent.py
index 37aec50..702b8af 100644
--- a/probe_rotation_agent.py
+++ b/probe_rotation_agent.py
@@ -26,7 +26,7 @@ def move_to(env, s, target, nmax=200):
   26     26          d = np.asarray(target) - s[[16, 17]]
   27     27          if np.linalg.norm(d) < 0.012:
   28     28              break
   29        -        a = np.clip(d, -0.05, 0.05)
          29 +        a = np.clip(d, -0.05, 0.05).astype(np.float32)
   30     30          s, _, done, trunc, _ = env.step(a)
   31     31          if done or trunc:
   32     32              break
@@ -42,7 +42,7 @@ def horizontal_scan(seed, yoff):
   42     42      s = move_to(env, s, [bx - 1.2, safe_y])
   43     43      first = None
   44     44      for k in range(38):
   45        -        s, _, done, trunc, _ = env.step(np.array([0.05, 0.0]))
          45 +        s, _, done, trunc, _ = env.step(np.array([0.05, 0.0], dtype=np.float32))
   46     46          delta = np.linalg.norm(s[:2] - p0[:2])
   47     47          if first is None and (delta > 1e-4 or abs(wrap(float(s[2]-p0[2]))) > 1e-4):
   48     48              first = (k, float(s[16]), float(s[17]))
@@ -59,7 +59,7 @@ def vertical_scan(seed, xoff):
   59     59      s = move_to(env, s, [bx + xoff, by - 1.2])
   60     60      first = None
   61     61      for k in range(38):
   62        -        s, _, done, trunc, _ = env.step(np.array([0.0, 0.05]))
          62 +        s, _, done, trunc, _ = env.step(np.array([0.0, 0.05], dtype=np.float32))
   63     63          delta = np.linalg.norm(s[:2] - p0[:2])
   64     64          if first is None and (delta > 1e-4 or abs(wrap(float(s[2]-p0[2]))) > 1e-4):
   65     65              first = (k, float(s[16]), float(s[17]))
```

</details>

<a id="C009"></a>
### C009 · stay within strict action bounds in probe

Commit `dde97e4c2350ee2b00c67a757765f6d45bf884e7`; parents: ed758690595e0893c878768fe86d3bd163321df2. Recorded author date: 2026-09-09T08:27:12+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C009_dde97e4.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_rotation_agent.py b/probe_rotation_agent.py
index 702b8af..9e2024d 100644
--- a/probe_rotation_agent.py
+++ b/probe_rotation_agent.py
@@ -26,7 +26,7 @@ def move_to(env, s, target, nmax=200):
   26     26          d = np.asarray(target) - s[[16, 17]]
   27     27          if np.linalg.norm(d) < 0.012:
   28     28              break
   29        -        a = np.clip(d, -0.05, 0.05).astype(np.float32)
          29 +        a = np.clip(d, -0.049, 0.049).astype(np.float32)
   30     30          s, _, done, trunc, _ = env.step(a)
   31     31          if done or trunc:
   32     32              break
@@ -42,7 +42,7 @@ def horizontal_scan(seed, yoff):
   42     42      s = move_to(env, s, [bx - 1.2, safe_y])
   43     43      first = None
   44     44      for k in range(38):
   45        -        s, _, done, trunc, _ = env.step(np.array([0.05, 0.0], dtype=np.float32))
          45 +        s, _, done, trunc, _ = env.step(np.array([0.049, 0.0], dtype=np.float32))
   46     46          delta = np.linalg.norm(s[:2] - p0[:2])
   47     47          if first is None and (delta > 1e-4 or abs(wrap(float(s[2]-p0[2]))) > 1e-4):
   48     48              first = (k, float(s[16]), float(s[17]))
@@ -59,7 +59,7 @@ def vertical_scan(seed, xoff):
   59     59      s = move_to(env, s, [bx + xoff, by - 1.2])
   60     60      first = None
   61     61      for k in range(38):
   62        -        s, _, done, trunc, _ = env.step(np.array([0.0, 0.05], dtype=np.float32))
          62 +        s, _, done, trunc, _ = env.step(np.array([0.0, 0.049], dtype=np.float32))
   63     63          delta = np.linalg.norm(s[:2] - p0[:2])
   64     64          if first is None and (delta > 1e-4 or abs(wrap(float(s[2]-p0[2]))) > 1e-4):
   65     65              first = (k, float(s[16]), float(s[17]))
```

</details>

<a id="C010"></a>
### C010 · Probe uncontaminated radial contacts from reset poses

Commit `f0d4d6a59a42682e86be99207c0a6fb04b550a17`; parents: dde97e4c2350ee2b00c67a757765f6d45bf884e7. Recorded author date: 2026-09-09T08:27:34+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C010_f0d4d6a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_geometry.py b/probe_geometry.py
index a8e06dc..2321799 100644
--- a/probe_geometry.py
+++ b/probe_geometry.py
@@ -24,7 +24,8 @@ def go(env, obs, target, speed=0.05, max_steps=100):
   24     24          delta = np.asarray(target, float) - obs[16:18]
   25     25          if np.linalg.norm(delta) < 1e-4:
   26     26              break
   27        -        act = np.clip(delta, -speed, speed)
          27 +        norm = np.linalg.norm(delta)
          28 +        act = delta if norm <= speed else delta * (speed / norm)
   28     29          before = obs.copy()
   29     30          obs, _, term, trunc, _ = env.step(act)
   30     31          out.append((before, act.copy(), obs.copy()))
@@ -65,7 +66,10 @@ def ray(seed, angle, start_dist=0.45, end_dist=-0.05, speed=0.005):
   65     66      target = c0 + d * end_dist
   66     67      for k in range(160):
   67     68          prev = obs.copy()
   68        -        obs, _, term, trunc, _ = env.step(np.clip(target - obs[16:18], -speed, speed))
          69 +        delta = target - obs[16:18]
          70 +        norm = np.linalg.norm(delta)
          71 +        act = delta if norm <= speed else delta * (speed / norm)
          72 +        obs, _, term, trunc, _ = env.step(act)
   69     73          change = np.linalg.norm(obs[:2] - prev[:2]) + abs(obs[2] - prev[2])
   70     74          if change > 1e-7 and first is None:
   71     75              first = (k, prev.copy(), obs.copy())
@@ -90,9 +94,41 @@ def ray(seed, angle, start_dist=0.45, end_dist=-0.05, speed=0.005):
   90     94      env.close()
   91     95  
   92     96  
          97 +def natural(seed, speed=0.005):
          98 +    """Approach directly from the reset robot location (no placement artifacts)."""
          99 +    env = make_env()
         100 +    obs, _ = env.reset(seed=seed)
         101 +    initial = obs.copy()
         102 +    first = None
         103 +    for k in range(1000):
         104 +        prev = obs.copy()
         105 +        delta = obs[:2] - obs[16:18]
         106 +        norm = np.linalg.norm(delta)
         107 +        act = delta if norm <= speed else delta * (speed / norm)
         108 +        obs, _, term, trunc, _ = env.step(act)
         109 +        change = np.linalg.norm(obs[:2] - prev[:2]) + abs(obs[2] - prev[2])
         110 +        if change > 1e-7:
         111 +            first = (k, prev.copy(), obs.copy())
         112 +            break
         113 +        if term or trunc:
         114 +            break
         115 +    if first is None:
         116 +        print(seed, "NO CONTACT")
         117 +    else:
         118 +        k, before, after = first
         119 +        rel = before[16:18] - before[:2]
         120 +        ct, st = math.cos(-before[2]), math.sin(-before[2])
         121 +        local = np.array([[ct, -st], [st, ct]]) @ rel
         122 +        a = math.atan2(local[1], local[0])
         123 +        print(seed, "theta", round(float(initial[2]), 4), "local_ray", round(a, 4),
         124 +              "contact_local", np.round(local, 5), "dist", round(float(np.linalg.norm(local)), 5),
         125 +              "dblock", np.round(after[:3] - before[:3], 7))
         126 +    env.close()
         127 +
         128 +
   93    129  if __name__ == "__main__":
   94    130      ap = argparse.ArgumentParser()
   95        -    ap.add_argument("mode", choices=["brief", "free", "rays"])
         131 +    ap.add_argument("mode", choices=["brief", "free", "rays", "natural"])
   96    132      ap.add_argument("--seed", type=int, default=0)
   97    133      args = ap.parse_args()
   98    134      if args.mode == "brief":
@@ -100,7 +136,10 @@ if __name__ == "__main__":
  100    136              brief(s)
  101    137      elif args.mode == "free":
  102    138          free_motion(args.seed, [0.05, 0.0])
  103        -    else:
         139 +    elif args.mode == "rays":
  104    140          env = make_env(); o, _ = env.reset(seed=args.seed); th = float(o[2]); env.close()
  105    141          for local_angle in np.linspace(0, 2 * math.pi, 12, endpoint=False):
  106    142              ray(args.seed, th + local_angle)
         143 +    else:
         144 +        for s in range(40):
         145 +            natural(s)
```

</details>

<a id="C011"></a>
### C011 · measure short offset pushes for controlled rotation

Commit `a7666290d77c31d12c31795c7faf73369baba177`; parents: f0d4d6a59a42682e86be99207c0a6fb04b550a17. Recorded author date: 2026-09-09T08:28:26+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C011_a766629.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_rotation_agent.py b/probe_rotation_agent.py
index 9e2024d..4a9ec23 100644
--- a/probe_rotation_agent.py
+++ b/probe_rotation_agent.py
@@ -69,11 +69,44 @@ def vertical_scan(seed, xoff):
   69     69      env.close()
   70     70  
   71     71  
          72 +def short_vertical(seed, xoff, direction, pushes):
          73 +    env = make_env(); s, _ = env.reset(seed=seed)
          74 +    bx, by = s[:2]
          75 +    start_y = by - 1.2 if direction > 0 else by + 1.2
          76 +    # Seed 11 starts well below the block; route around its left or right edge.
          77 +    route_x = bx - 1.0 if xoff < 0 else bx + 1.0
          78 +    s = move_to(env, s, [route_x, s[17]])
          79 +    s = move_to(env, s, [route_x, start_y])
          80 +    s = move_to(env, s, [bx + xoff, start_y])
          81 +    prep = s[:3].copy()
          82 +    contact = None
          83 +    after = 0
          84 +    for k in range(45):
          85 +        old = s[:3].copy()
          86 +        a = np.array([0.0, direction * 0.049], dtype=np.float32)
          87 +        s, _, done, trunc, _ = env.step(a)
          88 +        moved = np.linalg.norm(s[:2]-old[:2]) > 2e-5 or abs(wrap(float(s[2]-old[2]))) > 2e-5
          89 +        if contact is None and moved:
          90 +            contact = k
          91 +        if contact is not None:
          92 +            after += 1
          93 +            if after >= pushes: break
          94 +        if done or trunc: break
          95 +    print("SHORTV", "xoff", xoff, "dir", direction, "n", pushes,
          96 +          "prep", np.round(prep-[bx,by,s[2]*0 + prep[2]], 4),
          97 +          "contact", contact, "delta", np.round(s[:2]-prep[:2],4),
          98 +          "dth", round(wrap(float(s[2]-prep[2])),4),
          99 +          "vel", np.round(s[[3,4,5]],4))
         100 +    env.close()
         101 +
         102 +
   72    103  def main():
   73        -    for off in [-0.7, -0.5, -0.3, -0.1, 0.1, 0.3, 0.5, 0.7]:
   74        -        horizontal_scan(11, off)
   75        -    for off in [-0.7, -0.5, -0.3, -0.1, 0.1, 0.3, 0.5, 0.7]:
   76        -        vertical_scan(11, off)
         104 +    for off in [-0.5, -0.35, 0.35, 0.5]:
         105 +        for n in [1, 2, 4, 8]:
         106 +            short_vertical(11, off, 1, n)
         107 +    for off in [-0.5, 0.5]:
         108 +        for n in [1, 2, 4, 8]:
         109 +            short_vertical(11, off, -1, n)
   77    110  
   78    111  
   79    112  if __name__ == "__main__":
```

</details>

<a id="C012"></a>
### C012 · Add capped flushed rollouts for efficient policy iteration

Commit `359ffb77f40f5b6e2237bec69eb969a9b34e1ce5`; parents: a7666290d77c31d12c31795c7faf73369baba177. Recorded author date: 2026-09-09T08:29:39+02:00.

File roles (automatic): diagnostic/test.

- [E0034](01_timeline.md#E0034): commit title in command; output may not confirm creation.
[Exact all-file diff](evidence/diffs/C012_359ffb7.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/test_approach.py b/test_approach.py
index d107f07..c7fd662 100644
--- a/test_approach.py
+++ b/test_approach.py
@@ -4,7 +4,7 @@ from env_client import make_env
    4      4  from approach import GeneratedApproach
    5      5  
    6      6  
    7        -def run(seed, verbose=False):
           7 +def run(seed, verbose=False, cap=None):
    8      8      env = make_env()
    9      9      obs, info = env.reset(seed=seed)
   10     10      policy = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
@@ -12,7 +12,7 @@ def run(seed, verbose=False):
   12     12      initial = obs.copy()
   13     13      terminated = truncated = False
   14     14      steps = 0
   15        -    while not (terminated or truncated):
          15 +    while not (terminated or truncated) and (cap is None or steps < cap):
   16     16          obs, reward, terminated, truncated, info = env.step(policy.get_action(obs))
   17     17          steps += 1
   18     18      poserr = float(np.linalg.norm(obs[:2] - obs[29:31]))
@@ -20,13 +20,14 @@ def run(seed, verbose=False):
   20     20      env.close()
   21     21      if verbose:
   22     22          print(seed, terminated, steps, "init", np.round(initial[[0,1,2,16,17,29,30,31]],3),
   23        -              "finalerr", round(poserr,3), round(angerr,3))
          23 +              "finalerr", round(poserr,3), round(angerr,3), flush=True)
   24     24      return terminated, steps, poserr, angerr
   25     25  
   26     26  
   27     27  if __name__ == "__main__":
   28     28      ap = argparse.ArgumentParser()
   29     29      ap.add_argument("seeds", nargs="*", type=int, default=list(range(10)))
          30 +    ap.add_argument("--cap", type=int, default=None)
   30     31      args = ap.parse_args()
   31        -    results = [run(seed, True) for seed in args.seeds]
          32 +    results = [run(seed, True, args.cap) for seed in args.seeds]
   32     33      print("success", sum(x[0] for x in results), "/", len(results))
```

</details>

<a id="C013"></a>
### C013 · validate rotation contacts in arbitrary block frames

Commit `0968980d067539e16142d6d0e84ccebcec03b2dc`; parents: 359ffb77f40f5b6e2237bec69eb969a9b34e1ce5. Recorded author date: 2026-09-09T08:29:52+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C013_0968980.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_rotation_agent.py b/probe_rotation_agent.py
index 4a9ec23..944a516 100644
--- a/probe_rotation_agent.py
+++ b/probe_rotation_agent.py
@@ -100,13 +100,43 @@ def short_vertical(seed, xoff, direction, pushes):
  100    100      env.close()
  101    101  
  102    102  
         103 +def rot(theta, local):
         104 +    c, q = math.cos(theta), math.sin(theta)
         105 +    return np.array([c*local[0] - q*local[1], q*local[0] + c*local[1]])
         106 +
         107 +
         108 +def general_frame_trial(seed, xoff, pushes=4):
         109 +    env = make_env(); s, _ = env.reset(seed=seed)
         110 +    initial = s[:3].copy(); center = s[:2].copy(); theta = float(s[2])
         111 +    side = 1 if xoff > 0 else -1
         112 +    # Travel to the outer/below corner, then inward along local x, avoiding the T.
         113 +    s = move_to(env, s, center + rot(theta, [side*1.0, -1.15]))
         114 +    s = move_to(env, s, center + rot(theta, [xoff, -1.15]))
         115 +    prep = s[:3].copy()
         116 +    contact = None; moved_steps = 0
         117 +    for k in range(40):
         118 +        old = s[:3].copy()
         119 +        a = rot(theta, [0.0, 0.049]).astype(np.float32)
         120 +        s, _, done, trunc, _ = env.step(a)
         121 +        moved = np.linalg.norm(s[:2]-old[:2]) > 2e-5 or abs(wrap(float(s[2]-old[2]))) > 2e-5
         122 +        if contact is None and moved: contact = k
         123 +        if contact is not None:
         124 +            moved_steps += 1
         125 +            if moved_steps >= pushes: break
         126 +        if done or trunc: break
         127 +    world_dp = s[:2] - prep[:2]
         128 +    local_dp = rot(-theta, world_dp)
         129 +    print("FRAME", seed, "theta", round(theta,3), "xoff", xoff,
         130 +          "setup", np.round(prep[:2]-initial[:2],3), round(wrap(float(prep[2]-initial[2])),3),
         131 +          "contact", contact, "local_dp", np.round(local_dp,3),
         132 +          "dth", round(wrap(float(s[2]-prep[2])),3))
         133 +    env.close()
         134 +
         135 +
  103    136  def main():
  104        -    for off in [-0.5, -0.35, 0.35, 0.5]:
  105        -        for n in [1, 2, 4, 8]:
  106        -            short_vertical(11, off, 1, n)
  107        -    for off in [-0.5, 0.5]:
  108        -        for n in [1, 2, 4, 8]:
  109        -            short_vertical(11, off, -1, n)
         137 +    for seed in [0, 1, 2, 5, 7, 9, 10, 11]:
         138 +        general_frame_trial(seed, 0.5)
         139 +        general_frame_trial(seed, -0.5)
  110    140  
  111    141  
  112    142  if __name__ == "__main__":
```

</details>

<a id="C014"></a>
### C014 · Drive through block center to ensure contact and translation

Commit `40a0345bf4fc343f1c64c4e0874cfed79acd6345`; parents: 0968980d067539e16142d6d0e84ccebcec03b2dc. Recorded author date: 2026-09-09T08:29:57+02:00.

File roles (automatic): policy.

- [E0038](01_timeline.md#E0038): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C014_40a0345_approach.py) · [Exact all-file diff](evidence/diffs/C014_40a0345.diff)

[Previous saved controller snapshot](evidence/versions/C004_edd2c7d_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8e52236..ba422cd 100644
--- a/approach.py
+++ b/approach.py
@@ -24,9 +24,9 @@ class GeneratedApproach:
   24     24              direction = np.array([1.0, 0.0])
   25     25          else:
   26     26              direction = delta / distance
   27        -        # Conservative clearance for the initial positioning phase.
   28        -        staging = block - direction * 0.13
   29        -        target = staging if np.linalg.norm(robot - staging) > 0.035 else block + direction * 0.08
          27 +        # Aim through the block. Collision constrains the robot at the boundary;
          28 +        # continuing toward a point beyond the centre supplies the push.
          29 +        target = block + direction * 0.5
   30     30          # The server checks the open interval despite the advertised Box bounds.
   31     31          move = np.clip(target - robot, self.low + 1e-6, self.high - 1e-6)
   32     32          self.step += 1
```

</details>

<a id="C015"></a>
### C015 · test paired torque pushes for translation cancellation

Commit `9e1edf77ba7cbe5ec7aaa74714d0b44f6b12f48a`; parents: 40a0345bf4fc343f1c64c4e0874cfed79acd6345. Recorded author date: 2026-09-09T08:30:42+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C015_9e1edf7.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_rotation_agent.py b/probe_rotation_agent.py
index 944a516..d4d161a 100644
--- a/probe_rotation_agent.py
+++ b/probe_rotation_agent.py
@@ -133,10 +133,44 @@ def general_frame_trial(seed, xoff, pushes=4):
  133    133      env.close()
  134    134  
  135    135  
         136 +def push_until_moved(env, s, action, count=4):
         137 +    got = 0
         138 +    for _ in range(45):
         139 +        old = s[:3].copy()
         140 +        s, _, done, trunc, _ = env.step(np.asarray(action, dtype=np.float32))
         141 +        if np.linalg.norm(s[:2]-old[:2]) > 2e-5 or abs(wrap(float(s[2]-old[2]))) > 2e-5:
         142 +            got += 1
         143 +            if got >= count: break
         144 +        if done or trunc: break
         145 +    return s
         146 +
         147 +
         148 +def paired_torque(seed=11):
         149 +    env = make_env(); s, _ = env.reset(seed=seed); initial = s[:3].copy()
         150 +    # Right underside, push toward the crossbar: positive torque.
         151 +    b, th = s[:2].copy(), float(s[2])
         152 +    s = move_to(env, s, [b[0]+1.0, s[17]])
         153 +    s = move_to(env, s, b + rot(th, [1.0, -1.2]))
         154 +    s = move_to(env, s, b + rot(th, [0.5, -1.2]))
         155 +    s = push_until_moved(env, s, rot(th, [0, 0.049]), 4)
         156 +    middle = s[:3].copy()
         157 +    # Retreat and go around the outside to left topside; push down for same torque.
         158 +    b, th = s[:2].copy(), float(s[2])
         159 +    s = move_to(env, s, s[[16,17]] + rot(th, [0, -0.55]))
         160 +    s = move_to(env, s, b + rot(th, [1.0, -1.2]))
         161 +    s = move_to(env, s, b + rot(th, [1.0, 1.2]))
         162 +    s = move_to(env, s, b + rot(th, [-0.5, 1.2]))
         163 +    s = push_until_moved(env, s, rot(th, [0, -0.049]), 4)
         164 +    final = s[:3].copy()
         165 +    print("PAIR", "first", np.round(middle[:2]-initial[:2],3),
         166 +          round(wrap(float(middle[2]-initial[2])),3),
         167 +          "net", np.round(final[:2]-initial[:2],3),
         168 +          round(wrap(float(final[2]-initial[2])),3))
         169 +    env.close()
         170 +
         171 +
  136    172  def main():
  137        -    for seed in [0, 1, 2, 5, 7, 9, 10, 11]:
  138        -        general_frame_trial(seed, 0.5)
  139        -        general_frame_trial(seed, -0.5)
         173 +    paired_torque()
  140    174  
  141    175  
  142    176  if __name__ == "__main__":
```

</details>

<a id="C016"></a>
### C016 · Measure sustained push response after clean contact

Commit `ab58679b54a4b703ef9e33fa045e7dd62632eb2e`; parents: 9e1edf77ba7cbe5ec7aaa74714d0b44f6b12f48a. Recorded author date: 2026-09-09T08:31:35+02:00.

File roles (automatic): diagnostic/test, policy.

[Controller after this commit](evidence/versions/C016_ab58679_approach.py) · [Exact all-file diff](evidence/diffs/C016_ab58679.diff)

[Previous saved controller snapshot](evidence/versions/C014_40a0345_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index ba422cd..c2fc7c5 100644
--- a/approach.py
+++ b/approach.py
@@ -12,6 +12,12 @@ class GeneratedApproach:
   12     12  
   13     13      def reset(self, state, info):
   14     14          self.step = 0
          15 +        self.mode = "stage"
          16 +        self.push_steps = 0
          17 +
          18 +    @staticmethod
          19 +    def _wrap(angle):
          20 +        return (angle + math.pi) % (2.0 * math.pi) - math.pi
   15     21  
   16     22      def get_action(self, state):
   17     23          s = np.asarray(state, dtype=float)
@@ -24,9 +30,34 @@ class GeneratedApproach:
   24     30              direction = np.array([1.0, 0.0])
   25     31          else:
   26     32              direction = delta / distance
   27        -        # Aim through the block. Collision constrains the robot at the boundary;
   28        -        # continuing toward a point beyond the centre supplies the push.
   29        -        target = block + direction * 0.5
          33 +        behind = -direction
          34 +        desired_angle = math.atan2(behind[1], behind[0])
          35 +        rel = robot - block
          36 +        radius = float(np.linalg.norm(rel))
          37 +        current_angle = math.atan2(rel[1], rel[0]) if radius > 1e-8 else desired_angle
          38 +        angle_error = self._wrap(desired_angle - current_angle)
          39 +
          40 +        if self.mode == "push":
          41 +            # Periodically re-stage so angular or lateral errors cannot accumulate.
          42 +            target = block + direction * 0.45
          43 +            self.push_steps += 1
          44 +            if self.push_steps >= 35:
          45 +                self.mode = "stage"
          46 +        else:
          47 +            clearance = 0.78
          48 +            # Orbit outside the T's circumscribed radius; direct travel to the
          49 +            # far side would otherwise collide with and rotate the object.
          50 +            if radius < clearance - 0.04:
          51 +                target = block + clearance * np.array([math.cos(current_angle), math.sin(current_angle)])
          52 +            elif abs(angle_error) > 0.055:
          53 +                next_angle = current_angle + float(np.clip(angle_error, -0.10, 0.10))
          54 +                target = block + clearance * np.array([math.cos(next_angle), math.sin(next_angle)])
          55 +            else:
          56 +                target = block + clearance * behind
          57 +                if np.linalg.norm(robot - target) < 0.035:
          58 +                    self.mode = "push"
          59 +                    self.push_steps = 0
          60 +                    target = block + direction * 0.45
   30     61          # The server checks the open interval despite the advertised Box bounds.
   31     62          move = np.clip(target - robot, self.low + 1e-6, self.high - 1e-6)
   32     63          self.step += 1
diff --git a/probe_geometry.py b/probe_geometry.py
index 2321799..b7f341c 100644
--- a/probe_geometry.py
+++ b/probe_geometry.py
@@ -126,9 +126,45 @@ def natural(seed, speed=0.005):
  126    126      env.close()
  127    127  
  128    128  
         129 +def push_response(seed, approach_speed=0.015, push_speed=0.01, pushes=20):
         130 +    """Approach along the reset-to-center line, then maintain that push direction."""
         131 +    env = make_env()
         132 +    obs, _ = env.reset(seed=seed)
         133 +    initial = obs.copy()
         134 +    direction = initial[:2] - initial[16:18]
         135 +    direction /= np.linalg.norm(direction)
         136 +    contact = None
         137 +    for k in range(400):
         138 +        prev = obs.copy()
         139 +        obs, _, term, trunc, _ = env.step(direction * approach_speed)
         140 +        if np.linalg.norm(obs[:2] - prev[:2]) + abs(obs[2] - prev[2]) > 1e-7:
         141 +            contact = prev.copy()
         142 +            break
         143 +        if term or trunc:
         144 +            break
         145 +    if contact is None:
         146 +        print("push", seed, "NO CONTACT")
         147 +        env.close()
         148 +        return
         149 +    at_contact = obs.copy()
         150 +    for _ in range(pushes):
         151 +        obs, _, term, trunc, _ = env.step(direction * push_speed)
         152 +        if term or trunc:
         153 +            break
         154 +    rel = contact[16:18] - contact[:2]
         155 +    ct, st = math.cos(-contact[2]), math.sin(-contact[2])
         156 +    local = np.array([[ct, -st], [st, ct]]) @ rel
         157 +    db = obs[:3] - at_contact[:3]
         158 +    print("push", seed, "local_contact", np.round(local, 4),
         159 +          "20step block", np.round(db, 5), "robot", np.round(obs[16:18] - at_contact[16:18], 5),
         160 +          "per_action_xy", round(float(np.linalg.norm(db[:2])) / pushes, 5),
         161 +          "rot_per_action", round(float(db[2]) / pushes, 5))
         162 +    env.close()
         163 +
         164 +
  129    165  if __name__ == "__main__":
  130    166      ap = argparse.ArgumentParser()
  131        -    ap.add_argument("mode", choices=["brief", "free", "rays", "natural"])
         167 +    ap.add_argument("mode", choices=["brief", "free", "rays", "natural", "push"])
  132    168      ap.add_argument("--seed", type=int, default=0)
  133    169      args = ap.parse_args()
  134    170      if args.mode == "brief":
@@ -140,6 +176,9 @@ if __name__ == "__main__":
  140    176          env = make_env(); o, _ = env.reset(seed=args.seed); th = float(o[2]); env.close()
  141    177          for local_angle in np.linspace(0, 2 * math.pi, 12, endpoint=False):
  142    178              ray(args.seed, th + local_angle)
  143        -    else:
         179 +    elif args.mode == "natural":
  144    180          for s in range(40):
  145    181              natural(s)
         182 +    else:
         183 +        for s in range(12):
         184 +            push_response(s)
```

</details>

<a id="C017"></a>
### C017 · verify mirrored low-translation rotation pair

Commit `b17244ac89d2d63c88394272dfca7972118a3fd6`; parents: ab58679b54a4b703ef9e33fa045e7dd62632eb2e. Recorded author date: 2026-09-09T08:31:52+02:00.

File roles (automatic): diagnostic/test.

[Exact all-file diff](evidence/diffs/C017_b17244a.diff)

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/probe_rotation_agent.py b/probe_rotation_agent.py
index d4d161a..dc2197d 100644
--- a/probe_rotation_agent.py
+++ b/probe_rotation_agent.py
@@ -145,24 +145,27 @@ def push_until_moved(env, s, action, count=4):
  145    145      return s
  146    146  
  147    147  
  148        -def paired_torque(seed=11):
         148 +def paired_torque(seed=11, sign=1):
  149    149      env = make_env(); s, _ = env.reset(seed=seed); initial = s[:3].copy()
  150        -    # Right underside, push toward the crossbar: positive torque.
         150 +    # For positive torque: right underside upward, then left topside downward.
         151 +    first_x = 0.5 * sign
         152 +    outer_x = 1.0 * sign
         153 +    second_x = -first_x
  151    154      b, th = s[:2].copy(), float(s[2])
  152        -    s = move_to(env, s, [b[0]+1.0, s[17]])
  153        -    s = move_to(env, s, b + rot(th, [1.0, -1.2]))
  154        -    s = move_to(env, s, b + rot(th, [0.5, -1.2]))
         155 +    s = move_to(env, s, [b[0]+outer_x, s[17]])
         156 +    s = move_to(env, s, b + rot(th, [outer_x, -1.2]))
         157 +    s = move_to(env, s, b + rot(th, [first_x, -1.2]))
  155    158      s = push_until_moved(env, s, rot(th, [0, 0.049]), 4)
  156    159      middle = s[:3].copy()
  157    160      # Retreat and go around the outside to left topside; push down for same torque.
  158    161      b, th = s[:2].copy(), float(s[2])
  159    162      s = move_to(env, s, s[[16,17]] + rot(th, [0, -0.55]))
  160        -    s = move_to(env, s, b + rot(th, [1.0, -1.2]))
  161        -    s = move_to(env, s, b + rot(th, [1.0, 1.2]))
  162        -    s = move_to(env, s, b + rot(th, [-0.5, 1.2]))
         163 +    s = move_to(env, s, b + rot(th, [outer_x, -1.2]))
         164 +    s = move_to(env, s, b + rot(th, [outer_x, 1.2]))
         165 +    s = move_to(env, s, b + rot(th, [second_x, 1.2]))
  163    166      s = push_until_moved(env, s, rot(th, [0, -0.049]), 4)
  164    167      final = s[:3].copy()
  165        -    print("PAIR", "first", np.round(middle[:2]-initial[:2],3),
         168 +    print("PAIR", sign, "first", np.round(middle[:2]-initial[:2],3),
  166    169            round(wrap(float(middle[2]-initial[2])),3),
  167    170            "net", np.round(final[:2]-initial[:2],3),
  168    171            round(wrap(float(final[2]-initial[2])),3))
@@ -170,7 +173,8 @@ def paired_torque(seed=11):
  170    173  
  171    174  
  172    175  def main():
  173        -    paired_torque()
         176 +    paired_torque(sign=1)
         177 +    paired_torque(sign=-1)
  174    178  
  175    179  
  176    180  if __name__ == "__main__":
```

</details>

<a id="C018"></a>
### C018 · Implement geometry-aware rotation and centerline translation planner

Commit `2fc7f82a1351f900d6caff1f2a01b91a66ee3b1a`; parents: b17244ac89d2d63c88394272dfca7972118a3fd6. Recorded author date: 2026-09-09T08:37:31+02:00.

File roles (automatic): policy.

- [E0049](01_timeline.md#E0049): commit hash in recorded output.
[Controller after this commit](evidence/versions/C018_2fc7f82_approach.py) · [Exact all-file diff](evidence/diffs/C018_2fc7f82.diff)

[Previous saved controller snapshot](evidence/versions/C016_ab58679_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index c2fc7c5..8242f36 100644
--- a/approach.py
+++ b/approach.py
@@ -1,64 +1,220 @@
           1 +import heapq
    1      2  import math
    2      3  import numpy as np
    3      4  
    4      5  
    5      6  class GeneratedApproach:
    6        -    """Fast reactive baseline: get behind the block and push its centre to goal."""
           7 +    """Geometry-aware quasi-static manipulation of the T-shaped rigid body."""
    7      8  
    8      9      def __init__(self, action_space, observation_space, primitives):
    9        -        self.low = np.asarray(action_space.low, dtype=float)
   10        -        self.high = np.asarray(action_space.high, dtype=float)
   11        -        self.step = 0
          10 +        self.low = np.asarray(action_space.low, dtype=float) + 1e-6
          11 +        self.high = np.asarray(action_space.high, dtype=float) - 1e-6
   12     12  
   13        -    def reset(self, state, info):
   14        -        self.step = 0
   15        -        self.mode = "stage"
   16        -        self.push_steps = 0
          13 +    @staticmethod
          14 +    def _wrap(a):
          15 +        return (a + math.pi) % (2.0 * math.pi) - math.pi
   17     16  
   18     17      @staticmethod
   19        -    def _wrap(angle):
   20        -        return (angle + math.pi) % (2.0 * math.pi) - math.pi
          18 +    def _rot(a):
          19 +        c, q = math.cos(a), math.sin(a)
          20 +        return np.array([[c, -q], [q, c]])
          21 +
          22 +    def reset(self, state, info):
          23 +        self.mode = "idle"
          24 +        self.path = []
          25 +        self.next_mode = None
          26 +        self.force_local = np.zeros(2)
          27 +        self.push_start = None
          28 +        self.push_count = 0
          29 +        self.retreat_count = 0
          30 +        self.after_retreat = "idle"
          31 +        self.pair_sign = 0.0
          32 +        self.pair_start_theta = 0.0
          33 +        self.pair_amount = 0.0
          34 +        self.translate_amount = 0.0
          35 +
          36 +    def _local_to_world(self, s, point):
          37 +        return s[0:2] + self._rot(float(s[2])).dot(np.asarray(point, dtype=float))
          38 +
          39 +    def _world_to_local(self, s, point):
          40 +        return self._rot(-float(s[2])).dot(np.asarray(point, dtype=float) - s[0:2])
          41 +
          42 +    def _blocked(self, s, world, margin=0.14):
          43 +        xw, yw = world
          44 +        if xw < 0.105 or xw > 4.895 or yw < 0.105 or yw > 4.895:
          45 +            return True
          46 +        x, y = self._world_to_local(s, world)
          47 +        w, lh, lv = float(s[12]), float(s[13]), float(s[14])
          48 +        bar = (-lh / 2 - margin <= x <= lh / 2 + margin and
          49 +               -w - margin <= y <= margin)
          50 +        stem = (-w / 2 - margin <= x <= w / 2 + margin and
          51 +                -w - lv - margin <= y <= -w + margin)
          52 +        return bar or stem
          53 +
          54 +    def _plan(self, s, goal_local):
          55 +        """Small 4-neighbour A* around an inflated T and arena walls."""
          56 +        start = np.asarray(s[16:18], dtype=float)
          57 +        goal = self._local_to_world(s, goal_local)
          58 +        res = 0.10
          59 +        to_key = lambda p: (int(round((p[0] - 0.1) / res)),
          60 +                            int(round((p[1] - 0.1) / res)))
          61 +        to_pos = lambda k: np.array([0.1 + res * k[0], 0.1 + res * k[1]])
          62 +        sk, raw_gk = to_key(start), to_key(goal)
          63 +        candidates = []
          64 +        for radius in range(0, 5):
          65 +            for dx in range(-radius, radius + 1):
          66 +                for dy in range(-radius, radius + 1):
          67 +                    if max(abs(dx), abs(dy)) != radius:
          68 +                        continue
          69 +                    k = (raw_gk[0] + dx, raw_gk[1] + dy)
          70 +                    p = to_pos(k)
          71 +                    if not self._blocked(s, p):
          72 +                        candidates.append((float(np.linalg.norm(p - goal)), k))
          73 +            if candidates:
          74 +                break
          75 +        if not candidates:
          76 +            return [goal]
          77 +        gk = min(candidates)[1]
          78 +        frontier = [(0.0, sk)]
          79 +        came = {sk: None}
          80 +        cost = {sk: 0.0}
          81 +        found = False
          82 +        while frontier and len(came) < 5000:
          83 +            _, cur = heapq.heappop(frontier)
          84 +            if cur == gk:
          85 +                found = True
          86 +                break
          87 +            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
          88 +                nxt = (cur[0] + dx, cur[1] + dy)
          89 +                p = to_pos(nxt)
          90 +                if nxt != sk and self._blocked(s, p):
          91 +                    continue
          92 +                nc = cost[cur] + 1.0
          93 +                if nxt not in cost or nc < cost[nxt]:
          94 +                    cost[nxt] = nc
          95 +                    came[nxt] = cur
          96 +                    h = abs(nxt[0] - gk[0]) + abs(nxt[1] - gk[1])
          97 +                    heapq.heappush(frontier, (nc + h, nxt))
          98 +        if not found:
          99 +            return [goal]
         100 +        keys, cur = [], gk
         101 +        while cur is not None:
         102 +            keys.append(cur)
         103 +            cur = came[cur]
         104 +        keys.reverse()
         105 +        pts = [to_pos(k) for k in keys[1:]]
         106 +        compact = []
         107 +        for p in pts:
         108 +            if len(compact) >= 2:
         109 +                a, b = compact[-1] - compact[-2], p - compact[-1]
         110 +                if abs(a[0] * b[1] - a[1] * b[0]) < 1e-8:
         111 +                    compact[-1] = p
         112 +                    continue
         113 +            compact.append(p)
         114 +        compact.append(goal)
         115 +        return compact
         116 +
         117 +    def _start_nav(self, s, target_local, next_mode, force_local):
         118 +        self.path = self._plan(s, target_local)
         119 +        self.next_mode = next_mode
         120 +        self.force_local = np.asarray(force_local, dtype=float)
         121 +        self.mode = "nav"
         122 +
         123 +    def _begin_decision(self, s):
         124 +        angle_error = self._wrap(float(s[31] - s[2]))
         125 +        w, lh, lv = float(s[12]), float(s[13]), float(s[14])
         126 +        if abs(angle_error) > 0.065:
         127 +            self.pair_sign = 1.0 if angle_error > 0 else -1.0
         128 +            self.pair_start_theta = float(s[2])
         129 +            self.pair_amount = min(0.22, abs(angle_error))
         130 +            target = [self.pair_sign * 0.40 * lh, -w - 0.20]
         131 +            self._start_nav(s, target, "rot1", [0.0, 0.049])
         132 +            return
         133 +
         134 +        delta_local = self._rot(-float(s[2])).dot(s[29:31] - s[0:2])
         135 +        axis = 0 if abs(delta_local[0]) >= abs(delta_local[1]) else 1
         136 +        component = float(delta_local[axis])
         137 +        if abs(component) < 0.016:
         138 +            axis = 1 - axis
         139 +            component = float(delta_local[axis])
         140 +        sign = 1.0 if component >= 0 else -1.0
         141 +        self.translate_amount = max(0.0, min(0.28, abs(component) - 0.010))
         142 +        if self.translate_amount <= 0.002:
         143 +            self.mode = "idle"
         144 +            return
         145 +        com_y = -(lh * w / 2.0 + lv * w + lv * lv / 2.0) / (lh + lv)
         146 +        if axis == 0:
         147 +            target = [-sign * (w / 2.0 + 0.20), com_y]
         148 +            force = [sign * 0.049, 0.0]
         149 +        elif sign > 0:
         150 +            target = [0.0, -w - lv - 0.20]
         151 +            force = [0.0, 0.049]
         152 +        else:
         153 +            target = [0.0, 0.20]
         154 +            force = [0.0, -0.049]
         155 +        self._start_nav(s, target, "translate", force)
         156 +
         157 +    def _finish_push(self, next_after_retreat):
         158 +        self.mode = "retreat"
         159 +        self.retreat_count = 0
         160 +        self.after_retreat = next_after_retreat
         161 +
         162 +    def _action(self, vec):
         163 +        return np.clip(np.asarray(vec, dtype=float), self.low, self.high)
   21    164  
   22    165      def get_action(self, state):
   23    166          s = np.asarray(state, dtype=float)
   24        -        block = s[0:2]
   25        -        robot = s[16:18]
   26        -        goal = s[29:31]
   27        -        delta = goal - block
   28        -        distance = float(np.linalg.norm(delta))
   29        -        if distance < 1e-9:
   30        -            direction = np.array([1.0, 0.0])
   31        -        else:
   32        -            direction = delta / distance
   33        -        behind = -direction
   34        -        desired_angle = math.atan2(behind[1], behind[0])
   35        -        rel = robot - block
   36        -        radius = float(np.linalg.norm(rel))
   37        -        current_angle = math.atan2(rel[1], rel[0]) if radius > 1e-8 else desired_angle
   38        -        angle_error = self._wrap(desired_angle - current_angle)
   39        -
   40        -        if self.mode == "push":
   41        -            # Periodically re-stage so angular or lateral errors cannot accumulate.
   42        -            target = block + direction * 0.45
   43        -            self.push_steps += 1
   44        -            if self.push_steps >= 35:
   45        -                self.mode = "stage"
   46        -        else:
   47        -            clearance = 0.78
   48        -            # Orbit outside the T's circumscribed radius; direct travel to the
   49        -            # far side would otherwise collide with and rotate the object.
   50        -            if radius < clearance - 0.04:
   51        -                target = block + clearance * np.array([math.cos(current_angle), math.sin(current_angle)])
   52        -            elif abs(angle_error) > 0.055:
   53        -                next_angle = current_angle + float(np.clip(angle_error, -0.10, 0.10))
   54        -                target = block + clearance * np.array([math.cos(next_angle), math.sin(next_angle)])
   55        -            else:
   56        -                target = block + clearance * behind
   57        -                if np.linalg.norm(robot - target) < 0.035:
   58        -                    self.mode = "push"
   59        -                    self.push_steps = 0
   60        -                    target = block + direction * 0.45
   61        -        # The server checks the open interval despite the advertised Box bounds.
   62        -        move = np.clip(target - robot, self.low + 1e-6, self.high - 1e-6)
   63        -        self.step += 1
   64        -        return move.astype(float)
         167 +        if self.mode == "idle":
         168 +            self._begin_decision(s)
         169 +
         170 +        if self.mode == "nav":
         171 +            robot = s[16:18]
         172 +            while self.path and np.linalg.norm(self.path[0] - robot) < 0.028:
         173 +                self.path.pop(0)
         174 +            if self.path:
         175 +                return self._action(self.path[0] - robot)
         176 +            self.mode = self.next_mode
         177 +            self.push_start = s.copy()
         178 +            self.push_count = 0
         179 +
         180 +        if self.mode == "retreat":
         181 +            self.retreat_count += 1
         182 +            force_world = self._rot(float(s[2])).dot(self.force_local)
         183 +            if self.retreat_count >= 5:
         184 +                self.mode = self.after_retreat
         185 +                if self.mode == "rot2nav":
         186 +                    w, lh = float(s[12]), float(s[13])
         187 +                    target = [-self.pair_sign * 0.40 * lh, 0.20]
         188 +                    self._start_nav(s, target, "rot2", [0.0, -0.049])
         189 +                return np.zeros(2, dtype=float)
         190 +            return self._action(-force_world)
         191 +
         192 +        if self.mode == "rot1":
         193 +            signed = self.pair_sign * self._wrap(float(s[2] - self.pair_start_theta))
         194 +            self.push_count += 1
         195 +            if signed >= 0.45 * self.pair_amount or self.push_count >= 14:
         196 +                self._finish_push("rot2nav")
         197 +                return np.zeros(2, dtype=float)
         198 +            return self._action(self._rot(float(s[2])).dot(self.force_local))
         199 +
         200 +        if self.mode == "rot2":
         201 +            signed = self.pair_sign * self._wrap(float(s[2] - self.pair_start_theta))
         202 +            self.push_count += 1
         203 +            if signed >= 0.92 * self.pair_amount or self.push_count >= 14:
         204 +                self._finish_push("idle")
         205 +                return np.zeros(2, dtype=float)
         206 +            return self._action(self._rot(float(s[2])).dot(self.force_local))
         207 +
         208 +        if self.mode == "translate":
         209 +            force_world = self._rot(float(self.push_start[2])).dot(self.force_local)
         210 +            direction = force_world / max(1e-9, np.linalg.norm(force_world))
         211 +            progress = float(np.dot(s[0:2] - self.push_start[0:2], direction))
         212 +            self.push_count += 1
         213 +            if progress >= self.translate_amount or self.push_count >= 18:
         214 +                self._finish_push("idle")
         215 +                return np.zeros(2, dtype=float)
         216 +            remaining = self.translate_amount - max(0.0, progress)
         217 +            scale = min(1.0, max(0.20, remaining / 0.06))
         218 +            return self._action(force_world * scale)
         219 +
         220 +        return np.zeros(2, dtype=float)
```

</details>

<a id="C019"></a>
### C019 · Use accessible center-of-mass rays for faster direct translation

Commit `cc1fc8ace88520e4590daf6ae9aadc82943c0743`; parents: 2fc7f82a1351f900d6caff1f2a01b91a66ee3b1a. Recorded author date: 2026-09-09T08:40:04+02:00.

File roles (automatic): policy.

- [E0059](01_timeline.md#E0059): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C019_cc1fc8a_approach.py) · [Exact all-file diff](evidence/diffs/C019_cc1fc8a.diff)

[Previous saved controller snapshot](evidence/versions/C018_2fc7f82_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 8242f36..a6e92f9 100644
--- a/approach.py
+++ b/approach.py
@@ -111,9 +111,58 @@ class GeneratedApproach:
  111    111                      compact[-1] = p
  112    112                      continue
  113    113              compact.append(p)
  114        -        compact.append(goal)
         114 +        if not self._blocked(s, goal, margin=0.105):
         115 +            compact.append(goal)
  115    116          return compact
  116    117  
         118 +    @staticmethod
         119 +    def _ray_exit(origin, direction, rects):
         120 +        intervals = []
         121 +        for xmin, xmax, ymin, ymax in rects:
         122 +            lo, hi = -1e30, 1e30
         123 +            valid = True
         124 +            for p, d, lower, upper in ((origin[0], direction[0], xmin, xmax),
         125 +                                        (origin[1], direction[1], ymin, ymax)):
         126 +                if abs(d) < 1e-10:
         127 +                    if p < lower or p > upper:
         128 +                        valid = False
         129 +                        break
         130 +                else:
         131 +                    a, b = (lower - p) / d, (upper - p) / d
         132 +                    lo, hi = max(lo, min(a, b)), min(hi, max(a, b))
         133 +            if valid and hi >= max(0.0, lo):
         134 +                intervals.append((max(0.0, lo), hi))
         135 +        intervals.sort()
         136 +        end = 0.0
         137 +        for lo, hi in intervals:
         138 +            if lo <= end + 1e-7:
         139 +                end = max(end, hi)
         140 +        return end
         141 +
         142 +    def _translation_setup(self, s, delta_world):
         143 +        """Choose an accessible force ray through the exact polygon centroid."""
         144 +        w, lh, lv = float(s[12]), float(s[13]), float(s[14])
         145 +        com_y = -(lh * w / 2.0 + lv * w + lv * lv / 2.0) / (lh + lv)
         146 +        com = np.array([0.0, com_y])
         147 +        base_angle = math.atan2(delta_world[1], delta_world[0])
         148 +        rects = [(-lh / 2, lh / 2, -w, 0.0),
         149 +                 (-w / 2, w / 2, -w - lv, -w)]
         150 +        best = None
         151 +        # Angled alternatives are important when the ideal behind point is at a wall.
         152 +        for off in (0.0, 0.30, -0.30, 0.60, -0.60, 0.90, -0.90):
         153 +            dw = np.array([math.cos(base_angle + off), math.sin(base_angle + off)])
         154 +            dl = self._rot(-float(s[2])).dot(dw)
         155 +            q = -dl
         156 +            contact = com + q * self._ray_exit(com, q, rects)
         157 +            stage = contact + q * 0.19
         158 +            sw = self._local_to_world(s, stage)
         159 +            accessible = (0.11 <= sw[0] <= 4.89 and 0.11 <= sw[1] <= 4.89)
         160 +            if accessible:
         161 +                score = float(np.dot(dw, delta_world / max(1e-9, np.linalg.norm(delta_world))))
         162 +                if best is None or score > best[0]:
         163 +                    best = (score, stage, dl)
         164 +        return best
         165 +
  117    166      def _start_nav(self, s, target_local, next_mode, force_local):
  118    167          self.path = self._plan(s, target_local)
  119    168          self.next_mode = next_mode
@@ -126,32 +175,23 @@ class GeneratedApproach:
  126    175          if abs(angle_error) > 0.065:
  127    176              self.pair_sign = 1.0 if angle_error > 0 else -1.0
  128    177              self.pair_start_theta = float(s[2])
  129        -            self.pair_amount = min(0.22, abs(angle_error))
         178 +            self.pair_amount = min(0.45, abs(angle_error))
  130    179              target = [self.pair_sign * 0.40 * lh, -w - 0.20]
  131    180              self._start_nav(s, target, "rot1", [0.0, 0.049])
  132    181              return
  133    182  
  134        -        delta_local = self._rot(-float(s[2])).dot(s[29:31] - s[0:2])
  135        -        axis = 0 if abs(delta_local[0]) >= abs(delta_local[1]) else 1
  136        -        component = float(delta_local[axis])
  137        -        if abs(component) < 0.016:
  138        -            axis = 1 - axis
  139        -            component = float(delta_local[axis])
  140        -        sign = 1.0 if component >= 0 else -1.0
  141        -        self.translate_amount = max(0.0, min(0.28, abs(component) - 0.010))
         183 +        delta_world = s[29:31] - s[0:2]
         184 +        distance = float(np.linalg.norm(delta_world))
         185 +        self.translate_amount = max(0.0, min(0.50, distance - 0.012))
  142    186          if self.translate_amount <= 0.002:
  143    187              self.mode = "idle"
  144    188              return
  145        -        com_y = -(lh * w / 2.0 + lv * w + lv * lv / 2.0) / (lh + lv)
  146        -        if axis == 0:
  147        -            target = [-sign * (w / 2.0 + 0.20), com_y]
  148        -            force = [sign * 0.049, 0.0]
  149        -        elif sign > 0:
  150        -            target = [0.0, -w - lv - 0.20]
  151        -            force = [0.0, 0.049]
  152        -        else:
  153        -            target = [0.0, 0.20]
  154        -            force = [0.0, -0.049]
         189 +        setup = self._translation_setup(s, delta_world)
         190 +        if setup is None:
         191 +            self.mode = "idle"
         192 +            return
         193 +        _, target, direction_local = setup
         194 +        force = direction_local * 0.049
  155    195          self._start_nav(s, target, "translate", force)
  156    196  
  157    197      def _finish_push(self, next_after_retreat):
@@ -192,7 +232,7 @@ class GeneratedApproach:
  192    232          if self.mode == "rot1":
  193    233              signed = self.pair_sign * self._wrap(float(s[2] - self.pair_start_theta))
  194    234              self.push_count += 1
  195        -            if signed >= 0.45 * self.pair_amount or self.push_count >= 14:
         235 +            if signed >= 0.45 * self.pair_amount or self.push_count >= 22:
  196    236                  self._finish_push("rot2nav")
  197    237                  return np.zeros(2, dtype=float)
  198    238              return self._action(self._rot(float(s[2])).dot(self.force_local))
@@ -200,7 +240,7 @@ class GeneratedApproach:
  200    240          if self.mode == "rot2":
  201    241              signed = self.pair_sign * self._wrap(float(s[2] - self.pair_start_theta))
  202    242              self.push_count += 1
  203        -            if signed >= 0.92 * self.pair_amount or self.push_count >= 14:
         243 +            if signed >= 0.92 * self.pair_amount or self.push_count >= 22:
  204    244                  self._finish_push("idle")
  205    245                  return np.zeros(2, dtype=float)
  206    246              return self._action(self._rot(float(s[2])).dot(self.force_local))
@@ -210,7 +250,7 @@ class GeneratedApproach:
  210    250              direction = force_world / max(1e-9, np.linalg.norm(force_world))
  211    251              progress = float(np.dot(s[0:2] - self.push_start[0:2], direction))
  212    252              self.push_count += 1
  213        -            if progress >= self.translate_amount or self.push_count >= 18:
         253 +            if progress >= self.translate_amount or self.push_count >= 28:
  214    254                  self._finish_push("idle")
  215    255                  return np.zeros(2, dtype=float)
  216    256              remaining = self.translate_amount - max(0.0, progress)
```

</details>

<a id="C020"></a>
### C020 · Accelerate manipulation and handle angle branch-cut termination

Commit `0b98261ff7aa84974ad2e8528672e678cbf30f36`; parents: cc1fc8ace88520e4590daf6ae9aadc82943c0743. Recorded author date: 2026-09-09T08:41:28+02:00.

File roles (automatic): policy.

- [E0065](01_timeline.md#E0065): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C020_0b98261_approach.py) · [Exact all-file diff](evidence/diffs/C020_0b98261.diff)

[Previous saved controller snapshot](evidence/versions/C019_cc1fc8a_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index a6e92f9..5e35252 100644
--- a/approach.py
+++ b/approach.py
@@ -170,19 +170,26 @@ class GeneratedApproach:
  170    170          self.mode = "nav"
  171    171  
  172    172      def _begin_decision(self, s):
  173        -        angle_error = self._wrap(float(s[31] - s[2]))
         173 +        raw_angle_error = float(s[31] - s[2])
         174 +        angle_error = self._wrap(raw_angle_error)
  174    175          w, lh, lv = float(s[12]), float(s[13]), float(s[14])
  175        -        if abs(angle_error) > 0.065:
         176 +        # The environment compares the displayed [-pi,pi] angles directly.
         177 +        # If equivalent poses straddle that branch cut, deliberately cross it.
         178 +        branch_mismatch = abs(raw_angle_error) > math.pi
         179 +        if abs(angle_error) > 0.11 or branch_mismatch:
  176    180              self.pair_sign = 1.0 if angle_error > 0 else -1.0
         181 +            if abs(angle_error) < 1e-4:
         182 +                self.pair_sign = 1.0 if raw_angle_error < 0 else -1.0
  177    183              self.pair_start_theta = float(s[2])
  178        -            self.pair_amount = min(0.45, abs(angle_error))
         184 +            wanted = abs(angle_error) + (0.055 if branch_mismatch else 0.0)
         185 +            self.pair_amount = min(0.70, wanted)
  179    186              target = [self.pair_sign * 0.40 * lh, -w - 0.20]
  180    187              self._start_nav(s, target, "rot1", [0.0, 0.049])
  181    188              return
  182    189  
  183    190          delta_world = s[29:31] - s[0:2]
  184    191          distance = float(np.linalg.norm(delta_world))
  185        -        self.translate_amount = max(0.0, min(0.50, distance - 0.012))
         192 +        self.translate_amount = max(0.0, min(0.75, distance - 0.012))
  186    193          if self.translate_amount <= 0.002:
  187    194              self.mode = "idle"
  188    195              return
@@ -232,7 +239,7 @@ class GeneratedApproach:
  232    239          if self.mode == "rot1":
  233    240              signed = self.pair_sign * self._wrap(float(s[2] - self.pair_start_theta))
  234    241              self.push_count += 1
  235        -            if signed >= 0.45 * self.pair_amount or self.push_count >= 22:
         242 +            if signed >= 0.45 * self.pair_amount or self.push_count >= 28:
  236    243                  self._finish_push("rot2nav")
  237    244                  return np.zeros(2, dtype=float)
  238    245              return self._action(self._rot(float(s[2])).dot(self.force_local))
@@ -240,7 +247,7 @@ class GeneratedApproach:
  240    247          if self.mode == "rot2":
  241    248              signed = self.pair_sign * self._wrap(float(s[2] - self.pair_start_theta))
  242    249              self.push_count += 1
  243        -            if signed >= 0.92 * self.pair_amount or self.push_count >= 22:
         250 +            if signed >= 0.92 * self.pair_amount or self.push_count >= 28:
  244    251                  self._finish_push("idle")
  245    252                  return np.zeros(2, dtype=float)
  246    253              return self._action(self._rot(float(s[2])).dot(self.force_local))
```

</details>

<a id="C021"></a>
### C021 · Use diagonal routing and defer orientation cleanup during translation

Commit `cf6854bbfda542a0e87b219dbed6d63c2af2295d`; parents: 0b98261ff7aa84974ad2e8528672e678cbf30f36. Recorded author date: 2026-09-09T08:42:42+02:00.

File roles (automatic): policy.

- [E0071](01_timeline.md#E0071): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C021_cf6854b_approach.py) · [Exact all-file diff](evidence/diffs/C021_cf6854b.diff)

[Previous saved controller snapshot](evidence/versions/C020_0b98261_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 5e35252..bb2a059 100644
--- a/approach.py
+++ b/approach.py
@@ -32,6 +32,7 @@ class GeneratedApproach:
   32     32          self.pair_start_theta = 0.0
   33     33          self.pair_amount = 0.0
   34     34          self.translate_amount = 0.0
          35 +        self.has_oriented = False
   35     36  
   36     37      def _local_to_world(self, s, point):
   37     38          return s[0:2] + self._rot(float(s[2])).dot(np.asarray(point, dtype=float))
@@ -84,16 +85,19 @@ class GeneratedApproach:
   84     85              if cur == gk:
   85     86                  found = True
   86     87                  break
   87        -            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
          88 +            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1),
          89 +                           (1, 1), (1, -1), (-1, 1), (-1, -1)):
   88     90                  nxt = (cur[0] + dx, cur[1] + dy)
   89     91                  p = to_pos(nxt)
   90        -                if nxt != sk and self._blocked(s, p):
          92 +                midpoint = (to_pos(cur) + p) * 0.5
          93 +                if nxt != sk and (self._blocked(s, p) or self._blocked(s, midpoint)):
   91     94                      continue
   92        -                nc = cost[cur] + 1.0
          95 +                nc = cost[cur] + (1.41421356237 if dx and dy else 1.0)
   93     96                  if nxt not in cost or nc < cost[nxt]:
   94     97                      cost[nxt] = nc
   95     98                      came[nxt] = cur
   96        -                    h = abs(nxt[0] - gk[0]) + abs(nxt[1] - gk[1])
          99 +                    ax, ay = abs(nxt[0] - gk[0]), abs(nxt[1] - gk[1])
         100 +                    h = max(ax, ay) + 0.41421356237 * min(ax, ay)
   97    101                      heapq.heappush(frontier, (nc + h, nxt))
   98    102          if not found:
   99    103              return [goal]
@@ -173,10 +177,12 @@ class GeneratedApproach:
  173    177          raw_angle_error = float(s[31] - s[2])
  174    178          angle_error = self._wrap(raw_angle_error)
  175    179          w, lh, lv = float(s[12]), float(s[13]), float(s[14])
         180 +        distance = float(np.linalg.norm(s[29:31] - s[0:2]))
  176    181          # The environment compares the displayed [-pi,pi] angles directly.
  177    182          # If equivalent poses straddle that branch cut, deliberately cross it.
  178    183          branch_mismatch = abs(raw_angle_error) > math.pi
  179        -        if abs(angle_error) > 0.11 or branch_mismatch:
         184 +        should_orient = (not self.has_oriented) or distance < 0.15
         185 +        if should_orient and (abs(angle_error) > 0.11 or branch_mismatch):
  180    186              self.pair_sign = 1.0 if angle_error > 0 else -1.0
  181    187              if abs(angle_error) < 1e-4:
  182    188                  self.pair_sign = 1.0 if raw_angle_error < 0 else -1.0
@@ -187,8 +193,10 @@ class GeneratedApproach:
  187    193              self._start_nav(s, target, "rot1", [0.0, 0.049])
  188    194              return
  189    195  
         196 +        if abs(angle_error) <= 0.125 and not branch_mismatch:
         197 +            self.has_oriented = True
         198 +
  190    199          delta_world = s[29:31] - s[0:2]
  191        -        distance = float(np.linalg.norm(delta_world))
  192    200          self.translate_amount = max(0.0, min(0.75, distance - 0.012))
  193    201          if self.translate_amount <= 0.002:
  194    202              self.mode = "idle"
```

</details>

<a id="C022"></a>
### C022 · Recover navigation from wall-limited waypoints

Commit `7d6d4eda7384fa652399a4a6bee2a1d0a372700b`; parents: cf6854bbfda542a0e87b219dbed6d63c2af2295d. Recorded author date: 2026-09-09T08:44:15+02:00.

File roles (automatic): policy.

- [E0081](01_timeline.md#E0081): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C022_7d6d4ed_approach.py) · [Exact all-file diff](evidence/diffs/C022_7d6d4ed.diff)

[Previous saved controller snapshot](evidence/versions/C021_cf6854b_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index bb2a059..6a538b5 100644
--- a/approach.py
+++ b/approach.py
@@ -33,6 +33,8 @@ class GeneratedApproach:
   33     33          self.pair_amount = 0.0
   34     34          self.translate_amount = 0.0
   35     35          self.has_oriented = False
          36 +        self.nav_last_distance = None
          37 +        self.nav_stall = 0
   36     38  
   37     39      def _local_to_world(self, s, point):
   38     40          return s[0:2] + self._rot(float(s[2])).dot(np.asarray(point, dtype=float))
@@ -172,6 +174,8 @@ class GeneratedApproach:
  172    174          self.next_mode = next_mode
  173    175          self.force_local = np.asarray(force_local, dtype=float)
  174    176          self.mode = "nav"
         177 +        self.nav_last_distance = None
         178 +        self.nav_stall = 0
  175    179  
  176    180      def _begin_decision(self, s):
  177    181          raw_angle_error = float(s[31] - s[2])
@@ -227,6 +231,20 @@ class GeneratedApproach:
  227    231              while self.path and np.linalg.norm(self.path[0] - robot) < 0.028:
  228    232                  self.path.pop(0)
  229    233              if self.path:
         234 +                waypoint_distance = float(np.linalg.norm(self.path[0] - robot))
         235 +                if (self.nav_last_distance is not None and
         236 +                        abs(waypoint_distance - self.nav_last_distance) < 1e-5):
         237 +                    self.nav_stall += 1
         238 +                else:
         239 +                    self.nav_stall = 0
         240 +                self.nav_last_distance = waypoint_distance
         241 +                # Walls and residual contact can make a geometrically exact
         242 +                # waypoint unreachable; accept the closest physical point.
         243 +                if self.nav_stall >= 7:
         244 +                    self.path.pop(0)
         245 +                    self.nav_last_distance = None
         246 +                    self.nav_stall = 0
         247 +                    return np.zeros(2, dtype=float)
  230    248                  return self._action(self.path[0] - robot)
  231    249              self.mode = self.next_mode
  232    250              self.push_start = s.copy()
```

</details>

<a id="C023"></a>
### C023 · Preposition long blocks for wall-safe rotation

Commit `a3e7cd5b308992fe7c6cea88f748faeaecb61bb9`; parents: 7d6d4eda7384fa652399a4a6bee2a1d0a372700b. Recorded author date: 2026-09-09T08:45:38+02:00.

File roles (automatic): policy.

- [E0086](01_timeline.md#E0086): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C023_a3e7cd5_approach.py) · [Exact all-file diff](evidence/diffs/C023_a3e7cd5.diff)

[Previous saved controller snapshot](evidence/versions/C022_7d6d4ed_approach.py) — not the first-ever controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 6a538b5..1a8cedf 100644
--- a/approach.py
+++ b/approach.py
@@ -44,7 +44,7 @@ class GeneratedApproach:
   44     44  
   45     45      def _blocked(self, s, world, margin=0.14):
   46     46          xw, yw = world
   47        -        if xw < 0.105 or xw > 4.895 or yw < 0.105 or yw > 4.895:
          47 +        if xw < 0.125 or xw > 4.875 or yw < 0.125 or yw > 4.875:
   48     48              return True
   49     49          x, y = self._world_to_local(s, world)
   50     50          w, lh, lv = float(s[12]), float(s[13]), float(s[14])
@@ -162,7 +162,7 @@ class GeneratedApproach:
  162    162              contact = com + q * self._ray_exit(com, q, rects)
  163    163              stage = contact + q * 0.19
  164    164              sw = self._local_to_world(s, stage)
  165        -            accessible = (0.11 <= sw[0] <= 4.89 and 0.11 <= sw[1] <= 4.89)
         165 +            accessible = (0.13 <= sw[0] <= 4.87 and 0.13 <= sw[1] <= 4.87)
  166    166              if accessible:
  167    167                  score = float(np.dot(dw, delta_world / max(1e-9, np.linalg.norm(delta_world))))
  168    168                  if best is None or score > best[0]:
@@ -186,21 +186,29 @@ class GeneratedApproach:
  186    186          # If equivalent poses straddle that branch cut, deliberately cross it.
  187    187          branch_mismatch = abs(raw_angle_error) > math.pi
  188    188          should_orient = (not self.has_oriented) or distance < 0.15
         189 +        preposition_delta = None
  189    190          if should_orient and (abs(angle_error) > 0.11 or branch_mismatch):
  190        -            self.pair_sign = 1.0 if angle_error > 0 else -1.0
  191        -            if abs(angle_error) < 1e-4:
  192        -                self.pair_sign = 1.0 if raw_angle_error < 0 else -1.0
  193        -            self.pair_start_theta = float(s[2])
  194        -            wanted = abs(angle_error) + (0.055 if branch_mismatch else 0.0)
  195        -            self.pair_amount = min(0.70, wanted)
  196        -            target = [self.pair_sign * 0.40 * lh, -w - 0.20]
  197        -            self._start_nav(s, target, "rot1", [0.0, 0.049])
  198        -            return
         191 +            # First ensure the full stem can sweep without striking a wall.
         192 +            clearance = min(1.55, lv + w + 0.20)
         193 +            anchor = np.clip(s[0:2], clearance, 5.0 - clearance)
         194 +            if np.linalg.norm(anchor - s[0:2]) > 0.055:
         195 +                preposition_delta = anchor - s[0:2]
         196 +            else:
         197 +                self.pair_sign = 1.0 if angle_error > 0 else -1.0
         198 +                if abs(angle_error) < 1e-4:
         199 +                    self.pair_sign = 1.0 if raw_angle_error < 0 else -1.0
         200 +                self.pair_start_theta = float(s[2])
         201 +                wanted = abs(angle_error) + (0.055 if branch_mismatch else 0.0)
         202 +                self.pair_amount = min(0.70, wanted)
         203 +                target = [self.pair_sign * 0.40 * lh, -w - 0.20]
         204 +                self._start_nav(s, target, "rot1", [0.0, 0.049])
         205 +                return
  199    206  
  200    207          if abs(angle_error) <= 0.125 and not branch_mismatch:
  201    208              self.has_oriented = True
  202    209  
  203        -        delta_world = s[29:31] - s[0:2]
         210 +        delta_world = (preposition_delta if preposition_delta is not None
         211 +                       else s[29:31] - s[0:2])
  204    212          self.translate_amount = max(0.0, min(0.75, distance - 0.012))
  205    213          if self.translate_amount <= 0.002:
  206    214              self.mode = "idle"
@@ -241,9 +249,10 @@ class GeneratedApproach:
  241    249                  # Walls and residual contact can make a geometrically exact
  242    250                  # waypoint unreachable; accept the closest physical point.
  243    251                  if self.nav_stall >= 7:
  244        -                    self.path.pop(0)
         252 +                    self.path = []
  245    253                      self.nav_last_distance = None
  246    254                      self.nav_stall = 0
         255 +                    self.mode = "idle"
  247    256                      return np.zeros(2, dtype=float)
  248    257                  return self._action(self.path[0] - robot)
  249    258              self.mode = self.next_mode
```

</details>

<a id="C024"></a>
### C024 · Allow small final orientation corrections at valid goal poses

Commit `96336670221c7b16483ff9c8cf87139d1bcb8fae`; parents: a3e7cd5b308992fe7c6cea88f748faeaecb61bb9. Recorded author date: 2026-09-09T08:46:40+02:00.

File roles (automatic): policy.

- [E0092](01_timeline.md#E0092): commit title in command; output may not confirm creation.
[Controller after this commit](evidence/versions/C024_9633667_approach.py) · [Exact all-file diff](evidence/diffs/C024_9633667.diff)

[Previous saved controller snapshot](evidence/versions/C023_a3e7cd5_approach.py) — not the first-ever controller.

This controller snapshot is byte-identical to the final saved controller.

<details>
<summary>Show every changed line with OLD and NEW line numbers</summary>

```text
 OLD   NEW   CHANGE
diff --git a/approach.py b/approach.py
index 1a8cedf..45af65d 100644
--- a/approach.py
+++ b/approach.py
@@ -191,7 +191,7 @@ class GeneratedApproach:
  191    191              # First ensure the full stem can sweep without striking a wall.
  192    192              clearance = min(1.55, lv + w + 0.20)
  193    193              anchor = np.clip(s[0:2], clearance, 5.0 - clearance)
  194        -            if np.linalg.norm(anchor - s[0:2]) > 0.055:
         194 +            if not self.has_oriented and np.linalg.norm(anchor - s[0:2]) > 0.055:
  195    195                  preposition_delta = anchor - s[0:2]
  196    196              else:
  197    197                  self.pair_sign = 1.0 if angle_error > 0 else -1.0
```

</details>

