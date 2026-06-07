from governor.goals.contain_leak_goal import ContainLeakGoal
from governor.goals.evacuate_sector_goal import EvacuateSectorGoal
from governor.goals.increase_oxygen_goal import IncreaseOxygenGoal
from governor.goals.repair_generator_goal import RepairGeneratorGoal


class AtmospherePlanner:
    CRITICAL_OXYGEN = 70
    WARNING_OXYGEN = 85

    def __init__(self):
        pass

    def build_goals(
        self,
        snapshot,
        leaks,
        forecasts,
        pressures,
    ):
        goals = []
        goals.extend(self._create_leak_goals(leaks))
        goals.extend(self._create_oxygen_goals(snapshot))
        goals.extend(self._create_forecast_goals(forecasts))
        goals.extend(self._create_evacuation_goals(snapshot))
        goals.sort(
            key=lambda g: g.priority,
            reverse=True,
        )
        return goals

    def _create_leak_goals(
        self,
        leaks,
    ):
        goals = []
        for leak in leaks:
            goals.append(
                ContainLeakGoal(
                    priority=95,
                    sector_id=leak.sector_id,
                    leak_rate=leak.leak_rate,
                )
            )
        return goals

    def _create_oxygen_goals(
        self,
        snapshot,
    ):
        goals = []
        for sector in snapshot.sectors.values():
            if sector.oxygen >= self.WARNING_OXYGEN:
                continue
            deficit = self.WARNING_OXYGEN - sector.oxygen
            goals.append(
                IncreaseOxygenGoal(
                    priority=70,
                    sector_id=sector.sector_id,
                    deficit=deficit,
                )
            )
        return goals

    def _create_forecast_goals(
        self,
        forecasts,
    ):
        goals = []
        for forecast in forecasts.values():
            if forecast.time_to_critical > 60:
                continue
            goals.append(
                IncreaseOxygenGoal(
                    priority=80,
                    sector_id=forecast.sector_id,
                    deficit=20,
                )
            )
        return goals

    def _create_evacuation_goals(
        self,
        snapshot,
    ):
        goals = []
        for sector in snapshot.sectors.values():
            if sector.oxygen > self.CRITICAL_OXYGEN:
                continue
            goals.append(
                EvacuateSectorGoal(
                    priority=100,
                    source_sector=sector.sector_id,
                    target_sectors=[],
                    population=sector.population,
                )
            )
        return goals

    def _create_leak_goals(self, leaks):
        goals = []
        for leak in leaks:
            if not self.registry.can_create(
                "LEAK",
                leak.sector_id,
            ):
                continue
            if self.anomaly.is_hotspot(leak.sector_id):
                priority = 120  # escalate
            else:
                priority = 95
            goals.append(
                ContainLeakGoal(
                    priority=priority,
                    sector_id=leak.sector_id,
                    leak_rate=leak.leak_rate,
                )
            )
            self.registry.register(
                "LEAK",
                leak.sector_id,
            )
        return goals
