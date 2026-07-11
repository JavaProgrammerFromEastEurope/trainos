from dataclasses import dataclass

from .security_officer_status import SecurityOfficerStatus


@dataclass(frozen=True, slots=True)
class SecurityOfficer:

    officer_id: 	str
    resident_id: 	str
    status: SecurityOfficerStatus