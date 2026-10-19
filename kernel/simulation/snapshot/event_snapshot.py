from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EventSnapshot:

    event_id: str
    tick: int