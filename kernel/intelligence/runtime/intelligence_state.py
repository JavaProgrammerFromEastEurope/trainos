from dataclasses import dataclass


@dataclass(frozen=True)
class IntelligenceState:

    cycle: 		int
    active: 	bool