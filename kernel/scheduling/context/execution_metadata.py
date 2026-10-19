from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutionMetadata:

    scheduler_id: str
    runtime_id: 	str
    tick: 				int