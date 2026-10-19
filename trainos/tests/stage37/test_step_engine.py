from kernel.workflow.step.workflow_step import WorkflowStep

from kernel.workflow.step.step_engine import StepEngine
from kernel.workflow.step.step_type 	import StepType
from kernel.workflow.step.step_status import StepStatus


def test_step_engine():

    step = WorkflowStep(
        step_id="STEP-002",
        name="Register Insurance",
        step_type=StepType.ACTION,
    )
    engine = StepEngine()
    step = engine.start(step)
    assert step.status == StepStatus.RUNNING

    step = engine.complete(step)
    assert step.status == StepStatus.COMPLETED
