from dataclasses import dataclass

from kernel.security.patrols.security_patrol_status import (
    SecurityPatrolStatus,
)


@dataclass(frozen=True, slots=True)
class SecurityPatrolSnapshot:

    patrol_id: str
    status: SecurityPatrolStatus