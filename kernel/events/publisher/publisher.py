from dataclasses import dataclass

from .publisher_status import PublisherStatus


@dataclass(frozen=True, slots=True)
class Publisher:

    publisher_id: str
    name: str
    status: PublisherStatus = PublisherStatus.READY
