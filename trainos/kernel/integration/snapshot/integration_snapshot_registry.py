from kernel.core.registry.base_registry import BaseRegistry

from .integration_snapshot import IntegrationSnapshot


class IntegrationSnapshotRegistry(
    BaseRegistry[IntegrationSnapshot],
):
    pass
