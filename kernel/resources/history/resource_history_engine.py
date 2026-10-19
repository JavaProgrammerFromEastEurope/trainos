from .resource_history_entry import ResourceHistoryEntry


class ResourceHistoryEngine:

    def record(
        self,
        entry: ResourceHistoryEntry,
    ) -> ResourceHistoryEntry:
        return entry
