from kernel.core.registry.base_registry import BaseRegistry

from .governance_snapshot import GovernanceSnapshot


class GovernanceSnapshotRegistry(
    BaseRegistry[GovernanceSnapshot],
):
    pass
