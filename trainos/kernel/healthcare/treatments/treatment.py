from dataclasses import dataclass

from .treatment_status import TreatmentStatus
from .treatment_type import TreatmentType


@dataclass(frozen=True, slots=True)
class Treatment:

    treatment_id: str
    condition_id: str
    name: 				str
    treatment_type: TreatmentType
    status: TreatmentStatus