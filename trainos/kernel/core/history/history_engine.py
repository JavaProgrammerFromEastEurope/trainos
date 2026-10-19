from .base_history_entry import BaseHistoryEntry


class HistoryEngine:

    def snapshot(
        self,
        entry: BaseHistoryEntry,
    ) -> BaseHistoryEntry:
        return entry
