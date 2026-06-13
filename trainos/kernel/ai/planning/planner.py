from __future__ import annotations

from typing import List

from trainos.kernel.ai.decision.decision import Decision
from .plan import Plan
from .plan_step import PlanStep


class Planner:

    def build(self, decisions: List[Decision]) -> Plan:
        plan = Plan()
        for d in decisions:
            if d.action == "initialize_state":
                plan.add(
                    PlanStep(
                        name="init_state",
                        payload={},
                        depends_on=[],
                    )
                )
            if d.action == "trigger_recovery":
                plan.add(
                    PlanStep(
                        name="safe_recovery",
                        payload={"mode": "safe"},
                        depends_on=["init_state"],
                    )
                )
        return plan
