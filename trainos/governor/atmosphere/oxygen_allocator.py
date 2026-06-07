from enum import IntEnum
from dataclasses import dataclass

class OxygenPriority(IntEnum):
    MEDICAL = 100
    COMMAND = 90
    HABITAT = 80
    INDUSTRIAL = 60
    STORAGE = 20


@dataclass(slots=True)
class OxygenAllocation:
    sector_id: 	int
    flow: 			float

