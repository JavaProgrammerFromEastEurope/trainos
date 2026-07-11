from kernel.security.facilities.security_facility import SecurityFacility
from kernel.security.facilities.security_facility_engine 	import SecurityFacilityEngine
from kernel.security.facilities.security_facility_status 	import SecurityFacilityStatus
from kernel.security.facilities.security_facility_type 		import SecurityFacilityType


def test_security_facility_engine():

    engine = SecurityFacilityEngine()
    facility = SecurityFacility(
        facility_id="F1",
        name="Security Control Center",
        facility_type=SecurityFacilityType.CONTROL_CENTER,
        status=SecurityFacilityStatus.CLOSED,
    )

    opened = engine.open(facility)
    assert opened.status == SecurityFacilityStatus.OPERATIONAL

    closed = engine.close(opened)
    assert closed.status == SecurityFacilityStatus.CLOSED
