from .event import Event
from .event_status import EventStatus


class EventEngine:

    def publish(
        self,
        event: Event,
    ) -> Event:
        return Event(
            event_id=event.event_id,
            name=event.name,
            priority=event.priority,
            status=EventStatus.PUBLISHED,
        )

    def process(
        self,
        event: Event,
    ) -> Event:
        return Event(
            event_id=event.event_id,
            name=event.name,
            priority=event.priority,
            status=EventStatus.PROCESSED,
        )
