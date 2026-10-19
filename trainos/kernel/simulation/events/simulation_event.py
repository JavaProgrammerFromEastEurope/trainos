from dataclasses import dataclass

from .event_payload import EventPayload
from .event_status 	import EventStatus
from .event_type 		import EventType


@dataclass(frozen=True, slots=True)
class SimulationEvent:

    event_id: 	str
    tick: 			int
    event_type: EventType
    payload: 		EventPayload
    status: 		EventStatus