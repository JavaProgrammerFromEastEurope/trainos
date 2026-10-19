from dataclasses import dataclass

from .gravity import Gravity


@dataclass
class PhysicsState:

    gravity: Gravity
