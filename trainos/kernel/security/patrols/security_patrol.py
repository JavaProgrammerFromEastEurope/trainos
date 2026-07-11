from dataclasses import dataclass

from .security_patrol_status import SecurityPatrolStatus
from .security_patrol_type import SecurityPatrolType


@dataclass(frozen=True, slots=True)
class SecurityPatrol:

    patrol_id: 		str
    officer_id: 	str
    patrol_type: SecurityPatrolType
    status: SecurityPatrolStatus