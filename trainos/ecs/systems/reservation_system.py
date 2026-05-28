from trainos.ecs.component import (
    SpatialComponent,
    VelocityComponent,
    StatusComponent,
    NavigationComponent,
)


class ReservationSystem:

    def __init__(self, world):
        self.world = world

    def update(self, entity_manager, telemetry):

        spatials 		= entity_manager.get_components(SpatialComponent)
        velocities 	= entity_manager.get_components(VelocityComponent)
        statuses 		= entity_manager.get_components(StatusComponent)
        navigations = entity_manager.get_components(NavigationComponent)

        # --------------------------------------------------
        # STEP 1: RESET OLD RESERVATIONS (SAFE RESET ONLY)
        # --------------------------------------------------
        self._clear_reservations()

        # --------------------------------------------------
        # STEP 2: BUILD NEW RESERVATIONS FROM NAVIGATION
        # --------------------------------------------------
        reserved_cells = set()

        for entity_id, nav in navigations.items():

            spatial = spatials.get(entity_id)
            status = statuses.get(entity_id)

            if not spatial or not status:
                continue

            if not status.active:
                continue

            # --------------------------------------------------
            # USE PATH NOT VELOCITY (CRITICAL FIX)
            # --------------------------------------------------
            if not nav.path:
                continue

            next_cell = nav.path[0]
            target_x, target_y = next_cell

            wagon = self.world.wagons.get(spatial.wagon_id)
            if not wagon:
                continue

            sector = wagon.sectors.get(spatial.sector_id)
            if not sector:
                continue

            target_cell = sector.get_cell(target_x, target_y)
            if not target_cell:
                continue

            # --------------------------------------------------
            # PREVENT DOUBLE RESERVATION IN SAME TICK
            # --------------------------------------------------
            cell_key = (spatial.wagon_id, spatial.sector_id, target_x, target_y)
            if cell_key in reserved_cells:
                continue
            # --------------------------------------------------
            # BLOCKING LOGIC
            # --------------------------------------------------
            if target_cell.reserved and target_cell.reserved_by != entity_id:
                # cancel movement intent (NOT velocity anymore)
                nav.blocked_ticks += 1
                telemetry.log(
                    f"Entity {entity_id} waiting for cell {target_x},{target_y}"
                )
                continue

            # --------------------------------------------------
            # RESERVE CELL
            # --------------------------------------------------
            target_cell.reserved = True
            target_cell.reserved_by = entity_id
            reserved_cells.add(cell_key)

    # --------------------------------------------------
    # SAFE RESET (DO NOT BREAK CURRENT TICK CONSISTENCY)
    # --------------------------------------------------
    def _clear_reservations(self):

        for wagon in self.world.wagons.values():
            for sector in wagon.sectors.values():

                if hasattr(sector, "reset_reservations"):
                    sector.reset_reservations()
                    continue

                for cell in sector.cells.values():
                    cell.reserved = False
                    cell.reserved_by = None
