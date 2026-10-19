from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class LogisticsWarehouseSnapshot:

    warehouse_id: str
    status: str