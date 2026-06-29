from __future__ import annotations

from .arbitration_result import ArbitrationResult


class ArbitrationRegistry:

    def __init__(self) -> None:
        self._results: list[ArbitrationResult] = []

    def register(self, result: ArbitrationResult) -> None:
        self._results.append(result)

    def results(self) -> tuple[ArbitrationResult, ...]:
        return tuple(self._results)
