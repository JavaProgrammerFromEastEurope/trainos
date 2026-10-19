from dataclasses import dataclass

from .identity_trait import IdentityTrait


@dataclass(frozen=True)
class CivilizationIdentity:

    name: 				str
    description: 	str
    traits: tuple[IdentityTrait, ...]