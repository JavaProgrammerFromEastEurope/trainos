from trainos.ecs.component import BatteryComponent, VelocityComponent, StatusComponent


class BatterySystem:

    def update(self, entity_manager, telemetry):

        batteries 	= entity_manager.get_components(BatteryComponent)
        velocities 	= entity_manager.get_components(VelocityComponent)
        statuses 		= entity_manager.get_components(StatusComponent)

        for entity_id, battery in batteries.items():
            velocity 	= velocities.get(entity_id)
            status 		= statuses.get(entity_id)

            if not velocity:
                continue

            if not status:
                continue

            if not status.active:
                continue

            battery.current_energy -= battery.passive_drain
            moving = velocity.dx != 0 or velocity.dy != 0

            if moving:
                battery.current_energy -= battery.movement_drain

            if battery.current_energy < 0:
                battery.current_energy = 0

            if battery.current_energy <= battery.critical_threshold:
                telemetry.log(f"Entity {entity_id} " f"battery critical")

            if battery.charging:
                battery.current_energy += 1.5
                if battery.current_energy >= battery.max_energy:
                    battery.current_energy = battery.max_energy
                    battery.charging = False
                    telemetry.log(f"Entity {entity_id} " f"fully charged")
            telemetry.metric(
                f"entity.{entity_id}" f".battery", round(battery.current_energy, 2)
            )
