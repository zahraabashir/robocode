# Virtual Tools

The Virtual Tools Game (Allen, Smith & Tenenbaum, *PNAS* 2020) as a robocode
environment: `environment=virtual_tools`. Each episode is one level of the paper. The
agent drops one of three tools somewhere in the scene, physics runs, and the level is
solved if the goal condition becomes true, within at most 10 attempts per level. The
synthesized program sees the level and every earlier attempt's outcome, so it can
plan a placement, observe what happened, and revise.

Only the strict black box has been exercised so far. Source access and legacy black
box are wired but untested (see [Limits](#limits)).

## Setup

The game's code and levels are the `third-party/tool-games` submodule
(k-r-allen/tool-games, pinned). Its physics engine is JavaScript, so the **host**
needs node.js; a strict sandbox needs nothing new.

```bash
git submodule update --init third-party/tool-games
uv sync --extra virtualtools        # PyExecJS, the Python-to-node bridge
node --version                      # any recent node.js on PATH
pytest tests/environments/test_virtual_tools_env.py
```

## Running the strict black box

```bash
python experiments/run_experiment.py \
  approach=agentic approach/backend=codex_gpt6 \
  environment=virtual_tools primitive_level=none \
  approach.container_backend=docker \
  approach.blackbox=true approach.blackbox_strict=true \
  approach.max_budget_usd=20.0 \
  replicate_seed=42 eval_seed="$EVAL_SEED" \
  num_eval_tasks=28 eval_timeout=60 \
  hydra.run.dir=outputs/vtg-astra-strict-r42
```

`num_eval_tasks=28` evaluates every level exactly once (the runner cycles through
the level indices, so 100 would repeat levels unevenly). Use
`approach.container_backend=apptainer` where Docker is unavailable; node.js is still
needed on the host that runs the environment server and the evaluation.

### Prompt versions

Each version changes one thing from the one before it, so runs can be compared in
order. Choose a version with the overrides below; everything else in the command
stays the same.

| version | overrides | what changes |
|---|---|---|
| v1 | `environment=virtual_tools` | none: the KinDER prompt with the Virtual Tools description |
| v2 | `environment=virtual_tools_generalize` | adds, after the levels description: "Note that the levels available during development are just examples. You should write a policy that generalizes to held-out levels." |
| v3 | `environment=virtual_tools_generalize approach.search_advice_prompt=false` | as v2, but the 60-second sentence no longer ends with "so it must select actions efficiently rather than rely on exhaustive search or slow planners" (the time limit is still stated) |

## The game as an environment

[virtual_tools_env.py](../src/robocode/environments/virtual_tools_env.py) holds the
rules and the agent-facing description; the description is what the agent reads.

- **Action**: `[tool, x, y]`. `floor(tool)` picks one of the three tools; `(x, y)` is
  the placement point in world pixels (600 x 600, y up).
- **Attempts**: an accepted placement runs the physics for up to 20 s and costs one
  attempt (reward -1). The episode ends on success (`terminated`) or after 10 failed
  attempts (`truncated`), as in the paper, where a model run fails at its 11th attempt.
- **Rejected placements**: a placement that overlaps or touches an object, lies in a
  no-placement region, or falls outside the world runs no physics and costs no
  attempt (reward 0). This matches the human game, which never took such a click: no
  recorded human placement overlaps an object. At most 20 are allowed per episode, so
  a program cannot loop forever.
- **Observation**: a plain dict of JSON values (`JSONDictSpace`): the level in the
  game's own format (`world`), the three tools as polygons, the attempt counters, and
  a `history` with every placement and, for accepted ones, the outcome and each moving
  object's path (position and rotation every 0.1 s).
- **Deterministic**: the same placement in the same level always gives the same
  outcome.

## Levels and the held-out split

[virtual_tools.yaml](../experiments/conf/environment/virtual_tools.yaml) lists the 28
levels that have level files: the paper's 18 Original levels, then its 10 Validation
levels. They are fixed, hand-made scenes, so the runner's variable-count machinery is
reused with the **object count standing for a level index**:

- `design_counts` are the development levels (`dev_levels`, the 18 Original ones).
  Unpinned resets sample from them.
- `eval_counts` are all 28 levels, so evaluation covers seen and unseen levels.
- The black-box env server calls `restrict_to_synthesis()` on every env it serves to
  the agent ([base_env.py](../src/robocode/environments/base_env.py)), after which
  the 10 Validation levels refuse to load. The agent never sees them; the description
  tells it that evaluation includes 10 levels it cannot load.
- The level index is not in the observation or `info`, so a frozen program cannot look
  up memorized placements by index; it has to recognize a scene from its contents.

To develop and evaluate on the same levels instead, set `dev_levels` to all levels (or
`hold_out_from_synthesis=false`).

| index | level | | index | level |
|---|---|---|---|---|
| 0 | Original/Basic | | 14 | Original/Table_A |
| 1 | Original/Bridge | | 15 | Original/Table_B |
| 2 | Original/Catapult | | 16 | Original/Unbox |
| 3 | Original/Chaining | | 17 | Original/Unsupport |
| 4 | Original/Falling_A | | 18 | Validation/Balance |
| 5 | Original/Falling_B | | 19 | Validation/Basic_v2 |
| 6 | Original/Gap | | 20 | Validation/Collapse |
| 7 | Original/Launch_A | | 21 | Validation/Falling_v2 |
| 8 | Original/Launch_B | | 22 | Validation/Launch_v2 |
| 9 | Original/Prevention_A | | 23 | Validation/Remove |
| 10 | Original/Prevention_B | | 24 | Validation/Shove |
| 11 | Original/SeeSaw | | 25 | Validation/Spiky |
| 12 | Original/Shafts_A | | 26 | Validation/Table_v2 |
| 13 | Original/Shafts_B | | 27 | Validation/Trap |

## Reading results.json

- `solve_rate`: the fraction of the 28 levels solved within 10 attempts.
- `design_count_solve_rate` / `held_out_count_solve_rate`: the same for the 18
  development (Original) and 10 held-out (Validation) levels.
- `by_count`: per level index (table above), solved or not and its step count.
- `total_reward` per episode is minus the attempts used; `num_steps` also counts
  rejected placements.
- The determinism check replays levels 0-9 twice.
- `gen_env_steps`: how many placements the agent made through the env server while
  writing its program, its test scripts and render_policy included. Each one is
  an exact, noise-free simulation unless it was rejected. `gen_env_resets`,
  `gen_env_render_states` and `gen_env_connections` count the other requests, and
  `gen_env_failed_requests` the ones that raised, such as a reset of a held-out
  level. The same totals, per command, are in `env_server_usage.json`, and
  `env_server.log` has one line per connection.

## Fidelity: replaying the human data

[virtual_tools_human_replay.py](../experiments/virtual_tools_human_replay.py) replays
every recorded human placement on these 28 levels through the environment and
compares outcomes. Of 9,077 placements, 9,059 (99.8%) agree. Every human success is
also a success. 2 human failures succeed, and 16 human placements are rejected: each of
those rests exactly on a surface, and moving it by one pixel makes it valid. The human
data is used only for this check; agents never see it.

Comparing with the paper's human or SSUP numbers needs the data's level names, which
differ from the level files in five places: `Original/Launch_A.json` and
`Launch_B.json` carry each other's names, and the Validation levels BasicAlt,
FallingAlt, TableAlt and DoubleLaunch are `Basic_v2`, `Falling_v2`, `Table_v2` and
`Launch_v2`. Three Original levels in the data (FridgeMagnet, Towers_A, Towers_B)
have no level file and are not in the environment.

## How it is built

- **Physics**: [tool_games.py](../src/robocode/environments/tool_games.py) imports
  the submodule's `ToolPicker`, which runs each placement in the game's own engine
  (Chipmunk-JS 6.1.1, the engine humans and SSUP used) in node.js through PyExecJS.
  The package also has a Python copy of the physics on pymunk; it predates pymunk 7
  (which KinDER pins) and is never built (`checkThruPy=False`). One simulation takes
  about 0.15-0.25 s, mostly node start-up.
- **Rendering**: [virtual_tools_render.py](../src/robocode/environments/virtual_tools_render.py)
  draws an observation with Pillow alone, since the game's own viewer needs the
  pymunk copy: the scene, the last attempt's trajectories and final poses, and
  numbered markers for earlier attempts.
- **Dict observations in black-box mode**: `JSONDictSpace`
  ([json_dict_space.py](../src/robocode/utils/json_dict_space.py)) is serialized as
  `{"type": "JSONDict"}` by `serialize_space`, mirrored by `env_client`, and selects
  dict-specific prompt text (`dict_obs` in `prompts.py` and `mcp/__init__.py`).
  Observations need no codec: dicts, lists and scalars cross the wire unchanged.

## Limits

- Only the approaches built on `GeneratedProgramApproach` (`agentic`,
  `agentic_per_instance`) pass `dict_obs` to their prompts; the CDL and LLMGenPlan
  approaches would describe the observation as a vector.
- Per-instance runs synthesize against an evaluation instance, which the held-out
  restriction refuses for Validation levels; run them with
  `environment.hold_out_from_synthesis=false`.
- Source access is untested: the sandbox image has node.js (it is built on
  `node:22`) but would also need PyExecJS and the submodule mounted.
- The levels are the paper's fixed scenes. There are no procedural variants yet, so
  each level is one instance.
