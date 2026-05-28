from trainos.ecs.component import NavigationComponent, SpatialComponent
from trainos.ai.astar import astar


class NavigationSystem:

    def __init__(self, world, occupancy_map):
        self.world 				 = world
        self.occupancy_map = occupancy_map

    def update(self, entity_manager, telemetry):
        navigations = entity_manager.get_components(NavigationComponent)
        spatials 		= entity_manager.get_components(SpatialComponent)

        for entity_id, nav in navigations.items():
            spatial = spatials.get(entity_id)
            if not spatial:
                continue
            #
            # NO TARGET → SKIP
            #
            if nav.target_x is None or nav.target_y is None:
                continue
            current_target = (nav.target_x, nav.target_y)
            #
            # DETECT TARGET CHANGE (IMPORTANT FIX)
            #
            if nav.last_target != current_target:
                nav.dirty = True
                nav.last_target = current_target
                nav.destination_reached = False
            #
            # IF PATH STILL VALID → DO NOT REBUILD
            #
            if nav.path and not nav.dirty:
                continue
            #
            # BUILD PATH ONLY WHEN DIRTY
            #
            start = (spatial.cell_x, spatial.cell_y)
            goal = current_target
            walkable = self.occupancy_map.get_walkable_set(
                spatial.wagon_id,
                spatial.sector_id,
            )
            path = astar.find_path(start, goal, walkable)
            #
            # HANDLE FAILED PATH
            #
            if not path:
                nav.blocked_ticks += 1
                telemetry.log(
                    f"Entity {entity_id} path blocked (tick {nav.blocked_ticks})"
                )
                nav.dirty = False
                continue
            #
            # SUCCESSFUL PATH
            #
            nav.path = path
            nav.dirty = False
            nav.blocked_ticks = 0
            telemetry.log(f"Entity {entity_id} path rebuilt ({len(path)} steps)")
