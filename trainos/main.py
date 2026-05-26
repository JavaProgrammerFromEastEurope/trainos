from trainos.core.kernel 	import Kernel
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
    wagon.add_sector(reactor_sector)
    kernel.world.add_wagon(wagon)


def main():
    kernel = Kernel()
    build_world(kernel)
    kernel.boot()


if __name__ == "__main__":
    main()
