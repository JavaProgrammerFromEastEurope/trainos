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
        #
        # CLEAN INVALID STATION STATES
        #
        for station in stations.values():
            # cleanup dead charging entities
            if station.charging_entity is not None:
                status = statuses.get(station.charging_entity)
                if not status or not status.active:
                    station.charging_entity = None
                    station.occupied = False
            # cleanup reservation mismatch
            if station.reserved_by is not None:
                status = statuses.get(station.reserved_by)
                if not status or not status.active:
                    station.reserved_by = None
        #
        # MAIN LOOP
        #
        for entity_id, battery in batteries.items():
            status 	= statuses.get(entity_id)
            spatial = spatials.get(entity_id)
            if not status or not spatial:
                continue
            if not status.active:
                continue
            #
            # CHECK IF THIS ENTITY IS ON A STATION
            #
            for station_entity, station in stations.items():
                station_spatial = spatials.get(station_entity)
                if not station_spatial:
                    continue
                same_position = (
                    spatial.wagon_id == station_spatial.wagon_id
                    and spatial.sector_id == station_spatial.sector_id
                    and spatial.cell_x == station_spatial.cell_x
                    and spatial.cell_y == station_spatial.cell_y
                )
                if not same_position:
                    continue
                #
                # OCCUPY STATION
                #
                if station.charging_entity not in (None, entity_id):
                    # someone else is charging here
                    continue
                station.occupied = True
                station.charging_entity = entity_id
                #
                # START CHARGING
                #
                if not battery.charging:
                    battery.charging = True
                    telemetry.log(f"Entity {entity_id} started charging")
                #
                # CHARGE PROGRESSION
                #
                battery.level += 1.5
                if battery.level >= battery.max_level:
                    battery.level = battery.max_level
                    battery.charging = False
                    battery.seeking_charge = False
                    station.charging_entity = None
                    station.occupied = False
                    telemetry.log(f"Entity {entity_id} fully charged and left station")
                #
                # METRICS
                #
                telemetry.metric(f"entity.{entity_id}.battery", round(battery.level, 2))
                telemetry.metric(
                    f"entity.{entity_id}.battery_percent",
                    round((battery.level / battery.max_level) * 100, 2),
                )
