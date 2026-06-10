from global_main.models.plan_action import PlanAction
from global_main.models.system_state import SystemState


class EmergencyAI:

    def update(
        self,
        snapshot: SystemState,
    ) -> list[PlanAction]:

        actions = []

        if snapshot.oxygen_global < 40:

            actions.append(
                PlanAction(
                    priority=100,
                    source="emergency_ai",
                    action_type="seal_sections",
                )
            )

        if snapshot.power_global < 25:

            actions.append(
                PlanAction(
                    priority=95,
                    source="emergency_ai",
                    action_type="shutdown_noncritical_systems",
                )
            )

        return actions
