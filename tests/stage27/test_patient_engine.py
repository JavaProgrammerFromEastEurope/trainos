from kernel.healthcare.patients.patient import Patient
from kernel.healthcare.patients.patient_engine import PatientEngine
from kernel.healthcare.patients.patient_status import PatientStatus


def test_patient_engine():

    engine = PatientEngine()

    patient = Patient(
        patient_id="P1",
        resident_id="R1",
        status=PatientStatus.HEALTHY,
    )

    admitted = engine.admit(patient)
    assert admitted.status == PatientStatus.UNDER_OBSERVATION
    treated = engine.begin_treatment(admitted)
    assert treated.status == PatientStatus.IN_TREATMENT
    recovered = engine.recover(treated)
    assert recovered.status == PatientStatus.RECOVERED