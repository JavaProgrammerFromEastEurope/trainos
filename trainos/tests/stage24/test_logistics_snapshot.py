from kernel.logistics.jobs.delivery_job_status import DeliveryJobStatus
from kernel.logistics.runtime.logistics_lifecycle import LogisticsLifecycle
from kernel.logistics.shipments.shipment_status import ShipmentStatus
from kernel.logistics.snapshot.logistics_delivery_snapshot import LogisticsDeliverySnapshot
from kernel.logistics.snapshot.logistics_runtime_snapshot import LogisticsRuntimeSnapshot
from kernel.logistics.snapshot.logistics_shipment_snapshot import LogisticsShipmentSnapshot
from kernel.logistics.snapshot.logistics_snapshot import LogisticsSnapshot
from kernel.logistics.snapshot.logistics_snapshot_engine import LogisticsSnapshotEngine
from kernel.logistics.snapshot.logistics_transport_snapshot import LogisticsTransportSnapshot
from kernel.logistics.snapshot.logistics_warehouse_snapshot import LogisticsWarehouseSnapshot
from kernel.logistics.transport.transport_status import TransportStatus


def test_logistics_snapshot():

    engine = LogisticsSnapshotEngine()

    snapshot = LogisticsSnapshot(
        snapshot_id="SNAP1",
        runtime=LogisticsRuntimeSnapshot(
            lifecycle=LogisticsLifecycle.RUNNING,
        ),
        warehouses=(
            LogisticsWarehouseSnapshot(
                warehouse_id="WH1",
                status="ACTIVE",
            ),
        ),
        shipments=(
            LogisticsShipmentSnapshot(
                shipment_id="SHIP1",
                status=ShipmentStatus.IN_TRANSIT,
            ),
        ),
        transports=(
            LogisticsTransportSnapshot(
                transport_id="TR1",
                status=TransportStatus.BUSY,
            ),
        ),
        deliveries=(
            LogisticsDeliverySnapshot(
                job_id="JOB1",
                status=DeliveryJobStatus.RUNNING,
            ),
        ),
    )

    result = engine.capture(snapshot)

    assert result is snapshot