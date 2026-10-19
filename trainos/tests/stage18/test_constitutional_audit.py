from kernel.constitution.audit.audit_entry import ConstitutionalAuditEntry
from kernel.constitution.audit.audit_engine import AuditEngine
from kernel.constitution.audit.audit_runtime import AuditRuntime
from kernel.constitution.audit.constitutional_audit import ConstitutionalAudit


def test_constitutional_audit():

    entry = ConstitutionalAuditEntry(
        version="2.1",
        proposal_id="A-001",
        authority="Constitutional Council",
        reason="Emergency governance update",
    )

    assert entry.version == "2.1"
    assert entry.proposal_id == "A-001"
    assert ConstitutionalAudit is ConstitutionalAuditEntry
    assert AuditEngine().record(entry) is entry
    assert AuditRuntime().update(entry) is entry
