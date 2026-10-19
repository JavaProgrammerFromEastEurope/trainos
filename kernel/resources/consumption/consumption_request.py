from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class ConsumptionRequest:

    request_id: 	str
    resource_id: 	str
    consumer_id: 	str
    quantity: Decimal
    reason: str | None = None