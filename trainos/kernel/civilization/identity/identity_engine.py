from .identity import Identity
from .identity_type import IdentityType


class IdentityEngine:

    def define(self) -> Identity:
        return Identity(type=IdentityType.SURVIVOR)
