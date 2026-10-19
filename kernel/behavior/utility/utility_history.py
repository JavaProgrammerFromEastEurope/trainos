from __future__ import annotations

from .utility_result import (
    UtilityResult,
)


class UtilityHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[UtilityResult] = []

    def add(
        self,
        result: UtilityResult,
    ) -> None:
        self._history.append(
            result,
        )

    def records(
        self,
    ) -> tuple[UtilityResult, ...]:
        return tuple(
            self._history,
        )
