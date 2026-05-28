from trainos.ecs.component import BatteryComponent, VelocityComponent, StatusComponent


class BatterySystem:

    def update(self, entity_manager, telemetry):
        batteries 		= entity_manager.get_components(BatteryComponent)
        velocities 		= entity_manager.get_components(VelocityComponent)
        statuses 			= entity_manager.get_components(StatusComponent)

        for entity_id, battery in batteries.items():
            velocity = velocities.get(entity_id)
            status 	= statuses.get(entity_id)
            #
            # SAFETY CHECKS
            #
            if not status:
                continue
            if not status.active:
                continue
            if not velocity:
                continue
            #
            # ENERGY CONSUMPTION
            #
            moving = velocity.dx != 0 or velocity.dy != 0
            # base drain per tick
            drain = battery.consumption_rate
            # movement multiplier
            if moving:
                drain *= 2.0
            battery.level -= drain
            #
            # CLAMP ENERGY
            #
            if battery.level < 0:
                battery.level = 0
            if battery.level > battery.max_level:
                battery.level = battery.max_level
            #
            # CRITICAL STATE
            #
            battery_percent = (battery.level / battery.max_level) * 100
            if battery_percent <= battery.critical_threshold:
                if not battery.seeking_charge:
                    battery.seeking_charge = True
                    telemetry.log(
                        f"Entity {entity_id} battery critical ({battery_percent:.1f}%)"
                    )
            #
            # DEPLETION
            #
            if battery.level <= 0:
                status.active = False
                telemetry.log(f"Entity {entity_id} battery depleted")
                continue
            #
            # CHARGING
            #
            if battery.charging:
                battery.level += 1.5
                if battery.level >= battery.max_level:
                    battery.level = battery.max_level
                    battery.charging = False
                    battery.seeking_charge = False
                    telemetry.log(f"Entity {entity_id} fully charged")
            #
            # RECOVERY FROM CRITICAL
            #
            elif battery_percent > battery.critical_threshold:
                if battery.seeking_charge:
                    battery.seeking_charge = False
                    telemetry.log(f"Entity {entity_id} energy stabilized")
            #
            # METRICS
            #
            telemetry.metric(f"entity.{entity_id}.battery", round(battery.level, 2))
            telemetry.metric(
                f"entity.{entity_id}.battery_percent", round(battery_percent, 2)
            )
