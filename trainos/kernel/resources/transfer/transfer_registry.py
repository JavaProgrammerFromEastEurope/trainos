from kernel.core.registry.base_registry import BaseRegistry

from .resource_transfer import ResourceTransfer


class TransferRegistry(
    BaseRegistry[ResourceTransfer],
):
    pass
