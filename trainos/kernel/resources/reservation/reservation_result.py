from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class ReservationResult:

    reservation_id: str
    approved: 			bool
    reserved_quantity: Decimal