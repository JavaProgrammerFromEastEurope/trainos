from enum import Enum
from dataclasses import dataclass


class LeakSeverity(Enum):

    LOW 			= "LOW"
    MEDIUM 		= "MEDIUM"
    HIGH 			= "HIGH"
    CRITICAL 	= "CRITICAL"


@dataclass(slots=True)
class LeakReport:

    sector_id: int
    leak_rate: float
    severity: LeakSeverity


class LeakDetector:

    def __init__(self, world):
        self.world = world

    def detect(self) -> list[LeakReport]:
        reports = []
        for sector_id, sector in self.world.sectors.items():
            loss = sector.air_outflow - sector.air_inflow
            if loss <= 0:
                continue
            if loss > 20:
                severity = LeakSeverity.CRITICAL
            elif loss > 10:
                severity = LeakSeverity.HIGH
            elif loss > 5:
                severity = LeakSeverity.MEDIUM
            else:
                severity = LeakSeverity.LOW
            reports.append(
                LeakReport(
                    sector_id=sector_id,
                    leak_rate=loss,
                    severity=severity,
                )
            )
        return reports
