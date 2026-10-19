from dataclasses import dataclass

from .citizen_state import CitizenState


@dataclass(frozen=True)
class LifecycleTransition:

    from_state: CitizenState
    to_state: 	CitizenState