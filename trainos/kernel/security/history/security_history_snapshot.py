from dataclasses import dataclass

from kernel.security.incidents.security_incident_status import (
    SecurityIncidentStatus,
)


@dataclass(frozen=True, slots=True)
class SecurityHistorySnapshot:

    snapshot_id: str
    incident_id: str
    status: SecurityIncidentStatus