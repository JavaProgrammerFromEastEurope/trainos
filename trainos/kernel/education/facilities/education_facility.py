from dataclasses import dataclass

from .education_facility_status import EducationFacilityStatus
from .education_facility_type import EducationFacilityType


@dataclass(frozen=True, slots=True)
class EducationFacility:

    facility_id: 	str
    name: 				str
    facility_type: EducationFacilityType
    status: EducationFacilityStatus