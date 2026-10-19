from .domain_engine import DomainEngine


class DomainRuntime:

    def __init__(self) -> None:
        self._engine = DomainEngine()

    def initialize(self) -> None:
        pass

    def update(self, entry):
        return self._engine.assign(entry)

    def shutdown(self) -> None:
        pass
