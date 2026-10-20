# TrainOS Stage 43 — Execution lifecycle integration

## Scope

Connected the Stage 42 command dispatch path to the existing execution lifecycle and command event subsystem. Dispatches now produce a persistent execution record and publish lifecycle events for creation, start, completion, or failure.

## Changes

- `kernel/command/execution/execution_engine.py`: added `create()` and `fail()` transitions; guarded lifecycle operations against invalid state transitions; preserved immutable execution records and existing `start()` / `complete()` APIs.
- `kernel/command/bus/command_dispatcher.py`: integrated `ExecutionEngine`, `ExecutionRegistry`, and optional `CommandEventService`. Each dispatch records its current execution state and returns execution ID/status along with the existing command outcome.
- `kernel/command/bus/command_dispatch_result.py`: added optional, validated `execution_id` and `execution_status` fields without changing the existing leading positional fields.
- `kernel/command/events/event_dispatcher.py`: observer exceptions no longer interrupt other subscribers or command lifecycle transitions; exceptions are available through `last_errors` for diagnostics.
- `pytest.ini`: configured pytest's `importlib` mode to avoid collisions between many legacy stage tests that share identical module basenames.
- `tests/stage43/test_command_lifecycle_integration.py`: added coverage for successful lifecycle, routing failure, executor failure, observer failure, and invalid state transitions.

## Verification

- Full test suite: **406 passed** (`PYTHONPATH="$PWD" python3 -m pytest tests -q`).
- `python3 -m compileall -q kernel tests`: passed.
- AST parsing of all **2,109** Python files under `kernel`: zero syntax errors.
- ZIP integrity check: passed.

## Known limits

- The execution record is in-memory; it is not durable across process restarts.
- Event dispatch remains synchronous and best-effort. Subscriber exceptions are recorded for the most recent event but are not persisted to an audit store.
- This is application-level lifecycle bookkeeping, not a certified safety controller. It must not be connected directly to traction, braking, levitation, or life-support hardware without independent safety interlocks, hardware-in-the-loop validation, and formal safety engineering.
