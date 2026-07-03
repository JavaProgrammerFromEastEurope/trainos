from dataclasses import dataclass

from .history_snapshot import HistorySnapshot


@dataclass(frozen=True)
class BaseHistoryEntry:

    entry_id: str
    snapshot: HistorySnapshot