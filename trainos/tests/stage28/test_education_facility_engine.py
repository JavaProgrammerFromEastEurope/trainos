from kernel.education.facilities.education_facility import EducationFacility
from kernel.education.facilities.education_facility_engine import EducationFacilityEngine
from kernel.education.facilities.education_facility_status import EducationFacilityStatus
from kernel.education.facilities.education_facility_type import EducationFacilityType


def test_education_facility_engine():

    engine = EducationFacilityEngine()
    facility = EducationFacility(
        facility_id="F1",
        name="Academy",
        facility_type=EducationFacilityType.ACADEMY,
        status=EducationFacilityStatus.CLOSED,
    )

    opened = engine.open(facility)
    assert opened.status == EducationFacilityStatus.OPERATIONAL

    closed = engine.close(opened)
    assert closed.status == EducationFacilityStatus.CLOSED