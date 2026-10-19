from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class InventoryTransaction:

    transaction_id: str
    resource_id: 		str
    delta: Decimal  # +increase / -decrease
    reason: str | None