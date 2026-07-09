from kernel.consumption.jobs.consumption_job import ConsumptionJob
from kernel.consumption.jobs.consumption_job_engine import ConsumptionJobEngine
from kernel.consumption.jobs.consumption_job_status import ConsumptionJobStatus


def test_consumption_job_engine():

    engine = ConsumptionJobEngine()

    job = ConsumptionJob(
        job_id="JOB1",
        consumer_id="C1",
        request_id="REQ1",
        policy_id="POL1",
        status=ConsumptionJobStatus.CREATED,
    )

    result = engine.execute(job)

    assert result.job_id == "JOB1"
    assert result.status == ConsumptionJobStatus.COMPLETED
