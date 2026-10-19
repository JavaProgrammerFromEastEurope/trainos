from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProductionOutputPolicy:

    allow_zero_output: bool = False