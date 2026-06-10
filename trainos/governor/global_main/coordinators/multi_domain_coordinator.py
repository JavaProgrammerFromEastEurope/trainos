from global_main.models.plan_action import PlanAction


class MultiDomainCoordinator:

    def coordinate(
        self,
        plans: list[PlanAction],
    ) -> list[PlanAction]:

        result = []
        seen = set()
        for plan in plans:
            key = (
                plan.action_type,
                frozenset(plan.payload.items()),
            )
            if key in seen:
                continue
            seen.add(key)
            result.append(plan)
        result.sort(
            key=lambda x: x.priority,
            reverse=True,
        )
        return result
