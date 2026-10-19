class SharedMemory:

    def __init__(self) -> None:
        self._memory: dict[str, str] = {}

    def write(self, key: str, value: str) -> None:
        self._memory[key] = value

    def read(self, key: str) -> str | None:
        return self._memory.get(key)
