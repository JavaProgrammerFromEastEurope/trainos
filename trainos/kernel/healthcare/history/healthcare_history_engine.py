from .healthcare_history_entry import HealthcareHistoryEntry


class HealthcareHistoryEngine:

    def record(
        self,
        entry: HealthcareHistoryEntry,
    ) -> HealthcareHistoryEntry:
        return entry
