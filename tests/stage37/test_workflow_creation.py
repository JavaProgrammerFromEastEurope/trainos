from kernel.workflow.workflow.workflow import Workflow

from kernel.workflow.workflow.workflow_priority import WorkflowPriority
from kernel.workflow.workflow.workflow_status import WorkflowStatus


def test_workflow_creation():

    workflow = Workflow(
        workflow_id="WF-001",
        name="Citizen Registration",
        priority=WorkflowPriority.NORMAL,
    )

    assert workflow.workflow_id == "WF-001"
    assert workflow.name == "Citizen Registration"
    assert workflow.priority == WorkflowPriority.NORMAL
    assert workflow.status == WorkflowStatus.CREATED
