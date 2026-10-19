from .preference_engine import PreferenceEngine


class PreferenceRuntime:

    def __init__(self) -> None:
        self._engine = PreferenceEngine()

    def initialize(self) -> None:
        pass

    def update(self, profile):
        return self._engine.align(profile)

    def shutdown(self) -> None:
        pass
