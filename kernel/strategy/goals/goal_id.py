from dataclasses import dataclass


@dataclass(frozen=True)
class GoalId:

    value: str
