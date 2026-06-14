from __future__ import annotations

from trainos.kernel.world.entities.entity import (
    Entity,
)


class SpatialQuery:

    def __init__(self):
        self.radius: float = 0.0
        self.center = None
        self.result: list[Entity] = []
