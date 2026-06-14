from dataclasses import dataclass

from .mass import Mass
from .velocity import Velocity
from .acceleration import Acceleration


@dataclass
class RigidBody:

    mass: Mass
    velocity: Velocity
    acceleration: Acceleration
