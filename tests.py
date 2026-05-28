def _spawn_test_drones(self):
    #
    # ENGINEER DRONE
    #
    engineer_id = self.entities.create_entity()
    self.entities.add_component(
        engineer_id,
        SpatialComponent(wagon_id="wagon_001", sector_id="reactor", cell_x=1, cell_y=1),
    )
    self.entities.add_component(engineer_id, VelocityComponent())
    self.entities.add_component(engineer_id, NavigationComponent())
    self.entities.add_component(engineer_id, StatusComponent(active=True))
    self.entities.add_component(engineer_id, TaskComponent())
    self.entities.add_component(
        engineer_id, BatteryComponent(level=100.0, max_level=100.0, drain_rate=0.05)
    )
    self.entities.add_component(
        engineer_id, RoleComponent(role=DroneRole.ENGINEER, efficiency=1.5)
    )
    self.telemetry.log(f"Spawned ENGINEER drone " f"{engineer_id}")
    #
    # SECOND ENGINEER DRONE
    #
    engineer2_id = self.entities.create_entity()
    self.entities.add_component(
        engineer2_id,
        SpatialComponent(wagon_id="wagon_001", sector_id="reactor", cell_x=2, cell_y=1),
    )
    self.entities.add_component(engineer2_id, VelocityComponent())
    self.entities.add_component(engineer2_id, NavigationComponent())
    self.entities.add_component(engineer2_id, StatusComponent(active=True))
    self.entities.add_component(engineer2_id, TaskComponent())
    self.entities.add_component(
        engineer2_id, BatteryComponent(level=100.0, max_level=100.0, drain_rate=0.05)
    )
    self.entities.add_component(
        engineer2_id, RoleComponent(role=DroneRole.ENGINEER, efficiency=1.3)
    )
    self.telemetry.log(f"Spawned ENGINEER drone " f"{engineer2_id}")
    #
    # MINER DRONE
    #
    miner_id = self.entities.create_entity()
    self.entities.add_component(
        miner_id,
        SpatialComponent(wagon_id="wagon_001", sector_id="reactor", cell_x=3, cell_y=1),
    )
    self.entities.add_component(miner_id, VelocityComponent())
    self.entities.add_component(miner_id, NavigationComponent())
    self.entities.add_component(miner_id, StatusComponent(active=True))
    self.entities.add_component(miner_id, TaskComponent())
    self.entities.add_component(
        miner_id, BatteryComponent(level=100.0, max_level=100.0, drain_rate=0.06)
    )
    self.entities.add_component(
        miner_id, RoleComponent(role=DroneRole.MINER, efficiency=1.8)
    )
    self.telemetry.log(f"Spawned MINER drone " f"{miner_id}")
    #
    # HAULER DRONE
    #
    hauler_id = self.entities.create_entity()
    self.entities.add_component(
        hauler_id,
        SpatialComponent(wagon_id="wagon_001", sector_id="reactor", cell_x=4, cell_y=1),
    )
    self.entities.add_component(hauler_id, VelocityComponent())
    self.entities.add_component(hauler_id, NavigationComponent())
    self.entities.add_component(hauler_id, StatusComponent(active=True))
    self.entities.add_component(hauler_id, TaskComponent())
    self.entities.add_component(
        hauler_id, BatteryComponent(level=120.0, max_level=120.0, drain_rate=0.04)
    )
    self.entities.add_component(
        hauler_id, RoleComponent(role=DroneRole.HAULER, efficiency=0.9)
    )
    self.telemetry.log(f"Spawned HAULER drone " f"{hauler_id}")
    #
    # SCOUT DRONE
    #
    scout_id = self.entities.create_entity()
    self.entities.add_component(
        scout_id,
        SpatialComponent(wagon_id="wagon_001", sector_id="reactor", cell_x=5, cell_y=1),
    )
    self.entities.add_component(scout_id, VelocityComponent())
    self.entities.add_component(scout_id, NavigationComponent())
    self.entities.add_component(scout_id, StatusComponent(active=True))
    self.entities.add_component(scout_id, TaskComponent())
    self.entities.add_component(
        scout_id, BatteryComponent(level=80.0, max_level=80.0, drain_rate=0.03)
    )
    self.entities.add_component(
        scout_id, RoleComponent(role=DroneRole.SCOUT, efficiency=2.2)
    )
    self.telemetry.log(f"Spawned SCOUT drone " f"{scout_id}")
