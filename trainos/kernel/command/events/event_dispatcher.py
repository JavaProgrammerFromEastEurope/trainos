from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable

from .command_event import CommandEvent
from .event_type import CommandEventType


EventHandler = Callable[[CommandEvent], None]


class EventDispatcher:
    def __init__(self) -> None:
        self._handlers: dict[
            CommandEventType,
            list[EventHandler],
        ] = defaultdict(list)

    def subscribe(
        self,
        event_type: CommandEventType,
        handler: EventHandler,
    ) -> None:
        handlers = self._handlers[event_type]
        if handler not in handlers:
            handlers.append(handler)

    def unsubscribe(
        self,
        event_type: CommandEventType,
        handler: EventHandler,
    ) -> None:
        handlers = self._handlers.get(event_type)
        if handlers and handler in handlers:
            handlers.remove(handler)

    def dispatch(self, event: CommandEvent) -> None:
        handlers = tuple(self._handlers.get(event.event_type, ()))
        for handler in handlers:
            handler(event)
