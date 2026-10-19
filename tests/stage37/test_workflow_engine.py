from kernel.workflow.workflow.workflow import Workflow

from kernel.workflow.workflow.workflow_engine 	import WorkflowEngine
from kernel.workflow.workflow.workflow_priority import WorkflowPriority
from kernel.workflow.workflow.workflow_status 	import WorkflowStatus


def test_workflow_engine():

    workflow = Workflow(
        workflow_id="WF-002",
        name="Healthcare",
        priority=WorkflowPriority.HIGH,
    )
    engine = WorkflowEngine()
    workflow = engine.start(workflow)
    assert workflow.status == WorkflowStatus.RUNNING

    workflow = engine.complete(workflow)
    assert workflow.status == WorkflowStatus.COMPLETED
