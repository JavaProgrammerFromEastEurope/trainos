# TrainOS Stage 45 — Recovery classification for interrupted executions

## Scope

Added explicit startup-recovery classification for command executions whose last durable state is `running`. Recovery records the ambiguity; it does not rerun commands or assume whether an external side effect happened.

## Changes

- Added `ExecutionStatus.RECOVERY_REQUIRED`.
- Extended the audit transition policy so `running -> recovery_required` is permitted and the recovery state is terminal until an explicit reconciliation workflow is designed.
- Added `ExecutionAuditStore.recover_incomplete_executions()`, which identifies only executions whose latest persisted transition is `running`, appends a recovery-required transition, and returns the affected immutable execution records.
- Added `ExecutionAuditStore.get_latest_status()` for startup/reconciliation checks.
- Added tests for restart recovery, terminal executions, repeated recovery, independent concurrent records, and refusal to silently mark a recovery-required execution completed.

## Verification

- Full test suite: **417 passed** (`PYTHONPATH="$PWD" python3 -m pytest tests -q`).
- `python3 -m compileall -q kernel tests`: passed.
- AST parsing of all **2,110** Python files under `kernel`: zero syntax errors.

## Limits

Recovery classifies interrupted work; it does not prove whether a handler's external action occurred. Never automatically replay recovered commands without command-specific idempotency and reconciliation guarantees. SQLite is an application store, not a tamper-proof or safety-certified ledger.
