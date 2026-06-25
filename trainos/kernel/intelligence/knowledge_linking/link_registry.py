from __future__ import annotations

from .knowledge_link import KnowledgeLink


class LinkRegistry:

    def __init__(self) -> None:
        self._links: list[KnowledgeLink] = []

    def register(self, link: KnowledgeLink) -> None:
        self._links.append(link)

    def links(self) -> tuple[KnowledgeLink, ...]:
        return tuple(self._links)
