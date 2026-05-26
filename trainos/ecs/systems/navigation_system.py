from trainos.ecs.component import (
    NavigationComponent,
    SpatialComponent,
    VelocityComponent,
    StatusComponent,
)

from trainos.navigation.astar import AStar


class NavigationSystem:

    def __init__(self, world):
        self.world = world

    def update(self, entity_manager, telemetry):
        navigations 	= entity_manager.get_components(NavigationComponent)
        spatials 			= entity_manager.get_components(SpatialComponent)
        velocities 		= entity_manager.get_components(VelocityComponent)
        statuses 			= entity_manager.get_components(StatusComponent)

        for entity_id, navigation in navigations.items():
            spatial 	= spatials.get(entity_id)
            velocity 	= velocities.get(entity_id)
            status 		= statuses.get(entity_id)

            if not spatial:
                continue

            if not velocity:
                continue

            if not status:
                continue

            if not status.active:
                continue

            wagon = self.world.get_wagon(spatial.wagon_id)

            if not wagon:
                telemetry.log(f"Missing wagon " f"{spatial.wagon_id}")
                continue
            sector = wagon.sectors.get(spatial.sector_id)

            if not sector:
                telemetry.log(f"Missing sector " f"{spatial.sector_id}")
                continue
            walkable = set()
            for (cell_x, cell_y), cell in sector.cells.items():
                if cell.walkable and not cell.blocked and not cell.occupied:
                    walkable.add((cell_x, cell_y))
            start 	= (spatial.cell_x, spatial.cell_y)
            goal 		= (navigation.target_x, navigation.target_y)

            if start == goal:
                velocity.dx = 0
                velocity.dy = 0
                continue
            rebuild_required = False

            if navigation.dirty:
                rebuild_required = True
            elif not navigation.path:
                rebuild_required = True
            elif navigation.current_index >= len(navigation.path):
                rebuild_required = True

            if rebuild_required:
                path = AStar.find_path(start=start, goal=goal, walkable=walkable)
                navigation.path = path
                navigation.current_index = 0
                navigation.dirty = False
                telemetry.log(f"Entity {entity_id} " f"rebuilt path")

            if not navigation.path:
                velocity.dx = 0
                velocity.dy = 0
                telemetry.log(f"Entity {entity_id} " f"has empty path")
                continue

            if navigation.current_index >= len(navigation.path):
                velocity.dx = 0
                velocity.dy = 0
                telemetry.log(f"Entity {entity_id} " f"completed path")
                continue
            next_cell = navigation.path[navigation.current_index]

            if start == next_cell:
                navigation.current_index += 1
                if navigation.current_index >= len(navigation.path):
                    velocity.dx = 0
                    velocity.dy = 0
                    telemetry.log(f"Entity {entity_id} " f"reached target")
                    continue
                next_cell = navigation.path[navigation.current_index]

            next_x = next_cell[0]
            next_y = next_cell[1]
            target_cell = sector.get_cell(next_x, next_y)

            if not target_cell:
                navigation.dirty = True
                velocity.dx = 0
                velocity.dy = 0
                telemetry.log(f"Entity {entity_id} " f"invalid target cell")
                continue

            if target_cell.occupied or target_cell.blocked:
                navigation.dirty = True
                velocity.dx = 0
                velocity.dy = 0
                telemetry.log(f"Entity {entity_id} " f"path blocked")
                continue

            dx = next_x - spatial.cell_x
            dy = next_y - spatial.cell_y
            velocity.dx = dx
            velocity.dy = dy

            telemetry.metric(f"entity.{entity_id}.path_index", navigation.current_index)
            telemetry.metric(f"entity.{entity_id}.path_length", len(navigation.path))
            telemetry.metric(f"entity.{entity_id}.target_x", navigation.target_x)
            telemetry.metric(f"entity.{entity_id}.target_y", navigation.target_y)
