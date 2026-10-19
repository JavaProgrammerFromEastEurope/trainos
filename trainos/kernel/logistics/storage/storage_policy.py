from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StoragePolicy:

    allow_negative_quantity: 	bool = False
    allow_zero_quantity: 			bool = True