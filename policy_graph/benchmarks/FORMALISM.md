# Planning from execution: working definition v0.2

Status: a research proposal with an executable development benchmark. This is
an operational definition for this project, not a claim of universal consensus
or a description of everything the current recognizer can detect.

For the full advisor-facing explanation with worked examples, all case labels,
current results, and implementation milestones, see [ADVISOR_NOTES.md](ADVISOR_NOTES.md).

## Decisions and proposals

| Item | Status |
| --- | --- |
| Build toward general categories, not rules keyed to individual policies | User's stated objective |
| One-step action lookahead counts as minimal planning | Explicitly agreed |
| Checking a single proposed route counts as minimal planning | Explicitly agreed |
| Measure depth and breadth separately; multiple alternatives are not required | Explicitly agreed |
| Keep the Obstruction2D implementation only as an explicit reference measurement | Implemented recommendation; removed from automatic dispatch |
| Definition, category boundaries, and measurement scheme below | Working proposals for review |
| Automatic recognition is the primary track; a separate shared-API-contract track is also evaluated | Provisional; agreement on the contract track remains open |
| A universal scalar planningness score | Not defined yet |

## What counts

**Planning is computation that constructs, assesses, or revises prospective
behavior using relationships between actions, possible situations, constraints,
and objectives.**

A planning episode should have connected evidence for these three roles:

1. **Prospective hypothesis:** a possible action, action outcome, placement,
   route, task sequence, or contingent strategy.
2. **Assessment:** evaluate its effects, feasibility, constraints, cost, or
   objective value. This can be an analytic computation, not only simulation.
3. **Deliberative decision:** construct, accept, reject, select, or revise
   intended behavior using that assessment.

The roles need not be three separate functions, objects, or graph nodes. A
constraint solver can construct and assess candidates implicitly. A single
candidate with an accept/reject decision is enough; planning need not branch.
A search can fail and still perform planning. A selected plan can subsequently
be discarded; that affects action relevance, not whether deliberation ran.

`values + offsets` alone does not establish any of these roles:

| Meaning in context | Counts under this proposal? |
| --- | --- |
| Correct current sensor measurements before a reactive threshold | No |
| Predict positions but never assess or use them in deliberation | No; prediction only |
| Predict action outcomes, assess goal distance, choose an action | Yes |
| Generate prospective placements, check occupancy, choose a placement | Yes |
| Generate a proposed route, check its feasibility, decide whether to follow it | Yes, including one route |
| Execute a hardcoded action sequence without assessing it during this trace | No planning performed in this trace |

A learned policy or stored value lookup is not automatically evidence of online
planning merely because it reflects earlier training. A separate comparison of
hypothetical outcomes or prospective behavior can qualify. Borderline cases such
as ranking immediate actions by a learned score need additional paired examples
and an explicit agreement before we claim comprehensive coverage.

## Categories to cover generally

These are overlapping semantic categories, not algorithm names or a ranking.

| Category | Prospective objects and assessment | Example |
| --- | --- | --- |
| Action–effect | Successors or outcome distributions, assessed against objectives | One-step lookahead; multi-step rollout |
| Configuration/route | Placements, configurations, or paths, assessed for feasibility and cost | Validate one path; compare placements |
| Task/constraint | Task orders or assignments, assessed against prerequisites and objectives | Clear an obstruction before grasping |
| Contingency/information | Conditional strategies, observations, or uncertainty, assessed for expected utility | Inspect first versus act now |

Geometric route planning can qualify without generating a chain of simulated
states. Conversely, generating many simulated states without any assessment or
deliberative decision is not sufficient under this definition.

## What the execution graph must represent

For a particular policy, input sequence, and lifecycle, let
`G = (V, E_data, E_control)` be the trace: executed computation events, their data
dependencies, and their control dependencies. Repeated executions are distinct
events. Unexecuted branches contribute no computation events. Include
construction, reset, action selection, and update; retain dependencies through
cached fields across calls. Returned actions are designated sinks.

Let `P(G)` be the set of connected deliberative episodes satisfying the roles
above. This is a **semantic target**, not an algorithm that follows from the
graph definition. Source code, task meaning, and API contracts may be needed to
identify those roles. A dependency graph by itself cannot distinguish a sensor
calibration offset from an action displacement in all programs.

For action sink `a_t`, define the action-relevant episodes as
`P_t = {p in P(G) : p's deliberative result reaches a_t through recorded data or
control dependencies}`. This is a dependence-based notion of relevance. It does
not prove that changing the result would change the action, nor measure the
quality of the action. Comparisons with rejected candidates may still influence
the decision and therefore belong to its reasoning.

For each recognized episode, a future general schema should retain:

- source events and lifecycle call;
- hypothesis, assessment, and decision roles, with their connecting dependencies;
- category tags and action associations;
- typed measurements and origin IDs for reused work;
- how semantics were established: directly observed structure, a declared API
  contract, or an inference, with coverage limitations.

The current runtime emits a `semantic_profile` with role IDs, interpretation
basis, category tags, typed measurements, and action associations for recognized
events. Hypothesis/assessment boundaries can be declared on shared pure APIs;
the decision role remains inferred from selection/control flow. This is a partial
implementation of the semantic target, not recognition of all four categories.

## Measurements: a profile before a scalar score

Let `T(p)` be transition-evaluation event IDs used by planning episode `p`.
Each ID counts an actual execution, so reevaluating the same state/action pair
counts again; sharing a computed prefix does not duplicate its ID.

- **Model-transition depth:** the longest causally chained hypothetical successor
  sequence used in deliberation. One successor has depth 1. Real environment
  steps, arithmetic operations, and collision samples do not increase it.
- **Breadth:** the number of distinct alternatives assessed at a specified
  decision boundary. Record the candidate type and equality convention. Also
  retain total evaluations separately: repeated checks need not add alternatives.
- **Route/task horizon:** a separate extent with a declared unit, such as graph
  edges, task steps, nominal movement actions, or physical time. Do not equate
  it with model-transition depth or with the number of sampled points.
- **Work:** executed transition evaluations, candidate assessments, constraint
  checks, or optimization iterations, reported in their respective units.
- **Relevance and reuse:** which episodes contribute to each action, when they
  were computed, and whether an action reused earlier computation.
- **Coverage:** what is measured, inferred, unsupported, or incomplete. Unknown
  is not zero. Even a supported syntax trace may be semantically misclassified.

For model-based work, use unions of event IDs:

`performed_work = |union(T(p) for p in P(G))|`

`action_relevant_work = |union(T(p) for p in union(P_t over actions))|`

Work performed in one call restricts the first union to events executed during
that call. These equations concern transition work; analogous counts for paths
or constraints must retain their own units. Do not add unlike units together.

Example: reset evaluates three alternative action sequences, each with three
successor steps, and caches the chosen sequence. There are nine transition
evaluations, depth three, and three candidate sequences at that selection
boundary. Three later `get_action` calls can all depend on that computation while
performing zero new planning work. Episode work remains nine. The original depth
is not necessarily the remaining cached plan horizon.

The current benchmark checks numeric depth/work and supported breadth. Declared
assessment examples also check sequence extent in graph edges. Breadth currently
uses bounded, type-sensitive structural candidate identity; decision grouping and
cross-representation identity remain limited. General physical-time, selected and
remaining horizons, uncertainty, and quality are not implemented. For declared
geometric assessment without model transitions, the semantic profile explicitly
marks model depth not applicable; raw inline route cases still expose missed
recognition as benchmark failures.

## Benchmark protocol

Each fixture includes executable source, input/lifecycle calls, expected ordinary
outputs, semantic descriptions of the three roles, performed/action-relevance
labels, category tags, and optional exact metric expectations. Expected labels
are authored independently of analyzer output and are never given to tracing.

The 25 scenarios (the original 21 plus four shared-API cases) are a **development set**, not a held-out estimate of
generalization. They exercise all four categories, negative controls, failed and
discarded reasoning, caching, and equivalent implementations. They do not cover
all search, learning, optimization, belief-space, or hierarchical algorithms.

Two separately reported tracks:

1. **Automatic:** ordinary runtime configuration; no fixture-specific semantics
   or special Obstruction2D adapter.
2. **Shared contracts (provisional):** the same fixtures and labels, plus a
   documented transition contract for `world_model.step(state, action)` and pure
   assessment contracts for `route_clear` and `placement_cost`. The model means
   `s_next = 2*s + action`, one successor per call. Contracts apply globally to
   those APIs; they are not selected by fixture ID or source fingerprint.

For each run, first compare ordinary execution with the fixture's expected
outputs, then compare traced execution with ordinary execution. Record errors
and missing dependencies as visible gaps. Report false positives, false
negatives, abstentions, and numeric errors separately. Abstentions do not pass.
Implementation tests validate the harness; their passing does not erase semantic
benchmark failures.

Semantic invariance checks should compare renaming, helper extraction, equivalent
loops, batching, and representations of the same hypotheses. Depth and semantic
breadth should remain stable when meaning is preserved. Raw work need not remain
stable when memoization, pruning, or an analytic reformulation changes how much
computation is performed. Equivalent wrong answers are not benchmark success.

## Next agreements and implementation steps

1. Review category boundaries and these small fixtures before selecting a scalar
   score. Resolve prediction-only, learned-value ranking, and configuration-search
   boundary cases with matched positive and negative examples.
2. Decide whether API contracts are an acceptable deployment assumption; continue
   to report automatic and contract-assisted results separately in the meantime.
3. Define general event roles and typed breadth/horizon fields. Extend recognition
   by semantic role and shared operation interface, not by policy identity.
4. Add equivalence families and negative controls with every extension, including
   real execution branches, early termination, shared prefixes, repeated states,
   optimization, and uncertainty.
5. Once the development protocol stabilizes, create a separate held-out set of
   algorithms and RoboCode policies, with multiple task inputs/seeds and manual
   annotations checked independently. Freeze it before evaluating generality.

The retained Obstruction2D reference can validate specific geometric counts on
its reviewed source. It cannot serve as evidence that automatic recognition
generalizes to unfamiliar geometric planners.
