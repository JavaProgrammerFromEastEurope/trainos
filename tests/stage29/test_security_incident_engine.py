from kernel.security.incidents.security_incident import SecurityIncident
from kernel.security.incidents.security_incident_engine import SecurityIncidentEngine
from kernel.security.incidents.security_incident_status import SecurityIncidentStatus
from kernel.security.incidents.security_incident_type import SecurityIncidentType


def test_security_incident_engine():

    engine = SecurityIncidentEngine()
    incident = SecurityIncident(
        incident_id="I1",
        title="Unauthorized Access",
        incident_type=SecurityIncidentType.UNAUTHORIZED_ACCESS,
        status=SecurityIncidentStatus.REPORTED,
    )
    active = engine.begin(incident)
    assert active.status == SecurityIncidentStatus.IN_PROGRESS

    resolved = engine.resolve(active)
    assert resolved.status == SecurityIncidentStatus.RESOLVED
