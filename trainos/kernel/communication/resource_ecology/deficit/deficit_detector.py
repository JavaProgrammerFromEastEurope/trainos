from .deficit_event import DeficitEvent
from .severity_level import SeverityLevel


class DeficitDetector:

    def detect(self) -> DeficitEvent | None:
        return DeficitEvent(resource="food", severity=SeverityLevel.CRITICAL)
