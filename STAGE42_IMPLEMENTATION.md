# TrainOS Stage 42 — End-to-end command dispatch

## Scope

Added a single software-level dispatch path that composes the Stage 41 registry-based router with the existing handler execution engine. It routes a command, resolves the exact selected handler ID, invokes its executor once, and returns a unified diagnostic result.

## Changes

- `kernel/command/bus/command_dispatcher.py`: `CommandDispatcher` orchestrates routing and execution without reimplementing either engine.
- `kernel/command/bus/command_dispatch_result.py`: immutable result model distinguishes routing failure, execution failure, and completion; enforces success/error/output invariants.
- `tests/stage42/test_command_dispatcher.py`: covers successful output propagation, missing handler, metadata-only handler, executor exception, ambiguous routing, invalid command, and result invariants.

## Verification

- Full test suite: **400 passed** (`PYTHONPATH="$PWD" python3 -m pytest tests -q`).
- `python3 -m compileall -q kernel tests`: passed.
- AST parsing of all **2,109** Python files under `kernel`: 0 syntax errors.
- ZIP integrity check (`unzip -t`): passed.

## Safety boundary

This is application-level command dispatch only. It is not a safety controller and must not be treated as authorization to operate real traction, braking, levitation, or other safety-critical hardware. Such interfaces require explicit command allowlists, independent interlocks, simulation/HIL validation, and independent safety engineering.
