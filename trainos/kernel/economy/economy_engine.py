from .economy_context import EconomyContext
from .economy_state 	import EconomyState


class EconomyEngine:

    def initialize(
        self,
        context: EconomyContext,
    ) -> None:
        context.state = EconomyState.INITIALIZED

    def start(
        self,
        context: EconomyContext,
    ) -> None:
        context.state = EconomyState.RUNNING

    def stop(
        self,
        context: EconomyContext,
    ) -> None:
        context.state = EconomyState.STOPPED
