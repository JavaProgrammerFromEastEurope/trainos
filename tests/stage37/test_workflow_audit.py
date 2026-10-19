from kernel.workflow.audit.workflow_audit import WorkflowAudit

from kernel.workflow.audit.audit_status 		import AuditStatus
from kernel.workflow.audit.audit_statistics import AuditStatistics
from kernel.workflow.audit.audit_engine 		import AuditEngine


def test_workflow_audit():

    audit = WorkflowAudit(
        audit_id="AUDIT-001",
        workflow_id="WF-010",
        status=AuditStatus.COMPLETED,
        statistics=AuditStatistics(
            executed_steps=5,
            failed_steps=0,
        ),
        timestamp="2035-06-01T08:00",
    )
    result = AuditEngine().record(audit)
    assert result.audit_id == "AUDIT-001"
    assert result.workflow_id == "WF-010"
    assert result.status == AuditStatus.COMPLETED
    assert result.statistics.executed_steps == 5
    assert result.statistics.failed_steps == 0
