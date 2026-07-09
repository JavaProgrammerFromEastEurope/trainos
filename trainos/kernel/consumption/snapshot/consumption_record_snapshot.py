from dataclasses import dataclass

from kernel.consumption.records.consumption_record_status import (
    ConsumptionRecordStatus,
)


@dataclass(frozen=True, slots=True)
class ConsumptionRecordSnapshot:

    record_id: str
    status: ConsumptionRecordStatus