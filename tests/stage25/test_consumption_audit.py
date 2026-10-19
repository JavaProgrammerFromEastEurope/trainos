from kernel.consumption.audit.consumption_audit_engine import ConsumptionAuditEngine
from kernel.consumption.audit.consumption_audit_entry import ConsumptionAuditEntry


def test_consumption_audit():

    engine = ConsumptionAuditEngine()
    entry = ConsumptionAuditEntry(
        audit_id="AUD1",
        actor_id="government",
        consumer_id="C1",
        job_id="JOB1",
        action="consume",
    )

    result = engine.record(entry)
    assert result is entry