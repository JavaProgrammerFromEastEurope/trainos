from .warehouse import Warehouse
from .warehouse_status import WarehouseStatus


class WarehouseEngine:

    def open(
        self,
        warehouse: Warehouse,
    ) -> Warehouse:
        return Warehouse(
            warehouse_id=warehouse.warehouse_id,
            name=warehouse.name,
            warehouse_type=warehouse.warehouse_type,
            status=WarehouseStatus.ACTIVE,
        )

    def close(
        self,
        warehouse: Warehouse,
    ) -> Warehouse:
        return Warehouse(
            warehouse_id=warehouse.warehouse_id,
            name=warehouse.name,
            warehouse_type=warehouse.warehouse_type,
            status=WarehouseStatus.OFFLINE,
        )
