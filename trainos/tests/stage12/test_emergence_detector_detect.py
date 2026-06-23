from trainos.kernel.metacivilization.emergence.emergence_detector import EmergenceDetector


def test_emergence_detector_detect():

    detector 	= EmergenceDetector()
    event 		= detector.detect(
        "pattern detected",
    )

    assert event is not None
    assert event.pattern == "unknown_behavior"