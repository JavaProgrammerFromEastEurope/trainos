from dataclasses import dataclass

from kernel.integration.events.integration_event import IntegrationEvent
from .message_status import MessageStatus


@dataclass(frozen=True, slots=True)
class Message:

    message_id: str
    event: IntegrationEvent
    status: MessageStatus
