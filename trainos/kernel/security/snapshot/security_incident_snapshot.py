from dataclasses import dataclass

from kernel.security.incidents.security_incident_status import (
    SecurityIncidentStatus,
)


@dataclass(frozen=True, slots=True)
class SecurityIncidentSnapshot:

    incident_id: str
    status: SecurityIncidentStatus