from trainos.ecs.component import NavigationComponent, SpatialComponent
from trainos.ai.astar import astar


class NavigationSystem:

    def __init__(self, world, occupancy_map):
        self.world = world
        self.occupancy_map = occupancy_map

    def update(self, entity_manager, telemetry):

        navigations = entity_manager.get_components(NavigationComponent)
        spatials 		= entity_manager.get_components(SpatialComponent)
        for entity_id, nav in navigations.items():
            spatial = spatials.get(entity_id)
            #
            # REQUIRED COMPONENTS
            #
            if not spatial:
                continue
            #
            # NO TARGET
            #

            if nav.target_x is None:
                continue

            if nav.target_y is None:
                continue
            current_target = (
                nav.target_x,
                nav.target_y,
            )
            #
            # ALREADY AT DESTINATION
            #
            if (
                spatial.cell_x,
                spatial.cell_y,
            ) == current_target:
                nav.path.clear()
                nav.destination_reached = True
                nav.dirty = False
                nav.blocked_ticks 	= 0
                nav.cooldown_ticks 	= 0
                continue
            #
            # TARGET CHANGED
            #
            if nav.last_target != current_target:
                nav.last_target = current_target
                nav.destination_reached = False
                nav.dirty = True
                nav.cooldown_ticks = 0
            #
            # COOLDOWN
            #
            if nav.cooldown_ticks > 0:
                nav.cooldown_ticks -= 1
                continue
            #
            # PATH STILL VALID
            #
            if nav.path and not nav.dirty:
                continue
            #
            # REBUILD BACKOFF
            #
            if nav.blocked_ticks >= nav.max_blocked_ticks:
                nav.cooldown_ticks 	= nav.repath_cooldown
                nav.blocked_ticks 	= 0
                telemetry.log(f"Entity {entity_id} navigation cooldown")
                continue
            #
            # WORLD LOOKUP
            #
            wagon = self.world.get_wagon(spatial.wagon_id)
            if not wagon:
                continue
            sector = wagon.sectors.get(spatial.sector_id)
            if not sector:
                continue
            #
            # PATHFINDING
            #
            start = (
                spatial.cell_x,
                spatial.cell_y,
            )
            goal = current_target
            path = astar(
                sector=sector,
                start=start,
                goal=goal,
                occupancy_map=self.occupancy_map,
                ignore_entity=entity_id,
            )
            #
            # FAILED PATH
            #
            if not path:
                nav.blocked_ticks += 1
                nav.dirty = False
                telemetry.log(
                    f"Entity {entity_id} " f"path blocked " f"({nav.blocked_ticks})"
                )
                continue
            #
            # REMOVE CURRENT CELL
            #
            if path and path[0] == start:
                path = path[1:]
            #
            # SUCCESS
            #
            nav.path 	= path
            nav.dirty = False
            nav.blocked_ticks 	= 0
            nav.cooldown_ticks 	= 0
            telemetry.log(
                f"Entity {entity_id} " f"path rebuilt " f"({len(path)} steps)"
            )
