from dataclasses import dataclass

from .shipment_status import ShipmentStatus


@dataclass(frozen=True, slots=True)
class ShipmentResult:

    shipment_id: str
    status: ShipmentStatus