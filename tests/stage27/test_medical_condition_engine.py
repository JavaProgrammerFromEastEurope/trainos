from kernel.healthcare.conditions.medical_condition import MedicalCondition
from kernel.healthcare.conditions.medical_condition_engine import MedicalConditionEngine
from kernel.healthcare.conditions.medical_condition_status import MedicalConditionStatus
from kernel.healthcare.conditions.medical_condition_type import MedicalConditionType


def test_medical_condition_engine():

    engine = MedicalConditionEngine()
    condition = MedicalCondition(
        condition_id="C1",
        patient_id="P1",
        name="Fracture",
        condition_type=MedicalConditionType.INJURY,
        status=MedicalConditionStatus.ACTIVE,
    )

    improving = engine.improve(condition)
    assert improving.status == MedicalConditionStatus.IMPROVING

    resolved = engine.resolve(improving)
    assert resolved.status == MedicalConditionStatus.RESOLVED