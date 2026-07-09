from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConsumptionRequestPolicy:

    require_positive_quantity: 	bool = True
    allow_zero_quantity: 				bool = False