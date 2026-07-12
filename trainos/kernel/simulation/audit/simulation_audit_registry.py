from kernel.core.registry.base_registry import BaseRegistry

from .simulation_audit_entry import SimulationAuditEntry


class SimulationAuditRegistry(
    BaseRegistry[SimulationAuditEntry],
):
    pass
