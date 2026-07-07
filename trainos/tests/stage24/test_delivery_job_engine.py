from kernel.logistics.jobs.delivery_job import DeliveryJob
from kernel.logistics.jobs.delivery_job_engine import DeliveryJobEngine
from kernel.logistics.jobs.delivery_job_status import DeliveryJobStatus


def test_delivery_job_engine():

    engine = DeliveryJobEngine()

    job = DeliveryJob(
        job_id="JOB1",
        shipment_id="SHIP1",
        route_id="ROUTE1",
        transport_id="TR1",
        status=DeliveryJobStatus.CREATED,
    )

    result = engine.execute(job)

    assert result.job_id == "JOB1"
    assert result.status == DeliveryJobStatus.COMPLETED