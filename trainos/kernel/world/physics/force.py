from dataclasses import dataclass

from trainos.kernel.world.spatial.vector3 import (
    Vector3,
)


@dataclass
class Force:
    vector: Vector3
