# TrainOS — Stage 40: executable command-handler contract

Date: 2026-10-19  
Baseline: `trainos_stage39_audited.zip`  
Status: implemented and verified in the local project archive.

## Goal

Remove the false-success behavior from the command handler execution path. A handler invocation must either call real executable logic and return its output, or return an explicit failure with diagnostic information.

## Changes

- `trainos/kernel/command/handler/command_handler.py`
  - Added an optional `executor` callback accepting a `Command`.
  - Added descriptor validation for handler ID, name, status and callback.
  - Kept existing positional construction (`CommandHandler(handler_id, name, status)`) compatible.
  - Documented that a handler without an executor is metadata only.
- `trainos/kernel/command/handler/handler_engine.py`
  - Calls the executor when configured.
  - Returns successful results only after the callback returns normally.
  - Returns explicit failure when no executor exists.
  - Converts ordinary callback exceptions to diagnostic failure results; does not catch `BaseException`.
  - Validates argument types.
- `trainos/kernel/command/handler/handler_result.py`
  - Added `output` and `error` fields while preserving `success` and `command_id`.
  - Enforces consistent success/failure result invariants.
- `trainos/tests/stage38/test_policies_handler_and_routing.py`
  - Updated the regression expectation: an executable handler succeeds; metadata-only handler does not.
- `trainos/tests/stage40/test_handler_execution_contract.py`
  - Added focused acceptance tests for actual callback invocation, output propagation, missing executor, exception diagnostics, and invalid inputs.

## Verification

- `PYTHONPATH="$PWD/trainos" python3 -m pytest trainos/tests -q`: **387 passed**.
- `python3 -m compileall -q trainos`: passed.
- Import smoke test for 2,107 kernel Python modules: **0 import errors**.

## Remaining work (not claimed complete)

- `RoutingEngine` still validates an already-selected handler; it does not select one from a registry.
- The command path is not yet an end-to-end pipeline connecting authorization, route selection, handler execution, execution lifecycle, events and retry policy.
- `EventDispatcher` currently propagates subscriber exceptions; failure isolation/observability policy remains to be specified and tested.
- This is generic application command execution, not a safety-certified controller for maglev motion, levitation, traction, brakes or life-support equipment.

## Acceptance result

Stage 40 closes the specific false-success gap in `HandlerEngine`. It does not claim the whole command subsystem or the TrainOS project is complete.
