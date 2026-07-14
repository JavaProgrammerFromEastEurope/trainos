from kernel.events.routing.routing_engine import RoutingEngine

from kernel.events.subscriber.subscriber 		import Subscriber
from kernel.events.subscriber.subscription 	import Subscription
from kernel.events.events.event 						import Event
from kernel.events.events.event_priority 		import EventPriority


def test_event_routing():

    subscriber = Subscriber(
        subscriber_id="SUB-007",
        name="Persistence",
        subscription=Subscription(
            event_name="SnapshotCreated",
        ),
    )
    event = Event(
        event_id="EVENT-007",
        name="SnapshotCreated",
        priority=EventPriority.NORMAL,
    )
    result = RoutingEngine().route(
        [subscriber],
        event,
    )

    assert len(result) == 1
    assert result[0].name == "Persistence"
