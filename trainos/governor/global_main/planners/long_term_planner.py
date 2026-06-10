from global_main.models.plan_action import PlanAction
from global_main.models.system_state import SystemState


class LongTermPlanner:

    def plan(
        self,
        snapshot: SystemState,
    ) -> list[PlanAction]:

        plans: list[PlanAction] = []

        if snapshot.reactor_health < 60:

            plans.append(
                PlanAction(
                    priority=80,
                    source="long_term_planner",
                    action_type="schedule_reactor_maintenance",
                )
            )

        if snapshot.food_supply_days < 30:

            plans.append(
                PlanAction(
                    priority=90,
                    source="long_term_planner",
                    action_type="increase_food_production",
                )
            )

        return plans
