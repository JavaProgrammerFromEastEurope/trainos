from .base_history_entry import BaseHistoryEntry


class BaseHistoryRuntime:

    def initialize(self) -> None:
        pass

    def record(
        self,
        entry: BaseHistoryEntry,
    ) -> BaseHistoryEntry:
        return entry

    def shutdown(self) -> None:
        pass
