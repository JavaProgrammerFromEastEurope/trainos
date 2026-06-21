from __future__ import annotations

from .value import Value


class ValueRegistry:

    def __init__(self) -> None:
        self._values: list[Value] = []

    def add(self, value: Value) -> None:
        self._values.append(value)

    def values(self) -> tuple[Value, ...]:
        return tuple(self._values)
