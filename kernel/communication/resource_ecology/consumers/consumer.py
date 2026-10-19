from __future__ import annotations

from .consumer_result import ConsumerResult
from .consumer_status import ConsumerStatus


class Consumer:

    def consume(self) -> ConsumerResult:
        return ConsumerResult(status=ConsumerStatus.SUCCESS)
