from trainos.ecs.component import SpatialComponent, StatusComponent


class OccupancySystem:

    def __init__(self, world):
        self.world = world

    def update(self, entity_manager, telemetry):
        spatials = entity_manager.get_components(SpatialComponent)
        statuses = entity_manager.get_components(StatusComponent)
        self._clear_occupancy()

        for entity_id, spatial in spatials.items():
            status = statuses.get(entity_id)

            if not status:
                continue

            if not status.active:
                continue

            wagon = self.world.get_wagon(spatial.wagon_id)

            if not wagon:
                continue

            sector = wagon.sectors.get(spatial.sector_id)

            if not sector:
                continue

            cell = sector.get_cell(spatial.cell_x, spatial.cell_y)

            if not cell:
                continue

            cell.occupied = True
            cell.occupant_id = entity_id

    def _clear_occupancy(self):
        for wagon in self.world.wagons.values():
            for sector in wagon.sectors.values():
                for cell in sector.cells.values():
                    cell.occupied 	= False
                    cell.occupant_id = None
