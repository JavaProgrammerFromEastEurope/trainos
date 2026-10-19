from dataclasses import dataclass

from .consumer_status import ConsumerStatus


@dataclass
class ConsumerResult:
    status: ConsumerStatus
