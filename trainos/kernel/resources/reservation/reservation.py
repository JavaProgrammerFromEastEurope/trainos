from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class Reservation:

    reservation_id: str
    resource_id: 		str
    owner_id: 			str
    quantity: Decimal