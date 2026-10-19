from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class TaxSnapshot:
    total_tax_collected: Decimal
