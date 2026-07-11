from dataclasses import dataclass

from .security_incident_status 	import SecurityIncidentStatus
from .security_incident_type 		import SecurityIncidentType


@dataclass(frozen=True, slots=True)
class SecurityIncident:

    incident_id: str
    title: str
    incident_type: SecurityIncidentType
    status: SecurityIncidentStatus