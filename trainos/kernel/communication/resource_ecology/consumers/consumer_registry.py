from __future__ import annotations

from .consumer import Consumer


class ConsumerRegistry:

    def __init__(self) -> None:
        self._consumers: list[Consumer] = []

    def register(self, consumer: Consumer) -> None:
        self._consumers.append(consumer)

    def consumers(self) -> tuple[Consumer, ...]:
        return tuple(self._consumers)
