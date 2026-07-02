from dataclasses import dataclass

from .institution_state import InstitutionState


@dataclass(frozen=True)
class InstitutionLifecycle:

    institution_id: str
    state: InstitutionState