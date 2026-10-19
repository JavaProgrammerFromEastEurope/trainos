from dataclasses import dataclass

from kernel.simulation.clock.simulation_clock 				import SimulationClock
from kernel.simulation.scheduler.simulation_scheduler import SimulationScheduler


@dataclass(slots=True)
class RuntimeContext:

    clock: SimulationClock
    scheduler: SimulationScheduler
