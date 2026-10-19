from dataclasses import dataclass

from .bus_status import BusStatus


@dataclass(slots=True)
class EventBus:

    subscribers: list = None
    status: BusStatus = BusStatus.READY

    def __post_init__(self):
        if self.subscribers is None:
            self.subscribers = []