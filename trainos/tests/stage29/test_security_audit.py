from kernel.security.audit.security_audit_engine 	import SecurityAuditEngine
from kernel.security.audit.security_audit_entry 	import SecurityAuditEntry


def test_security_audit():

    engine = SecurityAuditEngine()
    entry = SecurityAuditEntry(
        audit_id="AUD1",
        actor_id="O1",
        incident_id="I1",
        action="resolve_incident",
    )
    result = engine.record(entry)
    assert result is entry
