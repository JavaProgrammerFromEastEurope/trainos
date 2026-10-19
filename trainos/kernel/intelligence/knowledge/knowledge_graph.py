class KnowledgeGraph:

    def __init__(self) -> None:
        self._connections: list[tuple[str, str]] = []

    def connect(self, source: str, target: str) -> None:
        self._connections.append((source, target))

    def connections(self) -> tuple[tuple[str, str], ...]:
        return tuple(self._connections)
