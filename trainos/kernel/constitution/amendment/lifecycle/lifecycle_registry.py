from __future__ import annotations

from .amendment_lifecycle import AmendmentLifecycle


class LifecycleRegistry:

    def __init__(self) -> None:
        self._entries: list[AmendmentLifecycle] = []

    def register(self, lifecycle: AmendmentLifecycle) -> None:
        self._entries.append(lifecycle)

    def entries(self) -> tuple[AmendmentLifecycle, ...]:
        return tuple(self._entries)
