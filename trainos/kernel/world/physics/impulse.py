from dataclasses import dataclass

from kernel.world.spatial.vector3 import (
    Vector3,
)


@dataclass
class Impulse:

    vector: Vector3
