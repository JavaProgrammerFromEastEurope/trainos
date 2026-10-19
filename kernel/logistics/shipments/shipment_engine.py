from .shipment import Shipment
from .shipment_result import ShipmentResult
from .shipment_status import ShipmentStatus


class ShipmentEngine:

    def dispatch(self, shipment: Shipment) -> ShipmentResult:
        return ShipmentResult(
            shipment_id=shipment.shipment_id,
            status=ShipmentStatus.IN_TRANSIT,
        )

    def deliver(self, shipment: Shipment) -> ShipmentResult:
        return ShipmentResult(
            shipment_id=shipment.shipment_id,
            status=ShipmentStatus.DELIVERED,
        )

    def fail(self, shipment: Shipment) -> ShipmentResult:
        return ShipmentResult(
            shipment_id=shipment.shipment_id,
            status=ShipmentStatus.FAILED,
        )

    def cancel(self, shipment: Shipment) -> ShipmentResult:
        return ShipmentResult(
            shipment_id=shipment.shipment_id,
            status=ShipmentStatus.CANCELLED,
        )
