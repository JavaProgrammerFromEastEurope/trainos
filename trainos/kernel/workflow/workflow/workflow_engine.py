from .workflow import Workflow
from .workflow_status import WorkflowStatus


class WorkflowEngine:

    def start(
        self,
        workflow: Workflow,
    ) -> Workflow:
        return Workflow(
            workflow_id=workflow.workflow_id,
            name=workflow.name,
            priority=workflow.priority,
            status=WorkflowStatus.RUNNING,
        )

    def complete(
        self,
        workflow: Workflow,
    ) -> Workflow:
        return Workflow(
            workflow_id=workflow.workflow_id,
            name=workflow.name,
            priority=workflow.priority,
            status=WorkflowStatus.COMPLETED,
        )
