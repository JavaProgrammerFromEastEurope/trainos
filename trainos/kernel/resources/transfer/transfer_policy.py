from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TransferPolicy:

    require_owner_validation: 	bool
    require_available_quantity: bool
    allow_partial_transfer: 		bool