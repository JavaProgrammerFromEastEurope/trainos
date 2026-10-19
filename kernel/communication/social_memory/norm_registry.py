from __future__ import annotations

from .social_norm import (
    SocialNorm,
)


class NormRegistry:

    def __init__(self) -> None:
        self._norms: list[SocialNorm] = []

    def add(self, norm: SocialNorm) -> None:
        self._norms.append(norm)

    def norms(self) -> tuple[SocialNorm, ...]:
        return tuple(self._norms)
