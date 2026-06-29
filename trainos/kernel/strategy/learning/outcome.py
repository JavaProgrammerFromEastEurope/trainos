from dataclasses import dataclass

from .outcome_type import OutcomeType


@dataclass(frozen=True)
class Outcome:

    description: str
    type: OutcomeType