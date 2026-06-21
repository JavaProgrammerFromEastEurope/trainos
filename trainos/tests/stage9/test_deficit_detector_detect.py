from trainos.kernel.communication.resource_ecology.deficit.deficit_detector import DeficitDetector
from trainos.kernel.communication.resource_ecology.deficit.deficit_event import DeficitEvent
from trainos.kernel.communication.resource_ecology.deficit.severity_level import SeverityLevel


def test_deficit_detector_detect():

    detector 	= DeficitDetector()
    event 		= detector.detect()
    expected 	= DeficitEvent(
        resource="food",
        severity=SeverityLevel.CRITICAL,
    )

    assert event == expected