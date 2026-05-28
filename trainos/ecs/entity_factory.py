from trainos.ecs.component import (
    PositionComponent,
    SpatialComponent,
    VelocityComponent,
    NavigationComponent,
    BatteryComponent,
    StatusComponent,
    TaskComponent,
)


class EntityFactory:

    def __init__(self, entity_manager, telemetry=None):

        #
        # ECS
        #

        self.entity_manager = entity_manager

        #
        # LOGGER
        #

        self.telemetry = telemetry

    def create_basic_drone(self, wagon_id, sector_id, x, y):

        #
        # ENTITY
        #

        entity_id = self.entity_manager.create_entity()

        #
        # POSITION
        #

        self.entity_manager.add_component(
            entity_id,
            PositionComponent(
                x=x,
                y=y,
            ),
        )

        #
        # SPATIAL
        #

        self.entity_manager.add_component(
            entity_id,
            SpatialComponent(
                wagon_id=wagon_id,
                sector_id=sector_id,
                cell_x=x,
                cell_y=y,
            ),
        )

        #
        # MOVEMENT
        #

        self.entity_manager.add_component(
            entity_id,
            VelocityComponent(
                dx=0,
                dy=0,
            ),
        )

        #
        # NAVIGATION
        #

        self.entity_manager.add_component(
            entity_id,
            NavigationComponent(
                target_x=None,
                target_y=None,
                path=[],
                dirty=True,
                blocked_ticks=0,
                destination_reached=False,
            ),
        )

        #
        # BATTERY
        #

        self.entity_manager.add_component(
            entity_id,
            BatteryComponent(
                level=100.0,
                max_level=100.0,
                consumption_rate=0.05,
                charging=False,
                critical_threshold=20.0,
                seeking_charge=False,
            ),
        )

        #
        # STATUS
        #

        self.entity_manager.add_component(
            entity_id,
            StatusComponent(
                active=True,
            ),
        )

        #
        # TASKS
        #

        self.entity_manager.add_component(
            entity_id,
            TaskComponent(
                current_task_id=None,
                executing_task=False,
                cooperative=False,
            ),
        )

        return entity_id

    def create_engineer_drone(self, wagon_id, sector_id, x, y):

        entity_id = self.create_basic_drone(
            wagon_id,
            sector_id,
            x,
            y,
        )

        #
        # ENGINEERS SUPPORT COOP
        #

        task_component = self.entity_manager.get_component(
            entity_id,
            TaskComponent,
        )

        if task_component:

            task_component.cooperative = True

        if self.telemetry:

            self.telemetry.log(f"Spawned ENGINEER drone {entity_id}")

        return entity_id

    def create_miner_drone(self, wagon_id, sector_id, x, y):

        entity_id = self.create_basic_drone(
            wagon_id,
            sector_id,
            x,
            y,
        )

        battery = self.entity_manager.get_component(
            entity_id,
            BatteryComponent,
        )

        if battery:

            battery.max_level = 150.0
            battery.level = 150.0
            battery.consumption_rate = 0.03

        if self.telemetry:

            self.telemetry.log(f"Spawned MINER drone {entity_id}")

        return entity_id

    def create_hauler_drone(self, wagon_id, sector_id, x, y):

        entity_id = self.create_basic_drone(
            wagon_id,
            sector_id,
            x,
            y,
        )

        battery = self.entity_manager.get_component(
            entity_id,
            BatteryComponent,
        )

        if battery:

            battery.max_level = 180.0
            battery.level = 180.0
            battery.consumption_rate = 0.02

        if self.telemetry:

            self.telemetry.log(f"Spawned HAULER drone {entity_id}")

        return entity_id

    def create_scout_drone(self, wagon_id, sector_id, x, y):

        entity_id = self.create_basic_drone(
            wagon_id,
            sector_id,
            x,
            y,
        )

        battery = self.entity_manager.get_component(
            entity_id,
            BatteryComponent,
        )

        if battery:

            battery.consumption_rate = 0.08

        if self.telemetry:

            self.telemetry.log(f"Spawned SCOUT drone {entity_id}")

        return entity_id

    def create_charging_station(self, wagon_id, sector_id, x, y):

        entity_id = self.entity_manager.create_entity()

        #
        # POSITION
        #

        self.entity_manager.add_component(
            entity_id,
            PositionComponent(
                x=x,
                y=y,
            ),
        )

        #
        # SPATIAL
        #

        self.entity_manager.add_component(
            entity_id,
            SpatialComponent(
                wagon_id=wagon_id,
                sector_id=sector_id,
                cell_x=x,
                cell_y=y,
            ),
        )

        #
        # STATUS
        #

        self.entity_manager.add_component(
            entity_id,
            StatusComponent(
                active=True,
            ),
        )

        if self.telemetry:

            self.telemetry.log(f"Spawned charging station {entity_id}")

        return entity_id
