# policy_graph: does a policy plan?

Two parts, standard library only, deterministic, no LLM:

- **`depgraph.py`** builds a dependency graph of Python code: what every value is
  computed from. It is general, not specific to robot policies.
- **`reactivity.py`** labels a policy **planning** or **reactive** (non-planning) with
  explicit rules on that graph, and separately reports whether the label is
  **supported** or **needs review**. Every planning label lists its evidence with
  file:line, the rubric rule it meets, and the dependence path to the action.

```bash
python agent_runs/tools/policy_graph/is_reactive.py my_policy.py   # one word: planning | reactive | needs_review
pbpaste | python agent_runs/tools/policy_graph/is_reactive.py --why
python agent_runs/tools/policy_graph path/to/approach.py           # graph summary + full report
python agent_runs/tools/policy_graph path/to/approach.py --config cfg.json --json report.json --dot slice.dot
uv run python agent_runs/tools/policy_graph/run_corpus.py          # re-label the 35 final policies
uv run --with pytest python -m pytest agent_runs/tools/policy_graph  # all tests
```

Modules that the given files import, absolutely or relatively (`from .planner import
choose`), are analysed too. The decision function is found automatically (see
*Entrypoints*), or set it with `--decision`.

## The rubric (`planning-rubric-2`)

A policy is **planning** when a reachable part of its implementation that influences
the returned action

1. **searches for or constructs a task plan, route, motion plan or control trajectory**
   with a planning procedure, or
2. **evaluates hypothetical consequences of candidate actions or plans and uses them to
   choose** what to do. A horizon of one step is enough.

Otherwise it is **reactive**, the name kept for the non-planning category. Reactive
covers rule-based controllers, **fixed scripts** (predefined action sequences, which are
not a separate category), and action rankings that predict nothing: an argmax over
logits, learned action scores or present-state heuristics.

Rules applied:

- Task and motion planning both count. Route planning is not excluded because it "only
  moves the robot".
- A planner may search internally and return its chosen or first feasible plan. No
  second argmin in the caller is needed.
- Planning survives action conversion and execution: `2 * argmin - 1`, `ACTIONS[i]`,
  `path[1]`, `np.clip(waypoint - pos, ...)` and plans cached in fields keep the label.
- A scripted policy that calls an action-relevant planner is planning.
- Dead code, discarded planning results and unrelated functions or classes do not count.
- Recursion, iteration, enumeration, numerical optimisation, copying, matching types and
  composition are not evidence on their own.
- The label is static: a planning path is reachable under the analysed configuration.
  It does not claim that planning runs on every call.

### Evidence

Every piece of evidence must be in the **backward slice of the decision function's
return value**, computed after unreachable code has been removed.

| kind | rule | what is recognised |
|---|---|---|
| `planner-call` | 1 | a call in the planner contract table (`PLANNERS`): networkx and `scipy.sparse.csgraph` shortest paths, skimage route search, OR-Tools routing, OMPL, pybullet_planning, Drake planning. Extra entries come from `PolicyConfig.planners`. |
| `graph-search` | 1 | a hand-written search: a **worklist** (in a `while` loop or a bounded `for` loop) that is popped and refilled with successors of the popped element and consults a visited/cost/parent table (BFS, Dijkstra, A*); a **relaxation**, where cost-table entries are replaced by smaller candidates computed from earlier costs while a predecessor table records where they came from (Bellman-Ford, dynamic-programming shortest paths, also vectorised with masks); a **layered expansion**, where each element of the current layer adds successors to the next one; or a **wavefront**, a dilation (`maximum_filter`, ...) applied again and again to the set it has reached. The cycle must close inside the function. |
| `tree-search` | 1 | recursion that branches over alternatives (in a loop or comprehension, or from two or more call sites) and compares the branches. The comparison can be a min/max/best-so-far over results, an ordering test between computed values in the recursion or a helper it calls (`cost < table[key][0]`), or a test on a recursive result (backtracking). |
| `ordering-search` | 1 | a choice among the orderings enumerated by `itertools.permutations` (exhaustive task-order search). |
| `generate-and-test` | 1 | candidates ranked by cost (`sorted`, `.sort`, `argsort`) are tried in order and the first that passes a project feasibility check is returned, where the check walks along the candidate itself (`for i in range(len(path) - 1)`): a candidate *plan*, such as a via-point path checked for collisions segment by segment. A check that only looks at the current state ("is this object free?") does not count. |
| `lookahead` | 2 | a **choice among candidates** whose scores depend on a **hypothetical outcome** of a candidate. Choices are `argmin/argmax/argsort`, `min/max/sorted` (with `key=` or over a collection), `xs.index(min(xs))` (also split over variables), best-so-far loops (plain or annotated assignments), and optimiser objectives. A hypothetical outcome is a state-like value updated additively by a candidate (`obs + a`, `pos + dt * v`, `s += a`, also inside helpers and multi-step rollouts); a **closed-loop rollout**, where a loop updates a state-like variable with its own previous value (`y += dy`) by steps that depend on the candidate being evaluated, while accumulating time or cost that reaches the scores (`steps += 1`); or a call to a configured transition model. |
| `transition-model` | 2 | a call to a function listed in `PolicyConfig.transition_models` whose prediction reaches the action. |

How the arithmetic rule decides, in more detail:

- **State-like** means the state itself, a copy or part of it (indexing, attributes,
  `d.get(k)`, conversions, argument binding), or the state shifted by `+`/`-`.
- **The candidate side** must come from a loop, comprehension or callback variable, or
  an optimiser's decision variable, and from no other state.
- **Rollouts.** The accumulator is what separates a simulation from a solver: an iterative
  IK loop converges to a value and accumulates nothing, so it does not count (see the
  ambiguities below). Variables built up as lists (`plan += segment`) are not simulated
  states.
- **Target versus action.** When the only predictions are one-step arithmetic, the chosen
  candidate must become the action through a **state-independent encoding**. This is
  what separates choosing an *action* by its predicted outcome from choosing a
  *target* by distance and then steering to it (`np.sign(t - pos)`), which stays
  reactive and is explained in a `target-choice` note. Targets scored by a closed-loop
  rollout or a configured transition model do count.

### Analysis status

`status` is independent of the label:

- `supported`: planning evidence was found, or nothing unresolved could change the
  reactive label.
- `needs_review`: the label is reactive, but one of these could change it:

| reason | meaning |
|---|---|
| `unresolved-import` | the action uses a function from a module that was not found (absolute or relative). |
| `unresolved-callback` | a `key=` function, an optimiser objective or a `map` callback could not be resolved. Builtins and library callables are fine. |
| `opaque-scorer` | candidates are scored by an unanalysed call that receives both a candidate and the state. It may be a transition model. |
| `solver-role` | a general solver (cvxpy, pulp, CP-SAT, LP, ...) whose role depends on its model. |
| `planner-like-call` | an unresolved call whose name tokens suggest planning (`plan`, `search`, `solve`, `rollout`, ...). |
| `dynamic-call` | a call whose target is not known statically, while planning code exists elsewhere. |
| `ambiguous-method` | a method call on an unknown object that could be a project method that plans. |
| `entrypoint` | the decision function was found only by a generic name (`step`, `predict`, `__call__`). |
| `parse-error` | an imported module could not be parsed. |

When planning evidence exists, these become notes, because unresolved code cannot remove
supported evidence. Patterns that were considered and rejected are also kept as notes:
`ranking`, `target-choice`, `recursion`, `enumeration`, and `not-action-relevant`
(planning code that does not influence the action).

### Configuration

`PolicyConfig`, or `--config cfg.json` with the same keys:

```json
{
  "decision": "GeneratedApproach.get_action",
  "state_params": ["state"],
  "state_fields": ["obs"],
  "planners": {"kin.plan_path": "motion planner", "mylib.": "task planner"},
  "transition_models": ["sim_step", "TModel.step"],
  "reactive_scorers": ["q_values"],
  "libraries": ["my_installed_pkg"]
}
```

- **State.** By default the state is the decision function's parameters (except `self`)
  plus *observation fields*: attributes assigned from what the policy's non-constructor
  methods receive (`observe(self, obs): self.obs = obs`). Constructor parameters are
  configuration, not state.
- **`transition_models` / `reactive_scorers`** settle `opaque-scorer` reviews either way,
  and let a helper that the arithmetic rule does not recognise, such as an IK or
  collision model, count as a prediction.

### Entrypoints

Methods and top-level functions are both candidates. The policy-specific names
`get_action`, `act`, `select_action`, `choose_action`, `compute_action` and `policy` are
tried before the generic `step`, `predict` and `__call__`, which also put the report under
review. Stubs (`raise NotImplementedError`) are skipped. If several functions share the
first matching name, `EntrypointError` lists them instead of guessing.

## Report schema (v2) and migration

`classify()`, `analyze()` and `find_decision_function()` keep their signatures.
`classify(g, decision, config=None)` and `analyze(paths, decision=None, config=None)`
accept an optional config.

| field | v1 | v2 |
|---|---|---|
| `planning` | `bool` | `True`, `False`, or **`None` when the reactive label needs review**. `if r.planning:` still works for planning; use `r.planning is False` or `r.status` to tell confident non-planning from unknown. |
| `verdict` | `"planning"` / `"reactive"` | `"planning"` / `"reactive"` / **`"needs_review"`**. An unknown result is never `"reactive"`. |
| `label` | — | binary `"planning"` / `"reactive"` |
| `status`, `review_reasons`, `notes` | — | see *Analysis status*; reasons and notes are `Issue(kind, what, file, line, function)` |
| `evidence[i]` | `kind, what, function, file, line` | adds `rule`, `influence` (dependence path to the action), `sites` (role, file, line) and `assumptions`. The v1 kinds (`library search`, `recursion`, `self-composition`, `successor`, `action choice`) are replaced by the kinds above. |
| `entrypoint`, `coverage`, `rubric_version` | — | how the decision function was found; modules, unresolved imports, how calls in the action slice were resolved, state sources |
| `find_decision_function` errors | `ValueError` | `EntrypointError` (a `ValueError` subclass) with `.candidates`, also raised for ambiguous names |
| field node names | `field:Policy.plan` | fully qualified: `field:pkg.mod.Policy.plan` |

`report.to_dict()` gives the JSON form written by `--json`.

## The graph

- **Nodes.** Every assignment is its own node (`move@150`). The other node kinds are
  parameters, returns (one `<return>@line` node per return statement, merged into the
  function's return), persistent attributes (`field:pkg.mod.Policy.plan`), module
  globals, call sites, and `+`/`-` operations (`op+@12`, which keep their two operands
  apart).
- **Edges.**
  - `data`: read in the expression.
  - `control`: an enclosing `if`/`while` test or `for` iterable, and also a test whose
    `return`/`break`/`continue`/`raise` decides whether later statements run. Conditional
    mutations such as `if c: out.append(x)` depend on `c`.
  - `arg`: argument to parameter.
  - `ret`: callee return to call site.
  - `field_write`: assignment to a persistent attribute.
  - `base`: the old value kept by an in-place update.
  - `iter`: an iterable to the variable bound to each element (loops, comprehensions,
    callback parameters).
- **Generators.** `yield v` and `yield from g` feed the function's result like `return`
  does, without ending it, so actions produced by a generator (`next(self.gen)`) keep
  their dependences.
- **Copies.** The edges that carry a value unchanged: assignment, indexing, unpacking,
  returns, argument binding, conversions, `d.get(k)`, and `min`/`max`/`sorted` results.
  Tuples unpacked from a literal or from a function that always returns an n-tuple stay
  element by element.
- **Reachability.** Nothing after an unconditional `return`/`raise`/`break`/`continue`
  is analysed. `while True` exits only through `break`. Bodies of `if`/`while` tests that
  are constant (literals, or attributes that can only hold one literal) are skipped and
  listed.
- **Constants.** An attribute is constant only if every visible write agrees:
  - class defaults and assignments in any method of the class family, constructor or not;
  - any assignment to an attribute of the same name on another object anywhere in the
    analysed code (`p.enabled = True`; without types it might be ours);
  - `setattr` with a computed name, `vars` or `__dict__` writes make nothing constant.
- **Function values.**
  - Lambdas and nested functions are analysed as functions.
  - Variables, parameters, globals and attributes holding functions resolve to them
    (`planner = plan; planner(x)`, `self.scorer = self._score`), in up to four passes.
  - Known higher-order calls bind their callbacks: `min/max/sorted(key=)`, `list.sort`,
    `heapq.nsmallest/nlargest`, `map`, `filter`, and `scipy.optimize` objectives, whose
    first parameter becomes the decision variable.
- **Calls.** Every call site records how it was resolved: `project`, `builtin`,
  `library`, `method` (unknown receiver), `dynamic`, `unresolved-name` or
  `unresolved-import`. Methods on unknown objects resolve by a unique method name only
  among classes of modules the caller imports, so adding an unrelated module changes
  nothing.

## Validation

Tests (168, run in about 1 s):

- `test_rubric.py`:
  - the review's 34 checks, with the label the rubric requires (not the old outputs);
  - 40 independent cases covering every rubric rule;
  - 17 rewrite-invariance pairs: lambda vs named or method key, direct vs identity
    helper, nested vs split selection, plain vs annotated, six action encodings, alias
    vs direct call, callback field vs method, renamed class;
  - unrelated-module and same-name-class invariance;
  - package entry file vs package directory;
  - eight needs-review cases and their resolution by configuration or by supplying the
    missing module;
  - entrypoint discovery and report schema.
- `test_depgraph.py`: graph properties behind each review finding, checked on the graph
  itself (field identity, constants, termination, control dependence of mutations and
  branch values, copies across calls, callbacks and function values, relative and
  missing imports, method resolution scope, additive operations).
- `test_policy_graph.py`: the original suite, updated where the rubric changed the answer
  (BFS route search is now planning; evidence kinds were renamed; field names are
  qualified). `cases/` files are still run by their `# expect:` line.

These are targeted checks of specific behaviours, not an accuracy estimate.

### Against the hand labels (`approach_table.md`, 35 final policies)

The hand labels describe task-level strategy ("Search" vs "Greedy"/"Fixed"). The rubric
also counts route and motion planning, so they are a reference, not ground truth.

| | v1 planning | v2 planning | v2 reactive | v2 needs review |
|---|---|---|---|---|
| hand: Search (12) | 12 | 12 | 0 | 0 |
| hand: Greedy (14) | 7 | 8 | 6 | 0 |
| hand: Fixed (9) | 2 | 5 | 4 | 0 |

Twelve verdicts changed. `all_runs_verdicts.json` has every run's evidence.

- **Reactive → planning (8): route planning that v1 deliberately ignored.**
  - Rovers Astra 24 (`csgraph.dijkstra` plus predecessor walk).
  - Rovers GPT-5.6 24 (A* in a bounded `for` loop).
  - Obstruction2D Claude 24 (vectorised dynamic-programming path search, run from a
    generator `get_action` consumes with `next`).
  - DynPushT2D Claude 444, Astra 24, Astra 424, GPT-5.6 24 and GPT-5.6 424, which each
    run a grid A*/Dijkstra/BFS and follow its waypoints.
- **Planning → reactive (4): v1 evidence that was a composition misfire.** Obstruction3D
  Claude 24, 222 and 424 and Astra 24 (`wrap`, `fk`, `ik`, `pos` applied to their own
  outputs). Their candidate rankings are listed as `ranking` /
    `target-choice` notes (see the ambiguities below).
- **Same verdict, right reason now:**
  - Obstruction2D Claude 42: v1 matched `_grasp_x(_grasp_x(...))`; now its generate-and-test
    path planner `_plan_path` (via-point paths sorted by length, first collision-free).
  - Obstruction2D Claude 222: v1 matched the one-chain recursion `_resolve`; now
    `_drop_spot`/`_place_candidates_target`, which score candidates by simulating the
    controller (`_est`) over predicted clearance profiles.
  - Rovers Claude 24's layered BFS is found directly (v1 matched a helper misfire).
  - Rovers Claude 222 and 444 are found through their wavefront expansions and Claude
    444's DFS over task orders.
  - Obstruction3D Astra 424's recovery routine predicts the clearance after each escape
    move (`hp[:2] + delta`) and tries the best first.

### Decisions on ambiguous points

These change labels, so they are stated rather than buried:

1. **Single-configuration solves (IK, kinematic feasibility).** Evaluating candidate
   grasps or base placements through IK or collision checks is not recognised as
   predicting an outcome. Only additive state updates and configured transition models
   count, because the rule cannot tell a kinematic model from a present-state heuristic.
   This is why Obstruction3D Claude 222 (`_jplan_to` tries base placements by IK) is
   reactive. To count it, list the solver in `transition_models`. Optimisers are
   treated like other choices: an objective that adds a decision variable to the state
   is look-ahead.
2. **Exhaustive ordering search counts as task planning** however the orderings are
   scored. `itertools.product`/`combinations` count only with a predicted outcome.
3. **Arithmetic transitions are recognised syntactically**, as an additive update of a
   state-like value by a candidate. Updates modulated by the state (`p + R(θ) @ a`,
   `x + v * cos(θ)`) are not recognised: the same shape covers linear action scores
   (`obs + w[a] * obs_v`). Configure the transition function instead.
4. **Graph searches are read by shape.** A perception flood fill with a visited table,
   or iterated smoothing with a dilation operator, would be read as a search.
5. **Planner influence includes control dependence.** For example, the action can depend
   on whether a route exists.

## Limitations (supported analysis boundary)

- **Static.** Settings changed from outside the analysed code are not visible, and a
  planning label does not mean planning runs on a given step. Confirm with runtime
  tracing when it matters.
- **No type inference.** Calls on unknown objects are named by method, and containers
  are tracked as whole values, apart from unpacked tuples. The analysis is
  context-insensitive across calls, so a helper's internals merge values from every
  call site.
- **Exceptions are approximated.** A handler may start from the state before or after
  the `try` body. Closures see the variables that reach their definition.
- **Search recognition** covers the shapes listed above. A search written in another
  form, such as states encoded through an external library or a relaxation without a
  predecessor table, is missed. It is flagged only if an unresolved call or callback is
  involved.
- **Arithmetic look-ahead** needs the candidate to come from a loop, comprehension,
  callback or optimiser variable. A single non-enumerated action checked by prediction
  (a safety filter) is not recognised.
