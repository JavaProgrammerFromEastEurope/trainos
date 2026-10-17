from typing import Protocol
from kernel.events.event import Event


class EventHandler(Protocol):
    def handle(self, event: Event) -> None: ...
