from __future__ import annotations

from .inference_engine import (
    InferenceEngine,
)
from .reasoning_context import (
    ReasoningContext,
)
from .reasoning_result import (
    ReasoningResult,
)
from .rule_set import RuleSet


class ReasoningEngine:

    def __init__(self) -> None:
        self._inference = InferenceEngine()
        self._rules = RuleSet()

    @property
    def rules(
        self,
    ) -> RuleSet:
        return self._rules

    def reason(
        self,
        context: ReasoningContext,
    ) -> ReasoningResult:
        return self._inference.infer(
            context,
            self._rules,
        )
