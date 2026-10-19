from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PublisherSnapshot:

    published_events: int
