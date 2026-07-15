from kernel.workflow.snapshot.workflow_snapshot import WorkflowSnapshot

from kernel.workflow.snapshot.execution_snapshot 	import ExecutionSnapshot
from kernel.workflow.snapshot.step_snapshot 			import StepSnapshot
from kernel.workflow.snapshot.snapshot_engine 		import SnapshotEngine


def test_workflow_snapshot():

    snapshot = WorkflowSnapshot(
        snapshot_id="SNAP-001",
        workflow_id="WF-009",
        execution=ExecutionSnapshot(
            execution_id="EXEC-009",
            current_step=2,
            completed_steps=1,
        ),
        steps=(
            StepSnapshot(
                step_id="STEP-1",
                status="DONE",
            ),
        ),
    )
    result = SnapshotEngine().capture(snapshot)
    assert result.workflow_id == "WF-009"
    assert result.execution.current_step == 2
    assert len(result.steps) == 1
