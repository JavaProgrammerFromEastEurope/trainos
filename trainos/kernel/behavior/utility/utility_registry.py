from __future__ import annotations

from .utility_function import (
    UtilityFunction,
)


class UtilityRegistry:

    def __init__(
        self,
    ) -> None:
        self._functions: dict[str, UtilityFunction] = {}

    def register(
        self,
        name: str,
        function: UtilityFunction,
    ) -> None:
        self._functions[name] = function

    def get(
        self,
        name: str,
    ) -> UtilityFunction | None:
        return self._functions.get(name)
