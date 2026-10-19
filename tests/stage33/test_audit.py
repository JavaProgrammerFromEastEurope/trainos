from kernel.persistence.audit.audit_record 		import AuditRecord
from kernel.persistence.audit.audit_operation import AuditOperation
from kernel.persistence.audit.audit_status 		import AuditStatus
from kernel.persistence.audit.audit_engine 		import AuditEngine


def test_audit():

    record = AuditRecord(
        audit_id="AUD1",
        object_id="RESIDENT1",
        operation=AuditOperation.UPDATE,
        status=AuditStatus.SUCCESS,
        timestamp="2035-01-01T10:00",
    )

    result = AuditEngine().record(record)
    assert result.audit_id == "AUD1"
    assert result.operation == AuditOperation.UPDATE
    assert result.status == AuditStatus.SUCCESS
