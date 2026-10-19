from dataclasses import dataclass

from .wagon_status 	import WagonStatus
from .wagon_type 		import WagonType


@dataclass
class Wagon:

    name: str
    type: WagonType
    status: WagonStatus
