from kernel.core.registry.base_registry import BaseRegistry

from .population_audit_entry import PopulationAuditEntry


class PopulationAuditRegistry(
    BaseRegistry[PopulationAuditEntry],
):
    pass
