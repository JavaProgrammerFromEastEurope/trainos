from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Allocation:

    allocation_id: 		str
    item_id: 					str
    allocated_amount: Decimal