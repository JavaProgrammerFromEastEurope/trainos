from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class TransferRequest:

    request_id: 			str
    resource_id: 			str
    source_owner_id: 	str
    destination_owner_id: str
    quantity: Decimal
    reason: str | None = None