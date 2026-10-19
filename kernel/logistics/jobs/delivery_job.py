from dataclasses import dataclass

from .delivery_job_status import DeliveryJobStatus


@dataclass(frozen=True, slots=True)
class DeliveryJob:

    job_id: 			str
    shipment_id: 	str
    route_id: 		str
    transport_id: str
    status: DeliveryJobStatus