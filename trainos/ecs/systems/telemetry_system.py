from trainos.ecs.component import PositionComponent, BatteryComponent, DroneComponent


class TelemetrySystem:

    def update(self, entity_manager, telemetry):

        positions = entity_manager.get_components(PositionComponent)

        batteries = entity_manager.get_components(BatteryComponent)

        drones 		= entity_manager.get_components(DroneComponent)

        for entity_id, drone in drones.items():

            position 	= positions.get(entity_id)

            battery 	= batteries.get(entity_id)

            if not position:
                continue

            if not battery:
                continue

            print(
                f"[DRONE] "
                f"{drone.drone_id} "
                f"POS=({position.x}, {position.y}) "
                f"BAT={battery.level}"
            )
