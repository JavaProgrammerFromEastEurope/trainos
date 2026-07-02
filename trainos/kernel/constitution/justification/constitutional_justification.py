from dataclasses import dataclass

from .justification_type import JustificationType


@dataclass(frozen=True)
class ConstitutionalJustification:

    proposal: str
    type: JustificationType
    explanation: str