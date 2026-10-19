from .institution_history_entry import InstitutionHistoryEntry


class InstitutionHistoryEngine:

    def append(
        self,
        entry: InstitutionHistoryEntry,
    ) -> InstitutionHistoryEntry:
        return entry