from .knowledge_link import KnowledgeLink
from .link_type import LinkType


class LinkingEngine:

    def connect(self, source: str, target: str) -> KnowledgeLink:
        return KnowledgeLink(
            source=source,
            target=target,
            type=LinkType.RELATED_TO,
        )
