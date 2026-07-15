from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WorkflowMetadata:

    runtime_id: 	str
    scheduler_id: str
    tick: 				int
    correlation_id: str