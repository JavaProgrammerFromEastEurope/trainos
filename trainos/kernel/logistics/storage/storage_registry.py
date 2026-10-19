from kernel.core.registry.base_registry import BaseRegistry

from .storage_record import StorageRecord


class StorageRegistry(
    BaseRegistry[StorageRecord],
):
    pass
