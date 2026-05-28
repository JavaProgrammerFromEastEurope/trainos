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

        batteries 	= entity_manager.get_components(BatteryComponent)
        navigations = entity_manager.get_components(NavigationComponent)
        spatials 		= entity_manager.get_components(SpatialComponent)
        statuses 		= entity_manager.get_components(StatusComponent)
        tasks 			= entity_manager.get_components(TaskComponent)
        stations 		= entity_manager.get_components(ChargingStationComponent)

        # -------------------------
        # PREBUILD STATION CACHE
        # -------------------------
        station_cache = []
        for station_id, station in stations.items():
            station_spatial = spatials.get(station_id)
            if not station_spatial:
                continue

            station_cache.append((station_id, station, station_spatial))

        # -------------------------
        # MAIN LOOP
        # -------------------------
        for entity_id, battery in batteries.items():
            navigation 	= navigations.get(entity_id)
            spatial 		= spatials.get(entity_id)
            status 			= statuses.get(entity_id)
            task 				= tasks.get(entity_id)

            if not navigation or not spatial or not status or not task:
                continue

            if not status.active:
                continue

            # -------------------------
            # BATTERY PERCENT
            # -------------------------
            battery_percent = (battery.level / battery.max_level) * 100

            # -------------------------
            # RECOVERY STATE
            # -------------------------
            if battery_percent > 35:
                if battery.seeking_charge:
                    battery.seeking_charge = False
                    battery.reserved_station = None
                    telemetry.log(f"Entity {entity_id} energy stabilized")

            # -------------------------
            # LOW ENERGY CHECK
            # -------------------------
            if battery_percent > 25:
                continue

            # already in charging logic
            if battery.charging:
                continue

            # already assigned → do NOT recalc every tick
            if battery.seeking_charge and battery.reserved_station is not None:
                continue

            # -------------------------
            # FIND BEST STATION
            # -------------------------
            best_station = None
            best_distance = 10**9

            for station_id, station, station_spatial in station_cache:

                if station.occupied:
                    continue

                if station.reserved_by is not None:
                    continue

                dx = spatial.cell_x - station_spatial.cell_x
                dy = spatial.cell_y - station_spatial.cell_y
                dist = abs(dx) + abs(dy)

                if dist < best_distance:
                    best_distance = dist
                    best_station = (station_id, station, station_spatial)

            if not best_station:
                telemetry.log(f"Entity {entity_id} cannot find charging station")
                continue
            station_id, station, station_spatial = best_station

            # -------------------------
            # TASK INTERRUPT (ONCE ONLY)
            # -------------------------
            if task.current_task_id is not None:
                telemetry.log(f"Entity {entity_id} interrupting task for charging")
                task.current_task_id = None
                task.executing_task = False
                task.cooperative = False

            # -------------------------
            # ASSIGN CHARGING GOAL
            # -------------------------
            battery.seeking_charge = True
            battery.reserved_station = station_id
            navigation.target_x = station_spatial.cell_x
            navigation.target_y = station_spatial.cell_y
            
            # IMPORTANT: only mark dirty ONCE
            if not navigation.dirty:
                navigation.dirty = True
            telemetry.log(f"Entity {entity_id} seeking charging station {station_id}")
            telemetry.metric(f"entity.{entity_id}.charging", 1)
