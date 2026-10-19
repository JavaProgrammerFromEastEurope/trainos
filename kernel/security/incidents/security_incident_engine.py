from .security_incident import SecurityIncident
from .security_incident_status import SecurityIncidentStatus


class SecurityIncidentEngine:

    def begin(
        self,
        incident: SecurityIncident,
    ) -> SecurityIncident:
        return SecurityIncident(
            incident_id=incident.incident_id,
            title=incident.title,
            incident_type=incident.incident_type,
            status=SecurityIncidentStatus.IN_PROGRESS,
        )

    def resolve(
        self,
        incident: SecurityIncident,
    ) -> SecurityIncident:
        return SecurityIncident(
            incident_id=incident.incident_id,
            title=incident.title,
            incident_type=incident.incident_type,
            status=SecurityIncidentStatus.RESOLVED,
        )
