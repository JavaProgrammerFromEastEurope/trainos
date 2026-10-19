from dataclasses import dataclass

from .fault_type import FaultType


@dataclass
class DamageEvent:

    system: str
    fault: 	FaultType
