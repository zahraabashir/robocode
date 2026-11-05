# Runtime planning analysis — first milestone

This backend executes a policy and records dependencies between individual
execution events. The original `depgraph.py`, `reactivity.py`, `scoring.py`, static
CLI and corpus results remain the reference baseline. `static_baseline.json`
records revision `27ec4fd`, source hashes, rubric/scoring versions and the original
test result (220 passed, 1 skipped).

## Run an environment episode (no scenario JSON)

From the repository root:

```bash
.venv/bin/python -m policy_graph.runtime /path/to/approach.py \
  --env motion2d_easy --seed 0 --max-steps 100 \
  --json /tmp/planning-report.json --dot /tmp/planning-graph.dot
```

Use the environment name matching your policy from `experiments/conf/environment/`.
The CLI constructs the environment and policy, calls `reset`, and repeatedly runs
`get_action` → environment step → optional `update`. Observations come from the
environment; no manually specified call sequence is required. The environment is
closed on success or failure, and errors still save an incomplete trace.

For a policy under a saved RoboCode run, the CLI discovers the nearest
`.hydra/config.yaml` or archive `evidence/config.yaml` automatically:

```bash
.venv/bin/python -m policy_graph.runtime /path/to/run/sandbox/approach.py \
  --seed 0 --json /tmp/planning-report.json
```

Use `--run-config /path/to/config.yaml` when the saved configuration is elsewhere.
Saved environment settings, primitive names and `max_steps` are reused. An explicit
`--env` selects its environment YAML instead of discovering a saved run; its default
step limit is 1000 and its primitive list is empty. `--max-steps` overrides the step
limit, `--object-count` pins a variable-count task, and `--primitives NAME ...`
overrides the primitive list (an empty list disables them). `--seed` defaults to 0
and selects one episode, not the entire saved evaluation suite. This is a local
diagnostic rollout, not the experiment runner's isolated evaluation protocol.

Ready-to-run example:

```bash
.venv/bin/python -m policy_graph.runtime \
  policy_graph/runtime/examples/maze_reactive.py \
  --env small_maze --seed 0 --max-steps 10 --json /tmp/maze-report.json
```

The policy uses only the current observation and ignores obstacles. With this
seed it reaches the goal in 3 actions and reports depth/work 0.

## General analysis versus reference measurements

Normal `RuntimeSession`, `trace_episode`, and the CLI always use the generic
tracer. They no longer select a policy-specific adapter by source fingerprint.
The Obstruction2D implementation is retained only as an explicitly invoked
[reference measurement](reference/README.md), outside the general benchmark.

Consequently, the normal CLI does not produce the previous compact geometric
counts for that policy. Its generic trace can still reach the event limit or
report unknown measurements. This is a known coverage gap, not evidence that the
policy performs no planning. Existing JSON configs with `"semantic_adapters":
false` remain readable; `true` is rejected rather than restoring automatic
special-case dispatch.

The [planning benchmark](../benchmarks/README.md) tests independently authored
semantic expectations, including generic route and placement planning. Its
[working formalism](../benchmarks/FORMALISM.md) records agreed boundaries and
proposals for broader coverage. The current recognizer does not yet satisfy all
of them; passing implementation tests must not be read as complete semantic
coverage.

## Manual test examples

From the repository root, using Python 3.11 or 3.12:

```bash
.venv/bin/python -m policy_graph.runtime \
  policy_graph/runtime/examples/cached_plan.py \
  --scenario policy_graph/runtime/examples/cached_plan.json \
  --json /tmp/cached-plan-report.json --dot /tmp/cached-plan-action.dot

.venv/bin/python -m policy_graph.runtime \
  policy_graph/runtime/examples/conditional.py \
  --scenario policy_graph/runtime/examples/conditional.json \
  --json /tmp/conditional-report.json
```

The cached example has depth **3**, episode work **6**, and **0** new updates in
each `get_action` call. Each returned action refers to the same planning event in
`reset`. The conditional example has action depths **1** and **0** for inputs 3
and -3. `contradictory.py` can use the same scenario; both depths are zero even
though the static baseline retains its infeasible branch.

`--include-graph` adds the complete event graph to JSON. DOT contains the union of
the returned actions' backward slices. `session.recorder.graph.to_dot([event_id])`
exports a single action's slice. Events contain source locations and dependency
IDs; arbitrary runtime objects are not serialized.

## API and execution contract

```python
from policy_graph.runtime import RuntimeSession

with RuntimeSession("approach.py") as session:
    session.load(constructor_kwargs={
        "action_space": action_space,
        "observation_space": observation_space,
        "primitives": primitives,
    })
    session.call("reset", state, info)
    action = session.call("get_action", state)

report = session.report()
```

`GeneratedApproach` is instantiated automatically when present. Supply
`class_name="Policy"` for another class. Otherwise the adapter calls functions in
the module. `get_action` results are action sinks; `action=True` designates another
method/function's result as an action. There is no guessing of a script's intended
main function. A session with no returned action reports `not_evaluated`, not zero.

By default only positional argument 0 of each harness call is an observation.
Use `state_args=()` for configuration-only calls, or a tuple of argument indices
and keyword names. New observations start at depth zero; executing a real action
does not add a hypothetical transition. State stored in fields retains provenance
between calls. Separate sessions isolate different policy instances/runs.

The JSON scenario accepts `class_name`, `constructor_args`, `constructor_kwargs`,
and an ordered `calls` list. Each call accepts `method`, `args`, `kwargs`,
`state_args`, and optional `action`. A scenario is an explicit call sequence,
not an environment rollout: its supplied observations need not be consequences of
the returned actions.

For an actual RoboCode episode:

```python
from policy_graph.runtime import trace_episode

session = trace_episode(
    "approach.py", env, seed=42, max_steps=100, primitives=primitives
)
report = session.report()
```

This uses `robocode.utils.episode.load_generated_approach` and `run_episode`, with
the normal constructor, reset, get_action, environment step and optional update.
The caller constructs/closes the environment and supplies its matching primitives.
RoboCode is imported lazily; the standalone recorder needs only the standard
library. Loading is instrumented through an optional compilation hook; existing
loader calls and source checks retain their normal behavior. Local sibling modules
are instrumented via a temporary import hook and restored on session exit.

## What the scores mean

Reports now also contain `semantic_profile`, a separate interpretation layer.
For each recognized decision it lists hypothesis, assessment, and decision event
IDs; category tags; the interpretation basis; and contributing action indices.
Arithmetic-based meaning is explicitly labeled as an assumption. Even with a
declared assessment API, the decision role is inferred from selection/control
flow. `role_chain_present` reports connected inferred roles, not verified meaning.

Its per-episode `measurements` include model depth, transition work, breadth,
candidate evaluations, and optional `max_assessed_horizon`. Every field has a unit
and a status (`measured`, `unknown`, or `not_applicable`). Breadth uses bounded,
type-sensitive structural candidate identity, not arbitrary Python equality.
Repeated assessments increase work without necessarily increasing breadth.
Condition grouping and candidate identity across representations remain limited.

`declared_assessment_work` deduplicates recognized assessment event IDs across
decisions/actions; `semantic_profile.actions` reports new assessment work and
earlier associated IDs. Candidate horizon describes the original full assessed
candidate, including an early-rejected candidate, not its selected/remaining suffix.
See the [advisor notes](../benchmarks/ADVISOR_NOTES.md) for examples and limitations.

- **`planning_depth`**: maximum explicit hypothetical depth among the observed,
  action-relevant planning events. It counts semantic model transitions, not AST
  nodes, dependency hops or loop iterations.
- **`planning_work`**: union of their transition execution IDs. Repeated evaluations
  count again; shared prefixes and cached events count once.
- **`performed_planning_work`**: work across all recognized planning events,
  including computations whose result was discarded. `calls` breaks this down by
  lifecycle call. Unsupported executed operations make this measure unknown even
  when the returned action has a fully supported dependency slice;
  `calls[].observed_planning_work` still gives the recognized count.
- **`planning_events`**: individual selection events (or a sequence of best-so-far
  comparisons at one site/invocation), their transitions, depth, work and relevance.
- **`actions`**: planning event IDs behind each action, depth, new work in that
  action call, and inherited event IDs. Inherited depth is the original planning
  event's depth, not an estimate of the cached plan's remaining horizon.
- **`planning_calls_per_action`**: distinct lifecycle calls containing
  action-relevant planning, divided by returned actions. It includes reset/setup
  and is not a measure of planning quality.
- **`executed_prediction_updates`**: diagnostic count of recognised predictions,
  including discarded predictions. Those do not automatically affect action scores.

The verdicts are `planning_observed`, `no_planning_observed`, `needs_review`, and
`not_evaluated`. They describe these executions under the recognizer's assumptions,
not every input the program could receive. Unsupported action dependencies or an
incomplete trace make counts unknown (`null`). Known planning can coexist with
unknown depth/work. A trace limit or policy error invalidates aggregate counts;
the prefix remains inspectable. Purely unexecuted branches produce no body events.
The explicit Obstruction2D reference may report `partial` status and separately
typed measurements; it is not selected by ordinary runtime analysis. Report schema version is `runtime-planning-5`.

## Transition and library contracts

Pure shared assessment APIs can declare one prospective candidate and its check:

```python
from policy_graph.runtime import AssessmentContract, RuntimeConfig

config = RuntimeConfig(assessments={
    "navigation.route_clear": AssessmentContract(
        candidate_arg=0, candidate_kind="route", category="configuration_route",
        horizon="sequence_edges", horizon_unit="graph edges",
        model_free=True,
    ),
})
```

The API must be pure and depend only on explicit arguments. Its body runs once;
internal operations are not independently counted as planning. A selection or
condition must consume its result; an unused assessment does not complete the
planning pattern. Contracts are caller-supplied semantic assumptions, not verified
automatically. Horizon options are `sequence_edges` and `sequence_items` on plain
lists/tuples, both requiring a unit. JSON accepts an `assessments` mapping with
these same fields. No contracts are selected by policy fingerprint.

`model_free=True` also declares no model transitions inside the assessor. Without
it, hidden model depth/work remain unknown, not inapplicable. Purity alone does
not rule out an internal simulator. Supported incoming model-transition evidence
can still contribute even when the assessor itself is model-free.

Arithmetic recognition initially covers scalar additive updates of a state-like
value by a candidate from a loop or selection callback. It is a heuristic semantic
assumption, not a proof that arbitrary arithmetic represents dynamics. Classification
is based on dependence, not counterfactual tests of whether changing a value would
change the chosen action. Compare the baseline's rubric and known ambiguities.

Declare non-additive models, native simulators, or tuple-returning models explicitly:

```python
from policy_graph.runtime import RuntimeConfig, TransitionContract

config = RuntimeConfig(transition_models={
    "model.step": TransitionContract(state_arg=0, action_arg=1, output_index=0),
})
```

One model call means **one successor transition**. The contract identifies the
state/action arguments (indices exclude `self`; parameter names also work), the
state output, and its unit. Internal arithmetic is not counted a second time.
Contracts must correctly describe the implementation; automatically inferring an
opaque simulator's semantics is outside this milestone. In-place simulator state
and batched transitions need dedicated adapters. `duration` can be declared as
metadata, but this release reports depths in model steps, not aggregated seconds.

Runtime configuration JSON:

```json
{
  "arithmetic_transitions": true,
  "max_events": 200000,
  "transition_models": {
    "model.step": {"state_arg": 0, "action_arg": 1, "output_index": 0}
  },
  "planners": ["my_search"],
  "pure_functions": ["my_library.cost"]
}
```

Declared pure functions are summarized as depending on their arguments; the caller
is responsible for that purity contract. Planner calls reuse the static planner
table plus configured names. Without a counting contract, they establish planning
with unknown numeric scores. Different abstraction units are not combined into a
single numeric depth.

## Supported boundary and next extensions

This is a first runtime backend, not a complete Python dynamic slicer. It supports
ordinary synchronous functions/methods, closures, conditionals, loops, scalar
operations, list/tuple/dict values, common mutations, eager comprehensions and
lazy generator expressions,
`min`/`max`/`sorted` callbacks, and explicit model/planner contracts. Dynamic
assignments and individual supported container elements have separate provenance.

Opaque calls, unsupported statements/expressions and their possible mutations
propagate uncertainty in the generic tracer. NumPy arrays have whole-array
dependencies, described in [NUMPY.md](NUMPY.md). Generator functions,
decorators other than `staticmethod`/`classmethod`,
computed class-body declarations, exception-handler dependencies, custom
descriptors/operators, async/concurrent execution, and general search/optimizer
internals do not yet have full support. The source-checked Obstruction2D reference
summarizes only its reviewed numerical search boundaries and does not extend
the automatic tracer's support.
Baseline graph, tree, ordering, generate-and-test and lookahead rules now supply
semantic candidates. Runtime decisions must have matching operation witnesses
in their dependency slice. Each recognition retains the static rule's assumptions.
Structural search labels do not imply measured transition counts or depths. Function bodies left
opaque still execute normally and produce unknown dependencies when relevant.

Import hooks and recorder state are synchronous and process-local. Use one session
at a time; nested sessions are rejected. Reports
include source hashes and the transition/recognition configuration. Trace events
and retained object identities are bounded by `max_events`; this is not a wall-clock
timeout for opaque native calls. Tracing changes runtime overhead, so a policy with
a wall-clock search budget may explore less than its ordinary run. Policy action
equivalence is tested on deterministic fixtures, not promised for all Python
introspection or time-dependent code.

The next design step is general semantic event roles for hypotheses, assessment,
and deliberative decisions, evaluated with paired positive/negative examples and
equivalent implementations. General NumPy/batched-model interfaces, broader structural
search evidence, exception/generator-function support, and a larger RoboCode corpus remain
necessary. Typed breadth and horizon fields need explicit semantics before being
added as scores; see the working formalism.

## Verification

```bash
UV_CACHE_DIR=/tmp/robocode-policy-uv-cache uv run --no-project \
  --with 'pytest>=7.2.2,<9.1' --python .venv/bin/python \
  python -m pytest policy_graph tests/utils/test_episode.py \
  tests/utils/test_strict_blackbox.py -q
```

The tests compare ordinary and instrumented return values and cover infeasible
branches, runtime branches, helper call contexts, overwrites, shared prefixes,
cached plans, mutable aliases, callback behavior, explicit models, unknowns,
trace limits, import cleanup and the actual RoboCode lifecycle.

Previous milestone verification (2026-11-02): **453 passed, 5 skipped**, including
**92 runtime tests** and **38 benchmark-harness tests**. All 12 source/artifact
hashes in `static_baseline.json` still match. The automatic recognizer meets all
expectations in **10/25 semantic benchmark scenarios** (still **9/21** on the
original set); implementation-test success is distinct from semantic coverage.
The separate shared-contract track meets **14/25**. See the benchmark for gaps.

## Recognition update (3 November 2026)

`runtime-planning-4` reuses the frozen static recognizer through `recognition.py`.
It collects candidates for action and reset computations, including discarded
work, and validates them using executed decisions and dependencies. Structural
loop markers are emitted only on entered iterations. Unexecuted branches, empty
frontiers, and recursive base cases do not establish planning. Cached dependencies
retain earlier recognition. Reports expose `recognition` on planning events and
`structural_evidence` in semantic profiles, including assumptions and witness IDs.
These are heuristic interpretations, not verified facts about the world.

Lazy generator expressions now preserve per-element provenance and evaluate their
outer iterable at construction, with bodies evaluated only when consumed.
Generator functions and arbitrary iterator internals remain outside this support.
Known static NumPy reducer patterns can support labels while opaque internals
keep numeric measurements unknown; this is not general NumPy tracing.

The 25-case benchmark now has **11/25** correct pairs of automatic labels and
**15/25** with shared contracts; all expected return values are preserved. The
same cases also meet their numeric expectations. Broader baseline search families
are covered separately by runtime regression tests. The remaining benchmark
failures are reported, not hidden. See `benchmarks/results/current-v0.3.json`.

Verification for this update: **466 passed, 5 skipped**, including 13 new
recognition/generator regression tests. Black, isort, pylint and mypy pass; all
12 static-baseline hashes remain unchanged.

## Reliability and performance update (3 November 2026, `runtime-planning-5`)

The v4 corpus run had no usable result: 24 process timeouts, 10 indexing crashes
and one event-limit failure. Stage-separated measurements (below) showed that the
timeouts came mainly from report generation, then from instrumentation compile,
not from tracing itself.

**Fixes.**

- *Indexing crash.* Container lookups hashed index tuples containing slices or
  arrays (unhashable in Python 3.11). Keys are now checked first. NumPy indexing,
  writes, views and aliases are supported with conservative whole-array
  dependencies; see [NUMPY.md](NUMPY.md).
- *Behavior changes caused by the tracer.* Tracer errors were raised inside
  policies and caught by their own `except Exception` fallbacks. In two
  DynPushT2D policies this changed the first action. Separately, `|=` and `&=`
  ran as non-in-place operators, which broke aliasing. Both are fixed.
- *Compile.* `ast.get_source_segment` re-split the whole file for every node
  (quadratic). Lines are now split once. Median compile: 2.5 s to 0.05 s.
- *Report.* Each decision event and each action ran a full backward slice, and
  recognition matching scanned each slice. Dependency queries now use forward
  passes over the event list with integer bitsets. On all 110 test traces the
  reports are unchanged, apart from deterministic witness ordering.
- *Fewer, smaller events.* An event references only the innermost entry of each
  control list. Each entry was recorded while the entries below it were active,
  so the closures are identical; this is audited in `test_numpy.py`. Reads,
  constants, single comparisons, redundant copies, transient index tuples and
  parallel assignments no longer create events. Unchanged content summaries are
  reused. The median number of control references per event fell from 10.2 to 1.3.
- *`staticmethod`/`classmethod` bodies* are instrumented instead of opaque.
- *Values from uninstrumented code.* A function that returns from inside an
  unsupported statement (for example a `try` body) depends on that frame's
  unknown marker, and is never treated as a constant. Objects that an unsupported
  statement may write through a name or attribute path have unknown contents
  afterwards; a plan cached inside a `try` body was previously a false
  "no planning". This fix is conservative: a handler that did not run still
  counts as a possible write.

**Recognition safeguards (no new planning rules).** The bridge collects static
candidates over all nodes so that discarded work is visible. This bypassed the
baseline's one action-slice rule: a look-ahead whose chosen candidate reaches the
action combined with the current state is a target choice (`_encodes`). Now:

1. that rule is applied to every look-ahead whose winner is in the static action
   slice, whichever entrypoint found it (446 corpus candidates rejected);
2. the reset classifier only judges code that `reset` runs, so decision-time
   tracking error is not read with reset's notion of state (117 rejected);
3. a look-ahead outside the static action slice still counts as performed
   planning. If it alone makes a decision relevant at runtime, the relevance is
   unresolved (`needs_review`), because the rule was never checked.

Static slice evidence remains a subset of runtime candidates for all 35 policies.
The reported false positive (Obstruction3D GPT-5.6 424, `target - cur`, line 130)
is no longer recognized as planning. Rejections are listed in
`recognition_coverage.rejected_by_action_slice_rules`.

**New report fields.** `possibly_action_relevant` and
`possibly_relevant_planning_event_count` (relevance only through whole-array
edges); `precision`; `unchecked_rule_planning_event_ids`; `unknown_count` and
`unknown_reasons`. Per action: `possible_planning_event_ids` and
`unknown_event_count`; `unknown_event_ids` lists at most 100 IDs.

**Diagnostics.** `python -m policy_graph.runtime.diagnostics approach.py --out DIR`
runs ordinary and traced execution in separate processes with identical settings.
It times (1) ordinary execution, (2) recognition and instrumentation, (3) traced
execution and recording, and (4) report generation, each with its own budget. It
records peak memory, event counts and the per-step action and observation
fingerprints that it compares. It also lists clock use, because tracing overhead
can change time-budgeted policies. `python -m policy_graph.runtime.corpus` reruns
the 35-policy protocol. See
[results/corpus35-seed0-v5/REPORT.md](results/corpus35-seed0-v5/REPORT.md).

**Verification for this update:** 510 passed, 5 skipped (44 new regression tests).
The old and new runtimes give identical per-action dependency signatures (reached
observations, conditions, transitions, choices and unknown reasons) on 19 of 19
comparable non-NumPy test fixtures and 24 of 24 non-NumPy benchmark cases. The one
other fixture differs as intended (`staticmethod`). The static analyzer can name a
different prediction line for the same look-ahead depending on Python's hash seed.
In the corpus this changes one policy's runtime witness requirement (Obstruction2D
Claude 424, line 215). Fix `PYTHONHASHSEED` for exactly reproducible recognition.
Pylint 10/10, and mypy reports no errors in the runtime and benchmark packages.
All 12 static-baseline hashes are unchanged. The benchmark results are identical
to v0.3 in every case, label and metric (11/25 automatic, 15/25 with contracts).

## Event-volume follow-up (3 November 2026)

Under the original protocol, 30 of 35 policies stop at the 200,000-event limit,
and 20 of them stop before their first action. This follow-up measured where the
events come from before deciding what to change.

**Where the events are.** `diagnostics` now attributes events to functions
(`trace.attribution`). A function is *candidate-free* if neither it nor anything
it calls contains a static candidate site. Summarizing calls to candidate-free
functions that produce no consumed events (unknowns, transitions, choices, search
markers) would remove a **median of 11%** of events across the corpus (45% if
unknown-producing helpers were included, which would be unsound). Most events are
in the planning code itself, such as search loops, candidate scoring and
choices. Helper summarization therefore cannot close the 10-100x gap and was not
implemented. Completing those episodes requires either a larger event budget or
analyzing selected decisions instead of whole episodes.

**Cost at larger budgets.** Recognition matching is now a few bitset tests per
event, with identical results: the slowest 3M-event report fell from 126 s to
45 s. Shadow-value copies and contract lookups are cheaper, and events without
details share one empty dictionary. In the 3M-event diagnostic, tracing runs at
a median of about 170,000 events per second and uses about 450 MB per million
events.

**Separately labelled runs.** These change the stated protocol parameters; the
original protocol and its results are unchanged. Results are summarized in
[the v5 report](results/corpus35-seed0-v5/REPORT.md):

```bash
# 3M events instead of 200k; everything else as in the original protocol.
python -m policy_graph.runtime.corpus --out results/NAME --max-events 3000000 --hash-seed 0
# The same, plus declared environment-accessor contracts (an assumption track).
python -m policy_graph.runtime.corpus --out results/NAME --max-events 3000000 --hash-seed 0 \
  --contracts policy_graph/runtime/contracts/object_centric_state.json
```

`--hash-seed` fixes `PYTHONHASHSEED` for every child process, so that the static
candidates are reproducible. `contracts/object_centric_state.json` declares the
`ObjectCentricState` lookups (`get`, `get_objects`, `get_object_names`,
`get_object_from_name`) pure. Their source reads stored features only, but this
remains a declared assumption. A declared-pure *method* now also depends on its
receiver. Previously `state.get(obj, "x")` lost its dependency on `state`; this
is a fixed bug.

**Remaining unknowns.** With accessors declared, every completed policy still has
other unknown sources. The common ones: iterators over unsupported values (`zip`,
`dict.items`, ...), builtins on unsupported values, writes inside unsupported
statements, `set` and `set.add`, starred or complex assignments, `try`, calls
with `*args`, `list.sort`, `heapq`, and `str` methods. These need broader Python
coverage. Each is a general, testable addition, but only resolving most of them
will turn `needs_review` into a definite verdict.
