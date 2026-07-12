from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MessageBusSnapshot:

    bus_id: str
    queued_messages: int
