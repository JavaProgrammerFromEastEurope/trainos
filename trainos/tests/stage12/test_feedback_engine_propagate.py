from trainos.kernel.metacivilization.feedback.feedback_engine import FeedbackEngine
from trainos.kernel.metacivilization.feedback.feedback_event import FeedbackEvent


def test_feedback_engine_propagate():

    engine = FeedbackEngine()
    event = FeedbackEvent(
        origin="risk",
        signal="danger",
        intensity=1.0,
    )
    result = engine.propagate(event)

    assert result.intensity == 1.1