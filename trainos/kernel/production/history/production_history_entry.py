from dataclasses import dataclass

from .production_snapshot import ProductionSnapshot


@dataclass(frozen=True, slots=True)
class ProductionHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: ProductionSnapshot