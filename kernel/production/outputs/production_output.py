from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class ProductionOutput:

    resource_id: str
    produced_quantity: Decimal