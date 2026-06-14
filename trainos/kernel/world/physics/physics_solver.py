from __future__ import annotations

from .rigid_body import (
    RigidBody,
)


class PhysicsSolver:

    def step(
        self,
        body: RigidBody,
        dt: float,
    ) -> None:
        body.velocity.vector.x += body.acceleration.vector.x * dt
        body.velocity.vector.y += body.acceleration.vector.y * dt
        body.velocity.vector.z += body.acceleration.vector.z * dt
