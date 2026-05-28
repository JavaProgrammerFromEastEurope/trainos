from trainos.core.kernel 	import Kernel
from trainos.ecs.roles import DroneRole
from trainos.tasks.task 	import Task
from trainos.world.wagon 	import Wagon
from trainos.world.sector import Sector


def build_world(kernel):
    wagon = Wagon(wagon_id="wagon_001")
    reactor_sector = Sector(sector_id="reactor", width=10, height=10)
    reactor_sector.generate()

    # Vertical wall
    for y in range(10):
        reactor_sector.set_wall(5, y)
    # Door opening
    door_cell = reactor_sector.get_cell(5, 5)

    if door_cell:
        door_cell.walkable = True
        door_cell.blocked = False
    wagon.add_sector(reactor_sector)
    kernel.world.add_wagon(wagon)


def main():
    kernel = Kernel()
    build_world(kernel)
    kernel.task_manager.add_task(
    Task(
			task_id="reactor_repair",
			task_type="repair",
			target_wagon="wagon_001",
			target_sector="reactor",
			target_x=8,
			target_y=8,
			priority=20,
			duration=500,
			required_workers=2,
			required_role=DroneRole.ENGINEER
    ))
    kernel.boot()


if __name__ == "__main__":
    main()
