from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TransportPolicy:

    require_available_unit: bool 		= True
    allow_parallel_shipments: bool 	= False