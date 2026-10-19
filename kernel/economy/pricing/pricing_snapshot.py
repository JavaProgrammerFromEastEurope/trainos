from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class PricingSnapshot:

    average_price: Decimal