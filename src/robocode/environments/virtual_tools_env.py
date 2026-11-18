"""The Virtual Tools Game (Allen, Smith & Tenenbaum, PNAS 2020) as an environment.

Each episode is one level. A step is one placement: choose one of three tools and a
point to drop it. An accepted placement runs the game's physics for up to 20 seconds;
the episode ends when the goal condition is met (terminated) or after
``max_attempts`` accepted placements without success (truncated), 10 as in the paper.
A placement that overlaps something is rejected without running the physics and uses
no attempt, which matches the human game, where such a click is not taken. Rejected
placements are capped (``max_rejected_placements``) so a program cannot loop forever.

Physics: placements run in the game's own JavaScript engine through
:mod:`robocode.environments.tool_games`. Replaying the 9,077 recorded human
placements on the 28 levels reproduces 99.8% of their outcomes: every human success,
plus 2 failures that the engine scores as successes, and 16 placements that touch an
object exactly and are rejected. See ``docs/virtual_tools.md``.

Levels and the count contract: the levels are fixed, hand-made scenes, so the
:class:`VariableCountEnv` "object count" is reused as a **level index**. ``levels``
fixes the index order; ``options={"object_count": k}`` loads level ``k``.
``design_counts`` are the development levels (``dev_levels``) and ``eval_counts``
are all levels, so with ``num_eval_tasks`` equal to the number of levels the runner
evaluates every level once and reports development vs. held-out solve rates as its
``design``/``held_out`` count regimes. The black-box env server calls
:meth:`restrict_to_synthesis`, after which held-out levels refuse to load, so the agent
never sees them. The level index is deliberately absent from observations and
``info`` (unlike the count contract's ``info["object_count"]``): a program that could
read it could look up memorized placements instead of solving the scene. The runner's
per-level breakdown comes from its own schedule, not from ``info``.
"""

from __future__ import annotations

import copy
import hashlib
import json
import math
from typing import Any, SupportsFloat, cast

import numpy as np
from gymnasium.core import RenderFrame
from gymnasium.spaces import Box
from numpy.typing import NDArray

from robocode.environments.tool_games import TRIALS_DIR, ToolPicker, require_node
from robocode.environments.variable_count import VariableCountEnv
from robocode.environments.virtual_tools_render import render_observation
from robocode.utils.json_dict_space import JSONDictSpace

_Obs = dict[str, Any]
_Action = NDArray[np.float64]

# ToolPicker's defaults, used for every simulation: paths are sampled every 0.1 s and
# a placement is simulated for at most 20 s (it stops early once the goal is met).
PATH_DT = 0.1
MAX_SIM_TIME = 20.0
NUM_TOOLS = 3
WORLD_SIZE = 600.0

_OBS_SUMMARY = (
    "Dict with keys: world (the level: objects, goal condition gcond, placement-blocked "
    "regions), tools (3 tools, each a list of polygons relative to the placement "
    "point), max_attempts, attempts_used, max_rejected_placements, "
    "rejected_placements, solved, path_dt, history (one entry per placement with the "
    "recorded object paths). The environment description documents every field."
)


class VirtualToolsEnv(VariableCountEnv[_Obs, _Action]):
    """Place one of three tools to make the goal condition true."""

    metadata = {"render_modes": ["rgb_array"]}

    def __init__(
        self,
        levels: list[str],
        dev_levels: list[str] | None = None,
        max_attempts: int = 10,
        max_rejected_placements: int = 20,
        hold_out_from_synthesis: bool = True,
        prompt_note: str | None = None,
    ) -> None:
        """``levels`` are level files relative to the game's ``Trials`` directory (e.g.
        ``"Original/Catapult"``), in level-index order.

        ``dev_levels`` (default:
        all) are the levels available while the program is developed.

        ``prompt_note`` (default: none) is extra text for the agent, added as its own
        paragraph after the description's account of the levels; it changes nothing
        else. ``virtual_tools_generalize.yaml`` uses it.
        """
        super().__init__()
        require_node()
        if not levels or len(set(levels)) != len(levels):
            raise ValueError("levels must be a non-empty list without duplicates")
        dev = list(levels) if dev_levels is None else list(dev_levels)
        unknown = sorted(set(dev) - set(levels))
        if unknown or not dev:
            raise ValueError(
                f"dev_levels must be a non-empty subset of levels: {unknown}"
            )
        if max_attempts < 1 or max_rejected_placements < 1:
            raise ValueError("max_attempts and max_rejected_placements must be >= 1")
        self._levels = list(levels)
        self._design = sorted(self._levels.index(name) for name in dev)
        self._max_attempts = max_attempts
        self._max_rejected = max_rejected_placements
        self._hold_out = hold_out_from_synthesis
        self._prompt_note = " ".join(prompt_note.split()) if prompt_note else None
        self._restricted = False
        self._games = [_load_level(name) for name in self._levels]
        # float64, not float32: the sandbox client casts actions to this dtype while
        # the evaluation harness passes the program's action as it is, and float32
        # rounding moves a point by up to ~3e-5 px, enough to flip a placement that
        # rests exactly on a surface between accepted and rejected.
        self.action_space = Box(
            low=np.array([0.0, 0.0, 0.0]),
            high=np.array([float(NUM_TOOLS), WORLD_SIZE, WORLD_SIZE]),
            dtype=np.float64,
        )
        self.observation_space = JSONDictSpace(_OBS_SUMMARY)
        self._state: _Obs | None = None
        self._level_index: int | None = None
        self._pickers: dict[str, Any] = {}

    # ------------------------------------------------------------------ contract
    @property
    def design_counts(self) -> list[int]:
        return list(self._design)

    @property
    def eval_counts(self) -> list[int]:
        return list(range(len(self._levels)))

    @property
    def current_count(self) -> int:
        assert self._level_index is not None, "Must call reset()"
        return self._level_index

    def max_steps_for_count(self, count: int) -> int:
        # Every step either uses an attempt or a rejected placement, and the env
        # truncates once either budget is spent.
        return self._max_attempts + self._max_rejected

    def restrict_to_synthesis(self) -> None:
        if self._hold_out:
            self._restricted = True

    @property
    def levels(self) -> list[str]:
        """Level names in index order (host-side only; never sent to the agent)."""
        return list(self._levels)

    # ------------------------------------------------------------------ gym API
    def reset(
        self, *, seed: int | None = None, options: dict[str, Any] | None = None
    ) -> tuple[_Obs, dict[str, Any]]:
        super().reset(seed=seed)
        requested = (options or {}).get("object_count")
        if requested is None:
            index = int(self.np_random.choice(self._design))
        else:
            index = int(requested)
            if not 0 <= index < len(self._levels):
                raise ValueError(
                    f"level index {index} out of range 0..{len(self._levels) - 1}"
                )
            if self._restricted and index not in self._design:
                raise ValueError(
                    f"level {index} is held out for evaluation; the development "
                    f"levels are {self._design}"
                )
        self._level_index = index
        game = self._games[index]
        self._state = {
            "world": copy.deepcopy(game["world"]),
            "tools": copy.deepcopy(game["tools"]),
            "max_attempts": self._max_attempts,
            "attempts_used": 0,
            "max_rejected_placements": self._max_rejected,
            "rejected_placements": 0,
            "solved": False,
            "path_dt": PATH_DT,
            "history": [],
        }
        return self.get_state(), {}

    def step(
        self, action: _Action
    ) -> tuple[_Obs, SupportsFloat, bool, bool, dict[str, Any]]:
        assert self._state is not None, "Must call reset() before step()"
        state = self._state
        if _is_over(state):
            raise RuntimeError("The episode is over; call reset() first")
        tool, x, y = _decode_action(action)
        entry: dict[str, Any] = {"tool": tool, "position": [x, y], "accepted": False}
        outcome = self._picker(state).observeFullPlacementPath(
            _tool_name(tool), (x, y), maxtime=MAX_SIM_TIME
        )
        if outcome[0] is None:
            # Overlaps or touches an object, lies in a blocked region, or is outside
            # the world: the game does not take the placement.
            state["rejected_placements"] += 1
            reward = 0.0
        else:
            paths, success, sim_time = outcome[0], bool(outcome[1]), outcome[2]
            entry.update(
                accepted=True,
                success=success,
                sim_time=float(sim_time),
                paths={
                    name: {"pos": path[0], "rot": path[1]}
                    for name, path in paths.items()
                },
            )
            state["attempts_used"] += 1
            state["solved"] = success
            reward = -1.0
        # JSON-normalize so the program sees exactly what crosses the wire.
        state["history"].append(json.loads(json.dumps(entry)))
        terminated = bool(state["solved"])
        truncated = not terminated and _is_over(state)
        info = {"accepted": entry["accepted"], "success": terminated}
        return self.get_state(), reward, terminated, truncated, info

    def get_state(self) -> _Obs:
        assert self._state is not None, "Must call reset()"
        return copy.deepcopy(self._state)

    def set_state(self, state: _Obs) -> None:
        missing = {"world", "tools", "history", "attempts_used"} - set(state)
        if missing:
            raise ValueError(f"Not a Virtual Tools state; missing {sorted(missing)}")
        self._state = copy.deepcopy(state)

    def render(self) -> RenderFrame | list[RenderFrame] | None:
        assert self._state is not None, "Must call reset()"
        return cast(RenderFrame, render_observation(self._state))

    # ------------------------------------------------------------------ internals
    def _picker(self, state: _Obs) -> Any:
        """The game's simulator for this state's level (one per distinct scene)."""
        scene = {"world": state["world"], "tools": state["tools"]}
        key = hashlib.sha1(
            json.dumps(scene, sort_keys=True).encode("utf-8")
        ).hexdigest()
        if key not in self._pickers:
            gamedict = {
                "world": copy.deepcopy(state["world"]),
                "tools": {_tool_name(i): t for i, t in enumerate(state["tools"])},
            }
            # checkThruPy=False: the placement check runs in the JS engine too; the
            # package's pymunk copy of the world is never built (see tool_games).
            self._pickers[key] = ToolPicker(gamedict, checkThruPy=False)
        return self._pickers[key]

    # ------------------------------------------------------------------ descriptions
    @property
    def env_description(self) -> str:
        return _describe(
            len(self._levels),
            self._design,
            self._max_attempts,
            self._max_rejected,
            self._prompt_note,
        )

    @property
    def env_description_blackbox(self) -> str:
        return self.env_description


def _tool_name(index: int) -> str:
    return f"obj{index + 1}"


def _decode_action(action: Any) -> tuple[int, float, float]:
    values = np.asarray(action, dtype=np.float64).reshape(-1)
    if values.shape != (3,):
        raise ValueError(f"action must have 3 entries [tool, x, y], got {values.shape}")
    if not np.all(np.isfinite(values)):
        raise ValueError(
            f"action entries must be finite numbers, got {values.tolist()}"
        )
    tool = int(np.clip(math.floor(values[0]), 0, NUM_TOOLS - 1))
    return tool, float(values[1]), float(values[2])


def _is_over(state: _Obs) -> bool:
    return bool(
        state["solved"]
        or state["attempts_used"] >= state["max_attempts"]
        or state["rejected_placements"] >= state["max_rejected_placements"]
    )


# Level fields that are numbers. One level file (Validation/Falling_v2) stores some
# of them as text ("1", "0.5"); the game's JavaScript engine converts them, so the
# physics is unaffected (all 300 recorded human placements on that level give the
# same outcomes and paths either way), but a program reading the observation would
# meet text where every other level, and the description, has numbers.
_NUMERIC_KEYS = ("density", "friction", "elasticity", "duration")


def _load_level(name: str) -> dict[str, Any]:
    """Read a level file; tools become a list in the game's tool order."""
    path = TRIALS_DIR / f"{name}.json"
    if not path.is_file():
        raise FileNotFoundError(f"No Virtual Tools level {name!r} at {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    names = data.get("toolNames") or sorted(data["tools"])
    if len(names) != NUM_TOOLS:
        raise ValueError(f"Level {name!r} has {len(names)} tools, expected {NUM_TOOLS}")
    if [float(d) for d in data["world"]["dims"]] != [WORLD_SIZE, WORLD_SIZE]:
        raise ValueError(f"Level {name!r} is not {WORLD_SIZE:g}x{WORLD_SIZE:g}")
    world = data["world"]
    for entry in [*world["objects"].values(), world.get("defaults"), world["gcond"]]:
        for key in _NUMERIC_KEYS:
            if isinstance(entry, dict) and isinstance(entry.get(key), str):
                entry[key] = float(entry[key])
    return {"world": world, "tools": [data["tools"][n] for n in names]}


def _index_list(indices: list[int]) -> str:
    """``0-17`` for a contiguous run of indices, else the list itself."""
    if len(indices) > 2 and indices == list(range(indices[0], indices[-1] + 1)):
        return f"{indices[0]}-{indices[-1]}"
    return ", ".join(str(i) for i in indices)


def _describe(
    num_levels: int,
    design: list[int],
    max_attempts: int,
    max_rejected: int,
    note: str | None = None,
) -> str:
    held_out = num_levels - len(design)
    note_text = f"\n\n{note}" if note else ""
    design_text = _index_list(design)
    if held_out:
        levels_eval = (
            "Evaluation runs your program once on every level, indices "
            f"0-{num_levels - 1}: the {len(design)} development levels and "
            f"{held_out} more levels that you "
            "cannot load now. The new levels use the same kinds of objects, tools and "
            "goal conditions in new arrangements, so a program that remembers "
            "placements for the development levels will fail them: it has to work out "
            "a placement from the observation."
        )
    else:
        levels_eval = "Evaluation runs your program once on each of these levels."
    return f"""\
# Virtual Tools

A 2D physics puzzle game. Each level is a scene of fixed and movable objects plus a
goal condition, for example "get the red ball into the green container". You act by
choosing one of three tools (rigid shapes) and a point to drop it. The tool appears
there and the physics runs for up to {MAX_SIM_TIME:g} seconds: gravity pulls everything
that can move, including your tool. If the goal condition becomes true in that time,
the level is solved. If not, the scene goes back to its initial state and you may try
again, up to {max_attempts} counted attempts per level.

## Actions

`action` is a float array of shape (3,): `[tool, x, y]`.

- `tool` selects the tool: `floor(tool)` clipped to 0..2, so values in [0, 1) select
  tool 0, [1, 2) tool 1, and [2, 3] tool 2.
- `(x, y)` is the placement point in world coordinates. A tool's polygons are given
  relative to this point.
- All three entries must be finite numbers; a NaN or infinite entry raises an error.

A placement is **rejected** if any of the tool's polygons would overlap or touch an
object, would lie in a placement-blocked region (`world["blocks"]`), or if the point
is not strictly inside the world (0 < x < 600 and 0 < y < 600). A rejected placement
runs no physics and uses no attempt, but at most {max_rejected} rejected placements are
allowed per episode.

## Episode

- `env.reset()` starts a level; every `env.step(action)` is one placement.
- Reward: -1 for every accepted placement (so an episode's total reward is minus the
  number of attempts it used) and 0 for a rejected one.
- `terminated` becomes true when the goal condition is met. `truncated` becomes true
  after {max_attempts} accepted placements without success, or after {max_rejected}
  rejected placements.
- Every attempt starts from the level's initial scene: earlier attempts change nothing
  in the world. They remain visible only in the observation's `history`.
- The physics is deterministic: the same placement in the same level always gives the
  same outcome.
- `info` is `{{"accepted": bool, "success": bool}}`.
- Simulating one accepted placement takes about 0.2 s on the environment server.

## Observation

A dict of JSON values (strings, numbers, booleans, lists, dicts), the same during
development and at evaluation:

- `world`: the level, in the game's own level format (described below). It does not
  change during an episode.
- `tools`: a list of 3 tools; the list index is the action's tool index. Each tool is
  a list of convex polygons, and each polygon a list of `[x, y]` vertices relative to
  the placement point.
- `max_attempts`, `attempts_used`, `max_rejected_placements`, `rejected_placements`,
  and `solved`.
- `path_dt`: {PATH_DT:g}, the sampling interval (seconds) of recorded paths.
- `history`: one entry per step so far, oldest first, with `tool`, `position`
  (`[x, y]`) and `accepted`. An accepted entry also has:
  - `success` and `sim_time` (seconds simulated; below {MAX_SIM_TIME:g} means it stopped
    early because the goal was met);
  - `paths`: for every object that moved, including your tool under the name
    `"PLACED"`, `{{"pos": [[x, y], ...], "rot": [angle, ...]}}` sampled every `path_dt`
    seconds from t = 0. `pos` is the object's body position and `rot` its rotation in
    radians, counter-clockwise. The object's shape at sample k is its initial shape
    rotated by `rot[k] - rot[0]` about `pos[0]` and then moved to `pos[k]`.

### Level format (`world`)

- Units are pixels. The origin is the bottom-left corner and y points up; `dims` is
  `[600, 600]`. `gravity` is the strength of gravity (pixels/s^2), pulling toward -y.
- `objects` maps a name to an object whose `type` is one of:
  - `Poly`: a convex polygon with `vertices` in world coordinates;
  - `Ball`: a circle with `position` and `radius`;
  - `Compound`: one rigid body made of several convex polygons, `polys`;
  - `Container`: a cup-shaped wall, the polyline `points` with wall thickness `width`;
  - `Goal`: a polygon region, `vertices`, that objects pass through (not solid).
  An object with `density` 0 is fixed in place; any other object moves. Objects may
  set `friction`, `elasticity` and `density`; missing values come from
  `world["defaults"]`. `color` is cosmetic, but it follows the game's convention:
  objects to get into a goal are usually red and goal regions green.
- `blocks` maps a name to a region (`vertices`) where tools may not be placed. Blocks
  are not solid: objects move through them.
- `gcond` is the goal condition, one of:
  - `SpecificInGoal`: object `obj` stays inside goal object `goal` for `duration`
    seconds;
  - `ManyInGoal`: the objects in `objlist` count; the timer starts when one of them
    enters `goal` and resets when none is inside, and the level is solved once it
    reaches `duration` seconds;
  - `SpecificTouch`: object `obj` touches object `goal` (for `duration` seconds; 0
    means any touch).
  Inside a `Container` means within the region its `points` enclose.

## Levels

`env.reset(seed=s)` loads one of the development levels, chosen by the seed.
`env.reset(seed=s, options={{"object_count": k}})` loads level `k`: in this environment
the `object_count` option, and the `object_count` argument of the render tools, is a
level index. The development levels are indices {design_text}. {levels_eval}{note_text}

Rendering an observation draws the scene, the latest placement's object trajectories
and final positions (a rejected placement is outlined in red), and numbered markers
for earlier placements.
"""
