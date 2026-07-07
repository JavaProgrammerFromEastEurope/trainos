from ...core.registry.base_registry import BaseRegistry

from .production_audit_entry import ProductionAuditEntry


class ProductionAuditRegistry(
    BaseRegistry[ProductionAuditEntry],
):
    pass
