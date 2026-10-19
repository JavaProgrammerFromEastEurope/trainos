from dataclasses import dataclass

from .origin_type import OriginType


@dataclass(frozen=True)
class PrincipleOrigin:

    description: str
    type: OriginType