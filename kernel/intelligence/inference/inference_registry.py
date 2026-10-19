from __future__ import annotations

from .inference_result import InferenceResult


class InferenceRegistry:

    def __init__(self) -> None:
        self._results: list[InferenceResult] = []

    def register(self, result: InferenceResult) -> None:
        self._results.append(result)

    def results(self) -> tuple[InferenceResult, ...]:
        return tuple(self._results)
