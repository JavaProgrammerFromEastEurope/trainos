from decimal import Decimal

from kernel.logistics.shipments.shipment import Shipment
from kernel.logistics.shipments.shipment_engine import ShipmentEngine
from kernel.logistics.shipments.shipment_status import ShipmentStatus


def test_shipment_engine():

    engine = ShipmentEngine()

    shipment = Shipment(
        shipment_id="SHIP1",
        from_warehouse_id="WH1",
        to_warehouse_id="WH2",
        resource_id="water",
        quantity=Decimal("50"),
        status=ShipmentStatus.CREATED,
    )

    dispatched = engine.dispatch(shipment)

    assert dispatched.shipment_id == "SHIP1"
    assert dispatched.status == ShipmentStatus.IN_TRANSIT

    delivered = engine.deliver(shipment)

    assert delivered.status == ShipmentStatus.DELIVERED