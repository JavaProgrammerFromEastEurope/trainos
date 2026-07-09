from kernel.consumption.consumers.consumer import Consumer
from kernel.consumption.consumers.consumer_engine import ConsumerEngine
from kernel.consumption.consumers.consumer_status import ConsumerStatus
from kernel.consumption.consumers.consumer_type import ConsumerType


def test_consumer_engine():

    engine = ConsumerEngine()

    consumer = Consumer(
        consumer_id="C1",
        name="Hospital",
        consumer_type=ConsumerType.HOSPITAL,
        status=ConsumerStatus.OFFLINE,
    )

    active = engine.activate(consumer)
    assert active.status == ConsumerStatus.ACTIVE

    inactive = engine.deactivate(active)
    assert inactive.status == ConsumerStatus.OFFLINE