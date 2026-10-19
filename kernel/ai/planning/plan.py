from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
from .plan_step import PlanStep


@dataclass
class Plan:

    steps: List[PlanStep] = field(default_factory=list)

    def add(self, step: PlanStep) -> None:
        self.steps.append(step)
