from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class TreasurySnapshot:

    treasury_id: 	str
    total_assets: Decimal