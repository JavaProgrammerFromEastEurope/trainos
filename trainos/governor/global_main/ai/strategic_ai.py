from global_main.models.plan_action import PlanAction
from global_main.models.system_state import SystemState
from global_main.planners.long_term_planner import LongTermPlanner
from global_main.services.resource_balancer import ResourceBalancer


class StrategicAI:

    def __init__(
        self,
        long_term_planner: LongTermPlanner,
        resource_balancer: ResourceBalancer,
    ):
        self.long_term_planner = long_term_planner
        self.resource_balancer = resource_balancer

    def update(
        self,
        snapshot: SystemState,
    ) -> list[PlanAction]:
        plans = []
        plans.extend(self.long_term_planner.plan(snapshot))
        plans.extend(self.resource_balancer.balance(snapshot))
        return plans
