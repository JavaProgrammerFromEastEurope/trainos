from dataclasses import dataclass


@dataclass
class CrossSystemEvent:

    source_system: 	str
    target_system: 	str
    payload: 				str