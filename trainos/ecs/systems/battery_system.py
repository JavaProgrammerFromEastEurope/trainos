from trainos.ecs.component import BatteryComponent, StatusComponent


class BatterySystem:

    def update(self, entity_manager, telemetry):

        batteries 	= entity_manager.get_components(BatteryComponent)
        statuses 		= entity_manager.get_components(StatusComponent)

        for entity_id, battery in batteries.items():

            status = statuses.get(entity_id)

            if not status:
                continue

            if battery.level <= 0:
                status.active = False
                telemetry.log(f"Entity {entity_id} battery depleted")
