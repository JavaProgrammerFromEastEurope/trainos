from kernel.institution.audit.institution_audit_entry import InstitutionAuditEntry
from kernel.institution.audit.institution_audit_registry import InstitutionAuditRegistry


def test_register_audit_entry():

    registry = InstitutionAuditRegistry()

    entry = InstitutionAuditEntry(
        institution_id="EO-001",
        action="delegation_created",
        actor="CC-001",
        reason="Emergency",
    )

    registry.register(entry)
    entries = registry.entries()

    assert len(entries) == 1
    assert entries[0] == entry
