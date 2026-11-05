# NumPy in the runtime tracer

The tracer runs every NumPy operation natively, on the real objects, exactly as the
untraced policy would. Results, dtypes, views, exceptions (for example
`IndexError`, broadcasting `ValueError`, ambiguous truth values) and in-place
updates are NumPy's own. What the tracer adds is a record of *which earlier values
each result depends on*. This page describes how detailed that record is.

## What is supported

| Operation | How it is recorded |
| --- | --- |
| Arithmetic, comparisons and unary operators on arrays and NumPy scalars, including broadcasting and `@` | One event per operation, depending on the whole operands |
| NumPy functions, ufuncs and their methods (`reduce`, `outer`, ...), ndarray methods: construction (`np.array`, `np.zeros`, ...), reductions (`sum`, `argmin`, `np.any`, ...), `np.where`, `np.clip`, stacking, `linalg`, ... | One `array-operation` event depending on the whole arguments; no event per element |
| Indexing with integers, slices, `None`, `...`, index arrays, boolean masks and any combination (`a[:, :2]`, `a[idx]`, `a[mask]`, `a[1, idx]`) | One `item-read` event depending on the whole array and on the exact index |
| Writes: `a[key] = v`, `a += v`, `out=` arguments, `np.copyto`, `fill`, `sort`, `ufunc.at`, ... | The new contents depend on the old contents, the index and the written value |
| Views and aliases | A write through any view or alias updates the provenance shared by all arrays on the same memory (the root of NumPy's `.base` chain) |
| Writes in branches and loops that did not execute | Later reads still depend on the test that decided they did not run |
| Iteration and unpacking (`for row in a`, `x, y = a[:2]`), `tolist()`, `list(a)` | Each part depends on the whole array |

## Where precision is lost

NumPy arrays do not keep a separate record for each element. Reading part of an
array (`a[0]`, `a[:2]`, a row while iterating, `a.tolist()`) is therefore recorded
as depending on the **whole** array. This is conservative: it can include
dependencies that are not real, but it never omits a real one. These events are
marked with `imprecise_parents` and drawn as dotted edges in DOT output.

The report checks whether this matters:

- A planning decision reached from an action **only** through such whole-array
  edges is reported as `possibly_action_relevant`, not `action_relevant`. If no
  decision is exactly relevant, the verdict is `needs_review`, never
  `planning_observed` or `no_planning_observed`.
- If transitions are reached from a decision only through such edges, its depth
  and work are `null`, with the reason *"Whole-array dependencies may include
  unrelated transitions"*. The counts would be upper bounds, not measurements.
- `precision.affects_scores` says whether either case occurred;
  `precision.imprecise_events_in_action_slices` counts the flagged events.

Example: `values = np.array([obs * 2, planned]); return float(values[0])` truly
does not depend on `planned`, but it is reported as *possibly* relevant, not as
planning.

## What is not interpreted as planning

NumPy support adds dependencies, not planning heuristics. The scalar arithmetic
rule (state ± candidate is a hypothetical transition) still applies only to plain
`int`/`float`. Arrays have no candidate marks, so a NumPy addition or subtraction of
a state-derived value and either a candidate or **any multi-element array** (which
could be a batch of candidate actions) is recorded as **unknown**. It is never
recorded as transitions, and never as evidence that no planning happened. For
example, `obs + moves` with `moves = np.array([-1, 0, 1])` makes the report
`needs_review`. Batched candidate evaluation is not recognized as planning.

## Still opaque (unknown dependencies)

- `numpy.random` (hidden generator state), file I/O (`np.load`, `np.save`, ...);
- object-dtype arrays and array subclasses (their operators can run user code);
- NumPy functions that receive a callable (`np.vectorize`, `np.apply_along_axis`);
- bound methods called without their array's provenance;
- library objects that wrap arrays, such as environment state accessors (for
  example `ObjectCentricState.get`), unless declared `pure_functions`.

Opaque calls make the affected counts unknown, as before. Memory shared with
non-NumPy buffers through `memoryview` is followed one level only.
