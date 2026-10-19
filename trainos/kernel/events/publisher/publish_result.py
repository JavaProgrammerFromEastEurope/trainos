from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PublishResult:

    success: bool
    event_id: str