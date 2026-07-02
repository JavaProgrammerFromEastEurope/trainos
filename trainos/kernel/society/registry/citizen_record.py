from dataclasses import dataclass

from kernel.society.identity.identity_role import IdentityRole


@dataclass(frozen=True)
class CitizenRecord:

    entity_id: str
    role: IdentityRole
    active: bool