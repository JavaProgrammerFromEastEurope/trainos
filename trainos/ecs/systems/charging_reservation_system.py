from trainos.ecs.component import (
    BatteryComponent,
    SpatialComponent,
    ChargingStationComponent,
    NavigationComponent,
    StatusComponent,
)


class ChargingReservationSystem:

    def update(self, entity_manager, telemetry):
        batteries 	= entity_manager.get_components(BatteryComponent)
        spatials 		= entity_manager.get_components(SpatialComponent)
        stations 		= entity_manager.get_components(ChargingStationComponent)
        navigations = entity_manager.get_components(NavigationComponent)
        statuses 		= entity_manager.get_components(StatusComponent)
        #
        # CLEAN INVALID RESERVATIONS (IMPORTANT FIX)
        #
        for station in stations.values():
            if station.reserved_by is None:
                continue
            reserved_entity = statuses.get(station.reserved_by)
            if not reserved_entity or not reserved_entity.active:
                station.reserved_by = None
                station.occupied = False
        #
        # MAIN LOOP
        #
        for entity_id, battery in batteries.items():
            if not battery.seeking_charge:
                continue
            status 			= statuses.get(entity_id)
            spatial 		= spatials.get(entity_id)
            navigation 	= navigations.get(entity_id)
            if not status or not spatial or not navigation:
                continue
            if not status.active:
                continue
            #
            # CHECK IF ALREADY HAS RESERVATION
            #
            already_reserved = False
            for station in stations.values():
                if station.reserved_by == entity_id:
                    already_reserved = True
                    break
            if already_reserved:
                continue
            #
            # FIND BEST STATION
            #
            best_station = None
            best_distance = float("inf")
            for station_entity, station in stations.items():
                if station.occupied:
                    continue
                if station.reserved_by is not None:
                    continue
                station_spatial = spatials.get(station_entity)
                if not station_spatial:
                    continue
                distance = abs(spatial.cell_x - station_spatial.cell_x) + abs(
                    spatial.cell_y - station_spatial.cell_y
                )
                if distance < best_distance:
                    best_distance = distance
                    best_station = (station_entity, station, station_spatial)
            if not best_station:
                continue
            station_entity, station, station_spatial = best_station
            #
            # RESERVE STATION
            #
            station.reserved_by = entity_id
            navigation.target_x = station_spatial.cell_x
            navigation.target_y = station_spatial.cell_y
            navigation.dirty = True
            telemetry.log(
                f"Entity {entity_id} reserved charging station {station_entity}"
            )
