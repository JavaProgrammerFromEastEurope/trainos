from dataclasses 	import dataclass
from decimal 			import Decimal


@dataclass(frozen=True, slots=True)
class ProductionInputCheck:

    resource_id: str
    available_quantity: Decimal
    required_quantity: 	Decimal