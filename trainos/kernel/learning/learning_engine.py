from __future__ import annotations

from .learning_result import (
    LearningResult,
)


class LearningEngine:

    def train(self, data: list) -> LearningResult:
        return LearningResult(improved=True)
