from dataclasses import dataclass

from .outcome import Outcome


@dataclass(frozen=True)
class LearningEvent:

    context: str
    outcome: Outcome