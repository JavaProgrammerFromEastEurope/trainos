from dataclasses import dataclass

from .identity_type import IdentityType


@dataclass
class Identity:

    type: IdentityType