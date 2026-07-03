from dataclasses import dataclass


@dataclass(frozen=True)
class TaxPolicy:

    allow_zero_rate: bool
    immutable_rates: bool