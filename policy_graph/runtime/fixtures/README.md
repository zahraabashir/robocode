`obstruction2d_polyline.py.txt` is the unmodified generated policy from
`agent_runs/environments/Obstruction2D/runs/claude_opus55_high_r42_820cc0f3/evidence/final/approach.py`.
It is retained as a regression fixture so tests do not depend on local run archives.
The `.txt` suffix prevents formatters from rewriting the original evidence.

The explicit reference under `../reference/` checks its AST fingerprint, including
constants, imports, and controller logic, before applying the semantic contract.
Only whitespace/comments and the positive collision sample spacing literal may
vary; other source changes are rejected by that reference. Normal runtime analysis
never selects it, even for this exact source. The fixture preserves reference
evidence, not a recognition rule for the general planning benchmark.
