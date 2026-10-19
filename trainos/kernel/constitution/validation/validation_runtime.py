from .validation_engine import ValidationEngine


class ValidationRuntime:

    def __init__(self) -> None:
        self._engine = ValidationEngine()

    def initialize(self) -> None:
        pass

    def update(self, validation):
        return self._engine.validate(validation)

    def shutdown(self) -> None:
        pass
