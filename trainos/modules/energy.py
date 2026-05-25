from trainos.core import state
from trainos.core.module import BaseModule
from trainos.core.events import Event


class EnergyModule(BaseModule):

    def __init__(self, event_bus, telemetry, state, config):
        super().__init__("energy", event_bus, telemetry, state)

        self.config = config.load("energy.yaml")

        self.energy = self.config["initial_energy"]

        self.consumption = self.config["consumption_per_tick"]

        self.critical_threshold = self.config["critical_threshold"]

    def start(self):

        self.telemetry.log("Energy module started")

    def update(self, current_tick):

        self.energy -= self.consumption

        self.telemetry.metric("energy.level", self.energy)

        self.state.set("energy.level", self.energy)

        if self.energy < self.critical_threshold:
            self.event_bus.publish(
                Event(type="LOW_ENERGY", payload={"energy": self.energy})
            )

    def shutdown(self):
        self.telemetry.log("Energy module shutdown")
