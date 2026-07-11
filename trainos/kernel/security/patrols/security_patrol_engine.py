from .security_patrol import SecurityPatrol
from .security_patrol_status import SecurityPatrolStatus


class SecurityPatrolEngine:

    def activate(
        self,
        patrol: SecurityPatrol,
    ) -> SecurityPatrol:
        return SecurityPatrol(
            patrol_id=patrol.patrol_id,
            officer_id=patrol.officer_id,
            patrol_type=patrol.patrol_type,
            status=SecurityPatrolStatus.ACTIVE,
        )

    def complete(
        self,
        patrol: SecurityPatrol,
    ) -> SecurityPatrol:
        return SecurityPatrol(
            patrol_id=patrol.patrol_id,
            officer_id=patrol.officer_id,
            patrol_type=patrol.patrol_type,
            status=SecurityPatrolStatus.COMPLETED,
        )
