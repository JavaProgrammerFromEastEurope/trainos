from .education_history_entry import EducationHistoryEntry


class EducationHistoryEngine:

    def record(
        self,
        entry: EducationHistoryEntry,
    ) -> EducationHistoryEntry:
        return entry