from kernel.society.audit.civil_audit_entry import CivilAuditEntry
from kernel.society.audit.civil_audit_registry import CivilAuditRegistry


def test_register_audit_entry():

    registry = CivilAuditRegistry()

    entry = CivilAuditEntry(
        entity_id="A-104",
        action="joined_group",
        actor="system",
        reason="Volunteer registration",
    )

    registry.register(entry)
    entries = registry.entries()

    assert len(entries) == 1
    assert entries[0] == entry
