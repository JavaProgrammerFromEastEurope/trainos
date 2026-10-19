from dataclasses import dataclass

from kernel.logistics.shipments.shipment_status import ShipmentStatus


@dataclass(frozen=True, slots=True)
class LogisticsShipmentSnapshot:

    shipment_id: str
    status: ShipmentStatus
