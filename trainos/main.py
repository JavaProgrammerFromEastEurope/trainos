from trainos.core.kernel import Kernel

from trainos.tasks.task import Task

from trainos.world.wagon import Wagon
from trainos.world.sector import Sector


def build_world(kernel):

    #
    # CREATE WAGON
    #

    wagon = Wagon(wagon_id="wagon_001")

    #
    # CREATE SECTOR
    #

    reactor_sector = Sector(sector_id="reactor", width=10, height=10)

    reactor_sector.generate()

    #
    # WALL
    #

    for y in range(10):

        reactor_sector.set_wall(5, y)

    #
    # DOOR
    #

    door_cell = reactor_sector.get_cell(5, 5)

    if door_cell:

        door_cell.walkable = True

    #
    # REGISTER
    #

    wagon.add_sector(reactor_sector)

    kernel.world.add_wagon(wagon)


def spawn_worker_drones(kernel):

    factory = kernel.entity_factory

    #
    # ENGINEERS
    #

    factory.create_engineer_drone("wagon_001", "reactor", 0, 0)

    factory.create_engineer_drone("wagon_001", "reactor", 1, 0)

    #
    # MINER
    #

    factory.create_miner_drone("wagon_001", "reactor", 2, 0)

    #
    # HAULER
    #

    factory.create_hauler_drone("wagon_001", "reactor", 3, 0)

    #
    # SCOUT
    #

    factory.create_scout_drone("wagon_001", "reactor", 4, 0)

    #
    # CHARGER
    #

    factory.create_charging_station("wagon_001", "reactor", 0, 9)


def create_tasks(kernel):

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

    kernel.task_manager.add_task(repair_task)


def main():

    kernel = Kernel()

    build_world(kernel)

    spawn_worker_drones(kernel)

    create_tasks(kernel)

    kernel.boot()


if __name__ == "__main__":

    main()
