from kernel.logistics.warehouses.warehouse import Warehouse
from kernel.logistics.warehouses.warehouse_engine import WarehouseEngine
from kernel.logistics.warehouses.warehouse_status import WarehouseStatus
from kernel.logistics.warehouses.warehouse_type import WarehouseType


def test_warehouse_engine():

    engine = WarehouseEngine()

    warehouse = Warehouse(
        warehouse_id="WH1",
        name="Water Warehouse",
        warehouse_type=WarehouseType.WATER,
        status=WarehouseStatus.OFFLINE,
    )

    opened = engine.open(warehouse)

    assert opened.status == WarehouseStatus.ACTIVE

    closed = engine.close(opened)

    assert closed.status == WarehouseStatus.OFFLINE