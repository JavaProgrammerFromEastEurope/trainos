from __future__ import annotations

from typing import List

from .decision import Decision
from .decision_context import DecisionContext


class DecisionEngine:

    def analyze(
        self,
        context: DecisionContext,
    ) -> List[Decision]:
        decisions: List[Decision] = []
        # базовая эвристика (Stage 5.1 foundation)
        if len(context.state_snapshot) == 0:
            decisions.append(
                Decision(
                    action="initialize_state",
                    confidence=0.9,
                    payload={},
                )
            )
        if context.metrics.get("error_rate", 0) > 0.5:
            decisions.append(
                Decision(
                    action="trigger_recovery",
                    confidence=0.8,
                    payload={"mode": "safe"},
                )
            )
        return decisions
