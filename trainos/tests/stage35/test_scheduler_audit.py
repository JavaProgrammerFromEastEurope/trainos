from kernel.scheduling.audit.audit_record import AuditRecord

from kernel.scheduling.audit.audit_status import AuditStatus
from kernel.scheduling.audit.execution_statistics import ExecutionStatistics
from kernel.scheduling.audit.audit_engine import AuditEngine


def test_scheduler_audit():
    record = AuditRecord(
        audit_id="AUDIT-001",
        task_id="TASK-010",
        status=AuditStatus.SUCCESS,
        statistics=ExecutionStatistics(
            duration_ms=25,
        ),
        timestamp="2035-01-01T10:00",
    )
    result = AuditEngine().record(record)

    assert result.audit_id == "AUDIT-001"
    assert result.task_id == "TASK-010"
    assert result.status == AuditStatus.SUCCESS
    assert result.statistics.duration_ms == 25
