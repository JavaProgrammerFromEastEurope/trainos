from __future__ import annotations

from .constitutional_authority import ConstitutionalAuthority


class AuthorityRegistry:

    def __init__(self) -> None:
        self._authorities: dict[str, ConstitutionalAuthority] = {}

    def register(
        self,
        authority: ConstitutionalAuthority,
    ) -> None:
        self._authorities[authority.institution_id] = authority

    def get(
        self,
        institution_id: str,
    ) -> ConstitutionalAuthority | None:
        return self._authorities.get(institution_id)

    def authorities(
        self,
    ) -> tuple[ConstitutionalAuthority, ...]:
        return tuple(self._authorities.values())
