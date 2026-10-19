from dataclasses import dataclass

from .healthcare_history_snapshot import HealthcareHistorySnapshot


@dataclass(frozen=True, slots=True)
class HealthcareHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: HealthcareHistorySnapshot