from kernel.core.registry.base_registry import BaseRegistry

from .consumption_audit_entry import ConsumptionAuditEntry


class ConsumptionAuditRegistry(
    BaseRegistry[ConsumptionAuditEntry],
):
    pass
