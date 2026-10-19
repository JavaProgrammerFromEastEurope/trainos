from kernel.core.registry.base_registry import BaseRegistry

from .security_audit_entry import SecurityAuditEntry


class SecurityAuditRegistry(
    BaseRegistry[SecurityAuditEntry],
):
    pass
