from .integration_engine import IntegrationEngine


class IntegrationRuntime:

    def __init__(self) -> None:
        self._engine = IntegrationEngine()

    def initialize(self) -> None:
        pass

    def update(self, integration):
        return self._engine.integrate(integration)

    def shutdown(self) -> None:
        pass
