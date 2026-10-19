from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutionSnapshot:

    execution_id: 		str
    current_step: 		int
    completed_steps: 	int