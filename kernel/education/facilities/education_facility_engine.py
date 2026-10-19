from .education_facility import EducationFacility
from .education_facility_status import EducationFacilityStatus


class EducationFacilityEngine:

    def open(
        self,
        facility: EducationFacility,
    ) -> EducationFacility:
        return EducationFacility(
            facility_id=facility.facility_id,
            name=facility.name,
            facility_type=facility.facility_type,
            status=EducationFacilityStatus.OPERATIONAL,
        )

    def close(
        self,
        facility: EducationFacility,
    ) -> EducationFacility:
        return EducationFacility(
            facility_id=facility.facility_id,
            name=facility.name,
            facility_type=facility.facility_type,
            status=EducationFacilityStatus.CLOSED,
        )