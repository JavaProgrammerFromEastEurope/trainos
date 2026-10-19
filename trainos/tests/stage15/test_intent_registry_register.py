from kernel.strategy.intent.civilization_intent import CivilizationIntent
from kernel.strategy.intent.intent_priority import IntentPriority
from kernel.strategy.intent.intent_registry import IntentRegistry


def test_intent_registry_register():

    registry = IntentRegistry()
    intent = CivilizationIntent(
        name="Preserve Civilization",
        description="Maintain long-term survival",
        priority=IntentPriority.CRITICAL,
    )
    registry.register(intent)
    assert registry.intents() == (intent,)
