from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutionResult:

    success: bool
    task_id: str