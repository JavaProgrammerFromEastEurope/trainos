from collections import defaultdict
from typing import Callable

from trainos.core.events import Event  # type: ignore


class EventBus:

    def __init__(self):

        self._subscribers: dict[str, list[Callable]] = defaultdict(list)  # type: ignore

    def subscribe(self, event_type: str, callback: Callable):

        self._subscribers[event_type].append(callback)

    def publish(self, event: Event):

        listeners = self._subscribers.get(event.type, [])

        for listener in listeners:
            listener(event)
