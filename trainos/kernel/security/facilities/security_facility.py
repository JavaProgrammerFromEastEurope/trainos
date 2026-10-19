from dataclasses import dataclass

from .security_facility_status import SecurityFacilityStatus
from .security_facility_type import SecurityFacilityType


@dataclass(frozen=True, slots=True)
class SecurityFacility:

    facility_id: 	str
    name: 				str
    facility_type: SecurityFacilityType
    status: SecurityFacilityStatus