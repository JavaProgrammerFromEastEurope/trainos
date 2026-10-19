from .security_history_entry import SecurityHistoryEntry


class SecurityHistoryEngine:

    def record(
        self,
        entry: SecurityHistoryEntry,
    ) -> SecurityHistoryEntry:
        return entry
