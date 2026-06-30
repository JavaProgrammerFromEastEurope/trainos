from .origin_engine import OriginEngine


class OriginRuntime:

    def __init__(self) -> None:
        self._engine = OriginEngine()

    def initialize(self) -> None:
        pass

    def update(self, origin):
        return self._engine.establish(origin)

    def shutdown(self) -> None:
        pass
