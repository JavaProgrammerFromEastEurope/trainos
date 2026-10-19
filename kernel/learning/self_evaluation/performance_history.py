from __future__ import annotations

from .performance_score import PerformanceScore


class PerformanceHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[PerformanceScore] = []

    def add(
        self,
        score: PerformanceScore,
    ) -> None:
        self._history.append(score)

    def scores(
        self,
    ) -> tuple[PerformanceScore, ...]:
        return tuple(self._history)
