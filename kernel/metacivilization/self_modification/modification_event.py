from dataclasses import dataclass


@dataclass
class ModificationEvent:

    source: 						str
    target_system: 			str
    change_description: str