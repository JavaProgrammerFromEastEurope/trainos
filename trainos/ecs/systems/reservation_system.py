from trainos.ecs.component import SpatialComponent, VelocityComponent, StatusComponent


class ReservationSystem:

    def __init__(self, world):
        self.world = world

    def update(self, entity_manager, telemetry):
        spatials 		= entity_manager.get_components(SpatialComponent)
        velocities 	= entity_manager.get_components(VelocityComponent)
        statuses 		= entity_manager.get_components(StatusComponent)
        self._clear_reservations()

        for entity_id, spatial in spatials.items():
            velocity 	= velocities.get(entity_id)
            status 		= statuses.get(entity_id)
            if not velocity:
                continue
            if not status:
                continue
            if not status.active:
                continue
            target_x = spatial.cell_x + int(velocity.dx)
            target_y = spatial.cell_y + int(velocity.dy)
            wagon = self.world.get_wagon(spatial.wagon_id)
            if not wagon:
                continue
            sector = wagon.sectors.get(spatial.sector_id)
            if not sector:
                continue
            target_cell = sector.get_cell(target_x, target_y)
            if not target_cell:
                continue
            if target_cell.reserved:
                velocity.dx = 0
                velocity.dy = 0
                telemetry.log(
                    f"Entity {entity_id} " f"waiting for cell " f"{target_x},{target_y}"
                )
                continue
            target_cell.reserved = True
            target_cell.reserved_by = entity_id

    def _clear_reservations(self):
        for wagon in self.world.wagons.values():
            for sector in wagon.sectors.values():
                for cell in sector.cells.values():
                    cell.reserved = False
                    cell.reserved_by = None
