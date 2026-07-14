from kernel.events.events.event import Event, EventPriority, EventStatus
from kernel.events.events.event_engine import EventEngine


def test_event_lifecycle():

    event = Event(
        event_id="EVENT-002",
        name="SimulationTick",
        priority=EventPriority.HIGH,
    )

    engine = EventEngine()
    event = engine.publish(event)

    assert event.status == EventStatus.PUBLISHED

    event = engine.process(event)
    assert event.status == EventStatus.PROCESSED
