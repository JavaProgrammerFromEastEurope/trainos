from __future__ import annotations

from .system_link import SystemLink


class InteractionMatrix:

    def __init__(self) -> None:
        self._links: list[SystemLink] = []

    def add_link(self, link: SystemLink) -> None:
        self._links.append(link)

    def links(self) -> tuple[SystemLink, ...]:
        return tuple(self._links)
