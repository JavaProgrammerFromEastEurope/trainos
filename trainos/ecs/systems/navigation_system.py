from trainos.ecs.component import NavigationComponent, SpatialComponent
from trainos.ai.astar import astar


class NavigationSystem:

    def __init__(self, world, occupancy_map):
        self.world = world
        self.occupancy_map = occupancy_map

    def update(self, entity_manager, telemetry):

        navigations = entity_manager.get_components(NavigationComponent)
        spatials = entity_manager.get_components(SpatialComponent)

        for entity_id, nav in navigations.items():

            spatial = spatials.get(entity_id)

            if not spatial:
                continue

            # --------------------------------------------------
            # NO TARGET → IDLE
            # --------------------------------------------------
            if nav.target_x is None or nav.target_y is None:
                continue

            current_target = (nav.target_x, nav.target_y)

            # --------------------------------------------------
            # INIT SAFETY FIELDS (FIX #1)
            # --------------------------------------------------
            if not hasattr(nav, "last_target"):
                nav.last_target = None

            if not hasattr(nav, "blocked_ticks"):
                nav.blocked_ticks = 0

            if not hasattr(nav, "destination_reached"):
                nav.destination_reached = False

            if not hasattr(nav, "cooldown"):
                nav.cooldown = 0

            # --------------------------------------------------
            # ALREADY AT TARGET
            # --------------------------------------------------
            if (spatial.cell_x, spatial.cell_y) == current_target:
                nav.path = []
                nav.destination_reached = True
                nav.dirty = False
                nav.blocked_ticks = 0
                continue

            # --------------------------------------------------
            # TARGET CHANGE DETECTION
            # --------------------------------------------------
            if nav.last_target != current_target:
                nav.dirty = True
                nav.last_target = current_target
                nav.destination_reached = False
                nav.cooldown = 0

            # --------------------------------------------------
            # COOLDOWN AFTER FAILURE (FIX #2)
            # --------------------------------------------------
            if nav.cooldown > 0:
                nav.cooldown -= 1
                continue

            # --------------------------------------------------
            # DO NOT REBUILD IF PATH STILL VALID
            # --------------------------------------------------
            if nav.path and not nav.dirty:
                continue

            # --------------------------------------------------
            # BLOCKED PATH BACKOFF
            # --------------------------------------------------
            if nav.blocked_ticks > 3:
                nav.cooldown = 5
                nav.blocked_ticks = 0
                nav.dirty = True

            # --------------------------------------------------
            # PATHFINDING
            # --------------------------------------------------
            start = (spatial.cell_x, spatial.cell_y)
            goal = current_target

            walkable = self.occupancy_map.get_walkable_set(
                spatial.wagon_id,
                spatial.sector_id,
            )
            path = astar.find_path(start, goal, walkable)

            # --------------------------------------------------
            # FAILED PATH
            # --------------------------------------------------
            if not path:
                nav.blocked_ticks += 1
                nav.dirty = False

                telemetry.log(
                    f"Entity {entity_id} path blocked (tick {nav.blocked_ticks})"
                )
                continue

            # --------------------------------------------------
            # SUCCESS PATH
            # --------------------------------------------------
            nav.path = path
            nav.dirty = False
            nav.blocked_ticks = 0
            nav.cooldown = 0
            telemetry.log(f"Entity {entity_id} path rebuilt ({len(path)} steps)")
