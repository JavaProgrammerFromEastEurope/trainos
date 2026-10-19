from dataclasses import dataclass

from .simulation_tick import SimulationTick
from .simulation_clock import SimulationClock


@dataclass
class SimulationContext:

    tick: 	SimulationTick
    clock: SimulationClock
