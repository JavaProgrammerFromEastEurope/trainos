from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable

from .command_event import CommandEvent
from .event_type import CommandEventType

EventHandler = Callable[[CommandEvent], None]


class EventDispatcher:
    """Synchronous event fan-out; observer failures never block other observers.

    Failures are retained in ``last_errors`` for diagnostics. Event delivery is
    best-effort and does not roll back the event already recorded by the service.
    """

    def __init__(self) -> None:
        self._handlers: dict[CommandEventType, list[EventHandler]] = defaultdict(list)
        self._last_errors: tuple[tuple[EventHandler, Exception], ...] = ()

    @property
    def last_errors(self) -> tuple[tuple[EventHandler, Exception], ...]:
        return self._last_errors

    def subscribe(self, event_type: CommandEventType, handler: EventHandler) -> None:
        if not isinstance(event_type, CommandEventType):
            raise TypeError("event_type must be a CommandEventType")
        if not callable(handler):
            raise TypeError("handler must be callable")
        handlers = self._handlers[event_type]
        if handler not in handlers:
            handlers.append(handler)

    def unsubscribe(self, event_type: CommandEventType, handler: EventHandler) -> None:
        handlers = self._handlers.get(event_type)
        if handlers and handler in handlers:
            handlers.remove(handler)

    def dispatch(self, event: CommandEvent) -> None:
        if not isinstance(event, CommandEvent):
            raise TypeError("event must be a CommandEvent")
        errors: list[tuple[EventHandler, Exception]] = []
        for handler in tuple(self._handlers.get(event.event_type, ())):
            try:
                handler(event)
            except Exception as exc:
                errors.append((handler, exc))
        self._last_errors = tuple(errors)
