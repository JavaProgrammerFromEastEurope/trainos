from kernel.core.registry.base_registry import BaseRegistry

from .resource_audit_entry import ResourceAuditEntry


class ResourceAuditRegistry(
    BaseRegistry[ResourceAuditEntry]
):
    pass