from __future__ import annotations

from .gravity import Gravity
from .physics_state import PhysicsState


class PhysicsService:

    def __init__(
        self,
    ) -> None:
        self._state = PhysicsState(
            gravity=Gravity(),
        )

    @property
    def state(
        self,
    ) -> PhysicsState:
        return self._state
