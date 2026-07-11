from .healthcare_facility import HealthcareFacility
from .healthcare_facility_status import HealthcareFacilityStatus


class HealthcareFacilityEngine:

    def open(
        self,
        facility: HealthcareFacility,
    ) -> HealthcareFacility:
        return HealthcareFacility(
            facility_id=facility.facility_id,
            name=facility.name,
            facility_type=facility.facility_type,
            status=HealthcareFacilityStatus.OPERATIONAL,
        )

    def close(
        self,
        facility: HealthcareFacility,
    ) -> HealthcareFacility:
        return HealthcareFacility(
            facility_id=facility.facility_id,
            name=facility.name,
            facility_type=facility.facility_type,
            status=HealthcareFacilityStatus.CLOSED,
        )
