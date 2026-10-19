from kernel.production.execute.production_context import ProductionContext
from kernel.production.execute.production_engine 	import ProductionEngine


def test_production_engine():

    engine = ProductionEngine()

    context = ProductionContext(
        factory_id="factory1",
        job_id="job1",
        recipe_id="recipe1",
    )

    engine.run(context)