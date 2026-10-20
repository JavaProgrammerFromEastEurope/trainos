# TrainOS Stage 46 — Explicit recovery reconciliation

## Scope

Added an explicit, reasoned reconciliation workflow for executions classified as `recovery_required`. The workflow never infers the result of an interrupted external action.

## Changes

- Added `ExecutionAuditStore.reconcile_recovery()` with three decisions: `manual_investigation`, `confirmed_completed`, and `confirmed_failed`.
- Manual investigation appends a separate reconciliation record while preserving the execution's `recovery_required` status.
- A confirmed final decision atomically records the decision and appends a terminal `completed` or `failed` audit transition with a required reason.
- Added optional evidence references and a query method for reconciliation history.
- Added a SQLite migration for the new nullable `transition_reason` column, preserving existing databases.
- Ordinary `append()` still rejects direct transitions out of `recovery_required`; final transitions are only possible through the reconciliation method.

## Verification

- Full test suite: **424 passed** (`PYTHONPATH="$PWD" python3 -m pytest tests -q`).
- `python3 -m compileall -q kernel tests`: passed.
- AST parsing of all **2,110** Python files under `kernel`: zero syntax errors.
- `unzip -t /mnt/data/trainos_stage46.zip`: passed.

## Limits

The API records operator/application assertions; it does not independently verify external side effects, authenticate the decision-maker, or provide a tamper-proof ledger. Production use should add authorization, evidence validation, backup/recovery policy, and independent safety controls.
