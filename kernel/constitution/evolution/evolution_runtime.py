from .evolution_engine import EvolutionEngine


class EvolutionRuntime:

    def __init__(self) -> None:
        self._engine = EvolutionEngine()

    def initialize(self) -> None:
        pass

    def update(self, evolution):
        return self._engine.evolve(evolution)

    def shutdown(self) -> None:
        pass
