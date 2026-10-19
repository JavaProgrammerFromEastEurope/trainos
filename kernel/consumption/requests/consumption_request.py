from dataclasses import dataclass
from decimal import Decimal

from .consumption_request_priority 	import ConsumptionRequestPriority
from .consumption_request_status 		import ConsumptionRequestStatus


@dataclass(frozen=True, slots=True)
class ConsumptionRequest:

    request_id: 	str
    consumer_id: 	str
    resource_id: 	str
    quantity: 		Decimal
    priority: ConsumptionRequestPriority
    status: 	ConsumptionRequestStatus