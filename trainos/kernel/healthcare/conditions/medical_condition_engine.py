from .medical_condition import MedicalCondition
from .medical_condition_status import MedicalConditionStatus


class MedicalConditionEngine:

    def improve(
        self,
        condition: MedicalCondition,
    ) -> MedicalCondition:
        return MedicalCondition(
            condition_id=condition.condition_id,
            patient_id=condition.patient_id,
            name=condition.name,
            condition_type=condition.condition_type,
            status=MedicalConditionStatus.IMPROVING,
        )

    def resolve(
        self,
        condition: MedicalCondition,
    ) -> MedicalCondition:
        return MedicalCondition(
            condition_id=condition.condition_id,
            patient_id=condition.patient_id,
            name=condition.name,
            condition_type=condition.condition_type,
            status=MedicalConditionStatus.RESOLVED,
        )
