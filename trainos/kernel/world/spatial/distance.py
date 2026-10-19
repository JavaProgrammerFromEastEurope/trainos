from math import sqrt

from .vector3 import Vector3


class Distance:

    @staticmethod
    def between(
        a: Vector3,
        b: Vector3,
    ) -> float:
        dx = a.x - b.x
        dy = a.y - b.y
        dz = a.z - b.z
        return sqrt(dx * dx + dy * dy + dz * dz)
