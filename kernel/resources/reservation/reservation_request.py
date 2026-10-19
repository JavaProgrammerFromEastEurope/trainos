from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class ReservationRequest:

    request_id: 	str
    resource_id: 	str
    requester_id: str
    quantity: Decimal
    reason: str | None = None