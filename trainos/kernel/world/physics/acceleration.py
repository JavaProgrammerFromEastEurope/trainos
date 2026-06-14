from dataclasses import dataclass

from trainos.kernel.world.spatial.vector3 import (
    Vector3,
)


@dataclass
class Acceleration:
    vector: Vector3
