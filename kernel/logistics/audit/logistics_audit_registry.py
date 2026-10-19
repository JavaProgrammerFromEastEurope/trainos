from kernel.core.registry.base_registry import BaseRegistry

from .logistics_audit_entry import LogisticsAuditEntry


class LogisticsAuditRegistry(
    BaseRegistry[LogisticsAuditEntry],
):
    pass
