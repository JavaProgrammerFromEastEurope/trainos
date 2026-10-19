from kernel.core.registry.base_registry import BaseRegistry

from .governance_audit_entry import GovernanceAuditEntry


class GovernanceAuditRegistry(
    BaseRegistry[GovernanceAuditEntry],
):
    pass
