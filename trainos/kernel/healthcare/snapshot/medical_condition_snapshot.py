from dataclasses import dataclass

from kernel.healthcare.conditions.medical_condition_status import MedicalConditionStatus


@dataclass(frozen=True, slots=True)
class MedicalConditionSnapshot:

    condition_id: str
    status: MedicalConditionStatus