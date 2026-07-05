from dataclasses import dataclass

from decimal import Decimal


@dataclass
class ResourceInventory:

    resource_id: str
    quantity: Decimal