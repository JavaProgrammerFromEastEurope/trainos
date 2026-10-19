from kernel.security.officers.security_officer import SecurityOfficer
from kernel.security.officers.security_officer_engine import SecurityOfficerEngine
from kernel.security.officers.security_officer_status import SecurityOfficerStatus


def test_security_officer_engine():

    engine = SecurityOfficerEngine()
    officer = SecurityOfficer(
        officer_id="O1",
        resident_id="R1",
        status=SecurityOfficerStatus.AVAILABLE,
    )
    responding = engine.dispatch(officer)
    assert responding.status == SecurityOfficerStatus.RESPONDING
    returned = engine.return_to_duty(responding)
    assert returned.status == SecurityOfficerStatus.ON_DUTY
