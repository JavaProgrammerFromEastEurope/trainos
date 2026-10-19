from dataclasses import dataclass

from kernel.security.facilities.security_facility_status import (
    SecurityFacilityStatus,
)


@dataclass(frozen=True, slots=True)
class SecurityFacilitySnapshot:

    facility_id: str
    status: SecurityFacilityStatus