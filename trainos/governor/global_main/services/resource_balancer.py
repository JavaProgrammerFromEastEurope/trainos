from global_main.models.plan_action import PlanAction
from global_main.models.system_state import SystemState


class ResourceBalancer:

    def balance(
        self,
        snapshot: SystemState,
    ) -> list[PlanAction]:

        plans: list[PlanAction] = []

        for wagon_id, oxygen in snapshot.oxygen_per_wagon.items():

            if oxygen >= 70:
                continue

            plans.append(
                PlanAction(
                    priority=70,
                    source="resource_balancer",
                    action_type="increase_oxygen",
                    payload={
                        "wagon_id": wagon_id,
                    },
                )
            )

        return plans
