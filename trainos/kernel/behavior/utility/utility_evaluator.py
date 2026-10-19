from __future__ import annotations

from .utility_option import (
    UtilityOption,
)

from .utility_result import (
    UtilityResult,
)


class UtilityEvaluator:

    def evaluate(
        self,
        options: list[UtilityOption],
    ) -> UtilityResult:
        best = max(
            options,
            key=lambda x: x.score,
        )
        return UtilityResult(
            option=best.name,
            score=best.score,
        )
