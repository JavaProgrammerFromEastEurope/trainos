from trainos.kernel.metacivilization.self_modification.modification_engine import ModificationEngine
from trainos.kernel.metacivilization.self_modification.modification_event import ModificationEvent


def test_modification_engine_apply():

    engine = ModificationEngine()
    event = ModificationEvent(
        source="emergence",
        target_system="planning",
        change_description="increase depth",
    )
    result = engine.apply(event)

    assert result.change_description == "applied: increase depth"