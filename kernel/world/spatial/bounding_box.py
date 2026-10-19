from dataclasses import dataclass

from .vector3 import Vector3


@dataclass
class BoundingBox:

    center: Vector3
    width: 	float
    height: float
    depth: 	float