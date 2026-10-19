from dataclasses import dataclass

from ..contracts.integration_contract import IntegrationContract
from .integration_event_status import IntegrationEventStatus
from .integration_event_type import IntegrationEventType


@dataclass(frozen=True, slots=True)
class IntegrationEvent:

    event_id: str
    event_type: IntegrationEventType
    contract: IntegrationContract
    status: IntegrationEventStatus
