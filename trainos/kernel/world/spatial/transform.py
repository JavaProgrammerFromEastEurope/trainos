from dataclasses import dataclass

from .vector3 import Vector3
from .rotation import Rotation
from .scale import Scale


@dataclass
class Transform:

    position: Vector3
    rotation: Rotation
    scale: Scale
