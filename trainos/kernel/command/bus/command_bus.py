from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CommandBus:

    bus_id: str
