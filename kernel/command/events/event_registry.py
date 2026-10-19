from __future__ import annotations

from collections import defaultdict
from .command_event import CommandEvent


class EventRegistry:
    def __init__(self, max_events_per_command: int = 100) -> None:
        if max_events_per_command < 1:
            raise ValueError("max_events_per_command must be positive")

        self._max_events = max_events_per_command
        self._events: dict[str, list[CommandEvent]] = defaultdict(list)

    def register(self, event: CommandEvent) -> None:
        history = self._events[event.command_id]
        history.append(event)

        if len(history) > self._max_events:
            del history[:-self._max_events]

    def get_events(self, command_id: str) -> tuple[CommandEvent, ...]:
        return tuple(self._events.get(command_id, ()))

    def get_latest(self, command_id: str) -> CommandEvent | None:
        history = self._events.get(command_id)
        return history[-1] if history else None

    def clear(self, command_id: str | None = None) -> None:
        if command_id is None:
            self._events.clear()
        else:
            self._events.pop(command_id, None)
