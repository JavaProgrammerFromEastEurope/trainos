from global_main.enums.crisis_level import CrisisLevel
from global_main.models.system_state import SystemState


class CrisisManager:

    def evaluate(
        self,
        snapshot: SystemState,
    ) -> CrisisLevel:

        if snapshot.population_alive <= 0:
            return CrisisLevel.EXTINCTION

        if snapshot.oxygen_global < 40:
            return CrisisLevel.CRITICAL

        if snapshot.power_global < 30:
            return CrisisLevel.CRITICAL

        if snapshot.reactor_health < 25:
            return CrisisLevel.CRITICAL

        if snapshot.oxygen_global < 60:
            return CrisisLevel.SERIOUS

        if snapshot.power_global < 60:
            return CrisisLevel.SERIOUS

        if snapshot.oxygen_global < 80:
            return CrisisLevel.WARNING

        return CrisisLevel.NORMAL
