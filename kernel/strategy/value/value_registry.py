from __future__ import annotations

from .value_assessment import ValueAssessment


class ValueRegistry:

    def __init__(self) -> None:
        self._assessments: list[ValueAssessment] = []

    def register(self, assessment: ValueAssessment) -> None:
        self._assessments.append(assessment)

    def assessments(self) -> tuple[ValueAssessment, ...]:
        return tuple(self._assessments)
