from __future__ import annotations

from .social_event import SocialEvent


class SocialHistory:

    def __init__(self) -> None:
        self._events: list[SocialEvent] = []

    def add(self, event: SocialEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[SocialEvent, ...]:
        return tuple(self._events)
