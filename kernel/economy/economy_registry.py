class EconomyRegistry:

    def __init__(self) -> None:
        self._services = {}

    def register(self, name: str, service) -> None:
        self._services[name] = service

    def get(self, name: str):
        return self._services.get(name)
