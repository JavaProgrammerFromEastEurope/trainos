from kernel.core.registry.base_registry import BaseRegistry

from .security_snapshot import SecuritySnapshot


class SecuritySnapshotRegistry(
    BaseRegistry[SecuritySnapshot],
):
    pass
