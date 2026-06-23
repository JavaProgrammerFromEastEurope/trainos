from trainos.kernel.metacivilization.interaction.interaction_registry import InteractionRegistry
from trainos.kernel.metacivilization.interaction.cross_system_event import CrossSystemEvent


def test_interaction_registry_emit():

    registry = InteractionRegistry()

    event = CrossSystemEvent(
        source_system="planning",
        target_system="risk",
        payload="update",
    )

    registry.emit(event)

    assert registry.events() == (event,)