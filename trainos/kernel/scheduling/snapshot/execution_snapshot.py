from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutionSnapshot:

    completed_tasks: int