from kernel.healthcare.facilities.healthcare_facility_status import HealthcareFacilityStatus
from kernel.healthcare.patients.patient_status import PatientStatus
from kernel.healthcare.conditions.medical_condition_status import MedicalConditionStatus
from kernel.healthcare.runtime.healthcare_lifecycle import HealthcareLifecycle
from kernel.healthcare.snapshot.healthcare_facility_snapshot import HealthcareFacilitySnapshot
from kernel.healthcare.snapshot.healthcare_runtime_snapshot import HealthcareRuntimeSnapshot
from kernel.healthcare.snapshot.healthcare_snapshot import HealthcareSnapshot
from kernel.healthcare.snapshot.healthcare_snapshot_engine import HealthcareSnapshotEngine
from kernel.healthcare.snapshot.medical_condition_snapshot import MedicalConditionSnapshot
from kernel.healthcare.snapshot.patient_snapshot 		import PatientSnapshot
from kernel.healthcare.snapshot.treatment_snapshot 	import TreatmentSnapshot
from kernel.healthcare.treatments.treatment_status 	import TreatmentStatus


def test_healthcare_snapshot():

    engine = HealthcareSnapshotEngine()
    snapshot = HealthcareSnapshot(
        snapshot_id="SNAP1",
        runtime=HealthcareRuntimeSnapshot(
            lifecycle=HealthcareLifecycle.RUNNING,
        ),
        patients=(
            PatientSnapshot(
                patient_id="P1",
                status=PatientStatus.IN_TREATMENT,
            ),
        ),
        conditions=(
            MedicalConditionSnapshot(
                condition_id="C1",
                status=MedicalConditionStatus.ACTIVE,
            ),
        ),
        treatments=(
            TreatmentSnapshot(
                treatment_id="T1",
                status=TreatmentStatus.ACTIVE,
            ),
        ),
        facilities=(
            HealthcareFacilitySnapshot(
                facility_id="H1",
                status=HealthcareFacilityStatus.OPERATIONAL,
            ),
        ),
    )
    result = engine.capture(snapshot)
    assert result is snapshot