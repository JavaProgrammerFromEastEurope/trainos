from trainos.ecs.component import SpatialComponent, StatusComponent


class OccupancySystem:

    def __init__(self, world):
        self.world = world

    def update(self, entity_manager, telemetry):

        spatials = entity_manager.get_components(SpatialComponent)
        statuses = entity_manager.get_components(StatusComponent)

        # --------------------------------------------------
        # STEP 1: CLEAR ONLY LOCAL GRID STATE (NOT FULL RESET)
        # --------------------------------------------------
        self._reset_occupied_flags()

        # --------------------------------------------------
        # STEP 2: REBUILD OCCUPANCY FROM ACTIVE ENTITIES
        # --------------------------------------------------
        for entity_id, spatial in spatials.items():

            status = statuses.get(entity_id)

            if not status or not status.active:
                continue

            wagon = self.world.wagons.get(spatial.wagon_id)
            if not wagon:
                continue

            sector = wagon.sectors.get(spatial.sector_id)
            if not sector:
                continue

            cell = sector.get_cell(spatial.cell_x, spatial.cell_y)
            if not cell:
                continue

            # --------------------------------------------------
            # IMPORTANT: DO NOT OVERWRITE IF ALREADY SET SAME ENTITY
            # --------------------------------------------------
            if cell.occupied and cell.occupant_id == entity_id:
                continue

            cell.occupied = True
            cell.occupant_id = entity_id

    # --------------------------------------------------
    # FIX: SAFE RESET (ONLY FLAGS, NOT STRUCTURE)
    # --------------------------------------------------
    def _reset_occupied_flags(self):

        for wagon in self.world.wagons.values():
            for sector in wagon.sectors.values():

                # optional fast path if sector supports bulk reset
                if hasattr(sector, "reset_occupancy"):
                    sector.reset_occupancy()
                    continue

                for cell in sector.cells.values():
                    cell.occupied = False
                    cell.occupant_id = None