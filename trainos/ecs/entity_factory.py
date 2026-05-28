from trainos.ecs.component import (
    PositionComponent,
    SpatialComponent,
    VelocityComponent,
    NavigationComponent,
    BatteryComponent,
    StatusComponent,
    TaskComponent,
    DroneComponent,
    ChargingStationComponent,
)


class EntityFactory:

    def __init__(self, entity_manager, telemetry=None):
        #
        # ECS STORAGE
        #
        self.entity_manager = entity_manager
        #
        # OPTIONAL LOGGER
        #
        self.telemetry = telemetry

    #
    # INTERNAL LOGGER
    #
    def _log(self, message):
        if self.telemetry:
            self.telemetry.log(message)

    #
    # CREATE BASE DRONE
    #
    def create_basic_drone(
        self,
        wagon_id,
        sector_id,
        x,
        y,
        role="WORKER",
    ):
        #
        # CREATE ENTITY
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
        # SPATIAL LOCATION
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
        # VELOCITY
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
            NavigationComponent(),
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
                reserved_station=None,
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
        # DRONE METADATA
        #
        self.entity_manager.add_component(
            entity_id,
            DroneComponent(
                drone_id=f"drone_{entity_id}",
                role=role,
                drone_type="GROUND",
                enabled=True,
                state="IDLE",
                cooperative=(role == "ENGINEER"),
            ),
        )
        #
        # TASK STATE
        #
        self.entity_manager.add_component(
            entity_id,
            TaskComponent(
                current_task_id=None,
                executing_task=False,
                cooperative=(role == "ENGINEER"),
            ),
        )
        return entity_id

    #
    # ENGINEER
    #
    def create_engineer_drone(
        self,
        wagon_id,
        sector_id,
        x,
        y,
    ):
        entity_id = self.create_basic_drone(
            wagon_id=wagon_id,
            sector_id=sector_id,
            x=x,
            y=y,
            role="ENGINEER",
        )
        drone = self.entity_manager.get_component(
            entity_id,
            DroneComponent,
        )
        if drone:
            drone.sensor_range = 8
            drone.interaction_range = 2
            drone.priority = 10
        self._log(f"Spawned ENGINEER drone {entity_id}")
        return entity_id

    #
    # MINER
    #
    def create_miner_drone(
        self,
        wagon_id,
        sector_id,
        x,
        y,
    ):
        entity_id = self.create_basic_drone(
            wagon_id=wagon_id,
            sector_id=sector_id,
            x=x,
            y=y,
            role="MINER",
        )
        battery = self.entity_manager.get_component(
            entity_id,
            BatteryComponent,
        )
        drone = self.entity_manager.get_component(
            entity_id,
            DroneComponent,
        )
        if battery:
            battery.max_level = 150.0
            battery.level = 150.0
            battery.consumption_rate = 0.03
        if drone:
            drone.priority = 5
            drone.max_speed = 0.9
        self._log(f"Spawned MINER drone {entity_id}")
        return entity_id

    #
    # HAULER
    #
    def create_hauler_drone(
        self,
        wagon_id,
        sector_id,
        x,
        y,
    ):
        entity_id = self.create_basic_drone(
            wagon_id=wagon_id,
            sector_id=sector_id,
            x=x,
            y=y,
            role="HAULER",
        )
        battery = self.entity_manager.get_component(
            entity_id,
            BatteryComponent,
        )
        drone = self.entity_manager.get_component(
            entity_id,
            DroneComponent,
        )

        if battery:
            battery.max_level = 180.0
            battery.level = 180.0
            battery.consumption_rate = 0.02

        if drone:
            drone.priority = 3
            drone.max_speed = 0.8

        self._log(f"Spawned HAULER drone {entity_id}")
        return entity_id

    #
    # SCOUT
    #
    def create_scout_drone(
        self,
        wagon_id,
        sector_id,
        x,
        y,
    ):
        entity_id = self.create_basic_drone(
            wagon_id=wagon_id,
            sector_id=sector_id,
            x=x,
            y=y,
            role="SCOUT",
        )
        battery = self.entity_manager.get_component(
            entity_id,
            BatteryComponent,
        )
        drone = self.entity_manager.get_component(
            entity_id,
            DroneComponent,
        )
        if battery:
            battery.consumption_rate = 0.08

        if drone:
            drone.max_speed = 1.5
            drone.sensor_range = 12
            drone.priority = 15

        self._log(f"Spawned SCOUT drone {entity_id}")
        return entity_id

    #
    # CHARGING STATION
    #
    def create_charging_station(
        self,
        wagon_id,
        sector_id,
        x,
        y,
        station_id,
    ):
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
        # SPATIAL LOCATION
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
        #
        # CHARGING DATA
        #
        self.entity_manager.add_component(
            entity_id,
            ChargingStationComponent(
                station_id=station_id,
                occupied=False,
                charging_entity=None,
                reserved_by=None,
            ),
        )
        self._log(f"Spawned charging station {entity_id}")
        return entity_id
