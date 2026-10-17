from kernel.strategy.learning.learning_event import LearningEvent
from kernel.strategy.learning.learning_registry import LearningRegistry
from kernel.strategy.learning.outcome import Outcome
from kernel.strategy.learning.outcome_type import OutcomeType


def test_learning_registry_register():

    registry = LearningRegistry()
    event = LearningEvent(
        context="hydroponics",
        outcome=Outcome(
            description="successful expansion",
            type=OutcomeType.SUCCESS,
        ),
    )
    registry.register(event)
    assert registry.events() == (event,)
