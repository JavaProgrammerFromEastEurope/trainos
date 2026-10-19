from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ResourcesConfiguration:

    enable_inventory: 	bool = True
    enable_ownership: 	bool = True
    enable_allocation: 	bool = True
    enable_reservation: bool = True
    enable_transfer: 		bool = True
    enable_consumption: bool = True