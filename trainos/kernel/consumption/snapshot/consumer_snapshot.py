from dataclasses import dataclass

from kernel.consumption.consumers.consumer_status import ConsumerStatus


@dataclass(frozen=True, slots=True)
class ConsumerSnapshot:

    consumer_id: str
    status: ConsumerStatus