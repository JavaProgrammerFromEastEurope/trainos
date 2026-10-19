from dataclasses import dataclass

from .value_dimension import ValueDimension


@dataclass(frozen=True)
class ValueScore:

    dimension: ValueDimension
    score: float