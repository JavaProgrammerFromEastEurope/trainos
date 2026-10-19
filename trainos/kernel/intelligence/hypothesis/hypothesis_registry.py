from __future__ import annotations

from .hypothesis import Hypothesis


class HypothesisRegistry:

    def __init__(self) -> None:
        self._hypotheses: list[Hypothesis] = []

    def register(self, hypothesis: Hypothesis) -> None:
        self._hypotheses.append(hypothesis)

    def hypotheses(self) -> tuple[Hypothesis, ...]:
        return tuple(self._hypotheses)
