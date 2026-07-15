from dataclasses import dataclass

from .workflow_priority import WorkflowPriority
from .workflow_status import WorkflowStatus


@dataclass(frozen=True, slots=True)
class Workflow:

    workflow_id: 	str
    name: 				str
    priority: WorkflowPriority
    status: WorkflowStatus = WorkflowStatus.CREATED