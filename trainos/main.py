from trainos.core.kernel import Kernel
from trainos.tasks.task import Task
from trainos.world.wagons import Wagon
from trainos.world.sectors import Sector


def build_world(kernel):
    #
    # CREATE WAGON
    #
    wagon = Wagon(
        wagon_id="wagon_001",
    )

    #
    # CREATE SECTOR
    #
    reactor_sector = Sector(
        sector_id="reactor",
        width=10,
        height=10,
    )

    reactor_sector.generate()

    #
    # WALL BARRIER
    #
    for y in range(10):

        reactor_sector.set_wall(
            5,
            y,
        )

    #
    # DOOR OPENING
    #
    door_cell = reactor_sector.get_cell(
        5,
        5,
    )

    if door_cell:
        door_cell.walkable = True
    #
    # REGISTER SECTOR
    #
    wagon.add_sector(
        reactor_sector,
    )
    #
    # REGISTER WAGON
    #
    kernel.world.add_wagon(
        wagon,
    )
    kernel.telemetry.log(
        "World generated",
    )


def spawn_worker_drones(kernel):

    factory = kernel.entity_factory
    #
    # ENGINEERS
    #
    factory.create_engineer_drone(
        wagon_id="wagon_001",
        sector_id="reactor",
        x=0,
        y=0,
    )
    factory.create_engineer_drone(
        wagon_id="wagon_001",
        sector_id="reactor",
        x=1,
        y=0,
    )
    #
    # MINER
    #
    factory.create_miner_drone(
        wagon_id="wagon_001",
        sector_id="reactor",
        x=2,
        y=0,
    )
    #
    # HAULER
    #
    factory.create_hauler_drone(
        wagon_id="wagon_001",
        sector_id="reactor",
        x=3,
        y=0,
    )
    #
    # SCOUT
    #
    factory.create_scout_drone(
        wagon_id="wagon_001",
        sector_id="reactor",
        x=4,
        y=0,
    )
    #
    # CHARGING STATIONS
    #
    factory.create_charging_station(
        wagon_id="wagon_001",
        sector_id="reactor",
        x=0,
        y=9,
        station_id="charger_alpha",
    )

    factory.create_charging_station(
        wagon_id="wagon_001",
        sector_id="reactor",
        x=9,
        y=9,
        station_id="charger_beta",
    )


def create_tasks(kernel):
    #
    # COOPERATIVE REPAIR TASK
    #
    repair_task = Task(
        task_id="reactor_repair",
        task_type="repair",
        target_wagon="wagon_001",
        target_sector="reactor",
        target_x=8,
        target_y=8,
        priority=10,
        required_workers=2,
        duration=500,
    )
    kernel.task_manager.add_task(
        repair_task,
    )
    kernel.telemetry.log(
        "Task reactor_repair registered",
    )


def main():
    #
    # CREATE KERNEL
    #
    kernel = Kernel()
    #
    # BUILD WORLD
    #
    build_world(
        kernel,
    )
    #
    # SPAWN ENTITIES
    #
    spawn_worker_drones(
        kernel,
    )
    #
    # REGISTER TASKS
    #
    create_tasks(
        kernel,
    )
    #
    # START SIMULATION
    #
    kernel.boot()


if __name__ == "__main__":
    main()
