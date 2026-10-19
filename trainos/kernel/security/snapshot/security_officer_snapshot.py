from dataclasses import dataclass

from kernel.security.officers.security_officer_status import (
    SecurityOfficerStatus,
)


@dataclass(frozen=True, slots=True)
class SecurityOfficerSnapshot:

    officer_id: str
    status: SecurityOfficerStatus