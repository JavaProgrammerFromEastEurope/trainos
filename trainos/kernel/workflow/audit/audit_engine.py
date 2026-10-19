from .workflow_audit import WorkflowAudit


class AuditEngine:

    def record(
        self,
        audit: WorkflowAudit,
    ) -> WorkflowAudit:
        return audit
