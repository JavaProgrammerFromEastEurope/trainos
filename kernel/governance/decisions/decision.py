from dataclasses import dataclass

from .decision_status import DecisionStatus
from .decision_type import DecisionType


@dataclass(frozen=True, slots=True)
class Decision:

    decision_id: 	str
    authority_id: str
    title: str
    decision_type: DecisionType
    status: DecisionStatus