from __future__ import annotations

from .producer_result import ProducerResult
from .producer_status import ProducerStatus


class Producer:

    def produce(self) -> ProducerResult:
        return ProducerResult(status=ProducerStatus.SUCCESS)
