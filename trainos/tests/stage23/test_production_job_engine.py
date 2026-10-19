from kernel.production.jobs.production_job import ProductionJob
from kernel.production.jobs.production_job_engine import ProductionJobEngine
from kernel.production.jobs.production_job_status import ProductionJobStatus


def test_production_job_engine():

    engine = ProductionJobEngine()

    job = ProductionJob(
        job_id="JOB1",
        recipe_id="recipe1",
        factory_id="factory1",
        status=ProductionJobStatus.CREATED,
    )

    result = engine.execute(job)

    assert result.job_id == "JOB1"
    assert result.status == ProductionJobStatus.COMPLETED