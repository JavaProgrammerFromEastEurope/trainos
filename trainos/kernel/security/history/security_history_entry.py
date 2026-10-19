from dataclasses import dataclass

from .security_history_snapshot import SecurityHistorySnapshot


@dataclass(frozen=True, slots=True)
class SecurityHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: SecurityHistorySnapshot