from dataclasses import dataclass

from .event_priority import EventPriority
from .event_status import EventStatus


@dataclass(frozen=True, slots=True)
class Event:

    event_id: str
    name: 		str
    priority: EventPriority
    status: EventStatus = EventStatus.CREATED