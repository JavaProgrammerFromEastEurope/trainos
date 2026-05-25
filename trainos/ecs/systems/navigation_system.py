from trainos.navigation.astar import AStar
from trainos.ecs.component import (
    NavigationComponent,
    SpatialComponent,
    VelocityComponent,
)

class NavigationSystem:

    def update(self, entity_manager, telemetry):
        navigations = entity_manager.get_components(NavigationComponent)
        spatials 		= entity_manager.get_components(SpatialComponent)
        velocities 	= entity_manager.get_components(VelocityComponent)
        walkable = set()

        for x in range(100):
            for y in range(100):
                walkable.add((x, y))

        for entity_id, nav in navigations.items():
            spatial = spatials.get(entity_id)
            velocity = velocities.get(entity_id)

            if not spatial:
                continue

            if not velocity:
                continue

            start = (spatial.cell_x, spatial.cell_y)
            goal = (nav.target_x, nav.target_y)
            path = AStar.find_path(start, goal, walkable)
            nav.path = path

            if path:
                next_cell = path[0]
                dx = next_cell[0] - spatial.cell_x
                dy = next_cell[1] - spatial.cell_y
                velocity.dx = dx
                velocity.dy = dy
