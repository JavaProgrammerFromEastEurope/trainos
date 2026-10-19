from kernel.core.registry.base_registry import BaseRegistry

from .healthcare_audit_entry import HealthcareAuditEntry


class HealthcareAuditRegistry(
    BaseRegistry[HealthcareAuditEntry],
):
    pass
