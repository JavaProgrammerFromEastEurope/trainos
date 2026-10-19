from kernel.core.registry.base_registry import BaseRegistry

from .workflow_audit import WorkflowAudit


class AuditRegistry(
    BaseRegistry[WorkflowAudit],
):
    pass
