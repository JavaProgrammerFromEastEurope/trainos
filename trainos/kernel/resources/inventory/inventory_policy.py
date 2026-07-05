from dataclasses import dataclass


@dataclass(frozen=True)
class InventoryPolicy:

    allow_negative_stock: bool
    strict_validation: 		bool