from dataclasses import dataclass

from .identity_role import IdentityRole


@dataclass(frozen=True)
class CivilIdentity:

    entity_id: str
    role: IdentityRole