from .consumer import Consumer
from .consumer_status import ConsumerStatus


class ConsumerEngine:

    def activate(
        self,
        consumer: Consumer,
    ) -> Consumer:
        return Consumer(
            consumer_id=consumer.consumer_id,
            name=consumer.name,
            consumer_type=consumer.consumer_type,
            status=ConsumerStatus.ACTIVE,
        )

    def deactivate(
        self,
        consumer: Consumer,
    ) -> Consumer:
        return Consumer(
            consumer_id=consumer.consumer_id,
            name=consumer.name,
            consumer_type=consumer.consumer_type,
            status=ConsumerStatus.OFFLINE,
        )
