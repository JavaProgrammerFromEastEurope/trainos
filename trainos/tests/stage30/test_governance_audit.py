from kernel.governance.audit.governance_audit_engine import (
    GovernanceAuditEngine,
)
from kernel.governance.audit.governance_audit_entry import (
    GovernanceAuditEntry,
)


def test_governance_audit():

    engine = GovernanceAuditEngine()
    entry = GovernanceAuditEntry(
        audit_id="AUD1",
        authority_id="A1",
        decision_id="D1",
        action="approve_decision",
    )

    result = engine.record(entry)
    assert result is entry
