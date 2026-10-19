from dataclasses import dataclass

from .htn_task import HTNTask


@dataclass
class HTNPlan:

    tasks: list[HTNTask]
