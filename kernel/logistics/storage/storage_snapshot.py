from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class StorageSnapshot:

    warehouse_id: str
    resource_id: str
    quantity: Decimal