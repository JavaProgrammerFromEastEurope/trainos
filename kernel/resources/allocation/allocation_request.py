from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class AllocationRequest:

    request_id: 	str
    resource_id: 	str
    receiver_id: 	str
    quantity: Decimal
    reason: str | None = None