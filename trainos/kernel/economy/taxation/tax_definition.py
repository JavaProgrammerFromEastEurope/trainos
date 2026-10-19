from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class TaxDefinition:

    tax_id: str
    name: str
    rate: Decimal