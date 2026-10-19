from dataclasses import dataclass

from .value_score import ValueScore


@dataclass(frozen=True)
class ValueAssessment:

    outcome: 	str
    scores: tuple[ValueScore, ...]