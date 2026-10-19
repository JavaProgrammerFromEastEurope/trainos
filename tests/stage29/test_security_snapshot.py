from kernel.security.snapshot.security_snapshot import SecuritySnapshot
from kernel.security.snapshot.security_snapshot_engine import SecuritySnapshotEngine
from kernel.security.snapshot.security_runtime_snapshot import SecurityRuntimeSnapshot
from kernel.security.snapshot.security_officer_snapshot import SecurityOfficerSnapshot
from kernel.security.snapshot.security_incident_snapshot import SecurityIncidentSnapshot
from kernel.security.snapshot.security_patrol_snapshot import SecurityPatrolSnapshot
from kernel.security.snapshot.security_facility_snapshot import SecurityFacilitySnapshot

from kernel.security.runtime.security_lifecycle import SecurityLifecycle
from kernel.security.officers.security_officer_status import SecurityOfficerStatus
from kernel.security.incidents.security_incident_status import SecurityIncidentStatus
from kernel.security.patrols.security_patrol_status import SecurityPatrolStatus
from kernel.security.facilities.security_facility_status import SecurityFacilityStatus


def test_security_snapshot():

    engine = SecuritySnapshotEngine()

    snapshot = SecuritySnapshot(
        snapshot_id="SNAP1",
        runtime=SecurityRuntimeSnapshot(
            lifecycle=SecurityLifecycle.RUNNING,
        ),
        officers=(
            SecurityOfficerSnapshot(
                officer_id="O1",
                status=SecurityOfficerStatus.ON_DUTY,
            ),
        ),
        incidents=(
            SecurityIncidentSnapshot(
                incident_id="I1",
                status=SecurityIncidentStatus.IN_PROGRESS,
            ),
        ),
        patrols=(
            SecurityPatrolSnapshot(
                patrol_id="P1",
                status=SecurityPatrolStatus.ACTIVE,
            ),
        ),
        facilities=(
            SecurityFacilitySnapshot(
                facility_id="F1",
                status=SecurityFacilityStatus.OPERATIONAL,
            ),
        ),
    )
    result = engine.capture(snapshot)

    assert result is snapshot
