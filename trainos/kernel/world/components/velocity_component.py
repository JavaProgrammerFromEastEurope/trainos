from dataclasses import dataclass

from .component import Component


@dataclass
class VelocityComponent(Component):

    vx: float = 0.0
    vy: float = 0.0
    vz: float = 0.0
