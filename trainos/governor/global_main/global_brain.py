from global_main.ai.emergency_ai 			import EmergencyAI
from global_main.ai.strategic_ai 			import StrategicAI
from global_main.coordinators.multi_domain_coordinator import (
    MultiDomainCoordinator,
)
from global_main.enums.crisis_level 	import CrisisLevel
from global_main.managers.crisis_manager import CrisisManager
from global_main.models.plan_action 	import PlanAction
from global_main.models.system_state 	import SystemState


class GlobalBrain:

    def __init__(
        self,
        strategic_ai: 	StrategicAI,
        emergency_ai: 	EmergencyAI,
        crisis_manager: CrisisManager,
        coordinator: 		MultiDomainCoordinator,
    ):
        self.strategic_ai = strategic_ai
        self.emergency_ai = emergency_ai
        self.crisis_manager = crisis_manager
        self.coordinator = coordinator

    def update(
        self,
        snapshot: SystemState,
    ) -> list[PlanAction]:
        crisis = self.crisis_manager.evaluate(snapshot)
        if crisis >= CrisisLevel.CRITICAL:
            plans = self.emergency_ai.update(snapshot)
        else:
            plans = self.strategic_ai.update(snapshot)
        return self.coordinator.coordinate(plans)
