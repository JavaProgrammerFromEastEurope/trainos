from dataclasses import dataclass

from kernel.consumption.requests.consumption_request_status import (
    ConsumptionRequestStatus,
)


@dataclass(frozen=True, slots=True)
class ConsumptionRequestSnapshot:

    request_id: str
    status: ConsumptionRequestStatus