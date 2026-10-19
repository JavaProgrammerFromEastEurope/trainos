from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class ResourceSnapshot:

    snapshot_id: str
    resource_id: str
    quantity: Decimal