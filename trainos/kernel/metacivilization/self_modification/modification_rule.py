from dataclasses import dataclass


@dataclass
class ModificationRule:

    trigger_pattern: 	str
    allowed_change: 	str