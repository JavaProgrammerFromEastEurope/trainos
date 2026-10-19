from dataclasses import dataclass

from .consumption_job_status import ConsumptionJobStatus


@dataclass(frozen=True, slots=True)
class ConsumptionJob:

    job_id: 			str
    consumer_id: 	str
    request_id: 	str
    policy_id: 		str
    status: ConsumptionJobStatus