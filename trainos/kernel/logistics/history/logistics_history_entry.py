from dataclasses import dataclass

from .logistics_snapshot import LogisticsSnapshot


@dataclass(frozen=True, slots=True)
class LogisticsHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: LogisticsSnapshot