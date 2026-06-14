from trainos.kernel.world.physics.physics_service import (
    PhysicsService,
)

from trainos.kernel.world.physics.gravity import (
    Gravity,
)


def test_physics():

    service = PhysicsService()

    assert service.state is not None
    assert service.state.gravity is not None
    assert isinstance(service.state.gravity, Gravity)
