from dataclasses import dataclass

from kernel.healthcare.patients.patient_status import PatientStatus


@dataclass(frozen=True, slots=True)
class PatientSnapshot:

    patient_id: str
    status: PatientStatus