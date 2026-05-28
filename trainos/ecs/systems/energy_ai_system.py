from trainos.ecs.component import (
    BatteryComponent,
    NavigationComponent,
    SpatialComponent,
    StatusComponent,
    TaskComponent,
    ChargingStationComponent,
)


class EnergyAISystem:

    def update(self, entity_manager, telemetry):
        batteries 			= entity_manager.get_components(BatteryComponent)
        navigations 		= entity_manager.get_components(NavigationComponent)
        spatials 				= entity_manager.get_components(SpatialComponent)
        statuses 				= entity_manager.get_components(StatusComponent)
        task_components = entity_manager.get_components(TaskComponent)
        charging_stations = entity_manager.get_components(ChargingStationComponent)
        #
        # FIND ALL STATIONS
        #
        station_positions = []
        for station_entity_id, station in charging_stations.items():
            station_spatial = spatials.get(station_entity_id)

            if not station_spatial:
                continue
            station_positions.append((station.station_id, station_spatial))
        #
        # PROCESS ENTITIES
        #
        for entity_id, battery in batteries.items():
            navigation = navigations.get(entity_id)
            spatial = spatials.get(entity_id)
            status = statuses.get(entity_id)
            task_component = task_components.get(entity_id)

            if not navigation:
                continue
            if not spatial:
                continue
            if not status:
                continue
            if not task_component:
                continue
            if not status.active:
                continue
            #
            # BATTERY PERCENT
            #
            battery_percent = (battery.level / battery.max_level) * 100
            #
            # ENERGY RECOVERED
            #
            if battery_percent > 35:
                if battery.seeking_charge:
                    battery.seeking_charge = False
                    telemetry.log(f"Entity {entity_id} " f"energy stabilized")
            #
            # LOW ENERGY DECISION
            #
            low_energy = battery_percent <= 25
            if not low_energy:
                continue
            #
            # ALREADY CHARGING
            #
            if battery.charging:
                continue
            #
            # ALREADY SEEKING
            #
            if battery.seeking_charge:
                continue
            #
            # FIND CLOSEST STATION
            #
            closest_station = None
            closest_distance = 999999
            for station_id, station_spatial in station_positions:
                dx = abs(spatial.cell_x - station_spatial.cell_x)
                dy = abs(spatial.cell_y - station_spatial.cell_y)
                distance = dx + dy
                if distance < closest_distance:
                    closest_distance = distance
                    closest_station = station_spatial
                    battery.reserved_station = station_id
            #
            # NO STATION FOUND
            #
            if not closest_station:
                telemetry.log(f"Entity {entity_id} " f"cannot find charging station")
                continue
            #
            # OVERRIDE TASK
            #
            if task_component.current_task_id is not None:
                telemetry.log(f"Entity {entity_id} " f"interrupting task for charging")
                task_component.current_task_id = None
                task_component.executing_task = False
                task_component.cooperative = False
            #
            # SEEK CHARGING
            #
            battery.seeking_charge = True
            navigation.target_x = closest_station.cell_x
            navigation.target_y = closest_station.cell_y
            navigation.dirty = True
            telemetry.log(
                f"Entity {entity_id} "
                f"seeking charging station "
                f"{battery.reserved_station}"
            )
            telemetry.metric(f"entity.{entity_id}.charging", 1)
