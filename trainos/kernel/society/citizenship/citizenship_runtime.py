from .citizenship_engine import CitizenshipEngine


class CitizenshipRuntime:

    def __init__(self) -> None:
        self._engine = CitizenshipEngine()

    def initialize(self) -> None:
        pass

    def update(self, citizenship):
        return self._engine.evaluate(citizenship)

    def shutdown(self) -> None:
        pass
