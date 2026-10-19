from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class ConsumptionResult:

    consumption_id: 		str
    consumed_quantity: Decimal
    approved: 					bool