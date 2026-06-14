from dataclasses import dataclass

from .component import Component


@dataclass
class PositionComponent(Component):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0