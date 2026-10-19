from kernel.events.routing.routing_engine import RoutingEngine

from kernel.events.subscriber.subscriber import Subscriber
from kernel.events.subscriber.subscription import Subscription
from kernel.events.events.event import Event
from kernel.events.events.event_priority import EventPriority


def test_event_routing_ignore():

    subscriber = Subscriber(
        subscriber_id="SUB-008",
        name="Healthcare",
        subscription=Subscription(
            event_name="MedicalEmergency",
        ),
    )
    event = Event(
        event_id="EVENT-008",
        name="CitizenBorn",
        priority=EventPriority.NORMAL,
    )
    result = RoutingEngine().route(
        [subscriber],
        event,
    )
    assert len(result) == 0
