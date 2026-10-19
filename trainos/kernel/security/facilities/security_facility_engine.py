from .security_facility import SecurityFacility
from .security_facility_status import SecurityFacilityStatus


class SecurityFacilityEngine:

    def open(
        self,
        facility: SecurityFacility,
    ) -> SecurityFacility:
        return SecurityFacility(
            facility_id=facility.facility_id,
            name=facility.name,
            facility_type=facility.facility_type,
            status=SecurityFacilityStatus.OPERATIONAL,
        )

    def close(
        self,
        facility: SecurityFacility,
    ) -> SecurityFacility:
        return SecurityFacility(
            facility_id=facility.facility_id,
            name=facility.name,
            facility_type=facility.facility_type,
            status=SecurityFacilityStatus.CLOSED,
        )
