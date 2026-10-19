from dataclasses import dataclass
from decimal import Decimal

from .storage_status import StorageStatus


@dataclass(frozen=True, slots=True)
class StorageRecord:

    storage_id: 	str
    warehouse_id: str
    resource_id: 	str
    quantity: Decimal
    status: StorageStatus