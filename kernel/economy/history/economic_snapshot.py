from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class EconomicSnapshot:

    snapshot_id: str
    treasury_assets: 	Decimal
    planned_budget: 	Decimal
    collected_tax: 		Decimal