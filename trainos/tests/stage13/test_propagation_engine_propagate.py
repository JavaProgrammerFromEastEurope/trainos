from trainos.kernel.evolution.memetics.propagation.propagation_engine import PropagationEngine
from trainos.kernel.evolution.memetics.propagation.propagation_event import PropagationEvent


def test_propagation_engine_propagate():

    engine = PropagationEngine()

    event = PropagationEvent(
        meme="cooperation",
        source="a",
        target="b",
    )

    result = engine.propagate(event)

    assert result == event