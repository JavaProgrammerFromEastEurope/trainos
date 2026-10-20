# TrainOS Stage 50 — Diagnostic recurrence correlation

## Implemented

- Extended each retained execution diagnostic group (`execution_id`, `code`) with occurrence count, first-seen timestamp, latest event details, and a `repeated` indicator.
- Added global snapshot metrics for retained repeated groups and repeated occurrences.
- Added `ExecutionDiagnosticSummary` and `summary_for_execution()` for severity/group/recurrence summaries over currently retained groups.
- Kept correlation bounded by the existing `max_findings` limit. Evicting a group also evicts its per-group recurrence metadata; cumulative global event and severity counters remain available.
- Hardened severity validation so malformed unhashable values are counted instead of raising during event processing.
- Exported the new summary type from the existing events package.

## Scope and limitations

This is an in-memory diagnostic correlation layer, not durable audit history or an automated remediation mechanism. Per-execution summaries describe retained groups only. Execution-history verification remains read-only; no records are repaired and no operational actions are triggered.

## Verification

Verification results are recorded below after running the test suite, compile check, syntax audit, and archive integrity check.

- Focused Stage 49–50 tests: **10 passed**.
- Full test suite: **444 passed**.
- `python3 -m compileall -q kernel tests`: passed.
- AST parse of all kernel Python files: passed with zero syntax errors.
