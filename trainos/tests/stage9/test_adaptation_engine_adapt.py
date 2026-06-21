from trainos.kernel.communication.resource_ecology.evolution.adaptation_engine import AdaptationEngine
from trainos.kernel.communication.resource_ecology.evolution.adaptation_plan import AdaptationPlan

def test_adaptation_engine_adapt():

    engine 		= AdaptationEngine()
    plan 			= engine.adapt()
    expected 	= AdaptationPlan(
        description="increase hydroponics capacity",
    )

    assert plan == expected