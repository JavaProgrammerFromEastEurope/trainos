from dataclasses import dataclass

from .consumption_snapshot import ConsumptionSnapshot


@dataclass(frozen=True, slots=True)
class ConsumptionHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: ConsumptionSnapshot