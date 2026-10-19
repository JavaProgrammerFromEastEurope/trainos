from __future__ import annotations

from typing import Any

from .command_event import CommandEvent
from .event_dispatcher import EventDispatcher
from .event_registry import EventRegistry
from .event_type import CommandEventType


class CommandEventService:
    def __init__(
        self,
        registry: EventRegistry | None = None,
        dispatcher: EventDispatcher | None = None,
    ) -> None:
        self._registry = registry if registry is not None else EventRegistry()
        self._dispatcher = dispatcher if dispatcher is not None else EventDispatcher()

    @property
    def registry(self) -> EventRegistry:
        return self._registry

    @property
    def dispatcher(self) -> EventDispatcher:
        return self._dispatcher

    def publish(
        self,
        command_id: str,
        event_type: CommandEventType,
        payload: dict[str, Any] | None = None,
    ) -> CommandEvent:
        event = CommandEvent.create(
            command_id=command_id,
            event_type=event_type,
            payload=payload,
        )
        self._registry.register(event)
        self._dispatcher.dispatch(event)

        return event
