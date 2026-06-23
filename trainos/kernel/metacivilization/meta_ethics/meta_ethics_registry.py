from __future__ import annotations

from .meta_ethics import MetaEthics


class MetaEthicsRegistry:

    def __init__(self) -> None:
        self._ethics: list[MetaEthics] = []

    def add(self, ethics: MetaEthics) -> None:
        self._ethics.append(ethics)

    def ethics(self) -> tuple[MetaEthics, ...]:
        return tuple(self._ethics)
