class SocialGraph:

    def __init__(self) -> None:
        self._links: dict[str, list[str]] = {}

    def connect(self, a: str, b: str) -> None:
        self._links.setdefault(a, []).append(b)

    def links(self, agent: str) -> list[str]:
        return self._links.get(agent, [])
