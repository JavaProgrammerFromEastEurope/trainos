from __future__ import annotations

from .utility_evaluator import (
    UtilityEvaluator,
)


class UtilityRuntime:

    def __init__(
        self,
    ) -> None:
        self.evaluator = UtilityEvaluator()
