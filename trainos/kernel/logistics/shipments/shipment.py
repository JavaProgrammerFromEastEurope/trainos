from dataclasses import dataclass
from decimal import Decimal

from trainos.kernel.logistics.shipments import shipment_status


@dataclass(frozen=True, slots=True)
class Shipment:

    shipment_id: str

    from_warehouse_id: str

    to_warehouse_id: str

    resource_id: str

    quantity: Decimal

    status: shipment_status