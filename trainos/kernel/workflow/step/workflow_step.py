from dataclasses import dataclass

from .step_status import StepStatus
from .step_type import StepType


@dataclass(frozen=True, slots=True)
class WorkflowStep:

    step_id: 	str
    name: 		str
    step_type: StepType
    status: StepStatus = StepStatus.CREATED