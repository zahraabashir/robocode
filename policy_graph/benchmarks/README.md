# Planning benchmark v0.2

This development benchmark compares the runtime analyzer with independently
specified planning semantics. Start with [ADVISOR_NOTES.md](ADVISOR_NOTES.md) for
the Notion-ready explanation, notation, examples, cases, and implementation plan.
Read [FORMALISM.md](FORMALISM.md) for the compact definition,
agreements, proposals, and measurement units. Inspect the executable examples and
their labels in [cases.py](cases.py).

From the repository root:

```bash
.venv/bin/python -m policy_graph.benchmarks
.venv/bin/python -m policy_graph.benchmarks --list
.venv/bin/python -m policy_graph.benchmarks --case single_route_validation
.venv/bin/python -m policy_graph.benchmarks --track both --json /tmp/planning-benchmark.json
```

`--strict` returns exit code 1 if any expectation is unmet, including abstentions,
missing dependencies, and numeric errors. The ordinary command returns 0 after
successfully producing a report, even when it discovers semantic gaps. NumPy is
required for its batching fixture; missing NumPy is recorded, never silently
removed from the denominator. No RoboCode environment simulation is required for
these small fixtures: inputs and expected outputs are explicit in each case.

## Scope

The 25 scenarios include the original 21 plus four shared-API cases:

| Family | What it distinguishes |
| --- | --- |
| Calibration, unused prediction, unexecuted branch | Current-state processing and prediction alone versus deliberation |
| One-step action choice in five forms | Callback, loop, helper, NumPy batch, generator |
| Three-step shared model | Automatic recognition versus a documented API contract |
| Route choice in two forms, one-route validation, failed search | Geometric reasoning without explicit dynamics rollouts |
| Placement, task order, risky outcome, information gathering | General categories beyond scalar prediction |
| Discarded search, cached plan, hardcoded sequence | Work performed versus contribution, reuse, and execution of prior choices |
| Shared route validation, repeated failed routes, placement, unused check | Declared API meaning; breadth versus repeated work; assessment without a decision |

Every case supplies expected ordinary outputs and independent performed/relevance
labels. Positive cases describe the prospective hypothesis, assessment, and
decision. Selected cases also specify exact depth/work. Equivalent one-step
examples now check breadth. Shared route cases check breadth, assessment work,
and candidate extent in graph edges. Raw inline route cases still test recognition
and remain unsupported. Fixture names, descriptions, labels, and category tags
are not passed to the analyzer.

Automatic recognition is the default. The optional `shared_contracts` track
declares `world_model.step` as a one-step transition, and `route_clear` and
`placement_cost` as pure assessments of prospective candidates. It uses
the same labels and no policy-specific rules. The choice to adopt this as a
deployment assumption is still open. The Obstruction2D reference is excluded from
both tracks.

## Initial baseline

[Baseline report](results/baseline-v0.1.json), produced on 2026-11-02:

| Track | All expectations met | Behavior preserved | False positives* | False negatives* | Abstentions* |
| --- | --- | --- | --- | --- | --- |
| Automatic | 9/21 | 21/21 | 1 | 9 | 2 |
| Shared contracts | 10/21 | 21/21 | 1 | 8 | 2 |

\* The counts happen to be the same for performed and action-relevant labels in
this baseline; both are evaluated and stored separately. These are two runs of
the same 21 scenarios, not 42 independent examples. Categories overlap.

The automatic recognizer misclassifies calibration alternatives as planning. It
misses generic route validation/selection, placements, task ordering, contingent
outcomes, and information gathering. NumPy and generator variants abstain. The
shared contract resolves the non-additive model example, not those other gaps.
The five equivalent one-step implementations therefore do not receive consistent
measurements; the two route implementations are consistent but both incorrect.

These failures are retained as research results. They are not `xfail` tests,
exceptions to the semantic labels, or evidence of general coverage. The report
includes source/API hashes, calls, units, runtime configuration, behavior checks,
and discrepancy details. It can be regenerated with the command above; the saved
baseline is a snapshot, not a golden output that future recognizers must copy.

## Current results (runtime-planning-4, 3 November 2026)

[Current report](results/current-v0.3.json):

| Track | All expectations met | Behavior preserved | False positives | False negatives | Unknown |
| --- | --- | --- | --- | --- | --- |
| Automatic | 11/25 | 25/25 | 1 | 12 | 1 |
| Shared contracts | 15/25 | 25/25 | 1 | 8 | 1 |

The original 21 now produce 10/21 and 11/21 respectively: generator-expression
tracing fixes one additional case in each track. The four added examples have the same
expected labels in both tracks. The shared contracts enable three positives;
the unused check is correctly negative in both. Numeric role-profile fields are
checked with their units, not just their numbers. Current runtime version is
`runtime-planning-4`, with `semantic_profile.version = planning-semantics-1`.

The profile records interpretation assumptions, roles, breadth, and optional
typed horizons. It does not repair the known calibration false positive or imply
general automatic support for the missing categories.

Harness validation is separate (38 tests). The full local regression command on
2026-11-02 passed **453 tests, 5 skipped**. These results validate implementation
behavior, not all semantic expectations. Run the current harness tests with:

```bash
python -m pytest policy_graph/benchmarks -q
```

Future generality claims require additional fixtures, independently reviewed
labels, held-out implementations, and multiple observed inputs per policy.

### Reusing the baseline recognition rules

The runtime now consults the unchanged static recognizer for graph search,
recursive search, ordering search, ranked generate-and-test, and lookahead.
It requires matching executed operations connected to a runtime decision;
a static verdict alone is insufficient. Evidence reports the reused rule,
assumptions, and trace witness IDs. Known planner/model contracts remain supported.
Separate runtime regression tests cover these families, unexecuted searches,
empty frontiers, recursive base cases, discarded results, and cached searches.
These regression tests are **not additional cases in the 25-case benchmark**.

The CLI now prints **labels only** separately from **all expectations**. JSON
also separates metric results by field. Both-label correctness happens to equal
all-expectations correctness in this snapshot: 11/25 automatic, 15/25 with contracts.
This is not a claim that labels and numeric scores are the same measurement.

Reusing the old rules does not solve all new benchmark categories. In particular,
the static analyzer also misses the inline route/placement examples and has the
calibration false positive. No benchmark names, variable-name meanings, or
per-policy fingerprints were added to force those labels to pass.

## Reliability update (runtime-planning-5, 3 November 2026)

[Report](results/current-v0.4.json). The tracer gained NumPy support, faster
reports and stricter reuse of the baseline's action-slice rules (see the
[runtime README](../runtime/README.md)). The benchmark outcome is **identical to
v0.3 in every case and track**, both for labels and for each numeric check:

| Track | Both labels correct | Numeric checks correct / unmeasured / incorrect | Behavior preserved |
| --- | --- | --- | --- |
| Automatic | 11/25 | 19 / 11 / 2 | 25/25 |
| Shared contracts | 15/25 | 29 / 3 / 0 | 25/25 |

Label correctness and numeric correctness are reported separately; here they
happen to give the same case count. `one_step_numpy` still abstains in both
tracks. NumPy arithmetic now has known dependencies, but a state-derived value
shifted by a possible batch of candidates is recorded as unknown rather than
interpreted. Without that safeguard this case became a false "no planning"
during development. The remaining gaps are the semantic coverage gaps listed
above; this update adds no planning rules.
