from .patient import Patient
from .patient_status import PatientStatus


class PatientEngine:

    def admit(
        self,
        patient: Patient,
    ) -> Patient:
        return Patient(
            patient_id	=	patient.patient_id,
            resident_id	=	patient.resident_id,
            status=PatientStatus.UNDER_OBSERVATION,
        )

    def begin_treatment(
        self,
        patient: Patient,
    ) -> Patient:
        return Patient(
            patient_id	=	patient.patient_id,
            resident_id	=	patient.resident_id,
            status=PatientStatus.IN_TREATMENT,
        )

    def recover(
        self,
        patient: Patient,
    ) -> Patient:
        return Patient(
            patient_id	=	patient.patient_id,
            resident_id	=	patient.resident_id,
            status=PatientStatus.RECOVERED,
        )
