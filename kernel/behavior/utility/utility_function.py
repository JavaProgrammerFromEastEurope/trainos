from __future__ import annotations

from .utility_context import (
    UtilityContext,
)

from .utility_score import (
    UtilityScore,
)


class UtilityFunction:

    def evaluate(
        self,
        context: UtilityContext,
    ) -> UtilityScore:
        return UtilityScore(
            value=0.0,
        )
