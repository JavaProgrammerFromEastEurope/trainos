from kernel.events.snapshot.event_snapshot import EventSnapshot

from kernel.events.snapshot.publisher_snapshot import PublisherSnapshot
from kernel.events.snapshot.subscriber_snapshot import SubscriberSnapshot
from kernel.events.snapshot.routing_snapshot import RoutingSnapshot
from kernel.events.snapshot.snapshot_engine import SnapshotEngine


def test_event_snapshot():

    snapshot = EventSnapshot(
        snapshot_id="SNAP-001",
        publisher=PublisherSnapshot(
            published_events=100,
        ),
        subscriber=SubscriberSnapshot(
            active_subscribers=25,
        ),
        routing=RoutingSnapshot(
            routes=40,
        ),
    )

    result = SnapshotEngine().capture(snapshot)
    assert result.snapshot_id == "SNAP-001"
    assert result.publisher.published_events == 100
    assert result.subscriber.active_subscribers == 25
    assert result.routing.routes == 40
