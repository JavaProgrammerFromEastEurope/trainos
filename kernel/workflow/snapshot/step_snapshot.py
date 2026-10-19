from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StepSnapshot:

    step_id: 	str
    status: 	str