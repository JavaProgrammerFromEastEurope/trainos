from dataclasses import dataclass

from .component import Component


@dataclass
class SensorComponent(Component):

    radius: float = 10.0
