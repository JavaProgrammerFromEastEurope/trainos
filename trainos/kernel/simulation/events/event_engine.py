from .simulation_event 	import SimulationEvent
from .event_status 			import EventStatus


class EventEngine:

    def process(
        self,
        event: SimulationEvent,
    ) -> SimulationEvent:
        return SimulationEvent(
            event_id=event.event_id,
            tick=event.tick,
            event_type=event.event_type,
            payload=event.payload,
            status=EventStatus.PROCESSED,
        )
