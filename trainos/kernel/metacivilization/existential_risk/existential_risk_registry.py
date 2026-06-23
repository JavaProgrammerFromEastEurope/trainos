from __future__ import annotations

from .existential_risk import ExistentialRisk


class ExistentialRiskRegistry:

    def __init__(self) -> None:
        self._risks: list[ExistentialRisk] = []

    def add(self, risk: ExistentialRisk) -> None:
        self._risks.append(risk)

    def risks(self) -> tuple[ExistentialRisk, ...]:
        return tuple(self._risks)
