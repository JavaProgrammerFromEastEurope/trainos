from trainos.kernel.strategy.adaptation.adaptation_registry import AdaptationRegistry
from trainos.kernel.strategy.adaptation.adaptive_strategy import AdaptiveStrategy
from trainos.kernel.strategy.adaptation.strategy_state import StrategyState


def test_adaptation_registry_register():

    registry = AdaptationRegistry()
    strategy = AdaptiveStrategy(
        name="Winter",
        description="Adapt to cold",
        state=StrategyState.ADAPTING,
    )
    registry.register(strategy)
    assert registry.strategies() == (strategy,)
