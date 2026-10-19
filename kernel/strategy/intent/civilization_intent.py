from dataclasses import dataclass

from .intent_priority import IntentPriority


@dataclass(frozen=True)
class CivilizationIntent:

    name: 				str
    description: 	str
    priority: IntentPriority