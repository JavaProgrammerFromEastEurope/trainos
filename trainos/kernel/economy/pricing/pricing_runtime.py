from .pricing_engine import PricingEngine


class PricingRuntime:

    def __init__(self) -> None:
        self._engine = PricingEngine()

    def initialize(self) -> None:
        pass

    def update(self, price):
        return self._engine.evaluate(price)

    def shutdown(self) -> None:
        pass
