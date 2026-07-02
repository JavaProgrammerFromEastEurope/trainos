from dataclasses import dataclass

from .citizen_state import CitizenState


@dataclass(frozen=True)
class CitizenLifecycle:

    entity_id: str
    state: CitizenState
