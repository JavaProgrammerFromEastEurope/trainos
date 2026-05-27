from trainos.ecs.component import (
    BatteryComponent,
    SpatialComponent,
    ChargingStationComponent,
    NavigationComponent,
    StatusComponent,
)


class ChargingReservationSystem:

    def update(self, entity_manager, telemetry):

        batteries = entity_manager.get_components(BatteryComponent)
        spatials 	= entity_manager.get_components(SpatialComponent)
        stations 	= entity_manager.get_components(ChargingStationComponent)
        navigations = entity_manager.get_components(NavigationComponent)
        statuses 	= entity_manager.get_components(StatusComponent)

        for entity_id, battery in batteries.items():
            if not battery.seeking_charge:
                continue
            status 		= statuses.get(entity_id)
            spatial 	= spatials.get(entity_id)
            navigation = navigations.get(entity_id)

            if not status:
                continue

            if not spatial:
                continue

            if not navigation:
                continue

            if not status.active:
                continue

            existing_reservation = None
            for station_entity, station in stations.items():
                if station.reserved_by == entity_id:
                    existing_reservation = station_entity
                    break
            if existing_reservation:
                continue
            best_station = None
            best_distance = 999999
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
            station.reserved_by = entity_id
            navigation.target_x = station_spatial.cell_x
            navigation.target_y = station_spatial.cell_y
            navigation.dirty = True
            telemetry.log(
                f"Entity {entity_id} "
                f"reserved charging "
                f"station "
                f"{station.station_id}"
            )
