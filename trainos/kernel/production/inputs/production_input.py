from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class ProductionInput:

    resource_id: str
    required_quantity: Decimal