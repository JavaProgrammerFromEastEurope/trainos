from dataclasses import dataclass


@dataclass(frozen=True)
class PricingPolicy:

    immutable_prices: bool
    allow_zero_price: bool