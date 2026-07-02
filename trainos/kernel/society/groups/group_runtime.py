from .group_engine import GroupEngine


class GroupRuntime:

    def __init__(self) -> None:
        self._engine = GroupEngine()

    def initialize(self) -> None:
        pass

    def update(self, group):
        return self._engine.evaluate(group)

    def shutdown(self) -> None:
        pass
