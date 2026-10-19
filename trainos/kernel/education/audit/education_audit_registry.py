from kernel.core.registry.base_registry import BaseRegistry

from .education_audit_entry import EducationAuditEntry


class EducationAuditRegistry(
    BaseRegistry[EducationAuditEntry],
):
    pass
