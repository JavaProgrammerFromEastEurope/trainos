from __future__ import annotations

from .modification_event import ModificationEvent


class ModificationRegistry:

    def __init__(self) -> None:
        self._mods: list[ModificationEvent] = []

    def register(self, event: ModificationEvent) -> None:
        self._mods.append(event)

    def all(self) -> tuple[ModificationEvent, ...]:
        return tuple(self._mods)
