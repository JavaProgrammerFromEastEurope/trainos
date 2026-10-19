from kernel.workflow.execution.workflow_execution import WorkflowExecution

from kernel.workflow.execution.execution_progress import ExecutionProgress
from kernel.workflow.execution.execution_engine 	import ExecutionEngine
from kernel.workflow.execution.execution_status 	import ExecutionStatus


def test_workflow_execution():

    execution = WorkflowExecution(
        execution_id="EXEC-001",
        workflow_id="WF-006",
        progress=ExecutionProgress(
            current_step=1,
            completed_steps=0,
            total_steps=5,
        ),
    )
    engine = ExecutionEngine()
    execution = engine.start(execution)
    assert execution.status == ExecutionStatus.RUNNING

    execution = engine.complete(execution)
    assert execution.status == ExecutionStatus.COMPLETED
