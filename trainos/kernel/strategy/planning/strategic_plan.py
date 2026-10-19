from dataclasses import dataclass

from .plan_step import PlanStep


@dataclass(frozen=True)
class StrategicPlan:

    name: 				str
    description: 	str
    steps: tuple[PlanStep, ...]