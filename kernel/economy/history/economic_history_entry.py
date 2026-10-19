from dataclasses import dataclass

from .economic_snapshot import EconomicSnapshot


@dataclass(frozen=True)
class EconomicHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: EconomicSnapshot