# Measuring planning from code execution

**Working proposal and implementation status — 2 November 2026**

This document is written for discussion with advisors and for copying into Notion.
The definition below is our project's proposed measurement rule. It is not a claim
that all researchers use the same definition of planning.

### Implementation update — 3 November 2026

The runtime now reuses the old static graph's recognition rules for graph search,
recursive search, ordering search, ranked candidate validation, and lookahead.
A rule must have matching operations in the observed decision's dependency graph.
A static planning label by itself does not prove that planning ran.
The report retains the rule, assumptions, and executed witness IDs. Numerical
measures remain unknown when tracing cannot count the relevant operations.

Generator expressions now preserve lazy evaluation and element dependencies.
The benchmark improves to **11/25 automatic** and **15/25 contract-assisted**,
with expected outputs preserved in all cases. These are both-label correctness
counts; the CLI now reports labels separately from numeric expectations. In this
snapshot the same cases also meet all numeric expectations. The static recognizer
also misses several new benchmark categories, so reusing it is not a complete fix.

The results and implementation tables below describe the previous 2 November
milestone unless explicitly updated here. Generator functions and general NumPy
tracing remain unsupported. Current results are in `results/current-v0.3.json`;
`current-v0.2.json` is retained for comparison.

## 1. The idea in one minute

We want to examine a policy while it runs and answer:

1. Did it consider possible behavior before choosing what to do?
2. How far ahead did it consider?
3. How many alternatives did it assess?
4. How much computation did it perform?
5. Which of that reasoning contributed to the returned action?

Example: a robot is at position **2** and wants to reach **5**. It considers moving
left and right. Left would reach **1**, four units from the target. Right would
reach **3**, two units from the target. It chooses right.

That is a small planning computation: **two alternatives, one move ahead, two
predicted outcomes**. A deep search is not required for something to count as
planning under our proposed definition.

We also want to count planning that does not explicitly simulate future states.
Checking whether a route is clear, comparing possible placements, or checking a
task order can all influence a decision about future behavior.

We want a **profile of planning**, before choosing any single overall score.
Looking farther ahead, considering more alternatives, doing more work, and
choosing better actions are different properties.

## 2. What is agreed, and what is still a proposal?

| Item | Status |
| --- | --- |
| The system should work across policies, not recognize individual policy files | Project objective |
| One-step action lookahead counts as minimal planning | Agreed |
| Checking one proposed route counts as minimal planning | Agreed |
| Depth and breadth are separate measurements | Agreed |
| The three-part definition below | Working proposal being made precise through examples |
| The four broad planning categories below | Working proposal; categories can overlap |
| Allowing shared API meanings as an input to the analyzer | Implemented as a separate experimental track; deployment choice remains open |
| A single numeric planningness score | Not defined |
| Complete automatic understanding of arbitrary Python | Not achieved; not claimed |

## 3. A small notation dictionary

| Symbol or name | Plain meaning | Example |
| --- | --- | --- |
| \(C\) | The computation we are examining | Comparing left and right |
| \(h\) | A possibility being considered, called a hypothesis | Move right; follow route S–B–G |
| \(R\) | Rules used to reason about that possibility | Right adds 1 to position; a route cannot cross a blocked node |
| \(J\) | The objective or preference | Be closer to position 5; prefer a shorter clear route |
| \(q\) | An assessment result | Distance 2; route is clear; task order is invalid |
| \(d\) | A choice made using an assessment | Choose right; accept this route; wait because none worked |
| \(s\) | A state, or information describing a situation | Robot position 2 |
| \(a\) | An action | Move right |
| \(T(s,a)\) | A model predicting the next state | \(T(2,+1)=3\) |
| \(a_t\) | The actual action returned at call \(t\) | The command sent to the environment |
| \(G\) | The recorded execution graph | Operations that ran, linked to their inputs and conditions |

These are labels for explanation. The policy does not need variables named `h`,
`R`, `J`, or `d`. The rules and objective may be spread across several functions.
A decision inside the planner, such as rejecting a route, is not necessarily the
final action returned to the environment.

## 4. Our proposed definition

\[
\operatorname{Planning}(C)
= \operatorname{Prospective}(C)
\land \operatorname{Assessment}(C)
\land \operatorname{DecisionRole}(C).
\]

Read this as: **a computation counts as planning when it considers possible
behavior, assesses it, and uses that assessment in a choice about behavior.**

| Condition | Simple question |
| --- | --- |
| Prospective | Is this about something we could do, or a situation that could result? |
| Assessment | Do we check whether it works, is allowed, or is good? |
| DecisionRole | Does that check help construct, accept, reject, select, or revise behavior? |

The three parts must be connected. Unrelated prediction, arithmetic, and choices
in the same file are not enough. More explicitly, we seek a connected pattern:

\[
h \longrightarrow q=\operatorname{Assess}(h;R,J)
\longrightarrow d.
\]

The first formula names the requirements; the arrow shows how they connect.
`R` and `J` are conceptual inputs to the check, not necessarily explicit function
arguments. A feasibility-only check can be enough: it does not need a numeric
reward or a comparison between two candidates.

One node may serve more than one role. A solver can construct and assess a plan
at the same time. We do not require exactly three Python statements.

## 5. Examples that define the boundary

### A. One-step lookahead: yes

```python
def get_action(position):
    moves = [-1, 1]
    return min(moves, key=lambda move: abs((position + move) - 5))
```

For `position = 2`:

| Possibility | Predicted position | Assessment |
| --- | --- | --- |
| Move left | 1 | Distance to goal = 4 |
| Move right | 3 | Distance to goal = 2 |

The policy chooses right. `position + move` predicts; the distance assesses;
`min` chooses. Depth is **1 model step**, breadth is **2 candidate movements**,
and transition work is **2 evaluations**.

### B. Current sensor correction: no

```python
def get_action(measured_clearance):
    corrected_clearance = measured_clearance + 0.1
    return "STOP" if corrected_clearance < 0.2 else "GO"
```

The addition corrects a current measurement. It does not predict the result of a
possible action. There is a choice, but the prospective part is absent.

`value + offset` is therefore not enough evidence of planning. Meaning matters.
The same numeric operations can describe calibration, prediction, or placement.

### C. Prediction that is never assessed: no

```python
def get_action(position):
    possible_positions = [position - 1, position + 1]
    return "WAIT"
```

The predictions execute, but they do not feed any assessment or planning choice.
They are prediction work, not a complete planning computation under this rule.

### D. Checking one proposed route: yes

```python
def get_action(blocked):
    route = ["S", "B", "G"]
    if all(node not in blocked for node in route):
        return "B"
    return "WAIT"
```

The route is prospective behavior. Checking blocked nodes assesses it. Choosing
to follow it or wait supplies the decision role. Breadth is **1 route**. Its full
proposed horizon is **2 graph edges**. No dynamics model was run, so we do not call
that “simulation depth 2.” This snippet explains the definition; this exact
generator-based implementation is not automatically supported yet.

A route may be written as a constant in code and still be assessed online. That
differs from executing a constant action list without checking it.

### E. Every route fails: still yes

```python
def get_action(blocked):
    routes = [["S", "A", "G"], ["S", "B", "G"]]
    for route in routes:
        if route_is_clear(route, blocked):
            return route[1]
    return "WAIT"
```

If both A and B are blocked, the policy checks two routes and waits because neither
worked. Failure to find a plan does not erase the work. The failed checks also
contribute to the wait decision.

If it returns after the first clear route, the second route was not assessed on
that execution and must not be counted.

### F. Choosing a placement: yes

```python
def get_action(occupied_slots):
    candidates = [1, 2, 3, 4]
    feasible = [slot for slot in candidates if slot not in occupied_slots]
    return min(feasible, key=lambda slot: abs(slot - 3))
```

Here the returned number commands a box placement. If slot 3 is occupied, choose
slot 2. These are intended placements, not alternative estimates of where a box
already is. No explicit future-state rollout is necessary.

### G. Choosing a task order: yes

Consider `grasp → clear` and `clear → grasp`. The object starts inaccessible.
Clearing makes it accessible; grasping requires accessibility. Checking these
effects and prerequisites selects `clear → grasp`.

The hypotheses are task sequences, the assessment checks prerequisites, and the
decision selects an order. Task steps and low-level movement steps are different
units, so their horizons must not be silently mixed.

### H. Reasoning about uncertainty: yes

A risky action gives reward 10 with probability 0.5 and reward −20 otherwise.
Its expected reward is `0.5 × 10 + 0.5 × (−20) = −5`. A safe action gives 2.
Comparing those outcomes selects the safe action.

Another example: the target is equally likely to be left or right. Guessing earns
expected reward 5. Perfectly inspecting first gives reward 10 minus inspection
cost 1, or 9. Comparing “inspect then choose” with “choose now” selects inspection.
This is reasoning about future behavior even when computed with a short formula.
The formula's dependency length is not a simulated-state depth.

### I. Planning is computed, then discarded: performed, but not action-relevant

```python
def get_action(position):
    chosen = min([-1, 1], key=lambda move: abs(position + move - 5))
    return "WAIT"  # ignores chosen
```

The internal choice completes the planning pattern. The final action ignores it.
We count the planning as performed, but not as contributing to the returned action.

### J. Cached planning: count the computation once

During `reset`, evaluate three candidate sequences of three movements each and
store the best sequence. Later, return its three movements in separate calls.

| Stage | Newly performed transition work | Depends on earlier planning? |
| --- | --- | --- |
| Reset | 9 evaluations | Creates the plan |
| First action | 0 | Yes |
| Second action | 0 | Yes |
| Third action | 0 | Yes |

Episode transition work is **9**, not 27. The original reasoning has depth **3**.
Its three candidates are **whole sequences at that choice**, not nine alternatives.
The stored plan's original horizon is not automatically its remaining horizon.

A hardcoded action list with no online assessment does not demonstrate planning
performed in this trace. We make no claim about how it was designed or trained.

### K. Unexecuted code: no work on this run

```python
def get_action(position):
    if position < 0:
        return min([-1, 1], key=lambda move: abs(position + move))
    return 0
```

For positive input, the planning branch does not run. For negative input, it can.
An execution-based result concerns the tested inputs, not every possible execution
of the file. A class that is never instantiated and called also supplies no
evidence of planning performed during a run.

## 6. Three layers in the system

| Layer | Its job | Example |
| --- | --- | --- |
| Record execution | Record what ran and which inputs or conditions it used | Addition → distance calculation → comparison |
| Interpret meaning | Identify possibilities, assessments, and choices | “This addition predicts a movement outcome” |
| Measure | Count or measure the interpreted reasoning | Depth 1, breadth 2, two transition evaluations |

These layers are related, but not interchangeable. Correct recording does not
guarantee correct interpretation. An interpretation can be plausible but wrong.
A recognized planning computation may still lack a reliable numeric horizon.

For meaning, the implementation currently has two main sources:

- **Heuristic:** infer likely meaning from code patterns. Example: a state-like
  value plus a candidate movement, followed by comparison. This can mistake
  calibration offsets for movements.
- **Declared API contract:** supply the meaning of a shared operation. Example:
  `route_clear(route, blocked)` checks one prospective route; `model.step(s,a)`
  predicts one successor. This meaning is declared and must be reviewed. The
  tracer does not automatically verify that the declaration is true.

An API contract should apply to the same operation in every policy using it. It
must not mean “this particular file is planning.” Neither a familiar function name
nor an arbitrary NumPy call proves what an operation means.

## 7. What the execution graph means

\[
G=(V,E_{\mathrm{data}},E_{\mathrm{control}}).
\]

- `V`: individual operations that actually executed.
- A data edge: “this operation used that earlier result.”
- A control edge: “this operation ran, or this value survived, because of that
  earlier condition.”

Example: “route is blocked” can lead to the final `WAIT` through control flow,
even though `WAIT` does not contain the route-check result as a numeric input.
The implementation now retains guards against returning from the function when
execution continues after a loop. This covers the failed-route-search example.
General exception and concurrency dependencies still need work.

One source statement may execute many times and produce many graph events.
Unexecuted statements produce no computation events. Dependencies point backward
to earlier events, including earlier lifecycle calls when a plan is cached.

The system preserves the original static graph as a separate baseline. Static
structure can show code that might run. The runtime graph describes the particular
execution we observed.

## 8. Performed planning versus planning behind an action

Let `P(G)` be the planning computations identified in the recorded execution.
For action `a_t`, let `Anc(a_t)` be all recorded events that can reach that action
through data or control dependencies.

\[
P_t=\{p\in P(G):\operatorname{DecisionEvents}(p)\cap
\operatorname{Anc}(a_t)\ne\varnothing\}.
\]

In words: a planning computation is associated with an action if its decision
events feed that action through the recorded dependencies.

This measures **recorded dependence**, not proof that changing the computation
would change the action. That stronger question would require intervention or
counterfactual tests, which are not implemented.

Rejected alternatives can contribute to the decision. “Only the selected route
matters” would incorrectly discard the comparisons that made it the winner.
Unrelated planning can be performed without contributing to any returned action.

## 9. Measurement rules

### Depth: how many model steps ahead?

For a root observation, `depth = 0`. For a declared one-step model:

\[
\operatorname{depth}(T(s,a))=\operatorname{depth}(s)+1.
\]

The depth of a planning computation is the maximum linked hypothetical model
depth it used. Ten predictions made independently from the current state have
depth 1, not 10. One chain of ten predictions has depth 10.

A real environment step is not hypothetical planning. A loop iteration, matrix
operation, or collision sample is not automatically a model step.

### Breadth: how many alternatives were assessed?

\[
B(d)=|\{h:h\text{ was assessed for decision }d\}/\!\sim|.
\]

`~` means “counts as the same alternative under our stated equality rule.” A
decision considering left and right has breadth 2. Checking one route has breadth
1. Checking the same route three times has breadth 1 and three evaluations.

Breadth belongs to a specified choice, with a specified candidate type. Two root
actions, three complete trajectories, and ten sampled configurations are not the
same kind of count. We do not add all these numbers into a universal breadth.

Current equality is deliberately limited: bounded plain Python values are
compared by type and structure. Equal node lists count as the same route. A list
and a tuple are different representations under this rule. Arbitrary objects,
NaNs, and large or cyclic structures have unknown identity. We do not call
user-defined equality methods or merge approximately equal states automatically.

For `min`/`max`/`sorted`, the current implementation can count distinct assessed
selection inputs. For supported scalar comparison loops it can count distinct
first-step action candidates. These are labeled separately. General identification
of whole search episodes and candidate identity across representations is future
work; grouping repeated conditions by invocation and source site is approximate.

### Work: how many computations ran?

Let `T(p)` be the IDs of actual transition evaluations used in planning computation
`p`. Then:

\[
W_{\mathrm{performed}}=\left|\bigcup_{p\in P(G)}T(p)\right|,
\qquad
W_{\mathrm{action}}=\left|\bigcup_t\bigcup_{p\in P_t}T(p)\right|.
\]

The union means an existing computation is counted once, even when reused. A fresh
evaluation of the same state and action gets a new ID and counts as new work.
For work during one call, count only IDs created during that call.

We also count assessment evaluations at declared API boundaries. A route-check
call counts as one assessment even if it checks many points internally. Internal
collision rows require another separately defined measurement.

Transition evaluations, candidate evaluations, collision checks, and optimizer
iterations retain separate units. CPU time and trace-event count can be diagnostics,
but neither is a general planningness score.

### Horizon: how far does a proposed route or task sequence extend?

For a graph route with `n` nodes, the full proposed route has `n−1` edges. For a
task list, a declared task horizon may be its number of tasks.

Current contracts can measure these two sequence extents with an explicit unit.
The reported maximum is the longest **assessed candidate**, including a candidate
rejected early. It describes the proposed candidate's extent; it does not claim
that every edge was checked or that the route was selected or is executable.

Physical duration, nominal movement actions, remaining cached horizon, and
selected-route horizon need their own definitions and general implementations.
More collision samples must not make a route look farther into the future.

### Unknown, not applicable, and zero

| Value/status | Meaning |
| --- | --- |
| Measured value | A count or extent under the stated interpretation and unit |
| Unknown | We cannot measure this reliably with the current trace/interpretation |
| Not applicable | This kind of measure does not apply to the described operation |
| Zero | No counted events under the recognizer and its stated assumptions |

For a geometric checker with no explicit dynamics rollout, model depth is not
applicable to that checker. If the code hides an unsupported simulator, depth is
unknown. These are different from proving that the policy did no planning.

An interrupted trace invalidates complete-run aggregates. Unknown semantic
coverage can remain even when all recorded syntax was supported. In particular,
the current analyzer can still produce incorrect zeros for missed categories.

## 10. Categories we want to cover

| Category | What is considered? | What is checked? | Examples |
| --- | --- | --- | --- |
| Action–effect | Actions, successors, trajectories | Consequences and objective values | One-step lookahead, rollout, tree search |
| Configuration/route | Placements, configurations, paths | Feasibility, collision, path cost | Route validation, placement search |
| Task/constraint | Task orders, assignments, abstract plans | Preconditions, constraints, task cost | Clear before grasping, scheduling |
| Contingency/information | Possible outcomes, conditional strategies, information gathering | Expected utility, risk, information benefit | Risky versus safe; inspect before acting |

The categories overlap. Task planning can also predict state changes. Geometric
planning can be embedded in a larger task plan. Reporting several tags does not
mean counting the same work several times.

Optimization may also qualify when it constructs and assesses prospective behavior.
A trajectory optimizer does not need to enumerate named routes in a Python loop.
General solver and optimizer support is planned, not currently demonstrated.

## 11. What runs, and where execution begins

The intended RoboCode lifecycle is:

```text
load module → construct policy → reset
                              → get_action → real environment step → update
                              → get_action → ...
```

`get_action` is the default returned-action boundary. Planning in construction or
reset can contribute to later actions. We retain its origin rather than counting
it again on every call. Other entry points can be designated explicitly.

For small benchmark snippets we supply inputs and call order directly. No live
environment is needed. For real RoboCode policies we run the matching environment,
or reuse saved run settings, to obtain meaningful observations. The policy code
alone does not determine every input, seed, or task instance that it may encounter.

A file with no returned action is not evaluated as an action policy. A run with
no observed planning does not establish that no other input would trigger it.

## 12. What is implemented now

| Component | Current state |
| --- | --- |
| Static reference baseline | Preserved independently |
| Runtime tracing and cached dependencies | Implemented for supported synchronous Python |
| Ordinary-versus-traced output checks | Implemented for benchmark fixtures |
| Explicit semantic profile | Implemented: source-event IDs for hypotheses, assessments, decisions; category tags; interpretation basis; action association |
| Heuristic scalar lookahead | Implemented, but has a demonstrated calibration false positive |
| Declared one-step model calls | Implemented |
| Declared pure assessment calls | Implemented: candidate argument, candidate type, category, optional typed sequence extent |
| General role recognition without contracts | Partial; many cases are missed |
| Breadth | Implemented for supported selection inputs, first-step scalar actions, and declared assessed candidates |
| Work | Transition work plus declared assessment work; reused event IDs counted once |
| Route/task horizon | Optional sequence edges/items under a contract; broader horizon measures remain planned |
| General NumPy internals and generators | Not implemented |
| General task, uncertainty, optimization recognition | Not implemented |
| Single planningness score | Not defined |

Example of a reusable contract in runtime configuration:

```python
from policy_graph.runtime import AssessmentContract, RuntimeConfig

config = RuntimeConfig(assessments={
    "navigation.route_clear": AssessmentContract(
        candidate_arg=0,
        category="configuration_route",
        candidate_kind="route",
        horizon="sequence_edges",
        horizon_unit="graph edges",
        model_free=True,
    ),
})
```

This declares that the named shared API is pure, depends only on its explicit
arguments, and checks a prospective route. Its normal implementation runs once.
The recorder adds a hypothesis/assessment boundary; ordinary selection or
control flow must still use that assessment to establish a decision.

The declaration does not by itself label every call planning: an unused check
has no decision role. Conversely, giving an ordinary calibration function an
incorrect prospective contract could produce a false planning label. Contracts
are explicit assumptions, not automatic proofs.

`model_free=True` additionally declares that this checker does not simulate model
transitions internally. Without that promise, hidden model depth and transition
work remain **unknown**, even when candidate breadth and assessment work can be
counted. A pure assessment function can contain a simulator; purity alone does
not establish that simulation depth is not applicable.

The contract describes the hypothesis and assessment. The current decision role
is still inferred from value selection or control flow, and is labeled that way
in `role_basis`. For example, distinguishing a behavior choice from a condition
used only for logging needs further negative controls and stronger role rules.
`role_chain_present` means the inferred roles are connected in the record; it
does not certify that all their meanings are correct.

The profile appears in JSON under `semantic_profile`. Older top-level scores
remain for compatibility. The legacy direct-model fallback can still report a
model-based event without exposing all three roles; such a profile has an
incomplete role chain. The new representation makes this limitation visible;
reconciling all legacy recognition rules with the definition remains work.

The Obstruction2D implementation is retained only as an explicitly selected
reference measurement. It is excluded from the normal analyzer and benchmark.
Its previously measured path-search counts do not demonstrate general geometric
recognition. The original policy can still reach the generic trace limit.

## 13. Benchmark: what the command actually checks

```bash
.venv/bin/python -m policy_graph.benchmarks
.venv/bin/python -m policy_graph.benchmarks --track both --json /tmp/planning.json
.venv/bin/python -m policy_graph.benchmarks --list
```

Each example has source code, explicit calls/inputs, expected outputs, expected
planning labels, and descriptions of the three roles. Some also specify exact
depth, work, breadth, or route extent. These answers are not supplied to tracing.

The runner:

1. Runs the example normally and checks its expected output.
2. Runs it with tracing and checks that the output is unchanged.
3. Checks whether planning was performed and whether it fed a returned action.
4. Checks the numeric expectations that exist for that example.
5. Reports mistakes and unknowns without silently dropping cases.

There are two separate tracks. **Automatic** supplies no additional shared API
contracts. **Shared contracts** supplies meanings for the same shared model,
route-check, and placement-cost APIs in every case. Both use the same expected
answers. A contract-assisted result must not be presented as automatic discovery.

The v0.2 development benchmark contains **25 scenarios**: the original 21 plus
four shared-API scenarios. Current results:

| Track | All expectations met | Outputs preserved | False positives | False negatives | Unknown |
| --- | --- | --- | --- | --- | --- |
| Automatic | 10/25 | 25/25 | 1 | 12 | 2 |
| Shared contracts | 14/25 | 25/25 | 1 | 8 | 2 |

Error counts happen to match for performed and action-relevant labels in this
run; they are evaluated separately. The original 21 scenarios still yield 9/21
and 10/21 respectively. Adding examples changed the denominator; the new totals
must not be presented as an accuracy improvement on the original set.

Known gaps remain: calibration alternatives are misread as planning, raw route
and placement code is missed, task and uncertainty reasoning is missed, and NumPy
and generator versions report unknown. The new shared-API route and placement
cases succeed only with the declared meanings.

Equivalent implementations are compared, too. Correct scalar callback and loop
versions should agree on depth and breadth. Loop-to-NumPy equivalence currently
exposes missing support. Two equally wrong route answers do not count as success.

This is a **development set**, not a held-out estimate of generality. Passing
software tests validates behavior and bookkeeping; it does not make benchmark
recognition failures disappear. `--strict` returns failure for any unmet semantic
expectation; ordinary mode returns successfully after reporting the results.

Implementation verification for this milestone: **453 tests passed, 5 skipped**,
including 92 runtime tests and 38 benchmark-harness tests. Format, lint, and the
repository's type checks passed. All 12 recorded static-baseline hashes match.
These are separate checks from the 10/25 and 14/25 semantic benchmark results.

## 14. Planned implementation and how we will judge it

| Step | Work to implement | Evidence needed before calling it done |
| --- | --- | --- |
| 1. Make interpretation explicit | Common hypothesis/assessment/decision representation, provenance, assumptions, units | Inspectable event links; unused or disconnected operations do not become complete planning |
| 2. Broaden recognition | Reusable assessment/model interfaces; structural reasoning rules for inline code | The same rule works across multiple policies, helpers, loops, and negative examples |
| 3. Strengthen tracing | NumPy/batched models, generators, exceptions, aliases and mutation, numerical libraries | Ordinary/traced outputs agree; uncertainty is retained where dependencies remain unsupported |
| 4. Strengthen measurements | Candidate identity and decision boundaries, route/task/time horizons, selected versus assessed extent | Repeated work does not inflate breadth; denser collision sampling does not inflate horizon |
| 5. Cover more reasoning | Task constraints, contingent outcomes, information gathering, hierarchical planning, optimizers | Matched positive/negative examples and multiple implementations for each category |
| 6. Validate generality | Independent label review, unfamiliar algorithms, held-out policies, multiple inputs/seeds | Report precision, recall, abstentions, metric error, coverage, and behavior changes separately |
| 7. Consider an overall score | Agree purpose, normalization, units, and weights | Evidence that the scalar answers the research question rather than rewarding wasted work |

Steps 1 and 4 now have initial implementations, and step 2 has reusable declared
assessment boundaries. None of these steps is complete for arbitrary programs.
No numerical-library operation will be called planning solely because it uses
NumPy, and no source fingerprint will be added to improve general benchmark scores.

Benchmark expansion should include shared prefixes, duplicate states, early
termination, branch coverage, failed/abandoned plans, cache invalidation, nested
search, different representation types, and solver-internal decisions. Matched
controls should separate current-state estimation from prospective reasoning.

For the held-out evaluation, split by algorithm/policy family rather than merely
renaming variables. Freeze labels and protocols before evaluation. Preserve
failures, missing dependencies, and timeouts in the denominator or report them
explicitly alongside conditional accuracy.

## 15. Decisions we should discuss with advisors

1. **What is the score for?** Detecting any planning, comparing lookahead depth,
   describing reasoning styles, or predicting task success are different goals.
2. **Where may meaning come from?** Are shared API contracts acceptable, or must
   the deployed analyzer work only from code and inputs? Report both until settled.
3. **Where is the boundary with reactive value ranking?** A learned score or a
   lookup can encode prior planning without performing it now. We need paired
   examples and an explicit rule for action-value comparisons.
4. **What counts as the same candidate?** Type/structure, approximately equal
   geometry, equivalent outcomes, and equivalent behavior give different breadth.
5. **What is one decision episode?** A loop site is an implementation convenience,
   not a universal definition of a search. Nested and hierarchical search need care.
6. **How should horizons compare?** Model steps, graph edges, abstract tasks, and
   seconds cannot be equated without additional domain information.
7. **How should task difficulty be handled?** More objects can require more work.
   Report task/input size and outcome separately before proposing normalization.
8. **What makes the ground truth credible?** Use independent review, disagreements,
   boundary cases, and held-out programs; do not derive labels from current output.

## 16. Claims we can and cannot make

We can inspect evidence from particular executions, measure supported operations
under declared assumptions, and show where recognition fails on authored examples.

We cannot yet claim complete planning detection, universal semantic inference,
equivalent measurement for all Python representations, proof of causal necessity,
or that a larger score means better intelligence or better actions. Tracing also
adds runtime overhead and may change how much a time-budgeted search can explore.
Results must name the inputs, trace limits, contracts, interpretation method, and
measurement units.

## 17. Relation to existing planning literature

Our three-role test and score design are project proposals. They are motivated
by a broader view of reasoning about actions and objectives, as discussed in
[Ghallab, Nau, and Traverso, *Automated Planning and Acting*, introduction](https://www.cambridge.org/core/books/automated-planning-and-acting/introduction/300E2FA41FC61295DFBB7A0E8E7EAFA6).

Including routes without explicit simulation is consistent with the separate
treatment of geometric paths, trajectories, and dynamics in
[LaValle, *Planning Algorithms*](https://lavalle.pl/planning/book.pdf).
These sources motivate the scope; they do not validate our particular detection
rules, benchmark labels, or numeric measurements.

## Appendix: benchmark cases

The companion `cases.py` contains executable code and inputs for every case.
The table below lists the intended labels, not the analyzer's predictions.

| Case | What it tests | Planning performed? | Feeds an action? |
| --- | --- | --- | --- |
| `current_correction` | Calibrate a current clearance measurement and apply a reactive threshold. | No | No |
| `calibration_alternatives` | Estimate current clearance under three calibration offsets; no prospective behavior is assessed. | No | No |
| `unused_prediction` | Predict possible movements but do not assess them or use them in a decision. | No | No |
| `unexecuted_branch` | The only planning branch is not executed for the supplied observation. | No | No |
| `one_step_min` | One-step action selection using a scalar comprehension callback. | Yes | Yes |
| `one_step_loop` | The same one-step decision expressed as a best-so-far loop. | Yes | Yes |
| `one_step_helper` | The same decision with renamed variables and a helper function. | Yes | Yes |
| `one_step_numpy` | The same three evaluations computed in a NumPy batch. | Yes | Yes |
| `one_step_generator` | The same decision evaluated through a generator expression. | Yes | Yes |
| `shared_model_rollout` | Three successor steps for each of three actions, using the shared model API. | Yes | Yes |
| `route_selection` | Choose the shortest feasible route around observed blocked nodes. | Yes | Yes |
| `route_selection_loop` | The same route choice, with feasibility and selection implemented in loops. | Yes | Yes |
| `single_route_validation` | Validate one proposed route before committing to its first movement. | Yes | Yes |
| `failed_route_search` | All proposed routes are infeasible; the failed search determines a wait action. | Yes | Yes |
| `placement_choice` | Choose an intended box placement in an unoccupied slot near slot 3. | Yes | Yes |
| `discarded_search` | A planning computation runs, but its selected action is discarded. | Yes | No |
| `cached_plan` | Compute a three-movement plan during reset and reuse it for three returned actions. | Yes | Yes |
| `hardcoded_sequence` | Execute a fixed sequence without constructing or assessing it during this trace. | No | No |
| `task_order` | Find a task ordering that satisfies clearing-before-grasping prerequisites. | Yes | Yes |
| `contingent_choice` | Compare a risky action's possible outcomes with a safe alternative. | Yes | Yes |
| `information_choice` | Compare inspecting before acting with acting immediately under uncertainty. | Yes | Yes |
| `shared_single_route` | Validate one route using a shared checking API. | Yes | Yes |
| `shared_failed_routes` | Repeated failed route checks: two distinct routes, three evaluations. | Yes | Yes |
| `shared_placement` | Rank prospective placements using the shared cost API. | Yes | Yes |
| `shared_unused_check` | Check a proposed route but never use the result in a decision. | No | No |

The original cases are retained when they fail. The shared-API cases supplement
them; they do not replace unsupported inline versions.
