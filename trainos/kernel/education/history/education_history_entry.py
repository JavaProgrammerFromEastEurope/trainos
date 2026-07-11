from dataclasses import dataclass

from .education_history_snapshot import EducationHistorySnapshot


@dataclass(frozen=True, slots=True)
class EducationHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: EducationHistorySnapshot