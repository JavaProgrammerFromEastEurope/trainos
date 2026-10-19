from .workflow_step import WorkflowStep
from .step_status 	import StepStatus


class StepEngine:

    def start(
        self,
        step: WorkflowStep,
    ) -> WorkflowStep:
        return WorkflowStep(
            step_id=step.step_id,
            name=step.name,
            step_type=step.step_type,
            status=StepStatus.RUNNING,
        )

    def complete(
        self,
        step: WorkflowStep,
    ) -> WorkflowStep:
        return WorkflowStep(
            step_id=step.step_id,
            name=step.name,
            step_type=step.step_type,
            status=StepStatus.COMPLETED,
        )
