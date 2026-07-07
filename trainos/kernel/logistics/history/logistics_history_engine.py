from .logistics_history_entry import LogisticsHistoryEntry


class LogisticsHistoryEngine:

    def record(
        self,
        entry: LogisticsHistoryEntry,
    ) -> LogisticsHistoryEntry:
        return entry