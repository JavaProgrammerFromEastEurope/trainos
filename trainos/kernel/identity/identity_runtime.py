from .identity_engine import IdentityEngine


class IdentityRuntime:

    def __init__(self) -> None:
        self._engine = IdentityEngine()

    def initialize(self) -> None:
        pass

    def update(self, identity):
        return self._engine.establish(identity)

    def shutdown(self) -> None:
        pass
