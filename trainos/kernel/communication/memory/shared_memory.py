class SharedMemory:

    def __init__(self) -> None:
        self._store: dict[str, str] = {}

    def write(self, key: str, value: str) -> None:
        self._store[key] = value

    def read(self, key: str) -> str | None:
        return self._store.get(key)