from dataclasses import dataclass

from kernel.healthcare.facilities.healthcare_facility_status import HealthcareFacilityStatus


@dataclass(frozen=True, slots=True)
class HealthcareFacilitySnapshot:

    facility_id: str
    status: HealthcareFacilityStatus