from dataclasses import dataclass

from kernel.healthcare.patients.patient_status import PatientStatus


@dataclass(frozen=True, slots=True)
class HealthcareHistorySnapshot:

    snapshot_id: 	str
    patient_id: 	str
    status: PatientStatus