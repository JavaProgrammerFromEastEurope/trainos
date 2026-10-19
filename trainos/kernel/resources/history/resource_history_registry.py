from kernel.core.registry.base_registry import BaseRegistry

from .resource_history_entry import ResourceHistoryEntry


class ResourceHistoryRegistry(
    BaseRegistry[ResourceHistoryEntry]
):
    pass