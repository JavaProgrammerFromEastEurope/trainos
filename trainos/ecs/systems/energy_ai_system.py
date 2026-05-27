from trainos.ecs.component import (
    BatteryComponent,
    NavigationComponent,
    SpatialComponent,
    ChargingStationComponent,
    StatusComponent,
    TaskComponent,
)


class EnergyAISystem:

    def update(self, entity_manager, telemetry):
        batteries = entity_manager.get_components(BatteryComponent)
        navigations = entity_manager.get_components(NavigationComponent)
        spatials 	= entity_manager.get_components(SpatialComponent)
        stations 	= entity_manager.get_components(ChargingStationComponent)
        statuses 	= entity_manager.get_components(StatusComponent)
        tasks 		= entity_manager.get_components(TaskComponent)

        for entity_id, battery in batteries.items():
            status 		= statuses.get(entity_id)
            navigation = navigations.get(entity_id)
            spatial 	= spatials.get(entity_id)
            task_component = tasks.get(entity_id)

            if not status:
                continue

            if not navigation:
                continue

            if not spatial:
                continue

            if not task_component:
                continue

            if not status.active:
                continue

            if battery.charging:
                continue

            if battery.current_energy > battery.critical_threshold:
                battery.seeking_charge = False
                continue

            battery.seeking_charge = True
            if task_component.current_task_id is not None:
                telemetry.log(
                    f"Entity {entity_id} " f"abandoned task due " f"to low battery"
                )
                task_component.current_task_id = None
            nearest_station = None
            nearest_distance = 999999
            for station_entity, station in stations.items():
                station_spatial = spatials.get(station_entity)
                if not station_spatial:
                    continue
                distance = abs(spatial.cell_x - station_spatial.cell_x) + abs(
                    spatial.cell_y - station_spatial.cell_y
                )
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_station = station_spatial

            if not nearest_station:
                continue

            navigation.target_x = nearest_station.cell_x
            navigation.target_y = nearest_station.cell_y
            navigation.dirty = True
            telemetry.log(f"Entity {entity_id} " f"seeking charging station")
