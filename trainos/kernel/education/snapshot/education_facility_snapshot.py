from dataclasses import dataclass

from kernel.education.facilities.education_facility_status import (
    EducationFacilityStatus,
)


@dataclass(frozen=True, slots=True)
class EducationFacilitySnapshot:

    facility_id: str
    status: EducationFacilityStatus