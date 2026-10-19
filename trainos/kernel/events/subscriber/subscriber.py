from dataclasses import dataclass

from .subscriber_status import SubscriberStatus

from .subscription import Subscription


@dataclass(frozen=True, slots=True)
class Subscriber:

    subscriber_id: 	str
    name: 					str
    subscription: Subscription
    status: SubscriberStatus = SubscriberStatus.ACTIVE
