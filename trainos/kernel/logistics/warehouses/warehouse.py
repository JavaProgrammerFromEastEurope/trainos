from dataclasses import dataclass

from .warehouse_status import WarehouseStatus
from .warehouse_type import WarehouseType


@dataclass(frozen=True, slots=True)
class Warehouse:

    warehouse_id: 	str
    name: 					str
    warehouse_type: WarehouseType
    status: WarehouseStatus