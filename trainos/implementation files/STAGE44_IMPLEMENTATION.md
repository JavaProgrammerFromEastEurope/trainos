# TrainOS Stage 44 — Durable execution audit history

## Scope

Added an optional SQLite-backed append-only audit store for command execution lifecycle transitions. The existing in-memory registry remains available and default behavior is unchanged unless an audit store is explicitly supplied.

## Changes

- `trainos/kernel/command/execution/execution_audit_store.py`: new SQLite audit store with transactional writes, execution and command history queries, reopen-after-restart support, duplicate-write idempotency, and transition-order validation.
- `trainos/kernel/command/bus/command_dispatcher.py`: optional `audit_store` integration records every lifecycle state transition while preserving the existing constructor behavior for callers that do not configure persistence.
- `trainos/tests/stage44/test_execution_audit_store.py`: tests persistence after reopening the database, successful and failed dispatch history, duplicate writes, invalid transition ordering, ID reuse, and input validation.

## Verification

- Full test suite: **412 passed** (`PYTHONPATH="$PWD" python3 -m pytest tests -q`, run from `trainos/`).
- `python3 -m compileall -q kernel tests`: passed.
- AST parsing of all **2,110** Python files under `kernel`: zero syntax errors.
- ZIP integrity check: passed.

## Limits and operational notes

- Persistence is opt-in. Construct `ExecutionAuditStore("path/to/execution-audit.sqlite3")` and pass it as `audit_store=` to `CommandDispatcher`.
- SQLite history survives application process restarts, but the store is not tamper-proof, replicated, or designed as a safety-certified audit ledger.
- If a durable write fails, dispatch does not silently report success; the storage exception can surface. For commands with external side effects, production integration must define recovery/reconciliation semantics before enabling this store.
- This is application-level history, not authorization to control traction, braking, levitation, or life-support hardware.
