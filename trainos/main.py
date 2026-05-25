from trainos.core.kernel import Kernel

from trainos.modules.energy import EnergyModule
from trainos.modules.drone.drone_module import DroneModule


def main():

    kernel = Kernel()

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
            kernel.telemetry
        )
    )

    kernel.boot()


if __name__ == "__main__":
    main()