from dataclasses import dataclass

from .awareness_level import AwarenessLevel


@dataclass
class SelfAwareness:

    level: AwarenessLevel
