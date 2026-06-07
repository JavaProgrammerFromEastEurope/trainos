class PriorityScheduler:

    def schedule(self, execution_plans):
        execution_plans.sort(
            key=lambda p: self._score(p),
            reverse=True,
        )
        return execution_plans

    def _score(self, plan):
        base = len(plan["entities"])
        urgency = plan["task"].get("priority", 50)
        return base + urgency

