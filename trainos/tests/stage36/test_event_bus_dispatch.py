from kernel.events.bus.event_bus import EventBus

from kernel.events.bus.bus_engine import BusEngine
from kernel.events.subscriber.subscriber import Subscriber
from kernel.events.subscriber.subscription import Subscription
from kernel.events.events.event import Event
from kernel.events.events.event_priority import EventPriority


def test_event_bus_dispatch():

    subscriber = Subscriber(
        subscriber_id="SUB-005",
        name="Security",
        subscription=Subscription(
            event_name="SecurityAlert",
        ),
    )
    bus = EventBus(subscribers=[subscriber])
    event = Event(
        event_id="EVENT-005",
        name="SecurityAlert",
        priority=EventPriority.CRITICAL,
    )
    result = BusEngine().dispatch(bus, event)
    assert result.delivered == 1
