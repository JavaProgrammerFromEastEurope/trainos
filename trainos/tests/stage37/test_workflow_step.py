from kernel.workflow.step.workflow_step import WorkflowStep

from kernel.workflow.step.step_type 	import StepType
from kernel.workflow.step.step_status import StepStatus


def test_workflow_step():

    step = WorkflowStep(
        step_id="STEP-001",
        name="Create Citizen",
        step_type=StepType.ACTION,
    )

    assert step.step_id == "STEP-001"
    assert step.name == "Create Citizen"
    assert step.step_type == StepType.ACTION
    assert step.status == StepStatus.CREATED
