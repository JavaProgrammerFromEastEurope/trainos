from dataclasses import dataclass

from .patient_status import PatientStatus


@dataclass(frozen=True, slots=True)
class Patient:

    patient_id: 	str
    resident_id: 	str
    status: PatientStatus