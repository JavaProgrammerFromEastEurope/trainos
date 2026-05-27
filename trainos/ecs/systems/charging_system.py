from trainos.ecs.component import (
    BatteryComponent,
    SpatialComponent,
    ChargingStationComponent,
    StatusComponent,
)


class ChargingSystem:

    def update(self, entity_manager, telemetry):
        batteries = entity_manager.get_components(BatteryComponent)
        spatials 	= entity_manager.get_components(SpatialComponent)
        stations 	= entity_manager.get_components(ChargingStationComponent)
        statuses 	= entity_manager.get_components(StatusComponent)

        for entity_id, battery in batteries.items():
            status 	= statuses.get(entity_id)
            spatial = spatials.get(entity_id)

            if not status:
                continue

            if not spatial:
                continue

            if not status.active:
                continue

            for station_entity, station in stations.items():
                station_spatial = spatials.get(station_entity)

                if not station_spatial:
                    continue

                same_position = (
                    station_spatial.wagon_id 		== spatial.wagon_id
                    and station_spatial.sector_id == spatial.sector_id
                    and station_spatial.cell_x 	== spatial.cell_x
                    and station_spatial.cell_y 	== spatial.cell_y
                )

                if not same_position:
                    continue

                if not station.occupied or station.charging_entity == entity_id:
                    station.occupied = True
                    station.charging_entity = entity_id

                    if not battery.charging:
                        telemetry.log(f"Entity {entity_id} " f"started charging")
                    battery.charging = True

                    if battery.current_energy >= battery.max_energy:
                        station.occupied = False
                        station.charging_entity = None
                        battery.charging = False
                        telemetry.log(f"Entity {entity_id} " f"left charging station")
