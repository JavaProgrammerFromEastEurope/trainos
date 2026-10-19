from __future__ import annotations

from .reasoning_result import ReasoningResult


class ReasoningRegistry:

    def __init__(self) -> None:
        self._results: list[ReasoningResult] = []

    def register(self, result: ReasoningResult) -> None:
        self._results.append(result)

    def results(self) -> tuple[ReasoningResult, ...]:
        return tuple(self._results)
