from .hierarchy_engine import HierarchyEngine


class HierarchyRuntime:

    def __init__(self) -> None:
        self._engine = HierarchyEngine()

    def initialize(self) -> None:
        pass

    def update(self, hierarchy):
        return self._engine.classify(hierarchy)

    def shutdown(self) -> None:
        pass
