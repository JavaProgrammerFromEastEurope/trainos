from __future__ import annotations

from .rule_set import RuleSet
from .reasoning_context import (
    ReasoningContext,
)
from .reasoning_result import (
    ReasoningResult,
)


class InferenceEngine:

    def infer(
        self,
        context: ReasoningContext,
        rules: RuleSet,
    ) -> ReasoningResult:
        for rule in rules.all():
            if rule.condition in context.state:
                return ReasoningResult(
                    success=True,
                    conclusion=rule.conclusion,
                )

        return ReasoningResult(
            success=False,
            conclusion="",
        )
