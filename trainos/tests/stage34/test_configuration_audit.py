from kernel.configuration.audit.audit_record import AuditRecord

from kernel.configuration.audit.audit_operation import AuditOperation
from kernel.configuration.audit.audit_status 		import AuditStatus
from kernel.configuration.audit.audit_engine 		import AuditEngine


def test_configuration_audit():

    record = AuditRecord(
        audit_id="AUD1",
        configuration_key="simulation.tick_duration",
        operation=AuditOperation.UPDATE,
        status=AuditStatus.SUCCESS,
        timestamp="2035-01-01T10:00",
    )

    result = AuditEngine().record(record)

    assert result.audit_id == "AUD1"
    assert result.operation == AuditOperation.UPDATE
    assert result.status == AuditStatus.SUCCESS
