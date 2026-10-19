from kernel.healthcare.treatments.treatment import Treatment
from kernel.healthcare.treatments.treatment_engine import TreatmentEngine
from kernel.healthcare.treatments.treatment_status import TreatmentStatus
from kernel.healthcare.treatments.treatment_type import TreatmentType


def test_treatment_engine():

    engine = TreatmentEngine()

    treatment = Treatment(
        treatment_id="T1",
        condition_id="C1",
        name="Surgery",
        treatment_type=TreatmentType.SURGERY,
        status=TreatmentStatus.PLANNED,
    )

    active = engine.start(treatment)
    assert active.status == TreatmentStatus.ACTIVE
    completed = engine.complete(active)
    assert completed.status == TreatmentStatus.COMPLETED