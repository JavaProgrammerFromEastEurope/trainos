from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutionResult:

    success: 			bool
    workflow_id: 	str