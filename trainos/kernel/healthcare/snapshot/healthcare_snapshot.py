from dataclasses import dataclass

from .healthcare_facility_snapshot import HealthcareFacilitySnapshot
from .healthcare_runtime_snapshot import HealthcareRuntimeSnapshot
from .medical_condition_snapshot import MedicalConditionSnapshot
from .patient_snapshot import PatientSnapshot
from .treatment_snapshot import TreatmentSnapshot


@dataclass(frozen=True, slots=True)
class HealthcareSnapshot:

    snapshot_id: str
    runtime: HealthcareRuntimeSnapshot
    patients: 	tuple[PatientSnapshot, ...]
    conditions: tuple[MedicalConditionSnapshot, ...]
    treatments: tuple[TreatmentSnapshot, ...]
    facilities: tuple[HealthcareFacilitySnapshot, ...]