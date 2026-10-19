from dataclasses import dataclass

from .planning_horizon import PlanningHorizon


@dataclass
class LongTermPlan:

    horizon: PlanningHorizon
