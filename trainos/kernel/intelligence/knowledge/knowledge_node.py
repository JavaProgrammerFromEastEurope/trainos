from dataclasses import dataclass

from .knowledge_type import KnowledgeType


@dataclass
class KnowledgeNode:

    type: KnowledgeType
    content: str