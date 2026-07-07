from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ShipmentPolicy:

    require_positive_quantity: 			bool = True
    allow_same_source_destination: 	bool = False