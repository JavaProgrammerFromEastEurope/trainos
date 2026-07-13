from kernel.core.registry.base_registry import BaseRegistry

from .configuration_snapshot import ConfigurationSnapshot


class SnapshotRegistry(
    BaseRegistry[ConfigurationSnapshot],
):
    pass
