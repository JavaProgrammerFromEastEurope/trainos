from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutionProgress:

    current_step: 		int
    completed_steps: 	int
    total_steps: 			int