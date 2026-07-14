from kernel.events.events.event import Event, EventPriority, EventStatus


def test_event_creation():

    event = Event(
        event_id="EVENT-001",
        name="CitizenBorn",
        priority=EventPriority.NORMAL,
    )

    assert event.event_id == "EVENT-001"
    assert event.name == "CitizenBorn"
    assert event.priority == EventPriority.NORMAL
    assert event.status == EventStatus.CREATED
