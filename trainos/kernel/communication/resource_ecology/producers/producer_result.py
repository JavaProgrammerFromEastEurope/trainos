from dataclasses import dataclass

from .producer_status import ProducerStatus


@dataclass
class ProducerResult:
    status: ProducerStatus
