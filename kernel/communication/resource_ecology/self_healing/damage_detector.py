from .damage_event import DamageEvent
from .fault_type import FaultType


class DamageDetector:

    def detect(self) -> DamageEvent | None:
        return DamageEvent(
            system="hydroponics",
            fault=FaultType.MAJOR,
        )
