from dataclasses import dataclass

from .publisher_snapshot import PublisherSnapshot
from .subscriber_snapshot import SubscriberSnapshot
from .routing_snapshot import RoutingSnapshot


@dataclass(frozen=True, slots=True)
class EventSnapshot:

    snapshot_id: 	str
    publisher: 		PublisherSnapshot
    subscriber: 	SubscriberSnapshot
    routing: 			RoutingSnapshot