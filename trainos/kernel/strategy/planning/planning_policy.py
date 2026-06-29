from dataclasses import dataclass


@dataclass(frozen=True)
class PlanningPolicy:

    allow_empty_plan: bool
