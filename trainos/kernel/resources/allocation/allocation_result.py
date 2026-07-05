from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class AllocationResult:

    allocation_id: 	str
    resource_id: 		str
    receiver_id: 		str
    approved_quantity: Decimal
    approved: bool