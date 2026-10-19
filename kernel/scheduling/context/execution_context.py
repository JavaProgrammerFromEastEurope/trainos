from dataclasses import dataclass

from .execution_metadata import ExecutionMetadata
from .execution_state import ExecutionState


@dataclass(frozen=True, slots=True)
class ExecutionContext:

    task_id: str
    metadata: ExecutionMetadata
    state: ExecutionState = ExecutionState.CREATED