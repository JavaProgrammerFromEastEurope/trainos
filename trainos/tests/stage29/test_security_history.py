from kernel.security.history.security_history_engine import SecurityHistoryEngine
from kernel.security.history.security_history_entry import SecurityHistoryEntry
from kernel.security.history.security_history_snapshot import SecurityHistorySnapshot
from kernel.security.incidents.security_incident_status import SecurityIncidentStatus


def test_security_history():

    engine = SecurityHistoryEngine()
    snapshot = SecurityHistorySnapshot(
        snapshot_id="HS1",
        incident_id="I1",
        status=SecurityIncidentStatus.IN_PROGRESS,
    )
    entry = SecurityHistoryEntry(
        entry_id="HE1",
        timestamp="2026-01-01T00:00:00Z",
        snapshot=snapshot,
    )

    result = engine.record(entry)
    assert result is entry
