from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DeliveryJobPolicy:

    require_transport: 	bool = True
    require_route: 			bool = True
    require_shipment: 	bool = True