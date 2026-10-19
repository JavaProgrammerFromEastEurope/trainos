from .registry_engine import RegistryEngine


class RegistryRuntime:

    def __init__(self) -> None:
        self._engine = RegistryEngine()

    def initialize(self) -> None:
        pass

    def update(self, record):
        return self._engine.process(record)

    def shutdown(self) -> None:
        pass
