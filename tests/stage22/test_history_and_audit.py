from kernel.resources.audit.resource_audit_engine import ResourceAuditEngine
from kernel.resources.audit.resource_audit_entry import ResourceAuditEntry

from kernel.resources.history.resource_history_engine import ResourceHistoryEngine
from kernel.resources.history.resource_history_entry import ResourceHistoryEntry
from kernel.resources.history.resource_snapshot import ResourceSnapshot


def test_history_and_audit():

    snapshot = ResourceSnapshot(
        snapshot_id="S1",
        resource_id="water",
        quantity=100,
    )

    history = ResourceHistoryEntry(
        entry_id="H1",
        timestamp="2026-01-01T00:00:00Z",
        snapshot=snapshot,
    )

    history_engine = ResourceHistoryEngine()
    result = history_engine.record(history)

    assert result is history

    audit = ResourceAuditEntry(
        audit_id="A1",
        actor_id="government",
        action="allocate",
        resource_id="water",
        reason="daily ration",
    )

    audit_engine = ResourceAuditEngine()
    audit_result = audit_engine.record(audit)

    assert audit_result is audit