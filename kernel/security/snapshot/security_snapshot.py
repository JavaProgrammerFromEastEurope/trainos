from dataclasses import dataclass

from .security_facility_snapshot 	import SecurityFacilitySnapshot
from .security_incident_snapshot 	import SecurityIncidentSnapshot
from .security_officer_snapshot 	import SecurityOfficerSnapshot
from .security_patrol_snapshot 		import SecurityPatrolSnapshot
from .security_runtime_snapshot 	import SecurityRuntimeSnapshot


@dataclass(frozen=True, slots=True)
class SecuritySnapshot:

    snapshot_id: 	str
    runtime: 			SecurityRuntimeSnapshot
    officers: 		tuple[SecurityOfficerSnapshot, ...]
    incidents: 		tuple[SecurityIncidentSnapshot, ...]
    patrols: 			tuple[SecurityPatrolSnapshot, ...]
    facilities: 	tuple[SecurityFacilitySnapshot, ...]