from collections import defaultdict, deque
from typing import Callable, Any, Union
# CASE 2: (type, payload)
from trainos.kernel.events.event import Event

class EventBus:
    def __init__(self) -> None:
        self._subscribers = defaultdict(list)
        self._queue = deque()

    def subscribe(self, event_type: str, handler: Callable[[Any], None]) -> None:
        self._subscribers[event_type].append(handler)

    def unsubscribe(self, event_type: str, handler: Callable[[Any], None]) -> None:
        if handler in self._subscribers[event_type]:
            self._subscribers[event_type].remove(handler)

    def publish(self, event_or_type: Any, payload: Any = None) -> None:
        # CASE 1: Event object
        if payload is None and hasattr(event_or_type, "event_type"):
            self._queue.append(event_or_type)
            return


        self._queue.append(Event(event_or_type, payload))

    def update(self) -> None:
        queue = self._queue
        self._queue = deque()

        while queue:
            event = queue.popleft()

            for handler in list(self._subscribers.get(event.event_type, [])):
                try:
                    # ALWAYS pass Event object
                    handler.handle(event)
                except Exception:
                    continue
