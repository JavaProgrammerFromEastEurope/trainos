from global_main.models.system_state import SystemState
from global_main.models.train_health import TrainHealth


class TrainHealthMonitor:

    def compute(
        self,
        snapshot: SystemState,
    ) -> TrainHealth:

        oxygen 	= snapshot.oxygen_global
        power 	= snapshot.power_global
        reactor = snapshot.reactor_health

        food 	= min(snapshot.food_supply_days, 100)
        water = min(snapshot.water_supply_days, 100)

        value = (
            oxygen * 0.30 + power * 0.25 + reactor * 0.15 + food * 0.15 + water * 0.15
        )

        return TrainHealth(
            value	=	max(0.0, min(100.0, value)),
            oxygen_score		=	oxygen,
            power_score			=	power,
            reactor_score		=	reactor,
            food_score			=	food,
            water_score			=	water,
        )
