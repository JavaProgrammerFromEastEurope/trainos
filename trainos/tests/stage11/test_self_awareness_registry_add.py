from kernel.metacivilization.self_awareness.self_awareness import SelfAwareness
from kernel.metacivilization.self_awareness.awareness_level import AwarenessLevel
from kernel.metacivilization.self_awareness.self_awareness_registry import SelfAwarenessRegistry


def test_self_awareness_registry_add():

    registry = SelfAwarenessRegistry()

    awareness = SelfAwareness(
        level=AwarenessLevel.NORMAL,
    )

    registry.add(awareness)

    assert registry.awareness() == (awareness,)