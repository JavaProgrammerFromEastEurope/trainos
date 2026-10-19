from __future__ import annotations

from .constitutional_integration import ConstitutionalIntegration


class IntegrationRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalIntegration] = []

    def register(self, integration: ConstitutionalIntegration) -> None:
        self._entries.append(integration)

    def entries(
        self,
    ) -> tuple[ConstitutionalIntegration, ...]:
        return tuple(self._entries)
