from trainos.kernel.events.event_bus import EventBus
from trainos.kernel.events.event import Event
from trainos.kernel.events.event_handler import EventHandler


class TestHandler(EventHandler):
    def __init__(self):
        self.events = []

    def handle(self, event: Event):
        self.events.append(event)


def test_event_bus_publish_subscribe():
    bus = EventBus()
    handler = TestHandler()

    bus.subscribe("test_event", handler)

    # ✔ FIX: timestamp is auto-managed by Event
    event = Event("test_event", {"value": 1})

    bus.publish(event)
    bus.update()

    assert len(handler.events) == 1
    assert handler.events[0].event_type == "test_event"
    assert handler.events[0].payload["value"] == 1
    assert handler.events[0].timestamp is not None
