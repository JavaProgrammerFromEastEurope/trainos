from __future__ import annotations

from .principle_origin import PrincipleOrigin


class OriginRegistry:

    def __init__(self) -> None:
        self._origins: list[PrincipleOrigin] = []

    def register(self, origin: PrincipleOrigin) -> None:
        self._origins.append(origin)

    def origins(self) -> tuple[PrincipleOrigin, ...]:
        return tuple(self._origins)
