from kernel.metacivilization.stability.stability_engine import StabilityEngine
from kernel.metacivilization.stability.drift_event import DriftEvent


def test_stability_engine_process():

    engine = StabilityEngine()

    event = DriftEvent(
        source="culture",
        deviation=10.0,
    )

    corrected = engine.process(event)

    assert corrected.deviation == 8.0