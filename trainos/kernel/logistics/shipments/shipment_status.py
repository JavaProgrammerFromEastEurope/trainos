from enum import Enum


class ShipmentStatus(Enum):

    CREATED 		= "created"
    IN_TRANSIT 	= "in_transit"
    DELIVERED 	= "delivered"
    FAILED 			= "failed"
    CANCELLED 	= "cancelled"