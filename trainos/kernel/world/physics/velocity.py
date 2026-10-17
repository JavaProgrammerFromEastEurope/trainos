from dataclasses import dataclass

from kernel.world.spatial.vector3 import (
    Vector3,
)


@dataclass
class Velocity:
    vector: Vector3
