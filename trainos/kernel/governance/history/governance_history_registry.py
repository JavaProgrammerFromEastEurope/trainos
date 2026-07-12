from kernel.core.registry.base_registry import BaseRegistry

from .governance_history_entry import GovernanceHistoryEntry


class GovernanceHistoryRegistry(
    BaseRegistry[GovernanceHistoryEntry],
):
    pass
