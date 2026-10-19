from .jurisdiction_engine import JurisdictionEngine


class JurisdictionRuntime:

    def __init__(self) -> None:
        self._engine = JurisdictionEngine()

    def initialize(self) -> None:
        pass

    def update(self, jurisdiction):
        return self._engine.assign(jurisdiction)

    def shutdown(self) -> None:
        pass
