from dataclasses import dataclass

from .severity_level import SeverityLevel


@dataclass
class DeficitEvent:

    resource: str
    severity: SeverityLevel
