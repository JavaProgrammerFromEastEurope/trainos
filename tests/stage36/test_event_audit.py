from kernel.events.audit.audit_record import AuditRecord

from kernel.events.audit.audit_status import AuditStatus
from kernel.events.audit.delivery_statistics import DeliveryStatistics
from kernel.events.audit.audit_engine import AuditEngine


def test_event_audit():

    record = AuditRecord(
        audit_id="AUDIT-001",
        event_id="EVENT-010",
        status=AuditStatus.DELIVERED,
        statistics=DeliveryStatistics(
            subscribers=5,
        ),
        timestamp="2035-01-01T12:00",
    )
    result = AuditEngine().record(record)
    assert result.audit_id == "AUDIT-001"
    assert result.event_id == "EVENT-010"
    assert result.status == AuditStatus.DELIVERED
    assert result.statistics.subscribers == 5
