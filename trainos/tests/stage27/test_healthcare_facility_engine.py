from kernel.healthcare.facilities.healthcare_facility import HealthcareFacility
from kernel.healthcare.facilities.healthcare_facility_engine import HealthcareFacilityEngine
from kernel.healthcare.facilities.healthcare_facility_status import HealthcareFacilityStatus
from kernel.healthcare.facilities.healthcare_facility_type import HealthcareFacilityType


def test_healthcare_facility_engine():

    engine = HealthcareFacilityEngine()

    facility = HealthcareFacility(
        facility_id="HOSP1",
        name="Central Hospital",
        facility_type=HealthcareFacilityType.HOSPITAL,
        status=HealthcareFacilityStatus.CLOSED,
    )

    opened = engine.open(facility)
    assert opened.status == HealthcareFacilityStatus.OPERATIONAL

    closed = engine.close(opened)
    assert closed.status == HealthcareFacilityStatus.CLOSED