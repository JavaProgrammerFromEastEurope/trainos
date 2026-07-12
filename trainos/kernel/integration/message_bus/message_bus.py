from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MessageBus:

    bus_id: str
