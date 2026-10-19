from kernel.core.registry.base_registry import BaseRegistry

from .audit_record import AuditRecord


class AuditRegistry(
    BaseRegistry[AuditRecord],
):
    pass
