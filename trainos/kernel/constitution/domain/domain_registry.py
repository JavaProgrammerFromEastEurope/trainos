from __future__ import annotations

from .constitutional_domain import ConstitutionalDomain


class DomainRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalDomain] = []

    def register(self, entry: ConstitutionalDomain) -> None:
        self._entries.append(entry)

    def entries(self) -> tuple[ConstitutionalDomain, ...]:
        return tuple(self._entries)
