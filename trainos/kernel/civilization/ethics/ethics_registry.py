from __future__ import annotations

from .ethics import Ethics


class EthicsRegistry:

    def __init__(self) -> None:
        self._ethics: list[Ethics] = []

    def add(self, ethics: Ethics) -> None:
        self._ethics.append(ethics)

    def ethics(self) -> tuple[Ethics, ...]:
        return tuple(self._ethics)
