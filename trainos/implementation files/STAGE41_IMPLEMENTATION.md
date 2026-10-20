# TrainOS — Stage 41: registry-based command routing

Date: 2026-10-19  
Baseline: `trainos_stage40.zip`  
Status: implemented and verified in the local project archive.

## Goal

Resolve a command to a registered executable handler using existing TrainOS registries, with deterministic failure results for missing, ambiguous, or non-executable handlers.

## Changes

- `kernel/command/bus/routing_engine.py`
  - Added `route_command(command, registry)` to resolve by exact command/handler name, the only routing key represented by the current `Command` model.
  - Missing and ambiguous matches fail closed with diagnostics.
  - Metadata-only handlers are not accepted as executable routing targets.
  - Preserved `route(handler)` and added `route(command, registry)` convenience routing.
  - Added input type validation.
- `kernel/command/bus/routing_result.py`
  - Added optional `command_id` and diagnostic `error` fields while preserving the original first two constructor fields.
  - Validates successful and failed result invariants.
- `tests/stage41/test_handler_registry_routing.py`
  - Covers unique match, convenience API, missing match, ambiguous match, metadata-only handler, and invalid inputs.

## Design note

The current `Command` type does not define a handler key or command type. Exact `command.name == handler.name` matching is therefore a conservative interim contract, not a claim that names are an ideal long-term routing key. A future explicit immutable `handler_key`/`command_type` should be introduced only after auditing all command construction sites and compatibility requirements.

## Safety boundary

This is generic software command routing. It does not directly actuate train movement, levitation, traction, brakes, or life-support equipment and is not safety-certified.

## Verification

- `PYTHONPATH="$PWD" python3 -m pytest tests -q`: **393 passed**.
- `python3 -m compileall -q kernel tests`: passed.
- AST parse of all Python files under `kernel`: passed with 0 syntax errors.
