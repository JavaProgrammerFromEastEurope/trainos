from abc import ABC, abstractmethod

from trainos.core.event_bus import EventBus
from trainos.core.telemetry import Telemetry


class BaseModule(ABC):

    def __init__(self,
                name: str,
                event_bus: EventBus,
                telemetry: Telemetry):
        self.name = name
        self.event_bus = event_bus
        self.telemetry = telemetry

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass
