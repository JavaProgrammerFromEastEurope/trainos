from dataclasses import dataclass

from .priority_level import PriorityLevel


@dataclass
class Priority:
    level: PriorityLevel
