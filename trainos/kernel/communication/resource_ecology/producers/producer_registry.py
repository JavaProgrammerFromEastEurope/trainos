from __future__ import annotations

from .producer import (
    Producer,
)


class ProducerRegistry:

    def __init__(self) -> None:
        self._producers: list[Producer] = []

    def register(self, producer: Producer) -> None:
        self._producers.append(producer)

    def producers(self) -> tuple[Producer, ...]:
        return tuple(self._producers)
