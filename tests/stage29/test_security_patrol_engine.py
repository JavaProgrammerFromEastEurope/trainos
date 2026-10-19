from kernel.security.patrols.security_patrol import SecurityPatrol
from kernel.security.patrols.security_patrol_engine import SecurityPatrolEngine
from kernel.security.patrols.security_patrol_status import SecurityPatrolStatus
from kernel.security.patrols.security_patrol_type 	import SecurityPatrolType


def test_security_patrol_engine():

    engine = SecurityPatrolEngine()
    patrol = SecurityPatrol(
        patrol_id="P1",
        officer_id="O1",
        patrol_type=SecurityPatrolType.ROUTINE,
        status=SecurityPatrolStatus.PLANNED,
    )

    active = engine.activate(patrol)
    assert active.status == SecurityPatrolStatus.ACTIVE

    completed = engine.complete(active)
    assert completed.status == SecurityPatrolStatus.COMPLETED
