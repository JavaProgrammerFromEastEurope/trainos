from typing import Protocol
from trainos.kernel.events.event import Event


class EventHandler(Protocol):
    def handle(self, event: Event) -> None: ...
