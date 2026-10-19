from dataclasses import dataclass
from decimal import Decimal

from .consumption_record_status import ConsumptionRecordStatus


@dataclass(frozen=True, slots=True)
class ConsumptionRecord:

    record_id: 		str
    consumer_id: 	str
    resource_id: 	str
    quantity: Decimal
    status: ConsumptionRecordStatus