from dataclasses import dataclass

from .medical_condition_status import MedicalConditionStatus
from .medical_condition_type import MedicalConditionType


@dataclass(frozen=True, slots=True)
class MedicalCondition:

    condition_id: str
    patient_id: 	str
    name: 				str
    condition_type: MedicalConditionType
    status: MedicalConditionStatus