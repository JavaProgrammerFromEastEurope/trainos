from trainos.kernel.constitution.audit.audit_entry import ConstitutionalAuditEntry


def test_constitutional_audit():

    entry = ConstitutionalAuditEntry(
        version="2.1",
        proposal_id="A-001",
        authority="Constitutional Council",
        reason="Emergency governance update",
    )

    assert entry.version == "2.1"
    assert entry.proposal_id == "A-001"
