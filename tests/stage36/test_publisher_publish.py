from kernel.events.publisher.publisher import Publisher

from kernel.events.events.event import Event
from kernel.events.events.event_priority import EventPriority
from kernel.events.publisher.publisher_engine import PublisherEngine


def test_publisher_publish():

    publisher = Publisher(
        publisher_id="PUB-001",
        name="PopulationService",
    )
    event = Event(
        event_id="EVENT-003",
        name="CitizenBorn",
        priority=EventPriority.NORMAL,
    )
    result = PublisherEngine().publish(
        publisher,
        event,
    )

    assert result.success is True
    assert result.event_id == "EVENT-003"
