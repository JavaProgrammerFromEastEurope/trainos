from trainos.kernel.evolution.memetics.propagation.propagation_event import PropagationEvent
from trainos.kernel.evolution.memetics.propagation.propagation_registry import PropagationRegistry


def test_propagation_registry_register():

    registry = PropagationRegistry()

    event = PropagationEvent(
        meme="cooperation",
        source="group_a",
        target="group_b",
    )

    registry.register(event)

    assert registry.events() == (event,)