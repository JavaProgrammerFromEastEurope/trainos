from dataclasses import dataclass

from .logistics_warehouse_snapshot import LogisticsWarehouseSnapshot
from .logistics_shipment_snapshot import LogisticsShipmentSnapshot
from .logistics_transport_snapshot import LogisticsTransportSnapshot
from .logistics_delivery_snapshot import LogisticsDeliverySnapshot
from .logistics_runtime_snapshot import LogisticsRuntimeSnapshot


@dataclass(frozen=True, slots=True)
class LogisticsSnapshot:

    snapshot_id: str
    runtime: LogisticsRuntimeSnapshot
    warehouses: tuple[LogisticsWarehouseSnapshot, ...]
    shipments: 	tuple[LogisticsShipmentSnapshot, ...]
    transports: tuple[LogisticsTransportSnapshot, ...]
    deliveries: tuple[LogisticsDeliverySnapshot, ...]