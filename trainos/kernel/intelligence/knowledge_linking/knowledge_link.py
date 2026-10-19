from dataclasses import dataclass

from .link_type import LinkType


@dataclass
class KnowledgeLink:

    source: str
    target: str
    type: LinkType