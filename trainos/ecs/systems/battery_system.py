from trainos.ecs.component import BatteryComponent, VelocityComponent, StatusComponent


class BatterySystem:

    def update(self, entity_manager, telemetry):
        batteries = entity_manager.get_components(BatteryComponent)
        velocities = entity_manager.get_components(VelocityComponent)
        statuses = entity_manager.get_components(StatusComponent)

        for entity_id, battery in batteries.items():
            velocity = velocities.get(entity_id)
            status = statuses.get(entity_id)

            if not velocity:
                continue

            if not status:
                continue

            if not status.active:
                continue
            #
            # PASSIVE DRAIN
            #
            battery.level -= battery.drain_rate
            #
            # MOVEMENT DRAIN
            #
            moving = velocity.dx != 0 or velocity.dy != 0
            if moving:
                battery.level -= battery.drain_rate * 2.0
            #
            # CLAMP MINIMUM
            #
            if battery.level < 0:
                battery.level = 0
            #
            # CRITICAL BATTERY
            #
            critical_level = battery.max_level * 0.15
            if battery.level <= critical_level:
                telemetry.log(f"Entity {entity_id} " f"battery critical")
            #
            # BATTERY DEPLETED
            #
            if battery.level <= 0:
                status.active = False
                telemetry.log(f"Entity {entity_id} " f"battery depleted")
            #
            # CHARGING
            #
            if battery.charging:
                battery.level += 1.5
                if battery.level >= battery.max_level:
                    battery.level = battery.max_level
                    battery.charging = False
                    battery.seeking_charge = False
                    battery.reserved_station = None
                    telemetry.log(f"Entity {entity_id} " f"fully charged")
            #
            # BATTERY METRICS
            #
            telemetry.metric(f"entity.{entity_id}.battery", round(battery.level, 2))
            telemetry.metric(
                f"entity.{entity_id}.battery_percent",
                round((battery.level / battery.max_level) * 100, 2),
            )
