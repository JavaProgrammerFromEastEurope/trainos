from dataclasses import dataclass

from .execution_status import ExecutionStatus
from .execution_progress import ExecutionProgress


@dataclass(frozen=True, slots=True)
class WorkflowExecution:

    execution_id: 	str
    workflow_id: 		str
    progress: ExecutionProgress
    status: ExecutionStatus = ExecutionStatus.CREATED