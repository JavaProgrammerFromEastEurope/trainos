from kernel.core.registry.base_registry import BaseRegistry

from .security_history_entry import SecurityHistoryEntry


class SecurityHistoryRegistry(
    BaseRegistry[SecurityHistoryEntry],
):
    pass
