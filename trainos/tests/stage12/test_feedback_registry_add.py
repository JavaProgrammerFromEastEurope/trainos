from trainos.kernel.metacivilization.feedback.feedback_registry import FeedbackRegistry
from trainos.kernel.metacivilization.feedback.feedback_loop import FeedbackLoop


def test_feedback_registry_add():

    registry = FeedbackRegistry()

    loop = FeedbackLoop(
        source="risk",
        target="planning",
        strength=0.8,
    )

    registry.add(loop)

    assert registry.loops() == (loop,)