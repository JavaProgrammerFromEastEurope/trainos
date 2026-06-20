from .knowledge_snapshot import KnowledgeSnapshot


class KnowledgeEngine:

    def snapshot(self, version: int) -> KnowledgeSnapshot:
        return KnowledgeSnapshot(version=version)
