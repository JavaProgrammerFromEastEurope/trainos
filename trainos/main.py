from trainos.core.kernel import Kernel

from trainos.modules.energy import EnergyModule
from trainos.modules.drone.drone_module import DroneModule
from trainos.world.wagon import Wagon
from trainos.world.sector import Sector


def main():

    kernel = Kernel()

    wagon = Wagon(wagon_id="wagon_001")
    reactor_sector = Sector(
      sector_id="reactor",
      width=10, height=10)
    reactor_sector.generate()
    wagon.add_sector(reactor_sector)
    kernel.world.add_wagon(wagon)

    kernel.modules.register(
        EnergyModule(
						kernel.event_bus,
						kernel.telemetry,
						kernel.state,
						kernel.config
					)
    )



    kernel.modules.register(
        DroneModule(
            kernel.event_bus,
            kernel.telemetry,
            kernel.state,
        )
    )

    kernel.boot()


if __name__ == "__main__":
    main()
