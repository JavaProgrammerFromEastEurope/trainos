from trainos.core.config import ConfigLoader
from trainos.core.event_bus import EventBus
from trainos.core.module_manager import ModuleManager
from trainos.core.state import SystemState
from trainos.core.telemetry import Telemetry
from trainos.core.persistence import PersistenceManager
from trainos.simulation.simulation_clock import SimulationClock
from trainos.simulation.tick import TickLoop
from trainos.tasks.task_manager import TaskManager
from trainos.world.world_grid import WorldGrid


class Kernel:

    def __init__(self):
        self.world = WorldGrid()
        self.config = ConfigLoader()
        self.clock = SimulationClock(tick_rate=60)
        self.persistence = PersistenceManager()
        self.system_config = self.config.load("system.yaml")
        self.event_bus = EventBus()
        self.modules = ModuleManager()
        self.state = SystemState()
        self.telemetry = Telemetry()
        tick_rate = self.system_config["tick_rate"]
        self.tick = TickLoop(tick_rate)
        self.task_manager = (TaskManager())

    def boot(self):
        self.telemetry.log("Kernel booting")
        self.modules.start_all()
        self.tick.run(self.update)

    def update(self):
        self.clock.step()
        current_tick = self.clock.current_tick()
        self.modules.update_all(current_tick)

    def shutdown(self):
        self.telemetry.log("Kernel shutdown")
        self.tick.stop()
        self.modules.shutdown_all()
