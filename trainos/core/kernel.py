from trainos.core.config import ConfigLoader
from trainos.core.event_bus import EventBus
from trainos.core.module_manager import ModuleManager
from trainos.core.state import SystemState
from trainos.core.telemetry import Telemetry
from trainos.core.persistence import PersistenceManager

from trainos.simulation.tick import TickLoop


class Kernel:

    def __init__(self):

        self.config = ConfigLoader()

        self.persistence = PersistenceManager()

        self.system_config = self.config.load("system.yaml")

        self.event_bus = EventBus()

        self.modules = ModuleManager()

        self.state = SystemState()

        self.telemetry = Telemetry()

        tick_rate = self.system_config["tick_rate"]

        self.tick = TickLoop(tick_rate)

    def boot(self):

        self.telemetry.log("Kernel booting")

        self.modules.start_all()

        self.tick.run(self.update)

    def update(self):

        self.modules.update_all()

        self.persistence.save_world(self.state.export())

    def shutdown(self):

        self.telemetry.log("Kernel shutdown")

        self.tick.stop()

        self.modules.shutdown_all()
