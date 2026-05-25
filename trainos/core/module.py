from abc import ABC, abstractmethod

from trainos.core.event_bus import EventBus
from trainos.core.telemetry import Telemetry
from trainos.core.state import SystemState


class BaseModule(ABC):

    def __init__(
        self,
        name: str,
        event_bus: EventBus,
        telemetry: Telemetry,
        state: SystemState
    ):

        self.name = name

        self.event_bus = event_bus

        self.telemetry = telemetry

        self.state = state

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass