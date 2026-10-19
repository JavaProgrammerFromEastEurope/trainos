from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AllocationPolicy:

    allow_partial_allocation: 		bool
    require_available_inventory: 	bool