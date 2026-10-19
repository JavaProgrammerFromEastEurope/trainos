from kernel.events.subscriber.subscriber import Subscriber

from kernel.events.subscriber.subscription import Subscription
from kernel.events.events.event import Event
from kernel.events.events.event_priority import EventPriority
from kernel.events.subscriber.subscriber_engine import SubscriberEngine


def test_subscriber_accepts():

    subscriber = Subscriber(
        subscriber_id="SUB-001",
        name="Healthcare",
        subscription=Subscription(
            event_name="CitizenBorn",
        ),
    )
    event = Event(
        event_id="EVENT-004",
        name="CitizenBorn",
        priority=EventPriority.NORMAL,
    )
    result = SubscriberEngine().accepts(
        subscriber,
        event,
    )
    assert result is True
