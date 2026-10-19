from dataclasses import dataclass


@dataclass(frozen=True)
class PlanStep:

    name: 				str
    description: 	str